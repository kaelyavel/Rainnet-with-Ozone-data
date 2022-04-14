#THIS SCRIPT GENERATES THE IMAGE KEYS FROM THE OZONE IMAGES' NAMES

import re
import os
import numpy as np

i=0
keys=[]
#array = np.zeros()
rootdir = 'Data/'
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        for image in os.listdir(d):
            numbers = re.findall(r"\d+", image)
            numbers.__delitem__(0)
            keys.append(numbers[0])

with open("Ozone_keys.txt", "w") as output:
    output.write(str(keys))