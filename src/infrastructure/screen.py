import mss
import numpy as np
from mss.screenshot import ScreenShot
from src.infrastructure.utils import time_monitor
from src.infrastructure.config import CaptureBox

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
            path_file = "src/infrastructure/screenshots" + f"/{file_name}"
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=path_file)
            print(f"Salvo nome do arquivo: {file_name}")
            
            return np.array(sct_img), path_file
        
if __name__ == "__main__":
    pass

            

    