print("==== Seja Bem-vindo à Locadora ====")

# Exibe o catálogo de filmes
def exibir_catalogo():
    print("\nCatálogo de Filmes:")
    print("1 - Matrix (R$ 5,00 por dia)")
    print("2 - Vingadores (R$ 6,00 por dia)")
    print("3 - Toy Story (R$ 4,00 por dia)")
    print("4 - Jurassic Park (R$ 5,50 por dia)")
    print("5 - Up (R$ 6,50 por dia)")
    print("6 - Encerrar")


def pegar_filme(opcao):
    if opcao == 1:
        return "Matrix", 5.00
    if opcao == 2:
        return "Vingadores", 6.00
    if opcao == 3:
        return "Toy Story", 4.00
    if opcao == 4:
        return "Jurassic Park", 5.50
    if opcao == 5:
        return "Up", 6.50
    return "", 0


def alugar_filme(opcao, dias, alugueis):
    nome, preco = pegar_filme(opcao)
    if nome != "":
        valor = preco * dias
        alugueis += [[nome, dias, valor]]
        print("Você alugou", nome, "por", dias, "dia(s). Valor: R$", (valor))
    else:
        print("Opção inválida.")


def exibir_resumo(alugueis):
    print("\nResumo das Locações:")
    if alugueis == 0:
        print("Nenhum filme foi alugado.")
    else:
        total = 0
        contador = 1
        for aluguel in alugueis:
            print(str(contador) + ".", aluguel[0], "-", aluguel[1], "dia(s) - R$", (aluguel[2]))
            total += aluguel[2]
            contador += 1
        print("Total geral: R$", (total))


def main():
    alugueis = []
    while True:
        exibir_catalogo()
        try:
            escolha = int(input("Escolha o número do filme que deseja alugar: "))
            if escolha == 6:
                print("Encerrando o sistema...")
                break
            if escolha >= 1 and escolha <= 5:
                dias = int(input("Por quantos dias deseja alugar? "))
                if dias > 0:
                    alugar_filme(escolha, dias, alugueis)
                else:
                    print("Número de dias inválido.")
            else:
                print("Opção inválida.")
        except:
            print("Entrada inválida. Digite um número.")

    exibir_resumo(alugueis)

main()