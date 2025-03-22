import keyboard
import mouse

from core.HotkeyStorage import HotkeyStorage

class Hotkeys:
  def __init__(self):
    self.storage = HotkeyStorage()
    self._position = None

    self._game_revive = None
    self._game_medicine = None
    self._game_pokeball = None
    self._game_combo = []

    self._macro_revive = None
    self._macro_combo = None

  @property
  def game_revive(self):
    return self._game_revive

  @game_revive.setter
  def game_revive(self, value):
    self._game_revive = value

  @property
  def game_medicine(self):
    return self._game_medicine

  @game_medicine.setter
  def game_medicine(self, value):
    self._game_medicine = value

  @property
  def game_pokeball(self):
    return self._game_pokeball

  @game_pokeball.setter
  def game_pokeball(self, value):
    self._game_pokeball = value

  @property
  def game_combo(self):
    return self._game_combo

  @game_combo.setter
  def game_combo(self, value: list[str | int]):
    self._game_combo = value

  @property
  def macro_revive(self):
    return self._macro_revive

  @macro_revive.setter
  def macro_revive(self, value):
    self._macro_revive = value

  @property
  def macro_combo(self):
    return self._macro_combo

  @macro_combo.setter
  def macro_combo(self, value):
    self._macro_combo = value

  @property
  def position(self):
    return self._position

  @position.setter
  def position(self, value):
    self._position = value

  def save_config(self):
    """Salva as configurações no storage."""
    self.storage.save_game_keys(
      self.game_revive,
      self.game_medicine,
      self.game_pokeball,
      self.game_combo,
      self.position
    )
    self.storage.save_macro_keys(
      self.macro_revive,
      self.macro_combo
    )

  def load_config(self):
    """Carrega as configurações salvas."""
    game_keys = self.storage.load_game_keys()
    if game_keys:
      (self.game_revive,
      self.game_medicine,
      self.game_pokeball,
      self.game_combo,
      self.position) = game_keys
    macro_keys = self.storage.load_macro_keys()
    if macro_keys:
      (self.macro_revive, self.macro_combo) = macro_keys
