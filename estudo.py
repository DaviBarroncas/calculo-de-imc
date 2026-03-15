while True:
   print("""escolha uma das opções: 
         [ 1 ] calcular o imc e condiçoes de saúde
         [ 2 ] plano de dietas 
         [ 3 ] planos de treino""")
   opçao=int(input("sua opção: "))
   if opçao==1:
      a=float(input("digite sua altura: ").replace(",","."))
      print("você tem {}m de altura".format(a))
      b=float(input("digite seu peso: ").replace(",","."))
      if b.is_integer():
         print("voce pesa {} ".format(b).replace(".", ","))
      else:
         print("voce pesa {}kg ".format(float(b)).replace(".", ","))
      c=b/(a**2)
      print("seu imc é {:.2f}".format(c).replace(".", ","))
      if c<18.5:
         print("voce esta abaixo do peso")
      elif 18.5<=c<24.9:
         print(" voce está com peso normal")
      elif 25<=c<29.9:
         print("voce esta em sobrepeso")
      elif 30<=c<45:
         print("você está com obesidade GRAU I")
      elif 35<=c<40:
         print("voce esta com obesidade GRAU II")
      elif c>=40:
         print("voce esta com obesidade GRAU III")
      #interface para a obesidade
      if c>30:
         d=float((input("sua dieta está em torno de quantas calorias diarias?:")))
         if d>5000:
            print("teste")
   
      break

   if opçao==2:
         a=input("digite seu nome: ")
         b=int(input("digite sua idade: "))
         w=input("digite seu sexo[M/F]: ")
         d=float(input("digite seu imc: ").replace(",","."))
         if d <=30:
            print(" voce sera redirecionado para sua dieta")
         if d>30 and w in "Mm":
            if b<18:
               print("""SITUAÇÃO:
               {}
               HOMEM
               MENOR DE IDADE
               oBESIDADE""".format(a))
            else:
                  print(""" SITUAÇÃO:
                  {}
                  HOMEM
                  MAIOR DE IDADE
               OBESIDADE""".format(a) )
         if d>30 and  w in "Ff":
            if b<18:
               print("""SITUAÇÃO:
               {}
               MULHER
               MENOR DE IDADE
               OBESIDADE""".format(a))
            else:
               print("""SITUAÇÃO:
               {}
               MULHER
               MAIOR DE IDADE
               OBESIDADE""".format(a))
         print("sua dieta será .")




