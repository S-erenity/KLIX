from Circle import Circle

circles = []
game_started = False
kliks = 0
clicked = False
circle_size = 200  

def setup():
    size(800, 600)
    for _ in range(50):
        circles.append(Circle(random(width), random(-500, -50), random(10, 30), random(1, 3), color(random(100, 200), random(100, 200), random(200, 255))))

def draw():
    global game_started
    if not game_started:
        start_screen()
    else:
        game_screen()

def start_screen():
    global clicked
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

def game_screen():
    global kliks, clicked, circle_size
    background(173, 216, 230)
    fill(100, 150, 200)  
    ellipse(width/2, height/2, circle_size, circle_size)

    if dist(width/2, height/2, mouseX, mouseY) < circle_size / 2 and mousePressed and not clicked:
        kliks += 1
        clicked = True
        circle_size *= 1.1  
    elif not mousePressed:
        clicked = False
        circle_size = 200  

    fill(255)
    textSize(24)
    textAlign(RIGHT)
    text("Kliks: " + str(kliks), width - 20, 30)

def mousePressed():
    global game_started
    game_started = True

