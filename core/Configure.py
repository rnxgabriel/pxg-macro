import os
import time
import mouse
import keyboard

from core.HotkeyStorage import HotkeyStorage

class Configure:
  def __init__(self):
    self.storage = HotkeyStorage()
    self.position = None

    self.game_confirmed = False
    self.game_revive_key = None
    self.game_medicine_key = None
    self.game_pokeball_key = None
    self.game_combo_keys = []

    self.macro_confirmed = False
    self.macro_revive_key = None
    self.macro_combo_key = None

  def set_all_keys(self):
    if self.load_config(): return
    self.set_game_keys()
    time.sleep(1)
    os.system('cls')
    time.sleep(1)
    self.set_macro_keys()
    self.save_config()

  def continue_configuring(self):
    """Aguarda o usuário apertar 'enter' para continuar."""
    print("Aperte 'enter' para ir para a próxima configuração.")
    while True:
      key = keyboard.read_key(suppress=True)  # Evita que a tecla continue no buffer
      if key == 'enter':
        time.sleep(0.5)  # Um pequeno atraso, se necessário
        break

  def read_combo_keys(self):
    """Lê múltiplas teclas para combo até o usuário pressionar ENTER."""
    self.game_combo_keys.clear()
    print("Pressione as teclas para o combo (ENTER para finalizar):")
    while True:
      key = keyboard.read_key()
      time.sleep(0.2)
      if key == 'enter':
        break
      if key not in self.game_combo_keys:
        print(f"Tecla {key} adicionada ao combo.")
        self.game_combo_keys.append(key)

  def set_game_keys(self):
    """Configura as teclas do jogo e posição do revive."""
    while not self.game_confirmed:
      print("Pressione a tecla do jogo para o revive:")
      self.game_revive_key = keyboard.read_key()
      print(f"Tecla salva: {self.game_revive_key}")
      self.continue_configuring()

      print("Clique na posição do revive.")
      mouse.wait(button="left")
      self.position = mouse.get_position()
      print(f"Posição salva: {self.position}")
      self.continue_configuring()

      print("Pressione a tecla do jogo para o medicine:")
      self.game_medicine_key = keyboard.read_key()
      print(f"Tecla salva: {self.game_medicine_key}")
      self.continue_configuring()

      print("Pressione a tecla para enviar o Pokémon:")
      self.game_pokeball_key = keyboard.read_key()
      print(f"Tecla salva: {self.game_pokeball_key}")
      self.continue_configuring()

      self.read_combo_keys()

      print("Confirma as configurações? (y/n)")
      confirmed = keyboard.read_key().lower() # type: ignore
      if confirmed == 'y':
        self.game_confirmed = True
        print("Configuração do jogo concluída!")
      else:
        print("Reiniciando configuração do jogo...")

  def get_game_keys(self):
    """Retorna revive_key, medicine_key, pokeball_key, combo_keys e position."""
    return (self.game_revive_key, self.game_medicine_key, 
            self.game_pokeball_key, self.game_combo_keys, self.position)

  def set_macro_keys(self):
    """Configura as teclas do macro."""
    while not self.macro_confirmed:
      print("Pressione a tecla do macro para o revive:")
      self.macro_revive_key = keyboard.read_key()
      self.continue_configuring()

      print("Pressione a tecla do macro para o combo:")
      self.macro_combo_key = keyboard.read_key()
      self.continue_configuring()

      print("Confirma as configurações do macro? (y/n)")
      confirmed = keyboard.read_key().lower() # type: ignore
      if confirmed == 'y':
        self.macro_confirmed = True
        print("Configuração do macro concluída!")
      else:
        print("Reiniciando configuração do macro...")

  def get_macro_keys(self):
    """Retorna revive_key e combo_key do macro."""
    return self.macro_revive_key, self.macro_combo_key

  def load_config(self):
    """Carrega as configurações salvas, se existir."""
    time.sleep(1)
    if self.storage.has_data():
      print("Deseja carregar as configurações salvas? (y/n)")
      key = keyboard.read_key(suppress=True).lower()  #type: ignore
      if key == 'y':
        game_keys = self.storage.load_game_keys()
        if game_keys:
          self.game_revive_key, self.game_medicine_key, self.game_pokeball_key, self.game_combo_keys, self.position = game_keys.values()
        macro_keys = self.storage.load_macro_keys()
        if macro_keys:
          self.macro_revive_key, self.macro_combo_key = macro_keys.values()
        print("Configurações carregadas com sucesso!")
        return True
    print("Configurações não carregadas.")
    return False

  def save_config(self):
    """Salva as configurações atuais."""
    time.sleep(1)
    print("Deseja salvar estas configurações? (y/n)")
    key = keyboard.read_key(suppress=True).lower()  #type: ignore
    if key == 'y':
        self.storage.save_game_keys(self.game_revive_key, self.game_medicine_key, self.game_pokeball_key, self.game_combo_keys, self.position)
        self.storage.save_macro_keys(self.macro_revive_key, self.macro_combo_key)
        print("Configurações salvas com sucesso!")
    else:
        print("Configurações não salvas.")