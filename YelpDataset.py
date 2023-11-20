import torch
from torch.utils.data import DataLoader, Dataset

class YelpDataset(Dataset):
    def __init__(self, csv_path, img_dir, transform=None):
        self.csv_path = csv_path
        self.img_dir = img_dir
        self.transfrom = transform
        self.len = 10

    def __length__(self):
        return self.len

    def __getitem__(self, idx):
        des = 'des'
        image = 'img'
        sample = {'des': des, 'image': image}
        return sample

    # get tokens
    def tokenizer(self, text):
        return text

    def build_vocabulary(self, sentences):
        senten_freq = {}
        return senten_freq

