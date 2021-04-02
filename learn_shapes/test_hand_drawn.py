
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image, ImageOps, ImageDraw
from pathlib import Path


model = tf.keras.models.load_model('trained_models/9700_100_cnn')
hand_drawn = tf.keras.preprocessing.image_dataset_from_directory(
        'hand_drawn/',
        image_size=(120, 120),
        label_mode='int',
        )

cats = {0: 'circle', 1: 'square', 2: 'triangle'}
answers = []

for filename in sorted(hand_drawn.file_paths):
    image = ImageOps.grayscale(Image.open(filename)) 
    shape = np.array(image)
    shape = shape.reshape((1, 120, 120, 1))
    shape = shape.astype('float32')/255.0
    prediction = model(shape)
    if 'square' in filename:
        true_form = 'square'
        cat = 1
    elif 'circle' in filename:
        true_form = 'circle'
        cat = 0
    elif 'triangle' in filename:
        true_form = 'triangle'
        cat = 2
    else:
        print(f'{filename} is not a triangle, circle or square')
        break
    name = cats[np.argmax(prediction)]
    img = ImageDraw.Draw(image)
    img.text(xy=(5, 5), text=f"This is a {name}")
    image.show(title=f'This must be a {name}')
    answers.append(np.argmax(prediction) == cat)
    print(f'This must be a {name}: {np.argmax(prediction) == cat} {cats[cat]}---- {prediction}')

print(f'Got {sum(answers)}/{len(answers)}')
