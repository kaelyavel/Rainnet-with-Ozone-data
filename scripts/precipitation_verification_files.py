#THIS SCRIPT CONTAINS GENERATES THE FILES FOR THE VERIFICATION OF RAINNET OZONE PREDICTIONS

import numpy as np
import h5py


import matplotlib.pyplot as plt



dataset_dict = h5py.File('Ozone.hdf5', 'r')

data_t_18 = dataset_dict['2019113000'][:]
np.savetxt("Ozone_valid_data/text.txt",data_t_18)
data2_t_12 = dataset_dict['2019113006'][:]
np.savetxt("Ozone_valid_data/text2.txt",data2_t_12)
data3_t_6 = dataset_dict['2019113012'][:]
np.savetxt("Ozone_valid_data/text3.txt", data3_t_6)
data4_t_0 = dataset_dict['2019113018'][:]
np.savetxt("Ozone_valid_data/text4.txt", data4_t_0)

data5_t_p_6 = dataset_dict['2019120100'][:]
np.savetxt("Ozone_valid_data/text5.txt", data5_t_p_6)
data5_t_p_12 = dataset_dict['2019120106'][:]
np.savetxt("Ozone_valid_data/text6.txt", data5_t_p_12)
data5_t_p_18 = dataset_dict['2019120112'][:]
np.savetxt("Ozone_valid_data/text7.txt", data5_t_p_18)
data5_t_p_00 = dataset_dict['2019120118'][:]
np.savetxt("Ozone_valid_data/text8.txt", data5_t_p_00)
