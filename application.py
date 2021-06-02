from flask import Flask, render_template,request
import sys

application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("hello.html")

@application.route("/apply")
def apply():
    return render_template("apply.html")

@application.route("/applyphoto")
def photo_apply():
    location = request.args.get("location")
    cleaness = request.args.get("clean")
    built = request.args.get("built")
    # return render_template("apply.html")
    print(location, cleaness, built)

@application.route("/list")
def list():
    return render_template("list.html")


if __name__ == "__main__":
    application.run(host='0.0.0.0')