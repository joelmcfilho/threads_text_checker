import tkinter as tk

#Main window setup
root = tk.Tk()
root.title("Threads Text Checker")
root.configure(bg="oldlace")

#Control variables
char_length = tk.StringVar()
char_length.set("Caracteres: 0/500")

#Functions
##Function to update character count
def update_length(Event=None):
    text = text_entry.get("1.0", "end-1c")
    char_length.set(f"Characters: {len(text)}/500")
    if len(text) > 500:
        length_display.config(fg="red")
    else:
        length_display.config(fg="black")

##Function to copy text to clipboard
def copy_text():
    content = text_entry.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(content)
    char_length.set(f"Characters: {len(content)}/500 - Copied!✅")

##Function to clear text box
def clear_text():
    text_entry.delete("1.0", "end")
    char_length.set("Characters: 0/500")



#GUI Widgets
## Frames
frame_upper = tk.Frame(root, bg="oldlace")
frame_upper.pack(side="top")

frame_txtbox = tk.Frame(root, bg="oldlace")
frame_txtbox.pack(side="top", expand=True)

##Widgets in frames
### Subtitle Label
upper_label = tk.Label(frame_upper, text="Enter the text of your Thread:",anchor='w',bg="oldlace", font=("Arial", 14))
upper_label.pack(pady=10)

### Text Box and Scrollbar
text_entry = tk.Text(frame_txtbox, width=50,height=10,font=("Arial", 12))
text_entry.pack(side="left", fill="y", expand=False)

scrollbar = tk.Scrollbar(frame_txtbox, command=text_entry.yview)
scrollbar.pack(side="right", fill="y")
text_entry.config(yscrollcommand=scrollbar.set)

### Display Length
length_display = tk.Label(root, textvariable=char_length, bg="oldlace", font=("Arial", 10))
length_display.pack(pady=10)

### Copy text button
btn_copy = tk.Button(root, text="Copy Text 📋",bg="NavajoWhite4",fg="black",command=copy_text)
btn_copy.pack(pady=10)

### Clear text button
btn_clear = tk.Button(root, text="Clear Text 🗑️",bg="red",fg="black",command=clear_text)
btn_clear.pack(padx=10, pady=10)

#Event binding for text entry
text_entry.bind("<KeyRelease>", update_length)


root.mainloop()