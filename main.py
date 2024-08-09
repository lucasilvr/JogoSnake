import pygame #pip install pygame #usada para criar jogos e aplicativos multimídia
import random #usada para gerar números aleatórios e realizar operações relacionadas a aleatoriedade

pygame.init() #inicializa todos os módulos do Pygam
pygame.display.set_caption("Jogo Snake em Python") #define o título do jogo
largura, altura = 1200, 800 #define as dimensões da tela do jogo
tela = pygame.display.set_mode((largura, altura)) #cria a janela do jogo com a largura e altura especificadas

#cores RGB #padrão RGB: quanto de vermelho, quanto de verde e quanto de azul
preta = (0,0,0)
branca = (255,255,255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
relogio = pygame.time.Clock()  #cria um objeto de relógio para controlar a taxa de atualização do jogo

#parametros da cobra
tamanho_quadrado = 20
velocidade_jogo = 15 #quanto a cobra anda a cada 'tick' do relogio, a cada execução do loop

def gerar_comida(): #gera uma nova posição para a comida de forma aleatória, garantindo que esteja alinhada com a grade da tela
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0 #gera uma posiçao da comida de 0 ate a largura - tamanho do quadrado para nao gerar um quadrado fora da tela
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0 #gera uma posiçao da comida de 0 ate a largura - tamanho do quadrado para nao gerar um quadrado fora da tela
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho]) #desenhando retângulo

def desenhar_cobra(tamanho, pixels): #desenha a cobra na tela como uma série de retângulos brancos
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao): #desenha a pontuação e uma mensagem de crédito na tela
    fonte = pygame.font.SysFont("Helvetica", 50)
    texto = fonte.render(f"Pontos: {pontuacao} ", True, vermelha) #o parametro true serve apenas visualmente mais bonito, nao tanto pixelado
    tela.blit(texto, [1,1])

    fonte1 = pygame.font.SysFont("Helvetica", 30)
    texto = fonte1.render("Desenvolvido por Lucas", True, branca)
    tela.blit(texto, [420,1])

def selecionar_velocidade(tecla): #ajusta a velocidade da cobra com base na tecla pressionada
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
    fim_jogo = False #indica que o jogo ainda está em andamento

    x = largura / 2 #eixo horizontal da tela; posiçao inicial da cobra no centro da tela
    y = altura / 2 #eixo vertical da tela

    velocidade_x = 0 #inicialmente a cobra nao se mexe
    velocidade_y = 0

    tamanho_cobra = 1 #define o tamanho inicial da cobra
    pixels = [] #lista que armazenará as coordenadas de todos os segmentos da cobra.

    comida_x, comida_y = gerar_comida() #gera a posição inicial da comida e a armazena nas variáveis

    while not fim_jogo: #o loop continua até que fim_jogo seja definido como True.
        tela.fill(preta) #preenche a tela com a cor pret
        for evento in pygame.event.get(): #para cada click que o usuario da; captura todos os eventos que ocorreram desde a última atualização, isso inclui cliques, pressionamentos de teclas, etc
            if evento.type == pygame.QUIT: #se o evento for o fechamento da janela (QUIT), define fim_jogo como True, encerrando o loop
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN: #apertar uma tecla
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key) #para atualizar a velocidade da cobra com base na tecla pressionada.

            #desenhar comida
            desenhar_comida(tamanho_quadrado, comida_x, comida_y) #desenha a comida na tela na posição especificada.

            #atualizar a posicao da cobra
            x = x + velocidade_x #atualiza a posição da cabeça da cobra com base na velocidade atual, a cobra se move em direção à nova posição
            y = y + velocidade_y

            #desenhar cobra
            pixels.append([x, y]) #adicionando novo pixel, adiciona a nova posição da cabeça da cobra na lista
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
            relogio.tick(velocidade_jogo) #controla a taxa de atualização do jogo

            #criar nova comida
            if x == comida_x and y == comida_y: #verifica se a cabeça da cobra colidiu com a comida
                tamanho_cobra  += 1 #aumenta o tamanho da cobra
                comida_x, comida_y = gerar_comida() #gera uma nova posição para a comida

rodar_jogo()