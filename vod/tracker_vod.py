from dotenv import load_dotenv
import os

import numpy as np
import cv2 as cv

def locate_minimap(frame): 

    # convert images to gray for template matching
    minimap = cv.cvtColor(cv.imread('vod/minimap.png'), cv.COLOR_BGR2GRAY)
    game = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    length = minimap.shape[0]
    match, location, scale = 0, (0, 0), 0

    # iterate through smaller sizes of minimap template
    for scale in np.linspace(0.33, 1, 15):
        scaled_length = int(length * scale)
        scaled_minimap = cv.resize(minimap, (scaled_length, scaled_length), interpolation=cv.INTER_AREA)
        res = cv.matchTemplate(game, scaled_minimap, cv.TM_CCOEFF_NORMED)
        _, val, _, loc = cv.minMaxLoc(res)
        if val > match:
            match, location, minimap_length = val, loc, scaled_length

    x1, y1 = location[0], location[1] # top-left
    x2, y2 = x1 + minimap_length, y1 + minimap_length #bottom-right
    
    return x1, y1, x2, y2

if __name__ == "__main__":

    load_dotenv()

    capture = cv.VideoCapture(os.getenv('VIDEO_PATH'))

    found = False

    while True:
        isTrue, frame = capture.read()

        if not found:
            x1, y1, x2, y2 = locate_minimap(frame)
            found = True

        cv.imshow('Video', frame[y1:y2, x1:x2]) 

        if cv.waitKey(20) & 0xFF==ord('q'):
            capture.release()
            break
    
    cv.destroyAllWindows()


