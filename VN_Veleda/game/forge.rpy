####################################################
# Ici figurent les scènes se déroulant à la Forge. #
####################################################

label forge_BrutalmundEtBeaudrik:
    
    stop music1 fadeout 1
    stop ambiance fadeout 0.5
    
    $ renpy.music.play("ambiances/AMB_Lieu_Forge_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music1')
    $ renpy.music.set_volume(0, delay=0.4, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='ambiance')

    $ interlocuteur = "brut_char"
    $ interlocuteur = "beau_char"

    if Acte2_Forge_FirstVisit == 0:
        $ forge_cannotpay_check = 0 # Check si on a déjà dit à Brutalmund qu'on ne peut pas payer
        jump forge_Intro
    if Acte2_Forge_FirstVisit == 1:
        jump forge_Brutalmund_Tampon_HUB
        
# ----------------------------------------- #

label forge_Brutalmund_Tampon_HUB:

    scene bg_forge with Dissolve(1.5)
    pause 0.5
    $ renpy.music.play("music/MUSIC_Forge.ogg", channel = "music1", loop = True, fadein = 1)
    show char_brutal normal :
        zoom 0.35 xpos -0.5 ypos 0.05
        linear 0.7 xpos 0.2
    brut "Gaufrid !"
    show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_02.ogg"
    brut "Alors, ça te tente un {b}Bouclier Original de Capitaine Germanie™{/b} tout neuf ?"
    show screen datingSim(brut_char, 0.57, 0.15)
    jump forge_Brutalmund_06_Hub

# -----------------------------------------#

label forge_Intro:
    
    scene bg_forge with Dissolve(1.5)
    #play sound "sfx/Voices/Player/Char_Player_Hesitation_01.ogg"
    #y "Euh... il y a quelqu'un ?"
    
    jump forge_Beaudrik_01

# -----------------------------------------#

label forge_Beaudrik_01:
    $ _window_during_transitions = False
    $ Acte2_Forge_FirstVisit = 1
    show char_beaudrik normal left :
        xalign 0.5 yalign 0.8
        zoom 0.8 xpos 1.5 ypos 0.78
        linear 0.4 xpos 0.8

jump forge_Beaudrik_02
    
# -----------------------------------------#

label forge_Beaudrik_02:
    
    pause 0.5
    show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Normal_02.ogg"
    bg "Tiens ! C’est le p’tit Gaufrid !"
    show screen datingSim(beau_char, 0.75, 0.10)
    
    $ renpy.music.play("music/MUSIC_Forge.ogg", channel = "music1", loop = True, fadein = 1)
    
    #bg "T’sais, justement je pensais à toi bonhomme."
    #show char_beaudrik normal left at notSpeakingAnim(0.8, 0.9, 0.88, 0.2)
    #play sound "sfx/Voices/Player/Char_Player_Heureux_01.ogg"
    #y "Ah, merci Beaudrik ! Je suis flatté."
    
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    $ loveGauge(beau_char, -5, 0.85, 0.10)
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_02.ogg"
    bg "J’ai entendu des rumeurs comme quoi tu voudrais épouser Ingrid !"
    show char_beaudrik drague right at speakingAnim(0.7, 0.9, 0.88, 0.88)
        #zoom 0.22 xpos 0.4 ypos 0.09
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Drague_04.ogg"
    bg "C’est tellement n’importe quoi ! Ahahah."
    show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.8)
        #zoom 0.2 xpos 0.6 ypos 0.09

jump forge_Beaudrik_03_EpouserIngrid
    
#------------------------------------------#

label forge_Beaudrik_03_EpouserIngrid:
    
    #show char_beaudrik normal left at notSpeakingAnim(0.8, 0.9, 0.88, 0.2)
    #menu:
    #    bg "On entend vraiment des trucs drôles à la taverne, quand les gens se bourrent la gueule."
    #    "Ouais… très drôles" :
    #        y "Euh… heureusement que c’est juste des rumeurs."
    #        show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    #        bg "Ouais, grave ! Ça aurait été dommage que je te casse la gueule."
    #        jump forge_Beaudrik_04
    #    "Ça ne te regarde pas" :
    #        y "Euh… oh ! Ce qu’il se passe entre Ingrid et moi, ça ne te regarde pas !"
    #        show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    #        bg "Ahahahah !"
    #        bg "Vraiment, tu me tues mon pote. T’as raison, faut jouer le jeu."
    #        bg "En tout cas, c’est bien que ce ne soit qu’une rumeur."
    #        bg "Ça aurait été dommage que je te casse la gueule."
    #        jump forge_Beaudrik_04
    #    "On va se marier pour de vrai !" :
    #        y "Euh… oui, mais tu sais, Ingrid et moi on va se marier vraiment !"
    #        show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    #        bg "Ahahahah !"
    #        bg "Vraiment, tu me tues mon pote. T’as raison, faut jouer le jeu."
    #        bg "En tout cas, c’est bien que ce ne soit qu’une rumeur."
    #        bg "Ça aurait été dommage que je te casse la gueule."
    #        jump forge_Beaudrik_04
            
    jump forge_Beaudrik_04
        
#------------------------------------------#

label forge_Beaudrik_04:

    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    bg "Tu sais, c’est moi qui vais me marier avec Ingrid. J’ai une dot et tout."
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    bg "J'ai envie de me poser. Tu sais, avoir quelqu’un qui me fasse des câlins et la vaisselle."
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
    show char_brutal colere:
        xalign 0.5 yalign 0.8
        xpos -0.55 ypos 1.5 zoom 0.2 rotate 45
        linear 0.7 xpos 0.045 ypos 0.7
    pause 1
    brut "{i}Hé, la feignasse ! Beaudrik ! Viens ici !{/i}"    
    show char_beaudrik choque left at speakingAnim(0.8, 0.9, 0.88, 0.8)

    show char_brutal colere:
        xalign 0.5 yalign 0.8
        xpos 0.1 ypos 0.6 zoom 0.2 rotate 45
        linear 2.5 xpos -1.0 ypos 1.5

    $ renpy.pause(0.5, hard = True)
    
    show char_beaudrik choque left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    hide char_brutal
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Insult_02.ogg"
    bg "Oh non, Papa m’appelle ! Je me casse !"
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    bg "De toute façon, je dois aller régler un truc avec Josiane... mon autre fiancée."

jump forge_Beaudrik_06_leaving

#------------------------------------------#

label forge_Beaudrik_05_Josiane:
    
    show char_beaudrik normal left at notSpeakingAnim(0.8, 0.9, 0.88, 0.8)
    menu:
        bg "{cps=0}De toute façon, je dois aller régler un truc avec Josiane... mon autre fiancée.{/cps}"
        "Deux fiancées ? C’est abusé !" :
            play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
            y "Attends, moi je me trimballe Ernust, et toi tu drague des filles à droite et à gauche ?"
            show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
            $ loveGauge(beau_char, -5, 0.85, 0.10)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_02.ogg"
            bg "Ouais, je sais, c’est compliqué."
        "Tu ferais ça à Ingrid ?" :
            play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
            y "Deux copines, c’est un peu abusé et pas très gentil quand même."
            y "Tu penses pas que ça briserait le cœur à Ingrid ?"
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_02.ogg"
            show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
            $ loveGauge(beau_char, -5, 0.85, 0.10)
            bg "Euh, je sais, c’est compliqué."
        "Brutalmund a l’air vénère" :
            y "Et ton père ? Il a pas l’air d’être content."
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_06.ogg"
            bg "Oui, il s’est mis en tête que je dois travailler pour gagner ma vie."
            show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
            bg "Mais là j’ai des questions de meufs à régler."

jump forge_Beaudrik_06_leaving

#------------------------------------------#

label forge_Beaudrik_06_leaving:
    
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    bg "Heureusement que toi tu n’as pas ce genre de problèmes, Gaufrid ! Je t’envie mon pote."
    show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    bg "Bon, je me casse, avant que Papa n'arrive."
    show char_beaudrik drague right at speakingAnim(0.7, 0.9, 0.88, 0.88)
        #zoom 0.23 xpos 0.4 ypos 0.09
    hide screen datingSim
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Normal_04.ogg"
    bg "À plus !"
    show char_beaudrik drague right :
        zoom 0.88 xpos 0.7 ypos 0.9
        linear 1.0 xpos 1.5
    pause 1
    hide char_beaudrik drague right
    pause 1.0
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
    brut "Beaudrik !"
    
    jump forge_Brutalmund_01
    
#------------------------------------------#

label forge_Brutalmund_01:
    
    show char_brutal colere :
        xalign 0.5 yalign 0.8
        zoom 0.35 xpos -0.5 ypos 0.77
        linear 0.7 xpos 0.52
    pause 0.9
    show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
    pause 0.3
    show char_brutal colere at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    brut "..."
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
    brut "Tiens ! J'cherche un guignol et j’en trouve un autre !"
    show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
    show screen datingSim(brut_char, 0.57, 0.15)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_02.ogg"
    brut "Ahahahah !"
    show char_brutal normal
    brut "T'as pas vu mon fils ?"

    jump forge_Brutalmund_02
    
#------------------------------------------#

label forge_Brutalmund_02:
    
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    menu:
        brut "{cps=0}T’as pas vu mon fils ?{/cps}"
        "Pas vraiment, non" :
            y "Je l’ai pas vu, non. Pourquoi ?"
            play sound "sfx/Voices/Player/Char_Player_Non_01.ogg"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            if Acte1_Tour_CoupableJugement == "Crossfit":
                show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
                play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
                brut "Il devait surveiller les {b}boucliers{/b} pendant que j'vais chercher les buffles !"
                show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
                brut "Il mérite une torgnole, j'te dis !"
            if Acte1_Tour_CoupableJugement == "Brutalmund":
                show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
                $ loveGauge(brut_char, -5, 0.57, 0.15)
                play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
                brut "Parce que grâce à ta prophétesse, là, on n’a plus un seul buffle à se mettre sous la dent !"
                show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
                brut "Et tous ces {b}boucliers{/b} ne vont pas se vendre tout seuls !"
            #show char_brutal colere at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            #play sound "sfx/Voices/Player/Char_Player_Sarcastic_03.ogg"
            #y "Il faudrait que t'ailles le chercher, non ?"
            #show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            #play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_04.ogg"
            #brut "Et te laisser là tout seul avec mes précieux boucliers ?"
            #show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            #play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
            #brut "Hors de question !"
        "Il est à la taverne" :
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_03.ogg"
            y "Il allait à la taverne, t'as encore le temps de l’attraper."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_04.ogg"
            brut "Et te laisser là tout seul avec mes précieux {b}boucliers{/b} ?"
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
            brut "Hors de question !"
            #if Acte1_Tour_CoupableJugement == "Crossfit":
                #jump forge_Brutalmund_03
            #if Acte1_Tour_CoupableJugement == "Brutalmund":
                #$ loveGauge(brut_char, -5, 0.57, 0.15)
                #play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
                #brut "Tu m’as déjà dévalisé une fois avec cette histoire de buffles, tu ne m’auras pas une deuxième fois ! Ha !"

jump forge_Brutalmund_03

#------------------------------------------#

label forge_Brutalmund_03:
    
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere2_02.ogg"
    brut "De toute façon, ça sert à rien. Beaudrik, c’est vraiment une cause perdue."
    show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
    brut "J’aurais dû l'jeter d’une falaise quand il est né !"
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
    brut "Le troisième téton, c’était pas bon signe."
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    menu:
        brut "{cps=0}Le troisième téton, c’était pas bon signe.{/cps}"
        "Trois tétons, c'est pas si grave" :
            play sound "sfx/Voices/Player/Char_Player_Non_05.ogg"
            y "C’est pas de sa faute, s’il est né comme ça."
            y "Les enfants comme lui ont besoin d’encore plus d’amour que les gens normaux."
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
            brut "C’est c'que disait sa mère  aussi ! Et ça l’a ruinée ! Ruinée, j'te dis !"
        #"En quoi c’est mauvais signe ?" :
            #play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            #y "Ah bon ? Trois tétons c’est mauvais signe ?"
            #show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            #$ loveGauge(brut_char, -5, 0.57, 0.152)
            #play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
            #brut "Mais enfin, Veléda ne t’a rien appris ?"
            #show char_brutal colere at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            #y "Euh, nous on fait plutôt des prophéties. Les tétons en rab c’est pas trop notre truc."
            #show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            #play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
            #brut "Et alors je t’explique..."
            #show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            #play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
            #brut "Le troisième téton, c’est signe de faiblesse !"
        "Les gens comme lui, c’est des monstres !" :
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_03.ogg"
            y "C’est peut-être pas trop tard, je vous accompagne à la falaise la plus proche ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, +5, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere2_04.ogg"
            brut "C'est trop tard, fallait l'faire avant."
            brut "J’ai essayé d'le lâcher de l’autre côté de la Lippe, mais il revient toujours."
        "D'autres secrets bizarres sur lui ?":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_03.ogg"
            y "Tu sais si ton fils a d’autres secrets gênants ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
            brut "Ha ! Tu veux connaitre son secret ?"
            
    jump forge_Brutalmund_04

#------------------------------------------#

label forge_Brutalmund_04:
    
    show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_04.ogg"
    brut "On l’a trop gâté, c'te Breaudrik !"
    brut "Il dort avec un nounours parce qu'il a peur du noir !"
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
    brut "Enfin bref...."
    show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_03.ogg"
    brut "J’imagine que t'as besoin d’un {b}Bouclier Original de Capitaine Germanie™{/b}, hein ?"
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    jump forge_Brutalmund_04_choice
    
#-------------------------------------------#

label forge_Brutalmund_04_choice:
    
    menu:
        brut "{cps=0}J’imagine que t'as besoin d’un {b}Bouclier Original de Capitaine Germanie™{/b}, hein ?{/cps}"
        "{color=#FFFFFF}C'est possible un bouclier normal ?{/color}":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
            y "Vous avez des sous-marques ? Je fais des economies."
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            if Forge_LeaderPrice_check == 0:  
                $ loveGauge(brut_char, -5, 0.57, 0.15)
                $ Forge_LeaderPrice_check = 1
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
            brut "Tu t'crois où, Gaufrid. Chez Leader Price ?"
            show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            jump forge_Brutalmund_04_choice
        "J'peux en prendre un en essai avant ?":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_03.ogg"
            y "Ça m’intéresse, mais comment je sais s’ils sont bien ? Je peux en essayer un ?"
            show char_brutal surpris at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, -5, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
            brut "Ah, là, tu m'brise le cœur, mon p’tit Gaufrid !"
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_02.ogg"
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "Mes {b}Boucliers Originaux de Capitaine Germanie™{/b}, c’est d'la balle !"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "Les essais sont interdits."
            jump forge_Brutalmund_04_01_Branche_EssaiRoutier
        "Je ne peux pas payer...":
            jump forge_Brutalmund_05_CannotPay
            
    jump forge_Brutalmund_05_CannotPay

#-----------------------------------------#

label forge_Brutalmund_04_01_Branche_EssaiRoutier:
    
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    menu:
        brut "{cps=0}Je te promets.{/cps}"
        "{color=#FFFFFF}Ça sent l'arnaque...{/color}":
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            y "Tu serais pas en train de m'arnaquer ?"
            show char_brutal surpris at speakingAnim(0.52, 0.93, 0.91, 0.35)
            if Forge_reply_arnaque == 0:
                $ loveGauge(brut_char, -5, 0.57, 0.15)
                $ Forge_reply_arnaque = 1
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
            brut "Qui ?! Moi ?!"
            show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_01.ogg"
            brut "Pourquoi perdre ton temps à les regarder, mon p’tit Gaufrid, quand tu peux directement les acheter ?"
            jump forge_Brutalmund_04_01_Branche_EssaiRoutier
        "Je vais l'acheter à Crossfitrichernvald, alors.":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_01.ogg"
            y "Je vais peut être me fournir chez Crossfitrichernvald alors !"
            show char_brutal surpris at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
            brut "Quoi ? Ce sale Batave m'accuse de vol, et en plus, il me fait d'la concurrence ?!"
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
            brut "Ha ! Là, j’en peux plus mon p’tit Gaufrid. J’en peux plus j'te dis !"
            brut "J'vais lui dire ses quatre vérités."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            hide screen datingSim
            brut "Attends-moi ici, j'reviens dans une minute."
            show char_brutal normal :
                zoom 0.35 xpos 0.5 ypos 0.9
                linear 3.0 xpos -1.5
            pause 0.7
            show char_brutal colere:
                xalign 0.5 yalign 0.8
                xpos -0.5 ypos 2.0 zoom 0.35 rotate 30
                linear 0.7 xpos 0.1 ypos 1.1
            pause 0.5
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
            brut "Et ne touche à rien !"
            show char_brutal colere:
                xalign 0.5 yalign 0.8
                xpos 0.1 ypos 1.1 zoom 0.35 rotate 30
                linear 1.0 xpos -1.0 ypos 2.0
            pause 1.5
            hide char_brutal
            jump forge_Brutalmund_07_Bouclier
            
        "En tout cas je ne peux pas payer…":
            jump forge_Brutalmund_05_CannotPay
        

#------------------------------------------#

label forge_Brutalmund_05_CannotPay:

    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Player/Char_Player_Hesitation_02.ogg"
    y "J'ai pas un rond."
    show char_brutal surpris at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
    brut "Rien du tout ? Allez mon p’tit Gaufrid, ça fait deux mois que je ne vends rien, fais un effort !"

    $ Acte2_Forge_FirstVisit = 1

jump forge_Brutalmund_06_Hub

#------------------------------------------#

label forge_Brutalmund_06_Hub:
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    
    menu:
        brut "{cps=0}Rien du tout ? Allez mon p’tit Gaufrid, ça fait deux mois que je ne vends rien, fais un effort !{/cps}"
        
        "{color=#FFFFFF}Tu veux quoi en échange ?{/color}":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "J'ai pas d'argent, mais on peut peut être faire du troc ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            if Acte1_Tour_CoupableJugement == "Brutalmund":
                play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_06.ogg"
                brut "Si tu trouves un moyen de me fournir un ou deux buffles… T'sais que j’ai perdu les miens…"
                show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
                y "Tu penses vraiment que j'ai des buffles en rab ?"
                show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
                brut "J’ai pas dit qu’il faut que ça soit tes buffles à toi, hein !"
                brut "Allez, mon p’tit Gaufrid ! T’es p'têtre un boulet, mais t’es débrouillard..."
            if Acte1_Tour_CoupableJugement == "Crossfit":
                show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
                play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_06.ogg"
                brut "Crossfit traîne des pieds pour m'amener mes buffles."
                brut "Si tu pouvais accélerer les choses... on pourra s'arranger."
                show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_03.ogg"
            brut "Amène-moi mes buffles et t’auras ton {b}Bouclier Original de Capitaine Germanie™{/b} !"
            jump forge_Brutalmund_06_Hub
        
        "Tes buffles sont en liberté..." if _testLunettes == 1:
            play sound "sfx/Voices/Player/Char_Player_Heureux_01.ogg"
            y "Si ça vous intéresse, j’ai récupéré vos buffles."
            show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, +10, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_01.ogg"
            brut "Ah, tu sers enfin à quelqu'chose mon p’tit Gaufrid !"
            #show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
            #y "Enfin, presque…"
            #show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            #brut "Euh ? Comment ça ?"
            #show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
            y "Enfin, je les ai libérés des étables... faut aller les chercher."
            show char_brutal heureux at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            pause 1.0
            show char_brutal surpris at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            pause 1.0
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, -15, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_04.ogg"
            brut "Mais tu le fais exprès, ou quoi ?"
            hide screen datingSim
            brut "Attends ici, j'vais les chercher !"
            show char_brutal normal :
                zoom 0.35 xpos 0.5 ypos 0.9
                linear 3.0 xpos -1.5
            pause 0.7
            show char_brutal colere:
                xalign 0.5 yalign 0.8
                xpos -0.5 ypos 2.0 zoom 0.35 rotate 30
                linear 0.7 xpos 0.1 ypos 1.1
            pause 0.5
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
            brut "Et ne touche à rien ! T'auras pas de bouclier avant que j'les ai trouvés !"
            show char_brutal colere:
                xalign 0.5 yalign 0.8
                xpos 0.1 ypos 1.1 zoom 0.35 rotate 30
                linear 1.0 xpos -1.0 ypos 2.0
            pause 1.5
            hide char_brutal
            jump forge_Brutalmund_07_Bouclier
            
        "Je reviens quand je peux te payer." if _testLunettes == 0:
            play sound "sfx/Voices/Player/Char_Player_Non_01.ogg"
            y "J'ai rien à te donner pour l'instant."
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            if forge_cannotpay_check == 0:
                $ loveGauge(brut_char, -5, 0.57, 0.15)
                $ forge_cannotpay_check = 1
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
            brut "Dégages, alors ! J’ai du travail."
            hide screen datingSim

            stop music1 fadeout 1.5
            stop ambiance fadeout 0.5

            jump PlaceDuVillageDefault

#---------------------------------------------------#

label forge_Brutalmund_07_Bouclier:

    stop music1 fadeout 1.5
    
    hide  char_brutal
    outline "Ainsi, Brutalmund quitta son poste." 
    outline "En profiter pour lui voler un {b}bouclier{/b} serait parfaitement déloyal !"
    play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
    y "T'as raison, c'est une super bonne idée !"
    $ inventory.add(bouclier)
    $ _testBouclier = 1
    show img_bouclier at center:
        xalign 0.7 yalign 0.9 zoom 0.3
        linear 0.5 yalign 0.7 zoom 0.7
        easein 0.5 zoom 0.45
        easeout 0.5 zoom 0.4
        pause 0.5
        parallel :
            linear 0.8 yalign 0.05 xalign 0.95 zoom 0.3
        parallel :
            linear 0.9 alpha 0
    
    show img_bag:
        xpos 1.0 yalign 0.05 zoom 1.0
        linear 0.5 xpos 0.87 yalign 0.05
        pause 2.3
        easein 0.3 zoom 1.1
        easeout 0.3 zoom 1.0 
        pause 0.5
        linear 0.3 xpos 1.0
        
    $renpy.pause(0.5, hard = True)
    
    play sound "sfx/SFX_UI_Bouclier_01.ogg"
    $renpy.pause(1.8, hard = True)
    play sound "sfx/SFX_UI_Inventory_Bag_01.ogg"
    $renpy.pause(0.2, hard = True)
    
    stop ambiance fadeout 0.5

    if _testGlaive == 1 & _testBouclier == 1:
        jump PlaceDuVillageAllObjects
    else:
        jump PlaceDuVillageDefault
    
#--------Backup Conditions et Variables-------------#

#    if _testBlague == 1:
#        menu:
#            "Retour Place du Village":
#                jump PlaceDuVillageDefault
#            "Donner la blague":
#                jump forge_BrutalMundBlaguePart2
#    else:
#        "Pas de blague..."
#        jump PlaceDuVillageDefault

# -----------------------------------------#

#label forge_BrutalMundBlaguePart2:
#    "Entrée forge_BrutalMundBlaguePart2"
#    
#    $ inventory.add(bouclier)
#    $ _testBouclier = 1
#    
#    "Bouclier récupéré"
#    
#    if _testGlaive == 1 & _testBouclier == 1:
#        jump PlaceDuVillageAllObjects
#    else:
#        jump PlaceDuVillageDefault
    
jump PlaceDuVillageDefault   