from flask import *
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)

db.create_all()
 
class RegisterForm(FlaskForm):
    name = StringField("Enter your name:", validators=[DataRequired()])
    mail = EmailField("Enter your email:", validators=[DataRequired(),  Email(granular_message=True)])
    password = PasswordField("Enter your password:", validators=[DataRequired()])
    submit = SubmitField("Register")


@app.route("/", methods=["GET", "POST"])
def home():
    rform = RegisterForm()
    if rform.validate_on_submit():
        new_user = User(name=rform.name.data, email=rform.mail.data, password=rform.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
        except:
            flash("User already exists!")
            return render_template("home.html", rform=rform)

        return render_template("index.html")
    return render_template("home.html", rform=rform)

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
