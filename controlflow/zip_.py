# python code to demonstrate working of zip()

# initializing list
questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']

# using zip() to combine two containers
# and print values
for question, answer in zip(questions, answers):
    print('What is your {0}? I am {1}.'.format(question, answer))
