import sys
def evener(val):
    val = (val/2)%1
    return val



def Collatz(number):
    if evener(number) == 0:
        coll = number//2
        print(coll)
        return coll
    elif evener(number) == 0.5:
        coll = 3* number + 1
        print(coll)
        return coll
    else:
        print('Fuck!')
# while True:
#     print('Enter:')
#     ofo = int(input())
#     Collatz(ofo)


# while True:
#     print('Type in a number.')
#     try:
#         ipot = int(input())
#         while True:
#             Collatz(ipot)
#             ipot = Collatz(ipot)
#             if Collatz(ipot) == 1:
#                 sys.exit()
#     except ValueError:
#         print('You need to type an integer!.')
#         continue

while True:
    print('Type in a number.')
    try:
        ipot = int(input())
        while True:
            ipot = Collatz(ipot)
            if ipot == 1:
                break
    except ValueError:
        print('You need to type an integer!.')
        continue