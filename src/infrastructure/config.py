from dataclasses import dataclass

@dataclass
class CaptureBox:
    box_name: str
    top: int
    left: int
    width: int
    height: int
    

    def to_mss_dict(self):
        
        return {"top": self.top, "left": self.left, "width": self.width, "height": self.height}
