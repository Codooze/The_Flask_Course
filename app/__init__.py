# brights our application together
from flask import Flask
app = Flask(__name__)
from app import adm_views  # ctrl + shift + p / save withoud formating
from app import views  # - dicen que se debe hacer así con flask, para evitar no sé  que circular import
