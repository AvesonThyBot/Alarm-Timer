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

# alarm code
def alarm(seconds):
    time = "10:00"
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
    
    print(f"{CLEAR_RETURN}The total time of {time} is now over.")
    playsound(alarm_sound)
        
# menu code
def menu():
    pass


alarm(10)
# -------------------- End of Main code ---------------------
