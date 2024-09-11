# Sequências lógicas e suas soluções
sequencias = {
    "a": [1, 3, 5, 7, 9],   # Números ímpares
    "b": [2, 4, 8, 16, 32, 64, 128],   # Multiplicação por 2
    "c": [0, 1, 4, 9, 16, 25, 36, 49],   # Quadrados perfeitos
    "d": [4, 16, 36, 64, 100],   # Quadrados de números pares
    "e": [1, 1, 2, 3, 5, 8, 13],   # Sequência de Fibonacci
    "f": [2, 10, 12, 16, 17, 18, 19, 20]   # Lógica de alternância
}

# Exibindo as sequências completas
for key, seq in sequencias.items():
    print(f"Sequência {key}: {seq}")