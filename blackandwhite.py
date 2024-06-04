# import cv2

# # Load the color image
# image = cv2.imread('image.jpg')

# # Convert the image to grayscale (black and white)
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Save the grayscale image
# cv2.imwrite('black_and_white_image.jpg', gray_image)


# from PIL import Image, ImageOps
# image = Image.open('image.jpg')
# gray_image = ImageOps.grayscale(image)
# gray_image.save('baw_image.jpg')


from PIL import Image

# Open the image file
img = Image.open('image.jpg')

# Split the image into individual bands (red, green, blue)
r, g, b = img.split()

# Convert each band to black and white by thresholding
r_bw = r.point(lambda x: 255 if x > 127 else 0)
g_bw = g.point(lambda x: 255 if x > 127 else 0)
b_bw = b.point(lambda x: 255 if x > 127 else 0)

# Merge the black and white bands back into a single image
img_bw = Image.merge('RGB', (r_bw, g_bw, b_bw))

# Save the black and white image
img_bw.save('output_image.jpg')