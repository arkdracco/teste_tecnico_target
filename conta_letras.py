def contar_letras_a(s):
    contagem = s.lower().count('a')
    return f"A letra 'a' aparece {contagem} vezes na string."

# Exemplo de uso
string = input("Digite uma string: ")
print(contar_letras_a(string))
