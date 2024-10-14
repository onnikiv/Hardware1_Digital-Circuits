from machine import Pin
import time

class Light:
    def __init__(self, delay, button, led):
        self.delay = delay
        self.btn = Pin(button, Pin.IN, Pin.PULL_UP)
        self.led = Pin(led, Pin.OUT)
        self.state = self.off
        
    def execute(self):
        self.state()

    def off(self):
        self.led.off()
        time.sleep(self.delay)
        print(f"State: OFF, --> button output: {self.btn.value()}")
        
        if self.btn.value() == 0:
            self.state = self.onw
        else:
            self.state = self.off
        
    def onw(self):
        self.led.on()
        time.sleep(self.delay)
        print(f"State: ONW, --> button output: {self.btn.value()}")
        
        if self.btn.value() == 1:
            self.state = self.on
        else:
            self.state = self.onw
        
    def on(self):
        self.led.on()
        time.sleep(self.delay)
        print(f"State: ON, --> button output: {self.btn.value()}")
        
        if self.btn.value() == 1:
            self.state = self.on
        else:
            self.state = self.offw
        
    def offw(self):
        self.led.off()
        time.sleep(self.delay)
        print(f"State: OFFW, --> button output: {self.btn.value()}")
        
        if self.btn.value() == 1:
            self.state = self.off
        else:
            self.state = self.offw

asm = Light(0.05, 7, 20)

while True:
    asm.execute()
