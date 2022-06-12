from dis import disco
import secrets
import tkinter as tk
from tkinter.ttk import Sizegrip

from setuptools import Command

window = tk.Tk()
window.title('Random Coordinate Generator')
window.geometry("1280x720+325+150")
window.config(bg="#323232")

mian_title = tk.Label()
mian_title.config(bg="#323232")
mian_title.config(fg="#FFFFFF")
mian_title.config(text="The Occisor Application")
mian_title.config(font="jf-openhuninn-1.1 30")
mian_title.pack()

profile_img = tk.PhotoImage(file="D:\Code\occisor_app\profile_logo.png")

def screach () :
    screach_id = screach_input.get()
    if screach_id == "Percent.06_27#0639" or screach_id == "Percent.06_27" or screach_id == "0639" or screach_id == "Percent" or screach_id == "Percent#パーセント" or screach_id =="IceBlue0627":
        discord_id = "Percent.06_27#0639"
        valorant_id = "Percent#パーセント"
        osu_id = "IceBlue0627"
        role = "呼拉牙薩、刺針教成員"
    elif screach_id == "まりん#3882" or screach_id == "まりん" or screach_id == "3882" or screach_id == "" or screach_id == "":
        discord_id = "まりん#3882"
        valorant_id = "N/A"
        osu_id = "N/A"
        role = "刺針教教主"
    elif screach_id == "派蒙#5811" or screach_id == "派蒙" or screach_id == "5811" or screach_id == "" or screach_id== "":
        discord_id = "派蒙#5811"
        valorant_id = "N/A"
        osu_id = "N/A"
        role = "手持制式手槍的男人、刺針教成員"
    print(f">>Sercach : {screach_id}")
    discord_id_output.config(text=f"Discord ID : {discord_id}" )
    valorant_id_output.config(text=f"Valorant ID : {valorant_id}")
    osu_id_output.config(text=f"osu! ID : {osu_id}" )
    role_output.config(text=f"Role : {role}")

screach_input = tk.Entry()
screach_input.config(width=40)
screach_input.pack()

enter_btn = tk.Button()
enter_btn.config(text="Screach")
enter_btn.config(bg="#323232")
enter_btn.config(fg="#FFFFFF")
enter_btn.config(command=screach)
enter_btn.pack()

discord_id_output = tk.Label()
discord_id_output.config(text="Discord ID : " )
discord_id_output.config(bg="#323232")
discord_id_output.config(fg="#FFFFFF")
discord_id_output.config(font="jf-openhuninn-1.1 20")
discord_id_output.pack()

valorant_id_output = tk.Label()
valorant_id_output.config(text="Valorant ID : " )
valorant_id_output.config(bg="#323232")
valorant_id_output.config(fg="#FFFFFF")
valorant_id_output.config(font="jf-openhuninn-1.1 20")
valorant_id_output.pack()

osu_id_output = tk.Label()
osu_id_output.config(text="osu! ID : ")
osu_id_output.config(bg="#323232")
osu_id_output.config(fg="#FFFFFF")
osu_id_output.config(font="jf-openhuninn-1.1 20")
osu_id_output.pack()

role_output = tk.Label()
role_output.config(text="Role : ")
role_output.config(bg="#323232")
role_output.config(fg="#FFFFFF")
role_output.config(font="jf-openhuninn-1.1 20")
role_output.pack()

window.mainloop()
