import init_spark as sp
import model.model
import glob
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
#import torchvision.transforms as transforms

sp.init_spark()
test_name = ""
test_path = "test.csv/*.csv"
for file in glob.glob(test_path):
    test_name = file
test = pd.read_csv(test_name, encoding = "UTF-8")
train_name = ""
train_path = "train.csv/*.csv"
for file in glob.glob(train_path):
    train_name = file
train = pd.read_csv(train_name, encoding = "UTF-8")

test_tensor = torch.Tensor(test.values)
train_tensor = torch.Tensor(train.values)

print(train_tensor.shape)

# It's time to train our data
dataloader = DataLoader(train_tensor, batch_size=300, shuffle=True)