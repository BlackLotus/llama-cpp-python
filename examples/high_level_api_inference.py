import json
import argparse

from llama_cpp import Llama

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model", type=str, default="./models/...")
args = parser.parse_args()

llm = Llama(model_path=args.model)

output = llm(
    "Question: What are the names of the planets in the solar system? Answer: ",
    max_tokens=1,
    stop=["Q:", "\n"],
    echo=True,
)

print(json.dumps(output, indent=2))
