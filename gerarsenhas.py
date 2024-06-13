import random
import string

def gerar_senha(segura=True, comprimento=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiais=True):
    caracter = ''

    if incluir_maiusculas:
        caracter += string.ascii_uppercase
    if incluir_minusculas:
        caracter += string.ascii_lowercase
    if incluir_numeros:
        caracter += string.digits
    if incluir_especiais:
        caracter += string.punctuation

    if not caracter:
        raise ValueError("Ao menos um tipo de caracter deve ser incluido")

    senha = ''.join(random.choice(caracter) for _ in range(comprimento))

    if segura:
        while (incluir_maiusculas and not any(c.isupper() for c in senha)) or \
                (incluir_minusculas and not any(c.islower() for c in senha)) or \
                (incluir_numeros and not any(c.isdigit() for c in senha)) or \
                (incluir_especiais and not any(c in string.punctuation for c in senha)):
                        senha = ''.join(random.choice(caracter) for _ in range(comprimento))

    return senha

print(gerar_senha(comprimento=16))
