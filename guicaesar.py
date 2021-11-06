"""
Student Code by Tanishq Sarkar
This is a tkinter version of a Caesar Cipher

"""
import tkinter as tk

root = tk.Tk()

frame_a = tk.Frame(bg="#00fff0")
frame_b = tk.Frame(bg="#ff00e4")

label_a = tk.Label(master=frame_a, text="Enter your word:", bg="#00fff0", width = 30)
label_a.pack()

entry_a = tk.Entry(master=frame_a,fg="#aa00ff", width = 40)
entry_a.pack()

label_b = tk.Label(master=frame_b, text="Enter your shift number:", bg="#ff00e4", width = 30)
label_b.pack()

entry_b = tk.Entry(master=frame_b, fg="#aa00ff", width = 40)
entry_b.pack()

frame_a.pack()
frame_b.pack()

def binarysearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid =int((left+right)/2)
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def caeser():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s','t','u','v','w','x','y','z']
    alphabet += alphabet
    text = entry_a.get()
    s = int(entry_b.get())
    newword = ''
    for i in range(0, len(text)):
        if text.isupper():
            ch = text[i].lower()
            x = binarysearch(alphabet, ch)
            x += s
            newword += alphabet[x].upper()
        else:
            ch = text[i]
            x = binarysearch(alphabet, ch)
            x += s
            newword += alphabet[x]
    message = "Your encrypted message is: " + newword
    label = tk.Label(text=message, fg="#aa00ff")
    label.pack()
def validation():
    x = 0
    text = entry_a.get()
    s = entry_b.get()
    if len(text) == 0:
        msg = "You need to input a word"
    else:
        if any(ch.isdigit() for ch in text):
            msg = "Your Word can't have numbers"
        else:
            if len(s) == 0:
                msg = "You need to input a shift"
            for i in s:
                if i.isdecimal() == False:
                    msg = "Your shift must be a number!"
                else:
                    x = 1
                    caeser()
    if x == 0:
        label = tk.Label(text=msg, fg="#aa00ff")
        label.pack()

W = tk.Button(text="Encrypt", command=validation, bg="#17ff00")
W.pack()
quit = tk.Button(text="Quit", command=quit, bg="#ea4747")
quit.pack()
root.mainloop()
