from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():  # put application's code here
    if request.method == "POST":
        if request.form.get("username") == "Dexter" and request.form.get("password") == "D3xt3r_R0x":
            return redirect(url_for("secret"))

    return render_template("login.html")


@app.route('/s3cr3t_p4g3')
def secret():  # put application's code here
    return render_template("secret.html", hash="ZmxhZ3tHb09Pb2Rfd2VsbF90QWxrX3NPb05fMTk0NjQ5MDJ9")


if __name__ == '__main__':
    app.run(debug=True)
