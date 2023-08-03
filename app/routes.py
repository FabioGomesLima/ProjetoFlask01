from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    name = "Gomes"
    dados = {"profissao": "beck-end","canal":"euartux"}
    return render_template('index.html' , name=name, dados=dados)

@app.route('/contato')
def contato():
   return render_template('contato.html')