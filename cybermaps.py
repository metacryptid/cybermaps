from tkinter import *
from PIL import ImageTk, Image
import osmnx as ox
import matplotlib.pyplot as plt
import sys

ox.config(log_console=True, use_cache=True, timeout=360)

w, h = 800,800
if 0 <= 1 < len(sys.argv):
    theme = sys.argv[1]
else:
    theme = 'punk'

# this will eventually be replaced with a more robust theming system.

if theme == "tron":
    themeColor = "turquoise"
    themeColorTwo = "cyan"
elif theme == "blade":
    themeColor = "yellow"
    themeColorTwo = "orange"
elif theme == "punk":
    themeColor = "red"
    themeColorTwo = "yellow"
elif theme == "spice":
    themeColor = "orange"
    themeColorTwo = "orange"
elif theme == "neon":
    themeColor = "magenta"
    themeColorTwo = "turquoise"
elif theme == "matrix":
    themeColor = "lime"
    themeColorTwo = "green"
elif theme == "wick":
    themeColor = "cyan"
    themeColorTwo = "red"
elif theme == "martian":
    themeColor = "red"
    themeColorTwo = "orange"
elif theme == "valentine":
    themeColor = "pink"
    themeColorTwo = "white"

root = Tk()
root.title("Cybermaps v3.7.3")
root.geometry("1920x1080")
root.configure(bg='black')
canvas = Canvas(root, bg="black", width = w, height = h)
canvas.config(highlightbackground=themeColorTwo)
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

def show_map(location):
    global img
    canvas.delete("all")
    if location == "override":
        inputStr = file.get("1.0", "end-1c")
    else:
        inputStr = location
    rangeInt = int(mapRange.get("1.0", "end-1c"))
    areaMDG = ox.graph.graph_from_address(inputStr, dist=rangeInt, dist_type='bbox', network_type='all', simplify=True, retain_all=True, truncate_by_edge=False, return_coords=False, clean_periphery=True, custom_filter=None)
    nodes, edges = ox.utils_graph.graph_to_gdfs(areaMDG, nodes=True, edges=True, node_geometry=True, fill_edge_geometry=True)
    grp = edges.plot(color=themeColor, figsize=(9,9))
    grp.set_facecolor('black')
    plt.tight_layout()
    grp.spines['bottom'].set_color(themeColor)
    grp.spines['left'].set_color(themeColor)
    grp.tick_params(axis='x', colors=themeColorTwo)
    grp.tick_params(axis='y', colors=themeColorTwo)
    plt.savefig('tmpImg.png', facecolor=grp.get_facecolor(), bbox_inches=0)
    
    im = Image.open("tmpImg.png")
    w,h = im.size
    canvas.config(width=w, height=h)
    img = ImageTk.PhotoImage(im)
    canvas.create_image(w/2,h/2, anchor=CENTER, image=img)
    
file = Text(root, height = 1, width = 20,bg="black",fg=themeColor)
mapRange = Text(root, height = 1, width = 20,bg="black",fg=themeColor)

label = Label(root, text = "> RANGE [METERS]")
flabel = Label(root, text = "> LOCATION")

label.config(font=("Monospace", 14),bg="black", fg=themeColor)
flabel.config(font =("Monospace", 14),bg="black", fg=themeColor)

fbtn = Button(root, height = 2, width = 20,bg="black", fg=themeColor, text ="Render Map", command = lambda:show_map('override'))

fbtn.config(font =("Monospace", 14))

file.config(highlightbackground=themeColorTwo)
label.config(highlightbackground=themeColorTwo)
flabel.config(highlightbackground=themeColorTwo)
fbtn.config(highlightbackground=themeColorTwo)
mapRange.config(highlightbackground=themeColorTwo)

file.place(relx=0.9, rely=0.15, anchor=CENTER)
label.place(relx=0.1, rely=0.1, anchor=CENTER)
flabel.place(relx=0.9, rely=0.1, anchor=CENTER)
fbtn.place(relx=0.9, rely=0.2, anchor=CENTER)
mapRange.place(relx=0.1, rely=0.15, anchor=CENTER)

mainloop()

