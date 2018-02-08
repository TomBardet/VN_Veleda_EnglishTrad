#########################################################################################
######################## - Defining Characters - ########################################

init:
    
    define goat = Character("Chêvre : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define y = Character("Gaufrid : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define e = Character("Ernust : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define i = Character("Ingrid : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define v = Character("Véléda : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define brut = Character("Brutalmund : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define cross = Character("Crossfitrichernvald : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"),
        who_size=22,
        who_ypos=0.8)
    
    define bg = Character("Beaudrik : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define num = Character("Numerimus : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define dig = Character("Digitimus : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
 
    define ve = Character("Véléda(Ernust) : ",
        what_suffix=" ",
        #who_size=24,
        ctc=anim.Blink("gui/ctc.png"))

    define nar = Character("Narrateur : ",
        what_italic=True,
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    $ outline = Character(None,
        what_size=32,
        what_color = "#ffffff",
        what_outlines=[(3, "#000000", 0, 0)],
        what_layout="subtitle",
        what_xalign=0.5,
        what_text_align=0.5,
        window_background=None,
        window_yminimum=0,
        window_xfill=True,
        window_xalign=0.5,
        window_yalign=0.5)
    
    $ outlineTop = Character(None,
        what_size=32,
        what_color = "#ffffff",
        what_outlines=[(3, "#000000", 0, 0)],
        what_layout="subtitle",
        what_xalign=0.5,
        what_text_align=0.5,
        window_background=None,
        window_yminimum=0,
        window_xfill=True,
        window_xalign=0.5,
        window_yalign=0.1)
    
    $ outlineBot = Character(None,
        what_size=32,
        what_color = "#ffffff",
        what_outlines=[(3, "#000000", 0, 0)],
        what_layout="subtitle",
        what_xalign=0.5,
        what_text_align=0.5,
        window_background=None,
        window_yminimum=0,
        window_xfill=True,
        window_xalign=0.5,
        window_yalign=0.8,
        window_width=3100)

#########################################################################################
######################## - Defining Images - ############################################

init:
    image temp = "images/inv_sword.png"
    image temp2 = "images/goat_idle.png"
    
    #Les images des Lieux
    image bg_taverneJ = "images/decor/Lieu_taverneJ.png"
    image bg_taverne2J = "images/decor/Lieu_taverne2J.png"
    image bg_taverneN = "images/decor/Lieu_taverneN.png"
    image bg_taverne2N = "images/decor/Lieu_taverne2N.png"
    image bg_taverneFull = "images/decor/Lieu_taverneAll.png"
    image bg_etables = "images/decor/Lieu_etablesBuffles.jpg"
    image bg_etables2 = "images/decor/Lieu_etables.png"
    image bg_forge = "images/decor/Lieu_forge.png"
    image bg_antichambre = "images/decor/Lieu_antichambre.png"
    image bg_chambre = im.FactorScale("images/decor/Lieu_chambre.png", 0.70)
    image bg_chambre_nuit = im.FactorScale("images/decor/Lieu_chambre_nuit.png", 0.70)
    image bg_romains = ("images/decor/Lieu_romains.png")
    image bg_place = im.FactorScale("images/decor/Lieu_place.png", 0.70)
    image bg_tour = im.FactorScale("images/decor/Lieu_tour.png", 0.70)
    image bg_buffles = "images/decor/Lieu_BuffleScene.png"
    #iamges de veleda
    image vel normal = im.FactorScale("images/decor/Lieu_chambre_veleda.png", 0.70)
    image vel normal2 = im.FactorScale("images/decor/Lieu_chambre_veleda2.png", 0.70)
    image vel morte = im.FactorScale("images/decor/Lieu_chambre_veledaMorte.png", 0.70)
    image vel mario = im.FactorScale("images/decor/Lieu_chambre_veledaMarionnette.png", 0.70)
    image vel mario2 = im.FactorScale("images/decor/Lieu_chambre_veledaMarionnette2.png", 0.70)
    image vel normal_nuit = im.FactorScale("images/decor/Lieu_chambre_veleda_nuit.png", 0.70)
    image vel morte_nuit = im.FactorScale("images/decor/Lieu_chambre_veledaMorte_nuit.png", 0.70)
    image vel mario_nuit = im.FactorScale("images/decor/Lieu_chambre_veledaMarionnette_nuit.png", 0.70)
    image vel normal2_nuit = im.FactorScale("images/decor/Lieu_chambre_veleda2_nuit.png", 0.70)
    image vel mario2_nuit = im.FactorScale("images/decor/Lieu_chambre_veledaMarionnette2_nuit.png", 0.70)
    
    #Intro
    image introCarte = im.FactorScale("images/intro/intro_map.png", 0.35)
    image introFlag = im.FactorScale("images/intro/intro_flag.png", 0.55)
    image introCrack = im.FactorScale("images/intro/intro_crack.png", 0.45)
    image introPoint = im.FactorScale("images/intro/intro_cross.png", 0.35)
    
    #Ending
    image endingTemp = "images/ending.png"
    
    image endBro01 = "images/endings/END_Brotrip_01.png"
    image endBro02 = "images/endings/END_Brotrip_02.png"
    image endBro03 = "images/endings/END_Brotrip_03.png"
    image endBro04 = "images/endings/END_Brotrip_04.png"
    image endBroKey = "images/endings/END_Brotrip_Key.png"
    
    image endBad01 = "images/endings/END_Badass_01.png"
    image endBad02 = "images/endings/END_Badass_02.png"
    image endBad03 = "images/endings/END_Badass_03.png"
    image endBad04 = "images/endings/END_Badass_04.png"
    image endBadKey = "images/endings/END_Badass_Key.png"
    
    image endGoat01 = "images/endings/END_Goatrip_01.png"
    image endGoat02 = "images/endings/END_Goatrip_02.png"
    image endGoat03 = "images/endings/END_Goatrip_03.png"
    image endGoat04 = "images/endings/END_Goatrip_04.png"
    image endGoatKey = "images/endings/END_Goatrip_Key.png"
    
    image endSad01 = "images/endings/END_Sad_01.png"
    image endSad02 = "images/endings/END_Sad_02.png"
    image endSad03 = "images/endings/END_Sad_03.png"
    image endSad04 = "images/endings/END_Sad_04.png"
    image endSadKey = "images/endings/END_Sad_Key.png"
    
    #Items
    image img_bag = "images/backpack.png"
    image img_glaive = "images/inv_swordIdle.png"
    image img_bouclier = "images/inv_shieldIdle.png" 
    image img_blague = "images/inv_jokeIdle.png"
    image img_lunettes = "images/inv_glassesIdle.png"
    image img_trompette = "images/inv_trumpetidle.png"
    
    #------ Les images des Personnages -------
    
    #Left ou Right correspond au sens dans lequel regarde le personnage#
    
    #Véléda
    image char_veleda normal = "images/char/Char_veleda_normal.png"
    image char_veleda morte = "images/char/Char_veleda_morte.png"
    image char_veleda marionnette = "images/char/Char_veleda_marionnette.png"
    
    #Véléda(Ernust)
    image char_veledaernust 01 = "images/char/Char_veledaernust_01.png"
    image char_veledaernust 02 = "images/char/Char_veledaernust_02.png"
    
    #Ernust
    image char_ernust normal left = "images/char/Char_ernust_normal.png"
    image char_ernust normal right = im.Flip("images/char/Char_ernust_normal.png", horizontal = True)
    image char_ernust joyeux left = "images/char/Char_ernust_joyeux.png"
    image char_ernust joyeux right = im.Flip("images/char/Char_ernust_joyeux.png", horizontal = True)
    image char_ernust love1 = "images/char/Char_ernust_love1.png"
    image char_ernust love2 = "images/char/Char_ernust_love2.png"
    image char_ernust marionnette1 = "images/char/Char_ernust_marionnette1.png"
    image char_ernust marionnette2 = "images/char/Char_ernust_marionnette2.png"
    image char_ernust trahi = "images/char/Char_ernust_trahi.png"
    image char_ernust inquiet = "images/char/Char_ernust_inquiet.png"
    
    #Ingrid
    image char_ingrid normal = "images/char/Char_ingrid_normal.png"
    image char_ingrid degout = "images/char/Char_ingrid_degout.png"
    image char_ingrid love = "images/char/Char_ingrid_love.png"
    image char_ingrid choc = "images/char/Char_ingrid_choc.png"
    
    #Crossfit
    image char_crossfit colere = "images/char/Char_Crossfit_Colere_02.png"
    image char_crossfit colereG = "images/char/Char_Crossfit_Colere_01.png"
    image char_crossfit serieux = "images/char/Char_Crossfit_Serieux_02.png"
    image char_crossfit serieuxG = "images/char/Char_Crossfit_Serieux_01.png"
    image char_crossfit inquiet = "images/char/Char_Crossfit_Inquiet_02.png"
    image char_crossfit inquietG = "images/char/Char_Crossfit_Inquiet_01.png"
    image char_crossfit pleurs = "images/char/Char_Crossfit_Pleurs_02.png"
    image char_crossfit pleursG = "images/char/Char_Crossfit_Pleurs_01.png"
    image char_crossfit choc = "images/char/Char_Crossfit_Choc_02.png"
    image char_crossfit chocG = "images/char/Char_Crossfit_Choc_01.png"
    
    image char_crossfit colere right = im.Flip("images/char/Char_Crossfit_Colere_02.png", horizontal = True)
    image char_crossfit colereG right = im.Flip("images/char/Char_Crossfit_Colere_01.png", horizontal = True)
    image char_crossfit serieux right = im.Flip("images/char/Char_Crossfit_Serieux_02.png", horizontal = True)
    image char_crossfit serieuxG right = im.Flip("images/char/Char_Crossfit_Serieux_01.png", horizontal = True)
    image char_crossfit inquiet right = im.Flip("images/char/Char_Crossfit_Inquiet_02.png", horizontal = True)
    image char_crossfit inquietG right = im.Flip("images/char/Char_Crossfit_Inquiet_01.png", horizontal = True)
    image char_crossfit pleurs right = im.Flip("images/char/Char_Crossfit_Pleurs_02.png", horizontal = True)
    image char_crossfit pleursG right = im.Flip("images/char/Char_Crossfit_Pleurs_01.png", horizontal = True)
    image char_crossfit choc right = im.Flip("images/char/Char_Crossfit_Choc_02.png", horizontal = True)
    image char_crossfit chocG right = im.Flip("images/char/Char_Crossfit_Choc_01.png", horizontal = True)

    
    #Brutalmund
    image char_brutal normal = "images/char/Char_brutal_normal.png"
    image char_brutal colere = "images/char/Char_brutal_colere.png"
    image char_brutal heureux = "images/char/Char_brutal_heureux.png"
    image char_brutal surpris = "images/char/Char_brutal_surpris.png"
    
    #Beaudrik
    image char_beaudrik mepris left = "images/char/Char_beaudrik_mepris.png"
    image char_beaudrik drague left = "images/char/Char_beaudrik_drague.png"
    image char_beaudrik insulte left = "images/char/Char_beaudrik_insulte.png"
    image char_beaudrik normal left = "images/char/Char_beaudrik_normal.png"
    image char_beaudrik choque right = "images/char/Char_beaudrik_surpris.png"
    image char_beaudrik mepris right = im.Flip("images/char/Char_beaudrik_mepris.png", horizontal = True)
    image char_beaudrik drague right = im.Flip("images/char/Char_beaudrik_drague.png", horizontal = True)
    image char_beaudrik insulte right = im.Flip("images/char/Char_beaudrik_insulte.png", horizontal = True)
    image char_beaudrik normal right = im.Flip("images/char/Char_beaudrik_normal.png", horizontal = True)
    image char_beaudrik choque left = im.Flip("images/char/Char_beaudrik_surpris.png", horizontal = True)
    image char_beaudrik mepris2 left = "images/char/Char_Beaudrik_Mepris_02.png"
    image char_beaudrik mepris2 right = im.Flip("images/char/Char_Beaudrik_Mepris_02.png", horizontal = True)
    
    #Numerimus
    image char_numerimus normal = "images/char/Char_numerimus_normal.png"
    image char_numerimus heureux = "images/char/Char_numerimus_heureux.png"
    image char_numerimus dubitatif = "images/char/Char_numerimus_dubitatif.png"
    image char_numerimus normal lunette = "images/char/Char_numerimus_normal_lunette.png"
    image char_numerimus heureux lunette = "images/char/Char_numerimus_heureux_lunette.png"
    image char_numerimus dubitatif lunette = "images/char/Char_numerimus_dubitatif_lunette.png"
    
    #Digitimus
    image char_digitimus normal right = "images/char/Char_digitimus_normal_right.png"
    image char_digitimus rire right = "images/char/Char_digitimus_rire_right.png"
    image char_digitimus normal left = "images/char/Char_digitimus_normal_left.png"
    image char_digitimus rire left = "images/char/Char_digitimus_rire_left.png"

    
    #Chêvre-Josiane
    image char_goat normal = "images/char/Char_goat_normal.png"
    image char_goat love = "images/char/Char_goat_love.png"
    image char_goat choc = "images/char/Char_goat_choc.png"
    
    #foule
    image char_foule normal = "images/char/Char_foule_normal.png"
    image char_foule colere = "images/char/Char_foule_colere.png"
    
    ##PROTO ASSETS
    image bg_bar = "images/bg_bar.png"
    image bg_blackscreen = "images/bg_blackscreen.png"
    image goat = "images/goat_idle.png"
    image bg_champ = "images/bg_champs.png"
    image bg_blacksmith = "images/bg_blacksmith.jpg"
    image bg_house = "gui/menu_bg.jpg"
    image bg_map = "images/bg_map.png"
    
#########################################################################################
######################## - Defining Sounds & Musics - ###################################

    # MUSIC
   # music etable01 = "game/music/MUSIC_Etable_Normale.ogg"
   
    #CHANNELS
    $renpy.music.register_channel("music1", mixer=None, loop=None, stop_on_mute=True, tight=True, buffer_queue=True, movie=False)
    $renpy.music.register_channel("music2", mixer=None, loop=None, stop_on_mute=True, tight=True, buffer_queue=True, movie=False)
    $renpy.music.register_channel("ambiance", mixer=None, loop=None, stop_on_mute=True, tight=True, buffer_queue=True, movie=False)
    $renpy.music.register_channel("endings", mixer=None, loop=None, stop_on_mute=True, tight=True, buffer_queue=True, movie=False)
    

