from flask import Flask, render_template, request
from controllers import controller_user, controller_contactos
from flask_login import LoginManager

app = Flask(__name__, template_folder="views")
login_manager= LoginManager()
login_manager.init_app(app)


app.secret_key = "75fc78df8vhj92gv92yvhz"




