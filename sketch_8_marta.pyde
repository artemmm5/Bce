x=-500

marta=u'с 8 марта!'
def setup():
    size(600,600)
def draw():
    global x, marta
    background(190)
    x=x+1
    fill(random(0,255))
    text(marta,x,100)
    textSize(100)
    stroke(250,20,20)
    strokeWeight(5)
    line(250,250,330,300)
    line(400,250,330,300)
    line(330,450,200,300)
    line(250,250,200,300)
    line(450,300,330,450)
    line(400,250,450,300)
    
    
        
