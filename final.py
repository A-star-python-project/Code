import tkinter as tk
from tkinter import *
from tkinter import messagebox


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
from tkinter import *
from tkinter import messagebox

window = Tk()
t = IntVar()
lb1 = tk.Label(window, text="Number of steps:")
t = tk.Entry()
lb1.place(x=0, y=50)
t.place(x=100, y=50)


def message():
    messagebox.showinfo("program finished", "Program Finished.The shortest distance is %s blocks away" % (t.get()))
    window.destroy()


b1 = Button(window, text='OK', command=message)
b1.place(x=50, y=100)
window.title('Program Finished')
window.geometry("300x200+10+20")
window.mainloop()

# algorithm

from queue import PriorityQueue
import math


def heuristic(a, b):
    d_x = abs(a[0] - b[0])
    d_y = abs(a[1] - b[1])
    return math.sqrt(math.pow(d_x, 2) + math.pow(d_y, 2))


def neighbors(node, X, Y):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
    result = []
    for direction in dirs:
        neighbor = [node[0] + direction[0], node[1] + direction[1]]
        if 0 <= neighbor[0] < X and 0 <= neighbor[1] < Y:
            result.append(neighbor)
    return result


print(vinay_list)
X, Y = input("enter the dimensions of Grid:").split()
X = int(X)
Y = int(Y)
nodes = []
came_from = {}
cost_so_far = {}
for i in range(X):
    for j in range(Y):
        nodes.append([i, j])
        cost_so_far.update({i: {j: 0}})
        came_from.update({i: {j: None}})


start_X, start_Y = int(vinay_list[0]), int(vinay_list[1])
start = [start_X, start_Y]
goal_X, goal_Y = int(vinay_list[2]), int(vinay_list[3])
goal = [goal_X, goal_Y]
frontier = PriorityQueue()
frontier.put(start, 0)
came_from.update({start[0]: {start[1]: start}})
cost_so_far.update({start[0]: {start[1]: 0}})

while not frontier.empty():
    current = frontier.get()

    if current == goal:
        break

    for child in neighbors(current, X, Y):
        print(child)
        print('hi')
        print(cost_so_far[current[0]])
        new_cost = cost_so_far[current[0]][current[1]] + 1
        index = child[0] not in cost_so_far or child[1] not in cost_so_far[child[0]]
        if index is True or new_cost < cost_so_far[child[0]][child[1]]:
            cost_so_far[child[0]].update({child[1]: new_cost})
            priority = new_cost + heuristic(goal, child)
            frontier.put(child, priority)
            came_from[child[0]].update({child[1]: current})


path = []
while current != start:
    path.append(current)
    current = came_from[current[0]][current[1]]
path.append(start)
path.reverse()
print(path)


