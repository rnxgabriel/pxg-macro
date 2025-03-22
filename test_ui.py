import tkinter as tk
from tkinter import messagebox
import mouse  # Biblioteca para pegar a posição do mouse

class KeyConfiguratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pxg-macro")
        self.root.geometry("350x300")
        self.root.config(bg="#8B0000")  # Fundo vermelho escuro

        self.game_revive_key = None
        self.game_medicine_key = None
        self.game_pokeball_key = None
        self.game_combo_keys = None
        self.position = None

        # Frame principal
        self.main_frame = tk.Frame(root, bg="#8B0000")
        self.main_frame.pack(pady=4)

        # Colunas: Botões e Exibição das configurações
        self.button_frame = tk.Frame(self.main_frame, bg="#8B0000")
        self.button_frame.grid(row=0, column=0, padx=4)

        self.info_frame = tk.Frame(self.main_frame, bg="#8B0000")
        self.info_frame.grid(row=0, column=1, padx=4)

        # Botões e Labels para exibição
        self.create_button("Configurar Tecla de Revive", self.set_game_revive_key, 0)
        self.create_button("Configurar Tecla de Medicine", self.set_game_medicine_key, 1)
        self.create_button("Configurar Teclas de Combo", self.set_game_combo_keys, 2)
        self.create_button("Configurar Tecla de Pokéball", self.set_game_pokeball_key, 3)
        self.create_button("Configurar Posição do Mouse", self.set_game_position, 4)

        # Labels para mostrar as teclas ou posição
        self.label_revive = tk.Label(self.info_frame, text="Revive Key: Não configurada", font=("Arial", 8), fg="white", bg="#8B0000")
        self.label_revive.grid(row=0, column=0, sticky="w")

        self.label_medicine = tk.Label(self.info_frame, text="Medicine Key: Não configurada", font=("Arial", 8), fg="white", bg="#8B0000")
        self.label_medicine.grid(row=1, column=0, sticky="w")

        self.label_combo = tk.Label(self.info_frame, text="Combo Keys: Não configurada", font=("Arial", 8), fg="white", bg="#8B0000")
        self.label_combo.grid(row=2, column=0, sticky="w")

        self.label_pokeball = tk.Label(self.info_frame, text="Pokeball Key: Não configurada", font=("Arial", 8), fg="white", bg="#8B0000")
        self.label_pokeball.grid(row=3, column=0, sticky="w")

        self.label_position = tk.Label(self.info_frame, text="Posição do Mouse: Não configurada", font=("Arial", 8), fg="white", bg="#8B0000")
        self.label_position.grid(row=4, column=0, sticky="w")

    def create_button(self, text, command, row):
        button = tk.Button(self.button_frame, text=text, font=("Arial",8), fg="white", bg="#B22222", width=24, height=2, command=command)
        button.grid(row=row, column=0, pady=8)

    def set_game_revive_key(self):
        self.game_revive_key = "R"  # Simulação, você pode usar `keyboard.read_key()` aqui
        self.label_revive.config(text=f"Revive Key: {self.game_revive_key}")

    def set_game_medicine_key(self):
        self.game_medicine_key = "M"  # Simulação
        self.label_medicine.config(text=f"Medicine Key: {self.game_medicine_key}")

    def set_game_combo_keys(self):
        self.game_combo_keys = ["C", "X"]  # Simulação
        self.label_combo.config(text=f"Combo Keys: {', '.join(self.game_combo_keys)}")

    def set_game_pokeball_key(self):
        self.game_pokeball_key = "P"  # Simulação
        self.label_pokeball.config(text=f"Pokeball Key: {self.game_pokeball_key}")

    def set_game_position(self):
        # Captura a posição do mouse
        self.position = mouse.get_position()  # Pega a posição atual do mouse
        self.label_position.config(text=f"Posição do Mouse: {self.position}")

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyConfiguratorApp(root)
    root.mainloop()
