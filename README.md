# [Rainnet](https://github.com/hydrogo/rainnet) for Ozone prediction
Projet TER fait par KHARAOUI Mohamed El Bachir et encadré par Professeur Luiz Angelo Steffenel


* Les Notebooks de ce dossier sont fonctionnels avec Colab de Google en utilisant un GPU :

  * RainNet_Training_Ozone_2e.ipynb
  * Rainnet_tests.ipynb


* [**Ozone_model_powered_by_Rainnet_v2e.h5**](https://drive.google.com/drive/u/0/folders/1yyq4TW6cv2huzKZMBOOXVRsgTHGuCZGl) est le modèle de Rainnet entrainé avec les données d'Ozone

* [**Ozone.hdf5**](https://drive.google.com/drive/u/0/folders/1yyq4TW6cv2huzKZMBOOXVRsgTHGuCZGl) est le dataset des données d'Ozone.


* Le dossier "Ozone_valid_data_for_evaluation" contient les fichiers ayant servi à l'évaluation
de Rainnet avec les données d'Ozone

* Le dossier "scripts" contient les fichiers suivants : 
  * precipitation_verification_files.py : Generates verification files for Rainnet precipitation predictions
  * Ozone_verification_files.py : Generates verification files for Rainnet Ozone prediction
  * Ozone_to_dataset.py : Transforms Ozone images into HDF5 Dataset for Rainnet
  * Ozone_image_keys.py : Extracts Ozone images keys into file

