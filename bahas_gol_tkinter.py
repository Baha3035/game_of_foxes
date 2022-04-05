from tkinter import *
from random import randint, choice
from fox import Fox
from grass import Grass
from rabbit import Rabbit
import fox
import grass
import rabbit


class Field:
    def __init__(self, c, n, m, width, height, fox, rabbit, grass):
        '''
       c - canvas instance
       n - number of rows
       m - number of columns
       width - width of game field in pixels
       height - width of game field in pixels
       '''
        self.c = c
        self.a = []
        self.n = n + 2
        self.m = m + 2
        self.width = width
        self.height = height
        self.fox = fox
        self.rabbit = rabbit
        self.grass = grass
        self.count = 0
        for i in range(self.n):
            self.a.append([])
            for j in range(self.m):
                self.a[i].append(0)
        self.a = [[randint(0, 2) for i in range(width)] for j in range(height)]
        # 1 - Fox (orange)
        # 2 - Rabbit (blue)
        # 0 - Grass (green)
        self.draw()
    # helper check all its neighbors into temporary (tmp) array

    def helper(self, r, c):
        M, N = self.n, self.m
        cnt_foxes, cnt_rabbits = 0, 0
        coordinates = [(0, 1), (0, -1), (1, 0), (-1, 0),
                       (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for x, y in coordinates:
            if 0 <= r + y < M and 0 <= c + x < N and self.a[r+y][x+c] == 1:
                cnt_foxes += 1
            elif 0 <= r + y < M and 0 <= c + x < N and self.a[r+y][x+c] == 2:
                cnt_rabbits += 1

        if self.a[r][c] == 2:
            if cnt_foxes > 1:
                return 1
# if foxes are at least 2 and there is one rabbit
# they can eat it and reproduce to its place
            elif 2 <= cnt_rabbits <= 3:
                return 2
        elif self.a[r][c] == 1:
            if cnt_foxes < 2:
                return 0
            elif 2 <= cnt_foxes <= 3 and cnt_rabbits > 1:
                return 1
            else:
                return 0
        else:
            if cnt_rabbits == 3:
                return 2
            else:
                return 0

    def step(self):
        tmp = [[None] * self.m for _ in range(self.n)]
        for r in range(self.n):
            for c in range(self.m):
                tmp[r][c] = self.helper(r, c)
                # temporary array filled with next moves of animals
        self.a = tmp

    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()

    def draw(self):
        color = "grey"
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if (self.a[i][j] == 1):
                    color = self.fox.get_color()  # fox
                elif (self.a[i][j] == 2):
                    color = self.rabbit.get_color()  # rabbit
                else:
                    color = self.grass.get_color()  # grass
                self.c.create_rectangle((i-1) * sizen, (j-1) * sizem,
                                        (i) * sizen, (j) * sizem, fill=color)
        self.step()
        self.c.after(2000, self.draw)

root = Tk()
root.geometry("800x800")
c = Canvas(root, width=800, height=800)
c.pack()
fox, rabbit, grass = None, None, None
try:
    fox = Fox()
    rabbit = Rabbit()
    grass = Grass()
    # Exception handling to ensure that objects are properly initialized
except:
    print("objects are not initialized")
f = Field(c, 40, 40, 800, 800, fox, rabbit, grass)
cntt = 0
f.print_field()
cntt += 1
print(cntt)
root.mainloop()
