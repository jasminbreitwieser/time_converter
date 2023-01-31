import tkinter as tk
from tkinter import ttk

window =tk.Tk()
window.title("Time Converter")
window.configure()

# Set the window size (Width x Height)
window_width = 250
window_height = 550

## Center the window
# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# find the center point
center_x = int(0.5*screen_width - window_width)
center_y = int(screen_height/8 - window_height/8)
# set the position of the window to the center of the screen
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

## create scrollbars
def scrollbars(window):
    # create main frame
    main_frame= tk.Frame(window)
    main_frame.pack(fill="both", expand=True)
    # create canvas
    canvas = tk.Canvas(main_frame)
    # add scrollbar to the canvas 
    scrollbar_y = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollbar_x = ttk.Scrollbar(main_frame, orient="horizontal", command=canvas.xview)
    # configure the canvas
    canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    # create a second frame inside the canvas
    second_frame = tk.Frame(canvas)
    # add that new frame to a window in the canvas
    canvas.create_window((0,0), window=second_frame, anchor="nw")

    scrollbar_y.pack(side="right", fill="y")
    scrollbar_x.pack(side="bottom", fill="x")
    canvas.pack(side="left", fill="both", expand=True)
    return second_frame

second_frame = scrollbars(window)


times =["Years", "Months", "Weeks", "Days", "Hours", "Minutes", "Seconds", "Milliseconds"]
# organize the position of widgets with tkinter.Frame
frames = {} # a dictionary to hold all frames
for idx,time in enumerate(times):
    frames[time] = tk.Frame(second_frame)
    if idx < len(times)-1:
        frames["inp_inter_{}".format(idx)] = tk.Frame(second_frame)
frames["convert_button"] = tk.Frame(second_frame)
frames["convert_text"] = tk.Frame(second_frame)


# create input and output fields and labelds
defaults = {} # a dictionary to hold all default values
inputfields = {} # a dictionary to hold all input fields
entry_width = 10
inputlabels = {} # a dictionary to hold all input labels
inputlabel_width= 10
for time in times:
    defaults[time] = tk.StringVar(second_frame, value="0") # default value = "0"
    inputfields[time] = tk.Entry(frames[time], textvariable=tk.StringVar(second_frame, value="0"), width=entry_width)
    inputlabels[time] = tk.Label(frames[time], text=time, width=inputlabel_width)
   
# create interframes
inp_interlabels = {} 
for frame in frames.keys():
    if "inp_inter" in frame:
        inp_interlabels["{}".format(frame)] = tk.Label(frames[frame], text="+")


# time conversion
def convert():
    total_times={}
    years, months, weeks, days, hours, minutes, seconds, milliseconds = [float(i.get()) for i in inputfields.values()]
    total_times["Years"] = years + months / 12 + weeks / 52.1429  + days / 365 + hours / 8760 + minutes / 525600 + seconds / 3.154*10**-7 + milliseconds / 3.154*10**-10
    total_times["Months"] = years*12 + months + weeks / 4.34524 + days / 30.4167 + hours / 730.48 + minutes / 43829.1 + seconds / 2629746 + milliseconds / 2.629746*10**-9
    total_times["Weeks"] = years * 52.1429 + months * 4.34524 + weeks + days / 7 + hours / 168 + minutes / 10080 + seconds / 604800 + milliseconds / 6.048*10**-8
    total_times["Days"] = years * 365 + months * 30.4167 + weeks * 7 + days + hours / 24 + minutes / 1440 + seconds / 86400 + milliseconds / 8.64*10**-7
    total_times["Hours"] = years * 8760 + months * 730.48 + weeks * 168 + days * 24 + hours + minutes / 60 + seconds / 3600 + milliseconds / 3.6*10**-6
    total_times["Minutes"] = years * 525600 + months * 43829.1 + weeks * 10080 + days * 1440 + hours * 60 + minutes + seconds / 60 + milliseconds / 60000
    total_times["Seconds"] = years * 3.154*10**7 + months * 2.629746*10**9 + weeks * 6.048*10**8 + days * 8.64*10**7 + hours * 3.6*10**6 + minutes * 60000 + seconds + milliseconds / 1000
    total_times["Milliseconds"] = years * 3.154*10**10 + months * 2.629746*10**12 + weeks * 6.048*10**11 + days * 8.64*10**10 + hours * 3.6*10**9 + minutes * 60000 * 1000 + seconds * 1000 + milliseconds
   
    total_time = years * 365.25 * 24 * 60 * 60 + \
                 months * 30.44 * 24 * 60 * 60 + \
                 weeks * 7 * 24 * 60 * 60 + \
                 days * 24 * 60 * 60 + \
                 hours * 60 * 60 + \
                 minutes * 60 + \
                 seconds + \
                 milliseconds / 1000
    
    total_time_in_years = int(total_time / (365.25 * 24 * 60 * 60))
    total_time = total_time % (365.25 * 24 * 60 * 60)
    total_time_in_months = int(total_time / (30.44 * 24 * 60 * 60))
    total_time = total_time % (30.44 * 24 * 60 * 60)
    total_time_in_weeks = int(total_time / (7 * 24 * 60 * 60))
    total_time = total_time % (7 * 24 * 60 * 60)
    total_time_in_days = int(total_time / (24 * 60 * 60))
    total_time = total_time % (24 * 60 * 60)
    total_time_in_hours = int(total_time / (60 * 60))
    total_time = total_time % (60 * 60)
    total_time_in_minutes = int(total_time / 60)
    total_time = total_time % 60
    total_time_in_seconds = int(total_time)
    total_time_in_milliseconds = int((total_time - total_time_in_seconds) * 1000)
    total_times["Y:M:W:D:h:m:s:ms"] = f"{total_time_in_years} years : {total_time_in_months} months : {total_time_in_weeks} weeks : {total_time_in_days} days : {total_time_in_hours} hours : {total_time_in_minutes} minutes : {total_time_in_seconds} seconds : {total_time_in_milliseconds} milliseconds"
    # round all values to 2 decimal places
    for key in total_times.keys():
        print(type(total_times[key]))
        if type(total_times[key]) == float:
            print(type(total_times[key]))
            total_times[key] = round(total_times[key], 2)
    return total_times

def on_click():
    window_width = 550
    result_win = tk.Toplevel(window)
    result_win.title("Time Converter - Result")
    center_x = int(0.5*screen_width)
    center_y = int(screen_height/8 - window_height / 8)
    # set the position of the window to the center of the screen
    result_win.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    second_frame = scrollbars(result_win)

    frames_out={}
    frames_out["result_text"] = tk.Frame(second_frame)
    frames_out["result_text"].pack()

    outputlabels = {} # a dictionary to hold all input labels
    out_interlabels = {} 
    for time in times:
        try:
            if convert()[time] > 0:
                frames_out[time] = tk.Frame(second_frame)
                frames_out["out_inter_{}".format(time)] = tk.Frame(second_frame)
                outputlabels[time] = tk.Label(frames_out[time], text="{} {}".format(convert()[time], time))
                out_interlabels[time] = tk.Label(frames_out["out_inter_{}".format(time)], text="or")
        except ValueError as ve:
            convert_text["text"] = """You entered an invalid number,\nplease try again.\nUse "." as decimal point (e.g., 2.5)."""
            result_win.destroy()
            return
    frames_out["Y:M:W:D:h:m:s:ms"] = tk.Frame(second_frame)
    outputlabels["Y:M:W:D:h:m:s:ms"] = tk.Label(frames_out["Y:M:W:D:h:m:s:ms"], text = convert()["Y:M:W:D:h:m:s:ms"])

    for frame in frames_out:
        frames_out[frame].pack()

    for output in outputlabels:
        outputlabels[output].pack(in_=frames_out[output], side="right")
    for out_interlabel in out_interlabels:
        out_interlabels[out_interlabel].pack(in_=frames_out["out_inter_{}".format(out_interlabel)], side="left")
    result_text = tk.Label(frames_out["result_text"], text="Result:", fg='#00ff00', height=3)
    result_text.pack()

      
# create convert button
convert_button = tk.Button(frames["convert_button"], text="Convert", relief="raised", bg='#000000', fg='#000000',command=on_click)
convert_text = tk.Label(frames["convert_text"], text="", fg='#ff5733')

#pack
for frame in frames.keys():
    frames[frame].pack()

for input in inputfields.keys():
    inputfields[input].pack(in_=frames[input], side="left")
    inputlabels[input].pack(in_=frames[input], side="right")

for inp_interlabel in inp_interlabels.keys():
    inp_interlabels[inp_interlabel].pack(in_=frames[inp_interlabel], side="left")


convert_button.pack(in_=frames["convert_button"], pady=20)
convert_text.pack(in_=frames["convert_text"])

window.mainloop()