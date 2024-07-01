from torch.utils.data import Dataset, DataLoader

class Reviews(Dataset):
    def __init__(self) -> None:
        super().__init__()