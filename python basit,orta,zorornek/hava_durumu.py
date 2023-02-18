from tkinter import *
from PIL  import ImageTk,Image
import requests

url= "https://api.openweathermap.org/data/2.5/weather"
api_key= "0ebe82b95b28c23274812415c82f61bb"
icon_url ="http://openweathermap.org/img/wn/{}@2x.png"

app = Tk()
app.geometry("300x450")
app.title("hava durumu")

def getweather(city):
    params={'q':city,'appid':api_key,'lang':"tr"}
    data=requests.get(url,params=params).json()
    if data:
       city=data["name"].capitalize()
       country=data["sys"] ["country"]
       temp=int(data["main"]["temp"]-273.)
       icon=data["weather"][0]["icon"]
       condation= data["weather"][0] ["description"]
       return (city,country,temp,icon,condation)

def main():
    city=city_entry.get()
    weather=getweather(city)
    if weather:
        locationLabel["text"]='{} {}'.format(weather[0],weather[1])
        tempLabel["text"]='{}'.format(weather[2])
        condationLabel["text"]=weather[4]
        icon=ImageTk.PhotoImage(Image.open(requests.get(icon_url.format(weather[3]),stream=True).raw))
        icon_label.configure(image=icon)
        icon_label.image=icon






city_entry=Entry(app,justify="center")
city_entry.pack(fill=BOTH,ipady=10 ,padx=18, pady=5)
city_entry.focus()

search_button=Button(app,text="arama",font=("Arial,15"),command=main)
search_button.pack(fill=BOTH,padx=10, pady=20)

icon_label=Label(app)
icon_label.pack()


locationLabel=Label(app,font=("Arial",40))
locationLabel.pack()


tempLabel=Label(app,font=("Arial",50,"bold"))
tempLabel.pack()


condationLabel=Label(app,font=("Arial",20))
condationLabel.pack()

app.mainloop()