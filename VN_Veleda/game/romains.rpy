################################################################################
# Ici figurent les scènes se déroulant à l'aurée du village, chez les romains. #
################################################################################
init python:
    _testA = 0
    _testB = 0
label romains_PremiereRencontre:
    if Acte2_Romains_FirstVisit == 1:
        scene bg_romains with Dissolve(1.5):
                zoom 1.15 xpos -0.15
    else:
        scene bg_romains with Dissolve(1.5)
    jump romains_Part1

# -----------------------------------------#

label romains_Part1:
    
    stop music1 fadeout 1.0
    
    $ renpy.music.play("music/MUSIC_Tente_Romain.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Sentier_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    $ renpy.music.set_volume(0.4 , delay=0, channel='music1')
    $ renpy.music.set_volume(0, delay=0, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='ambiance')
    
    
    $ interlocuteur = "num_char"
    
    window hide
    if Acte2_Romains_FirstVisit == 1:
        scene bg_romains:
            zoom 1.15 xpos -0.15
        $ _return = renpy.call_screen("action_choice_Tente1")
        
        if _return == "tente":

            pause 0.6
            window show
            jump romains_Part5
        elif _return == "sortir":
            hide screen datingSim
            stop music1 fadeout 1.0
            jump PlaceDuVillageDefault
    
        jump romains_Part5
    else :
        scene bg_romains
        $ _return = renpy.call_screen("action_choice_Tente")
        
        if _return == "tente":
            scene bg_romains:
                linear 0.4 zoom 1.15 xpos -0.15
            pause 0.6
            window show
            y "On dirait qu'il y a personne..."
            jump romains_Part2
        elif _return == "sortir":
            hide screen datingSim
            stop music1 fadeout 1.0
            jump PlaceDuVillageDefault
            
            
                     
# -----------------------------------------#

label romains_Part2:
    
    show char_digitimus normal right :
        xalign 0.5 yalign 0.8 zoom 1
        xpos 1.2 ypos 0.78
        linear 1 xpos 0.5
    
    
    show char_numerimus normal:
        xalign 0.5 yalign 0.8 zoom 1
        xpos 1.3 ypos 0.82
        linear 0.7 xpos 0.2
    pause 4
   
    show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
    show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
    
   
    
    play sound "sfx/Voices/Num/Char_Num_Normal_03.ogg"
    num "{i}Ave{/i}, sauvage !"
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    play sound "sfx/Voices/Player/Char_Player_Hesitation_03.ogg"
    y "Euh...{i}Ave{/i} à vous... j'imagine ?"
    show screen datingSim(num_char, 0.28, 0.3)
    $ loveGauge(num_char, +10, 0.36, 0.28)
    y "On se connait ?"
    jump romains_Part3

        
# -----------------------------------------#

label romains_Part3:
    
    show char_numerimus heureux at speakingAnim(0.2, 0.82, 0.8, 1)
    show char_digitimus normal right at speakingAnim(0.5, 0.8, 0.815, 1)
    
    play sound "sfx/Voices/Num et Dig/Char_Num_Dig_Heureux_04.ogg"
    num "Haha ! T’as l’air d’un marrant, Germain. Moi c’est Numerimus et lui, là, c’est Digitimus ! C’est mon cousin, germain."
    dig "{i}Ave{/i}..."
    show char_digitimus normal at notSpeakingAnim(0.5, 0.8, 0.815, 1)
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
     
    play sound "sfx/Voices/Num/Char_Num_Normal_03.ogg"
    show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
    num "On est en permission, alors on visite un peu les alentours."
    num "Et on s'est dit : \"Tiens, pourquoi pas s'amuser de vos coutumes locales !\""
    num "Du coup, on est là."
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    jump romains_Part4

# -----------------------------------------#

label romains_Part4:
    $ Acte2_Romains_FirstVisit = 1

    play sound "sfx/Voices/Num et Dig/Char_Num_Dig_Normal_01.ogg"
    
    show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
    show char_digitimus normal right at speakingAnim(0.5, 0.8, 0.815, 1)
    dig "On s'ennuie un peu..."
    show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
    num "Ouais. On s'ennuie..."
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    menu :
        num "{cps=0}Ouais. On s'ennuie...{/cps}"
        "Je vous fais visiter ?" if _testGlaive == 0:
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Il y a de belles choses à voir dans le coin."
            y "Venez avec moi, j'vais vous faire visiter."
            jump romains_VisitePart1
            
        "J'ai une bonne blague pour vous !" if _testTrompette == 0:
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
            y "Tenez vous bien, on m'a donné une excellente blague !"
            show char_numerimus dubitatif at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
            jump romains_Blague

# -----------------------------------------#

label romains_Part5:
    $ Acte2_Romains_FirstVisit = 1
    show screen datingSim(num_char, 0.28, 0.3)
    
    show char_digitimus normal right :
        xalign 0.5 yalign 0.8 zoom 1
        xpos 1.2 ypos 0.78
        linear 1 xpos 0.5
    
    
    show char_numerimus normal:
        xalign 0.5 yalign 0.8 zoom 1
        xpos 1.3 ypos 0.82
        linear 0.7 xpos 0.2
    pause 1.2
    show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
    show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
    
    play sound "sfx/Voices/Num/Char_Num_Normal_02.ogg"
    num "On s'ennuie..."
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    menu :
        num "{cps=0}On s'ennuie...{/cps}"
        "Voilà, j'ai trouvé des lunettes !" if _testLunettes == 1:
            play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"
            y "C'est une longue histoire, mais j'ai trouvé des lunettes !"
            jump romains_VisitePart2
            
        "Je vous fais visiter ?" if _testGlaive == 0:
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Il y a des belles choses à voir dans le coin."
            y "Venez avec moi, j'vais vous faire visiter."
            jump romains_VisitePart1
            
        "J'ai une bonne blague pour vous !" if _testTrompette == 0:
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
            y "Ca tombe bien, on m'a donné une excellente blague hier soir !"
            show char_numerimus dubitatif at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
            jump romains_Blague
           
# -----------------------------------------#
                #VISITE
# -----------------------------------------#
label romains_VisitePart1:
    

    show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
    play sound "sfx/Voices/Num/Char_Num_Doute_03.ogg"
    num "Je vois pas à 2 mètres. Pour le folklore local, on repassera...  "
    num "Le génie qui me sert de porte-enseigne a oublié mes {b}lunettes{/b} à Rome."
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    
    if _testLunettes == 1:
        play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
        y "Vous avez de la chance j’en ai justement une paire sur moi."
        y "Si ça c'est pas un coup de bol !"
        show screen inventory_screen(obj = "lunettes")
        jump romains_VisitePart2
        
    else:
        menu :
            num "{cps=0}Le génie qui me sert de porte-enseigne a oublié mes {b}lunettes{/b} à Rome.{/cps}"
            "Ah mince...vous avez pas une paire de rechange ?":
                play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
                y "Vous avez pas une paire de rechange ?"
                
                show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
                
                play sound "sfx/Voices/Num/Char_Num_Doute_02.ogg"
                num "Non. On l'a oubliée aussi."
                num "Ca nous aiderait pas mal, si vous en trouviez une, Germain."
                
            "Retournez les chercher à Rome.":
                play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
                y "Vous n'avez qu'à retourner les chercher à Rome."
                y "Ca tombe bien, toutes les routes y mènent."
                play sound "sfx/Voices/Num/Char_Num_Normal_02.ogg"
                show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
                num "T'es un marrant toi..."
                $ loveGauge(num_char, -10, 0.36, 0.28)
        
        show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
        show char_digitimus normal right at speakingAnim(0.5, 0.8, 0.815, 1)
        dig "Dis nous si tu trouves des {b}lunettes{/b} !"
        show char_digitimus normal at notSpeakingAnim(0.5, 0.8, 0.815, 1)
        hide screen datingSim
     #   scene bg_romains:
      #      linear 0.4 zoom 1.0 xpos 0
        show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
        show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
        
        if _testTrompette == 0:
                jump romains_Part5
        else :
            show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1) :
                linear 1.5 xpos -1.0
            show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1) :
                linear 1.5 xpos -1.0
            pause 2.0
            jump romains_Part1
# -----------------------------------------#

label romains_VisitePart2:
    
    play sound "sfx/Voices/Num/Char_Num_Heureux_02.ogg"
    show char_numerimus heureux at speakingAnim(0.2, 0.82, 0.8, 1)
    num "Mais c'est extra ! Donne moi ça !"
    $ loveGauge(num_char, +35, 0.36, 0.28)
    hide screen inventory_screen
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    hide char_numerimus normal
    
    show char_numerimus heureux lunette at speakingAnim(0.2, 0.82, 0.8, 1)
    num "Regarde moi ça, Germain ! La grande classe !"
    show char_numerimus heureux lunette at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    
    jump romains_VisitePart3

# -----------------------------------------#
label romains_VisitePart3:
        
    play sound "sfx/Voices/Num/Char_Num_Normal_02.ogg"
    show char_numerimus normal lunette at speakingAnim(0.2, 0.82, 0.8, 1)
    num "Qu’est ce qu’il y a à voir dans le coin ?"
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            
    menu :
        num "{cps=0}Qu’est ce qu’il y a à voir dans le coin ?{/cps}"
        "L’air vivifiant du paysage Bructère !" if _testA == 0:
            $ _testA = 1
            play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
            y "La Lippe, l'herbe fraiche, l'air vivifiant du paysage Bructère !"
            
            play sound "sfx/Voices/Num et Dig/Char_Num_Dig_Doute_04.ogg"
            show char_digitimus normal right at speakingAnim(0.5, 0.8, 0.815, 1)
            show char_numerimus normal lunette lunette at speakingAnim(0.2, 0.82, 0.8, 1)
            dig "Ouais..."
            show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
            num "Mais encore ?"
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            jump romains_VisitePart3
            
        "Deux gros abrutis."if _testB == 0:
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_01.ogg"
            y "Deux bons gros abrutis."
            $ _testB = 1
            play sound "sfx/Voices/Num/Char_Num_Heureux_02.ogg"
            show char_numerimus normal lunette at speakingAnim(0.2, 0.82, 0.8, 1)
            num "Oh, vous savez ! Pour nous, vous vous ressemblez tous..."
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            jump romains_VisitePart3
            
        "Véléda ?":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "Il y a bien la prophétesse Véléda, mais..."
            
            play sound "sfx/Voices/Num et Dig/Char_Num_Dig_Heureux_03.ogg"
            show char_numerimus heureux lunette at speakingAnim(0.2, 0.82, 0.8, 1)
            show char_digitimus rire at speakingAnim(0.5, 0.8, 0.815, 1)
            dig "Mais c'est bien sur ! On a toujours voulu la rencontrer !"
            show char_digitimus rire at notSpeakingAnim(0.5, 0.8, 0.815, 1)
            num "Ouais ! Super idée, le Germain !"
            show char_numerimus heureux lunette at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            
            
            play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
            y "non mais là elle est pas..."
            
            play sound "sfx/Voices/Num/Char_Num_Heureux_01.ogg"
            show char_numerimus heureux lunette at speakingAnim(0.2, 0.82, 0.8, 1)
            num "Vendu ! On y va tout de suite !"
            show char_numerimus heureux lunette at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            
            stop music1 fadeout 1.5
            stop ambiance fadeout 1.0
            
            hide screen datingSim
            scene black with Dissolve (2.0)
            
            y "Dans quoi je me suis encore fourré...?"
            

            jump romains_VisitePart4
            
           
    
# -----------------------------------------#
                #VISITE (A LA TOUR)
# -----------------------------------------#
    
# -----------------------------------------#

label romains_VisitePart4:
    

    $ renpy.music.play("music/MUSIC_Tour_Antichambre.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("music/MUSIC_Tour_Chambre_Jour.ogg", channel = "music2", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Tour_Chambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music1')
    $ renpy.music.set_volume(0, delay=0, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='ambiance')
    
    scene bg_tour with Dissolve (1) :
        xpos 0 ypos -960
    show char_ernust normal right at notSpeakingAnim (0.3, 0.92, 0.9, 0.6)  with Dissolve(1.5)
    jump romains_VisitePart5
    
# -----------------------------------------#

label romains_VisitePart5:
    
  
    play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
    y "Ernust ! On a un problème !"
    y "Y'a deux Romains qui veulent voir Véléda !"
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_03.ogg"
    show char_ernust normal right at speakingAnim(0.3, 0.99, 0.97, 0.6) 
    e "Oh ! Dommage qu'elle soit morte !"
    show char_ernust normal right at notSpeakingAnim(0.3, 0.99, 0.97, 0.6) 
    
    play sound "sfx/SFX_Knock_01.ogg"
    num "Dites donc, on peut rentrer, là ? Il fait froid dehors !"
    
    play sound "sfx/Voices/Player/Char_Player_Non_02.ogg"
    y "Ahhhhh ! Les voilà !"
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_07.ogg"
    show char_ernust normal right at speakingAnim(0.3, 0.99, 0.97, 0.6) 
    e "T'en fais pas, Gaufrid, j'ai une idée géniale ! Fais moi confiance !"
    show char_ernust normal right at notSpeakingAnim(0.3, 0.99, 0.97, 0.6) 
    menu :
        e "{cps=0}T'en fais pas Gaufrid j'ai une idée géniale, fais moi confiance !{/cps}"
        "J'ai pas confiance.":
            play sound "sfx/Voices/Player/Char_Player_Non_01.ogg"
            y "Je te fais absolument pas confiance."
            y "Tu serais capable de la re-tuer !"
            y "Mais j'ai pas vraiment le choix, là..."
            jump romains_VisitePart7           
        "J'ai pas du tout confiance !":
            play sound "sfx/Voices/Player/Char_Player_Non_01.ogg"
            y "Je te fais absolument pas confiance !"
            y "Tu serais capable de la re-tuer !"
            y "Mais j'ai pas vraiment le choix, là..."
            jump romains_VisitePart7
        "J'ai vraiment pas du tout confiance !":
            play sound "sfx/Voices/Player/Char_Player_Non_02.ogg"
            y "Je te fais absolument pas confiance !"
            y "Tu serais capable de la re-tuer !"
            y "Mais j'ai pas vraiment le choix, là..."
            jump romains_VisitePart7
            
# -----------------------------------------#
label romains_VisitePart7:
   
    show char_ernust normal right at speakingAnim(0.3, 0.99, 0.97, 0.6) 
    play sound "sfx/Voices/Ernust/Char_Ernust_Love_03.ogg"
    e"Je te décevrais pas, Gaufrid !"
    show char_ernust normal right at notSpeakingAnim(0.3, 0.99, 0.97, 0.6) 
    show char_ernust normal right:
        linear 1.5 xpos -0.5 rotate 10
    pause 0.5
 
    play sound "sfx/Voices/Player/Char_Player_Heureux_01.ogg"
    y "Entrez !"
    play sound "sfx/SFX_Entrance_01.ogg"
    show char_numerimus dubitatif lunette:
        xalign 0.5 yalign 0.8 zoom 1
        xpos 1.3 ypos 0.90
        linear 1.0 xpos 0.475
    pause 1.0
    show char_numerimus dubitatif lunette at speakingAnim(0.475, 0.92, 0.9, 1)
    play sound "sfx/Voices/Num/Char_Num_Doute_03.ogg"
    num "C'est pas trop tôt !"
    show screen datingSim(num_char, 0.55, 0.35)
    show char_numerimus dubitatif lunette at notSpeakingAnim(0.475, 0.92, 0.9, 1)
    play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
    y "Mais... il est où, votre porte-enseigne ?"
    show char_numerimus normal lunette at speakingAnim(0.475, 0.92, 0.9, 1)
    play sound "sfx/Voices/Num/Char_Num_Normal_01.ogg"
    num "Il est puni de visite."
    num "Il a fait une remarque déplacée sur mes sandales."
    num "Bon, elle est où Véléda ?"
    show char_numerimus normal lunette at notSpeakingAnim(0.475, 0.92, 0.9, 1)
    
    jump romains_VisitePart8

            
# -----------------------------------------#

label romains_VisitePart8:
    
 #   play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    
    y "À l'étage. Elle se prépare..."
    play sound "sfx/Voices/Player/Char_Player_Hesitation_01.ogg"
    y "Ca devrait être bon... j'imagine ?"
    y "Suivez-moi."
    jump romains_VisitePart9

# -----------------------------------------#

label romains_VisitePart9:
    
    stop music1 fadeout 1.0
    hide screen datingSim
    scene bg_tour :
        xpos 0 ypos -960
        linear 2.0 xpos 0 ypos 0
        
    play sound "sfx/SFX_Stairs_01.ogg"   
    pause 3.0
    scene vel mario zorder 1 :
        xpos 0 ypos 0
    play sound "sfx/SFX_Stairs_01.ogg"
    jump romains_VisitePart10

# -----------------------------------------#
label romains_VisitePart10:
    
    
    $ renpy.music.play("music/MUSIC_Tour_Chambre_Jour.ogg", channel = "music1", loop = True, fadein = 2)
    show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
    show char_veledaernust 02 at notSpeakingAnim(0.8, 0.72, 0.70, 0.3) zorder 3:
    show screen datingSim(num_char, 0.25, 0.35)
    
    play sound "sfx/Voices/Num/Char_Num_Normal_01.ogg"
    num "Wow. Voici donc la vénérable Véléda..."    
    play sound "sfx/Voices/Ernust/Char_Ernust_Marionnette_02.ogg"
    show char_veledaernust 01 at speakingAnim(0.8, 0.80, 0.82, 0.3) zorder 3:
        
    ve "Bonnnnnnnjouuuuur, étranger !"
    ve "Je vaiiiis vous faire... une prophétie !!!"
    scene vel mario2 zorder 1:
        xpos 0 ypos 0

    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
        
    show char_veledaernust 02 at speakingAnim(0.8, 0.80, 0.82, 0.3) zorder 3:
    ve "Souuus le soleil de la pierre couleur cailloux !!!!!!"
    scene vel mario zorder 1 :
        xpos 0 ypos 0
    show char_veledaernust 01 at notSpeakingAnim(0.8, 0.72, 0.70, 0.3) zorder 3:
 
        
 #   play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
    play sound "sfx/Voices/Num/Char_Num_Normal_02.ogg"
    num "Fascinant... Qu'est-ce qu'elle veut dire ?"
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    
 #   play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
    y "Euuh là elle dit... qu’à votre retour les... gens à Rome... seront… très contents de vous voir."
    
 #   play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"    show char_numerimus normal at speakingAnim(0.2, 0.92, 0.9, 1.25)
    play sound "sfx/Voices/Num/Char_Num_Heureux_02.ogg"
    $ loveGauge(num_char, +15, 0.34, 0.28)
    num "Ahah ! C'est bien vrai !"
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    
    jump romains_VisiteProphetie
    
# -----------------------------------------#
label romains_VisiteProphetie:
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Marionnette_01.ogg"
    scene vel mario2 zorder 1 :
        xpos 0 ypos 0
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    show char_veledaernust 01 at speakingAnim(0.8, 0.80, 0.82, 0.3) zorder 3:
    ve  " Les oiseauuuuuuux chantent ! On dirait des corbeaux  !" 
    show char_veledaernust 02 at notSpeakingAnim(0.8, 0.72, 0.70, 0.3) zorder 3:
    
    show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
    play sound "sfx/Voices/Num/Char_Num_Normal_01.ogg"
    num "... Une traduction, s'il vous plaît ?"
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    
    play sound "sfx/Voices/Player/Char_Player_Hesitation_01.ogg"
    y "Là, elle dit que..."
    
 #   play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "{cps=0}Là, elle dit que...{/cps}"
        "La mort est proche !" :
            y "Un présage de mort plane sur vous !"
            show char_numerimus dubitatif lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
            play sound "sfx/Voices/Num/Char_Num_Normal_04.ogg"
            $ loveGauge(num_char, -15, 0.34, 0.28)
            num "Euuh... Merci... J'imagine? "
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
        "Il y a... des corbeaux ?" :
            y "Les oiseaux sont surement des corbeaux."
            show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
            play sound "sfx/Voices/Num/Char_Num_Normal_04.ogg"
            $ loveGauge(num_char, +1, 0.34, 0.28)
            num "Humm..."
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
        "Les oiseaux profiterons bientôt du printemps." : 
            y "Les oiseaux profiterons bientôt du printemps qui arrive."
            show char_numerimus heureux lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
            play sound "sfx/Voices/Num/Char_Num_Heureux_02.ogg"
            $ loveGauge(num_char, +15, 0.34, 0.28)
            num "Super ! Qui n'aime pas le printemps ?"
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
            
    
    
    #Proph 03#
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Marionnette_03.ogg"
    scene vel mario zorder 1 :
        xpos 0 ypos 0
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:    
    show char_veledaernust 01 at speakingAnim(0.8, 0.80, 0.82, 0.3) zorder 3:
   
    ve  " Eau chauuuuuude….. et eau froide ne font pas bon ménage !" 

    show char_veledaernust 02 at notSpeakingAnim(0.8, 0.72, 0.70, 0.3) zorder 3:
    play sound "sfx/Voices/Player/Char_Player_Hesitation_02.ogg"
    y "Et là elle dit que..."
 #   play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "{cps=0}Et là elle dit que...{/cps}"
        "Il y a un traître dans vos rangs !" :
            y "Il y a un traître dans vos rangs !"
            show char_numerimus dubitatif lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
            play sound "sfx/Voices/Num/Char_Num_Doute_02.ogg"
            $ loveGauge(num_char, -15, 0.34, 0.28)
            num "J'espère que ce n'est pas Digitimus !"
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
        "Vous allez sortir du lot." :
            y "Vous vous démarquerez en tant que grand centurion."
            show char_numerimus heureux lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
            play sound "sfx/Voices/Num/Char_Num_Heureux_03.ogg"
            $ loveGauge(num_char, +15, 0.34, 0.28)
            num "J'en étais sur !"
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
        "L'eau tiède, c'est désagréable" :
            y "Mélanger l'eau chaude et l'eau froide, c'est mal. " 
            show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
            play sound "sfx/Voices/Num/Char_Num_Normal_04.ogg"
            $ loveGauge(num_char, +1, 0.34, 0.28)
            num "Humm... oui."
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
            
    play sound "sfx/Voices/Ernust/Char_Ernust_Marionnette_04.ogg"
    scene vel mario2 zorder 1 :
        xpos 0 ypos 0
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    show char_veledaernust 02 at speakingAnim(0.8, 0.80, 0.82, 0.3) zorder 3:
    ve  " Ah.... je commence à avoir mal au bras..."
    show char_veledaernust 01 at notSpeakingAnim(0.8, 0.72, 0.70, 0.3) zorder 3:
    
 #   play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
    play sound "sfx/Voices/Num/Char_Num_Normal_04.ogg"
    num "Hein ?"
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
    y "Heuuu là... elle dit que..."
#    play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "{cps=0}Heuuu là... elle dit que...{/cps}"
        "Vous vous faites vieux." :
            y "La vieillesse vous guette… et de près"
            show char_numerimus dubitatif lunette at speakingAnim(0.2, 0.92, 0.9, 1)
            play sound "sfx/Voices/Num/Char_Num_Normal_03.ogg"
            $ loveGauge(num_char, -15, 0.34, 0.28)
            num "Ça va, je le sais ça !"
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1)
            jump romains_FinDeLaVisite80
        "Votre bras est très musclé." :
            y "Votre bras droit est plus musclé que le gauche. "
            show char_numerimus heureux lunette at speakingAnim(0.2, 0.92, 0.9, 1)
            play sound "sfx/Voices/Num/Char_Num_Heureux_03.ogg"
            $ loveGauge(num_char, +15, 0.34, 0.28)
            num "C'est extraordinaire !"
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1)
            jump romains_FinDeLaVisite80
        "Le poids de votre réussite sera remarquable !" :
            y "Le poids de votre réussite se fera sentir sur tout l’empire."
            show char_numerimus heureux lunette at speakingAnim(0.2, 0.92, 0.9, 1)
            play sound "sfx/Voices/Num/Char_Num_Heureux_02.ogg"
            $ loveGauge(num_char, +20, 0.34, 0.28)
            num "Pas étonnant, mon petit père... pas étonnant !"
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1)
            jump romains_FinDeLaVisite80

# -----------------------------------------#
label romains_FinDeLaVisite80:
    
 
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Marionnette_01.ogg"
    scene vel mario zorder 1 :
        xpos 0 ypos 0
    show char_veledaernust 02 at speakingAnim(0.8, 0.80, 0.82, 0.3) zorder 3:
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    ve  "... C'est fini."
    show char_veledaernust 01 at notSpeakingAnim(0.8, 0.72, 0.70, 0.3) zorder 3:
    show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
    play sound "sfx/Voices/Num/Char_Num_Normal_01.ogg"
    num "De quoi ?"
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"
    y "Le spectacle est terminé ! Hop hop hop, on retourne à l'entrée !"
    hide screen datingSim
    scene bg_tour :
        xpos 0 ypos 0
        linear 2.0 xpos 0 ypos -960
    play sound "sfx/SFX_Stairs_01.ogg"   
    pause 2.0
    
    show char_numerimus heureux lunette at speakingAnim(0.5, 0.92, 0.9, 1)
    show screen datingSim(num_char, 0.55, 0.35)

 
    
    play sound "sfx/Voices/Num/Char_Num_Heureux_02.ogg"
    num "Les propos de cette prophétesse m'ont vraiment inspirés !"
    num "Je vais quitter l'armée et rejoindre la Rome insoumise. On ne peut rester indifférent à de telles paroles !"
    num "Je n'aurais plus besoin de ça, tenez !"
    show char_numerimus heureux lunette at notSpeakingAnim(0.5, 0.92, 0.9, 1)
    $ inventory.add(glaive)
    $ _testGlaive = 1
    play sound "sfx/SFX_UI_Inventory_Glaive_01.ogg"
    show img_glaive at center:
        xalign 0.7 yalign 0.9 zoom 0.3
        linear 0.5 yalign 0.7 zoom 0.4
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
    pause 2.5
    play sound "sfx/SFX_UI_Inventory_Bag_01.ogg"
    pause 0.5
        
    hide screen datingSim
    hide char_numerimus normal lunette with Dissolve(1.5)
    hide screen datingSim
    pause 3.0
    y "Eh, mais c'est un {b}glaive{/b} ! Merci !"
    
    if _testGlaive == 1 & _testBouclier == 1:
        stop music1 fadeout 1.0
        hide screen datingSim
        jump PlaceDuVillageAllObjects
        
    else:
        stop music1 fadeout 1.0
        hide screen datingSim
        jump PlaceDuVillageDefault
    
# -----------------------------------------#
                #BLAGUE
# -----------------------------------------#

label romains_Blague:
    
    if _testBlague == 1:
        y "Tenez lisez ça..."
        show screen inventory_screen(obj = "blague")
        
        play sound "sfx/SFX_UI_Inventory_Glaive_01.ogg"

        pause 3.0
        
        hide screen inventory_screen
        play sound "sfx/Voices/Num et Dig/Char_Num_Dig_Rire_01.ogg"
        show char_numerimus heureux at speakingAnim(0.2, 0.82, 0.8, 1)
        show char_digitimus rire right at speakingAnim(0.5, 0.8, 0.815, 1)
        num "Hahahaha !"
        $ loveGauge(num_char, +10, 0.36, 0.28)
        show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
        dig "Haahahahaha... haahaha!"
        $ loveGauge(num_char, +25, 0.36, 0.28)
        dig "C'est la meilleure blague que j'ai entendu de ma vie !"
        show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
        dig "Bon bah, merci ! Pour te remercier je... bah, tiens ! C'est... ma {b}trompette{b}."
        
        $ inventory.add(trompette)
        $ _testTrompette = 1
        
        play sound "sfx/SFX_UI_Inventory_Trumpet_01.ogg"
        
        show img_trompette at center:
            xalign 0.7 yalign 0.9 zoom 0.3
            linear 0.5 yalign 0.7 zoom 0.4
            easein 0.5 zoom 0.55
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
        pause 2.5
        play sound "sfx/SFX_UI_Inventory_Bag_01.ogg"
        pause 0.5
        y "... Qu'est ce que je vais bien faire d'une {b}trompette{/b}, moi ?"
        show char_ernust normal left:
            xalign 0.5 yalign 0.8
            xpos 0.999 ypos 1.9 zoom 0.8 rotate -30
            linear 0.3 xpos 0.9 ypos 1.3
        #pause 1.5
        
        play sound "sfx/Voices/Ernust/Char_Ernust_Normal_03.ogg"
        e "On peut s'en servir pour faire peur aux animaux !"
        y "... Mais, de quoi tu parles ?"
        show char_ernust normal left:
            xalign 0.5 yalign 0.8
            xpos 0.9 ypos 1.3 zoom 0.8 rotate -30
            linear 0.3 xpos 0.999 ypos 1.9
        pause 1.0
        jump romains_Part5