#Tushar Bhosale

import tkinter as tk
from tkinter import Entry, Label,Button
import webbrowser

#Define the main wiindow
root = tk.Tk()
root.title("Tushar's AI Assistant")

#Adding a background colour
root.configure(bg='plum')

#Define the function to automate youtube search
def search_youtube():
    query=entry.get()
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

#Define the function to automate google search
def search_google():
    query=entry.get()
    url=f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

#Define the function to automate instagram search
def search_instagram():
    Username= entry.get().replace('@',"")  #Ensure username is clean of '@'
    url = f"www.instagram.com/{Username}/"
    webbrowser.open(url)

#Create input field, labels and buttons
Label(root, text="Enter your command :").pack(pady=10)
entry=Entry(root, width=50)
entry.pack(pady=10)

Button(root,text="Search on Google", command=search_google).pack(pady=5)
Button(root,text="Search on Youtube", command=search_youtube).pack(pady=5)
Button(root,text="Search on Instagram", command=search_instagram).pack(pady=5)

root.mainloop()
