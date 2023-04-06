from flask import Flask , url_for, render_template
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template ('Home.html')

@app.route('/contatos')
def cont():
    return render_template ('Contatos d1.html')

@app.route('/quem somos')
def qm():
    return render_template('Quem somos d1.html')