import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main

def test_cpf_valido():
    assert main.validar_cpf("52998224725") == True

def test_cpf_invalido():
    assert main.validar_cpf("12345678900") == False