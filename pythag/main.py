import pygame, random

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Score High Pythagorised")

dark_grey = (25, 25, 25)
white = (200, 200, 200)
black = (0, 0, 0)
screen.fill(dark_grey)


card_width = (screen_width - 100) // 5
card_height = 50

card_margin = 10
num_cards_to_display = 25

cards = []
card_values = [1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 10, 10, 25, 50, 100, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 10, 10, 25, 50, 100, 1000]
all_card_values = card_values * 3
random.shuffle(all_card_values)
all_card_values = all_card_values[:num_cards_to_display]
stage = 0
selected_cards = []
base_value = 0
height_value = 0

for i in range(num_cards_to_display):
    x = 10 + (card_width + card_margin) * (i % 5) #max 5 cards per row
    y = 80 + (card_height + card_margin) * (i // 5) #5
    card_rect = pygame.Rect(x, y, card_width, card_height) 
    cards.append({"rect": card_rect, "value": all_card_values[i], "hidden": True})

font = pygame.font.Font(None, 28)
base_score = 0
height_score = 0


# Instructions setup
instructions_text = [
    "Score High Pythagorised!",
    "Stage 1: Select 10 cards for the base.",
    "Stage 2: Select 10 cards for the height.",
    "Stage 3: Calculate the hypotenuse.",
    "",
    "Click the 'Close' button to start."
]
instructions_font = pygame.font.Font(None, 25)

instructions_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
instructions_surface.fill((0, 0, 0, 180))  # Semi-transparent black background
close_button_rect = pygame.Rect(screen_width // 2 - 50, screen_height - 120, 100, 40)
close_button_color = (100, 100, 100)
show_instructions = True

final_score = 0
show_final_score = False
reset_button_rect = pygame.Rect(screen_width // 2 - 75, screen_height - 80, 150, 40)

def draw_cards():
    for card in cards:
        if card["hidden"]:
            pygame.draw.rect(screen, white, card["rect"])
        else:
            pygame.draw.rect(screen, black, card["rect"])
            text = font.render(str(card["value"]), True, white)
            text_rect = text.get_rect(center=card["rect"].center)

            screen.blit(text, text_rect)

def update_score_and_cards_left():
    global base_score, height_score, cards_left
    base_score_text = font.render(f"Base Score: {base_score}", True, white)
    height_score_text = font.render(f"Height Score: {height_score}", True, white)
    screen.blit(base_score_text, (10, 10))    
    screen.blit(height_score_text, (10, 40))
    if stage == 3:
        base_text = font.render(f"Base: {base_value}", True, white)        
        screen.blit(base_text, (10, 70))        
        height_text = font.render(f"Height: {height_value}", True, white)
        screen.blit(height_text, (150, 70))
def draw_instructions():
    y_offset = 80
    for line in instructions_text:
        text = instructions_font.render(line, True, white)
        text_rect = text.get_rect(center=(screen_width // 2, y_offset))
        instructions_surface.blit(text, text_rect)
        y_offset += 30

    pygame.draw.rect(instructions_surface, close_button_color, close_button_rect)
    close_text = instructions_font.render("Close", True, white)
    close_text_rect = close_text.get_rect(center=close_button_rect.center)
    instructions_surface.blit(close_text, close_text_rect)

    screen.blit(instructions_surface, (0, 0))

def display_final_score():
    global final_score
    final_score_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    final_score_surface.fill((0, 0, 0, 180))    
    final_score_text = font.render(f"Final Score: {final_score:.2f}", True, white)
    final_score_rect = final_score_text.get_rect(center=(screen_width // 2, screen_height // 2))
    final_score_surface.blit(final_score_text, final_score_rect)
    pygame.draw.rect(final_score_surface, close_button_color, reset_button_rect)
    reset_text = instructions_font.render("Play Again", True, white)
    reset_text_rect = reset_text.get_rect(center=reset_button_rect.center)
    final_score_surface.blit(reset_text, reset_text_rect)
    screen.blit(final_score_surface, (0, 0))
    


def reset_cards():
    for card in cards:
        card["hidden"] = True

def reset_game():
    global stage, base_score, height_score, selected_cards, final_score, all_card_values, base_value, height_value
    stage = 1
    base_score = 0
    height_score = 0
    selected_cards = []
    final_score = 0
    reset_cards()
    show_final_score = False
    show_instructions = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if show_instructions:
                    if close_button_rect.collidepoint(mouse_pos):
                        show_instructions = False
                        stage = 1

                else:
                    if stage == 1:
                        if len(selected_cards) < 10:
                            for card in cards:
                                if card["rect"].collidepoint(mouse_pos) and card["hidden"]:
                                    if card not in selected_cards:
                                        selected_cards.append(card)
                                        card["hidden"] = False
                                        base_score += card["value"]                                        
                                        base_value = base_score                                        
                        else:
                            print("You can only select 10 cards")
                        if len(selected_cards) == 10:
                            stage = 2
                            all_card_values = card_values * 3
                            random.shuffle(all_card_values)
                            all_card_values = all_card_values[:num_cards_to_display]
                            for i, card in enumerate(cards):
                                card["value"] = all_card_values[i]

                            selected_cards = []
                            reset_cards()
                            print("Stage 2: Select 10 more cards to add to height.")
                    elif stage == 2:                        
                        if len(selected_cards) < 10:
                            for card in cards:
                                if card["rect"].collidepoint(mouse_pos) and card["hidden"]:
                                    if card not in selected_cards:
                                        selected_cards.append(card)
                                        card["hidden"] = False
                                        height_score += card["value"]
                                        height_value = height_score
                        else:
                            print("You can only select 10 cards")
                        if len(selected_cards) == 10:
                            stage = 3
                            print(f"Stage 3: Base: {base_value}, Height: {height_value}")
                            final_score = (base_value**2 + height_value**2)**0.5                            
                            show_final_score = True
                            



    screen.fill(dark_grey)
    
    if show_instructions:
        draw_instructions()
    else:
        draw_cards()
    update_score_and_cards_left()
    
    if show_final_score:
        display_final_score()        
        if reset_button_rect.collidepoint(mouse_pos):
            reset_game()
            show_final_score = False
            
    pygame.display.flip()
    


main()

