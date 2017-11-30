#Canaan Case - 10/1/17
#On my honor, I have neither given nor recieved unauthorized aid - canaan case
#In this project, I wanted to write a story about being stranded in the desert taking inspiration from hussain. I also had the cool idea of using a genie of kinds with a random number game that led to a mulitude of different outcomes depending on the number rolled. Overall, I wanted to tell a good and engaging story while also using lots of different kinds of code we learned this year.
#Sources 
	#-https://stackoverflow.com/questions/12774279/how-to-check-if-a-variable-is-equal-to-one-string-or-another-string, 
	#-https://stackoverflow.com/questions/15099379/limit-input-to-integer-only-text-crashes-python-program this source helped me with sorting out the details of the try and except functions  

import random

def playAgain(): #i used this fn to simplify my code and avoid repeating the following code every single death
	global playagain
	playagain = input('You have lost, play again? y/n: ')
	while playagain not in ('y', 'n'):
		playagain = input('Please enter y or n: ')
	start()	


def left(): #my left function, which again splits into two paths
	global playagain
	#source - https://stackoverflow.com/questions/12774279/how-to-check-if-a-variable-is-equal-to-one-string-or-another-string
	#I used this source to help with error checking and while statements 
	print('Ah the path into the cave, a good but dangerous choice.')
	print('You walk into the cave and continue, down into the depths.')			
	print('Eventually, you reach a split in the path.')
	print('You see a wall which looks breakable and a hole which leads deeper into the cave.')
	print('')
	walls = input('You could either break [break] the wall or climb down the hole [climb], which do you do? : ') 
	#after each variable i used to a while loop (source 1) to say that when each variable was not one of the options i watned, you are forced to re enter said variable
	while walls not in ('break', 'climb'): #code i got from source number 1, helpful with error checking
		walls = input('Please enter break or climb. Play by the rules. : ')

	if walls in ('break'): #once the variable is entered correctly, i used a simple if statement
		wall()

	else:
		climb()				


def climb(): #another path, which leads to death
	global playagain
	print('You opt to delve even deeper into the cave and test your luck.')
	print('You proceed to climb down the rock wall when suddenly your handhold cracks and seperates from the wall!')
	print('With nothing to grip, you fall down into the chasm beneath you.')
	print('')
	playAgain()


def wall(): #a path that leads to the genie and the dice game
	print('You back up, and charge full speed into the wall which tumbles down in a plethora of dust.')
	print('What you find behind the wall amazes you.')
	print('You see a room full of treasure, with a rustic table sitting in the center.')
	print('')
	print('On top of the table lies an old lamp which has a tempting aura about it.')
	print('You rub the lamp, and much to your surprise, a genie comes out.')
	print('')
	genie()


def right(): #the right path
	global playagain 
	print('You set off into the dunes, hoping you find some miracle amongst the sun scorched landscape.')
	print('You travel for what seems like days, walking in circles through the endless desert.')
	print('Just as you are about to give up, you hear the sound of thundering hoofbeats approaching.')
	print('As they get closer, you realize that these horsemen are foes not friends, and they start to charge at you.')
	print('')
	riders = input('You can attepmt to make peace [peace] with the horsemen or run away [run]. What do you do: ')

	while riders not in ('run', 'peace'): 
		riders = input('please enter run or peace: ')

	if riders in ('run'):
		run()

	else:
		peace()


def run(): #path that leads to number game
	global playagain #these global playagain statements are needed to allow playagain to work throughout the entire fucntion. Otherwise, playagin is stored locally wihthin each function
	print('You sprint immidiatley off into the dunes, but the horsemen are too quick and begin gaining ground.')
	print('Fortunately for you, a sandstorm starts to kick up, and you manage to lose your pursuers.')
	print('')
	print('You continue running for hours, and when the dust settles down, you look into the distance and see an abandoned city of some kind')
	print('You approach the city, and see a temple like structure in the center of a plaza.')
	print('Suddenly, you hear the sound of hoofbeats and are forced to enter.')
	print('Insdie the temple, you see an old man sitting alone at a table meant for two.')
	print('')
	oldMan()


def peace(): #death path
	global playagain
	print('You attempt to speak to the horsemen and get down on your knees while they circle around you.')
	print('One man dismounts, and approaches you. You try to speak to him, but he doesnt seem to understand you.')
	print('He looks at you menacingly, before speaking to one of his companions in some foreign tounge.')
	print('The burly bearded man walks up to you, slowly draws a balde from his belt, and slices your head clean off!')
	print('')
	playAgain()	


def start(): #the start function that also encompasses play again
	global playagain
	if playagain in ('y'): #if playagain is yes, it restarts the game
		print('')
		print('You wake up suddenly, stranded in the middle of the Bahrainian Desert.')
		print('You are thirsty and set off into the desert, searching for water.')
		print('A mountain looms ahead, and you have two paths to take') 
		print('')
		print('The left path leads to a narrow canyon with aof cave at the end.')
		print('The right leads towards the dunes that you pray will conceal an oasis of some kind.')
		path = str(input('Which path do you choose, the cave [left] or the dunes [right]??: '))
		print('')

		while path not in ('left', 'right'):
			path = input('Please enter left or right: ')
			print('')

		if path in ('left'):
			left()	
		
		else:
			right()
	else: 
		print('Bye!') #otherwise, it says bye!

def genie(): #my genie and his die, lists the 6 options
	print('The genie hands you a die, saying that depending on what you roll, all your your dreams or all your nightmares will come true.')
	print('The genie lamented, "There are 6 outcomes, with each number on the die representing one of the possiblities. Allow me to explain."')
	print('')
	print('')
	print('In the event of a 1, you die, but quickly and without pain')
	print('If you roll a 2, I will grant you a weapon to defeat all of your enemies.')
	print('A 3 means that I will send you back time and you shall have a second chance to make your decisions.')
	print('4 is an intresting one, which I shall explain if you happen to roll it.')
	print('If you roll a 5, you shall recieve wealth beyond measure')
	print('And a 6, oh, oh, oh, do not roll a 6')
	print('')

	die = input('Do you roll [roll] the die or refuse [refuse]: ')

	while die not in ('roll', 'refuse'):
		die = input('please enter roll or refuse: ')
	#you have to roll the die no matter what
	if die == 'roll': 
		print('')
		DieOutcomes()

	else: 
		print('Sorry thats not how this works. Either you roll the die or I do. Thats what happens when you wake up a genie from a thousand year slumber. ')	
		print('Bedrudgingly, you roll the die.')
		print('')
		DieOutcomes()


def DieOutcomes():
	global playagain
	rolls = random.randrange(0,6) #this generates a random number between 1 and 6

	if rolls == 1: 
		print('Oh no, you rolled a 1, that isnt good.')
		print('')
		print('You wake up once again in a horrid and dark place.')								
		print('You spend your few remaining days clawing around in the dark, eventually starving to death.')
		playAgain()

	elif rolls == 2:
		print('Ah yes, you rolled a 2.')
		print('I grant you the sword, Excalibur, to make you undefeateable in combat.')
		print('')
		win2()

	elif rolls == 3: 
		print('A 3, allow me to turn back the passage of time. Of course, you won\'t be allowed to remember this. Bye!')
		print('')
		playagain = 'y'
		start()

	elif rolls == 4: 
		print('A 4, now, let me explain.')
		print('')
		four()

	elif rolls == 5:
		print('')
		print('A 5, you have won the lottery. As promised, I grant you infinite wealth.')
		win3()

	elif rolls == 6:
		print('')
		print('No, no no, that is not supposed to happen. What makes you think you can roll a 6?')
		print('You know what that means, do you not?')
		print('But I have decided I can make an exception, so roll again, quickly, before he notices')
		print('')
		rolls == random.randomrange (0,6)
		#each roll leads to a different path: some victories, some losses, and some that take you back in time to replay scenarios


def four(): #my function for when you roll a 4 with the genie
	print('')
	print('You now get to play a special game with me, he says.')
	print('I have 3 riddles for you. Get them all right, and you may have anything, anything at all you desire.')
	print('Fail to do so, and you will take my place inside that godforsaken lamp until some other foolish traveler rolls a 4.')
	print('Keep in mind, I have had a thousand years to think of these 3 riddles, and its in my best intrest for you to lose, after all, I get my freedom!')
	print('')
	firstRiddle() #makes you answer 3 riddles


def firstRiddle():#the first riddle
	riddle1 = input('My first riddle - I travel all over the world, yet I never leave the corner. What am I: ')
	if riddle1.lower() in ('stamp', 'a stamp'):
		print('Correct')
		print('')
		secondRiddle()
	else: 
		print('No! The answer is a stamp! Bye!')
		riddleLoss()


def secondRiddle(): #second one
	riddle2 = input('The second riddle is this - As a stone inside a tree, I\'ll help your words outlive thee. But as you push me as I stand, the more I move thee less I am. What am I: ')
	if riddle2.lower() in ('pencil', 'a pencil'):
		print('Correct again, well done.')
		print('')
		thirdRiddle()
	else:
		riddleLoss()


def thirdRiddle(): #last one!
	riddle3 = input('My final riddle. Win, and you shall have whatever you desire - What has 13 hearts but no other organs: ')
	if riddle3.lower() in ('a deck of cards', 'cards', 'playing cards', 'deck of cards'):
		riddleWin()
	else:
		print('So close, yet so far, it was playing cards! Bye!')
		riddleLoss()

def riddleWin(): #if all 3 are right
	print('')
	desire = input('Impressive, you are quite witty. Indulge me, what is it you desire most: ')
	print('Very well, I hereby grant you ' + str(desire) + '! That\'s an intresting one but you asked for it.')
	print('With your desrires granted, you live happily ever after.')
	endWin()

def riddleLoss(): #if you lose the riddle game
	global playagain
	print('')
	print('Suddenly, you are sucked inside the lamp, where you lie forever. No one ever rubs or even touches the lamp again, and you live inside the lamp enternally.')
	playAgain()

def oldMan(): #intro to the old man, l
	print('The old man sits you down and welcomes you.')
	print('He hands you a drink and says, please, play my game.')
	print('')
	print('If you win, I will grant you enternal life in paradise.')
	print('But if you lose, you pay the price of playing: life.')
	leaveorstay = input('You can either play [play] or try to go back outside, but the riders will make things difficult [leave]: ')

	while leaveorstay not in ('play', 'leave'):
		print('Please enter leave or stay: ')

	if leaveorstay in ('leave'):
		outside ()
	else:
		game()


def outside(): #death path
	global playagain
	print('')
	print('You decided to head back outside despite the riders that follow you.')
	print('Fortunately, however, when you step into the street of the abandoned city, there seems to be no one there.')
	print('You turn a corner, looking for escape, but run into the tribe of natives once again.')
	print('')
	print('You try to run back the way you came, but more horsemen block your path. You are surrounded.')
	print('The largest of the group moves towards you, and with a swift stroke of his blade, he decapitates you.')
	playAgain()


def win1(): #these are some different win conditions
	print('')
	print('Wow, thats correct')
	print('As promised, you shall recieve your prize.')
	print('You wake up in Elysium, and live enternally in bliss.')
	endWin()


def win2():
	print('With you new sword, you quickly quell the barbarian hordes of Bahrain. They appoint you as your king and you build your kingdom from the ground up.')
	print('You are undefeatable, so your kingdom quickly expands. Eventually, when you tire of combat, you live out your remaining days as king.')
	endWin()

def win3():
	print('With your newfound wealth, you escape from the cave and eventually find your way to a local city, where you quickly make freinds with the inhabitants.')
	print('Eventually, you manage to become a powerful aristocrat in Bahranian society, and you live like a king to the ripe old age of 85.')
	endWin()

def endWin(): #all the win conditions lead here, which offers congratulations and a chance to playagain despite winning 
	global playagain
	print('Congrats, you managed to win!!')
	playagain = input('There are many other ways to win, so play again and try a new path! y/n: ')
	while playagain not in ('y', 'n'):
		playagain = input('Please enter y or n: ')
	start()


def lose(): #the loss outcome to my number game with the old man
	global answer
	global playagain
	print('')
	print('That would be 7 guesses...')
	print('The answer was: ' + str(answer)) #here, i wanted to print out the loss but also the actual answer in case you got really close. i had to convert the answer to a string though. 
	print('Sorry, but all actions have consequences, and you must pay the price.')
	print('Your vision turns to black, and you fall into a deep, deep sleep which you shall never awake from.')
	playAgain()


def game(): #here is my guessing game
	global answer
	#a simple guess a number game
	print('')
	print('He says, I am thinking of a number between 0 and 100 which you have 7 tries to guess.')
	print('Between each guess, I will tell you if you are too high or too low. After 7 tries, you lose! Let us begin.')
	answer = random.randrange(0,100) #first i generate a random number between 1 and 100
	#used a for loop to count the number of guesses
	for i in range(0,7): #https://stackoverflow.com/questions/15099379/limit-input-to-integer-only-text-crashes-python-program this source helped me with sorting out the details of the try and except functions, particularly raise valueError, which i didnt know how to do 
		try: #i needed to use a try statement in order to use the value error function becuase only ints work in the game
			guess = int(input("Guess: ")) #tells you to guess a number
			if not (0 < guess < 100): #if the number isnt between 0 and 100, it raises a value error
				raise ValueError() #got this from source 2

		except ValueError: #value error, forces a re guess
			print('Please enter an integer between 0 and 100. Not enetering ints wastes your guesses... : ')

		else: #these are the too high and too low statements that lead to a correct answer
			if guess > answer:
				print ('Too high')

			elif guess == answer:
				win1() #in the event of a right answer, you are taken to the win functions 
				break #the break statement is necessary to break out of the for loop and end it, otherwise it would keep asking for guesses

			else:
				print ('Too low')

		i = i + 1 #everytime you go through the loop, adds 1 to i to limit the number of guesses to 7

	else: #if you dont get the number after 7 tries, you are taken to the loss function
		lose()


playagain = ('y') #have to define the variable playagain at the start for the program to work, but its redefined every restart

start() #beginning of the program, runs the start function that then leads on to every other fn
