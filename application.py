from flask import Flask, render_template,request, redirect, url_for
import sys, database

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
    print(location, cleaness, built)

    if cleaness == None:
        cleaness = False
    else:
        cleaness == True

    database.save(location,cleaness,built)

    return render_template("apply_photo.html")

@application.route("/upload_done" , methods=["POST"])
def upload_done():
    uploaded_files = request.files["file"]
    uploaded_files.save("static/img/{}.jpeg".format(database.now_index()))
    return redirect(url_for("hello")) #hello 라는 함수에 보낼거다 


@application.route("/list")
def list():
    return render_template("list.html")


if __name__ == "__main__":
    application.run(host='0.0.0.0')