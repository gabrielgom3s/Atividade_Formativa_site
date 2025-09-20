import pytest
import main

def test_cpf_valido():
    """CPF válido conhecido"""
    assert main.validar_cpf("52998224725") == True

def test_cpf_invalido():
    """CPF inválido conhecido"""
    assert main.validar_cpf("12345678900") == False

def test_cpf_menor_que_11():
    """CPF menor que 11 dígitos deve retornar 1"""
    assert main.validar_cpf("12345") == 1

def test_cpf_com_pontos_tracos():
    """CPF válido com pontos e traço deve ser aceito"""
    assert main.validar_cpf("529.982.247-25") == True

def test_cpf_repetido():
    """CPF com todos os dígitos iguais é inválido"""
    assert main.validar_cpf("11111111111") == False

def test_cpf_invalido_aleatorio():
    """Outro CPF aleatório inválido"""
    assert main.validar_cpf("98765432100") == False
