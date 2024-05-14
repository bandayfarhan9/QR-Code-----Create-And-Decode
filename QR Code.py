import qrcode
from pyzbar.pyzbar import decode
import cv2

# Create and save the QR code images
img_link = qrcode.make("//enter a link//")
img_link.save("img1.jpg")

img_data = qrcode.make("//enter data//")
img_data.save("img2.jpg")

# Read and decode the QR code images
image1 = cv2.imread("img1.jpg")
image2 = cv2.imread("img2.jpg")

decoded_data1 = decode(image1)
decoded_data2 = decode(image2)

# Print the decoded data
print("Decoded data from img1.jpg:", decoded_data1)
print("Decoded data from img2.jpg:", decoded_data2)
