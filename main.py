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
            "bg_2": "#08111a",
            "panel": "#0d1821",
            "panel_2": "#111f2b",
            "panel_3": "#172c38",
            "line": "#1f6f50",
            "green": "#35ff8d",
            "green_soft": "#83ffc2",
            "green_dark": "#128044",
            "blue": "#20a4f3",
            "blue_dark": "#123f63",
            "red": "#ff3b57",
            "red_dark": "#711728",
            "yellow": "#ffd166",
            "text": "#e8f6ff",
            "muted": "#94a9ba",
            "terminal": "#06130c",
        }

        self.configure(fg_color=self.colors["bg"])
        self.current_phase = 0
        self.alert = 0
        self.score = 0
        self.last_final_victory = None
        self.phases = self.create_phases()

        self.show_start_screen()

    def create_phases(self):
        """Dados das fases: aqui aparecem as proposicoes e conectivos do jogo."""
        return [
            {
                "title": "Camada 1: Porta Digital",
                "module": "GATE-01",
                "narrative": "O scanner achou uma porta digital isolada. O terminal retorna apenas uma negacao.",
                "concept": "Negacao",
                "propositions": [
                    "p = A porta digital esta aberta",
                    "Informacao recebida: ¬p e verdadeiro",
                ],
                "question": "Se ¬p e verdadeiro, o que podemos concluir?",
                "options": [
                    "A porta digital esta aberta.",
                    "A porta digital nao esta aberta.",
                    "A porta esta aberta e fechada ao mesmo tempo.",
                    "Nao ha conclusao possivel.",
                ],
                "correct": 1,
                "hint": "A negacao ¬p inverte o valor de p. Se ¬p e verdadeiro, p e falso.",
                "explanation": [
                    "p significa: A porta digital esta aberta.",
                    "A pista diz que ¬p e verdadeiro.",
                    "Logo, p e falso.",
                    "Conclusao: a porta digital nao esta aberta.",
                ],
                "connectives": "¬",
                "log": ["scan porta: ativo", "flag p: bloqueada", "negacao detectada"],
            },
            {
                "title": "Camada 2: Validador de Credenciais",
                "module": "AUTH-02",
                "narrative": "A autenticacao pede senha e token ao mesmo tempo. Um dos dois sozinho nao abre nada.",
                "concept": "Conjuncao",
                "propositions": [
                    "p = A senha esta correta",
                    "q = O token foi validado",
                    "Expressao: p ∧ q",
                ],
                "question": "Quando p ∧ q e verdadeiro?",
                "options": [
                    "Quando apenas p e verdadeiro.",
                    "Quando apenas q e verdadeiro.",
                    "Quando p e q sao verdadeiros.",
                    "Quando p e q sao falsos.",
                ],
                "correct": 2,
                "hint": "Na conjuncao, as duas partes precisam ser verdadeiras.",
                "explanation": [
                    "p ∧ q significa: p e q acontecem ao mesmo tempo.",
                    "Se uma das partes for falsa, a conjuncao inteira e falsa.",
                    "Portanto, p ∧ q so e verdadeiro quando p e q sao verdadeiros.",
                ],
                "connectives": "∧",
                "log": ["auth handshake", "senha + token exigidos", "porta AND ativa"],
            },
            {
                "title": "Camada 3: Rota Alternativa",
                "module": "ROUTE-03",
                "narrative": "O firewall aceita duas rotas de entrada. Uma brecha valida ja basta para continuar.",
                "concept": "Disjuncao",
                "propositions": [
                    "p = O firewall foi desativado",
                    "q = A chave mestra foi encontrada",
                    "Expressao: p ∨ q",
                ],
                "question": "Quando p ∨ q e verdadeiro?",
                "options": [
                    "Somente quando p e q sao falsos.",
                    "Quando pelo menos uma das proposicoes e verdadeira.",
                    "Somente quando p e q sao verdadeiros.",
                    "Nunca, pois disjuncao sempre falha.",
                ],
                "correct": 1,
                "hint": "Na disjuncao inclusiva, uma proposicao verdadeira ja basta.",
                "explanation": [
                    "p ∨ q significa: p ou q.",
                    "A disjuncao e verdadeira quando p e verdadeiro, quando q e verdadeiro, ou quando ambos sao verdadeiros.",
                    "Ela so e falsa quando p e q sao falsos.",
                ],
                "connectives": "∨",
                "log": ["mapa de rotas carregado", "OR gateway online", "brecha alternativa detectada"],
            },
            {
                "title": "Camada 4: Protocolo Condicional",
                "module": "RULE-04",
                "narrative": "O sistema promete liberar acesso se as credenciais forem aceitas. Procure a unica falha possivel.",
                "concept": "Implicacao",
                "propositions": [
                    "p = O hacker possui credenciais",
                    "q = O acesso e liberado",
                    "Expressao: p → q",
                ],
                "question": "Em qual caso p → q e falso?",
                "options": [
                    "Quando p e verdadeiro e q e verdadeiro.",
                    "Quando p e falso e q e verdadeiro.",
                    "Quando p e falso e q e falso.",
                    "Quando p e verdadeiro e q e falso.",
                ],
                "correct": 3,
                "hint": "A implicacao so falha quando a promessa e quebrada: p acontece, mas q nao acontece.",
                "explanation": [
                    "p → q significa: se p, entao q.",
                    "A unica situacao falsa ocorre quando p e verdadeiro e q e falso.",
                    "Ou seja: o hacker possui credenciais, mas o acesso nao e liberado.",
                ],
                "connectives": "→",
                "log": ["regra condicional interceptada", "se credencial entao acesso", "validando tabela verdade"],
            },
            {
                "title": "Camada 5: Criptografia De Morgan",
                "module": "CRYPT-05",
                "narrative": "O algoritmo embaralha negacoes e conectivos. Reconheca a equivalencia para decifrar a camada.",
                "concept": "Leis de De Morgan e equivalencia",
                "propositions": [
                    "p = O sensor A detectou invasao",
                    "q = O sensor B detectou invasao",
                    "Expressao: ¬(p ∧ q)",
                ],
                "question": "Qual expressao e logicamente equivalente a ¬(p ∧ q)?",
                "options": [
                    "¬p ∧ ¬q",
                    "¬p ∨ ¬q",
                    "p ∨ q",
                    "p ↔ q",
                ],
                "correct": 1,
                "hint": "De Morgan troca a conjuncao por disjuncao quando a negacao entra nos parenteses.",
                "explanation": [
                    "A Lei de De Morgan diz: ¬(p ∧ q) ≡ ¬p ∨ ¬q.",
                    "Isso significa que nao e verdade que ambos os sensores detectaram invasao.",
                    "Logo, pelo menos um deles nao detectou invasao.",
                ],
                "connectives": "¬, ∧, ∨, ≡",
                "log": ["pacote criptografado", "negacao externa encontrada", "equivalencia em analise"],
            },
            {
                "title": "Camada 6: Nucleo Central",
                "module": "CORE-06",
                "narrative": "O nucleo combina regras, inferencias e equivalencias. Um erro aqui aciona bloqueio total.",
                "concept": "Caso completo com Modus Tollens e bicondicional",
                "propositions": [
                    "p = O hacker quebrou a senha principal",
                    "q = O token biometrico foi clonado",
                    "r = O acesso ao nucleo foi liberado",
                    "s = O modo stealth esta ativo",
                    "Regras: (p ∧ q) → r, ¬r, p, s ↔ p",
                ],
                "question": "Qual conclusao pode ser feita a partir das regras?",
                "options": [
                    "O token biometrico nao foi clonado.",
                    "O acesso ao nucleo foi liberado.",
                    "A senha principal nao foi quebrada.",
                    "A regra (p ∧ q) → r e falsa.",
                ],
                "correct": 0,
                "hint": "Use Modus Tollens: se (p ∧ q) levaria a r, mas r e falso, entao p ∧ q nao pode ser verdadeiro.",
                "explanation": [
                    "Temos a regra (p ∧ q) → r.",
                    "Tambem sabemos ¬r, ou seja, r e falso.",
                    "Pelo Modus Tollens, concluimos ¬(p ∧ q).",
                    "Como p e verdadeiro, q precisa ser falso.",
                    "Logo, o token biometrico nao foi clonado.",
                    "A regra s ↔ p mostra bicondicional: como p e verdadeiro, s tambem e verdadeiro.",
                ],
                "connectives": "¬, ∧, ∨, →, ↔, ≡",
                "log": ["core protegido", "modus tollens requerido", "bicondicional sincronizado"],
            },
        ]

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

    def create_card(self, parent, title=None, border=None, fg=None):
        card = ctk.CTkFrame(
            parent,
            fg_color=fg or self.colors["panel"],
            border_width=1,
            border_color=border or self.colors["line"],
            corner_radius=14,
        )
        if title:
            ctk.CTkLabel(
                card,
                text=title,
                font=ctk.CTkFont(size=17, weight="bold"),
                text_color=self.colors["green"],
            ).pack(anchor="w", padx=16, pady=(14, 6))
        return card

    def terminal_bar(self, parent, text):
        bar = ctk.CTkFrame(parent, fg_color=self.colors["terminal"], border_color=self.colors["line"], border_width=1, corner_radius=12)
        bar.pack(fill="x", pady=(0, 14))

        dots = ctk.CTkFrame(bar, fg_color="transparent")
        dots.pack(side="left", padx=14, pady=12)
        for color in (self.colors["red"], self.colors["yellow"], self.colors["green"]):
            ctk.CTkLabel(dots, text="●", text_color=color, font=ctk.CTkFont(size=13)).pack(side="left", padx=2)

        ctk.CTkLabel(
            bar,
            text=text,
            font=ctk.CTkFont(family="Consolas", size=14, weight="bold"),
            text_color=self.colors["green_soft"],
        ).pack(side="left", padx=8)

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

        body = ctk.CTkFrame(container, fg_color="transparent")
        body.pack(fill="both", expand=True)
        body.grid_columnconfigure(0, weight=1)
        body.grid_columnconfigure(1, weight=0)
        body.grid_rowconfigure(0, weight=1)

        hero = ctk.CTkFrame(
            body,
            fg_color=self.colors["panel"],
            border_color=self.colors["line"],
            border_width=2,
            corner_radius=18,
        )
        hero.grid(row=0, column=0, sticky="nsew", padx=(0, 18))

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

        ascii_panel = ctk.CTkFrame(hero, fg_color=self.colors["terminal"], border_color=self.colors["green_dark"], border_width=1, corner_radius=10)
        ascii_panel.pack(fill="x", padx=38, pady=(0, 26))

        terminal_text = (
            "> firewall detectado\n"
            "> carregando conectivos: ¬  ∧  ∨  →  ↔\n"
            "> protocolo academico: ON\n"
            "> resolva os desafios para acessar o nucleo"
        )
        ctk.CTkLabel(
            ascii_panel,
            text=terminal_text,
            font=ctk.CTkFont(family="Consolas", size=16),
            text_color=self.colors["green_soft"],
            justify="left",
        ).pack(anchor="w", padx=20, pady=18)

        ctk.CTkLabel(
            hero,
            text="Resolva desafios logicos para ultrapassar firewalls, decifrar protocolos e acessar o nucleo do sistema.",
            font=ctk.CTkFont(size=17),
            text_color=self.colors["muted"],
            wraplength=650,
            justify="left",
        ).pack(anchor="w", padx=40, pady=(0, 34))

        buttons = ctk.CTkFrame(hero, fg_color="transparent")
        buttons.pack(anchor="w", padx=40, pady=(0, 30))
        self.make_button(buttons, "🔐 Iniciar invasao", self.start_game, fg=self.colors["green_dark"]).pack(side="left", ipadx=28, padx=(0, 12))
        self.make_button(buttons, "🧠 Ver logica do jogo", self.show_logic_screen, fg=self.colors["blue_dark"], hover=self.colors["blue"]).pack(side="left", ipadx=20)

        side = self.create_card(body, "STATUS DO SISTEMA", border=self.colors["blue"], fg=self.colors["panel_2"])
        side.grid(row=0, column=1, sticky="ns", ipadx=8)

        status_items = [
            ("ALERTA", "0%"),
            ("CAMADAS", str(len(self.phases))),
            ("MODO", "STEALTH"),
            ("LOGICA", "ATIVA"),
            ("BANCO DE DADOS", "OFF"),
        ]
        for label, value in status_items:
            box = ctk.CTkFrame(side, fg_color=self.colors["terminal"], corner_radius=8)
            box.pack(fill="x", padx=16, pady=7)
            ctk.CTkLabel(box, text=label, font=ctk.CTkFont(family="Consolas", size=12), text_color=self.colors["muted"]).pack(anchor="w", padx=12, pady=(8, 0))
            ctk.CTkLabel(box, text=value, font=ctk.CTkFont(family="Consolas", size=22, weight="bold"), text_color=self.colors["green"]).pack(anchor="w", padx=12, pady=(0, 8))

        ctk.CTkLabel(
            side,
            text="Falhas elevam o alerta em 25%.\nAo chegar a 100%, a sessao e bloqueada.",
            font=ctk.CTkFont(size=13),
            text_color=self.colors["yellow"],
            wraplength=220,
            justify="left",
        ).pack(padx=16, pady=(16, 20))

    def start_game(self):
        self.current_phase = 0
        self.alert = 0
        self.score = 0
        self.last_final_victory = None
        self.show_phase_screen()

    def header(self, parent):
        self.terminal_bar(parent, f"root@hacklogic:~$ access_layer {self.current_phase + 1} --deduce")

        header = ctk.CTkFrame(parent, fg_color=self.colors["panel_2"], corner_radius=12, border_width=1, border_color=self.colors["line"])
        header.pack(fill="x", pady=(0, 14))

        ctk.CTkLabel(
            header,
            text=f"🔐 Camada {self.current_phase + 1}/{len(self.phases)}",
            font=ctk.CTkFont(family="Consolas", size=16, weight="bold"),
            text_color=self.colors["green"],
        ).pack(side="left", padx=16, pady=13)

        ctk.CTkLabel(
            header,
            text=f"Pontuacao: {self.score}",
            font=ctk.CTkFont(family="Consolas", size=15, weight="bold"),
            text_color=self.colors["text"],
        ).pack(side="left", padx=18)

        alert_frame = ctk.CTkFrame(header, fg_color="transparent")
        alert_frame.pack(side="right", padx=16, pady=9)

        alert_color = self.colors["red"] if self.alert >= 50 else self.colors["yellow"]
        ctk.CTkLabel(
            alert_frame,
            text=f"⚠ ALERTA {self.alert}%",
            font=ctk.CTkFont(family="Consolas", size=14, weight="bold"),
            text_color=alert_color,
        ).pack(anchor="e")

        progress = ctk.CTkProgressBar(alert_frame, width=210, progress_color=self.colors["red"], fg_color="#1a2630")
        progress.set(self.alert / 100)
        progress.pack(pady=(5, 0))

    def sidebar(self, parent):
        side = ctk.CTkFrame(parent, fg_color=self.colors["panel"], border_color=self.colors["blue_dark"], border_width=1, corner_radius=14, width=240)
        side.grid(row=0, column=0, sticky="nsew", padx=(0, 16))
        side.grid_propagate(False)

        ctk.CTkLabel(
            side,
            text="MAPA DE INVASAO",
            font=ctk.CTkFont(family="Consolas", size=15, weight="bold"),
            text_color=self.colors["blue"],
        ).pack(anchor="w", padx=16, pady=(16, 10))

        for index, phase in enumerate(self.phases):
            active = index == self.current_phase
            done = index < self.current_phase
            color = self.colors["green"] if active else self.colors["green_soft"] if done else self.colors["muted"]
            fg = self.colors["terminal"] if active else "transparent"
            row = ctk.CTkFrame(side, fg_color=fg, corner_radius=8)
            row.pack(fill="x", padx=12, pady=3)
            marker = ">" if active else "✓" if done else "·"
            ctk.CTkLabel(
                row,
                text=f"{marker} {phase['module']}",
                font=ctk.CTkFont(family="Consolas", size=14, weight="bold"),
                text_color=color,
            ).pack(anchor="w", padx=12, pady=8)

        log_card = ctk.CTkFrame(side, fg_color=self.colors["terminal"], corner_radius=10, border_width=1, border_color=self.colors["line"])
        log_card.pack(fill="x", padx=12, pady=(18, 12))
        ctk.CTkLabel(log_card, text="LIVE LOG", font=ctk.CTkFont(family="Consolas", size=13, weight="bold"), text_color=self.colors["green"]).pack(anchor="w", padx=12, pady=(12, 4))

        for item in self.phases[self.current_phase]["log"]:
            ctk.CTkLabel(
                log_card,
                text=f"[ok] {item}",
                font=ctk.CTkFont(family="Consolas", size=12),
                text_color=self.colors["green_soft"],
                wraplength=190,
                justify="left",
            ).pack(anchor="w", padx=12, pady=2)

    def show_phase_screen(self):
        self.clear_screen()
        self.last_final_victory = None
        phase = self.phases[self.current_phase]

        page = ctk.CTkFrame(self, fg_color=self.colors["bg"])
        page.pack(fill="both", expand=True, padx=24, pady=20)

        self.header(page)

        content = ctk.CTkFrame(page, fg_color="transparent")
        content.pack(fill="both", expand=True)
        content.grid_columnconfigure(0, weight=0)
        content.grid_columnconfigure(1, weight=1)
        content.grid_rowconfigure(0, weight=1)

        self.sidebar(content)

        main = ctk.CTkScrollableFrame(content, fg_color="transparent")
        main.grid(row=0, column=1, sticky="nsew")

        title_card = self.create_card(main, border=self.colors["blue"])
        title_card.pack(fill="x", pady=(0, 12))
        ctk.CTkLabel(
            title_card,
            text=f"{phase['module']} // {phase['title']}",
            font=ctk.CTkFont(family="Consolas", size=25, weight="bold"),
            text_color=self.colors["green"],
        ).pack(anchor="w", padx=18, pady=(16, 5))
        ctk.CTkLabel(
            title_card,
            text=phase["narrative"],
            font=ctk.CTkFont(size=15),
            text_color=self.colors["muted"],
            wraplength=760,
            justify="left",
        ).pack(anchor="w", padx=18, pady=(0, 16))

        logic_card = self.create_card(main, "PACOTE LOGICO INTERCEPTADO")
        logic_card.pack(fill="x", pady=(0, 12))

        ctk.CTkLabel(
            logic_card,
            text=f"Conceito: {phase['concept']}",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.colors["text"],
        ).pack(anchor="w", padx=18, pady=(4, 8))

        for proposition in phase["propositions"]:
            line = ctk.CTkFrame(logic_card, fg_color=self.colors["terminal"], corner_radius=7)
            line.pack(fill="x", padx=18, pady=3)
            ctk.CTkLabel(
                line,
                text=f"$ {proposition}",
                font=ctk.CTkFont(family="Consolas", size=14),
                text_color=self.colors["green_soft"],
                wraplength=740,
                justify="left",
            ).pack(anchor="w", padx=12, pady=7)

        ctk.CTkLabel(
            logic_card,
            text=f"Conectivos usados: {phase['connectives']}",
            font=ctk.CTkFont(family="Consolas", size=15, weight="bold"),
            text_color=self.colors["yellow"],
        ).pack(anchor="w", padx=18, pady=(10, 16))

        question_card = self.create_card(main, "DESAFIO DE AUTENTICACAO")
        question_card.pack(fill="x", pady=(0, 12))

        ctk.CTkLabel(
            question_card,
            text=phase["question"],
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.colors["text"],
            wraplength=760,
            justify="left",
        ).pack(anchor="w", padx=18, pady=(6, 14))

        for index, option in enumerate(phase["options"]):
            button = ctk.CTkButton(
                question_card,
                text=f"{index + 1}. {option}",
                command=lambda i=index: self.verify_answer(i),
                height=45,
                corner_radius=8,
                border_width=1,
                border_color=self.colors["blue_dark"],
                fg_color="#132532",
                hover_color=self.colors["green_dark"],
                text_color=self.colors["text"],
                font=ctk.CTkFont(size=14, weight="bold"),
                anchor="w",
            )
            button.pack(fill="x", padx=18, pady=5)

        tools = ctk.CTkFrame(main, fg_color="transparent")
        tools.pack(fill="x", pady=(4, 12))
        self.make_button(tools, "💡 Dica", self.show_hint, fg=self.colors["blue_dark"], hover=self.colors["blue"], height=42).pack(side="left", padx=(0, 10), ipadx=14)
        self.make_button(tools, "🧠 Ver logica do jogo", self.show_logic_screen, fg="#263544", hover="#34485d", height=42).pack(side="left", ipadx=12)

    def verify_answer(self, selected_index):
        phase = self.phases[self.current_phase]
        is_correct = selected_index == phase["correct"]

        if is_correct:
            self.score += 100
            status = "✅ Acesso parcial concedido"
        else:
            self.alert += 25
            status = "⚠ Erro de autenticacao logica"

        self.show_explanation(is_correct, status)

    def show_hint(self):
        phase = self.phases[self.current_phase]
        dialog = ctk.CTkToplevel(self)
        dialog.title("Dica")
        dialog.geometry("560x280")
        dialog.configure(fg_color=self.colors["bg"])
        dialog.transient(self)
        dialog.grab_set()

        card = self.create_card(dialog, "💡 DICA DO SISTEMA", border=self.colors["yellow"])
        card.pack(fill="both", expand=True, padx=22, pady=22)

        ctk.CTkLabel(
            card,
            text=f"> hint --layer {self.current_phase + 1}",
            font=ctk.CTkFont(family="Consolas", size=14, weight="bold"),
            text_color=self.colors["green"],
        ).pack(anchor="w", padx=18, pady=(4, 4))

        ctk.CTkLabel(
            card,
            text=phase["hint"],
            font=ctk.CTkFont(size=17),
            text_color=self.colors["text"],
            wraplength=470,
            justify="left",
        ).pack(expand=True, padx=18, pady=12)

        self.make_button(card, "Entendi", dialog.destroy, height=40).pack(pady=(0, 18), ipadx=20)

    def show_explanation(self, is_correct, status):
        self.clear_screen()
        phase = self.phases[self.current_phase]
        correct_text = phase["options"][phase["correct"]]

        page = ctk.CTkScrollableFrame(self, fg_color=self.colors["bg"])
        page.pack(fill="both", expand=True, padx=28, pady=22)

        self.header(page)

        border = self.colors["green"] if is_correct else self.colors["red"]
        card = self.create_card(page, border=border)
        card.pack(fill="both", expand=True)

        status_color = self.colors["green"] if is_correct else self.colors["red"]
        ctk.CTkLabel(
            card,
            text=status,
            font=ctk.CTkFont(family="Consolas", size=30, weight="bold"),
            text_color=status_color,
        ).pack(anchor="w", padx=24, pady=(24, 8))

        terminal = ctk.CTkFrame(card, fg_color=self.colors["terminal"], corner_radius=10, border_width=1, border_color=border)
        terminal.pack(fill="x", padx=24, pady=(4, 16))

        if is_correct:
            log_text = "> auth_result: TRUE\n> acesso parcial concedido\n> preparando proxima camada"
        else:
            log_text = (
                "> auth_result: FALSE\n"
                f"> nivel_alerta: {self.alert}%\n"
                "> firewall reagindo a tentativa de invasao"
            )

        ctk.CTkLabel(
            terminal,
            text=log_text,
            font=ctk.CTkFont(family="Consolas", size=15),
            text_color=self.colors["green_soft"] if is_correct else self.colors["yellow"],
            justify="left",
        ).pack(anchor="w", padx=16, pady=14)

        ctk.CTkLabel(
            card,
            text=f"Resposta correta: {correct_text}",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=self.colors["text"],
            wraplength=860,
            justify="left",
        ).pack(anchor="w", padx=24, pady=(2, 14))

        ctk.CTkLabel(
            card,
            text="Raciocinio passo a passo:",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=self.colors["green"],
        ).pack(anchor="w", padx=24, pady=(8, 8))

        for step in phase["explanation"]:
            ctk.CTkLabel(
                card,
                text=f"• {step}",
                font=ctk.CTkFont(size=15),
                text_color=self.colors["muted"],
                wraplength=860,
                justify="left",
            ).pack(anchor="w", padx=34, pady=3)

        ctk.CTkLabel(
            card,
            text=f"Conectivos usados nesta camada: {phase['connectives']}",
            font=ctk.CTkFont(family="Consolas", size=16, weight="bold"),
            text_color=self.colors["yellow"],
        ).pack(anchor="w", padx=24, pady=(18, 18))

        next_text = "Ver resultado" if self.alert >= 100 or self.current_phase == len(self.phases) - 1 else "Proxima camada"
        self.make_button(card, f"🔐 {next_text}", self.next_phase, height=48).pack(anchor="e", padx=24, pady=(6, 24), ipadx=18)

    def next_phase(self):
        if self.alert >= 100:
            self.show_final_screen(victory=False)
            return

        self.current_phase += 1
        if self.current_phase >= len(self.phases):
            self.show_final_screen(victory=True)
        else:
            self.show_phase_screen()

    def show_logic_screen(self):
        self.clear_screen()

        page = ctk.CTkScrollableFrame(self, fg_color=self.colors["bg"])
        page.pack(fill="both", expand=True, padx=28, pady=22)

        self.terminal_bar(page, "root@hacklogic:~$ cat /docs/logica_proposicional.md")

        card = self.create_card(page, border=self.colors["blue"])
        card.pack(fill="both", expand=True)

        ctk.CTkLabel(
            card,
            text="🧠 Logica do HackLogic",
            font=ctk.CTkFont(family="Consolas", size=32, weight="bold"),
            text_color=self.colors["green"],
        ).pack(anchor="w", padx=24, pady=(24, 8))

        intro = (
            "Nesta tela esta a parte academica do jogo. Cada camada usa conceitos de logica "
            "proposicional para transformar pistas em conclusoes."
        )
        ctk.CTkLabel(
            card,
            text=intro,
            font=ctk.CTkFont(size=16),
            text_color=self.colors["muted"],
            wraplength=900,
            justify="left",
        ).pack(anchor="w", padx=24, pady=(0, 18))

        topics = [
            ("Proposicao", "E uma frase declarativa que pode ser verdadeira ou falsa. Exemplo: p = A senha esta correta."),
            ("Negacao: ¬p", "Inverte o valor logico de p. Se p e verdadeiro, ¬p e falso; se p e falso, ¬p e verdadeiro."),
            ("Conjuncao: p ∧ q", "So e verdadeira quando p e q sao verdadeiros ao mesmo tempo."),
            ("Disjuncao: p ∨ q", "E verdadeira quando pelo menos uma das proposicoes e verdadeira."),
            ("Implicacao: p → q", "Significa se p, entao q. So e falsa quando p e verdadeiro e q e falso."),
            ("Bicondicional: p ↔ q", "Indica que p e q possuem o mesmo valor logico: ambas verdadeiras ou ambas falsas."),
            ("Equivalencia logica", "Duas expressoes sao equivalentes quando tem sempre o mesmo valor de verdade."),
            ("Leis de De Morgan", "¬(p ∧ q) ≡ ¬p ∨ ¬q e ¬(p ∨ q) ≡ ¬p ∧ ¬q."),
            ("Modus Ponens", "De p → q e p verdadeiro, concluimos q verdadeiro."),
            ("Modus Tollens", "De p → q e ¬q verdadeiro, concluimos ¬p verdadeiro."),
        ]

        grid = ctk.CTkFrame(card, fg_color="transparent")
        grid.pack(fill="x", padx=20, pady=4)
        grid.grid_columnconfigure(0, weight=1)
        grid.grid_columnconfigure(1, weight=1)

        for index, (title, text) in enumerate(topics):
            topic_card = ctk.CTkFrame(grid, fg_color=self.colors["panel_2"], corner_radius=10, border_width=1, border_color=self.colors["blue_dark"])
            topic_card.grid(row=index // 2, column=index % 2, sticky="nsew", padx=5, pady=5)
            ctk.CTkLabel(
                topic_card,
                text=title,
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color=self.colors["green"],
            ).pack(anchor="w", padx=14, pady=(12, 2))
            ctk.CTkLabel(
                topic_card,
                text=text,
                font=ctk.CTkFont(size=13),
                text_color=self.colors["text"],
                wraplength=410,
                justify="left",
            ).pack(anchor="w", padx=14, pady=(0, 12))

        appearances = (
            "Como aparece nas fases: Camada 1 usa negacao; Camada 2 usa conjuncao; "
            "Camada 3 usa disjuncao; Camada 4 usa implicacao; Camada 5 usa De Morgan "
            "e equivalencia; Camada 6 mistura conectivos, bicondicional e Modus Tollens."
        )
        ctk.CTkLabel(
            card,
            text=appearances,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.colors["yellow"],
            wraplength=900,
            justify="left",
        ).pack(anchor="w", padx=24, pady=(18, 20))

        if self.last_final_victory is not None:
            back_command = lambda: self.show_final_screen(self.last_final_victory)
        elif self.current_phase == 0 and self.score == 0 and self.alert == 0:
            back_command = self.show_start_screen
        else:
            back_command = self.show_phase_screen
        self.make_button(card, "Voltar", back_command, height=44).pack(anchor="e", padx=24, pady=(0, 24), ipadx=24)

    def show_final_screen(self, victory):
        self.clear_screen()
        self.last_final_victory = victory

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=36, pady=28)

        command = "cat /core/access_granted.log" if victory else "cat /security/blocked_session.log"
        self.terminal_bar(container, f"root@hacklogic:~$ {command}")

        card = ctk.CTkFrame(
            container,
            fg_color=self.colors["panel"],
            border_color=self.colors["green"] if victory else self.colors["red"],
            border_width=2,
            corner_radius=18,
        )
        card.pack(fill="both", expand=True)

        if victory:
            title = "✅ Sistema invadido com sucesso!"
            message = "Voce usou logica proposicional para atravessar todas as camadas de seguranca."
            terminal = "> core: unlocked\n> logic_score: accepted\n> session: victorious"
            color = self.colors["green"]
        else:
            title = "⚠ Invasao bloqueada"
            message = "O alerta chegou a 100%. O sistema encerrou sua sessao antes do acesso ao nucleo."
            terminal = "> core: locked\n> alert: 100%\n> session: terminated"
            color = self.colors["red"]

        ctk.CTkLabel(
            card,
            text=title,
            font=ctk.CTkFont(family="Consolas", size=36, weight="bold"),
            text_color=color,
        ).pack(pady=(58, 14))

        terminal_box = ctk.CTkFrame(card, fg_color=self.colors["terminal"], corner_radius=10, border_width=1, border_color=color)
        terminal_box.pack(padx=70, pady=(0, 22), fill="x")
        ctk.CTkLabel(
            terminal_box,
            text=terminal,
            font=ctk.CTkFont(family="Consolas", size=17),
            text_color=self.colors["green_soft"] if victory else self.colors["yellow"],
            justify="left",
        ).pack(anchor="w", padx=20, pady=18)

        ctk.CTkLabel(
            card,
            text=message,
            font=ctk.CTkFont(size=18),
            text_color=self.colors["text"],
            wraplength=760,
            justify="center",
        ).pack(pady=(0, 22))

        ctk.CTkLabel(
            card,
            text=f"Pontuacao final: {self.score}   |   Alerta final: {self.alert}%",
            font=ctk.CTkFont(family="Consolas", size=20, weight="bold"),
            text_color=self.colors["yellow"],
        ).pack(pady=(0, 30))

        self.make_button(card, "🔁 Tentar novamente", self.start_game, height=48).pack(pady=7, ipadx=24)
        self.make_button(card, "🧠 Ver logica do jogo", self.show_logic_screen, fg=self.colors["blue_dark"], hover=self.colors["blue"], height=46).pack(pady=7, ipadx=18)


if __name__ == "__main__":
    app = HackLogicGame()
    app.mainloop()


# Instrucoes de execucao:
# 1. pip install customtkinter
# 2. python main.py
#
# Conceitos logicos usados no jogo:
# - Proposicoes: frases que podem ser verdadeiras ou falsas.
# - Negacao (¬p): usada na Camada 1 e no caso final.
# - Conjuncao (p ∧ q): usada na Camada 2 e no caso final.
# - Disjuncao (p ∨ q): usada na Camada 3 e nas equivalencias de De Morgan.
# - Implicacao (p → q): usada na Camada 4 e no caso final.
# - Bicondicional (p ↔ q): usado na Camada 6.
# - Equivalencia logica (≡): usada nas Leis de De Morgan.
# - Modus Tollens: usado no caso final para concluir que o token nao foi clonado.
