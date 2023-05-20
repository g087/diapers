import argparse
import logging
from flask import Flask, request, jsonify

parser = argparse.ArgumentParser()
parser.add_argument('--diapers', type=int, help='initial diapers stock size')
args = parser.parse_args()
nb_diapers = args.diapers or 0

logging.basicConfig(filename='log.txt', level=logging.DEBUG)
logging.info(f"Initial inventory size : {nb_diapers}")

app = Flask(__name__)


@app.route('/count', methods=['GET'])
def count():
  return jsonify({"count": nb_diapers})


@app.route('/diaper', methods=['POST'])
def diaper():
  global nb_diapers
  nb_diapers -= 1
  logging.info(f"One diaper used, available diapers {nb_diapers}")
  return jsonify({"count": nb_diapers})


@app.route('/pack', methods=['POST'])
def pack():
  global nb_diapers
  pack_size = int(request.get_json()["pack_size"])
  nb_diapers += pack_size
  logging.info(
    f"A pack of {pack_size} diapers bought, available diapers {nb_diapers}")
  return jsonify({"count": nb_diapers})


@app.route('/update', methods=['POST'])
def update():
  global nb_diapers
  nb_diapers = int(request.get_json()["new_count"])
  logging.info(f"Inventory size updated, available diapers {nb_diapers}")
  return jsonify({"count": nb_diapers})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9090, debug=True)
