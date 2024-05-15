from turtle import*
import colorsys as cs
hideturtle()
speed('fastest')
bgcolor('black')
width(2)
h=0.0

for i in range(50):
    c=cs.hsv_to_rgb(h,1,1)
    color(c)
    for j in range(10):
        circle(i*4)
        right(36)
        h+=0.001
done()