import pygame
import random
import json
from button import Button
from text_box import Text_box

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Numa")
clock = pygame.time.Clock()

# constants
running = True
active_field = None
state = "home"
username = ""
password = ""
greetings = [
   "How can I help with?",
   "Hello! How can I assist you today?",
   "Hi there! I'm here to help if you have any questions."
]
data = {
   "username":username,
   "password":password
}

# text
pygame.font.init()
big_font = pygame.font.Font(None, 43)
font = pygame.font.Font(None, 32)
small = pygame.font.Font(None, 42)
tiny = pygame.font.Font(None, 35)

# colors
white = (255, 255, 255)
gray = (128, 128, 128)
dark_gray = ((169, 169, 169))
blue = (0, 0, 255)
black = (0, 0, 0)

# functions
def chooseGreeting():
   global greetings
   greeting = random.choice(greetings)
   return f"{greeting}"

def save(username, password,filename="account.json"):
  data = {"username": username, "password": password}
  with open(filename, "w") as f:
    json.dump(data,f,indent=4)

def load(filename="account.json"):
   try:
    with open(filename,"r") as f:
      return json.load(f)
   except(FileNotFoundError, json.JSONDecodeError):
    return None

# button functionality
def sendPrompt():
   print("Prompt sent!")

def signIn():
   global state
   state = "sign in"
   return state

def signUp():
   global state
   state = "sign up"
   return state
   
def back_action():
  global state
  if state in ["sign in","sign up"]:
    state = "home"
    
# UI
def continueAction():
  print("continued!")

def drawSignin():
  logo = pygame.Rect(350, 50, 100, 100)
  continue_btn.draw(screen)
  username_box.draw(screen)
  login_btn.draw(screen)
  pygame.draw.rect(screen, dark_gray, logo)
  screen.blit(new_accnt_txt, (200, 470))

def drawSignup():
  logo = pygame.Rect(350, 50, 100, 100)
  continue_btn = Button(250, 520, 300, 50, "Continue", continueAction)
  continue_btn.draw(screen)
  signup_btn.draw(screen)
  username_box.draw(screen)
  password_box.draw(screen)
  pygame.draw.rect(screen, dark_gray, logo)
  screen.blit(sign_up_txt, (200, 240))
  screen.blit(accnt_txt, (220, 480))

# text
welcome_text = big_font.render(chooseGreeting(), True, white)
sign_up_txt = font.render("Create your account", True, gray)
new_accnt_txt = small.render("Don't have an account?", True, black)
accnt_txt = small.render("Already have an account?", True, black)

# text boxes
username_box = Text_box(250, 340, 300, 60)
password_box = Text_box(250, 410, 300, 60)

# buttons
send_btn = Button(600, 480, 70, 70, "↑", sendPrompt)
sign_in_btn = Button(600, 185, 90, 50, "sign in", signIn)
sign_up_btn = Button(700, 185, 90, 50, "sign up", signUp)
continue_btn = Button(250, 410, 300, 50, "Continue", continueAction)
login_btn = Button(540, 460, 100, 50, "Sign up", signUp)
signup_btn = Button(600, 470, 100, 50, "Sign in", signIn)
back_btn = Button(20, 20, 100, 40, "<-", back_action)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
    if state == "home":
      send_btn.handle_event(event)
      sign_in_btn.handle_event(event)
      sign_up_btn.handle_event(event)
      
    if state in ["sign in","sign up"]:
      username_box.handle_event(event)
      password_box.handle_event(event)
      continue_btn.handle_event(event)
      login_btn.handle_event(event)
      signup_btn.handle_event(event)
    back_btn.handle_event(event)
    
  screen.fill(gray)
  if state == "home":
    bg_border = pygame.Rect(0, 0, 800, 200)
    bg = pygame.Rect(0, 185, 800, 415)
    logo = pygame.Rect(35, 50, 50, 50)
    prompt_bar = pygame.Rect(240, 480, 400, 70)
    pygame.draw.rect(screen, gray, bg_border, border_radius=20)
    pygame.draw.rect(screen, dark_gray, bg)
    pygame.draw.rect(screen, dark_gray, logo)
    pygame.draw.rect(screen, gray, prompt_bar, border_radius=20)
    send_btn.draw(screen)
    sign_in_btn.draw(screen)
    sign_up_btn.draw(screen)
    screen.blit(welcome_text, (250, 350))

  elif state == "sign in":
    drawSignin()

  elif state == "sign up":
    drawSignup()
    
  if state in ["sign in","sign up"]:
    back_btn.draw(screen)
    
  pygame.display.flip()
  clock.tick(60)
pygame.quit()
