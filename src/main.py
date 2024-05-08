from Achievements import Achievements
from Circle import Circle

circles = []
game_started = False
kliks = 0
clicked = False
circle_size = 200  
achievements = Achievements()  

spacebar_pressed = False
last_time_spacebar = 0  

auto_clicker_active = False
auto_clicker_rate = 3  
last_time_auto_clicker = 0  

klik_without_mouse_active = False
klik_increment = 1000  
last_time_mouse_clicked = 0  

def setup():
    global circles
    size(800, 600)
    for _ in range(50):
        circles.append(Circle(random(width), random(-500, -50), random(10, 30), random(1, 3), color(random(100, 200), random(100, 200), random(200, 255))))

def draw():
    global game_started, last_time_spacebar, last_time_auto_clicker, kliks, auto_clicker_rate
    if not game_started:
        start_screen()
    else:
        game_screen()

    if spacebar_pressed:
        if millis() - last_time_spacebar > 10:  
            kliks += 5
            last_time_spacebar = millis()

    if achievements.achieved_2000:  
        auto_clicker_rate = 10  
    if auto_clicker_active:
        if achievements.achieved_1500:  
            if millis() - last_time_auto_clicker > 1000:  
                kliks += auto_clicker_rate
                last_time_auto_clicker = millis()

    if klik_without_mouse_active:
        elapsed_time = millis() - last_time_mouse_clicked
        kliks += klik_increment * elapsed_time  

def keyPressed():
    global spacebar_pressed
    if key == ' ':
        spacebar_pressed = True

def keyReleased():
    global spacebar_pressed
    if key == ' ':
        spacebar_pressed = False

def mousePressed():
    global game_started, auto_clicker_active, klik_without_mouse_active, last_time_mouse_clicked
    game_started = True
    if achievements.achieved_1500:  
        auto_clicker_active = True
    if achievements.achieved_5000:  
        klik_without_mouse_active = True
        last_time_mouse_clicked = millis()  

def mouseReleased():
    global auto_clicker_active
    auto_clicker_active = False

def start_screen():
    global circles
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
    global kliks, clicked, circle_size, circles
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

    achievements.check_achievement(kliks)
    achievements.display_achievement()
