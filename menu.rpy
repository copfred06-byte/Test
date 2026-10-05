screen roommenu:
    $ rng = renpy.random.randint(1,3)
    zorder -1
    if daytime >= 3:
        add "images/ui/roommenu/DARK_BEDROOM_background.png"
    else:
        add "images/ui/roommenu/LIGHT_BEDROOM_background.png"

    #LAPTOP BUTTON
    if (streamergirlunlock == 1 and daytime == 3 and leannestage11event2 == 1) or (leannestage12event2 == 0 and daytime == 3) or (leannestage11event4 == 1 and leannestage11event2 == 0):
        imagebutton:
            focus_mask True
            auto "images/ui/roommenu/LAPTOP_%s.png"
            if teacher.stage >= 17 and marie.stage >= 8 and luna.stage >= 11 and leanne.stage >= 13 and leannestage13event2 == 0 and katrine.stage >= 10 and lisa.stage >= 11 and amber.stage >= 9 and trista.stage >= 10 and bonnie.stage >= 11 and maya.stage >= 9:
                action Jump("laptopmenu")
            elif leanne_stats_visible == 0:
                action [SetVariable("phoneMessages", False), Jump("leanne_introduction")]
            elif leannestage11event4 == 1 and leannestage11event2 == 0:
                action [SetVariable("phoneMessages", False), Jump("Leanne_Stage_11_Event_4")]
            elif leanne.stage <= 11 and leannestage11event2 == 1:
                action [SetVariable("phoneMessages", False), Jump("leanne_stream")]
            elif leanne.stage >= 12 and leannechoice == 1 and leannestage12event3 == 0:
                if leanne.stage >= 13 and leannestage13event == 0:
                    if rng == 1:
                        action [SetVariable("phoneMessages", False), Jump("lyn_stream")]
                    elif rng == 2:
                        action [SetVariable("phoneMessages", False), Jump("lyn_soda_stream")]
                    elif rng == 3:
                        action [SetVariable("phoneMessages", False), Jump("lyn_sugar_shop_stream")]
                else:
                    action [SetVariable("phoneMessages", False), Jump("lyn_stream")]
            elif leanne.stage >= 12 and leannechoice == 2 and leannestage12event3 == 0:
                if leanne.stage >= 13 and leannestage13event == 0:
                    if rng == 1:
                        action [SetVariable("phoneMessages", False), Jump("leanne_stream2")]
                    elif rng == 2:
                        action [SetVariable("phoneMessages", False), Jump("leanne_soda_stream")]
                    elif rng == 3:
                        action [SetVariable("phoneMessages", False), Jump("leanne_bunny_bites_stream")]
                else:
                    action [SetVariable("phoneMessages", False), Jump("leanne_stream2")]
            elif leanne.stage >= 12 and leannestage12event2 == 0 and leannestage12event3 == 1:
                action [SetVariable("phoneMessages", False), Jump("Leanne_Stage_12_Event_3")]

    #MIRROR BUTTON
    if charisma <= 6:
        imagebutton:
            focus_mask True
            auto "images/ui/roommenu/MIRROR_%s.png"
            action [SetVariable("phoneMessages", False), Jump("charisma_train")]

    #DOOR BUTTON
    imagebutton:
        focus_mask True
        auto "images/ui/roommenu/DOOR_%s.png"
        action [SetVariable("phoneMessages", False), Call("city")]

    #BOOK BUTTON
    if booksheld >= 1:
        imagebutton:
            focus_mask True
            auto "images/ui/roommenu/BOOK_%s.png"
            action [SetVariable("phoneMessages", False), SetVariable("bookday", 0), Jump("book_read_home")]

    #PILLOW BUTTON
    if teacherstage3event == 0:
        imagebutton:
            focus_mask True
            auto "images/ui/roommenu/PILLOW_%s.png"
            action [SetVariable("phoneMessages", False), Jump("goodtimes")]
    
    #PHONE BUTTON
    if leanne.stage >= 11 and leannestage11event2 == 0 and leannestage11event3 == 1 and daytime == 2:
        imagebutton:
            focus_mask True
            auto "images/ui/roommenu/PHONE_%s.png"
            action [SetVariable("phoneMessages", False), Jump("Leanne_Stage_11_Event_3")]
    elif haristage2event == 0 and haristage2event2 == 1 and hari.stage >= 2 and day >= 6:
        imagebutton:
            focus_mask True
            auto "images/ui/roommenu/PHONE_%s.png"
            action [SetVariable("phoneMessages", False), Jump("Hari_Stage_2_Event_2")]
    elif haristage4event2 == 0 and haristage4event3 == 1 and hari.weight >= 71 and day >= 6:
        imagebutton:
            focus_mask True
            auto "images/ui/roommenu/PHONE_%s.png"
            action [SetVariable("phoneMessages", False), Jump("Hari_Stage_4_Event_3")]
    elif cayenne.stage >= 2 and daisycayennetutorintro == 0 and cayennestage1event5 == 0 and daytime == 2 and cayennestage2event == 1:
        imagebutton:
            focus_mask True
            auto "images/ui/roommenu/PHONE_%s.png"
            action [SetVariable("phoneMessages", False), Jump("Cayenne_Stage_2_Event")]

screen citymenu:
    zorder -1
    add "images/ui/citymenu/CITY_background.png"
    #add "images/ui/citymenu/bottom.png"
    #add "images/ui/citymenu/shadow.png"

    #UNIVERSITY BUTTON
    if daytime == 2:
        imagebutton:
            focus_mask True
            if renpy.variant("android"):
                idle "images/ui/citymenu/UNIVERSITY_phone.png"
            else:
                auto "images/ui/citymenu/UNIVERSITY_%s.png"
            action [SetVariable("phoneMessages", False), Jump("library")]

    #HOSPITAL BUTTON
    if (nataliestage3event == 0 and nataliemilkcheck == 1) or (brittastage4event == 0 and brittamilkcheck == 1):
        imagebutton:
            focus_mask True
            if renpy.variant("android"):
                idle "images/ui/citymenu/HOSPITAL_phone.png"
            else:
                auto "images/ui/citymenu/HOSPITAL_%s.png"
            action [SetVariable("phoneMessages", False), Jump("hospital")]

    #CITY CENTER BUTTON
    if daytime == 2 or (lisastage0event == 0 and worked_today == 0) or (cayenne.stage >= 3 and cayennestage2event == 0 and cayenneleave == 0 and daytime == 2):
        imagebutton:
            focus_mask True
            if renpy.variant("android"):
                idle "images/ui/citymenu/CITY_CENTER_phone.png"
            else:
                auto "images/ui/citymenu/CITY_CENTER_%s.png"
            action Jump("citycentermenu")

    #HOUSES BUTTON
    imagebutton:
        focus_mask True
        if renpy.variant("android"):
            idle "images/ui/citymenu/HOUSES_phone.png"
        else:
            auto "images/ui/citymenu/HOUSES_%s.png"
        action Jump("housesmenu")

    #MALL BUTTON
    if leanne.stage >= 3 and leannestage3event == 1 and daytime == 2:
        imagebutton:
            focus_mask True
            if renpy.variant("android"):
                idle "images/ui/citymenu/Mall_phone.png"
            else:
                auto "images/ui/citymenu/MALL_%s.png"
            action Jump("mallmenu")

    #BEACH BUTTON
    if (mayastage1event2 == 0 and mayastage4event4 == 1 and daytime == 3) or (mayastage6event == 0 and daytime == 3):
        imagebutton:
            focus_mask True
            if renpy.variant("android"):
                idle "images/ui/citymenu/Beach_phone.png"
            else:
                auto "images/ui/citymenu/Beach_%s.png"
            action Jump("beachmenu")

    #RETURN BUTTON
    imagebutton:
        focus_mask True
        auto "images/ui/citymenu/RETURN_%s.png"
        action Jump("freetime")

label laptopmenu:
    image DARK_BEDROOM = "/ui/roommenu/DARK_BEDROOM_background.png"
    scene DARK_BEDROOM
    menu:
        "Watch [Lynname]'s livestream." if streamergirlunlock == 1 and daytime == 3 and leanne_stats_visible == 1:
            $ phoneMessages = False
            if leanne.stage <= 11 and leannestage11event2 == 1:
                jump leanne_stream
            elif leanne.stage >= 12 and leannechoice == 1 and leannestage12event3 == 0:
                if leanne.stage >= 13 and leannestage13event == 0:
                    $ rng = renpy.random.randint(1,3)
                    if rng == 1:
                        jump lyn_stream
                    elif rng == 2:
                        jump lyn_soda_stream
                    elif rng == 3:
                        jump lyn_sugar_shop_stream
                else:
                    jump lyn_stream
            elif leanne.stage >= 12 and leannechoice == 2 and leannestage12event3 == 0:
                if leanne.stage >= 13 and leannestage13event == 0:
                    $ rng = renpy.random.randint(1,3)
                    if rng == 1:
                        jump leanne_stream2
                    elif rng == 2:
                        jump leanne_soda_stream
                    elif rng == 3:
                        jump leanne_bunny_bites_stream
                else:
                    jump leanne_stream2
            elif leanne.stage >= 12 and leannestage12event2 == 0 and leannestage12event3 == 1:
                jump Leanne_Stage_12_Event_3
            else:
                "The webpage shows you that this user is banned from streaming."
                pc "FeelsBadMan"
                jump freetime

        "Watch Mira's livestream." if leannestage11event4 == 1 and leannestage11event2 == 0 and daytime == 3:
            $ phoneMessages = False
            if leannestage11event4 == 1:
                jump Leanne_Stage_11_Event_4
            #elif leannestage11event5 == 1 and leannestage11event4 == 0:
            #    jump Leanne_Stage_11_Event_5
            #elif leannestage11event6 == 1 and leannestage11event5 == 0:
            #    jump Leanne_Stage_11_Event_6
            #elif leannestage11event7 == 1 and leannestage11event6 == 0:
            #    jump Leanne_Stage_11_Event_7
            #elif leannestage11event8 == 1 and leannestage11event7 == 0:
            #    jump Leanne_Stage_11_Event_8

        "Watch the special costume contest stream." if teacher.stage >= 17 and marie.stage >= 8 and luna.stage >= 11 and leanne.stage >= 13 and leannestage13event2 == 0 and katrine.stage >= 10 and lisa.stage >= 11 and amber.stage >= 9 and trista.stage >= 10 and bonnie.stage >= 11 and maya.stage >= 9:
            $ phoneMessages = False
            call Halloween_Event
            jump freetime

        


label housesmenu:
    image CITY_MENU = "/ui/citymenu/CITY_background.png"
    scene CITY_MENU
    menu:
        "Go for a walk." if katrine_stats_visible == 0 and daytime == 2:
            $ phoneMessages = False
            jump katrine_intro_outside

        "Visit Daisy." if teacher.stage >= 8 and teacherstage8event == 0 and daytime == 2:
            $ phoneMessages = False
            if teacherstage12event == 1 and teacher.stage >= 12:
                jump Teacher_Stage_12_Event
            jump daisy_home

        "Go to the gym.":
            $ phoneMessages = False
            play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
            if katrinestage1event == 0 and tristastage1event == 1:
                call Trista_Stage_1_Event
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif gymunlock == 0:
                call trista_introduction
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif katrinestage2event == 0 and tristastage2event == 1 and trista.stage >= 2:
                call Trista_Stage_2_Event
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif katrinestage3event == 0 and tristastage3event == 1 and trista.stage >= 3:
                call Trista_Stage_3_Event
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif katrinestage1event == 1 and katrineintroduction == 0:
                call Katrine_Stage_1_Event
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif katrinestage9event == 1 and katrine.stage >= 9 and trista.stage >= 9 and tristastage8event == 0:
                call Katrine_Stage_9_Event
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif teacherstage9event2 == 1 and teacher.stage >= 9 and teacherstage9event == 0:
                call Teacher_Stage_9_Event_2
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif marie.stage >= 6 and mariestage6event == 1:
                call Marie_Stage_6_Event_1
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif katrine_stats_visible == 1:
                $ populateGym()
                if gymBench != False or gymLeftW != False or gymRightW != False or gymLeftT != False or gymRightT != False or gymStand != False:
                    call screen gymmenu
                    if teacher.stage >= 8:
                        scene gym
                        $ populateGym()
                        if gymBench != False or gymLeftW != False or gymRightW != False or gymLeftT != False or gymRightT != False or gymStand != False:
                            if trista.stage >= 10:
                                image trista_gym_shop1 = "/trista/[trista.stage]/gym_shop1.webp"
                                scene trista_gym_shop1
                                "You take a small break by getting a drink from Trista."
                                image trista_gym_shop2 = "/trista/[trista.stage]/gym_shop2.webp"
                                scene trista_gym_shop2
                                window hide
                                pause
                            else:
                                image trista_gym_shop = "/trista/[trista.stage]/gym_shop.webp"
                                scene trista_gym_shop
                                "You take a small break by getting a drink from Trista."
                            "A bit later you notice another familiar face."
                            call screen gymmenu
                        else:
                            scene gym
                            "Looks like there's nobody else here."
                            "You work out for a bit on your own."
                            call strengthup
                            "You take a quick shower and head home."
                else:
                    scene gym
                    "You go to the gym."
                    "It doesn't look like anyone else is here today."
                    "You work out for a bit on your own."
                    call strengthup
                    "You take a quick shower and head home."
                $ daytime += 1
                stop music fadeout 1.0
                if teacherstage6event2 == 1 and teacher.stage >= 6 and teacher_gym_today == 0 and teacherstage6event == 1 and katrine_gym_today == 0:
                    call Teacher_Stage_6_Event_2
                jump freetime

            else:
                scene gym
                "You workout for a bit."
                $ strength += 1
                "Strength increased by one point"
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

        "Return":
            call screen citymenu


label mallmenu:
    image CITY_MENU = "/ui/citymenu/CITY_background.png"
    scene CITY_MENU
    menu:
        "Go to the Anime Store." if leanne.stage >= 3 and leannestage3event == 1 and daytime == 2:
            $ phoneMessages = False
            jump Leanne_Stage_3_Event

        "Return":
            call screen citymenu


label beachmenu:
    image CITY_MENU = "/ui/citymenu/CITY_background.png"
    scene CITY_MENU
    menu:
        "Go to Velvet Shadows." if mayastage1event2 == 0 and mayastage4event4 == 1 and daytime == 3:  
            if mayastage4event3 == 1 and mayastage4event2 == 0:
                $ phoneMessages = False
                jump Maya_Stage_4_Event_3
            elif mayastage4event4 == 1 and mayastage4event3 == 0:
                $ phoneMessages = False
                jump Maya_Stage_4_Event_4
            else:
                $ phoneMessages = False
                jump Maya_Poledance

        "Go to The Curvy Corner." if mayastage6event == 0 and daytime == 3:
            $ phoneMessages = False
            jump Maya_Poledance

        "Return":
            call screen citymenu

label citycentermenu:
    image CITY_MENU = "/ui/citymenu/CITY_background.png"
    scene CITY_MENU
    menu:
        "Go to The Sugar Shop." if daytime == 2:
            $ phoneMessages = False
            jump sugarshop

        "Go to Bunny Bites." if workunlock == 0 and daytime == 2:
            $ phoneMessages = False
            jump bbintro

        "Visit Cayenne at her home." if cayenne.stage >= 3 and cayennestage2event == 0 and cayenneleave == 0 and daytime == 2:
            $ phoneMessages = False
            if cayennestage2event == 0 and cayennestage3event == 1 and cayenne.stage >= 3:
                jump Cayenne_Stage_3_Event
            elif cayennestage3event == 0 and cayennestage4event == 1 and cayenne.stage >= 4:
                jump Cayenne_Stage_4_Event
            elif cayennestage4event == 0 and cayennestage5event == 1 and cayenne.stage >= 5:
                jump Cayenne_Stage_5_Event
            elif cayennestage5event == 0 and cayennestage6event == 1 and cayenne.stage >= 6:
                jump Cayenne_Stage_6_Event
            elif cayennestage7event == 0 and cayennestage8event == 1 and cayenne.stage >= 8:
                jump Cayenne_Stage_8_Event
            else:
                jump Cayenne_Home

        "Go to work." if lisastage0event == 0 and worked_today == 0:
            $ phoneMessages = False
            if mariestage1event == 1 and lisastage0event == 0:
                #SECOND DAY WITH LISA(MARIE STAGE 1 EVENT)
                "You go to your work."
                play music "/music/bunny_bites.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                $ rngworkgirl = 3
                if daytime == 1:
                    call work_arrive_weekend
                else:
                    call work_arrive
                    "You start working the counter."
                call work_randomizer
                call Marie_Stage_1_Event_1
                "A while later."
                call work_randomizer
                "You work your ass off for the rest of your shift."
                $ money += 10
                "You earned ten dollars."
                "After a while, someone finally arrives to take over your shift."
                call work_leave
                $ daytime += 1
                $ worked_today = 1
                stop music fadeout 1.0
                jump freetime

            $ rngworkgirl = renpy.random.randint(1,3)
            if katrineintroduction == 1 and katrine_stats_visible == 1:
                play music "/music/bunny_bites.ogg" if_changed
                call Katrine_Introduction
                $ daytime += 1
                $ worked_today = 1
                jump freetime
            if lisastage1event == 1 and lisastage0event == 0 and rngworkgirl == 2:
                "You go to your work."
                play music "/music/bunny_bites.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                if daytime == 1:
                    call work_arrive_weekend
                else:
                    call work_arrive
                    "You start working the counter."
                call work_randomizer
                call Lisa_Stage_1_Event_1
                call work_randomizer
                $ money += 10
                "You earned ten dollars."
                $ daytime += 1
                $ hari_work_today = 0
                $ marie_work_today = 0
                $ lisa_work_today = 0
                $ amber_work_today = 0
                $ luna_work_today = 0
                $ daisy_work_today = 0
                $ leanne_work_today = 0
                $ bonnie_work_today = 0
                $ librarian_work_today = 0
                $ cayenne_work_today = 0
                $ maya_work_today = 0
                $ katrine_work_today = 0
                $ trista_work_today = 0
                $ caroline_work_today = 0
                $ roxie_work_today = 0
                $ natalie_work_today = 0
                $ charlene_work_today = 0
                $ vicky_work_today = 0
                $ sally_work_today = 0
                $ britta_work_today = 0
                $ rebecca_work_today = 0
                $ mylenna_work_today = 0
                $ worked_today = 1
                stop music fadeout 1.0
                jump freetime
            if amberstage1event == 1 and amberstage0event == 0 and rngworkgirl == 1:
                "You go to your work."
                play music "/music/bb_amber.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                if daytime == 1:
                    call work_arrive_weekend
                else:
                    call work_arrive
                    "You start working the counter."
                call work_randomizer
                call Amber_Stage_1_Event_1
                call work_randomizer
                $ money += 10
                "You earned ten dollars."
                $ daytime += 1
                $ hari_work_today = 0
                $ marie_work_today = 0
                $ lisa_work_today = 0
                $ amber_work_today = 0
                $ luna_work_today = 0
                $ daisy_work_today = 0
                $ leanne_work_today = 0
                $ bonnie_work_today = 0
                $ librarian_work_today = 0
                $ cayenne_work_today = 0
                $ maya_work_today = 0
                $ katrine_work_today = 0
                $ trista_work_today = 0
                $ caroline_work_today = 0
                $ roxie_work_today = 0
                $ natalie_work_today = 0
                $ charlene_work_today = 0
                $ vicky_work_today = 0
                $ sally_work_today = 0
                $ britta_work_today = 0
                $ rebecca_work_today = 0
                $ mylenna_work_today = 0
                $ worked_today = 1
                stop music fadeout 1.0
                jump freetime
            if lisastage2event == 1 and lisastage1event2 == 0 and rngworkgirl == 2 and lisa.stage >= 2:
                "You go to your work."
                play music "/music/bunny_bites.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                if daytime == 1:
                    call work_arrive_weekend
                else:
                    call work_arrive
                    "You start working the counter."
                call work_randomizer
                call work_randomizer
                call Lisa_Stage_2_Event_1
                $ daytime += 1
                $ hari_work_today = 0
                $ marie_work_today = 0
                $ lisa_work_today = 0
                $ amber_work_today = 0
                $ luna_work_today = 0
                $ daisy_work_today = 0
                $ leanne_work_today = 0
                $ bonnie_work_today = 0
                $ librarian_work_today = 0
                $ cayenne_work_today = 0
                $ maya_work_today = 0
                $ katrine_work_today = 0
                $ trista_work_today = 0
                $ caroline_work_today = 0
                $ roxie_work_today = 0
                $ natalie_work_today = 0
                $ charlene_work_today = 0
                $ vicky_work_today = 0
                $ sally_work_today = 0
                $ britta_work_today = 0
                $ rebecca_work_today = 0
                $ mylenna_work_today = 0
                $ worked_today = 1
                stop music fadeout 1.0
                jump freetime
            if amberstage2event == 1 and amberstage1event2 == 0 and rngworkgirl == 1 and amber.stage >= 2:
                "You go to your work."
                play music "/music/bb_amber.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                if daytime == 1:
                    call work_arrive_weekend
                else:
                    call work_arrive
                    "You start working the counter."
                call work_randomizer
                call Amber_Stage_2_Event_1
                $ daytime = 4
                $ hari_work_today = 0
                $ marie_work_today = 0
                $ lisa_work_today = 0
                $ amber_work_today = 0
                $ luna_work_today = 0
                $ daisy_work_today = 0
                $ leanne_work_today = 0
                $ bonnie_work_today = 0
                $ librarian_work_today = 0
                $ cayenne_work_today = 0
                $ maya_work_today = 0
                $ katrine_work_today = 0
                $ trista_work_today = 0
                $ caroline_work_today = 0
                $ roxie_work_today = 0
                $ natalie_work_today = 0
                $ charlene_work_today = 0
                $ vicky_work_today = 0
                $ sally_work_today = 0
                $ britta_work_today = 0
                $ rebecca_work_today = 0
                $ mylenna_work_today = 0
                $ worked_today = 1
                stop music fadeout 1.0
                jump freetime
            if mariestage2event2 == 1 and mariestage2event == 0 and rngworkgirl == 3 and marie.stage >= 2:
                "You go to your work."
                play music "/music/bunny_bites.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                if daytime == 1:
                    call work_arrive_weekend
                else:
                    call work_arrive
                    "You start working the counter."
                call work_randomizer
                call Marie_Stage_2_Event_2
                call work_randomizer
                $ daytime += 1
                $ hari_work_today = 0
                $ marie_work_today = 0
                $ lisa_work_today = 0
                $ amber_work_today = 0
                $ luna_work_today = 0
                $ daisy_work_today = 0
                $ leanne_work_today = 0
                $ bonnie_work_today = 0
                $ librarian_work_today = 0
                $ cayenne_work_today = 0
                $ maya_work_today = 0
                $ katrine_work_today = 0
                $ trista_work_today = 0
                $ caroline_work_today = 0
                $ roxie_work_today = 0
                $ natalie_work_today = 0
                $ charlene_work_today = 0
                $ vicky_work_today = 0
                $ sally_work_today = 0
                $ britta_work_today = 0
                $ rebecca_work_today = 0
                $ mylenna_work_today = 0
                $ worked_today = 1
                stop music fadeout 1.0
                jump freetime
            if lisastage3event2 == 1 and lisastage3event == 0 and rngworkgirl == 2 and lisa.stage >= 3:
                "You go to your work."
                play music "/music/bunny_bites.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                if daytime == 1:
                    call work_arrive_weekend
                else:
                    call work_arrive
                    "You start working the counter."
                call work_randomizer
                call work_randomizer
                call Lisa_Stage_3_Event_2
                $ daytime += 1
                $ hari_work_today = 0
                $ marie_work_today = 0
                $ lisa_work_today = 0
                $ amber_work_today = 0
                $ luna_work_today = 0
                $ daisy_work_today = 0
                $ leanne_work_today = 0
                $ bonnie_work_today = 0
                $ librarian_work_today = 0
                $ cayenne_work_today = 0
                $ maya_work_today = 0
                $ katrine_work_today = 0
                $ trista_work_today = 0
                $ caroline_work_today = 0
                $ roxie_work_today = 0
                $ natalie_work_today = 0
                $ charlene_work_today = 0
                $ vicky_work_today = 0
                $ sally_work_today = 0
                $ britta_work_today = 0
                $ rebecca_work_today = 0
                $ mylenna_work_today = 0
                $ worked_today = 1
                stop music fadeout 1.0
                jump freetime
            if amberstage4event == 1 and rngworkgirl == 1 and amber.stage >= 4:
                "You go to your work."
                play music "/music/bb_amber.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                if daytime == 1:
                    call work_arrive_weekend
                else:
                    call work_arrive
                    "You start working the counter."
                call work_randomizer
                "A while later."
                call work_randomizer
                call Amber_Stage_4_Event
                $ daytime = 4
                $ hari_work_today = 0
                $ marie_work_today = 0
                $ lisa_work_today = 0
                $ amber_work_today = 0
                $ luna_work_today = 0
                $ daisy_work_today = 0
                $ leanne_work_today = 0
                $ bonnie_work_today = 0
                $ librarian_work_today = 0
                $ cayenne_work_today = 0
                $ maya_work_today = 0
                $ katrine_work_today = 0
                $ trista_work_today = 0
                $ caroline_work_today = 0
                $ roxie_work_today = 0
                $ natalie_work_today = 0
                $ charlene_work_today = 0
                $ vicky_work_today = 0
                $ sally_work_today = 0
                $ britta_work_today = 0
                $ rebecca_work_today = 0
                $ mylenna_work_today = 0
                $ worked_today = 1
                stop music fadeout 1.0
                jump freetime
            if mariestage4event2 == 1 and mariestage4event == 0 and rngworkgirl == 3 and marie.stage >= 4:
                "You go to your work."
                play music "/music/bunny_bites.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                if daytime == 1:
                    call work_arrive_weekend
                else:
                    call work_arrive
                    "You start working the counter."
                call work_randomizer
                call Marie_Stage_4_Event_2
                $ daytime += 1
                $ hari_work_today = 0
                $ marie_work_today = 0
                $ lisa_work_today = 0
                $ amber_work_today = 0
                $ luna_work_today = 0
                $ daisy_work_today = 0
                $ leanne_work_today = 0
                $ bonnie_work_today = 0
                $ librarian_work_today = 0
                $ cayenne_work_today = 0
                $ maya_work_today = 0
                $ katrine_work_today = 0
                $ trista_work_today = 0
                $ caroline_work_today = 0
                $ roxie_work_today = 0
                $ natalie_work_today = 0
                $ charlene_work_today = 0
                $ vicky_work_today = 0
                $ sally_work_today = 0
                $ britta_work_today = 0
                $ rebecca_work_today = 0
                $ mylenna_work_today = 0
                $ worked_today = 1
                stop music fadeout 1.0
                jump freetime
            if amberstage5event == 1 and mariestage3event2 == 0 and rngworkgirl == 1 and amber.stage >= 5:
                "You go to your work."
                play music "/music/bb_amber.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                if daytime == 1:
                    call work_arrive_weekend
                else:
                    call work_arrive
                    "You start working the counter."
                call work_randomizer
                call Amber_Stage_5_Event_1
                call work_randomizer
                if mariestage4event == 0:
                    $ money += 20
                    "You earned twenty dollars."
                else:
                    $ money += 10
                    "You earned ten dollars."
                $ daytime = 4
                $ hari_work_today = 0
                $ marie_work_today = 0
                $ lisa_work_today = 0
                $ amber_work_today = 0
                $ luna_work_today = 0
                $ daisy_work_today = 0
                $ leanne_work_today = 0
                $ bonnie_work_today = 0
                $ librarian_work_today = 0
                $ cayenne_work_today = 0
                $ maya_work_today = 0
                $ katrine_work_today = 0
                $ trista_work_today = 0
                $ caroline_work_today = 0
                $ roxie_work_today = 0
                $ natalie_work_today = 0
                $ charlene_work_today = 0
                $ vicky_work_today = 0
                $ sally_work_today = 0
                $ britta_work_today = 0
                $ rebecca_work_today = 0
                $ mylenna_work_today = 0
                $ worked_today = 1
                stop music fadeout 1.0
                jump freetime
            if lisastage5event == 1 and mariestage3event2 == 0 and rngworkgirl == 2 and lisa.stage >= 5:
                "You go to your work."
                play music "/music/bunny_bites.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                if daytime == 1:
                    call work_arrive_weekend
                else:
                    call work_arrive
                    "You start working the counter."
                call work_randomizer
                call Lisa_Stage_5_Event
                call work_randomizer
                if mariestage4event == 0:
                    $ money += 20
                    "You earned twenty dollars."
                else:
                    $ money += 10
                    "You earned ten dollars."
                $ daytime = 4
                $ hari_work_today = 0
                $ marie_work_today = 0
                $ lisa_work_today = 0
                $ amber_work_today = 0
                $ luna_work_today = 0
                $ daisy_work_today = 0
                $ leanne_work_today = 0
                $ bonnie_work_today = 0
                $ librarian_work_today = 0
                $ cayenne_work_today = 0
                $ maya_work_today = 0
                $ katrine_work_today = 0
                $ trista_work_today = 0
                $ caroline_work_today = 0
                $ roxie_work_today = 0
                $ natalie_work_today = 0
                $ charlene_work_today = 0
                $ vicky_work_today = 0
                $ sally_work_today = 0
                $ britta_work_today = 0
                $ rebecca_work_today = 0
                $ mylenna_work_today = 0
                $ worked_today = 1
                stop music fadeout 1.0
                jump freetime
            if mariestage6event2 == 1 and rngworkgirl == 3 and marie.stage >= 6:
                "You go to your work."
                play music "/music/bunny_bites.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                call Marie_Stage_6_Event_2
                call work_randomizer
                "A while later."
                call work_randomizer
                "You work your ass off for the rest of your shift."
                $ daytime += 1
                if mariestage4event == 0:
                    $ money += 20
                    "You earned twenty dollars."
                else:
                    $ money += 10
                    "You earned ten dollars."
                "After a while, someone finally arrives to take over your shift."
                call work_leave
                $ hari_work_today = 0
                $ marie_work_today = 0
                $ lisa_work_today = 0
                $ amber_work_today = 0
                $ luna_work_today = 0
                $ daisy_work_today = 0
                $ leanne_work_today = 0
                $ bonnie_work_today = 0
                $ librarian_work_today = 0
                $ cayenne_work_today = 0
                $ maya_work_today = 0
                $ katrine_work_today = 0
                $ trista_work_today = 0
                $ caroline_work_today = 0
                $ roxie_work_today = 0
                $ natalie_work_today = 0
                $ charlene_work_today = 0
                $ vicky_work_today = 0
                $ sally_work_today = 0
                $ britta_work_today = 0
                $ rebecca_work_today = 0
                $ mylenna_work_today = 0
                $ worked_today = 1
                stop music fadeout 1.0
                jump freetime

            if daytime == 1:
                "You go to your work."
                if rngworkgirl == 1:
                    play music "/music/bb_amber.ogg" if_changed
                else:
                    play music "/music/bunny_bites.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                call work_arrive_weekend
                if amber_stats_visible == 0:
                    "While working you notice something on the company computer."
                    "It seems to be detailed records of the workers, complete with accurate body measurements and everything."
                    "This is probably Marie's work."
                    $ amber_stats_visible = 1
                    $ lisa_stats_visible = 1
                    $ marie_stats_visible = 1
                    "Amber, Lisa and Marie have been added to the stats page"
                call work_randomizer
                call work_snack
                "A while later."
                if lisastage4event2 == 1 and rngworkgirl == 2 and lisa.stage >= 4:
                    call Lisa_Stage_4_Event_2
                    $ daytime = 4
                    $ worked_today = 1
                    stop music fadeout 1.0
                    jump freetime
                if mariestage2event2 == 1 and mariestage2event == 0 and rngworkgirl == 3 and marie.stage >= 2:
                    call Marie_Stage_2_Event_2
                call work_randomizer
                "You work your ass off for the rest of your shift."
                $ daytime += 1
                if mariestage4event == 0:
                    $ money += 20
                    "You earned twenty dollars."
                else:
                    $ money += 10
                    "You earned ten dollars."
                $ workcall = 1
                call Phone_calls
                call screen menuBB
                if keep_working == 1:
                    $ workcall = 0
                    $ phoneMessages = False
                    if rngworkgirl == 1:
                        play music "/music/bb_amber.ogg" if_changed
                    else:
                        play music "/music/bunny_bites.ogg" if_changed
                    call work_randomizer
                    call work_snack
                    "A while later."
                    call work_randomizer
                    "You work your ass off for the rest of your shift."
                    $ daytime += 1
                    if mariestage4event == 0:
                        $ money += 20
                        "You earned twenty dollars."
                    else:
                        $ money += 10
                        "You earned ten dollars."
                    $ workcall = 1
                    call Phone_calls
                    call screen menuBB
                    if keep_working == 1:
                        $ workcall = 0
                        $ phoneMessages = False
                        if rngworkgirl == 1:
                            play music "/music/bb_amber.ogg" if_changed
                        else:
                            play music "/music/bunny_bites.ogg" if_changed
                        $ daytime += 1
                        call work_randomizer
                        call work_snack
                        "A while later."
                        call work_randomizer
                        "You work your ass off for the rest of your shift."
                        if mariestage4event == 0:
                            $ money += 20
                            "You earned twenty dollars."
                        else:
                            $ money += 10
                            "You earned ten dollars."
                        call work_leave_weekend
                    else:
                        $ workcall = 0
                        $ phoneMessages = False
                        "After a while, someone finally arrives to take over your shift."
                        call work_leave
                else:
                    $ workcall = 0
                    $ phoneMessages = False
                    "After a while, someone finally arrives to take over your shift."
                    call work_leave
            elif daytime == 2:
                call bbworking
                $ rngworkcustomer_norepeat = 0
                if rngworkgirl == 1:
                    play music "/music/bb_amber.ogg" if_changed
                else:
                    play music "/music/bunny_bites.ogg" if_changed
                call work_arrive
                "You start working the counter."
                if amber_stats_visible == 0:
                    "While working you notice something on the company computer."
                    "It seems to be detailed records of the workers, complete with accurate body measurements and everything."
                    "You wonder who keeps these records."
                    $ amber_stats_visible = 1
                    $ lisa_stats_visible = 1
                    $ marie_stats_visible = 1
                    "Amber, Lisa and Marie have been added to the stats page"
                call work_randomizer
                if lisastage4event2 == 1 and rngworkgirl == 2 and lisa.stage >= 4:
                    call Lisa_Stage_4_Event_2
                    $ daytime = 4
                    $ worked_today = 1
                    stop music fadeout 1.0
                    jump freetime
                if mariestage2event2 == 1 and mariestage2event == 0 and rngworkgirl == 3 and marie.stage >= 2:
                    call Marie_Stage_2_Event_2
                call work_snack
                "A while later."
                call work_randomizer
                "You work your ass off for the rest of your shift."
                $ daytime += 1
                if mariestage4event == 0:
                    $ money += 20
                    "You earned twenty dollars."
                else:
                    $ money += 10
                    "You earned ten dollars."
                $ workcall = 1
                call Phone_calls
                call screen menuBB
                if keep_working == 1:
                    $ workcall = 0
                    $ phoneMessages = False
                    if rngworkgirl == 1:
                        play music "/music/bb_amber.ogg" if_changed
                    else:
                        play music "/music/bunny_bites.ogg" if_changed
                    $ daytime += 1
                    call work_randomizer
                    call work_snack
                    "A while later."
                    call work_randomizer
                    "You work your ass off for the rest of your shift."
                    if mariestage4event == 0:
                        $ money += 20
                        "You earned twenty dollars."
                    else:
                        $ money += 10
                        "You earned ten dollars."
                    call work_leave_weekend
                else:
                    $ workcall = 0
                    $ phoneMessages = False
                    "After a while, someone finally arrives to take over your shift."
                    call work_leave
            elif daytime == 3:
                $ daytime += 1
                call bbworking
                if rngworkgirl == 1:
                    play music "/music/bb_amber.ogg" if_changed
                else:
                    play music "/music/bunny_bites.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                call work_arrive
                "You start working the counter."
                if amber_stats_visible == 0:
                    "While working you notice something on the company computer."
                    "It seems to be detailed records of the workers, complete with accurate body measurements and everything."
                    "This is probably Marie's work."
                    $ amber_stats_visible = 1
                    $ lisa_stats_visible = 1
                    $ marie_stats_visible = 1
                    "Amber, Lisa and Marie have been added to the stats page"
                call work_randomizer
                if lisastage4event2 == 1 and rngworkgirl == 2 and lisa.stage >= 4:
                    call Lisa_Stage_4_Event_2
                    $ daytime = 4
                    $ worked_today = 1
                    stop music fadeout 1.0
                    jump freetime
                if mariestage2event2 == 1 and mariestage2event == 0 and rngworkgirl == 3 and marie.stage >= 2:
                    call Marie_Stage_2_Event_2
                call work_snack
                "A while later."
                call work_randomizer
                "You work your ass off for the rest of your shift."
                if mariestage4event == 0:
                    $ money += 20
                    "You earned twenty dollars."
                else:
                    $ money += 10
                    "You earned ten dollars."
                call work_leave_weekend
            $ hari_work_today = 0
            $ marie_work_today = 0
            $ lisa_work_today = 0
            $ amber_work_today = 0
            $ luna_work_today = 0
            $ daisy_work_today = 0
            $ leanne_work_today = 0
            $ bonnie_work_today = 0
            $ librarian_work_today = 0
            $ cayenne_work_today = 0
            $ maya_work_today = 0
            $ katrine_work_today = 0
            $ trista_work_today = 0
            $ caroline_work_today = 0
            $ roxie_work_today = 0
            $ natalie_work_today = 0
            $ charlene_work_today = 0
            $ vicky_work_today = 0
            $ sally_work_today = 0
            $ britta_work_today = 0
            $ rebecca_work_today = 0
            $ mylenna_work_today = 0
            $ worked_today = 1
            jump freetime

        "Return":
            call screen citymenu


    

