from src.infrastructure import ScreenCapture, Bid_Reader, CaptureBox, time_monitor

if __name__ == "__main__":
    bid_reader = Bid_Reader()
    valueBid_CaptureBox = CaptureBox(box_name="valueBid",left=244, top=6, width=43, height=40)

    screen_capture = ScreenCapture(valueBid_CaptureBox)
    imageValueBid = screen_capture.capture()
    print(imageValueBid[0].shape)
    print(imageValueBid[1])
    reading_info= bid_reader.read_bid(imageValueBid)
    
    print(f"What was read: {reading_info[0]} , Reading precison: {reading_info[1]}")