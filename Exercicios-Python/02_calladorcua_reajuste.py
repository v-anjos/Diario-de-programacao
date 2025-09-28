Calculadora de reajuste salarial simples para iniciantes.

def calcular_reajuste(salario: float) -> tuple:
    if salario < 0:
        raise ValueError("Salário não pode ser negativo.")
    if salario < 500:
        percentual = 0.15
    elif salario <= 1000:
        percentual = 0.10
    else:
        percentual = 0.05

    reajuste = salario * percentual
    novo_salario = salario + reajuste
    return reajuste, novo_salario

def entrada_usuario() -> float:
    while True:
        texto = input("Digite o salário atual (ex: 1200.50): ").strip()
        texto = texto.replace(",", ".")
        try:
            salario = float(texto)
            return salario
        except ValueError:
            print("Entrada inválida. Digite um número, por exemplo: 1200.50")

def main():
    print("Calculadora de Reajuste Salarial\n")
    salario = entrada_usuario()
    try:
        reajuste, novo = calcular_reajuste(salario)
    except ValueError as e:
        print("Erro:", e)
        return

    print(f"\nSalário atual: R$ {salario:,.2f}")
    print(f"Reajuste aplicado: R$ {reajuste:,.2f}")
    print(f"Novo salário: R$ {novo:,.2f}")

if __name__ == "__main__":
    main()
