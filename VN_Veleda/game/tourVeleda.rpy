##########################################################
# Ici figurent les scènes se déroulant à la Tour Véléda. #
##########################################################

label tourVeleda_ErnustEtVeleda :
    
    scene bg_tour with Dissolve (2.5) :
        xpos 0 ypos 0
        
    $ renpy.music.play("music/MUSIC_Tour_Antichambre.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("music/MUSIC_Tour_Chambre_Jour.ogg", channel = "music2", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Tour_Chambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music1')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='ambiance')
    
    
    
    show vel normal with Dissolve (2.5) :
        xpos 0 ypos 0
    
    $ interlocuteur = "vel_char"
    
    show screen datingSim(vel_char, 0.625, 0.33)
    
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_04.ogg"
    
    show vel normal2 :
        xpos 0 ypos 0
        
    v "Vous voilà Gaufrid ! Dépèchez vous, nous attendons des clients très importants."
    
    play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"
    y "Mais... ils sont encore là, ces chiffres ? J'ai perdu la boule ou quoi ?"
    
    play sound "sfx/Voices/Veleda/Char_Veleda_rage_01.ogg"
    $ loveGauge(vel_char, -3, 0.75, 0.4)
    
    show vel normal :
        xpos 0 ypos 0

    v "Des chiffres ? De quoi parlez vous, enfin ?"
    
    $ loveGauge(vel_char, -3, 0.75, 0.4)
    
    v "Allez préparer la salle, Monsieur Gaufrid. Vos âneries ne nous intéressent pas."
    

    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_02.ogg"
    
    show vel normal2 :
        xpos 0 ypos 0
    
    v "Nous attendons un invité de marque aujourd'hui ! Monseigneur Crossfrit... croshfritsh... crosrustr..."
    
    
    v "Monseigneur Crossfriture, le digne chef de nos voisins les Bataves."
    
    show vel normal :
        xpos 0 ypos 0
        
    y "Vous voulez dire Crossfitrichernvald ?" 
    
    menu :
        y "{cps=0}Vous voulez dire Crossfitrichernvald ?{/cps}"
        "Il vient demander conseil, Ô Véléda ? ":
            play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
            
            y "Il vient écouter la grande sagesse de vos légendaires prophéties, Ô divine Véléda ?"
            
            play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
            
            $ loveGauge(vel_char, -3, 0.5, 0.25)
            
            show vel normal2 :
                xpos 0 ypos 0
            
            v "Oh vous ne nous trompez pas avec vos minauderies Monsieur Gaufrid."
            
            $ loveGauge(vel_char, -3, 0.75, 0.4)
    
            v "La flatterie est le refuge des incompétents."
            
            
        "Il veut quoi lui ?":

            play sound "sfx/Voices/Player/Char_Player_Sarcastic_04.ogg"
            y "Qu'est ce qu'il veut, celui-là ?"
            
            play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
            
            show vel normal2 :
                xpos 0 ypos 0
            
            $ loveGauge(vel_char, -3, 0.5, 0.25)
            v "Oh ! Quelle vulgarité Monsieur Gaufrid !"
            
            $ loveGauge(vel_char, -3, 0.5, 0.25)
            v "Qu'est ce que c'est que ce langage de sauvage ?"

            
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_01.ogg"
    
    show vel normal :
        xpos 0 ypos 0
    
    v "Monseigneur Crossfritrichenfer accuse le forgeron de notre village, Monsieur Brutalmund, de lui avoir dérobé sa propriété !"
    
    v "Monsieur Brutalmund nie l'accusation ! Nous allons donc les départager avec..."
    
    $ renpy.music.set_volume(0, delay = 0, channel='music1')
    $ renpy.music.set_volume(0, delay = 0, channel='music2')
    $ renpy.music.set_volume(0, delay=0, channel='ambiance')
    
    show vel normal2 :
        xpos 0 ypos 0
        
    play sound "sfx/SFX_Drama_01.ogg"
    show vel normal2 :
        xpos 0 ypos 0
        easein 0.8 xpos -300 zoom 1.2
    $ renpy.pause(2.0, hard = True)
    v "Une prophétie !"
    show vel normal2 with Dissolve(0.5):
        xpos 0 ypos 0 zoom 1.0
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music1')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='ambiance')
    
 
    play sound "sfx/Voices/Player/Char_Player_Hesitation_01.ogg"
    y "Euh.. il devrait pas plutôt porter plainte ?"
    
    show vel normal :
        xpos 0 ypos 0
    
    play sound "sfx/Voices/Veleda/Char_Veleda_Rage_01.ogg"

    
    $ loveGauge(vel_char, -3, 0.8, 0.25)
    v "Vous doutez de la sagesse de nos visions, Monsieur Gaufrid ?"
    
    v "Où se trouve votre cousin, d'ailleurs ? Le simplet, Monsieur Ernust ?"
    
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_04.ogg"
    v "Cela fait une heure qu'il doit nous apporter de quoi nous sustenter !"
    
    show vel normal2 :
        xpos 0 ypos 0
    
    play sound "sfx/SFX_Entrance_01.ogg"
    
    pause 0.8
    
    v "Ah ! Cela doit être lui !"
    
    play sound "sfx/SFX_Stairs_02.ogg"
    show char_ernust normal right :
        xalign 0.5 yalign 0.8
        xpos -0.2 ypos 2.0 zoom 0.6
        linear 1.2 xpos 0.20 ypos 0.94
        
    $ renpy.pause (1.7, hard=True)
    
    $ interlocuteur = "ern_char"
    show screen datingSim(ern_char, 0.15, 0.17)
    
    pause 0.5

    show char_ernust joyeux right at speakingAnim(0.21,1.025,1.0,0.6)
   
    
 #   play sound "sfx/SFX_Char_Ernust_Normal_01.ogg"
    
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
    e "Oh, bonjour Gaufrid !"
    $ loveGauge(ern_char, 1, 0.26, 0.14)
    show char_ernust normal right at notSpeakingAnim(0.193,1.02,1.0,0.6)
    show vel normal :
        xpos 0 ypos 0
    menu :
        e "{cps=0}Oh, bonjour Gaufrid !{/cps}"
        "Bonjour Ernust !" :
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Bonjour Ernust, comment ça va ?"
            
            show char_ernust love1 at speakingAnim(0.23,1.025,1.0,0.6)
            play sound "sfx/Voices/Ernust/Char_Ernust_Normal_05.ogg"
            $ loveGauge(ern_char, 3, 0.26, 0.14)            
            e "Ça va bien !"
            $ loveGauge(ern_char, 3, 0.26, 0.14)
            e "C'est gentil de demander Gaufrid !"
            
        "90 points d'affection ?" :
            play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
            y "90 de love ? Il est amoureux de moi ?"

            show char_ernust love1 at speakingAnim(0.23,1.025,1.0,0.6)
            play sound "sfx/Voices/Ernust/Char_Ernust_Normal_05.ogg"
            $ loveGauge(ern_char, 3, 0.26, 0.14)            
            e "T'es mon meilleur ami Gaufrid !"
            $ loveGauge(ern_char, 3, 0.26, 0.14)
            e "J'taime bien !"

            
        "Ah... t'es là, toi ?" :
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_01.ogg"
            y "Ah... t'es là toi ? Pfff..."

            show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)

            play sound "sfx/Voices/Ernust/Char_Ernust_Normal_05.ogg"
            $ loveGauge(ern_char, 3, 0.26, 0.14)            
            e "Oui je suis là !"
            $ loveGauge(ern_char, 3, 0.26, 0.14)
            show char_ernust love1 at speakingAnim(0.23,1.025,1.0,0.6)
            e "Moi aussi ça me fait plaisir de te voir Gaufrid !"


            
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
    
    pause 0.1 
    
    show char_ernust inquiet right :
            xpos 0.195 ypos 1.02 zoom 0.6
            linear 0.15 xpos 0.185 ypos 1.03 rotate -5
    
    $ interlocuteur = "vel_char"
    show screen datingSim(vel_char, 0.625, 0.33)
    
    show vel normal2 :
        xpos 0 ypos 0
    $ loveGauge(vel_char, -1, 0.75, 0.4)
    v "Amenez nous notre nourriture, monsieur Ernust !  Nous mourrons de faim."

    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_06.ogg"
    show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
    show vel normal :
        xpos 0 ypos 0
    e "Oh oui, Votre Excellessence Madame Véléda !"
    e "Je suis allé dans la forêt chasser un sanglier."
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_03.ogg"
    show char_ernust normal right at speakingAnim(0.19,1.02,1.0,0.6)
    e "Je me suis dit : un bon sanglier rôti, ça tient le corps et c'est vraiment bon !"
    show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
    e "Avec un peu de thym et des p'tites pommes sautées..."
    show char_ernust normal right at notSpeakingAnim(0.193,1.02,1.0,0.6)
    menu :
        e "{cps=0}Avec un peu de thym et des p'tites pommes sautées...{/cps}"
        "Ça a l'air délicieux !" :
            
            $ interlocuteur = "ern_char"
            show screen datingSim(ern_char, 0.15, 0.17)
            
            play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
            y "Ça a l'air super bon Ernust, j'ai hâte de voir ça !"
            
            show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
            
            play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_01.ogg"
            $ loveGauge(ern_char, 3, 0.26, 0.14)
            e "T'es gentil Gaufrid !"
            $ loveGauge(ern_char, 2, 0.26, 0.14)
            
            e "Je pensais à toi en plus. Je me suis dit : Gaufrid, il doit être triste !"
            $ loveGauge(ern_char, 2, 0.26, 0.14)
            
            show char_ernust normal right at speakingAnim(0.19,1.02,1.0,0.6)
            play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_02.ogg"
            e "Ingrid elle est pas gentille avec toi !"
            $ loveGauge(ern_char, 5, 0.26, 0.14)
            
            show char_ernust love1 at speakingAnim(0.23,1.025,1.0,0.6)
            
            e "Mais moi, je trouve que t'es vraiment spécial Gaufrid."

            
        "Tu peux abréger ?" :
            
            $ interlocuteur = "ern_char"
            show screen datingSim(ern_char, 0.15, 0.17)
            
            play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
            y "Abrège Ernust, on attend des clients."
            
            play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_02.ogg"
            show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
            e "T'as raison Gaufrid. Je parle trop encore !"
            
            show char_ernust love1 at speakingAnim(0.23,1.025,1.0,0.6)
            
            $ loveGauge(ern_char, 3, 0.26, 0.14)
            e "Tu me dis tout le temps quand je fais des bêtises !"
            
            play sound "sfx/Voices/Ernust/Char_Ernust_Normal_02.ogg"
            $ loveGauge(ern_char, 2, 0.26, 0.14)
            e "Ça m'aide beaucoup tu sais. J'ai l'impression d'être plus intelligent avec toi !"
            
                
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_01.ogg"
    
    pause 0.1 
    
    show char_ernust inquiet right :
            xpos 0.195 ypos 1.02 zoom 0.6
            linear 0.15 xpos 0.185 ypos 1.03 rotate -5
    
    #show char_veleda normal at speakingAnim(0.48,0.82,0.80,0.7)
    show vel normal2 :
        xpos 0 ypos 0
    
    $ interlocuteur = "vel_char"
    show screen datingSim(vel_char, 0.625, 0.33)
    
    v "Cela suffit ! Servez nous notre sanglier !"
    #show char_veleda normal at notSpeakingAnim(0.48,0.82,0.80,0.7)
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_06.ogg"
    show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
    show vel normal :
        xpos 0 ypos 0
    e "Ah bah non, y'a pas de sanglier !"
    e "J'en ai vu un dans la forêt, mais bon... j'ai pas d'armes !"
    e "Ça se chasse pas à mains nues, hein, le sanglier."
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
    e "Mais j'ai trouvé des champignons, alors j'ai fait une soupe ! Une bonne soupe de champignons !"
    show char_ernust normal right at notSpeakingAnim(0.193,1.02,1.0,0.6)
    #show char_veleda normal at speakingAnim(0.48,0.82,0.80,0.7)
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
    show vel normal2 :
        xpos 0 ypos 0
    v "Cela suffira ! Et vous, Gaufrid, allez accueillir nos invités. Nous prophétisons qu'ils vont frapper à la porte !"
    
    play sound "sfx/SFX_Knock_01.ogg"
    pause 1.0
    v "Haa, vous voyez ? Allez-y, Monsieur Gaufrid."
    #show char_veleda normal at notSpeakingAnim(0.48,0.82,0.80,0.7)
    play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
    show vel normal :
        xpos 0 ypos 0
    y "Ok, ok, j'y vais..."
    
    hide screen datingSim
    
    window hide 
    
    $ renpy.music.set_volume(0, delay=1, channel='music2')
    
    stop ambiance fadeout 1.5
    
    scene bg_tour :
        xpos 0 ypos 0
        linear 2.0 xpos 0 ypos -960
    show vel normal :
        xpos 0 ypos 0
        linear 2.0 xpos 0 ypos -960
    show char_ernust normal right :
        xalign 0.5 yalign 0.8
        xpos 0.20 ypos 1.02 zoom 0.6
        linear 2.0 xpos 0.24 ypos -0.55
    show char_crossfit colere right :
        xalign 0.5 yalign 0.8
        xpos 0.20 ypos 3.0 zoom 0.32
        linear 2.0 xpos 0.26 ypos 0.84
    show char_brutal normal:
        xalign 0.5 yalign 0.8
        xpos 0.81 ypos 3.0 zoom 0.32
        linear 2.0 xpos 0.75 ypos 0.92
        
    play sound "sfx/SFX_Stairs_01.ogg"   
    $ renpy.pause(2.5, hard = True)
             
    
    jump tourVeleda_HistoireBrevetPart1

        
# -----------------------------------------#

label tourVeleda_HistoireBrevetPart1:

    $ renpy.music.play("ambiances/AMB_Lieu_Antichambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    

    #show char_brutal normal at notSpeakingAnim(0.75, 0.92,0.92,0.32) with Dissolve(1)

    
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Colere_01.ogg"
    show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)
    cross "Nous voilà ! Je vais enfin trouver justice, Brutalmund !"
    
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    show char_brutal colere at speakingAnim(0.75, 1.05, 1.02, 0.32)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
    brut "J't'ai déjà dit que j't'ai rien volé du tout !"
    
    show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.2,0.32)
    show char_crossfit serieux at speakingAnim(0.26,0.94,0.92,0.32)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Colere_03.ogg"
    cross "Toi, l'assistant, va chercher la prophétesse !"
    
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
    y "Ah non ! La prophétesse ne voit pas directement ses visiteurs."
    y "Vous m'expliquez le problème, et je lui transmets. Après, je vous interprète ses visions."
    

    show char_crossfit serieux at speakingAnim(0.26,0.94,0.92,0.32)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Serieux_02.ogg"
    cross "Très bien, serviteur ! Mais si tu ne transmets pas nos messages exactement, je t'égorge."
    
    $ interlocuteur = "cross_char"
    
    show screen datingSim(cross_char, 0.35, 0.27)
    
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    menu :
        cross "{cps=0}Très bien, serviteur ! Mais si tu ne transmets pas nos messages exactement, je t'égorge.{/cps}"
        "Oui, Monseigneur" :
            
            $ loveGauge(cross_char, 5, 0.45, 0.27)
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Bien sur, Monsieur Crossfritrichernvald, je ferai bien attention."
            
        "Je sais faire mon travail, hein" :
            $ loveGauge(cross_char, -5, 0.45, 0.27)
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_04.ogg"
            y "Eh oh, je sais ce que je fais, hein ! Pas la peine de me menacer."
    
    y "Dites moi tout, quel est le problème ?"
    
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_01.ogg"
    show char_brutal normal at speakingAnim(0.75, 1.05,1.02,0.32)
    
    $ interlocuteur = "brut_char"
    
    show screen datingSim(brut_char, 0.63, 0.29)
    
    brut "J'vais t'expliquer, Gaufrid, mon pote !"
    brut "T'vois, l'autre jour, Crossfitrichernvald, il passe d'vant chez moi."
    show char_brutal heureux at speakingAnim(0.75, 1.05,1.02,0.32)
    
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
    brut "Et il voit un bouclier qui ressemble au sien."
    show char_brutal colere at speakingAnim(0.75, 1.05,1.02,0.32)
    
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
    brut "Mais j'l'ai pas volé c'te bouclier !"
    brut "C'est moi qui l'ai fait. De mes p'tites mains ! J'te jure mon p'tit Gaufrid !"
    show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.02,0.32)
    
    $ interlocuteur = "cross_char"
    
    show screen datingSim(cross_char, 0.35, 0.27)
    
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Choc_01.ogg"
    show char_crossfit choc right at speakingAnim(0.26,0.94,0.92,0.32)
    cross "Ah ! Mais tu sais bien que ce n'est pas ça, le problème, escroc !"
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)

    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
    show char_brutal surpris at speakingAnim(0.75, 1.05,1.02,0.32)
    brut "Moi ? Un escroc ?"
    show char_brutal normal at notSpeakingAnim(0.75, 1.05,0.92,0.32)
    
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_01.ogg"
    show char_crossfit serieux at speakingAnim(0.26,0.94,0.92,0.32)
    cross "Oui, un escroc ! Ce bouclier est exactement le même que le mien. Tu l'as copié !"
    cross "C'est du vol de propriété intellectuelle !"
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)        

    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
    show char_brutal colere at speakingAnim(0.75, 1.05,1.02,0.32)
    brut "Oh, toi, tout de suite avec les grands mots hein !"
    show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.0,0.32)
    
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Serieux_01.ogg"
    show char_crossfit serieux at speakingAnim(0.26,0.94,0.92,0.32)
    cross "Le concept de propriété intellectuelle est fondamental à la société Germaine du premier siècle !"
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    menu :
        cross "{cps=0}Le concept de propriété intellectuelle est fondamental à la société Germaine du premier siècle !{/cps}"
        "C'est très grave !" :
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            y "C'est vrai que c'est très grave !"
            $ interlocuteur = "brut_char"
    
            show screen datingSim(brut_char, 0.63, 0.29)
            
            
            
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
            show char_brutal surpris at speakingAnim(0.75, 1.05,1.02,0.32)
            brut "Tu t'y mets, toi aussi ! Gaufrid, mon poteau !"
            show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.02,0.32)
            
            $ loveGauge(brut_char, -5, 0.55, 0.27)
            
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Bon, je vais voir ce qu'en dit notre divine prophétesse."
        
        "On s'en fout, non ?" :
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            y "Y'a pas de quoi en faire tout un plat, non ?"
            
            $ loveGauge(cross_char, -5, 0.45, 0.27)
            
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Choc_01.ogg"
            show char_crossfit choc right at speakingAnim(0.26,0.94,0.92,0.32)
            cross "Comment oses-tu, domestique ?"
            show char_crossfit serieux at speakingAnim(0.26,0.94,0.92,0.32)
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Serieux_03.ogg"
            cross "Nos lois sont claires ! Va voir la prophétesse, maintenant !"
            show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
            
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Ok ! Ok ! J'y vais ! Faut pas s'énerver comme ça !"
            
    hide screen datingSim        
    
    window hide 
    
    stop ambiance fadeout 1.5

    scene bg_tour :
        xpos 0 ypos -960
        linear 2.0 xpos 0 ypos 0
    show vel morte :
        xpos 0 ypos -960
        linear 2.0 xpos 0 ypos 0
    show char_ernust normal right :
        xalign 0.5 yalign 0.8
        xpos 0.24 ypos -0.55 zoom 0.6
        linear 2.0 xpos 0.193 ypos 0.92
    show char_crossfit colere right :
        xalign 0.5 yalign 0.8
        xpos 0.26 ypos 0.84 zoom 0.32
        linear 2.0 xpos 0.20 ypos 3.0
    show char_brutal normal:
        xalign 0.5 yalign 0.8
        xpos 0.75 ypos 1.05 zoom 0.32
        linear 2.0 xpos 0.81 ypos 3.0
        
    play sound "sfx/SFX_Stairs_02.ogg"   
    $ renpy.pause(2.5, hard = True)
    
    jump tourVeleda_MortVeleda
    
# -----------------------------------------#
    
label tourVeleda_MortVeleda:
    
    $ renpy.music.set_volume(0.4, delay=1, channel='music2')
    $ renpy.music.play("ambiances/AMB_Lieu_Tour_Chambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    pause 0.5
    
    show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_07.ogg"
    
    e "Ah Gaufrid, ça c'est bien passé ?"
    e "Véléda fait une petite sieste !"
    
    show char_ernust normal right  at notSpeakingAnim(0.185,1.01,1.0,0.6)
   
    play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
    y "Comment ça, une sieste ?"
    
    show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
    
    e "Bah oui, elle a mangé ma soupe aux champignons et elle a fait des bruits bizarres."
    e "Je pense qu'elle a vomi à un moment, mais après elle s'est endormie tranquillement !"
    
    show char_ernust normal right  at notSpeakingAnim(0.185,1.01,1.0,0.6)
    play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
    y "Quoi ? Mais... c'était quoi comme champignons ?"
    y "Va voir si elle va bien !"
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_02.ogg"
    show char_ernust joyeux right :
        xalign 0.5 yalign 0.8
        xpos 0.185 ypos 1.01 zoom 0.6
        linear 1 xpos 0.35 ypos 1.05 zoom 0.55 rotate 5
        
    $ renpy.pause (1.1, hard = True)
    
    show char_ernust normal right :
        linear 0.15 rotate 25
    
    $ renpy.pause (0.6, hard = True)
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_01.ogg"
    e "Euh..."
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Trahi_02.ogg"
    show char_ernust inquiet right :
        linear 0.15 rotate -3
        linear 0.15 rotate 3
        linear 0.15 rotate 0
        
    $ renpy.pause (0.8, hard = True)
    
    show char_ernust inquiet right at speakingAnim(0.35,1.05,1.0,0.55)

    e "Elle va pas bien du tout, Gaufrid !"
    e "Je sens pas du tout son pouls !"
    
    show char_ernust inquiet right at notSpeakingAnim(0.35,1.04,1.0,0.55)
    play sound "sfx/Voices/Player/Char_Player_Non_02.ogg"
    y "Quoi ? Mais.. tu as tué Véléda, Ernust !"
    y "La prophétesse la plus connue de toute l'histoire !"
    
    show char_ernust inquiet right at speakingAnim(0.35,1.05,1.0,0.55)
    
    e "Oh, je suis désolé Gaufrid !"
    e "Qu'est ce qu'on va faire ?"
    
    show char_ernust inquiet right at notSpeakingAnim(0.35,1.04,1.0,0.55)
    play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"
    y "Tu sais quoi... je vais inventer une prophétie !"
    y "Ils verront jamais la différence !"
    y "Bouge surtout pas d'ici !"
    
    hide screen datingSim
    
    window hide 
    
    $ renpy.music.set_volume(0, delay=1, channel='music2')
    stop ambiance fadeout 1.5
    
    scene bg_tour :
        xpos 0 ypos 0
        linear 1.75 xpos 0 ypos -960
    show vel morte :
        xpos 0 ypos 0
        linear 1.75 xpos 0 ypos -960
    show char_ernust inquiet right :
        xalign 0.5 yalign 0.8
        xpos 0.35 ypos 0.94 zoom 0.55
        linear 2.0 xpos 0.36 ypos -0.59
    show char_crossfit colere right :
        xalign 0.5 yalign 0.8
        xpos 0.20 ypos 3.0 zoom 0.32
        linear 1.75 xpos 0.26 ypos 0.84
    show char_brutal normal:
        xalign 0.5 yalign 0.8
        xpos 0.81 ypos 3.0 zoom 0.32
        linear 1.75 xpos 0.75 ypos 0.92
        
    play sound "sfx/SFX_Stairs_02.ogg"   
    $ renpy.pause(2, hard = True)
    
    jump tourVeleda_HistoireBrevetPart2
    
# -----------------------------------------#
    
label tourVeleda_HistoireBrevetPart2:


    $ renpy.music.play("ambiances/AMB_Lieu_Antichambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    show char_brutal normal at notSpeakingAnim(0.75, 0.92,1.02,0.32)

    
    show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)
    
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Colere_02.ogg"
    cross "Ah, enfin ! Parle, larbin."
    
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    y "Messieurs ! La divine Véléda a consulté les dieux, et m'a transmis sa prophétie !"
    
    menu :
        y "{cps=0}Messieurs ! La divine Véléda a consulté les dieux, et m'a transmis sa prophétie !{/cps}"
        "Crossfitrichernvald a été spolié !" :
            $ Acte1_Tour_CoupableJugement = "Brutalmund"
            $ interlocuteur = "cross_char"
    
            show screen datingSim(cross_char, 0.35, 0.27)
            
            y "Brutalmund va devoir payer réparations !"
            
            $ loveGauge(cross_char, 5, 0.45, 0.27)
            
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Serieux_02.ogg"
            show char_crossfit serieux at speakingAnim(0.26,0.94,0.92,0.32)   
            cross "Aha ! Justice est faite !"
            show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
            
            $ interlocuteur = "brut_char"
    
            show screen datingSim(brut_char, 0.63, 0.29)
            
            
            show char_brutal colere at speakingAnim(0.75, 1.05,1.02,0.32)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
            brut "C'est quoi c't'histoire ?"
            show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.02,0.32)
            
            y "Brutlamund va donner 2 buffles à Crossfritrichernvald !"
            
            $ loveGauge(brut_char, -5, 0.73, 0.29)
            
            show char_brutal surpris at speakingAnim(0.75, 1.05,1.02,0.32)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
            brut "Quoi ? Deux buffles ? Ça va pas la tête ?"
            show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.02,0.32)
            
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_03.ogg"
            show char_crossfit inquiet at speakingAnim(0.26,0.94,0.92,0.32)
            cross "Des... des buffles ?"
            
        "Brutalmund est accusé à tort !":
            $ Acte1_Tour_CoupableJugement = "Crossfit"
            
            $ interlocuteur = "brut_char"
    
            show screen datingSim(brut_char, 0.63, 0.29)
            
            y "Les dieux sont insultés par la frivolité de cette accusation !"
            
            $ loveGauge(brut_char, 5, 0.73, 0.29)
            
            show char_brutal heureux at speakingAnim(0.75, 1.05,1.02,0.32)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_02.ogg"
            brut "Haha ! J'te l'avais dit !"
            show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.02,0.32)
            
            $ interlocuteur = "cross_char"
    
            show screen datingSim(cross_char, 0.35, 0.27)
            
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Choc_01.ogg"
            show char_crossfit choc right at speakingAnim(0.26,0.94,0.92,0.32) 
            cross "Quel scandale !"
            show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
            $ loveGauge(cross_char, -5, 0.45, 0.27)
            y "Crossfitrichernvald doit procurer deux buffles à Brutalmund, en tant que frais de dossier !"
            show char_brutal normal at speakingAnim(0.75, 1.05,1.02,0.32)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere2_03.ogg"
            brut "Des buffles ? Bah ! J'en ai plein déjà."
            show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.02,0.32)
            
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_03.ogg"
            show char_crossfit inquiet at speakingAnim(0.26,0.94,0.92,0.32)
            cross "Des... des buffles ?"
    
    
    show char_crossfit inquiet at notSpeakingAnim(0.26,0.94,0.92,0.32)
    y "La prophétesse a parlé, messieurs !"
    
    hide screen datingSim
    
    y "Je vous prie de dégager de là vite fait, maintenant !"
    
 #   play sound "sfx/SFX_Walk_02.ogg"
 
    show char_crossfit inquiet :
        xalign 0.5 yalign 0.8
        xpos 0.26 ypos 0.94 zoom 0.32 rotate -12
        linear 1.8 xpos 2.0 ypos 0.94
    show char_brutal normal:
        xalign 0.5 yalign 0.8
        xpos 0.75 ypos 1.05 zoom 0.32 rotate 8
        linear 2.0 xpos 2.0 ypos 1.05
    
    
    y "Allez, hop hop hop !"
    
    pause 0.5

    y "Bon, moi, je vais aller à la taverne ! Ça donne soif toutes ces émotions !"
    y "Je vais pouvoir voir Ingrid, en plus !"
    
    stop music1 fadeout 1.5
    stop music2 fadeout 1.5
    stop ambiance fadeout 0.5
    
    jump narration_ellipse02
    #jump tourVeleda_MarryingIngridPart2
    
# -----------------------------------------#

label tourVeleda_MarryingIngridPart2:
    scene bg_place:
        zoom 1 xanchor 0.0 yanchor 0.0
        easein 2.0 xpos -2000 ypos -150 zoom 2.5
    
    $ renpy.music.play("music/MUSIC_Main_CarteVillage.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_CarteVillage_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    pause 2.0
    show char_ernust normal right :
        xalign 0.5 yalign 0.8
        zoom 0.7 xpos 0.2 ypos 1.5
        easein 0.8 xpos 0.4 ypos 0.94 
    pause 0.8
    play sound "sfx/Voices/Player/Char_Player_Hesitation_02.ogg"
    y "Vite Ernust ! Passe devant et prépare la Vélédarionnette !"
    show char_ernust normal right at speakingAnim(0.4, 1.03, 1.01, 0.7)
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
    e "À tes ordres Gaufrid !"
    show char_ernust normal right :
        xalign 0.5 yalign 0.8
        zoom 0.7 xpos 0.4 ypos 1.03
        easeout 0.8 xpos 1.5
    pause 0.8
    hide char_ernust
    
    show char_ingrid normal right :
        xalign 0.5 yalign 0.8
        zoom 0.25 xpos 0.2 ypos 1.5
        easein 0.8 xpos 0.4 ypos 1.06
    pause 0.8
    show char_ingrid love at speakingAnim(0.4, 1.16, 1.14, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_02.ogg"
    i "Oh mon Gaufrid ! On va enfin pouvoir se marier !"
    i "Véléda doit nous attendre pour donner sa bénédiction"
    show char_ingrid love:
        xalign 0.5 yalign 0.8
        zoom 0.25 xpos 0.4 ypos 1.18
        easeout 0.8 xpos 1.5
    pause 0.8

    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    
    scene vel mario2 with Dissolve(1.5) 
    $ renpy.music.play("music/MUSIC_Tour_Antichambre.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Antichambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)

    show char_veledaernust 01 at speakingAnim(0.8, 0.78, 0.76, 0.3) zorder 2:

    show char_ingrid normal zorder 2:
        xalign 0.5 yalign 0.8 zoom 0.25
        xpos 0.0 ypos 1.5
        linear 1.5 xpos 0.15 ypos 1.16
    pause 2.0
    play sound "sfx/Voices/Ernust/Char_Ernust_Marionnette_04.ogg"
    ve "Nous sommes réunis en ce jour heureux pour célébrer le..."
    show vel mario zorder 1 with Dissolve(0.5) 
    pause 0.5
    show vel mario2 zorder 1 with Dissolve(0.5) 
    show char_veledaernust 02 at speakingAnim(0.8, 0.78, 0.76, 0.3) zorder 2:
    play sound "sfx/Voices/Ernust/Char_Ernust_Trahi_02.ogg"
    e "Eh ! Mais elle arrête pas de bouger !"
    play sound "sfx/Voices/Player/Char_Player_Hesitation_02.ogg"
    y "De bouger ?!"
    
    show vel normal zorder 1 with hpunch
    show char_veledaernust 02:
        xalign 0.5 yalign 0.8
        zoom 0.3 xpos 0.8 ypos 0.78
        linear 0.6 xpos 2.0 ypos 1.0
    play sound "sfx/Voices/Veleda/Char_Veleda_rage_01.ogg"
    v "Ernust ! Que faites-vous !"
    v "Lâchez nous immédiatement !"
    
    show char_ingrid choc at speakingAnim(0.15, 1.22, 1.20, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Choc_01.ogg"
    i "Ernust ! Tu as fait semblant d'être Véléda ?"
    i "Quelle horreur ! Tu as bafoué toutes nos traditions !"
    
    show char_ingrid choc at notSpeakingAnim(0.15, 1.22, 1.20, 0.25)
    show vel normal2 zorder 1
    show char_ernust inquiet left zorder 2:
            xalign 0.5 yalign 0.8
            xpos 1.0 ypos 1.9 zoom 0.7 rotate -15
            linear 0.8 xpos 0.9 ypos 1.13
    pause 1.2
    
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_01.ogg"
    e "Ah ben mince Gaufrid, on a été démasqué !"
    show char_ingrid choc at speakingAnim(0.15, 1.22, 1.20, 0.25)
    i "Gaufrid ?! Tu es dans le coup, toi aussi ?!"
    show char_ingrid choc at notSpeakingAnim(0.15, 1.22, 1.20, 0.25)
    y "Ernust ! Tu m'avais dit qu'elle était morte !"
    jump ending_AskErnust

# -----------------------------------------#

label ending_AskErnust:

    show char_ernust inquiet left at speakingAnim(0.9, 1.18, 1.16, 0.7)
    e "Bah oui ! Je l'ai reniflée et j'ai pas senti son pouls."
    e "Y avait bien une odeur d'oignon séché, mais c'est tout."
    show char_ernust inquiet left at notSpeakingAnim(0.9, 1.18, 1.16, 0.7)
    show char_ingrid choc at speakingAnim(0.15, 1.22, 1.20, 0.25)
    i "Gaufrid, explique toi !"
    show char_ingrid choc at notSpeakingAnim(0.15, 1.22, 1.20, 0.25)
    menu :
        i "{cps=0}Gaufrid, explique toi !{/cps}"
        "J'ai rien fait ! C'est Ernust !":
            jump ending_ErnustPart1
        "Ingrid, je dois t'avouer la vérité..." :
            jump ending_Admit
        "La vrai coupable, c'est la chèvre !" :
            jump ending_ChevrePart1

# -----------------------------------------#
label ending_ChevrePart1 :
    
    play sound "sfx/Voices/Player/Char_Player_Non_02.ogg"
    y "Ne l'écoute pas Ingrid !"
    y "La seule et unique coupable ici, c'est Josiane, la chêvre. J'en suis sûr !"
    show char_goat normal zorder 2:
        xalign 0.5 yalign 0.8
        zoom 0.45 xpos 0.5 ypos 1.5
        easein 0.8 ypos 0.85
    play sound "sfx/Voices/Chevre/Char_Chevre_Choc1_01.ogg"
    goat "Bêêêêêêêêêêêêh !"
    show char_ingrid choc at speakingAnim(0.15, 1.22, 1.20, 0.25)
    i "Josiane ?! Vraiment ?!"
    show char_ingrid choc at notSpeakingAnim(0.15, 1.22, 1.20, 0.25)
    show char_beaudrik choque right zorder 2:
        xalign 0.5 yalign 0.8 zoom 0.8
        xpos -0.2 ypos 0.88
        easein 0.8 xpos 0.2
    show char_ingrid choc:
        linear 0.8 xpos 0.1
    show char_goat normal:
        xpos 0.5
        linear 0.8 xpos 0.6
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Choc_01.ogg"
    bg "Josiane ?! Mais comment t'as pu me faire ça ?!"
    bg "Après tout ce que nous avons vécu ensemble, Josiane !"
    play sound "sfx/Voices/Chevre/Char_Chevre_Love_03.ogg"
    show char_goat choc at speakingAnim(0.6, 0.88, 0.86, 0.45)
    goat "Bêêêêêêêêh..."
    show char_goat choc at notSpeakingAnim(0.6, 0.88, 0.86, 0.45)
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_02.ogg"
    v "Josiane, les faits sont là."
    v "Je n'ai d'autre choix que de vous condamner à l'exil..."
    play sound "sfx/Voices/Chevre/Char_Chevre_Normal_01.ogg"
    show char_goat choc at speakingAnim(0.6, 0.88, 0.86, 0.45)
    goat "Bêêêêêêêêêêh !"
    show char_goat normal at notSpeakingAnim(0.6, 0.88, 0.86, 0.45)
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Humilie_01.ogg"
    show char_beaudrik insulte at speakingAnim(0.18, 0.98, 0.96, 0.8)
    bg "Adieu, Josiane..."
    bg "Mon amie..."

    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5

jump ending_ChevreTrahie
# -----------------------------------------#
label ending_Admit :
    
    y "Ingrid, je dois tout t'avouer..."
    y "Ernust et moi sommes coupables !"
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Choc_01.ogg"
    show char_ingrid choc at speakingAnim(0.15, 1.22, 1.20, 0.25)
    i "Oh ! Mon tout nouveau fiancé !"
    i "Comment as tu pu ? Quelle tristesse !"
    i "Je me suis tellement attachée à toi depuis que tu m'as rapporté un {b}glaive{/b} et un {b}bouclier{/b} !"
    show char_ingrid normal at notSpeakingAnim(0.15, 1.22, 1.20, 0.25)
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_04.ogg"
    v "Gaufrid ! Comment avez vous pu cracher sur nos traditions de la sorte ?"
    v "Votre punition sera..."
    play sound "sfx/SFX_Drama_01.ogg"
    pause 0.5
    v "L'exil !"
    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    
jump ending_ExilPart1
# -----------------------------------------#
label ending_ErnustPart1 :
    
    play sound "sfx/Voices/Player/Char_Player_Non_02.ogg"
    y "J'ai rien fait ! C'est Ernust, le coupable !"
    play sound "sfx/Voices/Ernust/Char_Ernust_Trahi_01.ogg"
    show char_ernust inquiet left at speakingAnim(0.9, 1.18, 1.16, 0.7)
    e "Oh bah... mais... Gaufrid !"
    show char_ernust inquiet left at notSpeakingAnim(0.9, 1.18, 1.16, 0.7)
    show char_ingrid degout at speakingAnim(0.15, 1.22, 1.20, 0.25)
    i "Ernust... il semble pourtant si gentil..."
    show char_ingrid degout at notSpeakingAnim(0.15, 1.22, 1.20, 0.25)
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
    v "Ernust, vous avez tourné en ridicule nos traditions."

    v "C'est avec grand plaisir que nous vous condamnons à..."
    play sound "sfx/SFX_Drama_01.ogg"
    v "L'exil !"
    play sound "sfx/Voices/Ernust/Char_Ernust_Trahi_02.ogg"
    show char_ernust inquiet left at speakingAnim(0.9, 1.18, 1.16, 0.7)
    e "Oh non ! Mais je vais aller où, moi ?"
    show char_ernust inquiet left at notSpeakingAnim(0.9, 1.18, 1.16, 0.7)
    
    
    scene black with Dissolve(1.5)
    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_06.ogg"
    e "Gaufrid... pourquoi ?"


jump ending_ErnustTrahi
# -----------------------------------------#

label ending_ExilPart1 :
    
    y "L'exil !?"
    y "Si je dois partir, je partirai avec mon meilleur ami !"
    show char_ernust love2:
        xalign 0.5 yalign 0.8 zoom 0.7
        xpos 0.88 ypos 1.16
        easeout 0.8 xpos 0.5 zoom 0.72
    pause 0.8
    show char_ernust love2 at speakingAnim(0.5, 1.16, 1.14, 0.72)
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_04.ogg"
    e "Vraiment ?"
    show char_ernust love2 at notSpeakingAnim(0.5, 1.16, 1.14, 0.72)
    menu:
        e "{cps=0}Vraiment ?{/cps}"
        "Oui Ernust, on s'en va !":
            y "Oui Ernust, on s'en va !"
            show char_ernust love2 at speakingAnim(0.5, 1.18, 1.16, 0.72)
            e "Oh bah, Gaufrid... si tu savais comme j'suis content !"
            show char_ernust love2 at notSpeakingAnim(0.5, 1.18, 1.16, 0.72)
            stop music1 fadeout 1.5
            stop ambiance fadeout 0.5
            
            jump ending_ExilAvecErnust
            
        "Allez viens Josiane, on s'en va !":
            y "Viens Josiane, allons découvrir le monde ensemble !"
            show char_goat choc zorder 2:
                xalign 0.5 yalign 0.8
                zoom 0.45 xpos 0.75 ypos 1.5
                easein 0.8 ypos 0.85
            pause 0.8
            show char_goat choc at speakingAnim(0.75, 0.88, 0.86, 0.45)
            play sound "sfx/Voices/Chevre/Char_Chevre_Heureux_03.ogg"
            goat "Bêêêêêêêêêêh ?"
            show char_goat choc at notSpeakingAnim(0.75, 0.88, 0.86, 0.45)
            stop music1 fadeout 1.5
            stop ambiance fadeout 0.5
            show char_ernust inquiet left at speakingAnim(0.5, 1.18, 1.16, 0.7)
            play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_04.ogg"
            e "Mais... Gaufrid ?"
            show char_ernust inquiet left at notSpeakingAnim(0.5, 1.18, 1.16, 0.7)
            jump ending_ExilAvecChevre