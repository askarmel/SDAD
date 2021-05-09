from torch.utils.data import Dataset
import pandas as pd

SAMPLE_FILENAME = 'art_daily_no_noise.csv'
DATA_PATH = '~/FSDL/SDAD/data/artificialNoAnomaly/'


class MyDataset(Dataset):
    def __init__(self, filename=SAMPLE_FILENAME, path=DATA_PATH, q=5):
        try:
            data_frame = pd.read_csv(path + filename)
        except Exception as e:
            print(e)
            exit(1)

        self.data = data_frame.values
        self.q = q

    def __len__(self):
        return self.data.shape[0] // self.q

    def __getitem__(self, index):
        return self.data[index * self.q: (index + 1) * self.q]


dt = MyDataset()
