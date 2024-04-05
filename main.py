import pygame
pygame.init()

win_h = 600
win_w = 800
click = 0
WHITE = (255, 255, 255)

pygame.mixer_music.load("Better Hand.mp3")
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.2)


font = pygame.font.SysFont(None, 36)
window = pygame.display.set_mode((win_w, win_h))


background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (win_w, win_h))



game = True
while game:
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    text = font.render("Clicks: " + str(click), True, WHITE)
    window.blit(text, (10, 550))    
                
    pygame.display.update()

    