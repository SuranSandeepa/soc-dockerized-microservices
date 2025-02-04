from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python Microservice!"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=6000)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7000)
