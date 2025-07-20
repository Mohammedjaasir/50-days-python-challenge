import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")
clock = pygame.time.Clock()

# Ball properties
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_radius = 20
ball_speed_x = 5
ball_speed_y = 4

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Bounce off walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_speed_y = -ball_speed_y
    
    # Keep ball within bounds (in case it goes slightly out)
    ball_x = max(ball_radius, min(WIDTH - ball_radius, ball_x))
    ball_y = max(ball_radius, min(HEIGHT - ball_radius, ball_y))
    
    # Draw everything
    screen.fill(BLACK)  # Clear screen with black
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)
    
    # Add some text
    font = pygame.font.Font(None, 36)
    text = font.render("Press ESC to quit", True, WHITE)
    screen.blit(text, (10, 10))
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit
pygame.quit()
sys.exit()

