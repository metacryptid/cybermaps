# cybermaps
Cyberpunk-inspired map viewing program that creates maps using OSM data.

# Dependencies
Uses OSMnx, TKinter, and Matplotlib.

# What is it?
This software is made to generate image-based maps of the area around a specific address. It was designed with a certain futuristic style in mind, and you can further customize its look with one of the included themes.

# How to install and use it
First, install Matplotlib, TKinter, and OSMnx if they are not already installed. Then download the source code. You can run this from the command line with `python3 cybermaps.py [valid theme name]`.
When you run it for the first time, cybermaps will generate a `cache` folder as well as a file named `tmpImage.png` in the directory in which you run it. The `cache` folder is created by OSMnx and stores cached OSM entries for faster map generation; this setting is on by default and encouraged for speed, but you can turn it off by telling OSMnx not to use the cache in `cybermaps.py`'s `ox.config()` function. `tmpImage.png` stores the most-recently generated map.

# Things to watch out for
- While using the program, very large `range` values will sometimes cause OSMnx to kill the program if it tries to process too much map data at once.

- The larger the area you are attempting to render, the more time it will take to process the map data. This can take several minutes maxium.

- If you plan to use this in an embedded system, be aware that *you will need an internet connection to get map data*.

- This software is not designed for serious navigation or commercial use. You should not treat its maps as 100% reliable.


