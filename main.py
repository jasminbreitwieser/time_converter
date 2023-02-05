import tkinter as tk
from tkinter import ttk

def create_window(root=None):
    # create a window
    if root == None:
        window =tk.Tk()
    else:
        window = tk.Toplevel(root)
    return window

def screen_width(window):
    return window.winfo_screenwidth()

def screen_height(window):
    return window.winfo_screenheight()


def window_settings(window, window_title, screen_width, screen_height, x, y, window_width, window_height):
    window.title(window_title)
    window.configure()
    # find the center point
    center_x = int(0.5*screen_width - x)
    center_y = int(screen_height/8 - y/8)
    # set the position of the window 
    window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


def scrollbars(main_frame, canvas, second_frame):
    # add scrollbar to the canvas 
    scrollbar_y = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollbar_x = ttk.Scrollbar(main_frame, orient="horizontal", command=canvas.xview)
    # configure the canvas
    canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    # add that new frame to a window in the canvas
    canvas.create_window((0,0), window=second_frame, anchor="nw")
    return scrollbar_x, scrollbar_y

def create_input_frames(times, inner_frame=None):
    frames = {} # a dictionary to hold all frames
    for idx,time in enumerate(times):
        frames[time] = tk.Frame(inner_frame)
        if idx < len(times)-1:
            frames["inp_inter_{}".format(idx)] = tk.Frame(inner_frame)
    frames["convert_button"] = tk.Frame(inner_frame)
    frames["convert_text"] = tk.Frame(inner_frame)
    return frames

# create input fields
def create_default_values(inner_frame=None, val="0"):
    return tk.StringVar(second_frame, value=val) # default value = "0"
def create_inputfield(frame, textvar, entry_width=10):
    return tk.Entry(frame, textvariable=textvar, width=entry_width)
def create_inputlabel(frame, text, width=10):
    return tk.Label(frame, text=text, width=width)
def create_interlabel(frame):
    return tk.Label(frame, text="+")   
def create_interlabels(frames):
    interlabels = {}
    for frame in frames.keys():
        if "inp_inter" in frame:
            interlabels["{}".format(frame)] = create_interlabel(frames[frame])
    return interlabels

def create_input_fields(times, frames, inner_frame=None):
    defaults = {} # a dictionary to hold all default values
    inputfields = {} # a dictionary to hold all input fields
    inputlabels = {} # a dictionary to hold all input labels
    
    for time in times:
        defaults[time] = create_default_values(inner_frame)
        inputfields[time] = create_inputfield(frames[time], defaults[time])
        inputlabels[time] = create_inputlabel(frames[time], time)
    return defaults, inputfields, inputlabels

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


def create_output_frames(inner_frame=None):
    frames_out = {}
    frames_out["result_text"] = tk.Frame(inner_frame)
    return frames_out

def create_output_label(frame, time):
    return tk.Label(frame, text="{} {}".format(convert()[time], time))

def create_output_interlabel(frame):
    return tk.Label(frame, text="or")

def reset():
    for time in times:
        inputfields[time].delete(0, "end")
        inputfields[time].insert(0, 0)
def on_click_reset(win):
    reset()
    win.destroy()



def on_click_convert():
    # create a new window
    result_win = create_window(root=window)
    window_settings(result_win, "Time Converter - Result", screen_width(result_win), screen_height(result_win), 0, 550, 550, 550)

    main_frame_out = tk.Frame(result_win)
    canvas_out = tk.Canvas(main_frame_out)
    second_frame_out = tk.Frame(canvas_out)
    main_frame_out.pack(fill="both", expand=True)
    second_frame_out.pack(fill="both", expand=True)
    scrollbar_x_out, scrollbar_y_out = scrollbars(main_frame_out, canvas_out, second_frame_out)
    frames_out = create_output_frames(inner_frame=second_frame_out)
    #defaults, inputfields, inputlabels = create_input_fields(times, frames, inner_frame=second_frame_out)


    # frames_out={}
    # frames_out["result_text"] = tk.Frame(second_frame_out)
    # frames_out["result_text"].pack()
    outputlabels = {} # a dictionary to hold all input labels
    out_interlabels = {} 
    for time in times:
        try:
            if convert()[time] > 0:
                frames_out[time] = tk.Frame(second_frame_out)
                frames_out["out_inter_{}".format(time)] = tk.Frame(second_frame_out)
                outputlabels[time] = create_output_label(frames_out[time], time)
                out_interlabels[time] = create_output_interlabel(frames_out["out_inter_{}".format(time)])
        except ValueError as ve:
            convert_text["text"] = """You entered an invalid number,\nplease try again.\nUse "." as decimal point (e.g., 2.5)."""
            result_win.destroy()
            return

    if len(frames_out) > 1:
        frames_out["Y:M:W:D:h:m:s:ms"] = tk.Frame(second_frame_out)
        outputlabels["Y:M:W:D:h:m:s:ms"] = tk.Label(frames_out["Y:M:W:D:h:m:s:ms"], text = convert()["Y:M:W:D:h:m:s:ms"])
    frames_out["reset_button"] = tk.Frame(second_frame_out)

    # create a reset button
    reset_button = tk.Button(frames_out["reset_button"], text="Reset", command=lambda: on_click_reset(result_win))

    # pack
    scrollbar_x_out.pack(side="bottom", fill="x")
    scrollbar_y_out.pack(side="right", fill="y")
    canvas_out.pack(side="left", fill="both", expand=True)

    for frame in frames_out:
        frames_out[frame].pack()

    for output in outputlabels:
        outputlabels[output].pack(in_=frames_out[output], side="right")
    for out_interlabel in out_interlabels:
        out_interlabels[out_interlabel].pack(in_=frames_out["out_inter_{}".format(out_interlabel)], side="left")
    result_text = tk.Label(frames_out["result_text"], text="Result:", fg='#00ff00', height=3)
    result_text.pack()
    reset_button.pack(in_=frames_out["reset_button"], side="bottom")


times =["Years", "Months", "Weeks", "Days", "Hours", "Minutes", "Seconds", "Milliseconds"]

window = create_window()
window_settings(window, "Time Converter", screen_width(window), screen_height(window), 250, 550, 250, 550)
main_frame = tk.Frame(window)
canvas = tk.Canvas(main_frame)
second_frame = tk.Frame(canvas)

# main_frame and second_frame are needed for the scrollbars
main_frame.pack(fill="both", expand=True)
second_frame.pack(fill="both", expand=True)

scrollbar_x, scrollbar_y = scrollbars(main_frame, canvas, second_frame)
frames = create_input_frames(times, inner_frame=second_frame)
defaults, inputfields, inputlabels = create_input_fields(times, frames, inner_frame=second_frame)
interlabels = create_interlabels(frames)

# create convert button
convert_button = tk.Button(frames["convert_button"], text="Convert", relief="raised", bg='#000000', fg='#000000',command=on_click_convert)
convert_text = tk.Label(frames["convert_text"], text="", fg='#ff5733')

#pack
scrollbar_x.pack(side="bottom", fill="x")
scrollbar_y.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

for frame in frames.keys():
    frames[frame].pack()

for input in inputfields.keys():
    inputfields[input].pack(in_=frames[input], side="left")
    inputlabels[input].pack(in_=frames[input], side="right")

for inp_interlabel in interlabels.keys():
    interlabels[inp_interlabel].pack(in_=frames[inp_interlabel], side="left")


convert_button.pack(in_=frames["convert_button"], pady=20)
convert_text.pack(in_=frames["convert_text"])

window.mainloop()