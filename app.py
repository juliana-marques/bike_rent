from flask import Flask
import os

app = Flask(__name__)

from .ms_usuario.app_usuario import app_usuario
app.register_blueprint(app_usuario)

from hello_world import hello_world
app.register_blueprint(hello_world)


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)

# version 1.0
