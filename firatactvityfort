from tkinter import *

root = Tk()
root.title("Grid Example")


nums = [
    [19, 8, 71],
    [6, 5, 4],
    [3, 2, 1],
    ['#', 0, '***']
]


for i in range(4):

    
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)

   
    for j in range(3):

       
        frame = Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=1
        )

        
        frame.grid(row=i, column=j, padx=2, pady=2)

       
        label = Label(
            master=frame,
            text=nums[i][j],
            bg="#defff"
        )

        label.pack(padx=10, pady=10)


root.mainloop()