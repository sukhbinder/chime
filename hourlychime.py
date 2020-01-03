from __future__ import print_function
import time
import argparse
import datetime

TEXT= {0:"Hourly", 15:"15 Mins", 30:"Half-Hourly"}
def play_beep():
    print ("\a \a")


def chime(mins):
    mins_in = [0]
    if mins == 30:
        mins_in = [0,30]
    elif mins == 15:
        mins_in = [0,15,30,45]
    print("{} Chimer on".format(TEXT[mins]))
    while True:
        try:
            now = datetime.datetime.now()
            if now.minute in mins_in:
                play_beep()
            time.sleep(60)
        except KeyboardInterrupt:
            print("Good bye!")
            break

def main():
    """
    Hourly chimer
    
    chime will do hourly chime
    chime 15 will do chime in 15 mins
    chime 30 will do chime in 30 mins
    """
    parser = argparse.ArgumentParser(description="Hourly Chimer")
    parser.add_argument("-m","--minutes", choices=[0,15,30] ,type=int, help="Time in seconds", default=0)
    args = parser.parse_args()
    chime(args.minutes)



if __name__ == "__main__":
    main()
