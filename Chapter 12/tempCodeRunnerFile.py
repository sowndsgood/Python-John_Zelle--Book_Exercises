class Dice:

    def __init__(self):
        '''5 Dices with value 0'''
        self.dices = [0] * 5
        self.rollAll()

    def roll(self, dice_list):
        '''Rolls specific dice'''
        for dice in dice_list:
            self.dices[dice] = randrange(1,7)

    def rollAll(self):
        '''Rolls all dices'''
        self.roll(range(5))

    def values(self):
        '''Returns the dice values'''
        return self.dices[:]

    def score(self):
        '''Calculates the dice score'''

        counts = [0] * 7

        for value in counts:
            counts[value] = counts[value] + 1

        if 5 in counts:
            return "Five of a Kind", 30
        elif 4 in counts:
            return "Four of a Kind", 15
        elif (3 in counts) and (2 in counts):
            return "Full house", 12
        elif 3 in counts:
            return "Three of a Kind", 8
        elif not (2 in counts) and (counts[1] == 0 or counts[6]==0):
            return "Straight", 20
        elif counts.count(2) == 2:
            return "Two Pair", 5
        else:
            return "Garbage", 0

class PokerApp:

    def __init__(self, interface):
        '''Creates a poker app'''
        self.dice = Dice()
        self.money = 100
        self.interface = interface    

    def play(self):
        '''Plays the poker game'''
        while self.money >= 10 and self.interface.wantToPlay():
            self.playRound()
        self.interface.close()

    def playRound(self):
        '''Play one round'''
        self.money -= 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money += score
        self.interface.setMoney(self.money)

    def doRolls(self):
        '''Do the rolls'''
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll += 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()

class GraphicalInterface:

    def __init__(self):
        '''Creates a graphical window'''
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green") 
        banner = Text(Point(300, 30), "Python Poker Parlor") 
        banner.setSize(24) 
        banner.setFill("yellow")
        banner.setStyle("bold") 
        banner.draw(self.win) 
        self.msg = Text(Point(300, 380), "Welcome to the Dice Table") 
        self.msg.setSize(18) 
        self.msg.draw(self.win) 
        self.createDice(Point(300, 100), 75) 
        self.buttons = [] 
        self.addDiceButtons(Point(300, 170), 75, 40) 
        b = Button(self.win, Point(300, 230), 400, 30, "Roll Dice") 
        self.buttons.append(b) 
        b = Button(self.win, Point(300, 280), 150, 40 , "Score" ) 
        self.buttons.append(b) 
        b = Button(self.win, Point(570 ,375), 40 , 30 , "Quit" ) 
        self.buttons.append(b) 
        self.money = Text(Point(300 ,325 ) ,"$100") 
        self.money.setSize(18) 
        self.money.draw(self.win)
        #help button
        help = Button(self.win, Point(70, 375), 40, 30, "Help")
        self.buttons.append(help)       

    def choose(self , choices):
        buttons = self.buttons
        # activate choice buttons , deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()
    
    def createDice(self , center, size): 
        center.move(-3* size, 0) 
        self.dice = [] 
        for i in range (5): 
            view = DieView(self.win, center, size) 
            self.dice.append(view) 
            center.move(1.5* size, 0) 

    def addDiceButtons (self , center , width, height ): 
        center.move(-3*width, 0) 
        for i in range ( 1 ,6 ): 
            label = "Die {0}".format (i) 
            b = Button(self.win, center , width, height , label) 
            self.buttons.append(b) 
            center.move(1.5*width, 0)

    def setMoney(self ,amt):
        self.money.setText("${0}".format(amt))
    
    def showResult(self, msg, score):
        if score > 0:
            text = "{0}! You win ${1}".format(msg , score)
        else:
            text = "You rolled {O}".format(msg)
            self.msg.setText(text)

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])
  
    def wantToPlay(self):
        ans = ""
        while ans != "Quit":
            ans = self.choose(["Roll Dice", "Quit", "Help"])
            self.msg.setText("")
            if ans == "Help":
                self.getHelp()
            else:
                return ans == "Roll Dice"

    def chooseDice(self):
        #choices is a list of the indexes of the selected dice
        choices = []
        # No dice chosen yet
        while True:
        # wait for user to click a valid butt on
            b = self.choose(["Die 1" , "Die 2" , "Die 3" , "Die 4" , "Die 5" ,"Roll Dice" , " Score"] )
            # User clicked a die button
            if b[0] == "D":
                i = int (b[4]) - 1
                if i in choices:
                    # Translate label to die index
                    # Currently selected , unselect it
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:
            # User clicked Roll or Score
                for d in self.dice:
                    # Revert appearance of all dice
                    d.setColor("black")
                if b == " Score":
                # Score clicked , ignore choices
                    return []
                elif choices != [] :
                    return choices
                
    def getHelp(self):
        win2 = GraphWin("Help Window", 800, 400)

        help = 'This game of dice poker allows the user to roll for hands "(5-3)-of-a-kind",\
        \n"Full House", "Straight", etc. Each round consists of up to three rolls. the user\n \
        will select the appropriate dice to re-roll. If no dice are chosen, the user will be scored\
        \n based on the initial roll.\n'
        payouts = "{0:<100}{1:>0}\n---------------------------------------\
        -------------------------------------\n".format("Hands", "Pay")
        hand_specs = [("Two Pairs", 5), ("Three of a Kind", 8), ("Full House", 12), ("Four of a Kind", 15), ("Straight (1-5 or 2-6)", 20), ("Five of a Kind", 30)]
        for (hand, pay) in hand_specs:
            payouts = payouts + '{0:<100} ${1:>0.2f}\n'.format(hand, pay)
        msg = Text(Point(400, 100), help)
        msg.setSize(14)
        msg2 = Text(Point(300, 300), payouts)
        msg.draw(win2)
        msg2.draw(win2) 
        win2.getMouse()
        win2.close()
                
    def close(self):
        self.win.close()

def poker():
    
    win = GraphWin("PokerGame", 600, 600)
    win.setBackground("yellow")
    text1 = Text(Point(300, 200), "Welcome to Poker game.")
    text2=Text(Point(300, 300),"\n \n Click Let's Play button to play the game. \n \n Click Quit button to exit from the game.")
    text1.setSize(32)
    text1.draw(win)
    text2.setSize(17)
    text2.draw(win)

    b1 = Button(win, Point(200, 500), 100, 30, "Ready") 
    b1.activate()

    b2 = Button(win, Point(400, 500), 100, 30, "Quit") #Quit button
    b2.activate()

    while True:

        pt = win.getMouse()

        if b1.clicked(pt):
            win.close()
            inter = GraphicalInterface()
            app = PokerApp(inter)
            app.play()
            break
        elif b2.clicked(pt):
            win.close()

    win.close()

if __name__ == "__main__":
    poker()
        


    