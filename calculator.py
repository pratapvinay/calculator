from tkinter import *
def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)
    
def btncleardisplay():
    global operator
    operator=''
    text_input.set('')
    
def btnequalsinput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=''


    
root=Tk()
root.title('calculator')
operator=""
text_input=StringVar()
textdisplay=Entry(root,font=('aerial',20,'bold'),textvariable=text_input,bd=30,
                  insertwidth=4,bg='powder blue',justify='right').grid(columnspan=4)

btn7=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='7',padx=16,command=lambda:btnclick(7)).grid(row=1,column=0)
btn8=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='8',padx=16,command=lambda:btnclick(8)).grid(row=1,column=1)
btn9=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='9',padx=16,command=lambda:btnclick(9)).grid(row=1,column=2)

btnadd=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='+',padx=16,command=lambda:btnclick('+')).grid(row=1,column=3)

btn4=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='4',padx=16,command=lambda:btnclick(4)).grid(row=2,column=0)
btn5=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='5',padx=16,command=lambda:btnclick(5)).grid(row=2,column=1)
btn6=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='6',padx=16,command=lambda:btnclick(6)).grid(row=2,column=2)

btnsub=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='-',padx=16,command=lambda:btnclick('-')).grid(row=2,column=3)

btn1=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='1',padx=16,command=lambda:btnclick(1)).grid(row=3,column=0)
btn2=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='2',padx=16,command=lambda:btnclick(2)).grid(row=3,column=1)
btn3=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='3',padx=16,command=lambda:btnclick(3)).grid(row=3,column=2)

btnmul=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='*',padx=16,command=lambda:btnclick('*')).grid(row=3,column=3)

btnzero=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='0',padx=16,command=lambda:btnclick(0)).grid(row=4,column=0)
btnclear=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='C',padx=16,command=btncleardisplay).grid(row=4,column=1)
btnequals=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='=',padx=16,command=btnequalsinput).grid(row=4,column=2)

btndiv=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='/',padx=16,command=lambda:btnclick('/')).grid(row=4,column=3)

root.mainloop()