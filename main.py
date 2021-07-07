from collections import OrderedDict
from blocks import *
from render import *
from conditionals import *

import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Tetris")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    run = True
    paused = False
    game_over = False
    # Create background.
    background = pygame.Surface(screen.get_size())
    bgcolor = (50, 50, 50)
    background.fill(bgcolor)
    # Draw the grid on top of the background.
    draw_grid(background)
    # This makes blitting faster.
    background = background.convert()
    
    try:
        font = pygame.font.Font("Roboto-Regular.ttf", 20)
    except OSError:
        # If the font file is not available, the default will be used.
        pass
    next_block_text = font.render("Siguiente figura:", True, (248, 165, 255), bgcolor)
    score_msg_text = font.render("Puntaje:", True, (255, 255, 255), bgcolor)
    game_over_text = font.render("¡Juego terminado!", True, (229, 13, 46),bgcolor)
    
    # Event constants.
    MOVEMENT_KEYS = 'left', 'right', 'down'
    EVENT_UPDATE_CURRENT_BLOCK = pygame.USEREVENT + 1
    EVENT_MOVE_CURRENT_BLOCK = pygame.USEREVENT + 2
    pygame.time.set_timer(EVENT_UPDATE_CURRENT_BLOCK, 1000)
    pygame.time.set_timer(EVENT_MOVE_CURRENT_BLOCK, 100)
    
    blocks = BlocksGroup()
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYUP:
                code = move( event.scancode )
                key_p = set_pause( event.scancode )
                if not paused and not game_over:
                    if code in MOVEMENT_KEYS:
                        blocks.stop_moving_current_block()
                    elif code == 'turn':
                        blocks.rotate_current_block()
                if key_p:
                    paused = not paused

            
            
            # Stop moving blocks if the game is over or paused.
            if game_over or paused:
                continue
            
            if event.type == pygame.KEYDOWN:
                code = move( event.scancode )
                if code in MOVEMENT_KEYS:
                    blocks.start_moving_current_block(code)
            
            try:
                if event.type == EVENT_UPDATE_CURRENT_BLOCK:
                    blocks.update_current_block()
                elif event.type == EVENT_MOVE_CURRENT_BLOCK:
                    blocks.move_current_block()
            except TopReached:
                game_over = True
        
        # Draw background and grid.
        screen.blit(background, (0, 0))
        # Blocks.
        blocks.draw(screen)
        # Sidebar with misc. information.
        draw_centered_surface(screen, next_block_text, 50)
        draw_centered_surface(screen, blocks.next_block.image, 100)
        draw_centered_surface(screen, score_msg_text, 240)
        score_text = font.render(
            str(blocks.score), True, (255, 255, 255), bgcolor)
        draw_centered_surface(screen, score_text, 270)

        if game_over:
            draw_centered_surface(screen, game_over_text, 360)

        
        text_score, color_score = score_message(blocks.score)
        if text_score is not None:
          text_score_format = font.render(text_score, True, (color_score[0], color_score[1], color_score[2]), bgcolor)
          draw_centered_surface(screen, text_score_format, 300)

        # Update.
        pygame.display.flip()
    
    pygame.quit()


if __name__ == "__main__":
    main()
