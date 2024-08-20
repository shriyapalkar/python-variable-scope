# outside function 
def outer():
    message='local'
    
    #nested function
    def inner():
        #declare nonlocal variable
        nonlocal message
        
        message ='nonlocal'
        print('inner:',message)
        
    inner()
    print("outter:",message)
outer()