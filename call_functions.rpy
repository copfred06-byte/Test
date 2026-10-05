#Call funtion that generates a random teaching scene for Daisy at the university.
label rngteachingscene:

    $ rng = renpy.random.randint(1,11)
    if rng == 6 and strip == 1:
        $ rng = renpy.random.randint(1,5)
    elif rng == 6 and strip == 2:
        $ rng = renpy.random.randint(7,11)
    elif rng == 6 and strip == 0:
        $ rng = renpy.random.randint(1,5)
    image uni_sexy_teacher_teaching = "/teacher/[teacher.stage]/[strip]/teaching[rng].webp"
    scene uni_sexy_teacher_teaching

    return

label strengthup:
    $ strength += 1
    $ renpy.notify("Strength increased by one point.")
    return

label BBfoodformula:
    "You create her food with the secret fattening formula."
    return

label lunastoryask:
    menu:
        "Ask Luna about herself.":
            "You decide to ask Luna about herself."
            luna "So you are not just here for the feeding and the sex? Very surprising."
            luna "I know it is a small gesture, but I appreciate the fact that you want to know more about me."
            "Luna talks a bit about herself."
            $ lunastory += 1
            #Unlocks more Luna story in the stats page.
            $ renpy.notify("New Luna story unlocked in the stats screen.")
            window hide
            pause
            return
        "Nevermind.":
            "You decide not to ask Luna anything."
            return

label bonniestoryask:
    menu:
        "Ask Bonnie about her past.":
            "You decide to ask Bonnie about her past."
            bonnie "Sure, I would love to talk about myself."
            bonnie "I didn't expect you to care about me like that though."
            "Bonnie talks a bit about herself."
            $ bonniestory += 1
            #Unlocks more Bonnie story in the stats page.
            $ renpy.notify("New Bonnie story unlocked in the stats screen.")
            window hide
            pause
            return
        "Nevermind.":
            "You decide not to ask Bonnie anything."
            return

label lisastoryask:
    menu:
        "Ask Lisa about her past.":
            "You decide to ask Lisa about her past."
            lisa "You want to know how it was like growing up for me?"
            lisa "Alright then."
            "Lisa talks a bit about herself."
            $ lisastory += 1
            #Unlocks more Lisa story in the stats page.
            $ renpy.notify("New Lisa story unlocked in the stats screen.")
            window hide
            pause
            return
        "Nevermind.":
            "You decide not to ask Lisa anything."
            return

label amberstoryask:
    menu:
        "Ask Amber about her past.":
            "You decide to ask Amber about her past."
            amber "My past? I never really get asked about that."
            amber "Sure, I'll tell you about myself."
            "Amber talks a bit about herself."
            $ amberstory += 1
            #Unlocks more Amber story in the stats page.
            $ renpy.notify("New Amber story unlocked in the stats screen.")
            window hide
            pause
            return
        "Nevermind.":
            "You decide not to ask Amber anything."
            return

label mariestoryask:
    menu:
        "Ask Marie about her past.":
            "You decide to ask Marie about her past."
            marie "Why do you care about that?"
            marie "Alright, I'll tell you what made me the way I am."
            "Marie talks a bit about herself."
            $ mariestory += 1
            #Unlocks more Marie story in the stats page.
            $ renpy.notify("New Marie story unlocked in the stats screen.")
            window hide
            pause
            return
        "Nevermind.":
            "You decide not to ask Marie anything."
            return

label katrine_feed_sauna:
    katrine "Yes, the only thing that could make it better would be something sweet."
    if foodheld >= 1:
        menu:
            "Give Katrine a bag of fattening sweets.":
                pc "I might have something."
                image katrine_sauna_beforeeat = "/katrine/[katrine.stage]/sauna_beforeeat.webp"
                scene katrine_sauna_beforeeat
                katrine "Really, I wouldn’t say no if you do."
                image katrine_sauna_eat = "/katrine/[katrine.stage]/sauna_eat.webp"
                scene katrine_sauna_eat
                "Handing her the snack she enjoys the sweet treats."
                $ foodheld -= 1
                if katrine.stage <= (trista.stage + 1):
                    $ katrine.weight += 0.2
                image katrine_sauna_sitting = "/katrine/[katrine.stage]/sauna_sitting.webp"
                scene katrine_sauna_sitting
                "Sitting around for another few minutes you decide to head home."
                katrine "See ya around [playername]."
                return
            "Don't give Katrine a bag of fattening sweets.":
                image katrine_sauna_sitting = "/katrine/[katrine.stage]/sauna_sitting.webp"
                scene katrine_sauna_sitting
                "Sitting around for another few minutes you decide to head home."
                katrine "See ya around [playername]."
                return
    else:
        image katrine_sauna_sitting = "/katrine/[katrine.stage]/sauna_sitting.webp"
        scene katrine_sauna_sitting
        "Sitting around for another few minutes you decide to head home."
        katrine "See ya around [playername]."
        return

#Call function that generates a random eating scene for Daisy at home
label rngeatingdaisyhome:

    $ rng = renpy.random.randint(1,6)
    image daisy_home_eating = "/teacher/[teacher.stage]/[stuffed]/home_eating[rng].webp"
    scene daisy_home_eating

    return

#Call function that generates a random eating scene for Luna at home
label rngeatinglunahome:

    $ rng = renpy.random.randint(1,3)
    image luna_home_eating = "/luna/[luna.stage]/home_feeding_eating[rng]_[stuffed].webp"
    scene luna_home_eating

    return

label rngeatingcayennehome:

    $ rng = renpy.random.randint(1,3)
    if rng == 1:
        call rngeatingcayennehomesweets from _call_rngeatingcayennehomesweets
        return
    if rng == 2:
        call rngeatingcayennehomefastfood from _call_rngeatingcayennehomefastfood
        return
    if rng == 3:
        image cayenne_home_eating_chocolate = "/cayenne/[cayenne.stage]/home_eating_chocolate1_[stuffed].webp"
        scene cayenne_home_eating_chocolate
        return
    return

#Call function that generates a random sweets eating scene for Cayenne at home
label rngeatingcayennehomesweets:

    $ rng = renpy.random.randint(1,2)
    image cayenne_home_eating_sweets = "/cayenne/[cayenne.stage]/home_eating_sweets[rng]_[stuffed].webp"
    scene cayenne_home_eating_sweets

    return

#Call function that generates a random fastfood eating scene for Cayenne at home
label rngeatingcayennehomefastfood:

    $ rng = renpy.random.randint(1,2)
    image cayenne_home_eating_fastfood = "/cayenne/[cayenne.stage]/home_eating_fastfood[rng]_[stuffed].webp"
    scene cayenne_home_eating_fastfood

    return

#Call function that generates a random scene to choose the food that needs to be eaten by Cayenne at home
label rngeatingcayennehomefoodchoice:

    $ rng = renpy.random.randint(1,3)
    image cayenne_home_foodchoice = "/cayenne/[cayenne.stage]/home_foodchoice[rng]_[stuffed].webp"
    scene cayenne_home_foodchoice

    return

label rngeatingbonniehome:

    $ rng = renpy.random.randint(1,7)
    image bonnie_home_eating_sweets = "/bonnie/[bonnie.stage]/feeding_[rng]_[stuffed].webp"
    scene bonnie_home_eating_sweets

    return

label rngeatingkatrinehome:

    $ rng = renpy.random.randint(1,4)
    image katrine_home_feeding = "/katrine/[katrine.stage]/home_feeding[rng]_[stuffed].webp"
    scene katrine_home_feeding

    return

label rngeatingtristagym:

    $ rng = renpy.random.randint(1,4)
    image trista_gym_feeding = "/trista/[trista.stage]/gym_feed[rng]_[stuffed].webp"
    scene trista_gym_feeding

    return

label rngeatingamberhome:

    $ rng = renpy.random.randint(1,4)
    image amber_home_feeding = "/amber/[amber.stage]/home_feeding[rng]_[stuffed].webp"
    scene amber_home_feeding

    return



#Call function that generates a random showoff scene for Daisy at the university(strip4 only)
label rngshowoffscene:

    $ rngshowoff = renpy.random.randint(1,10)
    image uni_sexy_teacher_showoff = "/teacher/[teacher.stage]/4/showoff[rngshowoff].webp"
    scene uni_sexy_teacher_showoff

    return

#Call function that generates a random arrive scene for Bunny Bites.
label rngbbarrive:

    $ rng = renpy.random.randint(1,4)
    image bunny_bites_arriving = "restaurant_guests_arriving[rng].webp"
    scene bunny_bites_arriving

    return

#Call function that returns the correct Bunny Bites working scene with the correct coworker.
label bbworking:

    if rngworkgirl == 1:
        scene restaurant_amber
    elif rngworkgirl == 2:
        scene restaurant_lisa
    elif rngworkgirl == 3:
        scene restaurant_marie

    return

#Call function that is the bridge between the room menu and the city menu.
label city:
    call screen citymenu

#Call function for visiting the Sugar Shop
label sugarshop:
    image bonnie_sweetshop = "/bonnie/[bonnie.stage]/sweetshop.webp"
    scene bonnie_sweetshop
    "You go to the Sugar Shop to buy some more fattening meal packages."
    if bonnie.stage <= 2:
        bonnie "Hello, welcome to The Sugar Shop."
        bonnie "What can I get for you today?"
        pc "I'd like to buy some fattening meal packages, please."
        image bonnie_sweetshop3 = "/bonnie/[bonnie.stage]/sweetshop3.webp"
        scene bonnie_sweetshop3
        bonnie "Sure thing, how many would you like?"
    elif bonnie.stage <= 6:
        bonnie "Hey, [playername]. How are you doing?"
        pc "I'm good, thanks."
        bonnie "Great to hear, you after your usual packages?"
        pc "Yes, please."
        image bonnie_sweetshop3 = "/bonnie/[bonnie.stage]/sweetshop3.webp"
        scene bonnie_sweetshop3
        bonnie "Sure thing, how many would you like?"
    else:
        bonnie "Hey, [playername]. Back again?"
        pc "Yeah. My friends can't get enough of your sweets."
        bonnie "Good to hear they are doing so well."
        image bonnie_sweetshop3 = "/bonnie/[bonnie.stage]/sweetshop3.webp"
        scene bonnie_sweetshop3
        bonnie "But I don't need to worry about these “friends” do I?"
        pc "Definitely not. How else would I get their chocolates?"
        bonnie "I was just teasing, but it's good to know I have that much power over you."
        bonnie "Anyway, how many packages would you like?"
    menu:
        "One ($5)":
            if money <= 4:
                "You do not have enough money."
                jump freetime
            else:
                $ money -= 5
                $ foodheld += 1
                "You bought one fattening meal package."
        "Two ($10)":
            if money <= 9:
                "You do not have enough money."
                jump freetime
            else:
                $ money -= 10
                $ foodheld += 2
                "You bought two fattening meal packages."
        "Five ($20)":
            if money <= 19:
                "You do not have enough money."
                jump freetime
            else:
                $ money -= 20
                $ foodheld += 5
                "You bought five fattening meal packages."
        "Ten ($40)":
            if money <= 39:
                "You do not have enough money."
                jump freetime
            else:
                $ money -= 40
                $ foodheld += 10
                "You bought ten fattening meal packages."
        "Twenty ($60)" if hagglelikeapro == 1:
            if money <= 59:
                "You do not have enough money."
                jump freetime
            else:
                $ money -= 60
                $ foodheld += 20
                "You bought twenty fattening meal packages."
        "Fourty ($120)" if hagglelikeapro == 1:
            if money <= 119:
                "You do not have enough money."
                jump freetime
            else:
                $ money -= 120
                $ foodheld += 40
                "You bought fourty fattening meal packages."
        "Nevermind":
            "You decide not to buy anything."
            jump freetime
    image bonnie_sweetshop2 = "/bonnie/[bonnie.stage]/sweetshop2.webp"
    scene bonnie_sweetshop2
    if bonnie.stage <= 2:
        bonnie "Thanks for shopping, See you again soon!"
    elif bonnie.stage <= 6:
        bonnie "See you again soon, [playername]!"
    else:
        bonnie "See you around, [playername]."
    jump freetime

#Call function for visiting the Library.
label library:
    image library_start = "/side/library[librarianstage].webp"
    scene library_start
    play music "/music/university.ogg" if_changed
    "You go to the library to get some books."
    if librarianmeet == 1:
        pc "I wonder if that's the librarian over there."
        image librarian_library1 = "/side/librarian1_[librarianstage].webp"
        scene librarian_library1
        pc "Hey, do you work here?"
        librarian "Yes I do, can I help you?"
        $ librarianmeet = 0
    else:
        image librarian_library1 = "/side/librarian1_[librarianstage].webp"
        scene librarian_library1
        librarian "Can I help you?"
    image librarian_library2 = "/side/librarian2_[librarianstage].webp"
    scene librarian_library2
    pc "I'm looking for some personal development books, or something that can help me learn some new skills."
    librarian "I think these books might interest you."
    image librarian_library3 = "/side/librarian3_[librarianstage].webp"
    scene librarian_library3
    call buybook from _call_buybook_2
    stop music fadeout 1.0
    jump freetime

#Call function for visiting the Hospital.
label hospital:
    if nataliestage4event == 1 and natalie.stage >= 4 and brittastage4event == 0:
        call Natalie_Stage_4_Event_1
        $ daytime += 1
        jump freetime
    "You decide to go to the hospital for another milking session."
    image natalie_milk_start = "/natalie/[natalie.stage]/milk_start.webp"
    scene natalie_milk_start
    "You find Natalie at the receptionist desk."
    "Who should I milk today?"
    menu:
        "Natalie" if nataliemilkcheck == 1:
            pc "Hi Natalie! I was just thinking of you and thought I would stop by to see how you are doing and see if you might want some help with some milking."
            natalie "That’s thoughtful of you. Yes that would be great thanks! I could use another milking session. I can get someone else to watch the front while I go do that."
            call Natalie_Milking from _call_Natalie_Milking
        "Britta" if brittastage4event == 0 and brittamilkcheck == 1:
            pc "Hi Natalie! I'm here for another milking session, this time with Britta."
            natalie "Hey [playername]! I'll call Britta into the milking room, she should be there in a minute."
            pc "Thank you Natalie, see you later."
            call Britta_Milking from _call_Britta_Milking_1
    $ daytime += 1
    jump freetime

#Call function that trains your charisma by one whenever you click the mirror in the player room.
label charisma_train:
    "After a couple of hours you feel more charismatic."
    $ charisma += 1
    "Charisma increased by 1 point."
    $ daytime += 1
    jump freetime

#Call function that is the bridge between the room menu and the Remember the good times menu.
label goodtimes:
    window hide
    $ AppendGirls()
    call screen GallerySelect
    $ availableGirls = []
    $ recollection = False
    jump freetime

#Choice screen for reading books
label book_read:
    "Which book should you read?"
    menu:
        "Secret Feeder volume1" if secretfeedervol1hold == 1 and secretfeedervol1 == 0:
            "You read Secret Feeder volume1"
            $ secretfeedervol1times += 1
            if secretfeedervol1times >= 5:
                "You read through the whole book."
                "You are now able to enhance food to be more fattening."
                $ secretfeedervol1hold = 0
                $ secretfeedervol1 = 1
                $ booksheld -= 1
            else:
                "You read [secretfeedervol1times] out of the 5 chapters."
                "You have to continue it another time."
            return

        "Secret Feeder volume2" if secretfeedervol2hold == 1 and secretfeedervol2 == 0:
            "You read Secret Feeder volume2"
            $ secretfeedervol2times += 1
            if secretfeedervol2times >= 5:
                "You read through the whole book."
                "You are now able to enhance food to be even more fattening."
                $ secretfeedervol2hold = 0
                $ secretfeedervol2 = 1
                $ booksheld -= 1
            else:
                "You read [secretfeedervol2times] out of the 5 chapters."
                "You have to continue it another time."
            return
        
        "Haggle like a Pro" if hagglelikeaprohold == 1 and hagglelikeapro == 0:
            "You read Haggle like a Pro."
            $ hagglelikeaprotimes += 1
            if hagglelikeaprotimes >= 5:
                "You read through the whole book."
                "You are now able to haggle for better prices on bulk deals."
                $ hagglelikeaprohold = 0
                $ hagglelikeapro = 1
                $ booksheld -= 1
            else:
                "You read [hagglelikeaprotimes] out of the 5 chapters."
                "You have to continue it another time."
            return

        "Kamasutra volume1" if kamasutravol1hold == 1 and kamasutravol1 == 0:
            "You read Kamasutra volume1"
            $ kamasutravol1times += 1
            if kamasutravol1times >= 3:
                "You read through the whole book."
                "You are now able to use new sex positions you learned from the book."
                $ kamasutravol1hold = 0
                $ kamasutravol1 = 1
                $ booksheld -= 1
            else:
                "You read [kamasutravol1times] out of the 3 chapters."
                "You have to continue it another time."
            return

        "Belly rubs" if bellyrubshold == 1 and bellyrubs == 0:
            "You read Belly rubs"
            $ bellyrubstimes += 1
            if bellyrubstimes >= 5:
                "You read through the whole book."
                "You are now confident in your ability to rub bellies to relieve pressure."
                $ bellyrubshold = 0
                $ bellyrubs = 1
                $ booksheld -= 1
            else:
                "You read [bellyrubstimes] out of the 5 chapters."
                "You have to continue it another time."
            return

        "Workout Champion" if workoutchampionhold == 1 and workoutchampion == 0:
            "You read Workout Champion."
            $ workoutchampiontimes += 1
            if workoutchampiontimes >= 3:
                "You read through the whole book."
                "You gained 3 strength!"
                $ strength += 3
                $ workoutchampionhold = 0
                $ workoutchampion = 1
                $ booksheld -= 1
            else:
                "You read [workoutchampiontimes] out of the 3 chapters."
                "You have to continue it another time."
            return

        "Charisma Master volume1" if charismamastervol1hold == 1 and charismamastervol1 == 0:
            "You read Charisma Master volume1."
            $ charismamastervol1times += 1
            if charismamastervol1times >= 3:
                "You read through the whole book."
                "You gained 3 charisma!"
                $ charisma += 3
                $ charismamastervol1hold = 0
                $ charismamastervol1 = 1
                $ booksheld -= 1
            else:
                "You read [charismamastervol1times] out of the 3 chapters."
                "You have to continue it another time."
            return

        "Charisma Master volume2" if charismamastervol2hold == 1 and charismamastervol2 == 0:
            "You read Charisma Master volume2."
            $ charismamastervol2times += 1
            if charismamastervol2times >= 3:
                "You read through the whole book."
                "You gained 5 charisma!"
                $ charisma += 5
                $ charismamastervol2hold = 0
                $ charismamastervol2 = 1
                $ booksheld -= 1
            else:
                "You read [charismamastervol2times] out of the 3 chapters."
                "You have to continue it another time."
            return

        "Sweet tooth volume1" if sweettoothvol1hold == 1 and sweettoothvol1 == 0:
            "You read Sweet tooth volume1"
            $ sweettoothvol1times += 1
            if sweettoothvol1times >= 3:
                "You read through the whole book."
                "You learned how to make delicious chocolates!"
                $ sweettoothvol1hold = 0
                $ sweettoothvol1 = 1
                $ booksheld -= 1
            else:
                "You read [sweettoothvol1times] out of the 3 chapters."
                "You have to continue it another time."
            return

        "Sweet tooth volume2" if sweettoothvol2hold == 1 and sweettoothvol2 == 0:
            "You read Sweet tooth volume2"
            $ sweettoothvol2times += 1
            if sweettoothvol2times >= 3:
                "You read through the whole book."
                "You learned how to make Delicious Chocolates!"
                $ sweettoothvol2hold = 0
                $ sweettoothvol2 = 1
                $ booksheld -= 1
            else:
                "You read [sweettoothvol2times] out of the 3 chapters."
                "You have to continue it another time."
            return

        "Nevermind":
            return

label book_read_home:
    "Which book should you read?"
    menu:
        "Secret Feeder volume1" if secretfeedervol1hold == 1 and secretfeedervol1 == 0:
            "You read Secret Feeder volume1"
            $ secretfeedervol1times += 1
            if secretfeedervol1times >= 5:
                "You read through the whole book."
                "You are now able to enhance food to be more fattening."
                $ secretfeedervol1hold = 0
                $ secretfeedervol1 = 1
                $ booksheld -= 1
            else:
                "You read [secretfeedervol1times] out of the 5 chapters."
                "You have to continue it another time."
            $ daytime += 1
            jump freetime

        "Secret Feeder volume2" if secretfeedervol2hold == 1 and secretfeedervol2 == 0:
            "You read Secret Feeder volume2"
            $ secretfeedervol2times += 1
            if secretfeedervol2times >= 5:
                "You read through the whole book."
                "You are now able to enhance food to be even more fattening."
                $ secretfeedervol2hold = 0
                $ secretfeedervol2 = 1
                $ booksheld -= 1
            else:
                "You read [secretfeedervol2times] out of the 5 chapters."
                "You have to continue it another time."
            $ daytime += 1
            jump freetime

        "Haggle like a Pro" if hagglelikeaprohold == 1 and hagglelikeapro == 0:
            "You read Haggle like a Pro."
            $ hagglelikeaprotimes += 1
            if hagglelikeaprotimes >= 5:
                "You read through the whole book."
                "You are now able to haggle for better prices on bulk deals."
                $ hagglelikeaprohold = 0
                $ hagglelikeapro = 1
                $ booksheld -= 1
            else:
                "You read [hagglelikeaprotimes] out of the 5 chapters."
                "You have to continue it another time."
            $ daytime += 1
            jump freetime

        "Kamasutra volume1" if kamasutravol1hold == 1 and kamasutravol1 == 0:
            "You read Kamasutra volume1"
            $ kamasutravol1times += 1
            if kamasutravol1times >= 3:
                "You read through the whole book."
                "You are now able to use new sex positions you learned from the book."
                $ kamasutravol1hold = 0
                $ kamasutravol1 = 1
                $ booksheld -= 1
            else:
                "You read [kamasutravol1times] out of the 3 chapters."
                "You have to continue it another time."
            $ daytime += 1
            jump freetime

        "Belly rubs" if bellyrubshold == 1 and bellyrubs == 0:
            "You read Belly rubs"
            $ bellyrubstimes += 1
            if bellyrubstimes >= 5:
                "You read through the whole book."
                "You are now confident in your ability to rub bellies to relieve pressure."
                $ bellyrubshold = 0
                $ bellyrubs = 1
                $ booksheld -= 1
            else:
                "You read [bellyrubstimes] out of the 5 chapters."
                "You have to continue it another time."
            $ daytime += 1
            jump freetime

        "Workout Champion" if workoutchampionhold == 1 and workoutchampion == 0:
            "You read Workout Champion."
            $ workoutchampiontimes += 1
            if workoutchampiontimes >= 3:
                "You read through the whole book."
                "You gained 3 strength!"
                $ strength += 3
                $ workoutchampionhold = 0
                $ workoutchampion = 1
                $ booksheld -= 1
            else:
                "You read [workoutchampiontimes] out of the 3 chapters."
                "You have to continue it another time."
            $ daytime += 1
            jump freetime

        "Charisma Master volume1" if charismamastervol1hold == 1 and charismamastervol1 == 0:
            "You read Charisma Master volume1."
            $ charismamastervol1times += 1
            if charismamastervol1times >= 3:
                "You read through the whole book."
                "You gained 3 charisma!"
                $ charisma += 3
                $ charismamastervol1hold = 0
                $ charismamastervol1 = 1
                $ booksheld -= 1
            else:
                "You read [charismamastervol1times] out of the 3 chapters."
                "You have to continue it another time."
            $ daytime += 1
            jump freetime

        "Charisma Master volume2" if charismamastervol2hold == 1 and charismamastervol2 == 0:
            "You read Charisma Master volume2."
            $ charismamastervol2times += 1
            if charismamastervol2times >= 3:
                "You read through the whole book."
                "You gained 5 charisma!"
                $ charisma += 5
                $ charismamastervol2hold = 0
                $ charismamastervol2 = 1
                $ booksheld -= 1
            else:
                "You read [charismamastervol2times] out of the 3 chapters."
                "You have to continue it another time."
            $ daytime += 1
            jump freetime

        "Sweet tooth volume1" if sweettoothvol1hold == 1 and sweettoothvol1 == 0:
            "You read Sweet tooth volume1"
            $ sweettoothvol1times += 1
            if sweettoothvol1times >= 3:
                "You read through the whole book."
                "You learned how to make delicious chocolates!"
                $ sweettoothvol1hold = 0
                $ sweettoothvol1 = 1
                $ booksheld -= 1
            else:
                "You read [sweettoothvol1times] out of the 3 chapters."
                "You have to continue it another time."
            $ daytime += 1
            jump freetime

        "Sweet tooth volume2" if sweettoothvol2hold == 1 and sweettoothvol2 == 0:
            "You read Sweet tooth volume2"
            $ sweettoothvol2times += 1
            if sweettoothvol2times >= 3:
                "You read through the whole book."
                "You learned how to make Delicious Chocolates!"
                $ sweettoothvol2hold = 0
                $ sweettoothvol2 = 1
                $ booksheld -= 1
            else:
                "You read [sweettoothvol2times] out of the 3 chapters."
                "You have to continue it another time."
            $ daytime += 1
            jump freetime
        
        "Nevermind":
            jump freetime

#Animated dancing choices
label leanne_dance:
    if leanne.stage == 2:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/2/idle.webm" loop
        show movie with dissolve
        menu:
            "Dance.":
                ##Player Chooses Dance
                stop movie
                leanne "Oooh, sounds fun. I know just the song for it."
                image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
                scene leanne_typing
                "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
                ##Dance animation starts.
                $ movielength = 35
                $ movieplaying = "/images/leanne/2/dance1.webm"
                call screen custommoviescreen
                pause
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                "After the song concludes, Leanne sits back down at her desk."
                leanne "That was just what I needed. Now I’m all limbered up and you all got a bit of a show. I’ll have to do this again sometime."
                return

            "Excercise.":
                ##Player Chooses Exercise
                stop movie
                leanne "Okay. Can’t say I’m too thrilled about doing this on a full tummy, but here I go."
                ##Exercise animation starts
                $ movielength = 25
                $ movieplaying = "/images/leanne/2/excercise.webm"
                call screen custommoviescreen
                pause
                "After completing several reps, Leanne sits back at her desk and wipes her face off with a towel."
                image stream_girl_towel = "/leanne/[leanne.stage]/towel.webp"
                scene stream_girl_towel
                leanne "I’m a little sweaty, but I think that worked. I should be ready to get back to the game now."
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                return
    elif leanne.stage == 3:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/3/idle.webm" loop
        show movie with dissolve
        menu:
            "Dance.":
                ##Player Chooses Dance
                stop movie
                leanne "Oooh, sounds fun. I know just the song for it."
                image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
                scene leanne_typing
                "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
                ##Dance animation starts.
                $ movielength = 34
                $ movieplaying = "/images/leanne/3/dance1.webm"
                call screen custommoviescreen
                pause
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                "After the song concludes, Leanne sits back down at her desk."
                leanne "That was just what I needed. Now I’m all limbered up and you all got a bit of a show. I’ll have to do this again sometime."
                return

            "Excercise.":
                ##Player Chooses Exercise
                stop movie
                leanne "Okay. Can’t say I’m too thrilled about doing this on a full tummy, but here I go."
                ##Exercise animation starts
                $ movielength = 25
                $ movieplaying = "/images/leanne/3/excercise.webm"
                call screen custommoviescreen
                pause
                "After completing several reps, Leanne sits back at her desk and wipes her face off with a towel."
                image stream_girl_towel = "/leanne/[leanne.stage]/towel.webp"
                scene stream_girl_towel
                leanne "I’m a little sweaty, but I think that worked. I should be ready to get back to the game now."
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                return

    elif leanne.stage == 4:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/4/idle.webm" loop
        show movie with dissolve
        menu:
            "Dance.":
                ##Player Chooses Dance
                stop movie
                leanne "Oooh, sounds fun. I know just the song for it."
                image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
                scene leanne_typing
                "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
                ##Dance animation starts.
                $ movielength = 34
                $ movieplaying = "/images/leanne/4/dance1.webm"
                call screen custommoviescreen
                pause
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                "After the song concludes, Leanne sits back down at her desk."
                leanne "That was just what I needed. Now I’m all limbered up and you all got a bit of a show. I’ll have to do this again sometime."
                return

            "Excercise.":
                ##Player Chooses Exercise
                stop movie
                leanne "Okay. Can’t say I’m too thrilled about doing this on a full tummy, but here I go."
                ##Exercise animation starts
                $ movielength = 25
                $ movieplaying = "/images/leanne/4/excercise.webm"
                call screen custommoviescreen
                pause
                "After completing several reps, Leanne sits back at her desk and wipes her face off with a towel."
                image stream_girl_towel = "/leanne/[leanne.stage]/towel.webp"
                scene stream_girl_towel
                leanne "I’m a little sweaty, but I think that worked. I should be ready to get back to the game now."
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                return

    elif leanne.stage == 5:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/5/idle.webm" loop
        show movie with dissolve
        menu:
            "Dance.":
                ##Player Chooses Dance
                stop movie
                leanne "Oooh, sounds fun. I know just the song for it."
                image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
                scene leanne_typing
                "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
                ##Dance animation starts.
                $ movielength = 34
                $ movieplaying = "/images/leanne/5/dance1.webm"
                call screen custommoviescreen
                pause
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                "After the song concludes, Leanne sits back down at her desk."
                leanne "That was just what I needed. Now I’m all limbered up and you all got a bit of a show. I’ll have to do this again sometime."
                return

            "Excercise.":
                ##Player Chooses Exercise
                stop movie
                leanne "Okay. Can’t say I’m too thrilled about doing this on a full tummy, but here I go."
                ##Exercise animation starts
                $ movielength = 25
                $ movieplaying = "/images/leanne/5/excercise.webm"
                call screen custommoviescreen
                pause
                "After completing several reps, Leanne sits back at her desk and wipes her face off with a towel."
                image stream_girl_towel = "/leanne/[leanne.stage]/towel.webp"
                scene stream_girl_towel
                leanne "I’m a little sweaty, but I think that worked. I should be ready to get back to the game now."
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                return

    elif leanne.stage == 6:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/6/idle.webm" loop
        show movie with dissolve
        menu:
            "Dance.":
                ##Player Chooses Dance
                stop movie
                leanne "Oooh, sounds fun. I know just the song for it."
                image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
                scene leanne_typing
                "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
                ##Dance animation starts.
                $ movielength = 34
                $ movieplaying = "/images/leanne/6/dance1.webm"
                call screen custommoviescreen
                pause
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                "After the song concludes, Leanne sits back down at her desk."
                leanne "That was just what I needed. Now I’m all limbered up and you all got a bit of a show. I’ll have to do this again sometime."
                return

            "Excercise.":
                ##Player Chooses Exercise
                stop movie
                leanne "Okay. Can’t say I’m too thrilled about doing this on a full tummy, but here I go."
                ##Exercise animation starts
                $ movielength = 25
                $ movieplaying = "/images/leanne/6/excercise.webm"
                call screen custommoviescreen
                pause
                "After completing several reps, Leanne sits back at her desk and wipes her face off with a towel."
                image stream_girl_towel = "/leanne/[leanne.stage]/towel.webp"
                scene stream_girl_towel
                leanne "I’m a little sweaty, but I think that worked. I should be ready to get back to the game now."
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                return

    elif leanne.stage == 7:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/7/idle.webm" loop
        show movie with dissolve
        menu:
            "Dance.":
                ##Player Chooses Dance
                stop movie
                leanne "Oooh, sounds fun. I know just the song for it."
                image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
                scene leanne_typing
                "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
                ##Dance animation starts.
                $ movielength = 34
                $ movieplaying = "/images/leanne/7/dance1.webm"
                call screen custommoviescreen
                pause
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                "After the song concludes, Leanne sits back down at her desk."
                leanne "That was just what I needed. Now I’m all limbered up and you all got a bit of a show. I’ll have to do this again sometime."
                return

            "Excercise.":
                ##Player Chooses Exercise
                stop movie
                leanne "Okay. Can’t say I’m too thrilled about doing this on a full tummy, but here I go."
                ##Exercise animation starts
                $ movielength = 25
                $ movieplaying = "/images/leanne/7/excercise.webm"
                call screen custommoviescreen
                pause
                "After completing several reps, Leanne sits back at her desk and wipes her face off with a towel."
                image stream_girl_towel = "/leanne/[leanne.stage]/towel.webp"
                scene stream_girl_towel
                leanne "I’m a little sweaty, but I think that worked. I should be ready to get back to the game now."
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                return

    elif leanne.stage == 8:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/8/idle.webm" loop
        show movie with dissolve
        menu:
            "Dance.":
                ##Player Chooses Dance
                stop movie
                leanne "Oooh, sounds fun. I know just the song for it."
                image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
                scene leanne_typing
                "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
                ##Dance animation starts.
                $ movielength = 34
                $ movieplaying = "/images/leanne/8/dance1.webm"
                call screen custommoviescreen
                pause
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                "After the song concludes, Leanne sits back down at her desk."
                leanne "That was just what I needed. Now I’m all limbered up and you all got a bit of a show. I’ll have to do this again sometime."
                return

            "Excercise.":
                ##Player Chooses Exercise
                stop movie
                leanne "Okay. Can’t say I’m too thrilled about doing this on a full tummy, but here I go."
                ##Exercise animation starts
                $ movielength = 25
                $ movieplaying = "/images/leanne/8/excercise.webm"
                call screen custommoviescreen
                pause
                "After completing several reps, Leanne sits back at her desk and wipes her face off with a towel."
                image stream_girl_towel = "/leanne/[leanne.stage]/towel.webp"
                scene stream_girl_towel
                leanne "I’m a little sweaty, but I think that worked. I should be ready to get back to the game now."
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                return

    elif leanne.stage == 9:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/9/idle.webm" loop
        show movie with dissolve
        menu:
            "Dance.":
                ##Player Chooses Dance
                stop movie
                leanne "Oooh, sounds fun. I know just the song for it."
                image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
                scene leanne_typing
                "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
                ##Dance animation starts.
                $ movielength = 34
                $ movieplaying = "/images/leanne/9/dance1.webm"
                call screen custommoviescreen
                pause
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                "After the song concludes, Leanne sits back down at her desk."
                leanne "That was just what I needed. Now I’m all limbered up and you all got a bit of a show. I’ll have to do this again sometime."
                return

            "Excercise.":
                ##Player Chooses Exercise
                stop movie
                leanne "Okay. Can’t say I’m too thrilled about doing this on a full tummy, but here I go."
                ##Exercise animation starts
                $ movielength = 25
                $ movieplaying = "/images/leanne/9/excercise.webm"
                call screen custommoviescreen
                pause
                "After completing several reps, Leanne sits back at her desk and wipes her face off with a towel."
                image stream_girl_towel = "/leanne/[leanne.stage]/towel.webp"
                scene stream_girl_towel
                leanne "I’m a little sweaty, but I think that worked. I should be ready to get back to the game now."
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                return

    elif leanne.stage == 10:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/10/idle.webm" loop
        show movie with dissolve
        menu:
            "Dance.":
                ##Player Chooses Dance
                stop movie
                leanne "Oooh, sounds fun. I know just the song for it."
                image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
                scene leanne_typing
                "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
                ##Dance animation starts.
                $ movielength = 34
                $ movieplaying = "/images/leanne/10/dance1.webm"
                call screen custommoviescreen
                pause
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                "After the song concludes, Leanne sits back down at her desk."
                leanne "That was just what I needed. Now I’m all limbered up and you all got a bit of a show. I’ll have to do this again sometime."
                return

            "Excercise.":
                ##Player Chooses Exercise
                stop movie
                leanne "Okay. Can’t say I’m too thrilled about doing this on a full tummy, but here I go."
                ##Exercise animation starts
                $ movielength = 25
                $ movieplaying = "/images/leanne/10/excercise.webm"
                call screen custommoviescreen
                pause
                "After completing several reps, Leanne sits back at her desk and wipes her face off with a towel."
                image stream_girl_towel = "/leanne/[leanne.stage]/towel.webp"
                scene stream_girl_towel
                leanne "I’m a little sweaty, but I think that worked. I should be ready to get back to the game now."
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                return

    elif leanne.stage == 11:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/11/idle.webm" loop
        show movie with dissolve
        menu:
            "Dance.":
                ##Player Chooses Dance
                stop movie
                leanne "Oooh, sounds fun. I know just the song for it."
                image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
                scene leanne_typing
                "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
                ##Dance animation starts.
                $ movielength = 34
                $ movieplaying = "/images/leanne/11/dance1.webm"
                call screen custommoviescreen
                pause
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                "After the song concludes, Leanne sits back down at her desk."
                leanne "That was just what I needed. Now I’m all limbered up and you all got a bit of a show. I’ll have to do this again sometime."
                return

            "Excercise.":
                ##Player Chooses Exercise
                stop movie
                leanne "Okay. Can’t say I’m too thrilled about doing this on a full tummy, but here I go."
                ##Exercise animation starts
                $ movielength = 25
                $ movieplaying = "/images/leanne/11/excercise.webm"
                call screen custommoviescreen
                pause
                "After completing several reps, Leanne sits back at her desk and wipes her face off with a towel."
                image stream_girl_towel = "/leanne/[leanne.stage]/towel.webp"
                scene stream_girl_towel
                leanne "I’m a little sweaty, but I think that worked. I should be ready to get back to the game now."
                image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                scene stream_girl_webcam
                return

return

label leanne_dance2:
    if leanne.stage == 4:
        leanne "I know just the song for it."
        image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
        scene leanne_typing
        "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
        ##Dance animation starts.
        $ renpy.movie_cutscene("/images/leanne/4/dance2.webm", stop_music=False)
        image leanne_dance2end = "/leanne/[leanne.stage]/dance2end.webp"
        scene leanne_dance2end
        window hide
        pause
        return
    elif leanne.stage == 5:
        leanne "I know just the song for it."
        image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
        scene leanne_typing
        "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
        ##Dance animation starts.
        $ renpy.movie_cutscene("/images/leanne/5/dance2.webm", stop_music=False)
        image leanne_dance2end = "/leanne/[leanne.stage]/dance2end.webp"
        scene leanne_dance2end
        window hide
        pause
        return
    elif leanne.stage == 6:
        leanne "I know just the song for it."
        image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
        scene leanne_typing
        "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
        ##Dance animation starts.
        $ renpy.movie_cutscene("/images/leanne/6/dance2.webm", stop_music=False)
        image leanne_dance2end = "/leanne/[leanne.stage]/dance2end.webp"
        scene leanne_dance2end
        window hide
        pause
        return
    elif leanne.stage == 7:
        leanne "I know just the song for it."
        image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
        scene leanne_typing
        "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
        ##Dance animation starts.
        $ renpy.movie_cutscene("/images/leanne/7/dance2.webm", stop_music=False)
        image leanne_dance2end = "/leanne/[leanne.stage]/dance2end.webp"
        scene leanne_dance2end
        window hide
        pause
        return
    elif leanne.stage == 8:
        leanne "I know just the song for it."
        image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
        scene leanne_typing
        "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
        ##Dance animation starts.
        $ renpy.movie_cutscene("/images/leanne/8/dance2.webm", stop_music=False)
        image leanne_dance2end = "/leanne/[leanne.stage]/dance2end.webp"
        scene leanne_dance2end
        window hide
        pause
        return
    elif leanne.stage == 9:
        leanne "I know just the song for it."
        image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
        scene leanne_typing
        "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
        ##Dance animation starts.
        $ renpy.movie_cutscene("/images/leanne/9/dance2.webm", stop_music=False)
        image leanne_dance2end = "/leanne/[leanne.stage]/dance2end.webp"
        scene leanne_dance2end
        window hide
        pause
        return
    elif leanne.stage == 10:
        leanne "I know just the song for it."
        image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
        scene leanne_typing
        "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
        ##Dance animation starts.
        $ renpy.movie_cutscene("/images/leanne/10/dance2.webm", stop_music=False)
        image leanne_dance2end = "/leanne/[leanne.stage]/dance2end.webp"
        scene leanne_dance2end
        window hide
        pause
        return
    elif leanne.stage == 11:
        leanne "I know just the song for it."
        image leanne_typing = "/leanne/[leanne.stage]/typing.webp"
        scene leanne_typing
        "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
        ##Dance animation starts.
        $ renpy.movie_cutscene("/images/leanne/11/dance2.webm", stop_music=False)
        image leanne_dance2end = "/leanne/[leanne.stage]/dance2end.webp"
        scene leanne_dance2end
        window hide
        pause
        return
return

#Feeding choices for Daisy at the university
label foodchoice:

    menu:

        "Ask Daisy to eat donuts.":
            image uni_sexy_teacher_food_eating_donut = "/teacher/[teacher.stage]/4/food_eating_donut.webp"
            scene uni_sexy_teacher_food_eating_donut
            teacher "Very good."
            $ teacher.weight += 0.2
            $ eatcount += 1
            return

        "Ask Daisy to eat a burger.":
            image uni_sexy_teacher_food_eating_burger = "/teacher/[teacher.stage]/4/food_eating_burger.webp"
            scene uni_sexy_teacher_food_eating_burger
            teacher "Very good."
            $ teacher.weight += 0.2
            $ eatcount += 1
            return

        "Ask Daisy to eat fries.":
            image uni_sexy_teacher_food_eating_fries = "/teacher/[teacher.stage]/4/food_eating_fries.webp"
            scene uni_sexy_teacher_food_eating_fries
            teacher "Very good."
            $ teacher.weight += 0.2
            $ eatcount += 1
            return

        "Ask Daisy to drink some soda.":
            image uni_sexy_teacher_food_eating_soda = "/teacher/[teacher.stage]/4/food_eating_soda.webp"
            scene uni_sexy_teacher_food_eating_soda
            teacher "Very good."
            $ teacher.weight += 0.2
            $ eatcount += 1
            return

        "Ask Daisy to eat some chicken nuggets.":
            image uni_sexy_teacher_food_eating_nuggets = "/teacher/[teacher.stage]/4/food_eating_nuggets.webp"
            scene uni_sexy_teacher_food_eating_nuggets
            teacher "Very good."
            $ teacher.weight += 0.2
            $ eatcount += 1
            return

        "Ask Daisy to eat a corndog." if corndogunlock == 1:
            image uni_sexy_teacher_food_eating_corndog = "/teacher/[teacher.stage]/4/food_eating_corndog.webp"
            scene uni_sexy_teacher_food_eating_corndog
            teacher "Very good."
            $ teacher.weight += 0.2
            $ eatcount += 1
            return

        "Ask Daisy to drink a milkshake." if milkshakeunlock == 1:
            image uni_sexy_teacher_food_eating_milkshake = "/teacher/[teacher.stage]/4/food_eating_milkshake.webp"
            scene uni_sexy_teacher_food_eating_milkshake
            teacher "Very good."
            $ teacher.weight += 0.2
            $ eatcount += 1
            return

        "Ask Daisy to eat some onion rings." if onionringunlock == 1:
            image uni_sexy_teacher_food_eating_onionrings = "/teacher/[teacher.stage]/4/food_eating_onionrings.webp"
            scene uni_sexy_teacher_food_eating_onionrings
            teacher "Very good."
            $ teacher.weight += 0.2
            $ eatcount += 1
            return

        "Ask Daisy to eat a burrito." if burritounlock == 1:
            image uni_sexy_teacher_food_eating_burrito = "/teacher/[teacher.stage]/4/food_eating_burrito.webp"
            scene uni_sexy_teacher_food_eating_burrito
            teacher "Very good."
            $ teacher.weight += 0.2
            $ eatcount += 1
            return

label buybook:
    menu:
        "Secret Feeder volume 1 ($15)" if secretfeedervol1hold == 0 and secretfeedervol1 == 0 and teacher.stage >= 8:
            if money >= 15:
                "You buy Secret Feeder volume 1."
                $ secretfeedervol1hold = 1
                $ money -= 15
                $ booksheld += 1
                jump buybook
            else:
                "You do not have enough money."
                jump buybook

        "Secret Feeder volume 2 ($20)" if secretfeedervol2hold == 0 and secretfeedervol1 == 1 and secretfeedervol2 == 0 and teacher.stage >= 8:
            if money >= 20:
                "You buy Secret Feeder volume 2."
                $ secretfeedervol2hold = 1
                $ money -= 20
                $ booksheld += 1
                jump buybook
            else:
                "You do not have enough money."
                jump buybook

        "Haggle like a Pro ($30)" if hagglelikeaprohold == 0 and hagglelikeapro == 0:
            if money >= 30:
                "You buy Haggle like a Pro."
                $ hagglelikeaprohold = 1
                $ money -= 30
                $ booksheld += 1
                jump buybook
            else:
                "You do not have enough money."
                jump buybook

        "Kamasutra volume 1 ($10)" if kamasutravol1hold == 0 and kamasutravol1 == 0 and teacher.stage >= 8:
            if money >= 10:
                "You buy Kamasutra volume 1."
                $ kamasutravol1hold = 1
                $ money -= 10
                $ booksheld += 1
                jump buybook
            else:
                "You do not have enough money."
                jump buybook

        "Workout Champion ($10)" if workoutchampionhold == 0 and workoutchampion == 0:
            if money >= 10:
                "You buy Workout Champion."
                $ workoutchampionhold = 1
                $ money -= 10
                $ booksheld += 1
                jump buybook
            else:
                "You do not have enough money."
                jump buybook

        "Belly rubs ($50)" if bellyrubshold == 0 and bellyrubs == 0 and teacher.stage >= 8:
            if money >= 50:
                "You buy Belly rubs."
                $ bellyrubshold = 1
                $ money -= 50
                $ booksheld += 1
                jump buybook
            else:
                "You do not have enough money."
                jump buybook

        "Sweet tooth volume 1 ($10)" if sweettoothvol1hold == 0 and sweettoothvol1 == 0 and bonniestage2event == 0:
            if money >= 10:
                "You buy Sweet tooth volume 1."
                $ sweettoothvol1hold = 1
                $ money -= 10
                $ booksheld += 1
                jump buybook
            else:
                "You do not have enough money."
                jump buybook

        "Sweet tooth volume 2 ($15)" if sweettoothvol2hold == 0 and sweettoothvol2 == 0 and bonniestage8event == 0:
            if money >= 15:
                "You buy Sweet tooth volume 2."
                $ sweettoothvol2hold = 1
                $ money -= 15
                $ booksheld += 1
                jump buybook
            else:
                "You do not have enough money."
                jump buybook

        "Charisma Master volume 1 ($10)" if charismamastervol1hold == 0 and charismamastervol1 == 0:
            if money >= 10:
                "You buy Charisma Master volume 1."
                $ charismamastervol1hold = 1
                $ money -= 10
                $ booksheld += 1
                jump buybook
            else:
                "You do not have enough money."
                jump buybook

        "Charisma Master volume 2 ($15)" if charismamastervol2hold == 0 and charismamastervol2 == 0 and charismamastervol1 == 1:
            if money >= 15:
                "You buy Charisma Master volume 2."
                $ charismamastervol2hold = 1
                $ money -= 15
                $ booksheld += 1
                jump buybook
            else:
                "You do not have enough money."
                jump buybook

        "Nevermind.":
            return
