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
    house_list = database.load_list()
    print(house_list)
    length = len(house_list)
    return render_template("list.html", house_list = house_list, length = length)


@application.route("/house_info/<int:index>/")
def house_info(index):
    house_info = database.load_house(index)
    location = house_info["location"]
    cleaness = house_info["cleaness"]
    built_in = house_info["built_in"]
    print(location, cleaness, built_in)
    return render_template("house_info.html", location = location, cleaness = cleaness, built_in = built_in)
if __name__ == "__main__":
    application.run(host='0.0.0.0')