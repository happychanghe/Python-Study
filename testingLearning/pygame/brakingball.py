import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breaking Wall Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRICK_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

# Set up the paddle
paddle_width = 100
paddle_height = 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 10
paddle_speed = 10

# Set up the ball
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = random.choice([-3, -2, 2, 3])
ball_speed_y = -10
ball = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)

# Set up the bricks
brick_width = 80
brick_height = 20
brick_rows = 5
brick_margin = 5
brick_cols = WIDTH // (brick_width + brick_margin)
bricks = []
for row in range(brick_rows):
    brick_row = []
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_margin) + brick_margin
        brick_y = row * (brick_height + brick_margin) + brick_margin
        brick_color = random.choice(BRICK_COLORS)
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        brick_row.append((brick_rect, brick_color))
    bricks.append(brick_row)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Set the frame rate

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check for collision with the paddle
    if ball.colliderect(pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)):
        ball_speed_y = -ball_speed_y

    # Check for collision with the bricks
    for row in bricks:
        for brick in row:
            brick_rect, brick_color = brick
            if ball.colliderect(brick_rect):
                row.remove(brick)
                ball_speed_y = -ball_speed_y
                break

    # Check for collision with the walls
    if ball.x <= 0 or ball.x >= WIDTH - ball_radius * 2:
        ball_speed_x = -ball_speed_x
    if ball.y <= 0:
        ball_speed_y = -ball_speed_y

    # Draw the game objects
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(window, WHITE, (ball.x + ball_radius, ball.y + ball_radius), ball_radius)
    for row in bricks:
        for brick in row:
            brick_rect, brick_color = brick
            pygame.draw.rect(window, brick_color, brick_rect)

    pygame.display.update()

# Quit the game
pygame.quit()
