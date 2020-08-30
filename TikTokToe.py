import random as rnd
class InitilizeBoard:
    def __init__(self):
        self.boardvalues=[0,0,0,0,0,0,0,0,0]
    def printBoard(self):
        print('{}|{}|{}'.format(self.boardvalues[0],self.boardvalues[1],self.boardvalues[2]))
        print('_|_|_')
        print('{}|{}|{}'.format(self.boardvalues[3],self.boardvalues[4],self.boardvalues[5]))
        print('_|_|_')
        print('{}|{}|{}'.format(self.boardvalues[6],self.boardvalues[7],self.boardvalues[8]))
        print(' | | ')

    def playerchoice(self):
        values=['O','X']
        player1choice=rnd.random(values)


obj=InitilizeBoard()

obj.printBoard()