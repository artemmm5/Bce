z=100
def setup():
    size(600,600)
def draw():
    global z
    background(0)
    ellipse(z,z,100,100)
    z=z+1
    if z > 564:
        z=0
        
        
    
