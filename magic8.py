# In magic8.py, declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.
name = 'Chris'

# Next, declare a variable question, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.
question = 'Is the earth flat'

# We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.
answer = ''

# In Python, we can use the .randint() function from the random module to generate a random number from a range.

# But first, let’s import this module so we can use its functions. Add this line of code to the top of magic8.py:

import random

# Next, we’ll create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call:

random_number = random.randint(1, 9)

# Now that we’ve declared all the variables needed, it’s time to implement the core logic of our program!

# For this section, we’ll be utilizing control flow using an if/elif/else statement to assign different answers for each randomly generated value.

# First, write an if statement where if the random_number is equal to 1, answer is assigned to the phrase “Yes - definitely.”

# Next, write an elif statement after the if statement where if the random_number is equal to 2, answer is assigned to the phrase “It is decidedly so”.

# Then, continue writing elif statements for each of the remaining phrases for the values 3 to 9.

# Following the if/elif statements, add an else statement that will set answer to the string “Error”, if the number was accidentally assigned a value outside of our range.

if random_number == 1:
  answer = 'Yes, definitely.'
elif random_number == 2:
  answer = 'It is decidedly so.'
elif random_number == 3:
  answer = 'Without a doubt.'
elif random_number == 4:
  answer = 'Reply hazy, try again.'
elif random_number == 5:
  answer = 'Reply hazy, try again.'
elif random_number == 6:
  answer = 'Better not tell you now.'
elif random_number == 7:
  answer = 'My sources say no.'
elif random_number == 8:
  answer = 'Outlook not so good.'
elif random_number == 9:
  answer = 'Very doubtful.'
else:
  answer = "Error"

# Now, let’s see our program in action! Write a print() statement to output the asker’s name and their question, which should be in the following format: [Name] asks: [Question]

print(name + ' asks: ' + question)

# Add a second print() statement that will output the Magic 8-Ball’s answer in the following format: Magic 8-Ball's answer: [answer]

print("Magic 8-Ball's: " + answer)

# What if the asker does not provide a name, such that the value of name is an empty string? If the name string is empty, the output of the program looks like the following: asks: Will I win the lottery?

# asks: Will I win the lottery
# Magic 8 Ball's answer: Outlook not so good

# As you can see, the formatting of the output can use some improvement when there is no name provided.

# We can address this by printing out just the question, such that it looks like the following:

# Question: Will I win the lottery?
# Magic 8 Ball's answer: Outlook not so good

# You can implement this by creating an if/else statement such that:

# If the name is an empty string, it will only print the question.
# Else, the player’s name and question are both printed.

if name == '':
  print(question)
else: 
  print( name + ' asks: ' + question)

# What if the question string is empty? If the user does not provide any question, then the Magic 8-Ball cannot provide a fortune, otherwise, the fabric of reality is at risk!

# To ensure that the fabric of reality is safe, we can create an if/else statement where:

# If the question is an empty string, print out a message to the user.
# Else, print the name and question, with the Magic 8-Ball’s answer.

if question == '':
  print('No Question Asked')
else:
  print("Magic 8-Ball's: " + answer)






