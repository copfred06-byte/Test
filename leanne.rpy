label leanne_stream:
    if leanne.weight >= 57 and leannestage2event2 == 1:
        call Leanne_Stage_2_Event_2 from _call_Leanne_Stage_2_Event_2
        $ daytime += 1
        jump freetime
    elif leanne.stage >= 4 and leannestage4event == 1:
        call Leanne_Stage_4_Event_1
        $ daytime += 1
        jump freetime
    elif leanne.stage >= 4 and leannestage4event == 0 and leannestage4event2 == 1:
        call Leanne_Stage_4_Event_2 from _call_Leanne_Stage_4_Event_2
        $ daytime += 1
        jump freetime
    elif leanne.stage >= 5 and leannestage5event == 1:
        call Leanne_Stage_5_Event_1
        $ daytime += 1
        jump freetime
    elif leanne.stage >= 5 and leannestage5event == 0 and leannestage5event2 == 1:
        call Leanne_Stage_5_Event_2
        $ daytime += 1
        jump freetime
    elif leanne.stage >= 6 and leannestage6event == 0 and leannestage6event2 == 1:
        call Leanne_Stage_6_Event_2 from _call_Leanne_Stage_6_Event_2
        $ daytime += 1
        jump freetime
    elif leanne.weight >= 100 and leannestage11event2 == 1:
        call Leanne_Stage_11_Event_2
        $ daytime += 1
        jump freetime
    elif leanne.stage >= 12 and leannestage12event3 == 1 and leannestage12event2 == 0:
        call Leanne_Stage_12_Event_3 from _call_Leanne_Stage_12_Event_3
        $ daytime += 1
        jump freetime
    elif leanne.stage >= 11 and leannestage11event2 == 0:
        "The webpage shows me that this user is banned from streaming."
        pc "FeelsBadMan"
        jump freetime
    else:
        "You go check who is online."
        pc "Nice, Leanne is live."
        image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
        scene stream_girl_webcam
        $ rng = renpy.random.randint(1,2)
        play music "/music/leanne_stream.ogg" if_changed
        window hide
        pause
        leanne "Hey viewers! Luxury Leanne here back to play some games. Remember, I take special pizza donations. If you order one, I'll eat it on camera."
        "Should you donate to her?"
        menu:
            "Yes, I will buy her a pizza. (-$5)":
                if money <= 4:
                    "You do not have enough money to buy Leanne a pizza, you can earn money by working at the restaurant."
                    image stream_girl_side = "/leanne/[leanne.stage]/side.webp"
                    scene stream_girl_side
                    leanne "Let's play some more Carl on Duty."
                    image stream_girl_gaming = "/leanne/[leanne.stage]/gaming.webp"
                    scene stream_girl_gaming
                    pc "You watch her play until it's time to go to bed."
                    stop music fadeout 1.0
                    $ daytime += 1
                    jump freetime
                elif leannestage1event == 1:
                    call Leanne_Stage_1_Event from _call_Leanne_Stage_1_Event
                    stop music fadeout 1.0
                    $ daytime += 1
                    jump freetime
                elif leannestage2event == 1 and leanne.stage >= 2:
                    call Leanne_Stage_2_Event_1
                    stop music fadeout 1.0
                    $ daytime += 1
                    jump freetime
                else:
                    image stream_girl_happy = "/leanne/[leanne.stage]/happy.webp"
                    scene stream_girl_happy
                    $ money -= 5
                    leanne "Nice, someone made a pizza donation. Thank you so much! I'll order right away."
                    "About ten minutes later the pizza arrives."
                    image stream_girl_pizza = "/leanne/[leanne.stage]/pizza.webp"
                    scene stream_girl_pizza
                    "Opening up the box, she devours the entire thing like she hasn't eaten all day."
                    $ leanne.weight += 0.5
                    image stream_girl_happy = "/leanne/[leanne.stage]/happy.webp"
                    scene stream_girl_happy
                    leanne "That really hit the spot. Thanks again for the donation. Now for your reward: the pizza celebration dance!"
                    image leanne_standup = "/leanne/[leanne.stage]/standup.webp"
                    scene leanne_standup
                    window hide
                    pause
                    image leanne_standupside = "/leanne/[leanne.stage]/standup_side.webp"
                    scene leanne_standupside
                    pause
                    image leanne_standing = "/leanne/[leanne.stage]/standing.webp"
                    scene leanne_standing
                    pause
                    call leanne_dance from _call_leanne_dance
                    image stream_girl_side = "/leanne/[leanne.stage]/side.webp"
                    scene stream_girl_side
                    pause
                    image stream_girl_gaming = "/leanne/[leanne.stage]/gaming.webp"
                    scene stream_girl_gaming
                    "You watch her play until it's time to go to bed."
                    stop music fadeout 1.0
                    $ daytime += 1
                    jump freetime

            "Buy Leanne five pizzas (-$25)" if leannestage4event2 == 0:
                if money <= 24:
                    "You do not have enough money to buy Leanne 5 pizzas, you can earn money by working at the restaurant."
                    image stream_girl_side = "/leanne/[leanne.stage]/side.webp"
                    scene stream_girl_side
                    leanne "Let's play some more Carl on Duty."
                    image stream_girl_gaming = "/leanne/[leanne.stage]/gaming.webp"
                    scene stream_girl_gaming
                    pc "You watch her play until it's time to go to bed."
                    stop music fadeout 1.0
                    $ daytime += 1
                    jump freetime
                elif leanne.stage >= 10:
                    $ money -= 25
                    image stream_girl_happy = "/leanne/[leanne.stage]/happy.webp"
                    scene stream_girl_happy
                    leanne "Thank you soooooooooo much. I'll go ahead and order the pizzas right away. While I'm waiting for that though, I think it's time I give you a prize."
                    image leanne_standup = "/leanne/[leanne.stage]/standup.webp"
                    scene leanne_standup
                    window hide
                    pause
                    image leanne_standupside = "/leanne/[leanne.stage]/standup_side.webp"
                    scene leanne_standupside
                    window hide
                    pause
                    image leanne_standing = "/leanne/[leanne.stage]/standing.webp"
                    scene leanne_standing
                    window hide
                    pause
                    ##(Player chooses between the dances or exericse)
                    call leanne_dance2 from _call_leanne_dance2
                    image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                    scene stream_girl_webcam
                    leanne "Hope you liked it. Oh, and just in time too."
                    image stream_girl_pizzastack = "/leanne/[leanne.stage]/pizzastack.webp"
                    scene stream_girl_pizzastack
                    "Leanne walks offscreen for a moment, only to come back with her arms burdened with five pizza boxes."
                    "Wasting little time, she opens up the first box and scarfs down the slices as fast as possible."
                    image stream_girl_eating = "/leanne/[leanne.stage]/eating.webp"
                    scene stream_girl_eating
                    leanne "Mmm, as good as always. I'll work on the rest of these as we play."
                    image stream_girl_gaming = "/leanne/[leanne.stage]/gaming.webp"
                    scene stream_girl_gaming
                    "The game moves at a snail's pace as Leanne works through her collection of pizza. Multiple times she has to pause the game to force down another slice."
                    image stream_girl_eating2 = "/leanne/[leanne.stage]/eating2.webp"
                    scene stream_girl_eating2
                    pause
                    image stream_girl_eating3 = "/leanne/[leanne.stage]/eating3.webp"
                    scene stream_girl_eating3
                    "Though towards the end it's obvious she's struggling. There is a fire in her eyes that keeps her going until the very end of the stream."
                    "With one hand balanced on her swollen belly, she uses the other to push the last slice past her lips."
                    image stream_girl_stuffed_unhappy = "/leanne/[leanne.stage]/stuffed_unhappy.webp"
                    scene stream_girl_stuffed_unhappy
                    "Though she tries to smile, the moment of triumph is hindered by a look of discomfort."
                    leanne "Oof, I did it. All thanks to your-"
                    image stream_girl_burp = "/leanne/[leanne.stage]/burp.webp"
                    scene stream_girl_burp with vpunch
                    leanne "UUURRP help."
                    image stream_girl_ashamed = "/leanne/[leanne.stage]/ashamed.webp"
                    scene stream_girl_ashamed
                    "She covers her face for a moment as she watches the chat erupt in response."
                    leanne "Whoops, sorry about that. Kind of just slipped out. Anyway, I think that's going to be it for me tonight. This is Luxury Leanne signing off."
                    image stream_girl_stuffed_goodbye2 = "/leanne/[leanne.stage]/stuffed_goodbye2.webp"
                    scene stream_girl_stuffed_goodbye2
                    "Standing up from her seat with a hand cradling her gut, she lets the chat admire her overstuffed belly for a few seconds before she turns off the feed."
                    $ leanne.weight += 1.5
                    stop music fadeout 1.0
                    $ daytime += 1
                    jump freetime
                elif leanne.stage >= 7:
                    $ money -= 25
                    image stream_girl_happy = "/leanne/[leanne.stage]/happy.webp"
                    scene stream_girl_happy
                    leanne "Thank you soooooooooo much. I'll go ahead and order the pizzas right away. While I'm waiting for that though, I think it's time I give you a prize."
                    image leanne_standup = "/leanne/[leanne.stage]/standup.webp"
                    scene leanne_standup
                    window hide
                    pause
                    image leanne_standupside = "/leanne/[leanne.stage]/standup_side.webp"
                    scene leanne_standupside
                    window hide
                    pause
                    image leanne_standing = "/leanne/[leanne.stage]/standing.webp"
                    scene leanne_standing
                    window hide
                    pause
                    ##(Player chooses between the dances or exericse)
                    call leanne_dance2 from _call_leanne_dance2_1
                    image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                    scene stream_girl_webcam
                    leanne "Hope you liked it. Oh, and just in time too."
                    image stream_girl_pizzastack = "/leanne/[leanne.stage]/pizzastack.webp"
                    scene stream_girl_pizzastack
                    "Leanne walks offscreen for a moment, only to come back with her arms burdened with five pizza boxes."
                    "Wasting little time, she opens up the first box and scarfs down the slices as fast as possible."
                    image stream_girl_eating = "/leanne/[leanne.stage]/eating.webp"
                    scene stream_girl_eating
                    leanne "Mmmmm, as good as always. I'll work on the rest of these as we play."
                    image stream_girl_gaming = "/leanne/[leanne.stage]/gaming.webp"
                    scene stream_girl_gaming
                    "The stream is made a little more awkward as Leanne struggles through her pizza."
                    "Pausing multiple times to help force down the slices with a swig of soda, she manages to push herself all the way to the end of the stream."
                    "Her efforts allow her to finish off the fourth pizza just as things are winding down."
                    image stream_girl_eating2 = "/leanne/[leanne.stage]/eating2.webp"
                    scene stream_girl_eating2
                    pause
                    image stream_girl_eating3 = "/leanne/[leanne.stage]/eating3.webp"
                    scene stream_girl_eating3
                    pause
                    image stream_girl_stuffed_happy = "/leanne/[leanne.stage]/stuffed_happy.webp"
                    scene stream_girl_stuffed_happy
                    leanne "Woo, that was a lot!"
                    image stream_girl_stuffed = "/leanne/[leanne.stage]/stuffed.webp"
                    scene stream_girl_stuffed
                    pause
                    image stream_girl_stuffed2 = "/leanne/[leanne.stage]/stuffed2.webp"
                    scene stream_girl_stuffed2
                    "She stands up to cradle her belly like a pregnant woman."
                    image stream_girl_stuffed3 = "/leanne/[leanne.stage]/stuffed3.webp"
                    scene stream_girl_stuffed3
                    leanne "Next time I'll see if I can get through all five. Until then, this is Luxury Leanne signing off."
                    image stream_girl_stuffed_goodbye = "/leanne/[leanne.stage]/stuffed_goodbye.webp"
                    scene stream_girl_stuffed_goodbye
                    "The stream ends."
                    $ leanne.weight += 1.5
                    stop music fadeout 1.0
                    $ daytime += 1
                    jump freetime
                else:
                    image stream_girl_happy = "/leanne/[leanne.stage]/happy.webp"
                    scene stream_girl_happy
                    "Leanne pauses the stream to show off a wide smile."
                    $ money -= 25
                    leanne "Thank you soooooooooo much. I'll go ahead and order the pizzas right away. While I'm waiting for that though, I think it's time I give you a prize."
                    image leanne_standup = "/leanne/[leanne.stage]/standup.webp"
                    scene leanne_standup
                    window hide
                    pause
                    image leanne_standupside = "/leanne/[leanne.stage]/standup_side.webp"
                    scene leanne_standupside
                    pause
                    image leanne_standing = "/leanne/[leanne.stage]/standing.webp"
                    scene leanne_standing
                    pause
                    ##(Animation: Dance 2 plays)
                    call leanne_dance2 from _call_leanne_dance2_2
                    image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
                    scene stream_girl_webcam
                    leanne "Hope you liked it. Oh, and just in time too."
                    image stream_girl_pizzastack = "/leanne/[leanne.stage]/pizzastack.webp"
                    scene stream_girl_pizzastack
                    "Leanne walks offscreen for a moment, only to come back with her arms burdened with five pizza boxes."
                    "Wasting little time, she opens up the first box and scarfs down the slices as fast as possible."
                    image stream_girl_eating = "/leanne/[leanne.stage]/eating.webp"
                    scene stream_girl_eating
                    leanne "Hmmm, as good as always. I'll work on the rest of these as we play."
                    image stream_girl_gaming = "/leanne/[leanne.stage]/gaming.webp"
                    scene stream_girl_gaming
                    "The stream goes as usual, albeit with more frequent breaks to allow Leanne to eat more pizza."
                    "Towards the end of the night, her eating slows down. However, she manages to get through pizza number three before she has to give up."
                    image stream_girl_eating2 = "/leanne/[leanne.stage]/eating2.webp"
                    scene stream_girl_eating2
                    pause
                    image stream_girl_stuffed = "/leanne/[leanne.stage]/stuffed.webp"
                    scene stream_girl_stuffed
                    leanne "I think that's going to do it for me tonight."
                    image stream_girl_stuffed2 = "/leanne/[leanne.stage]/stuffed2.webp"
                    scene stream_girl_stuffed2
                    "Leanne leans back, showing her stuffed tummy."
                    image stream_girl_stuffed3 = "/leanne/[leanne.stage]/stuffed3.webp"
                    scene stream_girl_stuffed3
                    leanne "Sorry I couldn't finish all of it. I'll try to finish off the rest later. Until next time, this is Luxury Leanne signing off."
                    image stream_girl_stuffed_goodbye = "/leanne/[leanne.stage]/stuffed_goodbye.webp"
                    scene stream_girl_stuffed_goodbye
                    "The stream ends."
                    $ leanne.weight += 1.5
                    stop music fadeout 1.0
                    $ daytime += 1
                    jump freetime

            "No, I will just watch.":
                image stream_girl_side = "/leanne/[leanne.stage]/side.webp"
                scene stream_girl_side
                leanne "Let's play some more Carl on Duty."
                image stream_girl_gaming = "/leanne/[leanne.stage]/gaming.webp"
                scene stream_girl_gaming
                pc "You watch her play until it's time to go to bed."
                $ leanne.weight += 0.1
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime

label leanne_stream2:
    if leanne.stage >= 13 and leannestage13event == 0 and leannestage13event2 == 1:
        call Leanne_Stage_13_Event_2 from _call_Leanne_Stage_13_Event_2
        $ daytime += 1
        jump freetime
    image Leanne_webcam = "/leanne/[leanne.stage]/Leanne_webcam.webp"
    scene Leanne_webcam
    $ rng = renpy.random.randint(1,2)
    play music "/music/leanne_stream.ogg" if_changed
    "You decide to watch Leanne's stream."
    leanne "Hey, everyone! This is Luxury Leanne. Today will be another session of Carl on Duty. Let's jump right on in and have some fun."
    image Leanne_side = "/leanne/[leanne.stage]/Leanne_side.webp"
    scene Leanne_side
    "Will you donate?"
    #CHOICE: A) No, just watch, B) Donate a single pizza (-$5), or C) Donate five pizzas (-$25)
    menu:
        "No, just watch.":
            image Leanne_gaming = "/leanne/[leanne.stage]/Leanne_gaming.webp"
            scene Leanne_gaming
            "You watch Leanne stream for a bit. Between light hearted commentary with the chat, she absolutely destroys most of the opponents she faces."
            "Her various victories and impressive display of skill are accompanied with a number of jokes and quips from her to keep her viewers entertained."
            "She manages to keep up this energy up until the very end of the stream."
            image Leanne_goodbye = "/leanne/[leanne.stage]/Leanne_goodbye.webp"
            scene Leanne_goodbye
            leanne "Think that's going to do it for me tonight. Until next time, this is Luxury Leanne signing off!"
            "The stream ends."
            $ leanne.weight += 0.1
            stop music fadeout 1.0
            $ daytime += 1
            jump freetime
        "Donate a single pizza. (-$5)":
            if money <= 4:
                "You do not have enough money to buy Leanne 5 pizzas. You can earn money by working at the diner."
                image Leanne_gaming = "/leanne/[leanne.stage]/Leanne_gaming.webp"
                scene Leanne_gaming
                "You watch Leanne stream for a bit. Between light hearted commentary with the chat, she absolutely destroys most of the opponents she faces."
                "Her various victories and impressive display of skill are accompanied with a number of jokes and quips from her to keep her viewers entertained."
                "She manages to keep up this energy up until the very end of the stream."
                image Leanne_goodbye = "/leanne/[leanne.stage]/Leanne_goodbye.webp"
                scene Leanne_goodbye
                leanne "Think that's going to do it for me tonight. Until next time, this is Luxury Leanne signing off!"
                "The stream ends."
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime
            $ money -= 5
            image Leanne_smile = "/leanne/[leanne.stage]/Leanne_smile.webp"
            scene Leanne_smile
            leanne "Thanks for the pizza. I'll order it right away."
            image Leanne_pizzabox = "/leanne/[leanne.stage]/Leanne_pizzabox.webp"
            scene Leanne_pizzabox
            "About ten minutes later, a pizza arrives at the door."
            image Leanne_pizza1 = "/leanne/[leanne.stage]/Leanne_pizza1.webp"
            scene Leanne_pizza1
            "Bringing the box over to her desk, Leanne proceeds to devour the entire thing as if it was a small snack to her."
            image Leanne_goodbye = "/leanne/[leanne.stage]/Leanne_goodbye.webp"
            scene Leanne_goodbye
            leanne "There, that should keep me going. Thanks again, loyal viewer."
            "You watch the rest of the stream until she finishes up her gaming session and then you head to bed."
            $ leanne.weight += 0.5
            stop music fadeout 1.0
            $ daytime += 1
            jump freetime
        "Donate five pizzas. (-$25)":
            if money <= 24:
                "You do not have enough money to buy Leanne 5 pizzas. You can earn money by working at the diner."
                image Leanne_gaming = "/leanne/[leanne.stage]/Leanne_gaming.webp"
                scene Leanne_gaming
                "You watch Leanne stream for a bit. Between light hearted commentary with the chat, she absolutely destroys most of the opponents she faces."
                "Her various victories and impressive display of skill are accompanied with a number of jokes and quips from her to keep her viewers entertained."
                "She manages to keep up this energy up until the very end of the stream."
                image Leanne_goodbye = "/leanne/[leanne.stage]/Leanne_goodbye.webp"
                scene Leanne_goodbye
                leanne "Think that's going to do it for me tonight. Until next time, this is Luxury Leanne signing off!"
                "The stream ends."
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime
            $ money -= 25
            image Leanne_smile = "/leanne/[leanne.stage]/Leanne_smile.webp"
            scene Leanne_smile
            leanne "Wow, really? That's awesome! Pizzas have been ordered. All that's left is to pass the time with a little fun."
            image Leanne_standing = "/leanne/[leanne.stage]/Leanne_standing.webp"
            scene Leanne_standing
            
            if leanne.stage <= 13:
                leanne "Okay, lucky viewer, what would you like me to do?"
                menu:
                    "Dance.":
                        "Starting up a royalty free song on her speaker, Leanne begins to dance around to the rhythm of the beat."
                        if leanne.stage == 12:
                            $ renpy.movie_cutscene("/images/leanne/12/Leanne_dance.webm", stop_music=False)
                        elif leanne.stage == 13:
                            $ renpy.movie_cutscene("/images/leanne/13/Leanne_dance.webm", stop_music=False)
                        window hide
                        pause
                        "Through the constant shaking of her body, she proves how comfortable she is showing off how she can swing her extra weight around."
                    "Exercise.":
                        "Though there's a momentary look of hesitation, Leanne eventually starts her exercise routine."
                        if leanne.stage == 12:
                            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                            play movie "/images/leanne/12/Leanne_exercise.webm" loop
                            show movie with dissolve
                        elif leanne.stage == 13:
                            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                            play movie "/images/leanne/13/Leanne_exercise.webm" loop
                            show movie with dissolve
                        "In a matter of moments sweat begins to bead down her pudgy flesh."
                        window hide
                        pause
                        "She struggles to get through the routine, but she remains motivated from the reactions she receives from the chat."
                        stop movie

            else:
                "Leanne stands up, giving the stream a good view of her full body."
                image Leanne_bellydrop = "/leanne/[leanne.stage]/Leanne_bellydrop.webp"
                scene Leanne_bellydrop
                "She lifts up her belly with both hands."
                if leanne.stage == 14:
                    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                    play movie "/images/leanne/14/Leanne_bellydrop_1.webm" loop
                    show movie with dissolve
                    window hide
                    pause
                    stop movie
                    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                    play movie "/images/leanne/14/Leanne_bellydrop_2.webm" loop
                    show movie with dissolve
                    window hide
                    pause
                    stop movie
                elif leanne.stage == 15:
                    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                    play movie "/images/leanne/15/Leanne_bellydrop_1.webm" loop
                    show movie with dissolve
                    window hide
                    pause
                    stop movie
                    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                    play movie "/images/leanne/15/Leanne_bellydrop_2.webm" loop
                    show movie with dissolve
                    window hide
                    pause
                    stop movie

            image Leanne_towel = "/leanne/[leanne.stage]/Leanne_towel.webp"
            scene Leanne_towel
            leanne "Hope you enjoyed it. I know I did. Ah, looks like the pizzas just arrived. Hang on a sec and I'll be right back."
            image Leanne_pizzastack = "/leanne/[leanne.stage]/Leanne_pizzastack.webp"
            scene Leanne_pizzastack
            leanne "Mmmm, so good. I'll chow down on these as I play."
            image Leanne_pizza2 = "/leanne/[leanne.stage]/Leanne_pizza2.webp"
            scene Leanne_pizza2
            "Despite how focused she appears to be in absolutely destroying the greasy meal, her gaming skill remains consistently impressive."
            image Leanne_pizza3 = "/leanne/[leanne.stage]/Leanne_pizza3.webp"
            scene Leanne_pizza3
            "She eagerly downs each slice like she's on the brink of starvation. One after another the boxes are emptied out as her belly fills up."
            image Leanne_stuffed1 = "/leanne/[leanne.stage]/Leanne_stuffed1.webp"
            scene Leanne_stuffed1
            "Finishing up the last slice, Leanne leans back in her seat as she absentmindedly rubs her overstuffed stomach."
            image Leanne_stuffed2 = "/leanne/[leanne.stage]/Leanne_stuffed2.webp"
            scene Leanne_stuffed2
            leanne "Nothing like gaming and good UUURRP pizza to close out the night."
            image Leanne_stuffed3 = "/leanne/[leanne.stage]/Leanne_stuffed3.webp"
            scene Leanne_stuffed3
            leanne "Catch you all later. This is Luxury Leanne signing off."
            "The stream ends."
            $ leanne.weight += 1.5
            stop music fadeout 1.0
            $ daytime += 1
            jump freetime

label lyn_stream:
    if leanne.stage >= 13 and leannestage13event == 0 and leannestage13event2 == 1:
        call Leanne_Stage_13_Event_2 from _call_Leanne_Stage_13_Event_2_1
        $ daytime += 1
        jump freetime
    #Scene: Lyn Regular Gaming Stream
    #Image: Lyn sitting at her desk.
    image Lyn_webcam = "/leanne/[leanne.stage]/Lyn_webcam.webp"
    scene Lyn_webcam
    $ rng = renpy.random.randint(1,2)
    play music "/music/leanne_stream2.ogg" if_changed
    "You decide to watch Lyn's stream."
    leanne "Hello, everyone, and welcome to the stream. Today I'll be playing some Carl on Duty. I hope you enjoy."
    image Lyn_side = "/leanne/[leanne.stage]/Lyn_side.webp"
    scene Lyn_side
    "Will you donate?"
    #CHOICE: A) No, just watch, B) Donate a single pizza (-$5), or C) Donate five pizzas (-$25)
    menu:
        "No, just watch.":
            image Lyn_gaming = "/leanne/[leanne.stage]/Lyn_gaming.webp"
            scene Lyn_gaming
            "You watch Lyn stream for a bit."
            "Though she seems to struggle a lot more than she used to, the presence of the chat is more than enough to keep her spirits up through each loss over the course of the session."
            image Lyn_goodbye = "/leanne/[leanne.stage]/Lyn_goodbye.webp"
            scene Lyn_goodbye
            leanne "That'll do it for me tonight. Thank you everyone for watching. See you next time!"
            "The stream ends."
            $ leanne.weight += 0.1
            stop music fadeout 1.0
            $ daytime += 1
            jump freetime
        "Donate a single pizza. (-$5)":
            if money <= 4:
                "You do not have enough money to buy Lyn 5 pizzas. You can earn money by working at the diner."
                image Lyn_gaming = "/leanne/[leanne.stage]/Lyn_gaming.webp"
                scene Lyn_gaming
                "You watch Lyn stream for a bit."
                "Though she seems to struggle a lot more than she used to, the presence of the chat is more than enough to keep her spirits up through each loss over the course of the session."
                image Lyn_goodbye = "/leanne/[leanne.stage]/Lyn_goodbye.webp"
                scene Lyn_goodbye
                leanne "That'll do it for me tonight. Thank you everyone for watching. See you next time!"
                "The stream ends."
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime
            $ money -= 5
            image Lyn_happy = "/leanne/[leanne.stage]/Lyn_happy.webp"
            scene Lyn_happy
            leanne "Thank you for the donation. I'll go ahead and order the pizza right away."
            image Lyn_pizzabox = "/leanne/[leanne.stage]/Lyn_pizzabox.webp"
            scene Lyn_pizzabox
            "About ten minutes later, a pizza arrives at the door."
            image Lyn_pizza1 = "/leanne/[leanne.stage]/Lyn_pizza1.webp"
            scene Lyn_pizza1
            "Bringing the box over to her desk, Lyn proceeds to devour the entire thing as if it was a small snack to her."
            image Lyn_goodbye = "/leanne/[leanne.stage]/Lyn_goodbye.webp"
            scene Lyn_goodbye
            leanne "That was a nice treat. Thank you again."
            "You watch the rest of the stream until she finishes up her gaming session and then head to bed."
            $ leanne.weight += 0.5
            stop music fadeout 1.0
            $ daytime += 1
            jump freetime
        "Donate five pizzas. (-$25)":
            if money <= 24:
                "You do not have enough money to buy Lyn 5 pizzas. You can earn money by working at the diner."
                image Lyn_gaming = "/leanne/[leanne.stage]/Lyn_gaming.webp"
                scene Lyn_gaming
                "You watch Lyn stream for a bit."
                "Though she seems to struggle a lot more than she used to, the presence of the chat is more than enough to keep her spirits up through each loss over the course of the session."
                image Lyn_goodbye = "/leanne/[leanne.stage]/Lyn_goodbye.webp"
                scene Lyn_goodbye
                leanne "That'll do it for me tonight. Thank you everyone for watching. See you next time!"
                "The stream ends."
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime
            $ money -= 25
            image Lyn_happy = "/leanne/[leanne.stage]/Lyn_happy.webp"
            scene Lyn_happy
            leanne "Thank you so very much for the generous donation. While I wait for the pizzas to arrive, let me give you a little treat."
            image Lyn_standing = "/leanne/[leanne.stage]/Lyn_standing.webp"
            scene Lyn_standing
            leanne "Alright. What would you like me to do?"
            #CHOICE: A) Dance or B) Exercise
            #(NOTE: Add more choices as the stages progress if possible to add new animations)
            if leanne.stage <= 13:
                menu:
                    "Dance.":
                        "Starting up a royalty free song on her speakers, Lyn begins to dance around to the rhythm of the beat."
                        if leanne.stage == 12:
                            $ renpy.movie_cutscene("/images/leanne/12/Lyn_dance.webm", stop_music=False)
                        elif leanne.stage == 13:
                            $ renpy.movie_cutscene("/images/leanne/13/Lyn_dance.webm", stop_music=False)
                        window hide
                        pause
                        "Though she struggles to move with her extra weight, she still keeps up a modest smile as she finishes up her routine."

                    "Exercise.":
                        "Looking reluctant at first, Lyn eventually pushes herself to begin exercising."
                        if leanne.stage == 12:
                            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                            play movie "/images/leanne/12/Lyn_exercise.webm" loop
                            show movie with dissolve
                        elif leanne.stage == 13:
                            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                            play movie "/images/leanne/13/Lyn_exercise.webm" loop
                            show movie with dissolve
                        window hide
                        pause
                        "Though it's clear that's she struggling through the exertion. she tries to keep up a smile for her viewers as she works through the routine."
                        stop movie

            else:
                "Lyn stands up, giving the stream a good view of her full body."
                image Lyn_bellydrop = "/leanne/[leanne.stage]/Lyn_bellydrop.webp"
                scene Lyn_bellydrop
                "She lifts up her belly with both hands."
                if leanne.stage == 14:
                    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                    play movie "/images/leanne/14/Lyn_bellydrop_1.webm" loop
                    show movie with dissolve
                    window hide
                    pause
                    stop movie
                    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                    play movie "/images/leanne/14/Lyn_bellydrop_2.webm" loop
                    show movie with dissolve
                    window hide
                    pause
                    stop movie
                elif leanne.stage == 15:
                    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                    play movie "/images/leanne/15/Lyn_bellydrop_1.webm" loop
                    show movie with dissolve
                    window hide
                    pause
                    stop movie
                    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                    play movie "/images/leanne/15/Lyn_bellydrop_2.webm" loop
                    show movie with dissolve
                    window hide
                    pause
                    stop movie

            image Lyn_towel = "/leanne/[leanne.stage]/Lyn_towel.webp"
            scene Lyn_towel
            leanne "That was a bit of a work out. Thankfully, I think the pizzas just arrived to help me refuel."
            image Lyn_pizzastack = "/leanne/[leanne.stage]/Lyn_pizzastack.webp"
            scene Lyn_pizzastack
            leanne "This all looks so good. Let me try to work through these as I play."
            image Lyn_pizza2 = "/leanne/[leanne.stage]/Lyn_pizza2.webp"
            scene Lyn_pizza2
            "Though her gaming skill declines as she eats, she doesn't seem to care."
            image Lyn_pizza3 = "/leanne/[leanne.stage]/Lyn_pizza3.webp"
            scene Lyn_pizza3
            "She eagerly downs each slice like she's on the brink of starvation. One after another the boxes are emptied out as her belly fills up with pizza."
            image Lyn_stuffed1 = "/leanne/[leanne.stage]/Lyn_stuffed1.webp"
            scene Lyn_stuffed1
            "Finishing up the last slice, Lyn leans back in her seat as she absentmindedly rubs her overstuffed stomach."
            image Lyn_stuffed2 = "/leanne/[leanne.stage]/Lyn_stuffed2.webp"
            scene Lyn_stuffed2
            leanne "Whoo. That really hit the spot."
            image Lyn_stuffed3 = "/leanne/[leanne.stage]/Lyn_stuffed3.webp"
            scene Lyn_stuffed3
            leanne "I think that's going to do it for me tonight. Thank you all for stopping by."
            $ leanne.weight += 1.5
            stop music fadeout 1.0
            $ daytime += 1
            jump freetime

label leanne_feeding_sugarshop:
    #Image: Sugar Shop interior with Leanne in her incognito outfit sitting across from the player.
    image stream_girl_sugarshop_1 = "/leanne/[leanne.stage]/sugarshop_1.webp"
    scene stream_girl_sugarshop_1
    play music "<loop 0.2 from 39>/music/generic_date.ogg" if_changed fadein 1.0
    leanne "Everything looks so good. I don't know where to even start."
    image stream_girl_sugarshop_2 = "/leanne/[leanne.stage]/sugarshop_2.webp"
    scene stream_girl_sugarshop_2
    leanne "Perhaps you could offer a 'suggestion' for what you want me to order?"
    #(NOTE: The player is prompted to choose from various menu items with different prices. There would also be an option to not buy anything, in which case Leanne would buy a small plate of donuts to eat. Depending on the choice, the following would occur as Leanne eats the chosen meal.)
    menu:
        "Buy her loads of sweets. (-$20)":
            if money <= 19:
                "You do not have enough money to buy her loads of sweets, you can earn money by working at the restaurant."
                "She orders a small plate of sweets."
            else:
                $ money -= 20
                "You buy loads of sweets for Lyn. These should certainly help fatten her up."
                $ leanne.weight += 1
        "Buy her a couple sweets. (-$10)":
            if money <= 9:
                "You do not have enough money to buy her a couple sweets, you can earn money by working at the restaurant."
                "She orders a small plate of sweets."
            else:
                $ money -= 10
                "You buy a couple of sweets for Lyn."
                $ leanne.weight += 0.5
        "Let her buy her own sweets.":
            "She orders a small plate of sweets."
            $ leanne.weight += 0.2

    if leanne.stage == 6 or leanne.stage == 7:
        "While waiting for your order, you consider asking Lyn something."
        #CHOICE: A) What’s your favorite kind of sweets? or B) Don’t ask anything
        #(NOTE: Regardless of choice, after each section the scene will move to Lyn/Leanne stuffing herself with the sweet order selected earlier in the scene.)
        menu:
            "What’s your favorite kind of sweets?":
                #IMAGE: Lyn/Leanne thinking.
                leanne "Hmm, that’s pretty hard to choose. This place alone has a lot of different options."
                "Lyn goes quiet for a moment as she scratches her chin in thought."
                #IMAGE: Lyn/Leanne staring at the player with a smile
                "Eventually a smile appears on her face as she finally makes up her mind."
                leanne "Buuuuuut, if I had to pick one…I guess I’d have to say a strawberry shortcake."
                pc "Why?"
                leanne "Do I need a reason?"
                pc "I guess not, but I’m still curious."
                #IMAGE: Lyn/Leanne holding up a hand as she speaks.
                leanne "Firstly, it’s because it tastes really good. The combination of the strawberries mixed with the cream is absolutely heavenly."
                leanne "Second, and this is admittedly a little embarrassing, it’s the favorite dessert of this one character from an anime I like."
                pc "That’s nothing to be ashamed of."
                leanne "Yeah, but it still feels weird talking about it in public. Back when I tried to bring up anime in class everyone gave me this weird look."
                #IMAGE: A smiling Lyn reminiscing as she stares at the player.
                leanne "Their loss. Guess not everyone can understand the simple joys of cake and shows about friendship."
                pc "Which anime are you talking about?"
                leanne "Eh, I’ll tell you later. Looks like our order is here."
            "Don’t ask anything":
                "Though it’s a little awkward just sitting there and not saying anything, eventually the order arrives."

    elif leanne.stage == 8 or leanne.stage == 9:
        "Looking for something to talk about and with your mind still racing about Maid Mecha, you ponder asking her if she knows of any other shows of equal quality."
        #CHOICE: A) Any good anime recommendations? Or B) Don’t say anything
        menu:
            "Any good anime recommendations?":
                #IMAGE: Lyn/Leanne with an excited look on her face.
                "Lyn perks up a bit and leans over the table with a smug smirk."
                leanne "Ah, I see you’ve been impressed by my taste. Alright, let me see if I can think of something on par with Maid Mecha."
                #IMAGE: Lyn/Leanne in thought.
                "Scratching her chin for a bit, she ponders the perfect response."
                leanne "Hmm, well I can think of one thing. It’s not as fanservicey as that show, but it does have some cute girls in it."
                #IMAGE: Lyn/Leanne talking excitedly to the player.
                leanne "It’s called Garden Guardians. It’s about a group of fruit based magical girls fighting together to protect an enchanted garden from the forces of evil."
                #IMAGE: Lyn/Leanne suspicious of the player.
                "Though you don’t say anything, she seems to pick up on the way your face shifts."
                leanne "Don’t think I can’t see that look in your eyes. I’ll admit, it’s not exactly a complicated show in terms of things like plot. And yes, it was made for younger audiences."
                #IMAGE: Lyn/Leanne with her hand on her chest.
                leanne "But sometimes you just need a simple story about friendship to fill a space in your head. Kind of like having the occasional craving for sweets. Speaking of…"
            "Don’t say anything.":
                "Your attempt to avoid the embarrassing idea of talking about anime in public only succeeds in making things more uncomfortable through the use of silence between the two of you until the food arrives."

    elif leanne.stage == 10 or leanne.stage == 11:
        #IMAGE: Uncomfortable Lyn/Leanne trying to adjust her clothes
        "Over the course of the few minutes it takes for the food to arrive, you can’t help noticing how Lyn keeps pulling at her clothes. You feel like something might be wrong."
        #CHOICE: A) Are you feeling alright? Or B) Don’t say anything.
        menu:
            "Are you feeling alright?":
                leanne "Um, yeah, yeah, it’s fine."
                "Still worried, you decide to push the issue."
                pc "If something is bothering you, I might be able to help you out."
                #IMAGE
                "Letting out a sigh, Lyn finally replies."
                leanne "It’s just…I’ve been having some issues with my clothing lately."
                leanne "I think my popularity is coming back to bite me. All of these pizza donations I’ve been receiving has shot me past my weight goal and then some."
                #IMAGE: Lyn/Leanne tugging at her clothes as she looks at the player.
                leanne "My clothes are starting to get tight. A few are a struggle to even squeeze into. I might need to get a whole new wardrobe before long."
                pc "That sounds pretty bad."
                #IMAGE: Lyn/Leanne shrugging
                leanne "Eh, not really. My viewers should be able to help me get the money back."
                #IMAGE: Lyn/Leanne grinning at the player
                leanne "I might even make a special stream out of showing off new outfits. Make the best out of a bad situation, right?"
                pc "You should still slow it down if things are getting too much for you."
                leanne "It’s fine, really. Now come on and let’s eat. Our order just arrived."
            "Don’t say anything":
                "You figure it’s best not to bring up an awkward conservation. While she still struggles a bit with her clothes, she perks up the moment the food is brought to your table."

    image stream_girl_sugarshop_3 = "/leanne/[leanne.stage]/sugarshop_3.webp"
    scene stream_girl_sugarshop_3
    "Between mouthfuls of food, Lyn manages to hold a conversation with you about various, nerdy hobbies."
    image stream_girl_sugarshop_4 = "/leanne/[leanne.stage]/sugarshop_4.webp"
    scene stream_girl_sugarshop_4
    pause
    image stream_girl_sugarshop_5 = "/leanne/[leanne.stage]/sugarshop_5.webp"
    scene stream_girl_sugarshop_5
    pause
    image stream_girl_sugarshop_6 = "/leanne/[leanne.stage]/sugarshop_6.webp"
    scene stream_girl_sugarshop_6
    "With the table cleared and the bill paid, you go your separate ways."
    return

label leanne_feeding_bunnybites:

    #IMAGE: Bunny Bites interior with Leanne in her incognito outfit sitting across from the player.
    "Looking to meet up with Lyn you head down to Bunny Bites and go inside."
    image leanne_BB_talk1 = "/leanne/[leanne.stage]/BB_talk1.webp"
    scene leanne_BB_talk1
    play music "<loop 0.2 from 39>/music/generic_date.ogg" if_changed fadein 1.0
    if leanne.stage == 6 or leanne.stage == 7:
        "Expecting her normal large sunglasses and hoodie, you're met with a pleasant surprise. She's dressed in a much cuter outfit."
        "She's still clearly trying to hide who she is in public but her outfit gives you a great view of her recent gain."
    "You make your way over to her booth and take a seat opposite of her."
    leanne "So many options for fattening myself up, so little time. Shame I have such a strict leash on my wallet right now."
    image leanne_BB_talk2 = "/leanne/[leanne.stage]/BB_talk2.webp"
    scene leanne_BB_talk2
    leanne "If only there was a loyal viewer nearby to give me some help picking something out."
    "You can’t help noticing that she says that with a look similar to the way she asks for donations."
    #(NOTE: The player is prompted to choose from various menu items with different prices. There would also be an option to not buy anything, in which case Lyn/Leanne would buy a small basket of fries to eat. Depending on the choice, the following would occur before the order arrives.)
    #IMAGE: Lyn/Leanne looking bored as sits across from the player.
    menu:
        "Buy her a big meal. (-$20)":
            if money <= 19:
                "You do not have enough money to buy her a big meal, you can earn money by working at the restaurant."
                "She orders a small meal for herself."
                $ mealoption = 1
            else:
                $ money -= 20
                "You buy her the biggest meal they have."
                $ mealoption = 3
        "Buy her a medium meal. (-$10)":
            if money <= 9:
                "You do not have enough money to buy her a medium meal, you can earn money by working at the restaurant."
                "She orders a small meal for herself."
                $ mealoption = 1
            else:
                $ money -= 10
                "You buy her a medium meal."
                $ mealoption = 2
        "Let her buy her own food.":
            "She orders a small meal for herself."
            $ mealoption = 1

    if (leanne.stage == 6 or leanne.stage == 7) and leannequestion1 == 1:
        image leanne_BB_talk3 = "/leanne/[leanne.stage]/BB_talk3.webp"
        scene leanne_BB_talk3
        "After putting in the order, you’re left with an odd atmosphere as neither of you say a thing but your ears ring with the sound of servers and the other customers in the diner."
        #CHOICE: A) What made you want to start streaming? or B) Wait and see if she says anything
        #(NOTE: Regardless of choice, after each section the scene will move to Lyn/Leanne stuffing herself with the food order selected earlier in the scene.)
        menu:
            "Do you want to say something?"
            "What made you want to start streaming?":
                image leanne_BB_question1 = "/leanne/[leanne.stage]/BB_question1.webp"
                scene leanne_BB_question1
                "Lyn stirs a bit, as if the question has woken her up from a nap."
                leanne "You mean, besides being broke?"
                pc "There must have been some other options."
                image leanne_BB_question2 = "/leanne/[leanne.stage]/BB_question2.webp"
                scene leanne_BB_question2
                leanne "Yeah, but nothing that I really wanted to do. Tried a few things like food service and retail, but I could feel myself dying inside each time I punched in for a shift."
                image leanne_BB_question3 = "/leanne/[leanne.stage]/BB_question3.webp"
                scene leanne_BB_question3
                leanne "Streaming just has some kind of allure to it, you know? Like it’s some big, revolutionary new way to entertain people."
                pc "I can’t say I feel exactly like it, but I kind of get it."
                image leanne_BB_question4 = "/leanne/[leanne.stage]/BB_question4.webp"
                scene leanne_BB_question4
                leanne "When I wasn’t studying for the classes that I skipped out on during my short time at college, I spent a lot of nights watching streams. Something really clicked with me."
                leanne "Faced with being broke, I decided to give it a shot. So far, I haven’t regretted my decision."
                pc "I’m really glad it’s working out for you."
                image leanne_BB_question5 = "/leanne/[leanne.stage]/BB_question5.webp"
                scene leanne_BB_question5
                leanne "Well, the entire experience hasn’t been great. While I have had fun, there have been certain…difficulties I didn’t expect."
                pc "Like what?"
                leanne "Ugh, I don’t really feel like getting into it right now. Anyway, our food is here. Let’s chow down."
                $ leannequestion1 = 0
            "Wait and see if she says anything.":
                "Your plan is immediately foiled as a rush of customers flood in. Though Lyn tries to speak every now and then, her voice is drowned out by the noise."
                "Unable to hold a conversation, the two of you merely wait until the food arrives."
    elif (leanne.stage == 8 or leanne.stage == 9) and leannequestion2 == 1:
        image leanne_BB_talk3 = "/leanne/[leanne.stage]/BB_talk3.webp"
        scene leanne_BB_talk3
        "After putting in the order, you’re left with an odd atmosphere as neither of you say a thing but your ears ring with the sound of servers and the other customers in the diner."
        #CHOICE: A) Are there any big challenges to streaming? or B) Don’t try to bring up work in her off time
        menu:
            "Thinking about how much effort Lyn puts into her streams, you wonder what kind of hurdles she has to go through to make it all work."
            "Are there any big challenges to streaming":
                image leanne_BB_question1 = "/leanne/[leanne.stage]/BB_question1.webp"
                scene leanne_BB_question1
                "Slumping in her seat, she lets out a sigh. Though it appears like she’s unhappy with the question, it looks like you’ve given her an opportunity for a long overdue venting session."
                leanne "Ugh, like you wouldn’t believe."
                leanne "Things usually get tough right at the start. Equipment doesn’t want to work for one reason or another and you have no idea why."
                leanne "Seriously, there was this one time I spent three hours trying to get a camera working. Turns out the problem was caused by just a pair of wires getting mixed up."
                image leanne_BB_question2 = "/leanne/[leanne.stage]/BB_question2.webp"
                scene leanne_BB_question2
                leanne "Although, that pales in comparison to certain viewers that decide to try and make my life a living hell for the fun of it."
                pc "I’m so sorry."
                image leanne_BB_question3 = "/leanne/[leanne.stage]/BB_question3.webp"
                scene leanne_BB_question3
                leanne "Eh, it’s really no big deal. Sure they’re annoying, but thankfully that’s what I have mods for."
                leanne "Just stings a little whenever they manage to slip through the cracks."
                pc "It’s still a shame that you have to hear such awful things."
                image leanne_BB_question4 = "/leanne/[leanne.stage]/BB_question4.webp"
                scene leanne_BB_question4
                leanne "Don’t worry so much about it. They’re a one in every 1000 or so people that show up to watch my streams."
                leanne "Everyone else either lurks silently or sends me support. It’s because of the latter that I’m able to keep streaming."
                image leanne_BB_question5 = "/leanne/[leanne.stage]/BB_question5.webp"
                scene leanne_BB_question5
                leanne "For the record, you’re in that category. You’ve been a big help with keeping me sane and well fed. Even joining me for this meal is a big boost."
                leanne "Hope what I’m about to do this food give you a little boost as well."
                $ leannequestion2 = 0
            "Don’t try to bring up work in her off time":
                "Rather than irritate her mood any further, you decide to give her some peace and quiet until the food arrives."
    elif (leanne.stage == 10 or leanne.stage == 11) and leannequestion3 == 1:
        image leanne_BB_talk3 = "/leanne/[leanne.stage]/BB_talk3.webp"
        scene leanne_BB_talk3
        "Watching Lyn tap her fingers against the table as she patiently waits for the food, you try to think of something to fill the air."
        #CHOICE: A) Why do you always play Carl on Duty or B) That’s a little too obvious to ask
        menu:
            "Your mind centers on one of her more obvious hobbies. The very game where you met her in the first place."
            "Why do you always play Carl on Duty?":
                image leanne_BB_question1 = "/leanne/[leanne.stage]/BB_question1.webp"
                scene leanne_BB_question1
                leanne "You mean besides the fact that I find it fun?"
                pc "Yeah. I don’t think I’ve seen you play anything else on your streams."
                image leanne_BB_question2 = "/leanne/[leanne.stage]/BB_question2.webp"
                scene leanne_BB_question2
                leanne "True, but it’s not the only game I find enjoyable. I do play other things when I’m not streaming, watching anime, or recovering from said streams."
                leanne "However, I have a more important reason for playing it so much: stability."
                leanne "Carl on Duty is one of the most popular games to stream right now."
                image leanne_BB_question3 = "/leanne/[leanne.stage]/BB_question3.webp"
                scene leanne_BB_question3
                leanne "It’s something that feels comfortable, not just to me, but to my audience. During my anime review stream, I got plenty of complaints that I wasn’t playing it."
                leanne "It’s like a comfort food for me and the viewers. Whenever I can’t think of anything else, it’s something good for me to turn to."
                leanne "I’m not saying it’s going to be the only game I’ll ever play, but it’s certainly doing the job for now. Maybe I’ll try diversifying more in the future."
                $ leannequestion3 = 0
            "That’s a little too obvious to ask":
                "Unable to think of a better question to ask at the time, you let Lyn do most of the talking until the server returns with your order."

    if mealoption == 1:
        image leanne_BB_food1 = "/leanne/[leanne.stage]/BB_food1.webp"
        scene leanne_BB_food1
        "A moment later the food arrives."
        "Lyn looks a bit disappointed by her single burger."
        image leanne_BB_eat1 = "/leanne/[leanne.stage]/BB_eat1.webp"
        scene leanne_BB_eat1
        "Between mouthfuls of food, Lyn manages to hold a conversation with you about various, nerdy hobbies."
        "Lyn easily makes quick work of her meager meal."
        image leanne_BB_bye1 = "/leanne/[leanne.stage]/BB_bye1.webp"
        scene leanne_BB_bye1
        "Clearly less filling than what she has been consuming in a single sitting on stream over the last few weeks."
        "With the table cleared and the bill paid, you go your separate ways."
        stop music fadeout 1.0
        $ leanne.weight += 0.2
        $ mealoption = 1
        return
    if mealoption == 2:
        image leanne_BB_food2 = "/leanne/[leanne.stage]/BB_food2.webp"
        scene leanne_BB_food2
        "A moment later the food arrives."
        "Lyn seems happy with the food in front of her."
        image leanne_BB_eat2 = "/leanne/[leanne.stage]/BB_eat2.webp"
        scene leanne_BB_eat2
        "Between mouthfuls of food, Lyn manages to hold a conversation with you about various, nerdy hobbies."
        image leanne_BB_eat1 = "/leanne/[leanne.stage]/BB_eat1.webp"
        scene leanne_BB_eat1
        window hide
        pause
        image leanne_BB_bye2 = "/leanne/[leanne.stage]/BB_bye2.webp"
        scene leanne_BB_bye2
        "With a satiated sigh and rub of her stomach, Lyn stands up giving you a view of her slightly bloated form."
        "Her recent indulgences on stream have clearly had an effect on her with how effortlessly she was able to put away her meal."
        "With the table cleared and the bill paid, you go your separate ways."
        stop music fadeout 1.0
        $ leanne.weight += 0.5
        $ mealoption = 1
        return
    if mealoption == 3:
        image leanne_BB_food3 = "/leanne/[leanne.stage]/BB_food3.webp"
        scene leanne_BB_food3
        "A moment later the food arrives."
        "Lyn looks very excited at the huge amount of food given to her."
        image leanne_BB_eat3 = "/leanne/[leanne.stage]/BB_eat3.webp"
        scene leanne_BB_eat3
        "Between mouthfuls of food, Lyn manages to hold a conversation with you about various, nerdy hobbies."
        image leanne_BB_eat2 = "/leanne/[leanne.stage]/BB_eat2.webp"
        scene leanne_BB_eat2
        window hide
        pause
        image leanne_BB_eat1 = "/leanne/[leanne.stage]/BB_eat1.webp"
        scene leanne_BB_eat1
        window hide
        pause
        image leanne_BB_bye3 = "/leanne/[leanne.stage]/BB_bye3.webp"
        scene leanne_BB_bye3
        "The results of her huge feast are made clear as she gets to her feet."
        "Lyn looks absolutely stuffed."
        "After eating enough food to rival that of her largest donations on stream; her clothes equally pushed to their limit to accommodate her rapidly expanded form."
        "With the table cleared and the bill paid, you go your separate ways."
        stop music fadeout 1.0
        $ leanne.weight += 1.0
        $ mealoption = 1
        return

label lyn_date_sugarshop:

    image lyn_SS_talk1 = "/leanne/[leanne.stage]/SS_talk1.webp"
    scene lyn_SS_talk1
    play music "/music/date_cozy.ogg" if_changed
    leanne "Thank you for coming with me."
    image lyn_SS_talk2 = "/leanne/[leanne.stage]/SS_talk2.webp"
    scene lyn_SS_talk2
    leanne "Mind helping me pick something out?"
    #CHOICE: A) Let Lyn pick her own B) Pay for a little treat or C) Pay for a large feast
    #(NOTE: Choice A would cost nothing from the player, while B and C would each cost more money and lead to Lyn eating larger portions of food).
    menu:
        "Let Lyn pick her own.":
            "She orders sweets for herself."
            image lyn_SS_food1 = "/leanne/[leanne.stage]/SS_food1.webp"
            scene lyn_SS_food1
            "A moment later the food arrives."
            "Lyn looks slightly disappointed by the amount of sweets in front of her."

            #Image: Various scenes of Lyn eating sweets, the number depending on which option the player chose.
            image lyn_SS_eat1 = "/leanne/[leanne.stage]/SS_eat1.webp"
            scene lyn_SS_eat1
            window hide
            pause
            image lyn_SS_bye1 = "/leanne/[leanne.stage]/SS_bye1.webp"
            scene lyn_SS_bye1
            leanne "Just as delicious as always. Thanks again for joining me."
            $ leanne.weight += 0.2
            stop music fadeout 1.0
            return
        "Pay for a little treat. (-15$)":
            if money <= 14:
                "You do not have enough money to buy Lyn a little treat, you can earn money by working at Bunny Bites."
                "She orders sweets for herself."
                image lyn_SS_food1 = "/leanne/[leanne.stage]/SS_food1.webp"
                scene lyn_SS_food1
                "A moment later the food arrives."
                "Lyn looks slightly disappointed by the amount of sweets in front of her."

                #Image: Various scenes of Lyn eating sweets, the number depending on which option the player chose.
                image lyn_SS_eat1 = "/leanne/[leanne.stage]/SS_eat1.webp"
                scene lyn_SS_eat1
                window hide
                pause
                #Image: Lyn sitting back in her seat with a stuffed belly.
                image lyn_SS_bye1 = "/leanne/[leanne.stage]/SS_bye1.webp"
                scene lyn_SS_bye1
                leanne "Just as delicious as always. Thanks again for joining me."
                $ leanne.weight += 0.2
                stop music fadeout 1.0
                return
            $ money -= 15
            "You buy her a decently amount of sweets."
            image lyn_SS_food2 = "/leanne/[leanne.stage]/SS_food2.webp"
            scene lyn_SS_food2
            "A moment later the food arrives."
            "Lyn looks excited at the large amount of sweets given to her."
            image lyn_SS_eat2 = "/leanne/[leanne.stage]/SS_eat2.webp"
            scene lyn_SS_eat2
            "Between mouthfuls of food, Lyn manages to hold a conversation with you about various, nerdy hobbies."
            image lyn_SS_eat1 = "/leanne/[leanne.stage]/SS_eat1.webp"
            scene lyn_SS_eat1
            window hide
            pause
            image lyn_SS_bye2 = "/leanne/[leanne.stage]/SS_bye2.webp"
            scene lyn_SS_bye2
            $ leanne.weight += 0.5
        "Pay for a large feast. (-30$)":
            if money <= 29:
                "You do not have enough money to buy Lyn a large feast, you can earn money by working at Bunny Bites."
                "She orders sweets for herself."
                image lyn_SS_food1 = "/leanne/[leanne.stage]/SS_food1.webp"
                scene lyn_SS_food1
                "A moment later the food arrives."
                "Lyn looks slightly disappointed by the amount of sweets in front of her."

                #Image: Various scenes of Lyn eating sweets, the number depending on which option the player chose.
                image lyn_SS_eat1 = "/leanne/[leanne.stage]/SS_eat1.webp"
                scene lyn_SS_eat1
                window hide
                pause
                #Image: Lyn sitting back in her seat with a stuffed belly.
                image lyn_SS_bye1 = "/leanne/[leanne.stage]/SS_bye1.webp"
                scene lyn_SS_bye1
                leanne "Just as delicious as always. Thanks again for joining me."
                $ leanne.weight += 0.2
                stop music fadeout 1.0
                return
            #Image: Various scenes of Lyn eating sweets, the number depending on which option the player chose.
            $ money -= 30
            "You buy her a large amount of sweets."
            image lyn_SS_food3 = "/leanne/[leanne.stage]/SS_food3.webp"
            scene lyn_SS_food3
            "A moment later the food arrives."
            "Lyn looks very excited at the huge amount of sweets given to her."
            image lyn_SS_eat3 = "/leanne/[leanne.stage]/SS_eat3.webp"
            scene lyn_SS_eat3
            "Between mouthfuls of food, Lyn manages to hold a conversation with you about various, nerdy hobbies."
            image lyn_SS_eat2 = "/leanne/[leanne.stage]/SS_eat2.webp"
            scene lyn_SS_eat2
            window hide
            pause
            image lyn_SS_eat1 = "/leanne/[leanne.stage]/SS_eat1.webp"
            scene lyn_SS_eat1
            pause
            image lyn_SS_bye3 = "/leanne/[leanne.stage]/SS_bye3.webp"
            scene lyn_SS_bye3
            $ leanne.weight += 1.0
    #Image: Lyn sitting back in her seat with a stuffed belly.
    leanne "Just as delicious as always. Thanks again for joining me."
    stop music fadeout 1.0
    return

label leanne_date_bunnybites:

    image leanne_BB_talk1 = "/leanne/[leanne.stage]/BB_talk1.webp"
    scene leanne_BB_talk1
    play music "<loop 0.2 from 39>/music/generic_date.ogg" if_changed fadein 1.0
    leanne "Hey there fan, you ready for another private show? Just give me a chance to pick something out."
    image leanne_BB_talk2 = "/leanne/[leanne.stage]/BB_talk2.webp"
    scene leanne_BB_talk2
    leanne "That is unless you had something in mind."
    menu:
        "Let Leanne pick her own.":
            "She orders a meal for herself."
            image leanne_BB_food1 = "/leanne/[leanne.stage]/BB_food1.webp"
            scene leanne_BB_food1
            "A moment later the food arrives."
            "Leanne looks slightly disappointed by the size of her meal."
            image leanne_BB_eat1 = "/leanne/[leanne.stage]/BB_eat1.webp"
            scene leanne_BB_eat1
            "What would be a large meal for the average person, is quickly demolished by your pink-haired dining partner."
            image leanne_BB_bye1 = "/leanne/[leanne.stage]/BB_bye1.webp"
            scene leanne_BB_bye1
            "Not long ago this 'snack' sized order would have been more than enough to satiate her."
            leanne "That really hit the spot. This place never disappoints."
            leanne "Thanks for the date, see you later!"
            "You watch Leanne waddle away, before leaving yourself."
            $ leanne.weight += 0.2
            stop music fadeout 1.0
            return
        "Pay for a treat. (-15$)":
            if money <= 14:
                "You do not have enough money to buy Leanne a little treat, you can earn money by working at Bunny Bites."
                "She orders a meal for herself."
                image leanne_BB_food1 = "/leanne/[leanne.stage]/BB_food1.webp"
                scene leanne_BB_food1
                "A moment later the food arrives."
                "Leanne looks slightly disappointed by the size of her meal."
                image leanne_BB_eat1 = "/leanne/[leanne.stage]/BB_eat1.webp"
                scene leanne_BB_eat1
                "What would be a large meal for the average person, is quickly demolished by your pink-haired dining partner."
                image leanne_BB_bye1 = "/leanne/[leanne.stage]/BB_bye1.webp"
                scene leanne_BB_bye1
                "Not long ago this 'snack' sized order would have been more than enough to satiate her."
                leanne "That really hit the spot. This place never disappoints."
                leanne "Thanks for the date, see you later!"
                "You watch Leanne waddle away, before leaving yourself."
                $ leanne.weight += 0.2
                stop music fadeout 1.0
                return
            $ money -= 15
            "You buy her a decently sized meal."
            image leanne_BB_food2 = "/leanne/[leanne.stage]/BB_food2.webp"
            scene leanne_BB_food2
            "A moment later the food arrives."
            "Leanne looks excited at the large amount of food given to her."
            image leanne_BB_eat2 = "/leanne/[leanne.stage]/BB_eat2.webp"
            scene leanne_BB_eat2
            "Between mouthfuls of food, Leanne manages to hold a conversation with you about various, nerdy hobbies."
            image leanne_BB_eat1 = "/leanne/[leanne.stage]/BB_eat1.webp"
            scene leanne_BB_eat1
            window hide
            pause
            image leanne_BB_bye2 = "/leanne/[leanne.stage]/BB_bye2.webp"
            scene leanne_BB_bye2
            "Leanne easily rises to her feet giving you a clear view of her ample stomach, only slightly bloated after her heavy meal."
            "The pink-haired streamer polished off more food than even the largest feast she would have ever been able to eat in the past."
            $ leanne.weight += 0.5
        "Pay for a large feast. (-30$)":
            if money <= 29:
                "You do not have enough money to buy Leanne a large feast, you can earn money by working at Bunny Bites."
                "She orders a meal for herself."
                image leanne_BB_food1 = "/leanne/[leanne.stage]/BB_food1.webp"
                scene leanne_BB_food1
                "A moment later the food arrives."
                "Leanne looks slightly disappointed by the size of her meal."
                image leanne_BB_eat1 = "/leanne/[leanne.stage]/BB_eat1.webp"
                scene leanne_BB_eat1
                "What would be a large meal for the average person, is quickly demolished by your pink-haired dining partner."
                image leanne_BB_bye1 = "/leanne/[leanne.stage]/BB_bye1.webp"
                scene leanne_BB_bye1
                "Not long ago this 'snack' sized order would have been more than enough to satiate her."
                leanne "That really hit the spot. This place never disappoints."
                leanne "Thanks for the date, see you later!"
                "You watch Leanne waddle away, before leaving yourself."
                $ leanne.weight += 0.2
                stop music fadeout 1.0
                return
            $ money -= 30
            "You buy her the biggest meal they have."
            image leanne_BB_food3 = "/leanne/[leanne.stage]/BB_food3.webp"
            scene leanne_BB_food3
            "A moment later the food arrives."
            "Leanne looks very excited at the huge amount of food given to her."
            image leanne_BB_eat3 = "/leanne/[leanne.stage]/BB_eat3.webp"
            scene leanne_BB_eat3
            "Between mouthfuls of food, Leanne manages to hold a conversation with you about various, nerdy hobbies."
            image leanne_BB_eat2 = "/leanne/[leanne.stage]/BB_eat2.webp"
            scene leanne_BB_eat2
            window hide
            pause
            image leanne_BB_eat1 = "/leanne/[leanne.stage]/BB_eat1.webp"
            scene leanne_BB_eat1
            pause
            image leanne_BB_bye3 = "/leanne/[leanne.stage]/BB_bye3.webp"
            scene leanne_BB_bye3
            "The pink-haired glutton struggles to get to her feet."
            "It's clear from her bloated form that the amount of food ordered has pushed even her to her limits."
            "You doubt even someone as greedy as Leanne could handle another 'donation' right now."
            $ leanne.weight += 1.0
    leanne "That really hit the spot. This place never disappoints."
    leanne "Thanks for the date, see you later!"
    "You watch Leanne waddle away, before leaving yourself."
    stop music fadeout 1.0
    return

label lyn_soda_stream:

    #(NOTE: The following is a random event that can occur after Lyn Stage 12 when the player decides to watch her stream.)
    image lyn_soda1 = "/leanne/[leanne.stage]/Lyn_soda1.webp"
    scene lyn_soda1
    play music "/music/leanne_stream2.ogg" if_changed
    leanne "Hello everyone and thanks for tuning in. I wanted to do a little something different tonight."
    image lyn_soda2 = "/leanne/[leanne.stage]/Lyn_soda2.webp"
    scene lyn_soda2
    leanne "I was able to find a bunch of tasty sodas to try on stream. The amount I drink, and which kind will be dependent on donations."
    image lyn_soda3 = "/leanne/[leanne.stage]/Lyn_soda3.webp"
    scene lyn_soda3
    leanne "I'm really interested to see what they taste like so let's get started."
    #CHOICE: A) Don’t donate, B) Donate a little (-$5) or C) Donate a lot (-$25)
    #(NOTE: The following choices will decide how much she drinks alongside how much she burps at the end)
    menu:
        "Don't donate.":
            image lyn_soda4 = "/leanne/[leanne.stage]/Lyn_soda4.webp"
            scene lyn_soda4
            "The stream goes fairly normal, albeit with small donations coming in now and then to get her to sip a cup of soda."
            image lyn_soda7 = "/leanne/[leanne.stage]/Lyn_soda7.webp"
            scene lyn_soda7
            "Though a few gas bubbles try to escape, she manages to stifle them with her hand fairly easily."
            image lyn_soda8 = "/leanne/[leanne.stage]/Lyn_soda8.webp"
            scene lyn_soda8
            leanne "I still have quite a bit left, but I think I'm done for the night. This was really fun. I'll have to do it again some time. See you all later."
            "The stream ends."
            $ leanne.weight += 0.2
        "Donate a little. (-$5)":
            if money <= 4:
                "You do not have enough money to donate, you can earn money by working at Bunny Bites."
                image lyn_soda4 = "/leanne/[leanne.stage]/Lyn_soda4.webp"
                scene lyn_soda4
                "The stream goes fairly normal, albeit with small donations coming in now and then to get her to sip a cup of soda."
                image lyn_soda7 = "/leanne/[leanne.stage]/Lyn_soda7.webp"
                scene lyn_soda7
                "Though a few gas bubbles try to escape, she manages to stifle them with her hand fairly easily."
                image lyn_soda8 = "/leanne/[leanne.stage]/Lyn_soda8.webp"
                scene lyn_soda8
                leanne "I still have quite a bit left, but I think I'm done for the night. This was really fun. I'll have to do it again some time. See you all later."
                "The stream ends."
                $ leanne.weight += 0.2
                $ daytime += 1
                jump freetime
            $ money -= 5
            image lyn_soda4 = "/leanne/[leanne.stage]/Lyn_soda4.webp"
            scene lyn_soda4
            "As the stream starts, Lyn begins by pouring soda into small cups."
            "Though she tries to keep a gradual pace with her drinking, she's forced to speed up once your donation comes in."
            image lyn_soda5 = "/leanne/[leanne.stage]/Lyn_soda5.webp"
            scene lyn_soda5
            "Forgoing her first strategy, she begins to drink the soda straight from the cans."
            "Motivated by this, more people begin to put in small donations to keep her drinking."
            "This has the effect of making her begin to blush as the occasional burp leaves her mouth."
            image lyn_soda9 = "/leanne/[leanne.stage]/Lyn_soda9.webp"
            scene lyn_soda9 with vpunch
            leanne "UUUURRP! Oh, excuse me."
            image lyn_soda10 = "/leanne/[leanne.stage]/Lyn_soda10.webp"
            scene lyn_soda10
            leanne "I think that little bit of soda left a few too many bubbles inside of me. While I still have some soda left, I guess I'll save that for another time."
            leanne "Thank you again for all of your donations."
            "The stream ends."
            $ leanne.weight += 0.5
        "Donate a lot. (-$25)":
            if money <= 24:
                "You do not have enough money to donate, you can earn money by working at Bunny Bites."
                image lyn_soda4 = "/leanne/[leanne.stage]/Lyn_soda4.webp"
                scene lyn_soda4
                "The stream goes fairly normal, albeit with small donations coming in now and then to get her to sip a cup of soda."
                image lyn_soda7 = "/leanne/[leanne.stage]/Lyn_soda7.webp"
                scene lyn_soda7
                "Though a few gas bubbles try to escape, she manages to stifle them with her hand fairly easily."
                image lyn_soda8 = "/leanne/[leanne.stage]/Lyn_soda8.webp"
                scene lyn_soda8
                leanne "I still have quite a bit left, but I think I'm done for the night. This was really fun. I'll have to do it again some time. See you all later."
                "The stream ends."
                $ leanne.weight += 0.2
                $ daytime += 1
                jump freetime
            $ money -= 25
            image lyn_soda4 = "/leanne/[leanne.stage]/Lyn_soda4.webp"
            scene lyn_soda4
            "Though Lyn starts off the stream by trying to sip at her soda, she nearly spits it out when your donation is dropped."
            "For a moment she stays still as she watches more and more people send money in to get her to drink."
            "Finishing off her cup, she takes a deep breath as she prepares to take care of the rest of the soda."
            image lyn_soda5 = "/leanne/[leanne.stage]/Lyn_soda5.webp"
            scene lyn_soda5
            "Leaving the cups by the wayside, Lyn pops open one can after another. Pushed forwards by the donations that keep rolling in, she tries to keep drinking despite the burps escaping her lips."
            "However, even this isn't enough to keep up with her audience's constant desire to see her drink."
            image lyn_soda6 = "/leanne/[leanne.stage]/Lyn_soda6.webp"
            scene lyn_soda6
            "She begins twisting open full bottles of soda and putting them to her lips."
            "Chugging down the sugary drinks, she's left no time to pay any mind to the constant belches that erupt from her mouth whenever she dares to take the bottle away."
            "Her belly bulges out to contain the massive amount of soda, helping her to make her way through her entire collection."
            image lyn_soda11 = "/leanne/[leanne.stage]/Lyn_soda11.webp"
            scene lyn_soda11 with vpunch
            leanne "That was BWOOOOOOORRRPPP a lot of soda."
            leanne "I didn't think I could UUUUUURRRP drink that much at once."
            image lyn_soda12 = "/leanne/[leanne.stage]/Lyn_soda12.webp"
            scene lyn_soda12
            leanne "My tummy is a little bubbly, so I think that will be it for me."
            image lyn_soda13 = "/leanne/[leanne.stage]/Lyn_soda13.webp"
            scene lyn_soda13
            leanne "See you all UUUUURRRP next time."
            "The stream ends."
            $ leanne.weight += 1.0
    $ daytime += 1
    jump freetime

label leanne_soda_stream:

    play music "/music/leanne_stream.ogg" if_changed
    image leanne_soda1 = "/leanne/[leanne.stage]/Leanne_soda1.webp"
    scene leanne_soda1
    leanne "Hey there! This is Luxury Leanne coming at you live with a special stream."
    leanne "I've managed to get my hands on a bunch of different sodas."
    image leanne_soda2 = "/leanne/[leanne.stage]/Leanne_soda2.webp"
    scene leanne_soda2
    leanne "While I'm sure they're all tasty, I'm more interested in seeing what they can do to really bloat my belly."
    image leanne_soda3 = "/leanne/[leanne.stage]/Leanne_soda3.webp"
    scene leanne_soda3
    leanne "If you want to see a big me and even bigger burps, make sure to send your donations in!"
    menu:
        "Don't donate.":
            image leanne_soda4 = "/leanne/[leanne.stage]/Leanne_soda4.webp"
            scene leanne_soda4
            "The stream goes fairly normal, albeit with small donations coming in now and then to get her to drink a cup of soda."
            "As eager as she seemed before, she deliberately takes her time sipping the sugary beverages."
            "The odd burp leaving her lips serves to tease her viewers of her true skills, but the stream ends before anything really comes of it."
            image leanne_soda7 = "/leanne/[leanne.stage]/Leanne_soda7.webp"
            scene leanne_soda7 with vpunch
            leanne "BWOORRP. Hmm, that was pretty weak."
            image leanne_soda10 = "/leanne/[leanne.stage]/Leanne_soda10.webp"
            scene leanne_soda10
            leanne "Ah well, guess we'll have to try this again some other time. Until then, this is Luxury Leanne signing off."
            "The stream ends."
            $ leanne.weight += 0.2
        "Donate a little (-$5)":
            if money <= 4:
                image leanne_soda4 = "/leanne/[leanne.stage]/Leanne_soda4.webp"
                scene leanne_soda4
                "The stream goes fairly normal, albeit with small donations coming in now and then to get her to drink a cup of soda."
                "As eager as she seemed before, she deliberately takes her time sipping the sugary beverages."
                "The odd burp leaving her lips serves to tease her viewers of her true skills, but the stream ends before anything really comes of it."
                image leanne_soda7 = "/leanne/[leanne.stage]/Leanne_soda7.webp"
                scene leanne_soda7 with vpunch
                leanne "BWOORRP. Hmm, that was pretty weak."
                image leanne_soda10 = "/leanne/[leanne.stage]/Leanne_soda10.webp"
                scene leanne_soda10
                leanne "Ah well, guess we'll have to try this again some other time. Until then, this is Luxury Leanne signing off."
                "The stream ends."
                $ leanne.weight += 0.2
                $ daytime += 1
                jump freetime
            $ money -= 5
            image leanne_soda4 = "/leanne/[leanne.stage]/Leanne_soda4.webp"
            scene leanne_soda4
            "As the stream starts, Leanne begins by pouring soda into cups to tease her audience with small burps leaving her mouth."
            "Upon you and the other viewers dropping in donations, she quickly abandons this in favor of a much more direct method."
            image leanne_soda5 = "/leanne/[leanne.stage]/Leanne_soda5.webp"
            scene leanne_soda5
            "Opening up cans of soda, she begins to pour them down her throat in rapid succession to appease her donators."
            "She only pauses on occasion to grab another can, or let the chat get a good view of her mouth opening up for a loud burp."
            image leanne_soda8 = "/leanne/[leanne.stage]/Leanne_soda8.webp"
            scene leanne_soda8 with vpunch
            leanne "As BWOOOOOORRRRRP tasty as that was, I've still got a bit left. Pretty sure my burps could be much UUUUUURRRRPP stronger too."
            image leanne_soda11 = "/leanne/[leanne.stage]/Leanne_soda11.webp"
            scene leanne_soda11
            leanne "Ah, well. Guess we'll have to go bigger and better next time. Until then, this is Luxury Leanne signing off."
            "The stream ends."
            $ leanne.weight += 0.5
        "Donate a lot. (-$25)":
            if money <= 24:
                image leanne_soda4 = "/leanne/[leanne.stage]/Leanne_soda4.webp"
                scene leanne_soda4
                "The stream goes fairly normal, albeit with small donations coming in now and then to get her to drink a cup of soda."
                "As eager as she seemed before, she deliberately takes her time sipping the sugary beverages."
                "The odd burp leaving her lips serves to tease her viewers of her true skills, but the stream ends before anything really comes of it."
                image leanne_soda7 = "/leanne/[leanne.stage]/Leanne_soda7.webp"
                scene leanne_soda7 with vpunch
                leanne "BWOORRP. Hmm, that was pretty weak."
                image leanne_soda10 = "/leanne/[leanne.stage]/Leanne_soda10.webp"
                scene leanne_soda10
                leanne "Ah well, guess we'll have to try this again some other time. Until then, this is Luxury Leanne signing off."
                "The stream ends."
                $ leanne.weight += 0.2
                $ daytime += 1
                jump freetime
            $ money -= 25
            image leanne_soda4 = "/leanne/[leanne.stage]/Leanne_soda4.webp"
            scene leanne_soda4
            "Though Leanne tries to start with a gentle sip to ease the audience in, that plan is thrown out the moment she sees your donation."
            "For a few seconds she stays still as she watches more and more people send money in to either match your contribution or go beyond it."
            "Finishing off the cup with a single gulp, she shoots a grin at the camera before she grabs an armful of cans."
            image leanne_soda5 = "/leanne/[leanne.stage]/Leanne_soda5.webp"
            scene leanne_soda5
            "Popping open one can after another, Leanne effortlessly pours the sweet concoctions down her throat."
            "Pushed forwards by the donations that keep rolling in, she shows no hesitation in letting out one guttural belch after another to appease her audience."
            "However, even this isn't enough to keep up with the chat's constant desire to see her indulge in the sugary drinks."
            image leanne_soda6 = "/leanne/[leanne.stage]/Leanne_soda6.webp"
            scene leanne_soda6
            "More than willing to step up to the challenge, she begins twisting open full bottles of soda and putting them to her lips."
            "Chugging down the fizzy liquids, she only stops drinking to grab more soda or let her viewers enjoy the sight and sound of her letting out belches that echo through her room."
            "Her belly bulges out to contain the massive amount of soda, helping her drink the entire collection."
            #Image: Leanne sitting at her desk rubbing her exposed belly.
            "Finishing off the last bottle, Leanne leans back in her seat. After furiously shaking around her belly for a bit, she opens her lips wide."
            image leanne_soda9 = "/leanne/[leanne.stage]/Leanne_soda9.webp"
            scene leanne_soda9 with vpunch
            leanne "BOOOOOOOOOOUUUUUUUUUURRRRRRRPPPPPP! Yeah, that's what I'm talking about."
            leanne "I knew I had it UUUUUUURRRP in me."
            leanne "Thank you my loyal BWOOOOOOOORRRP viewers for helping me break my record."
            image leanne_soda12 = "/leanne/[leanne.stage]/Leanne_soda12.webp"
            scene leanne_soda12
            leanne "Let's see if we can go even bigger next time."
            image leanne_soda13 = "/leanne/[leanne.stage]/Leanne_soda13.webp"
            scene leanne_soda13
            leanne "Until then, this is Luxury Leanne signing off!"
            "The stream ends."
            $ leanne.weight += 1.0
    $ daytime += 1
    jump freetime

label lyn_sugar_shop_stream:
    #Scene: Lyn Sugar Shop Sponsored Stream
    #(NOTE: The following should occur as a random event after Lyn stage 12 when the player decides to watch her stream.)
    play music "/music/leanne_stream2.ogg" if_changed
    image lyn_ad1_1 = "/leanne/[leanne.stage]/Lyn_ad1_1.webp"
    scene lyn_ad1_1
    "You tune into the stream to see Lyn dressed in only an apron."
    image lyn_ad1_2 = "/leanne/[leanne.stage]/Lyn_ad1_2.webp"
    scene lyn_ad1_2
    "Her clothing, or better yet, lack thereof doesn't go unnoticed by her viewers."
    "This fact is probably why she seems to be shaking like a leaf in the wind as she tries to start the stream."
    leanne "Um, hello everyone. Welcome to a very special, sponsored stream."
    image lyn_ad1_3 = "/leanne/[leanne.stage]/Lyn_ad1_3.webp"
    scene lyn_ad1_3
    leanne "This stream is brought to you by a small bakery called the Sugar Shop. It's still an upstart business, but their treats are simply divine."
    leanne "Hopefully I can convince you over the course of the stream to go there and give them some business."
    image lyn_ad1_4 = "/leanne/[leanne.stage]/Lyn_ad1_4.webp"
    scene lyn_ad1_4
    "Diving into a game, Lyn occasionally takes a hand away from the controller to procure one of the sweets."
    "Each delectable treat is given a few moments to bask in the attention of her viewers before she scarfs it down."
    image lyn_ad1_5 = "/leanne/[leanne.stage]/Lyn_ad1_5.webp"
    scene lyn_ad1_5
    "Though she attempts to keep up this slow pace, her appetite ends up making her eat more than she intended."
    image lyn_ad1_6 = "/leanne/[leanne.stage]/Lyn_ad1_6.webp"
    scene lyn_ad1_6
    "Lyn lifts up her apron to show her stuffed gut to the audience."
    image lyn_ad1_7 = "/leanne/[leanne.stage]/Lyn_ad1_7.webp"
    scene lyn_ad1_7
    leanne "I think I might have had a little too much."
    image lyn_ad1_8 = "/leanne/[leanne.stage]/Lyn_ad1_8.webp"
    scene lyn_ad1_8
    leanne "I'm sorry, but that just shows you how good these are."
    leanne "Make sure to visit the Sugar Shop and thank them again for providing tonight's treats. See you later!"
    "The stream ends."
    $ leanne.weight += 0.5
    $ daytime += 1
    jump freetime

label leanne_bunny_bites_stream:
    #Scene: Leanne Bunny Bites Stream
    #(NOTE: The following should occur after Leanne Stage 12 and, if possible after the player has invested money into Bunny Bites, as a random event whenever the player chooses to watch her stream.)
    play music "/music/leanne_stream.ogg" if_changed
    image leanne_ad1_1 = "/leanne/[leanne.stage]/Leanne_ad1_1.webp"
    scene leanne_ad1_1
    "You tune in to the stream to see Leanne dressed in a very familiar uniform."
    leanne "Hey everyone! This is Luxury Leanne coming at you live with a special stream."
    image leanne_ad1_2 = "/leanne/[leanne.stage]/Leanne_ad1_2.webp"
    scene leanne_ad1_2
    leanne "Today I'm being sponsored by one of the best diners in town, Bunny Bites."
    image leanne_ad1_3 = "/leanne/[leanne.stage]/Leanne_ad1_3.webp"
    scene leanne_ad1_3
    "Getting up from her desk, she begins to pose to allow her viewers to get a good look at the way her outfit tightly clings to her pudgy body."
    image leanne_ad1_4 = "/leanne/[leanne.stage]/Leanne_ad1_4.webp"
    scene leanne_ad1_4
    leanne "They were generous enough to give me one of their uniforms."
    image leanne_ad1_5 = "/leanne/[leanne.stage]/Leanne_ad1_5.webp"
    scene leanne_ad1_5
    leanne "It's a little tight, but I figured that you all would enjoy getting to see how it emphasizes my body. However, that's not all they gave me."
    image leanne_ad1_6 = "/leanne/[leanne.stage]/Leanne_ad1_6.webp"
    scene leanne_ad1_6
    "Upon grabbing a collection of take out containers, Leanne returns to her seat and shows the food off to her audience."
    leanne "Their food is even more awesome than this costume if you can believe it. I go there all the time to maintain this perfect body for your viewing pleasure."
    leanne "As much as I'd like to continue praising them, I know that's not the main reason why you're here. Let's get to some gaming and food gobbling."
    image leanne_ad1_7 = "/leanne/[leanne.stage]/Leanne_ad1_7.webp"
    scene leanne_ad1_7
    "Similar to her other streams, Leanne manages to maintain a solid performance in her game while simultaneously shoving food into her mouth."
    image leanne_ad1_8 = "/leanne/[leanne.stage]/Leanne_ad1_8.webp"
    scene leanne_ad1_8
    "Bite after bite she effortlessly puts the heavy meals down her throat, picking up speed over the course of the stream as she becomes more engrossed with the flavor."
    "Perhaps a little too obsessed with her binging session, she ends up pausing towards the end of the stream to over indulge herself in the tasty meals."
    image leanne_ad1_9 = "/leanne/[leanne.stage]/Leanne_ad1_9.webp"
    scene leanne_ad1_9
    "Swallowing up the last bit of food, Leanne sits back in her seat."
    image leanne_ad1_10 = "/leanne/[leanne.stage]/Leanne_ad1_10.webp"
    scene leanne_ad1_10
    "Lazily dragging her hand across her belly, she opens up her mouth to let out a loud burp to finish off her meal."
    image leanne_ad1_11 = "/leanne/[leanne.stage]/Leanne_ad1_11.webp"
    scene leanne_ad1_11 with vpunch
    leanne "You can probably UUURRP see why I like this place so much now."
    image leanne_ad1_12 = "/leanne/[leanne.stage]/Leanne_ad1_12.webp"
    scene leanne_ad1_12
    leanne "Make sure you stop by to get some of this delicious food for yourself. Until next time, this is Luxury Leanne signing off!"
    "The stream ends."
    $ leanne.weight += 0.5
    $ daytime += 1
    jump freetime

label leanne_velvet_shadows_stream:
    #Scene: Leanne Velvet Shadows Stream
    #(NOTE: The following random event should occur when the player chooses to watch Leanne’s stream after Leanne Stage 12. If possible, this should occur after the player has invested in the Velvet Shadows)
    #Image: Leanne dressed in a stripper outfit standing in the middle of her room.
    "As you tune in to watch Leanne, you realize that she's once more streaming on Eroticabase. More than a little curious, you visit the site."
    "You're greeted by a live feed of Leanne standing in her room, with a skimpy outfit just barely clinging to her body."
    leanne "Hey there everyone! This is Luxury Leanne coming at you with a special stream."
    leanne "Thanks to my sponsor, a little place known as the Triangle Club, you all get to see me in one of my cuter outfits today."
    leanne "They were also awesome enough to teach me some of their moves. Let's see if I can do them any justice."
    #Image: Stripper Leanne dancing around in her room.
    "Turning on some music that you've heard reverberate through the Triangle Club speakers, Leanne begins to move about the room."
    "While her dancing lacks the same professionalism as the girls at the club, she still manages to entertain the viewers and yourself well enough with the way she shakes around her body."
    #Image: Stripper Leanne continuing to dance with her top off.
    "In a single, fluid movement Leanne tears off her top to reveal her meaty breasts."
    "No longer held back by the restraining fabric, her tits are left free to jostle around with the music in unison with her belly rolls."
    #Image: Stripper Leanne continuing to dance with her panties off.
    "With the help of a few shimmies and the motivation of donations from her audience, she gladly shakes her hips to rid herself of her panties."
    "Left with her assets on full display, she throws her entire body into the rhythm of the music to both entertain and seduce her adoring fans."
    #Image: Stripper Leanne sitting at her desk.
    "Left sweaty and exhausted by the end of the song, Leanne goes back to her desk and slumps down in her chair."
    leanne "Whoo, that was a real work out. I don't know how those dancers do it on a daily basis."
    leanne "If you want to see how a professional does it, make sure you stop by and tell them I sent you. For now though, this is Luxury Leanne signing off!"
    "The stream ends."
    return
