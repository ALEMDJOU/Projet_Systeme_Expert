import customtkinter as ctk
from chat_interface import ChatInterface

def main():
    """
    Point d'entrée principal de l'expert system.
    Lance directement l'interface de chat.
    """
    root = ctk.CTk()
    
    # Stylisation optionnelle si possible (selon l'OS)
    try:
        # Sur Windows, on peut essayer d'activer le rendu DPI haute résolution
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass
        
    app = ChatInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
