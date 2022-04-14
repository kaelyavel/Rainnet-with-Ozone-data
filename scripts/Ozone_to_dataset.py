#THIS SCRIPT TRANSFORMS THE DATA OZONE IMAGES INTO AN HDF5 DATASET

import numpy as np
import h5py
import cv2
import os
import re

hf = h5py.File('Ozone.hdf5', 'w')


rootdir = 'Data/'
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        for image in os.listdir(d):
            numbers = re.findall(r"\d+", image)
            numbers.__delitem__(0)
            
            im = cv2.imread(d+"/"+image)

            img_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            dataset = np.array(img_gray.astype(np.float16))
            hf.create_dataset(numbers[0], data=dataset)


hf.close()

hf = h5py.File('Ozone.hdf5', 'r')

for i in hf.items():
    print(i)

hf.close()




