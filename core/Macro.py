import time
import keyboard
import win32api  # type: ignore
import win32con  # type: ignore

from ui.Ui import Ui

class Macro(Ui):
  def __init__(self):
    super().__init__()

  def perform_combo(self, use_medicine_in_combo: bool):
    """
    Executa o combo, pressionando cada tecla da lista combo_keys, opcionalmente usando medicine.
    """
    keyboard.press_and_release("alt+1")
    for key in self.game_combo:
      if use_medicine_in_combo:
        self.perform_medicine()
      keyboard.press_and_release(key)
      time.sleep(0.6)
    self.perform_revive()
    keyboard.press_and_release("alt+3")

  def perform_medicine(self):
    if self.game_medicine:
      keyboard.press_and_release(self.game_medicine)

  def perform_revive(self):
    """Executa o processo de reviver o Pokémon (irá mover o cursor para clicar na posição)."""
    if self.position and self.game_revive and self.game_pokeball:
      current_pos = win32api.GetCursorPos()
      keyboard.press_and_release(self.game_pokeball)
      time.sleep(0.2)

      keyboard.press_and_release(self.game_revive)
      time.sleep(0.3)

      x, y = self.position
      # Move o cursor para a posição salva e clica
      win32api.SetCursorPos((x, y))
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
      time.sleep(0.2)

      keyboard.press_and_release(self.game_pokeball)
      win32api.SetCursorPos(current_pos)
      time.sleep(0.2)
