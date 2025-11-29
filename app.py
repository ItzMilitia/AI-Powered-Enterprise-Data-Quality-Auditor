from project.main_agent import run_agent
from typing import Dict, Any
import json

def serve_text_input(text: str) -> Dict[str, Any]:
    result = run_agent(text)
    return result

if __name__ == '__main__':
    print(serve_text_input('Hello from app'))
