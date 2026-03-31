class Rule:
    """Classe représentant une règle (SI conditions ALORS diagnostic)."""
    def __init__(self, conditions, diagnosis):
        self.conditions = conditions
        self.diagnosis = diagnosis

    def __repr__(self):
        return f"Rule({self.conditions} -> {self.diagnosis})"

class RulesBase:
    """
    Base de règles enrichie pour le diagnostic (~150 règles).
    """
    RULES = [
        # ══════════════════════════════════════════════════════════════
        #  ALIMENTATION & DÉMARRAGE
        # ══════════════════════════════════════════════════════════════
        Rule(["pas_d_alimentation"], "Panne de bloc d'alimentation (PSU)"),
        Rule(["pas_d_alimentation", "odeur_de_brulé"], "Court-circuit interne ou alimentation brûlée"),
        Rule(["voyant_allume", "ecran_noir"], "Problème d'affichage ou GPU"),
        Rule(["voyant_allume", "bruit_ventilation", "ecran_noir"], "Problème lié à la Carte Mère ou CPU"),
        Rule(["bips_au_demarrage", "ecran_noir"], "Erreur de test de démarrage (POST) - Vérifier RAM/GPU"),
        Rule(["bloque_sur_logo"], "Problème de configuration BIOS ou disque de démarrage"),
        Rule(["erreur_boot"], "Secteur de démarrage corrompu ou disque dur défaillant"),
        Rule(["date_heure_incorrecte"], "Pile CMOS (CR2032) épuisée"),
        Rule(["vibrations_boitier"], "Ventilateur ou disque dur mal fixé"),
        Rule(["redemarrage_boucle"], "Boucle de redémarrage (fichier système critique corrompu)"),
        Rule(["redemarrage_boucle", "ecran_bleu"], "BSOD en boucle — pilote ou mise à jour défaillante"),
        Rule(["alimentation_intermittente"], "Condensateur d'alimentation fatigué ou RAM mal enfoncée"),
        Rule(["alimentation_intermittente", "odeur_de_brulé"], "Alimentation en court-circuit imminent"),
        Rule(["pas_d_alimentation", "voyant_allume"], "Problème de bouton d'allumage ou carte mère"),

        # ══════════════════════════════════════════════════════════════
        #  AFFICHAGE & ÉCRAN
        # ══════════════════════════════════════════════════════════════
        Rule(["ecran_scintille"], "Câble vidéo (HDMI/DisplayPort) défectueux ou pilote GPU"),
        Rule(["image_distordue"], "Carte graphique (GPU) en fin de vie ou surchauffe GPU"),
        Rule(["ecran_externe_pas_de_signal"], "Port de sortie vidéo défaillant ou mauvais canal sur l'écran"),
        Rule(["ecran_noir", "bruit_ventilation"], "Rétroéclairage de l'écran HS (si portable) ou GPU"),
        Rule(["ecran_fige"], "Gel d'affichage — pilote GPU crashé ou surcharge VRAM"),
        Rule(["ecran_fige", "surchauffe"], "Surchauffe GPU provoquant un gel de l'affichage"),
        Rule(["resolution_bloquee"], "Pilote graphique générique installé (pilote constructeur manquant)"),
        Rule(["resolution_bloquee", "erreur_pilote"], "Pilote GPU corrompu empêchant la bonne résolution"),
        Rule(["double_ecran_non_detecte"], "Câble ou port vidéo secondaire défectueux"),
        Rule(["double_ecran_non_detecte", "erreur_pilote"], "Pilote GPU ne supportant pas le multi-écran"),
        Rule(["ecran_tactile_ne_repond_pas"], "Pilote d'écran tactile désactivé ou câble nappe déconnecté"),
        Rule(["tache_ecran"], "Pixels morts ou début de fuite de la dalle LCD"),
        Rule(["ecran_noir", "ecran_externe_pas_de_signal"], "Panne totale de la puce graphique (GPU)"),
        Rule(["ecran_scintille", "image_distordue"], "VRAM de la carte graphique défectueuse"),

        # ══════════════════════════════════════════════════════════════
        #  PERFORMANCE & SYSTÈME
        # ══════════════════════════════════════════════════════════════
        Rule(["lenteur_systeme", "processeur_100_pourcent"], "Processus gourmand ou infection virale"),
        Rule(["lenteur_systeme", "ram_saturee"], "Mémoire vive insuffisante pour les tâches actuelles"),
        Rule(["lenteur_systeme", "disque_dur_plein"], "Espace disque insuffisant pour le swap système"),
        Rule(["demarrage_lent"], "Trop d'applications au démarrage ou disque dur fragmenté"),
        Rule(["systeme_fige"], "Incompatibilité matérielle ou surchauffe processeur"),
        Rule(["crash_applications"], "Fichiers système corrompus ou RAM défectueuse"),
        Rule(["ecran_bleu"], "Erreur critique de pilote ou défaillance matérielle (RAM/HDD)"),
        Rule(["ecran_bleu", "surchauffe"], "Instabilité système due à la chaleur excessive"),
        Rule(["ecran_bleu", "ram_saturee"], "Défaut de barrette mémoire (RAM)"),
        Rule(["lenteur_systeme", "popups_publicitaires", "redirection_navigateur"], "Infection massive par malwares"),
        Rule(["lenteur_systeme", "bruit_disque_dur"], "Disque dur en train de lâcher (données en danger)"),
        Rule(["crash_applications", "dll_manquante"], "Runtime C++ manquant ou installation corrompue"),
        Rule(["crash_applications", "ram_saturee"], "Fuite mémoire dans une application"),
        Rule(["lenteur_systeme", "demarrage_lent"], "Système Windows dégradé nécessitant une réinstallation propre"),
        Rule(["video_saccadee", "processeur_100_pourcent"], "CPU insuffisant pour le rendu vidéo/3D"),
        Rule(["video_saccadee", "image_distordue"], "GPU en difficulté — surchauffe ou VRAM défectueuse"),

        # ══════════════════════════════════════════════════════════════
        #  SYSTÈME & LOGICIEL
        # ══════════════════════════════════════════════════════════════
        Rule(["echec_windows_update"], "Services Windows Update corrompus"),
        Rule(["licence_invalide"], "Changement matériel majeur ou problème de serveur d'activation"),
        Rule(["dll_manquante"], "Logiciel mal installé ou Runtime C++ manquant"),
        Rule(["erreur_systeme_fichiers"], "Corruption de la table de fichiers (NTFS/FAT)"),
        Rule(["erreur_systeme_fichiers", "ecran_bleu"], "Corruption Windows suite à un arrêt brutal"),
        Rule(["echec_overclocking"], "Paramètres BIOS instables (Reset CMOS requis)"),
        Rule(["echec_overclocking", "systeme_fige"], "Paramètres BIOS instables (Reset CMOS requis)"),
        Rule(["mode_sans_echec"], "Pilote récemment installé incompatible ou malware bloquant"),
        Rule(["mode_sans_echec", "ecran_bleu"], "Pilote critique corrompu nécessitant une restauration système"),
        Rule(["erreur_registre"], "Registre Windows corrompu après désinstallation agressive"),
        Rule(["restauration_impossible"], "Points de restauration corrompus ou espace disque insuffisant"),
        Rule(["installation_logiciel_echoue"], "Permissions insuffisantes ou installeur corrompu"),
        Rule(["installation_logiciel_echoue", "erreur_registre"], "Registre Windows bloquant les nouvelles installations"),
        Rule(["erreur_pilote"], "Pilote obsolète ou incompatible avec la version de Windows"),

        # ══════════════════════════════════════════════════════════════
        #  SURCHAUFFE
        # ══════════════════════════════════════════════════════════════
        Rule(["surchauffe", "bruit_ventilation"], "Accumulation de poussière dans les dissipateurs"),
        Rule(["surchauffe", "extinction_aleatoire"], "Mise en sécurité thermique du CPU (Pâte thermique à changer)"),
        Rule(["surchauffe", "ventilateur_ne_tourne_pas"], "Ventilateur CPU/GPU en panne — remplacement urgent"),
        Rule(["throttling_visible"], "Throttling thermique — pâte thermique sèche ou ventilation bouchée"),
        Rule(["throttling_visible", "surchauffe"], "Throttling thermique dû à une charge CPU excessive"),
        Rule(["ventilateur_permanent"], "Capteur thermique défaillant ou poussière accumulée"),
        Rule(["ventilateur_permanent", "surchauffe"], "Système de refroidissement saturé"),

        # ══════════════════════════════════════════════════════════════
        #  STOCKAGE
        # ══════════════════════════════════════════════════════════════
        Rule(["bruit_disque_dur"], "Panne mécanique imminente du disque dur (HDD)"),
        Rule(["transfert_fichier_lent"], "Secteurs défectueux sur le disque dur"),
        Rule(["disque_non_visible"], "Câble SATA débranché ou disque dur HS"),
        Rule(["vibrations_boitier", "bruit_disque_dur"], "Tête de lecture du disque dur qui raye le plateau"),
        Rule(["bloque_sur_logo", "bruit_disque_dur"], "Échec d'initialisation du support de stockage"),
        Rule(["erreur_boot", "disque_non_visible"], "Perte de connexion physique avec le disque dur"),
        Rule(["demarrage_lent", "transfert_fichier_lent"], "Disque dur extrêmement fragmenté ou fatigué"),
        Rule(["partition_raw"], "Table de partition corrompue nécessitant une récupération de données"),
        Rule(["ssd_non_detecte_apres_clonage"], "Clonage incomplet ou mode AHCI/IDE mal configuré dans le BIOS"),
        Rule(["espace_disque_fantome"], "Fichiers temporaires ou clichés instantanés occupant l'espace"),
        Rule(["disque_externe_non_reconnu"], "Port USB défaillant ou alimentation insuffisante pour le disque"),
        Rule(["disque_externe_non_reconnu", "usb_non_reconnu"], "Contrôleur USB en panne ou hub surchargé"),
        Rule(["fichiers_disparus"], "Corruption du système de fichiers ou attaque de malware"),
        Rule(["fichiers_disparus", "ransomware_detecte"], "Fichiers chiffrés par un ransomware"),

        # ══════════════════════════════════════════════════════════════
        #  RÉSEAU & INTERNET
        # ══════════════════════════════════════════════════════════════
        Rule(["pas_d_internet", "wifi_non_detecte"], "Carte Wi-Fi désactivée ou pilote manquant"),
        Rule(["connectivite_limitee"], "Problème de configuration IP ou DNS"),
        Rule(["pas_d_internet", "connectivite_limitee"], "Problème venant du routeur ou du FAI"),
        Rule(["bluetooth_ne_fct_pas"], "Service Bluetooth arrêté ou antenne débranchée"),
        Rule(["pas_d_internet", "wifi_non_detecte", "bluetooth_ne_fct_pas"], "Défaillance de la carte réseau combo (Wi-Fi + BT)"),
        Rule(["debit_internet_lent"], "Congestion réseau ou limitation FAI"),
        Rule(["debit_internet_lent", "coupures_wifi"], "Signal Wi-Fi faible (éloignement du routeur ou interférences)"),
        Rule(["coupures_wifi"], "Pilote Wi-Fi instable ou canal Wi-Fi saturé"),
        Rule(["vpn_ne_connecte_pas"], "Port VPN bloqué par le pare-feu ou configuration serveur incorrecte"),
        Rule(["vpn_ne_connecte_pas", "pas_d_internet"], "Réseau sous-jacent défaillant empêchant le tunnel VPN"),
        Rule(["ping_eleve"], "Congestion réseau locale ou problème de routage FAI"),
        Rule(["ping_eleve", "debit_internet_lent"], "Saturation de la bande passante (téléchargements en cours)"),
        Rule(["dns_ne_resout_pas"], "Serveurs DNS configurés inaccessibles ou corrompus"),
        Rule(["dns_ne_resout_pas", "redirection_navigateur"], "DNS détourné par un malware (DNS Hijacking)"),
        Rule(["port_ethernet_hs"], "Port Ethernet physiquement endommagé ou câble RJ45 défectueux"),

        # ══════════════════════════════════════════════════════════════
        #  PÉRIPHÉRIQUES
        # ══════════════════════════════════════════════════════════════
        Rule(["clavier_ne_repond_pas"], "Clavier défectueux ou port USB défaillant"),
        Rule(["souris_ne_repond_pas"], "Capteur de souris sale ou pile déchargée"),
        Rule(["usb_non_reconnu"], "Contrôleur USB surchargé ou pilote chipset obsolète"),
        Rule(["usb_non_reconnu", "clavier_ne_repond_pas"], "Problème de concentrateur USB interne"),
        Rule(["pas_de_son"], "Périphérique de sortie par défaut mal configuré ou pilote audio"),
        Rule(["voyant_allume", "pas_de_son"], "Haut-parleurs débranchés ou carte son intégrée désactivée"),
        Rule(["imprimante_ne_fct_pas"], "File d'attente d'impression bloquée ou câble débranché"),
        Rule(["webcam_non_detectee"], "Confidentialité Windows bloquant l'accès ou câble nappe débranché"),
        Rule(["touchpad_ne_repond_pas"], "Pavé tactile désactivé par raccourci clavier"),
        Rule(["dock_usbc_non_fonctionne"], "Firmware du dock obsolète ou port USB-C non compatible"),
        Rule(["dock_usbc_non_fonctionne", "double_ecran_non_detecte"], "Dock USB-C ne supporte pas le DisplayPort Alt Mode"),
        Rule(["scanner_non_reconnu"], "Pilote TWAIN/WIA manquant pour le scanner"),
        Rule(["casque_non_detecte"], "Prise jack défectueuse ou pilote audio mal routé"),
        Rule(["casque_non_detecte", "pas_de_son"], "Carte audio intégrée en panne"),
        Rule(["manette_non_reconnue"], "Pilote XInput/DirectInput manquant ou port USB défaillant"),
        Rule(["lecteur_optique_bloque"], "Mécanisme d'éjection bloqué ou courroie d'entraînement HS"),
        Rule(["pas_d_internet", "pas_de_son", "clavier_ne_repond_pas"], "Problème majeur de chipset ou pont sud (Southbridge)"),

        # ══════════════════════════════════════════════════════════════
        #  AUDIO / VIDÉO
        # ══════════════════════════════════════════════════════════════
        Rule(["micro_non_detecte"], "Microphone désactivé dans les paramètres de confidentialité"),
        Rule(["micro_non_detecte", "webcam_non_detectee"], "Paramètres de confidentialité Windows bloquant caméra et micro"),
        Rule(["gresillements_audio"], "Jack audio oxydé ou interférence électromagnétique"),
        Rule(["gresillements_audio", "pas_de_son"], "Carte son en fin de vie"),
        Rule(["latence_audio"], "Buffer audio trop petit ou pilote ASIO manquant"),
        Rule(["video_saccadee"], "GPU sous-dimensionné ou pilote graphique obsolète"),

        # ══════════════════════════════════════════════════════════════
        #  SÉCURITÉ
        # ══════════════════════════════════════════════════════════════
        Rule(["popups_publicitaires"], "Adware ou logiciel malveillant installé"),
        Rule(["redirection_navigateur"], "Browser Hijacker ou DNS infecté"),
        Rule(["ransomware_detecte"], "Ransomware actif — isoler immédiatement la machine du réseau"),
        Rule(["ransomware_detecte", "fichiers_chiffres"], "Ransomware ayant chiffré les données — récupération urgente"),
        Rule(["antivirus_desactive"], "Malware avancé désactivant les protections (rootkit probable)"),
        Rule(["antivirus_desactive", "popups_publicitaires"], "Infection profonde nécessitant un scan hors-ligne"),
        Rule(["fichiers_chiffres"], "Fichiers corrompus ou chiffrés par un malware"),
        Rule(["activite_suspecte"], "Potentiel cheval de Troie (RAT) communicant avec un serveur distant"),
        Rule(["activite_suspecte", "debit_internet_lent"], "Malware utilisant la bande passante pour du minage ou du spam"),
        Rule(["compte_pirate"], "Compromission de compte — changement de mots de passe urgent"),
        Rule(["compte_pirate", "redirection_navigateur"], "Session piratée via un keylogger ou phishing"),

        # ══════════════════════════════════════════════════════════════
        #  PORTABLE
        # ══════════════════════════════════════════════════════════════
        Rule(["batterie_ne_charge_pas"], "Chargeur défectueux ou connecteur de charge (DC-Jack) cassé"),
        Rule(["batterie_se_vide_vite"], "Batterie en fin de cycle de vie (usure chimique)"),
        Rule(["batterie_ne_charge_pas", "batterie_se_vide_vite"], "Circuit de charge ou batterie totalement HS"),
        Rule(["liquide_renverse"], "Oxydation imminente des composants (nécessite nettoyage ISOPRO)"),
        Rule(["pas_d_alimentation", "liquide_renverse"], "Court-circuit majeur dû au liquide"),
        Rule(["charniere_cassee"], "Charnière d'écran à remplacer (risque de coupure du câble nappe)"),
        Rule(["charniere_cassee", "ecran_scintille"], "Câble nappe vidéo endommagé par la charnière cassée"),
        Rule(["clavier_portable_touches_collantes"], "Nettoyage clavier nécessaire ou remplacement de membrane"),
        Rule(["clavier_portable_touches_collantes", "liquide_renverse"], "Dommage par liquide sous les touches"),
        Rule(["chargeur_chauffe"], "Chargeur non d'origine ou puissance insuffisante"),
        Rule(["chargeur_chauffe", "batterie_ne_charge_pas"], "Chargeur défaillant risquant d'endommager la batterie"),
        Rule(["ecran_portable_casse"], "Dalle LCD à remplacer"),
        Rule(["ecran_portable_casse", "ecran_tactile_ne_repond_pas"], "Dalle LCD+tactile complète à remplacer"),

        # ══════════════════════════════════════════════════════════════
        #  RÈGLES COMBINÉES AVANCÉES
        # ══════════════════════════════════════════════════════════════
        Rule(["odeur_de_brulé", "fumee_du_pc"], "Court-circuit critique (Danger d'incendie !)"),
        Rule(["extinction_aleatoire", "fumee_du_pc"], "Composant VRM ou condensateur qui a explosé"),
        Rule(["bips_au_demarrage", "voyant_allume"], "Code d'erreur sonore de la carte mère (consulter manuel)"),
    ]
