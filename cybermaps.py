from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from PIL import ImageTk, Image
import osmnx as ox
import matplotlib.pyplot as plt
import sys

ox.config(log_console=True, use_cache=True, timeout=360)

w, h = 800,800

themes = {
'tron': ("turquoise", "cyan"),
'blade': ("yellow", "orange"),
'punk': ("red", "yellow"),
'neon': ("magenta", "turquoise"),
'matrix': ("lime", "green"),
'wick': ("cyan", "red"),
'martian': ("red", "orange"),
'valentine': ("pink", "white"),
'gilded': ("yellow", "blue")
}

if 0 <= 1 < len(sys.argv):
    theme = themes[sys.argv[1]]
else:
    theme = themes['punk']

root = Tk()
root.title("Cybermaps v3.8.6")
root.geometry("1920x1080")
root.configure(bg='black')

def show_map():
    global img
    canvas.delete("all")
    inputStr = file.get("1.0", "end-1c")
    rangeInt = int(mapRange.get("1.0", "end-1c"))
    
    progress['value'] = 20
    root.update_idletasks()
    
    areaMDG = ox.graph.graph_from_address(inputStr, dist=rangeInt, dist_type='bbox', network_type='all', simplify=True, retain_all=True, truncate_by_edge=False, return_coords=False, clean_periphery=True, custom_filter=None)
    
    progress['value'] = 50
    root.update_idletasks()
    
    nodes, edges = ox.utils_graph.graph_to_gdfs(areaMDG, nodes=True, edges=True, node_geometry=True, fill_edge_geometry=True)
    
    progress['value'] = 60
    root.update_idletasks()
    
    grp = edges.plot(color=theme[0], figsize=(9,9))
    
    progress['value'] = 70
    root.update_idletasks()
    
    grp.set_facecolor('black')
    plt.tight_layout()
    grp.spines['bottom'].set_color(theme[0])
    grp.spines['left'].set_color(theme[0])
    
    progress['value'] = 75
    root.update_idletasks()
    
    grp.tick_params(axis='x', colors=theme[1])
    grp.tick_params(axis='y', colors=theme[1])
    plt.savefig('tmpImg.png', facecolor=grp.get_facecolor(), bbox_inches=0)
    
    progress['value'] = 90
    root.update_idletasks()
    
    im = Image.open("tmpImg.png")
    w,h = im.size
    canvas.config(width=w, height=h)
    img = ImageTk.PhotoImage(im)
    canvas.create_image(w/2,h/2, anchor=CENTER, image=img)
    
    progress['value'] = 100
    root.update_idletasks()
    
location = Text(root, height = 1, width = 20,bg="black",fg=theme[0],highlightbackground=theme[1])
mapRange = Text(root, height = 1, width = 20,bg="black",fg=theme[0],highlightbackground=theme[1])
canvas = Canvas(root, bg="black", width = w, height = h,highlightbackground=theme[1])
label = Label(root, text = "> RANGE [METERS]",font=("Monospace", 14),bg="black", fg=theme[0],highlightbackground=theme[1])
flabel = Label(root, text = "> LOCATION",font =("Monospace", 14),bg="black", fg=theme[0],highlightbackground=theme[1])
fbtn = Button(root, height = 2, width = 20,bg="black", fg=theme[0], text ="Render Map", command = lambda:show_map(),activebackground=theme[1],font =("Monospace", 14),highlightbackground=theme[1])

s = ttk.Style()
s.theme_use('default')
s.configure("black.Horizontal.TProgressbar", background=theme[0], highlightbackground=theme[1])

progress = Progressbar(root, orient = HORIZONTAL,length = 200, mode = 'determinate', s = 'black.Horizontal.TProgressbar')

location.place(relx=0.9, rely=0.15, anchor=CENTER)
label.place(relx=0.1, rely=0.1, anchor=CENTER)
flabel.place(relx=0.9, rely=0.1, anchor=CENTER)
fbtn.place(relx=0.9, rely=0.2, anchor=CENTER)
progress.place(relx=0.1, rely=0.2, anchor=CENTER)
mapRange.place(relx=0.1, rely=0.15, anchor=CENTER)
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

mainloop()

