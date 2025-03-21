import mouse
import keyboard
import time

from core.Configure import Configure
from core.Healing import Healing


class Attack:
  def __init__(self, healingInstance: Healing, combo_keys: list[keyboard._Key], medicine = False):
    self.healingInstance = healingInstance
    self.combo_keys = combo_keys
    self.medicine = medicine
    pass

  def use_medicine(self):
    print("Deseja utilizar medicine ? [Y/N]")
    if(keyboard.read_key() == 'y' or keyboard.read_key() == 'Y'):
      self.medicine = True
    pass

  def use_combo(self):
    for i in self.combo_keys:
      if self.medicine: self.healingInstance.medicine()
      keyboard.press_and_release(i)
      time.sleep(0.2)
    pass
  
  pass