from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image as image

root = Tk()
root.geometry("500x650")
root.configure(bg="#1B1B21")
root.title("Image conversion")
root.iconbitmap("logo.ico")

def show():
    global picture

    root.filename = filedialog.askopenfilename(title="choose a picture", filetypes=(("png files", "*.png"),("all types","*.*")))
    png_pic = image.open(root.filename)
    r_png_pic = png_pic.resize((450,500), image.ANTIALIAS)
    picture = ImageTk.PhotoImage(r_png_pic)

    lab = Label(frame, image=picture).pack()

# function that convert from PNG to JPG
def pngTjpg():

    global picture
    global error
    error = None

    # destroy the old picture
    for widget in frame.winfo_children():
        widget.destroy()

    # ask for the picture that you want to convert
    root.filename = filedialog.askopenfilename(title="choose a picture",
                                               filetypes=(("png files", "*.png"), ("all types", "*.*")))
    if root.filename != '':
        png_pic = image.open(root.filename)
        r_png_pic = png_pic.resize((450, 500), image.ANTIALIAS)
        picture = ImageTk.PhotoImage(r_png_pic)

        lab = Label(frame, image=picture)
        lab.pack()

        if file_name.get() == '':
            lab.destroy()

            error = Label(root, text="Enter the name of your file please", bg="#1B1B21", fg="red")
            error.grid(row=3, column=0, columnspan=2)
        else:
            with open(root.filename, 'rb') as pic:
                b_pic = pic.read()
            with open((file_name.get() + ".jpg"), 'wb') as n_pic:
                jpg_pic = n_pic.write(b_pic)
            save = Label(root, text="Your picture is saved successfully", bg="#1B1B21", font="none 12 bold")
            save.grid(row=3, column=0, columnspan=2)


# function that convert from JPG to PNG

def jpgTpng():

    global picture1
    global error1
    error1 = None
    for widget in frame.winfo_children():
        widget.destroy()
    root.filename = filedialog.askopenfilename(title="choose a picture",
                                               filetypes=(("jpg files", "*.jpg"), ("all types", "*.*")))
    if root.filename != '':
        jpg_pic = image.open(root.filename)
        r_jpg_pic = jpg_pic.resize((450, 500), image.ANTIALIAS)
        picture1 = ImageTk.PhotoImage(r_jpg_pic)

        lab = Label(frame, image=picture1)
        lab.pack()

        if file_name.get() == '':
            lab.destroy()
            error1 = Label(root, text="Enter the name of your file please", bg="#1B1B21", fg="red")
            error1.grid(row=3, column=0, columnspan=2)

        else:
            with open(root.filename, 'rb') as pic:
                b_pic = pic.read()
            with open((file_name.get() + ".png"), 'wb') as n_pic:
                png_pic = n_pic.write(b_pic)
            save1 = Label(root, text="Your picture is saved successfully", bg="#1B1B21", font="none 12 bold")
            save1.grid(row=3, column=0, columnspan=2)


def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()
    file_name.delete(0, END)



frame = Frame(root, width=450, height=500)
png_text = Label(root, text="file name", bg="#1B1B21", font="propaganda 12")
file_name = Entry(root, font="none 12")
type_text = Label(root, text=".jpg", bg="#6AF2D6", font="propaganda 12")
clear = Button(root, text="clear", padx=30, pady=8,font="none 12 bold",command=clear_frame)
pngTojpg = Button(root, text="pngTjpg", padx=20, pady=7,font="none 12 bold", command=pngTjpg)
jpgTopng = Button(root, text="jpgTpng", padx=20, pady=7,font="none 12 bold", command=jpgTpng)

frame.grid(row=0, column=0, columnspan=3, padx=27, pady=(0,5))
pngTojpg.grid(row=1,column=0)
clear.grid(row=1, column=1, pady=5)
jpgTopng.grid(row=1, column=2)
png_text.grid(row=2, column=0, pady=(10,0))
file_name.grid(row=2, column=1, pady=(10,0))
# type_text.grid(row=2, column=2, pady=(10,0))

root.mainloop()