label work_randomizer:
    if cayennestage1event == 1 and rngworkgirl == 1:
        $ cayenne_work_today = 1
        call Cayenne_Stage_1_Event_1 from _call_Cayenne_Stage_1_Event_1
        call bbworking
        return
    elif cayennestage1event2 == 1 and cayennestage1event == 0 and teacher.stage >= 2 and cayenne_work_today == 0:
        $ cayenne_work_today = 1
        call Cayenne_Stage_1_Event_2 from _call_Cayenne_Stage_1_Event_2
        call bbworking
        return
    elif cayennestage1event3 == 1 and cayennestage1event2 == 0 and teacher.stage >= 3 and cayenne_work_today == 0:
        $ cayenne_work_today = 1
        call Cayenne_Stage_1_Event_3 from _call_Cayenne_Stage_1_Event_3
        call bbworking
        return
    elif cayennestage1event4 == 1 and cayennestage1event3 == 0 and teacher.stage >= 4 and cayenne_work_today == 0:
        $ cayenne_work_today = 1
        call Cayenne_Stage_1_Event_4 from _call_Cayenne_Stage_1_Event_4
        call bbworking
        return
    elif cayennestage1event5 == 1 and cayennestage1event4 == 0 and teacher.stage >= 5 and cayenne_work_today == 0:
        $ cayenne_work_today = 1
        call Cayenne_Stage_1_Event_5 from _call_Cayenne_Stage_1_Event_5
        call bbworking
        return

    $ rngworkcustomer = renpy.random.randint(1,145)
    if rngworkcustomer <= 20:
        if rngworkgirl == 3:
            if amber_work_today == 1:
                jump work_randomizer
            $ amber_work_today = 1
            image cafe_amber_arrive = "/amber/[amber.stage]/arrive.webp"
            scene cafe_amber_arrive
            "A customer arrives at the diner."
            pc "Oh, hey, Amber."
            image cafe_amber_talk = "/amber/[amber.stage]/work_talk.webp"
            scene cafe_amber_talk
            amber "Hey. How's everything going today?"
            pc "Good. Not too busy."
            amber "Glad to hear it. I just came in to get some food."
            amber "I would like to order a hamburger and one slice of pizza."
            pc "Coming right up, please feel free to sit anywhere you would like."
            menu:
                "Create her food normally.":
                    "You create her food."
                    image cafe_amber_booth = "/amber/[amber.stage]/eating_booth.webp"
                    scene cafe_amber_booth
                    pc "Here you go. Have a nice meal."
                    amber "Thank you!"
                    $ amber.weight += 0.2
                "Use the secret fattening formula." if secretfeedervol1 == 1:
                    call BBfoodformula
                    image cafe_amber_booth = "/amber/[amber.stage]/eating_booth.webp"
                    scene cafe_amber_booth
                    pc "Here you go. Have a nice meal."
                    amber "Thank you!"
                    if secretfeedervol2 == 1:
                        $ amber.weight += 0.5
                    elif secretfeedervol1 == 1:
                        $ amber.weight += 0.3
                    else:
                        $ amber.weight += 0.2
                "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                    "You make her a lot more food than she asked for."
                    if secretfeedervol1 == 1:
                        call BBfoodformula
                    call Amber_BB_Extra
                    if secretfeedervol2 == 1:
                        $ amber.weight += 0.8
                    elif secretfeedervol1 == 1:
                        $ amber.weight += 0.5
                    else:
                        $ amber.weight += 0.3
                "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0 and amber.stage >= 7:
                    if secretfeedervol1 == 1:
                        call BBfoodformula
                    call Amber_BB_Prize
                    if secretfeedervol2 == 1:
                        $ amber.weight += 1.0
                    elif secretfeedervol1 == 1:
                        $ amber.weight += 0.8
                    else:
                        $ amber.weight += 0.6
                    $ weeklyprize -= 1
            call bbworking
            return

        elif rngworkgirl == 2:
            if marie_work_today == 1:
                jump work_randomizer
            $ marie_work_today = 1
            image cafe_marie_arrive = "/marie/[marie.stage]/arrive.webp"
            scene cafe_marie_arrive
            "A customer arrives at the diner."
            pc "Hey, it's Marie."
            image cafe_marie_talk = "/marie/[marie.stage]/work_talk.webp"
            scene cafe_marie_talk
            marie "Hey. How is my favourite coworker doing today?"
            pc "Pretty good."
            marie "Great. I'm just passing by for some food."
            marie "One burger and one slice of pizza, please."
            pc "Sure. Just grab a seat."
            menu:
                "Create her food normally.":
                    "You create her food."
                    image cafe_marie_booth = "/marie/[marie.stage]/eating_booth.webp"
                    scene cafe_marie_booth
                    pc "Here you go. Have a nice meal."
                    marie "Thank you!"
                    $ marie.weight += 0.2
                "Use the secret fattening formula." if secretfeedervol1 == 1:
                    call BBfoodformula
                    image cafe_marie_booth = "/marie/[marie.stage]/eating_booth.webp"
                    scene cafe_marie_booth
                    pc "Here you go. Have a nice meal."
                    marie "Thank you!"
                    if secretfeedervol2 == 1:
                        $ marie.weight += 0.5
                    elif secretfeedervol1 == 1:
                        $ marie.weight += 0.3
                    else:
                        $ marie.weight += 0.2
                "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                    "You make her a lot more food than she asked for."
                    if secretfeedervol1 == 1:
                        call BBfoodformula
                    call Marie_BB_Extra
                    if secretfeedervol2 == 1:
                        $ marie.weight += 1.0
                    elif secretfeedervol1 == 1:
                        $ marie.weight += 0.8
                    else:
                        $ marie.weight += 0.5
                "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0:
                    if secretfeedervol1 == 1:
                        call BBfoodformula
                    call Marie_BB_Prize
                    $ weeklyprize -= 1
                    if secretfeedervol2 == 1:
                        $ marie.weight += 1.5
                    elif secretfeedervol1 == 1:
                        $ marie.weight += 1.0
                    else:
                        $ marie.weight += 0.8
            call bbworking
            return

        elif rngworkgirl == 1:
            if lisa_work_today == 1:
                jump work_randomizer
            $ lisa_work_today = 1
            image cafe_lisa_arrive = "/lisa/[lisa.stage]/arrive.webp"
            scene cafe_lisa_arrive
            "A customer arrives at the diner."
            pc "Hey, it's Lisa."
            image cafe_lisa_talk = "/lisa/[lisa.stage]/work_talk.webp"
            scene cafe_lisa_talk
            lisa "Hey there, good day so far?"
            pc "Yeah, everything's running pretty smooth."
            lisa "Nice, I'm just here for some lunch."
            lisa "Can I get a burger and a slice of pizza?"
            pc "Coming right up, grab a seat and I'll bring it over."
            menu:
                "Create her food normally.":
                    "You create her food."
                    image cafe_lisa_booth = "/lisa/[lisa.stage]/eating_booth.webp"
                    scene cafe_lisa_booth
                    pc "Here you go. Have a nice meal."
                    lisa "Thank you!"
                    $ lisa.weight += 0.2
                "Use the secret fattening formula." if secretfeedervol1 == 1:
                    call BBfoodformula
                    image cafe_lisa_booth = "/lisa/[lisa.stage]/eating_booth.webp"
                    scene cafe_lisa_booth
                    pc "Here you go. Have a nice meal."
                    lisa "Thank you!"
                    if secretfeedervol2 == 1:
                        $ lisa.weight += 0.5
                    elif secretfeedervol1 == 1:
                        $ lisa.weight += 0.3
                    else:
                        $ lisa.weight += 0.2
                "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                    "You make a lot more food than she asked for."
                    if secretfeedervol1 == 1:
                        call BBfoodformula
                    call Lisa_BB_Extra
                    if secretfeedervol2 == 1:
                        $ lisa.weight += 0.8
                    elif secretfeedervol1 == 1:
                        $ lisa.weight += 0.5
                    else:
                        $ lisa.weight += 0.3
                "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0 and lisa.stage >= 7:
                    if secretfeedervol1 == 1:
                        call BBfoodformula
                    call Lisa_BB_Prize
                    $ weeklyprize -= 1
                    if secretfeedervol2 == 1:
                        $ lisa.weight += 1.0
                    elif secretfeedervol1 == 1:
                        $ lisa.weight += 0.8
                    else:
                        $ lisa.weight += 0.6
            call bbworking
            return
    #BONNIE
    elif rngworkcustomer <= 30:
        if bonnie_work_today == 1:
            jump work_randomizer
        $ bonnie_work_today = 1
        if bonnieintroduction == 1:
            call Bonnie_Introduction from _call_Bonnie_Introduction
            return
        elif bonniestage11event == 0:
            image cafe_bonnie_arrive = "/bonnie/[bonnie.stage]/cafe_arrive.webp"
            scene cafe_bonnie_arrive
            "A customer arrives at the diner."
            pc "Hey, it’s Bonnie!"
            image cafe_bonnie_talk = "/bonnie/[bonnie.stage]/cafe_talk.webp"
            scene cafe_bonnie_talk
            bonnie "Hi, [playername]."
            pc "Hi. How are you today?"
            bonnie "I am good and so is the shop."
            bonnie "Things are selling well. We might have to increase how much you make each week if this keeps up."
            pc "Well, we have to keep our customers satisfied."
            pc "Speaking of, what can I get you today?"
        elif bonniestage10event == 0:
            image cafe_bonnie_arrive = "/bonnie/[bonnie.stage]/cafe_arrive.webp"
            scene cafe_bonnie_arrive
            "A customer arrives at the diner."
            pc "Hey, it’s Bonnie!"
            image cafe_bonnie_talk = "/bonnie/[bonnie.stage]/cafe_talk.webp"
            scene cafe_bonnie_talk
            bonnie "Hi, [playername]."
            pc "Hi. How are you today?"
            bonnie "I am good, thank you."
            bonnie "Although truthfully, I'm still a little on edge after what happened."
            bonnie "But I have changed the locks and everything seems to have gone back to normal."
            pc "I'm sure it was just a hungry fan."
            bonnie "Yeah. Although, I have been wondering if it might have something to do with the new chocolates. They are really good and a little bit addictive, even for me!"
            pc "So, do you want me to stop making them?"
            bonnie "No way! I just need to be more careful who I give them to."
            pc "What can I get you today?"
        elif bonniestage9event == 0:
            image cafe_bonnie_arrive = "/bonnie/[bonnie.stage]/cafe_arrive.webp"
            scene cafe_bonnie_arrive
            "A customer arrives at the diner."
            pc "Hey, it’s Bonnie!"
            image cafe_bonnie_talk = "/bonnie/[bonnie.stage]/cafe_talk.webp"
            scene cafe_bonnie_talk
            bonnie "Hi, [playername]."
            pc "Hi. How are you today?"
            bonnie "I am really good. The customers are already flooding back."
            bonnie "I really do owe you for helping with Rebecca."
            pc "It was no problem. Besides, I think you more than paid me back."
            bonnie "I think I slept for about twelve hours after that cake."
            bonnie "Hopefully that's the last time you have to save the shop. Not sure I can take another thank you cake stuffing."
            bonnie "It took me two days to be able to fit into my clothes again after all that cake."
            pc "Well, if that's the payment I might have to try and find a way of saving the shop again."
            pc "What can I get you today?"
        elif bonniestage8event == 0:
            image cafe_bonnie_arrive = "/bonnie/[bonnie.stage]/cafe_arrive.webp"
            scene cafe_bonnie_arrive
            "A customer arrives at the diner."
            pc "Hey, it’s Bonnie!"
            image cafe_bonnie_talk = "/bonnie/[bonnie.stage]/cafe_talk.webp"
            scene cafe_bonnie_talk
            bonnie "Hi, [playername]."
            pc "Hi. How are you today?"
            bonnie "I am good."
            bonnie "How is everyone here? Have you had any complaints about the chocolates I accidentally sent here?"
            pc "No. In fact, we have people asking when they might be back!"
            bonnie "That's good to hear. Well, at least people don't seem to be mad."
            pc "I don't think anyone can get mad about free chocolates."
            pc "What can I get you today?"
        elif bonniestage7event == 0:
            image cafe_bonnie_arrive = "/bonnie/[bonnie.stage]/cafe_arrive.webp"
            scene cafe_bonnie_arrive
            "A customer arrives at the diner."
            pc "Hey, it’s Bonnie!"
            image cafe_bonnie_talk = "/bonnie/[bonnie.stage]/cafe_talk.webp"
            scene cafe_bonnie_talk
            bonnie "Hi, [playername]."
            pc "Hi. How are you today?"
            bonnie "I am good. Relieved that the event is over."
            bonnie "Happy to go back to just running the store."
            pc "I'm sure it went well and people appreciated your chocolates."
            pc "Or at least I appreciated what you did to them."
            "Bonnie blushes."
            pc "What can I get you today?"
        elif bonniestage6event == 0:
            image cafe_bonnie_arrive = "/bonnie/[bonnie.stage]/cafe_arrive.webp"
            scene cafe_bonnie_arrive
            "A customer arrives at the diner."
            pc "Hey, it’s Bonnie!"
            image cafe_bonnie_talk = "/bonnie/[bonnie.stage]/cafe_talk.webp"
            scene cafe_bonnie_talk
            bonnie "Hi, [playername]."
            pc "Hi. How are you doing?"
            bonnie "Good. Although, I’m a little embarrassed."
            bonnie "I just can't seem to control myself around your chocolates."
            pc "Don't be. It's the best compliment the chocolates can get."
            pc "What can I get you today?"
        elif bonniestage5event == 0:
            image cafe_bonnie_arrive = "/bonnie/[bonnie.stage]/cafe_arrive.webp"
            scene cafe_bonnie_arrive
            "A customer arrives at the diner."
            pc "Hey, it’s Bonnie!"
            image cafe_bonnie_talk = "/bonnie/[bonnie.stage]/cafe_talk.webp"
            scene cafe_bonnie_talk
            bonnie "Hi. Thanks again for all your help earlier."
            bonnie "Although I'm a little embarrassed about what happened."
            pc "Don't be. It's the best compliment the chocolates can get."
            pc "What can I get you today?"
        elif bonniestage4event == 0:
            image cafe_bonnie_arrive = "/bonnie/[bonnie.stage]/cafe_arrive.webp"
            scene cafe_bonnie_arrive
            "A customer arrives at the diner."
            pc "Hey, it’s Bonnie!"
            image cafe_bonnie_talk = "/bonnie/[bonnie.stage]/cafe_talk.webp"
            scene cafe_bonnie_talk
            bonnie "Hi, thanks again for all your help earlier."
            pc "No problem, glad to see the shop is doing so well."
            pc "What can I get you today?"
        elif bonniestage3event == 0:
            image cafe_bonnie_arrive = "/bonnie/[bonnie.stage]/cafe_arrive.webp"
            scene cafe_bonnie_arrive
            "A customer arrives at the diner."
            pc "Hey, it’s Bonnie!"
            image cafe_bonnie_talk = "/bonnie/[bonnie.stage]/cafe_talk.webp"
            scene cafe_bonnie_talk
            bonnie "Hi. How have you been?"
            pc "I've been good, thank you. How is the store?"
            bonnie "Doing much better thanks to you."
            pc "It’s a team effort."
            pc "What can I get you today?"
        elif bonniestage2event == 0:
            image cafe_bonnie_arrive = "/bonnie/[bonnie.stage]/cafe_arrive.webp"
            scene cafe_bonnie_arrive
            "A customer arrives at the diner."
            pc "Hey, it’s Bonnie!"
            image cafe_bonnie_talk = "/bonnie/[bonnie.stage]/cafe_talk.webp"
            scene cafe_bonnie_talk
            bonnie "Hey, if it isn’t my loyal customer. How were those sweets?"
            pc "They were great, my friend really enjoyed them."
            bonnie "That’s good to hear."
            pc "What can I get you today?"
        else:
            image cafe_bonnie_arrive = "/bonnie/[bonnie.stage]/cafe_arrive.webp"
            scene cafe_bonnie_arrive
            "A customer arrives at the diner."
            pc "Hey, it’s the girl from the sweets shop."
            image cafe_bonnie_talk = "/bonnie/[bonnie.stage]/cafe_talk.webp"
            scene cafe_bonnie_talk
            bonnie "Hey, if it isn’t my loyal customer."
            pc "This time you are my customer haha."

        bonnie "I would like to order a hamburger and one slice of pizza."
        pc "Coming right up, please feel free to sit anywhere you would like."
        image cafe_bonnie_ass = "/bonnie/[bonnie.stage]/cafe_ass.webp"
        scene cafe_bonnie_ass
        menu:
            "Create her food normally.":
                "You create her food."
                call Bonnie_BB_Normal
                $ bonnie.weight += 0.1

            "Use the secret fattening formula." if secretfeedervol1 == 1:
                call BBfoodformula
                call Bonnie_BB_Normal
                if secretfeedervol2 == 1:
                    $ bonnie.weight += 0.3
                elif secretfeedervol1 == 1:
                    $ bonnie.weight += 0.2
                else:
                    $ bonnie.weight += 0.1

            "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                "You make her a lot more food than she asked for."
                if secretfeedervol1 == 1:
                    call BBfoodformula
                "You decide to pay the difference yourself."
                $ money -= 5
                call Bonnie_BB_Extra
                

            "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0 and bonnie.stage >= 7:
                if secretfeedervol1 == 1:
                    call BBfoodformula
                call Bonnie_BB_Prize
                if secretfeedervol2 == 1:
                    $ bonnie.weight += 1.0
                elif secretfeedervol1 == 1:
                    $ bonnie.weight += 0.8
                else:
                    $ bonnie.weight += 0.6
                $ weeklyprize -= 1

        call bbworking
        return

    elif rngworkcustomer <= 40:
        if trista_work_today == 1:
            jump work_randomizer
        $ trista_work_today = 1
        image cafe_trista_arrive = "/trista/[trista.stage]/cafe_arrive.webp"
        scene cafe_trista_arrive
        if tristastage10event == 0:
            "Hey, it's Trista."
            image cafe_trista_talk = "/trista/[trista.stage]/cafe_talk.webp"
            scene cafe_trista_talk
            trista "Hey, [playername]. How are you doing?"
            pc "I'm good, thanks. What about you?"
            trista "Really good, thanks. I'm excited for the first time in a while."
            trista "I haven't had a new challenge in a while."
            pc "That is good to hear. What would you like to order?"
        elif tristastage8event == 0:
            "Hey, it's Trista."
            image cafe_trista_talk = "/trista/[trista.stage]/cafe_talk.webp"
            scene cafe_trista_talk
            trista "Hey, [playername]."
            pc "How are you doing?"
            trista "Good. Working hard to start turning this bulk into muscle mass."
            trista "But I still need to keep the calories up to make sure I don't lose any performance."
            pc "What would you like to order?"
        elif tristastage7event == 0:
            "Hey, it's Trista."
            image cafe_trista_talk = "/trista/[trista.stage]/cafe_talk.webp"
            scene cafe_trista_talk
            trista "Hey, [playername]. How are you doing?"
            pc "I'm good, thanks. Feeling fitter every day."
            trista "Perfect. You have come a long way since you started."
            pc "Thank you. I definitely notice the difference."
            pc "What would you like to order?"
        elif tristastage6event == 0:
            "Hey, it's Trista."
            image cafe_trista_talk = "/trista/[trista.stage]/cafe_talk.webp"
            scene cafe_trista_talk
            trista "Hey, [playername]. How are you doing?"
            pc "I'm good. How is your training?"
            trista "Good. The gym has been a bit quiet, so the machines are free."
            pc "What would you like to order?"
        elif katrinestage5event == 0:
            "Hey, it's Trista."
            image cafe_trista_talk = "/trista/[trista.stage]/cafe_talk.webp"
            scene cafe_trista_talk
            trista "Hey, [playername]. How are you doing?"
            pc "I'm good, what about you?"
            trista "Good, still buzzing from qualifying."
            trista "But the hard work starts now."
            pc "What would you like to order?"
        elif tristastage4event == 0:
            "Hey, it's Trista."
            image cafe_trista_talk = "/trista/[trista.stage]/cafe_talk.webp"
            scene cafe_trista_talk
            trista "Hey, [playername]. How are you doing?"
            pc "I'm good. What about you?"
            trista "Good. Still buzzing from qualifying."
            trista "But the hard work starts now."
            pc "What would you like to order?"
        elif tristastage3event == 0:
            "Hey, it's Trista."
            image cafe_trista_talk = "/trista/[trista.stage]/cafe_talk.webp"
            scene cafe_trista_talk
            trista "Hey, [playername]. How are you doing?"
            pc "I'm good, thanks. You coming here from your gym?"
            trista "Yes. Worked up quite the appetite."
            pc "Well in that case what would you like to order?"
        elif tristastage2event == 0:
            "Hey, it's Trista."
            image cafe_trista_talk = "/trista/[trista.stage]/cafe_talk.webp"
            scene cafe_trista_talk
            trista "Hey, [playername]. How are you doing?"
            pc "I'm feeling good. Thanks to our workouts."
            trista "No problem. Keep working at it and we will make an athlete out of you one day."
            pc "What would you like to order?"
        elif gymunlock == 1:
            "Hey, it's Trista."
            image cafe_trista_talk = "/trista/[trista.stage]/cafe_talk.webp"
            scene cafe_trista_talk
            trista "Hey, [playername]. How are you doing?"
            pc "I'm feeling good. How are you?"
            trista "Good. Worked up quite the appetite."
            pc "Well, in that case, what would you like to order?"
        else:
            $ unknownname = 'Sporty girl'
            "A customer arrives."
            image cafe_trista_talk = "/trista/[trista.stage]/cafe_talk.webp"
            scene cafe_trista_talk
            pc "Hi, how can I help you today?"
            unknown "I would like to order a hamburger and one slice of pizza."
            pc "Coming right up, please feel free to sit anywhere you would like."
            image cafe_trista_ass = "/trista/[trista.stage]/cafe_ass.webp"
            scene cafe_trista_ass
            "You create her food."
            image cafe_trista_booth = "/trista/[trista.stage]/cafe_booth.webp"
            scene cafe_trista_booth
            pc "Here you go. Have a nice meal."
            unknown "Thank you!"
            $ unknownname = 'Unknown'
            $ trista.weight += 0.2
            call bbworking
            return

        trista "I would like to order a hamburger and one slice of pizza."
        pc "Coming right up, please feel free to sit anywhere you would like."
        image cafe_trista_ass = "/trista/[trista.stage]/cafe_ass.webp"
        scene cafe_trista_ass
        menu:
            "Create her food normally.":
                "You create her food."
                image cafe_trista_booth = "/trista/[trista.stage]/cafe_booth.webp"
                scene cafe_trista_booth
                pc "Here you go. Have a nice meal."
                trista "Thank you!"
                $ trista.weight += 0.2
            "Use the secret fattening formula." if secretfeedervol1 == 1:
                call BBfoodformula
                image cafe_trista_booth = "/trista/[trista.stage]/cafe_booth.webp"
                scene cafe_trista_booth
                pc "Here you go. Have a nice meal."
                trista "Thank you!"
                if secretfeedervol2 == 1:
                    $ trista.weight += 0.5
                elif secretfeedervol1 == 1:
                    $ trista.weight += 0.3
                else:
                    $ trista.weight += 0.2
            "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                "You make her a lot more food than she asked for."
                if secretfeedervol1 == 1:
                    call BBfoodformula
                "You decide to pay the difference yourself."
                $ money -= 5
                image cafe_trista_extrafood = "/trista/[trista.stage]/cafe_extrafood.webp"
                scene cafe_trista_extrafood
                call Trista_BB_Extra
                if secretfeedervol2 == 1:
                    $ trista.weight += 0.8
                elif secretfeedervol1 == 1:
                    $ trista.weight += 0.5
                else:
                    $ trista.weight += 0.3
            "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0 and trista.stage >= 5:
                if secretfeedervol1 == 1:
                    call BBfoodformula
                call Trista_BB_Prize
                $ weeklyprize -= 1
                if secretfeedervol2 == 1:
                    $ trista.weight += 1.0
                elif secretfeedervol1 == 1:
                    $ trista.weight += 0.8
                else:
                    $ trista.weight += 0.6

        call bbworking
        return

    elif rngworkcustomer <= 45:
        if caroline_work_today == 1:
            jump work_randomizer
        if carolinestage3event == 1:
            $ caroline_work_today = 1
            image cafe_hanna_arrive = "/side/hanna_cafe_arrive.webp"
            scene cafe_hanna_arrive
            "A customer arrives at the diner."
            $ unknownname = 'Plump Woman'
            "She looks quite large."
            image cafe_hanna_talk = "/side/hanna_cafe_talk.webp"
            scene cafe_hanna_talk
            unknown "Hello, I would like to order."
            pc "Go ahead."
            "She points at the menu."
            unknown "I would like one of these and one of that thing."
            pc "Coming right up, please feel free to sit anywhere you would like."
            "You create her food."
            image cafe_hanna_booth = "/side/hanna_cafe_booth.webp"
            scene cafe_hanna_booth
            pc "Here you go. Have a nice meal."
            unknown "Thank you!"
            $ unknownname = 'Unknown'
            call bbworking
            return
        $ caroline_work_today = 1
        if carolinestage3event == 0 and caroline.stage == 3 and carolineBBfirsttime == 1:
            ##First time Stage 3 ##
            image cafe_caroline_arrive = "/caroline/[caroline.stage]/cafe_arrive.webp"
            scene cafe_caroline_arrive
            "A customer arrives."
            pc "Hey, it's Caroline."
            image cafe_caroline_talk = "/caroline/[caroline.stage]/cafe_talk.webp"
            scene cafe_caroline_talk
            caroline "Hi [playername]."
            pc "How are you doing?"
            caroline "Good thanks, just thought I would pop out to get some food."
            caroline "Needed some space."
            pc "Sorry to hear that."
            caroline "But that is enough about me, I guess I should tell you what I want right."
            pc "Sure, what would you like?"
            caroline "Can I just get some chicken nuggets and fries please."
            pc "Coming right up, if you want to find a seat I'll bring it over when it is done."
            image cafe_caroline_ass = "/caroline/[caroline.stage]/cafe_ass.webp"
            scene cafe_caroline_ass
            caroline "Thanks."
            "You create her food."
            if secretfeedervol1 == 1:
                call BBfoodformula
            image cafe_caroline_booth2 = "/caroline/[caroline.stage]/cafe_booth2.webp"
            scene cafe_caroline_booth2
            pc "Here you go, enjoy your meal."
            caroline "Thank you."
            $ carolineBBfirsttime = 0
        
        elif carolinestage3event == 0 and caroline.stage == 3 and carolineBBfirsttime == 0:
            ##Stage 3 ##
            image cafe_caroline_arrive = "/caroline/[caroline.stage]/cafe_arrive.webp"
            scene cafe_caroline_arrive
            pc "Hey, it's Caroline."
            image cafe_caroline_talk = "/caroline/[caroline.stage]/cafe_talk.webp"
            scene cafe_caroline_talk
            caroline "Hi [playername]."
            pc "How are you doing?"
            caroline "Good thanks, was having a walk and thought I would pop in."
            pc "What can I get for you?"
            caroline "Can I get a burger, some fries, onion rings and a soda please."
            pc "Coming right up, please find a nice place to sit down."
            image cafe_caroline_ass = "/caroline/[caroline.stage]/cafe_ass.webp"
            scene cafe_caroline_ass
            caroline "Thanks."
            "You create her food."
            if secretfeedervol1 == 1:
                call BBfoodformula
            image cafe_caroline_booth = "/caroline/[caroline.stage]/cafe_booth.webp"
            scene cafe_caroline_booth
            pc "Here you go, enjoy your meal."
            caroline "Thank you."

        elif caroline.stage >= 4:
            ##Stage 4 ##
            image cafe_caroline_arrive = "/caroline/[caroline.stage]/cafe_arrive.webp"
            scene cafe_caroline_arrive
            pc "Hey, it's Caroline."
            image cafe_caroline_talk = "/caroline/[caroline.stage]/cafe_talk.webp"
            scene cafe_caroline_talk
            caroline "Hey."
            pc "How are you doing?"
            caroline "Good thanks, really good actually."
            pc "I am happy to hear that."
            caroline "Thanks, I really feel like I have turned a corner in my life and I am excited to see what comes next."
            pc "Well, it might not be your next big thing but what can I get for you to eat?"
            caroline "Can I get a burger, some fries, onion rings and a soda please."
            pc "Coming right up, please find a nice place to sit down."
            image cafe_caroline_ass = "/caroline/[caroline.stage]/cafe_ass.webp"
            scene cafe_caroline_ass
            caroline "Thanks."
            "You create her food."
            if secretfeedervol1 == 1:
                call BBfoodformula
            image cafe_caroline_booth = "/caroline/[caroline.stage]/cafe_booth.webp"
            scene cafe_caroline_booth
            pc "Here you go, enjoy your meal."
            caroline "Thank you."

        if secretfeedervol2 == 1:
            $ caroline.weight += 0.5
        elif secretfeedervol1 == 1:
            $ caroline.weight += 0.3
        else:
            $ caroline.weight += 0.2
        call bbworking
        return


    elif rngworkcustomer <= 50:
        if cayenne_work_today == 1:
            jump work_randomizer
        if cayennestage2event == 1:
            jump work_randomizer
        $ cayenne_work_today = 1
        image cafe_cayenne_arrive = "/cayenne/[cayenne.stage]/cafe_arrive.webp"
        scene cafe_cayenne_arrive
        "Hey, it's Cayenne."
        image cafe_cayenne_talk = "/cayenne/[cayenne.stage]/cafe_talk.webp"
        scene cafe_cayenne_talk
        cayenne "Hey, [playername]. How’s the diner?"
        pc "Same as always. You here for an extra studying session?"
        cayenne "You got it. I’ve got to make my tutor proud."
        pc "I’ll do my best as well then. What can I get you?"
        cayenne "I would like to order a hamburger and one slice of pizza."
        pc "Coming right up, please feel free to sit anywhere you would like."
        image cafe_cayenne_ass = "/cayenne/[cayenne.stage]/cafe_ass.webp"
        scene cafe_cayenne_ass
        menu:
            "Create her food normally.":
                image cafe_cayenne_booth = "/cayenne/[cayenne.stage]/cafe_booth.webp"
                scene cafe_cayenne_booth
                "Making the food, you bring it over to her table and decide to chat for a bit."
                #(NOTE: At different stages, Cayenne should reply with different dialogue when choosing this option.)
                #Option 1)
                if cayenne.stage == 2 and cayennestage2event == 0:
                    pc "How’s the new house treating you?"
                    cayenne "A lot better than the old place I had. Feels great not having to count change for rent anymore."
                    cayenne "Well, I guess it just got swapped out for counting calories, but I’d say that’s an even trade."
                #Option 4) (Available after Cayenne’s stage 3 event)
                elif cayenne.stage == 3 and cayennestage3event == 0:
                    pc "How long have you been dancing?"
                    cayenne "It’s just something I’ve been doing for as far back as I can remember."
                    cayenne "One of the few things that you can do for fun that doesn’t cost a lot of money."
                    cayenne "Well, aside from that outfit, but I think it was worth it considering how you reacted to me."
                #Option 5) (Available after Cayenne’s stage 4 event)
                elif cayenne.stage == 4 and cayennestage4event == 0:
                    pc "Sorry if this is a little personal, but have you ever ‘exposed’ yourself like that in front of someone?"
                    cayenne "Can’t say it’s that personal since you were there with me."
                    cayenne "I don’t think I have an exhibitionist kink, but who knows. Maybe it was just something in the food."
                #Option 6) (Available after Cayenne’s stage 5 event)
                elif cayenne.stage == 5 and cayennestage5event == 0:
                    pc "I know I didn’t get a chance to say it at the time, but you have a really nice shower."
                    cayenne "To be fair you were kind of preoccupied with something else."
                    cayenne "That being said, thank you for the compliment. I spared no expense in making sure I lived the high life when I got that house."
                    cayenne "Had the shower custom made and everything. Thank goodness I sprung the extra cash for the larger size."
                    cayenne "Could you imagine trying do that kind of stuff in a dinky little tub?"
                #Option 7) (Available after Cayenne’s stage 6 event)
                elif cayenne.stage == 6 and cayennestage6event == 0:
                    pc "Were you every able to get the icing out of your workout clothes?"
                    cayenne "No, but then again I didn’t really bother. The outfit was already starting to feel a little tight, so I just bought a new one."
                    cayenne "Not like I don’t have the money to spare on more. That being said, I did keep the old clothes."
                    cayenne "Figured I might need them if I ever feel like acting like a pig again."
                #Option 2)
                elif cayenne.stage == 7 or cayenne.stage == 8:
                    pc "Have you been doing alright with your studies?"
                    cayenne "I think so. Kind of hard to say since I’m not with the other students."
                    cayenne "Only thing I can keep track of is how much I can eat in a single session."
                #Option 8) (Available after Cayenne’s stage 9 event)
                elif cayenne.stage == 9 and cayennestage9event == 0:
                    "Before you can ask your question, Cayenne speaks up."
                    cayenne "Are you okay with me ordering you around? I know you said it’s fine, but I can’t help feeling a little guilty about it."
                    pc "Rest assured, you’re not hurting me or anything. To be honest, everything you’ve been asking has been enjoyable and helpful for your study sessions."
                    "Cayenne breathes a sigh of relief."
                    cayenne "That’s what I figured, but I wanted to make sure. I’ll try not to go too crazy with the demands."
                #Option 3)
                elif cayenne.stage >= 2 and cayennestage2event == 0:
                    pc "How have you been liking the study materials?"
                    cayenne "You mean the food? Alright I guess."
                    cayenne "Still not sure what this all has to do with my education, but I’m not complaining about free stuff. Especially when it tastes so good."
                #(NOTE: The following should play out after any of the above dialogue options)
                #Image: Cayenne waving at the player as she leaves Bunny Bites
                "Finishing up her food and paying her bill, Cayenne waves goodbye as she leaves the diner."
                $ cayenne.weight += 0.2
            "Use the secret fattening formula." if secretfeedervol1 == 1:
                image cafe_cayenne_booth = "/cayenne/[cayenne.stage]/cafe_booth.webp"
                scene cafe_cayenne_booth
                "Making the food with the secret fattening formula, you bring it over to her table and decide to chat for a bit."
                #(NOTE: At different stages, Cayenne should reply with different dialogue when choosing this option.)
                #Option 1)
                if cayenne.stage == 2 and cayennestage2event == 0:
                    pc "How’s the new house treating you?"
                    cayenne "A lot better than the old place I had. Feels great not having to count change for rent anymore."
                    cayenne "Well, I guess it just got swapped out for counting calories, but I’d say that’s an even trade."
                #Option 4) (Available after Cayenne’s stage 3 event)
                elif cayenne.stage == 3 and cayennestage3event == 0:
                    pc "How long have you been dancing?"
                    cayenne "It’s just something I’ve been doing for as far back as I can remember."
                    cayenne "One of the few things that you can do for fun that doesn’t cost a lot of money."
                    cayenne "Well, aside from that outfit, but I think it was worth it considering how you reacted to me."
                #Option 5) (Available after Cayenne’s stage 4 event)
                elif cayenne.stage == 4 and cayennestage4event == 0:
                    pc "Sorry if this is a little personal, but have you ever ‘exposed’ yourself like that in front of someone?"
                    cayenne "Can’t say it’s that personal since you were there with me."
                    cayenne "I don’t think I have an exhibitionist kink, but who knows. Maybe it was just something in the food."
                #Option 6) (Available after Cayenne’s stage 5 event)
                elif cayenne.stage == 5 and cayennestage5event == 0:
                    pc "I know I didn’t get a chance to say it at the time, but you have a really nice shower."
                    cayenne "To be fair you were kind of preoccupied with something else."
                    cayenne "That being said, thank you for the compliment. I spared no expense in making sure I lived the high life when I got that house."
                    cayenne "Had the shower custom made and everything. Thank goodness I sprung the extra cash for the larger size."
                    cayenne "Could you imagine trying do that kind of stuff in a dinky little tub?"
                #Option 7) (Available after Cayenne’s stage 6 event)
                elif cayenne.stage == 6 and cayennestage6event == 0:
                    pc "Were you every able to get the icing out of your workout clothes?"
                    cayenne "No, but then again I didn’t really bother. The outfit was already starting to feel a little tight, so I just bought a new one."
                    cayenne "Not like I don’t have the money to spare on more. That being said, I did keep the old clothes."
                    cayenne "Figured I might need them if I ever feel like acting like a pig again."
                #Option 2)
                elif cayenne.stage == 7 or cayenne.stage == 8:
                    pc "Have you been doing alright with your studies?"
                    cayenne "I think so. Kind of hard to say since I’m not with the other students."
                    cayenne "Only thing I can keep track of is how much I can eat in a single session."
                #Option 8) (Available after Cayenne’s stage 9 event)
                elif cayenne.stage == 9 and cayennestage6event == 0:
                    "Before you can ask your question, Cayenne speaks up."
                    cayenne "Are you okay with me ordering you around? I know you said it’s fine, but I can’t help feeling a little guilty about it."
                    pc "Rest assured, you’re not hurting me or anything. To be honest, everything you’ve been asking has been enjoyable and helpful for your study sessions."
                    "Cayenne breathes a sigh of relief."
                    cayenne "That’s what I figured, but I wanted to make sure. I’ll try not to go too crazy with the demands."
                #Option 3)
                elif cayenne.stage >= 2 and cayennestage2event == 0:
                    pc "How have you been liking the study materials?"
                    cayenne "You mean the food? Alright I guess."
                    cayenne "Still not sure what this all has to do with my education, but I’m not complaining about free stuff. Especially when it tastes so good."
                #(NOTE: The following should play out after any of the above dialogue options)
                #Image: Cayenne waving at the player as she leaves Bunny Bites
                "Finishing up her food and paying her bill, Cayenne waves goodbye as she leaves the diner."
                if secretfeedervol2 == 1:
                    $ cayenne.weight += 0.5
                elif secretfeedervol1 == 1:
                    $ cayenne.weight += 0.3
                else:
                    $ cayenne.weight += 0.2
            "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                "You make her a lot more food than she asked for."
                if secretfeedervol1 == 1:
                    "You create her food with the secret fattening formula."
                "You decide to pay the difference yourself."
                $ money -= 5
                image cafe_cayenne_extrafood = "/cayenne/[cayenne.stage]/cafe_extrafood.webp"
                scene cafe_cayenne_extrafood
                cayenne "Woah, this is way more than I ordered, I think the orders got mixed up."
                pc "Oh, I'm sorry, are you alright with taking this order without additional cost?"
                cayenne "Well, I won't say no to free food."
                pc "In that case, I hope you enjoy the food."
                cayenne "Thank you!"
                image cafe_cayenne_struggle = "/cayenne/[cayenne.stage]/cafe_struggle.webp"
                scene cafe_cayenne_struggle
                "You notice Cayenne struggling to eat all of the extra food."
                if secretfeedervol2 == 1:
                    $ cayenne.weight += 0.8
                elif secretfeedervol1 == 1:
                    $ cayenne.weight += 0.5
                else:
                    $ cayenne.weight += 0.3
            "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0 and disable == 1:
                "You make her at least 50 chicken nuggets and 5 burgers."
                if secretfeedervol1 == 1:
                    "You create her food with the secret fattening formula."
                #Picture NEEDED
                "You walk up to her booth to inform her that she won a prize."
                pc "Congratulations, you win the customer of the week prize."
                pc "Which means you get to eat as much food as you wish today."
                cayenne "OMG, thank you so much."
                "You set down the food on her table."
                #PICTURE NEEDED
                "Cayenne looks nervously at the tower of food you put on her table."
                pc "There you go, i hope you enjoy the food."
                pc "And don't be afraid to ask for more, you get to have as much as you want."
                #PICTURE NEEDED
                cayenne "I am not sure if i can eat this much, this is enough to feed a small family."
                cayenne "But i will do my best, thanks again!"
                #PICTURE NEEDED
                "You keep an eye on Cayenne"
                "She looks determined to eat as much as she can"
                #PICTURE NEEDED
                "After a while her eating slows down."
                "Her belly looks visibly larger than before she started eating."
                #PICTURE NEEDED
                "She finished eating all the food."
                "While rubbing her stuffed belly she looks embarresed by what she just did."
                #PICTURE NEEDED
                pc "It looks like you enjoyed the food."
                cayenne "I might have eaten a bit too much this time."
                #PICTURE NEEDED
                "You clean up while Cayenne takes her leave."
                cayenne "Thanks again, have a good day!"
        call bbworking
        return


    elif rngworkcustomer <= 60:
        if katrine_work_today == 1:
            jump work_randomizer
        $ katrine_work_today = 1
        image cafe_katrine_arrive = "/katrine/[katrine.stage]/cafe_arrive.webp"
        scene cafe_katrine_arrive
        "A customer arrives."
        if katrinestage10event == 0:
            pc "Hey, it's Katrine."
            image cafe_katrine_talk = "/katrine/[katrine.stage]/cafe_talk.webp"
            scene cafe_katrine_talk
            katrine "Hey, [playername]. How are you doing?"
            pc "I am good, thanks. What about you?"
            katrine "Really good, thanks."
            katrine "After our talk the other day it feels like a weight has been lifted off my shoulders."
            pc "That is good to hear. Glad you are feeling back to your old self."
            pc "What would you like to order?"
        elif katrinestage9event == 0:
            pc "Hey, it's Katrine."
            image cafe_katrine_talk = "/katrine/[katrine.stage]/cafe_talk.webp"
            scene cafe_katrine_talk
            katrine "Hey, [playername]."
            pc "How are you doing?"
            katrine "I'm exhausted. Still trying to lose the weight, but it keeps piling on."
            pc "You look great to me. Ignore what Trista says."
            katrine "Thanks. That's sweet."
            katrine "But she is right. This is the heaviest I have ever been."
            pc "What would you like to order?"
        elif katrinestage8event == 0:
            pc "Hey, it's Katrine."
            image cafe_katrine_talk = "/katrine/[katrine.stage]/cafe_talk.webp"
            scene cafe_katrine_talk
            katrine "Hey, [playername]."
            pc "How are you doing?"
            katrine "I'm exhausted. I've been working out nonstop trying to lose this weight."
            katrine "But at least I have earned it this time."
            pc "You look great to me."
            katrine "Thanks. That's sweet."
            pc "What would you like to order?"
        elif katrinestage7event == 0:
            pc "Hey, it's Katrine."
            image cafe_katrine_talk = "/katrine/[katrine.stage]/cafe_talk.webp"
            scene cafe_katrine_talk
            katrine "Hey, [playername]. How is my gym buddy doing?"
            pc "I am good. You been to the gym?"
            katrine "Yes. Had the place to myself, thankfully."
            pc "You still avoiding Trista?"
            katrine "Not exactly avoiding, just enjoying it when she is not around."
            pc "It is her gym."
            katrine "I know and I'm thankful for her letting me work out there."
            katrine "Can I place my order?"
            pc "Sorry. What would you like to order?"
        elif katrinestage6event == 0:
            pc "Hey, it's Katrine."
            image cafe_katrine_talk = "/katrine/[katrine.stage]/cafe_talk.webp"
            scene cafe_katrine_talk
            katrine "Hey, [playername]. How is my gym buddy doing?"
            pc "I am good. You been to the gym?"
            katrine "Yes. Thankfully passed Trista on her way in."
            katrine "Might be able to eat in peace this time."
            pc "I'm sure she didn’t mean to interrupt our meal."
            katrine "You give people too much benefit of the doubt, but I guess you are right."
            pc "Anyway, what would you like to order?"
        elif katrinestage5event == 0:
            pc "Hey, it's Katrine."
            image cafe_katrine_talk = "/katrine/[katrine.stage]/cafe_talk.webp"
            scene cafe_katrine_talk
            katrine "Hey, [playername]. How is my gym buddy doing?"
            pc "I am good. What about you?"
            katrine "Great. I needed a break from writing."
            pc "And here I was thinking you had come to see me."
            katrine "Needy much?"
            pc "What would you like to order?"
        elif katrinestage4event == 0:
            pc "Hey, it's Katrine."
            image cafe_katrine_talk = "/katrine/[katrine.stage]/cafe_talk.webp"
            scene cafe_katrine_talk
            katrine "Hey, [playername]. How is my gym buddy doing?"
            pc "I am good. What about you?"
            katrine "I'm starving. Been looking forward to this all workout."
            pc "Well, we do have some of the best food in town."
            pc "What would you like to order?"
        elif katrinestage3event == 0:
            pc "Hey, it's Katrine."
            image cafe_katrine_talk = "/katrine/[katrine.stage]/cafe_talk.webp"
            scene cafe_katrine_talk
            katrine "Hey, [playername]. How is my gym buddy doing?"
            pc "I am good. You just been to the gym?"
            katrine "You know me, burning off these calories before I eat them."
            pc "What would you like to order?"
        elif katrinestage2event == 0:
            pc "Hey, it's Katrine."
            image cafe_katrine_talk = "/katrine/[katrine.stage]/cafe_talk.webp"
            scene cafe_katrine_talk
            katrine "Hey, [playername]. How is my gym buddy doing?"
            pc "I am good. You just been to the gym?"
            katrine "No. I'm taking it a little bit easier this week."
            katrine "It's always good to listen to your body if you get a muscle tweak."
            katrine "But I can work extra hard next time to burn off this meal."
            pc "What would you like to order?"
        elif katrine_stats_visible == 1:
            pc "Hey, it's Katrine."
            image cafe_katrine_talk = "/katrine/[katrine.stage]/cafe_talk.webp"
            scene cafe_katrine_talk
            katrine "Hey, [playername]. How are you doing?"
            pc "I'm good thank you, what about you?"
            katrine "I'm good, just got back from the gym."
            pc "Working up an appetite."
            katrine "Exactly, means I can eat what I want here."
            pc "What would you like to order?"
        else:
            $ unknownname = 'Sporty brunette'
            pc "Hey, is that the girl I saw running earlier?"
            image cafe_katrine_talk = "/katrine/[katrine.stage]/cafe_talk.webp"
            scene cafe_katrine_talk
            unknown "Hey, how are you doing?"
            pc "I'm good thank you, what would you like to order?"
            unknown "I would like to order a hamburger and one slice of pizza."
            pc "Coming right up, please feel free to sit anywhere you would like."
            image cafe_katrine_booth = "/katrine/[katrine.stage]/cafe_booth.webp"
            scene cafe_katrine_booth
            pc "Here you go. Have a nice meal."
            unknown "Thank you!"
            $ katrine.weight += 0.2
            $ unknownname = 'Unknown'
            call bbworking
            return

        katrine "I would like to order a hamburger and one slice of pizza."
        pc "Coming right up, please feel free to sit anywhere you would like."
        menu:
            "Create her food normally.":
                "You create her food."
                image cafe_katrine_booth = "/katrine/[katrine.stage]/cafe_booth.webp"
                scene cafe_katrine_booth
                pc "Here you go. Have a nice meal."
                katrine "Thank you!"
                $ katrine.weight += 0.2
            "Use the secret fattening formula." if secretfeedervol1 == 1:
                call BBfoodformula
                image cafe_katrine_booth = "/katrine/[katrine.stage]/cafe_booth.webp"
                scene cafe_katrine_booth
                pc "Here you go. Have a nice meal."
                katrine "Thank you!"
                if secretfeedervol2 == 1:
                    $ katrine.weight += 0.5
                elif secretfeedervol1 == 1:
                    $ katrine.weight += 0.3
                else:
                    $ katrine.weight += 0.2
            "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                "You make her a lot more food than she asked for."
                if secretfeedervol1 == 1:
                    call BBfoodformula
                "You pay for the difference yourself."
                $ money -= 5
                image cafe_katrine_extrafood = "/katrine/[katrine.stage]/cafe_extrafood.webp"
                scene cafe_katrine_extrafood
                call Katrine_BB_Extra
                if secretfeedervol2 == 1:
                    $ katrine.weight += 0.8
                elif secretfeedervol1 == 1:
                    $ katrine.weight += 0.5
                else:
                    $ katrine.weight += 0.3
            "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0 and katrine.stage >= 6:
                if secretfeedervol1 == 1:
                    call BBfoodformula
                call Katrine_BB_Prize
                $ weeklyprize -= 1
                if secretfeedervol2 == 1:
                    $ katrine.weight += 1.0
                elif secretfeedervol1 == 1:
                    $ katrine.weight += 0.8
                else:
                    $ katrine.weight += 0.6
        call bbworking
        return

    elif rngworkcustomer <= 70:
        if luna_work_today == 1:
            jump work_randomizer
        $ luna_work_today = 1
        if teacherstage3event == 1:
            if lunabunnybitesevent == 1:
                image cafe_luna_arrive = "/luna/[luna.stage]/cafe_arrive.webp"
                scene cafe_luna_arrive
                "A customer comes into the restaurant."
                "You can't help but notice how attractive she is and she in return looks particularly happy to see you."
                $ unknownname = 'Attractive Woman'
                image cafe_luna_talk = "/luna/[luna.stage]/cafe_talk.webp"
                scene cafe_luna_talk
                unknown "Hi, you must be new."
                pc "Yes, I'm new, just helping out and working part time."
                unknown "That's great, nice to see Bunny Bites has hired some rather cute male help, so I'd like to take on The Big Bunny Challenge."
                "You are quite surprised by this, you've heard about it and seen it tried before as it's supposed to be a very difficult eating challenge that most people could not hope to finish."
                "You are quite doubtful this small woman could come close."
                pc "The Big Bunny Challenge? Are you sure?"
                pc "That's our most expensive item on the menu. I should warn you it's quite a difficult challenge and you only get to eat for free if you finish the whole thing."
                "Bunny Bites had created The Big Bunny Challenge as a way to bring in challengers and business."
                "They had also purposefully made it so it was nearly impossible to actually accomplish so people would have to pay extra money when they inevitably failed."
                image luna_stage1_1 = "/luna/events/stage1/1.webp"
                scene luna_stage1_1
                "The woman however just smiles and nods."
                unknown "I'm well aware of the challenge, just bring me the food, thanks."
                pc "Well okay, if that's what you want, I'll bring you your food when it's ready."
                unknown "Thanks."
                image luna_stage1_2 = "/luna/events/stage1/2.webp"
                scene luna_stage1_2
                "After her food is ready, you bring it to her."
                pc "You have 20 minutes to complete it, bathroom breaks or leaving the table for any reason is not allowed."
                unknown "Bring it on!"
                image luna_stage1_3 = "/luna/events/stage1/3.webp"
                scene luna_stage1_3
                "You start your watch and she immediately starts eating with a fury and desire you've never seen before."
                "You watch in amazement as large bite after large bite disappears down her throat."
                image luna_stage1_4 = "/luna/events/stage1/4.webp"
                scene luna_stage1_4
                "Even at halfway done when other challengers would tap out or give up, this woman is still going at it without showing any sign of slowing down."
                "Just who is this woman?"
                image luna_stage1_5 = "/luna/events/stage1/5.webp"
                scene luna_stage1_5
                "She manages to finish all of the food with nearly a couple minutes to spare and she sits back with a contented look on her face, her hand on a very stuffed full belly."
                unknown "So how did I do this time?"
                pc "18 minutes, 4 seconds."
                image luna_stage1_6 = "/luna/events/stage1/6.webp"
                scene luna_stage1_6
                unknown "A new record for me, nice."
                pc "You've tried this before?"
                unknown "Oh yes, plenty of times and I'll keep trying it until they stop letting me take it."
                pc "Is that why you were happy to see me, since I'm new and didn't know any better?"
                image luna_stage1_7 = "/luna/events/stage1/7.webp"
                scene luna_stage1_7
                unknown "Mmm, partly but I did mean it when I said I like a new, cute face."
                "Since she is flirting with you a little, you feel like you can flirt back."
                pc "Thanks and I'm glad to have such an attractive customer come in, especially one that can eat like that, like I'm still just shocked you managed to do that."
                unknown "Thanks, I'm certainly glad that you like girls that can and want to eat a lot."
                pc "Definitely."
                unknown "Well, hopefully I'll see you again then. And I'm assuming that my meal for today is free?"
                pc "For sure, it's all on the house, I hope to see you again."
                unknown "Until I run you out of business with getting free food all the time."
                pc "I'm not worried about that. Although, I'm not sure how long Bunny Bites will have that challenge with you around."
                unknown "Well, I'll continue to take advantage of it until they find out. Nice to meet you."
                pc "Nice to meet you too."
                $ unknownname = 'Unknown'
                $ lunabunnybitesevent = 0
                call bbworking
                return
            else:
                image cafe_luna_arrive = "/luna/[luna.stage]/cafe_arrive.webp"
                scene cafe_luna_arrive
                "The same woman that completed the Big Bunny Challenge and amazed you with her eating skills comes back in."
                $ unknownname = 'Attractive Woman'
                image cafe_luna_talk = "/luna/[luna.stage]/cafe_talk.webp"
                scene cafe_luna_talk
                unknown "I'll take on The Big Bunny Challenge again."
                "Having seen her simply unbelievable eating skills the first time, you don't try to warn her this time."
                pc "Sure, coming right up, I'll bring it to you when it's all ready."
                unknown "Thanks."
                image luna_stage1_2 = "/luna/events/stage1/2.webp"
                scene luna_stage1_2
                "After the food is ready, you bring it to her."
                pc "I'm assuming I don't need to tell you the rules again?"
                unknown "Nope, I know it all by now, I'll just say thank you for the free food now."
                pc "You're welcome, enjoy."
                image luna_stage1_3 = "/luna/events/stage1/3.webp"
                scene luna_stage1_3
                "She starts eating just as quickly and strongly as the first time, finishing the food with around 2 minutes to spare."
                image luna_stage1_5 = "/luna/events/stage1/5.webp"
                scene luna_stage1_5
                "She happily sits back in her seat with a full belly once again."
                pc "I don't think I'll ever get over how you can eat like that."
                image luna_stage1_6 = "/luna/events/stage1/6.webp"
                scene luna_stage1_6
                unknown "Well, I can definitely tell you enjoy watching me eat. It turns you on, doesn't it?"
                pc "Uh, is it wrong of me to admit that I do?"
                unknown "Not at all, nor do I have a problem with admitting I like you bringing me all that food and then you watching me eat."
                image luna_stage1_7 = "/luna/events/stage1/7.webp"
                scene luna_stage1_7
                unknown "Anyway, thanks again for the free food, see you next time."
                pc "See you next time, looking forward to it."
                $ unknownname = 'Unknown'
                call bbworking
                return

        image cafe_luna_arrive = "/luna/[luna.stage]/cafe_arrive.webp"
        scene cafe_luna_arrive
        "A customer arrives at the diner."
        pc "Hey, it's Luna!"
        image cafe_luna_talk = "/luna/[luna.stage]/cafe_talk.webp"
        scene cafe_luna_talk
        if luna.stage >= 9:
            "Or rather Luna's huge breasts arrive and then the rest of Luna does."
            pc "Hi Luna!"
            luna "I think I need a proper greeting if you expect a big tip."
            pc "Oh, how about this then?"
            "You move in and give her a nice, long kiss while also grabbing and squeezing her huge boobs."
            luna "That's better, such service!"
            pc "I just want to satisfy my customers! So what will you be having, your usual?"
            luna "If I want to leave not completely full, I can definitely eat more than that now, so feel free to add some more to my order."
            pc "Coming right up."
        else:
            pc "Did you come to see me or did you come for the food?"
            luna "Both, of course."
            "Luna gives you a quick kiss."
            if lunabunnybitesevent == 0:
                luna "It really is a shame they don't do The Big Bunny Challenge anymore, I guess me coming here so often made them remove it."
                $ lunabunnybitesevent = 1
            pc "Do you want your usual?"
            luna "Yes, please! You know what I like."
            pc "Me."
            luna "Yes, you too, but I meant the food."
            pc "Coming right up."
        if luna.stage >= 11:
            image cafe_luna_ass = "/luna/[luna.stage]/cafe_ass.webp"
            scene cafe_luna_ass
        menu:
            "Create her food normally.":
                "You create her food."
                image cafe_luna_booth = "/luna/[luna.stage]/cafe_booth.webp"
                scene cafe_luna_booth
                if luna.stage >= 9:
                    luna "Thank you for the food!"
                    "She eats it all and then goes and gives you a kiss as she leaves."
                else:
                    pc "Here you go. Have a nice meal."
                    luna "Thank you!"
                $ luna.weight += 0.2
            "Use the secret fattening formula." if secretfeedervol1 == 1:
                call BBfoodformula
                image cafe_luna_booth = "/luna/[luna.stage]/cafe_booth.webp"
                scene cafe_luna_booth
                if luna.stage >= 9:
                    luna "Thank you for the food!"
                    "She eats it all and then goes and gives you a kiss as she leaves."
                else:
                    pc "Here you go. Have a nice meal."
                    luna "Thank you!"
                if secretfeedervol2 == 1:
                    $ luna.weight += 0.5
                elif secretfeedervol1 == 1:
                    $ luna.weight += 0.3
                else:
                    $ luna.weight += 0.2
            "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                "You make her her usual order plus a lot extra."
                if secretfeedervol1 == 1:
                    call BBfoodformula
                "You decide to pay the difference yourself."
                $ money -= 5
                image cafe_luna_extrafood = "/luna/[luna.stage]/cafe_extrafood.webp"
                scene cafe_luna_extrafood
                if luna.stage >= 9:
                    luna "Look at you bringing me extra food! How sweet of you!"
                    pc "I don't know what you're talking about, there must have been a mixup or a mistake somewhere, don't worry I won't charge you extra."
                    "Both of you know better however."
                    luna "Well lucky me then for the mistake, this does give me an extra food eating challenge to finish all of this though and you know I love a good challenge."
                    if luna.stage >= 11:
                        image cafe_luna_eat = "/luna/[luna.stage]/cafe_eat.webp"
                        scene cafe_luna_eat
                        "You watch as she quickly eats the huge meal without much struggle."
                        image cafe_luna_struggle = "/luna/[luna.stage]/cafe_struggle.webp"
                        scene cafe_luna_struggle
                        "Her belly impressively swells up into a tight orb as she finishes her meal."
                    else:
                        image cafe_luna_struggle = "/luna/[luna.stage]/cafe_struggle.webp"
                        scene cafe_luna_struggle
                        "She really seems to struggle, but she still manages to finish all of it."
                    #"You get an extra long kiss as a reward as she leaves."
                else:
                    luna "This is a lot more than just my usual."
                    pc "I must have made a mistake. You can have what's extra for no extra charge - it's on me."
                    "Luna gives you a wink."
                    luna "Right, I'm sure it was just a mistake. Anyway, thanks for treating me. Besides, I'm super hungry."
                    pc "You're always super hungry."
                    image cafe_luna_struggle = "/luna/[luna.stage]/cafe_struggle.webp"
                    scene cafe_luna_struggle
                    "Luna is only too happy to eat all of the extra food that you give her  as she chows down."
                if secretfeedervol2 == 1:
                    $ luna.weight += 0.8
                elif secretfeedervol1 == 1:
                    $ luna.weight += 0.5
                else:
                    $ luna.weight += 0.3
            "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0 and luna.stage >= 6:
                "You make her at least 3 times as much food as you normally would."
                if secretfeedervol1 == 1:
                    call BBfoodformula
                image cafe_luna_prize1 = "/luna/[luna.stage]/cafe_prize1.webp"
                scene cafe_luna_prize1
                "You walk up to her booth to inform her that she won a prize."
                image cafe_luna_prize2 = "/luna/[luna.stage]/cafe_prize2.webp"
                scene cafe_luna_prize2
                pc "Congratulations, you win the customer of the week prize."
                pc "Which means you get to eat as much food as you wish today."
                image cafe_luna_prize3 = "/luna/[luna.stage]/cafe_prize3.webp"
                scene cafe_luna_prize3
                luna "Oh wow, it must be my lucky day! I'm sure it was totally random and by chance that I somehow won the prize?"
                "She obviously knows that it was not at all random."
                pc "Uh, yeah, let's go with that."
                luna "Sounds good to me! Thank you so much! So I get to eat as much as I want?"
                pc "As much as you want."
                image cafe_luna_prize4 = "/luna/[luna.stage]/cafe_prize4.webp"
                scene cafe_luna_prize4
                luna "Then I guess I better take full advantage of the opportunity! My boobs and the rest of me still need to do plenty of growing."
                pc "For sure."
                luna "Well this isn't going to be enough, have them start making me more."
                pc "Will do!"
                image cafe_luna_prize5 = "/luna/[luna.stage]/cafe_prize5.webp"
                scene cafe_luna_prize5
                "Luna is already going at what you already brought her, happily eating the food quickly but also enjoying every bite."
                image cafe_luna_prize6 = "/luna/[luna.stage]/cafe_prize6.webp"
                scene cafe_luna_prize6
                "Even when more food arrives she keeps eating even though you know she is getting full."
                image cafe_luna_prize7 = "/luna/[luna.stage]/cafe_prize7.webp"
                scene cafe_luna_prize7
                "With every bite, her belly becomes bigger and bigger."
                image cafe_luna_prize8 = "/luna/[luna.stage]/cafe_prize8.webp"
                scene cafe_luna_prize8
                window hide
                pause
                image cafe_luna_prize9 = "/luna/[luna.stage]/cafe_prize9.webp"
                scene cafe_luna_prize9
                "Finally she stops after eating the last bite and sits back, a satisfied look on her face, as she gives both her tummy and then each of her boobs a nice pat."
                image cafe_luna_prize10 = "/luna/[luna.stage]/cafe_prize10.webp"
                scene cafe_luna_prize10
                luna "Mmm, that was delicious thank you."
                pc "You're welcome, our lucky winner!"
                image cafe_luna_prize11 = "/luna/[luna.stage]/cafe_prize11.webp"
                scene cafe_luna_prize11
                "As Luna stands up to leave, she waves you goodbye."
                $ weeklyprize -= 1
                if secretfeedervol2 == 1:
                    $ luna.weight += 1.0
                elif secretfeedervol1 == 1:
                    $ luna.weight += 0.8
                else:
                    $ luna.weight += 0.6


        call bbworking
        return

    elif rngworkcustomer <= 80:
        if daisy_work_today == 1:
            jump work_randomizer
        $ daisy_work_today = 1
        image cafe_daisy_arrive = "/teacher/[teacher.stage]/0/cafe_arrive.webp"
        scene cafe_daisy_arrive
        "A customer arrives at the diner."
        image cafe_daisy_talk = "/teacher/[teacher.stage]/0/cafe_talk.webp"
        scene cafe_daisy_talk
        teacher "Well, if it isn’t my favorite student."
        pc "Hello, Ms. Tanwen. I mean, Daisy."
        teacher "You probably know why I’m here."
        pc "To stuff your face with food?"
        teacher "Correct. You get an A+."
        pc "What can I get you then?"
        teacher "I would like to order a hamburger and one slice of pizza."
        pc "Coming right up, please feel free to sit anywhere you would like."
        menu:
            "Create her food normally.":
                "You create her food."
                image cafe_teacher_booth = "/teacher/[teacher.stage]/0/cafe_booth.webp"
                scene cafe_teacher_booth
                pc "Here you go. Have a nice meal."
                teacher "Thank you!"
                $ teacher.weight += 0.2
            "Use the secret fattening formula." if secretfeedervol1 == 1:
                "You create her food with the secret fattening formula."
                image cafe_teacher_booth = "/teacher/[teacher.stage]/0/cafe_booth.webp"
                scene cafe_teacher_booth
                pc "Here you go. Have a nice meal."
                teacher "Thank you!"
                if secretfeedervol2 == 1:
                    $ teacher.weight += 0.5
                elif secretfeedervol1 == 1:
                    $ teacher.weight += 0.3
                else:
                    $ teacher.weight += 0.2
            "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                "You end up making a lot more food than she asked for."
                if secretfeedervol1 == 1:
                    "You create her food with the secret fattening formula."
                "You decide to pay the difference yourself."
                $ money -= 5
                image cafe_teacher_extrafood = "/teacher/[teacher.stage]/0/cafe_extrafood.webp"
                scene cafe_teacher_extrafood
                teacher "Making it a little obvious, aren’t you?"
                pc "Sorry. I’m covering the extra cost if that helps."
                teacher "Nothing to be sorry for. Although, I do appreciate the free meal. Thank you very much."
                image cafe_teacher_eating = "/teacher/[teacher.stage]/0/cafe_eating.webp"
                scene cafe_teacher_eating
                "Without a hint of trouble, Daisy manages to eat everything in front of her in record time."
                image cafe_teacher_happy_stuffed = "/teacher/[teacher.stage]/0/cafe_happy_stuffed.webp"
                scene cafe_teacher_happy_stuffed
                teacher "Excellent as always. Keep up the good work."
                if secretfeedervol2 == 1:
                    $ teacher.weight += 0.8
                elif secretfeedervol1 == 1:
                    $ teacher.weight += 0.5
                else:
                    $ teacher.weight += 0.3
            "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0 and disable == 1:
                "After creating a sizable feast, you approach Daisy’s seat."
                if secretfeedervol1 == 1:
                    "You create her food with the secret fattening formula."
                #Picture NEEDED
                pc "Congratulations! You’re the winner of this week’s prize. That means you get to eat as much as you want today."
                teacher "While I’m sure this isn’t a mere coincidence. I am more than willing to overlook it for this."
                teacher "Well, as long as you stay behind for my victory dinner."
                #Image: The player sitting across from Daisy as she eats the food.
                "The moment you sit across from her, Daisy begins to eat. Though many have been intimidated by the prize feast, she shows no hesitation as she goes at it like a wild animal."
                #Image: Daisy continuing to eat at a rapid pace.
                "You only turn away from the impressive sight to add more food to her table. The feeding frenzy becomes so great that several other servers pitch in to keep pace with her."
                #Image: Daisy slowing down on her feast.
                "Left more than a little exhausted, you’re somewhat relieved to see Daisy begin to slow down."
                "Even as she’s reaching her breaking point, she revels in each bite of food; knowing how much it will push her towards her ultimate goal."
                #Image: Daisy slouched in the booth and rubbing her exposed belly.
                "As the final plate is cleared, Daisy leans back in her seat to nurse her overstuffed gut."
                teacher "So much excellent food. My only regret is that I couldn’t eat anymore. Don’t suppose I can take a few boxes home?"
                pc "I’d be more than happy to oblige."
                "After you help her with a sizable number of take out boxes, Daisy says goodbye and heads out."
        call bbworking
        return

    elif rngworkcustomer <= 90:
        if maya_work_today == 1:
            jump work_randomizer
        $ maya_work_today = 1
        if mayastage1event2 == 1:
            jump work_randomizer
        if mayastage4event4 == 0 and mayastage5event2 == 1:
            jump work_randomizer
        image cafe_maya_arrive = "/maya/[maya.stage]/cafe_arrive.webp"
        scene cafe_maya_arrive
        "A customer arrives at the diner."
        pc "Hey Maya."
        image cafe_maya_talk = "/maya/[maya.stage]/cafe_talk.webp"
        scene cafe_maya_talk
        maya "Hey [playername]."
        if maya.stage <= 2:
            pc "What brings you in?"
            image cafe_maya_talk2 = "/maya/[maya.stage]/cafe_talk2.webp"
            scene cafe_maya_talk2
            maya "Thought I'd stop in to get something quick before heading to work."
            pc "What can I get you?"
            maya "I'll just have a burger with fries."
            pc "Coming right up. Why don't you find a seat and I'll bring that out to you when it's done."
        elif maya.stage >= 3 and mayastage4event2 == 1:
            pc "What brings you in?"
            image cafe_maya_talk2 = "/maya/[maya.stage]/cafe_talk2.webp"
            scene cafe_maya_talk2
            maya "I need something to eat and I don't care what Mr. Vanthorne says."
            maya "Now that I've started coming back here regularly, I can't help myself. The food here is so good."
            pc "I don't blame you, the food here is pretty good. So, What can I get you?"
            maya "I'll just have a burger with fries."
            pc "Coming right up. Why don't you find a seat and I'll bring that out to you when it's done."
        elif maya.stage == 4 and mayastage4event2 == 0:
            pc "Taking a break from the strike?"
            image cafe_maya_talk2 = "/maya/[maya.stage]/cafe_talk2.webp"
            scene cafe_maya_talk2
            maya "No, I'm just stopping by to grab the food for everyone, but as long as I'm here I could go for a burger and some fries before heading back."
            pc "Coming right up. I'll let them know you're here for that order for the strikers while I'm back there."
            pc "Why don't you find a seat and I'll bring your order out when it's done."
        elif maya.stage == 5 and mayastage5event2 == 0 and mayastage5event5 == 1:
            pc "How are the fundraisers going?"
            image cafe_maya_talk2 = "/maya/[maya.stage]/cafe_talk2.webp"
            scene cafe_maya_talk2
            maya "They're going really well. The calendars are selling like crazy."
            pc "I'm glad to hear. You think you'll hit your goal?"
            maya "We still have a long way to go, but I think we might be able to do it."
            pc "That's great. So what can I get you?"
            maya "I'll have my usual burger with fries."
            pc "Coming right up, why don't you find a spot to sit."
        elif maya.stage >= 5 and mayastage5event5 == 0 and mayastage6event == 1:
            pc "How are you doing?"
            image cafe_maya_talk2 = "/maya/[maya.stage]/cafe_talk2.webp"
            scene cafe_maya_talk2
            maya "Doing great! Been working hard getting the club ready for the grand reopening."
            pc "I'm really excited for it. You'll let me know when that is, right?"
            maya "Oh, of course. You'll be the first one I call."
            pc "Can't wait. So, what can I get you?"
            maya "I'll have my usual burger with fries."
            pc "Coming right up, why don't you find a spot to sit."
        elif maya.stage >= 6 and mayastage6event == 0:
            pc "How's Curvy Corner doing?"
            image cafe_maya_talk2 = "/maya/[maya.stage]/cafe_talk2.webp"
            scene cafe_maya_talk2
            maya "Business is booming."
            pc "That's great to hear."
            maya "Just heading there now, but thought I'd stop in for a quick bite."
            pc "So, what can I get you?"
            maya "I'll have my usual burger with fries."
            pc "Coming right up, why don't you find a spot to sit."
        image cafe_maya_ass = "/maya/[maya.stage]/cafe_ass.webp"
        scene cafe_maya_ass
        "Maya finds an open booth and takes a seat."
        menu:
            "Create her food normally.":
                "You create her food."
                call Maya_BB_Normal
                if mayastage6event == 0:
                    $ maya.weight += 0.2
            "Use the secret fattening formula." if secretfeedervol1 == 1:
                "You create her food with the secret fattening formula."
                call Maya_BB_Normal
                if mayastage6event == 0:
                    if secretfeedervol2 == 1:
                        $ maya.weight += 0.5
                    elif secretfeedervol1 == 1:
                        $ maya.weight += 0.3
                    else:
                        $ maya.weight += 0.2
            "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                "You make her a lot more food than she asked for."
                if secretfeedervol1 == 1:
                    "You create her food with the secret fattening formula."
                "You decide to pay the difference yourself."
                $ money -= 5
                image cafe_maya_extrafood = "/maya/[maya.stage]/cafe_extrafood.webp"
                scene cafe_maya_extrafood
                pc "Here you go."
                if maya.stage == 1:
                    maya "Oh!"
                    pc "Is something wrong?"
                    maya "I don't think this is my order. I didn't order this much food."
                    pc "I'm sorry they must have mixed up your ticket. We can throw this out and redo your order."
                    image cafe_maya_extrafood2 = "/maya/[maya.stage]/cafe_extrafood2.webp"
                    scene cafe_maya_extrafood2
                    maya "Well if you're just going to throw it out. I guess there's something I'd like to try out. Will I need to pay for the extra food here."
                    pc "Of course not, this was completely our fault."
                    maya "Then I think I'll stick with this. It looks so good."
                elif maya.stage == 2:
                    maya "Oh!"
                    pc "Is something wrong?"
                    maya "I think my order got messed up again."
                    pc "I'm sorry they must have mixed up your ticket. We can throw this out and redo your order."
                    image cafe_maya_extrafood2 = "/maya/[maya.stage]/cafe_extrafood2.webp"
                    scene cafe_maya_extrafood2
                    maya "No this is fine, I'm still trying to figure something out. Whoever ordered this has good taste."
                elif maya.stage >= 3 and mayastage4event2 == 1:
                    maya "Oh! The order is wrong again."
                    pc "I'm sorry. I can go back to the kitchen and see if I can find your order."
                    image cafe_maya_extrafood2 = "/maya/[maya.stage]/cafe_extrafood2.webp"
                    scene cafe_maya_extrafood2
                    maya "That's ok. This looks better than what I ordered anyways."
                    pc "Are you sure, it's a lot of food?"
                    maya "I'm sure."
                elif maya.stage == 4 and mayastage4event2 == 0:
                    maya "Oh! The order is wrong again."
                    pc "I'm sorry. It seems that this keeps happening."
                    image cafe_maya_extrafood3 = "/maya/[maya.stage]/cafe_extrafood3.webp"
                    scene cafe_maya_extrafood3
                    maya "I'm sure you don't have anything to do with that, do you?"
                    pc "Me? Of course not, would you like me to go find your order."
                    image cafe_maya_extrafood2 = "/maya/[maya.stage]/cafe_extrafood2.webp"
                    scene cafe_maya_extrafood2
                    maya "No, with the strike going I'll take whatever I can get. So this is fine."
                elif maya.stage == 5 and mayastage5event2 == 0 and mayastage5event4 == 1:
                    maya "Oh! The order is wrong again."
                    pc "I'm sorry. Would you like for me to go back and make you a new one?"
                    image cafe_maya_extrafood2 = "/maya/[maya.stage]/cafe_extrafood2.webp"
                    scene cafe_maya_extrafood2
                    maya "No, this will be ok. I feel I should treat myself for all the hard work we have been putting in on fundraising."
                elif maya.stage >= 5 and mayastage5event4 == 0 and mayastage6event == 1:
                    maya "Oh! The order is wrong again."
                    pc "I'm sorry. Would you like for me to go back and make you a new one?"
                    image cafe_maya_extrafood2 = "/maya/[maya.stage]/cafe_extrafood2.webp"
                    scene cafe_maya_extrafood2
                    maya "No, this will be ok, but you should really try to figure out why this keeps happening."
                elif maya.stage >= 6 and mayastage6event == 0:
                    maya "Oh! The order is wrong again."
                    pc "I'm sorry. Would you like for me to go back and make you a new one?"
                    image cafe_maya_extrafood2 = "/maya/[maya.stage]/cafe_extrafood2.webp"
                    scene cafe_maya_extrafood2
                    maya "No, this will be ok, I'm getting the feeling that someone might be behind this, but I'm not complaining."

                pc "Sounds good enjoy."
                "You leave Maya to enjoy her food."
                image cafe_maya_struggle = "/maya/[maya.stage]/cafe_struggle.webp"
                scene cafe_maya_struggle
                "A short time later you notice Maya sitting there with her last burger holding her stomach deep in thought."

                if maya.stage == 1:
                    pc "Was everything alright."
                    image cafe_maya_struggle2 = "/maya/[maya.stage]/cafe_struggle2.webp"
                    scene cafe_maya_struggle2
                    maya "Oh yes! Delicious as always. Can I ask you a question?"
                    pc "Sure."
                    maya "I don't want to get in trouble with Mr. Vanthorne. Are you able to tell I've had a big meal?"
                    pc "Umm…"
                    maya "Nevermind you don't have to answer. This isn't the first time I've done this. I have my ways of hiding things from Mr. Vanthorne."
                    maya "Let me finish this last burger quick."
                    image cafe_maya_eat = "/maya/[maya.stage]/cafe_eat.webp"
                    scene cafe_maya_eat
                    "Maya quickly finishes her burger, unfazed by the amount of food she just ate, she gets up and runs her finger across your face as she walks by."
                    image cafe_maya_bye = "/maya/[maya.stage]/cafe_bye.webp"
                    scene cafe_maya_bye
                    maya "Don't forget to stop by the club sometime."
                    "Shocked by how Maya was able to quickly eat such a big meal and act like it was nothing, you go back to work."
                elif maya.stage == 2:
                    pc "Was everything alright."
                    image cafe_maya_struggle2 = "/maya/[maya.stage]/cafe_struggle2.webp"
                    scene cafe_maya_struggle2
                    maya "Oh yes! Delicious as always. Can I ask you a question?"
                    pc "Sure."
                    maya "This meal hasn't ruined my figure, has it?"
                    image cafe_maya_struggle3 = "/maya/[maya.stage]/cafe_struggle3.webp"
                    scene cafe_maya_struggle3
                    "Maya rubs her belly playfully."
                    pc "Umm…"
                    maya "I'm just giving you a hard time."
                    maya "Let me finish this last burger quick."
                    image cafe_maya_eat = "/maya/[maya.stage]/cafe_eat.webp"
                    scene cafe_maya_eat
                    "Maya quickly finishes her burger, unfazed by the amount of food she just ate, she gets up and runs her finger across your face as she walks by."
                    image cafe_maya_bye = "/maya/[maya.stage]/cafe_bye.webp"
                    scene cafe_maya_bye
                    maya "Don’t forget to stop by the club sometime."
                    "Shocked by how Maya was able to quickly eat such a big meal and act like it was nothing, you go back to work."
                elif maya.stage >= 3 and mayastage4event2 == 1:
                    pc "How was everything?"
                    image cafe_maya_struggle2 = "/maya/[maya.stage]/cafe_struggle2.webp"
                    scene cafe_maya_struggle2
                    maya "Delicious as always."
                    pc "It wasn't too much?"
                    maya "Too much? Oh, the food, no it's fine. It sure does look like it was."
                    image cafe_maya_struggle3 = "/maya/[maya.stage]/cafe_struggle3.webp"
                    scene cafe_maya_struggle3
                    "Maya rubs her belly playfully and smiles at you."
                    maya "Let me just finish this last burger quick."
                    image cafe_maya_eat = "/maya/[maya.stage]/cafe_eat.webp"
                    scene cafe_maya_eat
                    "Maya quickly finishes her burger, unfazed by the amount of food she just ate, she gets up and runs her finger across your face as she walks by."
                    image cafe_maya_bye = "/maya/[maya.stage]/cafe_bye.webp"
                    scene cafe_maya_bye
                    maya "Don't forget to stop by the club sometime."
                    "Shocked by how Maya was able to quickly eat such a big meal and act like it was nothing, you go back to work."
                elif maya.stage == 4 and mayastage4event2 == 0:
                    pc "How was everything?"
                    image cafe_maya_struggle2 = "/maya/[maya.stage]/cafe_struggle2.webp"
                    scene cafe_maya_struggle2
                    maya "It was so good."
                    pc "Glad to hear. Would you like me to get you a container for the last burger there?"
                    image cafe_maya_struggle3 = "/maya/[maya.stage]/cafe_struggle3.webp"
                    scene cafe_maya_struggle3
                    maya "No that's ok I'll finish this last burger quick."
                    image cafe_maya_eat = "/maya/[maya.stage]/cafe_eat.webp"
                    scene cafe_maya_eat
                    "Maya quickly finishes her burger, unfazed by the amount of food she just ate."
                    image cafe_maya_bye = "/maya/[maya.stage]/cafe_bye.webp"
                    scene cafe_maya_bye
                    maya "So, is my other order ready?"
                    pc "I think so, let me go back and grab it for you."
                    "You go to get Maya's order."
                    "Maya leaves with bags full of food."
                    "You are left amazed by how Maya was able to quickly eat such a big meal and act like it was nothing, you go back to work."
                elif maya.stage == 5 and mayastage5event2 == 0 and mayastage5event4 == 1:
                    pc "How was everything?"
                    image cafe_maya_struggle2 = "/maya/[maya.stage]/cafe_struggle2.webp"
                    scene cafe_maya_struggle2
                    maya "It was so good."
                    pc "Glad to hear. Would you like me to get you a container for the last burger there?"
                    image cafe_maya_struggle3 = "/maya/[maya.stage]/cafe_struggle3.webp"
                    scene cafe_maya_struggle3
                    maya "No that's ok I'll finish this last burger quick."
                    image cafe_maya_eat = "/maya/[maya.stage]/cafe_eat.webp"
                    scene cafe_maya_eat
                    "Maya quickly finishes her burger, unfazed by the amount of food she just ate."
                    image cafe_maya_bye = "/maya/[maya.stage]/cafe_bye.webp"
                    scene cafe_maya_bye
                    "Maya gets up."
                    maya "I better get going those calendars won't sell themselves."
                    "You are still amazed on how effortlessly Maya devoured her meal, like it was nothing. You go back to work."
                elif maya.stage >= 5 and mayastage5event4 == 0 and mayastage6event == 1:
                    pc "How was everything?"
                    image cafe_maya_struggle2 = "/maya/[maya.stage]/cafe_struggle2.webp"
                    scene cafe_maya_struggle2
                    maya "It was so good."
                    pc "Glad to hear. Would you like me to get you a container for the last burger there?"
                    image cafe_maya_struggle3 = "/maya/[maya.stage]/cafe_struggle3.webp"
                    scene cafe_maya_struggle3
                    maya "No that's ok I'll finish this last burger quick."
                    image cafe_maya_eat = "/maya/[maya.stage]/cafe_eat.webp"
                    scene cafe_maya_eat
                    "Maya quickly finishes her burger, unfazed by the amount of food she just ate."
                    image cafe_maya_bye = "/maya/[maya.stage]/cafe_bye.webp"
                    scene cafe_maya_bye
                    "Maya gets up."
                    maya "Thanks for the meal. I'll message you once we get things up and running."
                    "You are still amazed on how effortlessly Maya devoured her meal, like it was nothing. You go back to work."
                elif maya.stage >= 6 and mayastage6event == 0:
                    pc "How was everything?"
                    image cafe_maya_struggle2 = "/maya/[maya.stage]/cafe_struggle2.webp"
                    scene cafe_maya_struggle2
                    maya "It was so good."
                    pc "Glad to hear. Would you like me to get you a container for the last burger there?"
                    image cafe_maya_struggle3 = "/maya/[maya.stage]/cafe_struggle3.webp"
                    scene cafe_maya_struggle3
                    maya "No that's ok I'll finish this last burger quick."
                    image cafe_maya_eat = "/maya/[maya.stage]/cafe_eat.webp"
                    scene cafe_maya_eat
                    "Maya quickly finishes her burger, unfazed by the amount of food she just ate."
                    image cafe_maya_bye = "/maya/[maya.stage]/cafe_bye.webp"
                    scene cafe_maya_bye
                    "Maya gets up."
                    maya "Thanks for the meal. I better get back to work."
                    "You are still amazed on how effortlessly Maya devoured her meal, like it was nothing. You go back to work."

                if mayastage6event == 0:
                    if secretfeedervol2 == 1:
                        $ maya.weight += 0.8
                    elif secretfeedervol1 == 1:
                        $ maya.weight += 0.5
                    else:
                        $ maya.weight += 0.3
            "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0 and maya.stage >= 6 and mayastage6event == 0 and disable == 1:
                if secretfeedervol1 == 1:
                    "You create her food with the secret fattening formula."
                else:
                    "You create her food."
                "You set a lavish feast on the table."
                maya "What's all this?"
                "Maya looks puzzled."
                pc "Surprise! You're the lucky winner of our weekly prize."
                maya "Prize? I didn't even enter a contest."
                pc "Every customer gets entered into a random drawing, and today you hit the jackpot!"
                maya "Seriously? What did I win?"
                pc "An all-you-can-eat meal, on the house."
                maya "Oh, wow! I never win anything. And all this food is included?"
                pc "Absolutely, just give us a shout if you need more."
                "You leave Maya to enjoy her feast."
                "Initially unsure, Maya succumbs to the wonderful smells coming off from the spread."
                "She dives in, relishing each bite and calling for more."
                "You and the servers quickly replenish Maya's table as she continues to eat."
                "Plate after plate they try to keep up with her, but despite their efforts, the kitchen couldn't keep up, and Maya eventually polishes off everything on the table."
                "She leans back, letting out a loud burp."
                maya "UUUURRP!"
                "Maya leans back, eyes closed, rubbing her swollen belly."
                pc "Would you like us to bring you another round?"
                "Like coming out of a trance, Maya opens her eyes and sees what she has done. She looks embarrassed."
                maya "Ummm, no thanks. I think I've had my fill for now."
                pc "Are you sure? You seemed to be enjoying yourself."
                maya "I did, but I think I've reached my limit. Can you help me up?"
                "You help Maya out of her seat."
                maya "Whew, it's been ages since… oh, never mind."
                "Maya massages her belly, feeling content."
                maya "That was an amazing treat."
                "Grateful, Maya pecks you on the cheek before departing."
                "As you watch her go, you wonder if Maya was truly satisfied or simply putting on a show. With that thought, you return to work."
                if mayastage6event == 0:
                    if secretfeedervol2 == 1:
                        $ maya.weight += 1.5
                    elif secretfeedervol1 == 1:
                        $ maya.weight += 1.2
                    else:
                        $ maya.weight += 1

        call bbworking
        return

    elif rngworkcustomer <= 100:
        if leanne_work_today == 1:
            jump work_randomizer
        $ leanne_work_today = 1
        if leanne.stage <= 5 or (leannestage11event == 0 and leanne.stage == 11):
            jump work_randomizer
        if leanne.stage <= 9:
            image cafe_leanne_arrive = "/leanne/[leanne.stage]/cafe_arrive.webp"
            scene cafe_leanne_arrive
            "A customer arrives."
            image cafe_leanne_talk = "/leanne/[leanne.stage]/cafe_talk.webp"
            scene cafe_leanne_talk
            pc "Hey there Leanne, er, I mean Lyn."
            leanne "Shh, keep your voice down. I'd rather not have my meal interrupted by a fan."
            pc "Sorry. What can I get you, stranger?"
            leanne "Let's see. I think I'll have the cheese burger menu."
            pc "Coming right up. Take a seat and I'll bring it to you."
            leanne "Thanks."
            #(NOTE: From here Lyn/Leanne would order from the menu. Leaving this spot blank for whatever meals you want to include. Choice B and C would open up as the player progresses through the story)
            menu:
                "Make a regular meal.":
                    image cafe_leanne_booth = "/leanne/[leanne.stage]/cafe_booth.webp"
                    scene cafe_leanne_booth
                    "Though you want to stick around to chat while she eats, Lyn's need for secrecy keeps your interactions to a minimum."
                    "You have to settle for watching her enjoy her meal from a distance."
                    image cafe_leanne_bye = "/leanne/[leanne.stage]/cafe_bye.webp"
                    scene cafe_leanne_bye
                    "Even still, she's willing to risk being exposed for the sake of waving you goodbye as she leaves."
                    $ leanne.weight += 0.1
                    call bbworking
                    return
                "Use the secret fattening formula." if secretfeedervol1 == 1:
                    "You create her food with the secret fattening formula."
                    image cafe_leanne_booth = "/leanne/[leanne.stage]/cafe_booth.webp"
                    scene cafe_leanne_booth
                    "Though you want to stick around to chat while she eats, Lyn's need for secrecy keeps your interactions to a minimum."
                    "You have to settle for watching her enjoy her meal from a distance."
                    image cafe_leanne_bye = "/leanne/[leanne.stage]/cafe_bye.webp"
                    scene cafe_leanne_bye
                    "Even still, she's willing to risk being exposed for the sake of waving you goodbye as she leaves."
                    if secretfeedervol2 == 1:
                        $ leanne.weight += 0.3
                    elif secretfeedervol1 == 1:
                        $ leanne.weight += 0.2
                    else:
                        $ leanne.weight += 0.1
                    call bbworking
                    return
                "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                    "You end up making a lot more food than she asked for and pay for the difference with your own money."
                    $ money -= 5
                    image cafe_leanne_extrafood = "/leanne/[leanne.stage]/cafe_extrafood.webp"
                    scene cafe_leanne_extrafood
                    leanne "Not that I don't appreciate it, but could you be a little more subtle about your in-person donation?"
                    pc "Sorry about that. Would you like me to take it away?"
                    leanne "No point in wasting food now. Have a seat and try not to draw too much attention."
                    image cafe_leanne_eating = "/leanne/[leanne.stage]/cafe_eating.webp"
                    scene cafe_leanne_eating
                    "Lyn's need for secrecy keeps her pace slow, but she still manages to work her way through the small feast."
                    image cafe_leanne_stuffed = "/leanne/[leanne.stage]/cafe_stuffed.webp"
                    scene cafe_leanne_stuffed
                    leanne "That really hit the spot. Thank you for the support, loyal viewer."
                    "After waiting for her stomach to settle down, she eventually leaves."
                    if secretfeedervol2 == 1:
                        $ leanne.weight += 0.5
                    elif secretfeedervol1 == 1:
                        $ leanne.weight += 0.3
                    else:
                        $ leanne.weight += 0.2
                    call bbworking
                    return
                "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0 and disable == 1:
                    "Creating a sizable feast, you approach Lyn's seat."
                    #IMAGE: Lyn/Leanne awestruck at the massive amount of food.
                    pc "Congratulations! You're the winner of this week's prize. That means you get to eat as much as you want."
                    leanne "Are you crazy? I thought I told you I didn't want to draw attention. Not to mention I'm not sure if I can eat all of this."
                    leanne "Although…it does look pretty good."
                    #IMAGE: The player sitting across from Lyn/Leanne as she eats her food.
                    "As Lyn begins to dig into the food, you hazard to take a seat across from her. Though she's eager at first to eat every last bite, she eventually starts to slow down."
                    #IMAGE: Lyn/Leanne struggling to eat her food.
                    "Each time you get up to bring another platter over, you notice that she moves with added lethargy. Inevitably she's forced to stop."
                    #IMAGE: Lyn/Leanne slouched back in her seat, rubbing her bloated stomach.
                    leanne "Ugh, I can't remember the last time I ate like that. This is going to make my next stream extra challenging. Anyway, thanks for the food. Would you mind packing up the leftovers?"
                    "Helping Lyn with her take out bags, you escort her out of the diner."
                    if secretfeedervol2 == 1:
                        $ leanne.weight += 1.5
                    elif secretfeedervol1 == 1:
                        $ leanne.weight += 1.2
                    else:
                        $ leanne.weight += 1
                    $ weeklyprize -= 1
                    call bbworking
                    return

        if leanne.stage <= 11:
            image cafe_leanne_arrive = "/leanne/[leanne.stage]/cafe_arrive.webp"
            scene cafe_leanne_arrive
            "A customer arrives."
            image cafe_leanne_talk = "/leanne/[leanne.stage]/cafe_talk.webp"
            scene cafe_leanne_talk
            pc "Are you doing alright Lyn?"
            leanne "Yeah, I'm just fine. Would you mind taking my order?"
            pc "Sure, what can I get you?"
            leanne "Let's see. I think I'll have the chunky bunny menu."
            pc "Coming right up. Take a seat and I'll bring it to you."
            leanne "Thanks."
            #(NOTE: From here Lyn/Leanne would order from the menu. Leaving this spot blank for whatever meals you want to include. Choice B and C would open up as the player progresses through the story)
            menu:
                "Make a regular meal.":
                    image cafe_leanne_booth = "/leanne/[leanne.stage]/cafe_booth.webp"
                    scene cafe_leanne_booth
                    "Concerned, you stick around to watch Lyn eat."
                    "Despite your earlier worries, she manages to make her way through the meal just fine."
                    image cafe_leanne_bye = "/leanne/[leanne.stage]/cafe_bye.webp"
                    scene cafe_leanne_bye
                    "Shrugging it off as just misreading the situation, you wave Lyn goodbye as she leaves the diner."
                    $ leanne.weight += 0.1
                    call bbworking
                    return
                "Use the secret fattening formula." if secretfeedervol1 == 1:
                    "You create her food with the secret fattening formula."
                    image cafe_leanne_booth = "/leanne/[leanne.stage]/cafe_booth.webp"
                    scene cafe_leanne_booth
                    "Concerned, you stick around to watch Lyn eat."
                    "Despite your earlier worries, she manages to make her way through the meal just fine."
                    image cafe_leanne_bye = "/leanne/[leanne.stage]/cafe_bye.webp"
                    scene cafe_leanne_bye
                    "Shrugging it off as just misreading the situation, you wave Lyn goodbye as she leaves the diner."
                    if secretfeedervol2 == 1:
                        $ leanne.weight += 0.3
                    elif secretfeedervol1 == 1:
                        $ leanne.weight += 0.2
                    else:
                        $ leanne.weight += 0.1
                    call bbworking
                    return
                "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                    "You end up making a lot more food than she asked for and pay for the difference with your own money."
                    $ money -= 5
                    image cafe_leanne_extrafood = "/leanne/[leanne.stage]/cafe_extrafood.webp"
                    scene cafe_leanne_extrafood
                    leanne "I didn't ask for all of this."
                    pc "You looked a little worried so I was thinking a bit extra would help you out."
                    leanne "That's…generous of you."
                    image cafe_leanne_eating = "/leanne/[leanne.stage]/cafe_eating.webp"
                    scene cafe_leanne_eating
                    "An unnatural nervousness affects Lyn as she eats her way through the meal."
                    "Every so often, you notice her tug at her clothes in-between bites as if trying to double check that they still fit."
                    "Though it's slow, she eventually manages to make her way through the feast."
                    image cafe_leanne_stuffed = "/leanne/[leanne.stage]/cafe_stuffed.webp"
                    scene cafe_leanne_stuffed
                    leanne "Thank you for that. Although, please try to warn me next time. I don't want to be too bloated for my next stream."
                    "After waiting for her stomach to settle down, she eventually leaves."
                    if secretfeedervol2 == 1:
                        $ leanne.weight += 0.5
                    elif secretfeedervol1 == 1:
                        $ leanne.weight += 0.3
                    else:
                        $ leanne.weight += 0.2
                    call bbworking
                    return
                "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0 and disable == 1:
                    "Creating a sizable feast, you approach Lyn's seat."
                    #IMAGE: Lyn/Leanne awestruck at the massive amount of food.
                    pc "Congratulations! You're the winner of this week's prize. That means you get to eat as much as you want."
                    "Lyn remains silent for a moment. Noticing the way you're staring at her; she forces a smile."
                    leanne "Thank you so much. I'll get started right away."
                    #IMAGE: The player sitting across from Lyn/Leanne as she eats her food.
                    "Lyn insists on you joining her as she digs into the food."
                    "Though you acknowledge your coworkers as they come by to drop off more platters, your focus is entirely on Lyn."
                    "For the first time, you notice her hesitate to take bites."
                    #IMAGE: Lyn/Leanne struggling to eat her food.
                    "The look in Lyn's eyes speaks of the anxiety she refuses to say out loud."
                    "Though she tries to hide this face through a display of gluttony, reality strikes hard as she's forced to stop far from her usual limit."
                    #IMAGE: Lyn/Leanne slouched back in her seat, an apologetic look on her face.
                    leanne "Sorry I wasted so much. I guess I wasn't as hungry as I thought."
                    pc "That's alright. You can just eat the rest later."
                    leanne "Yeah…I guess you're right."
                    "Understanding that Lyn isn't in a mood to say what's on her mind, you help her pack up the leftovers and escort her out of the diner."
                    if secretfeedervol2 == 1:
                        $ leanne.weight += 1.5
                    elif secretfeedervol1 == 1:
                        $ leanne.weight += 1.2
                    else:
                        $ leanne.weight += 1
                    $ weeklyprize -= 1
                    call bbworking
                    return

        if leanne.stage >= 12 and leannechoice == 1 and leannestage12event2 == 0:
            image lyn_cafe_arrive = "/leanne/[leanne.stage]/Lyn_cafe_arrive.webp"
            scene lyn_cafe_arrive
            "A customer arrives at the diner."
            pc "Hey, it's Lyn!"
            image lyn_cafe_talk = "/leanne/[leanne.stage]/Lyn_cafe_talk.webp"
            scene lyn_cafe_talk
            leanne "Hello. Good to see you."
            pc "Wait, I thought you preferred sweet stuff."
            leanne "I do, but I can get burned out on it sometimes. Besides, I hear that this place has some pretty good dessert options."
            pc "I'll do my best then. What can I get you?"
            leanne "Let's see. I think I'll have the large chunky bunny menu."
            pc "Coming right up. Take a seat and I'll bring it to you."
            image lyn_cafe_assview = "/leanne/[leanne.stage]/Lyn_cafe_assview.webp"
            scene lyn_cafe_assview
            leanne "Thanks."
            #(NOTE: From here Lyn would order from the menu. Leaving this spot blank for whatever meals you want to include. Choice B and C would open up as the player progresses through the story)
            #CHOICE: A) Make a regular meal B) Accidentally make a larger order or C) Give her the weekly customer special prize
            menu:
                "Create her food normally.":
                    image lyn_cafe_booth = "/leanne/[leanne.stage]/Lyn_cafe_booth.webp"
                    scene lyn_cafe_booth
                    "Bringing the food over to Lyn's table, you chat for a little bit before leaving her to eat."
                    image lyn_cafe_bye = "/leanne/[leanne.stage]/Lyn_cafe_bye.webp"
                    scene lyn_cafe_bye
                    "Finishing up her food and paying the bill, Lyn waves goodbye as she exits the diner."
                    $ leanne.weight += 0.2
                    call bbworking
                    return
                "Use the secret fattening formula." if secretfeedervol1 == 1:
                    "You create her food with the secret fattening formula."
                    image lyn_cafe_booth = "/leanne/[leanne.stage]/Lyn_cafe_booth.webp"
                    scene lyn_cafe_booth
                    "Bringing the food over to Lyn's table, you chat for a little bit before leaving her to eat."
                    image lyn_cafe_bye = "/leanne/[leanne.stage]/Lyn_cafe_bye.webp"
                    scene lyn_cafe_bye
                    "Finishing up her food and paying the bill, Lyn waves goodbye as she exits the diner."
                    if secretfeedervol2 == 1:
                        $ leanne.weight += 0.5
                    elif secretfeedervol1 == 1:
                        $ leanne.weight += 0.3
                    else:
                        $ leanne.weight += 0.2
                    call bbworking
                    return
                "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                    "You end up making a lot more food than she asked for and pay for the difference with your own money."
                    $ money -= 5
                    image lyn_cafe_extrafood = "/leanne/[leanne.stage]/Lyn_cafe_extrafood.webp"
                    scene lyn_cafe_extrafood
                    leanne "I think you made a mistake. There's no way I ordered this much."
                    pc "Sorry. I got a little carried away. Don't worry about the extra, I'll cover the cost."
                    leanne "I really appreciate it."
                    image lyn_cafe_eat = "/leanne/[leanne.stage]/Lyn_cafe_eat.webp"
                    scene lyn_cafe_eat
                    "Appreciative of the food, she proceeds to eat every last bite."
                    image lyn_cafe_struggle = "/leanne/[leanne.stage]/Lyn_cafe_struggle.webp"
                    scene lyn_cafe_struggle
                    leanne "That was delicious. Thank you again."
                    "After wiping her face clean, Lyn heads out."
                    if secretfeedervol2 == 1:
                        $ leanne.weight += 0.8
                    elif secretfeedervol1 == 1:
                        $ leanne.weight += 0.5
                    else:
                        $ leanne.weight += 0.3
                    call bbworking
                    return
                "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0:
                    image lyn_cafe_prize1 = "/leanne/[leanne.stage]/Lyn_prize1.webp"
                    scene lyn_cafe_prize1
                    "Creating a sizable feast, you approach Lyn's seat."
                    image lyn_cafe_prize2 = "/leanne/[leanne.stage]/Lyn_prize2.webp"
                    scene lyn_cafe_prize2
                    pc "Congratulations! You're the winner of this week's prize. That means you get to eat as much as you want today."
                    leanne "Really? I won? Thank you so much. If you don't mind I think I'll start with…"
                    image lyn_cafe_prize3 = "/leanne/[leanne.stage]/Lyn_prize3.webp"
                    scene lyn_cafe_prize3
                    "Taking a seat across from Lyn as the other servers get more food, you watch as she lovingly gazes at the one woman feast."
                    "The intimidating spread makes her hesitate for a moment, but eventually she moves to take the first bite."
                    image lyn_cafe_prize4 = "/leanne/[leanne.stage]/Lyn_prize4.webp"
                    scene lyn_cafe_prize4
                    "Though she tried to pace herself at first, she picks up speed as she realizes how much food is left."
                    "Whenever she starts to slow down, a quick glance at your expectant face is enough to get her going again."
                    image lyn_cafe_prize5 = "/leanne/[leanne.stage]/Lyn_prize5.webp"
                    scene lyn_cafe_prize5
                    "Looking at her midrif, you see her soft belly growing more round by the second."
                    image lyn_cafe_prize6 = "/leanne/[leanne.stage]/Lyn_prize6.webp"
                    scene lyn_cafe_prize6
                    window hide
                    pause
                    image lyn_cafe_prize7 = "/leanne/[leanne.stage]/Lyn_prize7.webp"
                    scene lyn_cafe_prize7
                    "Her skin strained to keep her expanding stomach contained."
                    image lyn_cafe_prize8 = "/leanne/[leanne.stage]/Lyn_prize8.webp"
                    scene lyn_cafe_prize8
                    "As motivated as she is, she inevitably starts to hit her limits. It becomes a slog as she tries to force down bite after bite."
                    "More than once she has to pause to catch her breath before going back in an attempt to not let the meal go to waste."
                    image lyn_cafe_prize9 = "/leanne/[leanne.stage]/Lyn_prize9.webp"
                    scene lyn_cafe_prize9
                    "Finally hitting her breaking point, Lyn surrenders as she slouches back in her seat."
                    leanne "No…more."
                    pc "It was still pretty impressive you made it this far."
                    image lyn_cafe_prize10 = "/leanne/[leanne.stage]/Lyn_prize10.webp"
                    scene lyn_cafe_prize10
                    leanne "Thank you."
                    image lyn_cafe_prize11 = "/leanne/[leanne.stage]/Lyn_prize11.webp"
                    scene lyn_cafe_prize11
                    "Keeping Lyn company for a while to let her food digest, you help her to her feet and escort her out the door before returning to the counter for the rest of your shift."
                    if secretfeedervol2 == 1:
                        $ leanne.weight += 1.5
                    elif secretfeedervol1 == 1:
                        $ leanne.weight += 1.2
                    else:
                        $ leanne.weight += 1
                    $ weeklyprize -= 1
                    call bbworking
                    return

        if leanne.stage >= 12 and leannechoice == 2 and leannestage12event2 == 0:
            image leanne_cafe_arrive = "/leanne/[leanne.stage]/Leanne_cafe_arrive.webp"
            scene leanne_cafe_arrive
            "A customer arrives at the diner."
            pc "Hey, it's Leanne!"
            image leanne_cafe_talk = "/leanne/[leanne.stage]/Leanne_cafe_talk.webp"
            scene leanne_cafe_talk
            leanne "Hey there! Always nice to see one of my favorite fans working hard."
            pc "What brings you in today?"
            leanne "Same as always. Stuffing myself and writing it off as a business expense. Promise you'll take care of me?"
            pc "I'll do my best. What can I get you?"
            if leanne.stage >= 14:
                image leanne_cafe_talk2 = "/leanne/[leanne.stage]/Leanne_cafe_talk2.webp"
                scene leanne_cafe_talk2
            leanne "Let's see. I think I'll have the large chunky bunny menu."
            pc "Coming right up. Take a seat and I'll bring it to you."
            if leanne.stage <= 13:
                image leanne_cafe_assview = "/leanne/[leanne.stage]/Leanne_cafe_assview.webp"
                scene leanne_cafe_assview
            leanne "Thanks."
            #(NOTE: From here Leanne would order from the menu. Leaving this spot blank for whatever meals you want to include. Choice B and C would open up as the player progresses through the story)
            #CHOICE: A) Make a regular meal B) Accidentally make a larger order or C) Give her the weekly customer special prize
            menu:
                "Create her food normally.":
                    image leanne_cafe_booth = "/leanne/[leanne.stage]/Leanne_cafe_booth.webp"
                    scene leanne_cafe_booth
                    "Bringing the food over to Leanne's table, you chat for a little bit before leaving her to eat."
                    image leanne_cafe_bye = "/leanne/[leanne.stage]/Leanne_cafe_bye.webp"
                    scene leanne_cafe_bye
                    "Finishing up her food and paying the bill, Leanne waves goodbye as she leaves the diner."
                    $ leanne.weight += 0.2
                    call bbworking
                    return
                "Use the secret fattening formula." if secretfeedervol1 == 1:
                    "You create her food with the secret fattening formula."
                    image leanne_cafe_booth = "/leanne/[leanne.stage]/Leanne_cafe_booth.webp"
                    scene leanne_cafe_booth
                    "Bringing the food over to Leanne’s table, you chat for a little bit before leaving her to eat."
                    image leanne_cafe_bye = "/leanne/[leanne.stage]/Leanne_cafe_bye.webp"
                    scene leanne_cafe_bye
                    "Finishing up her food and paying the bill, Leanne waves goodbye as she leaves the diner."
                    if secretfeedervol2 == 1:
                        $ leanne.weight += 0.5
                    elif secretfeedervol1 == 1:
                        $ leanne.weight += 0.3
                    else:
                        $ leanne.weight += 0.2
                    call bbworking
                    return
                "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                    "You end up making a lot more food than she asked for and pay for the difference with your own money."
                    $ money -= 5
                    image leanne_cafe_extrafood = "/leanne/[leanne.stage]/Leanne_cafe_extrafood.webp"
                    scene leanne_cafe_extrafood
                    leanne "Hold on, I didn't think I'd get this much."
                    pc "Sorry, I got a little carried away. Don't worry about the extra. I'll cover the cost."
                    leanne "Aww, supporting your favorite streamer even when she's not performing? Alright, let me give you a bit of a show then."
                    image leanne_cafe_eat = "/leanne/[leanne.stage]/Leanne_cafe_eat.webp"
                    scene leanne_cafe_eat
                    "True to her word, she proceeds to eat every last bite."
                    image leanne_cafe_struggle = "/leanne/[leanne.stage]/Leanne_cafe_struggle.webp"
                    scene leanne_cafe_struggle
                    leanne "That was great. Thanks again."
                    if leanne.stage >= 14:
                        image leanne_cafe_struggle2 = "/leanne/[leanne.stage]/Leanne_cafe_struggle2.webp"
                        scene leanne_cafe_struggle2
                    "After wiping her face clean, Leanne heads out."
                    if secretfeedervol2 == 1:
                        $ leanne.weight += 0.8
                    elif secretfeedervol1 == 1:
                        $ leanne.weight += 0.5
                    else:
                        $ leanne.weight += 0.3
                    call bbworking
                    return
                "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0:
                    image leanne_cafe_prize1 = "/leanne/[leanne.stage]/Leanne_prize1.webp"
                    scene leanne_cafe_prize1
                    "Creating a sizable feast, you approach Leanne's seat."
                    image leanne_cafe_prize2 = "/leanne/[leanne.stage]/Leanne_prize2.webp"
                    scene leanne_cafe_prize2
                    pc "Congratulations! You're the winner of this week's prize. That means you get to eat as much as you want."
                    leanne "Seriously? Must be my lucky day. And yours if you have time to chat while you watch my skills at work."
                    image leanne_cafe_prize3 = "/leanne/[leanne.stage]/Leanne_prize3.webp"
                    scene leanne_cafe_prize3
                    "Taking a seat across from Leanne as the other servers get more food, you watch as she dives into her one woman feast."
                    "The intimidating spread doesn't even make her flinch as she scarfs down one bite after another."
                    image leanne_cafe_prize4 = "/leanne/[leanne.stage]/Leanne_prize4.webp"
                    scene leanne_cafe_prize4
                    "Upon finishing off the first few courses, she eagerly accepts the next servings of food to continue stuffing her gut."
                    "More than once you hear someone in the diner remark about her incredible appetite."
                    image leanne_cafe_prize5 = "/leanne/[leanne.stage]/Leanne_prize5.webp"
                    scene leanne_cafe_prize5
                    "Looking at her midrif, you see her soft belly growing more round by the second."
                    image leanne_cafe_prize6 = "/leanne/[leanne.stage]/Leanne_prize6.webp"
                    scene leanne_cafe_prize6
                    window hide
                    pause
                    image leanne_cafe_prize7 = "/leanne/[leanne.stage]/Leanne_prize7.webp"
                    scene leanne_cafe_prize7
                    "Her skin strained to keep her expanding stomach contained."
                    image leanne_cafe_prize8 = "/leanne/[leanne.stage]/Leanne_prize8.webp"
                    scene leanne_cafe_prize8
                    "As impressive as she is, she starts to slow down by the end." 
                    "Her supposed bottomless belly forces her eating to a crawl as she finally starts to hit her limit."
                    image leanne_cafe_prize9 = "/leanne/[leanne.stage]/Leanne_prize9.webp"
                    scene leanne_cafe_prize9
                    "Managing to force one last morsel of food, she slouches back in her seat to catch her breath."
                    image leanne_cafe_prize10 = "/leanne/[leanne.stage]/Leanne_prize10.webp"
                    scene leanne_cafe_prize10 with vpunch
                    leanne "That was UUUURRP excellent."
                    pc "It was pretty amazing that you were able to make it this far."
                    image leanne_cafe_prize11 = "/leanne/[leanne.stage]/Leanne_prize11.webp"
                    scene leanne_cafe_prize11
                    leanne "Oh that was nothing. I bet you I can eat even more next time."
                    image leanne_cafe_prize12 = "/leanne/[leanne.stage]/Leanne_prize12.webp"
                    scene leanne_cafe_prize12
                    "Keeping Leanne company to praise her abilities and rub her overstuffed stomach, you eventually part ways as she heads out and you get back to work."
                    if secretfeedervol2 == 1:
                        $ leanne.weight += 1.5
                    elif secretfeedervol1 == 1:
                        $ leanne.weight += 1.2
                    else:
                        $ leanne.weight += 1
                    $ weeklyprize -= 1
                    call bbworking
                    return




    elif rngworkcustomer <= 105:
        if hari_work_today == 1:
            jump work_randomizer
        if haristage2event2 == 1:
            $ hari_work_today = 1
            image cafe_tracy_arrive = "/side/tracy_cafe_arrive.webp"
            scene cafe_tracy_arrive
            "A customer arrives at the diner."
            $ unknownname = 'Cool-looking Woman'
            image cafe_tracy_talk = "/side/tracy_cafe_talk.webp"
            scene cafe_tracy_talk
            unknown "Hello, I would like to order."
            pc "Go ahead."
            unknown "I would like a slice of pizza and a burger please."
            pc "Coming right up, please feel free to sit anywhere you would like."
            "You create her food."
            image cafe_tracy_booth = "/side/tracy_cafe_booth.webp"
            scene cafe_tracy_booth
            pc "Here you go. Have a nice meal."
            unknown "Thank you!"
            $ unknownname = 'Unknown'
            call bbworking
            return
        $ hari_work_today = 1
        image cafe_hari_arrive = "/hari/[hari.stage]/cafe_arrive.webp"
        scene cafe_hari_arrive
        "A customer walks into the diner."
        pc "Hey, it’s Hari!"
        image cafe_hari_talk = "/hari/[hari.stage]/cafe_talk.webp"
        scene cafe_hari_talk
        hari "Oh, hello, [playername]."
        pc "Hey, Hari. What can I get you today?"
        hari "Um, I think I’ll have a hamburger and one slice of pizza."
        menu:
            "Create her food normally.":
                "You create her food."
                image cafe_hari_booth = "/hari/[hari.stage]/cafe_booth.webp"
                scene cafe_hari_booth
                "Bringing the food to Hari, you chat with her a little bit while she enjoys her meal."
                image cafe_hari_bye = "/hari/[hari.stage]/cafe_bye.webp"
                scene cafe_hari_bye
                "Finishing the food and paying the bill, Hari says goodbye before leaving the diner."
                $ hari.weight += 0.2
                call bbworking
                return
            "Use the secret fattening formula." if secretfeedervol1 == 1:
                "You create her food with the secret fattening formula."
                image cafe_hari_booth = "/hari/[hari.stage]/cafe_booth.webp"
                scene cafe_hari_booth
                "Bringing the food to Hari, you chat with her a little bit while she enjoys her meal."
                image cafe_hari_bye = "/hari/[hari.stage]/cafe_bye.webp"
                scene cafe_hari_bye
                "Finishing the food and paying the bill, Hari says goodbye before leaving the diner."
                if secretfeedervol2 == 1:
                    $ hari.weight += 0.5
                elif secretfeedervol1 == 1:
                    $ hari.weight += 0.3
                else:
                    $ hari.weight += 0.2
                call bbworking
                return
            "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                "You end up making more food than she asked for."
                if secretfeedervol1 == 1:
                    "You create her food with the secret fattening formula."
                "You decide to pay the difference yourself."
                $ money -= 5
                image cafe_hari_extrafood = "/hari/[hari.stage]/cafe_extrafood.webp"
                scene cafe_hari_extrafood
                "Looking at the food, Hari seems to squirm in her seat."
                pc "Is everything okay?"
                hari "Well…I didn’t order this much. I’m sorry, but I’m not sure I can afford this right now."
                pc "Don’t worry about it. I’ll cover the extra cost. You just enjoy your meal."
                hari "You don’t have to… Well, I guess it’s fine for now."
                image cafe_hari_eating = "/hari/[hari.stage]/cafe_eating.webp"
                scene cafe_hari_eating
                "The knowledge of where the extra food came from pushes Hari to scarf down every last bite."
                image cafe_hari_stuffed = "/hari/[hari.stage]/cafe_stuffed.webp"
                scene cafe_hari_stuffed
                pc "How was it?"
                hari "It was…pretty good. Thank you."
                "Cleaning herself up and saying goodbye, she leaves the diner."
                if secretfeedervol2 == 1:
                    $ hari.weight += 0.8
                elif secretfeedervol1 == 1:
                    $ hari.weight += 0.5
                else:
                    $ hari.weight += 0.3
                call bbworking
                return
            "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0 and disable == 1:
                "Creating a sizable feast, you approach Hari’s seat."
                #IMAGE: Hari awestruck at the massive amount of food.
                pc "Congratulations! You’re the winner of this week’s prize. That means you get to eat as much as you want."
                hari "B-but I didn’t do anything."
                pc "It’s a random drawing. You just so happen to be the lucky customer."
                hari "I, um, well…"
                #IMAGE: The player sitting across from Hari as she eats her food
                "Out of a need to do something other than focus on the people staring at her, Hari proceeds to dive into the meal."
                #IMAGE: Hari struggling to eat her food.
                "Unfortunately, Hari’s nerves seem to be a lot larger than her appetite."
                "Not even halfway through you watch as she struggles to continue through the feast."
                #IMAGE: Hari slouched in the booth with a stuffed belly.
                "Inevitably, Hari has to give up eating in favor of leaning back to nurse her overburdened belly."
                pc "How was it?"
                hari "It was good, but I couldn’t eat all of it. I’m sorry."
                pc "That’s alright. We’ll pack up the rest so you can take it home."
                hari "Thank you."
                "Staying with Hari to keep her mind off of the people glancing at her, you go back to the counter after the servers hand her the take out bags and she leaves the diner."
                call bbworking
                return

    elif rngworkcustomer <= 110:
        if vicky_work_today == 1:
            jump work_randomizer
        if vickystage2event == 1:
            jump work_randomizer
        $ vicky_work_today = 1
        image cafe_vicky_arrive = "/vicky/[vicky.stage]/cafe_arrive.webp"
        scene cafe_vicky_arrive
        "A customer walks in, it's Vicky."
        image cafe_vicky_talk = "/vicky/[vicky.stage]/cafe_talk.webp"
        scene cafe_vicky_talk
        pc "Hey Vicky, what'll it be today?"
        vicky "Hmmm, I think I'll have the same thing as last time."
        image cafe_vicky_ass = "/vicky/[vicky.stage]/cafe_ass.webp"
        scene cafe_vicky_ass
        "You've already been paying for her meals, so you're certainly not going to give her any extra."
        menu:
            "Give her what she ordered.":
                "You create her food and bring it to her table."
                image cafe_vicky_booth = "/vicky/[vicky.stage]/cafe_booth.webp"
                scene cafe_vicky_booth
                "Vicky doesn't say much as she ferociously chows down her meal."
                image cafe_vicky_leave = "/vicky/[vicky.stage]/cafe_leave.webp"
                scene cafe_vicky_leave
                vicky "That was, like, really good [playername]. Oh and um, thanks I guess."
                pc "Don't mention it."
                $ vicky.weight += 0.5
                call bbworking
                return
            "Use the secret fattening formula." if secretfeedervol1 == 1:
                "You create her food with the secret fattening formula and bring it to her table."
                image cafe_vicky_booth = "/vicky/[vicky.stage]/cafe_booth.webp"
                scene cafe_vicky_booth
                "Vicky doesn't say much as she ferociously chows down her meal."
                image cafe_vicky_leave = "/vicky/[vicky.stage]/cafe_leave.webp"
                scene cafe_vicky_leave
                vicky "That was, like, really good [playername]. Oh and um, thanks I guess."
                pc "Don't mention it."
                if secretfeedervol2 == 1:
                    $ vicky.weight += 0.9
                elif secretfeedervol1 == 1:
                    $ vicky.weight += 0.7
                else:
                    $ vicky.weight += 0.5
                call bbworking
                return
            "Give her the weekly special customer prize." if weeklyprize >= 1 and mariestage6event2 == 0 and disable == 1:
                "You're tired of covering her meals, time to let the restaurant handle the bill for once."
                "You prepare a massive platter of food for Vicky."
                #[Image: Vicky with a hand in front of her mouth in surprise, looking at the giant platter.]
                vicky "Um, wow! What's the occasion?"
                pc "You're the winner of our weekly draw, so today you can eat as much as you want, on the house. Congratulation!"
                #[Image: Vicky smirking at the player]
                "Vicky smirks"
                vicky "Mmm, like, lucky me!"
                #[Image: Vicky eating like a pig]
                "Given carte blanche, Vicky lets her appetite run wild."
                #[Image:Vicky lets out a loud burp]
                vicky "HOOOURP! More!"
                #[Image: Vicky drinking two milkshakes at once]
                "You almost wonder if she was holding back whenever you had to pay for her."
                "Either that or she was just in the mood to make a spectacle of herself today."
                #[Image: Vicky leaning back, rubbing her stuffed gut.]
                "Eventually, her feast came to an end."
                vicky "Oof, that was like —hic!— SO good!"
                pc "Glad you enjoyed, come back soon."
                vicky "Oh, I will."
                "With that, Vicky struggles up from her booth and heads for the door."
                if secretfeedervol2 == 1:
                    $ vicky.weight += 1.5
                elif secretfeedervol1 == 1:
                    $ vicky.weight += 1.2
                else:
                    $ vicky.weight += 1.0
                call bbworking
                return

    elif rngworkcustomer <= 115:
        if librarian_work_today == 1:
            jump work_randomizer
        $ librarian_work_today = 1
        image cafe_librarian_arrive = "/side/lib_cafe_arrive[librarianstage].webp"
        scene cafe_librarian_arrive
        "A customer arrives at the diner."
        pc "Hey, it's the girl from the library."
        image cafe_librarian_talk = "/side/lib_cafe_talk[librarianstage].webp"
        scene cafe_librarian_talk
        librarian "Hello, I would like to order."
        pc "Go ahead."
        librarian "I would like to order a hamburger and one slice of pizza."
        pc "Coming right up, please feel free to sit anywhere you would like."
        "You create her food."
        image cafe_librarian_booth = "/side/lib_cafe_booth[librarianstage].webp"
        scene cafe_librarian_booth
        pc "Here you go. Have a nice meal."
        librarian "Thank you!"
        call bbworking
        return

    elif rngworkcustomer <= 120:
        if roxie_work_today == 1:
            jump work_randomizer
        $ roxie_work_today = 1
        if lunastage5event == 1:
            jump work_randomizer
        image cafe_roxie_arrive = "/roxie/[roxie.stage]/cafe_arrive.webp"
        scene cafe_roxie_arrive
        "A customer arrives at the diner."
        pc "Hey, it’s Roxie!"
        image cafe_roxie_talk = "/roxie/[roxie.stage]/cafe_talk.webp"
        scene cafe_roxie_talk
        if roxie.stage == 4:
            roxie "Hey, thank you again for helping me with Luna."
            if roxiestory == 0:
                pc "No problem."
                menu:
                    "Ask Roxie about herself.":
                        "You decide to ask Roxie about herself."
                        roxie "Well, I like Luna, and I really like Luna, and I would love to be with Luna."
                        roxie "I'm just kidding."
                        "Roxie talks a bit about herself."
                        $ roxiestory += 1
                        #Unlocks more Roxie story in the stats page.
                        $ renpy.notify("New Roxie story unlocked in the stats screen.")
                        window hide
                        pause
                        pc "So what will you be having?"
                    "Nevermind.":
                        "You decide not to ask Roxie anything."
                        pc "So what will you be having?"
            else:
                pc "No problem, so what will you be having?"
            roxie "I’m going to try to eat the Luna special again, I think I can eat all of it this time."
            pc "Well the old Luna special maybe, she’s eating even more now."
            roxie "I’m not surprised, well I guess I’ll take the old Luna special then since I can at least maybe do that one now."
            pc "Coming right up."
            image cafe_roxie_ass = "/roxie/[roxie.stage]/cafe_ass.webp"
            scene cafe_roxie_ass
            "She goes and takes a seat."
            image cafe_roxie_booth = "/roxie/[roxie.stage]/cafe_booth.webp"
            scene cafe_roxie_booth
            "While waiting for her food, she spends a great deal of time playing with and enjoying her huge breasts, as if still amazed by their rapid increase in size and weight."
            "Not that you can blame her."
            image cafe_roxie_eat = "/roxie/[roxie.stage]/cafe_eat.webp"
            scene cafe_roxie_eat
            "You then bring her food and Roxie really digs in and eats."
            "When she eats the last bite, she yells in triumph!"
            image cafe_roxie_happy = "/roxie/[roxie.stage]/cafe_happy.webp"
            scene cafe_roxie_happy
            roxie "I did it!"
            pc "Congratulations!"
            image cafe_roxie_stuffed = "/roxie/[roxie.stage]/cafe_stuffed.webp"
            scene cafe_roxie_stuffed
            roxie "Thanks! I think I still even have some room leftover for dessert. Can I get some of the Natalie or Britta ice cream? That looks really tasty."
            pc "Unfortunately not, it’s really popular and already sold out."
            roxie "Shame, well I’ll just have some cake then."
            image cafe_roxie_bye = "/roxie/[roxie.stage]/cafe_bye.webp"
            scene cafe_roxie_bye
            "She gets the cake, eats it, and then leaves."
        else:
            roxie "I’ll have a pair of big chicken breasts."
            pc "We don’t have that on the menu."
            roxie "I know. It got you to look at mine though, didn't it?"
            pc "Yeah, you got me! So what do you really want to have?"
            roxie "Whatever Luna’s favorite meal is whenever she comes in sounds good right now."
            pc "Sure, I can do that. Why don't you have a seat and I'll bring it to you?"
            image cafe_roxie_ass = "/roxie/[roxie.stage]/cafe_ass.webp"
            scene cafe_roxie_ass
            "Roxie goes and sits down and waits until you bring her her food, which is also Luna’s regular order."
            image cafe_roxie_extrafood = "/roxie/[roxie.stage]/cafe_extrafood.webp"
            scene cafe_roxie_extrafood
            "Roxie looks over the very large amount of food, which goes beyond the extra large sizes you normally have at the restaurant to something you can only call Luna-sized."
            roxie "Luna sure does manage to eat a lot doesn’t she?"
            pc "Yes, she does. Would you maybe like a to-go box?"
            roxie "No. If Luna can eat this much, I can too."
            image cafe_roxie_struggle = "/roxie/[roxie.stage]/cafe_struggle.webp"
            scene cafe_roxie_struggle
            "She does her best to try and finish eating all of it, but ultimately can’t and has to ask for a to-go box, much to her disappointment."
            roxie "Next time I’ll succeed."
        call bbworking
        return

    elif rngworkcustomer <= 125:
        if natalie_work_today == 1:
            jump work_randomizer
        $ natalie_work_today = 1
        if lunastage5event == 1:
            jump work_randomizer
        image cafe_natalie_arrive = "/natalie/[natalie.stage]/cafe_arrive.webp"
        scene cafe_natalie_arrive
        "A customer arrives at the diner."
        pc "Hey, it’s Natalie!"
        image cafe_natalie_talk = "/natalie/[natalie.stage]/cafe_talk.webp"
        scene cafe_natalie_talk
        if nataliestage3event == 0:
            "Natalie smiles widely at you."
            natalie "Hi, I thought I would come in and see you as well as take advantage of the free meals or at least large discounts on food I’m able to get now."
            pc "It’s nice to see you too and this time it’s an all you can eat totally on the house discount. Your milk ice cream is selling super well, we sell out almost as fast as I deliver it!"
            natalie "That’s great! I’m really glad to hear that."
            pc "So what would you like?"
            natalie "Hmm, I’m not sure, all I know is I’m so hungry I feel like I could eat an entire cow! I almost feel like I’m turning into a cow."
            pc "You’re certainly my sexy, growing cow."
            image cafe_natalie_blush = "/natalie/[natalie.stage]/cafe_blush.webp"
            scene cafe_natalie_blush
            natalie "That I am, well how about you surprise me with what you think I would like and you would like to see me eat and I’ll keep eating it until I can’t eat anymore."
            pc "Sure, sounds great."
            image cafe_natalie_ass = "/natalie/[natalie.stage]/cafe_ass.webp"
            scene cafe_natalie_ass
            "Natalie goes and sits down and waits."
            image cafe_natalie_booth2 = "/natalie/[natalie.stage]/cafe_booth2.webp"
            scene cafe_natalie_booth2
            "You order a bunch of food and as it starts to come out you start taking it out to Natalie."
            natalie "You always seem to know what I like…which to be fair is just about everything especially when you’re the one delivering it."
            image cafe_natalie_eat = "/natalie/[natalie.stage]/cafe_eat.webp"
            scene cafe_natalie_eat
            "Natalie starts happily eating food after food and you keep bringing it out until she can’t eat anymore."
            natalie "Mmm, thank you for all the free food."
            pc "You’re very welcome!"
            image cafe_natalie_leave = "/natalie/[natalie.stage]/cafe_leave.webp"
            scene cafe_natalie_leave
            "A while later Natalie gets up leaves the diner."
        else:
            "Natalie shyly smiles at you."
            natalie "Hi. It's really nice to see you."
            pc "It's really nice to see you too. So, what will you be having?"
            natalie "I'll have a twenty piece box of chicken nuggets with an extra large serving of fries and two extra large chocolate milkshakes."
            natalie "I’m just trying to do what I can for the drug trial."
            pc "Well, you're doing a great job!"
            image cafe_natalie_blush = "/natalie/[natalie.stage]/cafe_blush.webp"
            scene cafe_natalie_blush
            "Natalie blushes at hearing you say that."
            natalie "Thanks! Can you be the one to bring me my food?"
            pc "Sure. I'd be happy to bring it to you. Why don't you go have a seat somewhere? Your order will be coming right up!"
            image cafe_natalie_ass = "/natalie/[natalie.stage]/cafe_ass.webp"
            scene cafe_natalie_ass
            "Natalie goes and sits down and waits."
            image cafe_natalie_booth = "/natalie/[natalie.stage]/cafe_booth.webp"
            scene cafe_natalie_booth
            "Seeming to enjoy watching you work and blushing every time you look back at her until you bring over her food, which she happily eats all of."
        call bbworking
        return

    elif rngworkcustomer <= 130:
        if charlene_work_today == 1:
            jump work_randomizer
        $ charlene_work_today = 1
        if lunastage5event == 1:
            jump work_randomizer
        image cafe_charlene_arrive = "/charlene/[charlene.stage]/cafe_arrive.webp"
        scene cafe_charlene_arrive
        if charlene.stage == 4:
            "A customer arrives at the diner."
            "Hey, it’s Charlene!"
            image cafe_charlene_talk = "/charlene/[charlene.stage]/cafe_talk.webp"
            scene cafe_charlene_talk
            "Unlike previous visits though, she seems almost happy to see you."
            charlene "I keep having cravings for your food here. I just couldn’t help myself in coming in to eat."
            pc "It’s okay, I actually hear that a lot from customers."
            if charlenestory == 0:
                menu:
                    "Ask Charlene about herself.":
                        "You decide to ask Charlene about herself."
                        charlene "I don't think I have ever had a man ask me about myself."
                        charlene "You are certainly surprising."
                        "Charlene talks a bit about herself."
                        $ charlenestory += 1
                        #Unlocks more Charlene story in the stats page.
                        $ renpy.notify("New Charlene story unlocked in the stats screen.")
                        window hide
                        pause
                    "Nevermind.":
                        "You decide not to ask Charlene anything."
            pc "So what can I get you?"
            charlene "Can I get a Hog Feast…actually could you get me one to-go as well for later?"
            pc "Sure, coming right up, why don’t you go have a seat?"
            image cafe_charlene_ass = "/charlene/[charlene.stage]/cafe_ass.webp"
            scene cafe_charlene_ass
            "Charlene goes and takes a seat, but is unable to wait and pulls out some snacks she had hidden to tide her over until you bring her food out."
            image cafe_charlene_booth = "/charlene/[charlene.stage]/cafe_booth.webp"
            scene cafe_charlene_booth
            charlene "Thank you…you can uh, watch me eat if you want, just make sure nobody else is really watching me."
            "She looks around the restaurant nervously as if afraid other people are going to see her pig out before she relaxes and starts stuffing her face."
            image cafe_charlene_eating = "/charlene/[charlene.stage]/cafe_eating.webp"
            scene cafe_charlene_eating
            "You do have to still work but you still look over occasionally at her and watch her eat, seeing the happy look on her face as she does so."
            "Before she leaves, you can’t help but notice that the second meal she was intending to eat later got eaten as well."
        else:
            "A customer arrives at the diner."
            pc "Hey, it’s Charlene!"
            image cafe_charlene_talk = "/charlene/[charlene.stage]/cafe_talk.webp"
            scene cafe_charlene_talk
            "Charlene groans in annoyance at seeing you there."
            charlene "I’ll have the Hog Feast and make sure it is done right this time."
            pc "Of course. Coming right up. Why don't you have a seat and I'll bring it to you?"
            charlene "Okay. Just don't take too long. And I expect it to be hot!"
            image cafe_charlene_ass = "/charlene/[charlene.stage]/cafe_ass.webp"
            scene cafe_charlene_ass
            "She goes and takes a seat until you bring her her food, which she examines closely."
            image cafe_charlene_booth = "/charlene/[charlene.stage]/cafe_booth.webp"
            scene cafe_charlene_booth
            charlene "It's acceptable, I suppose. This time at least."
            pc "Great! I’m glad that you approve!"
            charlene "Yeah, uh…thanks."
            "She grudgingly thanks you."
            image cafe_charlene_eating = "/charlene/[charlene.stage]/cafe_eating.webp"
            scene cafe_charlene_eating
            "You start walking away but turn around to see a big smile on her face as she happily begins eating, but scowls again when she sees you looking at her."
            "You get back to your work and let her eat in peace."

        call bbworking
        return

    elif rngworkcustomer <= 135:
        if sally_work_today == 1:
            jump work_randomizer
        $ sally_work_today = 1
        if lunastage5event == 1:
            jump work_randomizer
        image cafe_sally_arrive = "/sally/[sally.stage]/cafe_arrive.webp"
        scene cafe_sally_arrive
        "A customer arrives at the diner."
        pc "Hey, it’s Sally!"
        image cafe_sally_talk = "/sally/[sally.stage]/cafe_talk.webp"
        scene cafe_sally_talk
        if sally.stage == 4:
            sally "Hi, you got enough food here for me?"
            pc "I certainly hope so but the way you eat I can never be sure!"
            if sallystory == 0:
                menu:
                    "Ask Sally about herself.":
                        "You decide to ask Sally about herself."
                        sally "You want to know some more about the woman you are having sex with huh?"
                        sally "Just try not to fall in love with me, okay?"
                        "Sally talks a bit about herself."
                        $ sallystory += 1
                        #Unlocks more Sally story in the stats page.
                        $ renpy.notify("New Sally story unlocked in the stats screen.")
                        window hide
                        pause
                    "Nevermind.":
                        "You decide not to ask Sally anything."
            pc "So what will you be having?"
            image cafe_sally_talk2 = "/sally/[sally.stage]/cafe_talk2.webp"
            scene cafe_sally_talk2
            sally "Mmm, how about I have you right here, right now?"
            pc "Tempting but that would definitely get me fired and probably both of us arrested."
            sally "Shame, well in that case I’ll have a Family Sized Fried Appetizer Mix, a Big Chungus Meal, and a cheesecake for dessert."
            pc "Coming right up, why don’t you go have a seat somewhere?"
            image cafe_sally_ass = "/sally/[sally.stage]/cafe_ass.webp"
            scene cafe_sally_ass
            "Sally manages to squeeze into a booth and watches the waitresses walk around."
            image cafe_sally_booth = "/sally/[sally.stage]/cafe_booth.webp"
            scene cafe_sally_booth
            sally "So how many of them have you had sex with so far?"
            pc "No comment."
            image cafe_sally_eating = "/sally/[sally.stage]/cafe_eating.webp"
            scene cafe_sally_eating
            "Sally just laughs and focuses on her food, eating it all before leaving."
            image cafe_sally_bye = "/sally/[sally.stage]/cafe_bye.webp"
            scene cafe_sally_bye
            pause
        else:
            sally "Hi. You got enough food here for me?"
            pc "I certainly hope so! So, what will you be having?"
            sally "You look good. Can I have you to eat?"
            pc "I’m not sure I would be all that tasty."
            sally "You look plenty tasty to me, but since you’re busy working I think I’ll have the Big Chungus Meal."
            pc "Coming right up! Why don’t you have a seat and I’ll bring it to you?"
            image cafe_sally_ass = "/sally/[sally.stage]/cafe_ass.webp"
            scene cafe_sally_ass
            "Sally then goes and finds a booth, managing to wiggle her big butt onto the seat cushion."
            "Then while she waits, she alternates between watching you and then the Bunny Bites server girls walking around in their bunny costumes."
            image cafe_sally_booth = "/sally/[sally.stage]/cafe_booth.webp"
            scene cafe_sally_booth
            sally "Maybe I should get a bunny costume like that. Do you think it would look sexy on me?"
            pc "Yeah, I'm sure it would. You would probably just outgrow it though."
            image cafe_sally_eating = "/sally/[sally.stage]/cafe_eating.webp"
            scene cafe_sally_eating
            "However, Sally doesn't appear to be paying attention anymore as she is now eating rapidly as if she were starving."
            "She doesn’t even seem to notice you asking if there is anything else you can get her as you decide to just leave and let her eat."
        call bbworking
        return

    elif rngworkcustomer <= 140:
        if britta_work_today == 1:
            jump work_randomizer
        $ britta_work_today = 1
        if lunastage5event == 1:
            jump work_randomizer
        image cafe_britta_arrive = "/britta/[britta.stage]/cafe_arrive.webp"
        scene cafe_britta_arrive
        "A customer arrives at the diner."
        pc "Hey, it’s Britta!"
        image cafe_britta_talk = "/britta/[britta.stage]/cafe_talk.webp"
        scene cafe_britta_talk
        if britta.stage == 4:
            pc "Hey girl, your milk has been a big hit here."
            pc "Since it's been selling so well, your next meal is on the house."
            pc "You can order as much as you want just make sure to finish it all here, okay? So, what can I get you?"
            britta "Oh why thank you, if that’s the case then I definitely want to take full advantage. Can I see a menu real quick?"
            "You give her one and she studies it for a moment before giving it back to you."
            image cafe_britta_talk2 = "/britta/[britta.stage]/cafe_talk2.webp"
            scene cafe_britta_talk2
            britta "I’ve been able to increase my stomach capacity by another 52 percent so given those parameters to work with."
            britta "I should be able to eat 3 cheeseburgers with extra mayo, 3 extra large servings of fries with cheese dip, an extra large milkshake, and 2 chocolate pies for dessert."
            britta "Giving me a total of 6,352 calories consumed."
            pc "Coming right up! Take a seat and I'll have it out to you when it’s ready."
            image cafe_britta_ass = "/britta/[britta.stage]/cafe_ass.webp"
            scene cafe_britta_ass
            "Britta finds a place to sit down, she seems to be working on complicated math equations when you bring out her order."
            image cafe_britta_booth = "/britta/[britta.stage]/cafe_booth.webp"
            scene cafe_britta_booth
            britta "Just what I need, food always helps me think better, which is why I eat while working all the time now."
            "She manages to eat all of the food while still working, but stops you afterwards."
            image cafe_britta_booth2 = "/britta/[britta.stage]/cafe_booth2.webp"
            scene cafe_britta_booth2
            britta "It appears that my calculations were slightly incorrect and I can actually eat a little more, can I get another chocolate pie? I do so love pie, both the math and food versions."
            pc "Sure, coming right up."
            image cafe_britta_bye = "/britta/[britta.stage]/cafe_bye.webp"
            scene cafe_britta_bye
            "Britta finishes eating yet more pie and then leaves."
        else:
            britta "Hey. How is it going?"
            pc "Good. What about you?"
            britta "Oh, the usual. Lots of work to do. I just couldn't concentrate on my work anymore, until I got something to eat."
            pc "Well, you definitely need to eat - especially for the drug trial."
            image cafe_britta_talk2 = "/britta/[britta.stage]/cafe_talk2.webp"
            scene cafe_britta_talk2
            britta "For sure. If I wish to achieve my desired results, I would need to consume over 3,500 calories for this meal."
            britta "So if my math is correct, I would like and will need two cheeseburgers with extra mayo,"
            britta "two extra large servings of fries with cheese dip, an extra large chocolate milkshake and a chocolate pie for dessert."
            pc "Coming right up! Why don’t you go have a seat somewhere and I will bring it to you?"
            image cafe_britta_ass = "/britta/[britta.stage]/cafe_ass.webp"
            scene cafe_britta_ass
            "Britta goes and sits down, seeming to now be thinking hard about something probably to do with work. She doesn’t even notice at first when you come and bring her food."
            image cafe_britta_booth2 = "/britta/[britta.stage]/cafe_booth2.webp"
            scene cafe_britta_booth2
            britta "Oh, is it ready already? Time flies when you’re having fun doing complicated mathematical equations in your head."
            pc "Uh, I suppose so. At least for some people. Enjoy your food though."
            britta "Thanks!"
            "Britta then however turns all of her attention to eating, seeming to forget even about work as she does so."
        call bbworking
        return

    elif rngworkcustomer <= 145:
        if rebecca_work_today == 1:
            jump work_randomizer
        if bonniestage9event == 1:
            jump work_randomizer
        $ rebecca_work_today = 1
        image cafe_rebecca_arrive = "/rebecca/[rebecca.stage]/cafe_arrive.webp"
        scene cafe_rebecca_arrive
        "A customer arrives at the diner."
        pc "Hey, it's Rebecca."
        image cafe_rebecca_talk = "/rebecca/[rebecca.stage]/cafe_talk.webp"
        scene cafe_rebecca_talk
        rebecca "Hey, cutie. How has work treated you today?"
        pc "Hey, Rebecca. Work is alright - not much happening today."
        rebecca "We can always spice things up a bit *wink*."
        pc "What would you like to order."
        rebecca "I would like to order a hamburger and one slice of pizza."
        image cafe_rebecca_ass = "/rebecca/[rebecca.stage]/cafe_ass.webp"
        scene cafe_rebecca_ass
        pc "Coming right up, please feel free to sit anywhere you would like."
        "You create her food."
        image cafe_rebecca_booth = "/rebecca/[rebecca.stage]/cafe_booth.webp"
        scene cafe_rebecca_booth
        pc "Here you go. Have a nice meal."
        rebecca "Thank you!"
        $ rebecca.weight += 0.2
        call bbworking
        return


    elif rngworkcustomer <= 150:
        if mylenna_work_today == 1:
            jump work_randomizer
        $ mylenna_work_today = 1
        image cafe_mylenna_arrive = "/mylenna/[mylenna.stage]/cafe_arrive.webp"
        scene cafe_mylenna_arrive
        "A customer arrives at the diner."
        pc "Hey, it's Mylenna."
        image cafe_mylenna_talk = "/mylenna/[mylenna.stage]/cafe_talk.webp"
        scene cafe_mylenna_talk
        mylenna "Hey, cutie. How has work treated you today?"
        pc "Hey, Mylenna. Work is alright - not much happening today."
        mylenna "We can always spice things up a bit *wink*."
        pc "What would you like to order"
        $ rngworkboothorcounter = renpy.random.randint(1,2)
        if rngworkboothorcounter == 1:
            mylenna "I would like to order a hamburger and one slice of pizza."
            pc "Coming right up, please feel free to sit anywhere you would like."
            menu:
                "Create her food normally.":
                    "You create her food."
                    image cafe_mylenna_booth = "/mylenna/[mylenna.stage]/cafe_booth.webp"
                    scene cafe_mylenna_booth
                    pc "Here you go. Have a nice meal."
                    mylenna "Thank you!"
                    $ mylenna.weight += 0.2
                "Use the secret fattening formula." if secretfeedervol1 == 1:
                    "You create her food with the secret fattening formula."
                    image cafe_mylenna_booth = "/mylenna/[mylenna.stage]/cafe_booth.webp"
                    scene cafe_mylenna_booth
                    pc "Here you go. Have a nice meal."
                    mylenna "Thank you!"
                    if secretfeedervol2 == 1:
                        $ mylenna.weight += 0.5
                    elif secretfeedervol1 == 1:
                        $ mylenna.weight += 0.3
                    else:
                        $ mylenna.weight += 0.2
                "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                    "You make her a lot more food than she asked for."
                    if secretfeedervol1 == 1:
                        "You create her food with the secret fattening formula."
                    "You decide to pay the difference yourself."
                    $ money -= 5
                    image cafe_mylenna_extrafood = "/mylenna/[mylenna.stage]/cafe_extrafood.webp"
                    scene cafe_mylenna_extrafood
                    mylenna "Woah, this is way more than I ordered, I think the orders got mixed up."
                    pc "Oh, I'm sorry, are you alright with taking this order without additional cost?"
                    mylenna "Well, I won't say no to free food."
                    pc "In that case, I hope you enjoy the food."
                    mylenna "Thank you!"
                    image cafe_mylenna_struggle = "/mylenna/[mylenna.stage]/cafe_struggle.webp"
                    scene cafe_mylenna_struggle
                    "You notice Mylenna struggling to eat all of the extra food."
                    if secretfeedervol2 == 1:
                        $ mylenna.weight += 0.8
                    elif secretfeedervol1 == 1:
                        $ mylenna.weight += 0.5
                    else:
                        $ mylenna.weight += 0.3
            call bbworking
            return
        elif rngworkboothorcounter == 2:
            mylenna "I would like to order a whole pizza please."
            pc "Coming right up, please feel free to sit anywhere you would like."
            menu:
                "Create her food normally.":
                    "You create her food."
                    image cafe_mylenna_counter = "/mylenna/[mylenna.stage]/cafe_counter.webp"
                    scene cafe_mylenna_counter
                    pc "Here you go. Have a nice meal."
                    mylenna "Thank you!"
                    $ mylenna.weight += 0.2
                "Use the secret fattening formula." if secretfeedervol1 == 1:
                    "You create her food with the secret fattening formula."
                    image cafe_mylenna_counter = "/mylenna/[mylenna.stage]/cafe_counter.webp"
                    scene cafe_mylenna_counter
                    pc "Here you go. Have a nice meal."
                    mylenna "Thank you!"
                    if secretfeedervol2 == 1:
                        $ mylenna.weight += 0.5
                    elif secretfeedervol1 == 1:
                        $ mylenna.weight += 0.3
                    else:
                        $ mylenna.weight += 0.2
                "“Accidentally” make a larger order. (-$5)" if mariestage2event == 0 and money >= 5:
                    "You make her a lot more food than she asked for."
                    if secretfeedervol1 == 1:
                        "You create her food with the secret fattening formula."
                    "You decide to pay the difference yourself."
                    $ money -= 5
                    image cafe_mylenna_extrafood = "/mylenna/[mylenna.stage]/cafe_extrafood.webp"
                    scene cafe_mylenna_extrafood
                    mylenna "Woah, this is way more than I ordered, I think the orders got mixed up."
                    pc "Oh, I'm sorry, are you alright with taking this order without additional cost?"
                    mylenna "Well, I won't say no to free food."
                    pc "In that case, I hope you enjoy the food."
                    mylenna "Thank you!"
                    image cafe_mylenna_struggle = "/mylenna/[mylenna.stage]/cafe_struggle.webp"
                    scene cafe_mylenna_struggle
                    "You notice Mylenna struggling to eat all of the extra food."
                    if secretfeedervol2 == 1:
                        $ mylenna.weight += 0.8
                    elif secretfeedervol1 == 1:
                        $ mylenna.weight += 0.5
                    else:
                        $ mylenna.weight += 0.3
            call bbworking
            return


label work_arrive:
    if rngworkgirl == 2:
        $ marie_work_today = 1
        image work_marie_workattire_counter = "/marie/[marie.stage]/workattire_counter.webp"
        scene work_marie_workattire_counter
        marie "I'm so glad you came."
        pc "That bad, huh?"
        marie "Not really, I'm just ready to go home."
        pc "I'll manage out here, you go get changed."
        image work_marie_workattire_counter_assview = "/marie/[marie.stage]/workattire_counter_assview.webp"
        scene work_marie_workattire_counter_assview
        "Marie goes and gets changed."
        image work_marie_work_change = "/marie/[marie.stage]/work_change.webp"
        scene work_marie_work_change
        marie "Well, good luck!"
        pc "Thank you, Marie. Enjoy the rest of the day."
        return
    elif rngworkgirl == 3:
        $ amber_work_today = 1
        image work_amber_workattire_counter = "/amber/[amber.stage]/workattire_counter.webp"
        scene work_amber_workattire_counter
        amber "I'm so glad you came."
        pc "Couldn't be that bad, right?"
        amber "Nah, it was fine. I'm just glad to go home."
        pc "I'll take over out here, you go get changed."
        if amber.stage <= 11:
            image work_amber_workattire_counter_assview = "/amber/[amber.stage]/workattire_counter_assview.webp"
            scene work_amber_workattire_counter_assview
        amber "Let me finish this."
        amber "There we go."
        "Amber goes and gets changed."
        image work_amber_work_change = "/amber/[amber.stage]/work_change.webp"
        scene work_amber_work_change
        amber "I'll be going now, talk to you later!"
        pc "Thanks Amber, see you around!"
        return
    else:
        $ lisa_work_today = 1
        image work_lisa_workattire_counter = "/lisa/[lisa.stage]/workattire_counter.webp"
        scene work_lisa_workattire_counter
        lisa "Boy, are you a sight for sore eyes."
        pc "Rough day?"
        lisa "Not really, just glad I can go home."
        pc "I'll take over, you can go get changed."
        image work_lisa_workattire_counter_assview = "/lisa/[lisa.stage]/workattire_counter_assview.webp"
        scene work_lisa_workattire_counter_assview
        lisa "Let me finish this."
        lisa "There we go."
        "Lisa goes and gets changed."
        image work_lisa_work_change = "/lisa/[lisa.stage]/work_change.webp"
        scene work_lisa_work_change
        lisa "Alright, have a good shift."
        pc "Thank you Lisa, enjoy the rest of the day!"
        return

label work_leave:
    if rngworkgirl == 1:
        image work_marie_arrive = "/marie/[marie.stage]/work_arrive.webp"
        scene work_marie_arrive
        pc "Finally!"
        image work_marie_greet = "/marie/[marie.stage]/work_greet.webp"
        scene work_marie_greet
        pc "How's it going, Marie?"
        marie "Not bad, how about you? Sounds like you had a rough shift."
        image work_marie_talk = "/marie/[marie.stage]/work_talk.webp"
        scene work_marie_talk
        pc "Work is work you know, but it wasn't that bad I suppose."
        image work_marie_change = "/marie/[marie.stage]/work_change.webp"
        scene work_marie_change
        marie "Well, let me get changed real quick so you can go home."
        image work_marie_changed = "/marie/[marie.stage]/work_changed.webp"
        scene work_marie_changed
        marie "I'm ready to take over, have a good evening!"
        pc "Thanks, Marie. Good luck with work!"
        scene outside
        stop music fadeout 1.0
        "You make your way back home."
        return

    elif rngworkgirl == 2:
        image work_amber_arrive = "/amber/[amber.stage]/work_arrive.webp"
        scene work_amber_arrive
        pc "Finally!"
        image work_amber_greet = "/amber/[amber.stage]/work_greet.webp"
        scene work_amber_greet
        pc "Boy, am I glad to see you, Amber."
        amber "Work was that bad, huh?"
        image work_amber_talk = "/amber/[amber.stage]/work_talk.webp"
        scene work_amber_talk
        pc "Work is work, you know. I'd rather be at home gaming."
        amber "Tell me about it. But y'know, we all need money."
        image work_amber_change = "/amber/[amber.stage]/work_change.webp"
        scene work_amber_change
        amber "Just let me get changed real quick so you can go home."
        pc "See ya in a bit."
        image work_amber_changed = "/amber/[amber.stage]/work_changed.webp"
        scene work_amber_changed
        amber "I'm ready to take over. Have a good evening!"
        pc "Thanks, Amber. Have a good shift!"
        scene outside
        stop music fadeout 1.0
        "You make your way back home."
        return

    else:
        image work_lisa_arrive = "/lisa/[lisa.stage]/work_arrive.webp"
        scene work_lisa_arrive
        pc "Finally!"
        image work_lisa_greet = "/lisa/[lisa.stage]/work_greet.webp"
        scene work_lisa_greet
        pc "Hey Lisa, I'm really happy to see you here."
        lisa "Hey, was it really that bad?"
        image work_lisa_talk = "/lisa/[lisa.stage]/work_talk.webp"
        scene work_lisa_talk
        pc "Work is work you know, I'm just glad to see you."
        "She flashes you a smile."
        lisa "Aw that's sweet. But yeah, I wouldn't work here if I didn't need the money."
        image work_lisa_change = "/lisa/[lisa.stage]/work_change.webp"
        scene work_lisa_change
        lisa "Just let me get changed real quick so you can go home."
        pc "No problem."
        image work_lisa_changed = "/lisa/[lisa.stage]/work_changed.webp"
        scene work_lisa_changed
        lisa "I'm ready to take over, have a good evening!"
        pc "Thanks Lisa, good luck with work!"
        scene outside
        stop music fadeout 1.0
        "You make your way back home."
        return

label work_arrive_weekend:
    if rngworkgirl == 1:
        image amber_leaning_pillar = "/amber/[amber.stage]/leaning_pillar.webp"
        scene amber_leaning_pillar
        amber "Hey, sugar."
        pc "Good morning, Amber."
        amber "I hope you're ready for another fun day of food service."
        amber "I just need to get changed, brb."
        image amber_work_changed = "/amber/[amber.stage]/work_changed.webp"
        scene amber_work_changed
        amber "There we go."
        pc "You look good in that outfit."
        amber "Thanks!"
        "Amber opens the front door and comes back to talk some more until the customers arrive."
        image amber_standing_on_chair_workattire = "/amber/[amber.stage]/standing_on_chair_workattire.webp"
        scene amber_standing_on_chair_workattire
        amber "Ugh, I'm fighting temptation really hard here."
        pc "What do you mean?"
        amber "I want a burger."
        amber "The owners are okay with us eating after hours, but they're pretty strict about eating on shift."
        pc "I'm not gonna tell, go have as much as you want!"
        amber "Well in that case..."
        "Amber runs off to make some food."
        image amber_workattire_eating = "/amber/[amber.stage]/workattire_eating.webp"
        scene amber_workattire_eating
        "After a while you see Amber in the corner snacking on a burger. She talks to you with her mouth full."
        amber "Mmph, this is sooooo good. I really needed this."
        if amber.stage >= 6:
            $ amber.weight += 1
        else:
            $ amber.weight += 0.5
        image amber_idle_workattire = "/amber/[amber.stage]/idle_workattire.webp"
        scene amber_idle_workattire
        amber "Just don't tell the others about this, yeah? I don't want them thinking I'm a pig."
        pc "Don't worry your secret is safe with me."
        call rngbbarrive
        amber "Well, we've got customers, guess it's time to get started."
        "You start working."
        return

    elif rngworkgirl == 2:
        image lisa_leaning_pillar = "/lisa/[lisa.stage]/leaning_pillar.webp"
        scene lisa_leaning_pillar
        lisa "Morning, good looking."
        pc "Hey Lisa."
        if lisa.stage >= 4:
            image lisa_leaning_pillar_close = "/lisa/[lisa.stage]/leaning_pillar_close.webp"
            scene lisa_leaning_pillar_close
        lisa "Looks like it's you and me again this morning."
        lisa "Gotta go change, brb."
        image lisa_work_changed = "/lisa/[lisa.stage]/work_changed.webp"
        scene lisa_work_changed
        lisa "There we go."
        pc "You look good in that outfit."
        lisa "Thank you!"
        "Lisa opens the front door and comes back to talk some more until the customers arrive."
        image lisa_standing_on_chair_workattire = "/lisa/[lisa.stage]/standing_on_chair_workattire.webp"
        scene lisa_standing_on_chair_workattire
        lisa "You know what I'm in the mood for right now?"
        pc "What?"
        lisa "A burger."
        lisa "But eating during work is kind of a no go."
        pc "I don't mind, you can eat as much as you want and I won't tell anyone."
        lisa "Well in that case..."
        "Lisa runs off to make some food."
        image lisa_workattire_eating = "/lisa/[lisa.stage]/workattire_eating.webp"
        scene lisa_workattire_eating
        "After a while you see Lisa in the corner snacking on a burger."
        lisa "Mmm, I needed this soo much."
        if lisa.stage >= 6:
            $ lisa.weight += 1
        else:
            $ lisa.weight += 0.5
        image lisa_idle_workattire = "/lisa/[lisa.stage]/idle_workattire.webp"
        scene lisa_idle_workattire
        lisa "Please don't tell the other girls, they'd think I'm a pig for doing that."
        pc "My lips are sealed."
        call rngbbarrive
        lisa "There is our first customer, let's get to work."
        "You start working."
        return

    elif rngworkgirl == 3:
        image marie_leaning_pillar = "/marie/[marie.stage]/leaning_pillar.webp"
        scene marie_leaning_pillar
        marie "Good morning, sunshine."
        pc "Hey, Marie."
        marie "Looks like it's just us again."
        marie "Just let me get changed, brb."
        image marie_work_changed = "/marie/[marie.stage]/work_changed.webp"
        scene marie_work_changed
        marie "There we go."
        pc "Looking good as always."
        marie "Flatterer."
        "Marie opens the front door and comes back to talk some more until the customers arrive."
        image marie_standing_on_chair_workattire = "/marie/[marie.stage]/standing_on_chair_workattire.webp"
        scene marie_standing_on_chair_workattire
        marie "Ohhh, not again!"
        pc "What is it?"
        marie "I'm craving a burger."
        marie "I wish there wasn't a rule against eating on shift..."
        pc "Hey, I don't mind. Go right ahead, I won't tell anyone."
        marie "You're a lifesaver."
        "Marie runs off to make some food."
        image marie_workattire_eating = "/marie/[marie.stage]/workattire_eating.webp"
        scene marie_workattire_eating
        "After a while you see Marie in the corner snacking on a burger."
        marie "Mmm, so good."
        $ marie.weight += 1
        image marie_idle_workattire = "/marie/[marie.stage]/idle_workattire.webp"
        scene marie_idle_workattire
        marie "Please don't tell the others, I don't need them thinking I'm so greedy I can't resist having a burger for breakfast."
        pc "I won't tell a soul."
        call rngbbarrive
        marie "There is our first customer, let's get to work."
        "You start working."
        return

#The end of the weekend workday, you get to sitdown and talk to 1 of your coworkers.
label work_leave_weekend:
    if sallystage3event == 1 and lunastage10event == 0:
        "After a while, the last customers leave the diner."
        if rngworkgirl == 1:
            image amber_standing_on_chair_workattire = "/amber/[amber.stage]/standing_on_chair_workattire.webp"
            scene amber_standing_on_chair_workattire
            amber "Finally! [playername], could you do me a big favor?"
            amber "I told my friends I would go out with them, but it is already really late."
            amber "Would you want to do the cleanup alone? Then I can still make it."
            pc "Of course, but next time I have something planned you'll have to return the favor."
            amber "Thank you, cya later."
        if rngworkgirl == 2:
            image lisa_standing_on_chair_workattire = "/lisa/[lisa.stage]/standing_on_chair_workattire.webp"
            scene lisa_standing_on_chair_workattire
            lisa "Finally! [playername], could you do me a big favor?"
            lisa "I told my friends I would go out with them, but it is already really late."
            lisa "Would you want to do the cleanup alone? Then I can still make it."
            pc "Of course, but next time I have something planned you'll have to return the favor."
            lisa "Thank you, cya later."
        if rngworkgirl == 3:
            image marie_standing_on_chair_workattire = "/marie/[marie.stage]/standing_on_chair_workattire.webp"
            scene marie_standing_on_chair_workattire
            marie "Finally! [playername], could you do me a big favor?"
            marie "I told my friends I would go out with them, but it is already really late."
            marie "Would you want to do the cleanup alone? Then I can still make it."
            pc "Of course, but next time I have something planned you'll have to return the favor."
            marie "Thank you, cya later."
        call Sally_Stage_3_Event from _call_Sally_Stage_3_Event
        return
    if rngworkgirl == 1:
        if amberstage1event2 == 1:
            call Amber_Stage_1_Event_2 from _call_Amber_Stage_1_Event_2
            return
        if amberstage2event2 == 1 and amber.stage >= 2 and amberstage2event == 0 and teacherstage6event == 0:
            call Amber_Stage_2_Event_2 from _call_Amber_Stage_2_Event_2
            return
        if mayastage3event2 == 1 and mayastage3event == 0:
            call Maya_Stage_3_Event_2 from _call_Maya_Stage_3_Event_2
            return
        if amberstage6event == 1 and amber.stage >= 6 and amberstage5event2 == 0:
            call Amber_Stage_6_Event from _call_Amber_Stage_6_Event
            return

        if amber.stage >= 3:
            ##End of day dialogue - Same for all of them for simplicity but bigger changes in events ###
            #TODO Rework all of Amber's stages to this.#
            image amber_afterwork_sitdown1 = "/amber/[amber.stage]/afterwork_sitdown1.webp"
            scene amber_afterwork_sitdown1
            amber "Another day down."
            pc "A lot of satisfied customers."
            amber "I hope so, we work too hard for them not to be."
            image amber_afterwork_sitdown2 = "/amber/[amber.stage]/afterwork_sitdown2.webp"
            scene amber_afterwork_sitdown2
            amber "Hey, I was wondering if you wanted to get a drink with me tonight?"
            #[Game options - yes / no ]
            menu:
                "Yes":
                    ##If yes###
                    pc "Sure, I'd love to."
                    image amber_afterwork_sitdown3 = "/amber/[amber.stage]/afterwork_sitdown3.webp"
                    scene amber_afterwork_sitdown3
                    amber "Great, let's finish up here first and I need to go home and changed."
                    pc "Meet you there in 30 minutes?"
                    amber "Perfect!"
                    "Quickly cleaning up, you lock up and head home for some fresh clothes too."
                    call Amber_bar_new
                    stop music fadeout 1.0
                    return
                "No":
                    ##If no, return to home##
                    pc "Not today, I am cooked."
                    image amber_afterwork_sitdown4 = "/amber/[amber.stage]/afterwork_sitdown4.webp"
                    scene amber_afterwork_sitdown4
                    amber "Alright, maybe next time."
                    "After a quick cleanup, you lock up and head home."
                    stop music fadeout 1.0
                    return

        else:
            ##Stage 1&2 ###
            ###End of work shift, Amber comes up to us at the till ###
            image amber_afterwork1 = "/amber/[amber.stage]/afterwork1.webp"
            scene amber_afterwork1
            amber "Phew, that was a long day."
            pc "Yeah, pretty busy today. I think we held our own though."
            amber "Definately, but I can't wait to get off my feet and relax."
            amber "The kitchen's about to close if you want to order anything?"
            pc "Nah, I think I've got something at home I can cook."
            image amber_afterwork2 = "/amber/[amber.stage]/afterwork2.webp"
            scene amber_afterwork2
            amber "Ughh, I can't bear the thought of more work."
            amber "I just want to curl up in bed with a movie and not move for like 12 hours."
            amber "Guess we should finish cleaning up here first though."
            image amber_afterwork3 = "/amber/[amber.stage]/afterwork3.webp"
            scene amber_afterwork3
            "Grabbing cleaning supplies, the pair of you get to work cleaning up."
            "Hearing the door to the kitchen open, you spot a couple of burgers on the counter."
            image amber_afterwork4 = "/amber/[amber.stage]/afterwork4.webp"
            scene amber_afterwork4
            pc "Are these yours?"
            amber "Oh yeah, like I said, I can't be bothered to cook tonight."
            image amber_afterwork5 = "/amber/[amber.stage]/afterwork5.webp"
            scene amber_afterwork5
            "Grabbing them Amber sits at a booth."
            amber "You can join me if you want?"
            ###In booth with Amber ###
            image amber_afterwork6 = "/amber/[amber.stage]/afterwork6.webp"
            scene amber_afterwork6
            "Digging into her burgers, Amber relaxes."
            image amber_afterwork7 = "/amber/[amber.stage]/afterwork7.webp"
            scene amber_afterwork7
            amber "Honestly, this is one of the best perks of working here."
            amber "I couldn't imagine working in customer service somewhere that didn't give you food."
            pc "Yeah, it's a nice bonus."
            amber "You did good work today."
            amber "I know you are still a bit new, but you have picked it up quickly."
            pc "Thanks, you all make it so easy."
            if amberstory <= 4 and amber.stage >= 11:
                call amberstoryask
            elif amberstory == 3 and amber.stage >= 9:
                call amberstoryask
            elif amberstory == 2 and amber.stage >= 6:
                call amberstoryask
            elif amberstory == 1 and amber.stage >= 4:
                call amberstoryask
            elif amberstory == 0 and amber.stage >= 2:
                call amberstoryask
            image amber_afterwork8 = "/amber/[amber.stage]/afterwork8.webp"
            scene amber_afterwork8
            "Making small talk for a few minutes, Amber polishes off both burgers quickly."
            image amber_afterwork9 = "/amber/[amber.stage]/afterwork9.webp"
            scene amber_afterwork9
            amber "I needed that, but I guess we better finish up and head home."
            "Cleaning down the tables, you wave goodbye to Amber and head home for the evening."
            $ amber.weight += 0.5
            stop music fadeout 1.0
            return

    if rngworkgirl == 2:
        if lisastage1event2 == 1:
            call Lisa_Stage_1_Event_2 from _call_Lisa_Stage_1_Event_2
            return
        if lisastage2event2 == 1 and lisa.stage >= 2 and lisastage2event == 0:
            call Lisa_Stage_2_Event_2 from _call_Lisa_Stage_2_Event_2
            return
        if lisastage6event == 1 and lisa.stage >= 6 and lisastage5event == 0:
            call Lisa_Stage_6_Event from _call_Lisa_Stage_6_Event
            return
        if lisastage7event == 1 and lisa.stage >= 7 and lisastage6event == 0:
            call Lisa_Stage_7_Event from _call_Lisa_Stage_7_Event
            return
        if lisa.stage >= 7:
            image lisa_idle_workattire = "/lisa/[lisa.stage]/idle_workattire.webp"
            scene lisa_idle_workattire
            lisa "Hey, do you want to hang out like we always do?"
            pc "Yeah, let me grab some food and drinks for us."
            "You get some drinks for both of you and a pizza and a burger for Lisa."
            image lisa_afterwork_sitdown1 = "/lisa/[lisa.stage]/afterwork_sitdown1.webp"
            scene lisa_afterwork_sitdown1
            lisa "Thanks! See this is why I love working with you."
            pc "We do make a great team."
            image lisa_afterwork_sitdown_food1 = "/lisa/[lisa.stage]/afterwork_sitdown_food1.webp"
            scene lisa_afterwork_sitdown_food1
            "Lisa starts chowing down on the pizza while talking about work."
            "She eats the whole thing in a matter of minutes."
            image lisa_afterwork_sitdown3 = "/lisa/[lisa.stage]/afterwork_sitdown3.webp"
            scene lisa_afterwork_sitdown3
            lisa "The pizzas here always taste amazing, I really can't keep my hands off them."
            lisa "But they always make me so thirsty."
            pc "Want a drink?"
            image lisa_afterwork_sitdown_food2 = "/lisa/[lisa.stage]/afterwork_sitdown_food2.webp"
            scene lisa_afterwork_sitdown_food2
            "Lisa quickly grabs her drink."
            "Her drinking doesn't seem to stop until the cup is empty."
            lisa "Ahhh, much better."
            image lisa_afterwork_sitdown7 = "/lisa/[lisa.stage]/afterwork_sitdown7.webp"
            scene lisa_afterwork_sitdown7
            lisa "So I have to ask you something. Am I going too far with this weight gain?"
            pc "No, you look great with a bit more curviness."
            image lisa_afterwork_sitdown5 = "/lisa/[lisa.stage]/afterwork_sitdown5.webp"
            scene lisa_afterwork_sitdown5
            lisa "Let's be honest, it's more than a bit."
            "She looks down at her body."
            image lisa_afterwork_sitdown4 = "/lisa/[lisa.stage]/afterwork_sitdown4.webp"
            scene lisa_afterwork_sitdown4
            lisa "I mean, look at this ass."
            pc "Like I said, you look amazing with some added weight."
            image lisa_afterwork_sitdown2 = "/lisa/[lisa.stage]/afterwork_sitdown2.webp"
            scene lisa_afterwork_sitdown2
            lisa "Well, of course you'd say that, Mr. Chubby Chaser."
            lisa "Not that I mind the attention of course..."
            image lisa_afterwork_sitdown_food3 = "/lisa/[lisa.stage]/afterwork_sitdown_food3.webp"
            scene lisa_afterwork_sitdown_food3
            "Right after she finishes her sentence she grabs a burger."
            "You wonder how much bigger Lisa will get now that she's seemingly given up on self-control."
            image lisa_afterwork_sitdown1 = "/lisa/[lisa.stage]/afterwork_sitdown1.webp"
            scene lisa_afterwork_sitdown1
            lisa "Mmm, delicious."
            $ lisa.weight += 1
            if lisastory <= 3 and lisa.stage >= 9:
                call lisastoryask
            elif lisastory == 2 and lisa.stage >= 6:
                call lisastoryask
            elif lisastory == 1 and lisa.stage >= 4:
                call lisastoryask
            elif lisastory == 0 and lisa.stage >= 2:
                call lisastoryask
            image lisa_afterwork_sitdown6 = "/lisa/[lisa.stage]/afterwork_sitdown6.webp"
            scene lisa_afterwork_sitdown6
            lisa "Do you want to help clean up this place?"
            image lisa_afterwork_sitdown2 = "/lisa/[lisa.stage]/afterwork_sitdown2.webp"
            scene lisa_afterwork_sitdown2
            pc "Yeah, of course."
            "Lisa and you clean up the whole place."
            image lisa_afterwork_sitdown8 = "/lisa/[lisa.stage]/afterwork_sitdown8.webp"
            scene lisa_afterwork_sitdown8
            lisa "Thanks for the help."
            if lisastage4event2 == 0:
                lisa "Do you want to go to the pub together?"
                menu:
                    "Join Lisa at the pub.":
                        pc "Yeah let's go!"
                        lisa "Great, let's meet there in thirty minutes."
                        stop music fadeout 1.0
                        call Lisa_repeatable_pub from _call_Lisa_repeatable_pub
                        return
                    "Go home.":
                        pc "Sorry, I have something else planned."
                        lisa "Oh well, another time then."
                        pc "Have a good evening."
                        "You walk home."
                        stop music fadeout 1.0
                        return
            pc "Have a good evening."
            "You walk home."
            stop music fadeout 1.0
            return
        image lisa_idle_workattire = "/lisa/[lisa.stage]/idle_workattire.webp"
        scene lisa_idle_workattire
        lisa "Hey, do you want to hang out a bit before going home?"
        pc "Of course, I would love to hang out with you, Lisa."
        image lisa_afterwork_sitdown1 = "/lisa/[lisa.stage]/afterwork_sitdown1.webp"
        scene lisa_afterwork_sitdown1
        "Lisa sits down in one of the booths."
        lisa "Ahhh, it's good to be done with work."
        image lisa_afterwork_sitdown2 = "/lisa/[lisa.stage]/afterwork_sitdown2.webp"
        scene lisa_afterwork_sitdown2
        if lisastory <= 3 and lisa.stage >= 9:
            call lisastoryask
        elif lisastory == 2 and lisa.stage >= 6:
            call lisastoryask
        elif lisastory == 1 and lisa.stage >= 4:
            call lisastoryask
        elif lisastory == 0 and lisa.stage >= 2:
            call lisastoryask
        else:
            window hide
            pause
        image lisa_afterwork_sitdown3 = "/lisa/[lisa.stage]/afterwork_sitdown3.webp"
        scene lisa_afterwork_sitdown3
        lisa "Marie and Amber seem quite a bit happier lately."
        pc "Yeah, I noticed."
        image lisa_afterwork_sitdown4 = "/lisa/[lisa.stage]/afterwork_sitdown4.webp"
        scene lisa_afterwork_sitdown4
        lisa "Whenever they are happy, it makes me happy too."
        lisa "And our happiness seems to have an effect on our waistlines too."
        image lisa_afterwork_sitdown5 = "/lisa/[lisa.stage]/afterwork_sitdown5.webp"
        scene lisa_afterwork_sitdown5
        lisa "I think all three of us have been snacking on the fast food a bit too much lately."
        pc "I don't think it's too much, you all could do with some more cushion."
        image lisa_afterwork_sitdown6 = "/lisa/[lisa.stage]/afterwork_sitdown6.webp"
        scene lisa_afterwork_sitdown6
        lisa "Marie keeps telling me the same thing."
        lisa "Would you want to help me clean this place up?"
        pc "Yeah, of course."
        "Lisa and you clean up the whole place."
        image lisa_afterwork_sitdown7 = "/lisa/[lisa.stage]/afterwork_sitdown7.webp"
        scene lisa_afterwork_sitdown7
        lisa "Thanks for the help."
        if lisastage4event2 == 0:
            lisa "Do you want to go to the pub together?"
            menu:
                "Join Lisa at the pub.":
                    pc "Yeah let's go!"
                    lisa "Great, let's meet there in thirty minutes."
                    stop music fadeout 1.0
                    call Lisa_repeatable_pub from _call_Lisa_repeatable_pub_1
                    return
                "Go home.":
                    pc "Sorry, I have something else planned."
                    lisa "Oh well, another time then."
                    pc "Have a good evening."
                    "You walk home."
                    stop music fadeout 1.0
                    return
        pc "No problem, have a good evening."
        stop music fadeout 1.0
        return

    if rngworkgirl == 3:
        if mariestage1event2 == 1 and mariestage1event == 0:
            call Marie_Stage_1_Event_2 from _call_Marie_Stage_1_Event_2
            return
        if marie.stage >= 7:
            image marie_idle_workattire = "/marie/[marie.stage]/idle_workattire.webp"
            scene marie_idle_workattire
            marie "Hey, do you want to hang out like we always do?"
            pc "Yeah. Let me grab some food and drinks for us."
            "You get some drinks for both of you and a pizza and a burger for Marie."
            image marie_afterwork_sitdown1 = "/marie/[marie.stage]/afterwork_sitdown1.webp"
            scene marie_afterwork_sitdown1
            marie "Mmm, friendly, good-looking and you bring me food. Is there anything about you that isn't perfect?"
            pc "Ah, now that would be telling."
            image marie_afterwork_sitdown_food1 = "/marie/[marie.stage]/afterwork_sitdown_food1.webp"
            scene marie_afterwork_sitdown_food1
            "Marie finishes her pizza in a matter of minutes."
            image marie_afterwork_sitdown3 = "/marie/[marie.stage]/afterwork_sitdown3.webp"
            scene marie_afterwork_sitdown3
            marie "God, these pizzas are divine. I just wish they didn't make me so thirsty."
            pc "Drink?"
            image marie_afterwork_sitdown_food2 = "/marie/[marie.stage]/afterwork_sitdown_food2.webp"
            scene marie_afterwork_sitdown_food2
            "Marie quickly grabs her drink."
            "Her drinking doesn't seem to stop until the cup is empty."
            marie "URRRRRRRP, excuse me!"
            image marie_afterwork_sitdown7 = "/marie/[marie.stage]/afterwork_sitdown7.webp"
            scene marie_afterwork_sitdown7
            marie "Hey, do you think I've gained a bit too much?"
            pc "Not at all. You look great."
            image marie_afterwork_sitdown5 = "/marie/[marie.stage]/afterwork_sitdown5.webp"
            scene marie_afterwork_sitdown5
            marie "Really? Not even a bit?"
            "She says while showing her body."
            image marie_afterwork_sitdown4 = "/marie/[marie.stage]/afterwork_sitdown4.webp"
            scene marie_afterwork_sitdown4
            marie "I mean, I'm getting seriously thicc."
            pc "Like I said, you look amazing with some added weight."
            image marie_afterwork_sitdown2 = "/marie/[marie.stage]/afterwork_sitdown2.webp"
            scene marie_afterwork_sitdown2
            marie "Well, you are biased."
            pc "And you aren't?"
            marie "Haha fair. I do look pretty damn sexy, I just never figured I'd be the one getting fat."
            if mariestory <= 3 and marie.stage >= 9:
                call mariestoryask
            elif mariestory == 2 and marie.stage >= 6:
                call mariestoryask
            elif mariestory == 1 and marie.stage >= 4:
                call mariestoryask
            elif mariestory == 0 and marie.stage >= 2:
                call mariestoryask
            image marie_afterwork_sitdown_food3 = "/marie/[marie.stage]/afterwork_sitdown_food3.webp"
            scene marie_afterwork_sitdown_food3
            "Right after she finishes her sentence, she grabs a burger."
            "It seems ridiculous to you that Marie never considered that she'd get fat considering how greedy she is, but you humor her."
            image marie_afterwork_sitdown1 = "/marie/[marie.stage]/afterwork_sitdown1.webp"
            scene marie_afterwork_sitdown1
            marie "Well, this has been fun, but I think it's time to go home and stuff myself silly."
            marie "All this fast food makes me want to feel bloated."
            $ marie.weight += 2
            image marie_afterwork_sitdown6 = "/marie/[marie.stage]/afterwork_sitdown6.webp"
            scene marie_afterwork_sitdown6
            marie "Would you want to join me?"
            menu:
                "Join Marie at her home.":
                    pc "Yeah let's go!"
                    image marie_afterwork_sitdown2 = "/marie/[marie.stage]/afterwork_sitdown2.webp"
                    scene marie_afterwork_sitdown2
                    marie "Before I go I have to clean up the rest and go put on some better clothes."
                    marie "Would you want to help me clean this place up?"
                    pc "Yeah, of course."
                    "Marie and you clean up the whole place."
                    image marie_afterwork_sitdown8 = "/marie/[marie.stage]/afterwork_sitdown8.webp"
                    scene marie_afterwork_sitdown8
                    marie "Thanks for the help."
                    marie "Meet in thirty minutes at my home?"
                    pc "Yes, see you there."
                    stop music fadeout 1.0
                    call marie_home from _call_marie_home_1
                "Go home.":
                    pc "Sorry, I have something else planned."
                    image marie_afterwork_sitdown2 = "/marie/[marie.stage]/afterwork_sitdown2.webp"
                    scene marie_afterwork_sitdown2
                    marie "That's fine, do you want to help clean up this place?"
                    pc "Yeah, of course."
                    "Marie and you clean up the whole place."
                    image marie_afterwork_sitdown8 = "/marie/[marie.stage]/afterwork_sitdown8.webp"
                    scene marie_afterwork_sitdown8
                    marie "Thanks for the help."
                    pc "Have a good evening."
                    "You walk home."
                    stop music fadeout 1.0
                    if mariestage7phone == 1:
                        scene player_room
                        "After a while you receive a message from Marie."
                        call MarieStage7Phone
            return
        image marie_idle_workattire = "/marie/[marie.stage]/idle_workattire.webp"
        scene marie_idle_workattire
        marie "Hey, do you want to hang out a bit before going home?"
        pc "Of course. I'd love to hang out with you, Marie."
        image marie_afterwork_sitdown1 = "/marie/[marie.stage]/afterwork_sitdown1.webp"
        scene marie_afterwork_sitdown1
        "Marie sits down in one of the booths."
        marie "Finally done working."
        if mariestory <= 3 and marie.stage >= 9:
            call mariestoryask
        elif mariestory == 2 and marie.stage >= 6:
            call mariestoryask
        elif mariestory == 1 and marie.stage >= 4:
            call mariestoryask
        elif mariestory == 0 and marie.stage >= 2:
            call mariestoryask
        image marie_afterwork_sitdown2 = "/marie/[marie.stage]/afterwork_sitdown2.webp"
        scene marie_afterwork_sitdown2
        marie "How are the girls eating lately?"
        pc "They've been chowing down on fast food a lot more lately."
        image marie_afterwork_sitdown3 = "/marie/[marie.stage]/afterwork_sitdown3.webp"
        scene marie_afterwork_sitdown3
        marie "That's good, please keep encouraging them."
        marie "I'll do the same."
        image marie_afterwork_sitdown4 = "/marie/[marie.stage]/afterwork_sitdown4.webp"
        scene marie_afterwork_sitdown4
        marie "I also noticed some of our customers plumping up."
        marie "I guess that is your doing?"
        pc "I support their gains, yeah."
        image marie_afterwork_sitdown5 = "/marie/[marie.stage]/afterwork_sitdown5.webp"
        scene marie_afterwork_sitdown5
        marie "Great work, it really makes me horny to see all these customers slowly getting fatter."
        marie "You working here is the best thing that happened to Bunny Bites."
        pc "Thank you."
        image marie_afterwork_sitdown6 = "/marie/[marie.stage]/afterwork_sitdown6.webp"
        scene marie_afterwork_sitdown6
        if mariestage2event == 0:
            marie "On that note would you want to come to my home to see me stuff myself with liquid?"
            marie "Maybe even have some sexy times together?"
            menu:
                "Absolutely.":
                    pc "Absolutely."
                    marie "Great, let's first clean up this place."
                    "Marie and you clean up the whole place."
                    image marie_afterwork_sitdown7 = "/marie/[marie.stage]/afterwork_sitdown7.webp"
                    scene marie_afterwork_sitdown7
                    marie "I first have to clean up my place a bit, could you come in like fifteen minutes?"
                    pc "No problem, see you there in fifteen."
                    stop music fadeout 1.0
                    if mariestage4event == 1 and mariestage3event2 == 0 and marie.stage >= 4:
                        call Marie_Stage_4_Event_1
                    else:
                        call marie_home from _call_marie_home
                    return
                "I had something else planned for tonight.":
                    pc "I had something else planned for tonight."
                    marie "Your loss, I'll just have to do it all myself then."
                    marie "Would you want to help me clean this place up?"
                    pc "Yeah, of course."
                    "Marie and you clean up the whole place."
                    image marie_afterwork_sitdown7 = "/marie/[marie.stage]/afterwork_sitdown7.webp"
                    scene marie_afterwork_sitdown7
                    marie "Thanks for the help."
                    pc "No problem, have a good evening."
                    marie "You too!"
                    stop music fadeout 1.0
                    return
        marie "Would you want to help me clean this place up?"
        pc "Yeah, of course."
        "Marie and you clean up the whole place."
        image marie_afterwork_sitdown7 = "/marie/[marie.stage]/afterwork_sitdown7.webp"
        scene marie_afterwork_sitdown7
        marie "Thanks for the help."
        pc "No problem, have a good evening."
        marie "You too!"
        stop music fadeout 1.0
        return

label work_snack:
    $ rng = renpy.random.randint(1,100)
    if rng >= 50:
        if amberstage4event == 0 and rngworkgirl == 1:
            "After a while the customers leave and you get a moment to breathe."
            "You decide to clean a couple of tables to help out Amber."
            image amber_work_snack1 = "/amber/[amber.stage]/work_snack1.webp"
            scene amber_work_snack1
            amber "Hey, [playername]. Can I have that burrito?"
            "You realize that there is a completely untouched burrito on the table you are cleaning."
            pc "Sure. Open your mouth."
            image amber_work_snack2 = "/amber/[amber.stage]/work_snack2.webp"
            scene amber_work_snack2
            "Amber opens her mouth and waits for you to feed her the burrito."
            "As if she hadn't eaten in days she started munching."
            image amber_work_snack3 = "/amber/[amber.stage]/work_snack3.webp"
            scene amber_work_snack3
            "Her appetite has certainly grown."
            "You wonder how much food her growing belly can now hold."
            $ amber.weight += 0.2
        elif amberstage4event == 0 and rngworkgirl == 2 and lisa.stage >= 4:
            "After a while the customers leave and you get a moment to breathe."
            "You decide to clean a couple tables to help out Lisa."
            image lisa_work_snack1 = "/lisa/[lisa.stage]/work_snack1.webp"
            scene lisa_work_snack1
            lisa "Hey, [playername], is that an untouched hotdog just sitting there?"
            "You realize that there is indeed a fully pristine hotdog on the table you are cleaning."
            pc "Yes. Do you want it?"
            lisa "Feed it to me!"
            image lisa_work_snack2 = "/lisa/[lisa.stage]/work_snack2.webp"
            scene lisa_work_snack2
            "Lisa opens her mouth and waits for you to feed her the hotdog."
            "She seems to do her best to keep gaining for Marie."
            image lisa_work_snack3 = "/lisa/[lisa.stage]/work_snack3.webp"
            scene lisa_work_snack3
            "You wonder how much she has already eaten today."
            "Lisa's love for Marie has certainly had an impact on her figure."
            $ lisa.weight += 0.2
    return
