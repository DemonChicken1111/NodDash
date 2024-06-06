
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, tkk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from tinydb import TinyDB, Query
import os.path
import numpy as np


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.title("NodDash")
window.geometry("1920x1080")
window.configure(bg = "#282828")


canvas = Canvas(
    window,
    bg = "#282828",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1920.0,
    72.0,
    fill="#7DAEA3",
    outline="")

canvas.create_text(
    88.0,
    18.0,
    anchor="nw",
    text="NodDash\n",
    fill="#1E1E1E",
    font=("Inter Bold", 30 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    64.0,
    36.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    302.0,
    175.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    302.0,
    505.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    304.0,
    875.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    969.0,
    652.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    1636.0,
    655.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    969.0,
    175.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    1636.0,
    175.0,
    image=image_image_8
)

canvas.create_text(
    113.0,
    144.0,
    anchor="nw",
    text="Total Activity in last 24 hours:",
    fill="#D4BE98",
    font=("Inter Bold", 13 * -1)
)

canvas.create_text(
    780.0,
    144.0,
    anchor="nw",
    text="Smart Deployables",
    fill="#D4BE98",
    font=("Inter Bold", 13 * -1)
)

canvas.create_text(
    1447.0,
    144.0,
    anchor="nw",
    text="Up Time",
    fill="#D4BE98",
    font=("Inter Bold", 13 * -1)
)

canvas.create_text(
    90.0,
    175.0,
    anchor="nw",
    text="104 Pings",
    fill="#D4BE98",
    font=("Inter Bold", 22 * -1)
)

canvas.create_text(
    754.0,
    175.0,
    anchor="nw",
    text="20 Online",
    fill="#D4BE98",
    font=("Inter Bold", 22 * -1)
)

canvas.create_text(
    1511.0,
    154.0,
    anchor="nw",
    text="00:20:58:05",
    fill="#D4BE98",
    font=("Inter Bold", 36 * -1)
)

canvas.create_text(
    439.0,
    157.0,
    anchor="nw",
    text="5.8%",
    fill="#A9B665",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    1106.0,
    157.0,
    anchor="nw",
    text="10.9%",
    fill="#A9B665",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    439.0,
    185.0,
    anchor="nw",
    text="Past Week",
    fill="#D4BE98",
    font=("Inter Bold", 10 * -1)
)

canvas.create_text(
    1106.0,
    185.0,
    anchor="nw",
    text="Past Week",
    fill="#D4BE98",
    font=("Inter Bold", 10 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    415.0,
    172.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1082.0,
    172.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    94.0,
    152.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    764.0,
    153.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    1431.0,
    154.0,
    image=image_image_13
)

fpath = os.path.dirname(__file__) + '/../pingdb.json'
db = TinyDB(fpath)
result = db.all()
df = pd.DataFrame(result)
h = df.groupby(["time"]).agg({"amount": "sum"}).reset_index()
h["time"] = pd.to_datetime(h["time"])

#Creating Ping Bar Graph
fig_1 = Figure(figsize=(4, 2.9), facecolor="#7DAEA3")
ax_1 = fig_1.add_subplot()
ax_1.bar(x=h["time"], height=h["amount"] ,width=0.1, linewidth=0.7)
ax_1.tick_params(labelsize=7, colors="white")
fig_1.autofmt_xdate()
ax_1.grid(visible=True)
ax_1.set_xlabel("time")
ax_1.set_ylabel("pings")

fig_2 = Figure()
fig_3 = Figure()

#Creating Table
table = ttk.Treeview(master=window, columns=df, show="headings")

canvas = FigureCanvasTkAgg(fig_1, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=110, y=723)

window.resizable(True, True)
window.mainloop()