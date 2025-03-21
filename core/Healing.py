import pyautogui
import time
import mouse
import keyboard


class Healing:
  def __init__(self, revive_key, medicine_key, pokeball_key, position):
    """
    position: posição (x, y) onde o mouse deve clicar no revive.
    revive_key: tecla do jogo para o revive.
    medicine_key: tecla do jogo para o medicine.
    pokeball_key: tecla do jogo para enviar o Pokémon.
    """
    self.position = position
    self.revive_key = revive_key
    self.medicine_key = medicine_key
    self.pokeball_key = pokeball_key

  def revive(self):
    """Executa o processo de reviver o Pokémon."""
    if self.position and self.revive_key and self.pokeball_key:
      print("⏳ Iniciando revive...")
      current_mouse_pos = pyautogui.position()

      keyboard.press_and_release(self.pokeball_key)
      time.sleep(0.2)

      # Movimentação suave do mouse
      pyautogui.moveTo(self.position[0], self.position[1], duration=0)
      time.sleep(0.1)

      keyboard.press_and_release(self.revive_key)
      time.sleep(0.2)
      mouse.click(button="left")
      time.sleep(0.2)

      keyboard.press_and_release(self.pokeball_key)
      time.sleep(0.2)

      # Opcional: volta o mouse para onde estava
      pyautogui.moveTo(current_mouse_pos[0], current_mouse_pos[1], duration=0)

      print("✅ Revive concluído.")
    else:
      print("⚠️ Configuração incompleta. Revive não pode ser executado.")

  def medicine(self):
    """Executa o uso de medicine."""
    if self.medicine_key:
      print("Usando medicine...")
      keyboard.press_and_release(self.medicine_key)
      time.sleep(0.2)
      print("✅ Medicine usado.")
    else:
      print("⚠️ Tecla de medicine não configurada.")
