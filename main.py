import tkinter as tk

window =tk.Tk()
window.title("Time Converter")
window.configure()

# Set the window size (Width x Height)
window_width = 600
window_height = 1000

## Center the window
# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

times =["Years", "Months", "Weeks", "Days", "Hours", "Minutes", "Seconds", "Milliseconds"]
# organize the position of widgets with tkinter.Frame
frames = {} # a dictionary to hold all frames
for idx,time in enumerate(times):
    frames[time] = tk.Frame(window)
    if idx < len(times)-1:
        frames["inp_inter_{}".format(idx)] = tk.Frame(window)
frames["convert_button"] = tk.Frame(window)
frames["convert_text"] = tk.Frame(window)
for idx,time in enumerate(times):
    frames["out_{}".format(time)] = tk.Frame(window)
    frames["out_inter_{}".format(idx)] = tk.Frame(window)


# create input and output fields and labelds
defaults = {} # a dictionary to hold all default values
inputfields = {} # a dictionary to hold all input fields
entry_width = 10
inputlabels = {} # a dictionary to hold all input labels
inputlabel_width= 10
outputlabels = {} # a dictionary to hold all input labels
outputlabel_width= 10
outputfields = {} # a dictionary to hold all output fields
outputfield_width = 20
for time in times:
    defaults[time] = tk.StringVar(window, value="0") # default value = "0"
    inputfields[time] = tk.Entry(frames[time], textvariable=tk.StringVar(window, value="0"), width=entry_width)
    inputlabels[time] = tk.Label(frames[time], text=time, width=inputlabel_width)
    outputlabels[time] = tk.Label(frames["out_{}".format(time)], text=time, width=outputlabel_width)
    outputfields[time] = tk.Label(frames["out_{}".format(time)], text = "0.0", width=outputfield_width, fg='#ff5733')

# create interframes
inp_interlabels = {} 
for frame in frames.keys():
    if "inp_inter" in frame:
        inp_interlabels["{}".format(frame)] = tk.Label(frames[frame], text="+")

out_interlabels = {} 
for frame in frames.keys():
    if "out_inter" in frame:
        out_interlabels["{}".format(frame)] = tk.Label(frames[frame], text="or")


# time conversion
def convert():
    total_times={}
    years, months, weeks, days, hours, minutes, seconds, milliseconds = [float(i.get()) for i in inputfields.values()]
    total_times["Years"] = years + months / 12 + weeks / 52.142857142857  + days / 365 + hours / 8760 + minutes / 525600 + seconds / 3.154*10**7 + milliseconds / 3.154*10**10
    total_times["Months"] = years*12 + months + weeks / 4.34524 + days / 30.437 + hours / 730.48 + minutes / 43829.1 + seconds / 2629746 + milliseconds / 2.629746*10**9
    total_times["Weeks"] = years * 52.142857142857 + months * 4.34524 + weeks + days / 7 + hours / 168 + minutes / 10080 + seconds / 604800 + milliseconds / 6.048*10**8
    total_times["Days"] = years * 365 + months * 30.437 + weeks * 7 + days + hours / 24 + minutes / 1440 + seconds / 86400 + milliseconds / 8.64*10**7
    total_times["Hours"] = years * 8760 + months * 730.48 + weeks * 168 + days * 24 + hours + minutes / 60 + seconds / 3600 + milliseconds / 3.6*10**6
    total_times["Minutes"] = years * 525600 + months * 43829.1 + weeks * 10080 + days * 1440 + hours * 60 + minutes + seconds / 60 + milliseconds / 60000
    total_times["Seconds"] = years * 3.154*10**7 + months * 2.629746*10**9 + weeks * 6.048*10**8 + days * 8.64*10**7 + hours * 3.6*10**6 + minutes * 60000 + seconds + milliseconds / 1000
    total_times["Milliseconds"] = years * 3.154*10**10 + months * 2.629746*10**12 + weeks * 6.048*10**11 + days * 8.64*10**10 + hours * 3.6*10**9 + minutes * 60000 * 1000 + seconds * 1000 + milliseconds
    # round all values to 2 decimal places
    for key in total_times.keys():
        total_times[key] = round(total_times[key], 2)
    return total_times

def update_convert_text():
    text_years = "{} Years".format(inputfields["Years"].get())
    convert_text["text"] = "{} and  Months".format(text_years)
def on_click():
    for key in convert().keys():
        outputfields[key]["text"] = convert()[key]
    update_convert_text()
    

# create convert button
convert_button = tk.Button(frames["convert_button"], text="Convert", relief="raised", bg='#000000', fg='#000000',command=on_click)
convert_text = tk.Label(frames["convert_text"], text="Click the button to convert", fg='#ff5733')

#pack
for frame in frames.keys():
    frames[frame].pack()

for input in inputfields.keys():
    inputfields[input].pack(in_=frames[input], side="left")
    inputlabels[input].pack(in_=frames[input], side="right")

for output in outputfields.keys():
    outputfields[output].pack(in_=frames["out_{}".format(output)], side="left")
    outputlabels[output].pack(in_=frames["out_{}".format(output)], side="right")

for inp_interlabel in inp_interlabels.keys():
    inp_interlabels[inp_interlabel].pack(in_=frames[inp_interlabel], side="left")

for out_interlabel in out_interlabels.keys():
    out_interlabels[out_interlabel].pack(in_=frames[out_interlabel], side="left")

convert_button.pack(in_=frames["convert_button"], pady=20)
convert_text.pack(in_=frames["convert_text"])
print(frames)
window.mainloop()