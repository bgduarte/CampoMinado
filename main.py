


import pygame
 
class CampoMinadoApp:
    def __init__(self):
        self.__running = True
        self.__screen = None
        self.size = self.weight, self.height = 640, 400
 
    def on_init(self):
        pygame.init()
        print('Init')
        self.__screen = pygame.display.set_mode(self.size)
        self.__running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.__running = False
    def on_loop(self):
        pass
    def on_render(self):
        red = (255, 0, 0) #Remover mais tarde: Apenas para teste
        self.__screen.fill(red) #Remover mais tarde: Apenas para teste
        #Chamadas das funções de renderização

        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self.__running = False
 
        while( self.__running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = CampoMinadoApp()
    theApp.on_execute()