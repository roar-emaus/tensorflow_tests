
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path
from PIL import Image

from multiprocessing import Pool


def create_circle(i):
    dpi = 100
    pixels = 120
    fig, ax = plt.subplots(figsize=(pixels/dpi, pixels/dpi), dpi=dpi)
    radius = np.random.random() + 0.2
    x = np.random.random() - 1
    y = np.random.random() - 1
    circle = patches.Circle((x, y), radius)
    ax.add_patch(circle)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.axis('off')
    ax.set_aspect(1)

    plt.savefig(circle_path/f'circle_{i:08d}.png')
    plt.close(fig)


def create_square(i):
    dpi = 100
    pixels = 120
    fig, ax = plt.subplots(figsize=(pixels/dpi, pixels/dpi), dpi=dpi)

    x, y = np.random.random(2) + 0.01
    width, height = np.random.random(2) + 0.2
    square = patches.Rectangle(xy=(x, y), width=width, height=height)
    ax.add_patch(square)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.axis('off')
    ax.set_aspect(1)

    plt.savefig(square_path/f'square_{i:08d}.png')
    plt.close(fig)


def create_triangle(i):
    dpi = 100
    pixels = 120
    fig, ax = plt.subplots(figsize=(pixels/dpi, pixels/dpi), dpi=dpi)

    bot, top = 0.15, 0.65
    rang = 0.2
    t = (np.random.random(), np.random.random()*rang + top)
    bl = (np.random.random()*0.45, np.random.random()*0.5)
    br = (np.random.random()*0.45 + 0.55, np.random.random()*0.5)

    triangle = patches.Polygon(xy=[t, bl, br], closed=True)
    ax.add_patch(triangle)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_aspect(1)

    plt.savefig(triangle_path/f'triangle_{i:08d}.png')
    plt.close(fig)


circle_path = Path('data/circles')
square_path = Path('data/squares')
triangle_path = Path('data/triangles')

n_images = 4000
n_rotations = 7000
n_processes = 6

with Pool(n_processes) as p:
    p.map(create_circle, list(range(n_images)))

with Pool(n_processes) as p:
    p.map(create_square, list(range(n_images)))

with Pool(n_processes) as p:
    p.map(create_triangle, list(range(n_images)))
#for i in range(n_images):
#    create_circle()

for i in range(n_rotations):
    image_file = Image.open(circle_path/f'circle_{i:08d}.png')
    degs = np.random.random()*360
    rotated = image_file.rotate(degs)
    rotated.save(fp=circle_path/f'circle_{i + n_images:08d}.png')

#for i in range(n_images):
#    create_square()

for i in range(n_rotations):
    image_file = Image.open(square_path/f'square_{i:08d}.png')
    degs = np.random.random()*360
    rotated = image_file.rotate(degs)
    rotated.save(fp=square_path/f'square_{i + n_images:08d}.png')

#for i in range(n_images):
#    create_triangle()

for i in range(n_rotations):
    image_file = Image.open(triangle_path/f'triangle_{i:08d}.png')
    degs = np.random.random()*360
    rotated = image_file.rotate(degs)
    rotated.save(fp=triangle_path/f'triangle_{i + n_images:08d}.png')

