r=0
g=0
b=0
img=0
img1=0
s=255
img2=0
img3=0
q=0
xa=0
add_library('sound')
def setup():
    global img, img1,img2,img3,q,xa
    size (1000,1000)
    strokeWeight(0)
    xa=SoundFile(this,"paskhalko-1488-dzhoker.mp3")
    q=SoundFile(this,"bulochka-s-sosiskoiu.mp3")
    img3=loadImage('111.png')
    img2=loadImage('222.png')
    img1=loadImage('22.jpeg')
    img=loadImage('ooo.png')
 
def draw():
    global r, g, b,img,img1,img2,q
    
    fill(116,13,13)
    rect(0,540,1000,500)
    fill(0)
    rect(600,300,150,300)
    rect(500,650,30,50)
    rect(280,500,50,60)
    rect(200,550,200,20)
    push()
    strokeWeight(5)
    fill(r,g,b)
    rect(100,300,400,200)
    pop()
    push()
    textSize(50)
    fill(0)
    rect(150,350,20,20)
    text("windows1488",155,400)
    pop()
    fill(82,228,255)
    rect(625,325,25,25)
    rect(675,325,25,25)
    fill(0)
    rect(200,650,250,75)
    fill(229,2,2)
    rect(215,700,50,15)
    image(img2,750,700,100,100)
def mouseClicked():
    global r, g, b, img, img3,q,xa
    if mouseX > 625 and mouseX < 650 and mouseY > 325 and mouseY < 350:
        r=8
        g=203
        b=250
    if mouseX > 150 and mouseX < 170 and mouseY > 350 and mouseY < 370:
        img=loadImage("pon.jpeg")
        image(img,0,0,1100,600)
        xa.play()
    if mouseX > 215 and mouseX < 265 and mouseY > 700 and mouseY < 715:
        img1=loadImage("22.jpeg")
        image(img1,-650,0,2500,600)
        q.play()
    if mouseX > 675 and mouseX < 700 and mouseY > 325 and mouseY < 350:
        r=0
        g=0
        b=0
    if mouseX > 750 and mouseX < 850 and mouseY > 700 and mouseY < 800:
        img3=loadImage("111.png") 
        image(img3,0,-100,1200,650)
        
        
        
    print(mouseX, mouseY)
        
