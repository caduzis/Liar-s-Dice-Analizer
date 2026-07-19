import cv2
import numpy as np
from pathlib import Path
import os

class TemplateLoader:
    CACHE_FILE = Path("assets/dices_cache.npz")
    
    @classmethod
    def load_dice_grid(cls, base_folder_path: str, force_rebuild: bool = False) -> dict:

        caminho_absoluto = os.path.abspath("assets/dices_cache.npz")
        print(f"[DEBUG] O Python tentou salvar/ler o arquivo EXATAMENTE aqui: {caminho_absoluto}")

        if cls.CACHE_FILE.exists() and not force_rebuild:
            print("[CACHE_LOG] Loading templates from Binary Cache (.npz)...")

            with np.load(cls.CACHE_FILE, allow_pickle=True) as data:
                return data['memory_card'].item()
        
        print("[CACHE_LOG] Building Memory Card from PNG Files...")
        memory_card = {}
        base_path = Path(base_folder_path)

        for folder in base_path.iterdir():
            print("DEBUG Loop Folder")
            if folder.is_dir():
                dice_face_name = folder.name
                memory_card[dice_face_name] = []

                for img_file in folder.glob("*.png"):
                    print(f"Debug test - File Name: {img_file.name} \n")
                    img_array = cv2.imread(str(img_file), cv2.IMREAD_GRAYSCALE)
                    if img_array is not None:
                        memory_card[dice_face_name].append(img_array)
        
        print("[CACHE_LOG] Saving new Binary Cache (.npz) on disk...")
        cls.CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(cls.CACHE_FILE, memory_card=memory_card)
        
        return memory_card
    
if __name__ == "__main__":
    TemplateLoader.load_dice_grid("assets/template_test")

        