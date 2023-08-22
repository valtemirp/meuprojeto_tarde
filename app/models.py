from app import app,db

class ContatoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(60), nullable = False)
    telefone = db.Column(db.String(14), nullable = False)
    mensagem = db.Column(db.Text, nullable = True)
    
    def __repr__(self):
        return 'Contato!'

class CadastroModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    sobrenome = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    cpf = db.Column(db.String(14), nullable=False, unique=True)  
    telefone = db.Column(db.String(15), nullable=False)  
    endereco_rua = db.Column(db.String(100), nullable=False)
    endereco_bairro = db.Column(db.String(50), nullable=False)
    endereco_cidade = db.Column(db.String(50), nullable=False)
    endereco_uf = db.Column(db.String(2), nullable=False)
    senha = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return 'Cadastro!'