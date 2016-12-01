import pygame
import sys

global efecto
global efecto2

ancho=800
alto=600

blanco=[255,255,255]
negro=[0,0,0]
rojo=[255,0,0]

efecto=True
efecto2=True

class Opcion:
    ver=False

    def __init__(self,ido,texto,pos,tam):
        self.texto=texto
        self.id=ido
        self.pos=pos
        self.fuente=pygame.font.Font(None,tam)
        self.set_rect()
        self.dibujar()




    def set_rect(self):
        self.enunciado()
        self.rect=self.txt.get_rect()
        self.rect.topleft=self.pos

    def colortxt(self):
        if self.ver:
            return(blanco)
        else:
            return(negro)


    def enunciado(self):
        self.txt=fuente.render(self.texto,True,self.colortxt())

    def dibujar(self):
        self.enunciado()
        pantalla.blit(self.txt,self.rect)

class Opcion2:
    ver=False

    def __init__(self,ido,texto,pos,tam):
        self.texto=texto
        self.id=ido
        self.pos=pos
        self.fuente=pygame.font.Font(None,tam)
        self.set_rect()
        self.dibujar()

    def set_rect(self):
        self.enunciado()
        self.rect=self.txt.get_rect()
        self.rect.topleft=self.pos

    def colortxt(self):
        if self.ver:
            return(negro)
        else:
            return(rojo)

    def enunciado(self):
        self.txt=fuente.render(self.texto,True,self.colortxt())

    def dibujar(self):
        self.enunciado()
        pantalla.blit(self.txt,self.rect)

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    pygame.display.set_caption("Soul Memory")

    fuente=pygame.font.Font("opciones.ttf",50)
    fuente2=pygame.font.Font(None,40)
    fuenteTitulo=pygame.font.Font("soulMemory.ttf",80)

    fondo=pygame.image.load("fondo.jpg")




    #-------------MENU---------------------------------------#

    pygame.mixer.music.load("musicaMenu.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.85)




    opciones=[Opcion(1,"Iniciar",(ancho/2-60,alto/20+220),50)]
    opciones2=[Opcion(2,"Salir",(ancho/2-40,alto/20+290),50)]


    Starting=fuente2.render("Has iniciado el juego...",True,blanco)
    titulo=fuenteTitulo.render("Soul Memory",True,negro)



    reloj=pygame.time.Clock()

    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for op in opciones:
                    if op.rect.collidepoint(pygame.mouse.get_pos()):
                        print "Starting",op.id
                        fin = False
                        while not fin:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    fin = True
                                    exit()

                            pantalla.fill(negro)
                            pantalla.blit(Starting,(ancho/2-150,alto/2))

                            pygame.display.flip()
                for op in opciones2:
                    if op.rect.collidepoint(pygame.mouse.get_pos()):
                        print op.id
                        fin=True


        pantalla.blit(fondo,(0,0))
        pantalla.blit(titulo,(ancho/2-235,alto/2-230))

        for op in opciones:
            if op.rect.collidepoint(pygame.mouse.get_pos()):
                op.ver=True

                while efecto==True:
                    sonido=pygame.mixer.Sound("mouse.wav")
                    sonido.play()
                    efecto=False

            else:
                op.ver=False
                efecto=True

            op.dibujar()

        for op in opciones2:
            if op.rect.collidepoint(pygame.mouse.get_pos()):
                op.ver=True

                while efecto2==True:
                    sonido=pygame.mixer.Sound("mouse.wav")
                    sonido.play()
                    efecto2=False

            else:
                op.ver=False
                efecto2=True

            op.dibujar()


        reloj.tick(60)
        pygame.display.flip()
