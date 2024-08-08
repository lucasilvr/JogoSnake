import pygame #pip install pygame #usada para criar jogos e aplicativos multimídia
import random #usada para gerar números aleatórios e realizar operações relacionadas a aleatoriedade

pygame.init()
pygame.display.set_caption("Jogo Snake em Python") #definindo nome do jogo
largura, altura = 1200, 800 #tela do jogo
tela = pygame.display.set_mode((largura, altura)) #passando as informações da largura e altura

#cores RGB #padrão RGB: quanto de vermelho, quanto de verde e quanto de azul
preta = (0,0,0)
branca = (255,255,255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
relogio = pygame.time.Clock()

#parametros da cobra
tamanho_quadrado = 20
velocidade_jogo = 15 #quanto a cobra anda a cada 'tick' do relogio, a cada execução do loop

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0 #gera uma posiçao da comida de 0 ate a largura - tamanho do quadrado para nao gerar um quadrado fora da tela
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0 #gera uma posiçao da comida de 0 ate a largura - tamanho do quadrado para nao gerar um quadrado fora da tela
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho]) #desenhando retângulo

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 50)
    texto = fonte.render(f"Pontos: {pontuacao} ", True, vermelha) #o parametro true serve apenas visualmente mais bonito, nao tanto pixelado
    tela.blit(texto, [1,1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = - tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = - tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False

    x = largura / 2 #eixo horizontal da tela
    y = altura / 2 #eixo vertical da tela

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preta)
        for evento in pygame.event.get(): #para cada click que o usuario da
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN: #apertar uma tecla
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

            #desenhar comida
            desenhar_comida(tamanho_quadrado, comida_x, comida_y)

            #atualizar a posicao da cobra
            x = x + velocidade_x
            y = y + velocidade_y

            #desenhar cobra
            pixels.append([x, y]) #adicionando novo pixel
            if len(pixels) > tamanho_cobra: #se a quantidade de pixel for maior que o tamanho que a cobra tem que ter
                del pixels[0] #deleta o ultimo pixel, o 'andar' da cobra

            #se a cobrinha bateu a 'cabeça' no proprio corpo
            for pixel in pixels[:-1]:
                if pixel == [x, y]:
                    fim_jogo = True

            desenhar_cobra(tamanho_quadrado, pixels)

            #desenhar pontos
            desenhar_pontuacao(tamanho_cobra - 1)

            #atualizaçao da tela
            if x < 0 or x >= largura or y < 0 or y >= altura:
                fim_jogo = True #quando a cobra bate na parede encerrar o jogo

            pygame.display.update()
            relogio.tick(velocidade_jogo)

            #criar nova comida
            if x == comida_x and y == comida_y:
                tamanho_cobra  += 1
                comida_x, comida_y = gerar_comida()

rodar_jogo()