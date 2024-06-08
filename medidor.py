
# Função que realiza o cálculo da média de temperatura anual
def calcular_media(temperaturas):
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)



# Menu de seleção de meses
mes = int(input("Informe um mês representado por um número inteiro de 1 a 12: "))
if mes<1 or mes>12 : print("Inválido! Informe um valor de 1 a 12.")
else :  
    meses =["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    print(f"Mês selecionado: {meses[mes - 1]}" )



temp = float(input("Informe a temperatura em graus Celsius mais elevada deste mês: "))
if temp<40 : print("---> Esta temperatura não se configura como escaldante.")
if temp<-90 or temp>60 : print("Temperatura inválida.")
print(f"Temperatura: {temp} ºC")


# Pede para informar as temperaturas de todos os meses, incluindo o selecionado anteriormente
temperaturas = []
meses_escaldantes = 0
for mes in meses:
    temperatura = float(input(f"\nInforme a temperatura, em graus Celsius, mais elevada de {mes}: "))
    if temperatura>38 : print(" ---> Este mês teve temperatura escaldante.")
    temperaturas.append(temperatura)

    if temperatura>38:
        meses_escaldantes += 1



# Informes que aparecerão na tela
media_temp = calcular_media(temperaturas)
mes_mais_quente = meses[temperaturas.index(max(temperaturas))]
mes_mens_quente = meses[temperaturas.index(min(temperaturas))]

print("\n===================== INFORMATIVO =====================")
print("\nTemperaturas        : ", temperaturas)
print(f"Temperatura média   : {media_temp}")
print(f"Meses escaldantes   : {meses_escaldantes} meses.")
print(f"Mês mais escaldante : {mes_mais_quente}")
print(f"Mês menos quente    : {mes_mens_quente}")
print("\n=======================================================")