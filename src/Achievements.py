class Achievements:
    def __init__(self):
        self.achieved_200 = False
        self.achieved_700 = False
        self.achieved_1500 = False
        self.achieved_2000 = False  # New achievement
        self.achieved_5000 = False  # New achievement
        self.unlocked_auto_clicker = False
        self.achievement_time_200 = 0
        self.achievement_time_700 = 0
        self.achievement_time_1500 = 0
        self.achievement_time_2000 = 0  # Time when the achievement was unlocked
        self.achievement_time_5000 = 0  # Time when the achievement was unlocked

    def check_achievement(self, kliks):
        if kliks >= 200 and not self.achieved_200:
            self.achieved_200 = True
            self.achievement_time_200 = millis()
            return True
        if kliks >= 700 and not self.achieved_700:
            self.achieved_700 = True
            self.achievement_time_700 = millis()
            return True
        if kliks >= 1500 and not self.achieved_1500:
            self.achieved_1500 = True
            self.achievement_time_1500 = millis()
            return True
        if kliks >= 2000 and not self.achieved_2000:  # Check for 2000 kliks
            self.achieved_2000 = True
            self.achievement_time_2000 = millis()
            return True
        if kliks >= 5000 and not self.achieved_5000:  # Check for 5000 kliks
            self.achieved_5000 = True
            self.achievement_time_5000 = millis()
            return True
        return False

    def display_achievement(self):
        if self.achieved_200 and millis() - self.achievement_time_200 <= 5000:
            fill(106, 164, 184)
            rectMode(CORNER)
            rect(10, 10, 300, 60, 7)
            fill(255)
            textSize(16)
            textAlign(LEFT, CENTER)
            text("Getting better. Clicked the circle 200 times", 20, 40)
        if self.achieved_700 and millis() - self.achievement_time_700 <= 5000:
            fill(255, 150, 150)
            rectMode(CORNER)
            rect(10, 10, 300, 60, 7)
            fill(255)
            textSize(16)
            textAlign(LEFT, CENTER)
            text("OMG You're so pro! Clicked the circle 700 times.", 20, 40)
        if self.achieved_1500 and millis() - self.achievement_time_1500 <= 5000:
            fill(200, 150, 200)
            rectMode(CORNER)
            rect(10, 10, 400, 60, 7)
            fill(255)
            textSize(16)
            textAlign(LEFT, CENTER)
            text("uwu. Unlocked auto clicker because you're lazy. You can click anywhere now.", 20, 40)
        if self.achieved_2000 and millis() - self.achievement_time_2000 <= 5000:
            fill(255, 204, 0)  # Yellow color
            rectMode(CORNER)
            rect(10, 10, 450, 60, 7)
            fill(255)
            textSize(16)
            textAlign(LEFT, CENTER)
            text("BOOM! Your strength is now parallel to the strength of gods. Improved autokliker.", 20, 40)
        if self.achieved_5000 and millis() - self.achievement_time_5000 <= 5000:  # Display for 5 seconds
            fill(255, 215, 0)  # Gold color
            rectMode(CORNER)
            rect(10, 10, 500, 60, 7)
            fill(255)
            textSize(16)
            textAlign(LEFT, CENTER)
            text("You are now a kliker god. You now have the power to klik without your mouse.", 20, 40)
