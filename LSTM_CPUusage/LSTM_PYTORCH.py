#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 01:34:58 2017

@author: allen
"""

import pandas as pd
from pandas import read_csv

import matplotlib
matplotlib.use('Agg')
#%matplotlib inline

import matplotlib.pyplot as plt

import torch
import torch.nn as nn 
from torch.autograd import Variable
import torch.optim as optim

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

class Sequence(nn.Module):
    def __init__(self):
        super(Sequence, self).__init__()
        self.lstm1 = nn.LSTMCell(1, 51)
        self.lstm2 = nn.LSTMCell(51, 1)

    def forward(self, input, future=0):
        outputs = []
        h_t = Variable(
            torch.zeros(input.size(0), 51), requires_grad=False)
        c_t = Variable(
            torch.zeros(input.size(0), 51), requires_grad=False)
        h_t2 = Variable(
            torch.zeros(input.size(0), 1), requires_grad=False)
        c_t2 = Variable(
            torch.zeros(input.size(0), 1), requires_grad=False)

        for i, input_t in enumerate(input.chunk(input.size(1), dim=1)):
            h_t, c_t = self.lstm1(input_t, (h_t, c_t))
            h_t2, c_t2 = self.lstm2(c_t, (h_t2, c_t2))
            outputs += [c_t2]

        for i in range(future):  # if we should predict the future
            h_t, c_t = self.lstm1(c_t2, (h_t, c_t))
            h_t2, c_t2 = self.lstm2(c_t, (h_t2, c_t2))
            outputs += [c_t2]

        outputs = torch.stack(outputs, 1).squeeze(2)
        return outputs

# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
        
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    
    # put it all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg
 
# load dataset
dataset = read_csv('data.csv', header=0, index_col=0)
    
values = dataset.values
print(values[:,4])

encoder = LabelEncoder()
set(encoder.fit_transform(values[:,4]))

values = dataset.values

# integer encode direction
encoder = LabelEncoder()
values[:,4] = encoder.fit_transform(values[:,4])

# ensure all data is float
values = values.astype('float32')
# normalize features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)

# frame as supervised learning
reframed = series_to_supervised(scaled, 1, 1)
# drop columns we don't want to predict
reframed.drop(reframed.columns[[0,1,2,3]], axis=1, inplace=True)

print(reframed.head())

data = reframed.values

n_split = int(0.3 * len(data))
print(n_split)

train_X = Variable(torch.from_numpy(data[n_split:, :-1]), requires_grad=False)
train_y = Variable(torch.from_numpy(data[n_split:, 1:]), requires_grad=False)
test_X = Variable(torch.from_numpy(data[:n_split, :-1]), requires_grad=False)
test_y = Variable(torch.from_numpy(data[:n_split, 1:]), requires_grad=False)

print(train_X.size(), train_y.size(), test_X.size(), test_y.size())

# build the model
seq = Sequence()
# seq.double()
criterion = nn.MSELoss()

# use LBFGS as optimizer since we can load the whole data to train
optimizer = optim.Adam(seq.parameters())

loss_list = []
test_loss_list = []

epoch_num = 200

# begin to train
for epoch in range(epoch_num):
    print('epoch : %d'%epoch, end="\t")

    def closure():
        optimizer.zero_grad()
        out = seq(train_X)
        loss = criterion(out, train_y)
        print('loss : %.3f'%loss.data.numpy()[0],end="\t")
        loss_list.append(loss.data.numpy()[0])
        loss.backward()
        return loss

    optimizer.step(closure)

    #begin to predict
    pred = seq(test_X)
    loss = criterion(pred, test_y)
    print('test loss : %.3f '%loss.data.numpy()[0])
    test_loss_list.append(loss.data.numpy()[0])

    y = pred.data.numpy()

plt.figure(figsize=(10,6))
plt.plot(range(epoch_num), loss_list, label='train loss')
plt.plot(range(epoch_num), test_loss_list, label='test loss')
plt.legend()
