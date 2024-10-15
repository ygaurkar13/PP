import random

def guess_the_number_and_win_the_prize():
    game_info = initialize()
    result = start_game(game_info)
    print(result)

def start_game(gsinfo):
    secret_number, rewards = gsinfo
    amount_user_want_to_bet = int(input("Enter the amount you want to bet (must be at least 5): "))
    
    if amount_user_want_to_bet < 5:
        return "Bet amount must be at least 5."
    
    previous_guess = None
    
    for attempt in range(1, 6):
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess == secret_number:
            reward = rewards[attempt - 1] if attempt <= len(rewards) else 0
            return f"Congratulations! You have guessed it correctly in {attempt} attempts. You win rupees {reward * amount_user_want_to_bet}!"
        
        
        if previous_guess is not None:
            difference = abs(secret_number - guess) / 100
            
            if difference > 0.8:
                print("Hint: Your guess is too far off!")
            elif guess < secret_number:
                if difference < 0.5:
                    print("Hint: You're getting closer, but it's still too small.")
                elif difference < 0.3:
                    print("Hint: You're very close, but still too small!")
                elif difference < 0.2:
                    print("Hint: Almost there! Just a bit larger.")
                else:
                    print("Hint: Your guess is too small.")
            else:  
                if difference < 0.5:
                    print("Hint: You're getting closer, but it's still too large.")
                elif difference < 0.3:
                    print("Hint: You're very close, but still too large!")
                elif difference < 0.2:
                    print("Hint: Almost there! Just a bit smaller.")
                else:
                    print("Hint: Your guess is too large.")
        
        previous_guess = guess
        print("Guess is incorrect!")
    
    return f"Sorry, you've used all attempts! The secret number was {secret_number}."

def initialize():
    secret_number = random.randint(1, 100)
    rewards = [5, 4, 3, 2, 1]  
    return secret_number, rewards

guess_the_number_and_win_the_prize()

