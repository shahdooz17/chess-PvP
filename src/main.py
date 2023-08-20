from constant import *
import pygame
import sys
from game import Game
from square import Square
class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('CHESS')
        self.game = Game()

    def mainloop(self):
        game = self.game
        screen = self.screen
        dragger = self.game.dragger
        board = self.game.board
        while True:
            game.show_bg(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blitt(screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY//SQ_SIZE
                    clicked_col = dragger.mouseX // SQ_SIZE

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        dragger.update_blitt(screen)
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.mainloop()