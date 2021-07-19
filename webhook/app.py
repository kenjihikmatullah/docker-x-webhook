import os
from flask import Flask, jsonify
from subprocess import call

app = Flask(__name__, template_folder='.')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/webhook', methods=['GET', 'POST'])
def index():
  call("./scripts/update-backend.sh", shell=True)
  call('./scripts/update-frontend.sh', shell=True)

  return jsonify({
    'message': 'Successfully handle push action'
  })


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

