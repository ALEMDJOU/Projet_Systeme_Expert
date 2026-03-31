# text_analyzer.py

from knowledge_base import KnowledgeBase


class TextAnalyzer:
    """
    Analyseur de texte libre.
    Détecte les symptômes et la catégorie probable à partir d'une description
    en langage naturel fournie par l'utilisateur.
    """

    def __init__(self):
        self.symptoms = KnowledgeBase.SYMPTOMS

    def analyze(self, user_text):
        """
        Analyse le texte de l'utilisateur.
        Retourne:
            detected_codes: set() de codes de symptômes détectés
            category_scores: dict {catégorie: score} pour identifier la catégorie principale
        """
        text = user_text.lower()
        # Nettoyage des accents pour permettre plus de tolérance
        text_clean = self._normalize(text)

        detected_codes = set()
        category_scores = {}

        for symptom in self.symptoms:
            match_count = 0
            for keyword in symptom.keywords:
                kw_clean = self._normalize(keyword.lower())
                if kw_clean in text_clean:
                    match_count += 1

            if match_count >= 1:
                detected_codes.add(symptom.code)
                cat = symptom.category
                # Le score est pondéré par le nombre de mots-clés détectés
                category_scores[cat] = category_scores.get(cat, 0) + match_count

        # Trier les catégories par score décroissant
        sorted_categories = sorted(category_scores.items(), key=lambda x: x[1], reverse=True)
        best_category = sorted_categories[0][0] if sorted_categories else None

        return detected_codes, best_category, dict(sorted_categories)

    def _normalize(self, text):
        """Normalise le texte en supprimant les accents courants pour la tolérance."""
        replacements = {
            'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
            'à': 'a', 'â': 'a', 'ä': 'a',
            'ù': 'u', 'û': 'u', 'ü': 'u',
            'î': 'i', 'ï': 'i',
            'ô': 'o', 'ö': 'o',
            'ç': 'c',
            "'": ' ', "'": ' ', "-": ' ',
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text

    def get_symptoms_for_category(self, category):
        """Retourne tous les symptômes d'une catégorie donnée."""
        return [s for s in self.symptoms if s.category == category]

    def get_description_for_codes(self, codes):
        """Retourne une liste de descriptions pour un ensemble de codes."""
        sym_dict = {s.code: s.description for s in self.symptoms}
        return [sym_dict.get(code, code) for code in codes]
