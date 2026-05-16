import pygame

class Slider:

    def __init__(self,x,y,width,min_val,max_val,start_val):
        self.x=x
        self.y=y
        self.width=width
        self.min_val=min_val
        self.max_val=max_val
        self.value=start_val
        self.radius=5
        self.dragging=False
        self.knob_x=self.get_position()

    def get_position(self):
        ratio=((self.value-self.min_val)/(self.max_val-self.min_val))
        return self.x+ratio*self.width

    def draw(self,screen):
        pygame.draw.line(screen,(90,90,90),(self.x,self.y),(self.x+self.width,self.y),6)
        pygame.draw.circle(screen,(0,180,255),(int(self.knob_x),self.y),self.radius)

    def handle_event(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            distance=((mouse_x-self.knob_x)**2+(mouse_y-self.y)**2)**0.5
            if distance<=self.radius:
                self.dragging=True
        if event.type==pygame.MOUSEBUTTONUP:
            self.dragging=False
        if event.type==pygame.MOUSEMOTION and self.dragging:
            mouse_x=pygame.mouse.get_pos()[0]
            self.knob_x=max(self.x,min(mouse_x,self.x+self.width))
            ratio=((self.knob_x-self.x)/self.width)
            self.value=self.min_val+ratio*(self.max_val-self.min_val)

    def get_value(self):
        return self.value
