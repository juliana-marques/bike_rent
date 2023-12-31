from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World - Gerenciamento Estação Microsservice:)"

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 4000)),host='0.0.0.0',debug=True)
