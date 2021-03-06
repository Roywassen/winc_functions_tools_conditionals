# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1: Greet template
def greet(name, template = 'Hello, <name>!'):
    greet = template.replace('<name>', name)
    return greet

# Part 2: Force
def force (mass, body = 'earth'):
    gravity = { 'sun' : 274, 
                'jupiter' : 24.9, 
                'neptune' : 11.2, 
                'saturn' : 10.4,
                'earth' : 9.8,
                'uranus' : 274,
                'venus' : 8.9,
                'mars' : 3.7,
                'mercury' : 3.7,
                'moon' : 1.6, 
                'pluto' : 0.6
                }
    force = mass * gravity[body]
    return round(force, 1)

#Part 3: Gravity
def pull (m1, m2, d):
    pull = 6.674e-11 * ((m1 * m2) / d**2)
    return pull
