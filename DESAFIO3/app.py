from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_Host'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'contatos'

mysql = MySQL(app)

app.config
@app.route('/')
@app.route('/home')
def home():
    return render_template ('Home.html')

@app.route('/contatos', methods=['GET', 'POST'])
def cont():
    if request.method == "POST":
        email = request.form['E-mail']
        assunto = request.form['Assunto']
        descricao = request.form['Descrição']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos(email, assunto, descrição) VALUES (%s, %s, %s)", (email, assunto, descricao))

        mysql.connection.commit()
        cur.close()

        return 'sucesso'
    return render_template('Contatos d1.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contatos")

    if users > 0:
        userDetails = cur.fetchall()
        return render_template("users.html", userDetails=userDetails)

@app.route('/quemsomos')
def qm():
    return render_template('Quem somos d1.html')