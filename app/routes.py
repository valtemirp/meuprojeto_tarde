from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Olá mundo"

@app.route('/projetos')
def projetos():
    return 'Projetos'