import random

def start_game():
    print("--- 3 લાઇવ વાળી નંબર ગેસિંગ ગેમ! ---")
    secret_number = random.randint(1, 20)
    lives = 3
    score = 0
    
    while lives > 0:
        print(f"\nતમારી પાસે {lives} લાઇવ બાકી છે. વર્તમાન સ્કોર: {score}")
        try:
            guess = int(input("1 થી 20 ની વચ્ચે નંબર ગેસ કરો: "))
            
            if guess == secret_number:
                score += 10
                print(f"અભિનંદન! તમે સાચો નંબર પકડ્યો! તમારો સ્કોર: {score}")
                # નવી ગેમ માટે નવો નંબર
                secret_number = random.randint(1, 20)
            else:
                lives -= 1
                print("ખોટો નંબર!")
                if lives > 0:
                    print(f"ફરી પ્રયત્ન કરો. (સાચો નંબર {secret_number} હતો, નવો નંબર આપ્યો છે)")
                    secret_number = random.randint(1, 20)
        
        except ValueError:
            print("કૃપા કરીને ફક્ત આંકડા જ લખો!")
            
    print(f"\nગેમ ઓવર! તમારો ફાઈનલ સ્કોર: {score}")

start_game()
