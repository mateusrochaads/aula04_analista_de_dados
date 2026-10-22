print("Prova")
nome = input("Nome:")

prova01 = float(input("Digite a nota da prova01:").replace(",","."))
prova02 = float(input("Digite a nota da prova02:").replace(",","."))
prova03 = float(input("Digite a nota da prova 03:").replace(",","."))

media = (prova01 + prova02 + prova03) / 3

if media >=7:
    situacao = "aprovado"
elif media >= 5:
    situacao = "recuperaçao"
else: 
    situacao = "reprovado" 

print("\nResultado:")   
print(f"Nome: {nome}")
print(f"Prova01: {prova01:.1f}".replace(".",","))
print(f"Prova02: {prova02:.1f}".replace(".",","))
print(f"Prova03: {prova03:.1f}".replace(".",","))
print(f"Situacao: {situacao.upper()}")


