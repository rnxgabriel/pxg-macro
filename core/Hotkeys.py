import os
import json
import sys


def resource_path(relative_path):
  """Retorna o caminho absoluto, funcionando tanto com PyInstaller quanto em dev."""
  if hasattr(sys, '_MEIPASS'):
      return os.path.join(sys._MEIPASS, relative_path) # type: ignore
  return os.path.join(os.path.abspath("."), relative_path)


class Hotkeys:
  def __init__(self):
    self.path = './macro-config/hotkeys.json'
    self._position = None

    self._game_revive = None
    self._game_medicine = None
    self._game_pokeball = None
    self._game_combo = []

    self._macro_revive = None
    self._macro_combo = None
    self.load_config()

  @property
  def game_revive(self):
    return self._game_revive

  @game_revive.setter
  def game_revive(self, value):
    self._game_revive = value
    self.save_config()

  @property
  def game_medicine(self):
    return self._game_medicine

  @game_medicine.setter
  def game_medicine(self, value):
    self._game_medicine = value
    self.save_config()

  @property
  def game_pokeball(self):
    return self._game_pokeball

  @game_pokeball.setter
  def game_pokeball(self, value):
    self._game_pokeball = value
    self.save_config()

  @property
  def game_combo(self):
    return self._game_combo

  @game_combo.setter
  def game_combo(self, value: list[str | int]):
    self._game_combo = value
    self.save_config()

  @property
  def macro_revive(self):
    return self._macro_revive

  @macro_revive.setter
  def macro_revive(self, value):
    self._macro_revive = value
    self.save_config()

  @property
  def macro_combo(self):
    return self._macro_combo

  @macro_combo.setter
  def macro_combo(self, value):
    self._macro_combo = value
    self.save_config()

  @property
  def position(self):
    return self._position

  @position.setter
  def position(self, value):
    self._position = value
    self.save_config()

  def load_config(self):
    """Carrega as configurações de um arquivo JSON."""
    try:
        with open(self.path, "r") as file:
            self.config = json.load(file)
    except FileNotFoundError:
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        self.config = {}

    # Carregar as configurações individuais
    self._game_medicine = self.config.get("game_medicine")
    self._game_revive = self.config.get("game_revive")
    self._game_pokeball = self.config.get("game_pokeball")
    self._game_combo = self.config.get("game_combo", [])
    self._position = self.config.get("position")
    self._macro_revive = self.config.get("macro_revive")
    self._macro_combo = self.config.get("macro_combo")

  def save_config(self):
    """Salva as configurações no arquivo JSON."""
    self.config["game_revive"] = self.game_revive
    self.config["game_medicine"] = self.game_medicine
    self.config["game_pokeball"] = self.game_pokeball
    self.config["game_combo"] = self.game_combo
    self.config["position"] = self.position
    self.config["macro_revive"] = self.macro_revive
    self.config["macro_combo"] = self.macro_combo

    with open(self.path, "w") as file:
      json.dump(self.config, file, indent=4)