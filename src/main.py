from flask import Flask
import re

app = Flask(__name__)

def validar_cpf(cpf_digitado_pelo_usuario):
    lista_valores_primeiro_digito = []
    lista_valores_segundo_digito = []
    nove_digitos = ''

    contador_dos_nove_digitos = 9
    contador_segundo_digito = 11
    contador_primeiro_digito = 10

    # Mantém apenas números
    cpf_limpo = re.sub(r'[^0-9]', '', cpf_digitado_pelo_usuario)

    # Verifica se tem 11 dígitos
    if len(cpf_limpo) < 11:
        return 1

    # Verifica CPFs inválidos por repetição (ex: 11111111111, 00000000000, etc.)
    if cpf_limpo == cpf_limpo[0] * 11:
        return False

    # Cálculo do primeiro dígito
    for i in cpf_limpo:
        i = int(i)
        lista_valores_primeiro_digito.append(i * contador_primeiro_digito)
        contador_primeiro_digito -= 1
        if contador_primeiro_digito == 1:
            break

    soma_total_primeiro_digito = sum(lista_valores_primeiro_digito) * 10
    ultimo_primeiro_digito = soma_total_primeiro_digito % 11
    ultimo_primeiro_digito = ultimo_primeiro_digito if ultimo_primeiro_digito <= 9 else 0

    # Cálculo do segundo dígito
    for i in cpf_limpo:
        i = int(i)
        lista_valores_segundo_digito.append(i * contador_segundo_digito)
        contador_segundo_digito -= 1
        if contador_segundo_digito == 1:
            break

    soma_total_segundo_digito = sum(lista_valores_segundo_digito) * 10
    ultimo_segundo_digito = soma_total_segundo_digito % 11
    ultimo_segundo_digito = ultimo_segundo_digito if ultimo_segundo_digito <= 9 else 0

    # Monta o CPF gerado pelo cálculo
    for i in cpf_limpo:
        nove_digitos += i
        contador_dos_nove_digitos -= 1
        if contador_dos_nove_digitos == 0:
            break

    cpf_gerado_pelo_calculo = f'{nove_digitos}{ultimo_primeiro_digito}{ultimo_segundo_digito}'

    # Compara com o CPF digitado
    if cpf_gerado_pelo_calculo == cpf_limpo:
        return True
    else:
        return False

@app.route("/")
def instrucoes():
    return "<p>Esse é um site onde valida se o CPF é válido ou não. Você precisa passar o CPF pela URL, logo após o localhost coloque /valida/'o seu cpf'</p>"

@app.route("/valida/<cpf>")
def valida(cpf):
    valido = validar_cpf(cpf)
    if valido == True:
        return f"Seu CPF é válido! {cpf}"
    elif valido == 1:
        return f"Digite um CPF com pelo menos 11 caracteres!"
    else:
        return f"Seu CPF é inválido!"

if __name__ == "__main__":
    app.run(debug=True)
