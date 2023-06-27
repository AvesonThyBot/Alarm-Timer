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
    sleep(1)
    exit()
except ModuleNotFoundError:
    print(CLEAR)
    print("Importion Error: Essential modules not found.")
    print("Program shutting down.")
    sleep(1)
    exit()
except Exception as e:
    print(CLEAR)
    print(f"An unknown error occurred: {str(e)}")
    print("Program shutting down.")
    sleep(1)
    exit()
# -------------------- End of Importing modules -------------

# -------------------- Main code ----------------------------

# Main Menu code
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
                break
            elif choice == 2:
                import timer
                break
            else:
                print(f"{spacing}\nInvalid choice. Please enter 1 or 2.\n{spacing}")
        except ValueError:
            print(f"{spacing}\nYou must enter an integer value of 1 or 2.\n{spacing}")
        except Exception as e:
            print(f"An unknown error occurred: {str(e)}")
            print("Program shutting down.")
            sleep(1)
            exit()
    
                
            




main_menu()


# -------------------- End of Main code ---------------------