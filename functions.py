import numpy as np
imprt sys
 #Define a fujctio that returns a vule
 def expo(x):
 	return np.exp(x) #return the np e^x funtion


#define subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))	#call the expo func


#define our main function
def main():

	n = 10

	#check if there is a command line arg provided
	if(len(sys.argv) > 1):
		n = int(sys.argv[1]) #if an arg was provided, set n to it

	show_expo(n) #call the show expo sub

#run the main function
if __name__ == "__main__":
	main()