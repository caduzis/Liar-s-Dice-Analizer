import cv2
import numpy as np
import math
from pathlib import Path


class DiceChecker:
    
    def __init__(self,  dice_template_path: str):
        self.templates = {}
        template_folder = Path(dice_template_path)

        for file_path in template_folder.glob("*.png"):
            dice_value = file_path.stem
            template_image = cv2.imread(str(file_path), cv2.IMREAD_GRAYSCALE)
            if template_image is not None:
                self.templates[dice_value] = template_image
        
    def get_dice_matches(self, image_data: tuple[np.ndarray, str]):
        imgArray, imgPath= image_data
        canvas_debug = imgArray.copy()
        gray_image = cv2.cvtColor(imgArray, cv2.COLOR_BGR2GRAY)
        
        dices_found = {}

        for dice_value, template in self.templates.items():
            result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
            height, width = template.shape
            threshold = 0.7 # not reconizing all dices
            locations = np.where(result >= threshold)
            points = list(zip(*locations[::-1]))
            confirmed_points = []
            
            for x, y in points:
                new_dice = True
                # A for loop is skipped entirely 
                # when a list is empty 
                # because there are no elements available 
                # to trigger an iteration
                for confirmed_x, confirmed_y in confirmed_points:
                    if math.dist((x,y), (confirmed_x,confirmed_y)) > 25:
                        new_dice = False
                        break
                if new_dice:
                    confirmed_points.append((x,y))
                    # Debug window, showing a bouding box around the element that was matched
                    cv2.rectangle(canvas_debug, (confirmed_x, confirmed_y), (confirmed_x + width, confirmed_y + height), (0, 0, 255))
                    cv2.imshow('Dices', canvas_debug)
                    cv2.waitKey(0)
                    # \\-------------------------------------//
                    
            dices_found[dice_value] = len(confirmed_points)
        
        return dices_found
        
                
                


                
            


    



