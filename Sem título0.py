# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 07:22:38 2018

@author: rodrigo.bulgarelli
"""

from keras.models import load_model

model = load_model('C:\\Users\\rodrigo.bulgarelli\\Downloads\\New folder\\FRmodel.HDF5')

print(model.summary())