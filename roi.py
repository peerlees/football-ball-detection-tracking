# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:11:08 2020

@author: KNUT
"""

import numpy as np
import cv2

col, width, row, height = -1, -1, -1, -1
frame = None
frame2 = None
inputmode = False
rectangle = False
trackWindow = None
roi_hist = None

# 마우스 처리는 강좌 35편에서 보인 예와 아주 비슷합니다.​

def onMouse(event, x, y, flags, param):
    global col, width, row, height, frame, frame2, inputmode
    global rectangle, roi_hist, trackWindow
    
    
# meanShift() 함수에서 키보드 'i'가 입력되면 마우스로 추적할 객체를 지정할 수 있도록 코드를 구현함
    if inputmode:
        if event == cv2.EVENT_LBUTTONDOWN:
            rectangle = True
            col, row = x, y


# 마우스 왼쪽 버튼이 클릭되었을 때 처리할 루틴 작성
        elif event == cv2.EVENT_MOUSEMOVE:
            if rectangle:
                frame = frame2.copy()
                cv2.rectangle(frame, (col, row), (x,y), (0, 255, 0), 2)
                cv2.imshow('frame', frame)

# 마우스가 왼쪽 버튼을 누른채 움직일 때 처리할 루틴 작성
        elif event == cv2.EVENT_LBUTTONUP:
            inputmode = False
            rectangle = False
            cv2.rectangle(frame, (col, row), (x,y), (0, 255, 0), 2)
            height, width = abs(row-y), abs(col-x)
            trackWindow = (col, row, width, height)
            roi = frame[row:row+height, col:col+width]
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            roi_hist = cv2.calcHist([roi], [0], None, [180], [0, 180])
            cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    return

def camShift():
    global frame, frame2, inputmode, roi_hist, trackWindow
    
    try:
        cap = cv2.VideoCapture(0)
    except Exception as e:
        print(e)
        return
    
    ret, frame = cap.read()
    
    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', onMouse, param=(frame, frame2))
    
    termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if trackWindow is not None:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
            ret, trackWindow = cv2.meanShift(dst, trackWindow, termination)
            
            x, y, w, h = trackWindow
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
        cv2.imshow('frame', frame)
        
        k = cv2.waitkey(60) & 0xFF
        if k ==27:
            break
    
        if k == ord('i'):
            print('Select Area for Camshift and Enter a key')
            inputmode = True
            frame2 = frame.copy()
            
            while inputmode:
                cv2.imshow('frame', frame)
                cv2.waitkey(0)
                
    cap.release()
    cv2.destroyAllWindows()

camShift()