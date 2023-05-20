
print ("Lista de Nomes e Idade de convidados\n")

nome1 = str(input("Insira o Nome do seu convidado : "))
idade1 = int(input("Qual a idade ? "))


nome2 = str(input("Insira o Nome do seu convidado : "))
idade2 = int(input("Qual a idade ? ")) 


nome3 = str(input("Insira o Nome do seu convidado : "))
idade3 = int(input("Qual a idade ? ")) 

idade_media1 = int(idade1 + idade2 + idade3) / 3


print ("Sua lista de convidados é a seguinte:\n" "\n", nome1, " : ", idade1, " Anos", "\n", nome2, " : ", idade2, " Anos", "\n", nome3, " : ", idade3, " Anos", )
print (f"\nA média de idade do seu evento é de : {idade_media1:.0f} Anos de Idade\n")

input()