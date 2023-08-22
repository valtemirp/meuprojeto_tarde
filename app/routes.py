from app import app , db, bcrypt
from flask import render_template, url_for, request, flash, session, redirect
from app.forms import Contato, Cadastro
from app.models import ContatoModel, CadastroModel
from flask_bcrypt import check_password_hash

import time


@app.route('/')
def index():
    return render_template('index.html',titulo = 'Página inicial')

@app.route('/contatos', methods=['POST', 'GET'])
def contatos():
    
    formulario = Contato()
    print('Acessou a rota contatos!')
    if formulario.validate_on_submit():
        flash('Seu cadastro foi enviado com sucesso!')
        nome = formulario.nome.data
        email = formulario.email.data
        mensagem = formulario.mensagem.data
        
        novo_contato = ContatoModel(nome=nome,email=email,mensagem=mensagem)
        db.session.add(novo_contato)
        db.session.commit()
    return render_template('contatos.html', titulo = 'Contatos',formulario = formulario)
@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo = 'Sobre')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html', titulo = 'Projetos' )

@app.route('/blog')
def blog():
    return render_template('blog.html', tituto = 'Blog')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    print('Acessou a rota de cadastro')
    cadastro = Cadastro()
    if cadastro.validate_on_submit():
        try:
            nome = cadastro.nome.data
            sobrenome = cadastro.sobrenome.data
            email = cadastro.email.data
            senha = cadastro.senha.data
            hash_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
            novo_cadastro = CadastroModel(nome=nome, sobrenome=sobrenome, email=email, senha=hash_senha)
            db.session.add(novo_cadastro)
            db.session.commit()
            flash('Seu cadastro foi realizado com sucesso!')
        except Exception as e:
            flash('Ocorreu um erro ao cadastrar! Entre em contato com o suporte: adm@admin.com')
            print(str(e))
    return render_template('cadastro.html', titulo='Cadastro', cadastro=cadastro)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        user = CadastroModel.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.senha, senha):
            session['email'] = user.email  
            session['nome'] = user.nome
            session['sobrenome'] = user.sobrenome
            session['senha'] = user.senha
            flash('Seja bem vindo')
            return redirect(url_for('login')) 
        else:
            flash('Senha ou e-mail incorreto!')
    return render_template('login.html', titulo='Login')
@app.route('/sair')
def sair():
    session.pop('email', None)
    session.pop('nome', None)
    session.pop('sobrenome', None)
    session.pop('senha', None)
    return redirect(url_for('login'))

@app.route('/editar', methods=['POST', 'GET'])
def editar():
    if 'email' not in session:
        return redirect(url_for('login'))
    usuario = CadastroModel.query.filter_by(email = session['email']).first()
    if request.method == 'POST':
        usuario.nome = request.form.get('nome')
        usuario.sobrenome = request.form.get('sobrenome')
        usuario.email = request.form.get('email')
        senha = request.form.get('senha')
        usuario.senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        db.session.commit()
        session['email'] = usuario.email  
        session['nome'] = usuario.nome
        session['sobrenome'] = usuario.sobrenome
        session['senha'] = usuario.senha

        flash('Seus dados foram atualizados com sucesso!')
        return redirect(url_for('editar'))
    return render_template('editar.html', titulo= 'Editar', usuario = usuario)

@app.route('/excluir_conta', methods=['GET'])
def excluir_conta():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    usuario = CadastroModel.query.filter_by(email = session['email']).first()
    db.session.delete(usuario)
    db.session.commit()
    session.clear()

    flash('Sua conta foi excluida com sucesso!')
    return redirect(url_for('cadastro'))

