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

print("Alarm")

# -------------------- End of Main code ---------------------
