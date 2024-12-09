from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def callback():
    print(request.args)
    return 'Callback Page'


if __name__ == '__main__':
    app.run(port=3000)