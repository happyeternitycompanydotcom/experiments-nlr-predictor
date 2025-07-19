# visualization/phase_portrait.py

import numpy as np
import matplotlib.pyplot as plt

def save_phase_portrait(y_pred, save_path="attractor.svg"):
    t = np.linspace(0, 10, 500)
    x = np.sin(t * y_pred)
    y = np.cos(t * y_pred)
    z = np.sin(t * 0.5 * y_pred)

    fig = plt.figure(figsize=(6,5))
    ax = fig.add_subplot(projection='3d')
    ax.plot(x, y, z, color='purple')
    ax.set_title("🌀 Strange Attractor View (3D)")
    plt.savefig(save_path)
