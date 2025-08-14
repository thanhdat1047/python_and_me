def number_guessing_game():
    import random
    print("\n --- NUMBER GUESSING GAME")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attemps = 7
    
    while attempts < max_attemps:
        try:
            guess = int(input(f"Lan doan {attempts + 1}/{max_attemps}:"))
            attempts += 1
            
            if guess == secret_number:
                print(f"Binggo {secret_number} in {attempts} times!")
                return
            elif guess < secret_number:
                print("Greater than")
            else:
                print("Less than")
        except ValueError:
            print("Vui lòng nhập một số nguyên!")
            attempts -= 1 
    
    print(f"Game over: {secret_number}")

number_guessing_game()