print("console for devs")
# HOW MUCH STUFF DO YOU HAVE TO IMPORT?!
print("Importing Modules...")
import time
import tkinter as tk
import apisys
import os
from pathlib import Path

time.sleep(0.5)
BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

#pre tk setup
def enterZIPbtnPressed():
    zipcode = inputZIP.get()
    print("zip code : " + zipcode)
    temp, percip, windSpeed = apisys.weatherAPI(zipcode)

    # add the path of images to the empty quotes
    if percip >= 0.2 and percip < 2:
        bgIMG = tk.PhotoImage(file = "")
        bgLABEL = tk.Label(window, image = bgIMG)
        bgLABEL.place(x = 0, y = 0)
    elif percip < 0.2:
        bgIMG = tk.PhotoImage(file = "")
        bgLABEL = tk.Label(window, image = bgIMG)
        bgLABEL.place(x = 0, y = 0)
    elif percip > 2:
        bgIMG = tk.PhotoImage(file = "")
        bgLABEL = tk.Label(window, image = bgIMG)
        bgLABEL.place(x = 0, y = 0)

    tempTXT = tk.Label(window, text=("Temprature:"))
    tempValueTXT = tk.Label(window, text=(str(round(temp)) + "°F"))

    tempTXT.pack()
    tempValueTXT.pack()

    precipTXT = tk.Label(window, text=("Precipitation:"))
    precipValueTXT = tk.Label(window, text=(str(round(percip)) + " Inches"))
    
    precipTXT.pack()
    precipValueTXT.pack()  

    windSpeedTXT = tk.Label(window, text=("Wind Speed:"))
    WindSpeedValueTXT = tk.Label(window, text=(str(round(windSpeed)) + " MPH"))

    windSpeedTXT.pack()
    WindSpeedValueTXT.pack()

# tkinter has entered the chat
window = tk.Tk()
window.geometry("420x420")
window.title("Weather")

iconPath = Path("img") / "logo.png"
if iconPath.exists():
    icon = tk.PhotoImage(file=str(iconPath))
    window.iconphoto(True, icon)
window.config(background="white")

#input zip code
inputZIPtxt = tk.Label(window,text=("Enter Zip Code:")) #text
inputZIPtxt.pack()

inputZIPenterbtn = tk.Button(window,text="Enter",command=enterZIPbtnPressed) #button
inputZIPenterbtn.pack()

inputZIP = tk.Entry(state="normal") #entry box
inputZIP.pack()
# getting the zip code back like a boomerang

window.mainloop()
