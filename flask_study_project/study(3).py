from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/goods_list")
def goods_list():
    return render_template("goods_list.html")

@app.route("/user_list")
def user_list():
    return render_template("user_list.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register_url", methods=["GET"])
def register_url():
    print(request.args)
    return render_template("register_url.html")

if __name__ == '__main__':
    app.run()