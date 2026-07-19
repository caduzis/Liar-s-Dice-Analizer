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
    
    # not reconizing all dices, need fix
    def get_myDices_match(self, image_data: tuple[np.ndarray, str], debug_mode: bool = True):
        imgArray, imgPath= image_data
        canvas_debug = imgArray.copy()
        gray_image = cv2.cvtColor(imgArray, cv2.COLOR_BGR2GRAY)
        
        dices_found = {}

        for dice_value, template in self.templates.items():
            result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
            height, width = template.shape
            threshold = 0.8 # 0.6 make matches skyrocket
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
                    if math.dist((x,y), (confirmed_x,confirmed_y)) < 20:
                        new_dice = False
                        break
                if new_dice:
                    confirmed_points.append((x,y))
                    if debug_mode:
                        # Debug window, showing a bounding box around the element that was matched
                        cv2.rectangle(canvas_debug, 
                                      (x, y), 
                                      (x + width, y + height), 
                                      (0, 0, 255), 2)
                        # \\-------------------------------------//
                    
            dices_found[dice_value] = len(confirmed_points)

        if debug_mode: 
            cv2.imshow('Dices', canvas_debug)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return dices_found
    
    def get_diceBid_match(self, image_data: tuple[np.ndarray, str], debug_mode: bool = True):
        imgArray, imgPath= image_data
        canvas_debug = imgArray.copy()
        gray_image = cv2.cvtColor(imgArray, cv2.COLOR_BGR2GRAY)

        best_score = 0.0
        best_dice = None
        best_loc = None
        best_dims = (0, 0)

        for dice_value, template in self.templates.items():
            result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            if max_val >= 0.8 and max_val > best_score:
                best_score = max_val       
                best_dice = dice_value   
                best_loc = max_loc         
                best_dims = template.shape 
                
        if best_dice is not None:
            
            if debug_mode:
                x, y = best_loc
                h, w = best_dims
                cv2.rectangle(canvas_debug, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                cv2.putText(canvas_debug, f"{best_dice}: {best_score:.2f}", (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

                cv2.imshow('Bid Dice (Aposta)', canvas_debug)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
            return best_dice 
            
        return "Nenhum dado encontrado"


                


                
            


    



