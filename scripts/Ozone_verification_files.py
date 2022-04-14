#THIS SCRIPT GENERATES THE FILES CONTAINING THE DATA FOR VERIFICATION OF RAINNET PRECIPITATION PREDICTIONS
#PREREQUISITE : THE RAINET HDF5 DATASET

import h5py
import numpy as np


dataset_dict= h5py.File("RYDL.hdf5", "r")


data_t_15 = dataset_dict['200903090935'][:]
np.savetxt("text.txt",data_t_15)
data_t_10 = dataset_dict['200903090940'][:]
np.savetxt("text2.txt",data_t_10 )
data_t_5 = dataset_dict['200903090945'][:]
np.savetxt("text3.txt", data_t_5)
data_t_0 = dataset_dict['200903090950'][:]
np.savetxt("text4.txt", data_t_0)

data_t_p_5 = dataset_dict['200903090955'][:]
np.savetxt("text5.txt",data_t_p_5)
data_t_p_10 = dataset_dict['200903091000'][:]
np.savetxt("text6.txt",data_t_p_10)
data_t_p_15 = dataset_dict['200903091005'][:]
np.savetxt("text7.txt", data_t_p_15)
data_t_p_20 = dataset_dict['200903091010'][:]
np.savetxt("text8.txt", data_t_p_20)

dataset_dict.close()

