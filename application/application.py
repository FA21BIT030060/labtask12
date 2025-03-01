from flask import Flask

app = Flask(__name__)  # Corrected version

@app.route("/")
def home():
    return "hello,My name is AbdulRafay and my nme isSharoon  Khan"

if __name__ == "__main__":
    app.run()
