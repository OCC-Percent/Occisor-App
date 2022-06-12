from cProfile import label
import tkinter as tk

window = tk.Tk()
window.title('Random Coordinate Generator')
window.geometry("1280x720+325+150")
window.config(bg="#323232")

profile_img = tk.PhotoImage(file="D:\Code\occisor_app\profile_logo.png")

title = tk.Label()
title.config(bg="#323232")
title.config(fg="#FFFFFF")
title.config(text="The Occisor Application")
title.config()
title.pack()

profile_btn = tk.Button()
profile_btn.config(bg="#323232")
profile_btn.config(fg="#FFFFFF")
profile_btn.config(image=profile_img)
profile_btn.pack()

window.mainloop()
