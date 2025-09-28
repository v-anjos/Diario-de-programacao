"""
Calculadora de Áreas
Autor: Vinicius Anjos
Data: 2025-09-28
Descrição: Calcula a área de diferentes figuras geométricas
"""

import math

def area_circulo(raio):
    return math.pi * raio**2

def area_retangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def main():
    print("Calculadora de Áreas de Figuras Geométricas\n")
    print("Escolha a figura:")
    print("1 - Círculo")
    print("2 - Retângulo")
    print("3 - Triângulo")

    opcao = input("Digite o número da figura: ")

    if opcao == "1":
        raio = float(input("Digite o raio do círculo: "))
        print(f"A área do círculo é: {area_circulo(raio):.2f}")
    elif opcao == "2":
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        print(f"A área do retângulo é: {area_retangulo(base, altura):.2f}")
    elif opcao == "3":
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        print(f"A área do triângulo é: {area_triangulo(base, altura):.2f}")
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
