#!/usr/bin/env python3
#
# A Monte Carlo simulation of the Monty Hall problem
# written in a language named after Monty Python
#
# Inspired by James Mays' Man Lab show. (?)
#
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

def animate(i):
    game.playgame()
    game.displayResult()
    game.displayStatistics()

    ax.bar(range(4), (1e-10, game.choiceWins, game.otherWins, 1e-10), width=0.8)
    return ax,

anim = animation.FuncAnimation(fig, animate,
                               frames=200, interval=20)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('MontyMonteMonty.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#ani = animation.FuncAnimation(fig, animate)
plt.show()

print('\nFinal: %u games:'%game.nGames)
game.displayStatistics()
#--------
