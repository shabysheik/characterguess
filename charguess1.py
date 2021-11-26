import os
os.system("color")
from timeit import default_timer as timer
from datetime import timedelta

COLOR = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "ENDC": "\033[0m",
}
print('------------------------------------')
print('   FIND the 1 character passcode   ')
print('------------------------------------')

# below are 2 lists - a simple one to start off with (a-z), then a more comprehensive one (a-z, A-Z, 0-9)
# just hashtag out the code you don't want below and in the exception at the end as well

#charlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
charlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
print(charlist)

name = input('player, what is your name? ')

code = input("player what is your secret code...shhhhh I won't tell? ")

start = timer()
if code not in charlist:
    end = timer()
    print("I could not find your password in my list")
    print(end - start)
else:
    end = timer()
    position = charlist.index(code)
    print("yes I found your password in the list")
    print("It is at location ", position)
    print("Remember locations start at 0 not 1...so 'a' will be at location 0 ")
    print('here is where I found your character in the list...')
    try:
        print(charlist[position-1],COLOR["RED"], charlist[position], COLOR["ENDC"], charlist[position+1])
    except IndexError:
        pass
        # choose one of the two below statements and hash out # the one you don't need

        # print("y, z, end of list")
        print("8,9,end of list")

    time_taken = timedelta(seconds=end-start)
    print("It took about ", time_taken,'microseconds to find your character')
