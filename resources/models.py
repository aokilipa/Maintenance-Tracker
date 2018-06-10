import flask
import datetime
from run import create_app
from config import dbconfig, filename , section
from flask_bcrypt import Bcrypt

app = create_app('production')
bcrypt = Bcrypt(app)

class User(object):

    def __init__(self, username, password ,created_on, firstname, lastname):
        pass
