import flask

from app import app

@app.server.route("/static/ds1.csv")
def serve_ds1():
    return flask.send_file("./raw_data/ds1.csv", mimetype="text")

@app.server.route("/static/ds2.csv")
def serve_ds2():
    return flask.send_file("./raw_data/ds2.csv", mimetype="text")

@app.server.route("/static/ds3.csv")
def serve_ds3():
    return flask.send_file("./raw_data/ds3.csv", mimetype="text")

