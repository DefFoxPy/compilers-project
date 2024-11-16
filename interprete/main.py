class Cell:
    
    def __init__(self, z=0, active=False, lit=False): 
        self.z = z
        self.active = active
        self.lit = lit

    def __repr__(self):
        if self.z == 1:  # Muro
            return 'M'
        elif self.z == 2:  # Bot
            return 'B'
        elif self.z == 9 and not self.lit:  # Meta
            return 'G'
        elif self.lit:  # Espacio iluminado
            return 'L'
        else:  # Espacio vacío
            return ' '

    def toggle_lit(self):
        self.lit = not self.lit # alternar el estado de "iluminación"

class Board:

    def __init__(self, filename: str):
        """Reads a board file from disk and stores it as a Board object."""
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
        done = True
        for x in range(self.width):
            for y in range(self.height):
                if self.cells[x][y].z == 9 and self.cells[x][y].lit == False:
                    done = False

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
        if 0 <= new_x < self.height and 0 <= new_y < self.width and self.cells[new_x][new_y].z == 0 or self.cells[new_x][new_y].z == 9:
            self.bot_x, self.bot_y = new_x, new_y

    def turn_left(self):
        self.bot_direction = (self.bot_direction - 1) % 4

    def turn_right(self):
        self.bot_direction = (self.bot_direction + 1) % 4

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                if x == self.bot_x and y == self.bot_y:
                    print('B', end=' ')
                else:
                    print(self.cells[x][y], end=' ')
            print()

## Uso
if __name__ == '__main__':
    board = Board('board.txt')
    print("Mapa inicial") # debug
    board.draw()
    board.check_status()
    input('presione enter para cargar las acciones') # una espera 
    board.execute_actions('actions.txt')
    print("Mapa final") #debug
    board.draw()
    board.check_status()