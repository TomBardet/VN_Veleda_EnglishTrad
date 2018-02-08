#####################################################
# Ici figurent les scènes se déroulant aux étables. #
#####################################################
init:
    define buf = Character("Buffles : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    $  _testCrossfitTalk = 0
    $ _etableDone = 0
    $  _testEtable = 0
    $  _testRomainsTalk = 0
label etable_fromPlace:
            
    $ renpy.music.play("music/MUSIC_Etable_Normale.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("music/MUSIC_Etable_Panique.ogg", channel = "music2", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Etable_Normal_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    $ renpy.music.set_volume(0.4, delay=0, channel='music1')
    $ renpy.music.set_volume(0, delay=0, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0, channel='ambiance')
    
    scene bg_etables with Dissolve(1.5):
        zoom 0.70
    jump etables_PeurDesBufflesPart1
label etables_PeurDesBufflesPart1:
    $ _window_during_transitions = False
    scene bg_etables:
        zoom 0.70
    show char_crossfit inquiet right at notSpeakingAnim(0.7, 0.77, 0.8, 0.27)
    #$ _testTrompette = 1
    if _testTrompette == 1:
        if _testCrossfitTalk == 1:
            $ _testEtable = 1
    window show
    if _testEtable == 1:
        $ _return = renpy.call_screen("action_choice_EtableTrumpet")
        if _return == "trompette":
            jump etables_PeurDesBufflesPart2
        elif _return == "buffles":
            buf "Meuuuuuuuh !"
            y "À vos souhaits !"
            jump etables_PeurDesBufflesPart1
        elif _return == "crossfit":
            scene bg_etables:
                zoom 0.7
                linear 0.5 zoom 0.75 xpos -0.1
            show char_crossfit inquiet right:
                xalign 0.5 yalign 0.8 zoom 0.27
                xpos 0.7 ypos 0.77
                linear 0.5 zoom 0.28 xpos 0.65 ypos 0.76
            pause 0.5
            if _testCrossfitTalk == 0:
                jump etables_PeurDesBufflesPart1bis
            else:
                jump etables_PeurDesBufflesPart1boucle
        elif _return == "sortir":
            y "Retournons au village..."
            jump PlaceDuVillageDefault

    else:
        $ _return = renpy.call_screen("action_choice_Etable")
        if _return == "buffles":
            play sound "sfx/SFX_Buffle_Dialogue.ogg"
            buf "Meuuuuuuuh !"
            y "A vos souhaits"
            jump etables_PeurDesBufflesPart1
        elif _return == "crossfit":
            scene bg_etables:
                zoom 0.7
                linear 0.5 zoom 0.75 xpos -0.1
            show char_crossfit inquiet right:
                xalign 0.5 yalign 0.8 zoom 0.27
                xpos 0.7 ypos 0.77
                linear 0.5 zoom 0.28 xpos 0.65 ypos 0.76
            pause 0.5
            if _testCrossfitTalk == 0:
                jump etables_PeurDesBufflesPart1bis
            else:
                jump etables_PeurDesBufflesPart1boucle
        elif _return == "sortir":
            y "Retournons au village..."
            jump PlaceDuVillageDefault

# -----------------------------------------#

label etables_PeurDesBufflesPart1bis:
    
    show screen datingSim(cross_char, 0.45, .27)
    play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
    y "Bonjour ! Alors, ces buffles ?"
    show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    cross "..."
    show char_crossfit inquiet right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)

    show char_crossfit inquiet right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    y "... ?"
    show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    cross "..."
    show char_crossfit inquiet right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    menu:
        cross "{cps=0}...{/cps}"
        "Ca a pas l'air d'aller fort, dites moi !":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
            y "Ça a pas l'air d'aller fort, dites moi !"
            $ loveGauge(cross_char, -4, 0.44, 0.27)
            show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_01.ogg"
            cross "Ils...ils sont toujours là !"
        "Satisfait de vos buffles ?" if Acte1_Tour_CoupableJugement=="Brutalmund":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "Alors, satisfait de vos buffles ?"
            $ loveGauge(cross_char, -4, 0.44, 0.27)
            show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_01.ogg"
            cross "Ils...Ils sont toujours là !"
        "Vous avez livrés vos buffles à Brutalmund ?" if Acte1_Tour_CoupableJugement=="Crossfit":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "... Du coup, vous avez livré vos buffles à Brutalmund ?"
            $ loveGauge(cross_char, -4, 0.44, 0.27)
            show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_01.ogg"
            cross "Ils...Ils sont toujours là !"
        "Vous étiez plus bavard avec la prophétesse...":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_01.ogg"
            y "Ben dis donc, vous êtiez plus bavard avec la prophétesse..."
            $ loveGauge(cross_char, -4, 0.44, 0.27)
            show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_01.ogg"
            cross "Ca n'a rien à voir ! C'est juste que..."
            cross "Ils...Ils sont toujours là !"
    show char_crossfit inquiet right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
    y "Je vous demande pardon ?"
    $ loveGauge(cross_char, -6, 0.44, 0.27)
    show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_03.ogg"
    cross "Les buffles, crétin ! Ils sont toujours là !"
    $ loveGauge(cross_char, -4, 0.44, 0.27)
    show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    cross "Ça fait 12 heures que la porte est ouverte, et ces imbéciles de bovins ne bougent pas d'un poil !"
    play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
    y "Attendez... quoi ?"
    show char_crossfit pleurs right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_inquiet_02.ogg"
    cross "Chuuuuuuuuuut ! Ils vont vous entendre !"
    show char_crossfit pleurs right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
    y "Mais... vous avez peur des buffles ?"
    $ loveGauge(cross_char, -20, 0.44, 0.27)
    show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Colere_03.ogg"
    cross "Répète ça et je t'écrase !"
    show char_crossfit inquiet right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/SFX_Buffle_Dialogue.ogg"
    buf "Meuuuuuuuuuuuuuuuh !"
    hide screen datingSim
    show char_crossfit pleurs:
        zoom 0.28 ypos 0.84
        linear 0.4 xpos 0.79 rotate 15 ypos 0.95
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Pleurs_01.ogg"
    cross "Aaaaaaah !"
    show char_crossfit pleurs:
        zoom 0.28 ypos 0.95 xpos 0.79
        linear 0.8 rotate 0 ypos 0.84
    pause 1.2
    show char_crossfit inquiet right at speakingAnim(0.79, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Colere_02.ogg"
    cross "..."
    cross "Bon, d'accord, je trouve les buffles absolument terrifiants. Heureux ?!"
    show char_crossfit inquiet right at notSpeakingAnim(0.79, 0.84, 0.82, 0.28)
    show char_crossfit inquiet right:
        xalign 0.5 yalign 0.8
        zoom 0.28 xpos 0.79 ypos 0.84
        parallel:
            linear 1.5 xpos -0.5 ypos 0.86
        parallel:
            linear 0.5 rotate -16 
    pause 1.6
    nar "{i}Il y a forcèment quelquechose à faire pour aider ce pauvre homme...{/i}"
    nar "{i}Et qui sait... ça pourrait peut-être t'aider dans ta quête...{/i}"
    scene bg_etables:
        zoom 0.75 xpos -0.1
        linear 0.5 zoom 0.7 xpos 0.0
    pause .5
    show char_crossfit inquiet right:
        xalign 0.5 yalign 0.8 zoom 0.28
        xpos 0.7 ypos 1.5
        linear 0.5 zoom 0.27 xpos 0.7 ypos 0.77
    pause .5
    $ _testCrossfitTalk = 1
    jump etables_PeurDesBufflesPart1
    
    
# -----------------------------------------#

label etables_PeurDesBufflesPart1boucle:
    show screen datingSim(cross_char, 0.45, .27)
    play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
    y "Alors, tout baigne ?"
    show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_01.ogg"
    cross "Les... les buffles. Ils me regardent..."
    show char_crossfit inquiet right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    y "Je vais vous laisser, hein ?"
    hide screen datingSim
    scene bg_etables:
        zoom 0.75 xpos -0.1
        linear 0.5 zoom 0.7 xpos 0.0
    show char_crossfit inquiet right:
        xalign 0.5 yalign 0.8 zoom 0.28
        xpos 0.65 ypos 0.76
        linear 0.5 zoom 0.27 xpos 0.7 ypos 0.77
    pause 0.5
    jump etables_PeurDesBufflesPart1
    
# -----------------------------------------#    
label etables_PeurDesBufflesPart2:
    scene bg_etables:
        zoom 0.7 
        linear 1.0 zoom 0.85 xpos -0.07 ypos -0.02
    show char_crossfit inquiet right:
        xalign 0.5 yalign 0.8 zoom 0.27
        xpos 0.7 ypos 0.77
        linear 0.8 xpos 1.2 
    pause 1.0
    
    $ renpy.music.set_volume(0.3, delay=1, channel='music1')
    $ renpy.music.set_volume(0, delay=0, channel='music2')
    $ renpy.music.set_volume(0.3, delay=1, channel='ambiance')
    
    show char_ernust inquiet left:
        xalign 0.5 yalign 0.8
        xpos 0.65 zoom 0.65 ypos 1.6
        linear 0.4 ypos 0.94
    pause 1.0
    

    show char_ernust inquiet left at speakingAnim(0.65, 1.02, 1.0, 0.65)
    play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_04.ogg"
    e "Euh... Gaufrid, t'es sur que c'est une bonne idée ?"
    show char_ernust inquiet left at notSpeakingAnim(0.65, 1.02, 1.0, 0.65)
    play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
    y "Il faut bien utiliser cette trompette quelque part, non ?"
    nar "Je ne ferai pas ça, à ta place..."
    play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"
    y "Trop tard."
    scene black with Dissolve (1.0)
    show screen inventory_screen(obj = "trompette")
    pause 3.0
    
    $ renpy.music.play("ambiances/AMB_Lieu_Etable_Panic_01.ogg", channel = "ambiance", loop = True, fadein = 0.5)
    
    $ renpy.music.set_volume(0.4, delay=0.5, channel='music1')
    $ renpy.music.set_volume(0.4, delay=0.5, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0.5, channel='ambiance')
    
    play sound "sfx/SFX_Trumpet_01.ogg"
    
    pause 1.0
    
    play sound "sfx/SFX_Buffle_Peur.ogg"
    hide screen inventory_screen
    window hide
    scene bg_buffles with hpunch:
        zoom 0.7
    pause 1.5
    window show
    show char_crossfit pleursG right:
        zoom 0.3 xalign 0.5 yalign 0.8
        xpos 1.2 ypos 0.84
        linear 1.8 xpos -0.5 rotate -15
    
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Pleurs_01.ogg"
    cross "Au secooouuuurs ! Les buffles m'attaquent !" 
    #scene black with Dissolve(1.0)
    outline "Et c'est ainsi que le brave Crossfitrichernvald prit la fuite devant les buffles fonçant sur lui..."
    scene bg_etables2 with Dissolve(1.0):
        zoom 0.7
    show char_ernust normal right:
        xalign 0.5 yalign 0.8
        xpos 0.65 zoom 0.65 ypos 1.6
        linear 0.3 ypos 0.94
    pause 0.3
    show char_ernust normal right at speakingAnim(0.65, 1.02, 1.0, 0.65)
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
    e "Ah ben tiens, il a fait tomber ses lunettes en courant."
    
    show char_ernust normal right at notSpeakingAnim(0.65, 1.02, 1.0, 0.65)
    
    $ inventory.add(lunettes)
    $ _testLunettes = 1
    show img_lunettes at center:
        xalign 0.7 yalign 0.9 zoom 0.3
        linear 0.5 yalign 0.7 zoom 0.4
        easein 0.5 zoom 0.55
        easeout 0.5 zoom 0.4
        pause 0.5
        parallel :
            linear 0.8 yalign 0.05 xalign 0.95 zoom 0.3
        parallel :
            linear 0.9 alpha 0
    pause 0.5
    play sound "sfx/SFX_UI_Lunettes_01.ogg"
    show img_bag:
        xpos 1.0 yalign 0.05 zoom 1.0
        linear 0.5 xpos 0.87 yalign 0.05
        pause 2.3
        easein 0.3 zoom 1.1
        easeout 0.3 zoom 1.0 
        pause 0.5
        linear 0.3 xpos 1.0
    pause 2.0
    play sound "sfx/SFX_UI_Inventory_Bag_01.ogg"
    pause 0.5
    show char_ernust normal right at speakingAnim(0.65, 1.02, 1.0, 0.65)
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_07.ogg"
    e "On devrais ptêtre les lui rendre ?"
    show char_ernust normal right at notSpeakingAnim(0.65, 1.02, 1.0, 0.65)
    $ _etableDone = 1
    $ renpy.music.play("ambiances/AMB_Lieu_Etable_Panic_01.ogg", channel = "ambiance", loop = True, fadein = 0.5)
    
    stop music1 fadeout 1.5
    stop music2 fadeout 1.5
    stop ambiance fadeout 0.5
    
    pause 0.5
    
    jump PlaceDuVillageDefault
    
# -----------------------------------------#
