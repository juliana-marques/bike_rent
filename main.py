from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    try:
        return "Hello World :)"
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
