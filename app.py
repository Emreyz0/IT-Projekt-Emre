from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []
devices = []

@app.route("/")
def startseite():
    return render_template("index.html", users=users, devices=devices)

@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form.get("name")
    if name and name not in users:
        users.append(name)
    return redirect(url_for("startseite"))

@app.route("/delete_user", methods=["POST"])
def delete_user():
    name = request.form.get("name")
    if name in users:
        users.remove(name)
    return redirect(url_for("startseite"))

@app.route("/add_device", methods=["POST"])
def add_device():
    device = request.form.get("device")
    if device and device not in devices:
        devices.append(device)
    return redirect(url_for("startseite"))

@app.route("/delete_device", methods=["POST"])
def delete_device():
    device = request.form.get("device")
    if device in devices:
        devices.remove(device)
    return redirect(url_for("startseite"))

if __name__ == "__main__":
    app.run(debug=True)
