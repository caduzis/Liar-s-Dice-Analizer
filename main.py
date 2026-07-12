from src.infrastructure import ScreenCapture, Bid_Reader, CaptureBox, time_monitor, DiceChecker

@time_monitor
def main():
    bid_reader = Bid_Reader()
    myDice_checker = DiceChecker(dice_template_path="assets\myDices_template")


    valueBid_CaptureBox = CaptureBox(box_name="valueBid",left=244, top=6, width=43, height=40)
    value_capture = ScreenCapture(valueBid_CaptureBox)
    imageValueBid = value_capture.capture()
    print(imageValueBid[0].shape)
    print(imageValueBid[1])
    valueBid_reading_info= bid_reader.read_bid(imageValueBid)
    print(f"What was read: {valueBid_reading_info[0]} , Reading precison: {valueBid_reading_info[1]}")

    print("\n\n")

    diceBid_CaptureBox = CaptureBox(box_name="diceBid",left=303, top=7, width=40, height=40)
    dice_capture = ScreenCapture(diceBid_CaptureBox)
    imageDiceBid = dice_capture.capture()
    print(imageDiceBid[0].shape)
    print(imageDiceBid[1])
    

    print("\n\n")

    myDices_CaptureBox = CaptureBox(box_name="myDices",left=400, top=600, width=1370, height=400)
    myDices_capture = ScreenCapture(myDices_CaptureBox)
    imageMyDices = myDices_capture.capture()
    print(imageMyDices[0].shape)
    print(imageMyDices[1])
    dices_found = myDice_checker.get_dice_matches(imageMyDices, True)
    print(dices_found)


    print("\n\n")

if __name__ == "__main__":
    main()