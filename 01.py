#programa que peergunte se é estudante ou não, o dia da semana e o tipo de sala
estado_civil = input("Você é estudante?: ")
dia = input("Que dia é hoje?: ")
tipo_da_sala = input("Em que tipo de sala você vai assistir?: ")

if estado_civil == "sim" or dia == "terca" and tipo_da_sala == "comum":
    print (f"Ok! Você ganhará o desconto.")
elif estado_civil == "sim":
    if dia != "terca"  and tipo_da_sala == "comum":
        print(f"Ok! Você ganhará o desconto, pois é estudante.")
elif dia == "terca" and tipo_da_sala != "vip":
    if estado_civil != "sim":
        print(f"Processado, nas terças você tem direito ao desconto!")
elif estado_civil != "sim" and dia != "terca":
    print(f"Liberado, porém sem desconto.")
