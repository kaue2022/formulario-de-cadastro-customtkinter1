import customtkinter as ctk


def cadastrar_usuario():
    nome = campo_nome.get().strip()
    idade = idd.get().strip()
    email = mail.get().strip()
    senha = snh.get().strip()
    confirmar = confirma.get().strip()

    # Verificações de preenchimento
    if not nome.strip() or not idade.strip() or not email.strip() or not senha or not confirmar:
        resultado.configure(text='Preencha todos os campos.', text_color='red')
        return

    if not idade.isdigit():
        resultado.configure(text='Idade deve ser um número.', text_color='red')
        return

    if '@' not in email or '.' not in email:
        resultado.configure(text='E-mail inválido.', text_color='red')
        return

    if senha != confirmar:
        resultado.configure(text='Senhas não coincidem', text_color='red')
        return
    
    try:
        # Salvamento em arquivo txt
        with open('usuarios.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{nome},{idade},{email},{senha}\n")

        resultado.configure(text='Cadastro realizado com sucesso!', text_color='green')
    
        # Limpa os campos
        campo_nome.delete(0, 'end')
        idd.delete(0, 'end')
        mail.delete(0, 'end')
        snh.delete(0, 'end')
        confirma.delete(0, 'end')

    except Exception as erro:
        resultado.configure(text=f"Erro ao salvar: {erro}", text_color='red')

    # Tudo certo → abrir nova janela
    abrir_janela_sucesso()

def abrir_janela_sucesso():
    nova_janela = ctk.CTkToplevel(janela)
    nova_janela.geometry('400x500')
    nova_janela.title('Sucesso')
    nova_janela.grab_set()

    
    msg = ctk.CTkLabel(nova_janela, text='Bem-Vindo!Você está cadastrado em nosso sistema', font=('Arial', 14, 'bold'), text_color='white')
    msg.pack(pady=50)

# Janela principal
janela = ctk.CTk()
janela.geometry('400x550')
janela.title('Formulário de Cadastro')
janela.grid_columnconfigure(0, weight=1)

# Campos
label_nome = ctk.CTkLabel(janela, text='Nome', font=('Arial',14,'bold'))
label_nome.grid(row=0, column=0, sticky='w', padx=20, pady=(20, 0))

campo_nome = ctk.CTkEntry(janela, placeholder_text='Nome completo', width=250)
campo_nome.grid(row=1, column=0, padx=20, pady=(5, 10))

idd_label = ctk.CTkLabel(janela, text='Idade', font=('Arial',14,'bold'))
idd_label.grid(row=2, column=0, sticky='w', padx=20)

idd = ctk.CTkEntry(janela, placeholder_text='Sua idade', width=250)
idd.grid(row=3, column=0, padx=20, pady=(5, 10))

mail_label = ctk.CTkLabel(janela, text='E-mail', font=('Arial',14,'bold'))
mail_label.grid(row=4, column=0, sticky='w', padx=20)

mail = ctk.CTkEntry(janela, placeholder_text="Seu Email", width=250)
mail.grid(row=5, column=0, padx=20, pady=(5, 10))

snh_label = ctk.CTkLabel(janela, text='Crie sua Senha', font=('Arial',14,'bold'))
snh_label.grid(row=6, column=0, sticky='w', padx=20)

snh = ctk.CTkEntry(janela, placeholder_text='Senha', show='*', width=250)
snh.grid(row=7, column=0, padx=20, pady=(5, 10))

confirma_label = ctk.CTkLabel(janela, text="Confirme sua senha", font=('Arial',14,'bold'))
confirma_label.grid(row=8, column=0, sticky='w', padx=20)

confirma = ctk.CTkEntry(janela, placeholder_text='Digite sua senha novamente', show='*', width=250)
confirma.grid(row=9, column=0, padx=20, pady=(5, 10))

btn = ctk.CTkButton(janela, text='Cadastrar', command=cadastrar_usuario, font=('Arial',14,'bold'))
btn.grid(row=10, column=0, pady=(10, 10), padx=20)

resultado = ctk.CTkLabel(janela, text='', font=('Arial',14,'bold'))
resultado.grid(row=11, column=0, pady=10)

janela.mainloop()
