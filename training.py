import json
from tokenize import tokenize

import numpy
import nltk
import numpy as np

from main import stem, bag_of_words

nltk.download('punkt')
import torch
import torch.nn as nn
from torch.utils.data import Dataset , DataLoader

with open('intents.json' , 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []
for intent in intents['intents']:
    tag = intent['tag']
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w,tag))

ignore_words = ['?','!',',','.']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

x_train = []
y_train = []
for (pattern_sentence , tag ) in xy:
    bag = bag_of_words(pattern_sentence , all_words)
    x_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)

new_output_size = 1000

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples

batch_size = 114
hidden_sizw = 114
output_size = new_output_size
input_size = len(x_train[0])
learning_rate = 0.001
num_epochs = 1000


