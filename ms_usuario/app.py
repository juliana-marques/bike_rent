from flask import Flask

app = Flask(__name__)

@app.route('/teste/usuario', methods=['GET'])
def ola_mundo():
    return "Olá mundo"

if __name__ == '__main__':
    app.run(debug=True)
