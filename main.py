# Para instalar a interface grafica:
# pip install customtkinter

import customtkinter as ctk


class HackLogicGame(ctk.CTk):
    """Jogo HackLogic: desafios de logica proposicional em uma interface visual."""

    def __init__(self):
        super().__init__()

        self.title("HackLogic")
        self.geometry("1100x720")
        self.minsize(980, 650)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.colors = {
            "bg": "#05080d",
            "panel": "#0d1821",
            "line": "#1f6f50",
            "green": "#35ff8d",
            "green_dark": "#128044",
            "blue": "#20a4f3",
            "blue_dark": "#123f63",
            "red": "#ff3b57",
            "yellow": "#ffd166",
            "text": "#e8f6ff",
            "muted": "#94a9ba",
            "terminal": "#06130c",
        }

        self.configure(fg_color=self.colors["bg"])
        self.show_start_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def make_button(self, parent, text, command, fg=None, hover=None, height=48):
        return ctk.CTkButton(
            parent,
            text=text,
            command=command,
            height=height,
            corner_radius=10,
            border_width=1,
            border_color=self.colors["line"],
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color=fg or self.colors["green_dark"],
            hover_color=hover or self.colors["green"],
            text_color=self.colors["text"],
        )

    def terminal_bar(self, parent, text):
        bar = ctk.CTkFrame(
            parent,
            fg_color=self.colors["terminal"],
            border_color=self.colors["line"],
            border_width=1,
            corner_radius=12,
        )
        bar.pack(fill="x", pady=(0, 14))

        ctk.CTkLabel(
            bar,
            text=text,
            font=ctk.CTkFont(family="Consolas", size=14, weight="bold"),
            text_color=self.colors["green"],
        ).pack(side="left", padx=16, pady=12)

        ctk.CTkLabel(
            bar,
            text="SESSION: ACTIVE",
            font=ctk.CTkFont(family="Consolas", size=12),
            text_color=self.colors["muted"],
        ).pack(side="right", padx=16)

    def show_start_screen(self):
        self.clear_screen()

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=34, pady=28)

        self.terminal_bar(container, "root@hacklogic:~$ ./start_invasion --logic-mode")

        hero = ctk.CTkFrame(
            container,
            fg_color=self.colors["panel"],
            border_color=self.colors["line"],
            border_width=2,
            corner_radius=18,
        )
        hero.pack(fill="both", expand=True)

        ctk.CTkLabel(
            hero,
            text="HACKLOGIC",
            font=ctk.CTkFont(family="Consolas", size=64, weight="bold"),
            text_color=self.colors["green"],
        ).pack(anchor="w", padx=36, pady=(52, 2))

        ctk.CTkLabel(
            hero,
            text="INVADA O SISTEMA USANDO LOGICA PROPOSICIONAL",
            font=ctk.CTkFont(family="Consolas", size=18, weight="bold"),
            text_color=self.colors["blue"],
        ).pack(anchor="w", padx=40, pady=(0, 26))

        ctk.CTkLabel(
            hero,
            text="Resolva desafios logicos para ultrapassar firewalls, decifrar protocolos e acessar o nucleo do sistema.",
            font=ctk.CTkFont(size=17),
            text_color=self.colors["muted"],
            wraplength=650,
            justify="left",
        ).pack(anchor="w", padx=40, pady=(0, 34))

        self.make_button(hero, "Iniciar invasao", self.start_game).pack(anchor="w", padx=40, ipadx=28)

    def start_game(self):
        self.clear_screen()
        page = ctk.CTkFrame(self, fg_color=self.colors["bg"])
        page.pack(fill="both", expand=True, padx=28, pady=22)
        self.terminal_bar(page, "root@hacklogic:~$ access_layer 1 --deduce")

        ctk.CTkLabel(
            page,
            text="Jogo em construcao",
            font=ctk.CTkFont(family="Consolas", size=32, weight="bold"),
            text_color=self.colors["green"],
        ).pack(expand=True)


if __name__ == "__main__":
    app = HackLogicGame()
    app.mainloop()
