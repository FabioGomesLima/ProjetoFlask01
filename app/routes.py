from app import app
from flask import render_template

@app.route('/')
@app.route('/index', defaults={"nome":"usuario"})
@app.route('/index/<nome>/<profissao>/<canal>') 
def index(nome, profissao, canal):
    
    dados = {"profissao": profissao,"canal":canal}
    return render_template('index.html' , nome=nome, dados=dados)

@app.route('/contato')
def contato():
   return render_template('contato.html')