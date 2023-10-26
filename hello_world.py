from flask import Blueprint, request, Response, abort

hello_world = Blueprint('hello_world', __name__)

@hello_world.route('/', methods=['GET'])
def hello_world():
    try:
        return "Hello World! :)"
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return "Internal Server Error", 500