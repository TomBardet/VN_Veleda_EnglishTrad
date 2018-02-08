#######################################################################################################
# On gère ici les interventions du narrateur sans décor, ainsi que la place du village et les endings #
#######################################################################################################

label start:
    
    python :
        
        #########################################################################################
        ######################## - Defining Misc - ##############################################
        interlocuteur = "None" ## Ne pas oublier d'actualiser le nom de l'interlocuteur à chaque changement
        lieu = "None" ## Ne pas oublier d'actualiser le nom du lieu à chaque changement
        CAactif = False ## Set à False après chaque actionChoice
        inventory = Inventory()
        
        ######### - LES PERSONNAGES DATING SIM - ############
        
        goat_char = Chara("Goat", 20,100)
        ingrid_char = Chara("Ingrid", 50, 100)
        vel_char = Chara("Véléda", 25,100)
        ern_char = Chara("Ernust", 90, 9999)
        brut_char = Chara("Brutalmund", 35, 100)
        cross_char = Chara("Crossfitrichernvald", 20, 100)
        beau_char = Chara("Beaudrik", 50, 100)
        num_char = Chara ("Numerimus", 0, 100)
        dig_char = Chara("Digitimus", 0, 100)

        
        ########## - LES ITEMS DE L'INVENTAIRE - ############
        
        glaive = Item("glaive",player="ex", imageIdle="images/inv_swordIdle.png",imageHover="images/inv_swordHover.png")
        bouclier = Item("bouclier",player="ex", imageIdle="images/inv_shieldIdle.png",imageHover="images/inv_shieldHover.png")   
        blague = Item("blague",player="ex", imageIdle="images/inv_jokeIdle.png",imageHover="images/inv_jokeHover.png") 
        lunettes = Item("lunettes",player="ex", imageIdle="images/inv_glassesIdle.png",imageHover="images/inv_glassesHover.png")
        trompette = Item("trompette",player="ex", imageIdle="images/inv_trumpetidle.png",imageHover="images/inv_glassesHover.png")
            
        ########## - LES ITEMS DE L'INVENTAIRE - ############
        
        _testBlague = 0
        _testBouclier = 0
        _testGlaive = 0
        _testLunettes = 0
        _testTrompette = 0
        
        ########## - TAGs (CHOIX ET BRANCHES) - #################
        
        Acte1_Tour_CoupableJugement = "Brutalmund" # Coupable de l'Acte 1 -> "Brutalmund" ou "Crossfit"
        Acte2_Forge_FirstVisit = 0 # Check si on a déjà visité la forge
        Acte2_Romains_FirstVisit = 0 #
        Forge_reply_arnaque = 0
        Forge_LeaderPrice_check = 0
        Romain_EntenduParlerDesLunettes_check = 0
    
    stop music
    jump intro
    
# -----------------------------------------#
label intro:
    
    window hide

    $ renpy.music.play("music/MUSIC_Main_CarteVillage.ogg", channel = "music1", loop = True, fadein = 1.5)
    $ renpy.music.play("ambiances/AMB_Lieu_CarteVillage_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    $ renpy.music.set_volume(0.4, delay=0, channel='music1')
    $ renpy.music.set_volume(0.4, delay=0, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0, channel='ambiance')
    show introCarte :
        zoom 1,xanchor 0.0 yanchor 0.0
        xpos 0 ypos 0
        linear 1.0 xpos -0.05 ypos 0.0025 zoom 1.05
        
   # show introCarte:
   #     xpos 0.01 ypos 0.01 zoom 1.1
    $ renpy.pause(0.8, hard=True)
    play sound "sfx/SFX_Drapeau_Fall_01.ogg"
    show introFlag zorder 2 with vpunch:
        zoom 1 xanchor 0.5 yanchor 0.5
        xpos 0.65 ypos 0.20
        linear 0.2 ypos 0.35 zoom 0.65
    show introCrack zorder 1 with Dissolve(0.25):
        zoom 0.75,xanchor 0.5 yanchor 0.5
        xpos 0.651 ypos 0.37  
    $ renpy.pause(0.2, hard=True)
    
    

    play sound "sfx/Voices/Narrateur/Narrateur_Intro_01.ogg"
      
    outlineBot "{cps=1} {/cps}{cps=18}En l'an 70 après Jissé,{cps=2} {/cps}{cps=18}toute la Germanie est occupée par les Romains.{/cps}"
    
    
    
    play sound "sfx/SFX_Drapeau_Fly_01.ogg"
    
    show introFlag:
        parallel:
            linear 1.5 xpos -.2
        parallel:
            easeout 1.5 rotate -3200
            repeat #counterclockwise
        parallel:
            linear 2.0 alpha 0.0
    
    show introCrack:
        linear 1.3 alpha 0.0
        
    $ renpy.pause(0.9, hard=True)
    
    play sound "sfx/Voices/Narrateur/Narrateur_Intro_02.ogg"
       
    outlineBot "{cps=1} {/cps}{cps=20}Bon,{cps=1} {/cps}{cps=18}pas vraiment toute en fait...{/cps}"
    
    

    play sound "sfx/SFX_Cross_01.ogg"
    show introPoint with vpunch:
        zoom 1.1,xanchor 0.5 yanchor 0.5
        xpos 0.6 ypos 0.45 
    
    play sound "sfx/Voices/Narrateur/Narrateur_Intro_03.ogg"
    
    $ renpy.pause (0.2, hard = True)
    
    outlineBot "{cps=1} {/cps}{cps=20}En tout cas,{cps=2} {/cps}pas le village des Bructères,{cps=2} {/cps}{cps=20}où habite la légendaire prophétesse Véléda.{/cps}"
    
    play sound "sfx/Voices/Narrateur/Narrateur_Intro_04.ogg"
    show bg_place with Dissolve (0.5):
        zoom 1 xanchor 0.0 yanchor 0.0
    show bg_place :
        zoom 1 xanchor 0.0 yanchor 0.0
        linear 2.5 xpos -1000 ypos 0 zoom 1.8

    outlineBot "{cps=2} {/cps}{cps=20}Elle habite dans la tour,{/cps}{cps=2} {/cps}{cps=10}là,{/cps}{cps=20} adulée par tous{/cps}{cps=3}...{/cps} {cps=45}sauf par ses proches parceque c'est quand même une vieille peau.{/cps}"
    
    play sound "sfx/Voices/Narrateur/Narrateur_Intro_05.ogg"
    
    outlineBot "{cps=2} {/cps}{cps=20}Tu vas incarner Gaufrid{/cps},{cps=2} {/cps}{cps=20}son assistant.{/cps}"
    
    play sound "sfx/Voices/Narrateur/Narrateur_Intro_06.ogg"
    
    #scene black with Dissolve(1.5)
    show bg_place :
        zoom 1.8 xanchor 0.0 yanchor 0.0
        linear 0.9 xpos -400 ypos -500 zoom 1.8
    
    outlineBot "{cps=2} {/cps}{cps=20}Il doit être à la Taverne{/cps}{cps=10}...{/cps}{cps=20} c'est un peu sa deuxième maison.{/cps}"

    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    show bg_place :
        linear 1 xpos -600 ypos -650 zoom 2.1
    scene black with Dissolve (1.5)
    
    jump taverne_DatingIngrid
    
# -----------------------------------------#

label narration_ellipse01: #La première ellipse après le Dating Sim avec Ingrid
    
    scene black with Dissolve (1.5)
    
    play sound "sfx/SFX_Sleep_01.ogg"
    
    pause 3.0
    
    outline "Le lendemain matin..."
    
    play sound "sfx/Voices/Player/Char_Player_Baille_02.ogg"
    y "Ooooaaaaah !"
    y "C'était vraiment bizarre, hier soir je voyais des chiffres au-dessus de la tête des gens !"
    y "Et puis le narrateur arrêtait pas de parler..."
    y "Allez, faut que j'aille au boulot moi !"
    
    play sound "sfx/SFX_Walk_01.ogg"
    
    pause 2.0
    
    jump tourVeleda_ErnustEtVeleda
    
# -----------------------------------------#    
    
label narration_ellipse02:
    scene black with Dissolve (1.5)
    outline "De retour à la Taverne..."
    
    jump taverne_PresentationDot
    
# -----------------------------------------#

label PlaceDuVillageDefault:

    scene bg_place with Dissolve(1.0):
        zoom 1.0
    window hide
    
    $ renpy.music.play("music/MUSIC_Main_CarteVillage.ogg", channel = "music1", loop = True, fadein = 1.5)
    $ renpy.music.play("ambiances/AMB_Lieu_CarteVillage_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    $ _return = renpy.call_screen("action_choice_placeVillage")
    
    if _return == "etables":
        y "On passe aux étables !"
        scene bg_place:
            zoom 1.0
            linear 0.5 zoom 1.3 xpos -0.35 ypos -0.28
        pause 0.1
        stop music1 fadeout 1.5
        stop ambiance fadeout 0.5
        scene black with Dissolve(1.5)
        window show
    
        jump etable_fromPlace
        
    elif _return == "forge":
        y "Direction : la forge !"
        scene bg_place:
            zoom 1.0
            linear 0.5 zoom 1.3 xpos -0.3 ypos -0.28
        pause 0.1
        window show
        stop music1 fadeout 1.5
        stop ambiance fadeout 0.5
        scene black with Dissolve(1.5)
        jump forge_BrutalmundEtBeaudrik
    elif _return == "tente":
        y "Allons faire un coucou aux Romains !"
        scene bg_place:
            zoom 1.0
            easeout 0.5 zoom 1.6 xpos 0.0 ypos -0.45
        pause 0.1
        stop music1 fadeout 1.5
        stop ambiance fadeout 0.5
        scene black with Dissolve(1.5)
        jump romains_PremiereRencontre

# -----------------------------------------#

label narration_ellipseCuite:
    scene black with Dissolve (1.5)
    outline "Une durée indéterminée de temps plus tard..."
    y "J'ai mal à la tête..."
    y "Bon. Ingrid m'a demandé de lui ramener un {b}glaive{/b} et un {b}bouclier{/b}..."
    y "Je trouverai surement ça au village."
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    $ _window_during_transitions = False
    jump PlaceDuVillageDefault

# -----------------------------------------#

label PlaceDuVillageAllObjects:
    scene bg_place
    window hide
    $ renpy.music.play("music/MUSIC_Main_CarteVillage.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_CarteVillage_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    y "Attends... J'ai un glaive..."
    show screen inventory_screen(obj = "glaive")
    pause 3.0
    hide screen inventory_screen
    y "... Et j'ai un bouclier..."
    show screen inventory_screen(obj = "bouclier")
    pause 3.0
    hide screen inventory_screen
    y "J'ai la dot pour Ingrid !"
    y "Faut que j'aille à la taverne !"
    
    $ _return = renpy.call_screen("action_choice_placeVillageFinal")
    
    if _return == "taverne":
        window show
        stop music1 fadeout 1.5
        stop ambiance fadeout 0.5
        jump Act2_transition_alldone

# -----------------------------------------#





###########################################################################################
# OLD - Le proto technique avec les dialogues correspondant et les enchainements utilisés #
###########################################################################################

label OLD_start:
    python :
        ###Les personnages
        goat_char = Chara("Goat", 20,100)
        vel_char = Chara("Véléda", 25,100)
        #### On crée nos items
        glaive = Item("glaive",player="ex", imageIdle="images/inv_swordIdle.png",imageHover="images/inv_swordHover.png")
        bouclier = Item("bouclier",player="ex", imageIdle="images/inv_shieldIdle.png",imageHover="images/inv_shieldHover.png")   
        blague = Item("blague",player="goat_char", imageIdle="images/inv_jokeIdle.png",imageHover="images/inv_jokeHover.png") 
        lunettes = Item("lunettes",player="ex", imageIdle="images/inv_glassesIdle.png",imageHover="images/inv_glassesHover.png") 
            
        inventory = Inventory()
        inventory.add(glaive)
        inventory.add(bouclier)
        inventory.add(blague)
        inventory.add(lunettes)  
        
        interlocuteur = "None" ## Ne pas oublier d'actualiser le nom de l'interlocuteur à chaque changement
        lieu = "None"
        CAactif = False ## Set à False après chaqu actionChoice

label startBar:
    
    scene bg_bar with Dissolve (2.0)
    window show
    show goat with Dissolve(1.5)
    hide screen inventory_button

    $ lieu = "bar"
    
    $ CAactif = True
    $ actionChoice = "action_choice_"+ str(lieu) ##Copier ces lignes à chaque fois qu'on change de lieu, en actualisant le nom
    $ CAactif = False
    $ _return = renpy.call_screen(actionChoice)
    
    if _return == "boire":
        narration "Tu bois un verre."
        narration "C'est de l'eau."
        narration "L'effet escompté n'est pas au rendez-vous..."
        jump startBar
        
    elif _return == "sortir":
        narration "Tu essaies de sortir"
        narration "Malheureusement, les développeurs n'ont pas encore développé cette feature"
        
        menu:
            narration "t'es vraiment sur de vouloir sortir ?"
            
            "OUIIIII !":
                menu:
                    
                    narration "genre vraiment ?"
                   
                    "OUI.":
                        narration "bon, ok. ciao"
                        return
                   
                    "Non pas vraiment en fait, je voulais juste voir ce que ça faisait, mais maintenant j'hésite":
                        narration "sage décision"
                        jump startBar
           
            "Je suis pas sur du tout ! Je déteste faire des choix ça me stresse ! aaaaaah!":
                narration "Oui, tout-à-fait..."
                narration "On va faire comme si rien ne s'était passé ok ?"
                jump startBar
        
    elif _return == "goat2":
        $ interlocuteur = "goat_char"
        show screen datingSim(goat_char, 0.54, 0.45) 
        jump goat

label goat:
    c "Bêêêêêêêêê"
    
    menu :
        c "{cps=0}Bêêêêêêêêê{/cps}"
        "{color=#c4ae33}1. Absolument, tu as raison{/color}":
            y "Mais... OUI !"
            $ loveGauge(goat_char, 5)
            y "C'est TOUT A FAIT CA !"
            $ loveGauge(goat_char, 10)
            y "Mon dieu, toi et moi c'est comme si notre conscience ne faisait qu'un !"
            $ loveGauge(goat_char, 2)
            y "Tu sais... moi j'appelle ça le destin"
            y "On pense pareil, on fait les même réflexion, on fréquente la même taverne..."
            $ loveGauge(goat_char, 1)
            y "Tu crois aux âmes soeurs toi ?"
            jump goat_a2
        "{color=#c4ae33}2. Je ne suis pas daccord{/color}":
            y "Je peux pas te laisser dire ça désolé !"
            $ loveGauge(goat_char, -2)
            y "C'est complètement irrespectueux pour les buffles, ils ont pas une vie facile les buffles tu sais ?"
            $ loveGauge(goat_char, -3)
            y "Et puis c'est fondamentalement faux en plus"
            $ loveGauge(goat_char, -3)
            y "Non vraiment, ce que tu dis là, ça me déçoit de toi !"
            $ loveGauge(goat_char, -5)
            jump goat_b2
        "3. Je n'ai pas compris":
            y "Excusez-moi, je n'ai pas bien saisi le sens de ce que vous venez de dire"
            y "Vous pouvez détailler ?"
            y "..."
            y "non ?"
            jump goat_a2

label goat_a2:        
    c "Bêêêêêêêêê"
    menu :
        c "{cps=0}Bêêêêêêêêê{/cps}"
        
        "{color=#c4ae33}1. Ouais, moi non plus... {/color}":
            y "Ouais, moi non plus j'y crois pas..."
            $ loveGauge(goat_char, 5)
            y "Comme disait mon oncle pêcheur, les âmes soeurs ça vaut rien, mieux vaut un bon âme-çon"
            $ loveGauge(goat_char, -3)
            y "Je sais pas pourquoi ça le faisait toujours rire de dire ça..."
            $ loveGauge(goat_char, 10)
            jump goat_a3
            
        "{color=#c4ae33}2. Tu devrais y croire tu sais !{/color}":
            y "Tu devrais y croire aux âmes soeurs, tu sais !"
            y "Certaines choses ne peuvent pas être simplement le fruit du hasard !"
            y "Les étoiles dans le ciel, le chant des oiseaux, notre rencontre..."
            $ loveGauge(goat_char, 3)
            y "C'était forcément écrit !"
            $ loveGauge(goat_char, 15)
            jump goat_a3
        
        "{color=#c4ae33}3. Tu t'en fiches en fait ?{/color}":
            y "Tu t'en fiches en fait ?"
            y "Tu peux le dire clairement hein, pas besoin d'être méprisante !"
            $ loveGauge(goat_char, -5)
            y "C'est blessant tu sais ?"
            y "Parfois... J'ai l'impression que t'écoutes pas vraiment ce que je dis..."
            $ loveGauge(goat_char, -2)
            jump goat_a3
            
label goat_a3:
    c "Bêêêêêêêêê"
    menu :
        c "{cps=0}Bêêêêêêêêê{/cps}"
        
        "{color=#c4ae33}1. Sinon, tu sais que tu as de beaux yeux ? {/color}":
            y "Sinon, on t'as déjà dit que t'avais de beaux yeux ?"
            $ loveGauge(goat_char, 5)
            y "Je suis sérieux, l'éclat de tes yeux illumine les tréfonds de mon âme"
            $ loveGauge(goat_char, 15)
            jump goat_a4
        "1. T'as raison, ça n'a pas d'importance, désolé":
            y "T'as raison, ça n'a aucune importance, désolé..."
            $ loveGauge(goat_char, 2)
            y "C'est ma faute j'ai  tendance à divaguer et à changer de sujet"
            y "J'ai toujours eu du mal à suivre le fil d'une discussion"
            y "C'est assez handicapant au quotidien tu sais ?"
            y "T'as jamais eu cette impression que tout n'était qu'illusion ?"
            $ loveGauge(goat_char, 6)
            y "Que tes choix, tes interactions avec les autres, tout ça n'avait aucune importance ?"
            $ loveGauge(goat_char, 1)
            y "Que quoi que tu fasses, la fin sera la même ?"
            y "Enfin... Voilà que je recommence... Revenons à nos moutons"
            c "Bêêêêêêê !"
            $ loveGauge(goat_char, -5)
            y "Oups pardon je voulais pas te vexer !"
            y "Je suis absolument confus..."
            $ loveGauge(goat_char, 3)
            jump goat_a3
            
label goat_a4:
    c "Bêêêêêêêêê"
    menu :
        c "{cps=0}Bêêêêêêêêê{/cps}"
        
        "{color=#c4ae33}1. Marions-nous ! {/color}":
            y "Tu es la perfection incarnée"
            $ loveGauge(goat_char, 20)
            y "Et je suis pas mal non plus"
            y "On est fait l'un pour l'autre, marions-nous !"
            c "Bêêêêêêêêêêê !"
            jump mariage
        "{color=#c4ae33}2. Viens chez moi {/color}":
            y "Tu sais... chez moi, j'ai un hydromel que mon cousin fait lui-même"
            $ loveGauge(goat_char,3)
            y "Il a un goût fabuleux !"
            $ loveGauge(goat_char,6)
            y "Légèrement fruité, avec un arôme de crustacé qui relêve le tout"
            y "On peut peut-être en boire ensemble... ?"
            $ loveGauge(goat_char,11)
            c "Bêêêêêêêêêêê !"
            jump mariage

label goat_b2:
    y "Tu devrais faire attention à ce que tu dis tu sais"
    $ loveGauge(goat_char, -4)
    y "Moi, c'est bon, je t'aime bien donc ça va"
    $ loveGauge(goat_char, 2)
    y "Mais si tu dis ça à la mauvais personne, tu risque de la vexer"
    $ loveGauge(goat_char, -1)
    y "Imagine, si le père de la personne en question est un buffle !"
    y "C'est l'accident diplomatique assuré !"
    c "Bêêêêêêêêêêêêêêê"
    y "Voilà, je préfère ça !"
    c "Bêêêêêêêêêêêêêêê"
    y "Mais... OUI !"
    $ loveGauge(goat_char, 5)
    y "C'est TOUT A FAIT CA !"
    $ loveGauge(goat_char, 10)
    y "Mon dieu, toi et moi on est pareil en fait!"
    $ loveGauge(goat_char, 2)
    y "Désolé de m'être énervé tout à l'heure"
    y "Je pensais juste pas rencontrer quelqu'un comme toi ici"
    y "Tu sais... moi j'appelle ça le destin"
    y "On pense pareil, on fait les même réflexion, on fréquente la même taverne..."
    $ loveGauge(goat_char, 1)
    y "Tu crois aux âmes soeurs toi ?"
    jump goat_a2
label mariage:
    y "Comment ? Tu me trouves ennuyant ?"
    "{i}*Si seulement j'avais une histoire drôle à lui raconter...*{/i}"
    hide screen datingSim
    show screen inventory_screen(obj = "blague")
    narration "{w=1.5}Gaufrid sort une blague de son sac"
    jump useBlagueSuccess