import pygame
import datetime

pygame.init()

WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Exams calendar")

FONT = pygame.font.SysFont("Arial", 18)

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
START_HOUR = 8
END_HOUR = 18

HOUR_COL_WIDTH = 60
COL_WIDTH = (WIDTH - HOUR_COL_WIDTH) // len(DAYS)
ROW_HEIGHT = HEIGHT // (END_HOUR - START_HOUR + 3)



def draw_grid():
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())


    for i, day in enumerate(DAYS):
        x = HOUR_COL_WIDTH + i * COL_WIDTH

        date = monday + datetime.timedelta(days=i)

        if date == today:
            pygame.draw.rect(screen, (80, 140, 255),
                             (x, ROW_HEIGHT, COL_WIDTH, 4))

        date_text = FONT.render(f"{date.day}.{date.month}", True, (0, 0, 0))
        screen.blit(date_text,
                    (x + COL_WIDTH//2 - date_text.get_width()//2,
                     ROW_HEIGHT + 5))

        day_text = FONT.render(day, True, (0, 0, 0))
        screen.blit(day_text,
                    (x + COL_WIDTH//2 - day_text.get_width()//2,
                     ROW_HEIGHT + 25))

        pygame.draw.rect(screen, (220, 220, 220),
                         (x, ROW_HEIGHT, COL_WIDTH, HEIGHT), 1)

    for h in range(START_HOUR, END_HOUR + 1):
        y = (h - START_HOUR) * ROW_HEIGHT + 2 * ROW_HEIGHT
        pygame.draw.line(screen, (200, 200, 200), (HOUR_COL_WIDTH, y), (WIDTH, y))
        label = FONT.render(f"{h}:00", True, (80, 80, 80))
        screen.blit(label, (5, y + 2))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    draw_grid()

    pygame.display.flip()

pygame.quit()
