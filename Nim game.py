print("Welcome to Nim Game !\n   In this game, you can play against CPU or another player.\n   In your turn you can take 1 or more sticks from a single row.")
print("Let's get started!")

import random # Importing the random module for CPU's Turn
import time   # To add a short delay to demonstarte that CPU is thinking

# Function to print the current state of the game
def print_rows(rows):
    max_len = max(rows)
    for i, row in enumerate(rows):
        print(f"{i+1}. {' ' * (max_len - row)}{' |' * row}")

# Function to print the move made by the current player
def print_move(current_player, row, stick_quantity):
    print(f"{current_player} takes {stick_quantity} stick{'s' if stick_quantity > 1 else ''} from row {row+1}.")

# Main function to play the game
def nim_game():
    # Main game loop
    while True:
        
        rows = [1, 3, 5, 7]
        player_name = input("Enter your name: ")
        
        # Ask the user to select the opponent 
        while True:
            opponent = input("Who would you like to play against? Enter 'CPU' for computer or 'player' for another player: ")
            if opponent.lower() in ['cpu', 'player']:
                break
            else:
                print("Invalid choice. Please enter 'CPU' or 'player'.")
        
        if opponent.lower() == 'player':
            player2_name = input("Enter the second player's name: ")
        else:
            player2_name = 'CPU'
        current_player = random.choice([player_name, player2_name])
        print(f"Game is starting. {current_player} will be going first!")
        print("Generating sticks, get ready!")
        print_rows(rows)
        
        # Initialize win and loss counts
        win_count = {player_name: 0, player2_name: 0}
        loss_count = {player_name: 0, player2_name: 0}

        # Ask the user to select the game rule 
        while True:
            game_rule = input("Choose the game rule. Enter 'win' if the last stick picked is a win, or 'loss' if the last stick picked is a loss: ")
            if game_rule.lower() in ['win', 'loss']:
                break
            else:
                print("Invalid game rule. Please enter 'win' or 'loss'.")
        
        # Loop until all sticks are taken
        while sum(rows) > 0:
            # If it's the user's turn
            if current_player == player_name or (opponent.lower() == 'player' and current_player == player2_name):
                while True:
                    try:
                        row_num, num_sticks = map(int,input(f"{current_player},which row and how many sticks would you like to take? (format: row, sticks) ").split(','))
                        row_num -= 1
                        if row_num < 0 or row_num > 3 or num_sticks < 1 or num_sticks > rows[row_num]:
                            print("Invalid choice. Please try again.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter two numbers separated by a comma.")
            # If it's the CPU's turn
            else:
                print('CPU is thinking..........')
                time.sleep(1.5)  
                while True:
                    row_num = random.randint(0, 3)
                    if rows[row_num] > 0:
                        break
                num_sticks = random.randint(1, rows[row_num])
        
            # Substracting the number of sticks taken from the chosen row
            rows[row_num] -= num_sticks
            print_move(current_player, row_num, num_sticks)
            # print the current state of the game
            print_rows(rows)
        
            # Check if the game is over
            if sum(rows) == 0:
                if game_rule.lower() == 'win':
                    print(f"Game Over! {current_player} took the last stick. {current_player} wins!")
                    win_count[current_player] += 1
                    loss_count[player2_name if current_player == player_name else player_name] += 1
                else:
                    print(f"Game Over! {current_player} took the last stick. {current_player} loses!")
                    loss_count[current_player] += 1
                    win_count[player2_name if current_player == player_name else player_name] += 1
                break
        
            # Switch to the other player
            current_player = player2_name if current_player == player_name else player_name
    
        # Print the win and loss counts
        print(f"Win count: {win_count}")
        print(f"Loss count: {loss_count}")

        # Ask if the user wants to play again
        while True:
            play_again = input("Would you like to play again? (yes/no) ")
            if play_again.lower() in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        if play_again.lower() != 'yes':
            break

nim_game()
