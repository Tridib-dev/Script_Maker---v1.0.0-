import datetime
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR,"messages.txt")
HEADER = f"\n\n{'<=: All of the messages :=>'.center(80)}\n{("\t"*6)+('='*48)}\n\n"    # for decoration

def reset_file():
    
    """
    Initializes or resets the message log file.

    If the file does not exist, it creates it.
    If the file exists, it clears all existing messages
    and writes the default header.
    """
    
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write(HEADER)
    else:
        with open(FILE_NAME, "w") as file:
            file.write(HEADER)
    
    
class Message:   
    """
    Represents a single chat message.

    Attributes:
        msg (str): Message content.
        time (str): Formatted timestamp.
        owner (str): Name of the sender.
    """
    
    def __init__(self,msg,time,owner):
        self.msg = msg
        self.time = time.strftime("\t\t%Y-%m-%d ==> [ %H:%M:%S ]")
        self.owner = owner
    
    def msg_show(self):
        return f"{self.owner} : {self.msg} \n\n{self.time} \n" + "-"*50 + "\n\n"

