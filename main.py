import pygame

pygame.init()

width=600
height =600

size_window = (width, height)
window = pygame.display.set_mode(size_window)
pygame.display.set_caption('Valentine')
heart_img = (pygame.image.load("heart_smaller.png"),pygame.image.load("heart_bigger (1).png"))
text = "I LOVE YOU!"
text2 = "HAPPY VALENTINE`S DAY"
font=pygame.font.SysFont("verdana",30)

text_image = font.render(text, True, pygame.Color("white"))
text_image2 = font.render(text2, True, pygame.Color("white"))

x = width // 2
y = height // 2

clock = pygame.time.Clock()
image_index = 0
run=True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill("black")
    window.blit(heart_img[image_index], (width//2, width//2))

    image_index += 1
    if image_index>1:
        image_index=0

    if pygame.mouse.get_pressed()[0]==1:
        print("Click")
    clock.tick(2)

    window.blit(text_image, (x, y))
    window.blit(text_image2, (35, 100))
    pygame.display.update()


pygame.quit()