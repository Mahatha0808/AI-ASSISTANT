from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action

root = Tk()
root.title("VoX Assist")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="grey")

# ask function and implementing it
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action()
    text.insert(END, "User----->" + user_val + "\n")
    if bot_val is not None:
        text.insert(END, "Bot<----" + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()

def send():
    send_val = entry.get()
    bot_val = action.Action(send_val)
    text.insert(END, "User----->" + send_val + "\n")
    if bot_val is not None:
        text.insert(END, "Bot<----" + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()

def delete():
    text.delete('1.0', END)

# frame creation
frame = LabelFrame(root, padx=100, pady=9, borderwidth=3, relief="raised", bg="grey")
frame.grid(row=0, column=1, padx=85, pady=50)

# text label
text_label = Label(frame, text="AI Assistant", font=("Comic Sans MS", 15, "bold"), bg="olive")
text_label.grid(row=0, column=0, padx=20, pady=10)

# image
image = ImageTk.PhotoImage(Image.open(r"D:\download.jpg"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, padx=10, pady=5)

# Adding a text widget
text = Text(root, font=("Courier", 10, "bold"), bg="blue", width=50, height=4)
text.place(x=100, y=375)

# entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=100, y=500, width=350, height=30)

# button 1
Button1 = Button(root, text="ASK", bg="green", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

# button 2
Button2 = Button(root, text="SEND", bg="green", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400, y=575)

# button 3
Button3 = Button(root, text="DELETE", bg="green", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete)
Button3.place(x=225, y=575)

root.mainloop()
