from Circle import Circle

circles = []

def setup():
    size(800, 600)
    for _ in range(50):
        circles.append(Circle(random(width), random(-500, -50), random(10, 30), random(1, 3), color(random(100, 200), random(100, 200), random(200, 255))))

def draw():
    background(173, 216, 230)
    
    for circle in circles[:]:
        noStroke()
        fill(circle.color)
        ellipse(circle.x, circle.y, circle.diameter, circle.diameter)
        circle.move()
        circle.reset(width, height)
        
        if circle.y - circle.diameter/2 > height and circle not in circles:
            circles.remove(circle)

    fill(51, 102, 153)
    textSize(48)
    textAlign(CENTER)
    textFont(createFont("Arial", 48))
    text("KLIX", width/2, height/4)
    
    fill(102, 51, 153)
    textSize(24)
    textFont(createFont("Arial", 24))
    text("Click anywhere to start", width/2, height/2)

def mousePressed():
    pass

