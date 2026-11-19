from cupom import desconto_valido


def test_percentual_igual_ao_limite_22_e_aceito():
    # Preparar
    percentual = 22
    # Agir
    resultado = desconto_valido(percentual)
    # Verificar
    assert resultado is True


def test_percentual_acima_do_limite_23_e_rejeitado():
    # Preparar
    percentual = 23
    # Agir
    resultado = desconto_valido(percentual)
    # Verificar
    assert resultado is False


def test_percentual_zero_e_rejeitado():
    # Preparar
    percentual = 0
    # Agir
    resultado = desconto_valido(percentual)
    # Verificar
    assert resultado is False
