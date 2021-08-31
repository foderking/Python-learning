import random



dic = ("True: You told the truth.", "False: Liar! Liar! You told a lie")
while True:
    var = input("Type a statement that is either true or untrue: ")
    print(dic[random.randint(0,1)])