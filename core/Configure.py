import mouse
import keyboard

class Configure:
  def __init__(self):
    self.game_confirmed = False
    self.position = None
    self.game_revive_key = None
    self.game_medicine_key = None
    self.game_pokeball_key = None
    self.game_combo_keys: list[keyboard._Key] = []

    self.macro_confirmed = False
    self.macro_revive_key = 0
    self.macro_combo_key = 0

  def set_game_keys(self):
    while not self.game_confirmed:
      print("Pressione a tecla do jogo para o revive:")
      self.game_revive_key = keyboard.read_key()

      print("Clique na posição que deseja salvar para o revive.")
      mouse.wait(button="left")
      self.position = mouse.get_position()

      print("Pressione a tecla do jogo para o medicine:")
      self.game_medicine_key = keyboard.read_key()

      print("Pressione a tecla do jogo para enviar o pokemon:")
      self.game_pokeball_key = keyboard.read_key()

      print("Pressione as teclas do jogo que deseja definir para o combo:")
      print("Aperte Enter para finalizar a configuração.")
      while True:
        key = keyboard.read_key()
        if key == 'enter':
          break
        self.game_combo_keys.append(key)

      print("Está tudo certo ? [Y/N]")
      confirmed = keyboard.read_key()
      if confirmed == 'y' or confirmed == 'Y':
        self.confirmed = True
      else:
        print("Reiniciando configuração...")

  def get_game_keys(self):
    """ Retorna as configurações do jogo. Nesta sequencia:
      - revive_key
      - medicine_key
      - pokeball_key
      - combo_keys
      - position
    """
    return self.game_revive_key, self.game_medicine_key, self.game_pokeball_key, self.game_combo_keys, self.position

  def set_macro_keys(self):
    while not self.macro_confirmed:
      print("Pressione a tecla do macro para o revive:")
      self.macro_revive_key = keyboard.read_key()

      print("Pressione a tecla do macro para o combo:")
      self.macro_combo_key = keyboard.read_key()

      print("Está tudo certo ? [Y/N]")
      confirmed = keyboard.read_key()
      if(confirmed == 'y' or confirmed == 'Y'):
        self.macro_confirmed = True

  def get_macro_keys(self):
    """ Retorna as configurações do macro. Nesta sequencia:
        - revive_key
        - combo_keys
    """
    return self.macro_revive_key, self.macro_combo_key