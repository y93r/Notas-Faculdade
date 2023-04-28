#!/usr/bin/env python
# coding: utf-8

# In[1]:


#bibliotecas
import tkinter as tk

janela = tk.Tk()
janela.geometry("350x450")
janela.title('Simulador de Notas')

#função para validar os valores, o usuário só consegue inserir um valor float de 0 a 10
def validar_valor(valor):
    if valor == "":
        return True
    try:
        valor = float(valor.replace(",", "."))
        valor = round(valor, 1)
        if valor < 0 or valor > 10:
            return False
    except ValueError:
        return False
    return True

#a faculdade utiliza a media ponderada onde cada atividade tem um peso diferente
#APOL 1 e 2 peso 15, Atividade prática 40 e prova objetiva 30
def simular_notas():
    if entry5.get().strip() == "" or entry6.get().strip() == "":
        resultado_label.config(text="Por favor, preencha todos os campos!")
        return
    
    try:
        n1 = float(entry1.get().replace(",", "."))
        n2 = float(entry2.get().replace(",", "."))
        n3 = float(entry3.get().replace(",", "."))
        n4 = float(entry4.get().replace(",", "."))
        media_final = float(n1 * 15 + n2 * 15 + n3 * 40 + n4 * 30) / 100
    except ValueError:
        resultado_label.config(text="Por favor, insira um valor válido!")
        return
    
    try:
        nome = entry5.get().upper().strip()
        disciplina = entry6.get().title().strip()
    except ValueError:
        resultado_label.config(text="Por favor, insira um valor válido!")
        return        

    if media_final >= 7:
        resultado = f'''Parabéns, {nome}!
   Aprovação na disciplina de {disciplina}
   com a média de {media_final :.1f}'''
    elif media_final >= 5:
        resultado = f'''{nome} está de recuperação 
    na disciplina de {disciplina}
    com a média de {media_final :.1f}'''
    else:
        resultado = f'''Estude mais da próxima vez, {nome}!
    Reprovação na disciplina de {disciplina}
    com a média de {media_final :.1f}'''
    resultado_label.config(text=resultado)

    
def limpar_campos():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)
    entry6.delete(0, tk.END)
    resultado_label.config(text="")
           
#inserir as notas
label_texto = tk.Label(text = "Insira sua nota de 0 a 10", font=("Arial", 10, "bold"))
label_texto.pack() 

validacao = janela.register(validar_valor)
entry1 = tk.Entry(janela, width=20, validate="key", validatecommand=(validacao, "%P"))
entry2 = tk.Entry(janela, width=20, validate="key", validatecommand=(validacao, "%P"))
entry3 = tk.Entry(janela, width=20, validate="key", validatecommand=(validacao, "%P"))
entry4 = tk.Entry(janela, width=20, validate="key", validatecommand=(validacao, "%P"))

label1 = tk.Label(text="APOL 1:")
label1.pack()
entry1.pack()

label2 = tk.Label(text="APOL 2:")
label2.pack()
entry2.pack()

label3 = tk.Label(text="Atividade Prática:")
label3.pack()
entry3.pack()

label4 = tk.Label(text="Prova Objetiva:")
label4.pack()
entry4.pack()

label5 = tk.Label(text="Digite seu nome:")
label5.pack()
entry5 = tk.Entry()
entry5.pack()

label6 = tk.Label(text="Digite a disciplina:")
label6.pack()
entry6 = tk.Entry()
entry6.pack()

calcular = tk.Button(text="Simular Notas", command=simular_notas, width=15)
calcular.pack(pady=10)

limpar = tk.Button(text="Limpar Campos", command=limpar_campos, width=15)
limpar.pack(pady=10)

resultado_label = tk.Label(text="")
resultado_label.pack(pady=10)

janela.mainloop()


# In[ ]:




