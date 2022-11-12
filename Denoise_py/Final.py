from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

window = Tk()
window.title("Denoise")

#label_data = Label(window, text="Data")
#label_data.grid(row=0, column=0, columnspan=2)

#-------------------------"Equation 1"-----------------------------------
label_Equation_1 = Label(window, text="Equation 1")
label_Equation_1.grid(row=1, column=1)

label_Type_1 = Label(window ,text="Type : ")
label_Type_1.grid(row=2, column=0)
drop_Type_1 = StringVar()
drop_Type_1.set("select")
drop_1 = OptionMenu(window, drop_Type_1, "sin", "cos")
drop_1.grid(row=2, column=1)

label_Amplitude_1 = Label(window ,text="Amplitude : ")
label_Amplitude_1.grid(row=3, column=0)
entry_Amplitude_1 = Entry(window, borderwidth=2)
entry_Amplitude_1.grid(row=3, column=1)

label_Frequency_1 = Label(window ,text="Frequency : ")
label_Frequency_1.grid(row=4, column=0)
entry_Frequency_1 = Entry(window, borderwidth=2)
entry_Frequency_1.grid(row=4, column=1)

#-------------------------"Equation 2"-----------------------------------
label_Equation_2 = Label(window ,text="Equation 2")
label_Equation_2.grid(row=5, column=1)

label_Type_2 = Label(window ,text="Type : ")
label_Type_2.grid(row=6, column=0)
drop_Type_2 = StringVar()
drop_Type_2.set("select")
drop_2 = OptionMenu(window, drop_Type_2, "sin", "cos")
drop_2.grid(row=6, column=1)

label_Amplitude_2 = Label(window ,text="Amplitude : ")
label_Amplitude_2.grid(row=7, column=0)
entry_Amplitude_2 = Entry(window, borderwidth=2)
entry_Amplitude_2.grid(row=7, column=1)

label_Frequency_2 = Label(window ,text="Frequency : ")
label_Frequency_2.grid(row=8, column=0)
entry_Frequency_2 = Entry(window, borderwidth=2)
entry_Frequency_2.grid(row=8, column=1)

#-------------------------"Slide Bar"-----------------------------------
label_NoiseLevel = Label(window, text="[Noise Level]")
label_NoiseLevel.grid(row=10, column=1)
slide_bar = Scale(window, from_=0, to=30, orient=HORIZONTAL)
slide_bar.grid(row=9,column=1)

#-------------------------"Reset Button // Reset Function"-----------------------------------
def reset():
    drop_Type_1.set("select")
    entry_Amplitude_1.delete(0, END)
    entry_Frequency_1.delete(0, END)

    drop_Type_2.set("select")
    entry_Amplitude_2.delete(0, END)
    entry_Frequency_2.delete(0, END)


reset_button = Button(window, text="Reset", padx=10, pady=5, command=reset)
reset_button.grid(row=11, column=1)

#-------------------------"Generate Button // Generate Function"-----------------------------------
dt  =0.001                                                          
t = np.arange(0,1,dt)

def noise_add(val):                               
    return val*np.random.sample(1000)-7

def set_data1():
    Amplitude_1 = int(entry_Amplitude_1.get())
    Type_1 = (drop_Type_1.get())
    Frequency_1 = int(entry_Frequency_1.get()) 
    return (eval("{amp_data1}*np.{type_data1}( 2*np.pi * {fr_data1} * t)".format(amp_data1 =Amplitude_1, type_data1 = Type_1, fr_data1 = Frequency_1)))

def set_data2():
    Amplitude_2 = int(entry_Amplitude_2.get())
    Type_2 = (drop_Type_2.get())
    Frequency_2 = int(entry_Frequency_2.get()) 
    return (eval("{amp_data2}*np.{type_data2}( 2*np.pi * {fr_data2} * t)".format(amp_data2 =Amplitude_2, type_data2 = Type_2, fr_data2 = Frequency_2)))

def generate():
    NoiseLevel = int(slide_bar.get())
    Sum = set_data1()+set_data2()

    tpCount     = len(Sum)
    values      = np.arange(int(tpCount/2))
    timePeriod  = tpCount/1000
    frequencies = values/timePeriod
    
    #--------------"Noisy vs Original"-----------------------------------
    noise = noise_add(NoiseLevel)
    noisy=noise+Sum

    #--------------"Recovered vs Original"-----------------------------------
    # Frequency domain representation
    ft = np.fft.fft(noisy)/len(noisy)      
    tpCount     = len(noisy)
    values      = np.arange(int(tpCount/2))
    timePeriod  = tpCount/1000
    frequencies = values/timePeriod
    psd=2*abs(ft)
    indices = [psd > 2]
    filt_ft = ft*indices
    inve_ft = np.fft.ifft(filt_ft)
    dt = 0.001                                                          
    t = np.arange(0,1,dt)

    #--fig 1
    f = Figure(figsize=(8, 6), dpi=100)
    pic1 = f.add_subplot(211)
    pic1.plot(t,noisy,label="Noisy", color="dodgerblue")
    pic1.plot(t,Sum,label="Org sound",color="orange",linewidth=2.5)
    pic1.set_xlabel("Time(t)", fontsize = 8)
    pic1.set_ylabel("Amplitude", fontsize= 8)
    pic1.set_title("Noisy vs Original",fontsize = 12)
    pic1.legend(loc='upper right')
    #--fig 2
    pic2 = f.add_subplot(212)
    pic2.plot(t,1000*inve_ft.reshape((1000,)),label="Re sound", color="lime")
    pic2.plot( t,Sum,label="Org sound",color="orange")
    pic2.set_xlabel("Time(t)", fontsize = 8)
    pic2.set_ylabel("Amplitude", fontsize= 8)
    pic2.set_title("Recovered vs Original",fontsize = 12)
    pic2.legend(loc='upper right')
    f.tight_layout()
    canvas = FigureCanvasTkAgg(f, master = window)
    canvas.draw()
    
    get_widz = canvas.get_tk_widget()
    get_widz.grid(row=0, column=3, rowspan=13)



generate_button = Button(window, text="Generate", padx=10, pady=5 , command=generate)
generate_button.grid(row=12, column=1)

window.geometry("1000x700+500+150")
window.mainloop()