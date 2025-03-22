import mouse
import keyboard
import time

from core.Healing import Healing

class Attack:
  """
  Classe responsável por executar combos e acionar o uso de medicine durante o ataque.
  """
  def __init__(self, healing_instance: Healing, combo_keys: list, medicine=False):
    self.healing_instance = healing_instance
    self.combo_keys = combo_keys
    self.medicine = medicine

  def perform_combo(self):
    """
    Executa o combo, pressionando cada tecla da lista combo_keys, opcionalmente usando medicine.
    """
    print(f"⏳ Executando combo...")
    self.healing_instance.medicine() if self.medicine else None
    for key in self.combo_keys:
      if key == self.combo_keys[1]: self.healing_instance.medicine()
      keyboard.press_and_release(key)
      time.sleep(0.6)
    self.healing_instance.revive()
    print("✅ Combo finalizado.")
