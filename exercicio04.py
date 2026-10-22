idade = int(input("Digite sua idade: "))
esporte = input ("Escolha o Esporte (1 - Natação / 2 - Corrida / 3 - Ciclismo:")
match esporte:
    case 1: 
        if idade < 10:
            print("Categoria: Mirim")
        elif idade <= 14:
            print("Categoria: Infantil")
        else: 
            print("Categoria: Juvenil") 

    case 2:
        if idade < 16:
            print("Categoria: Júnior")
        elif idade >= 16: 
            print("Categoria: Adulto")

    case 3:
         if idade >= 18:
            print("Categoria: Profissional")
         elif idade <18: 
            print("Categoria: Amador")
