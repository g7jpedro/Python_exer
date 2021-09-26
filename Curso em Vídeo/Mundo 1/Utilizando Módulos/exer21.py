#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.mixer.init()
pygame.mixer.music.load('op.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass









