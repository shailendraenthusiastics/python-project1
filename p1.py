from tkinter import *
root=Tk()
root.geometry("500x300")
def show_result():
    print("your vote submitted successfully")
show_result()
Label(root,text="             Loksabha Election 2024",font="ar 15 bold").grid(row=0,column=3)
# fied variable
voterName=Label(root,text="VoterName").grid(row=1,column=2)
Voter_idno=Label(root,text="Voter-id_No").grid(row=2,column=2)
constituency=Label(root,text="Constituency").grid(row=3,column=2)
choose_party=Label(root,text="Choose party :").grid(row=4,column=2)
# value store to variable
voterName=StringVar
Voter_idno=IntVar
constituency=StringVar
choose_party=StringVar
# entry widget for taking input
name=Entry(root,textvariable=voterName).grid(row=1,column=3)
Id=Entry(root,textvariable=Voter_idno).grid(row=2,column=3)
const=Entry(root,textvariable=constituency).grid(row=3,column=3)
#party=Entry(root,textvariable=choose_party).grid(row=4,column=3)
button=Checkbutton(root,text="BJP").grid(row=4,column=3)
button=Checkbutton(root,text="Congress").grid(row=4,column=4)
# submit button
Button(text="Submit",command=show_result).grid(row=5,column=3)
root.mainloop()
