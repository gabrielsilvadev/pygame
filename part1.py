
import pygame
import random
preto=(0,0,0)
norte=(245,222,179)
vermelho=(255,0,0)
terra=(210,180,140)
verde=(0,255,0)
azul=(0,0.255)
amarelo=(233,433,244)


person = pygame.image.load('foto.png')
imagemPeixe = pygame.image.load('silhouette-3313481_1280.png')

LARGURAJANELA = 700
ALTURAJANELA = 400

LARGURAPEIXE = imagemPeixe.get_width()
ALTURAPEIXE = imagemPeixe.get_height()

LARGURA = person.get_width()
ALTURA = person.get_height()

VEL = 6
ITERACOES = 30

def moverJogador(jogador, teclas, dim_janela):
 borda_esquerda = 0
 borda_superior = 0
 borda_direita = dim_janela[0]
 borda_inferior = dim_janela[1]
 if teclas['esquerda'] and jogador['objRect'].left > borda_esquerda:
    jogador['objRect'].x -= jogador['vel']
 if teclas['direita'] and jogador['objRect'].right < borda_direita:
    jogador['objRect'].x += jogador['vel']
 if teclas['cima'] and jogador['objRect'].top > borda_superior:
   jogador['objRect'].y -= jogador['vel']
 if teclas['baixo'] and jogador['objRect'].bottom < borda_inferior:
    jogador['objRect'].y += jogador['vel']
def moverPeixe(peixe):
 peixe['objRect'].x += peixe['vel']

pygame.init()
relogio=pygame.time.Clock()
janela=pygame.display.set_mode((ALTURAJANELA,LARGURAJANELA))
pygame.display.set_caption("Arriegua")
jogador = {'objRect': pygame.Rect(300,100,LARGURA,ALTURA), 'imagem': person, 'vel': VEL}


somComer = pygame.mixer.Sound('djrodrigogpi-efeitos-especiais-som-d2c829.wav')
pygame.mixer.music.load('musica.mid')
pygame.mixer.music.play(-1, 0.0)
somAtivado = True

teclas = {'esquerda': False, 'direita': False, 'cima': False, 'baixo': False}


font=pygame.font.Font(None,48)
text=font.render("Arriegua",True,preto)
janela.blit(text,[30,350])
contador = 0
peixes = []
deve_continuar = True
while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar= False

if evento.type == pygame.KEYDOWN:
  if evento.key == pygame.K_ESCAPE:
      deve_continuar = False
  if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
      teclas['esquerda'] = True
  if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
      teclas['direita'] = True
  if evento.key == pygame.K_UP or evento.key == pygame.K_w:
      teclas['cim'] = True
  if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
      teclas['baixo'] = True
  if evento.key == pygame.K_m:
     if somAtivado:
      pygame.mixer.music.stop()
      somAtivado = False
     else:
       pygame.mixer.music.play(-1, 0.0)
       somAtivado = True

if evento.type == pygame.KEYUP:
  if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
     teclas['esquerda'] = False
  if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
     teclas['direita'] = False
  if evento.key == pygame.K_UP or evento.key == pygame.K_w:
     teclas['cima'] = False
  if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
     teclas['baixo'] = False
if evento.type == pygame.MOUSEBUTTONDOWN:
     peixes.append({'objRect': pygame.Rect(evento.pos[0], evento.pos[1],LARGURAPEIXE, ALTURAPEIXE), 'imagem': imagemPeixe, 'vel': VEL - 3})
contador += 1
if contador >= ITERACOES:
     contador = 0
     posY = random.randint(0, ALTURAJANELA - ALTURAPEIXE)
     posX = -LARGURAPEIXE
     velRandom = random.randint(VEL - 3, VEL + 3)
     peixes.append({'objRect': pygame.Rect(posX, posY,LARGURAPEIXE,ALTURAPEIXE), 'imagem': imagemPeixe, 'vel': velRandom})

janela.blit(imagemFundo, (0,0))
moverJogador(jogador, teclas, (LARGURAJANELA, ALTURA))
janela.blit(jogador['imagem'], jogador['objRect'])

for peixe in peixes[:]:
   comeu = jogador['objRect'].colliderect(peixe['bjRect'])
   if comeu and somAtivado:
     somComer.play()
   if comeu or peixe['objRect'].x > LARGURA:
      peixes.remove(peixe)
for peixe in peixes:
    moverPeixe(peixe)
    janela.blit(peixe['imagem'], peixe['objRect'])

pygame.display.update()
relogio.tick(40)
pygame.quit()

