
ana = 0
bruno = 0
carlos = 0
brancos = 0

opcao = 0

while opcao != 6:

    print(" - Eleição do Representante de Sala - ")
    print("1 - votar em ana")
    print("2 - votar em bruno")
    print("3 - votar em carlos")
    print("4 - votar em branco")
    print("5 - consultar resultado parcial")
    print("6 - encerrar votação")

    opcao = int(input("escolha uma opção: "))

    if opcao == 1:
        ana += 1
        print("voto em ana registrado")

    elif opcao == 2:
        bruno += 1
        print("voto em bruno registrado")

    elif opcao == 3:
        carlos += 1
        print("voto em carlos registrado")

    elif opcao == 4:
        brancos += 1
        print("voto em branco registrado")

    elif opcao == 5:
        total = ana + bruno + carlos + brancos

        print(" - Resultado Parcial - ")
        print("ana:", ana, "votos")
        print("bruno:", bruno, "votos")
        print("carlos:", carlos, "votos")
        print("brancos:", brancos, "votos")
        print("total de votos:", total)

    elif opcao == 6:
        print(" - Encerrando Votação - ")

    else:
        print(" - Opção inválida - tente novamente - ")

total = ana + bruno + carlos + brancos

print(" - Resultado Final - ")
print("ana:", ana, "votos")
print("bruno:", bruno, "votos")
print("carlos:", carlos, "votos")
print("brancos:", brancos, "votos")
print("total de votos:", total)

if ana > bruno and ana > carlos:
    print("candidato vencedor - ana")

elif bruno > ana and bruno > carlos:
    print("candidato vencedor - bruno")

elif carlos > ana and carlos > bruno:
    print("candidato vencedor - carlos")

elif ana == bruno and ana > carlos:
    print("empate - entre ana e bruno")

elif ana == carlos and ana > bruno:
    print("empate - entre ana e carlos")

elif bruno == carlos and bruno > ana:
    print("empate - entre bruno e carlos")

else:
    print("empate - entre ana, bruno e carlos")

print(" - Votação Encerrada - ")