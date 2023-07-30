from gpiozero import Motor
import time
coil1 = Motor(forward=18,backward=23, pwm=False)
coil2 = Motor(forward=24,backward=17, pwm=False)
forward_seq = ['FF','BF','BB','FB']
reverse_seq = list(forward_seq)
reverse_seq.reverse()
def forward(delay, steps):
  for i in range(steps):
    for step in forward_seq:
      set_step(step)
      time.sleep(delay)
def backwards(delay, steps):
  for i in range(steps):
    for step in reverse_seq:
      set_step(step)
      time.sleep(delay)
def set_step(step):
  if step == 'S':
    coil1.stop()
    coil2.stop()
  else:
    if step[0] == 'F':
      coil1.forward()
    else:
      coil.backward()
    if step[1] == 'F':
      coil2.forward()
    else:
      coil2.backward()
while True:
  set_setup('S')
  delay = input("Jaki odstęp pomiędzy krokami (milisekundy)?")
  steps = input("Ile kroków do przodu?")
  forward(int(delay)/1000.0, int(steps))
  set_step('S')
  steps = input("Ile kroków do tyłu?")
  backwards(int(delay)/1000.0, int(steps))
