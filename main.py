from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for, flash
from random import choice
from models import RegistroModel
import string
import re

#import mysql.connector

app = Flask(__name__)
app.secret_key = 'fjifjidfjied5df45df485h48@'


#@app.get("/")
#def index():
    # cursor = db.cursor()
    # cursor.execute("SELECT * FROM acortador ORDER BY id DESC LIMIT 5")
    # urlItems = cursor.fetchall()
    # cursor.close()
    #return render_template("/usuarios/registro.html")

@app.get("/crear")
def crearUsuario():
    return render_template("/usuarios/registro.html")

@app.post("/crear")

def crearUsuarioPost():
    name = request.form.get('name')
    email = request.form.get('email')

    if name == "":
        isValid = False
        flash("Debe ingresar su nombre")

    if email == "":
        isValid = False
        flash("Debe ingresar su correo")

    RegistroModel.crearUsuario(name = name, email = email)

    return redirect(url_for('registro'))
    
#VALIDAR CONTRASEÑA
def validar_pass(password):

    def validar_pass(password):
        if 8 <= len(password):
            if re.search('[a-z]', password) and re.search('[A-Z]', password):
                if re.search('[0-9]',password):
                    if re.search('[$*+#@]', password):
                        return True
        return False          
        

app.run(debug=True) #Comentar para heroku