spacing = "------"
CLEAR = "\033[2J" #clears the terminal
CLEAR_RETURN = "\033[H" #clears the terminal and starts from same line

# -------------------- Importing modules --------------------
try:
    from time import sleep
    from playsound import playsound
except FileNotFoundError:
    print(CLEAR)
    print("Importion Error : Essential files not found.")
    print("Program shutting down.")
    sleep(1) #Slows down the program to give better UX
    exit()
except ModuleNotFoundError:
    print(CLEAR)
    print("Importion Error: Essential modules not found.")
    print("Program shutting down.")
    sleep(1) #Slows down the program to give better UX
    exit()
except Exception as e:
    print(CLEAR)
    print(f"An unknown error occurred: {str(e)}")
    print("Program shutting down.")
    sleep(1) #Slows down the program to give better UX
    exit()
# -------------------- End of Importing modules -------------

# -------------------- Main code ----------------------------
# return menu code
def return_menu():
    while True:
        choice = input(f"{spacing}\nDo you want to go back to menu? (Yes or No): \n{spacing}\n")
        try:
            choice = str(choice)
            if choice.lower().strip() in ["yes","ye","yea","y"]:
                main_menu()
            elif choice.lower().strip() in ["no","nah","n"]:
                print("Exiting...")
                sleep(1) #Slows down the program to give better UX 
                exit()
            else:
                print("Enter either 'Yes' or 'No'.")
        except ValueError:
            print("Enter either 'Yes' or 'No'.")
            continue
        except Exception:
            print("There has been an unexpected error. Try again")

# main menu code
def main_menu():
    print(CLEAR)
    print(f"{spacing}\nMain Menu\n{spacing}")
    while True:
        choice = input(f"Pick a option: \n{spacing}\
        \n1) Alarm Clock\
        \n2) Timer\n{spacing}\n")
        try:
            choice = int(choice)
            if choice == 1:
                import alarm
                sleep(1) #Slows down the program to give better UX 
                return_menu()
            elif choice == 2:
                import timer
                sleep(1) #Slows down the program to give better UX 
                return_menu()
            else:
                print(f"{spacing}\nInvalid choice. Please enter 1 or 2.\n{spacing}")
        except ValueError:
            print(f"{spacing}\nYou must enter an integer value of 1 or 2.\n{spacing}")
        except Exception as e:
            print(f"An unknown error occurred: {str(e)}")
            print("Program shutting down.")
            sleep(1) #Slows down the program to give better UX
            exit()

main_menu()


# -------------------- End of Main code ---------------------