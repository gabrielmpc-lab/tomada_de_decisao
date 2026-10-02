inadimplencia = input("Você possui histórico de inadimplência? (sim ou não): ")
if inadimplencia == "nao":
    renda_mensal = float (input("Informe sua renda mensal: "))
    score_de_credito = int(input("Informe seu score de crédito: "))
    bens_garantia = input("Você possui bens como garantia? (sim ou não): ")


    if renda_mensal >= 3000 and score_de_credito >= 600 and inadimplencia == "nao":
        print(f"O empréstimo requisitado foi aprovado! favor retirar no hall.")
    elif inadimplencia == "nao" and bens_garantia == "sim":
        if renda_mensal < 3000 or score_de_credito < 600:
            print(f"Devido aos bens como garantia e o histórico de inadimplência inexistente, retire o empréstimo requisitado no hall.")
    elif renda_mensal < 3000 and score_de_credito < 600 and bens_garantia == "nao":
        print(f"Você não atende a nenhum dos reuisitos, empréstimo negado.")
    else:
        print(f"O empréstimo foi recusado devido à falta de requisitos cumpridos.")

elif inadimplencia == "sim":
    resposta = "Empréstimo negado devido ao histórico de inadimplência."
else:
    resposta = "Resposta inválida, tente novamente."

print(f"{resposta}")