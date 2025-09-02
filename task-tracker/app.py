from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


def main() -> None:
    app.run(host='0.0.0.0', port = 5555, debug=True)

if __name__ == '__main__':
    main()