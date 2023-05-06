import os
import openai
import argparse
import logging
import re
from flask import Flask, request, jsonify

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

openai.api_key = os.getenv("OPENAI_API_KEY")

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Diapers REST API")
parser.add_argument(
  "--inventory-size",
  type=int,
  default=0,
  help="Initial inventory size",
)
args = parser.parse_args()
inventory_size = args.inventory_size  # Set initial inventory size

app = Flask(__name__)


@app.route('/count', methods=['GET'])
def count():
  return jsonify({"count": inventory_size})


@app.route('/event', methods=['POST'])
def event():
  data = request.get_json()
  prompt = data["prompt"]

  global inventory_size  # Use the global variable
  challenge = f"I started with {inventory_size} diapers. Then {prompt}. How much do I have now?"

  logging.debug(f"Challenge sent to OpenAI GPT API: {challenge}")

  # Call OpenAI GPT-3 API to generate a completion
  completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=challenge,
    max_tokens=512,
    n=1,
    stop=None,
    temperature=0,
  )
  logging.debug(f"Completions received from OpenAI GPT API: {completions}")

  answer = completions.choices[0].text.strip()

  # assuming answer variable contains the word "diapers" preceded by a integer
  match = re.search(r'(\d+)\s*diapers', answer)
  if match:
    inventory_size = int(match.group(1))
    logging.debug(f"New inventory size: {inventory_size}")

  # Return a JSON response with the new inventory size and the answer
  result = {"count": inventory_size, "answer": answer}
  return jsonify(result)


def main():
  app.run(host="0.0.0.0", port=9090)


if __name__ == '__main__':
  main()
