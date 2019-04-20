import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

ysize = 15
xsize = 10

left_bottom = [2, 11]
right_bottom = [8, 13]
apex = [5, 2]

fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, 15))


print('XX')
print(XX)
print('YY')
print(YY)

region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))
print('region thresholds')
print(region_thresholds)

