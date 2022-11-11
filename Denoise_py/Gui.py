from tkinter import *

window = Tk()
window.title("Denoise")

label_data = Label(window, text="Data")
label_data.grid(row=0, column=1)

#-------------------------"Equation 1"-----------------------------------
label_Equation_1 = Label(window, text="Equation 1")
label_Equation_1.grid(row=1, column=1)

label_Type_1 = Label(window ,text="Type : ")
label_Type_1.grid(row=2, column=0)
drop_Type_1 = StringVar()
drop_1 = OptionMenu(window, drop_Type_1, "Sin", "Cos")
drop_1.grid(row=2, column=1)

label_Amplitude_1 = Label(window ,text="Amplitude : ")
label_Amplitude_1.grid(row=3, column=0)
entry_Amplitude_1 = Entry(window)
entry_Amplitude_1.grid(row=3, column=1)

label_Frequency_1 = Label(window ,text="Frequency : ")
label_Frequency_1.grid(row=4, column=0)
entry_Frequency_1 = Entry(window)
entry_Frequency_1.grid(row=4, column=1)

#-------------------------"Equation 2"-----------------------------------
label_Equation_2 = Label(window ,text="Equation 2")
label_Equation_2.grid(row=5, column=1)

label_Type_2 = Label(window ,text="Type : ")
label_Type_2.grid(row=6, column=0)
drop_Type_2 = StringVar()
drop_2 = OptionMenu(window, drop_Type_2, "Sin", "Cos")
drop_2.grid(row=6, column=1)

label_Amplitude_2 = Label(window ,text="Amplitude : ")
label_Amplitude_2.grid(row=7, column=0)
entry_Amplitude_2 = Entry(window)
entry_Amplitude_2.grid(row=7, column=1)

label_Frequency_2 = Label(window ,text="Frequency : ")
label_Frequency_2.grid(row=8, column=0)
entry_Frequency_2 = Entry(window)
entry_Frequency_2.grid(row=8, column=1)

#-------------------------"Slide Bar"-----------------------------------
label_NoiseLevel = Label(window, text="[Noise Level]")
label_NoiseLevel.grid(row=10, column=1)
slide_bar = Scale(window, from_=0, to=30, orient=HORIZONTAL)
slide_bar.grid(row=9,column=1)

#-------------------------"Reset Button"-----------------------------------
reset_button = Button(window, text="Reset")
reset_button.grid(row=11, column=1)

#-------------------------"Generate Button"-----------------------------------
generate_button = Button(window, text="Generate")
generate_button.grid(row=12, column=1)




window.geometry("500x500")
window.mainloop()