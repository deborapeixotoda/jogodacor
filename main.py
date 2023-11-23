import random
pontos_seus = 0
pontos_deles = 0
while(True):

  cor_secreta = random.choice(['R', 'G', 'B'])
  palpite = input("adivinhe a cor (R,G,B):").upper()
  if palpite not in ['R', 'G', 'B']:
     print("entrada invalida, escolha R,G,B")
  elif palpite == cor_secreta:
     print('paraben!, voce acertou!')
     pontos_seus = pontos_seus +1
  elif palpite != cor_secreta:
     print("voce errou")
     pontos_deles = pontos_deles +1
     print('a cor  era', cor_secreta)

     print(f"voce {pontos_seus} X PC {pontos_deles}")
