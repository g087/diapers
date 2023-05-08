import logging
from flask import Flask, request, jsonify

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

nb_diapers = 0

app = Flask(__name__)


@app.route('/count', methods=['GET'])
def count():
  return jsonify({"count": nb_diapers})


@app.route('/diaper', methods=['POST'])
def diaper():
  global nb_diapers
  nb_diapers -= 1
  logging.debug(f"One diaper used, available diapers {nb_diapers}")
  return jsonify({"count": nb_diapers})


@app.route('/pack', methods=['POST'])
def pack():
  global nb_diapers
  pack_size = int(request.get_json()["pack_size"])
  nb_diapers += pack_size
  logging.debug(
    f"One pack of {pack_size} diapers bought, available diapers {nb_diapers}")
  return jsonify({"count": nb_diapers})


@app.route('/update', methods=['POST'])
def update():
  global nb_diapers
  nb_diapers = int(request.get_json()["new_count"])
  logging.debug(f"Inventory size updated, available diapers {nb_diapers}")
  return jsonify({"count": nb_diapers})


def main():
  app.run(host="0.0.0.0", port=9090)


if __name__ == '__main__':
  main()
