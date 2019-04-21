import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

lines=[[[0,0,5,6]],[[7,0,4,3]],[[1,1,0,3]],[[3,4,7,8]]]
left_lines=[]
left_slopes=[]
left_coefficients=[]
right_lines=[]
right_slopes=[]
right_coefficients=[]

for line in lines:
    for x1,y1,x2,y2 in line:
        print('x1:' + str(x1) + ' y1:' + str(y1) + ' x2:' + str(x2) + ' y2:' +str(y2))
        if x1!=x2:
            slope=((y2-y1)/(x2-x1))
            print('slope:' + str(slope))
            if slope>0:
                right_lines.append([[x1,y1,x2,y2]])                
                coeffs=np.polyfit((x1, x2), (y1, y2), 1)
                right_slopes.append(coeffs[0])
                right_coefficients.append(coeffs[1])
            else:
                left_lines.append([[x1,y1,x2,y2]])
                coeffs=np.polyfit((x1, x2), (y1, y2), 1)
                left_slopes.append(coeffs[0])
                left_coefficients.append(coeffs[1])

print('right')
print(right_lines)

print('right slopes')
print(right_slopes)

print('right coeffs')
print(right_coefficients)

print('left')
print(left_lines)

print('left slopes')
print(left_slopes)

print('left coeffs')
print(left_coefficients)


# x = [2, 5, 6]
# y = [1, 3, 5]
# plt.plot(x, y)

#plt.imshow(lines)

#plt.show()

x = np.array([2.5,3,1,0])

print(x)