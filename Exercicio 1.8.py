
print ("Encontrando seu peso ideal baseado no sexo")

altura1 = float(input("Insira sua altura : "))
genero1 = str(input("Qual seu Genero sexual ? M ou F : "))
peso1 = (72.7*altura1)-58
peso2 = (62.1*altura1)-44.7

if genero1 == "M":
    print (f"Seu genero é Masculino e seu peso ideal é {peso1:.2f}")
elif genero1 == "F":
    print (f"Seu genero é Feminino e seu peso ideal é {peso2:.2f}")

input()
