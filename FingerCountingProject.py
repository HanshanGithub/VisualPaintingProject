import cv2
import time
import os
import mediapipe as mp

mpDraw = mp.solution.land_marks
mpFingerCount = 2
FingerCounting = mpFingerCount.imag