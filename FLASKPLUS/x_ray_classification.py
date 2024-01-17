import os
import pickle
import cv2
import numpy as np
urls =  os.listdir('C:\\Users\\SHREYASH VERMA\\Downloads\\archive (9)\\COVID-19_Radiography_Dataset\\COVID\\images')


path = "C:\\Users\\SHREYASH VERMA\\Downloads\\archive (9)\\COVID-19_Radiography_Dataset\\COVID\\images\\" + urls[0]
print(path)
def loadImages(path, urls, target):
  images = []
  labels = []
  for i in range(len(urls)):
    img_path = path + "/" + urls[i]
    img = cv2.imread(img_path)
    img = img / 255.0
    img = cv2.resize(img, (100, 100))
    images.append(img)
    labels.append(target)
  images = np.asarray(images)
  return images, labels

covid_path = "C:\\Users\\SHREYASH VERMA\\Downloads\\archive (9)\\COVID-19_Radiography_Dataset\\COVID\\images"
covidUrl = os.listdir(covid_path)
covidImages, covidTargets = loadImages(covid_path, covidUrl, 1)

len(covidUrl), len(covidImages)

normal_path = "C:\\Users\\SHREYASH VERMA\\Downloads\\archive (9)\\COVID-19_Radiography_Dataset\\Normal\\images"
normal_urls = os.listdir(normal_path)
normalImages, normalTargets = loadImages(normal_path, normal_urls, 0)

len(normal_urls), len(normalImages)  



data = np.r_[covidImages, normalImages]
data.shape

targets = np.r_[covidTargets, normalTargets]
targets.shape

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, targets, test_size=0.25)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
model = Sequential([
    Conv2D(32, 3, input_shape=(100,100,3), activation='relu'),
    MaxPooling2D(),
    Conv2D(16, 3, activation='relu'),
    MaxPooling2D(),
    Conv2D(16, 3, activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(256, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss=tf.keras.losses.BinaryCrossentropy(),metrics=['accuracy'])
model.fit(x_train, y_train,batch_size=32,epochs=5,validation_data=(x_test, y_test))

pickle.dump(model, open('x_ray_classification.pkl', 'wb'))


