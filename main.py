import os
import cv2 as cv
from dotenv import load_dotenv

from vod.tracker_vod import locate_minimap

if __name__ == "__main__":

    mode = "VOD"
    load_dotenv(override=True)

    if mode == "VOD":

        capture = cv.VideoCapture(os.getenv('VIDEO_PATH'))
        found = False
        i = 1

        while True:   
            isTrue, frame = capture.read()

            if not found:
                x1, y1, x2, y2 = locate_minimap(frame)
                found = True

            cv.imshow('Video', frame[y1:y2, x1:x2]) 

            if cv.waitKey(10) == ord("q"):
                capture.release()
                break
        
        cv.destroyAllWindows()

    elif mode == "API":
        pass