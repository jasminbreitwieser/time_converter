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
frames = {} # a dictionary to hold all frames
frames["years"] = tk.Frame(window)
frames["months"] = tk.Frame(window)
frames["weeks"] = tk.Frame(window)
frames["days"] = tk.Frame(window)
frames["hours"] = tk.Frame(window)
frames["seconds"] = tk.Frame(window)
frames["milliseconds"] = tk.Frame(window)
frames["convert"] = tk.Frame(window)
frames["output"] = tk.Frame(window)

for frame in frames.keys():
    frames[frame].pack()


# create input boxes

# each box needs its own default value,
# otherwise, the change in one value will affect all boxes
default_years = tk.StringVar(window, value="0") # default value = "0"
default_months = tk.StringVar(window, value="0") # default value = "0"
default_weeks = tk.StringVar(window, value="0") # default value = "0"
default_days = tk.StringVar(window, value="0") # default value = "0"
default_hours = tk.StringVar(window, value="0") # default value = "0"
default_seconds = tk.StringVar(window, value="0") # default value = "0"
default_milliseconds = tk.StringVar(window, value="0") # default value = "0"

inputfields = {} # a dictionary to hold all input fields
entry_width = 10
inputfields["years"] = tk.Entry(frames["years"], textvariable=default_years, width=entry_width) 
inputfields["months"] = tk.Entry(frames["months"], textvariable=default_months, width=entry_width) 
inputfields["weeks"] = tk.Entry(frames["weeks"], textvariable=default_weeks, width=entry_width) 
inputfields["days"] = tk.Entry(frames["days"], textvariable=default_days, width=entry_width) 
inputfields["hours"] = tk.Entry(frames["hours"], textvariable=default_hours, width=entry_width) 
inputfields["seconds"] = tk.Entry(frames["seconds"], textvariable=default_seconds, width=entry_width) 
inputfields["milliseconds"] = tk.Entry(frames["milliseconds"], textvariable=default_milliseconds, width=entry_width) 

# create labels
inputlabels = {} # a dictionary to hold all input labels
label_width= 10
inputlabels["years"] = tk.Label(frames["years"], text="Years", width=label_width)
inputlabels["months"] = tk.Label(frames["months"], text="Months", width=label_width)
inputlabels["weeks"] = tk.Label(frames["weeks"], text="Weeks", width=label_width)
inputlabels["days"] = tk.Label(frames["days"], text="Days", width=label_width)
inputlabels["hours"] = tk.Label(frames["hours"], text="Hours", width=label_width)
inputlabels["seconds"] = tk.Label(frames["seconds"], text="Seconds", width=label_width)
inputlabels["milliseconds"] = tk.Label(frames["milliseconds"], text="Milliseconds", width=label_width)

# create convert button
convert_button = tk.Button(frames["convert"], text="Convert", relief="raised", bg='#000000', fg='#000000')



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


#place input fields, labels, and button
for input in inputfields.keys():
    inputfields[input].pack(in_=frames[input], side="left")
    inputlabels[input].pack(in_=frames[input], side="right")



convert_button.pack(in_=frames["convert"], pady=20)

window.mainloop()