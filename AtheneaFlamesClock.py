############# Libraries #############

import turtle               # UX.
import os                   # Syscalls.
import time                 # Timers.
import math                 # Flame locations in [x,y].

############# Recursos #############

"""
Turte only support GIF.
"""

# Clock photo (background).
image_path = os.path.join("Resourses", "ClockImage.gif")

# Flame Gif (All Frames).
flame_frames = [os.path.join("Resourses","Gif_Flame", f"{i}.gif") for i in range(20)]

############# Window  #############

# Screen 600x600 by default
window = turtle.Screen()
window.title("Flame Clock")
window.bgcolor("gray")
window.setup(width=600, height=600)

# Putting background.
window.bgpic(image_path)


############# Flames overlaping #############

# Frames registration for turtle window.
for frame in flame_frames:
    window.addshape(frame)

flames = []
for _ in range(12):
    # Initializer.
    flame = turtle.Turtle()
    flame.shape(flame_frames[0])
    flame.penup()

    # Appen flames array.
    flames.append(flame)

# Circle distribution.
"""
In this fragment of code you can change
everything to overlap the flames where
you want.
"""
radius = 175
rotation_offset = 2988
for i in range(12):
    angle = math.radians(30 * i + rotation_offset)
    x = radius * math.cos(angle) + 2
    y = radius * math.sin(angle) + 20
    flames[i].goto(x, y)

# Actualization function
def animate_flames():
    remove_interval = 10  # Timer for flames.
    last_removal_time = time.time()
    
    while flames:
        current_time = time.time()
        
        for frame in flame_frames:
            for flame in flames:
                flame.shape(frame)
            window.update()
            time.sleep(0.05)
        
        if current_time - last_removal_time >= remove_interval and flames:
            flame_to_remove = flames.pop()
            flame_to_remove.hideturtle()
            last_removal_time = current_time

# Keep window.
window.tracer(0)
animate_flames()
turtle.done()
