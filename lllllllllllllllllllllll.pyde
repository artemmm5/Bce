s=30
ggg=5
def setup():
    size(600,600)
def draw():
    global s, ggg
    background(0)
    strokeWeight(5)
    stroke(random(0,255),random(0,255),random(0,255))
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(s,s,100,100)
    s=s+ggg
    if s > 570:
        ggg=-5
    
    
    if s < 30:
        ggg=+5
    
