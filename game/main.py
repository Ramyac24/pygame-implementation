# game/main.py
import pygame
import requests
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Escape the AI Lab")
font = pygame.font.SysFont(None, 36)

SERVER_URL = "http://localhost:5000"

def register_player(username):
    url = f"{SERVER_URL}/player/register"
    response = requests.post(url, json={"username": username})
    return response.json()

def get_player(username):
    url = f"{SERVER_URL}/player/{username}"
    response = requests.get(url)
    return response.json()

def get_puzzle(level):
    url = f"{SERVER_URL}/puzzle/{level}"
    response = requests.get(url)
    return response.json()

def get_clue(username, level, puzzle):
    url = f"{SERVER_URL}/clue"
    response = requests.post(url, json={"username": username, "level": level, "puzzle": puzzle})
    return response.json()["clue"]

def update_progress(username, solved):
    url = f"{SERVER_URL}/player/{username}/progress"
    response = requests.post(url, json={"solved": solved})
    return response.json()

def main():
    clock = pygame.time.Clock()
    username = input("Enter your player name: ").strip()
    
    # Register the player (or get error if already exists)
    reg = register_player(username)
    print(reg)
    
    player_data = get_player(username)
    current_level = player_data.get("current_level", 1)
    
    running = True
    # Get the puzzle and clue for the current level.
    puzzle_data = get_puzzle(current_level)
    if "puzzle" not in puzzle_data:
        print("No puzzle found for level", current_level)
        sys.exit(0)
    puzzle = puzzle_data["puzzle"]
    clue = get_clue(username, current_level, puzzle)

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Simulate puzzle solution by pressing SPACE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Update progress for the current player and level
                    update_progress(username, puzzle)
                    current_level += 1
                    puzzle_data = get_puzzle(current_level)
                    if "puzzle" in puzzle_data:
                        puzzle = puzzle_data["puzzle"]
                        clue = get_clue(username, current_level, puzzle)
                    else:
                        puzzle = "Congratulations! You have escaped the lab!"
                        clue = ""

        # Render puzzle and clue on the screen.
        puzzle_text = font.render(f"Level {current_level}: {puzzle}", True, (0, 255, 0))
        screen.blit(puzzle_text, (20, 100))
        if clue:
            clue_text = font.render(f"Clue: {clue}", True, (255, 255, 0))
            screen.blit(clue_text, (20, 150))

        instructions = font.render("Press SPACE when you solve the puzzle", True, (200, 200, 200))
        screen.blit(instructions, (20, 300))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

