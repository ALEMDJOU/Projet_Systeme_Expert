# knowledge_base.py

class Symptom:
    """Classe représentant un symptôme dans le système expert."""
    def __init__(self, code, description, category, keywords):
        self.code = code
        self.description = description
        self.category = category          # Catégorie pour le filtrage intelligent
        self.keywords = keywords          # Mots-clés pour l'analyse de texte libre

    def __repr__(self):
        return f"Symptom({self.code})"


class KnowledgeBase:
    """
    Base de connaissances enrichie du système expert.
    ~120 symptômes organisés par catégorie avec mots-clés pour l'analyse NLP.
    """

    CATEGORIES = [
        "Alimentation",
        "Affichage",
        "Performance",
        "Stockage",
        "Réseau",
        "Périphériques",
        "Sécurité",
        "Portable",
        "Système",
        "Surchauffe",
        "Audio/Vidéo",
    ]

    SYMPTOMS = [
        # ══════════════════════════════════════════════════════════════
        #  ALIMENTATION & DÉMARRAGE
        # ══════════════════════════════════════════════════════════════
        Symptom("pas_d_alimentation",
                "L'ordinateur ne s'allume pas du tout (aucun voyant)",
                "Alimentation",
                ["allume", "démarr", "aliment", "courant", "éteint", "mort", "voyant", "bouton power"]),

        Symptom("voyant_allume",
                "Le voyant d'alimentation est allumé mais rien ne se passe",
                "Alimentation",
                ["voyant", "led", "lumière", "allumé", "diode"]),

        Symptom("bips_au_demarrage",
                "L'ordinateur émet des bips sonores au démarrage",
                "Alimentation",
                ["bip", "beep", "son", "démarrage", "sonore", "signal"]),

        Symptom("odeur_de_brulé",
                "Il y a une odeur de brûlé venant du PC",
                "Alimentation",
                ["brûlé", "odeur", "sent", "cramé", "fumée", "chaud"]),

        Symptom("fumee_du_pc",
                "De la fumée sort de l'ordinateur",
                "Alimentation",
                ["fumée", "fume", "vapeur", "brûle"]),

        Symptom("vibrations_boitier",
                "Le boîtier du PC vibre de manière anormale",
                "Alimentation",
                ["vibr", "tremble", "boîtier", "secoue", "bouge"]),

        Symptom("extinction_aleatoire",
                "L'ordinateur s'éteint tout seul de façon aléatoire",
                "Alimentation",
                ["éteint", "s'arrête", "coupe", "aléatoire", "redémarr", "reboot", "crash"]),

        Symptom("redemarrage_boucle",
                "L'ordinateur redémarre en boucle sans s'arrêter",
                "Alimentation",
                ["boucle", "redémarr", "loop", "recommence", "cycle", "reboot"]),

        Symptom("alimentation_intermittente",
                "L'ordinateur s'allume puis s'éteint après quelques secondes",
                "Alimentation",
                ["quelques secondes", "s'éteint vite", "clignote", "intermittent"]),

        # ══════════════════════════════════════════════════════════════
        #  AFFICHAGE & ÉCRAN
        # ══════════════════════════════════════════════════════════════
        Symptom("ecran_noir",
                "L'écran reste noir (pas d'affichage)",
                "Affichage",
                ["noir", "écran", "affich", "image", "vide", "rien"]),

        Symptom("ecran_scintille",
                "L'écran scintille ou présente des lignes",
                "Affichage",
                ["scintill", "clignot", "ligne", "flash", "tremble", "flicker"]),

        Symptom("image_distordue",
                "L'image à l'écran est déformée ou les couleurs sont anormales",
                "Affichage",
                ["déform", "distord", "couleur", "artefact", "pixel", "bizarre"]),

        Symptom("ecran_externe_pas_de_signal",
                "L'écran externe affiche 'Pas de signal'",
                "Affichage",
                ["signal", "externe", "moniteur", "hdmi", "displayport", "vga", "branché"]),

        Symptom("ecran_fige",
                "L'écran se fige sur une image sans répondre",
                "Affichage",
                ["fige", "figé", "gelé", "freeze", "bloqué", "immobile"]),

        Symptom("resolution_bloquee",
                "La résolution d'écran est bloquée en basse qualité",
                "Affichage",
                ["résolution", "flou", "gros", "pixelisé", "qualité", "basse résolution"]),

        Symptom("double_ecran_non_detecte",
                "Le deuxième écran n'est pas détecté par le PC",
                "Affichage",
                ["deuxième écran", "double écran", "multi-écran", "second moniteur", "2ème"]),

        Symptom("ecran_tactile_ne_repond_pas",
                "L'écran tactile du portable ne répond plus aux touchers",
                "Affichage",
                ["tactile", "toucher", "touch", "doigt", "appui"]),

        Symptom("tache_ecran",
                "Des tâches sombres ou brillantes apparaissent sur l'écran",
                "Affichage",
                ["tache", "point", "pixel mort", "brillant", "sombre"]),

        # ══════════════════════════════════════════════════════════════
        #  PERFORMANCE & SYSTÈME
        # ══════════════════════════════════════════════════════════════
        Symptom("lenteur_systeme",
                "L'ordinateur est anormalement lent",
                "Performance",
                ["lent", "rame", "ralenti", "lag", "met du temps", "traîne", "patine", "lenteur"]),

        Symptom("processeur_100_pourcent",
                "L'utilisation du processeur est constamment à 100%",
                "Performance",
                ["cpu", "processeur", "100%", "occupation", "charge", "utilisation"]),

        Symptom("ram_saturee",
                "La mémoire vive (RAM) est saturée en permanence",
                "Performance",
                ["ram", "mémoire", "saturé", "plein", "insuffisant"]),

        Symptom("demarrage_lent",
                "L'ordinateur met très longtemps à démarrer",
                "Performance",
                ["démarrage lent", "boot", "long", "démarr", "mise en route"]),

        Symptom("systeme_fige",
                "Le système gèle complètement (nécessite un redémarrage forcé)",
                "Performance",
                ["gèle", "figé", "freeze", "bloqué", "planté", "ne répond plus"]),

        Symptom("crash_applications",
                "Les applications se ferment toutes seules sans raison",
                "Performance",
                ["crash", "ferme", "plante", "arrête", "application", "logiciel", "programme"]),

        Symptom("ecran_bleu",
                "Écran bleu de la mort (BSOD) avec un message d'erreur",
                "Performance",
                ["bleu", "bsod", "blue screen", "écran bleu", "erreur critique"]),

        Symptom("erreur_boot",
                "Message d'erreur au démarrage (ex: 'No bootable device')",
                "Système",
                ["boot", "bootable", "démarrage", "erreur", "no bootable", "device"]),

        Symptom("bloque_sur_logo",
                "Bloqué sur le logo BIOS ou le logo Windows au démarrage",
                "Système",
                ["logo", "bios", "bloqué", "démarrage", "windows", "charge"]),

        Symptom("date_heure_incorrecte",
                "La date et l'heure se réinitialisent après chaque redémarrage",
                "Système",
                ["date", "heure", "horloge", "réinitialis", "pile", "cmos"]),

        Symptom("echec_windows_update",
                "Les mises à jour Windows échouent systématiquement",
                "Système",
                ["mise à jour", "update", "échou", "windows update", "installation"]),

        Symptom("licence_invalide",
                "Erreur d'activation ou de licence Windows",
                "Système",
                ["licence", "activation", "license", "filigrane", "activer", "watermark"]),

        Symptom("dll_manquante",
                "Erreur concernant des fichiers DLL manquants",
                "Système",
                ["dll", "manquant", "fichier", "missing", "bibliothèque"]),

        Symptom("erreur_systeme_fichiers",
                "Erreur de système de fichiers NTFS ou corruption",
                "Système",
                ["ntfs", "fat", "système de fichiers", "corruption", "corrompu"]),

        Symptom("echec_overclocking",
                "Système instable après un essai d'overclocking",
                "Système",
                ["overclocking", "overclock", "fréquence", "instable", "oc"]),

        Symptom("mode_sans_echec",
                "Le PC ne démarre qu'en mode sans échec",
                "Système",
                ["mode sans échec", "safe mode", "sans échec", "démarrage minimal"]),

        Symptom("erreur_registre",
                "Erreurs du registre Windows empêchant le fonctionnement normal",
                "Système",
                ["registre", "registry", "regedit", "corruption registre"]),

        Symptom("restauration_impossible",
                "La restauration du système échoue",
                "Système",
                ["restauration", "point de restauration", "restaurer", "recovery"]),

        Symptom("installation_logiciel_echoue",
                "Impossible d'installer un logiciel ou une application",
                "Système",
                ["install", "setup", "impossible", "erreur install", "échec"]),

        Symptom("erreur_pilote",
                "Un périphérique affiche un point d'exclamation jaune dans le Gestionnaire",
                "Système",
                ["pilote", "driver", "gestionnaire", "exclamation", "périphérique"]),

        # ══════════════════════════════════════════════════════════════
        #  SURCHAUFFE
        # ══════════════════════════════════════════════════════════════
        Symptom("surchauffe",
                "L'ordinateur est anormalement chaud au toucher",
                "Surchauffe",
                ["chaud", "chaleur", "brûl", "surchauf", "température"]),

        Symptom("bruit_ventilation",
                "Le ventilateur tourne très fort ou fait un bruit anormal",
                "Surchauffe",
                ["ventilateur", "bruit", "souffle", "tourne", "fan", "bruyant", "fort"]),

        Symptom("ventilateur_ne_tourne_pas",
                "Le ventilateur ne tourne pas du tout alors que le PC est allumé",
                "Surchauffe",
                ["ventilateur", "ne tourne pas", "arrêté", "immobile", "fan"]),

        Symptom("throttling_visible",
                "Les performances chutent fortement après quelques minutes d'utilisation",
                "Surchauffe",
                ["performanc", "chute", "baisse", "throttl", "ralenti", "après quelques minutes"]),

        # ══════════════════════════════════════════════════════════════
        #  STOCKAGE
        # ══════════════════════════════════════════════════════════════
        Symptom("bruit_disque_dur",
                "Bruit de claquement ou de grattage venant du disque dur",
                "Stockage",
                ["claquement", "grattage", "bruit", "disque dur", "clique", "tic-tic"]),

        Symptom("transfert_fichier_lent",
                "La copie ou le transfert de fichiers est extrêmement lent",
                "Stockage",
                ["copie", "transfert", "lent", "fichier", "déplac"]),

        Symptom("disque_non_visible",
                "Le disque dur ou le SSD n'apparaît pas dans le système",
                "Stockage",
                ["disque", "invisible", "non visible", "non détecté", "ssd", "hdd"]),

        Symptom("disque_dur_plein",
                "Le disque dur est presque plein (espace insuffisant)",
                "Stockage",
                ["plein", "espace", "saturé", "insuffisant", "stockage", "disque"]),

        Symptom("partition_raw",
                "Une partition s'affiche en RAW au lieu de NTFS",
                "Stockage",
                ["raw", "partition", "format", "inaccessible", "données"]),

        Symptom("ssd_non_detecte_apres_clonage",
                "Le SSD n'est pas détecté après un clonage de disque",
                "Stockage",
                ["clonage", "clone", "ssd", "non détecté", "migration"]),

        Symptom("espace_disque_fantome",
                "L'espace disque utilisé ne correspond pas aux fichiers visibles",
                "Stockage",
                ["espace fantôme", "espace disparu", "fichier caché", "invisible"]),

        Symptom("disque_externe_non_reconnu",
                "Le disque dur externe n'est pas reconnu quand branché",
                "Stockage",
                ["externe", "usb", "non reconnu", "disque externe", "branché"]),

        Symptom("fichiers_disparus",
                "Des fichiers importants ont disparu sans raison apparente",
                "Stockage",
                ["fichier disparu", "perdu", "supprimé", "effacé", "manquant"]),

        # ══════════════════════════════════════════════════════════════
        #  RÉSEAU & INTERNET
        # ══════════════════════════════════════════════════════════════
        Symptom("pas_d_internet",
                "Impossible de se connecter à Internet",
                "Réseau",
                ["internet", "connexion", "connecter", "réseau", "web", "en ligne"]),

        Symptom("wifi_non_detecte",
                "Aucun réseau Wi-Fi n'apparaît dans la liste",
                "Réseau",
                ["wifi", "wi-fi", "sans fil", "réseau", "détect", "liste"]),

        Symptom("connectivite_limitee",
                "Connecté au réseau mais pas d'accès Internet",
                "Réseau",
                ["connecté", "limité", "pas d'accès", "connectivité", "pas d'internet"]),

        Symptom("bluetooth_ne_fct_pas",
                "Le Bluetooth ne fonctionne pas ou ne détecte rien",
                "Réseau",
                ["bluetooth", "bt", "sans fil", "appairer", "jumeler"]),

        Symptom("debit_internet_lent",
                "Le débit Internet est anormalement lent",
                "Réseau",
                ["débit", "lent", "vitesse", "download", "bande passante", "mbps"]),

        Symptom("coupures_wifi",
                "Le Wi-Fi se déconnecte de manière intermittente",
                "Réseau",
                ["coupure", "déconnect", "intermittent", "perd", "wifi", "instable"]),

        Symptom("vpn_ne_connecte_pas",
                "Impossible de se connecter au VPN",
                "Réseau",
                ["vpn", "tunnel", "distant", "travail à distance", "connexion vpn"]),

        Symptom("ping_eleve",
                "Le ping / la latence réseau est très élevée",
                "Réseau",
                ["ping", "latence", "lag", "réponse", "ms", "délai"]),

        Symptom("dns_ne_resout_pas",
                "Les sites web ne s'ouvrent pas mais le ping fonctionne",
                "Réseau",
                ["dns", "résolution", "nom de domaine", "site", "s'ouvre pas"]),

        Symptom("port_ethernet_hs",
                "La connexion filaire Ethernet ne fonctionne plus",
                "Réseau",
                ["ethernet", "filaire", "câble", "rj45", "port réseau"]),

        # ══════════════════════════════════════════════════════════════
        #  PÉRIPHÉRIQUES
        # ══════════════════════════════════════════════════════════════
        Symptom("clavier_ne_repond_pas",
                "Le clavier ne répond pas ou certaines touches sont mortes",
                "Périphériques",
                ["clavier", "touche", "tape", "saisie", "lettre", "frappe"]),

        Symptom("souris_ne_repond_pas",
                "La souris ne bouge pas ou le clic ne fonctionne pas",
                "Périphériques",
                ["souris", "curseur", "clic", "pointeur", "bouge"]),

        Symptom("usb_non_reconnu",
                "Les périphériques USB ne sont pas reconnus",
                "Périphériques",
                ["usb", "reconnu", "clé usb", "périphérique", "port"]),

        Symptom("imprimante_ne_fct_pas",
                "L'imprimante n'imprime pas ou n'est pas détectée",
                "Périphériques",
                ["imprimante", "impression", "print", "imprimer", "scanner"]),

        Symptom("webcam_non_detectee",
                "La webcam n'est pas reconnue ou affiche un écran noir",
                "Périphériques",
                ["webcam", "caméra", "vidéo", "appel", "visio"]),

        Symptom("touchpad_ne_repond_pas",
                "Le pavé tactile du portable ne répond plus",
                "Périphériques",
                ["touchpad", "pavé tactile", "tactile", "portable"]),

        Symptom("dock_usbc_non_fonctionne",
                "Le dock USB-C / station d'accueil ne fonctionne pas correctement",
                "Périphériques",
                ["dock", "usb-c", "station d'accueil", "thunderbolt", "hub"]),

        Symptom("scanner_non_reconnu",
                "Le scanner n'est pas détecté par l'ordinateur",
                "Périphériques",
                ["scanner", "numériqu", "scan", "numérisation"]),

        Symptom("casque_non_detecte",
                "Le casque audio / les écouteurs ne sont pas détectés",
                "Périphériques",
                ["casque", "écouteur", "headset", "jack", "audio"]),

        Symptom("manette_non_reconnue",
                "La manette de jeu n'est pas reconnue par le PC",
                "Périphériques",
                ["manette", "gamepad", "controller", "joystick", "jeu"]),

        Symptom("lecteur_optique_bloque",
                "Le tiroir CD/DVD ne s'ouvre pas",
                "Périphériques",
                ["cd", "dvd", "tiroir", "lecteur", "optique", "bloqué"]),

        # ══════════════════════════════════════════════════════════════
        #  AUDIO / VIDÉO
        # ══════════════════════════════════════════════════════════════
        Symptom("pas_de_son",
                "Aucun son ne sort des haut-parleurs",
                "Audio/Vidéo",
                ["son", "audio", "haut-parleur", "muet", "volume", "sourd"]),

        Symptom("micro_non_detecte",
                "Le microphone n'est pas détecté ou ne capte rien",
                "Audio/Vidéo",
                ["micro", "microphone", "voix", "enregistr", "capte"]),

        Symptom("gresillements_audio",
                "Des grésillements ou bruits parasites dans le son",
                "Audio/Vidéo",
                ["grésillement", "parasite", "crépite", "bruit", "grésille", "crachotement"]),

        Symptom("latence_audio",
                "Le son est décalé par rapport à la vidéo",
                "Audio/Vidéo",
                ["décalé", "latence", "retard", "sync", "décalage"]),

        Symptom("video_saccadee",
                "Les vidéos sont saccadées ou le GPU décroche en jeu",
                "Audio/Vidéo",
                ["saccad", "fps", "jeu", "lag", "game", "gpu", "image"]),

        # ══════════════════════════════════════════════════════════════
        #  SÉCURITÉ
        # ══════════════════════════════════════════════════════════════
        Symptom("popups_publicitaires",
                "Des fenêtres publicitaires inattendues s'ouvrent partout",
                "Sécurité",
                ["pub", "popup", "publicité", "fenêtre", "intempestive", "annonce"]),

        Symptom("redirection_navigateur",
                "Le navigateur redirige vers des sites étranges ou indésirables",
                "Sécurité",
                ["redirection", "redirige", "site étrange", "navigateur", "page d'accueil"]),

        Symptom("ransomware_detecte",
                "Un message demande de payer une rançon pour récupérer les fichiers",
                "Sécurité",
                ["rançon", "ransomware", "chiffré", "payer", "crypto", "bitcoin", "verrouillé"]),

        Symptom("antivirus_desactive",
                "L'antivirus se désactive tout seul ou ne peut pas se lancer",
                "Sécurité",
                ["antivirus", "désactivé", "protection", "sécurité", "windows defender"]),

        Symptom("fichiers_chiffres",
                "Des fichiers sont devenus illisibles avec une extension inconnue",
                "Sécurité",
                ["illisible", "chiffré", "extension", "crypté", "modifié"]),

        Symptom("activite_suspecte",
                "Activité réseau suspecte (envoi de données non autorisé)",
                "Sécurité",
                ["suspect", "trafic", "envoi", "réseau", "activité", "données sortantes"]),

        Symptom("compte_pirate",
                "Votre compte Windows ou e-mail semble avoir été piraté",
                "Sécurité",
                ["piraté", "hacké", "compte", "mot de passe", "accès non autorisé"]),

        # ══════════════════════════════════════════════════════════════
        #  PORTABLE
        # ══════════════════════════════════════════════════════════════
        Symptom("batterie_ne_charge_pas",
                "Le portable est branché mais la batterie ne charge pas",
                "Portable",
                ["batterie", "charge", "branché", "chargeur", "secteur"]),

        Symptom("batterie_se_vide_vite",
                "Le pourcentage de batterie chute très rapidement",
                "Portable",
                ["batterie", "vide", "autonomie", "décharge", "pourcentage"]),

        Symptom("liquide_renverse",
                "Du liquide a été renversé sur l'ordinateur",
                "Portable",
                ["liquide", "eau", "café", "renversé", "mouillé"]),

        Symptom("charniere_cassee",
                "La charnière de l'écran du portable est cassée ou lâche",
                "Portable",
                ["charnière", "cassé", "lâche", "écran tombe", "articulat"]),

        Symptom("ventilateur_permanent",
                "Le ventilateur du portable tourne en permanence même au repos",
                "Portable",
                ["ventilateur", "permanent", "repos", "tout le temps", "continu"]),

        Symptom("clavier_portable_touches_collantes",
                "Certaines touches du clavier portable sont collantes ou enfoncées",
                "Portable",
                ["touche collante", "enfoncé", "bloqué", "clavier portable", "sale"]),

        Symptom("chargeur_chauffe",
                "Le chargeur du portable chauffe anormalement",
                "Portable",
                ["chargeur chaud", "chargeur chauffe", "adaptateur", "bloc alimentation portable"]),

        Symptom("ecran_portable_casse",
                "L'écran du portable est fissuré ou a des lignes de cassure",
                "Portable",
                ["fissuré", "cassé", "fêlé", "écran cassé", "rayure profonde"]),
    ]
