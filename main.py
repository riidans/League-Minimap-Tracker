import cv2 as cv
from minimap_tracker import locate_minimap

if __name__ == "__main__":
    frame = cv.imread('game_example.png')
    x1, y1, x2, y2 = locate_minimap(frame)
    minimap = frame[y1:y2, x1:x2]
    cv.imshow('g', minimap)
    cv.waitKey(0)  