import random

MAX_LINES= 3
MAX_BET= 100
MIN_BET= 1

ROWS = 3
COLS = 3

symbol_count= {
    "A": 2,
    "B": 4,
    "C": 6, 
    "D": 8
}

symbol_value= {
    "A": 5,
    "B": 4,
    "C": 3, 
    "D": 2
}
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

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols= []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns= []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range (rows):
            value= random.choice(current_symbols)
            column.append(value)
            current_symbols.remove(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])): 
        for i, col in enumerate(columns):
            if i != len(columns[0]) - 1:
                print(col[row], end= " | ")
            else:
                print(col[row], end= "")
        print()
    
def deposit(str):
    while True:
        amount = input(str)
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Invalid amount of deposit")
        else: 
            print("Please enter a valid amount of deposit")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to be on (1-" + str(MAX_LINES) + "):")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print("Invalid amount of lines")
        else: 
            print("Please enter a valid number of lines")
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET :
                    break
            else:
                print(f"Invalid amount of bet between {MIN_BET} - {MAX_BET}")
        else: 
            print("Please enter a valid amount of bet")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    bet= get_bet()
    total_bet= bet * lines
    while balance < total_bet:
        option = input(f"Insufficient balance of ${balance}.\n Press [1] to add more deposit \n Press [2] to change the bet and lines \n Select option: ")
        if option.isdigit():
            option = int(option)
            if option == 1:
                addDeposit= deposit(f"The current balance of ${balance} is insufficient compared to your bet of ${total_bet}. Please add additional deposit of ${total_bet - balance}: $")
                balance += addDeposit
            elif option == 2:
                new_bet= get_bet()
                bet = new_bet
                new_lines= get_number_of_lines()
                lines= new_lines
                total_bet= new_bet*new_lines
    
    print(f"Current balance: ${balance}.\nYou are betting ${bet} on {lines} lines with the total bet of ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance= deposit("What would you like to deposit: $")
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()