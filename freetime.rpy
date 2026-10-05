label freetime:
    $ recollection = False
    $ phonecall = 0
    $ renpy.set_return_stack([])
    if workcall == 1:
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
        $ workcall = 0
    if daytime >= 4:
        if bonniestage7event2 == 1 and bonniestage7event == 0 and bonnie.stage >= 7 and day == 7:
            stop music fadeout 1.0
            call Bonnie_Stage_7_Event_2 from _call_Bonnie_Stage_7_Event_2
            jump freetime
        elif leannestage7event2 == 1 and leannestage7event == 0 and leanne.stage >= 7:
            stop music fadeout 1.0
            call Leanne_Stage_7_Event_2
        elif leannestage8event2 == 1 and leannestage8event == 0 and leanne.stage >= 8:
            stop music fadeout 1.0
            call Leanne_Stage_8_Event_2
        elif leannestage8event3 == 1 and leannestage8event2 == 0 and leanne.stage >= 8:
            stop music fadeout 1.0
            call Leanne_Stage_8_Event_3
        elif leannestage9event2 == 1 and leannestage9event == 0 and leanne.stage >= 9:
            stop music fadeout 1.0
            call Leanne_Stage_9_Event_2
        $ daytime = 1
        $ day += 1
        $ daycount += 1 #counts the days since leanne her stream got banned
        $ daycount2 += 1 #counts the days since Hari gets mad for discovering her secret
        $ daycount3 += 1 #counts the days since Cayenne decides to no longer gain weight
        $ daycount4 += 1 #counts the days since Caroline lost her leg
        $ daycount5 += 1 #counts the days since Maya got the stripclub back
        $ strip = 0
        $ stuffed = 0
        $ bellyrub = 0
        $ worked_today = 0
        $ bonnie_gym_today = 0
        $ rebecca_gym_today = 0
        $ maya_gym_today = 0
        $ cayenne_gym_today = 0
        $ teacher_gym_today = 0
        $ lisa_gym_today = 0
        $ hari_gym_today = 0
        $ marie_gym_today = 0
        $ katrine_gym_today = 0
        $ trista_gym_today = 0
        $ trista.fullness = 0
        $ bonnie.fullness = 0
        $ katrine.fullness = 0
        $ maya.fullness = 0
        $ amber.fullness = 0
        $ luna.fullness = 0
        $ cayenne.fullness = 0
        if day >= 8:
            $ day = 1
            $ week += 1
            if teacher.stage <= 2:
                $ teacher.weight += 1
                $ luna.weight = 54
            elif teacher.stage <= 8:
                $ teacher.weight += 0.8
            elif teacher.stage <= 13:
                $ teacher.weight += 0.5
            $ weeklyprize = 1
            $ nataliemilkcheck = 1
            $ brittamilkcheck = 1
            $ hari_study_times = 0
            $ caroline_study_times = 0
            $ vicky_study_times = 0
        jump start
    if daytime >= 3:
        image DARK_BEDROOM = "/ui/roommenu/DARK_BEDROOM_background.png"
        scene DARK_BEDROOM
    else:
        image LIGHT_BEDROOM = "/ui/roommenu/LIGHT_BEDROOM_background.png"
        scene LIGHT_BEDROOM
    call Phone_calls from _call_Phone_calls
    if teacherstage12event == 1 and teacher.stage >= 12 and day == 6:
        "I should check on Daisy this weekend."
    if haristage4event3 == 1 and haristage4event2 == 0 and hari.weight >= 71 and day == 6:
        "I should visit Hari's house to study with her."
    if mayastage5event == 1 and mayastage4event4 == 0 and daytime == 3 and day >= 6:
        stop music fadeout 1.0
        call Maya_Stage_5_Event_1 from _call_Maya_Stage_5_Event_1
        $ daytime += 1
        jump freetime
    if mayastage5event3 == 1 and mayastage5event2 == 0 and maya.fullness == 0:
        stop music fadeout 1.0
        call Maya_Stage_5_Event_3
        $ daytime += 1
        jump freetime
    $ athome = 1
    call screen roommenu

    if daytime >= 3:
        image DARK_BEDROOM = "/ui/roommenu/DARK_BEDROOM_background.png"
        scene DARK_BEDROOM
    else:
        image LIGHT_BEDROOM = "/ui/roommenu/LIGHT_BEDROOM_background.png"
        scene LIGHT_BEDROOM
    menu:
        pc "What should I do?"
        "Watch a livestream." if streamergirlunlock == 1 and daytime == 3 and leanne_stats_visible == 0:
            call leanne_introduction from _call_leanne_introduction
        #Watch Leanne her livestream(All leanne her content is behind this option)
        "Watch [Lynname]'s livestream." if streamergirlunlock == 1 and daytime == 3 and leanne_stats_visible == 1:
            $ phoneMessages = False
            if leanne.stage <= 11 and leannestage11event2 == 1:
                call leanne_stream from _call_leanne_stream_2
            elif leanne.stage >= 12 and leannechoice == 1 and leannestage12event3 == 0:
                if leanne.stage >= 13 and leannestage13event == 0:
                    $ rng = renpy.random.randint(1,3)
                    if rng == 1:
                        call lyn_stream from _call_lyn_stream
                    elif rng == 2:
                        call lyn_soda_stream from _call_lyn_soda_stream
                    elif rng == 3:
                        call lyn_sugar_shop_stream from _call_lyn_sugar_shop_stream
                else:
                    call lyn_stream from _call_lyn_stream_1
            elif leanne.stage >= 12 and leannechoice == 2 and leannestage12event3 == 0:
                if leanne.stage >= 13 and leannestage13event == 0:
                    $ rng = renpy.random.randint(1,3)
                    if rng == 1:
                        call leanne_stream2 from _call_leanne_stream2
                    elif rng == 2:
                        call leanne_soda_stream from _call_leanne_soda_stream
                    elif rng == 3:
                        call leanne_bunny_bites_stream from _call_leanne_bunny_bites_stream
                else:
                    call leanne_stream2 from _call_leanne_stream2_1
            elif leanne.stage >= 12 and leannestage12event2 == 0 and leannestage12event3 == 1:
                call Leanne_Stage_12_Event_3 from _call_Leanne_Stage_12_Event_3_1
            else:
                "The webpage shows you that this user is banned from streaming."
                pc "FeelsBadMan"
                jump freetime

        "Watch Mira's livestream." if leannestage11event4 == 1 and leannestage11event2 == 0 and daytime == 3:
            $ phoneMessages = False
            if leannestage11event4 == 1:
                jump Leanne_Stage_11_Event_4
            #elif leannestage11event5 == 1 and leannestage11event4 == 0:
            #    call Leanne_Stage_11_Event_5
            #elif leannestage11event6 == 1 and leannestage11event5 == 0:
            #    call Leanne_Stage_11_Event_6
            #elif leannestage11event7 == 1 and leannestage11event6 == 0:
            #    call Leanne_Stage_11_Event_7
            #elif leannestage11event8 == 1 and leannestage11event7 == 0:
            #    call Leanne_Stage_11_Event_8

        "Train charisma in the mirror." if charisma <= 6:
            $ phoneMessages = False
            jump charisma_train


        #Go work at the cafe together with you coworkers and have customers visit
        "Go to work." if lisastage0event == 0 and worked_today == 0:
            $ phoneMessages = False
            if mariestage1event == 1 and lisastage0event == 0:
                #SECOND DAY WITH LISA(MARIE STAGE 1 EVENT)
                "You go to your work."
                play music "/music/bunny_bites.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                $ rngworkgirl = 3
                if daytime == 1:
                    call work_arrive_weekend from _call_work_arrive_weekend_4
                else:
                    call work_arrive from _call_work_arrive_3
                    "You start working the counter."
                call work_randomizer from _call_work_randomizer_26
                call Marie_Stage_1_Event_1
                "A while later."
                call work_randomizer from _call_work_randomizer_27
                "You work your ass off for the rest of your shift."
                $ money += 10
                "You earned ten dollars."
                "After a while, someone finally arrives to take over your shift."
                call work_leave from _call_work_leave
                $ daytime += 1
                $ worked_today = 1
                stop music fadeout 1.0
                jump freetime

            $ rngworkgirl = renpy.random.randint(1,3)
            if katrineintroduction == 1 and katrine_stats_visible == 1:
                play music "/music/bunny_bites.ogg" if_changed
                call Katrine_Introduction from _call_Katrine_Introduction
                $ daytime += 1
                $ worked_today = 1
                jump freetime
            if lisastage1event == 1 and lisastage0event == 0 and rngworkgirl == 2:
                "You go to your work."
                play music "/music/bunny_bites.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                if daytime == 1:
                    call work_arrive_weekend from _call_work_arrive_weekend_5
                else:
                    call work_arrive from _call_work_arrive_4
                    "You start working the counter."
                call work_randomizer from _call_work_randomizer_28
                call Lisa_Stage_1_Event_1
                call work_randomizer from _call_work_randomizer_29
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
                    call work_arrive_weekend from _call_work_arrive_weekend_6
                else:
                    call work_arrive from _call_work_arrive_5
                    "You start working the counter."
                call work_randomizer from _call_work_randomizer_30
                call Amber_Stage_1_Event_1
                call work_randomizer from _call_work_randomizer_31
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
                    call work_arrive_weekend from _call_work_arrive_weekend_7
                else:
                    call work_arrive from _call_work_arrive_6
                    "You start working the counter."
                call work_randomizer from _call_work_randomizer_32
                call work_randomizer from _call_work_randomizer_33
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
                    call work_arrive_weekend from _call_work_arrive_weekend_8
                else:
                    call work_arrive from _call_work_arrive_7
                    "You start working the counter."
                call work_randomizer from _call_work_randomizer_34
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
                    call work_arrive_weekend from _call_work_arrive_weekend_9
                else:
                    call work_arrive from _call_work_arrive_8
                    "You start working the counter."
                call work_randomizer from _call_work_randomizer_35
                call Marie_Stage_2_Event_2 from _call_Marie_Stage_2_Event_2_1
                call work_randomizer from _call_work_randomizer_36
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
                    call work_arrive_weekend from _call_work_arrive_weekend_10
                else:
                    call work_arrive from _call_work_arrive_9
                    "You start working the counter."
                call work_randomizer from _call_work_randomizer_37
                call work_randomizer from _call_work_randomizer_38
                call Lisa_Stage_3_Event_2 from _call_Lisa_Stage_3_Event_2
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
                    call work_arrive_weekend from _call_work_arrive_weekend
                else:
                    call work_arrive from _call_work_arrive_10
                    "You start working the counter."
                call work_randomizer from _call_work_randomizer
                "A while later."
                call work_randomizer from _call_work_randomizer_1
                call Amber_Stage_4_Event from _call_Amber_Stage_4_Event_1
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
                    call work_arrive_weekend from _call_work_arrive_weekend_11
                else:
                    call work_arrive from _call_work_arrive_11
                    "You start working the counter."
                call work_randomizer from _call_work_randomizer_39
                call Marie_Stage_4_Event_2 from _call_Marie_Stage_4_Event_2
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
                    call work_arrive_weekend from _call_work_arrive_weekend_2
                else:
                    call work_arrive from _call_work_arrive_12
                    "You start working the counter."
                call work_randomizer from _call_work_randomizer_2
                call Amber_Stage_5_Event_1
                call work_randomizer from _call_work_randomizer_7
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
                    call work_arrive_weekend from _call_work_arrive_weekend_3
                else:
                    call work_arrive from _call_work_arrive_13
                    "You start working the counter."
                call work_randomizer from _call_work_randomizer_20
                call Lisa_Stage_5_Event from _call_Lisa_Stage_5_Event
                call work_randomizer from _call_work_randomizer_21
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
                call work_arrive_weekend from _call_work_arrive_weekend_1
                if amber_stats_visible == 0:
                    "While working you notice something on the company computer."
                    "It seems to be detailed records of the workers, complete with accurate body measurements and everything."
                    "This is probably Marie's work."
                    $ amber_stats_visible = 1
                    $ lisa_stats_visible = 1
                    $ marie_stats_visible = 1
                    "Amber, Lisa and Marie have been added to the stats page"
                call work_randomizer from _call_work_randomizer_8
                call work_snack from _call_work_snack
                "A while later."
                if lisastage4event2 == 1 and rngworkgirl == 2 and lisa.stage >= 4:
                    call Lisa_Stage_4_Event_2 from _call_Lisa_Stage_4_Event_2
                    $ daytime = 4
                    $ worked_today = 1
                    stop music fadeout 1.0
                    jump freetime
                if mariestage2event2 == 1 and mariestage2event == 0 and rngworkgirl == 3 and marie.stage >= 2:
                    call Marie_Stage_2_Event_2 from _call_Marie_Stage_2_Event_2_2
                call work_randomizer from _call_work_randomizer_9
                "You work your ass off for the rest of your shift."
                $ daytime += 1
                if mariestage4event == 0:
                    $ money += 20
                    "You earned twenty dollars."
                else:
                    $ money += 10
                    "You earned ten dollars."
                $ workcall = 1
                call Phone_calls from _call_Phone_calls_1
                call screen menuBB
                if keep_working == 1:
                    $ workcall = 0
                    $ phoneMessages = False
                    if rngworkgirl == 1:
                        play music "/music/bb_amber.ogg" if_changed
                    else:
                        play music "/music/bunny_bites.ogg" if_changed
                    call work_randomizer from _call_work_randomizer_10
                    call work_snack from _call_work_snack_1
                    "A while later."
                    call work_randomizer from _call_work_randomizer_11
                    "You work your ass off for the rest of your shift."
                    $ daytime += 1
                    if mariestage4event == 0:
                        $ money += 20
                        "You earned twenty dollars."
                    else:
                        $ money += 10
                        "You earned ten dollars."
                    $ workcall = 1
                    call Phone_calls from _call_Phone_calls_2
                    call screen menuBB
                    if keep_working == 1:
                        $ workcall = 0
                        $ phoneMessages = False
                        if rngworkgirl == 1:
                            play music "/music/bb_amber.ogg" if_changed
                        else:
                            play music "/music/bunny_bites.ogg" if_changed
                        $ daytime += 1
                        call work_randomizer from _call_work_randomizer_12
                        call work_snack from _call_work_snack_2
                        "A while later."
                        call work_randomizer from _call_work_randomizer_13
                        "You work your ass off for the rest of your shift."
                        if mariestage4event == 0:
                            $ money += 20
                            "You earned twenty dollars."
                        else:
                            $ money += 10
                            "You earned ten dollars."
                        call work_leave_weekend from _call_work_leave_weekend_1
                    else:
                        $ workcall = 0
                        $ phoneMessages = False
                        "After a while, someone finally arrives to take over your shift."
                        call work_leave from _call_work_leave_1
                else:
                    $ workcall = 0
                    $ phoneMessages = False
                    "After a while, someone finally arrives to take over your shift."
                    call work_leave from _call_work_leave_2
            elif daytime == 2:
                call bbworking
                $ rngworkcustomer_norepeat = 0
                if rngworkgirl == 1:
                    play music "/music/bb_amber.ogg" if_changed
                else:
                    play music "/music/bunny_bites.ogg" if_changed
                call work_arrive from _call_work_arrive_1
                "You start working the counter."
                if amber_stats_visible == 0:
                    "While working you notice something on the company computer."
                    "It seems to be detailed records of the workers, complete with accurate body measurements and everything."
                    "You wonder who keeps these records."
                    $ amber_stats_visible = 1
                    $ lisa_stats_visible = 1
                    $ marie_stats_visible = 1
                    "Amber, Lisa and Marie have been added to the stats page"
                call work_randomizer from _call_work_randomizer_14
                if lisastage4event2 == 1 and rngworkgirl == 2 and lisa.stage >= 4:
                    call Lisa_Stage_4_Event_2 from _call_Lisa_Stage_4_Event_2_1
                    $ daytime = 4
                    $ worked_today = 1
                    stop music fadeout 1.0
                    jump freetime
                if mariestage2event2 == 1 and mariestage2event == 0 and rngworkgirl == 3 and marie.stage >= 2:
                    call Marie_Stage_2_Event_2 from _call_Marie_Stage_2_Event_2_3
                call work_snack from _call_work_snack_3
                "A while later."
                call work_randomizer from _call_work_randomizer_15
                "You work your ass off for the rest of your shift."
                $ daytime += 1
                if mariestage4event == 0:
                    $ money += 20
                    "You earned twenty dollars."
                else:
                    $ money += 10
                    "You earned ten dollars."
                $ workcall = 1
                call Phone_calls from _call_Phone_calls_3
                call screen menuBB
                if keep_working == 1:
                    $ workcall = 0
                    $ phoneMessages = False
                    if rngworkgirl == 1:
                        play music "/music/bb_amber.ogg" if_changed
                    else:
                        play music "/music/bunny_bites.ogg" if_changed
                    $ daytime += 1
                    call work_randomizer from _call_work_randomizer_16
                    call work_snack from _call_work_snack_4
                    "A while later."
                    call work_randomizer from _call_work_randomizer_17
                    "You work your ass off for the rest of your shift."
                    if mariestage4event == 0:
                        $ money += 20
                        "You earned twenty dollars."
                    else:
                        $ money += 10
                        "You earned ten dollars."
                    call work_leave_weekend from _call_work_leave_weekend_2
                else:
                    $ workcall = 0
                    $ phoneMessages = False
                    "After a while, someone finally arrives to take over your shift."
                    call work_leave from _call_work_leave_3
            elif daytime == 3:
                $ daytime += 1
                call bbworking
                if rngworkgirl == 1:
                    play music "/music/bb_amber.ogg" if_changed
                else:
                    play music "/music/bunny_bites.ogg" if_changed
                $ rngworkcustomer_norepeat = 0
                call work_arrive from _call_work_arrive_2
                "You start working the counter."
                if amber_stats_visible == 0:
                    "While working you notice something on the company computer."
                    "It seems to be detailed records of the workers, complete with accurate body measurements and everything."
                    "This is probably Marie's work."
                    $ amber_stats_visible = 1
                    $ lisa_stats_visible = 1
                    $ marie_stats_visible = 1
                    "Amber, Lisa and Marie have been added to the stats page"
                call work_randomizer from _call_work_randomizer_18
                if lisastage4event2 == 1 and rngworkgirl == 2 and lisa.stage >= 4:
                    call Lisa_Stage_4_Event_2 from _call_Lisa_Stage_4_Event_2_2
                    $ daytime = 4
                    $ worked_today = 1
                    stop music fadeout 1.0
                    jump freetime
                if mariestage2event2 == 1 and mariestage2event == 0 and rngworkgirl == 3 and marie.stage >= 2:
                    call Marie_Stage_2_Event_2 from _call_Marie_Stage_2_Event_2_4
                call work_snack from _call_work_snack_5
                "A while later."
                call work_randomizer from _call_work_randomizer_19
                "You work your ass off for the rest of your shift."
                if mariestage4event == 0:
                    $ money += 20
                    "You earned twenty dollars."
                else:
                    $ money += 10
                    "You earned ten dollars."
                call work_leave_weekend from _call_work_leave_weekend_3
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

        #Read a book
        "Read a book." if booksheld >= 1:
            $ phoneMessages = False
            $ bookday = 0
            jump book_read_home

        #Go to the anime store(unlocked at stage 3 leanne)
        "Go to the Anime Store." if leanne.stage >= 3 and leannestage3event == 1 and daytime == 2:
            $ phoneMessages = False
            jump Leanne_Stage_3_Event

        "Meet up with Leanne." if leanne.stage >= 11 and leannestage11event2 == 0 and leannestage11event3 == 1 and daytime == 2:
            $ phoneMessages = False
            jump Leanne_Stage_11_Event_3

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

        #Go to Cayenne her home to feed her
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

        #Go to Cayenne her stage2 event
        "Help the home student with a tutoring session." if cayenne.stage >= 2 and daisycayennetutorintro == 0 and cayennestage1event5 == 0 and daytime == 2 and cayennestage2event == 1:
            $ phoneMessages = False
            jump Cayenne_Stage_2_Event

        #Buy books at the library(half of them unlock after daisy stage 8 event)
        "Go to the library." if daytime == 2:
            $ phoneMessages = False
            jump library

        #Go to the shop where you can buy the fattening meal packages
        "Go to The Sugar Shop." if daytime == 2:
            $ phoneMessages = False
            jump sugarshop

        #This option is only here to unlock working at the cafe
        "Go to Bunny Bites." if workunlock == 0 and daytime == 2:
            $ phoneMessages = False
            jump bbintro

        #This option is only here to unlock Katrine when you have 7 charisma
        "Go for a walk." if katrine_stats_visible == 0 and daytime == 2:
            $ phoneMessages = False
            jump katrine_intro_outside

        #Daisy her repeatable house event
        "Visit Daisy." if teacher.stage >= 8 and teacherstage8event == 0 and daytime == 2:
            $ phoneMessages = False
            if teacherstage12event == 1 and teacher.stage >= 12:
                jump Teacher_Stage_12_Event
            jump daisy_home

        "Go to the hospital." if (nataliestage3event == 0 and nataliemilkcheck == 1) or (brittastage4event == 0 and brittamilkcheck == 1):
            $ phoneMessages = False
            jump hospital

        "Take Hari out to eat." if haristage2event == 0 and haristage2event2 == 1 and hari.stage >= 2 and day >= 6:
            $ phoneMessages = False
            jump Hari_Stage_2_Event_2

        "Visit Hari's house." if haristage4event2 == 0 and haristage4event3 == 1 and hari.weight >= 71 and day >= 6:
            $ phoneMessages = False
            jump Hari_Stage_4_Event_3

        #Go to the gym where loads of content is waiting
        "Go to the gym.":
            $ phoneMessages = False
            play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
            if katrinestage1event == 0 and tristastage1event == 1:
                call Trista_Stage_1_Event from _call_Trista_Stage_1_Event
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif gymunlock == 0:
                call trista_introduction from _call_trista_introduction
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif katrinestage2event == 0 and tristastage2event == 1 and trista.stage >= 2:
                call Trista_Stage_2_Event from _call_Trista_Stage_2_Event
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif katrinestage3event == 0 and tristastage3event == 1 and trista.stage >= 3:
                call Trista_Stage_3_Event from _call_Trista_Stage_3_Event
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif katrinestage1event == 1 and katrineintroduction == 0:
                call Katrine_Stage_1_Event from _call_Katrine_Stage_1_Event
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif katrinestage9event == 1 and katrine.stage >= 9 and trista.stage >= 9 and tristastage8event == 0:
                call Katrine_Stage_9_Event from _call_Katrine_Stage_9_Event
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

            elif teacherstage9event2 == 1 and teacher.stage >= 9 and teacherstage9event == 0:
                call Teacher_Stage_9_Event_2 from _call_Teacher_Stage_9_Event_2
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
                    call Teacher_Stage_6_Event_2 from _call_Teacher_Stage_6_Event_2
                jump freetime

            else:
                scene gym
                "You workout for a bit."
                $ strength += 1
                "Strength increased by one point"
                $ daytime += 1
                stop music fadeout 1.0
                jump freetime

        "Watch the special costume contest stream." if teacher.stage >= 17 and marie.stage >= 8 and luna.stage >= 11 and leanne.stage >= 13 and leannestage13event2 == 0 and katrine.stage >= 10 and lisa.stage >= 11 and amber.stage >= 9 and trista.stage >= 10 and bonnie.stage >= 11 and maya.stage >= 9:
            $ phoneMessages = False
            call Halloween_Event from _call_Halloween_Event
            jump freetime

        "Remember the good times." if teacherstage3event == 0:
            $ phoneMessages = False
            jump goodtimes
