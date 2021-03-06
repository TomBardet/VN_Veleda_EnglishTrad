﻿################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
    


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.0
    ypos 0.84
    yanchor 1.0
    
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Nouveau"):
                text_font "gui/ardagh.ttf"
                text_size 45
                text_idle_color "#0F0B0A"
                text_hover_color "#B1991E"
                action Start()
            
        else:

           # textbutton _("History") action ShowMenu("history")

            textbutton _("Sauver"):
                text_font "gui/ardagh.ttf"
                text_size 45
                text_idle_color "#0F0B0A"
                text_hover_color "#B1991E"
                action ShowMenu("save")

        textbutton _("Charger"):
            text_font "gui/ardagh.ttf"
            text_size 45
            text_idle_color "#0F0B0A"
            text_hover_color "#B1991E"action ShowMenu("load")

       # textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Menu"):
                text_font "gui/ardagh.ttf"
                text_size 45
                text_idle_color "#0F0B0A"
                text_hover_color "#B1991E"
                action MainMenu()

       # textbutton _("About") action ShowMenu("about")

      #  if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
          #  textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
         #   textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")



## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu
image main_menu = Movie(size=None, channel="main_menu", play="gui/Splashscreen.webm")
image title_menu = "gui/title.png"
image button_menu = "gui/buttonMenu.png"
screen main_menu:
    tag menu
    add "main_menu"
    add "title_menu":
        zoom 0.32 xalign 0.5 xpos 0.47
    add "button_menu":
        zoom 0.11 xalign 0.5 yalign 0.5
        xpos 0.33 ypos 0.67
    add "button_menu":
        zoom 0.11 xalign 0.5 yalign 0.5
        xpos 0.41 ypos 0.78
    add "button_menu":
        zoom 0.11 xalign 0.5 yalign 0.5
        xpos 0.49 ypos 0.89
    textbutton _("Jouer"):
        xanchor 0.5
        xpos 0.33
        yanchor 0.5
        ypos 0.67
        text_idle_color gui.actionButton_colorIdle
        text_hover_color "#f2de5c"
       # text_outlines [(2,"#000000")]
        text_font "gui/ardagh.ttf"
        text_size 45
        action Start()
    textbutton _("Charger"):
        xanchor 0.5
        xpos 0.41
        yanchor 0.5
        ypos 0.78
        text_idle_color gui.actionButton_colorIdle
        text_hover_color "#f2de5c"
       # text_outlines [(2,"#000000")]
        text_font "gui/ardagh.ttf"
        text_size 45
        action ShowMenu("load")
    textbutton _("Quitter"):
        xanchor 0.5
        xpos 0.49
        yanchor 0.5
        ypos 0.89
        text_idle_color gui.actionButton_colorIdle
        text_hover_color "#f2de5c"
      #  text_outlines [(2,"#000000")]
        text_font "gui/ardagh.ttf"
        text_size 45
        action Quit(confirm=not main_menu)

screen main_menu_old():
    ## This ensures that any other menu screen is replaced.
    tag menu
    
    style_prefix "main_menu"
    add "movie_bg"
   # add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

   # background "gui/overlay/game_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")
    #outlines [(2, "#67d7cb")]
    color "#ffffff"
    size 35

style main_menu_version:
    properties gui.text_properties("version")
    color "#ffffff"
    size 20

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        xpos 0.032
        ypos 0.7
        text_font "gui/ardagh.ttf"
        text_size 45
        text_idle_color "#0F0B0A"
        text_hover_color "#B1991E"
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Sauvegarder"))


screen load():

    tag menu

    use file_slots(_("Charger"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "disable")
                    textbutton _("Right") action Preference("rollback side", "disable")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
    
    
###################################################################################################
#################### - INVENTORY SCREENS - ########################################################


#screen inventory_button(bool = True):
 #   zorder 5
 #   add "gui/toolTip.png" xalign 0.5 xpos 0.5 ypos 0.85 #at inv_fadeIn # bottom black bar
    #add "gui/toolTip.png" xalign 0.5 xpos 0.5 ypos 0.0 at inv_fadeIn # top black bar
 #   if(bool):
  #      imagebutton idle "images/backpack_idle.png" hover "images/backpack_hover.png" action [Hide("inventory_button"), Show("inventory_screen")] align (.97,.06) at inv_button
 #   else:
  #      imagebutton idle "images/backpack_idle.png" hover "images/backpack_hover.png" action [Hide("inventory_button"), Show("inventory_screen")] align (.97,.06) at inv_button2

  #  modal True#prevent clicking on other stuff when inventory is shown
    
screen inventory_screen(obj = ""): 
   # zorder 5
  #  add "gui/toolTip.png" xalign 0.5 xpos 0.5 ypos 0.85 #at inv_fadeIn # bottom black bar
   # add "gui/toolTip.png" xalign 0.5 xpos 0.5 ypos 0.0 #at inv_fadeIn # top black bar
    
   # modal True#prevent clicking on other stuff when inventory is shown
    
    add "images/backpack.png" align (.97,.06) at inv_button
    
    $ x = 1230 # coordinates of the top left item position
    $ y = 125
    $ i = 0
    $ sorted_items = sorted(inventory.items, reverse=True) # we sort the items, so non-consumable items that change elemental damage (guns) are listed first
    $ next_inv_page = inv_page + 1            
    if next_inv_page > int(len(inventory.items)/9):
        $ next_inv_page = 0
    for item in sorted_items:
        $ y += 75
        $ picIdle = item.image
        $ picHover = item.imageHover
     #   $ my_tooltip = "tooltip_inventory_" + picIdle.replace("images/inv_", "").replace(".png", "") # we use tooltips to describe what the item does.
        
        if obj == item.name:
            imagebutton idle picIdle hover picIdle xpos x ypos y action [SetVariable("item", item)] at inv_effGood(x,y)
        else:
            imagebutton idle picIdle hover picIdle xpos x ypos y action [SetVariable("item", item)] at inv_eff(x,y)

        
        $ i += 1
       # if len(inventory.items)>9:
         #   textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")] xpos .475 ypos .83

    
#screen gui_tooltip (my_picture="", my_tt_xpos=0.0, my_tt_ypos=0.0):
#    add my_picture xpos my_tt_xpos ypos my_tt_ypos xalign 0.5 yalign 0.5

###################################################################################################
################ - GESTION DES CHOIX D'ACTIONS - ##################


### ANIM DES CHOIX D'ACTION
transform sineV(y):
    ypos y
    parallel:
        block:
            linear 0.5 ypos y-0.002
            pause 0.1
            linear 0.5 ypos y+0.002
            repeat
    parallel:
        block:
            linear 1.8 rotate -1
            pause 0.1
            linear 1.8 rotate 1
            repeat
            
screen action_choice_placeVillage(lunette=0, glaive=0, bouclier=0):
    zorder 10
    if _testLunettes == 0:
        textbutton _("Etables"):
            xpos 0.82
            xanchor 0.5
            ypos 0.33
            yanchor 0.5
            text_idle_color gui.actionButton_colorIdle
            text_hover_color gui.actionButton_colorHover
            text_outlines [(2,"#000000")]
            text_size 32
            at sineV(0.83)
            action Return("etables")
    if _testBouclier == 0:
        textbutton _("Forge"):
            xpos 0.76
            xanchor 0.5
            ypos 0.55
            yanchor 0.5
            text_idle_color gui.actionButton_colorIdle
            text_hover_color gui.actionButton_colorHover
            text_outlines [(2,"#000000")]
            text_size 32
            at sineV(0.56)
            action Return("forge")
    if _testGlaive == 0:
        textbutton _("Tente romaine"):
            xpos 0.16
            xanchor 0.5
            ypos 0.58
            yanchor 0.5
            text_idle_color gui.actionButton_colorIdle
            text_hover_color gui.actionButton_colorHover
            text_outlines [(2,"#000000")]
            text_size 32
            at sineV(0.64)
            action Return("tente")

screen action_choice_placeVillageFinal:
    zorder 10
    textbutton _("Taverne"):
        xpos 0.5
        xanchor 0.5
        ypos 0.5
        yanchor 0.5
        text_idle_color gui.actionButton_colorIdle
        text_hover_color gui.actionButton_colorHover
        text_outlines [(2,"#000000")]
        text_size 32
        at sineV(0.5)
        action Return("taverne")

screen action_choice_EtableTrumpet:
    zorder 10
    textbutton _("Jouer de la trompette"):
        xpos 0.53
        xanchor 0.5
        ypos 0.35
        yanchor 0.5
        text_idle_color gui.actionButton_colorIdle
        text_hover_color gui.actionButton_colorHover
        text_outlines [(2,"#000000")]
        text_size 30
        at sineV(0.28)
        action Return("trompette")
    textbutton _("Parler aux buffles"):
        xpos 0.22
        xanchor 0.5
        ypos 0.68
        yanchor 0.5
        text_idle_color gui.actionButton_colorIdle
        text_hover_color gui.actionButton_colorHover
        text_outlines [(2,"#000000")]
        at sineV(0.68)
        action Return("buffles")
    textbutton _("Sortir de l'étable"):
        xpos 0.88
        xanchor 0.5
        ypos 0.95
        yanchor 0.5
        text_idle_color gui.actionButton_colorIdle
        text_hover_color gui.actionButton_colorHover
        text_outlines [(2,"#000000")]
        at sineV(0.70)
        action Return("sortir")

screen action_choice_Etable:
    zorder 10
    textbutton _("Parler aux buffles"):
        xpos 0.22
        xanchor 0.5
        ypos 0.4
        yanchor 0.5
        text_idle_color gui.actionButton_colorIdle
        text_hover_color gui.actionButton_colorHover
        text_outlines [(2,"#000000")]
        at sineV(0.68)
        action Return("buffles")
    textbutton _("Parler à Crossfitrichernvald"):
        xanchor 0.5
        xpos 0.53        
        yanchor 0.5
        ypos 150        
        text_idle_color gui.actionButton_colorIdle
        text_hover_color gui.actionButton_colorHover
        text_outlines [(2,"#000000")]
        text_size 30
        at sineV(0.28)
        action Return("crossfit")
    textbutton _("Sortir de l'étable"):
        xanchor 0.5
        xpos 0.88
        yanchor 0.5
        ypos 0.0
        text_idle_color gui.actionButton_colorIdle
        text_hover_color gui.actionButton_colorHover
        text_outlines [(2,"#000000")]
        at sineV(0.70)
        action Return("sortir")
        
screen action_choice_Tente:
    zorder 10
    textbutton _("S'approcher de la tente"):
        xpos 0.6
        xanchor 0.5
        ypos 0.68
        yanchor 0.5
        text_idle_color gui.actionButton_colorIdle
        text_hover_color gui.actionButton_colorHover
        text_outlines [(2,"#000000")]
        text_size 30
        at sineV(0.55)
        action Return("tente")
    textbutton _("Retourner au village"):
        xpos 0.35
        xanchor 0.5
        ypos 0.6
        yanchor 0.5
        text_idle_color gui.actionButton_colorIdle
        text_hover_color gui.actionButton_colorHover
        text_outlines [(2,"#000000")]
        at sineV(0.88)
        action Return("sortir")

screen action_choice_Tente1:
    zorder 10
    textbutton _("Parler aux Romains"):
        xpos 0.85
        xanchor 0.5
        ypos 0.68
        yanchor 0.5
        text_idle_color gui.actionButton_colorIdle
        text_hover_color gui.actionButton_colorHover
        text_outlines [(2,"#000000")]
        at sineV(0.68)
        action Return("tente")
    textbutton _("Retourner au village"):
        xpos 0.25
        xanchor 0.5
        ypos 0.6
        yanchor 0.5
        text_idle_color gui.actionButton_colorIdle
        text_hover_color gui.actionButton_colorHover
        text_outlines [(2,"#000000")]
        at sineV(0.58)
        action Return("sortir")

###################################################################################################
################ - Gestion des Jauges Dating Sim - ##################

screen datingSim(char_name, x, y):
    zorder 7
    
    $ loveValue = char_name.love
    $ loveMax = char_name.max_love
    text _(str(loveValue)+ "/100 {image=images/heart.png}"):
        xpos x
        xanchor 0.0
        ypos y
        yanchor 0.5
        if loveValue < 20:
            outlines[(2, "#390b0b")]
            color "#f23f3f"
        elif loveValue > 80:
            outlines[(2, "#0d390b")]
            color "#72f23f"
        else:
            outlines[(2, "#39340b")]
            color "#f2c63f"
        at apparitionJuicy
transform animFeedbackPos(x,y):
    alpha 1.0 ypos y xpos x #xalign 0.5 yalign 0.5
    linear 1.0 alpha 0.0 ypos y-0.1

transform animFeedbackNeg(x,y):
    alpha 1.0 ypos y xpos x #xalign 0.5 yalign 0.5
    linear 1.0 alpha 0.0 ypos y+0.1
