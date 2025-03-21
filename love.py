from math import sin, pi
import pygame
import turtle
import time
import random
import sys
import os

try:
    # Initialize turtle
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.shape("turtle")
    wn.bgcolor("black")
    t.speed(0)

    colors = ["red", "light pink"]

    # Initialize pygame mixer
    pygame.mixer.init()

    # Determine the correct path for the MP3 file
    if getattr(sys, 'frozen', False):
        # If running as a compiled EXE, use the PyInstaller temp directory
        base_path = sys._MEIPASS
    else:
        # If running as a normal Python script
        base_path = os.path.dirname(__file__)

    mp3_file = os.path.join(base_path, "Stevie Wonder - My Cherie Amour.mp3")

    # Function to play music
    def play_song():
        try:
            if not os.path.exists(mp3_file):
                print(f"Error: Music file not found at {mp3_file}")
                return

            pygame.mixer.music.load(mp3_file)
            pygame.mixer.music.play(-1)  # Loop indefinitely
            time.sleep(1)  # Small delay to ensure playback starts
        except Exception as e:
            print(f"Error playing music: {e}")

    # Start music
    play_song()

    # Function to set pen color
    def set_color(iteration):
        t.pencolor(colors[iteration % len(colors)])

    # Function to move the turtle to position (x, y)
    def at(x, y):
        t.penup()
        t.home()
        t.forward(x)
        t.left(90)
        t.forward(y)
        t.pendown()

    # Function to draw a heart shape
    def draw_heart(size, shape):
        t.pensize(5)
        radius = size * sin(shape * pi / 180) / (1 + sin((90 - shape) * pi / 180))
        t.right(shape)
        t.forward(size)
        t.circle(radius, 180 + shape)
        t.right(180)
        t.circle(radius, 180 + shape)
        t.forward(size)
        t.left(180 - shape)

    # Function to draw multiple hearts
    def draw_hearts():
        turtle.delay(50)
        for i in range(1, 10):
            set_color(i)
            at(0, i * -5)
            draw_heart(i * 10, 45)
            time.sleep(0.2)  # Small pause for effect
        t.penup()

    def heartCover():
        for i in range(1, 100):
            set_color(i)
            at(random.uniform(-300, 300), random.uniform(-300, 300))
            draw_heart(30, 45)
        

    # Function to draw a flower properly
    def draw_flower():
        at(-200, -50)  # Adjusted flower position
        t.pendown()
        for i in range(10):  # Reduced petals for balance
            set_color(i)
            t.begin_fill()
            t.circle(50, 180)
            t.right(180)
            t.circle(50, 180)
            t.end_fill()
            t.right(36)  # Rotates for a complete flower
        at(-300, -85)
        draw_heart(5, 45)

    # Function to display text
    def display_text(message, x, y, color="hot pink"):
        t.pencolor(color)
        at(x, y)
        t.write(message, align="center", font=("Arial", 24, "bold"))

    # Draw everything
    display_text("To: Jen <3", -250, 200)
    draw_hearts()
    draw_flower()
    display_text("Happy Valentine's Day!", 150, 150, "medium violet red")
    display_text("I love you, darling", 150, -200, "red")

    for i in range(1, 10):
        heartCover()


    wn.exitonclick()
except turtle.Terminator:  # Prevents errors if the window is closed early
    pass
except: 
    pass
