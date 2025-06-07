"""Minimal example to run a Langflow flow from a JSON file."""
import sys
from langflow import load_flow_from_json

def main(path: str) -> None:
    flow = load_flow_from_json(path)
    result = flow({"text": "Bonjour"})
    print(result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python langflow_demo.py <flow.json>")
    else:
        main(sys.argv[1])
