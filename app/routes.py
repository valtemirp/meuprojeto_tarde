from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html',titulo = 'Página inicial')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html', titulo = 'Contatos')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo = 'Sobre')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html', titulo = 'Projetos' )

