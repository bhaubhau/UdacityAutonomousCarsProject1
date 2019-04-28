import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Read in the image
image = mpimg.imread('colors.png')
print('image pixels')
print(image)

print('red component')
print(image[:,:,0])

print('green component')
print(image[:,:,1])

print('blue component')
print(image[:,:,2])

print('slice')
print(image[:,1,1])