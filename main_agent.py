from typing import Dict, Any
import uuid
from project.agents.planner import Planner
from project.agents.worker import Worker
from project.agents.evaluator import Evaluator
from project.memory.session_memory import SessionMemory
from project.core.observability import Observability

class MainAgent:
    def __init__(self):
        self.planner = Planner()
        self.worker = Worker()
        self.evaluator = Evaluator()
        self.memory = SessionMemory()

    def handle_message(self, user_input: str) -> Dict[str, Any]:
        # Minimal orchestration: create fake dataset, plan, run workers, evaluate
        session_id = str(uuid.uuid4())
        Observability.log_event(session_id, 'main_agent', 'start', f'Received input: {user_input}')
        # For demo, create a tiny CSV
        import pandas as pd
        df = pd.DataFrame({"id": [1,2,2,3], "amount": [10.0, None, 2000.0, 15.0]})
        dataset_path = f"/content/project/dataset_{session_id}.csv"
        df.to_csv(dataset_path, index=False)
        dataset_meta = {"row_count": len(df), "columns": [{"name": "id", "dtype": "int"}, {"name": "amount", "dtype": "float"}]}
        plan = self.planner.make_plan(dataset_meta)
        Observability.log_event(session_id, 'planner', 'plan_created', 'Plan created', {"plan_id": plan.get('plan_id')})
        # Run workers sequentially for simplicity
        worker_results = []
        for check in plan.get('checks', []):
            Observability.log_event(session_id, 'worker', 'worker_started', 'Running check', {"check": check.get('check')})
            res = self.worker.run_check(check, dataset_path)
            worker_results.append(res)
        Observability.log_event(session_id, 'evaluator', 'eval_start', 'Evaluator starting')
        report = self.evaluator.evaluate(session_id, worker_results)
        # Save session
        self.memory.save_session(session_id, {"input": user_input, "plan": plan, "worker_results": worker_results, "report": report})
        Observability.log_event(session_id, 'main_agent', 'complete', 'Audit complete', {"global_score": report.get('global_score')})
        return {"response": f"Audit complete. Global score: {report.get('global_score')}", "report": report}

def run_agent(user_input: str):
    agent = MainAgent()
    result = agent.handle_message(user_input)
    return result

if __name__ == '__main__':
    print(run_agent('demo input'))
