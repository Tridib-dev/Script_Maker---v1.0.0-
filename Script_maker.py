import functions
import datetime



def main():
    
    """ 
    Using main function for the programme 
    This function initializes the message log file, prompts users for their names,
    and allows them to send messages to each other. It also provides options to view
    all messages or clear the message log.
    """
    

    # preparing the file 
    functions.reset_file()
    print("\n\n\t\t\t\t\t\t<=: WELCOME TO MESSAGE LOG :=>\n\t\t\t\t\t_____________________________________________\n\n")
    
    # Users
    names = {
        "1" : input("Enter first users name : "),
        "2" : input("Enter second users name : ")
    }

    # messaging function 

    print(f"\n\n\t\t\t\t\t<=: Welcome {names['1']} and {names['2']} to the messaging world :=>\n\t\t\t\t   ________________________________________________________\n")
    print("You can start messaging now !...\n\n")
    
    running = True
    
    while(running):
        u_name = input(f"Enter your name 1 for {names['1']} and 2 for {names['2']} : ")
        if u_name == '1':
            u_name = names['1']
        elif u_name == '2':
            u_name = names['2']
        else:
            print("Invalid input !... Try again !...")
            continue
        
        # Get user message and time
        u_msg = input("Enter your message : ")
        if not u_msg.strip():
            print("Message cannot be empty !... Try again !...")
            continue
        
        #creating message object and writing to file
        u_time = datetime.datetime.now()
        u = functions.Message(msg=u_msg,owner=u_name,time=u_time,)
        with open(functions.FILE_NAME,"a")as File:
            File.write(u.msg_show())

        print("")
        
        # Asking for ending or continuing the conversation
        
        print("Message sent successfully !...\n")
        print("-"*50)
        E = input("press E to end this conersation or C to continue the conversation : ")
        if(E.lower() == 'e'):
            running = False
        
        elif(E.lower() == 'c'):
            continue
        
        else:
            print("Invalid input !... Try again !...")
            break
        
    
    
    
    # Show all messages   

    p = input("press A to show all the messages : ")
    if p.lower() == 'a':
        with open(functions.FILE_NAME,"r")as FILE:
            print(FILE.read())
            print("\n\n")

    # Clear all messages

    h = input("press H to clear all the messages : ")
    if h.lower() == 'h':
        functions.reset_file()
        print("All messages cleared !...")



if __name__ == '__main__':
    main()


# End of the programme 