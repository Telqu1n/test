def info():
    print("Enter a name")
    info.name input()
    
    while not info.name.isalpha():
        print("Invalid name")
        info.name = input()
        
    while not info.name.isdigit():
        print("Invalid name")
        info.name = input()
        
    while not info.name.isalnum():
        print("Invalid name")
        info.name = input()
        
    while not info.name.isspace():
        print("Invalid name")
        info.name = input()