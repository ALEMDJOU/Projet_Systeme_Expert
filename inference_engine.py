# inference_engine.py

class InferenceEngine:
    """
    Moteur d'inférence à chaînage avant.
    Gère la base de faits, applique les règles, et calcule un score de confiance.
    """
    def __init__(self, rules):
        self.rules = rules
        self.facts = set()
        self.diagnoses = []
        self.explained_diagnoses = {}
        self.confidence_scores = {}

    def add_fact(self, fact):
        """Ajoute un fait à la base de faits et déclenche l'inférence."""
        if fact not in self.facts:
            self.facts.add(fact)
            self.run()

    def add_facts(self, facts_set):
        """Ajoute plusieurs faits d'un coup puis déclenche l'inférence."""
        new_facts = facts_set - self.facts
        if new_facts:
            self.facts.update(new_facts)
            self.run()

    def run(self):
        """Exécute le chaînage avant pour trouver de nouveaux diagnostics."""
        new_diagnoses = []
        for rule in self.rules:
            if all(cond in self.facts for cond in rule.conditions):
                diagnosis = rule.diagnosis
                if diagnosis not in self.diagnoses:
                    new_diagnoses.append(diagnosis)
                    self.explained_diagnoses[diagnosis] = rule.conditions
                    # Score de confiance : ratio conditions matchées / conditions requises
                    matched = sum(1 for c in rule.conditions if c in self.facts)
                    self.confidence_scores[diagnosis] = matched / len(rule.conditions)

        self.diagnoses.extend(new_diagnoses)
        return new_diagnoses

    def get_diagnoses(self):
        """Retourne les diagnostics triés par confiance décroissante."""
        return sorted(
            self.diagnoses,
            key=lambda d: self.confidence_scores.get(d, 0),
            reverse=True
        )

    def get_confidence(self, diagnosis):
        """Retourne le score de confiance pour un diagnostic (0.0 à 1.0)."""
        return self.confidence_scores.get(diagnosis, 0)

    def get_confidence_label(self, diagnosis):
        """Retourne l'indicateur visuel de confiance."""
        score = self.get_confidence(diagnosis)
        if score >= 1.0:
            return "🟢 Certitude élevée"
        elif score >= 0.66:
            return "🟡 Confiance moyenne"
        else:
            return "🔴 Confiance faible"

    def get_explanation(self, diagnosis):
        symptoms = self.explained_diagnoses.get(diagnosis, [])
        return f"Ce diagnostic a été établi car les symptômes suivants ont été détectés : {', '.join(symptoms)}."

    def reset(self):
        self.facts = set()
        self.diagnoses = []
        self.explained_diagnoses = {}
        self.confidence_scores = {}
