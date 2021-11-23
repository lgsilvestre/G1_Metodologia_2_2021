from pygame.locals import QUIT
from pygame.locals import KEYDOWN
from pygame.locals import MOUSEBUTTONDOWN

import pygame
import sys
import cv2
import re

class text_field():
	
	def __init__(self,x,y,length,width,text,font,size,group,enable=True):
		
		self.x = x
		self.y = y
		self.length = length
		self.width = width
		self.text = text
		self.font = font
		self.size = size
		self.enable = enable
		self.selected = False
		group.append(self)
		
	def draw(self,mode,color):
		
		fuente = pygame.font.SysFont(self.font,self.size)
		texto = fuente.render(self.text,1,color)
		
		pygame.draw.rect(mode,(240,240,240),(self.x,self.y,self.length,self.width))
		mode.blit(texto,(self.x+(self.size/4), self.y+(self.size/4)))
		
		if(self.selected):
			pygame.draw.rect(mode,(255,0,0),(self.x,self.y,self.length-1,self.width-1),2)
		
	def get_status(self,position):
		
		if(self.enable):
			if(position[0] >= self.x and position[0] <= self.x + self.length):
				if(position[1] >= self.y and position[1] <= self.y + self.width):
					self.selected = True
					return
			
		self.selected = False

class button():
	
	def __init__(self,x,y,image,identifier,group):
		
		self.x = x
		self.y = y
		self.image = pygame.image.load(image)
		self.identifier = identifier
		self.length = self.image.get_height()
		self.width = self.image.get_width()
		group.append(self)
		
	def draw(self,mode):
		
		mode.blit(self.image,(self.x,self.y))
		
	def get_status(self,position):
		
		if(position[0] >= self.x and position[0] <= self.x + self.width):
			if(position[1] >= self.y and position[1] <= self.y + self.length):
				return True
			
		return False

def camara(mode):
	
	mode.fill((0,0,0))
	video = cv2.VideoCapture(1, cv2.CAP_DSHOW)
	
	running = True
	
	while(running):
		
		frame = video.read()[1]
		frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
		
		surface = pygame.surfarray.make_surface(frame)
		surface = pygame.transform.rotate(surface,270)
		
		salida = pygame.transform.scale(surface,(800,450))
		mode.blit(salida,(0,0))
		
		for evento in pygame.event.get():
			
			if(evento.type == QUIT):
				running = False
				pygame.quit()
				sys.exit()
			
		pygame.display.update()

def login(mode):
	
	buttons = []
	text_fields = []
	
	fondo = pygame.image.load("fondo_login.png")
	mode.blit(fondo,(0,0))
	
	user = pygame.image.load("user.png")
	mode.blit(user,(310,95))
	
	modo = " Inicio de Sesión: Alumno / Profesor"
	modo_actual = "alumno"
	
	texto1 = text_field(280, 45, 240, 30, modo, "Arial", 18, text_fields, False)
	texto1.draw(mode,(0,0,0))
	
	texto2 = text_field(280, 305, 240, 30, "", "Arial", 18, text_fields)
	texto2.draw(mode,(0,0,0))
	
	texto3 = text_field(280, 365, 240, 30, "", "Arial", 18, text_fields)
	texto3.draw(mode,(0,0,0))
	
	boton1 = button(315, 425, "login.png", "login", buttons)
	boton1.draw(mode)
	
	boton2 = button(230, 505, "empresa.png", "empresa", buttons)
	boton2.draw(mode)
	
	boton3 = button(435, 505, "alumno.png", "alumno", buttons)
	boton3.draw(mode)
	
	password = ""
	running = True
	
	while(running):
		
		for evento in pygame.event.get():
			
			if(evento.type == MOUSEBUTTONDOWN and evento.button == 1):
				
				for botones in buttons:
					
					if(botones.get_status(evento.pos)):
						
						if(botones.identifier == "empresa"):
							texto1.text = "        Inicio de Sesión: Empresa"
							texto1.draw(mode,(0,0,0))
							modo_actual = "empresa"
							
						if(botones.identifier == "alumno"):
							texto1.text = " Inicio de Sesión: Alumno / Profesor"
							texto1.draw(mode,(0,0,0))
							modo_actual = "alumno"
							
						if(botones.identifier == "login"):
							print(modo_actual)
							print(texto2.text)
							print(password)
							camara(mode)
							
							mode.blit(fondo,(0,0))
							mode.blit(user,(310,95))
							
							password = ""
							
							for x in buttons:
								x.draw(mode)
								
							for y in text_fields:
								
								if(y.enable):
									y.text = ""
									
								y.draw(mode,(0,0,0))
					
				for entradas in text_fields:
					entradas.get_status(evento.pos)
			
			for seleccionado in text_fields:
				
				if(seleccionado.selected):
					
					if(evento.type == KEYDOWN):
				
						caracter = evento.unicode
						
						if(caracter == '\x08'):
							
							if(seleccionado == texto3):
								password = password[:-1]
								
							seleccionado.text = seleccionado.text[:-1]
							
						else:
							
							caracter_valido = re.search('[a-zA-Z0-9 ]', caracter)
							
							if caracter_valido is not None:
								
								if(seleccionado == texto3):
									
									if(len(seleccionado.text) < 29):
										seleccionado.text += "*"
										password += caracter
										
								else:
									
									if(len(seleccionado.text) < 29):
										seleccionado.text += caracter
								
				seleccionado.draw(mode,(0,0,0))
			
			if(evento.type == QUIT):
				running = False
			
		pygame.display.update()

if __name__ == '__main__':
	
	pygame.init()
	
	mode = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Facial Recognition")
	
	login(mode)
	
	pygame.quit()
	cv2.destroyAllWindows()