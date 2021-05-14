# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#Part 1: Greet Template
def greet(fname, greeting = 'Hallo'):
    print(greeting, fname+'!')
greet('Frans', 'Yo')

#Part 2: Force
def force(mass, body = 'earth'):
    gravity = 9.8
    if body == 'sun':
        gravity = 274.0
    if body == 'jupiter':
        gravity = 24.9
    if body == 'neptune':
        gravity = 11.2
    if body == 'saturn':
        gravity = 10.4
    if body == 'uranus':
        gravity = 8.9
    if body == 'venus':
        gravity = 8.9
    if body == 'mars':
        gravity = 3.7
    if body == 'mercury':
        gravity = 3.7
    if body == 'moon':
        gravity = 1.6
    if body == 'pluto':
        gravity = 3.7
    print(mass*gravity)
force(2, '')

#Part 3: Gravity
def pull(m1, m2, d):
    print((6.674*10**-11)*((m1*m2)/d**2))
pull(800, 1500, 3)
pull(0.1, 5.972*(10**24), 6.371*(10**6))
