from flask import Flask
from bike_rent.ms_usuario.app import app_usuario
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    try:
        return "Hello World! :)"
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return "Internal Server Error", 500

app.register_blueprint(app_usuario)

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)

# version 1.0
