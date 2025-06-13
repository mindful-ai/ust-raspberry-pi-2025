import os
import zipfile
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import to_categorical

# Paths
DATA_DIR = "mnist"
TRAIN_ZIP = os.path.join(DATA_DIR, "mnist_train.csv.zip")
TEST_ZIP = os.path.join(DATA_DIR, "mnist_test.csv.zip")
TRAIN_CSV = os.path.join(DATA_DIR, "mnist_train.csv")
TEST_CSV = os.path.join(DATA_DIR, "mnist_test.csv")

# 1. Unzip CSV files (if not already)
for zip_path, csv_path in [(TRAIN_ZIP, TRAIN_CSV), (TEST_ZIP, TEST_CSV)]:
    if not os.path.exists(csv_path):
        print(f"Unzipping {zip_path} …")
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(DATA_DIR)

# 2. Load CSV data
def load_csv(path):
    data = np.loadtxt(path, delimiter=",", skiprows=1)
    x = data[:, 1:].astype('float32') / 255.0
    y = data[:, 0].astype('int')
    x = x.reshape(-1, 28, 28, 1)
    y = to_categorical(y, 10)
    return x, y

x_train, y_train = load_csv(TRAIN_CSV)
x_test, y_test = load_csv(TEST_CSV)
print("Loaded:", x_train.shape, y_train.shape, x_test.shape, y_test.shape)

# 3. Create tf.data pipelines
batch_size = 64
ds_train = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(batch_size).prefetch(tf.data.AUTOTUNE)
ds_test = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(batch_size).prefetch(tf.data.AUTOTUNE)

# 4. Build model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(ds_train, validation_data=ds_test, epochs=5)

# 5. Save model
model.save("mnist_cnn_model.h5")

# 6. Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite = converter.convert()

with open("mnist_model.tflite", "wb") as f:
    f.write(tflite)

print("🎉 Offline training and conversion complete!")
