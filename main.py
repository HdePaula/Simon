import pygame


pygame.init()


# setando display
screen = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Simon - by Henrique")

gameLoop = True

if __name__ == "__main__":
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

    