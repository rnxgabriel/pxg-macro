import keyboard

from core.Attack import Attack
from core.Healing import Healing
from core.Configure import Configure

def main():
  print("Macro inicializado...")
  configurator = Configure()
  configurator.set_game_keys()

  revive, medicine, pokeball, combo, position = configurator.get_game_keys()

  healing = Healing(position, revive, medicine, pokeball)
  attack = Attack(healing, combo)

  configurator.set_macro_keys()
  revive_key, combo_key = configurator.get_macro_keys()

  attack.use_medicine()

  while True:
    if keyboard.is_pressed(revive_key): healing.revive()
    if keyboard.is_pressed(combo_key): attack.use_combo()
    if keyboard.is_pressed('esc'): break
    pass
  print("Macro encerrado...")

if __name__ == '__main__': main()