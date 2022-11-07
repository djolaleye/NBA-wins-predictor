#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:00:35 2022

@author: deji
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

import pickle


'''
Logistic regression module
'''


class win_predictor():
    def __init__(self, model, scaler):
        with open('model', 'rb') as model, open('scaler', 'rb') as scaler:
            self.reg = pickle.load(model)
            self.scaler = pickle.load(scaler)
            self.data = None


    def load_clean(self, data_csv, games_played):
        ''' input data in MP, PER, VORP, ORtg/A, Drtg/A '''
        
        df = pd.read_csv(data_csv, delimiter=',')
        self.data_w_predictions = df.copy()
        column_names = ['MP', 'PER', 'VORP', 'ORtg/A', 'DRtg/A']
        df = df[column_names]
        df['MP'] = (df['MP'] / games_played) * 82
        self.preprocessed_data = df.copy()
        self.data = self.scaler.transform(df)

    def predicted_outputs(self):
        if (self.data is not None):
            self.preprocessed_data['Prediction'] = self.reg.predict(self.data)
            return self.preprocessed_data


