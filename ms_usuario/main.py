from flask import Flask
import os

app = Flask(__name__)

@app.route('/ciclista/dados', methods=['GET'])
def hello_world():
    return "Ciclista: Fulano\nIdade: Ciclano"

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)),host='0.0.0.0',debug=True)
