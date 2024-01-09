#Passo a passo

#Passo 01 - Entrar no sistema da empresa
  ## https://dlp.hashtagtreinamentos.com/python/intensivao/login

    #Instalar pyautogui - pip install pyautogui
import pyautogui
import time

# Clicar - pyautogui.click
# Escrever - pyautogui.write
# apertar uma tecla - payautogui.press

pyautogui.PAUSE = 1

# Etapas passo 01:
# 1º - abrir a janela do windows
pyautogui.press("win")

# 2º - escrever o nome do programa que deseja abrir
pyautogui.write("chrome")

# 3º - entrar no programa
pyautogui.press("enter")

# 4º - abrir link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# 5º - entrar no programa
pyautogui.press("enter")

# 6º - espere 5s
time.sleep(5)

#Passo 02 - Fazer login
# Etapas passo 02
# 6º - clicar no campo email
pyautogui.click(x=496, y=375)
# 7º - escrever email
pyautogui.write("fmmcba1@gmail.com")
# 8º - pular para o campo senha ou próximo campo
pyautogui.press("tab")
# 9º - Entrar com a senha
pyautogui.write("minhasenha")
# Clicar botão logar
pyautogui.click(x=689, y=543)

#Passo 03 - Importar a base de dados

#Passo 04 - Cadastrar um produto

#Passo 05 - Repetir passo 04 até finalizar base de dados 






