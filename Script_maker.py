import functions
import datetime
import decoration as deco



def main():
    
    """ 
    Using main function for the programme 
    This function initializes the message log file, prompts users for their names,
    and allows them to send messages to each other. It also provides options to view
    all messages or clear the message log.
    """
    

    # preparing the file 
    
    functions.reset_file()
    deco.print_welcome_message()
        
    # Users
    users = {}
    no_users = int(input("Enter number of users : "))
    if no_users <= 0:
        print("\n\nNo users\nProgramme ended !\n")
        return
    for i in range(1,no_users+1):
        users[str(i)] = input(f"Enter name of id~{i} user: ")

    # messaging function 

    deco.print_messaging_banner()
    print("You can start messaging now !...\n\n")
    
    running = True
    for i in users:
        print(f"[id : {i}] => [name : {users[i]}]\n","_"*30,"\n")
    

        
    while(running):
        user_id = input("Enter messager id : ")
        if user_id not in users.keys():
            print("Invalid user id !... Try again !...")
            continue
        u_name = (users[user_id].strip())
        u_name = u_name.capitalize()
        
        # Get user message and time
        u_msg = input("Enter your message : ")
        if not u_msg.strip():
            print("Message cannot be empty !... Try again !...")
            continue
        
        #creating message object and writing to file
        u_time = datetime.datetime.now()
        u = functions.Message(msg=u_msg,owner=u_name,time=u_time)
        u.msg_show()
        

        print("")
        
        # Asking for ending or continuing the conversation
        
        print("Message sent successfully !...\n")
        print("_"*50)       # for decoration
        E = input("press E to end this conersation or C to continue the conversation : ")
        if(E.lower() == 'e'):
            running = False
        
        elif(E.lower() == 'c'):
            continue
        
        else:
            print("Invalid input !... Try again !...")
            break
        print("_"*50)      # for decoration
    
    
    
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