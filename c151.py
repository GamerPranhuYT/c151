from tkinter import*

root=Tk()

root.title("Sales Application")
root.geometry("700x700")
root.configure(bg="yellow")

month_label = Label(root)
profit_label = Label(root)
max_label = Label(root)
min_label = Label(root)

month = ("January", "Feburuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

profits = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)

month_label["text"]=month
profit_label["text"]= profits

def max_profit():
   month = ("January", "Feburuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

   profits = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)
    
   max_profit = max(profits)
   max_profit_index = profits.index(max_profit)
   #print(max_profit_index)

   max_profit_month = month[max_profit_index]
   max_label["text"]= "The maximum profit of "+str(max_profit)+" was recorded in the month of "+str(max_profit_month)
   #print("The maximum profit of "+str(max_profit)+" was recorded in the month of "+str(max_profit_month))
 
def minprofit():
    month = ("January", "Feburuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

    profits = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    #print(min_profit_index)
    
    min_profit_month = month[min_profit_index]
    min_label["text"]="The minimum profit of "+str(min_profit)+" was recorded in the month of "+str(min_profit_month )
    #print("The minimum profit of "+str(min_profit)+" was recorded in the month of "+str(min_profit_month ))
    
month_label.place(relx=0.5, rely=0.2, anchor=CENTER)
profit_label.place(relx=0.5, rely=0.3, anchor=CENTER)
btnmax = Button(root, text="Show maximum profit month", command=max_profit)
btnmax.place(relx=0.5, rely=0.4, anchor=CENTER)
max_label.place(relx=0.5, rely=0.5, anchor=CENTER)

btnmin = Button(root, text="Show minimum profit month", command=minprofit)
btnmin.place(relx=0.5, rely=0.6, anchor=CENTER)
min_label.place(relx=0.5, rely=0.7, anchor=CENTER)
root.mainloop()