z=1000
def setup():
    size(600,600)
def draw():
    global z
    background(0)
    strokeWeight(5)
    stroke(random(0,255),random(0,255),random(0,255))
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(300,300,z,z)
    frameRate(1)
    z=z-100
    
