import subprocess as sub 
import os 

def engine():
    sub.run('python PhysiscToolchain-\main.py',shell=True)
    
def Security():
    sub.run('python SecurityToolchain\main.py',shell=True)

def Summrize():
    sub.run('python Summerizer\main.py',shell=True)

def Hacknash():
    if os.name == "Linux":
        sub.run('Hacknash.sh',shell=True) 
