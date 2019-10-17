import pygame
branco=(255,255,255)
preto=(0,0,0)


pygame.init()
janela = pygame.display.set_mode((700, 600))
pygame.display.set_caption('Figuras e Texto')
ret= pygame.Rect(10,10,45,45)
janela.fill(branco)

fonte = pygame.font.Font(None, 48)
texto = fonte.render('Olá, mundo!', True, branco,preto)
janela.blit(texto, [30, 150])
pygame.draw.line(janela, preto, (0, 600), (800, 600), 200)
pygame.draw.rect(janela, preto,ret)
deve_continuar = True
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
        if event.type == pygame.MOUSEBUTTONDOWN or pygame.MOUSEBUTTONUP:
            ret = ret.move(5,5)
pygame.display.upload()


pygame.quit()