import pygame
import sys
import tkinter as tk
from tkinter import filedialog

# constantes
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
MURO = 1
ROBOT = 2
META = 9
COLOR_MURO = (0, 0, 0)
COLOR_BOT = (0, 0, 255)
COLOR_META = (0, 255, 0)
COLOR_LIT = (255, 255, 0)
COLOR_VACIO = (255, 255, 255)

class Game:
    """ Representación del juego como tal """
    def __init__(self):
        self.levels = ['level1.txt', 'level2.txt', 'level3.txt'] 
        self.dir_levels = "levels/"
        self.current_level_index = 0
        self.board = None  
        self.load_level(self.current_level_index) 

    def load_level(self, level_index):
        """Carga el nivel especificado por level_index. return true si existe el nivel"""
        if level_index < len(self.levels):
            self.board = Board(self.dir_levels + self.levels[level_index])
            self.current_level_index = level_index
            return True
        else:
            return False

    def next_level(self):
        """Avanza al siguiente nivel si es posible."""
        if self.board.check_status():
            return self.load_level(self.current_level_index + 1)
        return False

class Cell:
    
    def __init__(self, z=0, lit=False): 
        self.z = z
        self.lit = lit

    def __repr__(self):
        if self.z == MURO:  
            return 'M'
        elif self.z == ROBOT:  
            return 'B'
        elif self.z == META and not self.lit:  
            return 'G'
        elif self.lit:  
            return 'L'
        else:  
            return ' '

    def toggle_lit(self):
        if self.z == META:
            self.lit = not self.lit

class Board:

    def __init__(self, filename: str):
        """lee un archivo .txt que contiene el mapa y lo guarda como un objeto Board"""
        with open(filename) as f:
            header = f.readline().strip()
            (self.width, self.height) = map(int, header.split())
            self.cells = [[Cell() for _ in range(self.width)] for _ in range(self.height)]
            for x, line in enumerate(f.read().splitlines()):
                for y, curr_cell in enumerate(map(int, line.split())):
                    self.cells[x][y] = Cell(curr_cell)
                    if curr_cell == 2:                  # Posición inicial del bot
                        self.bot_x, self.bot_y = x, y
                        self.cells[x][y].z = 0          # Marcamos la posición inicial como espacio vacío
            self.directions = ['N', 'E', 'S', 'O']      # Posibles direcciones
            self.bot_direction = 0                      # Inicia mirando hacia el norte

    def execute_actions(self, actions_filename: str, screen, update_screen_func, status_message):
        """lee y ejecuta acciones de un archivo .txt """
        with open(actions_filename) as f:
            for line in f:
                action = line.strip()
                if action == "Move forward":
                    self.move()
                elif action == "Turn left":
                    self.turn_left()
                elif action == "Turn right":
                    self.turn_right()
                elif action == "Light up the tile":
                    self.cells[self.bot_x][self.bot_y].toggle_lit()

                update_screen_func(screen, self, status_message)
                pygame.time.wait(500)

    def check_status(self):
        """ comprueba si cada casilla meta está iluminada"""
        for x in range(self.height):
            for y in range(self.width):
                if self.cells[x][y].z == META and self.cells[x][y].lit == False:
                    return False
        return True

    def move(self):
        """mueve el robot a la dirección que mira si la casilla está vacía"""
        dx, dy = 0, 0
        if self.directions[self.bot_direction] == 'N':
            dx = -1
        elif self.directions[self.bot_direction] == 'S':
            dx = 1
        elif self.directions[self.bot_direction] == 'E':
            dy = 1
        elif self.directions[self.bot_direction] == 'O':
            dy = -1

        new_x, new_y = self.bot_x + dx, self.bot_y + dy
        # Verificamos si la nueva posición es un espacio vacío y está dentro del tablero
        if 0 <= new_x < self.height and 0 <= new_y < self.width: 
            if self.cells[new_x][new_y].z == 0 or self.cells[new_x][new_y].z == META:
                self.bot_x, self.bot_y = new_x, new_y

    def turn_left(self):
        self.bot_direction = (self.bot_direction - 1) % 4

    def turn_right(self):
        self.bot_direction = (self.bot_direction + 1) % 4

    def draw(self, screen):
        cell_size = 100
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                if self.cells[y][x].z == MURO: 
                    pygame.draw.rect(screen, COLOR_MURO, rect) 
                elif self.cells[y][x].lit:  
                    pygame.draw.rect(screen, COLOR_LIT, rect)  
                elif self.cells[y][x].z == META: 
                    pygame.draw.rect(screen, COLOR_META, rect)  
                else:  # Espacio vacío
                    pygame.draw.rect(screen, COLOR_VACIO, rect)  
                if self.bot_x == y and self.bot_y == x:
                    pygame.draw.circle(screen, COLOR_BOT, (x * cell_size + cell_size//2, y * cell_size + cell_size//2), cell_size//2)


def open_file_dialog():
    """ permite al usuario ingresar sus instrucciones por medio de un botón """
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


def draw_button(screen, button_text, button_position, button_size):
    """ Muestra el botón en el cual se pide las acciones del jugador """
    font = pygame.font.Font(None, 36)
    text = font.render(button_text, True, (255, 255, 255))
    button_rect = pygame.Rect(button_position, button_size)
    pygame.draw.rect(screen, (0, 0, 255), button_rect) 
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    return button_rect

def draw_status_message(screen, message, position, size):
    """ Muestra el estado actual del juego """
    font = pygame.font.Font(None, size)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect)

def show_transition_message(screen, message, wait_time=2000):
    """Muestra un mensaje de transición durante un tiempo determinado."""
    screen.fill((0, 0, 0))
    draw_status_message(screen, message, (screen.get_width() // 2, screen.get_height() // 2), 48)
    pygame.display.flip()
    pygame.time.wait(wait_time)

def update_screen(screen, board, status_message = ""):
    """ función auxiliar que nos permite actualizar pantalla  """
    screen.fill((50, 50, 50))
    board.draw(screen) 
    draw_status_message(screen, status_message, (SCREEN_WIDTH - 250, SCREEN_HIGHT - 25), 36)
    load_button_rect = draw_button(screen, "Cargar Instrucciones", (0, SCREEN_HIGHT - 50), (300, 50))
    reset_button_rect = draw_button(screen, "Reiniciar Nivel", (0, SCREEN_HIGHT - 100), (200, 50)) 
    pygame.display.flip() 

if __name__ == '__main__':
    pygame.init()
    screen_size = (SCREEN_WIDTH, SCREEN_HIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Lightbot")
    
    game = Game()
    status_message = "Aún no ha pasado nada"
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if reset_button_rect.collidepoint(mouse_pos):
                    game.load_level(game.current_level_index)
                    status_message = "Nivel reiniciado"

                if load_button_rect.collidepoint(mouse_pos):
                    actions_file_path = open_file_dialog()
                    if actions_file_path:
                        game.board.execute_actions(actions_file_path, screen, update_screen, status_message)
                        if game.board.check_status():
                            status_message = "Objetivo Completado"
                            if game.next_level():
                                show_transition_message(screen, "Nivel completado. Cargando siguiente nivel...")
                                status_message = ""
                            else:
                                status_message = "¡Felicidades! Juego terminado."
                        else:
                            status_message = "Quedaron casillas metas sin encender"

        load_button_rect = draw_button(screen, "Cargar Instrucciones", (0, SCREEN_HIGHT - 50), (300, 50))
        reset_button_rect = draw_button(screen, "Reiniciar Nivel", (0, SCREEN_HIGHT - 100), (200, 50))
        update_screen(screen, game.board, status_message)

    pygame.quit()