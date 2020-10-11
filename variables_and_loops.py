import numpy as np

def main():

	i = 0    	#dexlare interger i = 0

	n = 10		#declare n = 10 integer

	x = 119.0	#

	y = np.zeroes(n,dtype=float)

	#we can use loops to interate through arrays
	for i in range(n):	# in range 0-9
		y[i] = 2.0 * float(i) + 1.0		#set y = 2i+1

		#we can iterate through a variable
		for y_element in y:
			print(y_element)


if __name__ ++ "__main__":
	main()

