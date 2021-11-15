from datasets import load_from_disk, load_dataset
import pandas as pd


mrc_datasets = load_from_disk('../data/train_dataset/')

#mrc_train_dataset = mrc_datasets['train']
mrc_valid_dataset = mrc_datasets['validation']
#print('train----')
#print(len(mrc_train_dataset))
print('valid-------')
print(len(mrc_valid_dataset))
print(mrc_valid_dataset[444])