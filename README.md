# Gerador de Senha Segura

Este é um gerador de senha em Python que permite a criação de senhas seguras de acordo com diferentes critérios configuráveis.

## Uso

### Função `gerar_senha`

A função `gerar_senha` é definida da seguinte forma:

```python
def gerar_senha(segura=True, comprimento=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiais=True):
    # Implementação da função
Parâmetros
segura: Booleano que define se a senha gerada deve garantir a inclusão de pelo menos um caractere de cada tipo especificado.
comprimento: Inteiro que define o comprimento da senha gerada (padrão é 12).
incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais: Booleanos que controlam quais tipos de caracteres devem ser incluídos na senha.

# Gerar uma senha segura com 16 caracteres
print(gerar_senha(comprimento=16))

#Considerações de Segurança
A função gerar_senha implementa um mecanismo de verificação (segura=True) para garantir que a senha gerada inclua pelo menos um caractere de cada tipo selecionado, se especificado. Isso ajuda a aumentar a segurança da senha gerada.

#Requisitos
Este script requer Python 3.x e utiliza o módulo padrão random e string.

#Contribuição
Contribuições são bem-vindas! Se você tiver sugestões de melhorias, sinta-se à vontade para enviar um pull request.
