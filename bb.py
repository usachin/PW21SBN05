import cv2
import numpy as np

img = cv2.imread("working_man_coco.jpg")

classes_90 = ["class list"] 


def test_negative(p):
	for i in range(len(p)):
		p[i] = int(float(p[i]))
		if(p[i]<0):
			p[i] = 0
	return p
bb = {'laptop': ['168.23457,6.927069,406.19733,230.25603'], 'person': ['-4.638708,231.86166,199.58554,460.63354']
, 'cell phone': ['402,211,507,292', '324,241,400,319'], 'book': ['465.1817,257.5819,636.49304,397.92422'],
 'bottle': ['443.14145,66.57839,524.3761,214.45682'], 'tennis racket': ['237.3369,356.8553,435.65707,463.1731'
]----} # assigh BB output dict

COLORS = np.random.uniform(0, 255, size=(len(classes_90), 3))
for i in bb.keys():
	idx = classes_90.index(i)
	for j in bb[i]:
		p = j.split(",")
		points = test_negative(p)
		cv2.rectangle(img,(points[0],points[1]),(points[2],points[3]), COLORS[idx],2,1)
		label = "{}".format(i)
		startY = points[1]
		startX = points[0]
		y = startY - 15 if startY - 15 > 15 else startY + 15
		cv2.putText(img, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
cv2.imwrite("bb_image.jpg", img)