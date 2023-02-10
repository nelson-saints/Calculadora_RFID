# importar o tkinter
from tkinter import *
from tkinter import ttk
import re



# cores
cor1 = "#3b3b3b" # black/preta
cor2 = "#feffff" # white/branca
cor3 = "#38576b" # Azul carregado
cor4 = "#ECEFF1" # Cizenta
cor5 = "#FFAB40" # Orange/Laranja

janela = Tk()
janela.title("Calculadora RFID")
janela.geometry("500x410")
janela.config(bg=cor1)


# criando frames
frame_tela = Frame(janela, width=500, height=100, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=500, height=410)
frame_corpo.grid(row=1, column=0)

#varialvel todos valores
todos_valores = ''

# criando label
valor_texto = StringVar()

#criando funcao
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores +  str(event)
    
    
    #passando o valor para tela
    valor_texto.set(todos_valores)

# funcao ASK
def ask():
    global todos_valores
    cartao = eval(todos_valores)
    
    area = cartao/4294967296
    codigo = cartao%4294967296
    
    todos_valores = f'{area:.0f}.{codigo}'
    valor_texto.set(todos_valores)

# funcao para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    #imprimir na tela
    valor_texto.set(str(resultado))
    todos_valores = ' '

# funcao para apagar o ultimo digito
def apagar():
    global todos_valores
    todos_valores = todos_valores[:-1]
    valor_texto.set(todos_valores)

#funcao limpa tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# criando botoes


b_0 = Button(frame_corpo, command=limpar_tela, text="C", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=0)
b_1 = Button(frame_corpo, command=apagar, text="<-", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=59, y=0)
b_2 = Button(frame_corpo, command= lambda:entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command= lambda:entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)
b_ASK = Button(frame_corpo, command= ask, text="ASK", width=15, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_ASK.place(x=236, y=0)

b_4 = Button(frame_corpo, command= lambda:entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command= lambda:entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, command= lambda:entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, command= lambda:entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)
b_MIFARE = Button(frame_corpo, command= "lambda:entrar_valores('/')", text="MIFARE", width=15, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_MIFARE.place(x=236, y=52)

b_8 = Button(frame_corpo, command= lambda:entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command= lambda:entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, command= lambda:entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, command= lambda:entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, command= lambda:entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command= lambda:entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, command= lambda:entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, command= lambda:entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_1 = Button(frame_corpo, command= lambda:entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=208)
b_2 = Button(frame_corpo, command= lambda:entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=208)
b_3 = Button(frame_corpo, command= calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=208)



janela.mainloop()