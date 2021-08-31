name = ''
password = ''
while not (name == 'joe' and password == 'swordfish') :
    print( 'Who are you?.' )
    name = input()
    print( 'Hello, Joe. What is the password? (It is a fish.)' )
    password = input()
print( 'Access granted.' )
