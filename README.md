# 🛡️ Verificador de Força de Senhas

![Licença](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)

Uma aplicação desktop desenvolvida em Python que avalia a força de senhas em tempo real, fornecendo feedback visual e dicas de segurança baseadas em requisitos de complexidade. Ideal para estudos de **Cibersegurança** e desenvolvimento de software seguro [cite: 2026-01-16].

## 💻 Demonstração

Aqui está o programa rodando no Linux, validando uma senha forte:

![Screenshot do Verificador](Captura%20de%20tela%20de%202026-03-31%2009-36-44.png)
## ✨ Funcionalidades

* **Validação em Tempo Real:** A análise é feita enquanto você digita [cite: 2026-03-31].
* **Feedback Visual:** Cores e textos indicam se a senha é "Curta", "Fraca", "Média" ou "Forte" [cite: 2026-03-31].
* **Lista de Melhorias:** Mostra exatamente o que falta para a senha ficar blindada [cite: 2026-03-31].
* **Ocultar/Mostrar Senha:** Botão funcional para privacidade [cite: 2026-03-31].
* **Bloqueio de Espaços:** Impede que o usuário digite espaços acidentais [cite: 2026-03-31].

## 🧠 Critérios de Segurança (Regex)

O motor de análise verifica os seguintes requisitos [cite: 2026-01-16]:
* Mínimo de 8 caracteres.
* Pelo menos uma letra maiúscula.
* Pelo menos uma letra minúscula.
* Pelo menos um número.
* Pelo menos um caractere especial (!@#$...).

## 🛠️ Instalação e Execução

### Pré-requisitos
* Python 3.x instalado [cite: 2026-03-31].
* Biblioteca `tkinter` (normalmente incluída no Python no Linux, mas se não estiver, instale com `sudo apt-get install python3-tk`) [cite: 2026-03-31].

### Passos
```bash
# 1. Clone o repositório
git clone [https://github.com/Dree-ap/Verificador-senha-phython2026-03-31.git](https://github.com/Dree-ap/Verificador-senha-phython2026-03-31.git)

# 2. Navegue até a pasta
cd Verificador-senha-phython2026-03-31

# 3. Execute a aplicação
python3 main.py
