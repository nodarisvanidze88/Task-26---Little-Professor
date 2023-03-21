import random                                                                                                           # import Random engine


def main():                                                                                                             # Run main function
    mode = level()                                                                                                      # get level
    score = 0                                                                                                           # initial score value
    counter = 0                                                                                                         # just counter
    for i in range(10):                                                                                                 # run main loop for 10 steps
        x, y = get_random_nums(mode)                                                                                    # get random integers
        z = x + y                                                                                                       # get results
        for k in range(3):                                                                                              # run another loop if something is wrong
            while True:
                try:                                                                                                    
                    res = int(input(f"{x} + {y} = "))                                                                   # get answer
                    break
                except:
                    print("Answer should be integer")                                                                   
            if res != z:                                                                                                # check answer is correct or not
                counter += 1                                                                                            # if answer is not correct count (limit of incorrect answer is 3)
            elif res == z:                                                                                              # if answer is correct
                score += 1                                                                                              # get score
                break
            if res != z and counter == 3:                                                                               # if 3 times is incorrect answer give correct answer
                print(f"{x} + {y} = {z}")                                                                               # print correct answer
    print(f"Score: {score}")                                                                                            # print last score


def level():                                                                                                            # function for level
    while True:
        try:
            user = int(input("Please add level from 1 to 3. Level: "))
            if 3 >= user > 0:
                return user
            else:
                print("Please Add level from 1 to 3")
        except:
            print("Please Add only integer")


def get_random_nums(lvl):
    if lvl == 1:
        return random.randint(1, 9), random.randint(1, 9)
    elif lvl == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:
        return random.randint(100, 999), random.randint(100, 999)


if __name__ == "__main__":
    main()
