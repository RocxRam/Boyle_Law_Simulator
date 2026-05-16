import pygame
from settings import *
from molecule import Molecule
import random
from slider import Slider
from gas_law import calculate_pressure

pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Boyle's Law Simulator")

clock=pygame.time.Clock()
loop=True

temp_slider=Slider(50,380,300,1,1000,300)
moles_slider=Slider(50,410,300,0.5,7,1)
volume_slider=Slider(50,440,300,10,100,50)

piston_y=CHAMBER_Y+50
molecules=[]
moles=1
scale=molecules_per_mole
temp=300
volume=50

for i in range(moles*scale):
    x=random.randint(CHAMBER_X+20,CHAMBER_X+CHAMBER_WIDTH-20)
    y=random.randint(int(piston_y+PISTON_HEIGHT+20),CHAMBER_Y+CHAMBER_HEIGHT-20)
    molecule=Molecule(x,y,temp)
    molecules.append(molecule)

font = pygame.font.SysFont("Arial",18)
title_font = pygame.font.SysFont("Segoe UI",20,bold=True)
old_temp=300
while loop:
    for event in pygame.event.get():
        temp_slider.handle_event(event)
        moles_slider.handle_event(event)
        volume_slider.handle_event(event)
        if event.type==pygame.QUIT:
            loop=False
    screen.fill((18,18,24))
    
    title_text = title_font.render("Ideal Gas Simulator(Boyle's law)",True,(255,255,255))
    screen.blit(title_text,(120,20))
    pygame.draw.rect(screen,(230,230,230),(CHAMBER_X,CHAMBER_Y,CHAMBER_WIDTH,CHAMBER_HEIGHT),3)
    pygame.draw.rect(screen,(160,160,160),(CHAMBER_X,piston_y,CHAMBER_WIDTH,PISTON_HEIGHT),border_radius=15)
    pygame.draw.rect(screen,(210,210,210),(0,350,500,120),border_radius=15)

    temp_slider.draw(screen)
    moles_slider.draw(screen)
    volume_slider.draw(screen)
    
    temp=temp_slider.get_value()
    moles=moles_slider.get_value()
    volume=volume_slider.get_value()
    pressure=calculate_pressure(volume,moles,temp)
    
    temp_text=font.render("T",True,(30,40,40))
    screen.blit(temp_text,(25,370))
    tempval_text=font.render(f"{temp:.1f}",True,(10,10,10))
    screen.blit(tempval_text,(400,370))
    mole_text=font.render("n",True,(30,30,40))
    screen.blit(mole_text,(25,400))
    moleval_text=font.render(f"{moles:.2f}",True,(10,10,10))
    screen.blit(moleval_text,(400,400))
    volume_text=font.render("V",True,(30,40,40))
    screen.blit(volume_text,(25,430))
    volumeval_text=font.render(f"{volume:.0f}",True,(10,10,10))
    screen.blit(volumeval_text,(400,430))
    pressure_text=font.render(f"Pressure={pressure:.1f}",True,(230,230,230))
    screen.blit(pressure_text,(20,80))

    gas_height=volume/100*(CHAMBER_HEIGHT-PISTON_HEIGHT)
    target_piston_y=(CHAMBER_Y+CHAMBER_HEIGHT-PISTON_HEIGHT-gas_height)
    MIN_GAS_HEIGHT=40
    target_piston_y=min(target_piston_y,CHAMBER_Y+CHAMBER_HEIGHT-PISTON_HEIGHT-MIN_GAS_HEIGHT)
    target_piston_y=max(target_piston_y,CHAMBER_Y)
    piston_y+=(target_piston_y-piston_y)*0.08

    target_molecules=int(moles*scale)
    while len(molecules)<target_molecules:
        x=random.randint(CHAMBER_X+20,CHAMBER_X+CHAMBER_WIDTH-20)
        y=random.randint(int(piston_y+PISTON_HEIGHT+20),CHAMBER_Y+CHAMBER_HEIGHT-20)
        molecule=Molecule(x,y,temp)
        molecules.append(molecule)
    while len(molecules)>target_molecules:
        molecules.pop()
        
    if old_temp!=temp:
        for molecule in molecules:
            molecule.set_temperature(temp,old_temp)
        old_temp=temp
    for molecule in molecules:
        molecule.move(piston_y)
    for i in range(len(molecules)):
        for j in range(i+1,len(molecules)):
            molecules[i].collide(molecules[j])
    for molecule in molecules:
        molecule.draw(screen)
        
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
