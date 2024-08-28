# Run to train a model (change the num_epoch below for more or less accuracy)

import numpy as np
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import deeplake

# Set mode
mode = 'train'

# plots accuracy and loss curves
def plot_model_history(model_history):
    """
    Plot Accuracy and Loss curves given the model_history
    """
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))

    # summarize history for accuracy
    axs[0].plot(range(1, len(model_history.history['accuracy']) + 1), model_history.history['accuracy'])
    axs[0].plot(range(1, len(model_history.history['val_accuracy']) + 1), model_history.history['val_accuracy'])
    axs[0].set_title('Model Accuracy')
    axs[0].set_ylabel('Accuracy')
    axs[0].set_xlabel('Epoch')
    axs[0].set_xticks(np.arange(1, len(model_history.history['accuracy']) + 1, step=max(1, len(model_history.history['accuracy']) // 10)))
    axs[0].legend(['train', 'val'], loc='best')

    # summarize history for loss
    axs[1].plot(range(1, len(model_history.history['loss']) + 1), model_history.history['loss'])
    axs[1].plot(range(1, len(model_history.history['val_loss']) + 1), model_history.history['val_loss'])
    axs[1].set_title('Model Loss')
    axs[1].set_ylabel('Loss')
    axs[1].set_xlabel('Epoch')
    axs[1].set_xticks(np.arange(1, len(model_history.history['loss']) + 1, step=max(1, len(model_history.history['loss']) // 10)))
    axs[1].legend(['train', 'val'], loc='best')

    fig.savefig('plot.png')
    plt.show()

# Define data generators
def deeplake_generator(ds, batch_size):
    while True:
        batch_images = []
        batch_labels = []
        for sample in ds:
            image = sample.images.data()["value"]
            label = sample.labels.data()["value"]

            # Preprocess image and label
            image = cv2.resize(image, (48, 48))
            image = np.expand_dims(image, axis=-1) / 255.0  # Normalize and add channel dimension

            # One-hot encode the label
            label = tf.keras.utils.to_categorical(label, num_classes=7)

            # Squeeze the label to remove the extra dimension
            label = np.squeeze(label)

            batch_images.append(image)
            batch_labels.append(label)

            # Yield the batch if it's full
            if len(batch_images) == batch_size:
                yield np.array(batch_images), np.array(batch_labels)
                batch_images, batch_labels = [], []

        # Handle the remaining samples in the last batch
        if batch_images:
            yield np.array(batch_images), np.array(batch_labels)


# Load DeepLake datasets
train_ds = deeplake.load('hub://activeloop/fer2013-train')
val_ds = deeplake.load('hub://activeloop/fer2013-public-test')

# Parameters
batch_size = 512
num_epoch = 100

train_generator = deeplake_generator(train_ds, batch_size)
validation_generator = deeplake_generator(val_ds, batch_size)

# Fetch one batch from the train generator to inspect
train_images, train_labels = next(train_generator)
print("Shape of images in a batch: ", train_images.shape)
print("Shape of labels in a batch: ", train_labels.shape)

steps_per_epoch = len(train_ds) // batch_size
validation_steps = len(val_ds) // batch_size

# Create the model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(48, 48, 1)),
    tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
    tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Dropout(0.25),

    tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Dropout(0.25),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1024, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(7, activation='softmax')
])

# Compile the model
model.compile(loss='categorical_crossentropy',
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
              metrics=['accuracy'])

# Train the model
model_info = model.fit(
    train_generator,
    steps_per_epoch=steps_per_epoch,
    epochs=num_epoch,
    validation_data=validation_generator,
    validation_steps=validation_steps
)

# Plot the model history
plot_model_history(model_info)
model.save_weights('model.weights.h5')
