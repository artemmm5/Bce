c=50
s=300
w=50
a=300
d=-1
c_napravlenie=2
s_napravlenie=5
w_napravlenie=1
a_napravlenie=3
def setup():
    size(600,600)
def draw():
    global c,s,d, c_napravlenie,s_napravlenie,w,a,w_napravlenie
    background(0)
    ellipse(c,s,100,100)
    ellipse(w,a,100,100)
    c=c+c_napravlenie
    
    if c > 550:
        c_napravlenie=0
        s = s-s_napravlenie
    
    
    w=w+w_napravlenie
    if w > 550:
         w_napravlenie=0
         a=a-a_napravlenie
        
    
