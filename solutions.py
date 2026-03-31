# solutions.py

class SolutionsSystem:
    """
    Fournit des solutions préventives, correctives et palliatives pour chaque diagnostic.
    ~100 entrées couvrant tous les diagnostics du système expert.
    """
    SOLUTIONS = {
        # ══════════════════════════════════════════════════════════════
        #  ALIMENTATION & DÉMARRAGE
        # ══════════════════════════════════════════════════════════════
        "Panne de bloc d'alimentation (PSU)": {
            "palliative": "Tester avec un autre câble d'alimentation standard.",
            "corrective": "Remplacer le bloc d'alimentation par un modèle de puissance équivalente ou supérieure.",
            "preventive": "Utiliser un onduleur (UPS) pour protéger l'alimentation des surtensions."
        },
        "Court-circuit interne ou alimentation brûlée": {
            "palliative": "Débrancher immédiatement l'ordinateur de la prise murale.",
            "corrective": "Remplacer l'alimentation et vérifier si la carte mère n'a pas été touchée.",
            "preventive": "Éviter de surcharger les multiprises et assurer une bonne ventilation du boîtier."
        },
        "Problème d'affichage ou GPU": {
            "palliative": "Utiliser un deuxième écran pour vérifier si le signal sort.",
            "corrective": "Changer la carte graphique ou utiliser le port vidéo de la carte mère.",
            "preventive": "Nettoyer les contacts dorés de la carte graphique avec de l'alcool isopropylique."
        },
        "Problème lié à la Carte Mère ou CPU": {
            "palliative": "Réinitialiser le BIOS en retirant la pile CMOS pendant 30 secondes.",
            "corrective": "Remplacer la carte mère ou le processeur après test croisé.",
            "preventive": "Ne jamais manipuler les composants sans bracelet antistatique."
        },
        "Erreur de test de démarrage (POST) - Vérifier RAM/GPU": {
            "palliative": "Retirer et replacer (resit) les barrettes de RAM.",
            "corrective": "Remplacer la barrette de mémoire défectueuse.",
            "preventive": "Vérifier régulièrement la fixation des composants internes."
        },
        "Problème de configuration BIOS ou disque de démarrage": {
            "palliative": "Vérifier l'ordre de démarrage (Boot Priority) dans le BIOS.",
            "corrective": "Réinstaller le gestionnaire de démarrage Windows via l'invite de commande.",
            "preventive": "Éviter de modifier les paramètres du BIOS sans connaissance préalable."
        },
        "Secteur de démarrage corrompu ou disque dur défaillant": {
            "palliative": "Lancer une réparation automatique à partir d'une clé USB Windows.",
            "corrective": "Remplacer le disque dur et réinstaller le système.",
            "preventive": "Activer les sauvegardes automatiques dans le Cloud (OneDrive/Google Drive)."
        },
        "Pile CMOS (CR2032) épuisée": {
            "palliative": "Régler l'heure manuellement à chaque démarrage.",
            "corrective": "Remplacer la pile bouton CR2032 sur la carte mère.",
            "preventive": "Changer la pile CMOS tous les 5 ans de manière proactive."
        },
        "Ventilateur ou disque dur mal fixé": {
            "palliative": "Identifier le composant qui vibre en posant la main sur le boîtier.",
            "corrective": "Serrer les vis de fixation ou remplacer les patins en caoutchouc.",
            "preventive": "Vérifier le serrage des vis lors du nettoyage annuel du PC."
        },
        "Boucle de redémarrage (fichier système critique corrompu)": {
            "palliative": "Tenter de démarrer en Mode Sans Échec (F8 ou Shift+Restart).",
            "corrective": "Exécuter 'sfc /scannow' et 'DISM /RestoreHealth' depuis une clé USB de récupération.",
            "preventive": "Créer régulièrement des points de restauration système."
        },
        "BSOD en boucle — pilote ou mise à jour défaillante": {
            "palliative": "Démarrer en Mode Sans Échec et désinstaller la dernière mise à jour.",
            "corrective": "Faire un rollback du pilote fautif via le Gestionnaire de périphériques.",
            "preventive": "Activer la création automatique de points de restauration avant chaque Update."
        },
        "Condensateur d'alimentation fatigué ou RAM mal enfoncée": {
            "palliative": "Ouvrir le boîtier et réenficher fermement les barrettes de RAM.",
            "corrective": "Tester l'alimentation avec un testeur PSU et remplacer si nécessaire.",
            "preventive": "Vérifier les composants internes une fois par an."
        },
        "Alimentation en court-circuit imminent": {
            "palliative": "DÉBRANCHER IMMÉDIATEMENT et ne plus rallumer.",
            "corrective": "Remplacer le bloc d'alimentation par un modèle certifié 80 PLUS.",
            "preventive": "Ne jamais utiliser une alimentation sans marque ou contrefaite."
        },
        "Problème de bouton d'allumage ou carte mère": {
            "palliative": "Tenter de court-circuiter les pins 'Power SW' sur la carte mère.",
            "corrective": "Remplacer le bouton du boîtier ou la carte mère.",
            "preventive": "Ne pas appuyer trop fort sur le bouton d'allumage."
        },

        # ══════════════════════════════════════════════════════════════
        #  AFFICHAGE & ÉCRAN
        # ══════════════════════════════════════════════════════════════
        "Câble vidéo (HDMI/DisplayPort) défectueux ou pilote GPU": {
            "palliative": "Inverser les deux bouts du câble vidéo.",
            "corrective": "Remplacer le câble par un modèle certifié et mettre à jour les pilotes.",
            "preventive": "Éviter de plier les câbles vidéo avec des angles trop serrés."
        },
        "Carte graphique (GPU) en fin de vie ou surchauffe GPU": {
            "palliative": "Sous-cadencer (underclock) le GPU avec MSI Afterburner pour la stabilité.",
            "corrective": "Changer la pâte thermique du GPU ou remplacer la carte.",
            "preventive": "Maintenir un flux d'air optimal dans le boîtier du PC."
        },
        "Port de sortie vidéo défaillant ou mauvais canal sur l'écran": {
            "palliative": "Changer de port (passer du HDMI au DisplayPort).",
            "corrective": "Réparer la soudure du port ou utiliser une carte graphique dédiée.",
            "preventive": "Brancher/débrancher les câbles avec précaution, sans forcer."
        },
        "Rétroéclairage de l'écran HS (si portable) ou GPU": {
            "palliative": "Éclairer l'écran avec une lampe torche pour voir si l'image est là.",
            "corrective": "Remplacer la dalle LCD ou l'inverter du rétroéclairage.",
            "preventive": "Éviter d'ouvrir/fermer l'écran du portable trop brusquement."
        },
        "Gel d'affichage — pilote GPU crashé ou surcharge VRAM": {
            "palliative": "Appuyer sur Win+Ctrl+Shift+B pour redémarrer le pilote graphique.",
            "corrective": "Mettre à jour ou réinstaller le pilote GPU depuis le site constructeur.",
            "preventive": "Ne pas surcharger la VRAM avec des textures trop lourdes."
        },
        "Surchauffe GPU provoquant un gel de l'affichage": {
            "palliative": "Augmenter la vitesse du ventilateur GPU via MSI Afterburner.",
            "corrective": "Changer la pâte thermique du GPU et nettoyer le système de refroidissement.",
            "preventive": "Surveiller les températures avec HWMonitor."
        },
        "Pilote graphique générique installé (pilote constructeur manquant)": {
            "palliative": "Utiliser Windows Update pour tenter de récupérer un pilote.",
            "corrective": "Télécharger le pilote depuis le site NVIDIA/AMD/Intel.",
            "preventive": "Sauvegarder les pilotes d'origine avant une réinstallation de Windows."
        },
        "Pilote GPU corrompu empêchant la bonne résolution": {
            "palliative": "Désinstaller le pilote en Mode Sans Échec avec DDU (Display Driver Uninstaller).",
            "corrective": "Installer le dernier pilote stable du constructeur.",
            "preventive": "Éviter les pilotes bêta instables."
        },
        "Câble ou port vidéo secondaire défectueux": {
            "palliative": "Tester avec un autre câble ou un autre port vidéo.",
            "corrective": "Remplacer le câble ou utiliser un adaptateur actif.",
            "preventive": "Utiliser des câbles certifiés et de bonne qualité."
        },
        "Pilote GPU ne supportant pas le multi-écran": {
            "palliative": "Vérifier que le GPU supporte le nombre d'écrans souhaité.",
            "corrective": "Mettre à jour le pilote GPU ou ajouter une carte graphique secondaire.",
            "preventive": "Vérifier la compatibilité multi-écran avant l'achat."
        },
        "Pilote d'écran tactile désactivé ou câble nappe déconnecté": {
            "palliative": "Réactiver le HID Touch Screen dans le Gestionnaire de périphériques.",
            "corrective": "Rebrancher la nappe tactile ou réinstaller le pilote.",
            "preventive": "Ne pas forcer sur l'écran tactile."
        },
        "Pixels morts ou début de fuite de la dalle LCD": {
            "palliative": "Utiliser un logiciel de test de pixels morts (JScreenFix).",
            "corrective": "Remplacer la dalle LCD si sous garantie.",
            "preventive": "Éviter de presser l'écran avec les doigts."
        },
        "Panne totale de la puce graphique (GPU)": {
            "palliative": "Utiliser l'IGPU (si disponible sur le processeur).",
            "corrective": "Changer la carte graphique.",
            "preventive": "Ne pas faire de minage de crypto sans refroidissement adéquat."
        },
        "VRAM de la carte graphique défectueuse": {
            "palliative": "Baisser la fréquence de la mémoire vidéo via logiciel.",
            "corrective": "Remplacer la carte graphique.",
            "preventive": "Maintenir les températures VRAM en dessous de 90°C."
        },

        # ══════════════════════════════════════════════════════════════
        #  PERFORMANCE & SYSTÈME
        # ══════════════════════════════════════════════════════════════
        "Processus gourmand ou infection virale": {
            "palliative": "Terminer les processus suspects via le Gestionnaire des tâches.",
            "corrective": "Lancer un scan complet avec Malwarebytes et désinstaller les bloatwares.",
            "preventive": "Installer un antivirus fiable et ne pas cliquer sur des liens suspects."
        },
        "Mémoire vive insuffisante pour les tâches actuelles": {
            "palliative": "Fermer les onglets de navigateur inutilisés.",
            "corrective": "Ajouter une barrette de RAM supplémentaire.",
            "preventive": "Surveiller l'utilisation de la RAM avant d'ouvrir de gros logiciels."
        },
        "Espace disque insuffisant pour le swap système": {
            "palliative": "Vider la corbeille et supprimer les fichiers temporaires (%temp%).",
            "corrective": "Utiliser l'outil de nettoyage de disque ou désinstaller les gros jeux.",
            "preventive": "Acheter un disque secondaire pour le stockage des données lourdes."
        },
        "Trop d'applications au démarrage ou disque dur fragmenté": {
            "palliative": "Désactiver les apps au démarrage dans l'onglet 'Démarrage' du gestionnaire.",
            "corrective": "Défragmenter le HDD (si ce n'est pas un SSD) et optimiser le démarrage.",
            "preventive": "Vérifier régulièrement la liste des programmes qui se lancent seuls."
        },
        "Incompatibilité matérielle ou surchauffe processeur": {
            "palliative": "Vérifier la température avec Hardware Monitor.",
            "corrective": "Mettre à jour le BIOS ou changer le système de refroidissement.",
            "preventive": "Vérifier la compatibilité des composants avant tout achat."
        },
        "Fichiers système corrompus ou RAM défectueuse": {
            "palliative": "Exécuter 'sfc /scannow' dans une invite de commande admin.",
            "corrective": "Faire une réinstallation propre de Windows ou changer la RAM.",
            "preventive": "Toujours éteindre l'ordinateur normalement via le menu démarrer."
        },
        "Erreur critique de pilote ou défaillance matérielle (RAM/HDD)": {
            "palliative": "Démarrer en mode sans échec pour diagnostiquer.",
            "corrective": "Réinstaller les pilotes constructeurs ou remplacer le disque dur.",
            "preventive": "Mettre à jour les pilotes uniquement depuis les sites officiels."
        },
        "Instabilité système due à la chaleur excessive": {
            "palliative": "Ouvrir le panneau latéral du boîtier.",
            "corrective": "Améliorer le 'Cable Management' pour un meilleur flux d'air.",
            "preventive": "Placer l'ordinateur dans un endroit frais et aéré."
        },
        "Défaut de barrette mémoire (RAM)": {
            "palliative": "Tester les barrettes une par une sur différents slots.",
            "corrective": "Acheter un kit de RAM certifié compatible.",
            "preventive": "Lancer un MemTest86 occasionnellement."
        },
        "Infection massive par malwares": {
            "palliative": "Démarrer en Mode Sans Échec avec prise en charge réseau.",
            "corrective": "Formatage complet et réinstallation de Windows.",
            "preventive": "Changer tous ses mots de passe après le nettoyage."
        },
        "Disque dur en train de lâcher (données en danger)": {
            "palliative": "Cesser toute utilisation et démarrer sur un système Live USB.",
            "corrective": "Remplacer immédiatement par un SSD.",
            "preventive": "Faire des sauvegardes hebdomadaires."
        },
        "Runtime C++ manquant ou installation corrompue": {
            "palliative": "Rechercher la DLL manquante sur un site sûr.",
            "corrective": "Réinstaller tous les Microsoft Visual C++ Redistributable.",
            "preventive": "Maintenir Windows à jour pour inclure les nouveaux runtimes."
        },
        "Fuite mémoire dans une application": {
            "palliative": "Redémarrer l'application fautive régulièrement.",
            "corrective": "Mettre à jour ou réinstaller l'application concernée.",
            "preventive": "Surveiller la consommation mémoire dans le Gestionnaire des tâches."
        },
        "Système Windows dégradé nécessitant une réinstallation propre": {
            "palliative": "Désactiver les services non essentiels avec 'msconfig'.",
            "corrective": "Effectuer une réinstallation propre de Windows en conservant les données.",
            "preventive": "Éviter d'installer trop de logiciels inutiles."
        },
        "CPU insuffisant pour le rendu vidéo/3D": {
            "palliative": "Baisser la qualité graphique dans les paramètres du jeu/logiciel.",
            "corrective": "Mettre à niveau le processeur si la carte mère le permet.",
            "preventive": "Vérifier les configs minimales requises avant d'installer un jeu."
        },
        "GPU en difficulté — surchauffe ou VRAM défectueuse": {
            "palliative": "Réduire la résolution et les détails graphiques.",
            "corrective": "Nettoyer le GPU et changer la pâte thermique, ou remplacer la carte.",
            "preventive": "Maintenir un bon flux d'air dans le boîtier."
        },

        # ══════════════════════════════════════════════════════════════
        #  SYSTÈME & LOGICIEL
        # ══════════════════════════════════════════════════════════════
        "Services Windows Update corrompus": {
            "palliative": "Lancer l'utilitaire de résolution de problèmes Windows Update.",
            "corrective": "Réinitialiser les dossiers SoftwareDistribution et Catroot2.",
            "preventive": "Laisser Windows finir ses mises à jour avant d'éteindre."
        },
        "Changement matériel majeur ou problème de serveur d'activation": {
            "palliative": "Utiliser Windows avec le filigrane d'activation temporairement.",
            "corrective": "Contacter le support Microsoft ou racheter une licence.",
            "preventive": "Lier votre licence Windows à votre compte Microsoft."
        },
        "Logiciel mal installé ou Runtime C++ manquant": {
            "palliative": "Rechercher la DLL manquante sur un site sûr.",
            "corrective": "Réinstaller Microsoft Visual C++ Redistributable.",
            "preventive": "Maintenir Windows à jour pour inclure les nouveaux runtimes."
        },
        "Corruption de la table de fichiers (NTFS/FAT)": {
            "palliative": "Utiliser un logiciel de récupération de données comme Recuva.",
            "corrective": "Formater la partition et restaurer la sauvegarde.",
            "preventive": "Ne jamais débrancher un disque dur externe sans 'Éjecter'."
        },
        "Corruption Windows suite à un arrêt brutal": {
            "palliative": "Démarrer sur le dernier point de restauration connu.",
            "corrective": "Réparation système via clé de démarrage.",
            "preventive": "Investir dans un onduleur contre les coupures de courant."
        },
        "Paramètres BIOS instables (Reset CMOS requis)": {
            "palliative": "Retirer la pile CMOS pendant 1 minute.",
            "corrective": "Remettre les paramètres par défaut dans le BIOS (Load Defaults).",
            "preventive": "Augmenter les fréquences/tensions par paliers très fins."
        },
        "Pilote récemment installé incompatible ou malware bloquant": {
            "palliative": "Démarrer en Mode Sans Échec et désinstaller le dernier pilote.",
            "corrective": "Faire une restauration système à un point antérieur.",
            "preventive": "Créer un point de restauration avant d'installer un nouveau pilote."
        },
        "Pilote critique corrompu nécessitant une restauration système": {
            "palliative": "Utiliser l'option 'Dernière bonne configuration connue' au démarrage.",
            "corrective": "Restaurer Windows via une clé USB de récupération.",
            "preventive": "Garder une clé USB bootable Windows à jour."
        },
        "Registre Windows corrompu après désinstallation agressive": {
            "palliative": "Utiliser CCleaner pour nettoyer les entrées de registre orphelines.",
            "corrective": "Restaurer le registre depuis une sauvegarde ou réinstaller Windows.",
            "preventive": "Toujours utiliser le désinstalleur officiel du logiciel."
        },
        "Points de restauration corrompus ou espace disque insuffisant": {
            "palliative": "Libérer de l'espace disque et recréer un point de restauration.",
            "corrective": "Désactiver puis réactiver la Protection du système.",
            "preventive": "Allouer suffisamment d'espace pour les points de restauration."
        },
        "Permissions insuffisantes ou installeur corrompu": {
            "palliative": "Exécuter l'installeur en tant qu'Administrateur.",
            "corrective": "Retélécharger l'installeur depuis le site officiel.",
            "preventive": "Toujours télécharger les logiciels depuis les sources officielles."
        },
        "Registre Windows bloquant les nouvelles installations": {
            "palliative": "Utiliser l'outil Microsoft 'Program Install and Uninstall Troubleshooter'.",
            "corrective": "Nettoyer manuellement les clés de registre problématiques.",
            "preventive": "Éviter les logiciels de nettoyage de registre douteux."
        },
        "Pilote obsolète ou incompatible avec la version de Windows": {
            "palliative": "Utiliser le mode de compatibilité pour l'ancien pilote.",
            "corrective": "Télécharger la dernière version du pilote depuis le site constructeur.",
            "preventive": "Vérifier la compatibilité des pilotes avant une mise à jour Windows."
        },

        # ══════════════════════════════════════════════════════════════
        #  SURCHAUFFE
        # ══════════════════════════════════════════════════════════════
        "Accumulation de poussière dans les dissipateurs": {
            "palliative": "Utiliser un ventilateur externe pour refroidir temporairement.",
            "corrective": "Nettoyer l'intérieur avec une bombe à air sec ou un compresseur.",
            "preventive": "Nettoyer la poussière tous les 6 mois."
        },
        "Mise en sécurité thermique du CPU (Pâte thermique à changer)": {
            "palliative": "Réduire la fréquence maximale du processeur dans les options d'alimentation.",
            "corrective": "Nettoyer l'ancienne pâte et appliquer une nouvelle pâte thermique de qualité.",
            "preventive": "Renouveler la pâte thermique tous les 2 à 3 ans."
        },
        "Ventilateur CPU/GPU en panne — remplacement urgent": {
            "palliative": "Utiliser le PC portes ouvertes avec un ventilateur d'appoint.",
            "corrective": "Remplacer le ventilateur défectueux par un modèle compatible.",
            "preventive": "Nettoyer les ventilateurs régulièrement pour éviter l'usure prématurée."
        },
        "Throttling thermique — pâte thermique sèche ou ventilation bouchée": {
            "palliative": "Limiter le nombre de tâches lourdes simultanément.",
            "corrective": "Changer la pâte thermique et nettoyer les dissipateurs.",
            "preventive": "Surveiller les températures avec HWMonitor ou Core Temp."
        },
        "Throttling thermique dû à une charge CPU excessive": {
            "palliative": "Limiter le nombre d'applications ouvertes simultanément.",
            "corrective": "Augmenter la courbe de ventilation dans le BIOS.",
            "preventive": "Changer le ventirad d'origine pour un modèle plus performant."
        },
        "Capteur thermique défaillant ou poussière accumulée": {
            "palliative": "Vérifier que les ventilateurs sont opérationnels.",
            "corrective": "Nettoyer l'intérieur et vérifier le capteur thermique dans le BIOS.",
            "preventive": "Nettoyage préventif tous les 6 mois."
        },
        "Système de refroidissement saturé": {
            "palliative": "Utiliser un support ventilé pour portable.",
            "corrective": "Remplacer le système de refroidissement par un modèle plus performant.",
            "preventive": "Ne pas utiliser le PC sur des surfaces molles (lit, couette)."
        },

        # ══════════════════════════════════════════════════════════════
        #  STOCKAGE
        # ══════════════════════════════════════════════════════════════
        "Panne mécanique imminente du disque dur (HDD)": {
            "palliative": "Sauvegarder immédiatement les données les plus importantes.",
            "corrective": "Remplacer le disque dur par un SSD (beaucoup plus rapide).",
            "preventive": "Éviter les chocs physiques lorsque l'ordinateur est allumé."
        },
        "Secteurs défectueux sur le disque dur": {
            "palliative": "Lancer un 'chkdsk /f /r' pour isoler les secteurs.",
            "corrective": "Cloner le disque sur un nouveau support avant la panne totale.",
            "preventive": "Activer la surveillance SMART du disque dur."
        },
        "Câble SATA débranché ou disque dur HS": {
            "palliative": "Ouvrir le boîtier et vérifier le branchement des câbles SATA.",
            "corrective": "Changer le câble SATA ou le port sur la carte mère.",
            "preventive": "S'assurer que les câbles sont bien clipsés lors du montage."
        },
        "Tête de lecture du disque dur qui raye le plateau": {
            "palliative": "AUCUNE. Éteindre immédiatement pour ne pas perdre plus de données.",
            "corrective": "Envoyer en salle blanche pour récupération de données.",
            "preventive": "Passer au SSD (sans pièces mobiles)."
        },
        "Échec d'initialisation du support de stockage": {
            "palliative": "Vérifier si le disque est détecté dans le BIOS.",
            "corrective": "Changer le disque dur ou le contrôleur SATA.",
            "preventive": "Vérifier la santé du disque avec CrystalDiskInfo."
        },
        "Perte de connexion physique avec le disque dur": {
            "palliative": "Rebrancher les câbles d'alimentation et de données.",
            "corrective": "Changer le câble SATA ou l'alimentation SATA.",
            "preventive": "Assurer un bon maintien mécanique des disques."
        },
        "Disque dur extrêmement fragmenté ou fatigué": {
            "palliative": "Désactiver l'indexation des fichiers.",
            "corrective": "Remplacement par un SSD et clonage.",
            "preventive": "Ne jamais remplir un disque à plus de 90%."
        },
        "Table de partition corrompue nécessitant une récupération de données": {
            "palliative": "Utiliser TestDisk pour tenter de restaurer la table de partition.",
            "corrective": "Récupérer les données avec un logiciel spécialisé puis reformater.",
            "preventive": "Ne jamais interrompre une opération de formatage ou de partitionnement."
        },
        "Clonage incomplet ou mode AHCI/IDE mal configuré dans le BIOS": {
            "palliative": "Vérifier le mode AHCI/IDE dans les paramètres du BIOS.",
            "corrective": "Recommencer le clonage avec un logiciel fiable (Macrium Reflect).",
            "preventive": "Toujours vérifier la compatibilité BIOS avant un clonage."
        },
        "Fichiers temporaires ou clichés instantanés occupant l'espace": {
            "palliative": "Utiliser l'outil 'Nettoyage de disque' de Windows.",
            "corrective": "Supprimer les anciens points de restauration et les clichés instantanés.",
            "preventive": "Planifier un nettoyage de disque automatique mensuel."
        },
        "Port USB défaillant ou alimentation insuffisante pour le disque": {
            "palliative": "Essayer un autre port USB (de préférence à l'arrière du PC).",
            "corrective": "Utiliser un câble USB avec alimentation externe pour le disque.",
            "preventive": "Utiliser un hub USB alimenté pour les disques externes."
        },
        "Contrôleur USB en panne ou hub surchargé": {
            "palliative": "Débrancher tous les autres périphériques USB.",
            "corrective": "Réinstaller les pilotes USB ou remplacer le hub.",
            "preventive": "Ne pas surcharger un seul hub USB avec trop de périphériques."
        },
        "Corruption du système de fichiers ou attaque de malware": {
            "palliative": "Lancer un scan antivirus immédiatement.",
            "corrective": "Exécuter 'chkdsk /f' et restaurer les fichiers depuis une sauvegarde.",
            "preventive": "Maintenir un antivirus actif et faire des sauvegardes régulières."
        },
        "Fichiers chiffrés par un ransomware": {
            "palliative": "NE PAS PAYER LA RANÇON. Isoler le PC du réseau.",
            "corrective": "Utiliser un outil de déchiffrement (nomoreransom.org) si disponible.",
            "preventive": "Sauvegarder les données sur un support externe non connecté en permanence."
        },

        # ══════════════════════════════════════════════════════════════
        #  RÉSEAU & INTERNET
        # ══════════════════════════════════════════════════════════════
        "Carte Wi-Fi désactivée ou pilote manquant": {
            "palliative": "Utiliser un adaptateur USB Wi-Fi externe.",
            "corrective": "Réactiver la carte dans le Gestionnaire de périphériques.",
            "preventive": "Vérifier que le mode avion n'est pas activé par erreur."
        },
        "Problème de configuration IP ou DNS": {
            "palliative": "Utiliser les DNS de Google (8.8.8.8 / 8.8.4.4).",
            "corrective": "Réinitialiser le catalogue TCP/IP (netsh int ip reset).",
            "preventive": "Laisser la configuration IP en mode 'Automatique' (DHCP)."
        },
        "Problème venant du routeur ou du FAI": {
            "palliative": "Redémarrer la box internet (éteindre 30s et rallumer).",
            "corrective": "Appeler le service technique de votre fournisseur d'accès.",
            "preventive": "Vérifier l'état des câbles réseau extérieurs."
        },
        "Service Bluetooth arrêté ou antenne débranchée": {
            "palliative": "Utiliser un dongle Bluetooth externe.",
            "corrective": "Relancer le service 'Support Bluetooth' dans services.msc.",
            "preventive": "S'assurer que les antennes Wi-Fi/BT derrière le PC sont vissées."
        },
        "Défaillance de la carte réseau combo (Wi-Fi + BT)": {
            "palliative": "Utiliser un câble Ethernet pour l'internet.",
            "corrective": "Remplacer la carte M.2 Wi-Fi interne.",
            "preventive": "Ne pas tordre les fils d'antenne lors du démontage."
        },
        "Congestion réseau ou limitation FAI": {
            "palliative": "Tester la vitesse sur fast.com ou speedtest.net.",
            "corrective": "Contacter le FAI pour vérifier les limitations de débit.",
            "preventive": "Monitorer le trafic réseau pour identifier les appareils gourmands."
        },
        "Signal Wi-Fi faible (éloignement du routeur ou interférences)": {
            "palliative": "Se rapprocher du routeur pour tester.",
            "corrective": "Installer un répéteur Wi-Fi ou un système Mesh.",
            "preventive": "Placer le routeur au centre du logement, en hauteur."
        },
        "Pilote Wi-Fi instable ou canal Wi-Fi saturé": {
            "palliative": "Se connecter en filaire (Ethernet) temporairement.",
            "corrective": "Mettre à jour le pilote Wi-Fi et changer le canal dans le routeur.",
            "preventive": "Utiliser la bande 5 GHz plutôt que 2.4 GHz si possible."
        },
        "Port VPN bloqué par le pare-feu ou configuration serveur incorrecte": {
            "palliative": "Essayer un autre protocole VPN (OpenVPN, WireGuard, IKEv2).",
            "corrective": "Configurer le pare-feu pour autoriser les ports VPN nécessaires.",
            "preventive": "Garder le client VPN à jour."
        },
        "Réseau sous-jacent défaillant empêchant le tunnel VPN": {
            "palliative": "Vérifier d'abord que la connexion Internet de base fonctionne.",
            "corrective": "Résoudre le problème de connexion Internet avant de relancer le VPN.",
            "preventive": "Tester la connexion Internet avant de lancer le VPN."
        },
        "Congestion réseau locale ou problème de routage FAI": {
            "palliative": "Redémarrer le routeur.",
            "corrective": "Contacter le FAI pour un diagnostic de ligne.",
            "preventive": "Limiter le nombre d'appareils connectés simultanément."
        },
        "Saturation de la bande passante (téléchargements en cours)": {
            "palliative": "Mettre en pause les téléchargements en cours.",
            "corrective": "Configurer la QoS (Qualité de Service) sur le routeur.",
            "preventive": "Planifier les gros téléchargements en heures creuses."
        },
        "Serveurs DNS configurés inaccessibles ou corrompus": {
            "palliative": "Configurer manuellement les DNS Google (8.8.8.8) ou Cloudflare (1.1.1.1).",
            "corrective": "Vider le cache DNS (ipconfig /flushdns) et réinitialiser le réseau.",
            "preventive": "Utiliser des serveurs DNS publics fiables par défaut."
        },
        "DNS détourné par un malware (DNS Hijacking)": {
            "palliative": "Remettre les DNS en automatique (DHCP).",
            "corrective": "Scanner avec Malwarebytes et vérifier le fichier hosts.",
            "preventive": "Installer une extension de sécurité dans le navigateur."
        },
        "Port Ethernet physiquement endommagé ou câble RJ45 défectueux": {
            "palliative": "Utiliser le Wi-Fi comme alternative.",
            "corrective": "Remplacer le câble RJ45 ou utiliser un adaptateur USB-Ethernet.",
            "preventive": "Manipuler les câbles Ethernet avec soin (ne pas forcer le clip)."
        },

        # ══════════════════════════════════════════════════════════════
        #  PÉRIPHÉRIQUES
        # ══════════════════════════════════════════════════════════════
        "Clavier défectueux ou port USB défaillant": {
            "palliative": "Utiliser le clavier visuel de Windows.",
            "corrective": "Nettoyer les touches ou remplacer le clavier.",
            "preventive": "Éviter de manger ou boire au-dessus du clavier."
        },
        "Capteur de souris sale ou pile déchargée": {
            "palliative": "Nettoyer le capteur optique avec un coton-tige.",
            "corrective": "Remplacer les piles ou essayer un autre tapis de souris.",
            "preventive": "Utiliser un tapis de souris propre et de qualité."
        },
        "Contrôleur USB surchargé ou pilote chipset obsolète": {
            "palliative": "Débrancher les périphériques USB non essentiels.",
            "corrective": "Mettre à jour les pilotes du chipset de la carte mère.",
            "preventive": "Utiliser un hub USB alimenté pour les gros périphériques."
        },
        "Problème de concentrateur USB interne": {
            "palliative": "Utiliser les ports USB situés directement sur la carte mère (arrière).",
            "corrective": "Remplacer le panneau avant du boîtier.",
            "preventive": "Débrancher les périphériques en tirant droit, pas de travers."
        },
        "Périphérique de sortie par défaut mal configuré ou pilote audio": {
            "palliative": "Vérifier le volume et changer le périphérique de sortie dans la barre des tâches.",
            "corrective": "Réinstaller la console audio (Realtek) ou le pilote.",
            "preventive": "Désactiver les améliorations audio susceptibles de bugger."
        },
        "Haut-parleurs débranchés ou carte son intégrée désactivée": {
            "palliative": "Tester avec des écouteurs sur le port jack avant.",
            "corrective": "Vérifier le branchement interne HD_AUDIO sur la carte mère.",
            "preventive": "Ne pas forcer sur la prise Jack."
        },
        "File d'attente d'impression bloquée ou câble débranché": {
            "palliative": "Annuler tous les documents en attente et redémarrer l'imprimante.",
            "corrective": "Relancer le service Spouleur d'impression.",
            "preventive": "Éteindre l'imprimante si elle n'est pas utilisée pendant longtemps."
        },
        "Confidentialité Windows bloquant l'accès ou câble nappe débranché": {
            "palliative": "Vérifier les paramètres de confidentialité de la caméra.",
            "corrective": "Démonter le cadre de l'écran pour rebrancher la webcam.",
            "preventive": "Ne pas coller de stickers trop abrasifs sur la webcam."
        },
        "Pavé tactile désactivé par raccourci clavier": {
            "palliative": "Brancher une souris USB externe.",
            "corrective": "Appuyer sur la touche de fonction correspondante (ex: Fn + F7).",
            "preventive": "Repérer le raccourci clavier du touchpad."
        },
        "Firmware du dock obsolète ou port USB-C non compatible": {
            "palliative": "Brancher les périphériques directement sur le portable.",
            "corrective": "Mettre à jour le firmware du dock et vérifier la compatibilité USB-C.",
            "preventive": "Vérifier les spécifications USB-C avant l'achat d'un dock."
        },
        "Dock USB-C ne supporte pas le DisplayPort Alt Mode": {
            "palliative": "Utiliser un câble HDMI direct sur le portable.",
            "corrective": "Acheter un dock compatible DisplayPort Alt Mode.",
            "preventive": "Vérifier la compatibilité DP Alt Mode avant tout achat."
        },
        "Pilote TWAIN/WIA manquant pour le scanner": {
            "palliative": "Utiliser une application mobile pour scanner temporairement.",
            "corrective": "Installer le pilote TWAIN/WIA depuis le site du fabricant.",
            "preventive": "Garder les pilotes du scanner à jour."
        },
        "Prise jack défectueuse ou pilote audio mal routé": {
            "palliative": "Utiliser un adaptateur USB-audio comme alternative.",
            "corrective": "Vérifier le routage audio dans les paramètres et réinstaller le pilote.",
            "preventive": "Manipuler la prise jack avec délicatesse."
        },
        "Carte audio intégrée en panne": {
            "palliative": "Utiliser une carte son USB externe.",
            "corrective": "Remplacer la carte mère ou installer une carte son PCI-E.",
            "preventive": "Éviter les surtensions qui endommagent les composants intégrés."
        },
        "Pilote XInput/DirectInput manquant ou port USB défaillant": {
            "palliative": "Essayer la manette sur un autre port USB.",
            "corrective": "Installer les pilotes Xbox ou le logiciel du fabricant.",
            "preventive": "Utiliser des manettes officielles compatibles."
        },
        "Mécanisme d'éjection bloqué ou courroie d'entraînement HS": {
            "palliative": "Utiliser un trombone dans le trou d'éjection forcée.",
            "corrective": "Remplacer le lecteur optique.",
            "preventive": "Éviter de forcer le tiroir manuellement."
        },
        "Problème majeur de chipset ou pont sud (Southbridge)": {
            "palliative": "Utiliser des cartes d'extension PCI-E.",
            "corrective": "Remplacer la carte mère.",
            "preventive": "Éviter les surtensions électriques."
        },

        # ══════════════════════════════════════════════════════════════
        #  AUDIO / VIDÉO
        # ══════════════════════════════════════════════════════════════
        "Microphone désactivé dans les paramètres de confidentialité": {
            "palliative": "Vérifier Paramètres > Confidentialité > Microphone.",
            "corrective": "Autoriser l'accès au micro pour les applications concernées.",
            "preventive": "Ne pas désactiver globalement l'accès au microphone."
        },
        "Paramètres de confidentialité Windows bloquant caméra et micro": {
            "palliative": "Aller dans Paramètres > Confidentialité et tout réactiver.",
            "corrective": "Réinitialiser les autorisations pour chaque application.",
            "preventive": "Vérifier les paramètres de confidentialité après chaque mise à jour."
        },
        "Jack audio oxydé ou interférence électromagnétique": {
            "palliative": "Nettoyer la prise jack avec de l'alcool isopropylique.",
            "corrective": "Utiliser un adaptateur audio USB pour contourner le jack.",
            "preventive": "Éloigner les câbles audio des câbles d'alimentation."
        },
        "Carte son en fin de vie": {
            "palliative": "Utiliser un adaptateur USB-audio externe.",
            "corrective": "Installer une carte son PCI-E ou remplacer la carte mère.",
            "preventive": "Protéger le PC des surtensions."
        },
        "Buffer audio trop petit ou pilote ASIO manquant": {
            "palliative": "Augmenter la taille du buffer audio dans les paramètres.",
            "corrective": "Installer ASIO4ALL pour une meilleure gestion audio.",
            "preventive": "Utiliser une interface audio dédiée pour la production."
        },
        "GPU sous-dimensionné ou pilote graphique obsolète": {
            "palliative": "Baisser la qualité vidéo ou la résolution.",
            "corrective": "Mettre à jour le pilote GPU ou changer la carte graphique.",
            "preventive": "Vérifier les configurations recommandées avant de jouer."
        },

        # ══════════════════════════════════════════════════════════════
        #  SÉCURITÉ
        # ══════════════════════════════════════════════════════════════
        "Adware ou logiciel malveillant installé": {
            "palliative": "Installer une extension de blocage de pub (uBlock Origin).",
            "corrective": "Nettoyer le système avec AdwCleaner.",
            "preventive": "Toujours décocher les logiciels 'offerts' lors des installations."
        },
        "Browser Hijacker ou DNS infecté": {
            "palliative": "Réinitialiser les paramètres par défaut du navigateur.",
            "corrective": "Vérifier et vider le fichier 'hosts' de Windows.",
            "preventive": "Ne pas installer d'extensions de navigateur non vérifiées."
        },
        "Ransomware actif — isoler immédiatement la machine du réseau": {
            "palliative": "DÉCONNECTER LE PC DU RÉSEAU IMMÉDIATEMENT (câble + Wi-Fi).",
            "corrective": "Consulter nomoreransom.org pour un outil de déchiffrement.",
            "preventive": "Sauvegarder régulièrement sur un support externe déconnecté."
        },
        "Ransomware ayant chiffré les données — récupération urgente": {
            "palliative": "NE PAS PAYER. Consulter un spécialiste en cybersécurité.",
            "corrective": "Restaurer les fichiers depuis une sauvegarde hors-ligne.",
            "preventive": "Appliquer la règle 3-2-1 : 3 copies, 2 supports, 1 hors-site."
        },
        "Malware avancé désactivant les protections (rootkit probable)": {
            "palliative": "Démarrer depuis un antivirus bootable (Kaspersky Rescue Disk).",
            "corrective": "Scan hors-ligne complet suivi d'une réinstallation si nécessaire.",
            "preventive": "Activer le Secure Boot dans le BIOS."
        },
        "Infection profonde nécessitant un scan hors-ligne": {
            "palliative": "Déconnecter le PC d'Internet pour limiter la propagation.",
            "corrective": "Utiliser un Live USB antivirus pour scanner le disque.",
            "preventive": "Ne jamais désactiver Windows Defender manuellement."
        },
        "Fichiers corrompus ou chiffrés par un malware": {
            "palliative": "Vérifier si des copies existent dans les 'Versions précédentes'.",
            "corrective": "Scanner et nettoyer avec un antivirus, restaurer depuis sauvegarde.",
            "preventive": "Maintenir des sauvegardes régulières sur un support externe."
        },
        "Potentiel cheval de Troie (RAT) communicant avec un serveur distant": {
            "palliative": "Couper la connexion Internet du PC.",
            "corrective": "Scanner avec un anti-malware avancé (Malwarebytes, HitmanPro).",
            "preventive": "Activer le pare-feu Windows et surveiller le trafic réseau."
        },
        "Malware utilisant la bande passante pour du minage ou du spam": {
            "palliative": "Surveiller les processus réseau dans le Gestionnaire des tâches.",
            "corrective": "Identifier et supprimer le processus malveillant, scanner le système.",
            "preventive": "Ne pas télécharger de logiciels depuis des sites non officiels."
        },
        "Compromission de compte — changement de mots de passe urgent": {
            "palliative": "Changer immédiatement le mot de passe depuis un autre appareil.",
            "corrective": "Activer l'authentification à deux facteurs (2FA) sur tous les comptes.",
            "preventive": "Utiliser un gestionnaire de mots de passe (Bitwarden, KeePass)."
        },
        "Session piratée via un keylogger ou phishing": {
            "palliative": "Se déconnecter de toutes les sessions actives.",
            "corrective": "Scanner le PC, changer tous les mots de passe, activer le 2FA.",
            "preventive": "Ne jamais entrer ses identifiants sur un lien reçu par mail."
        },

        # ══════════════════════════════════════════════════════════════
        #  PORTABLE
        # ══════════════════════════════════════════════════════════════
        "Chargeur défectueux ou connecteur de charge (DC-Jack) cassé": {
            "palliative": "Maintenir le chargeur dans une position précise pour charger.",
            "corrective": "Remplacer le chargeur ou souder un nouveau connecteur DC-Jack.",
            "preventive": "Ne pas tirer sur le câble du chargeur."
        },
        "Batterie en fin de cycle de vie (usure chimique)": {
            "palliative": "Utiliser l'ordinateur uniquement branché sur secteur.",
            "corrective": "Acheter une batterie neuve d'origine.",
            "preventive": "Éviter les décharges complètes (en dessous de 10%)."
        },
        "Circuit de charge ou batterie totalement HS": {
            "palliative": "Utiliser un chargeur universel pour tester.",
            "corrective": "Changement de batterie et vérification du contrôleur de charge.",
            "preventive": "Calibrer la batterie une fois par mois."
        },
        "Oxydation imminente des composants (nécessite nettoyage ISOPRO)": {
            "palliative": "Éteindre et retourner l'ordinateur pour laisser couler le liquide.",
            "corrective": "Ouvrir et nettoyer la carte mère à l'alcool isopropylique à 99%.",
            "preventive": "Garder les boissons loin de l'espace de travail."
        },
        "Court-circuit majeur dû au liquide": {
            "palliative": "Placer l'appareil dans un sac de déshydratant (PAS de riz).",
            "corrective": "Passage en bac à ultrasons pour désoxydation.",
            "preventive": "Acheter une housse de protection clavier."
        },
        "Charnière d'écran à remplacer (risque de coupure du câble nappe)": {
            "palliative": "Éviter d'ouvrir/fermer l'écran pour limiter les dégâts.",
            "corrective": "Faire remplacer la charnière par un réparateur.",
            "preventive": "Manipuler l'écran du portable avec douceur."
        },
        "Câble nappe vidéo endommagé par la charnière cassée": {
            "palliative": "Trouver un angle d'ouverture où l'écran fonctionne.",
            "corrective": "Remplacer le câble nappe vidéo (LVDS/eDP).",
            "preventive": "Réparer la charnière avant qu'elle n'endommage le câble."
        },
        "Nettoyage clavier nécessaire ou remplacement de membrane": {
            "palliative": "Utiliser un clavier USB externe.",
            "corrective": "Retirer les touches et nettoyer avec de l'air comprimé et alcool.",
            "preventive": "Utiliser un protège-clavier en silicone."
        },
        "Dommage par liquide sous les touches": {
            "palliative": "Retourner le portable immédiatement pour drainer le liquide.",
            "corrective": "Démonter le clavier, nettoyer à l'alcool isopropylique 99%.",
            "preventive": "Ne jamais boire au-dessus de son portable."
        },
        "Chargeur non d'origine ou puissance insuffisante": {
            "palliative": "Utiliser le chargeur d'origine si disponible.",
            "corrective": "Acheter un chargeur d'origine ou certifié avec la bonne puissance.",
            "preventive": "Toujours vérifier la puissance (Watts) du chargeur avant achat."
        },
        "Chargeur défaillant risquant d'endommager la batterie": {
            "palliative": "Cesser d'utiliser le chargeur suspect.",
            "corrective": "Remplacer par un chargeur d'origine certifié.",
            "preventive": "Ne pas utiliser de chargeurs contrefaits ou sans marque."
        },
        "Dalle LCD à remplacer": {
            "palliative": "Brancher un écran externe en attendant.",
            "corrective": "Commander et remplacer la dalle LCD compatible.",
            "preventive": "Transporter le portable dans une housse rembourrée."
        },
        "Dalle LCD+tactile complète à remplacer": {
            "palliative": "Utiliser un écran externe avec souris et clavier.",
            "corrective": "Remplacer l'ensemble dalle LCD + digitizer tactile.",
            "preventive": "Protéger l'écran avec un film protecteur."
        },

        # ══════════════════════════════════════════════════════════════
        #  DIVERS
        # ══════════════════════════════════════════════════════════════
        "Court-circuit critique (Danger d'incendie !)": {
            "palliative": "DÉBRANCHER TOUT IMMÉDIATEMENT !",
            "corrective": "Identifier le composant brûlé et le jeter (Recyclage DEEE).",
            "preventive": "Ne jamais laisser un PC suspect allumé sans surveillance."
        },
        "Composant VRM ou condensateur qui a explosé": {
            "palliative": "Aucune. Risque de dommages en cascade.",
            "corrective": "Remplacer la carte mère ou le composant (si expert soudure).",
            "preventive": "Éviter les alimentations bas de gamme sans marque."
        },
        "Code d'erreur sonore de la carte mère (consulter manuel)": {
            "palliative": "Compter le nombre de bips (longs/courts).",
            "corrective": "Se référer au manuel constructeur pour identifier le composant.",
            "preventive": "Noter la marque et le modèle de la carte mère."
        },
    }

    @classmethod
    def get_solutions(cls, diagnosis):
        return cls.SOLUTIONS.get(diagnosis, {
            "palliative": "Consulter un technicien spécialisé.",
            "corrective": "Rechercher le message d'erreur spécifique sur internet.",
            "preventive": "Maintenir votre système à jour."
        })
