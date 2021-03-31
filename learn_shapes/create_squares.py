import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from PIL import Image


square_path = Path('data/squares')

n_points = 1000
n_points_line = int(n_points/4)
n_images = 100
bot, top = 0.15, 0.65
rang = 0.25

for i in range(n_images):
    tl = (np.random.random()*rang + bot, np.random.random()*rang + top)
    tr = (np.random.random()*rang + top, np.random.random()*rang + top)
    bl = (np.random.random()*rang + bot, np.random.random()*rang + bot)
    br = (np.random.random()*rang + top, np.random.random()*rang + bot)
    
    bl_tl_coeffs = np.polyfit(x=[bl[0], tl[0]], y=[bl[1], tl[1]], deg=1)
    tl_tr_coeffs = np.polyfit(x=[tl[0], tr[0]], y=[tl[1], tr[1]], deg=1)
    tr_br_coeffs = np.polyfit(x=[tr[0], br[0]], y=[tr[1], br[1]], deg=1)
    br_bl_coeffs = np.polyfit(x=[br[0], bl[0]], y=[br[1], bl[1]], deg=1)
    
    bl_tl_poly = np.poly1d(bl_tl_coeffs)
    tl_tr_poly = np.poly1d(tl_tr_coeffs)
    tr_br_poly = np.poly1d(tr_br_coeffs)
    br_bl_poly = np.poly1d(br_bl_coeffs)
    
    bl_tl_x = np.linspace(bl[0], tl[0], n_points_line)
    bl_tl_y = bl_tl_poly(bl_tl_x)
    
    tl_tr_x = np.linspace(tl[0], tr[0], n_points_line)
    tl_tr_y = tl_tr_poly(tl_tr_x)
    
    tr_br_x = np.linspace(tr[0], br[0], n_points_line)
    tr_br_y = tr_br_poly(tr_br_x)
    
    br_bl_x = np.linspace(br[0], bl[0], n_points_line)
    br_bl_y = br_bl_poly(br_bl_x)
    
    
    x_offset = np.random.randint(low=0, high=2, size=n_points)*1.0
    y_offset = np.random.randint(low=0, high=2, size=n_points)*1.0
    x_offset *= (np.random.random(n_points) - 0.5)
    y_offset *= (np.random.random(n_points) - 0.5)

    x = np.concatenate([bl_tl_x, tl_tr_x, tr_br_x, br_bl_x]) + x_offset/15
    y = np.concatenate([bl_tl_y, tl_tr_y, tr_br_y, br_bl_y]) + y_offset/15
    
    
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
    plt.savefig(square_path/f'square_{i:08d}.png')
    plt.close(fig)


for i in range(n_images):
    image_file = Image.open(square_path/f'square_{i:08d}.png')
    degs = np.random.random()*360
    rotated = image_file.rotate(degs)
    rotated.save(fp=square_path/f'square_{i + n_images:08d}.png')
