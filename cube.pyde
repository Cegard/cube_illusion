

def setup():
    size(600, 400)
    background(0, 0, 0)
    translate(width/2, height/2)
    stroke(204, 102, 0)
    strokeWeight(4)
    line(-60, -60, -60, 60)
    line(-60, 60, 60, 60)
    line(60, -60, 60, 60)
    line(60, -60, -60, -60)
    
    line(-20, -20, -20, 100)
    line(-20, 100, 100, 100)
    line(100, -20, 100, 100)
    line(100, -20, -20, -20)
    
    line(-20, -20, -60, -60)
    line(-20, 100, -60, 60)
    line(100, -20, 60, -60)
    line(100, 100, 60, 60)
    