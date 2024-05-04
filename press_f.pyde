z=300
s=300
r=300
q=300
def setup():
    size(600,600)
    
def draw():
    global s,q,r,z
    background(0)
    ellipse(z,z,100,100)
    ellipse(s,s,100,100)
    ellipse(r,q,100,100)
    ellipse(q,r,100,100)
    z=z+1
    
    
    
    s=s-1
    
    
    
    r=r-1
    
    
    
    q=q+1
    
    
    
