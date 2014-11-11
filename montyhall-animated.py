#!/usr/bin/env python3
#
# A Monte Carlo simulation of the Monty Hall problem
# written in a language named after Monty Python
#
# Inspired by James Mays' Man Lab show. (?)
#
# 2014-10-29 Refactor outputs, decorate the graph a bit.
# 2014-10-28 Add animated graphical output!
#   Rethink of the MontyHall class to include the statistics
# streamlined, output documented 2014-03-23
# 2014-02-23
import sys
import random
import montyhall

game = montyhall.MontyHall()

#--------
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig = plt.figure('Monty Hall Statistics')
ax = fig.add_subplot(111)
#ax.axes.get_xaxis().set_visible(False)
ax.axes.get_xaxis().set_ticklabels(['','','', 'Original\nwins','', 'Switch\nwins'])

def animate(i):
    game.playgame()
    game.displayResult()
    game.displayStatistics()

    ax.bar(range(4), (1e-10, game.choiceWins, game.otherWins, 1e-10), width=0.8)
    return ax,

ani = animation.FuncAnimation(fig, animate)
plt.show()

print('\nFinal: %u games:'%game.nGames)
game.displayStatistics()
#--------
