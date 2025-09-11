from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Este é um pequeno site aonde vou implementar um codigo para validação de cpf, feito por mim com ajuda de um curso da udemy</p>"