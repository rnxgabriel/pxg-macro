import tkinter as tk
from typing import Literal



class Style():
  def __init__(self):
    self.BG = "#8B0000"
    self.BTN_BG = "#B22222"

  def create_label(self, text: str, parent, row: int, column=0, justify: Literal['left', 'center', 'right'] = 'center') -> tk.Label:
    label = tk.Label(
      parent,
      text=text,
      bg=self.BG,
      fg="white",
      justify=justify,
      font=("Arial", 8, "bold")
    )
    label.grid(row=row, column=column, pady=2, padx=2)
    return label

  def create_button(self, text: str, parent_frame, command, row: int, column=0):
    btn = tk.Button(
      parent_frame,
      text=text,
      font=("Arial", 8, "bold"),
      fg="white",
      bg=self.BTN_BG,
      width=20,
      height=1,
      command=command
    )
    btn.grid(row=row, column=column, pady=4)
    return btn
