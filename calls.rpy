default phoneMessages = False
default checkingPhone = False

init python:
    def checkPhone():
        global phoneMessages
        global phonegirl
        #Katrine Event Calls
        if katrinestage2event == 1 and katrine.stage >= 2 and tristastage1event == 0:
            phoneMessages = True
            phonegirl = 'Katrine'
            return
        elif katrinestage3event == 1 and katrine.stage >= 3 and tristastage2event == 0:
            phoneMessages = True
            phonegirl = 'Katrine'
            return
        elif katrinestage4event == 1 and katrine.stage >= 4 and tristastage4event == 0:
            phoneMessages = True
            phonegirl = 'Katrine'
            return
        elif katrinestage5event == 1 and katrine.stage >= 5 and trista.stage >= 5 and katrinestage4event == 0:
            phoneMessages = True
            phonegirl = 'Katrine'
            return
        elif katrinestage5phone == 1 and katrinestage5event == 0 and katrine.stage >= 5 and day != 4 and daytime == 3 and katrine_gym_today == 0:
            phoneMessages = True
            phonegirl = 'Katrine'
            return
        elif katrinestage6event == 1 and katrine.stage >= 6 and katrinestage5event == 0 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Katrine'
            return
        elif katrinestage6phone == 1 and katrinestage6event == 0 and katrine.stage >= 6:
            phoneMessages = True
            phonegirl = 'Katrine'
            return
        elif katrinestage7event == 1 and katrine.stage >= 7 and tristastage6event == 0:
            phoneMessages = True
            phonegirl = 'Katrine'
            return
        elif katrinestage10event == 1 and katrine.stage >= 10 and tristastage10event == 0:
            phoneMessages = True
            phonegirl = 'Katrine'
            return
        #Trista Event Calls
        if tristastage3phone == 1 and tristastage3event == 0 and trista.stage >= 3 and trista_gym_today == 0 and day == 6 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Trista'
            return
        elif tristastage4event == 1 and trista.stage >= 4 and katrine.stage >= 4 and tristastage3event == 0:
            phoneMessages = True
            phonegirl = 'Katrine'
            return
        elif tristastage6event == 1 and trista.stage >= 6 and katrinestage6event == 0:
            phoneMessages = True
            phonegirl = 'Trista'
            return
        elif tristastage7event == 1 and trista.stage >= 7 and katrinestage7event == 0:
            phoneMessages = True
            phonegirl = 'Trista'
            return
        elif tristastage8event == 1 and trista.stage >= 8 and katrinestage8event == 0 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Trista'
            return
        elif tristastage8phone == 1 and tristastage8event == 0 and trista.stage >= 8:
            phoneMessages = True
            phonegirl = 'Trista'
            return
        elif tristastage10event == 1 and trista.stage >= 10 and katrinestage9event == 0:
            phoneMessages = True
            phonegirl = 'Trista'
            return
        #Cayenne Event Calls
        if cayennestage7event == 1 and cayennestage6event == 0 and daycount3 >= 14 and cayenne.stage >= 7 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Cayenne'
            return
        if cayennestage9event == 1 and cayennestage8event == 0 and cayenne.stage >= 9 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Cayenne'
            return
        #Luna Event Calls
        if lunastage3event == 1 and luna.stage >= 3 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Luna'
            return
        elif lunastage4event == 1 and luna.stage >= 4 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Luna'
            return
        elif lunastage5event == 1 and luna.stage >= 5 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Luna'
            return
        elif lunastage6event == 1 and luna.stage >= 6 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Luna'
            return
        elif lunastage7event == 1 and luna.stage >= 7 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Luna'
            return
        elif lunastage8event == 1 and luna.stage >= 8 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Luna'
            return
        elif lunastage9event == 1 and luna.stage >= 9 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Luna'
            return
        elif lunastage10event == 1 and luna.stage >= 10 and daytime == 2 and day == 3:
            phoneMessages = True
            phonegirl = 'Luna'
            return
        elif lunastage10event2 == 1 and lunastage10event == 0 and daytime == 2 and day == 3:
            phoneMessages = True
            phonegirl = 'Luna'
            return
        elif lunastage11event == 1 and luna.stage >= 11 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Luna'
            return
        elif lunastage12event == 1 and lunastage11event == 0 and luna.stage >= 12 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Luna'
            return
        #Natalie Event Calls
        if nataliestage3event == 1 and lunastage10event2 == 0 and daytime == 2 and day == 3:
            phoneMessages = True
            phonegirl = 'Britta'
            return
        elif nataliestage4event2 == 1 and lunastage12event == 0 and nataliestage4event == 0 and daytime == 2 and day == 3:
            phoneMessages = True
            phonegirl = 'Natalie'
            return
        #Britta Event Calls
        if brittastage4event == 1 and lunastage11event == 0 and daytime == 2 and day == 3:
            phoneMessages = True
            phonegirl = 'Britta'
            return
        #Sally Event Calls
        if sallystage4event == 1 and sallystage3event == 0 and lunastage11event == 0 and daytime == 2 and day == 1:
            phoneMessages = True
            phonegirl = 'Sally'
            return
        #Roxie Event Calls
        if roxiestage4event == 1 and lunastage11event == 0 and daytime == 1 and day == 6:
            phoneMessages = True
            phonegirl = 'Roxie'
            return
        #Leanne/Lyn Calls
        if leannestage6event == 1 and leanne.stage >= 6 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Leanne'
            return
        elif leannestage7event == 1 and leanne.stage >= 7 and daytime == 1:
            phoneMessages = True
            phonegirl = 'Leanne'
            return
        elif leannestage8event == 1 and leanne.stage >= 8 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Leanne'
            return
        elif leannestage9event == 1 and leanne.stage >= 9 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Leanne'
            return
        elif leannestage10event == 1 and leanne.stage >= 10 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Leanne'
            return
        elif leannestage10event2 == 1 and leannestage10event == 0 and leanne.stage >= 10 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Leanne'
            return
        elif leanne.stage >= 11 and leannestage11event == 1 and leannestage10event2 == 0 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Leanne'
            return
        elif leannestage12event == 1 and leannestage11event4 == 0 and leanne.stage >= 11 and daytime == 3 and daycount >= 14:
            phoneMessages = True
            if leannechoice == 1:
                phonegirl = 'Lyn'
                return
            else:
                phonegirl = 'Leanne'
                return
        elif leannestage12event2 == 1 and leanne.stage >= 12 and daytime == 2 and leannestage12event == 0:
            phoneMessages = True
            if leannechoice == 1:
                phonegirl = 'Lyn'
                return
            else:
                phonegirl = 'Leanne'
                return
        elif leannestage13event == 1 and leanne.stage >= 13 and daytime == 2 and leannestage12event3 == 0:
            phoneMessages = True
            if leannechoice == 1:
                phonegirl = 'Lyn'
                return
            else:
                phonegirl = 'Leanne'
                return
        elif leannestage13event3 == 1 and leanne.stage >= 13 and daytime == 3 and leannestage13event2 == 0:
            phoneMessages = True
            if leannechoice == 1:
                phonegirl = 'Lyn'
                return
            else:
                phonegirl = 'Leanne'
                return
        #Bonnie Calls
        if bonnieintroduction == 0 and bonniestage1event == 1 and day == 3 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return
        elif bonniestage2event == 1 and bonnie.stage >= 2 and day == 3 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return
        elif bonniestage2event == 0 and bonniestage2event2 == 1 and sweettoothvol1 == 1 and day == 3 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return
        elif bonniestage3event == 1 and bonniestage2event2 == 0 and bonnie.stage >= 3 and day == 3 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return
        elif bonniestage4event == 1 and bonnie.stage >= 4 and day == 3 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return
        elif bonniestage5event == 1 and bonnie.stage >= 5 and day == 3 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return
        elif bonniestage6event == 1 and bonnie.stage >= 6 and day == 3 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return
        elif bonniestage7event == 1 and bonnie.stage >= 7 and day == 3 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return
        elif bonniestage8event == 1 and bonnie.stage >= 8 and day == 3 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return
        elif bonniestage9event == 1 and bonnie.stage >= 9 and sweettoothvol2 == 1 and day == 3 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return
        elif bonniestage10event == 1 and bonnie.stage >= 10 and day == 3 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return
        elif bonniestage10phone == 1 and bonniestage10event == 0 and bonnie.stage >= 10 and day != 3 and daytime == 3 and worked_today == 0:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return
        elif bonniestage11event == 1 and bonnie.stage >= 11 and day == 3 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return
        #Rebecca Calls
        if rebeccastage2event == 1 and bonniestage11event == 0 and rebecca.stage >= 2 and day == 2 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Unknown'
            return
        elif rebeccastage3phone == 1 and rebeccastage3event == 0 and rebecca.stage >= 3 and day != 3 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Rebecca'
            return
        #Hari Event Calls
        if haristage3event2 == 0 and haristage4event == 1 and hari.stage >= 4 and day == 7 and daytime == 1:
            phoneMessages = True
            phonegirl = 'Hari'
            return
        elif haristage4event3 == 0 and haristage5event == 1 and hari.stage >= 5 and daycount2 >= 14 and daytime == 1:
            phoneMessages = True
            phonegirl = 'Hari'
            return
        elif haristage6event == 0 and haristage6event2 == 1 and hari.stage >= 6 and day == 7 and daytime == 1:
            phoneMessages = True
            phonegirl = 'Hari'
            return
        elif haristage6event2 == 0 and haristage7event == 1 and hari.stage >= 7 and day == 6 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Hari'
            return
        #Caroline Event Calls
        if carolinestage2event2 == 0 and carolinestage2event3 == 1 and caroline.stage >= 2 and day >= 6 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Caroline'
            return
        elif carolinestage2event4 == 0 and carolinestage3event == 1 and caroline.stage >= 3 and day >= 6 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Caroline'
            return
        #Marie Event Calls
        if mariestage0event == 1 and workunlock == 1 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Marie'
            return
        elif mariestage2event == 1 and marie.stage >= 2 and lisastage2event2 == 0 and daytime == 2 and day == 1:
            phoneMessages = True
            phonegirl = 'Marie'
            return
        elif mariestage3event == 1 and mariestage3eventtrigger == 1 and mayastage1event == 0 and lisastage3event == 0 and daytime == 2 and day == 1:
            phoneMessages = True
            phonegirl = 'Marie'
            return
        elif mariestage3event2 == 1 and mariestage3event == 0 and lisastage4event2 == 0 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Marie'
            return
        #elif mariestage5event == 1 and mariestage4event2 == 0 and marie.stage >= 5 and lisa.stage >= 7 and amber.stage >= 6 and daytime == 2:
        #    phoneMessages = True
        #    $ phonegirl = "Marie"
        #    return
        #Maya Event Calls
        if mayastage1event == 1 and amberstage2event2 == 0 and daytime == 2 and day == 5:
            phoneMessages = True
            phonegirl = 'Amber'
            return
        elif mayastage1event2 == 1 and mayastage1event == 0 and daytime == 2 and day == 4:
            phoneMessages = True
            phonegirl = 'Amber'
            return
        elif mayastage1event3 == 1 and mayastage1event2 == 0 and daytime == 3 and day == 3:
            phoneMessages = True
            phonegirl = 'Maya'
            return
        elif mayastage2event == 1 and mayastage1event3 == 0 and daytime == 3 and day == 2:
            phoneMessages = True
            phonegirl = 'Maya'
            return
        elif mayastage2event2 == 1 and mayastage2event == 0 and daytime == 3 and day == 1:
            phoneMessages = True
            phonegirl = 'Maya'
            return
        elif mayastage2event3 == 1 and mayastage2event2 == 0 and daytime == 3 and day == 7:
            phoneMessages = True
            phonegirl = 'Maya'
            return
        elif mayastage2event4 == 1 and mayastage2event3 == 0 and daytime == 1 and day == 7:
            phoneMessages = True
            phonegirl = 'Amber'
            return
        elif mayastage3event == 1 and mayastage2event4 == 0 and daytime == 3 and day == 6:
            phoneMessages = True
            phonegirl = 'Maya'
            return
        elif mayastage3event3 == 1 and mayastage3event2 == 0 and daytime == 3 and day == 6:
            phoneMessages = True
            phonegirl = 'Maya'
            return
        elif mayastage4event == 1 and mayastage3event3 == 0 and daytime == 3 and day == 5:
            phoneMessages = True
            phonegirl = 'Maya'
            return
        elif mayastage4event2 == 1 and mayastage4event == 0 and daytime == 3 and day == 4:
            phoneMessages = True
            phonegirl = 'Maya'
            return
        elif mayastage5event2 == 1 and mayastage5event == 0 and daytime == 3 and day == 6:
            phoneMessages = True
            phonegirl = 'Maya'
            return
        elif mayastage5event5 == 1 and mayastage5event4 == 0 and daytime == 3 and day == 4:
            phoneMessages = True
            phonegirl = 'Maya'
            return
        #Amber Event Calls
        if amberstage0event == 1 and mariestage0event == 0 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Marie'
            return
        elif amberstage3event == 1 and mayastage1event == 0 and amber.stage >= 3 and daytime == 1:
            phoneMessages = True
            phonegirl = 'Amber'
            return
        elif amberstage5event2 == 1 and amberstage5event == 0 and daytime == 1:
            phoneMessages = True
            phonegirl = 'Amber'
            return
        #Lisa Event Calls
        if lisastage0event == 1 and amberstage0event == 0 and daytime == 3 and worked_today == 0:
            phoneMessages = True
            phonegirl = 'Marie'
            return
        elif lisastage3event == 1 and lisa.stage >= 3 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Lisa'
            return
        #Daisy Event Calls
        if teacherstage15event == 1 and teacher.stage >= 15 and daytime == 2 and day == 4:
            phoneMessages = True
            phonegirl = 'Daisy'
            return

        #Bonnie calls every Wednesday for you to make chocolates and feed her some(happens after stage2 event).
        if bonnie.stage >= 2 and day == 3 and bonniestage2event2 == 0 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Bonnie'
            return

        #Luna calls every tuesday for her sex scene at her home after she reaches stage3(Daisy stage 9 event triggers this).
        if teacherstage5event == 0 and luna.stage >= 3 and day == 2 and daytime == 3:
            phoneMessages = True
            phonegirl = 'Luna'
            return

        #Katrine calls every thursday to go on a date with you that can lead to going to her home.(available when you get your strength to 5 and visit her in the gym)
        if katrine.stage >= 2 and day == 4 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Katrine'
            return

        #Trista calls every Saturday to work out together
        if trista.stage >= 2 and tristastage2event == 0 and day == 6 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Trista'
            return

        #Leanne calls every monday to go and stuff her face(happens after stage7)
        if leanne.stage >= 6 and leannestage6event == 0 and leannestage11event2 == 1 and day == 1 and daytime == 2:
            phoneMessages = True
            phonegirl = 'Leanne'
            return

        if leanne.stage >= 12 and day == 1 and daytime == 2 and leannechoice == 1 and leannestage12event2 == 0:
            phoneMessages = True
            phonegirl = 'Lyn'
            return

        if leanne.stage >= 12 and day == 1 and daytime == 2 and leannechoice == 2 and leannestage12event2 == 0:
            phoneMessages = True
            phonegirl = 'Leanne'
            return

        #Lisa calls every Saturday evening if she hasn't working with you that day
        if lisa.stage >= 3 and daytime == 3 and lisastage3event == 0:
            if day == 6:
                if rngworkgirl == 1 or rngworkgirl == 3:
                    phoneMessages = True
                    phonegirl = 'Lisa'
                    return
                return
            return
        return

label Phone_calls:
    #Mandatory phone calls go in here.
    if mayastage1event == 1 and amberstage2event2 == 0 and daytime == 2 and day == 5:
        stop music fadeout 1.0
        call Maya_Stage_1_Event_1 from _call_Maya_Stage_1_Event_1
        jump freetime
    elif mayastage1event2 == 1 and mayastage1event == 0 and daytime == 2 and day == 4:
        stop music fadeout 1.0
        call Maya_Stage_1_Event_2 from _call_Maya_Stage_1_Event_2
        jump freetime
    elif lunastage6event == 1 and luna.stage >= 6 and daytime == 2:
        stop music fadeout 1.0
        call Luna_Stage_6_Event from _call_Luna_Stage_6_Event
        jump freetime
    elif haristage4event3 == 0 and haristage5event == 1 and hari.stage >= 5 and daycount2 >= 14 and daytime == 1:
        stop music fadeout 1.0
        call Hari_Stage_5_Event from _call_Hari_Stage_5_Event
        jump freetime
    elif mayastage2event4 == 1 and mayastage2event3 == 0 and daytime == 1 and day == 7:
        stop music fadeout 1.0
        call Maya_Stage_2_Event_4 from _call_Maya_Stage_2_Event_4
        jump freetime
    elif lunastage8event == 1 and luna.stage >= 8 and daytime == 2:
        stop music fadeout 1.0
        call Luna_Stage_8_Event from _call_Luna_Stage_8_Event
        jump freetime
    elif lunastage10event == 1 and luna.stage >= 10 and daytime == 2 and day == 3:
        stop music fadeout 1.0
        call Luna_Stage_10_Event_1 from _call_Luna_Stage_10_Event_1
        jump freetime
    elif lunastage10event2 == 1 and lunastage10event == 0 and daytime == 2 and day == 3:
        stop music fadeout 1.0
        call Luna_Stage_10_Event_2 from _call_Luna_Stage_10_Event_2_1
        jump freetime
    elif lunastage11event == 1 and luna.stage >= 11 and daytime == 2:
        stop music fadeout 1.0
        call Luna_Stage_11_Event from _call_Luna_Stage_11_Event_1
        jump freetime
    elif lunastage12event == 1 and lunastage11event == 0 and luna.stage >= 12 and daytime == 2:
        stop music fadeout 1.0
        call Luna_Stage_12_Event
        jump freetime
    elif nataliestage4event2 == 1 and lunastage12event == 0 and nataliestage4event == 0 and daytime == 2 and day == 3:
        stop music fadeout 1.0
        call Natalie_Stage_4_Event_2
        jump freetime
    elif sallystage4event == 1 and sallystage3event == 0 and lunastage11event == 0 and daytime == 2 and day == 1:
        stop music fadeout 1.0
        call Sally_Stage_4_Event from _call_Sally_Stage_4_Event
        jump freetime
    elif mayastage5event4 == 1 and mayastage5event3 == 0 and daytime == 3 and day == 5:
        stop music fadeout 1.0
        call Maya_Stage_5_Event_4
        jump freetime
    elif mayastage6event == 1 and mayastage5event5 == 0 and daytime == 3 and daycount5 >= 14:
        stop music fadeout 1.0
        call Maya_Stage_6_Event
        jump freetime
    elif mariestage0event == 1 and workunlock == 1 and daytime == 2:
        stop music fadeout 1.0
        call Marie_Stage_0_Event from _call_Marie_Stage_0_Event
        jump freetime
    elif amberstage0event == 1 and mariestage0event == 0 and daytime == 2:
        stop music fadeout 1.0
        call Amber_Stage_0_Event from _call_Amber_Stage_0_Event
        jump freetime
    elif lisastage0event == 1 and amberstage0event == 0 and daytime == 3 and worked_today == 0:
        stop music fadeout 1.0
        call Lisa_Stage_0_Event from _call_Lisa_Stage_0_Event
        jump freetime
    elif leannestage6event == 1 and leanne.stage >= 6 and daytime == 2:
        stop music fadeout 1.0
        call Leanne_Stage_6_Event_1
        jump freetime
    elif leanne.stage >= 10 and leannestage10event == 0 and leannestage10event2 == 1 and daytime == 3:
        stop music fadeout 1.0
        call Leanne_Stage_10_Event_2
        jump freetime
    elif leanne.stage >= 11 and leannestage11event == 1 and leannestage10event2 == 0 and daytime == 3:
        stop music fadeout 1.0
        call Leanne_Stage_11_Event_1
        jump freetime
    elif bonniestage10phone == 1 and bonniestage10event == 0 and bonnie.stage >= 10 and day != 3 and daytime == 3 and worked_today == 0:
        stop music fadeout 1.0
        call BonnieStage10Phone
        jump freetime
    elif rebeccastage3phone == 1 and rebeccastage3event == 0 and rebecca.stage >= 3 and day != 3 and daytime == 3:
        stop music fadeout 1.0
        call RebeccaStage3Phone
        jump freetime
    elif lisastage4phone == 1 and lisastage4event2 == 0 and lisa.stage >= 4:
        stop music fadeout 1.0
        call LisaStage4Phone
        jump freetime
    elif tristastage3phone == 1 and tristastage3event == 0 and trista.stage >= 3 and trista_gym_today == 0 and day == 6 and daytime == 3:
        stop music fadeout 1.0
        call TristaStage3Phone
        jump freetime
    elif tristastage8phone == 1 and tristastage8event == 0 and trista.stage >= 8:
        stop music fadeout 1.0
        call TristaStage8Phone
        jump freetime
    elif katrinestage5phone == 1 and katrinestage5event == 0 and katrine.stage >= 5 and day != 4 and daytime == 3 and katrine_gym_today == 0:
        stop music fadeout 1.0
        call KatrineStage5Phone
        jump freetime
    elif katrinestage6phone == 1 and katrinestage6event == 0 and katrine.stage >= 6:
        stop music fadeout 1.0
        call KatrineStage6Phone
        jump freetime
        return
    $ checkPhone()
    return

label view_phone:
    #Optional phone calls go in here.
    $ phoneMessages = False
    #Katrine Event Calls
    if katrinestage2event == 1 and katrine.stage >= 2 and tristastage1event == 0:
        stop music fadeout 1.0
        call Katrine_Stage_2_Event from _call_Katrine_Stage_2_Event_2
        if phonecall == 1:
            jump freetime
        return
    elif katrinestage3event == 1 and katrine.stage >= 3 and tristastage2event == 0:
        stop music fadeout 1.0
        call Katrine_Stage_3_Event from _call_Katrine_Stage_3_Event
        if phonecall == 1:
            jump freetime
        return
    elif katrinestage4event == 1 and katrine.stage >= 4 and tristastage4event == 0:
        stop music fadeout 1.0
        call Katrine_Stage_4_Event from _call_Katrine_Stage_4_Event
        if phonecall == 1:
            jump freetime
        return
    elif katrinestage5event == 1 and katrine.stage >= 5 and trista.stage >= 5 and katrinestage4event == 0:
        stop music fadeout 1.0
        call Katrine_Stage_5_Event from _call_Katrine_Stage_5_Event
        if phonecall == 1:
            jump freetime
        return
    elif katrinestage6event == 1 and katrine.stage >= 6 and katrinestage5event == 0 and daytime == 3:
        stop music fadeout 1.0
        call Katrine_Stage_6_Event from _call_Katrine_Stage_6_Event
        if phonecall == 1:
            jump freetime
        return
    elif katrinestage7event == 1 and katrine.stage >= 7 and tristastage6event == 0:
        stop music fadeout 1.0
        call Katrine_Stage_7_Event from _call_Katrine_Stage_7_Event
        if phonecall == 1:
            jump freetime
        return
    elif katrinestage10event == 1 and katrine.stage >= 10 and tristastage10event == 0:
        stop music fadeout 1.0
        call Katrine_Stage_10_Event from _call_Katrine_Stage_10_Event
        if phonecall == 1:
            jump freetime
        return
    #Trista Event Calls
    if tristastage4event == 1 and trista.stage >= 4 and katrine.stage >= 4 and tristastage3event == 0:
        stop music fadeout 1.0
        call Trista_Stage_4_Event from _call_Trista_Stage_4_Event
        if phonecall == 1:
            jump freetime
        return
    elif tristastage6event == 1 and trista.stage >= 6 and katrinestage6event == 0:
        stop music fadeout 1.0
        call Trista_Stage_6_Event from _call_Trista_Stage_6_Event
        if phonecall == 1:
            jump freetime
        return
    elif tristastage7event == 1 and trista.stage >= 7 and katrinestage7event == 0:
        stop music fadeout 1.0
        call Trista_Stage_7_Event from _call_Trista_Stage_7_Event
        if phonecall == 1:
            jump freetime
        return
    elif tristastage8event == 1 and trista.stage >= 8 and katrinestage8event == 0 and daytime == 2:
        stop music fadeout 1.0
        call Trista_Stage_8_Event from _call_Trista_Stage_8_Event
        if phonecall == 1:
            jump freetime
        return
    elif tristastage10event == 1 and trista.stage >= 10 and katrinestage9event == 0:
        stop music fadeout 1.0
        call Trista_Stage_10_Event from _call_Trista_Stage_10_Event
        if phonecall == 1:
            jump freetime
        return
    #Cayenne Event Calls
    if cayennestage7event == 1 and cayennestage6event == 0 and daycount3 >= 14 and daytime == 2:
        stop music fadeout 1.0
        call Cayenne_Stage_7_Event from _call_Cayenne_Stage_7_Event
        if phonecall == 1:
            jump freetime
        return
    elif cayennestage9event == 1 and cayennestage8event == 0 and cayenne.stage >= 9 and daytime == 2:
        stop music fadeout 1.0
        call Cayenne_Stage_9_Event from _call_Cayenne_Stage_9_Event
        if phonecall == 1:
            jump freetime
        return
    #Luna Event Calls
    if lunastage3event == 1 and luna.stage >= 3 and daytime == 2:
        stop music fadeout 1.0
        call Luna_Stage_3_Event from _call_Luna_Stage_3_Event
        if phonecall == 1:
            jump freetime
        return
    elif lunastage4event == 1 and luna.stage >= 4 and daytime == 2:
        stop music fadeout 1.0
        call Luna_Stage_4_Event from _call_Luna_Stage_4_Event
        if phonecall == 1:
            jump freetime
        return
    elif lunastage5event == 1 and luna.stage >= 5 and daytime == 2:
        stop music fadeout 1.0
        call Luna_Stage_5_Event from _call_Luna_Stage_5_Event
        if phonecall == 1:
            jump freetime
        return
    elif lunastage7event == 1 and luna.stage >= 7 and daytime == 2:
        stop music fadeout 1.0
        call Luna_Stage_7_Event from _call_Luna_Stage_7_Event
        if phonecall == 1:
            jump freetime
        return
    elif lunastage9event == 1 and luna.stage >= 9 and daytime == 2:
        stop music fadeout 1.0
        call Luna_Stage_9_Event from _call_Luna_Stage_9_Event
        if phonecall == 1:
            jump freetime
        return
    elif nataliestage3event == 1 and lunastage10event2 == 0 and daytime == 2 and day == 3:
        stop music fadeout 1.0
        call Natalie_Stage_3_Event from _call_Natalie_Stage_3_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif brittastage4event == 1 and lunastage11event == 0 and daytime == 2 and day == 3:
        stop music fadeout 1.0
        call Britta_Stage_4_Event from _call_Britta_Stage_4_Event
        if phonecall == 1:
            jump freetime
        return
    elif roxiestage4event == 1 and lunastage11event == 0 and daytime == 1 and day == 6:
        stop music fadeout 1.0
        call Roxie_Stage_4_Event
        if phonecall == 1:
            jump freetime
        return
    #LEANNE EVENTS
    if leannestage7event == 1 and leanne.stage >= 7 and daytime == 1:
        stop music fadeout 1.0
        call Leanne_Stage_7_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif leannestage8event == 1 and leanne.stage >= 8 and daytime == 3:
        stop music fadeout 1.0
        call Leanne_Stage_8_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif leannestage9event == 1 and leanne.stage >= 9 and daytime == 2:
        stop music fadeout 1.0
        call Leanne_Stage_9_Event from _call_Leanne_Stage_9_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif leannestage10event == 1 and leanne.stage >= 10 and daytime == 3:
        stop music fadeout 1.0
        call Leanne_Stage_10_Event from _call_Leanne_Stage_10_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif leannestage12event == 1 and leannestage11event4 == 0 and leanne.stage >= 11 and daytime == 3 and daycount >= 14:
        stop music fadeout 1.0
        call Leanne_Stage_12_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif leannestage12event2 == 1 and leanne.stage >= 12 and daytime == 2 and leannestage12event == 0:
        stop music fadeout 1.0
        call Leanne_Stage_12_Event_2 from _call_Leanne_Stage_12_Event_2_1
        if phonecall == 1:
            jump freetime
        return
    elif leannestage13event == 1 and leanne.stage >= 13 and daytime == 2 and leannestage12event3 == 0:
        stop music fadeout 1.0
        call Leanne_Stage_13_Event from _call_Leanne_Stage_13_Event
        if phonecall == 1:
            jump freetime
        return
    elif leannestage13event3 == 1 and leanne.stage >= 13 and daytime == 3 and leannestage13event2 == 0:
        stop music fadeout 1.0
        call Leanne_Stage_13_Event_3
        if phonecall == 1:
            jump freetime
        return
    #BONNIE EVENTS
    if bonnieintroduction == 0 and bonniestage1event == 1 and day == 3 and daytime == 3:
        stop music fadeout 1.0
        call Bonnie_Stage_1_Event from _call_Bonnie_Stage_1_Event
        if phonecall == 1:
            jump freetime
        return
    elif bonniestage2event == 1 and bonnie.stage >= 2 and day == 3 and daytime == 3:
        stop music fadeout 1.0
        call Bonnie_Stage_2_Event_1 from _call_Bonnie_Stage_2_Event_1_1
        if phonecall == 1:
            jump freetime
        return
    elif bonniestage2event == 0 and bonniestage2event2 == 1 and sweettoothvol1 == 1 and day == 3 and daytime == 3:
        stop music fadeout 1.0
        call Bonnie_Stage_2_Event_2 from _call_Bonnie_Stage_2_Event_2_1
        if phonecall == 1:
            jump freetime
        return
    elif bonniestage3event == 1 and bonniestage2event2 == 0 and bonnie.stage >= 3 and day == 3 and daytime == 3:
        stop music fadeout 1.0
        call Bonnie_Stage_3_Event from _call_Bonnie_Stage_3_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif bonniestage4event == 1 and bonnie.stage >= 4 and day == 3 and daytime == 2:
        stop music fadeout 1.0
        call Bonnie_Stage_4_Event from _call_Bonnie_Stage_4_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif bonniestage5event == 1 and bonnie.stage >= 5 and day == 3 and daytime == 3:
        stop music fadeout 1.0
        call Bonnie_Stage_5_Event from _call_Bonnie_Stage_5_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif bonniestage6event == 1 and bonnie.stage >= 6 and day == 3 and daytime == 3:
        stop music fadeout 1.0
        call Bonnie_Stage_6_Event from _call_Bonnie_Stage_6_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif bonniestage7event == 1 and bonnie.stage >= 7 and day == 3 and daytime == 3:
        stop music fadeout 1.0
        call Bonnie_Stage_7_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif bonniestage8event == 1 and bonnie.stage >= 8 and day == 3 and daytime == 3:
        stop music fadeout 1.0
        call Bonnie_Stage_8_Event from _call_Bonnie_Stage_8_Event
        if phonecall == 1:
            jump freetime
        return
    elif bonniestage9event == 1 and bonnie.stage >= 9 and sweettoothvol2 == 1 and day == 3 and daytime == 3:
        stop music fadeout 1.0
        call Bonnie_Stage_9_Event from _call_Bonnie_Stage_9_Event
        if phonecall == 1:
            jump freetime
        return
    elif bonniestage10event == 1 and bonnie.stage >= 10 and day == 3 and daytime == 2:
        stop music fadeout 1.0
        call Bonnie_Stage_10_Event from _call_Bonnie_Stage_10_Event
        if phonecall == 1:
            jump freetime
        return
    elif bonniestage11event == 1 and bonnie.stage >= 11 and day == 3 and daytime == 2:
        stop music fadeout 1.0
        call Bonnie_Stage_11_Event from _call_Bonnie_Stage_11_Event
        if phonecall == 1:
            jump freetime
        return
    #Rebecca Calls
    if rebeccastage2event == 1 and bonniestage11event == 0 and rebecca.stage >= 2 and day == 2 and daytime == 2:
        stop music fadeout 1.0
        call Rebecca_Stage_2_Event
        if phonecall == 1:
            jump freetime
        return
    #Hari Event Calls
    if haristage3event2 == 0 and haristage4event == 1 and hari.stage >= 4 and day == 7 and daytime == 1:
        stop music fadeout 1.0
        call Hari_Stage_4_Event_1 from _call_Hari_Stage_4_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif haristage6event == 0 and haristage6event2 == 1 and hari.stage >= 6 and day == 7 and daytime == 1:
        stop music fadeout 1.0
        call Hari_Stage_6_Event_2 from _call_Hari_Stage_6_Event_2
        if phonecall == 1:
            jump freetime
        return
    elif haristage6event2 == 0 and haristage7event == 1 and hari.stage >= 7 and day == 6 and daytime == 3:
        stop music fadeout 1.0
        call Hari_Stage_7_Event from _call_Hari_Stage_7_Event
        if phonecall == 1:
            jump freetime
        return
    #Caroline Event Calls
    if carolinestage2event2 == 0 and carolinestage2event3 == 1 and caroline.stage >= 2 and day >= 6 and daytime == 2:
        stop music fadeout 1.0
        call Caroline_Stage_2_Event_3
        if phonecall == 1:
            jump freetime
        return
    elif carolinestage2event4 == 0 and carolinestage3event == 1 and caroline.stage >= 3 and day >= 6 and daytime == 2:
        stop music fadeout 1.0
        call Caroline_Stage_3_Event
        if phonecall == 1:
            jump freetime
        return
    #Marie Event Calls
    if mariestage2event == 1 and marie.stage >= 2 and lisastage2event == 0 and daytime == 2 and day == 1:
        stop music fadeout 1.0
        call Marie_Stage_2_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif mariestage3event == 1 and mariestage2event2 == 0 and mariestage3eventtrigger == 1 and mayastage1event == 0 and lisastage3event == 0 and daytime == 2 and day == 1:
        stop music fadeout 1.0
        call Marie_Stage_3_Event_1 from _call_Marie_Stage_3_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif mariestage3event2 == 1 and mariestage3event == 0 and lisastage4event2 == 0 and daytime == 2:
        stop music fadeout 1.0
        call Marie_Stage_3_Event_2 from _call_Marie_Stage_3_Event_2
        if phonecall == 1:
            jump freetime
        return
    #elif mariestage5event == 1 and mariestage4event2 == 0 and marie.stage >= 5 and lisa.stage >= 7 and amber.stage >= 6 and daytime == 2:
    #    stop music fadeout 1.0
    #    call Marie_Stage_5_Event from _call_Marie_Stage_5_Event
    #    if phonecall == 1:
    #        jump freetime
    #    return
    #Maya Event Calls
    if mayastage1event3 == 1 and mayastage1event2 == 0 and daytime == 3 and day == 3:
        stop music fadeout 1.0
        call Maya_Stage_1_Event_3 from _call_Maya_Stage_1_Event_3
        if phonecall == 1:
            jump freetime
        return
    elif mayastage2event == 1 and mayastage1event3 == 0 and daytime == 3 and day == 2:
        stop music fadeout 1.0
        call Maya_Stage_2_Event_1 from _call_Maya_Stage_2_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif mayastage2event2 == 1 and mayastage2event == 0 and daytime == 3 and day == 1:
        stop music fadeout 1.0
        call Maya_Stage_2_Event_2 from _call_Maya_Stage_2_Event_2
        if phonecall == 1:
            jump freetime
        return
    elif mayastage2event3 == 1 and mayastage2event2 == 0 and daytime == 3 and day == 7:
        stop music fadeout 1.0
        call Maya_Stage_2_Event_3 from _call_Maya_Stage_2_Event_3
        if phonecall == 1:
            jump freetime
        return
    elif mayastage3event == 1 and mayastage2event4 == 0 and daytime == 3 and day == 6:
        stop music fadeout 1.0
        call Maya_Stage_3_Event_1 from _call_Maya_Stage_3_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif mayastage3event3 == 1 and mayastage3event2 == 0 and daytime == 3 and day == 6:
        stop music fadeout 1.0
        call Maya_Stage_3_Event_3 from _call_Maya_Stage_3_Event_3
        if phonecall == 1:
            jump freetime
        return
    elif mayastage4event == 1 and mayastage3event3 == 0 and daytime == 3 and day == 5:
        stop music fadeout 1.0
        call Maya_Stage_4_Event_1 from _call_Maya_Stage_4_Event_1
        if phonecall == 1:
            jump freetime
        return
    elif mayastage4event2 == 1 and mayastage4event == 0 and daytime == 3 and day == 4:
        stop music fadeout 1.0
        call Maya_Stage_4_Event_2 from _call_Maya_Stage_4_Event_2
        if phonecall == 1:
            jump freetime
        return
    elif mayastage5event2 == 1 and mayastage5event == 0 and daytime == 3 and day == 6:
        stop music fadeout 1.0
        call Maya_Stage_5_Event_2 from _call_Maya_Stage_5_Event_2
        if phonecall == 1:
            jump freetime
        return
    elif mayastage5event5 == 1 and mayastage5event4 == 0 and daytime == 3 and day == 4:
        stop music fadeout 1.0
        call Maya_Stage_5_Event_5
        if phonecall == 1:
            jump freetime
        return
    #Amber Event Calls
    if amberstage3event == 1 and mayastage1event == 0 and daytime == 1:
        stop music fadeout 1.0
        call Amber_Stage_3_Event from _call_Amber_Stage_3_Event
        if phonecall == 1:
            jump freetime
        return
    elif amberstage5event2 == 1 and amberstage5event == 0 and daytime == 1:
        stop music fadeout 1.0
        call Amber_Stage_5_Event_2 from _call_Amber_Stage_5_Event_2
        if phonecall == 1:
            jump freetime
        return
    #Lisa Event Calls
    if lisastage3event == 1 and lisa.stage >= 3 and daytime == 3:
        stop music fadeout 1.0
        call Lisa_Stage_3_Event_1
        if phonecall == 1:
            jump freetime
        return
    #Daisy Event Calls
    if teacherstage15event == 1 and teacher.stage >= 15 and daytime == 2 and day == 4:
        stop music fadeout 1.0
        call Teacher_Stage_15_Event from _call_Teacher_Stage_15_Event
        if phonecall == 1:
            jump freetime
        return

    #Bonnie calls every Wednesday for you to make chocolates and feed her some(happens after stage2 event).
    if bonnie.stage >= 2 and day == 3 and bonniestage2event2 == 0 and daytime == 3:
        stop music fadeout 1.0
        $ show_messenger()

        $ dialogue_one = []
        if bonnie.stage >= 9:
            $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
            $ msg ("Hi. Are you free tonight to help out with the shop?", who=1)
            pause
            menu:
                "Yes.":
                    $ msg ("Sure, I'll be there in a minute.")
                    pause
                    $ hide_messenger()
                    call bonnie_home4 from _call_bonnie_home4
                    $ daytime += 1
                    jump freetime

                "Not tonight.":
                    $ msg ("Sorry, I’m a little busy tonight.")
                    pause
                    $ msg ("Alright. I’ll catch you some other time.", who=1)
                    pause
                    $ hide_messenger()
                    return

        elif bonnie.stage == 7 or bonnie.stage == 8:
            $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
            $ msg ("Hi. Are you free tonight to help out with the shop?", who=1)
            pause
            menu:
                "Yes.":
                    $ msg ("Sure, I'll be there in a minute.")
                    pause
                    $ hide_messenger()
                    call bonnie_home3 from _call_bonnie_home3
                    $ daytime += 1
                    jump freetime

                "Not tonight.":
                    $ msg ("Sorry, I’m a little busy tonight.")
                    pause
                    $ msg ("Alright. I’ll catch you some other time.", who=1)
                    pause
                    $ hide_messenger()
                    return
        elif bonnie.stage == 6:
            $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
            $ msg ("Hi, are you free tonight?", who=1)
            pause
            menu:
                "Yes.":
                    $ msg ("Sure, I'll be there in a minute.")
                    pause
                    $ msg ("You should know where to go by now, so feel free to let yourself in.", who=1)
                    pause
                    $ hide_messenger()
                    call bonnie_home1 from _call_bonnie_home1
                    $ daytime += 1
                    jump freetime

                "Not tonight.":
                    $ msg ("Sorry, I’m a little busy tonight.")
                    pause
                    $ msg ("Alright. I’ll catch you some other time.", who=1)
                    pause
                    $ hide_messenger()
                    return
        elif bonnie.stage >= 4:
            $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
            $ msg ("Hi, are you free tonight? I’ve restocked everything you will need to make those chocolates.", who=1)
            pause
            menu:
                "Yes.":
                    $ msg ("Sure, I'll be there in a minute.")
                    pause
                    $ hide_messenger()
                    call bonnie_home1 from _call_bonnie_home1_1
                    $ daytime += 1
                    jump freetime

                "Not tonight.":
                    $ msg ("Sorry, I’m a little busy tonight.")
                    pause
                    $ msg ("Alright. I’ll catch you some other time.", who=1)
                    pause
                    $ hide_messenger()
                    return

        else:
            $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
            $ msg ("Hi, thank you for offering to help. I think I have everything ready if you are free today?", who=1)
            pause
            menu:
                "Yes.":
                    $ msg ("Sure, I'll be there in a minute.")
                    pause
                    $ hide_messenger()
                    call bonnie_home1 from _call_bonnie_home1_2
                    $ daytime += 1
                    jump freetime

                "Not tonight.":
                    $ msg ("Sorry, I’m a little busy tonight.")
                    pause
                    $ msg ("Alright. I’ll catch you some other time.", who=1)
                    pause
                    $ hide_messenger()
                    return


    #Luna calls every tuesday for her sex scene at her home after she reaches stage3(Daisy stage 5 event triggers this).
    if teacherstage5event == 0 and luna.stage >= 3 and day == 2 and daytime == 3:
        stop music fadeout 1.0
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Luna', dialogue=dialogue_one)
        $ msg ("Hey, hottie. Do you want to hang out this evening?", who=1)
        pause
        $ msg ("Do some sexy stuff together?", who=1)
        menu:
            "Go over to Luna's home.":
                $ hide_messenger()
                call Luna_home_new
                $ daytime += 1
                jump freetime
            "Do something else.":
                $ msg ("Sorry, I'm really busy today.")
                pause
                $ msg ("Alright, another time.", who=1)
                pause
                $ hide_messenger()
                return

    #Katrine calls every thursday to go on a date with you that can lead to going to her home.(available when you get your strength to 5 and visit her in the gym)
    if katrine.stage >= 2 and day == 4 and daytime == 2:
        stop music fadeout 1.0
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Katrine', dialogue=dialogue_one)
        $ msg ("Hey [playername].", who=1)
        pause
        $ msg ("Fancy meeting me for coffee?", who=1)
        pause
        $ msg ("We could call it a date?", who=1)
        menu:
            "Go on a date with Katrine.":
                $ hide_messenger()
                call katrine_date from _call_katrine_date_1
                $ daytime += 1
                jump freetime
            "Do something else.":
                $ msg ("Sorry, I’m really busy today.")
                pause
                $ msg ("Alright, another time.", who=1)
                pause
                $ hide_messenger()
                return

    if trista.stage >= 2 and tristastage2event == 0 and day == 6 and daytime == 2:
        stop music fadeout 1.0
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Trista', dialogue=dialogue_one)
        $ msg ("Hey, [playername]. Ready for our weekly session?", who=1)
        menu:
            "Work out with Trista.":
                $ hide_messenger()
                call trista_date from _call_trista_date
                $ daytime += 1
                jump freetime
            "Do something else.":
                $ msg ("Sorry, I'm really busy today.")
                pause
                $ msg ("Alright, another time.", who=1)
                pause
                $ hide_messenger()
                return

    #Leanne calls every monday to go and stuff her face(happens after stage7)
    if leanne.stage >= 6 and leannestage6event == 0 and leannestage11event2 == 1 and day == 1 and daytime == 2:
        stop music fadeout 1.0
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
        $ msg ("I have some free time today. Feel like hanging out to talk and see me stuff my face?", who=1)
        pause
        $ msg ("I'll let you decide where.", who=1)
        menu:
            "Sure. Let's head to Bunny Bites.":
                $ msg ("Sure. Let's head to Bunny Bites.")
                pause
                $ msg ("Sounds like a plan. My body could use a good binging session.", who=1)
                pause
                $ hide_messenger()
                call leanne_feeding_bunnybites from _call_leanne_feeding_bunnybites_1
                $ daytime += 1
                jump freetime
            #"Okay. Let's go to The Sugar Shop." if leannestage7event == 0:
            #    $ msg ("Okay. Let's go to The Sugar Shop.")
            #    pause
            #    $ msg ("Yeah, I can go for that. My sweet tooth has been acting up lately. Meet you there soon.", who=1)
            #    pause
            #    $ hide_messenger()
            #    call leanne_feeding_sugarshop from _call_leanne_feeding_sugarshop_1
            #    $ daytime += 1
            #    jump freetime
            "Sorry, I'm busy.":
                $ msg ("Sorry, I'm really busy today.")
                pause
                $ msg ("Alright. I'll catch you some other time then.", who=1)
                pause
                $ hide_messenger()
                return

    if leanne.stage >= 12 and day == 1 and daytime == 2 and leannechoice == 1 and leannestage12event2 == 0:
        #(NOTE: The following should occur after meeting up with Lyn after stage 12. This should occur at random times whenever the player is in his room.)
        stop music fadeout 1.0
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Lyn', dialogue=dialogue_one)
        $ msg ("I have some free time today. Would you like to join me for a date at the Sugar Shop?", who=1)
        menu:
            "Yes":
                $ msg ("Great. See you soon!", who=1)
                pause
                $ hide_messenger()
                call lyn_date_sugarshop from _call_lyn_date_sugarshop
                $ daytime += 1
                jump freetime
            "No":
                $ msg ("Sorry, I'm really busy today.")
                pause
                $ msg ("Okay. Some other time then.", who=1)
                pause
                $ hide_messenger()
                return

    if leanne.stage >= 12 and day == 1 and daytime == 2 and leannechoice == 2 and leannestage12event2 == 0:
        #(NOTE: The following should occur after meeting up with Lyn after stage 12. This should occur at random times whenever the player is in his room.)
        stop music fadeout 1.0
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
        $ msg ("I have an empty day and an even emptier stomach. Want to meet up at Bunny Bites?", who=1)
        menu:
            "Yes":
                $ msg ("Great. See you soon!", who=1)
                pause
                $ hide_messenger()
                call leanne_date_bunnybites from _call_leanne_date_bunnybites
                $ daytime += 1
                jump freetime
            "No":
                $ msg ("Sorry, I’m really busy today.")
                pause
                $ msg ("Alright, your loss.", who=1)
                pause
                $ hide_messenger()
                return


    if lisa.stage >= 3 and daytime == 3 and lisastage3event == 0:
        if day == 6:
            if rngworkgirl == 1 or rngworkgirl == 3:
                stop music fadeout 1.0
                $ show_messenger()

                $ dialogue_one = []

                $ switch_dialogue(name='Lisa', dialogue=dialogue_one)
                if lisa.stage <= 5:
                    $ msg ("Hi [playername]. Would you want to come over to my house again?", who=1)
                    pause
                    $ msg ("It is always easier with company to distract me.", who=1)
                    pause
                elif lisa.stage == 6:
                    $ msg ("Hi [playername]. Would you want to come over to my house again?", who=1)
                    pause
                elif lisa.stage >= 7:
                    $ msg ("Hi [playername]. Would you want to come over to my house again and feed me?", who=1)
                    pause
                menu:
                    "Yes.":
                        $ msg ("I'll be there in a minute.")
                        pause
                        if lisa.stage == 6:
                            $ msg ("Great, could you maybe pick up a couple of extra things on your way here?", who=1)
                            pause
                            $ msg ("Sure, no problem.")
                            pause
                        elif lisa.stage >= 7:
                            $ msg ("Great, make sure to pick up some dessert again.", who=1)
                            pause
                            $ msg ("Sure, no problem.")
                            pause
                        $ hide_messenger()
                        if lisastage4event == 1 and lisastage3event2 == 0 and lisa.stage >= 4:
                            call Lisa_Stage_4_Event_1
                        else:
                            call Lisa_home from _call_Lisa_home
                        $ daytime += 1
                        jump freetime

                    "I'm busy, sorry.":
                        $ msg ("Sorry, I'm really busy today.")
                        pause
                        $ msg ("Alright, another time.", who=1)
                        pause
                        $ hide_messenger()
                        return
