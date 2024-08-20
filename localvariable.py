def greet():
    #local variable
    message ='hello'
    print('local',message)
greet()
#try to access msg variable
#outside greet() function
print(message)