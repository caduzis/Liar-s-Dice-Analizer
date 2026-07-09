import easyocr
from src.infrastructure.utils import time_monitor

class Bid_Reader:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    @time_monitor
    def read_bid(self, imageInfoTuple):
        reader = easyocr.Reader(['en'])
        path = imageInfoTuple[1]
        result = reader.readtext(f"{path}")
        text_read = result[0][1]
        text_precision = round(float(result[0][2]), 3)

        return text_read, text_precision

if __name__ == "__main__":
    pass
        