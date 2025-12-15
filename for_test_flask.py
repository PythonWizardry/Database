from flask import Flask, request

app = Flask(__name__)

@app.route("/ingest", methods=["POST"])
def ingest():
    print(request.json)
    return "OK", 200

app.run()
