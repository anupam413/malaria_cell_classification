from keras.models import load_model
from keras.utils import load_img, img_to_array
import numpy as np

model = load_model("./models/inception_resnet_malaria.h5")

cell = './first_test.jpg'

image_shape = (132,132,3)

image1 = load_img(cell, target_size = image_shape)

image1 = img_to_array(image1)

image1 = np.expand_dims(image1, axis=0)

print(model.predict(image1))
