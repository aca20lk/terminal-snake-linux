import os
import time
from pynput import keyboard


class Game:

    def onPress(self, key):
        try:
            k=key.char
        except:
            k=key.name
        if k in ['w', 'a', 's', 'd']:
            if k == 'w':
                self.direction = 'UP'
            if k == 'a':
                self.direction = 'LEFT'
            if k == 's':
                self.direction = 'DOWN'
            if k == 'd':
                self.direction = 'RIGHT'

    def startListner(self):
        self.listener = keyboard.Listener(self.onPress)
        self.listener.start() 
        #self.listener.join()

    def __init__(self, width, height):
        self.field_width = width
        self.field_height = height

        self.head_x = int(self.field_width / 2)
        self.head_y = int(self.field_height / 2)

        self.direction = 'NONE'

        self.isNotDed = True
        
        self.startListner()
        
    def clearScreen(self):
        os.system("clear")    

    def drawField(self):
        self.clearScreen()
        for y in range(0, self.field_height):
            for x in range(0, self.field_width):
                if y == 0 or y == self.field_height-1 or x == 0 or x == self.field_width-1:
                    print("#", end = "")
                elif y == self.head_y and x == self.head_x:
                    print("O", end = "")
                else:
                    print(" ", end = "")
            print()

    def isHeadInWall(self):
        return self.head_x == 0 or self.head_x == self.field_width - 1 or self.head_y == 0 or self.head_y == self.field_height - 1
    
    def update(self):
        if self.direction == 'UP':
            self.head_y -= 1
        if self.direction == 'DOWN':
            self.head_y += 1
        if self.direction == 'LEFT':
            self.head_x -= 1
        if self.direction == 'RIGHT':
            self.head_x += 1
        
        if self.isHeadInWall():
            self.isNotDed = False

    
    def playGame(self):
        while self.isNotDed:
            self.drawField()
            time.sleep(0.2)
            self.update()
        print("GAME OVER")

def main():
    game = Game(51, 23)
    game.playGame()

if __name__ == "__main__":
    main()
