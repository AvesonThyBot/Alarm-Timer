spacing = "------"
CLEAR = "\033[2J" #clears the terminal
CLEAR_RETURN = "\033[H" #clears the terminal and starts from same line
alarm_sound = "alarm.mp3" #global variable for sound

# -------------------- Importing modules --------------------
try:
    import time 
    from playsound import playsound
    import pygame
except FileNotFoundError:
    print("Importion Error : Essential files not found.")
    print("Program shutting down.")
    time.sleep(1)
    exit()
except ModuleNotFoundError:
    print("Importion Error: Essential modules not found.")
    print("Program shutting down.")
    time.sleep(1)
    exit()
except Exception as e:
    print(f"An unknown error occurred: {str(e)}")
    print("Program shutting down.")
    time.sleep(1)
    exit()
# -------------------- End of Importing modules -------------

# -------------------- Main code ------------------------

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set window size
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200

# Set button size
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_SPACING = 20

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Timer")

# Load font
font = pygame.font.Font(None, 40)

# Initialize variables
start_time = None
elapsed_time = 0
is_running = False

# Function to format time as HH:MM:SS
def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

# Function to draw text on the window
def draw_text(text, x, y, color):
    rendered_text = font.render(text, True, color)
    text_rect = rendered_text.get_rect(center=(x, y))
    window.blit(rendered_text, text_rect)

# Function to handle button click events
def handle_start_click():
    global start_time, is_running
    if not is_running:
        start_time = time.time() - elapsed_time
        is_running = True

def handle_stop_click():
    global is_running
    if is_running:
        is_running = False

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                start_button_rect = pygame.Rect(BUTTON_SPACING, WINDOW_HEIGHT - BUTTON_HEIGHT - BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT)
                stop_button_rect = pygame.Rect(WINDOW_WIDTH - BUTTON_WIDTH - BUTTON_SPACING, WINDOW_HEIGHT - BUTTON_HEIGHT - BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT)
                if start_button_rect.collidepoint(event.pos):
                    handle_start_click()
                elif stop_button_rect.collidepoint(event.pos):
                    handle_stop_click()

    # Fill the window with black color
    window.fill(BLACK)

    # Update the elapsed time if stopwatch is running
    if is_running:
        elapsed_time = time.time() - start_time

    # Draw the timer
    draw_text(format_time(elapsed_time), WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, WHITE)

    # Draw the start button
    start_button_color = GRAY if is_running else WHITE
    pygame.draw.rect(window, start_button_color, (BUTTON_SPACING, WINDOW_HEIGHT - BUTTON_HEIGHT - BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT))
    draw_text("Start", BUTTON_SPACING + BUTTON_WIDTH // 2, WINDOW_HEIGHT - BUTTON_HEIGHT // 2 - BUTTON_SPACING, BLACK)

    # Draw the stop button
    stop_button_color = WHITE if is_running else GRAY
    pygame.draw.rect(window, stop_button_color, (WINDOW_WIDTH - BUTTON_WIDTH - BUTTON_SPACING, WINDOW_HEIGHT - BUTTON_HEIGHT - BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT))
    draw_text("Stop", WINDOW_WIDTH - BUTTON_WIDTH // 2 - BUTTON_SPACING, WINDOW_HEIGHT - BUTTON_HEIGHT // 2 - BUTTON_SPACING, BLACK)

    # Update the display
    pygame.display.update()

# Quit the program
pygame.quit()
# -------------------- End of Main code ---------------------
