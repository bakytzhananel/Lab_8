import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Drawing App")
clock = pygame.time.Clock()

radius = 15
mode = 'blue'
tool = 'brush'
points = []
drawing = False
start_pos = None

while True:
    pressed = pygame.key.get_pressed()
    alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and ctrl_held:
                pygame.quit()
                exit()
            if event.key == pygame.K_F4 and alt_held:
                pygame.quit()
                exit()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_r:
                mode = 'red'
            elif event.key == pygame.K_g:
                mode = 'green'
            elif event.key == pygame.K_b:
                mode = 'blue'
            elif event.key == pygame.K_e:
                tool = 'eraser'
            elif event.key == pygame.K_t:
                tool = 'rectangle'
            elif event.key == pygame.K_o:
                tool = 'circle'
            elif event.key == pygame.K_p:
                tool = 'brush'
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if tool in ['rectangle', 'circle']:
                    start_pos = event.pos
                    drawing = True
                else:
                    radius = min(50, radius + 5)
            elif event.button == 3:
                radius = max(5, radius - 5)
        
        if event.type == pygame.MOUSEBUTTONUP:
            if tool in ['rectangle', 'circle']:
                drawing = False
                end_pos = event.pos
                if tool == 'rectangle':
                    pygame.draw.rect(screen, pygame.Color(mode), pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))
                elif tool == 'circle':
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    radius = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                    pygame.draw.circle(screen, pygame.Color(mode), center, radius)
        
        if event.type == pygame.MOUSEMOTION and tool == 'brush':
            position = event.pos
            points.append((position, mode, radius, tool))
            points = points[-256:]
    
    screen.fill((0, 0, 0))
    
    for point in points:
        pos, color, size, t = point
        if t == 'eraser':
            pygame.draw.circle(screen, (0, 0, 0), pos, size)
        else:
            pygame.draw.circle(screen, pygame.Color(color), pos, size)
    
    pygame.display.flip()
    clock.tick(60)
