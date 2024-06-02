list_causes_effets = [
    {
        "organe": "Mémoire vive (RAM)",
        "mode_defaillance": "",
        "cause": "\t-\tMauvais contact des modules de RAM / Défaillance matérielle\n",
        "effets": ["Plantages fréquents", "Erreurs d'écran bleu", "Ralentissements"],
        "mots_cles":{
            "Plantages fréquents": ["plante","plantage", "dysfonctionnement", "ralentissement"],
            "Erreurs d'écran bleu": ["bleu"]
        },
        "detection": "audio/visuel",
        "solution": "\t-\tRetirer et réinsérer les modules de RAM,\n\t-\tvérifier leur compatibilité,\n\t-\texécuter des tests de mémoire,\n\t-\tremplacer les modules défectueux\n",
        "prevention": "Sauvegarde régulière des données dans un disque dur externe pour éviter une perte totale en cas de panne"
    },
    {
        "organe": "Carte sonore",
        "mode_defaillance": "",
        "cause": "\t-\tPilotes audio obsolètes, mauvaise configuration, défaillance matérielle\n",
        "effets": ["Pas de son", "son de mauvaise qualité", "icône de carte sonore grisée dans les paramètres audio"],
        "mots_cles":{
            "Pas de son": ["son", "audio"],
            "son de mauvaise qualité": ["qualité du son"],
            "icône de carte sonore grisée dans les paramètres audio": ["carte son", "paramètres audio", "icône grisée"]
        },
        "detection": "audio/visuel",
        "solution": "\t-\tMettre à jour les pilotes audio,\n\t-\tvérifier les paramètres de son et de périphériques,\n\t-\ttester avec des écouteurs ou des haut-parleurs externes,\n\t-\tremplacer la carte son défectueuse si nécessaire\n",
        "prevention":""
    },
    {
        "organe": "Alimentation",
        "mode_defaillance": "",
        "cause": "\t-\tProblèmes électriques, surcharge, vieillissement de l'alimentation\n",
        "effets": ["L'ordinateur ne démarre pas", "redémarrages aléatoires", "erreurs matérielles"],
        "mots_cles":{
            "L'ordinateur ne démarre pas": ["démarrage", "allumer", "allume"],
            "redémarrages aléatoires": ["redémarrages", "aléatoire"],
            "erreurs matérielles": ["matériel"]
        },
        "detection": "audio/visuel",
        "solution": "\t-\tVérifier les câbles d'alimentation,\n\t-\ttester l'alimentation avec un multimètre,\n\t-\tremplacer l'alimentation défectueuse si nécessaire\n",
        "prevention":""
    },
    {
        "organe": "Disque dur",
        "mode_defaillance": "Panne du disque dur",
        "cause": "\t-\tUsure normale/ Défaillance mécanique/ Surtension électrique\n",
        "effets": ["Le système ne démarre pas", "Des erreurs de lecture/écriture se produisent fréquemment", "Des bruits inhabituels émanents du disque dur"],
        "mots_cles":{
            "Le système ne démarre pas": ["système", "démarrage"],
            "Des erreurs de lecture/écriture se produisent fréquemment": ["erreurs de lecture", "erreurs d'écriture"],
            "Des bruits inhabituels émanents du disque dur": ["bruits inhabituels", "disque dur"]
        },
        "detection": "audio/visuel",
        "solution": "\t-\tRemplacement du disque dur défectueux,\n\t-\trécupération des données si possible\n",
        "prevention": "Sauvegarde régulière des données dans un disque dur externe pour éviter une perte totale en cas de panne"
    },
        {
        "organe": "Disque dur",
        "mode_defaillance": "Secteurs défectueux",
        "cause": "Usure normale des secteurs défectueux",
        "effets": ["Des erreurs de lecture/écriture apparaissent fréquemment", "Le système peut se figer ou redémarrer de manière inattendue"],
        "mots_cles": {
        "Des erreurs de lecture/écriture apparaissent fréquemment": ["erreurs de lecture", "erreurs d'écriture"],
        "Le système peut se figer ou redémarrer de manière inattendue": ["système", "figer", "redémarrer"]
        },
        "detection": "audio/visuel",
        "solution": "\t-\tUtiliser des outils de diagnostic pour marquer les secteurs défectueux,\n\t-\tremplacer le disque dur si nécessaire\n",
        "prevention": "\t-\tEffectuer régulièrement des analyses de disque pour détecter les secteurs défectueux et les corriger\n"
        },
        {
        "organe": "Processeur",
        "mode_defaillance": "",
        "cause": "Surchauffe, overclocking instable, défaillance matérielle",
        "effets": ["Ralentissements", "plantages fréquents", "redémarrages aléatoires"],
        "mots_cles": {
        "Ralentissements": ["ralentissements", "ralenti"],
        "plantages fréquents": ["plantages", "dysfonctionnements"],
        "redémarrages aléatoires": ["redémarrages", "aléatoire"]
        },
        "detection": "audio/visuel",
        "solution": "\t-\tVérifier les températures du processeur,\n\t-\tnettoyer les dissipateurs de chaleur,\n\t-\téviter l'overclocking instable,\n\t-\tremplacer le processeur défectueux si nécessaire\n",
        "prevention": ""
        },
        {
        "organe": "Câble réseau, Modem, câble Ethernet, routeur",
        "mode_defaillance": "Etat",
        "cause": "Carte réseau défectueuse/ Mauvaise connexion physique",
        "effets": ["Echec de la connexion à internet"],
        "mots_cles": {
        "Echec de la connexion à internet": ["connexion", "internet"],
        },
        "detection": "visuelle",
        "solution": "\t-\tRéparer ou changer la carte réseau,\n\t-\tvérifier les connexions\n",
        "prevention": ""
        },
        {
        "organe": "Proxy",
        "mode_defaillance": "Configuration",
        "cause": "Mauvaise configuration",
        "effets": ["Difficultés de navigation"],
        "mots_cles": {
        "Difficultés de navigation": ["navigation"]
        },
        "detection": "visuelle",
        "solution": "\t-\tVérifier les paramètres du pare-feu pour s'assurer que les applications et les ports concernés sont autorisés\n",
        "prevention": ""
        },
    {
    "organe": "Pare feu",
    "mode_defaillance": "Configuration",
    "cause": "Mauvaise configuration",
    "effets": ["Aucun accès à internet"],
    "mots_cles": {
    "Aucun accès à internet": ["accès à internet", "internet"]
    },
    "detection": "",
    "solution": "",
    "prevention": ""
    },
    {
    "organe": "Navigateur",
    "mode_defaillance": "Etat, configuration",
    "cause": "Extensions ou plugins problématiques/ Paramètres de sécurité excessivement stricts/ Navigateur obsolète",
    "effets": ["Mauvais accès à internet"],
    "mots_cles": {
    "Mauvais accès à internet": ["mauvais accès à internet", "accès à internet"]
    },
    "detection": "visuelle",
    "solution": "\t-\tUtiliser un autre navigateur ou réinitialiser les paramètres par défaut du navigateur\n",
    "prevention": ""
    },
    {
    "organe": "Antenne Wi-Fi",
    "mode_defaillance": "Etat",
    "cause": "Antenne défectueuse ou mal positionnée",
    "effets": ["Problèmes de connectivité"],
    "mots_cles": {
    "Problèmes de connectivité": ["connectivité", "wifi"]
    },
    "detection": "visuelle",
    "solution": "\t-\tVérifier les connexions de votre adaptateur Wi-Fi\n",
    "prevention": ""
    },
    {
    "organe": "Processeur",
    "mode_defaillance": "Surchage",
    "cause": "les applications ou les processus gourmands en ressources",
    "effets": ["Ralentissement d'exécution des tâches"],
    "mots_cles": {
    "Ralentisement d'exécution des tâches": ["ralentissement", "ralentit"]
    },
    "detection": "Visuelle",
    "solution": "\t-\tUtilisez le gestionnaire de tâches (Windows) ou le moniteur d'activité (Mac) pour identifier les processus ou les applications qui consomment anormalement des ressources.\n\t-\tSi nécessaire, fermez les applications ou les processus gourmands en ressources pour améliorer les performances globales\n",
    "prevention": "\t-\tEviter de faire tourner trop d'applications à la fois\n"
    },
{
    "organe": "Processeur",
    "mode_defaillance": "Surchage",
    "cause": "Programmes non essentiels au démarrage",
    "effets": ["Ralentissement au démarrage"],
    "mots_cles": {
        "Ralentissement au démarrage": ["démarrage", "ralenti"]
    },
    "detection": "visuelle",
    "solution": "Supprimer les programmes inutiles ou indésirables qui s'exécutent au démarrage de votre ordinateur.\n\t-\tUtilisez l'outil de configuration du système (msconfig sur Windows) pour désactiver les programmes non essentiels au démarrage.",
    "prevention": "N/A"
},
{
    "organe": "Disque Dur",
    "mode_defaillance": "Saturation",
    "cause": "Fragmentation des fichiers",
    "effets": ["Ralentissement lors de l'accès aux données"],
    "mots_cles": {
        "Ralentissement lors de l'accès aux données": ["ralenti", "accès aux données"]
    },
    "detection": "visuelle",
    "solution": "Utiliser l'outil de défragmentation intégré à votre système d'exploitation pour regrouper les fragments de fichiers et améliorer les performances de lecture et d'écriture.",
    "prevention": "Défragmenter régulièrement votre disque dur."
},
{
    "organe": "Disque dur",
    "mode_defaillance": "Saturation",
    "cause": "Disque dur plein ou presque plein",
    "effets": ["Ralentissement lors de l'accès aux données"],
    "mots_cles": {
        "Ralentissement lors de l'accès aux données": ["ralenti"]
    },
    "detection": "visuelle",
    "solution": "Utiliser l'outil de nettoyage de disque intégré à votre système d'exploitation pour libérer de l'espace disque et améliorer les performances.",
    "prevention": "Nettoyer régulièrement votre disque dur en supprimant les fichiers temporaires, les fichiers en cache, les fichiers inutiles et les anciennes sauvegardes."
},
{
    "organe": "RAM",
    "mode_defaillance": "Insuffisance",
    "cause": "Mémoire insuffisante",
    "effets": ["Ralentissements et blocages"],
    "mots_cles": {
        "Ralentissements et blocages": ["blocage", "ralenti"]
    },
    "detection": "visuelle",
    "solution": "Consulter les spécifications de votre ordinateur pour déterminer la quantité maximale de mémoire prise en charge et ajouter des modules RAM supplémentaires si nécessaire.",
    "prevention": "Utiliser des outils de nettoyage et d'optimisation du système pour détecter et résoudre les problèmes de performances."
},
{
    "organe": "Clavier",
    "mode_defaillance": "",
    "cause": "Saleté, Liquide renversé, Dommages mécaniques, Mauvaise connexion du périphérique",
    "effets": ["Certaines touches ne fonctionnent pas", "les raccourcis claviers qui ne répondent pas"],
    "mots_cles": {
        "Certaines touches ne fonctionnent pas": ["touche","bouton"]
    },
    "detection": "visuelle",
    "solution": "Nettoyer les boutons, vérifier les connexions, remplacer les boutons défectueux, sécher le clavier en cas de liquide.\n\t-\tUtilisation de la souris pour manipuler le clavier virtuel.\n\t-\tClavier Bluetooth.\n\t-\tOptions tiers dans les menus de fichiers.",
    "prevention": "Évitez de manger ou de boire au-dessus du clavier.\n\t-\tNettoyez régulièrement les touches avec un chiffon doux ou de l'air comprimé.\n\t-\tNe pas forcer les touches du clavier."
},
    {
        "organe": "Clavier et Souris",
        "mode_defaillance":"",
        "cause": "Câblages endommagés, connecteurs desserés, problèmes électriques",
        "effets":["Aucune connexion", "Alimentation défaillante"],
        "mots_cles":{
           "Aucune connexion": ["câble"],
           "Alimentation défaillante":["alimentation du clavier"]
        },
        "detection":"visuelle",
        "solution":"\t-\tVérifier régulièrement les câbles et connecteurs,\n \t-\tEviter de tirer sur les câbles défectueux,\n \t-\tRésoudre les problèmes électriques",
        "prevention":"\t-\tManipulez les câbles avec précaution,\n \t-\tEvitez de plier les câbles excessiveent,\n \t-\tFixez correctement les connecteurs",
    },
        {
        "organe": "Clavier sans fil/ Souris sans fil",
        "mode_defaillance": "",
        "cause": "Problème de connectivité/ Pilote obsolète/ Connexions défectueuses",
        "effets": [
            "Le clavier sans fil ne fonctionne pas ou n'est pas détecté après l'installation",
            "La souris sans fil ne fonctionne pas ou n'est pas détectée après l'installation"
        ],
        "mots_cles": {
            "Le clavier sans fil ne fonctionne pas ou n'est pas détecté après l'installation": [
                "clavier sans fil ne fonctione pas",
                "clavier sans fil n'est pas détecté"
            ],
            "La souris sans fil ne fonctionne pas ou n'est pas détectée après l'installation": [
                "souris sans fil ne fonctione pas",
                "souris sans fil n'est pas détecté"
            ]
        },
        "detection": "visuelle",
        "solution": "\t-\tVérifier les piles du clavier sans fil,\n\t-\tRapprochez le clavier(ou souris) sans fil du récepteur USB,\n\t-\tRéinstallation des pilotes, vérifier les connectivités de tout l'équipement (USB)\n",
        "prevention": "Utiliser les piles de bonne qualité,\n\t-\tEvitez les distances excessives entre le clavier(ou souris) et le récepteur,\n\t-\tEffectuez régulièrement les mises à jour des pilotes,\n\t-\tManipulez la souris(ou clavier) sans fil avec précaution"
    },
    {
        "organe": "Souris",
        "mode_defaillance": "",
        "cause": "Mauvaise connexion entre la souris et l'ordinateur/ Problème de surface (le capteur de la souris peut ne pas détecter les mouvements correctement)/ Capteurs de souris défectueux",
        "effets": [
            "Le curseur ne suit pas les mouvements de la souris",
            "Le curseur de la souris ne se déplace que dans le sens horizontal ou vertical (ou se déplace mal à l'écran)"
        ],
        "mots_cles": {
            "Le curseur ne suit pas les mouvements de la souris": [
                "curseur ne suit pas",
                "curseur"
            ],
            "Le curseur de la souris ne se déplace que dans le sens horizontal ou vertical (ou se déplace mal à l'écran)": [
                "vertical",
                "horizontal",
                "curseur se déplace mal"
            ]
        },
        "detection": "visuelle",
        "solution": "\t-\tVérification de la surface(utiliser un tapis de souris ou une surface mâte non-réfléchissante),\n\t-\tNettoyer la souris,\n\t-\tRéinstallation des pilotes\n",
        "prevention": "Assurez-vous d'utiliser une surface appropriée pour un suivi du curseur,\n\t-\tEffectuez des mises à jour réguilères des pilotes,\n\t-\tNettoyez régulièrement votre souris"
    },
    {
        "organe": "Souris",
        "mode_defaillance": "",
        "cause": "Usure mécanique/ Encrassement/ Poussière/ Mauvais contact électrique",
        "effets": [
            "Les boutons ne fonctionnent pas",
            "Clics intempestifs",
            "Molette bloquée"
        ],
        "mots_cles": {
            "Les boutons ne fonctionnent pas": [
                "bouton de la souris"
            ],
            "Clics intempestifs": [
                "clics intempestifs"
            ],
            "Molette bloquée": [
                "molette bloqué",
                "molette"
            ]
        },
        "detection": "visuelle",
        "solution": "\t-\tNettoyer les boutons électriques,\n\t-\tvérifier les connexions,\n\t-\tremplacer les boutons défectueux\n",
        "prevention": "Evitez de placer la souris dans des environnements poussiéreux,\n\t-\tnettoyer régulièrement la souris"
    }
]