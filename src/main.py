
import pygame
import sys
from game import Game
class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('CHESS')
        self.game = Game()

    def mainloop(self):
        game = self.game
        screen = self.screen
        while True:
            game.show_bg(screen)
            game.show_pieces(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.mainloop()