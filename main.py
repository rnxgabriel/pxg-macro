import keyboard
import time

from core.Attack import Attack
from core.Healing import Healing
from core.Configure import Configure

def main():
  print("🔴 Macro iniciado! Configure suas teclas seguindo as instruções abaixo:")
  configurator = Configure()
  configurator.set_all_keys()

  (revive_key,
  medicine_key,
  pokeball_key,
  combo_keys,
  position) = configurator.get_game_keys()
  macro_revive_key, macro_combo_key = configurator.get_macro_keys()

  healing = Healing(revive_key, medicine_key, pokeball_key, position)
  attack = Attack(healing, combo_keys, True)

  print("✅ Macro pronto! Pressione as teclas configuradas ou ESC para sair.")

  try:
    while True:
      if keyboard.is_pressed(macro_revive_key): # type: ignore
        print("[LOG] Revive acionado via macro!")
        healing.revive()

      if keyboard.is_pressed(macro_combo_key): # type: ignore
        print("[LOG] Combo iniciado via macro!")
        attack.perform_combo()

      if keyboard.is_pressed('esc'):
        print("[LOG] Encerrando macro...")
        break

      time.sleep(0.05)

  except KeyboardInterrupt:
    print("⚠️ Macro interrompido manualmente.")

  finally:
    print("Macro encerrado...")

if __name__ == '__main__': main()