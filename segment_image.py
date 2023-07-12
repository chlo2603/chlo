# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 15:11:00 2023

@author: Admin
"""
import numpy as np
import pydicom
import pylibjpeg
import nibabel as nib
import matplotlib.pyplot as plt
from PIL import Image


#Ici j'ai tenté d'ouvrir l'image NIFTI de la segmentation il n'apparairaissat que du noir..
image = nib.load('heart_28_06_23.nii.gz')

print(image.get_fdata().shape)
data = image.get_fdata()
plt.imshow(data[:, :, 100], cmap='gray')

plt.show()






'''
Ici j'ai tenté d'ouvrir l'image NIFTI de la segmentation il n'apparairaissat que du noir..
image = nib.load('heart_28_06_23.nii.gz')
print(image.get_fdata().shape)
data = image.get_fdata()
plt.imshow(data[:, :, 100], cmap='gray')
plt.show()
'''
