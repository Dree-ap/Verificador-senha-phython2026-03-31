import tkinter as tk
import sys
import os

# Ajuste de caminho para sistemas Linux
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.verificador import avaliar_forca_senha


class VerificadorApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Verificador de Senhas - Dree")
        self.janela.geometry("450x420")
        self.janela.configure(padx=20, pady=20)

        # Configuração de Validação (Bloqueio de espaço)
        vcmd = (self.janela.register(self.validar_entrada), '%P')

        # Elementos da Interface
        tk.Label(self.janela, text="Digite uma senha para testar:", font=("Arial", 12)).pack(pady=10)

        self.var_senha = tk.StringVar()
        self.var_senha.trace_add("write", self.atualizar_interface)

        frame_senha = tk.Frame(self.janela)
        frame_senha.pack(pady=5)

        self.entrada_senha = tk.Entry(
            frame_senha, textvariable=self.var_senha, font=("Arial", 14),
            width=20, show="*", validate="key", validatecommand=vcmd
        )
        self.entrada_senha.pack(side=tk.LEFT, padx=5)

        self.botao_ver = tk.Button(frame_senha, text="Mostrar", command=self.alternar_visibilidade)
        self.botao_ver.pack(side=tk.LEFT)

        self.label_resultado = tk.Label(self.janela, text="Aguardando senha...", font=("Arial", 14, "bold"), fg="gray")
        self.label_resultado.pack(pady=15)

        self.label_dicas = tk.Label(self.janela, text="", font=("Arial", 11), justify="left")
        self.label_dicas.pack(pady=10)

        # Bind da tecla Enter
        self.janela.bind('<Return>', lambda e: self.atualizar_interface())

    def validar_entrada(self, texto_novo):
        return " " not in texto_novo

    def atualizar_interface(self, *args):
        senha = self.var_senha.get()
        if not senha:
            self.label_resultado.config(text="Aguardando senha...", fg="gray")
            self.label_dicas.config(text="")
            return

        resultado, cor, resumo = avaliar_forca_senha(senha)
        self.label_resultado.config(text=resultado, fg=cor)

        texto_dicas = ("O que precisa melhorar:\n" + "\n".join(resumo)) if resumo else "Parabéns! Senha blindada."
        cor_dicas = "red" if resumo else "green"
        self.label_dicas.config(text=texto_dicas, fg=cor_dicas)

    def alternar_visibilidade(self):
        if self.entrada_senha.cget("show") == "*":
            self.entrada_senha.config(show="")
            self.botao_ver.config(text="Ocultar")
        else:
            self.entrada_senha.config(show="*")
            self.botao_ver.config(text="Mostrar")


if __name__ == "__main__":
    root = tk.Tk()
    app = VerificadorApp(root)
    root.mainloop()