import tkinter as tk
from tkinter import *
from tkinter import messagebox
from queue import PriorityQueue
import math
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))

def ok_button():
    window1.destroy()


window1 = Tk()
t = IntVar()
lb1 = tk.Label(window1, text=("Grid-Size : 30 X 30"),font = ("Verdana", 12))
lb1.place(x=40, y=60)
l1 = tk.Button(window1, text='Ok', command = ok_button)
l1.place(x = 100,y =100)
window1.title('Successfully Executed')
window1.geometry("400x200+10+20")
window1.mainloop()



def show():
    messagebox.showinfo("Submit", "Submit")
    print("start(x):%s\n start(y):%s\n end(x):%s\n end(y):%s \n checkbox:%d" % (
    e1.get(), e2.get(), e3.get(), e4.get(), var.get()))
    global vinay_list
    vinay_list = [e1.get(), e2.get(), e3.get(), e4.get()]
    master.destroy()


master = tk.Tk()
tk.Label(master, text="start(x)").grid(row=0)
tk.Label(master, text="start(y)").grid(row=1)
tk.Label(master, text="end(x)").grid(row=2)
tk.Label(master, text="end(y)").grid(row=3)
# e1 = IntVar()
# e2 = IntVar()
# e3 = IntVar()
# e4 = IntVar()

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
var = IntVar()
tk.Checkbutton(master, text='Show Steps:', variable=var).grid(row=4, column=1, sticky=tk.W, pady=4)
tk.Button(master, text='Submit', command=show).grid(row=5, column=1, sticky=tk.W, pady=4)
# tk.Button(master, text='Quit',command=master.quit).grid(row=5, column=2,sticky=W,pady=4)

tk.mainloop()
#####################

##new cell


##################

# algorithm


def heuristic(a, b):
    d_x = abs(a[0] - b[0])
    d_y = abs(a[1] - b[1])
    return math.sqrt(math.pow(d_x, 2) + math.pow(d_y, 2))


def neighbors(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
    result = []
    for direction in dirs:
        neighbor = [node[0] + direction[0], node[1] + direction[1]]
        if 0 <= neighbor[0] < 30 and 0 <= neighbor[1] < 30:
            result.append(neighbor)
    return result


def visited_rect(screen, coordinates):
    green = (0, 255, 0)
    rect = pygame.Rect(coordinates[0]*20, coordinates[1]*20, 19, 19)
    pygame.draw.rect(screen, green, rect, 0)


def shortest_path(screen, coordinates):
    blue = (0, 0, 255)
    rect = pygame.Rect(coordinates[0]*20, coordinates[1]*20, 19, 19)
    pygame.draw.rect(screen, blue, rect, 0)



print(vinay_list)
# X, Y = input("enter the dimensions of Grid:").split()
# X = int(X)
# Y = int(Y)
nodes = []
came_from = {}
cost_so_far = {}
for i in range(30):
    for j in range(30):
        nodes.append([i, j])
        cost_so_far.update({i: {j: 0}})
        came_from.update({i: {j: None}})


start_X, start_Y = int(vinay_list[0]), int(vinay_list[1])
starting_point = [start_X, start_Y]
goal_X, goal_Y = int(vinay_list[2]), int(vinay_list[3])
goal = [goal_X, goal_Y]
frontier = PriorityQueue()
frontier.put(starting_point, 0)
came_from.update({starting_point[0]: {starting_point[1]: starting_point}})
cost_so_far.update({starting_point[0]: {starting_point[1]: 0}})

while not frontier.empty():
    current = frontier.get()

    if current == goal:
        break

    for child in neighbors(current):
        visited_rect(screen, child)
        new_cost = cost_so_far[current[0]][current[1]] + 1
        index = child[0] not in cost_so_far or child[1] not in cost_so_far[child[0]]
        if index is True or new_cost < cost_so_far[child[0]][child[1]]:
            cost_so_far[child[0]].update({child[1]: new_cost})
            priority = new_cost + heuristic(goal, child)
            frontier.put(child, priority)
            came_from[child[0]].update({child[1]: current})

steps = 0
path = []
while current != starting_point:
    steps = steps + 1
    shortest_path(screen, current)
    path.append(current)
    current = came_from[current[0]][current[1]]
shortest_path(screen,starting_point)
path.append(starting_point)
path.reverse()
print(path)
print(steps)


# Pygame part

def draw_grid(screen, width, height):
    white = (255, 255, 255)
    for i in range(width):
        for j in range(height):
            rect = pygame.Rect(i * 20, j * 20, 20, 20)
            pygame.draw.rect(screen, white, rect, 2)


def start_end(screen, coordinates):
    red = (255, 0, 0)
    rect = pygame.Rect(coordinates[0], coordinates[1], 19, 19)
    pygame.draw.rect(screen, red, rect, 0)


start = [start_X*20, start_Y*20] #input
end = [goal_X*20, goal_Y*20]
print(start, end)
width = 600
height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
# list of all rectangles
all_rect = []
block_size = 20
for x in range(0, height, block_size):
    row = []
    for y in range(0, width, block_size):
        rect = pygame.Rect(y, x, block_size - 2, block_size - 2)
        if ((y == start[0] and x == start[1]) or (y == end[0] and x == end[1])):
            row.append([rect, red])
        else:
            row.append([rect, black])
    all_rect.append(row)


quit = False
loop = True
while (loop):
    draw_grid(screen, width, height)
    start_end(screen, start)
    start_end(screen, end)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            quit = True
        if pygame.mouse.get_pressed()[0]:
            for row in all_rect:
                for box in row:
                    rec, color = box
                    pos = pygame.mouse.get_pos()
                    if rec.collidepoint(pos):
                        if color == black:
                            box[1] = white
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                loop = False
                break

    # for row in all_rect:
    #     for box in row:
    #         rec, color = box
    #         pygame.draw.rect(screen, color, rec, 0)

    pygame.display.update()
if quit:
    pygame.quit()


#for number of steps(displaying)
from tkinter import *
from tkinter import messagebox

window2 = Tk()
t = IntVar()
lb1 = tk.Label(window2, text=("Program Finished.\nThe shortest distance is %d blocks away "%steps),font = ("Verdana", 12))
lb1.place(x=40, y=60)
window2.title('Successfully Executed')
window2.geometry("400x200+10+20")
window2.mainloop()





