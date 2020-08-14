import turtle as t
bob = t.Turtle()    # Open window
bob.fd(100) # Move forward by 100 pixels
for i in range(3):
    bob.lt(90)  # Turn left by 90 degrees
    bob.fd(100)
t.mainloop()    # Wait for user input
