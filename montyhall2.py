#!/usr/bin/env python
#
# A Monte Carlo simulation of the Monty Hall problem
# written in a language named after Monty Python
#
# Inspired by James Mays' Man Lab show. (?)
#
# 2014-10-28 Add graphical output!
# streamlined, output documented 2014-03-23
# 2014-02-23
import sys
import random

class MontyHall:
    def __init__(self):
        self.nGames, self.choiceWins, self.otherWins = 0, 0, 0
    #----
    def playgame(self):
        self.nGames += 1
        self.doors = {1:'loser',2:'loser',3:'loser'}
        self.winner = random.randint(1,3)
        self.doors[self.winner] = 'Winner'

        self.choice = random.randint(1,3)
        self.showbad()
        self.notchosen()
        if self.choice == self.winner:
            self.choiceWins += 1
        elif self.other == self.winner:
            self.otherWins += 1
        else:   # This should never happen.
            print>>sys.stderr, 'Error!', self.shown, self.doors[self.shown]
    #----
    def showbad(self):
        self.shown = random.sample({1,2,3} - {self.choice, self.winner}, 1)[0]
    #----
    def notchosen(self):
        choices = {1,2,3} - {self.shown, self.choice}
        self.other = choices.pop()
        if len(choices):
            print>>sys.stderr, 'OOPS! ', choices
    #----

    def displayResult(self):
        print "game: %2u:"%self.nGames,
        print "Choice: %u;"%(self.choice),
        print "Shown: %u is a %s"%(self.shown, self.doors[self.shown]),
        print "Other: %u is a %s"%(self.other, self.doors[self.other]),
        if self.choice == self.winner:
            print "Original choice is a %s!"%(self.doors[self.choice])
        else:
            print "Switch would win."
    #----

    def displayStatistics(self):
        print 'First Choice wins: %u (%.3f%%)' %(self.choiceWins, 100.0*self.choiceWins/self.nGames)
        print '       Other wins: %u (%.3f%%)' %(self.otherWins, 100.0*self.otherWins/self.nGames)
    #----
#--------

def main(args=[__name__]):
    game = MontyHall()

    total = int(input('Play how many games? '))
    for i in range(total):
        game.playgame()
        game.displayResult()

    game.displayStatistics()

    #--------
    # Let's show the results graphically:
    import matplotlib.pyplot as plt
    fig = plt.figure()
    fig.canvas.set_window_title('Monty Hall Results')
    ax = plt.subplot(111)
    ax.axes.get_xaxis().set_ticklabels(['','','', 'Original\nwins','', 'Switch\nwins'])
    ax.bar(range(4), (1e-10, game.choiceWins,game.otherWins, 1e-10), width=0.8)
    plt.show()
#--------

if __name__ == '__main__':
    sys.exit(main(sys.argv))
