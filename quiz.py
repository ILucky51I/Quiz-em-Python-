print("Seja muito bem vindo ao quiz do Rafael!")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S":
    quit()

score = 0

print("Começando...")
print("1- Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")

print("2- Qual é o nome do encanador protagonista da famosa franquia da Nintendo? \n (A) Luigi \n (B) Bowser \n (C) Wario \n (D) Mario \n")
answer_2 = input("Resposta: ")

if answer_2 == "D":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")

print("3- Em qual universo se passa a série de filmes e livros “Harry Potter”? \n (A) Nárnia \n (B) Westeros \n (C) Mundo Bruxo \n (D) Terra Média \n")
answer_3 = input("Resposta: ")

if answer_3 == "C":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")

print("4- Em “The Legend of Zelda”, qual é o nome do protagonista jogável? \n (A) Zelda \n (B) Ganondorf \n (C) Link \n (D) Hyrule \n")
answer_4 = input("Resposta: ")

if answer_4 == "C":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")

print("5- Qual é o nome do super-herói bilionário da Marvel que usa uma armadura tecnológica? \n (A) Batman \n (B) Thor \n (C) Capitão América \n (D) Homem de Ferro \n")
answer_5 = input("Resposta: ")

if answer_5 == "D":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")

print(f"Quiz acabou... Pontuação: {score}/5")



