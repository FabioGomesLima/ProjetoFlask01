from app import app
from flask import render_template
from flask import request

@app.route('/')
@app.route('/index', defaults={"nome":"usuario"})
@app.route('/index/<nome>/<profissao>/<canal>') 
def index(nome, profissao, canal):
    
    dados = {"profissao": profissao,"canal":canal}
    return render_template('index.html' , nome=nome, dados=dados)

@app.route('/contato')
def contato():
   return render_template('contato.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['GET'])
def autenticar():
    usuario = request.args.get ('usuario')
    senha = request.args.get('senha')
    return "usuario: {} e senha: {}".format(usuario, senha)
    
    