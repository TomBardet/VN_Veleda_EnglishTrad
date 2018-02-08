#######################################################################
######### - Le Check de l'objet qu'on utilise - #######################

label Obj_use (obj = "none", objUser = "none"):
    if objUser == interlocuteur :
        if obj == "glaive":
            jump useGlaiveSuccess
        elif obj == "bouclier":
            jump useBouclierSuccess
        elif obj == "blague":
            jump useBlagueSuccess
        elif obj == "lunettes" :
            jump useLunettesSuccess
        else:
            "erreur pas d'objet sélectionné - Success"
    else :                          # Ecrire ici les conditions d'échec d'objet, on peut en faire pour chaque interlocuteur ! faut en profiter
        if obj == "glaive" :
            y "Je suis pas certain qu'un glaive puisse me servir dans cette situation"
        elif obj == "bouclier":
            y "J'utiliserai le bouclier si on m'attaque, mais je me sens pas vraiment en danger là"
        elif obj == "blague" :
            y "Je pourrais pas dire pourquoi, mais je sens que ce n'est pas le bon moment pour faire une blague..."
        elif obj == "lunettes" :
            y "Je ne vois pas en quoi des lunettes me seraient utiles dans cette situation"
        else:
            "erreur pas d'objet sélectionné - Failed"
    call screen inventory_screen
    
label useGlaiveSuccess:
    narration "success"
    jump start
label useBouclierSuccess:
    narration "success"
    jump start
label useBlagueSuccess:
    hide screen inventory_screen
    narration "Héhé, tout le monde sait que chêvre qui rit, à moitié dans son lit !"
    y "Dis, tu connais l'histoire du goth, de l'ostrogoth et du wisogoth qui vont au cirque ?"
    hide screen datingSim
    show bg_blackscreen with Dissolve(2.0)
    c "Bêêêêêêêêêêêêêhêhêh"
    narration "Et c'est ainsi que la chêvre, séduite par ton humour"
    narration "Succomba des suite d'une crise de fou rire aigüe"
    narration "C'est triste mais c'est comme ça."
    narration "Fin."
    narration "..."
    narration "..........."
    narration "......................................................."
    narration "Non pour de vrai c'est fini, vous pouvez partir"
    narration "Genre, là le jeu est censer retourner sur le menu en fait"
    narration "Veuillez excusez les développeurs, il semblerait qu'il y ait un incident technique"
    narration "C'est étrange ça marche super bien d'habitude"
    narration "J'ai vraiment pas de chance aujo-"
    return
label useLunettesSuccess:
    narration "success"
    jump start