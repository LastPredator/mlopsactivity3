import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--threshold', type=float, required=True)
args = parser.parse_args()

with open(args.threshold, "r") as f:
    eval_threshold = float(f.read().strip())

with open("metrics/accuracy.json", "r") as f:
    metrics = json.load(f)
accuracy = metrics["accuracy"]

if accuracy < eval_threshold:
    raise ValueError(f"Model accuracy {accuracy:.2f} is below the threshold of {eval_threshold:.2f}.")
else:
    print(f"Model passed the quality gate with accuracy {accuracy:.2f}.")