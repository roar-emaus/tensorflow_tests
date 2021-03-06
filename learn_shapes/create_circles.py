
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from PIL import Image

from multiprocessing import Pool


def create_circle(i):
    theta_a = np.linspace(0, 2*np.pi, n_points)
    theta_b = np.linspace(0, 2*np.pi, n_points)

    theta_offset_a = np.random.randint(low=0, high=2, size=n_points)
    theta_offset_b = np.random.randint(low=0, high=2, size=n_points)

    theta_offset_a = theta_offset_a*(np.random.random(n_points)*1.2 - 1.2)
    theta_offset_b = theta_offset_b*(np.random.random(n_points)*1.2 - 1.2)

    theta_offset_a = theta_offset_a/(np.random.random()*10 + 1)
    theta_offset_b = theta_offset_b/(np.random.random()*10 + 1)

    theta_a = theta_a + theta_offset_a
    theta_b = theta_b + theta_offset_b
    
    r_a = np.random.random() + 0.2
    r_b = np.random.random() + 0.2
    a = r_a*np.cos(theta_a)
    b = r_b*np.sin(theta_b)
    
    fig, ax = plt.subplots(figsize=(pixels/dpi, pixels/dpi), dpi=dpi)
    
    linewidth = (np.random.random() + 0.1)*10
    ax.plot(a, b, color='black', linewidth=linewidth)
    ax.axis('off')
    ax.set_ylim((-1.4, 1.4))
    ax.set_xlim((-1.4, 1.4))
    ax.margins(0)
    ax.set_aspect(1)
    plt.savefig(circle_path/f'circle_{i:08d}.png')
    plt.close(fig)

circle_path = Path('data/circles')

n_points = 100
n_images = 2000
n_rots = 4000
dpi = 50
pixels = 120
n_procs = 6

with Pool(n_procs) as p:
    p.map(create_circle, list(range(n_images)))

for i in range(n_rots):
    image_file = Image.open(circle_path/f'circle_{i:08d}.png')
    degs = np.random.random()*360
    rotated = image_file.rotate(degs)
    rotated.save(fp=circle_path/f'circle_{i + n_images:08d}.png')

    
