#weather
import requests

from tkinter import messagebox, simpledialog
messagebox.showinfo("Welcome", "Weather wizerd is on\n Press <ok> to continue")
baseurl = "http://api.openweathermap.org/data/2.5/weather?q="


weatherapi = "8e44efb0ae84f237a5d93f5f4d629433"

place = simpledialog.askstring("location/place name", "For what location you want to get the Weather report ?")
url = baseurl + place + "&appid=" + str(weatherapi) + "&units=metric"
res = requests.get(url)
data = res.json()
if data["cod"] == 200:
    print("city found")
    messagebox.showinfo("info", "city found \n To continue press <ok>")
    temp = data["main"]["temp"]
    hum = data["main"]["humidity"]
    visi = data["visibility"]
    des = data["weather"][0]["description"]
    main = "temparature is {} degree celcious ,\nhumidity is {} percent ,\nvisibitily is {} ,\noverall {}".format(temp, hum, visi, des)
    print("weather : "+main)
    messagebox.showinfo("info", "weather : "+main + "Hope you enjoyed our service")

else:
    messagebox.showwarning("City not found", "looks like some thing went wrong,city not found,try again")
