import mss
import numpy as np
from mss.screenshot import ScreenShot
from utils import time_monitor
from config import CaptureBox

class ScreenCapture(ScreenShot):
    def __init__(self, regionofinterest: CaptureBox):
        self.monitor_number = 1
        self.roi_name = regionofinterest.box_name
        self.roi_dict = regionofinterest.to_mss_dict()

    @time_monitor
    def capture(self):

        with mss.MSS() as sct:

            sct_img = sct.grab(self.roi_dict)
            file_name = f"{self.roi_name}.png"
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=file_name)
            print(f"Salvo nome do arquivo: {file_name}.png")
            return np.array(sct_img)
        
if __name__ == "__main__":
    diceBid_CaptureBox = CaptureBox(box_name="diceBid",top=303, left=7, width=40, height=40)
    valueBid_CaptureBox = CaptureBox(box_name="valueBid",top=244, left=6, width=43, height=40)

    screen_capture = ScreenCapture(diceBid_CaptureBox)
    imageBid = screen_capture.capture()
    
    screen_capture = ScreenCapture(valueBid_CaptureBox)
    imageValue = screen_capture.capture()

    print(imageValue.shape)
    print("\n")
    print(imageBid.shape)


            

    