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

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    file_path = filedialog.askopenfilename()  # Abre el diálogo para seleccionar un archivo
    return file_path

class Cell:
    
    def __init__(self, z=0, active=False, lit=False): 
        self.z = z
        self.active = active
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
        self.lit = not self.lit # alternar el estado de "iluminación"

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
                    if curr_cell == 2:              # Posición inicial del bot
                        self.bot_x, self.bot_y = x, y
                        self.cells[x][y].z = 0      # Marcamos la posición inicial como espacio vacío
            self.directions = ['N', 'E', 'S', 'O']  # Posibles direcciones
            self.bot_direction = 0                  # Inicia mirando hacia el norte

    def execute_actions(self, actions_filename: str):
        """lee y ejecuta acciones de un archivo .txt """
        with open(actions_filename) as f:
            for line in f:
                action = line.strip()
                if action == "Move forward":
                    self.move()
                elif action == "Turn left":
                    self.turn_left()
                elif action == "Turn Right":
                    self.turn_right()
                elif action == "Light up the tile":
                    self.cells[self.bot_x][self.bot_y].toggle_lit()

    def check_status(self):
        """ comprueba si cada casilla meta está iluminada"""
        for x in range(self.width):
            for y in range(self.height):
                if self.cells[x][y].z == META and self.cells[x][y].lit == False:
                    return False
        return True

        if done:
            print("Objetivo completado")
        else:
            print("Quedaron casillas metas sin encender...")

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
        if 0 <= new_x < self.height and 0 <= new_y < self.width and self.cells[new_x][new_y].z == 0 or self.cells[new_x][new_y].z == META:
            self.bot_x, self.bot_y = new_x, new_y

    def turn_left(self):
        self.bot_direction = (self.bot_direction - 1) % 4

    def turn_right(self):
        self.bot_direction = (self.bot_direction + 1) % 4

    def draw(self, screen):
        cell_size = 100  # Tamaño de cada celda en píxeles
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                if self.cells[y][x].z == MURO: 
                    pygame.draw.rect(screen, (0, 0, 0), rect) 
                elif self.cells[y][x].lit:  
                    pygame.draw.rect(screen, (255, 255, 0), rect)  
                elif self.cells[y][x].z == META: 
                    pygame.draw.rect(screen, (0, 255, 0), rect)  
                else:  # Espacio vacío
                    pygame.draw.rect(screen, (255, 255, 255), rect)  
                if self.bot_x == y and self.bot_y == x:
                    pygame.draw.circle(screen, (0, 0, 255), (x * cell_size + cell_size//2, y * cell_size + cell_size//2), cell_size//2)

def draw_button(screen, button_text, button_position, button_size):
    font = pygame.font.Font(None, 36)
    text = font.render(button_text, True, (255, 255, 255))
    button_rect = pygame.Rect(button_position, button_size)
    pygame.draw.rect(screen, (0, 0, 255), button_rect) 
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    return button_rect

def draw_status_message(screen, message, position, size):
    font = pygame.font.Font(None, size)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect)

if __name__ == '__main__':
    pygame.init()
    screen_size = (SCREEN_WIDTH, SCREEN_HIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Lightbot")
    
    board = Board('board.txt')
    status_message = "Aún no ha pasado nada"
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if load_button_rect.collidepoint(mouse_pos):
                    actions_file_path = open_file_dialog()
                    if actions_file_path:  # Verifica si el usuario seleccionó un archivo
                        board.execute_actions(actions_file_path)
                        if board.check_status():
                            status_message = "Objetivo Completado"
                        else:
                            status_message = "Quedaron casillas metas sin encender"

        screen.fill((0, 0, 0))
        board.draw(screen) 
        load_button_rect = draw_button(screen, "Cargar Instrucciones", (0, SCREEN_HIGHT - 50), (300, 50))
        draw_status_message(screen, status_message, (SCREEN_WIDTH - 250, SCREEN_HIGHT - 25), 36) 
        pygame.display.flip() 

    pygame.quit()