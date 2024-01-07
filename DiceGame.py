import random


class Die:

    def __init__(self) -> None:
        self._value = None
    
    @property
    def value(self):
        return self._value
     
    def roll(self):
        new_value = random.randint(1,6)
        self._value = new_value
        return new_value
    

class Player:

    def __init__(self, die, is_computer=False) -> None:
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def die(self):
        return self._die
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter +=1
    
    def decrement_counter(self):
        self._counter -=1
    
    def roll_die(self):
        return self._die.roll()

class DiceGame:
    def __init__(self, player, computer) -> None:
        self._player = player
        self._computer = computer

    def play(self):
        print("=============================")
        print("🎲 Welcome to Roll the Dice!")
        print("=============================")
        while True:
            self.play_around()
            #Todo: implement game over.
            game_over = self.check_game_over()
            if game_over:
                break

    def play_around(self):
        #Welcome the user 
        self.print_round_welcome()

        
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()
        self.show_dice(player_value, computer_value )
        self.show_counters()

        #Determine winner and loser
        if player_value > computer_value:
            print ("You won ")
            self.update_counters(self._player, self._computer)
        elif computer_value > player_value:
            print("The computer won")
            self.update_counters(self._computer, self._player)
        else:
            print("It's a tie")
        
    def print_round_welcome(self):
        print("New Round")
        input("Press any key to roll the dice!")

    def show_dice(self, player_value, computer_value ):
        print(f"Your die: {player_value}")
        print(f"Computer die: {computer_value}")
    
    def update_counters(self, winner, loser):
        # if (winner.counter < 10):
        #     winner.increment_counter()
        loser.decrement_counter()
    
    def show_counters(self):
        print(f"Your counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")
    
    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(winner=self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(winner=self._computer)
            return True
        else:
            return False
    
    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n=======================")
            print(" G A M E   O V E R ✨")
            print("=======================")
            print("The computer won the game. Sorry...")
            print("=================================")
        else:
            print("\n=====================")
            print(" G A M E   O V E R ✨")
            print("=====================")
            print("You won the game! Congratulations")
            print("=================================")


        

player_die = Die()
computer_die = Die()
my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)
game = DiceGame(my_player,computer_player)
game.play()


    
    

    


    
