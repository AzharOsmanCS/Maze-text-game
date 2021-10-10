
def choose(text,optionA,optionB,optionC):
    '''
    Purpose:
    Allows user to input text and 3 options and select an option which gets returned
    Parameter(s):
    text prompt, OptionA, OptionB, OptionC
    Return value:
    The inputed option returned as A, B, or C
    '''
    print(text)
    print("A." + optionA)
    print("B." + optionB)
    print("C." + optionC)
    options = ['A','B','C']
    choice = input("Choose A, B, or C: ")
    if choice in options:
        return choice
    else:
        print("Invalid option")
        return "C"

def adventure():
    '''
    Purpose:
    Play a maze adventure text game
    Parameter(s):
    None
    Return value:
    Winning or losing the escape game, Winning returns true losing returns false
    '''
    Part1 = choose("You are in a maze which way do you go","Forward", "Left", "Backwards")
    if Part1 == 'A':
        Part2 = choose("You continue down the maze", "Right", "Left", "Forward")
        if Part2 == "A" or Part2 == "C":
            Part3 = choose("You keep walking whats your next move", "Right", "Left", "Forward")
            if Part3 == "A":
                print("Wrong turn you roamed into the hedges and found yourself stuck in quicksand")
                return False
            if Part3 == "B":
                Part4 = choose("You turn left whats your next move", "Forward", "Right", "Left")
                if (Part4 == "A") or (Part4 == "C"):
                    print("You escaped")
                    return True
                if Part4 == "B":
                    print("Wrong turn you fell into a bottomless pit!")
                    return False
            if Part3 == "C":
                print("You escaped")
                return True
        if Part2 == "B":
            print("You escaped")
            return True
    if Part1 == 'B':
        Part4 = choose("You turn left whats your next move", "Forward", "Right", "Left")
        if (Part4 == "A") or (Part4 == "C"):
            print("You escaped")
            return True
        if Part4 == "B":
            print("Wrong turn! You turned into a trap and and fell victim to a swinging axe!")
            return False
    if Part1 == "C":
        print("Wrong turn you entered an empty void in space and time")
        return False
