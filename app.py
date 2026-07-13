from flask import Flask, render_template, request, redirect, url_for, flash, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import date
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'qwretysfdsnfqywueqweqwegrgdivm342mfi29fm3782c8gn39gowg'
@app.route('/',methods =['POST', 'GET'])
def index():
    return 'zero'
@app.route('/login',methods =['POST', 'GET'])
def login():
    return redirect(url_for('boba.html'))
if __name__ == '__main__':
    app.run(debug=True)