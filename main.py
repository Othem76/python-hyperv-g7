import subprocess
import tkinter as tk
from tkinter import messagebox

def enable_hyper_v():
    try:
        # Commande PowerShell pour activer Hyper-V
        command = "Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All"
        
        # Exécuter la commande PowerShell
        subprocess.run(["powershell", "-Command", command], check=True)

        messagebox.showinfo("Succès", "Hyper-V a été activé avec succès!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'activation de Hyper-V : {e}")

def create_vm(vm_name, memory_mb, cpu_count):
    try:
        # Commande PowerShell pour créer une machine virtuelle
        command = f"New-VM -Name {vm_name} -MemoryStartupBytes {memory_mb}MB -Generation 2 -Switch \"Default Switch\""

        # Exécuter la commande PowerShell
        subprocess.run(["powershell", "-Command", command], check=True)

        messagebox.showinfo("Succès", f"La machine virtuelle '{vm_name}' a été créée avec succès!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erreur", f"Erreur lors de la création de la machine virtuelle : {e}")

# Fonction pour activer Hyper-V
def on_enable_hyper_v():
    enable_hyper_v()

# Fonction pour créer la machine virtuelle
def on_create_vm():
    vm_name = entry_vm_name.get()
    memory_mb = int(entry_memory_mb.get())
    cpu_count = int(entry_cpu_count.get())
    create_vm(vm_name, memory_mb, cpu_count)

def start_vm(vm_name):
    try:
        # Commande PowerShell pour démarrer une machine virtuelle
        command = f"Start-VM -Name {vm_name}"

        # Exécuter la commande PowerShell
        subprocess.run(["powershell", "-Command", command], check=True)

        messagebox.showinfo("Succès", f"La machine virtuelle '{vm_name}' a été démarrée avec succès!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erreur", f"Erreur lors du démarrage de la machine virtuelle : {e}")

# Fonction pour allumer la machine virtuelle
def on_start_vm():
    vm_name = entry_vm_name.get()
    start_vm(vm_name)
    
def connect_to_vm(vm_name):
    try:
        # Commande pour ouvrir une connexion RDP vers la machine virtuelle
        command = f"Get-VM -Name {vm_name}"

        # Exécuter la commande
        subprocess.run(["powershell", "-Command", command], check=True)

        messagebox.showinfo("Succès", f"Connexion RDP à '{vm_name}' ouverte avec succès!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'ouverture de la connexion RDP : {e}")

# Fonction pour initier la connexion RDP à la VM
def on_connect_to_vm():
    vm_name = entry_vm_name.get()
    connect_to_vm(vm_name)

# Créer l'interface graphique avec Tkinter
root = tk.Tk()
root.title("Configuration de VM Hyper-V")

# Bouton pour activer Hyper-V
button_enable_hyper_v = tk.Button(root, text="Activer Hyper-V", command=on_enable_hyper_v)
button_enable_hyper_v.grid(row=0, column=0, columnspan=2, pady=10)

# Entrées pour la configuration de la VM
label_vm_name = tk.Label(root, text="Nom de la VM:")
label_vm_name.grid(row=1, column=0)
entry_vm_name = tk.Entry(root)
entry_vm_name.grid(row=1, column=1)

label_memory_mb = tk.Label(root, text="Mémoire (Mo):")
label_memory_mb.grid(row=2, column=0)
entry_memory_mb = tk.Entry(root)
entry_memory_mb.grid(row=2, column=1)

label_cpu_count = tk.Label(root, text="Nombre de CPU:")
label_cpu_count.grid(row=3, column=0)
entry_cpu_count = tk.Entry(root)
entry_cpu_count.grid(row=3, column=1)

# Bouton pour créer la VM
button_create_vm = tk.Button(root, text="Créer la VM", command=on_create_vm)
button_create_vm.grid(row=4, column=0, pady=10)

# Bouton pour allumer la VM
button_start_vm = tk.Button(root, text="Allumer la VM", command=on_start_vm)
button_start_vm.grid(row=4, column=1, pady=10)

# Bouton pour initier la connexion RDP
button_connect_to_vm = tk.Button(root, text="Connecter à la VM", command=on_connect_to_vm)
button_connect_to_vm.grid(row=5, column=0, columnspan=2, pady=10)


# Lancer l'application
root.mainloop()
