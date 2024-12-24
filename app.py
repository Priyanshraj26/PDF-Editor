from tkinter.ttk import Style
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import *
import pyttsx3
import PyPDF2
from PIL import ImageTk,Image

root = Tk()
root.title('PDF Editor [BETA]')
root.geometry('450x650')
root.config(bg='#1a1f2b')
root.resizable(0, 0)
root.overrideredirect(True) # turns off title bar, geometry

def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

# make a frame for the title bar
title_bar = Frame(root, bg='#1a1f2b', relief='flat')

# put a close button on the title bar
close_button = Button(title_bar, text='✕', font='Segoe, 13',
                      command=root.destroy, relief='flat', width=4, 
                      bd=0, bg='#1a1f2b', fg='white', 
                      activebackground='red', 
                      activeforeground='white')

photo0 = PhotoImage(file = "Icon.png")
photoimage0 = photo0.subsample(6, 6)
title_name = Label(title_bar, compound=LEFT, 
                   image=photoimage0, text='PDF Editor (BETA)', 
                   bg='#1a1f2b', fg="white", padx=7)

# pack the widgets
title_bar.pack(expand=1, fill=X)
title_name.pack(side=LEFT)
close_button.pack(side=RIGHT)

# bind title bar motion to the move window function
title_bar.bind('<B1-Motion>', move_window)

canvas = Canvas(root, width=238, height=75, bd=0, 
                highlightthickness=0, relief='flat', 
                bg='#1a1f2b')
canvas.pack(pady=5)
img = ImageTk.PhotoImage(Image.open("Logo.png"))
canvas.create_image(0, 0, anchor=NW, image=img)

path = []


def choose_pdf():
    global path
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Import file",
        filetypes=(("PDF files", "*.pdf*"), 
                   ("all files", "*.*")))
    if filename:
        path.append(filename)
        return filename


def read_pdf():
    filename = choose_pdf()
    reader = PyPDF2.PdfFileReader(filename)
    pageObj = reader.getNumPages()
    for page_count in range(pageObj):
        page = reader.getPage(page_count)
        page_data = page.extractText()
        textbox.insert(END, page_data)


def save_file():
    content = textbox.get(1.0, "end-1c")
    fob = filedialog.asksaveasfile(defaultextension='.txt',
                                   filetypes=[('text file', '*.txt')],
                                   initialdir='D',
                                   mode='w')
    try:
        fob.write(content)
        fob.close()
        textbox.delete('1.0', END) #Delete from position 0 till end
        textbox.update()
        b1.config(text="Saved")
        b1.after(3000, lambda: b1.config(text='Save'))
    except:
        print(" There is an error...")


def copy_pdf_text():
    content = textbox.get(1.0, "end-1c")

    root.clipboard_clear()
    root.clipboard_append(content)
    root.update()


# The Textbox
textbox = Text(root, height=22, font=('Segoe UI', 12), width=49, wrap='word', 
               fg='white', bg='#222a3d',
               cursor='arrow',
               relief='flat',
               bd=0,
               padx=7,
               pady=7,
               selectforeground='#e85d1c',
               selectbackground='#1a1f2b')
textbox.configure(insertbackground='#e85d1c')
textbox.pack(expand=True)

# Creating Button for choosing pdf

style = Style()

style.configure('TButton', relief=FLAT, font=('calibri', 18))

style.map('TButton', foreground=[('active', '!disabled', '#0ed562')],
           background=[('active', 'black')])

#Inserting Images
photo1 = PhotoImage(file = "import-icon.png")
photoimage1 = photo1.subsample(30, 30)

photo2 = PhotoImage(file = "copy-icon.png")
photoimage2 = photo2.subsample(30, 30)

photo3 = PhotoImage(file = "narrate-icon.png")
photoimage3 = photo3.subsample(30, 30)

photo4 = PhotoImage(file = "export-icon.png")
photoimage4 = photo4.subsample(30, 30)
Button(root, text = ' Import', image = photoimage1,
    compound = LEFT,
    width=103,
    height=47,
    relief=FLAT,
    bd=0,
    background='#1a1f2b',
    foreground='#e85d1c',
    command=read_pdf,
    activebackground='#141821',
    activeforeground='#e85d1c'
).pack(expand=TRUE, side = LEFT)

# Creating Button for copying the text

Button(root, text = ' Copy', image = photoimage2,
     compound = LEFT,
    width=103,
    height=47,
    relief=FLAT,
    bd=0,
    background='#1a1f2b',
    foreground='#e85d1c',
    command=copy_pdf_text,
    activebackground='#141821',
    activeforeground='#e85d1c'
).pack(expand=TRUE, side = LEFT)


def myvoice123():
    engine = pyttsx3.init()

    # testing
    engine.setProperty('rate', 130)
    engine.say(textbox.get(1.0, "end-1c"))
    engine.runAndWait()


Button(root, text = ' Narrate', image = photoimage3,
     compound = LEFT,
    width=103,
    height=47,
    relief=FLAT,
    bd=0,
    background='#1a1f2b',
    foreground='#e85d1c',
    command=myvoice123,
    activebackground='#141821',
    activeforeground='#e85d1c'
).pack(expand=TRUE, side = LEFT)

b1 = Button(root, text = ' Export', image = photoimage4,
     compound = LEFT,
    width=103,
    height=47,
    relief=FLAT,
    bd=0,
    background='#1a1f2b',
    foreground='#e85d1c',
    command=save_file,
    activebackground='#141821',
    activeforeground='#e85d1c'
).pack(expand=TRUE, side = LEFT)

root.mainloop()
