import os
from flask import Flask, jsonify

app = Flask(__name__, template_folder='.')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/webhook', methods=['GET', 'POST'])
def index():
  # TODO
  return jsonify({
    'message': 'Successfully handle push action'
  })


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

