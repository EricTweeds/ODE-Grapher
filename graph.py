import numpy as np
import matplotlib.pyplot as plt
from numpy import *

def graph(equation, colour):
	#0,9 for the interval, 300 for the accuracy
	x = np.linspace(0,9,300)
	y = eval(equation)
	plt.plot(x,y,colour)

def getInput(count):
	try:
		equation = input("Equation "+str(count+1)+":")
		return equation
	except SyntaxError:
		equation = None
	except NameError:
		print("invalid input")
		equation = getInput(count)
		return equation

#The colour of each function need to be different
colours = ['b','r','g', 'k', 'm', 'y', 'c']
count = 0

equation = getInput(count)

#Requests up to 8 equations or user enters a blank equation
while (equation is not None and count < 7):
	graph(equation, colours[count])
	count += 1
	equation = getInput(count)

plt.grid()

#straight line at 0 to represent X-axis
plt.plot([0,9], [0,0], 'k')
plt.show()