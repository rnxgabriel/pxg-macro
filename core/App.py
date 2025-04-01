import threading
import time
import keyboard
import pygetwindow as gw

from core.Macro import Macro

class App(Macro):
  def __init__(self):
    super().__init__()
    # Iniciar o listener em uma thread separada
    self.listener_thread = threading.Thread(target=self.listen_keys, daemon=True)
    self.listener_thread.start()

    self.root.mainloop()

  def is_pokexgames_active(self):
    """Verifica se a janela ativa é o PokeXGames."""
    active_window = gw.getActiveWindow()
    return active_window and "PokeXGames" in active_window.title

  def listen_keys(self):
    while True:
      try:
        # Executa só se a janela do PokeXGames estiver ativa
        if self.is_pokexgames_active():
          if self.macro_revive and keyboard.is_pressed(self.macro_revive):
            self.perform_revive()
            time.sleep(0.3)  # para não repetir várias vezes

          if self.macro_combo and keyboard.is_pressed(self.macro_combo):
            self.perform_combo(self.use_medicine_in_combo.get())
            time.sleep(0.3)  # evitar múltiplas execuções em um único pressionamento
      except Exception as e:
        print(f"Erro na thread do macro: {e}")
      time.sleep(0.05)
