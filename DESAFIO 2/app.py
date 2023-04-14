from flask import Flask , url_for, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template ('Home.html')

@app.route('/contatos')
def cont():
    return render_template ('Contatos d1.html')

@app.route('/quemsomos')
def qm():
    return render_template('Quem somos d1.html')