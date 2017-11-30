import sys
t = float(input('What is the temperature?? '))
v = float(input('And what is the wind speed??? '))
if -50 < t < 50 and 3 < v < 120:
	w = str(35.74 + (0.6215*t) + ((0.4275*t) - 35.75) * (v**0.16))
	print('The wind chill is ' + w + ' degrees')
else:
	print('Sorry enter a wind speed value betwen 3 and 120 and a temp value between -50 and 50')