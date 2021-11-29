# pip install opencv-python
import cv2 as cv

im = cv.imread('covid-cert.png')
det = cv.QRCodeDetector()
retval, points, straight_qrcode = det.detectAndDecode(im)

print(retval)
print(points)
print(straight_qrcode)