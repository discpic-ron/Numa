import pygame
import random
from button import Button

# Constants
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ChatGPT in python")
clock = pygame.time.Clock()
running = True
greetings = [
    "How can I help with?",
    "Hello! How can I assist you today?",
    "Hi there! I'm here to help if you have any questions."
]
state = "home"

# text
pygame.font.init()
font = pygame.font.Font(None, 32)
small = pygame.font.Font(None,42)
tiny = pygame.font.Font(None,35)

# colors
white = (255, 255, 255)
gray = (128, 128, 128)
dark_gray = ((169, 169, 169))
blue = (0,0,255)
black = (0,0,0)

# functions
def chooseGreeting():
    global greetings
    greeting = random.choice(greetings)
    return f"{greeting}"
    
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
    
def continueAction():
    print("continued!")

def drawSignin():
    logo = pygame.Rect(350, 50, 100, 100)
    continue_btn.draw(screen)
    pygame.draw.rect(screen, dark_gray, logo)
    pygame.draw.rect(screen, dark_gray, username_field,border_radius=20)
    login_btn.draw(screen)
    screen.blit(new_accnt_txt, (200, 470))
    screen.blit(username_txt, (260, 340))
    
def drawSignup():
    logo = pygame.Rect(350, 50, 100, 100)
    continue_btn = Button(250, 520, 300, 50, "Continue", continueAction)
    continue_btn.draw(screen)
    signup_btn.draw(screen)
    username_field = pygame.Rect(250, 300, 300, 60)
    pygame.draw.rect(screen, dark_gray, logo)
    pygame.draw.rect(screen, dark_gray, username_field,border_radius=20)
    pygame.draw.rect(screen, dark_gray, password_field,border_radius=20)
    screen.blit(sign_up_txt, (200, 240))
    screen.blit(accnt_txt, (220, 480))
    screen.blit(username_txt, (260, 300))
    screen.blit(password_txt, (260, 400))

# text
welcome_text_surface = font.render(chooseGreeting(), True, white)
password_txt = tiny.render("Enter password", True, gray)
sign_up_txt = font.render("Create your account", True, gray)
new_accnt_txt = small.render("Don't have an account?", True, black)
accnt_txt = small.render("Already have and account?", True, black)
username_txt = tiny.render("Enter username", True, gray)

# rects
username_field = pygame.Rect(250, 340, 300, 60)
password_field = pygame.Rect(250, 400, 300, 60)

# buttons
send_btn = Button(600,480,70,70,"↑",sendPrompt)
sign_in_btn = Button(600,185,70,70,"sign in",signIn)
sign_up_btn = Button(700,185,70,70,"sign up",signUp)
continue_btn = Button(250, 410, 300, 50, "Continue", continueAction)
login_btn = Button(540,460,100,50,"Sign up",signUp)
signup_btn = Button(600,470,100,50,"Sign in",signIn)

while running:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        send_btn.handle_event(event)
        sign_in_btn.handle_event(event)
        sign_up_btn.handle_event(event)
        login_btn.handle_event(event)
        signup_btn.handle_event(event)

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
        screen.blit(welcome_text_surface, (250, 350))

  elif state == "sign in":
    drawSignin()

  elif state == "sign up":
    drawSignup()

  pygame.display.flip()
  clock.tick(60)
pygame.quit()
