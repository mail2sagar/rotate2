from tkinter import *
from PIL import Image,ImageTk
window = Tk()

window.title("Image Loader")
window.geometry("600x600")
window.config(background="gray9")


def open():
    
    variable_holding_image.rotate(angle)

    img = Image.open(img_path)

    variable = Image.open(variable_image_path)

    rotated_img = img.rotate(180)

    ImageTk.PhotoImage(variable_holding_image.rotate(angle))

    img = ImageTk.PhotoImage(rotated_img)






button_open = Button(window,text="Open Image")

button_open.place(relx=0.5,rely=0.2,anchor=CENTER)

label_loaded = Label(window)

label_loaded.place(relx=0.5,rely=0.5,anchor=CENTER)

button_rotate = Button(window,text="Rotate Image")

button_rotate.place(relx=0.5,rely=0.7,anchor=CENTER)

window.mainloop()