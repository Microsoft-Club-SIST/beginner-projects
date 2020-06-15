# Jonin Projects

import pygame
from pygame.locals import *
import sys
import time
import random

# Functions responsible for starting, reset and other helper functions for our project.
class Game:
    
    # The constructor for our class where we declare all the variables.
    def __init__(self):
        
        self.w = 750 # Width of the window
        self.h = 500 # Height of the window
        self.reset = True # For reseting the operations Boolean value
        self.active = False  # Boolean value for Game activity
        self.input_text = '' # For inputting the Test Sentences
        self.word = '' # The words from each sentences 
        self.time_start = 0 # The starting time for the  game counter
        self.total_time = 0 # The total time recorded counter
        self.accuracy = '0%' # The accuracy of our typig speed
        self.results = 'Time:0 Accuracy:0 % Wpm:0 ' # The final result of our typing game
        self.wpm = 0 # Words Per Minute counter
        self.end = False # End of the game boolean variable
        self.HEAD_C = (255,213,50) # RGB values for HEAD using Tuple_RGB_Encoding
        self.TEXT_C = (255,255,255) # RGB values for TEXT using Tuple_RGB_Encoding
        self.RESULT_C = (222,29,31) # RGB values for RESULT using Tuple_RGB_Encoding
        
        pygame.init() # initialise all importe pygame modules
        self.open_img = pygame.image.load('type-speed-open.png') #  Using pygame to load the image into the opening screen
        self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h)) # We fit the values inititialised for our app.window to image we display when starting the game using pygame.transform.scale
        self.bg = pygame.image.load('background.jpg') 
        self.bg = pygame.transform.scale(self.bg,(self.w,self.h)) # We do the same as we did for open_img for the background with it's required dimenions
        self.screen = pygame.display.set_mode((self.w, self.h)) # Using this method we assign the size for our pygame window
        pygame.display.set_caption('Typing Speed Test for the Cliqqies!') # We provide the Title for our game
        
    # Helper Function that will draw the text on the screen
    def draw_text(self, screen, msg, y, fsize, color): 
        font = pygame.font.Font('redline.ttf', fsize) 
        text = font.render(msg, 1,color) # Creates a suface with the msg rendered on it
        text_rect = text.get_rect(center=(self.w/2, y)) # .get_rect is for  the shape of a rectangle text surface object
        screen.blit(text, text_rect) # .blit is  used for renderring objects to our  pygame screen
        pygame.display.update() # We update our screen with the above objects
    
    # This will open up our sentences.txt file and return a random sentence from the list
    def get_sentence(self):
        f = open('sentences.txt').read()
        sentences = f.split('\n') # Split the string with a new line character
        sentence = random.choice(sentences) # Choosing a random sentence
        return sentence
    
    def show_results(self, screen):
        if(not self.end):
            # Calculating Time 
            self.total_time = time.time() - self.time_start
            
            # Calculating Accuracy
            count = 0 # Initialising the counter for correct typed characters to 0
            for i,c in enumerate(self.word): 
                try:
                    if self.input_text[i] == c: # We compare input_text characters ( i is the index for display text ) with the displayed_text (c)
                        count += 1 # And we increment the counter by 1
                except:
                    pass
            self.accuracy = (count/len(self.word))*100 # Accuracy = (Total no. of correct character/total length of the word)*100 in percentage 
            
            # Calculate WPM ( Words Per Minute )
            self.wpm = len(self.input_text)*60/(5*self.total_time) # WPM = (total no. of i/p characters//5)/(total time taken//60) [ We consider a typical word to have 5 characters and take time in seconds ] 
            self.end = True
            print(self.total_time)

            self.results = 'Time:'+str(round(self.total_time)) +" secs Accuracy:"+ str(round(self.accuracy)) + "%" + ' Wpm: ' + str(round(self.wpm)) # We assign a new variable self.results for printing our results

            
            # Draw Icon Image onto the reset button
            self.time_img = pygame.image.load('icon.png')
            self.time_img = pygame.transform.scale(self.time_img,(150,150))
            # screen.blit(self.time_img,(80,320))
            screen.blit(self.time_img, (self.w/2-75, self.h-140)) 
            self.draw_text(screen, "Reset", self.h-70, 26, (100,100,100))
            
            print(self.results)
            pygame.display.update()
        
    
    def run(self):
         self.reset_game() # We first reset the variables for our game
            
         self.running=True # Then we start the game
         while (self.running): # Infinite loop for keeping the window running ( Methods for detecting the mouse and keyboard + layouts ?)
                clock = pygame.time.Clock() # We now create a clock object .Clock() method of pygame
                self.screen.fill((0,0,0),(50,250,650,50)) # First attribute being the color and second being the rectangles dimensions
                pygame.draw.rect(self.screen, self.HEAD_C,(50,250,650,50),2) # Args -> (Surface, Color, Rect, Width) in order
                # Update the text of user input
                self.draw_text(self.screen, self.input_text, 274, 18,(250,250,250))  
                pygame.display.update()
                
                # Now we assign a for loop for the events of closing and running operations of the game.
                for event in pygame.event.get():
                    if event.type == QUIT: # For Closing events
                        self.running = False
                        sys.exit() 
                    elif event.type == pygame.MOUSEBUTTONUP:
                        x, y = pygame.mouse.get_pos() # For initiating the input box with mouse
                        # position of input box
                        if(x>=50 and x<=650 and y>=250 and y<=300):
                            self.active = True
                            self.input_text = ''
                            self.time_start = time.time() # Amount of time our input_box was active
                        #position of reset box
                        if(x>=310 and x<=510 and y>=390 and self.end):
                            self.reset_game()
                            x,y = pygame.mouse.get_pos() # For reseting the game with the mouse 
                    elif event.type == pygame.KEYDOWN: # KEYDOWN is for testing whether a key is physically pressed down or not
                        if self.active and not self.end:
                            if event.key == pygame.K_RETURN: # K_RETURN checks for ENTER on the keyboard
                                print(self.input_text)
                                self.show_results(self.screen)
                                print(self.results)
                                self.draw_text(self.screen, self.results, 350, 28, self.RESULT_C)
                                self.end = True
                                
                            elif event.key == pygame.K_BACKSPACE:
                                self.input_text = self.input_text[:-1] # For backspacing letters in our input_text
                            else:
                                try:
                                    self.input_text += event.unicode # For special characters
                                except:
                                    pass
                pygame.display.update()
            
         clock.tick(60) # We render the graphic to the screen with 60 times per second
    def reset_game(self):
        self.screen.blit(self.open_img,(0,0)) # (0,0) represents the top left coordinate on the pygame window
        pygame.display.update() 
        time.sleep(2) # The window restarts again with reset values as below
        
        self.reset = False
        self.end = False
        
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0
        
        # Get random sentence
        self.word = self.get_sentence()
        if (not self.word): self.reset_game()
        
        # Drawing the heading
        self.screen.fill((0,0,0)) 
        self.screen.blit(self.bg,(0,0))
        msg = "Twenty One Pilots Quotes" 
        self.draw_text(self.screen, msg, 80, 50, self.HEAD_C)  
        
        # Drawing the rectangle for input box
        pygame.draw.rect(self.screen,(255,192,25),(50,250,650,50),2)
        
        # Draw the sentence string
        self.draw_text(self.screen, self.word, 200, 20, self.TEXT_C)
        pygame.display.update()


Game().run()        
