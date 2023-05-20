
print ("Preço de Abastecimento de combustivel\n")

gasolina = float(5.00)
etanol = float(3.50)
gasolina_ad = float(6.99)
litros = float(input("Quantos Litros Deseja Abastecer ? "))

print (f"O Valor Encontrado na Bomba será de : \nGasolina R$ {litros * gasolina:.2f} \nEtanol R$ {litros * etanol:.2f} \nGasolina Aditivada R$ {litros * gasolina_ad:.2f}")

input()