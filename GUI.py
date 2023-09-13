# Import the necessary libraries
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

# Set the GPIO mode to BCM
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Define LED pins using GPIOZero
Red = LED(11)
White = LED(13)
Green = LED(15)

# Create the main GUI window
win = Tk()
win.title("LED BLINK")

# Create a custom font for the GUI buttons
myFont = tkinter.font.Font(family='Arial', size=12, weight="bold")

# Define functions for controlling the LEDs

# Function to turn the Red LED on/off
def RED_LED_ON():
    if Red.is_lit:
        Red.off()
        redButton["text"] = "TURN RED LED ON" 
    else:
        Red.on()
        redButton["text"] = "TURN RED LED OFF"

# Function to turn the White LED on/off
def WHITE_LED_ON():
    if White.is_lit:
        White.off()
        whiteButton["text"] = "TURN WHITE LED ON"
    else:
        White.on()
        whiteButton["text"] = "TURN WHITE LED OFF"

# Function to turn the Green LED on/off
def GREEN_LED_ON():
    if Green.is_lit:
        Green.off()
        greenButton["text"] = "TURN GREEN LED ON"
    else:
        Green.on()
        greenButton["text"] = "TURN GREEN LED OFF"

# Function to clean up GPIO and close the GUI
def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Create buttons for controlling the LEDs
redButton = Button(win, text="TURN RED LED ON", font=myFont, command=RED_LED_ON)
redButton.grid(row=0, column=1)

whiteButton = Button(win, text="TURN WHITE LED ON", font=myFont, command=WHITE_LED_ON)
whiteButton.grid(row=0, column=3)

greenButton = Button(win, text="TURN GREEN LED ON", font=myFont, command=GREEN_LED_ON)
greenButton.grid(row=0, column=6)

exitButton = Button(win, text="EXIT WINDOW", font=myFont, command=close, bg='red')
exitButton.grid(row=2, column=3)

# Define a protocol for handling window close
win.protocol("WM_DELETE_WINDOW", close)

# Start the main GUI event loop
win.mainloop()

# Loop forever