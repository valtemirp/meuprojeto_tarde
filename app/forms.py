from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TelField,TextAreaField,SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, Length, Regexp
from flask_wtf.csrf import CSRFProtect

class Contato(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email',validators=[DataRequired()])
    telefone = TelField('telefone',validators=[DataRequired()])
    mensagem = TextAreaField('mensagem')
    enviar = SubmitField('Enviar')

class Cadastro(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    cpf = StringField('CPF', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    endereco_rua = StringField('Endereço (Rua com Número)', validators=[DataRequired()])
    endereco_bairro = StringField('Bairro', validators=[DataRequired()])
    endereco_cidade = StringField('Cidade', validators=[DataRequired()])
    endereco_uf = SelectField('UF', choices=[
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    ], validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    enviar = SubmitField('Enviar')

