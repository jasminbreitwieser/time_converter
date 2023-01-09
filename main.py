import tkinter as tk

window =tk.Tk()
window.title("Time Converter")
window.configure()

# Set the window size (Width x Height)
window_width = 300
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

# organize the position of widgets with tkinter.Frame
frame_year = tk.Frame(window)
frame_months = tk.Frame(window)
frame_weeks = tk.Frame(window)
frame_days = tk.Frame(window)
frame_hours = tk.Frame(window)
frame_seconds = tk.Frame(window)
frame_milliseconds = tk.Frame(window)
frame_convert = tk.Frame(window)
frame_output = tk.Frame(window)


frame_year.pack()
frame_months.pack()
frame_weeks.pack()
frame_days.pack()
frame_hours.pack()
frame_seconds.pack()
frame_milliseconds.pack()
frame_convert.pack()
frame_output.pack()

# create input boxes
default_years = tk.StringVar(window, value="0") # default value = "0"
default_months = tk.StringVar(window, value="0") # default value = "0"
default_weeks = tk.StringVar(window, value="0") # default value = "0"
default_days = tk.StringVar(window, value="0") # default value = "0"
default_hours = tk.StringVar(window, value="0") # default value = "0"
default_seconds = tk.StringVar(window, value="0") # default value = "0"
default_milliseconds = tk.StringVar(window, value="0") # default value = "0"

entry_width = 10
input_years = tk.Entry(frame_year, textvariable=default_years, width=entry_width) 
input_months = tk.Entry(frame_months, textvariable=default_months, width=entry_width) 
input_weeks = tk.Entry(frame_weeks, textvariable=default_weeks, width=entry_width) 
input_days = tk.Entry(frame_days, textvariable=default_days, width=entry_width) 
input_hours = tk.Entry(frame_hours, textvariable=default_hours, width=entry_width) 
input_seconds = tk.Entry(frame_seconds, textvariable=default_seconds, width=entry_width) 
input_milliseconds = tk.Entry(frame_milliseconds, textvariable=default_milliseconds, width=entry_width) 

# create labels
label_width= 10
label_years = tk.Label(frame_year, text="Years", width=label_width)
label_months = tk.Label(frame_months, text="Months", width=label_width)
label_weeks = tk.Label(frame_weeks, text="Weeks", width=label_width)
label_days = tk.Label(frame_days, text="Days", width=label_width)
label_hours = tk.Label(frame_hours, text="Hours", width=label_width)
label_seconds = tk.Label(frame_seconds, text="Seconds", width=label_width)
label_milliseconds = tk.Label(frame_milliseconds, text="Milliseconds", width=label_width)

# create convert button
convert_button = tk.Button(frame_convert, text="Convert", relief="raised", bg='#000000', fg='#000000')

# # create a new instance of menu class
# drop_convert_from = tk.Menu(menu_convert_from, tearoff=False)

# # drop down menu options
# options_convert_from = [
#     "Milliseconds", "Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", 
#     "Years", "Y:M:D:H:m:s:ms"
#     ]
# options_convert_to = [
#     "Milliseconds", "Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", 
#     "Years", "Y:M:D:H:m:s:ms"
#     ]
# # get input from user
# input_time = tk.Entry(window, width=20, borderwidth=5)


# # add input field to window
# input_time.pack()

# # time conversion
# def input_to_seconds(opt, inpu):
#     inp = float(inpu)
#     if opt == "Milliseconds":
#         sec = inp * 0.001
#     elif opt == "Seconds":
#         sec = inp * 1
#     elif opt == "Minutes":
#         sec = inp * 60
#     elif opt == "Hours":
#         sec = inp * 60 * 60
#     elif opt == "Days":
#         sec = inp * 60 * 60 * 24
#     elif opt == "Weeks":
#         sec = inp * 60 * 60 * 24 * 7
#     elif opt == "Months":
#         sec = inp * 60 * 60 * 24 * 30.437
#     elif opt == "Years":
#         sec = inp * 60 * 60 * 24 * 365.24
#     elif opt == "Y:M:D:H:m:s:ms":
#         sec = inp[0] * 60 * 60 * 24 * 365.24 + inp[1] * 60 * 60 * 24 * 30.437 + inp[2] * 60 * 60 * 24 + inp[3] * 60 * 60 + inp[4] * 60 + inp[5] + inp[6] * 0.001
#     return sec

# def seconds_to_output(sec):
#     milli = sec * 1000
#     sec = sec
#     min = sec / 60
#     hrs = min / 60
#     days = hrs / 24
#     weeks = days / 7
#     months = days / 30.437
#     years = days / 365.24
#     Y_M_D_H_m_s_ms = str(years) + ":" + str(months) + ":" + str(days) + ":" + str(hrs) + ":" + str(min) + ":" + str(sec) + ":" + str(milli)
#     out = [str(i) for i in [milli, sec, min, hrs, days, weeks, months, years, Y_M_D_H_m_s_ms]]
#     return out

# # add options to the menu
# for option in options_convert_from:
#     drop_convert_from.add_command(label=option, command=input_to_seconds(opt = option, inpu = input_time.get()))

# # add menu to widget
# menu_convert_from.config(menu=drop_convert_from)




#place input fieldsm, labels, and button
input_years.pack(in_=frame_year, side="left")
input_months.pack(in_=frame_months, side="left")
input_weeks.pack(in_=frame_weeks, side="left")
input_days.pack(in_=frame_days, side="left")
input_hours.pack(in_=frame_hours, side="left")
input_seconds.pack(in_=frame_seconds, side="left")
input_milliseconds.pack(in_=frame_milliseconds, side="left")

label_years.pack(in_=frame_year, side="right")
label_months.pack(in_=frame_months, side="right")
label_weeks.pack(in_=frame_weeks, side="right")
label_days.pack(in_=frame_days, side="right")
label_hours.pack(in_=frame_hours, side="right")
label_seconds.pack(in_=frame_seconds, side="right")
label_milliseconds.pack(in_=frame_milliseconds, side="right")

convert_button.pack(in_=frame_convert, pady=20)

window.mainloop()