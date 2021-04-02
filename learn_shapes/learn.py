import numpy as np
from PIL import Image, ImageOps
from pathlib import Path
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras import layers
import matplotlib.pyplot as plt


batch_size = 300
epochs = 2000
img_height = 120
img_width = 120

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        'data/',
        image_size=(img_height, img_width),
        label_mode='int',
        batch_size=batch_size,
        )

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        'hand_drawn/',
        image_size=(img_height, img_width),
        label_mode='int',
        )

n_images = len(train_ds.file_paths)
n_classes = len(train_ds.class_names)
in_shape = (img_height, img_width, n_classes)

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)


#train_x = train_x.astype('float32')/255.0
#test_x = test_x.astype('float32')/255.0

model = Sequential(
        [
            layers.experimental.preprocessing.Rescaling(
                1./255, input_shape=(img_height, img_width, n_classes)
                ),
            layers.Conv2D(
                30, 20, activation='relu', strides=10, padding='same',
                kernel_initializer='he_uniform', input_shape=in_shape
                ),
            layers.MaxPool2D(2, strides=2),
            layers.Conv2D(
                60, 10, activation='relu', strides=5, padding='same',
                kernel_initializer='he_uniform'
                ),
            layers.MaxPool2D(2),
            layers.Flatten(),
            layers.Dense(30, activation='relu', kernel_initializer='he_uniform'),
            layers.Dropout(0.5),
            layers.Dense(n_classes, activation='softmax'),
        ]
)

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

history = model.fit(
        train_ds,
        validation_data=val_ds, epochs=epochs,
        verbose=1
        )

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

tf.keras.models.save_model(
        model,
        f'trained_models/{n_images}_{epochs}_cnn'
        )

