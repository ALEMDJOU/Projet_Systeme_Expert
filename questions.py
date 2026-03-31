class QuestionManager:
    """
    Gère le flux des questions posées à l'utilisateur.
    Supporte le filtrage par catégorie et l'exclusion de symptômes déjà détectés.
    """
    def __init__(self, symptoms_list):
        self.symptoms_list = symptoms_list
        self.asked_codes = set()
        self.active_category = None

    def set_category(self, category):
        """Définit la catégorie pour filtrer les questions."""
        self.active_category = category

    def exclude_codes(self, codes):
        """Marque des codes comme déjà traités (pré-activés par le TextAnalyzer)."""
        self.asked_codes.update(codes)

    def get_next_question(self):
        """
        Retourne le prochain symptôme et sa question.
        Si une catégorie est active, priorise les symptômes de cette catégorie.
        """
        # Phase 1 : Questions de la catégorie ciblée
        if self.active_category:
            for symptom in self.symptoms_list:
                if (symptom.category == self.active_category
                        and symptom.code not in self.asked_codes):
                    return symptom, f"Est-ce que vous remarquez : **{symptom.description}** ?"

        # Phase 2 : Questions des catégories proches (score > 0)
        for symptom in self.symptoms_list:
            if symptom.code not in self.asked_codes:
                return symptom, f"Est-ce que vous remarquez : **{symptom.description}** ?"

        return None, None

    def get_remaining_count(self):
        """Retourne le nombre de questions restantes."""
        if self.active_category:
            return sum(1 for s in self.symptoms_list
                       if s.category == self.active_category and s.code not in self.asked_codes)
        return sum(1 for s in self.symptoms_list if s.code not in self.asked_codes)

    def mark_as_asked(self, symptom_code):
        self.asked_codes.add(symptom_code)
