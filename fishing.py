import pygame
import random
import sys

pygame.init()

# =====================
# WINDOW
# =====================
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fishing Game")

BG_COLOR = (245, 245, 240)   # warna soft (cream)
TEXT_COLOR = (40, 40, 40)

font = pygame.font.SysFont("verdana", 26)
big_font = pygame.font.SysFont("verdana", 46)

clock = pygame.time.Clock()

# =====================
# DATA IKAN
# =====================
FISH_DB = {
    "Salmon": "salmon.png",
    "Shark": "shark.png",
    "Crab": "crab.png",
    "Blobfish": "blobfish.png",
    "Angler": "angler.png",
    "Manta Ray": "manta-ray.png",
    "Sawfish": "sawfish.png",
    "Goby Fish": "goby-fish.png",
    "Kraken": "kraken.png",
    "Megalodon": "megalodon.png"
}

# =====================
# LOAD GAMBAR
# =====================
start_img = pygame.image.load("fishing.png")
start_img = pygame.transform.scale(start_img, (400, 250))

fish_images = {}
for name, file in FISH_DB.items():
    img = pygame.image.load(file)
    fish_images[name] = pygame.transform.scale(img, (250, 250))

# =====================
# BUTTON
# =====================
stop_btn = pygame.Rect(650, 20, 120, 40)

def draw_button(rect, text):
    pygame.draw.rect(screen, (200, 80, 80), rect, border_radius=8)
    label = font.render(text, True, (255, 255, 255))
    screen.blit(label, label.get_rect(center=rect.center))

def draw_text(text, fnt, x, y):
    img = fnt.render(text, True, TEXT_COLOR)
    screen.blit(img, img.get_rect(center=(x, y)))

# =====================
# GAME STATE
# =====================
state = "START"
caught_fish = None
running = True

# =====================
# MAIN LOOP
# =====================
while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if state == "START" and event.key == pygame.K_RETURN:
                state = "FISHING"

            elif state == "FISHING" and event.key == pygame.K_SPACE:
                caught_fish = random.choice(list(FISH_DB.keys()))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "FISHING" and stop_btn.collidepoint(event.pos):
                state = "EXIT"

    # =====================
    # START SCREEN
    # =====================
    if state == "START":
        screen.blit(start_img, start_img.get_rect(center=(WIDTH//2, HEIGHT//2 - 40)))
        draw_text("PRESS ENTER TO START FISHING", font, WIDTH//2, HEIGHT - 100)

    # =====================
    # FISHING SCREEN
    # =====================
    elif state == "FISHING":
        draw_text("PRESS SPACE TO FISH 🎣", font, WIDTH//2, 40)
        draw_button(stop_btn, "STOP")

        if caught_fish:
            img = fish_images[caught_fish]
            screen.blit(img, img.get_rect(center=(WIDTH//2, HEIGHT//2)))
            draw_text(f"You caught: {caught_fish}", big_font, WIDTH//2, HEIGHT - 60)

    # =====================
    # EXIT SCREEN
    # =====================
    elif state == "EXIT":
        draw_text("SAMPAI JUMPA 👋", big_font, WIDTH//2, HEIGHT//2)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
