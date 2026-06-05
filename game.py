# Game Project
# By Sarah Han


import simplegui, random, math


# Constants
WIDTH = 1350
HEIGHT = 675

CHAR_WIDTH = 160
CHAR_HEIGHT = 160
CHAR_DASH_WIDTH = 210

MAILBOX_WIDTH = 175
MAILBOX_HEIGHT = 255

COIN_WIDTH = 45
COIN_HEIGHT = 45

HEART_HEIGHT = 38
HEART_WIDTH = 41
HEART_Y = 35
HEART_X = WIDTH/16
HEART_SPACE = 50

DASHBAR_WIDTH = 240
DASHBAR_HEIGHT = 70
DASHBAR_Y = 42

POINTS_DISPLAY_X = 1175
POINTS_DISPLAY_Y = 45

PLATFORM_WIDTH = 550
PLATFORM_HEIGHT = 45

PLATFORM_INTERVAL = 700

PLATFORM_START_X = 2600
PLAT_HEIGHT_DIFF = 100

OBJECT_SPACING = 100

TEXT_COLOUR = "#514469"
RED_COLOUR = "#EF5D6C"

GROUND = 625
GRAVITY = 1

DOUBLE_JUMP_REDUCTION = 5

NORMAL_SPD = -8
DASH_SPD = -12

END_TIME = 2700 # 45 seconds
END_DELAY = 360 # 6 seconds

START = 0
GAME = 1
END = 2
LEVEL_SELECT = 3
WIN = 4
INTRO_CUTSCENE = 5

screen = START
level = 0

scene_index = 0

play_intro_scene = True
added_birds = False


# Images
BG_IMG = simplegui.load_image("https://raw.githubusercontent.com/magenta-otter/delivery-dash-game/refs/heads/main/background.png")
CHAR_IMG = simplegui.load_image("https://www.image2url.com/r2/default/images/1780528884855-0361e68a-38f9-4af7-b71a-f22ff3e32a18.png")
CHAR_IMG2 = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-29-36262c4a-6188-4e74-8bd6-216c80ef9d52.png")
PLATFORM_IMG = simplegui.load_image("https://image2url.com/r2/default/images/1774196598380-d866da35-58c4-4491-be1d-d8714b390096.png")
PLATFORM2_IMG = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-12-c4c49b47-4be2-415c-9931-25799bdcf677.png")
TRASHCAN_IMG = simplegui.load_image("https://image2url.com/r2/default/images/1775075496535-c2227d39-7e6e-4f41-aaf8-13d5c5405cfb.png")
BOXES_IMG = simplegui.load_image("https://image2url.com/r2/default/images/1775076320770-715f6c1b-bb5a-4768-8d7c-7515101918ab.png")
BARRIER_IMG = simplegui.load_image("https://raw.githubusercontent.com/magenta-otter/delivery-dash-game/refs/heads/main/barrier_obstacle.png")
CONE_IMG = simplegui.load_image("https://www.image2url.com/r2/default/images/1776195471973-cf170f65-b361-42e5-b6fa-4c3807998f76.png")
BIRD_IMG = simplegui.load_image("https://raw.githubusercontent.com/magenta-otter/delivery-dash-game/refs/heads/main/bluebird_obstacle.png")
BIRD_IMG2 = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-27-3d080d34-2dc2-4656-88ce-fcf81b5f551f.png")
BIRD2_IMG = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-22-7f8d5344-ba55-45d5-9849-1d9c8261ca68.png")
BIRD2_IMG2 = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-27-dcddffdc-7cbf-4fa2-a01f-dec1a7c50917.png")
MENU_IMG = simplegui.load_image("https://image2url.com/r2/default/images/1775582345888-5bec6e94-7dfb-45b3-8d14-2a5a88eb2514.png")
HEART_IMG = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-22-91e696c5-7e1e-42f0-bcad-805ab181e1b0.png")
COIN_IMG = simplegui.load_image("https://cdn.phototourl.com/free/2026-06-01-7fab19b8-58b3-4d83-a845-1fffe8fb9118.png")
COIN_IMG2 = simplegui.load_image("https://cdn.phototourl.com/free/2026-06-01-b3a3cd15-3456-4f9e-8dda-0017a6555c73.png")
COIN_IMG3 = simplegui.load_image("https://cdn.phototourl.com/free/2026-06-01-59eb4503-682a-47e3-b7f9-1a16321f395e.png")
COIN_IMG4 = simplegui.load_image("https://cdn.phototourl.com/free/2026-06-01-b3a3cd15-3456-4f9e-8dda-0017a6555c73.png")
GAMEOVER_IMG = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-26-e1f2b56a-b963-4c6c-bbd0-1b42fddfe470.png")
LEVEL_IMG = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-26-0630e119-461b-4301-900f-b961f6d0456e.png")
MAILBOX_IMG = simplegui.load_image("https://cdn.phototourl.com/free/2026-06-03-48db3ee6-f8a5-4033-8a77-4148649f05a6.png")
MAILBOX_IMG2 = simplegui.load_image("https://cdn.phototourl.com/free/2026-06-03-10f6da15-92de-4b14-ac07-70dcd5c401d5.png")
WINSCREEN_IMG = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-28-e9296bff-b8ef-4a0a-843f-004323860436.png")
PLAYERDASH_IMG = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-20-29e77944-b0b9-4a53-b90d-17b33135c23e.png")
PLAYERDASH_IMG2 = simplegui.load_image("https://cdn.phototourl.com/free/2026-06-04-238a2ca9-dd4a-4192-b108-f5d6816e2e73.png")
INTRO_IMG = simplegui.load_image("https://t4.ftcdn.net/jpg/15/62/13/23/360_F_1562132364_z97PZPIvFl9zAhrsSgvt7h9JwJlqBWxn.jpg")
INTRO_IMG2 = simplegui.load_image("https://opengameart.org/sites/default/files/5_71.png")
DASHBAR0 = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-21-cf8d8a94-bebf-4530-8fb5-b89105f75558.png")
DASHBAR1 = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-21-76bae17d-bad8-44f5-8a7b-66463b7d139f.png")
DASHBAR2 = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-21-f4a1d063-c6f4-4cf4-a07d-cecdef1194c8.png")
DASHBAR3 = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-21-d0160ab4-d30c-40fb-aa1d-51d38d30a487.png")
DASHBAR4 = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-21-16e3bb43-11bf-4960-bf2e-9e5b1e501855.png")
DASHBAR5 = simplegui.load_image("https://cdn.phototourl.com/free/2026-05-21-9884f91e-0820-4461-84f2-b397000482f8.png")


# Store source image sizes
IMG_SIZE = {CHAR_IMG:(550,560), CHAR_IMG2:(550,560), BG_IMG:(3500,1750), PLATFORM_IMG:(1230,130), PLATFORM2_IMG:(1230,130), TRASHCAN_IMG:(260,360), BOXES_IMG:(370,320), BARRIER_IMG:(580,300), CONE_IMG:(250,290), BIRD_IMG:(300,200), BIRD_IMG2:(300,200), BIRD2_IMG:(300,200), BIRD2_IMG2:(300,200), MENU_IMG:(3500,1750), HEART_IMG:(300,280), COIN_IMG:(900,900), COIN_IMG2:(900,900), COIN_IMG3:(900,900), COIN_IMG4:(900,900), GAMEOVER_IMG:(3500,1750), LEVEL_IMG:(3500,1750), MAILBOX_IMG:(640,910), MAILBOX_IMG2:(640,910), WINSCREEN_IMG:(3500,1750), PLAYERDASH_IMG:(730,560), PLAYERDASH_IMG2:(730,560), INTRO_IMG:(641,360), INTRO_IMG2:(2304,1296), DASHBAR0:(890,290)}

BUTTONS = {"play":{"left":1035,"right":1280,"top":335,"bottom":400}, "yes":{"left":450,"right":595,"top":445,"bottom":525}, "no":{"left":750,"right":895,"top":445,"bottom":525}, "level1":{"left":260,"right":475,"top":225,"bottom":445}, "level2":{"left":565,"right":785,"top":225,"bottom":445}, "level3":{"left":875,"right":1095,"top":225,"bottom":445}, "back":{"left":35,"right":115,"top":30,"bottom":110}, "endless":{"left":450,"right":905,"top":515,"bottom":610}}

INTRO_SCENE = [INTRO_IMG,INTRO_IMG2]

OBSTACLE_IMAGES = [TRASHCAN_IMG, BOXES_IMG, BARRIER_IMG, CONE_IMG]
OBSTACLE_DEST_SIZE = {TRASHCAN_IMG:(55,75), BOXES_IMG:(100,85), BARRIER_IMG:(130,75), CONE_IMG:(60,75), BIRD_IMG:(75,50), BIRD2_IMG:(75,50)}

# Animation frames lists
PLAYER_FRAMES = [CHAR_IMG,CHAR_IMG2]
PLAYER_DASH_FRAMES = [PLAYERDASH_IMG,PLAYERDASH_IMG2]
BIRD_FRAMES = [BIRD_IMG,BIRD_IMG2]
BIRD2_FRAMES = [BIRD2_IMG,BIRD2_IMG2]
COIN_FRAMES = [COIN_IMG,COIN_IMG2,COIN_IMG3,COIN_IMG4]
MAILBOX_FRAMES = [MAILBOX_IMG,MAILBOX_IMG2]

# Function to calculate distance between two positions with Pythagorean theorem
def dist(pos1, pos2):
    a = pos2[1] - pos1[1]
    b = pos2[0] - pos1[0]
    distance = math.sqrt(a**2 + b**2)
    return distance


def new_game():
    global bg_shift, time, points, dash_points, object_speed, last_plat_dist, platforms_list, platform_heights, obstacles_list, coins_list, obstacle_x_list, hearts_list, screen, player, dash_recovery_timer, mailbox_spawned, anim_time
    bg_shift = 0
    time = 0
    points = 0
    dash_points = 0
    dash_recovery_timer = 0
    anim_time = 0
    mailbox_spawned = False
    object_speed = NORMAL_SPD
    last_plat_dist = 0 # since last platform
    
    platforms_list = []
    platform_heights = []
    obstacles_list = []
    coins_list = []
    obstacle_x_list = []
    hearts_list = []
    
    # Create starting platform
    platform = Platform([PLATFORM_START_X,GROUND - PLAT_HEIGHT_DIFF], # start position
                       PLATFORM_IMG,
                       PLATFORM_WIDTH,PLATFORM_HEIGHT)
    platforms_list.append(platform)
    platform_heights.append(1) # add starting y
    
    player = Character([200,550], # start position
                      CHAR_IMG,
                      CHAR_WIDTH,CHAR_HEIGHT)
    
    screen = GAME


def display_score(canvas, x, y):
    score = str(points)
    offset = 100
    canvas.draw_text("Score:",
                     (x,y), # position
                     35, # text size
                     TEXT_COLOUR)
    canvas.draw_text(score,
                     (x + offset,y), # position
                     35, # text size
                     TEXT_COLOUR)
    
def display_points(canvas, x, y, size, colour):
    score = str(points)
    offset = frame.get_canvas_textwidth(score, size)/2
    canvas.draw_text(score,
                     (x - offset,y), # position
                     size,
                     colour)
    
def animate(frames_list, entity):
    # Calculate the current frame index using the total number of frames to cycle frames in a loop
    frame_index = anim_time % len(frames_list)
    
    # Assign the correct image frame
    entity.img = frames_list[frame_index]
    
# Draw hearts on screen depending on how many lives the player has
def display_health(canvas):
    if player.lives >= 1:
        heart_w,heart_h = IMG_SIZE[HEART_IMG]
        canvas.draw_image(HEART_IMG, 
                          (heart_w/2,heart_h/2), # file center
                          (heart_w,heart_h), # file size
                          (HEART_X - HEART_SPACE,HEART_Y), # position
                          (HEART_WIDTH,HEART_HEIGHT))
    if player.lives >= 2:
        heart_w,heart_h = IMG_SIZE[HEART_IMG]
        canvas.draw_image(HEART_IMG, 
                          (heart_w/2,heart_h/2), # file center
                          (heart_w,heart_h), # file size
                          (HEART_X,HEART_Y), # position
                          (HEART_WIDTH,HEART_HEIGHT))
    if player.lives >= 3:
        heart_w,heart_h = IMG_SIZE[HEART_IMG]
        canvas.draw_image(HEART_IMG, 
                          (heart_w/2,heart_h/2), # file center
                          (heart_w,heart_h), # file size
                          (HEART_X + HEART_SPACE,HEART_Y), # position
                          (HEART_WIDTH,HEART_HEIGHT))
        
def dash_bar(canvas):
    w,h = IMG_SIZE[DASHBAR0]
    
    # Image changes depending on points
    if dash_points >= 1000:
        img = DASHBAR5
        
    elif dash_points >= 800:
        img = DASHBAR4
        
    elif dash_points >= 600:
        img = DASHBAR3
        
    elif dash_points >= 400:
        img = DASHBAR2
        
    elif dash_points >= 200:
        img = DASHBAR1
        
    else:
        img = DASHBAR0
        
    canvas.draw_image(img,
                      (w/2,h/2),
                      (w,h),
                      (WIDTH/2,DASHBAR_Y),
                      (DASHBAR_WIDTH,DASHBAR_HEIGHT))

            
# Create random platform            
def spawn_platform():
    global plat_y
    
    height_level = random.randint(1,4) # Choose random height
    
    # if chosen height is equal to last height OR if too far away, choose height again
    while height_level == platform_heights[-1] or abs(platform_heights[-1] - height_level) > 2:
        height_level = random.randint(1,4)
    
    plat_y = GROUND - (PLAT_HEIGHT_DIFF*height_level)
    
    # choose a random platform variation
    image = random.choice([PLATFORM_IMG,PLATFORM2_IMG])
    
    # create platform
    platform = Platform([PLATFORM_START_X,plat_y], # start position
                        image,
                        PLATFORM_WIDTH,PLATFORM_HEIGHT)
    platforms_list.append(platform)
    platform_heights.append(height_level)
    
    
# Create random obstacle
def spawn_obstacle():
    image = random.choice(OBSTACLE_IMAGES)
    # set obstacle w and h based on chosen image
    obstacle_width,obstacle_height = OBSTACLE_DEST_SIZE[image]
    # calculate radius of obstacle
    radius = (obstacle_width + obstacle_height)/4
    # sets obstacle spawn y position based on platform y position
    obstacle_y = plat_y - (PLATFORM_HEIGHT/2) - (obstacle_height/2)
    # if obstacle is a bird, spawn higher up
    if image in (BIRD_IMG, BIRD2_IMG):
        obstacle_y -= 130
    # choose random spawn x position
    space = OBJECT_SPACING
    obstacle_x = random.choice([PLATFORM_START_X, PLATFORM_START_X - space, PLATFORM_START_X + space])
    obstacle_x_list.append(obstacle_x)

    # create obstacle
    obstacle = Obstacle([obstacle_x,obstacle_y], # start position
           image,
           obstacle_width,obstacle_height, radius)
    obstacles_list.append(obstacle)
    

def spawn_heart():
    heart_height_dist = 30
    heart_y = plat_y - (PLATFORM_HEIGHT/2) - (HEART_HEIGHT/2) - heart_height_dist
    heart = Heart([PLATFORM_START_X,heart_y], 
                  HEART_IMG,
                  HEART_WIDTH,
                  HEART_HEIGHT)
    hearts_list.append(heart)
    

def spawn_coin():
    coin_height_dist = 30 # height from platform
    coin_y = plat_y - (PLATFORM_HEIGHT/2) - (COIN_HEIGHT/2) - coin_height_dist
    
    coin_x = PLATFORM_START_X
    space = OBJECT_SPACING
    if make_obstacle == 1:
        x = obstacle_x_list[-1] # last obstacle's x
        
    elif player.lives < 3 and make_heart == 1:
        x = PLATFORM_START_X # last heart's x
        
    else:
        x = 0
        
    # create coin
    # if nothing else in position, then spawn coin at position
    if not x == PLATFORM_START_X:
        coin = Coin([coin_x,coin_y],
                    COIN_IMG,
                    COIN_WIDTH,
                    COIN_HEIGHT)
        coins_list.append(coin)
    
    if not x == PLATFORM_START_X - space:
        coin = Coin([coin_x - space,coin_y],
                    COIN_IMG,
                    COIN_WIDTH,
                    COIN_HEIGHT)
        coins_list.append(coin)
    
    if not x == PLATFORM_START_X + space:
        coin = Coin([coin_x + space,coin_y],
                    COIN_IMG,
                    COIN_WIDTH,
                    COIN_HEIGHT)
        coins_list.append(coin)
    

def spawn_mailbox():
    global mailbox
    mailbox_y = GROUND - (MAILBOX_HEIGHT/2)
    mailbox = Mailbox([PLATFORM_START_X,mailbox_y], 
                      MAILBOX_IMG,
                      MAILBOX_WIDTH, 
                      MAILBOX_HEIGHT)
    
    
def off_screen(position):
    x,y = position
    return x < (0 - WIDTH)

    
    
# Classes
class Character:
    def __init__(self, position, image, width, height):
        self.pos = position
        self.img = image
        self.width = width
        self.height = height
        self.rad = 75
        self.vel = [0,0] # starting velocity
        self.JUMP_SPEED = 16
        self.jump_count = 0
        self.lives = 3
        self.immune = False
        self.dash = False
        self.shrink = 1.4 # sliding size reduction
        self.falling = True
        
    def draw(self, canvas):
        w,h = IMG_SIZE[self.img]
        canvas.draw_image(self.img,
                         (w/2,h/2), # center of file
                         (w,h), # size of file
                         self.pos,
                         (self.width, self.height))
#        canvas.draw_circle(self.pos, self.rad, 2, "red")
        
    def update(self):
        self.pos[0] += self.vel[0] # horizontal
        self.pos[1] += self.vel[1] # vertical
        
        if self.pos[1] < GROUND - (player.height/2): # above ground
            self.falling = True
            
        else:
            self.vel[1] = 0
            self.pos[1] = GROUND - (player.height/2)
            self.falling = False
            self.jump_count = 0
            
        if self.falling == True:
            self.vel[1] += GRAVITY
          
        
    def jump(self):
        if not self.jump_count == 2:
            if self.jump_count == 0:
                # reset velocity before jump so falling velocity doesn't affect jump height
                if self.vel[1] > 0:
                    self.vel[1] = 0
                    
                self.vel[1] += -self.JUMP_SPEED # up is negative
                self.falling = True
                self.jump_count += 1
                
            else:
                if self.vel[1] > 0:
                    self.vel[1] = 0

                # second jump has reduced jump height
                self.vel[1] += -self.JUMP_SPEED + DOUBLE_JUMP_REDUCTION
                self.falling = True
                self.jump_count += 1
                
    def slide(self):
        self.height /= self.shrink
        self.rad /= self.shrink
        # calculate offset after shrinking character
        offset = (CHAR_HEIGHT - self.height)/2
        # teleport player based on offset to make movement look consistent
        self.pos[1] += offset
        
    def unslide(self):
        offset = (CHAR_HEIGHT - self.height)/2
        self.height *= self.shrink
        self.rad *= self.shrink
        # teleport player so they don't fall through the platform
        self.pos[1] -= offset
            
    def on_platform(self, platform):
        # Player is between platform left and right
        condition1 = (self.pos[0] >= platform.left - (self.width/2)) and (self.pos[0] <= platform.right + (self.width/2))
        # Player is about to land on top of platform, next y makes sure function is true when player is landing down
        next_y = (self.pos[1] + (self.height/2)) + self.vel[1]
        condition2 = (self.pos[1] + (self.height/2) <= platform.top) and (next_y >= platform.top)
        return condition1 and condition2
        
    def collide(self, other):
        # Calculate distance
        distance = dist(self.pos, other.pos)
        # Return true or false
        return distance < self.rad + other.rad
        
        
class Platform:
    def __init__(self, position, image, width, height):
        self.pos = position
        self.img = image
        self.width = width
        self.height = height
        self.left = self.pos[0] - (self.width/2)
        self.right = self.pos[0] + (self.width/2)
        self.top = self.pos[1] - (self.height/2)
        self.vel = [object_speed,0] # starting velocity
        
    def draw(self, canvas):
        w,h = IMG_SIZE[self.img]
        canvas.draw_image(self.img,
                         (w/2,h/2), # center of file
                         (w,h), # size of file
                         self.pos,
                         (self.width,self.height))
        
    def update(self):
        self.vel[0] = object_speed
        self.pos[0] += self.vel[0]
        self.left = self.pos[0] - (self.width/2)
        self.right = self.pos[0] + (self.width/2)
        self.top = self.pos[1] - (self.height/2)
        
        
class Heart:
    def __init__(self, position, image, width, height):
        self.pos = position
        self.img = image
        self.width = width
        self.height = height
        self.rad = 25
        self.vel = [object_speed,0] # starting velocity
        
    def draw(self, canvas):
        w,h = IMG_SIZE[self.img]
        canvas.draw_image(self.img, 
                          (w/2,h/2),
                          (w,h), 
                          self.pos, 
                          (self.width,self.height))
        
    def update(self):
        self.vel[0] = object_speed
        self.pos[0] += self.vel[0]
        
        
class Obstacle:
    def __init__(self, position, image, width, height, radius):
        self.pos = position
        self.img = image
        self.width = width
        self.height = height
        self.rad = radius
        self.vel = [object_speed,0] # starting velocity
        
    def draw(self, canvas):
        w,h = IMG_SIZE[self.img]
        canvas.draw_image(self.img,
                         (w/2,h/2), # center of file
                         (w,h), # size of file
                         self.pos,
                         (self.width,self.height))
#        canvas.draw_circle(self.pos, self.rad, 2, "red")
        
    def update(self):
        self.vel[0] = object_speed
        self.pos[0] += self.vel[0]
        
        
class Coin:
    def __init__(self, position, image, width, height):
        self.pos = position
        self.img = image
        self.width = width
        self.height = height
        self.rad = 30
        self.vel = [object_speed,0] # starting velocity
        
    def draw(self, canvas):
        w,h = IMG_SIZE[self.img]
        canvas.draw_image(self.img, 
                          (w/2,h/2),
                          (w,h),
                          self.pos,
                          (self.width,self.height))
#        canvas.draw_circle(self.pos, self.rad, 2, "red")
        
    def update(self):
        self.vel[0] = object_speed
        self.pos[0] += self.vel[0]
        
       
class Mailbox:
    def __init__(self, position, image, width, height):
        self.pos = position
        self.img = image
        self.width = width
        self.height = height
        self.rad = 85
        self.vel = [object_speed,0] # starting velocity
        
    def draw(self, canvas):
        w,h = IMG_SIZE[self.img]
        canvas.draw_image(self.img, 
                          (w/2,h/2),
                          (w,h),
                          self.pos,
                          (self.width,self.height))
#        canvas.draw_circle(self.pos, self.rad, 2, "red")
    def update(self):
        self.vel[0] = object_speed
        self.pos[0] += self.vel[0]
    

# Handler to draw on canvas
def draw(canvas):
    global bg_shift, time, coins_list, obstacles_list, hearts_list, points, dash_points, make_obstacle, make_heart, screen, mailbox_spawned, last_plat_dist, object_speed, dash_recovery_timer, anim_time
    if screen == LEVEL_SELECT:
        w,h = IMG_SIZE[LEVEL_IMG]
        canvas.draw_image(LEVEL_IMG,
                          (w/2,h/2),
                          (w,h),
                          (WIDTH/2,HEIGHT/2),
                          (WIDTH,HEIGHT))
    if screen == START:
        w,h = IMG_SIZE[MENU_IMG]
        canvas.draw_image(MENU_IMG,
                         (w/2,h/2), # center of file
                         (w,h), # size of file
                         (WIDTH/2,HEIGHT/2), # center 
                         (WIDTH,HEIGHT)) # size
        
        
    elif screen == GAME:
        # Scrolling background
        bg_w,bg_h = IMG_SIZE[BG_IMG]
        canvas.draw_image(BG_IMG,
                         (bg_w/2,bg_h/2), # center of file
                         (bg_w,bg_h), # size of file
                         (WIDTH/2 - bg_shift,HEIGHT/2), # center of bg
                         (WIDTH,HEIGHT)) # size of bg
        # Repeat bg to the right of first bg
        canvas.draw_image(BG_IMG,
                         (bg_w/2,bg_h/2),
                         (bg_w,bg_h),
                         (WIDTH/2 + WIDTH - bg_shift,HEIGHT/2), # shift bg position
                         (WIDTH,HEIGHT))
        # changes background scroll speed
        bg_shift += -(object_speed) - 3
        # resets bg when it goes off-screen
        bg_shift %= WIDTH
        

        player.update()


        display_health(canvas)
        display_score(canvas, POINTS_DISPLAY_X, POINTS_DISPLAY_Y)
        
        if level >= 3:
            dash_bar(canvas) # dispay dash icon
        
        if player.dash: # when dashing
            if dash_points > 0:
                animate(PLAYER_DASH_FRAMES, player)
                player.width = CHAR_DASH_WIDTH
                dash_points -= 3 # decrease points
                player.immune = True # immune to obstacles
                object_speed = DASH_SPD # goes faster
                
        else: # when not dashing
            # creates player animation
            animate(PLAYER_FRAMES, player)
                
            player.width = CHAR_WIDTH
            player.immune = False
            object_speed = NORMAL_SPD
            if dash_points < 1000: # max dash points
                dash_points += 1 # increase points
                
        if dash_points <= 0:
            player.dash = False
            dash_recovery_timer = 80
            
        if dash_recovery_timer > 0:
            player.immune = True
            
            # create flashing effect
            flash_time = time//6
            if not flash_time % 2 == 0:
                player.draw(canvas)
            
            dash_recovery_timer -= 1
#            print(flash_time)
            
        else:
            player.draw(canvas)
            
            
#        print(player.dash)
#        print(dash_points)
        
        # spawn mailbox when level ends + delay a few seconds
        if time == END_TIME + END_DELAY:
            # only spawn the mailbox that ends the level if not in endless mode
            if not level == 4:
                spawn_mailbox()
                mailbox_spawned = True
            
        if mailbox_spawned:
            mailbox.draw(canvas)
            mailbox.update()
            animate(MAILBOX_FRAMES,mailbox)
            
            if player.collide(mailbox):
                screen = WIN
        
        last_plat_dist += abs(object_speed) # update distance
        # if level time hasn't reached the end time or if endless mode is activated, spawn platforms
        if time < END_TIME or level == 4:
            # spawn a platform after a certain distance since last one
            if last_plat_dist >= PLATFORM_INTERVAL:
                spawn_platform()
                last_plat_dist = 0 # reset count

                if level == 1:
                    make_obstacle = random.randint(0,2) # 1 in 3 chance
                    if make_obstacle == 1:
                        spawn_obstacle()

                elif level == 2:
                    make_obstacle = random.randint(0,1) # 50% chance
                    if make_obstacle == 1:
                        spawn_obstacle()

                elif level >= 3:
                    make_obstacle = 1
                    spawn_obstacle()

                if player.lives < 3:
                    # small chance to spawn a heart on platforms without obstacles
                    if not make_obstacle == 1:
                        make_heart = random.randint(0,8) # 10% chance
                        if make_heart == 1:
                            spawn_heart()

                spawn_coin()
            

        for platform in platforms_list:
            platform.draw(canvas)
            platform.update()
            
            # Check if player is on platform
            if player.on_platform(platform):
                player.falling = False
                player.jump_count = 0
                player.vel[1] = 0
                player.pos[1] = platform.top - (player.height/2)
                
            if off_screen(platform.pos):
                platforms_list.remove(platform)
                platform_heights.remove(platform_heights[0])
                
        
        new_obstacles = []
        for obstacle in obstacles_list:
            obstacle.draw(canvas)
            obstacle.update()
            
            if obstacle.img in (BIRD_IMG,BIRD_IMG2):
                animate(BIRD_FRAMES,obstacle)

            if obstacle.img in (BIRD2_IMG,BIRD2_IMG2):
                animate(BIRD2_FRAMES,obstacle)
            
            # Check if player has collided with obstacle
            if player.collide(obstacle):
                if not player.immune:
                    player.lives -= 1
            else:
                new_obstacles.append(obstacle)
                
            obstacles_list = new_obstacles
                
            if off_screen(obstacle.pos):
                obstacles_list.remove(obstacle)
                
#        print(time)
        new_hearts = []
        for heart in hearts_list:
            heart.draw(canvas)
            heart.update()
            
            # Check if player has collided with heart
            if player.collide(heart):
                player.lives += 1
            else:
                new_hearts.append(heart)
                
            hearts_list = new_hearts
            
            if off_screen(heart.pos):
                hearts_list.remove(heart)
                
        new_coins = []
        for coin in coins_list:
            coin.draw(canvas)
            coin.update()
            animate(COIN_FRAMES,coin)
            
            # Check if player has collided with coin
            if player.collide(coin):
                points += 1
            else:
                new_coins.append(coin)

            coins_list = new_coins
            
            if off_screen(coin.pos):
                coins_list.remove(coin)
                
        
        
        # Add 1 to time every 1/60th of a second
        time += 1
        anim_time = time//10
        ########## Test for removing items in list when off screen ##########
#        print(len(new_coins))
#        print(len(coins_list))
#        print(object_speed)
#        print(last_plat_dist)
#        print(dash_points)

        
        if player.lives == 0:
            screen = END
#        print(level)
#        print(OBSTACLE_IMAGES)
    if screen == END:
        w,h = IMG_SIZE[GAMEOVER_IMG]
        canvas.draw_image(GAMEOVER_IMG,
                          (w/2,h/2),
                          (w,h),
                          (WIDTH/2,HEIGHT/2),
                          (WIDTH,HEIGHT))
        
    if screen == WIN:
        w,h = IMG_SIZE[WINSCREEN_IMG]
        canvas.draw_image(WINSCREEN_IMG,
                          (w/2,h/2),
                          (w,h),
                          (WIDTH/2,HEIGHT/2),
                          (WIDTH,HEIGHT))
        display_points(canvas,
                       WIDTH/2, # x
                       525, # y
                       40, # size
                       RED_COLOUR)
        
    if screen == INTRO_CUTSCENE:
        image = INTRO_SCENE[scene_index]
        w,h = IMG_SIZE[image]
        canvas.draw_image(image,
                          (w/2,h/2),
                          (w,h),
                          (WIDTH/2,HEIGHT/2),
                          (WIDTH,HEIGHT))


def key_press(key):
    global screen, scene_index
    if screen == GAME:
        if key == simplegui.KEY_MAP["space"]:
            # player can't jump when level is ending
            if mailbox_spawned == False:
                player.jump()
    
    if level > 1:
        if key == simplegui.KEY_MAP["down"]:
            player.slide()
            
    if level >= 3:
        if key == simplegui.KEY_MAP["up"]:
            # if not dashing, enter dash mode
            if not player.dash:
                if dash_points >= 200:
                    player.dash = True
                    
    if screen == INTRO_CUTSCENE:
        # go to next scene after pressing space
        if key == simplegui.KEY_MAP["space"]:
            scene_index += 1
            # if at last scene, go to next screen
            if scene_index == len(INTRO_SCENE):
                screen = LEVEL_SELECT
                scene_index = 0 # reset index
            
            
def key_release(key):
    if level > 1:
        if key == simplegui.KEY_MAP["down"]:
            player.unslide()


def mouse_click(position):
    global screen,level, play_intro_scene, added_birds
    x = position[0]
    y = position[1]
    
    if screen == START:
        play = BUTTONS["play"]
        # Detects when play button is pressed and switches to next screen
        if (play["left"] <= x <= play["right"]) and (play["top"] <= y <= play["bottom"]):
            if play_intro_scene == True:
                screen = INTRO_CUTSCENE
                # set variable as false so cutscene only plays once
                play_intro_scene = False
            else:
                screen = LEVEL_SELECT
                # reset mouse click position
                x = 0
                y = 0

    if screen == LEVEL_SELECT:
        level1 = BUTTONS["level1"]
        level2 = BUTTONS["level2"]
        level3 = BUTTONS["level3"]
        back = BUTTONS["back"]
        endless = BUTTONS["endless"]
        # Detect when buttons are pressed
        if (level1["left"] <= x <= level1["right"]) and (level1["top"] <= y <= level1["bottom"]):
            new_game()
            level = 1
            if added_birds == True:
                OBSTACLE_IMAGES.remove(BIRD_IMG)
                OBSTACLE_IMAGES.remove(BIRD2_IMG)
                added_birds = False

            
        elif (level2["left"] <= x <= level2["right"]) and (level2["top"] <= y <= level2["bottom"]):
            new_game()
            level = 2
            # If level 2 or higher, bird obstacles can appear
            if added_birds == False: # if not added yet
                OBSTACLE_IMAGES.extend([BIRD_IMG, BIRD2_IMG])
                added_birds = True

            
        elif (level3["left"] <= x <= level3["right"]) and (level3["top"] <= y <= level3["bottom"]):
            new_game()
            level = 3
            
        elif (back["left"] <= x <= back["right"]) and (back["top"] <= y <= back["bottom"]):
            screen = START
            
        elif (endless["left"] <= x <= endless["right"]) and (endless["top"] <= y <= endless["bottom"]):
            new_game()
            level = 4

    if screen == END:
        yes = BUTTONS["yes"]
        no = BUTTONS["no"]
        # Detect when buttons are pressed
        if (yes["left"] <= x <= yes["right"]) and (yes["top"] <= y <= yes["bottom"]):
            new_game()
        
        # Return to main screen
        elif (no["left"] <= x <= no["right"]) and (no["top"] <= y <= no["bottom"]):
            screen = LEVEL_SELECT
            
    if screen == WIN:
        if (0 <= x <= WIDTH) and (0 <= y <= HEIGHT):
            screen = LEVEL_SELECT

# Frame
frame = simplegui.create_frame("Home", WIDTH, HEIGHT)
frame.set_keydown_handler(key_press)
frame.set_keyup_handler(key_release)
frame.set_mouseclick_handler(mouse_click)
frame.set_draw_handler(draw)

    
# Start frame
frame.start()
