from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
 
if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)
