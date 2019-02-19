import torch
from Linear import Linear
from ReLU import ReLU
from Dropout import Dropout
from BatchNorm import BatchNorm1D
from Model import Model
from Criterion import CrossEntropy
import torchfile
import math
from util import *

device = get_device(1)

data_folder = "../data/dataset/"
input_data, input_labels = get_data(data_folder)
input_data = normalize_data(input_data)
train_data, train_labels, val_data, val_labels = split_data(input_data, input_labels)

batch_size = 500
epochs = 20

# lr = [0.9,0.05] # lr, friction
lr = [0.01]
model = Model(lr, "GradientDescent")
model.addLayer(Linear(train_data.shape[1], 10))
# model.addLayer(BatchNorm1D(1024))
# model.addLayer(ReLU())
# model.addLayer(Linear(1024, 512))
# model.addLayer(BatchNorm1D(512))
# model.addLayer(ReLU())
# model.addLayer(Linear(512, 256))
# model.addLayer(BatchNorm1D(256))
# model.addLayer(ReLU())
# model.addLayer(Linear(256, 6))
model.set_device(device)

for epoch in range(epochs):

	for i in range(int(math.ceil(train_data.shape[0]/batch_size))):

		data = train_data[batch_size*(i) : batch_size*(i+1), :]
		target = train_labels[batch_size*(i) : batch_size*(i+1), :]

		out = model.forward(data)
		pred = torch.max(out, 1)[1]
		accuracy = torch.sum(pred.reshape(-1) == target.reshape(-1))

		loss = CrossEntropy.forward(out, target)
		model.backward(CrossEntropy.backward(out, target))
		model.setLearningRate(lr)
		print("Epoch = %d : Loss = %f : Accuracy = %d/%d" % (epoch, loss, accuracy, data.shape[0]))