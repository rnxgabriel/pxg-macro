import tkinter as tk
import keyboard
import mouse

from core.Hotkeys import Hotkeys
from ui.Style import Style


class Ui(Style, Hotkeys):
  def __init__(self):
    Hotkeys.__init__(self)
    Style.__init__(self)
    self.root = tk.Tk()
    self.root.title("Pxg-macro")
    self.root.geometry("360x400")
    self.root.config(bg=self.BG)
    self.root.resizable(False, False)

    self.use_medicine_in_combo = tk.BooleanVar(value=False)

    self.main_frame = tk.Frame(self.root, bg=self.BG)
    self.main_frame.pack(pady=10, padx=10)

    self.left_frame = tk.Frame(self.main_frame, bg=self.BG)
    self.left_frame.grid(row=0, column=0, padx=10)

    self.create_label("Teclas in-game:", self.left_frame, row=0, column=0)

    self.create_button("Configurar Revive", self.left_frame, self.set_game_revive_key, 1)
    self.label_revive = self.create_label(f"Tecla: {self.game_revive or ''}", self.left_frame, row=1, column=1)

    self.create_button("Configurar Medicine", self.left_frame, self.set_game_medicine_key, 2)
    self.label_medicine = self.create_label(f"Tecla: {self.game_medicine or ''}", self.left_frame, row=2, column=1)

    self.create_button("Configurar Pokeball", self.left_frame, self.set_game_pokeball_key, 3)
    self.label_pokeball = self.create_label(f"Tecla: {self.game_pokeball or ''}", self.left_frame, row=3, column=1)

    self.create_button("Configurar Combos", self.left_frame, self.set_game_combo_keys, 4)
    self.create_label("Enter para salvar o combo", self.left_frame, row=5)
    self.label_combos = self.create_label(f"Teclas: {self.game_combo or ''}", self.left_frame, row=4, column=1)

    self.create_button("Configurar Posição", self.left_frame, self.set_position, 6)
    self.label_position = self.create_label(f"Posição: {self.position or ''}", self.left_frame, row=6, column=1)

    self.create_label("Teclas do Macro:", self.left_frame, row=7)

    self.create_button("Ativar Revive", self.left_frame, self.set_macro_revive, row=8)
    self.label_macro_revive = self.create_label(f"Tecla: {self.macro_revive or ''}", self.left_frame, row=8, column=1)

    self.create_button("Ativar Combo", self.left_frame, self.set_macro_combo, row=9)
    self.label_macro_combo = self.create_label(f"Tecla: {self.macro_combo or ''}", self.left_frame, row=9, column=1)

    # Checkbox
    self.checkbox = tk.Checkbutton(
      self.left_frame,
      text="Usar medicine no combo",
      variable=self.use_medicine_in_combo,
      onvalue=True,
      offvalue=False,
      bg=self.BG,
      fg="white",
      activebackground=self.BG,
      selectcolor=self.BG,
      font=("Arial", 9, "bold")
    )
    self.checkbox.grid(row=10, column=0, pady=10, sticky="w")

  def set_game_revive_key(self):
    self.game_revive = self.wait_for_keypress()
    self.label_revive.config(text=f"Tecla: {self.game_revive}")

  def set_game_medicine_key(self):
    self.game_medicine = self.wait_for_keypress()
    self.label_medicine.config(text=f"Tecla: {self.game_medicine}")

  def set_game_pokeball_key(self):
    self.game_pokeball = self.wait_for_keypress()
    self.label_pokeball.config(text=f"Tecla: {self.game_pokeball}")

  def set_game_combo_keys(self):
    keys = []
    while True:
      key = self.wait_for_keypress()
      if key in ["esc", "enter"]:
        break
      if key not in keys:
        keys.append(key)
    self.game_combo = keys
    self.label_combos.config(text=f"Teclas: {', '.join(keys)}")

  def set_position(self):
    mouse.wait(button="left")
    self.position = mouse.get_position()
    self.label_position.config(text=f"Posição: {self.position}")

  def set_macro_revive(self):
    self.macro_revive = self.wait_for_keypress()
    self.label_macro_revive.config(text=f"Tecla: {self.macro_revive}")

  def set_macro_combo(self):
    self.macro_combo = self.wait_for_keypress()
    self.label_macro_combo.config(text=f"Tecla: {self.macro_combo}")

  def wait_for_keypress(self):
    """Aguarda a tecla pressionada e retorna o valor"""
    key = keyboard.read_event().name
    return key
