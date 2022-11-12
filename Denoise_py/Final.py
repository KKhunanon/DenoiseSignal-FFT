from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

window = Tk()
window.title("Denoise")

#-------------------------"Equation 1"-----------------------------------
label_Equation_1 = Label(window, font=("Helvetica", 11, "bold"), text="Equation 1")
label_Equation_1.grid(row=0, column=1, pady=20)

Equation_1_frame = Frame(window, bd=7, width=100, relief=RIDGE )
Equation_1_frame.grid(row=1, column=0, columnspan=3, padx=20)

label_Type_1 = Label(Equation_1_frame, font=("Helvetica", 8, "bold"), text="Type : ")
label_Type_1.grid(row=2, column=0, pady=15)
drop_Type_1 = StringVar()
drop_Type_1.set("select")
drop_1 = OptionMenu(Equation_1_frame, drop_Type_1, "sin", "cos")
drop_1.grid(row=2, column=1)

label_Amplitude_1 = Label(Equation_1_frame, font=("Helvetica", 8, "bold"), text="Amplitude : ")
label_Amplitude_1.grid(row=3, column=0, pady=15)
entry_Amplitude_1 = Entry(Equation_1_frame, borderwidth=2)
entry_Amplitude_1.grid(row=3, column=1)

label_Frequency_1 = Label(Equation_1_frame, font=("Helvetica", 8, "bold"), text="Frequency : ")
label_Frequency_1.grid(row=4, column=0)
entry_Frequency_1 = Entry(Equation_1_frame, borderwidth=2)
entry_Frequency_1.grid(row=4, column=1)

#-------------------------"Equation 2"-----------------------------------
label_Equation_2 = Label(window, font=("Helvetica", 11, "bold"),text="Equation 2")
label_Equation_2.grid(row=5, column=1, pady=25)

Equation_2_frame = Frame(window, bd=7, width=100, relief=RIDGE )
Equation_2_frame.grid(row=6, column=0, columnspan=3)

label_Type_2 = Label(Equation_2_frame, font=("Helvetica", 8, "bold"), text="Type : ")
label_Type_2.grid(row=6, column=0, pady=15)
drop_Type_2 = StringVar()
drop_Type_2.set("select")
drop_2 = OptionMenu(Equation_2_frame, drop_Type_2, "sin", "cos")
drop_2.grid(row=6, column=1)

label_Amplitude_2 = Label(Equation_2_frame, font=("Helvetica", 8, "bold"), text="Amplitude : ")
label_Amplitude_2.grid(row=7, column=0, pady=15)
entry_Amplitude_2 = Entry(Equation_2_frame, borderwidth=2)
entry_Amplitude_2.grid(row=7, column=1)

label_Frequency_2 = Label(Equation_2_frame, font=("Helvetica", 8, "bold"), text="Frequency : ")
label_Frequency_2.grid(row=8, column=0)
entry_Frequency_2 = Entry(Equation_2_frame, borderwidth=2)
entry_Frequency_2.grid(row=8, column=1)

#-------------------------"Slide Bar"-----------------------------------
slide_bar = Scale(window, from_=0, to=30, orient=HORIZONTAL)
slide_bar.grid(row=9,column=1, pady=20)
label_NoiseLevel = Label(window, font=("Helvetica", 9, "bold"), text="[Noise Level]")
label_NoiseLevel.grid(row=10, column=1)

#--------------------------"Set-grap"-------------------------
#--fig 1
f = Figure(figsize=(8, 6), dpi=100)
pic1 = f.add_subplot(211)
pic1.set_xlabel("Time(t)", fontsize = 8)
pic1.set_ylabel("Amplitude", fontsize= 8)
pic1.set_title("Noisy vs Original",fontsize = 12)
pic1.legend(loc='upper right')
pic1.set_facecolor('black')
pic1.grid('on', linestyle='--')
#--fig 2
pic2 = f.add_subplot(212)
pic2.set_xlabel("Time(t)", fontsize = 8)
pic2.set_ylabel("Amplitude", fontsize= 8)
pic2.set_title("Recovered vs Original",fontsize = 12)
pic2.legend(loc='upper right')
pic2.set_facecolor('black')
pic2.grid('on', linestyle='--')
f.tight_layout()
canvas = FigureCanvasTkAgg(f, master = window)
canvas.draw()

get_widz = canvas.get_tk_widget()
get_widz.grid(row=0, column=3, rowspan=13, padx=5)

#-------------------------"Reset Button // Reset Function"-----------------------------------
def reset():
    drop_Type_1.set("select")
    entry_Amplitude_1.delete(0, END)
    entry_Frequency_1.delete(0, END)

    drop_Type_2.set("select")
    entry_Amplitude_2.delete(0, END)
    entry_Frequency_2.delete(0, END)

    #--fig 1
    f = Figure(figsize=(8, 6), dpi=100)
    pic1 = f.add_subplot(211)
    pic1.set_xlabel("Time(t)", fontsize = 8)
    pic1.set_ylabel("Amplitude", fontsize= 8)
    pic1.set_title("Noisy vs Original",fontsize = 12)
    pic1.legend(loc='upper right')
    pic1.set_facecolor('black')
    pic1.grid('on', linestyle='--')
    #--fig 2
    pic2 = f.add_subplot(212)
    pic2.set_xlabel("Time(t)", fontsize = 8)
    pic2.set_ylabel("Amplitude", fontsize= 8)
    pic2.set_title("Recovered vs Original",fontsize = 12)
    pic2.legend(loc='upper right')
    pic2.set_facecolor('black')
    pic2.grid('on', linestyle='--')
    f.tight_layout()
    canvas = FigureCanvasTkAgg(f, master = window)
    canvas.draw()
    
    get_widz = canvas.get_tk_widget()
    get_widz.grid(row=0, column=3, rowspan=13)


reset_button = Button(window, text="Reset", padx=10, pady=5, command=reset)
reset_button.grid(row=11, column=1, pady=25)

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
    pic1.set_facecolor('black')
    pic1.grid('on', linestyle='--')
    #--fig 2
    pic2 = f.add_subplot(212)
    pic2.plot(t,1000*inve_ft.reshape((1000,)),label="Re sound", color="lime")
    pic2.plot( t,Sum,label="Org sound",color="orange")
    pic2.set_xlabel("Time(t)", fontsize = 8)
    pic2.set_ylabel("Amplitude", fontsize= 8)
    pic2.set_title("Recovered vs Original",fontsize = 12)
    pic2.legend(loc='upper right')
    pic2.set_facecolor('black')
    pic2.grid('on', linestyle='--')
    f.tight_layout()
    canvas = FigureCanvasTkAgg(f, master = window)
    canvas.draw()
    
    get_widz = canvas.get_tk_widget()
    get_widz.grid(row=0, column=3, rowspan=13)

def more_detail():
    NoiseLevel = int(slide_bar.get())
    Sum = set_data1()+set_data2()

    tpCount     = len(Sum)
    values      = np.arange(int(tpCount/2))
    timePeriod  = tpCount/1000
    frequencies = values/timePeriod
    
    #--------------"Noisy vs Original"-----------------------------------
    noise = noise_add(NoiseLevel)
    noisy=noise+Sum
    fig, axs = plt.subplots(2, 1)
    axs[0].grid(alpha = 0.3)
    axs[0].plot(t,noisy,label="Re sound", color="dodgerblue")
    axs[0].plot(t, Sum ,label="Org sound",color="orange")
    axs[0].set_xlabel("Time(t)", fontsize = 10)
    axs[0].set_ylabel("Amplitude", fontsize= 10)
    axs[0].set_title("Noisy vs Original",fontsize = 15) #Show graph
    axs[0].legend(loc='upper right')
    axs[0].set_facecolor('black')
    axs[0].grid('on', linestyle='--')

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
    axs[1].grid(alpha = 0.3)
    axs[1].plot(t,1000*inve_ft.reshape((1000,)),label="Re sound", color="lime")
    axs[1].plot( t, Sum ,label="Org sound",color="orange")
    axs[1].set_xlabel("Time(t)", fontsize = 10)
    axs[1].set_ylabel("Amplitude", fontsize= 10)
    axs[1].set_title("Recovered vs Original",fontsize = 15)
    axs[1].legend(loc='upper right')
    axs[1].set_facecolor('black')
    axs[1].grid('on', linestyle='--')
    fig.tight_layout()
    plt.show()

generate_button = Button(window, text="Generate", padx=10, pady=5 , command=generate)
generate_button.grid(row=12, column=1)


moreDetail_button = Button(window, text="More detail", padx=10, pady=5 , command=more_detail)
moreDetail_button.grid(row=13, column=3, padx=360, pady=10)

window.geometry("1070x720+250+30")
window.mainloop()