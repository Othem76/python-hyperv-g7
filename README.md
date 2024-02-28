# Configuration de VM Hyper-V

Ce projet est une application Python qui utilise Tkinter pour créer une interface utilisateur graphique. L'application permet d'activer Hyper-V, de créer, de démarrer et de se connecter à une machine virtuelle Hyper-V.

## Prérequis

- Python 3.6 ou supérieur
- Tkinter
- PowerShell

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Installez Python 3.6 ou supérieur si ce n'est pas déjà fait.
3. Tkinter est inclus avec Python. Si vous avez installé Python à partir de la source, avec une distribution Linux qui ne l'inclut pas par défaut, vous devrez l'installer séparément.

## Utilisation

1. Ouvrez une invite de commande ou un terminal.
2. Naviguez jusqu'au répertoire où vous avez cloné ce dépôt.
3. Exécutez `python main.py` (ou `python3 main.py` si votre installation Python 3.x n'est pas la version par défaut).
4. L'interface utilisateur de l'application s'ouvrira.
5. Suivez les instructions à l'écran pour activer Hyper-V, créer une machine virtuelle, la démarrer et vous y connecter.

## Fonctionnalités

- **Activer Hyper-V** : Cette fonctionnalité permet d'activer Hyper-V sur votre machine en utilisant une commande PowerShell.
- **Créer une machine virtuelle** : Cette fonctionnalité permet de créer une nouvelle machine virtuelle Hyper-V avec le nom, la mémoire et le nombre de CPU spécifiés.
- **Démarrer une machine virtuelle** : Cette fonctionnalité permet de démarrer une machine virtuelle Hyper-V existante.
- **Se connecter à une machine virtuelle** : Cette fonctionnalité permet d'ouvrir une connexion RDP à une machine virtuelle Hyper-V existante.

## Avertissement

Ce script doit être exécuté avec des privilèges d'administrateur car l'activation de Hyper-V, la création et le démarrage de machines virtuelles nécessitent des privilèges d'administrateur.

## Participants

Ce projet a été réalisé par Théo Mouisse, Clément Mabile, Enzo Dupré et Maxime Millat.
GROUPE 7
