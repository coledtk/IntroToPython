# Import the random module. 
import random

# Print welcome message and slot machine graphics.

print("╔═══════╗")
print("║ 7 7 7 ║")
print("╚═══════╝")
print("Hello, welcome!")

# Define constants for maximum lines, maximum bet, minimum bet, rows, columns, symbol count, and symbol value.

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3
symbol_count = {
    "%": 2,
    "@": 4,
    "&": 6,
    "*": 8,
}

symbol_value = {
    "%": 5,
    "@": 4,
    "&": 3,
    "*": 2,
}

# Define a function `check_winnings` that calculates the winnings based on the symbols, lines, and bet.

def check_winnings(columns, lines, bet, values):
  winnings = 0
  winning_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break
    else:
      winnings += values[symbol] * bet
      winning_lines.append(line + 1)
  return winnings, winning_lines
      
# Define a function `get_slot_machine_spin` that generates a random spin of the slot machine.

def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)
      
  columns = []
  for _ in range(cols):
    column = []
    current_symbol = all_symbols[:]
    for _ in range(rows):
      value = random.choice(current_symbol)
      current_symbol.remove(value)
      column.append(value)
    columns.append(column)
  return columns

# Define a function `print_slot_machine` that prints the current state of the slot machine.

def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i !=len(columns) -1:
        print(column[row], end = " | ")
      else:
        print(column[row], end = "")
    print()

# Define a function `deposit` that asks the user for the amount they want to deposit and validates the input.

def deposit():
  while True:
      amount = input("How much would you like to deposit? $")
      if amount.isdigit():
          amount = int(amount)
          if amount > 0:
            break
          else:
            print("The amount must be greater thn 0!")
      else:
        print("Please enter a number.")
  return amount

# Define a function `get_number_of_lines` that asks the user for the number of lines they want to bet on and validates the input.

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
              break
            else:
              print("Enter a valid number of lines.")
        else:
          print("Please enter a number.")
    return lines

# Define a function `get_bet` that asks the user for the amount they want to bet and validates the input.

def get_bet():
  while True:
      amount = input("What would you like to bet? $")
      if amount.isdigit():
          amount = int(amount)
          if MIN_BET <= amount <= MAX_BET:
            break
          else:
            print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
      else:
        print("Please enter a number.")
  return amount

# Define a function `spin` that performs a spin of the slot machine, calculates the winnings, and updates the balance.

def spin(balance):
  lines = get_number_of_lines()
  while True:
    bet = get_bet()
    total = bet * lines

    if total > balance:
      print(f"You do not have enough to bet that, your current balance is: ${balance}")
    else:
      break

  print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total}")

  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
  print(f"You won {winnings}.")
  print("You won on lines:", *winning_lines)
  return winnings - total
  

# Define a function `main` that controls the main flow of the game.
  # Ask the user for their initial deposit.
  # Loop until the user decides to quit.
    # Print the current balance.
    # Ask the user if they want to play or quit.
    # If the user wants to play, perform a spin and update the balance.
  # Print the final balance.
def main():
  balance = deposit()
  while True:
    print(f"Current balance is: ${balance}")
    answer = input("Press enter to play (q to quit).")
    if answer == "q":
      break
    balance += spin(balance)
  print(f"You left with ${balance}")
      

# Call the `main` function to start the game.

main()
