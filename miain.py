import tkinter as tk

window = tk.Tk()
window.title('Random Coordinate Generator')
window.geometry("1280x720+325+150")
window.config(bg="#323232")

profile_img = tk.PhotoImage(file="D:\Code\occisor_app\profile_logo.png")

mian_title = tk.Label()
mian_title.config(bg="#323232")
mian_title.config(fg="#FFFFFF")
mian_title.config(text="The Occisor Application")
mian_title.config(font="微軟正黑體 30")
mian_title.pack()

profile_btn = tk.Button()
profile_btn.config(bg="#323232")
profile_btn.config(fg="#FFFFFF")
profile_btn.config(image=profile_img)
profile_btn.pack()

window.mainloop()
