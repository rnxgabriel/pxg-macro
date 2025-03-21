import mouse
import keyboard
import time


class Healing:
  def __init__(self, position, revive_key, medicine_key, pokeball_key):
    self.position = position
    self.revive_key = revive_key
    self.medicine_key = medicine_key
    self.pokeball_key = pokeball_key

  def revive(self):
    if self.position and self.revive_key and self.pokeball_key:
      print("Revive acionado!")
      keyboard.press_and_release(self.pokeball_key)
      mouse.move(self.position[0], self.position[1], absolute=True, duration=0)
      keyboard.press_and_release(self.revive_key)
      mouse.click(button="left")
      keyboard.press_and_release(self.pokeball_key)
      print("Revive concluído.")

  def medicine(self):
    if self.medicine_key:
      print("Usando medicine...")
      keyboard.press_and_release(self.medicine_key)
      print("Medicine usado.")
