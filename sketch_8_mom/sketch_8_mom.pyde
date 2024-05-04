x=-500
img=100
y=500
marta=u'с 8 марта!'
mini=1
def setup():
    size(600,600)
def draw():
    global x, marta, y,mini
    background(190)
    x=x+1
    fill(250,0,175)
    text(marta,x,550)
    textSize(100)
    stroke(250,20,20)
    strokeWeight(5)
    line(250,250,330,300)
    line(400,250,330,300)
    line(330,450,200,300)
    line(250,250,200,300)
    line(450,300,330,450)
    line(400,250,450,300)
    img=loadImage("gosling.jpg")
    image(img,40,40,y,y)
    y=y-mini
    if y < 10:
        mini=-1
        
    
        
