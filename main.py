import customtkinter
from tkinter import *
from tkinter import messagebox
import database

app =  customtkinter.CTk()
app.title('Data Entry By Oussama Hamdaoui')
app.geometry('700x600')
app.config(bg='#E3CF57')
app.resizable(FALSE,FALSE)

font1 = ('Arial',30,'bold')
font2 = ('Arial',20,'bold')

def search_course():
    selection = variable3.get()
    if selection != 'Select':
        row = database.search_course(selection)
        id_result_label.configure(text = row[0])
        name_result_label.configure(text = row[1])
        duration_result_label.configure(text = row[2])
        format_result_label.configure(text = row[3])
        langauge_result_label.configure(text = row[4])
        price_result_label.configure(text = row[5])
    else:
        messagebox.showerror('Error','Select ID')
        

def insert_ids_options():
    ids = database.fetch_all_ids()
    ids_options.configure(values = ids)

def new_course():
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    variable1.set('1 Month')
    variable2.set('')
    langauge_entry.delete(0,END)
    price_entry.delete(0,END)
    
def submit_course():
    id = id_entry.get()
    name = name_entry.get()
    duration = variable1.get()
    format = variable2.get()
    langauge = langauge_entry.get()
    price = price_entry.get()
    try:
        if not (id and name and duration and format and langauge and price ):
            messagebox.showerror('Error','Enter All Fields.')
        elif database.id_exists(id):
            messagebox.showerror('Error','ID Already Exist.')
        else:
            price_value = int(price)
            database.insert_course(id,name,duration,format,langauge,price_value)
            insert_ids_options()
            messagebox.showinfo('Succes','Data Has Been Inserted.')
    except ValueError:
        messagebox.showerror('Error','Price Should Be An Integer.')
    except:
        messagebox.showerror('Error','Error Occured.')
        

title_lable = customtkinter.CTkLabel(app,font=font1,text='Courses Data Entry:',text_color='#fff',bg_color='#131314')
title_lable.place(x=25,y=20)

frame1 = customtkinter.CTkFrame(app,bg_color='#131314',fg_color='#292933',corner_radius=10,border_width=2,border_color='#0f0',width=650,height=230)
frame1.place(x=25,y=70)

frame2 = customtkinter.CTkFrame(app,bg_color='#131314',fg_color='#292933',corner_radius=10,border_width=2,border_color='#0f0',width=650,height=200)
frame2.place(x=25,y=350)



id_label = customtkinter.CTkLabel(frame1,font=font2,text='Course ID',text_color='#fff',bg_color='#292933')
id_label.place(x=50,y=15)

id_entry = customtkinter.CTkEntry(frame1,font=font2,text_color='#000',fg_color='#fff',border_color='#B2016C',border_width=2,width=150)
id_entry.place(x=50,y=45)

name_label = customtkinter.CTkLabel(frame1,font=font2,text='Course Name',text_color='#fff',bg_color='#292933')
name_label.place(x=245,y=15)

name_entry = customtkinter.CTkEntry(frame1,font=font2,text_color='#000',fg_color='#B2016C',border_width=2,width=150)
name_entry.place(x=245,y=45)

duration_label = customtkinter.CTkLabel(frame1,font=font2,text='Course Duration',bg_color='#292933',text_color='#fff')
duration_label.place(x=445,y=15)

variable1 =  StringVar()
options = ['1 Month','2 Months','3 Months']

duration_options = customtkinter.CTkComboBox(frame1, font=font2, text_color='#000',fg_color='#fff',dropdown_hover_color='#B2016C',button_color='#B2016C',button_hover_color='#B2016C',border_color='#B2016C',width=150,variable=variable1,values=options,state='readonly')
duration_options.set('1 Month')
duration_options.place(x=445,y=45)

format_label = customtkinter.CTkLabel(frame1,font=font2,text='Course Format :',text_color='#fff',bg_color='#292933')
format_label.place(x=40,y=90)



variable2 = StringVar()
rb1 =  customtkinter.CTkRadioButton(frame1,text='Online',fg_color='#B2016C',hover_color='#B2016C',font=font2,variable=variable2,value='Online')
rb2 =  customtkinter.CTkRadioButton(frame1,text='Class',fg_color='#B2016C',hover_color='#B2016C',font=font2,variable=variable2,value='Class')
rb1.place(x=40,y=125)
rb2.place(x=140,y=125)

langauge_label =customtkinter.CTkLabel(frame1,font=font2,text='Course Langauge',text_color='#fff',bg_color='#292933')
langauge_label.place(x=245,y=90)

langauge_entry = customtkinter.CTkEntry(frame1,font=font2,text_color='#000',fg_color='#fff',border_color='#B2016C',border_width=2,width=150)
langauge_entry.place(x=245,y=120)

price_label = customtkinter.CTkLabel(frame1,font=font2,text='Course Price',text_color='#fff', bg_color='#292933')
price_label.place(x=445,y=90)

price_entry = customtkinter.CTkEntry(frame1,font=font2,text_color='#000',fg_color='#fff',border_color='#B2016C',border_width=2,width=150)
price_entry.place(x=445,y=120)




submit_button = customtkinter.CTkButton(frame1,command=submit_course,font=font2,text_color='#fff',text='Submit',fg_color='#02ab10',hover_color='#02920D',bg_color='#292933',cursor ='hand2',corner_radius=5,width=100)
submit_button.place(x=200,y=170)

clear_button = customtkinter.CTkButton(frame1,command=new_course,font=font2,text_color='#fff',text='New Entry',fg_color='#F45E02',hover_color='#CB4E01',bg_color='#292933',cursor ='hand2',corner_radius=5,width=100)
clear_button.place(x=330,y=170)


search_label = customtkinter.CTkLabel(app,font=font1,text='Search By ID:',text_color='#fff',bg_color='#131314' ) 
search_label.place(x=25,y=310)


variable3 = StringVar()

ids_options = customtkinter.CTkComboBox(app,font=font2,text_color='#000',dropdown_hover_color='#B2016C',button_color='#B2016C',button_hover_color='#B2016C',border_color='#B2016C',width=150,variable=variable3,state='readonly')
ids_options.set('Select')
ids_options.place(x=250,y=312)

search_button = customtkinter.CTkButton(app,command=search_course,font=font2,text_color='#fff',text='Search',fg_color='#1345F9',hover_color='#0029BE',bg_color='#292933',cursor='hand2',corner_radius=5,width=100)
search_button.place(x=420,y=312)

id_label = customtkinter.CTkLabel(frame2,font=font2,text='Course ID',text_color='#fff',bg_color='#292933')
id_label.place(x=50,y=15)

name_label = customtkinter.CTkLabel(frame2,font=font2,text='Course Name',text_color='#fff',bg_color='#292933')
name_label.place(x=245,y=15)

duration_label = customtkinter.CTkLabel(frame2,font=font2,text='Course Duration',bg_color='#292933',text_color='#fff')
duration_label.place(x=445,y=15)

format_label = customtkinter.CTkLabel(frame2,font=font2,text='Course Format :',text_color='#fff',bg_color='#292933')
format_label.place(x=40,y=90)

langauge_label =customtkinter.CTkLabel(frame2,font=font2,text='Course Langauge',text_color='#fff',bg_color='#292933')
langauge_label.place(x=245,y=90)

price_label = customtkinter.CTkLabel(frame2,font=font2,text='Course Price',text_color='#fff', bg_color='#292933')
price_label.place(x=445,y=90)

id_result_label = customtkinter.CTkLabel(frame2,font=font2,text='',text_color='#0f0',bg_color='#292933')
id_result_label.place(x=50,y=45)

name_result_label = customtkinter.CTkLabel(frame2,font=font2,text='',text_color='#0f0',bg_color='#292933')
name_result_label.place(x=245,y=45)

duration_result_label = customtkinter.CTkLabel(frame2,font=font2,text='',text_color='#0f0',bg_color='#292933')
duration_result_label.place(x=445,y=45)

format_result_label = customtkinter.CTkLabel(frame2,font=font2,text='',text_color='#0f0',bg_color='#292933')
format_result_label.place(x=40,y=120)

langauge_result_label = customtkinter.CTkLabel(frame2,font=font2,text='',text_color='#0f0',bg_color='#292933')
langauge_result_label.place(x=245,y=120)

price_result_label = customtkinter.CTkLabel(frame2,font=font2,text='',text_color='#0f0',bg_color='#292933')
price_result_label.place(x=445,y=120)

insert_ids_options()









app.mainloop()
