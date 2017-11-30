import random
heads = 0
tails = 0
number = int(input('How many times should the coin be flipped: '))
for x in range (0,number):
	flip = random.uniform(0,1)
	if flip < .5:
		tails = tails + 1
	else:
		heads = heads + 1
percent = (heads / (tails + heads)) * 100
print ('You got heads', percent, 'percent of the time')

