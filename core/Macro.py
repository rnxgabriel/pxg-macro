import time
import mouse
import keyboard
import pyautogui

from core.Hotkeys import Hotkeys


class Macro:
  def __init__(self, hotkeys: Hotkeys ):
    self.hotkeys = hotkeys

  def execute_revive(self):
    """
    Executa o processo de reviver o Pokémon.
    """
    if self.hotkeys.position and self.hotkeys.game_revive and self.hotkeys.game_pokeball:
      print("[LOG] ⏳ Iniciando revive...")
      current_mouse_pos = pyautogui.position()

      keyboard.press_and_release(self.hotkeys.game_pokeball)
      time.sleep(0.2)

      pyautogui.moveTo(self.hotkeys.position[0], self.hotkeys.position[1], duration=0)
      time.sleep(0.1)

      keyboard.press_and_release(self.hotkeys.game_revive)
      time.sleep(0.2)
      mouse.click(button="left")
      time.sleep(0.2)

      keyboard.press_and_release(self.hotkeys.game_pokeball)
      time.sleep(0.2)

      pyautogui.moveTo(current_mouse_pos[0], current_mouse_pos[1], duration=0)

      print("[LOG] ✅ Revive concluído.")
    else:
      print("[LOG] ⚠️ Configuração incompleta. Revive não pode ser executado.")

  def execute_combo(self, medicine=False):
    """
    Executa o combo, pressionando cada tecla da lista combo_keys, opcionalmente usando medicine.
    """
    print(f"⏳ Executando combo...")
    if medicine: self.execute_medicine()
    for key in self.hotkeys.game_combo:
      keyboard.press_and_release(key)
      time.sleep(0.6)
    self.execute_revive()
    print("✅ Combo finalizado.")

  def execute_medicine(self):
    """
    Executa o uso de medicine
    """
    if self.hotkeys.game_medicine is not None:
      keyboard.press_and_release(self.hotkeys.game_medicine)
      print("[LOG] ✅ Medicine Utilizado.")
      return
    print("[LOG] ⚠️ Configuração incompleta. Medicine nao pode ser executado.")
