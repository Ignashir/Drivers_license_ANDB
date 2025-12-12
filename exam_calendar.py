import pygame
import datetime
<<<<<<< HEAD
=======
from zoneinfo import ZoneInfo
>>>>>>> 277ca55 (Changes)

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

week_offset = 0
LEFT_BTN = pygame.Rect(10, 10, 40, 30)
RIGHT_BTN = pygame.Rect(60, 10, 40, 30)
RES_BTN = pygame.Rect(120, 10, 130, 30)

click_processed = False

# ==========================================
# NEW: RESERVATIONS LIST
# ==========================================
reservations = []   # each reservation: {date: datetime.date, time: datetime.time, label: str}

# ==========================================
# FORM DATA
# ==========================================
show_form = False
active_field = None

form_fields = {
    "Date": "",      # Format: YYYY-MM-DD
    "Time": "",      # Format: HH:MM
    "Name": "",
    "Surname": "",
    "Birthday": "",
    "ID": "",
    "Category": "",
}

form_rects = {}
start_y = 150
for i, key in enumerate(form_fields.keys()):
    form_rects[key] = pygame.Rect(WIDTH//2 - 150, start_y + i*50, 300, 30)

submit_btn = pygame.Rect(WIDTH//2 - 70, start_y + len(form_fields)*50 + 20, 140, 35)


# ==========================================
# BUTTON DRAWING
# ==========================================
def draw_buttons():
    pygame.draw.rect(screen, (230, 230, 230), LEFT_BTN)
    pygame.draw.rect(screen, (230, 230, 230), RIGHT_BTN)
    pygame.draw.rect(screen, (230, 230, 230), RES_BTN)

    pygame.draw.rect(screen, (100, 100, 100), LEFT_BTN, 2)
    pygame.draw.rect(screen, (100, 100, 100), RIGHT_BTN, 2)
    pygame.draw.rect(screen, (100, 100, 100), RES_BTN, 2)

    screen.blit(FONT.render("<", True, (0, 0, 0)), (LEFT_BTN.x + 12, LEFT_BTN.y + 5))
    screen.blit(FONT.render(">", True, (0, 0, 0)), (RIGHT_BTN.x + 12, RIGHT_BTN.y + 5))
    screen.blit(FONT.render("Reservation", True, (0, 0, 0)), (RES_BTN.x + 10, RES_BTN.y + 5))


# ==========================================
# DRAW RESERVATION BLOCKS IN GRID
# ==========================================
def draw_reservations(monday):
    for r in reservations:
        date = r["date"]
        time = r["time"]
        label = r["label"]

        # Only draw if inside current week
        if monday <= date <= monday + datetime.timedelta(days=6):
            day_index = (date - monday).days

            # Find position
            hour = time.hour
            if hour < START_HOUR or hour > END_HOUR:
                continue

            x = HOUR_COL_WIDTH + day_index * COL_WIDTH + 3
            y = (hour - START_HOUR) * ROW_HEIGHT + 2 * ROW_HEIGHT + 3

            # Draw block
            pygame.draw.rect(screen, (150, 200, 255), (x, y, COL_WIDTH - 6, ROW_HEIGHT - 6))
            pygame.draw.rect(screen, (0, 0, 120), (x, y, COL_WIDTH - 6, ROW_HEIGHT - 6), 2)

            # Text
            txt = FONT.render(label, True, (0, 0, 0))
            screen.blit(txt, (x + 5, y + 5))


# ==========================================
# GRID DRAWING
# ==========================================
def draw_grid():
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday()) + datetime.timedelta(weeks=week_offset)
<<<<<<< HEAD
=======
    current_hour_pl = datetime.datetime.now(ZoneInfo("Europe/Warsaw")).hour
>>>>>>> 277ca55 (Changes)

    # Days header
    for i, day in enumerate(DAYS):
        x = HOUR_COL_WIDTH + i * COL_WIDTH
        date = monday + datetime.timedelta(days=i)

        if date == today:
            pygame.draw.rect(screen, (80, 140, 255), (x, ROW_HEIGHT, COL_WIDTH, 4))

<<<<<<< HEAD
=======
            y = (current_hour_pl - START_HOUR) * ROW_HEIGHT + 2 * ROW_HEIGHT
            pygame.draw.rect(screen, (80, 140, 255), (x, y, COL_WIDTH, ROW_HEIGHT))
            now_text = FONT.render("NOW", True, (0, 0, 0))
            screen.blit(now_text, (x + COL_WIDTH//2 - now_text.get_width()//2,
                        y + ROW_HEIGHT//2 - now_text.get_height()//2))
        
        if date == exam_date:
            y = (exam_hour - START_HOUR) * ROW_HEIGHT + 2 * ROW_HEIGHT
            pygame.draw.rect(screen, (255, 0, 0), (x, y, COL_WIDTH, ROW_HEIGHT))
            exam_text = FONT.render("EXAM", True, (0, 0, 0))
            screen.blit(exam_text, (x + COL_WIDTH//2 - exam_text.get_width()//2,
                        y + ROW_HEIGHT//2 - exam_text.get_height()//2))

>>>>>>> 277ca55 (Changes)
        screen.blit(FONT.render(f"{date.day}.{date.month}", True, (0, 0, 0)),
                    (x + COL_WIDTH//2 - 20, ROW_HEIGHT + 5))
        screen.blit(FONT.render(day, True, (0, 0, 0)),
                    (x + COL_WIDTH//2 - 20, ROW_HEIGHT + 25))

        pygame.draw.rect(screen, (220, 220, 220), (x, ROW_HEIGHT, COL_WIDTH, HEIGHT), 1)

    # Hour lines
    for h in range(START_HOUR, END_HOUR + 1):
        y = (h - START_HOUR) * ROW_HEIGHT + 2 * ROW_HEIGHT
        pygame.draw.line(screen, (200, 200, 200), (HOUR_COL_WIDTH, y), (WIDTH, y))
        screen.blit(FONT.render(f"{h}:00", True, (80, 80, 80)), (5, y + 2))

    # Draw reservations on top
    draw_reservations(monday)

<<<<<<< HEAD
=======
DATE_BTN = pygame.Rect(WIDTH - 200, 10, 180, 30)

# REZERWACJE EGZAMINU (jak na razie do testu, ktos inny implementuje sama rezerwacje)
exam_date = datetime.date(2025, 12, 12)
exam_hour = 15

def add_todays_date():
    pygame.draw.rect(screen, (230, 230, 230), DATE_BTN)

    date_text = FONT.render("Today's date: " + datetime.date.today().strftime('%Y-%m-%d'), True, (0, 0, 0))

    screen.blit(date_text, (DATE_BTN.x + 12, DATE_BTN.y + 5))

>>>>>>> 277ca55 (Changes)

# ==========================================
# FORM DRAWING
# ==========================================
def draw_form():
    pygame.draw.rect(screen, (240, 240, 240), (WIDTH//2 - 200, 100, 400, 500))
    pygame.draw.rect(screen, (0, 0, 0), (WIDTH//2 - 200, 100, 400, 500), 3)

    screen.blit(FONT.render("Reservation Form", True, (0, 0, 0)),
                (WIDTH//2 - 90, 110))

    for key, rect in form_rects.items():
        pygame.draw.rect(screen, (255, 255, 255), rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)

        screen.blit(FONT.render(key + ":", True, (0, 0, 0)),
                    (rect.x, rect.y - 22))
        screen.blit(FONT.render(form_fields[key], True, (0, 0, 0)),
                    (rect.x + 5, rect.y + 5))

    pygame.draw.rect(screen, (200, 255, 200), submit_btn)
    pygame.draw.rect(screen, (0, 100, 0), submit_btn, 2)
    screen.blit(FONT.render("Submit", True, (0, 0, 0)),
                (submit_btn.x + 30, submit_btn.y + 7))


# ==========================================
# MAIN LOOP
# ==========================================
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ================================
        # OPEN FORM
        # ================================
        if not show_form:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                # --- FIX: Handle week switching again ---
                if LEFT_BTN.collidepoint(event.pos):
                    week_offset -= 1

                if RIGHT_BTN.collidepoint(event.pos):
                    week_offset += 1

                # --- Open reservation form ---
                if RES_BTN.collidepoint(event.pos):
                    show_form = True

        # ================================
        # FORM INPUT LOGIC
        # ================================
        if show_form:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                show_form = False
                active_field = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                active_field = None
                for key, rect in form_rects.items():
                    if rect.collidepoint(event.pos):
                        active_field = key

                # ========== SUBMIT PRESSED ==========
                if submit_btn.collidepoint(event.pos):
                    try:
                        r_date = datetime.datetime.strptime(form_fields["Date"], "%Y-%m-%d").date()
                        r_time = datetime.datetime.strptime(form_fields["Time"], "%H:%M").time()

                        label = f"{form_fields['Name']} {form_fields['Surname']} ({form_fields['Category']})"
                        reservations.append({
                            "date": r_date,
                            "time": r_time,
                            "label": label
                        })
                        print("Reservation added:", reservations[-1])

                    except Exception as e:
                        print("Invalid date/time format:", e)

                    show_form = False
                    active_field = None

            # Typing
            if event.type == pygame.KEYDOWN and active_field:
                if event.key == pygame.K_BACKSPACE:
                    form_fields[active_field] = form_fields[active_field][:-1]
                elif len(form_fields[active_field]) < 30:
                    form_fields[active_field] += event.unicode

    # DRAW
    screen.fill((255, 255, 255))
    draw_buttons()
<<<<<<< HEAD
=======
    add_todays_date()
>>>>>>> 277ca55 (Changes)
    draw_grid()

    if show_form:
        draw_form()

    pygame.display.flip()

pygame.quit()
