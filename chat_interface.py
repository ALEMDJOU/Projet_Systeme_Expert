# chat_interface.py

import customtkinter as ctk
import tkinter as tk
from inference_engine import InferenceEngine
from questions import QuestionManager
from knowledge_base import KnowledgeBase
from rules import RulesBase
from solutions import SolutionsSystem
from text_analyzer import TextAnalyzer
import re
from PIL import Image, ImageDraw

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ChatInterface:
    """
    Interface de chat pour le système expert hybride.
    Flux en 4 phases :
        1. Accueil — L'utilisateur décrit son problème en texte libre
        2. Analyse — Le TextAnalyzer détecte les symptômes et la catégorie
        3. Questions ciblées — Questions complémentaires filtrées par catégorie
        4. Diagnostic — Rapport final avec score de confiance
    """

    # ── PHASE CONSTANTS ──
    PHASE_WELCOME = "welcome"
    PHASE_ANALYZING = "analyzing"
    PHASE_DETAILS = "details"       # Demander si l'utilisateur a d'autres détails
    PHASE_QUESTIONS = "questions"
    PHASE_DONE = "done"

    def __init__(self, root):
        self.root = root
        self.root.title("Assistant Expert Informatique")
        self.root.geometry("850x950")
        self.root.configure(fg_color="#212121")

        self.engine = InferenceEngine(RulesBase.RULES)
        self.qm = QuestionManager(KnowledgeBase.SYMPTOMS)
        self.analyzer = TextAnalyzer()

        self.current_symptom = None
        self.phase = self.PHASE_WELCOME
        self.msg_widgets = []
        self.msg_containers = []

        self.setup_ui()
        self.start_conversation()

    # ─────────────────────────────────────────────
    #  UI SETUP
    # ─────────────────────────────────────────────

    def setup_ui(self):
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self.root, fg_color="#212121", corner_radius=0)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        self.content_area = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.content_area.grid(row=0, column=0, sticky="nsew")
        self.content_area.grid_columnconfigure(0, weight=1)
        self.content_area.grid_rowconfigure(0, weight=1)

        self.chat_frame = ctk.CTkScrollableFrame(
            self.content_area,
            corner_radius=0,
            fg_color="transparent",
            scrollbar_button_color="#424242",
            scrollbar_button_hover_color="#565656",
        )
        self.chat_frame.grid(row=0, column=0, sticky="nsew", padx=0)
        self.chat_frame.grid_columnconfigure(0, weight=1)

        self.input_outer = ctk.CTkFrame(self.content_area, fg_color="transparent")
        self.input_outer.grid(row=1, column=0, sticky="ew", pady=(10, 30), padx=0)
        self.input_outer.grid_columnconfigure(0, weight=1)

        self.input_container = ctk.CTkFrame(
            self.input_outer, height=54, corner_radius=27, fg_color="#2f2f2f"
        )
        self.input_container.grid(row=0, column=0, sticky="ew")
        self.input_container.grid_columnconfigure(0, weight=1)
        self.input_container.grid_propagate(False)

        self.entry = ctk.CTkEntry(
            self.input_container,
            placeholder_text="Décrivez votre problème informatique...",
            font=("Segoe UI", 16),
            border_width=0,
            corner_radius=0,
            fg_color="transparent",
            text_color="#ECECEC",
        )
        self.entry.grid(row=0, column=0, sticky="nsew", padx=(25, 10), pady=0)
        self.entry.bind("<Return>", self.handle_user_input)

        self.img_normal = self._create_arrow_image(hover=False)
        self.img_hover = self._create_arrow_image(hover=True)

        self.send_button = ctk.CTkLabel(
            self.input_container,
            text="",
            image=self.img_normal,
            cursor="hand2"
        )
        self.send_button.grid(row=0, column=1, padx=(0, 9), pady=9)

        self.send_button.bind("<Button-1>", self.handle_user_input)
        self.send_button.bind("<Enter>", lambda e: self.send_button.configure(image=self.img_hover))
        self.send_button.bind("<Leave>", lambda e: self.send_button.configure(image=self.img_normal))

        self.chat_frame.bind("<Configure>", self._on_chat_resize)

    def _create_arrow_image(self, hover=False):
        size = 128
        img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        bg_col = "#D1D1D1" if hover else "#FFFFFF"
        draw.ellipse([0, 0, size, size], fill=bg_col)
        draw.rounded_rectangle([52, 54, 76, 100], radius=8, fill="black")
        draw.polygon([(64, 24), (24, 60), (104, 60)], fill="black")
        img = img.resize((36, 36), Image.LANCZOS)
        return ctk.CTkImage(light_image=img, dark_image=img, size=(36, 36))

    # ─────────────────────────────────────────────
    #  RESIZE
    # ─────────────────────────────────────────────

    def _on_chat_resize(self, event):
        real_w = event.width
        if real_w < 50:
            return
        max_w = 850
        inner_pad = (real_w - max_w) // 2 if real_w > max_w else 10

        self.input_container.grid_configure(padx=inner_pad)
        for container in self.msg_containers:
            if container.winfo_exists():
                container.grid_configure(padx=inner_pad)

        usable_w = min(real_w - 20, max_w)
        wrap_u = int(usable_w * 0.82)
        wrap_ai = int(usable_w * 0.90)

        for widget, is_user in self.msg_widgets:
            if not widget.winfo_exists():
                continue
            limit = wrap_u if is_user else wrap_ai
            if isinstance(widget, ctk.CTkLabel):
                widget.configure(wraplength=limit)
            elif isinstance(widget, tk.Text):
                self._fit_text_height(widget)

    def _get_wrap_limits(self):
        w = self.chat_frame.winfo_width()
        w = w if w > 50 else 700
        usable_w = min(w - 20, 850)
        return int(usable_w * 0.82), int(usable_w * 0.90)

    # ─────────────────────────────────────────────
    #  RICH TEXT (Markdown **gras**)
    # ─────────────────────────────────────────────

    def _create_rich_text_widget(self, parent, bg_color, text_color, wrap_length):
        widget = tk.Text(
            parent,
            font=("Segoe UI", 16),
            fg=text_color,
            bg=bg_color,
            bd=0,
            highlightthickness=0,
            relief="flat",
            wrap="word",
            width=1,
            height=1,
            padx=0,
            pady=0,
            cursor="arrow",
            spacing1=2,
            spacing3=2,
        )
        widget.tag_configure("normal", font=("Segoe UI", 16))
        widget.tag_configure("bold", font=("Segoe UI", 16, "bold"))

        def _forward_scroll(event):
            if event.delta:
                self.chat_frame._parent_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            return "break"

        widget.bind("<MouseWheel>", _forward_scroll)
        widget.bind("<Button-4>", lambda e: self.chat_frame._parent_canvas.yview_scroll(-1, "units") or "break")
        widget.bind("<Button-5>", lambda e: self.chat_frame._parent_canvas.yview_scroll(1, "units") or "break")

        widget.configure(state="disabled")
        return widget

    def _animate_typing(self, widget, full_text, callback=None):
        self.is_typing = True
        self.entry.configure(state="disabled")

        tokens = []
        for part in re.split(r"(\*\*.*?\*\*)", full_text):
            if part.startswith("**") and part.endswith("**"):
                for char in part[2:-2]:
                    tokens.append((char, "bold"))
            else:
                for char in part:
                    tokens.append((char, "normal"))

        self._type_next_chunk(widget, tokens, 0, callback)

    def _type_next_chunk(self, widget, tokens, index, callback=None):
        if not widget.winfo_exists():
            return

        chunk_size = 3
        end_idx = min(index + chunk_size, len(tokens))

        widget.configure(state="normal")
        for i in range(index, end_idx):
            char, tag = tokens[i]
            widget.insert("end", char, tag)

        widget.configure(state="disabled")

        dl = widget.count("1.0", "end", "displaylines")
        real_lines = dl[0] if dl else int(widget.index("end-1c").split(".")[0])

        if widget.cget("height") != real_lines:
            widget.configure(height=real_lines)

        # Auto-scroll fluide pendant la frappe (toutes les 5 itérations)
        if index % 15 == 0 or end_idx >= len(tokens):
            self.root.update_idletasks()
            self.chat_frame._parent_canvas.yview_moveto(1.0)

        if end_idx < len(tokens):
            self.root.after(8, self._type_next_chunk, widget, tokens, end_idx, callback)
        else:
            self._fit_text_height(widget)
            self.is_typing = False
            if self.entry.winfo_exists():
                self.entry.configure(state="normal")
                self.entry.focus()
            if callback:
                self.root.after(100, callback)


    def _fit_text_height(self, widget):
        if widget.winfo_exists():
            widget.configure(state="normal")
            dl = widget.count("1.0", "end", "displaylines")
            real_lines = dl[0] if dl else int(widget.index("end-1c").split(".")[0])
            widget.configure(height=real_lines, state="disabled")

    # ─────────────────────────────────────────────
    #  MESSAGES
    # ─────────────────────────────────────────────

    def add_message(self, text, is_user=False, callback=None):
        wrap_u, wrap_ai = self._get_wrap_limits()

        msg_container = ctk.CTkFrame(self.chat_frame, fg_color="transparent")
        w = self.chat_frame.winfo_width()
        start_pad = (w - 850) // 2 if w > 850 else 10
        msg_container.grid(column=0, sticky="ew", pady=15, padx=start_pad)
        self.msg_containers.append(msg_container)

        if is_user:
            bubble = ctk.CTkFrame(msg_container, fg_color="#2f2f2f", corner_radius=20)
            bubble.pack(side="right")

            label = ctk.CTkLabel(
                bubble,
                text=text,
                font=("Segoe UI", 16),
                text_color="#ECECEC",
                wraplength=wrap_u,
                justify="left",
            )
            label.pack(padx=20, pady=12)
            self.msg_widgets.append((label, True))

        else:
            ai_wrapper = ctk.CTkFrame(msg_container, fg_color="transparent")
            ai_wrapper.pack(side="left", fill="x", expand=True)

            avatar_frame = ctk.CTkFrame(
                ai_wrapper, width=32, height=32, corner_radius=16, fg_color="#FFFFFF"
            )
            avatar_frame.pack(side="left", anchor="nw", padx=(0, 15))
            avatar_frame.pack_propagate(False)
            ctk.CTkLabel(
                avatar_frame, text="ES", font=("Segoe UI", 12, "bold"), text_color="#000000"
            ).place(relx=0.5, rely=0.5, anchor="center")

            rich_txt = self._create_rich_text_widget(
                parent=ai_wrapper,
                bg_color="#212121",
                text_color="#ECECEC",
                wrap_length=wrap_ai,
            )
            rich_txt.pack(side="left", anchor="nw", pady=(4, 0), fill="x", expand=True)
            self.msg_widgets.append((rich_txt, False))

            self._animate_typing(rich_txt, text, callback=callback)

        self.root.update_idletasks()
        self.chat_frame._parent_canvas.yview_moveto(1.0)

    # ─────────────────────────────────────────────
    #  LOGIQUE CONVERSATION HYBRIDE
    # ─────────────────────────────────────────────

    def start_conversation(self):
        self.phase = self.PHASE_WELCOME
        self.add_message(
            "Bonjour ! 👋 Je suis votre **Assistant Expert en Maintenance Informatique**.\n\n"
            "Décrivez-moi votre problème en quelques mots et je ferai un diagnostic.\n"
            "Par exemple : « Mon PC est lent et le ventilateur fait du bruit »"
        )

    def handle_user_input(self, event=None):
        if getattr(self, "is_typing", False):
            return

        user_text = self.entry.get().strip()
        if not user_text:
            return

        self.entry.delete(0, tk.END)
        self.add_message(user_text.capitalize(), is_user=True)

        self.root.after(500, lambda: self.process_response(user_text.lower()))

    def process_response(self, user_text):
        if self.phase == self.PHASE_WELCOME:
            self._handle_welcome(user_text)

        elif self.phase == self.PHASE_DETAILS:
            self._handle_details(user_text)

        elif self.phase == self.PHASE_QUESTIONS:
            self._handle_question_response(user_text)

        elif self.phase == self.PHASE_DONE:
            self.add_message(
                "L'analyse est clôturée. Veuillez redémarrer l'application pour un nouveau diagnostic."
            )

    # ── PHASE 1 : ACCUEIL ──

    def _handle_welcome(self, user_text):
        self.phase = self.PHASE_ANALYZING

        # Stocker la catégorie pour usage ultérieur
        self._pending_category = None

        # Analyse du texte libre
        detected_codes, best_category, category_scores = self.analyzer.analyze(user_text)

        if detected_codes:
            # Pré-activer les symptômes détectés dans le moteur
            self.engine.add_facts(detected_codes)
            self.qm.exclude_codes(detected_codes)
            self._pending_category = best_category

            # Descriptions humaines
            descriptions = self.analyzer.get_description_for_codes(detected_codes)
            symptoms_list = "\n".join([f"  • {d}" for d in descriptions])

            # Résumé + demande de détails supplémentaires
            summary = (
                f"J'ai analysé votre description et détecté **{len(detected_codes)} symptôme(s)** :\n"
                f"{symptoms_list}\n\n"
                f"**Catégorie principale :** {best_category}\n\n"
                f"Avez-vous d'**autres détails** à apporter avant que je commence "
                f"le diagnostic ? Si oui, décrivez-les. Sinon, tapez **non**."
            )
            self.phase = self.PHASE_DETAILS
            self.add_message(summary)
        else:
            # Aucun symptôme détecté → demander de reformuler ou passer en questions
            self.phase = self.PHASE_DETAILS
            self.add_message(
                "Je n'ai pas pu identifier de symptômes précis dans votre description.\n\n"
                "Pouvez-vous **donner plus de détails** sur le problème ?\n"
                "Sinon, tapez **non** et je poserai des questions ciblées."
            )

    # ── PHASE 1.5 : DÉTAILS SUPPLÉMENTAIRES ──

    def _handle_details(self, user_text):
        if user_text in ["non", "n", "no", "c'est tout", "rien", "pas d'autre", "rien d'autre"]:
            # L'utilisateur n'a plus rien à ajouter → questions ciblées
            if self._pending_category:
                self.qm.set_category(self._pending_category)
            self.phase = self.PHASE_QUESTIONS
            self.add_message(
                "Compris ! Je vais maintenant poser quelques questions complémentaires "
                "pour affiner le diagnostic.\n"
                "Répondez par **oui**, **non**, ou **je ne sais pas**.",
                callback=self.ask_next
            )
        else:
            # L'utilisateur donne plus de détails → analyser à nouveau
            detected_codes, best_category, _ = self.analyzer.analyze(user_text)
            if detected_codes:
                new_codes = detected_codes - self.engine.facts
                if new_codes:
                    self.engine.add_facts(new_codes)
                    self.qm.exclude_codes(new_codes)
                    if best_category and not self._pending_category:
                        self._pending_category = best_category

                    descriptions = self.analyzer.get_description_for_codes(new_codes)
                    extra_list = "\n".join([f"  • {d}" for d in descriptions])
                    self.add_message(
                        f"Bien noté ! J'ai détecté **{len(new_codes)} nouveau(x) symptôme(s)** :\n"
                        f"{extra_list}\n\n"
                        f"Autre chose à ajouter ? Sinon, tapez **non**."
                    )
                else:
                    self.add_message(
                        "Ces symptômes étaient déjà pris en compte.\n"
                        "Autre chose à ajouter ? Sinon, tapez **non**."
                    )
            else:
                self.add_message(
                    "Je n'ai pas détecté de nouveaux symptômes dans cette description.\n"
                    "Essayez de décrire autrement ou tapez **non** pour continuer."
                )

    # ── PHASE 2 : QUESTIONS CIBLÉES ──

    def ask_next(self):
        # Vérifier d'abord si on a des diagnostics
        if self.engine.get_diagnoses():
            self.finish_diagnosis()
            return

        symptom, question = self.qm.get_next_question()
        if symptom:
            self.current_symptom = symptom
            self.add_message(question)
        else:
            self.finish_diagnosis()

    def _handle_question_response(self, user_text):
        if self.current_symptom:
            if user_text in ["oui", "o", "yes", "y", "vrai"]:
                self.engine.add_fact(self.current_symptom.code)
                self.qm.mark_as_asked(self.current_symptom.code)

                if self.engine.get_diagnoses():
                    self.finish_diagnosis()
                    return

            elif user_text in ["non", "n", "no", "faux"]:
                self.qm.mark_as_asked(self.current_symptom.code)

            elif user_text in ["je ne sais pas", "jsp", "sais pas", "pas sûr", "aucune idée", "?"]:
                # On passe la question sans pénaliser
                self.qm.mark_as_asked(self.current_symptom.code)

            else:
                # Tenter d'analyser le texte libre même au milieu des questions
                detected_codes, _, _ = self.analyzer.analyze(user_text)
                if detected_codes:
                    self.engine.add_facts(detected_codes)
                    self.qm.exclude_codes(detected_codes)
                    descriptions = self.analyzer.get_description_for_codes(detected_codes)
                    extra = "\n".join([f"  • {d}" for d in descriptions])
                    self.add_message(
                        f"J'ai capté de nouveaux symptômes dans votre réponse :\n{extra}",
                        callback=self.ask_next
                    )
                    return
                else:
                    self.add_message(
                        "Je n'ai pas bien compris. Répondez par **oui**, **non**, ou **je ne sais pas**."
                    )
                    return

            self.ask_next()
        else:
            self.finish_diagnosis()

    # ── PHASE 3 : DIAGNOSTIC FINAL ──

    def finish_diagnosis(self):
        self.phase = self.PHASE_DONE
        diagnoses = self.engine.get_diagnoses()

        if not diagnoses:
            self.add_message(
                "Je n'ai pas identifié de panne matérielle ou logicielle évidente.\n"
                "L'ordinateur pourrait nécessiter un examen physique approfondi par un technicien."
            )
        else:
            sym_dict = {s.code: s.description for s in KnowledgeBase.SYMPTOMS}

            final_output = f"**Analyse terminée !** J'ai identifié **{len(diagnoses)} diagnostic(s)** :\n\n"

            for i, diag in enumerate(diagnoses, 1):
                solutions = SolutionsSystem.get_solutions(diag)
                confidence = self.engine.get_confidence_label(diag)

                symptom_codes = self.engine.explained_diagnoses.get(diag, [])
                symptoms_text = "\n".join([f"  • {sym_dict.get(code, code)}" for code in symptom_codes])

                final_output += f"━━━ **Diagnostic {i}** ━━━\n"
                final_output += f"**{diag}**\n"
                final_output += f"{confidence}\n\n"
                final_output += f"**Symptômes observés :**\n{symptoms_text}\n\n"
                final_output += f"🛠️ **Solution corrective :**\n{solutions['corrective']}\n\n"
                final_output += f"🩹 **Solution palliative :**\n{solutions['palliative']}\n\n"
                final_output += f"💡 **Prévention :**\n{solutions['preventive']}\n\n"

            self.add_message(final_output)

        self.current_symptom = None


if __name__ == "__main__":
    app_root = ctk.CTk()
    app = ChatInterface(app_root)
    app_root.mainloop()