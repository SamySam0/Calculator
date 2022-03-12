from tkinter import *
from calculator_class import *
from onClick_Events import *
from tkinter import font as tkFont
from buttonStyle_class import *


root = Tk()
root.title("Calculatrice")
root.geometry("235x328")
root.resizable(0, 0)
root.configure(bg="#646464")

fontStyle = tkFont.Font(size=18)

myFinalDisplay = Label(root, bg="#646464", fg="lightgrey", font=fontStyle)

def equalsEvent():
    myFinalDisplay.configure(text = Calculator(liste_denvoi).calculer())
    myFinalDisplay.grid(row = 0, columnspan=4)
    myFinalDisplay.tkraise()


#def create_button(name, text, value):
#    name = Button(root, text=text)
#    name.value = value

Button_AC = TopButton(root, text="AC", command=onClick_AC)
Button_AC.grid(row = 1, column = 0)

Button1 = NumButton(root, text="1", command=onClick)
Button1.grid(row = 4, column = 0)

Button2 = NumButton(root, text="2", command=onClick2)
Button2.grid(row = 4, column = 1)

Button3 = NumButton(root, text="3", command=onClick3)
Button3.grid(row = 4, column = 2)

Button4 = NumButton(root, text="4", command=onClick4)
Button4.grid(row = 3, column = 0)

Button5 = NumButton(root, text="5", command=onClick5)
Button5.grid(row = 3, column = 1)

Button6 = NumButton(root, text="6", command=onClick6)
Button6.grid(row = 3, column = 2)

Button7 = NumButton(root, text="7", command=onClick7)
Button7.grid(row = 2, column = 0)

Button8 = NumButton(root, text="8", command=onClick8)
Button8.grid(row = 2, column = 1)

Button9 = NumButton(root, text="9", command=onClick9)
Button9.grid(row = 2, column = 2)

Button0 = NumButton(root, text="0", command=onClick0)
Button0.grid(row = 5, column = 1)

Button_add = SideButton(root, text="+", command=onClick_add)
Button_add.grid(row = 4, column = 3)

Button_substract = SideButton(root, text="-", command=onClick_substract)
Button_substract.grid(row = 3, column = 3)

Button_divide = SideButton(root, text="/", command=onClick_divide)
Button_divide.grid(row = 1, column = 3)

Button_multi = SideButton(root, text="x", command=onClick_multi)
Button_multi.grid(row = 2, column = 3)

Button_parenthese_fermee = TopButton(root, text="(", command=onClick_parenthese_fermee)
Button_parenthese_fermee.grid(row = 1, column = 1)

Button_parenthese_ouverte = TopButton(root, text=")", command=onClick_parenthese_ouverte)
Button_parenthese_ouverte.grid(row = 1, column = 2)

Button_crochet_ferme = NumButton(root, text="[", command=onClick_parenthese_fermee)
Button_crochet_ferme.grid(row = 5, column = 0)

Button_crochet_ouvert = NumButton(root, text="]", command=onClick_parenthese_ouverte)
Button_crochet_ouvert.grid(row = 5, column = 2)

Button_equals = SideButton(root, text="=", command=equalsEvent)
Button_equals.grid(row = 5, column = 3)


myDisplay = Label(root, text=liste_denvoi, borderwidth=1, bg="#646464")
myDisplay['font'] = tkFont.Font(size=30)
myDisplay.grid(row = 0, columnspan=4)

root.mainloop()