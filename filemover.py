import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def move_files(source_dir, dest_dir, file_types, os_type):
    # extensões de arquivo para diferentes tipos
    file_extensions = {
        "Fotos": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
        "Vídeos": ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.mpeg', '.mpg', '.m4v', '.3gp'],
        "Áudio": ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.alac', '.aiff']
    }
    
    extensions = file_extensions.get(file_types, [])
    
    # certifique-se de que o diretório de destino existe
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # ajuste os caminhos conforme o sistema operacional
    if os_type == "Windows":
        source_dir = source_dir.replace("/", "\\")
        dest_dir = dest_dir.replace("/", "\\")
    elif os_type == "Linux":
        source_dir = source_dir.replace("\\", "/")
        dest_dir = dest_dir.replace("\\", "/")

    # percorra todos os arquivos e diretórios na pasta de origem
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            #verifique se o arquivo tem uma das extensões selecionadas
            if any(file.lower().endswith(ext) for ext in extensions):
                # caminho completo do arquivo
                file_path = os.path.join(root, file)
                # caminho de destino
                dest_path = os.path.join(dest_dir, file)
                # mova o arquivo
                shutil.move(file_path, dest_path)
                print(f'movendo {file_path} para {dest_path}')
    
    messagebox.showinfo("concluído", f"os arquivos de {file_types.lower()} foram movidos com sucesso!")

def select_source_directory():
    source_dir = filedialog.askdirectory()
    if source_dir:
        source_entry.delete(0, tk.END)
        source_entry.insert(0, source_dir)

def select_dest_directory():
    dest_dir = filedialog.askdirectory()
    if dest_dir:
        dest_entry.delete(0, tk.END)
        dest_entry.insert(0, dest_dir)

def start_moving():
    source_dir = source_entry.get()
    dest_dir = dest_entry.get()
    file_type = file_type_var.get()
    os_type = os_type_var.get()
    if not source_dir or not dest_dir:
        messagebox.showwarning("Aviso", "Por favor, selecione os diretórios de origem e destino.")
    else:
        move_files(source_dir, dest_dir, file_type, os_type)

# crie a janela principal
root = tk.Tk()
root.title("Mover Arquivos")

# labels e entrys para os diretórios de origem e destino
tk.Label(root, text="Diretório de Origem:").grid(row=0, column=0, padx=10, pady=10)
source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Selecionar", command=select_source_directory).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Diretório de Destino:").grid(row=1, column=0, padx=10, pady=10)
dest_entry = tk.Entry(root, width=50)
dest_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Selecionar", command=select_dest_directory).grid(row=1, column=2, padx=10, pady=10)

# opções para selecionar o tipo de arquivo
tk.Label(root, text="Tipo de Arquivo:").grid(row=2, column=0, padx=10, pady=10)
file_type_var = tk.StringVar(value="Fotos")
file_type_options = ["Fotos", "Vídeos", "Áudio"]
file_type_menu = tk.OptionMenu(root, file_type_var, *file_type_options)
file_type_menu.grid(row=2, column=1, padx=10, pady=10)

# opções para selecionar o sistema operacional
tk.Label(root, text="Sistema Operacional:").grid(row=3, column=0, padx=10, pady=10)
os_type_var = tk.StringVar(value="Windows")
os_type_options = ["Windows", "Linux"]
os_type_menu = tk.OptionMenu(root, os_type_var, *os_type_options)
os_type_menu.grid(row=3, column=1, padx=10, pady=10)

# botão para iniciar o processo
tk.Button(root, text="Mover Arquivos", command=start_moving).grid(row=4, column=0, columnspan=3, pady=20)

# iniciando o loop da interface gráfica
root.mainloop()
