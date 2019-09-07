import numpy as np
import skimage.measure
import scipy
import scipy.ndimage
import math
import matplotlib.pyplot as plt
import cv2
import random
import statistics as s



EPOCHS = 6

#DIMENSIONS OF THE IMAGE:(275,183)


#loading in all of the images as copies
for i in range(1,6):
    globals()['cat%s' % i] = cv2.imread("cat" + "{}".format(i) + ".jpg",0).copy()

starting_filter = [1,1,1,
		   1,1,1,
		   1,1,1]
for i in range(0,274):
	#convolutional step
	cat1[i] = np.convolve(cat1[i],starting_filter,'same')

#max pooling
cat1= skimage.measure.block_reduce(cat1,(11,61),np.max)


cat2 = skimage.measure.block_reduce(cat2,(3,5),np.mean)


plt.imshow(cat1,cmap = 'gray')

plt.show()


#print(cat2.shape)
#flattening 
cat1 = cat1.flatten()

c_num = s.mean(cat1)

random_weight = np.random.rand(1,1)

output = c_num*random_weight

#print(output)

predicted = 200

error = abs(predicted - output)

print(error)
#print(cat2.shape)


