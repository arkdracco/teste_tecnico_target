def pertence_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n or n == 0:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero = int(input("Digite um número: "))
print(pertence_fibonacci(numero))