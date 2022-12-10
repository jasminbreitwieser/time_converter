import tkinter as tk
from tkinter import ttk

window =tk.Tk()
window.title("Time Converter")
window.configure(background="black")

# Set the window size (Width x Height)
window_width = 600
window_height = 600

## Center the window
# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


# create menu widget
menu_convert_from = ttk.Menubutton(window, text="Convert From") 

# create a new instance of menu class
drop_convert_from = tk.Menu(menu_convert_from, tearoff=False)
options_convert_from = [
    "Milliseconds", "Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"
    ]
# add options to the menu
for option in options_convert_from:
    drop_convert_from.add_command(label=option)
# add menu to widget
menu_convert_from.config(menu=drop_convert_from)



menu_convert_from.pack()

window.mainloop()