init -1:
    image bad_img = im.FactorScale("images/ds_bad.png", 0.1)
    image good_img = im.FactorScale("images/ds_neutral.png", 0.1)

init -1 python:
    import renpy.store as store
    import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    from operator import attrgetter # we need this for sorting items

    inv_page = 0 # initial page of teh inventory screen
    item = None
    interlocuteur = None
    lieu = None
    CAactif = False

    class Chara(renpy.store.object):
        def __init__(self, name, love=0,max_love=0):
            self.name=name
            self.max_love=max_love
            self.love=love
        

    
    class Item(store.object):
        def __init__(self, name, player=None,love=0, imageIdle="", imageHover=""):
            self.name = name
            self.player=player # which character can use this item?
            self.love = love # does this item restore love?
            self.image = imageIdle # image file to use for this item
            self.imageHover = imageHover
            

    class Inventory(store.object):
        def __init__(self):
            self.items = []
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)

    def checkInventory(string, value):
        value = 0
        for i in range(0, len(inventory.items)):
            item_name = inventory.items[i].name
            if string == item_name:
                value = 1
    
    def loveGauge(char_name ,loveCount, x, y):
        char_name.love+=loveCount
        if char_name == vel_char:
            x = 0.725
            y = 0.33
        if char_name.love < 0:
            char_name.love=0
        elif char_name.love > char_name.max_love:
            char_name.love=char_name.max_love
        
        if(loveCount>0):
            renpy.show("good_img", at_list=[animFeedbackPos(x,y)])
            renpy.play("/sfx/UI_FEEDBACK_GOOD.ogg", channel = None)
        else:
            renpy.show("bad_img", at_list=[animFeedbackNeg(x,y)])
            renpy.play("/sfx/UI_FEEDBACK_BAD.ogg", channel = None)
    
    def clickSound():
        renpy.play("/sfx/SFX_Drapeau_Fall_01.ogg", channel = None)
    
    style.tooltip_bottom = Style(style.default)
    style.tooltip_bottom.xalign = 0.5
    style.tooltip_bottom.yalign = 0.5
    style.tooltip_bottom.size = 22
    style.tooltip_bottom.italic = True
    

    
    
    showitems = False #turn True to debug the inventory
    def display_items_overlay():
        if showitems:
            inventory_show = "Interlocuteur:" + str(interlocuteur)+ " Love: "+ str(goat_char.love) + " Lieu: " + str(lieu) + "\nCA: " + str(actionChoice)+ " actif?" + str(CAactif) + "\nInventory: "
            for i in range(0, len(inventory.items)):
                item_name = inventory.items[i].name
                if i > 0:
                    inventory_show += ", "
                inventory_show += item_name
            
            ui.frame()
            ui.text(inventory_show, color="#000")
    config.overlay_functions.append(display_items_overlay)
    
transform inv_eff(x,y): 
    zoom 0.25 xanchor 1.0 yanchor 0.5
    alpha 0.0 ypos y-35
    pause 0.5
    linear 0.5 alpha 1.0 ypos y

transform inv_effGood(x,y):
    zoom 0.25 xanchor 1.0 yanchor 0.5
    alpha 0.0 ypos y-35
    pause 0.5
    linear 0.5 alpha 1.0 ypos y
    pause 0.5
    linear 0.6 zoom 0.5 xpos (x-150)
    parallel:
        block:
            linear 0.5 ypos y-5
            pause 0.1
            linear 0.5 ypos y+5
            repeat
    parallel:
        block:
            linear 1.8 rotate -1
            pause 0.1
            linear 1.8 rotate 1
            repeat
            
transform inv_button():
    zoom 0.8 xpos 1.2
    easein 0.5 xpos 0.97
    on idle:
        linear 0.2 zoom 0.8
    on hover:
        linear 0.2 zoom 0.85

transform inv_button2:
    zoom 0.9 ypos 0.06
    easein 0.5 zoom 0.8
    on idle:
        linear 0.2 zoom 0.8
    on hover:
        linear 0.2 zoom 0.85

transform speakingAnim(x, y, yto, zm):
    xalign 0.5 yalign 0.8
    xpos x ypos y zoom zm
    block:
        parallel:
            easein 0.23 ypos yto
            easeout 0.23 ypos y
            repeat
        parallel:
            linear 0.3 rotate -1.5
            linear 0.3 rotate 1.5
            repeat
            
#transform speakingAnim(name):
 #   if name == Brutalmund
  #      block:
   #         xalign 0.5 yalign 0.8
    #        xpos 0.75 ypos 0.92 zoom 0.32
     #       parallel:
      #          easein 0.23 ypos 0.92
       #         easeout 0.23 ypos 0.92
        #        repeat
         #   parallel:
          #      linear 0.3 rotate -1.5
           #     linear 0.3 rotate 1.5
            #    repeat

transform notSpeakingAnim(x, y, yto, zm):
    xalign 0.5 yalign 0.8
    xpos x ypos y zoom zm
        
transform inv_fadeIn:
    alpha 0.0
    linear 0.5 alpha 1.0
    
transform scrollEnding(y, ymax, speed):
    xpos 0.5 ypos y
    linear speed ypos ymax
    
transform apparitionJuicy:
    zoom 2.5
    parallel:
        block:
            easeout 0.3 zoom 1.0
        block:
            ease 0.1 rotate 20
            ease 0.4 rotate -20
            ease 0.2 rotate 0

            
#Tooltips-inventory: Très chiant de régler leur position, du à une restriction de Renpy qui pue un peu. Modifier à la main le 2e paramètres. WARNING : ça prend des plombes

#image tooltip_inventory_swordIdle=LiveComposite((1.0, 1.0), (0.71, 0.88), Text("Un glaive solide et affuté. Il y a écrit sur le pommeau \"made in china\"", style = "tooltip_bottom"))
#image tooltip_inventory_shieldIdle=LiveComposite((1.0,1.0), (0.77, 0.88), Text("Tout guerrier qui se respecte possède un bouclier.", style = "tooltip_bottom" ))
#image tooltip_inventory_jokeIdle=LiveComposite((1.0, 1.0), (0.77, 0.88), Text("Très certainement la blague la plus drôle du monde.", style = "tooltip_bottom" ))
#image tooltip_inventory_glassesIdle=LiveComposite((1.0, 1.0), (0.72, 0.88), Text("Des lunettes, pour mieux voir, ou pour brûler les fourmis. Au choix.", style = "tooltip_bottom" ))

