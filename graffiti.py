import sqlite3
import string
import flask from flask import Flask, request, session, g, redirect, url_for,\
                  abort, render_template, flash
from contextlib import closing

#configuration
DATABASE = 'data_graffiti.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
