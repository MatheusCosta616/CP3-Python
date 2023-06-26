
import random
import re


# Função para sortear um funcionário
def sortear_funcionario():
    funcionarios = ["Matheus", "João", "Pedro", "Henrique"]
    sorteado = funcionarios[random.randint(0, len(funcionarios) - 1)]
    return sorteado


# Função para validar as informações do cliente
def validar_informacoes(nome, cep, ano_nascimento):
    if not re.match("^[a-zA-Z\s]*$", nome):
        print("Nome só pode conter caracteres")
        return False
    if not re.match("^\d{5}-\d{3}$", cep):
        print("CEP deve ser composto de 5 dígitos, um traço e 3 dígitos")
        return False
    if not (ano_nascimento.isdigit() and len(ano_nascimento) == 4):
        print("O ano de nascimento deve ser composto de 4 dígitos")
        return False
    return True


# Função para calcular a idade do cliente
def calcular_idade(ano_nascimento):
    idade = 2023 - int(ano_nascimento)
    if idade < 18:
        print("Não é permitida a venda de bebidas alcóolicas para menores de idade.")
        return False
    return True


# Função para exibir opções de vinho
def exibir_vinhos():
    vinhos = [("Château Mouton Rothschild", 1000.0), ("Dom Pérignon Rosé", 4000.0),
              ("Screaming Eagle Cabernet 1992", 2000.0), ("Château d'Yquem", 3000.0),
              ("Penfolds Grange", 5000.0)]
    return vinhos


# Programa principal
def main():
# Sorteando um funcionário
    funcionario = sortear_funcionario()

# Bem-vindo ao cliente
    print(f"Bem-vindo, cliente! O funcionário que irá acompanhar sua compra é {funcionario}.")
    nome = input("Por favor, informe seu nome: ")
    cep = input("Informe seu CEP (formato xxxxx-xxx): ")
    ano_nascimento = input("Informe o ano do seu nascimento: ")

# Validação das informações
    if not validar_informacoes(nome, cep, ano_nascimento):
        return

# Cálculo da idade
    if not calcular_idade(ano_nascimento):
        return

# Carrinho de compras
    carrinho = []

# Compra de vinhos
    while True:
# Mostrando opções de vinho
        vinhos = exibir_vinhos()
        for i, vinho in enumerate(vinhos):
            print(f"{i + 1}. {vinho[0]} - R$ {vinho[1]}")
        escolha = int(input("Qual vinho você gostaria de comprar? ")) - 1
        quantidade = int(input("Quantas garrafas desse vinho você quer comprar? "))

# Verificando se o vinho já está no carrinho
        for item in carrinho:
            if item[0] == vinhos[escolha][0]:
                item[1] += quantidade
                item[2] += quantidade * vinhos[escolha][1]
                break
        else:
            carrinho.append([vinhos[escolha][0], quantidade, quantidade * vinhos[escolha][1]])

        continuar = input("Deseja continuar comprando mais vinhos? (s/n) ")
        if continuar.lower() != "s":
            break

# Finalizando a venda
    print(f"\nFuncionário que o atendeu: {funcionario}")
    print(f"Cliente: {nome}")
    total = 0
    for item in carrinho:
        print(f"{item[0]}: R$ {item[2]} ({item[1]} garrafas a R$ {item[2] / item[1]} cada)")
        total += item[2]

# Cálculo do frete
    if total < 200:
        print(f"Valor do frete: R$ 20.0")
        total += 20
    else:
        print("FRETE GRÁTIS")

    print(f"Total a pagar: R$ {total}")

# Mensagem de despedida
    print(f"Obrigado pela sua compra, {nome}! Esperamos vê-lo novamente em breve.")


if __name__ == "__main__":
    main()

