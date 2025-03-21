import json
import os

class HotkeyStorage:
  def __init__(self, filepath="hotkeys.json"):
    self.filepath = filepath

  def save_game_keys(self, revive_key, medicine_key, pokeball_key, combo_keys, position):
    data = self._load_data()
    data['game_keys'] = {
      "revive_key": revive_key,
      "medicine_key": medicine_key,
      "pokeball_key": pokeball_key,
      "combo_keys": combo_keys,
      "position": position
    }
    self._save_data(data)

  def load_game_keys(self) -> dict:
    """ Retorna as teclas do jogo.
        - revive_key
        - medicine_key
        - pokeball_key
        - combo_keys
        - position
    """
    data = self._load_data()
    return data.get('game_keys', None)

  def save_macro_keys(self, revive_key, combo_key):
    data = self._load_data()
    data['macro_keys'] = {
      "revive_key": revive_key,
      "combo_key": combo_key
    }
    self._save_data(data)

  def load_macro_keys(self) -> dict:
    """ Retorna as teclas do macro.
        - revive_key
        - combo_key
    """
    data = self._load_data()
    return data.get('macro_keys', None)

  def has_data(self):
    # Verifica se há dados no arquivo
    data = self._load_data()
    return bool(data)  # Retorna True se houver dados no arquivo

  def _load_data(self):
    if not os.path.exists(self.filepath):
      return {}
    with open(self.filepath, 'r') as file:
      return json.load(file)

  def _save_data(self, data):
    with open(self.filepath, 'w') as file:
      json.dump(data, file, indent=4)
