import socket
SERVERNAME = 'localhost'
PORT = 5000
while (True):
    #USING WITH, WE DON'T NEED TO CLOSE CONNECTION. IT WILL AUTO CLOSE CONNECTION WHEN USER INPUT QUIT IN PROMPT.
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try: 
            sendMessage = input("Enter message: (Enter 'quit' or 'QUIT' to disconnect from server: ")
            s.sendto(sendMessage.encode(), (SERVERNAME,PORT))
            serverResponse, serverAddress =s.recvfrom(1024)
            print(serverResponse.decode())
            #ADDING CONDITION TO DISCONNECT
            if ((sendMessage == 'quit') or (sendMessage == 'QUIT')):
                print ("Client has been disconnected")
                #BREAKING WHILE LOOP
                break
        #HANDLING ERROR IF USER PRESS CTRL+C
        except KeyboardInterrupt:
            print ("\n\nProgram terminated by user")
            break
