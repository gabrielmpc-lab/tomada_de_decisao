#programa que pede idade, altura e pergunta se tem autorização dos pais
idade = int(input("Qual sua idade?: "))
altura = int(input("E sua altura?: "))
autorização = input("Você tem autorização dos seus pais? (sim ou não): ")

if idade >= 12 and altura >= 140 or autorização == "sim":
    print (f"Aceso liberado")
elif idade <= 18:
    print (f"Acesso negado")
elif idade <12 and altura <140:
    if autorização == "sim":
        print (f"Acesso liberado")
    else:
        print(f"Acesso negado")