class Character:
    def __init__(self, name, phrase1, phrase2, level):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = level

    def speak(self, phraseNum):
        if phraseNum == 1:
            return self.phrase1
        elif phraseNum == 2:
            return self.phrase2

    def setLevel(self, newLevel):
        self.level = newLevel

char1 = Character('Kung Fu Panda', 'Skadoosh', 'You have been blinded by pure awesomeness!', 1)
char2 = Character('Spiderman', 'My Spider-Sense is tingling', 'Your friendly neighbourhood spiderman', 1)

while True:
    print('Main Menu')
    print('1: Get character to say primary catchphrase')
    print('2: Make character become level 2')
    print('3: Get character to say secondary catchphrase')
    print('4: Exit')
    answer = int(input("Enter number choice here: "))
    if answer == 1:
        answer2 = int(input("Enter character number here: "))
        if answer2 == 1:
            print(char1.phrase1)
        elif answer2 == 2:
            print(char2.phrase1)
    elif answer == 2:
        answer2 = int(input("Enter character number here: "))
        if answer2 == 1:
            print('Character 1 current level: ' + str(char1.level))
            char1.setLevel(2)
            print('Character 1 current level: ' + str(char1.level))
        elif answer2 == 2:
            print('Character 2 current level: ' + str(char1.level))
            char1.setLevel(2)
            print('Character 2 current level: ' + str(char1.level))
    elif answer == 3:
        answer2 = int(input("Enter character number here: "))
        if answer2 == 1:
            print(char1.phrase2)
        elif answer2 == 2:
            print(char2.phrase2)
    else:
        exit()
