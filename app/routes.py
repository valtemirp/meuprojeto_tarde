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
    
    if request.method == 'POST' and cadastro.validate():
        
        try:
            nome = cadastro.nome.data
            sobrenome = cadastro.sobrenome.data
            email = cadastro.email.data
            cpf = cadastro.cpf.data
            telefone = cadastro.telefone.data
            endereco_rua = cadastro.endereco_rua.data
            endereco_bairro = cadastro.endereco_bairro.data
            endereco_cidade = cadastro.endereco_cidade.data
            endereco_uf = cadastro.endereco_uf.data
            senha = cadastro.senha.data
            hash_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
            
            novo_cadastro = CadastroModel(
                nome=nome,
                sobrenome=sobrenome,
                email=email,
                cpf=cpf,  
                telefone=telefone,  
                endereco_rua=endereco_rua,
                endereco_bairro=endereco_bairro,
                endereco_cidade=endereco_cidade,
                endereco_uf=endereco_uf,
                senha=hash_senha
            )
            print(novo_cadastro)
            
            db.session.add(novo_cadastro)
            db.session.commit()
            flash('Seu cadastro foi realizado com sucesso!')
        except Exception as e:
            flash('Ocorreu um erro ao cadastrar! Entre em contato com o suporte: adm@admin.com')
            print(str(e))
    print("Resultado de validate_on_submit:", cadastro.validate_on_submit())
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
            session['endereco_bairro'] = user.endereco_bairro
            session['endereco_uf'] = user.endereco_uf
            session['endereco_rua'] = user.endereco_rua
            session['cpf'] = user.cpf
            session['telefone'] = user.telefone
            session['endereco_cidade'] = user.endereco_cidade
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
    
    usuario = CadastroModel.query.filter_by(email=session['email']).first()
    
    if request.method == 'POST':
        senha_atual = request.form.get('senha_atual')
        if check_password_hash(usuario.senha, senha_atual):
            usuario.nome = request.form.get('nome')
            usuario.sobrenome = request.form.get('sobrenome')
            usuario.email = request.form.get('email')
            nova_senha = request.form.get('nova_senha')
            if nova_senha:
                usuario.senha = bcrypt.generate_password_hash(nova_senha).decode('utf-8')
            
            usuario.endereco_rua = request.form.get('endereco_rua')
            usuario.endereco_bairro = request.form.get('endereco_bairro')
            usuario.endereco_cidade = request.form.get('endereco_cidade')
            usuario.endereco_uf = request.form.get('endereco_uf')
        
            db.session.commit()
        
            session['email'] = usuario.email  
            session['nome'] = usuario.nome
            session['sobrenome'] = usuario.sobrenome
            session['senha'] = usuario.senha
            session['endereco_rua'] = usuario.endereco_rua
            session['endereco_bairro'] = usuario.endereco_bairro
            session['endereco_cidade'] = usuario.endereco_cidade
            session['endereco_uf'] = usuario.endereco_uf

            flash('Seus dados foram atualizados com sucesso!')
            return redirect(url_for('editar'))
        else:
            flash('Senha atual incorreta!')
    
    return render_template('editar.html', titulo='Editar', usuario=usuario)



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

@app.route('/projeto1')
def projeto1():
    return render_template('projetos/projeto1.html')


@app.route('/projeto2')
def projeto2():
    return render_template('projetos/projeto2.html')