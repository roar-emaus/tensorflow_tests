import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np
from pathlib import Path


circle_path = Path('data/circles')

n_points = 100

for i in range(100):
    
    theta_a = np.linspace(0, 2*np.pi, n_points)
    theta_b = np.linspace(0, 2*np.pi, n_points)

    theta_offset_a = np.random.randint(low=0, high=2, size=n_points)
    theta_offset_b = np.random.randint(low=0, high=2, size=n_points)

    theta_offset_a = theta_offset_a*np.random.random(n_points)
    theta_offset_b = theta_offset_b*np.random.random(n_points)

    theta_offset_a = theta_offset_a/(np.random.random()*10 + 1)
    theta_offset_b = theta_offset_b/(np.random.random()*10 + 1)

    theta_a = theta_a + theta_offset_a
    theta_b = theta_b + theta_offset_b
    
    r_a = np.random.random() + 0.2 
    r_b = np.random.random() + 0.2
    a = r_a*np.cos(theta_a)
    b = r_b*np.sin(theta_b)
    
    dpi = 100
    fig, ax = plt.subplots(figsize=(160/dpi, 160/dpi), dpi=dpi)
    
    linewidth = (np.random.random() + 1)*4
    ax.plot(a, b, color='black', linewidth=linewidth)
    ax.axis('off')
    ax.margins(0)
    ax.set_aspect(1)
    plt.savefig(circle_path/f'circle_{i:04d}.png')
    plt.close(fig)
    #plt.show()


