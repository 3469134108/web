
from tkinter import *
import sys,os,time,pip
 

def insert_insert():
    os.system('start http://i.mooc.chaoxing.com/space/index')
    time.sleep(3)
    sys.exit()
def weichant():
        os.system('cd/')
        os.system('start D:/weichant')
        time.sleep(3)
        sys.exit()
def insert_end():
    sys.exit()
root = Tk()
root.minsize(200, 200)

button1 = Button(root, text="打开链接", command=insert_insert)
button1.pack()
button3 = Button(root, text="打开微信", command = weichant)
button3.pack()
button2 = Button(root, text="退出", command=insert_end)
button2.pack()

w = Label(root, text="点击‘打开’按钮即可。")
w.pack()

root.mainloop()
