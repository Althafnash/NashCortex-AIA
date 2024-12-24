import subprocess as sub 

def engine():
    sub.run('python PhysiscToolchain-\main.py',shell=True)
    
def Security():
    sub.run('python SecurityToolchain\main.py',shell=True)