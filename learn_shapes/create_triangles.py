import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from PIL import Image


square_path = Path('data/triangles')

n_points = 999
n_points_line = int(n_points/3)
n_images = 1000

bot, top = 0.15, 0.65
rang = 0.2

for i in range(n_images):
    t = (np.random.random(), np.random.random()*rang + top)
    bl = (np.random.random()*0.45, np.random.random()*0.5)
    br = (np.random.random()*0.45 + 0.55, np.random.random()*0.5)
    
    bl_t_coeffs = np.polyfit(x=[bl[0], t[0]], y=[bl[1], t[1]], deg=1)
    t_br_coeffs = np.polyfit(x=[t[0], br[0]], y=[t[1], br[1]], deg=1)
    br_bl_coeffs = np.polyfit(x=[br[0], bl[0]], y=[br[1], bl[1]], deg=1)
    
    bl_t_poly = np.poly1d(bl_t_coeffs)
    t_br_poly = np.poly1d(t_br_coeffs)
    br_bl_poly = np.poly1d(br_bl_coeffs)
    
    bl_t_x = np.linspace(bl[0], t[0], n_points_line)
    bl_t_y = bl_t_poly(bl_t_x)
    
    t_br_x = np.linspace(t[0], br[0], n_points_line)
    t_br_y = t_br_poly(t_br_x)
    
    br_bl_x = np.linspace(br[0], bl[0], n_points_line)
    br_bl_y = br_bl_poly(br_bl_x)
    
    
    x_offset = np.random.randint(low=0, high=2, size=n_points)*1.0
    y_offset = np.random.randint(low=0, high=2, size=n_points)*1.0
    x_offset *= (np.random.random(n_points) - 0.5)
    y_offset *= (np.random.random(n_points) - 0.5)

    x = np.concatenate([bl_t_x, t_br_x, br_bl_x]) + x_offset/15
    y = np.concatenate([bl_t_y, t_br_y, br_bl_y]) + y_offset/15
    
    
    dpi = 100
    pixels = 120
    fig, ax = plt.subplots(figsize=(pixels/dpi, pixels/dpi), dpi=dpi)

    linewidth = (np.random.random() + 0.1)*4
    ax.plot(x, y, color='black', linewidth=linewidth)
    ax.axis('off')
    ax.set_ylim((0, 1))
    ax.set_xlim((0, 1))
    #ax.margins(0)
    ax.set_aspect(1)
    plt.savefig(square_path/f'triangle_{i:08d}.png')
    plt.close(fig)


for i in range(n_images):
    image_file = Image.open(square_path/f'triangle_{i:08d}.png')
    degs = np.random.random()*360
    rotated = image_file.rotate(degs)
    rotated.save(fp=square_path/f'triangle_{i + n_images:08d}.png')

