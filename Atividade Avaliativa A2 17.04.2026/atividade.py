#questao 1:
print("Hello World!")



#questao 2:
idade = int(input("Digite a idade do aluno: "))

if idade >= 16:
    print("Pode votar!")
else:
    print("Ainda não pode votar.")



#questao 3:
def somaItens():
    total = 0

    while True:
        try:
            valor = float(input("Digite o valor do item: R$ "))

            if valor == 0:
                break

            total += valor
            print(f"Total: R$ {total:.2f}")

        except ValueError:
            print("Por favor, digite um número válido")

somaItens()



#questao 4:
def calcular_imc():
    try:
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura:"))

        if altura <= 0 or peso <= 0:
            print("O peso e a altura devem ser maiores que zero.")
            return
        
        imc = peso / altura ** 2
        print(f"IMC: {imc:.2f}")

        if imc == 24.9 or imc < 24.8:
            print("Magro.")
        elif imc == 25.0 or imc < 29.9:
            print("Normal.")
        elif imc == 30.0 or imc < 34.9:
            print("Acima do peso.")
        else:
            print("Está obeso, cuidado.")
    except ValueError:
        print("Por favor, digite um número válido.")

calcular_imc()



#questao 5:
nomes = []

while True:
    nome = input("Liste os nomes dos amigos: ")
    if nome == "":
        break
    nomes.append(nome)

quantidade = len(nomes)
print(f"Quantidade de amigos listados: {quantidade}")

if quantidade % 2 == 0:
    print("Quantidade de amigos é par.")
else:
    print("Quantidade de amigos é ímpar.")



#questao 6:
temperaturas = []
for i in range(1, 8):
    temperatura = float(input(f"Digite a temperatura do dia {i}:"))
    temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)
print(f"A média das temperaturas é: {media:.2f}")



#questao 7:
vendas = []
for i in range(1, 8):
    valor = int(input(f"Digite o valor da venda do dia {i}:"))
    vendas.append(valor)

soma = 0
for venda in vendas:
    if venda % 2 == 0:
        soma += venda

print(f"A soma dos valores pares é: {soma}")



#questao 8:
valor = float(input("Digite o valor da compra: R$"))

if valor > 500:
    desconto = valor * 0.20
elif valor >= 200:
    desconto = valor * 0.10
else:
    desconto = 0

valorFinal = valor - desconto
print(f"Preço final com desconto: R$ {valorFinal:.2f}")



#questao 9:
notas = []

for i in range(1, 6):
    nota = float(input(f"Digite as notas do aluno {i}:"))
    notas.append(nota)

acima = 0
for nota in notas:
    if nota > 7:
        acima += 1

print(f"Quantidade de notas acima de 7: {acima}")



#questao 11:
idades = []
for i in range(1,6):
    idade = int(input(f"Digite as idades dos alunos {i}: "))
    idades.append(idade)

idades.sort()
print("Idades em ordem crescente: ", idades)



#questao 10:
frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"

contarVogais = 0

for letra in frase:
    if letra in vogais:
        contarVogais += 1

print(f"Quantidade de vogais na frase é: {contarVogais}")



#questao 12:
#não consegui fazer