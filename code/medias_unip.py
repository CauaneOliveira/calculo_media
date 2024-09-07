import ctypes
ctypes.windll.kernel32.FreeConsole()

from tkinter import *
from tkinter import ttk
import pyscreenshot as ImageGrab
import os

def res_texto(res, x, y,cor,n):
    if n == 1:
        texto_status1.place(x=x, y=y)
        texto_status1.config(text=res)
    elif n ==2 :
        texto_status.place(x=x, y=y)
        texto_status.config(text=res,background=cor)
         
    #o label do status na interface 

def jane_est_mf(ms):
    janela_mf.destroy()
    global janela_est_mf
    janela_est_mf = Tk()
    tabela = ttk.Treeview(janela_est_mf)

   
    tabela["columns"] = ("MÉDIA SEMESTRAL", "EXAME", "MÉDIA FINAL")
   
    janela_est_mf.title('Mandar mensagem')
    janela_est_mf.geometry("700x300")
    janela_est_mf.configure(background='#9cd5fe') 
    
    def tirar_print():
        # Captura a tela da janela atual
        x = janela_est_mf.winfo_rootx()
        y = janela_est_mf.winfo_rooty()
        largura = janela_est_mf.winfo_width()
        altura = janela_est_mf.winfo_height()
        
        imagem = ImageGrab.grab((x+47, y+36, (x+largura)-48, (y+altura)-36))

        # Obtém o caminho completo para o diretório da área de trabalho
        diretorio_area_de_trabalho = os.path.join(os.path.expanduser('~'), 'Desktop')
        
        # Salva a imagem na área de trabalho
        caminho_imagem = os.path.join(diretorio_area_de_trabalho, 'media_semestral_estimativa.png')
        imagem.save(caminho_imagem)

        texto_tirado= Label(text="PRINT TIRADO",background='RED')
        texto_tirado.place( x=310, y=10)

    # Formata as colunas
    tabela.column("#0", width=0, stretch=NO)
    tabela.column("MÉDIA SEMESTRAL", anchor=CENTER, width=200)
    tabela.column("EXAME", anchor=CENTER, width=200)
    tabela.column("MÉDIA FINAL", anchor=CENTER, width=200)

    # Define os cabeçalhos das colunas
    tabela.heading("#0", text="", anchor=CENTER)
    tabela.heading("MÉDIA SEMESTRAL", text="MÉDIA SEMESTRAL", anchor=CENTER)
    tabela.heading("EXAME", text="EXAME", anchor=CENTER)
    tabela.heading("MÉDIA FINAL", text="MÉDIA FINAL", anchor=CENTER)
    
    
    media_desejada = 5
    
    ex = (2 * media_desejada) - (ms)
    mf = (ms+ex)/2

    if ex < 10:
        tabela.insert("", END, text="1", values=(ms,ex,mf))
    else:
        res = f"DP"
        res_texto(res, 195, 450,'RED',2)
    

    # Inicia o loop principal da aplicação
    tabela.grid(row=0, column=0, padx=10, pady=10)

    # Centraliza a tabela na janela
    janela_est_mf.grid_rowconfigure(0, weight=1)
    janela_est_mf.grid_columnconfigure(0, weight=1)

    # Cria um botão para tirar o print
    botao_print = ttk.Button(janela_est_mf, text="Tirar Print", command=tirar_print)
    botao_print.place(x =310,y=270)

    bt_voltar = Button(janela_est_mf,text='<-', bd=1,command=lambda:jane_mf(1),cursor="hand2",background='#0180ff')
    bt_voltar.place(width=40, height=35, x=4, y=4)


    janela_est_mf.mainloop()

def jane_est_ms(np1, np2,tipo):
    janela.destroy()
    global janela_est
    janela_est = Tk()
    # Cria um widget Treeview
    tabela = ttk.Treeview(janela_est)

    # Define as colunas da tabela
    tabela["columns"] = ("NP1", "NP2", "PIM")
   
    janela_est.title('Mandar mensagem')
    janela_est.geometry("700x300")
    janela_est.configure(background='#9cd5fe') 
    

    media_desejada = 7
    margens = [0.2,0.5,1.0, 1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5]
    
    lista_np2=[]
    lista_pim=[]

    for margem in margens:
        if np2 == None:
            # Cálculo da nota máxima possível na NP2 com base na margem permitida
            np2_max = min(10, ((media_desejada * 10) - (np1 * 4) - (10 * margem)) / 4)

            # Percorrendo as possíveis notas da NP2
            for i in range(0, int(np2_max * 10) + 1):
                np2_est = i / 10
                pim_est = (media_desejada * 10 - (np1 * 4) - (np2_est * 4)) / 2

                # Verificando se a diferença entre as notas da NP2 e do PIM está dentro da margem permitida
                if abs(np2_est - pim_est) <= margem:
                    pim_est = f'{pim_est:.2f}'
                    np2_est = f'{np2_est:.2f}'
                    lista_np2.append(np2_est)
                    lista_pim.append(pim_est)
                    break
                
        else:
            
            pim_est = (media_desejada * 10 - (np1 * 4) - (np2 * 4)) / 2

            if pim_est < 10:
                pim_est = f'{pim_est:.2f}'
                lista_pim.append(pim_est)
                
            else:
                res = f"Exame!"
                res_texto(res, 195, 450,'RED',2)


    def tirar_print():
        # Captura a tela da janela atual
        x = janela_est.winfo_rootx()
        y = janela_est.winfo_rooty()
        largura = janela_est.winfo_width()
        altura = janela_est.winfo_height()
        
        imagem = ImageGrab.grab((x+47, y+36, (x+largura)-48, (y+altura)-36))

        # Obtém o caminho completo para o diretório da área de trabalho
        diretorio_area_de_trabalho = os.path.join(os.path.expanduser('~'), 'Desktop')
        
        # Salva a imagem na área de trabalho
        caminho_imagem = os.path.join(diretorio_area_de_trabalho, 'media_semestral_estimativa.png')
        imagem.save(caminho_imagem)

        texto_tirado= Label(text="PRINT TIRADO",background='RED')
        texto_tirado.place( x=310, y=10)

    # Formata as colunas
    tabela.column("#0", width=0, stretch=NO)
    tabela.column("NP1", anchor=CENTER, width=200)
    tabela.column("NP2", anchor=CENTER, width=200)
    tabela.column("PIM", anchor=CENTER, width=200)

    # Define os cabeçalhos das colunas
    tabela.heading("#0", text="", anchor=CENTER)
    tabela.heading("NP1", text="NP1", anchor=CENTER)
    tabela.heading("NP2", text="NP2", anchor=CENTER)
    tabela.heading("PIM", text="PIM", anchor=CENTER)


    if tipo != 3:
        # Insere os dados na tabela
        tabela.insert("", END, text="1", values=(np1, lista_np2[0], lista_pim[0]))
        tabela.insert("", END, text="2", values=(np1, lista_np2[1], lista_pim[1]))
        tabela.insert("", END, text="3", values=(np1, lista_np2[2], lista_pim[2]))
    else:
        # Insere os dados na tabela
        tabela.insert("", END, text="1", values=(np1, np2, lista_pim[0]))



    # Inicia o loop principal da aplicação
    tabela.grid(row=0, column=0, padx=10, pady=10)

    # Centraliza a tabela na janela
    janela_est.grid_rowconfigure(0, weight=1)
    janela_est.grid_columnconfigure(0, weight=1)

    # Cria um botão para tirar o print
    botao_print = ttk.Button(janela_est, text="Tirar Print", command=tirar_print)
    botao_print.place(x =310,y=270)

    bt_voltar = Button(janela_est,text='<-', bd=1,command=lambda:janela_ms(2),cursor="hand2",background='#0180ff')
    bt_voltar.place(width=40, height=35, x=4, y=4)


    janela_est.mainloop()

def jane_mf(n):

    if n == 1:
        janela_est_mf.destroy()
    elif n == 2:
        janela.destroy()
    
    global janela_mf
    janela_mf = Tk()
    janela_mf.title("CALCULO DE MEDIAS")
    janela_mf.configure(background='#9cd5fe') 
    janela_mf.geometry("490x560")

    texto_ms= Label(text="DIGITE A NOTA DA MEDIA SEMESTRAL (MS)",background='#9cd5fe')
    texto_ms.place( x=49, y=120)

    en_ms = Entry(janela_mf, bd=2, font=("Calibri", 15), justify=CENTER,highlightthickness=2)
    en_ms.place(width=385, height=38, x=49, y=140)

    texto_ex= Label(text="DIGITE A NOTA DO EXAME",background='#9cd5fe')
    texto_ex.place( x=49, y=180)

    en_ex = Entry(janela_mf, bd=2, font=("Calibri", 15), justify=CENTER,highlightthickness=2)
    en_ex.place(width=385, height=38, x=49, y=200)


    def metodo_boton(n):
        global meio
        if n == 1:
            texto_ex.config(state=NORMAL)
            en_ex.config(state=NORMAL) 
            meio = 1
            
        else:
            texto_ex.config(state=DISABLED)
            en_ex.config(state=DISABLED)
            meio = 2


    var1 = StringVar(janela_mf,'1')
    metodo_boton(1)
    sel_radio1=Radiobutton(janela_mf, text="Calculo",command=lambda:metodo_boton(1), variable=var1,value='1',background='#9cd5fe')
    sel_radio1.place(x=49, y=250)
    sel_radio2=Radiobutton(janela_mf, text="Estimativa",command=lambda:metodo_boton(2), variable=var1,value='2',background='#9cd5fe')
    sel_radio2.place(x=200, y=250)


    def calculo():
        try:
            ms = float(en_ms.get())
            en_ms.config(highlightbackground = "grey")
        except:
            en_ms.config(highlightbackground = "red")
            

        try:
            ex = float(en_ex.get())
            en_ex.config(highlightbackground = "grey")
        except:
            en_ex.config(highlightbackground = "red")

        

        if meio == 1:
            try:
                mf = (ms+ex)/2
                res = f"A média Final\n"
                res_texto(res, 200, 350,'',1)

                if mf < 5:
                    res = f"{mf}"
                    res_texto(res, 230, 375,'red',2)
                else:
                    res = f"{mf}"
                    res_texto(res, 230, 375,'green',2)

            except:
                res = f"Ocorreu um erro!"
                res_texto(res, 190, 350,'',1)

                res = f""
                res_texto(res, 230, 375,'#9cd5fe',2)
        else:
            jane_est_mf(ms)
            

    bt_ok_calcular = Button(janela_mf,text='<-', bd=1,command=lambda:janela_ms(1),cursor="hand2",background='#0180ff')
    bt_ok_calcular.place(width=50, height=38, x=5, y=5)

    bt_mf = Button(janela_mf,text='MF', bd=1,command=calculo,cursor="hand2",background='#0180ff')
    bt_mf.place(width=80, height=38, x=202, y=300)

    global texto_status,texto_status1
    texto_status1 = Label(font=('Arial', 10),background='#9cd5fe')
    texto_status = Label(font=('Arial', 12),background='#9cd5fe')

    texto_co= Label(text="©cauaneooliveira",background='#9cd5fe',font=('Arial',7))
    texto_co.place( x=3, y=540)

    janela_mf.mainloop()

def janela_ms(n):
    
    global janela
    if n ==1:
        janela_mf.destroy()
    if n ==2:
        janela_est.destroy()
    
    janela = Tk()
    janela.title("CALCULO DE MEDIAS")
    janela.configure(background='#9cd5fe') 
    janela.geometry("490x560")

    texto_np1= Label(text="DIGITE A NOTA DA NP1",background='#9cd5fe')
    texto_np1.place( x=49, y=120)

    en_np1 = Entry(janela, bd=2, font=("Calibri", 15), justify=CENTER,highlightthickness=2)
    en_np1.place(width=385, height=38, x=49, y=140)

    texto_np2= Label(text="DIGITE A NOTA DA NP2",background='#9cd5fe')
    texto_np2.place( x=49, y=180)

    en_np2 = Entry(janela, bd=2, font=("Calibri", 15), justify=CENTER,highlightthickness=2)
    en_np2.place(width=385, height=38, x=49, y=200)

    texto_pim= Label(text="PIM",background='#9cd5fe')
    texto_pim.place( x=49, y=240)

    en_pim = Entry(janela, bd=2, font=("Calibri", 15), justify=CENTER,highlightthickness=2)
    en_pim.place(width=385, height=38, x=49, y=262)

    


    def metodo_boton(n):
        global meio
        if n == 1:
            texto_pim.config(state=NORMAL)
            en_pim.config(state=NORMAL) 
            texto_np2.config(state=NORMAL)
            en_np2.config(state=NORMAL)
            
            meio = 1
            
        else:
            def est_boton(n):
                global meio2
                if n == 3:
                    texto_pim.config(state=DISABLED)
                    en_pim.config(state=DISABLED)
                    texto_np2.config(state=NORMAL)
                    en_np2.config(state=NORMAL)
                    meio2 = 3
                    
                else:
                    texto_np2.config(state=DISABLED)
                    en_np2.config(state=DISABLED)
                    meio2 = 4

            est_var1 = StringVar(janela,'3')
            est_boton(3)
            sel_radio3=Radiobutton(janela, text="PIM",command=lambda:est_boton(3), variable=est_var1,value='3',background='#9cd5fe')
            sel_radio3.place(x=305, y=300)
            sel_radio4=Radiobutton(janela, text="NP2 E PIM",command=lambda:est_boton(4), variable=est_var1,value='4',background='#9cd5fe')
            sel_radio4.place(x=355, y=300)

            meio = 2


    
    var1 = StringVar(janela,'1')
    metodo_boton(1)
    sel_radio1=Radiobutton(janela, text="Calculo",command=lambda:metodo_boton(1), variable=var1,value='1',background='#9cd5fe')
    sel_radio1.place(x=49, y=335)
    sel_radio2=Radiobutton(janela, text="Estimativa",command=lambda:metodo_boton(2), variable=var1,value='2',background='#9cd5fe')
    sel_radio2.place(x=200, y=335)


    def calculo():
        try:
            np1 = float(en_np1.get())
            en_np1.config(highlightbackground = "grey")
        except:
            en_np1.config(highlightbackground = "red")
            

        try:
            np2 = float(en_np2.get())
            en_np2.config(highlightbackground = "grey")
        except:
            np2 = None
            en_np2.config(highlightbackground = "red")

        try:
            pim = float(en_pim.get())
            en_pim.config(highlightbackground = "grey")
        except:
            en_pim.config(highlightbackground = "red")

        
        if meio == 1:
            try:
                ms = ((np1*4)+(np2*4)+pim*2)/10
                res = f"A média Semestral\n"
                res_texto(res, 185, 450,'',1)

                if ms < 6.99:
                    res = f"{ms:.2f}"
                    res_texto(res, 232, 475,'red',2)
                else:
                    res = f"{ms:.2f}"
                    res_texto(res, 232, 475,'green',2)

            except:
                res = f"Ocorreu um erro!"
                res_texto(res, 195, 450,'',1)

                res = f""
                res_texto(res, 232, 475,'#9cd5fe',2)
        else:
            jane_est_ms(np1, np2,meio2)


    bt_ok_calcular = Button(janela,text='MS', bd=1,command=calculo,cursor="hand2",background='#0180ff')
    bt_ok_calcular.place(width=80, height=38, x=150, y=400)

    bt_mf = Button(janela,text='MF', bd=1,command=lambda:jane_mf(2),cursor="hand2",background='#0180ff')
    bt_mf.place(width=80, height=38, x=260, y=400)

    global texto_status,texto_status1
    texto_status1 = Label(font=('Arial', 10),background='#9cd5fe')
    texto_status = Label(font=('Arial', 12),background='#9cd5fe')


    texto_co= Label(text="©cauaneooliveira",background='#9cd5fe',font=('Arial',7))
    texto_co.place( x=3, y=540)
    janela.mainloop()

janela_ms(0)