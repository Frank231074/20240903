import sqlite3
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import requests
from io import BytesIO


conn = sqlite3.connect("pokemon.db")
c = conn.cursor()

name = input("検索したいポケモンの名前を入力してください：")

c.execute("SELECT type1, type2, hp, image_url FROM pokemon WHERE name = ?", (name,))

row = c.fetchone()

conn.close()


root = tk.Tk()
root.title("ポケモン情報表示")

if row:
    type1, type2, hp, image_url = row

    Label(root, text=f"名前{name}", font=("Arial, 20")).pack(padx=20, pady=10)
    Label(root, text=f"タイプ１{name}", font=("Arial, 20")).pack(padx=20, pady=10)
    if type2:
        Label(root, text=f"タイプ２{name}", font=("Arial, 20")).pack(padx=20, pady=10)
    Label(root, text=f"HP:{hp}", font=("Arial, 20")).pack(padx=20, pady=10)

    response = requests.get(image_url)
    image_data = BytesIO(response.content)
    img = Image.open(image_data)
    img = img.resize((200, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    Label(root, image=photo).pack(padx=20, pady=10)

else:
    Label(root, text=f"ポケモン'{name}'は見つかりませんでした。", font=("Arial", 16)).pack(padx=20, pady=20)

root.mainloop()
