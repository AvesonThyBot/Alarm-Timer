spacing = "------"
CLEAR = "\033[2J" #clears the terminal
CLEAR_RETURN = "\033[H" #clears the terminal and starts from same line
alarm_sound = "alarm.mp3" #global variable for sound

# -------------------- Importing modules --------------------
try:
    from time import sleep
    from playsound import playsound
except FileNotFoundError:
    print("Importion Error : Essential files not found.")
    print("Program shutting down.")
    sleep(1)
    exit()
except ModuleNotFoundError:
    print("Importion Error: Essential modules not found.")
    print("Program shutting down.")
    sleep(1)
    exit()
except Exception as e:
    print(f"An unknown error occurred: {str(e)}")
    print("Program shutting down.")
    sleep(1)
    exit()
# -------------------- End of Importing modules -------------

# -------------------- Main code ----------------------------

# time covert code
def total_time(seconds):
    minute = seconds // 60
    second = seconds % 60
    return f"{minute:02d}:{second:02d}"

# alarm code
def alarm(seconds,alarm_time):
    elapsed_time = 0
    print(CLEAR)
    while elapsed_time < seconds:
        sleep(1) #waits a second to make it a actual second
        elapsed_time += 1
        total_time = seconds - elapsed_time
        min_left = total_time // 60 #get minutes
        sec_left = total_time % 60 #get seconds
        print(f"{CLEAR_RETURN}Alarm is set to go off in {min_left:02d}:{sec_left:02d}")
    print(CLEAR)
    print(f"{CLEAR_RETURN}The total time of {alarm_time} is now over.")
    playsound(alarm_sound)
    # user returns to main.py 
        

# menu code
def menu():
    print(CLEAR)
    print(f"{spacing}\nMenu")
    while True:
        minutes = input(f"{spacing}\nHow many minutes do you want? (0-60).\n{spacing}\n")
        seconds = input(f"{spacing}\nHow many seconds do you want? (0-60).\n{spacing}\n")            
        try:
            minutes = int(minutes)
            seconds = int(seconds)
            if minutes == 0 and seconds == 0:
                print(f"{spacing}\nAlarm cannot be in 0 seconds.")
                continue
            elif (minutes == 0 and seconds > 0) or (minutes > 0 and seconds >= 0):
                total_seconds = (minutes * 60) + seconds
                if total_seconds > 3600:
                    print(f"{spacing}\nTime cannot exceed 60:00 (3600s).")
                    sleep(1.5)
                    menu()
                alarm_time = total_time(total_seconds)
                alarm(total_seconds,alarm_time)
                break
        except ValueError:
            print(f"{spacing}\nYou must enter an integer value from 0-60.")
        except Exception as e:
            print(f"An unknown error occurred: {str(e)}")
            print("Program shutting down.")
            sleep(1) #Slows down the program to give better UX
            exit()


menu()
# -------------------- End of Main code ---------------------
