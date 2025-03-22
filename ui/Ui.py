import tkinter as tk

import keyboard
import mouse

from core.Hotkeys import Hotkeys

bg = "#8B0000"
button_bg = "#B22222"

class Ui(Hotkeys):
  def __init__(self):
    super().__init__()
    # self.healing = Healing()
    # self.attack = Attack()
    self.root = tk.Tk()
    self.root.title("Pxg-macro")
    self.root.geometry("350x300")
    self.root.config(bg=bg)  # Fundo vermelho escuro

    # Frame principal
    self.main_frame = tk.Frame(self.root, bg=bg)
    self.main_frame.pack(pady=4)

    # Colunas: Botões e Exibição das configurações
    self.button_frame = tk.Frame(self.main_frame, bg=bg)
    self.button_frame.grid(row=0, column=0, padx=4)

    self.info_frame = tk.Frame(self.main_frame, bg=bg)
    self.info_frame.grid(row=0, column=1, padx=4)


  def set_game_revive_key(self): self.game_revive = keyboard.read_key()

  def set_game_medicine_key(self): self.game_medicine = keyboard.read_key()

  def set_game_pokeball_key(self): self.game_pokeball = keyboard.read_key()

  def set_game_combo_keys(self):
    keys = []
    while True:
      key = keyboard.read_key()
      if key == "esc" or key == "enter": break
      keys.append(key)
    self.game_combo = keys

  def set_position(self):
    mouse.wait(button="left")
    self.position = mouse.get_position

  def set_macro_revive(self):
    self.macro_revive = keyboard.read_key()
    pass

  def set_macro_combo(self):
    self.macro_combo = keyboard.read_key()
    pass

  def loop(self):
    self.root.mainloop()

  def create_button(self, text:str, command, row:int, column=0):
    button = tk.Button(
      self.button_frame,
      text=text,
      font=("Arial",8, "bold")
      , fg="white",
      bg=button_bg,
      width=24,
      height=2,
      command=command)
    button.grid(row=row, column=column, pady=8)
