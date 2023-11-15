from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()

root.title("Weather App")
root.geometry("900x500+300+200")

textfield=customtkinter.CTkEntry(master=root,
                               placeholder_text="Enter City",
                               width=200,
                               height=30,
                               border_width=1,
                               corner_radius=10)
textfield.pack(pady=10)

meter = ImageTk.PhotoImage(Image.open("D:\Meenu\Projects\weather app using python\weather.png"))
meter_img=Label(root, image=meter, bd=0)
meter_img.pack(pady=20)

def getWeather():
    try:
        city=textfield.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        res=obj.timezone_at(lng=location.longitude, lat=location.latitude)
        
        home=pytz.timezone(res)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clck.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=bf535520b86f6705bfe163bb30aa9d16"
        json_data=requests.get(api).json()
        cond=json_data['weather'][0]['main']
        desc=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pres=json_data['main']['pressure']
        humid=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(cond,"|","FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humid)
        d.config(text=desc)
        p.config(text=pres)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data from the API: {e}")
    except Exception as e:
        c.config(text=(city,"|", "city", "not", "found"))
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

'''bg_color="#1a1a1a"
pw_ent=tk.Entry(root, text="", font=("Helvetica", 20), bd=0, bg=bg_color, fg="white")
pw_ent.pack(pady=10)
'''

name=Label(root,font=("arial",15,"bold"),fg="white",background="#1a1a1a")
name.place(x=330,y=150)
clck=Label(root,font=("Helvitiva",20),fg="white",background="#1a1a1a")
clck.place(x=330,y=180)

label1=Label(root,text="Wind",font=("Helvitica",20,"bold"),fg="white",bg="#1a1a1a")
label1.place(x=330,y=400)

label2=Label(root,text="Humidity",font=("Helvitica",20,"bold"),fg="white",bg="#1a1a1a")
label2.place(x=520,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvitica",20,"bold"),fg="white",bg="#1a1a1a")
label3.place(x=700,y=400)

label4=Label(root,text="PRESSURE",font=("Helvitica",20,"bold"),fg="white",bg="#1a1a1a")
label4.place(x=960,y=400)

t=Label(font=("arial",70,"bold"),fg="#E44D21",background="#1a1a1a")
t.place(x=840,y=150)
c=Label(font=("arial",25,"bold"),fg="white",background="#1a1a1a")
c.place(x=840,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1a1a1a",fg="white")
w.place(x=330,y=435)
h=Label(text="...",font=("arial",20,"bold"),bg="#1a1a1a",fg="white")
h.place(x=520,y=435)
d=Label(text="...",font=("arial",20,"bold"),bg="#1a1a1a",fg="white")
d.place(x=700,y=435)
p=Label(text="...",font=("arial",20,"bold"),bg="#1a1a1a",fg="white")
p.place(x=960,y=435)


btn_1=customtkinter.CTkButton(master=root,
                              text="Get weather",
                              width=190,
                              height=40,
                              compound="top",
                              command=getWeather)
btn_1.place(x=360, y=330)

root.mainloop()