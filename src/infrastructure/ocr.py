import easyocr
from src.infrastructure.utils import time_monitor

class Bid_Reader:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    # If something is blocking the bidCaptureBox, ocur an error
    # in line 15 (text_read = result[0][1]). Because there is no text 
    # in result[0][1]. Need to handle this error in the future.
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
        