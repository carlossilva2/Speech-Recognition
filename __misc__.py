#version 2.1

from appJar import gui;

app = gui();

def button(btn):
    return app.yesNoBox("Confirm Exit", "Do you want to continue to Speech?");
    app.setStopFunction(btn);

def commands():
    print('****************************************************************************');
    print('*                            SPEECH COMMANDS                               *');
    print('*                                                                          *');
    print('*         -> Say "Hey Speech" for Speech start listening                   *');
    print('*         -> "Hi" or "Hello"                                               *');
    print('*         -> "How Are You"                                                 *');
    print('*         -> "What\'s my Username"                                          *');
    print('*         -> "What Time is it"                                             *');
    print('*         -> "What Day is today"                                           *');
    print('*         -> "clear" Which clears all what was said before                 *');
    print('*         -> "open Facebook" or "open Twitter" or "open Developer"         *');
    print('*         -> "Play Music"/"Stop Music"/"Next Song"/"Previous Song"         *');
    print('*         -> "Music List" to show Music Tracks available                   *');
    print('*         -> "Repeat" Which repeats the last valid command                 *');
    print('*                                                                          *');
    print('****************************************************************************');
    input('Speech: Press ENTER to wake me up!');
    #Start User Interface
    
    #Add Fillings
    #app.setTitle("Speech");
    #app.setIcon("Media/Skull.ico");
    #app.setGeometry(700,600);
    #app.addLabel("title","Speech Recognition Test Commands");
    #app.setLabelBg("title","red");
    #app.addMessage("mess","""
    #****************************************************************************
      #                                   SPEECH COMMANDS                                         
                                                                                     
      #       -> "Hi" or "Hello"                                                  
      #       -> "How Are You"                                                   
       #      -> "What\'s my Username"                                          
        #     -> "What Time is it"                                             
         #    -> "What Day is today"                                           
          #   -> "clear" Which clears all what was said before             
           #  -> "open Facebook" or "open Twitter" or "open Developer" 
            # -> "Play Music"/"Stop Music"/"Next Song"/"Previous Song" 
     #        -> "Music List" to show Music Tracks available                   
      #       -> "Repeat" Which repeats the last valid command                 
                                                                              
    #****************************************************************************""");
    #app.addButton("Continue to app!", button);
    
    #Activate Interface
    #app.go();
