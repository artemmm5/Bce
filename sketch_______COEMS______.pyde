x=10
z=10
s=100
a=150
def setup():
    size(600,600)
def draw():
    global x
    global z
    global s
    global a
    fill(200,5,40)
    rect(300,300,x,x)
    fill(35,56,69)
    rect(300,200,z,z)
    fill(250,60,100)
    rect(500,400,s,s)
    fill(200,200,200)
    rect(400,200,a,a)
    x=x+1
    z=z+10
    s=s-5
    a=a-2
