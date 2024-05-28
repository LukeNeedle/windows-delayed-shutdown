import subprocess
import time

def shutdown(totalSeconds):
    if totalSeconds > 0:
        hours, remainder = divmod(totalSeconds, 3600)
        mins, secs = divmod(remainder, 60)
        
        while totalSeconds > 0:
            print(f"{hours:02d}:{mins:02d}:{secs:02d}", end='\r')
            totalSeconds -= 1
            hours, remainder = divmod(totalSeconds, 3600)
            mins, secs = divmod(remainder, 60)
            time.sleep(1)
    subprocess.run(['shutdown', '/s'])

def getInput(prompt):
    while True:
        try:
            userInput = int(input(prompt))
            if userInput < 0:
                raise ValueError("Input must be greater than or equal to zero.")
            return userInput
        except ValueError as e:
            print(str(e) + ". Please enter a non-negative number.")

if __name__ == "__main__":
    try:
        hours = getInput("Enter the number of hours to wait before shutdown (0 or more): ")
        minutes = getInput("Enter the number of minutes to wait before shutdown (0 or more): ")
        seconds = getInput("Enter the number of seconds to wait before shutdown (0 or more): ")
        
        totalSeconds = (hours * 3600) + (minutes * 60) + seconds
        
        shutdown(totalSeconds)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
