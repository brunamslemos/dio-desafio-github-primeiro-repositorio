print ("Insira o valor")
X = float(input())

nota100 = int(X/100)
print (nota100, "nota(s) de R$100,00")

restnota100 = X%100
nota50 = int(restnota100/50)
print (nota50, "nota(s) de R$50,00")

restnota50 = restnota100%50
nota20 = int(restnota50/20)
print (nota20, "nota(s) de R$20,00")

restnota20 = restnota50%20
nota10 = int(restnota20/10)
print (nota10, "nota(s) de R$10,00")

restnota10 = restnota20%10
nota5 = int(restnota10/5)
print (nota5, "nota(s) de R$5,00")

restnota5 = restnota10%5
nota2 = int((restnota5)/2)
print (nota2, "nota(s) de R$2,00")

restnota2 = restnota5%2
moeda1 = int(restnota2/1)
print (moeda1, "moeda(s) de R$1,00")

restmoeda1 = restnota2%1
moeda05 = int(restmoeda1/0.5)
print (moeda05, "moeda(s) de R$0,50")

restmoeda05 = restmoeda1%0.5
moeda025 = int(restmoeda05/0.25)
print (moeda025, "moeda(s) de R$0,25")

restmoeda025 = restmoeda05%0.25
moeda010 = int(restmoeda025/0.10)
print (moeda010, "moeda(s) de R$0,10")

restmoeda010 = restmoeda025%0.10
moeda5 = int(restmoeda010/0.05)
print (moeda5, "moeda(s) de R$0,05")

restmoeda5 = restmoeda010%0.05
moeda01 = int(restmoeda5/0.01)
print (moeda01, "moeda(s) de R$0,01")
