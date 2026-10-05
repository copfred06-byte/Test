## LEANNE EVENTS

label leanne_introduction:
    pc "Hmm, I was interested in that streaming site, Fidget. Let me see what’s on there. Wait, I think that’s the person that absolutely destroyed me on Carl on Duty."
    image stream_girl_webcam = "/leanne/[leanne.stage]/webcam.webp"
    scene stream_girl_webcam
    play music "/music/leanne_stream.ogg" if_changed
    "You click on the stream to see a vibrant room of glowing pink colors and a woman sitting in a chair."
    "The skimpy outfit and pair of cat ears perched atop her twin, pink pigtails work with her wide smile to entice you to keep watching."
    leanne "Hey guys, my name is Luxury Leanne. Thank you, Sandclapper, I try my best. I'm doing well, Mando. Thanks for asking. How are you? My measurements?"
    image stream_girl_happy = "/leanne/[leanne.stage]/happy.webp"
    scene stream_girl_happy
    "She pauses for a moment before letting out a playful giggle."
    $ imperialweight = (leanne.weight * 2.2)
    leanne "Alright, but only because you asked nicely. I weigh [imperialweight:.02f] pounds or [leanne.weight:.02f]kg, my breasts fit snuggly into a [leanne.breast_cup] cup and measure [leanne.breast_size] inches across."
    leanne "My waist is close to [leanne.waist_size] inches and my hips are a little over [leanne.ass_size]. If that doesn’t answer your question, then how about I give a better demonstration?"
    image leanne_standup = "/leanne/[leanne.stage]/standup.webp"
    scene leanne_standup
    window hide
    pause
    image leanne_standupside = "/leanne/[leanne.stage]/standup_side.webp"
    scene leanne_standupside
    pause
    image leanne_standing = "/leanne/[leanne.stage]/standing.webp"
    scene leanne_standing
    "Standing up from her seat, Leanne changes various camera angles to show off different parts of her body. Once she’s finished, she sits back down."
    image leanne_showoff1 = "/leanne/events/stage1/showoff1.webp"
    scene leanne_showoff1
    pause
    image leanne_showoff2 = "/leanne/events/stage1/showoff2.webp"
    scene leanne_showoff2
    pause
    image leanne_showoff3 = "/leanne/events/stage1/showoff3.webp"
    scene leanne_showoff3
    pause
    leanne "Sorry if I'm looking a little malnourished. Some personal stuff has been going on."
    leanne "While we're on the topic, I want to remind everyone I will eat all the food donated to me. No exceptions. For now, let’s start up the game."
    $ leanne_stats_visible = 1
    image leanne_gaming = "/leanne/[leanne.stage]/gaming.webp"
    scene leanne_gaming
    "Leanne has been added to the stats page."
    "After watching her stream for a bit, your eyes grow tired and you decide to turn in for the night."
    stop music fadeout 1.0
    if recollection == False:
        $ daytime += 1
        jump freetime
    return

label Leanne_Stage_1_Event:
    image stream_girl_happy_event1 = "/leanne/1/happy.webp"
    scene stream_girl_happy_event1
    if recollection == False:
        $ money -= 5
    else:
        play music "/music/leanne_stream.ogg" if_changed
    leanne "Nice, someone made a pizza donation. Thank you so much! I'll order right away."
    "About ten minutes later the pizza arrives."
    image stream_girl_pizza_event1 = "/leanne/1/pizza.webp"
    scene stream_girl_pizza_event1
    "Opening up the box, she devours the entire thing like she hasn't eaten all day."
    image stream_girl_eating_event1 = "/leanne/1/eating.webp"
    scene stream_girl_eating_event1
    leanne "That really hit the spot. Thanks again for the donation."
    "Worried that she might not be eating enough off-stream, you ask Leanne if she is alright."
    image stream_girl_webcam_event1 = "/leanne/1/webcam.webp"
    scene stream_girl_webcam_event1
    leanne "I appreciate your concern, but I'm fine. I was just hungry."
    "Still a little concerned, you ask if she could stand up."
    leanne "Uh, sure."
    image leanne_standup_event1 = "/leanne/1/standup.webp"
    scene leanne_standup_event1
    window hide
    pause
    image leanne_standupside_event1 = "/leanne/1/standup_side.webp"
    scene leanne_standupside_event1
    window hide
    pause
    image leanne_standing_event1 = "/leanne/1/standing.webp"
    scene leanne_standing_event1
    "She stands up from her seat. Upon taking another look at her, you can’t help noticing that she is as skinny as a twig."
    pc "You’re looking really thin. Are you sure you’re okay?"
    "Leanne opens her mouth to speak, only to lower her head. A moment later, she looks back towards the camera with a much more somber expression on her face."
    leanne "Well, not really."
    image leanne_sad1 = "/leanne/events/stage1/sad1.webp"
    scene leanne_sad1
    leanne "I always relied on my boyfriend’s salary to get by. He left me for someone else about two months ago."
    leanne "I’ve been struggling with money ever since. I can’t remember the last time I had a decent meal."
    "She pauses to wipe her face with a handkerchief."
    image leanne_sad2 = "/leanne/events/stage1/sad2.webp"
    scene leanne_sad2
    leanne "I'm sorry. You all came to the stream for entertainment, not to hear about my burdens."
    "Moments after she finishes wiping away the tears, a massive amount of donations come flooding in."
    image leanne_sad3 = "/leanne/events/stage1/sad3.webp"
    scene leanne_sad3
    leanne "WHAT!? Is that real?"
    leanne "OMG it is! Thank you thank you thank you thank you!"
    image leanne_sad4 = "/leanne/events/stage1/sad4.webp"
    scene leanne_sad4
    leanne "Seriously, you don't know how much this means to me."
    image leanne_sad5 = "/leanne/events/stage1/sad5.webp"
    scene leanne_sad5
    leanne "You all are too much. You’re going to make me cry again."
    image leanne_sad6 = "/leanne/events/stage1/sad6.webp"
    scene leanne_sad6
    leanne "I think I’m going to go offline for now. It’s been a real emotional rollercoaster."
    leanne "Thanks again, everyone. See you next time!"
    stop music fadeout 1.0
    $ leannestage1event = 0
    if recollection == False:
        $ leanne.weight += 1
    return


label Leanne_Stage_2_Event_1:
    ##Scene: Dance/Exercise Introduction (Happens shortly after reaching stage 2)
    ##Note: Starts with standard option to watch Leanne stream. Upon being prompted to order a pizza, if the player says yes the following occurs.
    image stream_girl_happy_event2 = "/leanne/2/happy.webp"
    scene stream_girl_happy_event2
    if recollection == True:
        play music "/music/leanne_stream.ogg" if_changed
    leanne "Thank you so much for the pizza!"
    if recollection == False:
        $ money -= 5
    image stream_girl_pizza_event2 = "/leanne/2/pizza.webp"
    scene stream_girl_pizza_event2
    "Leanne quickly devours the pizza, showing just how hungry she was."
    image stream_girl_webcam_event2 = "/leanne/2/webcam.webp"
    scene stream_girl_webcam_event2
    leanne "Man that really hit the spot. Although, I am feeling a bit sluggish after that. Not to mention I’m feeling a little stiff from sitting here for so long."
    image leanne_standup_event2 = "/leanne/2/standup.webp"
    scene leanne_standup_event2
    "Leanne pauses the game and stands up from her desk."
    image leanne_standupside_event2 = "/leanne/2/standup_side.webp"
    scene leanne_standupside_event2
    window hide
    pause
    image leanne_standing_event2 = "/leanne/2/standing.webp"
    scene leanne_standing_event2
    pause
    leanne "Alright, let’s take a break and get moving. Loyal viewer, since you sent the pizza, you get to choose what I do first."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/leanne/2/idle.webm" loop
    show movie with dissolve
    ##Choice: Player is prompted to choose between Dance and Exercise routines
    menu:
        "Dance":
            ##Player Chooses Dance
            stop movie
            leanne "Oooh, sounds fun. I know just the song for it."
            image leanne_typing_event2 = "/leanne/2/typing.webp"
            scene leanne_typing_event2
            "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
            ##Dance animation starts.
            $ movielength = 35
            $ movieplaying = "/images/leanne/2/dance1.webm"
            call screen custommoviescreen
            window hide
            pause
            image stream_girl_webcam_event2 = "/leanne/2/webcam.webp"
            scene stream_girl_webcam_event2
            "After the song concludes, Leanne sits back down at her desk."
            leanne "That was just what I needed. Now I’m all limbered up and you all got a bit of a show. I’ll have to do this again sometime."
            ##Rest of the scene plays out as is.
        "Excercise":
            ##Player Chooses Exercise
            stop movie
            leanne "Okay. Can’t say I’m too thrilled about doing this on a full tummy, but here I go."
            ##Exercise animation starts
            $ movielength = 25
            $ movieplaying = "/images/leanne/2/excercise.webm"
            call screen custommoviescreen
            window hide
            pause
            "After completing several reps, Leanne sits back at her desk and wipes her face off with a towel."
            image stream_girl_towel_event2 = "/leanne/2/towel.webp"
            scene stream_girl_towel_event2
            leanne "I’m a little sweaty, but I think that worked. I should be ready to get back to the game now."
            image stream_girl_webcam_event2 = "/leanne/2/webcam.webp"
            scene stream_girl_webcam_event2
            ##Rest of the scene plays out.
    ##From this point forward, the player can choose between the dance and exercise upon donating a pizza to Leanne.
    image stream_girl_side_event2 = "/leanne/2/side.webp"
    scene stream_girl_side_event2
    leanne "Now, let's play some more Carl on Duty."
    image stream_girl_gaming_event2 = "/leanne/2/gaming.webp"
    scene stream_girl_gaming_event2
    "You watch her play games until you go to bed."
    stop music fadeout 1.0
    if recollection == False:
        $ leanne.weight += 1
    $ leannestage2event = 0
    return

label Leanne_Stage_2_Event_2:
    ##Scene: Anime Introduction (Happens near the end of Stage 2 upon Leanne reaching the weight needed for Stage 3)
    image leanne_stage2_arrive = "/leanne/events/stage2/arrive.webp"
    scene leanne_stage2_arrive
    play music "/music/leanne_stream2.ogg" if_changed
    "You turn into the stream to find something different. The usual bright pinks that illuminate Leanne’s room are replaced with more natural light."
    "Things are further distinguished from the typical streaming venue as she’s dressed in a sweater and pants rather than her typical skimpy outfit."
    "Though it looks modest at first, you notice how the sweater emphasizes her bosom, much to the delight of the people tuning in."
    ##Image: Leanne appears with the sweater on, but still without glasses and her pink hair in twin pigtails.
    leanne "Hey guys! I have something a little different for today. Since Carl on Duty is currently down for maintenance, I’d thought we’d do something new."
    image leanne_stage2_1 = "/leanne/events/stage2/1.webp"
    scene leanne_stage2_1
    "Leanne reaches below the desk and pops back up with an anime DVD case in her hands. The cover depicts an anime girl in a maid outfit with metal seams along parts of her body."
    image leanne_stage2_2 = "/leanne/events/stage2/2.webp"
    scene leanne_stage2_2
    leanne "I thought I’d get a chance to talk about one of my favorite anime that’s more on the obscure side. Maid Mecha wasn’t given its time to shine when it first came out and I hope to change that."
    "Leanne begins to break down the anime and praise its qualities. You can tell by the way she talks that she’s very passionate about the show."
    "Though a few people tune out of the stream, she seems to be keeping her viewers’ attention long enough to finish off her review."
    image leanne_stage2_3 = "/leanne/events/stage2/3.webp"
    scene leanne_stage2_3
    leanne "In conclusion, Maid Mecha may look like a shallow, fanservice show at first, but it has a heart I can’t say I’ve seen in many other anime."
    leanne "If you’re ever lucky enough to come across a copy, make sure you snatch it up quick."
    leanne "Last I checked, it’s not on any streaming services and the DVDs are at an all-time high online."
    "You recall hearing about an anime store somewhere in town that might be worth checking out later."
    image leanne_stage2_4 = "/leanne/events/stage2/4.webp"
    scene leanne_stage2_4
    "Anime store unlocked!"
    $ animestoreunlock = 1
    leanne "Anyway, that’s all for tonight. Sorry for the short stream, but I have a few things to take care of."
    leanne "Don’t worry, when Carl on Duty comes back online I’ll be sure to be there to show off my skills. This is Luxury-"
    image leanne_stage2_5 = "/leanne/events/stage2/5.webp"
    scene leanne_stage2_5
    "In the middle of Leanne’s sign off, a stray bump of her arm against her drink cup sends a splatter of soda through the air."
    "Though a good bit of the mess stains her sweater, the most damage is done to her precious DVD."
    "Holding up the case between her fingers, she looks distraught as the maid’s face is distorted by the soda."
    image leanne_stage2_eventend = "/leanne/events/stage2/eventend.webp"
    scene leanne_stage2_eventend
    leanne "I’ll…see you all next time."
    "She abruptly shuts off the stream."
    stop music fadeout 1.0
    $ leannestage2event2 = 0
    return

label Leanne_Stage_3_Event:
    ##Note: At the start of this stage the player will be given the option to visit the anime store during their free time.
    ##Scene: Anime Store First Visit (Occurs after the player character chooses to go to the anime store)
    ##Image: Anime store
    play music "/music/anime_store.ogg" if_changed
    image leanne_stage3_arrive = "/leanne/events/stage3/arrive.webp"
    scene leanne_stage3_arrive
    "Walking through the door, you're assaulted by a song from an anime you don't recognize being blasted over the speaker system."
    "Various displays are put up with screens displaying random clips from shows."
    "Looking past the shelves of countless manga, anime, Japanese game imports, and questionably legal hentai, you turn your attention towards the front counter."
    "Waiting there is a balding man in his 40s that only looks away from his phone once you knock on the counter."
    image leanne_stage3_1 = "/leanne/events/stage3/1.webp"
    scene leanne_stage3_1
    animestore "Sorry, didn’t see you there. Anything I can help you with?"
    pc "Yes. I was hoping you could help me find something a little obscure. It's called Maid Mecha."
    image leanne_stage3_2 = "/leanne/events/stage3/2.webp"
    scene leanne_stage3_2
    "He grins in a way that sends a shiver down your spine."
    animestore "Oh, that’s a good one. An absolute classic that belongs on any self-respecting collector’s shelf."
    pc "Do you have a copy?"
    image leanne_stage3_3 = "/leanne/events/stage3/3.webp"
    scene leanne_stage3_3
    "The clerk lets out a chuckle."
    animestore "I said SHOULD belong on the shelf. I didn’t say it would without some luck."
    pc "Isn’t there some way I can grab a copy?"
    image leanne_stage3_4 = "/leanne/events/stage3/4.webp"
    scene leanne_stage3_4
    "The clerk scratches the stubble around his chin."
    "I typically get some new shipments in on Saturdays. Tell you what, leave me your number and I’ll give you a call if a copy happens to show up."
    pc "Thanks. That would be great."
    "After handing over your name and number you turn to leave the store."
    image leanne_stage3_5 = "/leanne/events/stage3/5.webp"
    scene leanne_stage3_5
    "On the way out you let your gaze linger a little too long on a risqué manga cover and end up bumping into another customer."
    pc "Sorry. I was a little distracted by…"
    ##(NOTE: Show image of disguised Leanne, big bulky hoodie, maybe a small bump in the mid-section to show off her current weight, and a single strand of pink hair peeking out.)
    image leanne_stage3_6 = "/leanne/events/stage3/6.webp"
    scene leanne_stage3_6
    "You pause as you get a chance to get a look at the person. Though their body is mostly covered by a hoodie, you can’t help feeling like you recognize their curves."
    "Just as your eyes lock onto a singular lock of pink hair, they push past you."
    $ unknownname = 'Hooded Woman'
    unknown "Sorry, I have to go."
    image leanne_stage3_eventend = "/leanne/events/stage3/eventend.webp"
    scene leanne_stage3_eventend
    "The woman rushes over to the counter. Rather than dwell on it, you exit the shop and return home."
    $ unknownname = 'Unknown'
    $ leannestage3event = 0
    stop music fadeout 1.0
    if recollection == False:
        $ daytime += 1
        jump freetime
    return

label Leanne_Stage_4_Event_1:
    ##Scene: Maid Cosplay Plea (Occurs when the player chooses to watch the stream after visiting the anime store and reaching the needed weight for stage 4)
    image leanne_stage4_1 = "/leanne/events/stage4/1.webp"
    scene leanne_stage4_1
    play music "/music/leanne_stream2.ogg" if_changed
    "Upon opening up the stream, you can instantly tell that something is different."
    ##(IMAGE NOTE: Leanne in a maid uniform similar to the ones used by those in the anime)
    leanne "Hey there, everyone! Luxury Leanne here for another stream. As you've probably noticed, I'm wearing a little something special today and for good reason."
    image leanne_stage4_2 = "/leanne/events/stage4/2.webp"
    scene leanne_stage4_2
    "Leanne gets closer to the camera, centering the view on her face and bosom."
    leanne "Vigilant viewers will no doubt recognize that I’m wearing a replica Maid Mecha uniform. I will admit, it’s a little on the cheap side, but I think it gets my point across."
    image leanne_stage4_3 = "/leanne/events/stage4/3.webp"
    scene leanne_stage4_3
    window hide
    pause
    image leanne_stage4_4 = "/leanne/events/stage4/4.webp"
    scene leanne_stage4_4
    "She sits back down in her chair, very unsubtly shaking her hips to ruffle the edges of the skirt."
    image leanne_stage4_5 = "/leanne/events/stage4/5.webp"
    scene leanne_stage4_5
    leanne "A while back I made a little oopsie and destroyed my precious DVD copy of Maid Mecha."
    image leanne_stage4_6 = "/leanne/events/stage4/6.webp"
    scene leanne_stage4_6
    leanne "So, I’m putting out a bounty for any lucky viewer who manages to track down a copy and send it to me. The winner will get to have a special play session with yours truly."
    "Now with two reasons to get your hands on the DVD, you think it’s best to start saving up your money now."
    image leanne_stage4_7 = "/leanne/events/stage4/7.webp"
    scene leanne_stage4_7
    leanne "Anyway, that’s all for now. I’ll keep you updated on the hunt. Let’s get back to Carl on Duty."
    image leanne_stage4_8 = "/leanne/events/stage4/8.webp"
    scene leanne_stage4_8
    "Save for a few extra glamour shots of Leanne in her maid outfit, the stream goes as usual."
    image leanne_stage4_9 = "/leanne/events/stage4/9.webp"
    scene leanne_stage4_9
    window hide
    pause
    image leanne_stage4_10 = "/leanne/events/stage4/10.webp"
    scene leanne_stage4_10
    pause
    image leanne_stage4_11 = "/leanne/events/stage4/11.webp"
    scene leanne_stage4_11
    pause
    image leanne_stage4_12 = "/leanne/events/stage4/12.webp"
    scene leanne_stage4_12
    pause
    image leanne_stage4_eventend = "/leanne/events/stage4/eventend.webp"
    scene leanne_stage4_eventend
    "The stream ends."
    stop music fadeout 1.0
    $ leannestage4event = 0
    return

label Leanne_Stage_4_Event_2:
    ##SCENE: Dance 2 Unlock (Occurs after maid cosplay stream)
    "You decide to watch Leanne’s stream."
    image stream_girl_webcam_event4 = "/leanne/4/webcam.webp"
    scene stream_girl_webcam_event4
    play music "/music/leanne_stream.ogg" if_changed
    leanne "Hey everyone! Luxury Leanne here. We’re streaming Carl on Duty again today, but I have a special treat if someone hits this little button here."
    "On the side of the stream, you notice an extra option pop up that allows you to donate five pizzas at once."
    image leanne_stage4_point = "/leanne/events/stage4/point.webp"
    scene leanne_stage4_point
    leanne "Your eyes aren’t fooling you. Press this little button to donate the equivalent of five pizzas to me."
    leanne "Most of the money will go towards keeping me fed with delicious pizza, while the rest will go to helping me reclaim my lost Maid Mecha DVD."
    leanne "First one that uses it gets to see something brand new."
    ##Player Choice: Press the button (-$25) or Don’t press the button
    menu:
        "Press the button. (-$25)":
            if money <= 24:
                "You do not have enough money to buy Leanne 5 Pizzas."
                image stream_girl_side_event4 = "/leanne/4/side.webp"
                scene stream_girl_side_event4
                "The stream continues as normal."
                image leanne_stage4_point = "/leanne/events/stage4/point.webp"
                scene leanne_stage4_point
                leanne "Alright, I think I’m ready to call it for tonight."
                leanne "Don’t worry if you missed your chance, the big pizza button will be here next stream if anyone wants to help me out with food and my DVD quest."
                leanne "Until next time, this is Luxury Leanne signing off."
                if recollection == False:
                    $ leanne.weight += 0.1
            else:
                ##If the player chooses Press the button.
                image stream_girl_happy_event4 = "/leanne/4/happy.webp"
                scene stream_girl_happy_event4
                "Leanne pauses the game to show off a wide smile."
                if recollection == False:
                    $ money -= 25
                leanne "Thank you soooooooooo much. I’ll go ahead and order the pizzas right away. While I’m waiting for that though, I think it’s time I give you a prize."
                image leanne_standup_event4 = "/leanne/4/standup.webp"
                scene leanne_standup_event4
                window hide
                pause
                image leanne_standupside_event4 = "/leanne/4/standup_side.webp"
                scene leanne_standupside_event4
                pause
                image leanne_standing_event4 = "/leanne/4/standing.webp"
                scene leanne_standing_event4
                pause
                ##(Animation: Dance 2 plays)
                $ renpy.movie_cutscene("/images/leanne/4/dance2.webm", stop_music=False)
                image leanne_dance2end_event4 = "/leanne/4/dance2end.webp"
                scene leanne_dance2end_event4
                window hide
                pause
                image stream_girl_webcam_event4 = "/leanne/4/webcam.webp"
                scene stream_girl_webcam_event4
                leanne "Hope you liked it. Oh, and just in time too."
                image stream_girl_pizzastack_event4 = "/leanne/4/pizzastack.webp"
                scene stream_girl_pizzastack_event4
                "Leanne walks offscreen for a moment, only to come back with her arms burdened with five pizza boxes."
                "Wasting little time, she opens up the first box and scarfs down the slices as fast as possible."
                image stream_girl_eating_event4 = "/leanne/4/eating.webp"
                scene stream_girl_eating_event4
                leanne "Hmmm, as good as always. I’ll work on the rest of these as we play."
                image stream_girl_gaming_event4 = "/leanne/4/gaming.webp"
                scene stream_girl_gaming_event4
                "The stream goes as usual, albeit with more frequent breaks to allow Leanne to eat more pizza."
                "Towards the end of the night, her eating slows down. However, she manages to get through pizza number three before she has to give up."
                image stream_girl_eating2_event4 = "/leanne/4/eating2.webp"
                scene stream_girl_eating2_event4
                pause
                image stream_girl_stuffed_event4 = "/leanne/4/stuffed.webp"
                scene stream_girl_stuffed_event4
                leanne "I think that’s going to do it for me."
                image stream_girl_stuffed2_event4 = "/leanne/4/stuffed2.webp"
                scene stream_girl_stuffed2_event4
                "Leanne leans back, showing her stuffed tummy."
                image stream_girl_stuffed3_event4 = "/leanne/4/stuffed3.webp"
                scene stream_girl_stuffed3_event4
                leanne "Sorry I couldn’t finish all of it, but I don’t think I’ve ever eaten this much in one sitting. I’ll make sure to take care of the rest later. Until next time, this is Luxury Leanne signing off."
                image stream_girl_stuffed_goodbye_event4 = "/leanne/4/stuffed_goodbye.webp"
                scene stream_girl_stuffed_goodbye_event4
                "The stream ends."
                if recollection == False:
                    $ leanne.weight += 1.5
                $ leannestage4event2 = 0

        "Don't press the button.":
            ##If player chooses Don’t press the button
            image stream_girl_side_event4 = "/leanne/4/side.webp"
            scene stream_girl_side_event4
            "The stream continues as normal."
            image leanne_stage4_point = "/leanne/events/stage4/point.webp"
            scene leanne_stage4_point
            leanne "Alright, I think I’m ready to call it for tonight."
            leanne "Don’t worry if you missed your chance, the big pizza button will be here next stream if anyone wants to help me out with food and my DVD quest."
            leanne "Until next time, this is Luxury Leanne signing off."
            if recollection == False:
                $ leanne.weight += 0.1
    stop music fadeout 1.0
    return

label Leanne_Stage_5_Event_1:
    ##Scene: Weight Questions (Should occur upon her reaching stage 5 weight and choosing to watch her stream)
    image leanne_stage5_1 = "/leanne/events/stage5/1.webp"
    scene leanne_stage5_1
    play music "/music/leanne_stream2.ogg" if_changed
    "You tune in to the stream and immediately take notice of the extra chub around Leanne’s waist."
    "Judging by what’s being said in the chat, you’re not the only one who’s focused on her added weight."
    leanne "Hey everyone! Luxury Leanne back once again to entertain the masses. Carl on Duty is down for maintenance for a bit, so I’ll be using the first part of the stream for Q and A. Donators get to-"
    "Leanne pauses as her eyes follow a highlighted question on the chat stream."
    image leanne_stage5_2 = "/leanne/events/stage5/2.webp"
    scene leanne_stage5_2
    if persistent.imperial:
        $ imperialweight = (leanne.weight * 2.2)
        leanne "How much do I weigh? A weird way to start, but okay. My current weight is [imperialweight:.02f]lbs. As for the rest…"
    else:
        leanne "How much do I weigh? A weird way to start, but okay. My current weight is [leanne.weight:.02f]kg. As for the rest…"
    "Leanne makes sure the chat has a good look at her body."
    image leanne_stage5_3 = "/leanne/events/stage5/3.webp"
    scene leanne_stage5_3
    window hide
    pause
    image leanne_stage5_4 = "/leanne/events/stage5/4.webp"
    scene leanne_stage5_4
    if persistent.imperial:
        leanne "I’ve got a [leanne.waist_size] inch waist."
    else:
        $ metricwaist_size = (leanne.waist_size * 2.54)
        leanne "I’ve got a [metricwaist_size:.02f] cm waist."
    image leanne_stage5_5 = "/leanne/events/stage5/5.webp"
    scene leanne_stage5_5
    window hide
    pause
    image leanne_stage5_6 = "/leanne/events/stage5/6.webp"
    scene leanne_stage5_6
    pause
    image leanne_stage5_butt1 = "/leanne/events/stage5/butt1.webp"
    scene leanne_stage5_butt1
    "Leanne turns to have her butt close to the camera."
    image leanne_stage5_butt2 = "/leanne/events/stage5/butt2.webp"
    scene leanne_stage5_butt2
    if persistent.imperial:
        leanne "My hips are [leanne.ass_size] inches wide."
    else:
        $ metricass_size = (leanne.ass_size * 2.54)
        leanne "My hips are [metricass_size:.02f] cm wide."
    image leanne_stage5_breasts1 = "/leanne/events/stage5/breasts1.webp"
    scene leanne_stage5_breasts1
    "Leanne leans forward to give a good view of her cleavage."
    image leanne_stage5_breasts2 = "/leanne/events/stage5/breasts2.webp"
    scene leanne_stage5_breasts2
    if persistent.imperial:
        leanne "My bosom is [leanne.breast_size] inches across and fit comfortably into a [leanne.breast_cup] bra. If you didn’t get a good look, let me go ahead and make sure my viewers see all of it at once."
    else:
        $ metricbreast_size = (leanne.breast_size * 2.54)
        leanne "My bosom is [metricbreast_size:.02f] cm across and fit comfortably into a [leanne.breast_cup] bra. If you didn’t get a good look, let me go ahead and make sure my viewers see all of it at once."
    "Stepping back from the camera, Leanne breaks out into a dance that flings about her added heft."
    window hide
    pause
    $ movielength = 35
    $ movieplaying = "/images/leanne/events/stage5/stage5dance.webm"
    call screen custommoviescreen
    pause
    "The jiggle of her curves leaves you in a sort of trance. It makes you memorize every inch of her in the process."
    image leanne_stage5_5 = "/leanne/events/stage5/5.webp"
    scene leanne_stage5_5
    leanne "Hope you enjoyed that."
    "Taking her spot back at her desk, she once more scrolls through the chat."
    leanne "Alright, let's see... Ah, here's one. 'Are you okay with gaining weight like this?' Of course I am."
    leanne "After being so skinny for so long, it's kind of nice not being hungry all of the time."
    leanne "Plus, all of this is just a sign of how much you all have been helping me out with my streams. Thanks a bunch! That being said, I could always use a little more."
    image leanne_stage5_point = "/leanne/events/stage5/point.webp"
    scene leanne_stage5_point
    "Turning to the side, Leanne not so subtly points to her pizza donation buttons."
    leanne "Anyway, I think that'll do it for questions for the day. Looks like the game is back up. Let's get back to business."
    stop music fadeout 1.0
    ##(Note: From here the stream continues as normal with the typical text prompts and options to give her pizza)
    $ leannestage5event = 0
    return

label Leanne_Stage_5_Event_2:
    play music "/music/leanne_stream.ogg" if_changed
    image leanne_stage5_7 = "/leanne/events/stage5/7.webp"
    scene leanne_stage5_7
    "You enter Leanne's stream, greeted by the familiar sight of her lounging in her gaming chair, one hand on her mouse, the other casually grabbing a nearby chicken nugget."
    "The glow of the monitor reflects off her round cheeks as she focuses on the game, her brows furrowed in concentration."
    image leanne_stage5_8 = "/leanne/events/stage5/8.webp"
    scene leanne_stage5_8
    "The chat is as lively as ever, scrolling at breakneck speed."
    #"Leanne, focus! You’re on a streak!"
    #"She’s actually trying, LMAO."
    #"Snack break when?"
    image leanne_stage5_9 = "/leanne/events/stage5/9.webp"
    scene leanne_stage5_9
    "Leanne's stream has a certain rhythm. Play, banter, snack, repeat. Right now, she's in the play phase, fully locked in."
    "You watch as she racks up another kill, her smirk growing as her team pulls ahead."
    image leanne_stage5_10 = "/leanne/events/stage5/10.webp"
    scene leanne_stage5_10
    leanne "Boom! That's how it's done,"
    image leanne_stage5_11 = "/leanne/events/stage5/11.webp"
    scene leanne_stage5_11
    "She grabs a fry without even looking away from the screen." 
    image leanne_stage5_12 = "/leanne/events/stage5/12.webp"
    scene leanne_stage5_12
    "She pops it into her mouth, her voice muffled as she adds."
    image leanne_stage5_13 = "/leanne/events/stage5/13.webp"
    scene leanne_stage5_13
    leanne "This lobby's free. Next."
    "Just as she lines up her next shot—BANG!"
    image leanne_stage5_14 = "/leanne/events/stage5/14.webp"
    scene leanne_stage5_14
    "Her screen goes red."
    "You were eliminated by MiraByte."
    image leanne_stage5_15 = "/leanne/events/stage5/15.webp"
    scene leanne_stage5_15
    "The kill feed confirms it, and within seconds, chat explodes."
    #"OH SHIT, IT’S MIRA!"
    #"NO WAY LMAO"
    #"SNIPEDDDD."
    "Leanne freezes for half a second. Not enough for the casual viewer to notice, but you catch the shift—the slight narrowing of her eyes, the twitch in her lips before she forces them into a smirk."
    image leanne_stage5_16 = "/leanne/events/stage5/16.webp"
    scene leanne_stage5_16
    leanne "Oh wow, chat."
    leanne "Look who it is. What a totally unexpected surprise."
    "You already know who she's talking about. MiraByte."
    "The long-time rival. The fitness-obsessed, trash-talking contrast to Leanne's more indulgent, laid-back style."
    "Where Leanne embraced her softer image—both in personality and figure—Mira played up her speed and precision, always throwing shade whenever their paths crossed."
    image leanne_stage5_17 = "/leanne/events/stage5/17.webp"
    scene leanne_stage5_17
    "A donation pops up on-screen."
    "💰 $10 – MiraByte: Hey, Lyn. Maybe if you weren’t weighed down so much, you could dodge my shots. Just saying."
    image leanne_stage5_18 = "/leanne/events/stage5/18.webp"
    scene leanne_stage5_18
    "The chat loses it."
    #"OH SHIT SHE WENT THERE."
    #"LMAO MIRABYTE JUST COOKED YOU."
    #"Leanne, you gonna take that??"
    "For a moment, Leanne just stares at the screen, fingers lightly drumming on her desk."
    image leanne_stage5_19 = "/leanne/events/stage5/19.webp"
    scene leanne_stage5_19
    "Then, without a word, she grabs a chocolate bar from her side table, slowly unwrapping it. The deliberate movement makes chat go wild."
    #"NO WAY SHE’S DOING THIS LMAOO."
    #"Mira’s gonna lose it."
    #"POWER MOVE."
    image leanne_stage5_20 = "/leanne/events/stage5/20.webp"
    scene leanne_stage5_20
    "She takes a big, exaggerated bite, chewing slowly before leaning into the mic."
    image leanne_stage5_21 = "/leanne/events/stage5/21.webp"
    scene leanne_stage5_21
    leanne "You might be able to snipe me in-game, Mira."
    leanne "but I'm still ahead of you in views. So enjoy your little moment."
    image leanne_stage5_22 = "/leanne/events/stage5/22.webp"
    scene leanne_stage5_22
    "She hums, savoring the taste."
    leanne "Mmm. Victory's sweet."
    image leanne_stage5_23 = "/leanne/events/stage5/23.webp"
    scene leanne_stage5_23
    "Chat erupts."
    "Mira hasn't responded yet, but you already know this won't be the last time these two cross paths."
    image leanne_stage5_9 = "/leanne/events/stage5/9.webp"
    scene leanne_stage5_9
    "You watch the rest of the stream until she finishes up her gaming session and then you head to bed."
    stop music fadeout 1.0
    if recollection == False:
        $ daytime += 1
        $ leanne.weight += 0.5
    $ leannestage5event2 = 0
    return

label Leanne_Stage_6_Event_1:
    ##Scene: Anime store meeting with Lyn. (Occurs on the first Saturday after reaching the weight requirements for Stage 6.)
    "As you ponder what you’re going to do for the day, an unknown number calls."
    pc "Hello?"
    $ gabe = "???"
    animestore "Hey, this is Gabe from the anime store. You’re the guy who wanted the Maid Mecha DVD, right?"
    pc "Yes. Did you get a copy in?"
    $ gabe = "Gabe"
    animestore "Yeah, but only one."
    pc "That shouldn’t be a problem. I only need the one."
    animestore "Well, it is a problem when you're not the only person who wants it. I already called up the other customer and they said they're on their way."
    pc "Can’t you hold it for me?"
    animestore "Sorry, first come first served. Now get on down here as fast as you can if you want to claim it. Oh, and don't forget the money."
    "Hanging up your phone, you grab your stuff and rush out the door."
    ##Image: Anime Store
    play music "/music/anime_store.ogg" if_changed
    image leanne_stage6_1 = "/leanne/events/stage6/1.webp"
    scene leanne_stage6_1
    "Bursting through the door, your heart sinks as you arrive just in time to see Gabe hand the DVD over to a customer in a hoodie."
    pc "Excuse me, but could I please have that? It’s very important that I-"
    "You stop talking as the customer turns around."
    image leanne_stage6_2 = "/leanne/events/stage6/2.webp"
    scene leanne_stage6_2
    ##Image: Leanne/Lyn in her incognito outfits, with a pair of glasses, most of her pink hair obscured, and wearing a hoodie that’s a little too small for her curves.
    "You stumble on your words as you look over the woman. Though you don’t fully recognize the face with the glasses, her body’s curves seem familiar."
    "It feels like you’ve spent a lot of time gawking at them. As things start to click in your head, you finally understand what’s going on upon seeing a strand of pink hair dangling in front of her face."
    pc "Oh my god, it’s you. Luxury Lea-"
    image leanne_stage6_3 = "/leanne/events/stage6/3.webp"
    scene leanne_stage6_3
    "You are left silent again, this time by having a hand shoved up against your face."
    image leanne_stage6_4 = "/leanne/events/stage6/4.webp"
    scene leanne_stage6_4
    leanne "Zip it. Last thing I need is someone recognizing me out in the open."
    animestore "Is everything okay over there?"
    image leanne_stage6_5 = "/leanne/events/stage6/5.webp"
    scene leanne_stage6_5
    "Leanne spins on her heels and shows a bright smile towards the sales clerk."
    leanne "Yes, everything is just fine. Just a little fun between old friends."
    image leanne_stage6_6 = "/leanne/events/stage6/6.webp"
    scene leanne_stage6_6
    "Grasping your arm, Leanne drags you towards the exit."
    leanne "Come on. Let's head to that eatery we always go to. You know the one, right?"
    pc "Er, yeah. I know what you’re talking about."
    stop music fadeout 1.0
    #Image: Bunny Bites
    image leanne_stage6_7 = "/leanne/events/stage6/7.webp"
    scene leanne_stage6_7
    play music "/music/bunny_bites.ogg" if_changed
    "After a very awkward commute through town, you and Leanne manage to make your way to Bunny Bites."
    ##Image: Leanne sitting across from the player at a table with a look of exasperation on her face.
    leanne "Did you really have to choose a place like this? The waitresses here are dressed like they’re ready to strip at a moment’s notice."
    pc "It’s the first thing that came to mind. Besides, I don’t know why you’re so worried. You’re always wearing less clothes. At this point it’s part of Luxury Leanne’s-"
    image leanne_stage6_8 = "/leanne/events/stage6/8.webp"
    scene leanne_stage6_8
    "You’re silenced once more by Leanne holding up her hand."
    leanne "Like I said, I don’t want people finding out who I am. So please stop saying that name out loud. It’s not even my real name."
    pc "Okay then. What do you want me to call you?"
    image leanne_stage6_9 = "/leanne/events/stage6/9.webp"
    scene leanne_stage6_9
    "Leanne is silent for a moment, her fingers tapping against the table as she thinks."
    leanne "Lyn. You can call me Lyn."
    pc "Woah. Is that your real name?"
    $ leanne.name = 'Lyn'
    $ Lynname = 'Lyn'
    image leanne_stage6_10 = "/leanne/events/stage6/10.webp"
    scene leanne_stage6_10
    leanne "Yeah, and if anyone finds out I’ll know who to blame."
    image leanne_stage6_11 = "/leanne/events/stage6/11.webp"
    scene leanne_stage6_11
    "Lyn goes silent for a moment, passing the time by sipping on her soda. Feeling an air of awkwardness surround the table, you try to make conversation."
    pc "Still kind of hard to believe that I’d run into you at a random anime shop."
    image leanne_stage6_12 = "/leanne/events/stage6/12.webp"
    scene leanne_stage6_12
    leanne "Well, things just happen and I have to deal with them sometimes. Like having to start up a streaming channel just to make ends meet."
    pc "Right. Sorry about your ex-boyfriend treating you so badly."
    image leanne_stage6_13 = "/leanne/events/stage6/13.webp"
    scene leanne_stage6_13
    "Lyn gives you a look of confusion."
    leanne "What are you…OH! That, right. I forgot I told that story on stream."
    pc "How could you forget about that kind of thing?"
    image leanne_stage6_14 = "/leanne/events/stage6/14.webp"
    scene leanne_stage6_14
    "She lets a smirk show on her face."
    leanne "When I completely make it up."
    pc "Wait, what?"
    image leanne_stage6_15 = "/leanne/events/stage6/15.webp"
    scene leanne_stage6_15
    "She leans forward, fully showing off her smile."
    leanne "You heard me. I made it up. Don’t give me that look. You tend to do a lot of strange and unusual things when you’re flat broke."
    pc "That still seems pretty dishonest."
    leanne "I’m not saying what I’m doing is moral, but it’s what I needed to do to make sure I could keep eating."
    image leanne_stage6_16 = "/leanne/events/stage6/16.webp"
    scene leanne_stage6_16
    "Getting up from her seat, she rests her hands against her prominent belly."
    leanne "Considering I have this lump here, it’s safe to say that my plan worked."
    pc "It’s still unethical."
    image leanne_stage6_17 = "/leanne/events/stage6/17.webp"
    scene leanne_stage6_17
    "Sitting back down, she leans forward to look you in the eyes."
    leanne "Not like you have much room to talk. I’m sure that more than a few of my extra pounds are thanks to you. Am I wrong?"
    pc "No comment."
    image leanne_stage6_18 = "/leanne/events/stage6/18.webp"
    scene leanne_stage6_18
    "She lets out a giggle. The laughter lacks some of the bubbliness of Leanne. You realize this is the first time you’ve heard her actual laugh."
    leanne "Well, if you don’t want to admit to helping me with my strange kink, then let me ask you a question."
    image leanne_stage6_19 = "/leanne/events/stage6/19.webp"
    scene leanne_stage6_19
    "Reaching into her pocket, she pulls out the Maid Mecha DVD."
    leanne "Mind telling me why you wanted to get this? Pretty sure you could just pirate it on some site if you looked hard enough."
    ##Player Choice: A) Your review really convinced me to track it down or B) I wanted to give you a replacement for the one you lost.
    menu:
        "Your review really convinced me to track it down.":
            image leanne_stage6_20 = "/leanne/events/stage6/20.webp"
            scene leanne_stage6_20
            "She leans back and adjusts her glasses. The look on her face is one of pleasant surprise."
            leanne "Really? From my review?"
            pc "Yeah. You seemed really passionate about the show. I wanted to see what it was all about."
            image leanne_stage6_21 = "/leanne/events/stage6/21.webp"
            scene leanne_stage6_21
            leanne "Considering how few views the VOD got, I had assumed people weren’t paying attention. I do want to try giving the review thing another chance at some point."
            pc "I say go for it. A little variety never hurts."
        "I wanted to give you a replacement for the one you lost.":
            image leanne_stage6_22 = "/leanne/events/stage6/22.webp"
            scene leanne_stage6_22
            "Leanne lets out another giggle as she leans a little closer."
            leanne "Just another way to support your favorite streamer, huh?"
            pc "I mean, you were so passionate about the show, not to mention how disheartened you looked when it was destroyed."
            pc "On top of all that was the special stream with the maid outfit and your plea for help."
            image leanne_stage6_23 = "/leanne/events/stage6/23.webp"
            scene leanne_stage6_23
            leanne "Woah, slow down there. I think you got your point across. Even if you’re a little fanatical, I do appreciate the effort."
    image leanne_stage6_24 = "/leanne/events/stage6/24.webp"
    scene leanne_stage6_24
    marie "Are you two ready to order?"
    leanne "I honestly don’t know what to get. You seem to know what’s good around here. I’ll let you decide."
    pc "Really? If that’s the case, then I think you should try…"
    ##(Note: Player is given the option of picking from several different menu items to have Leanne/Lyn eat in front of them. Up to you on which scenes you’re willing to create)
    menu:
        "Burger":
            image leanne_stage6_25 = "/leanne/events/stage6/25.webp"
            scene leanne_stage6_25
            "She eats her food with astounding speed, making you think she hasn’t eaten anything all day."
        "Meatball Sub":
            image leanne_stage6_26 = "/leanne/events/stage6/26.webp"
            scene leanne_stage6_26
            "She eats her food with astounding speed, making you think she hasn’t eaten anything all day."
        "Chicken Nuggets":
            image leanne_stage6_27 = "/leanne/events/stage6/27.webp"
            scene leanne_stage6_27
            "She eats her food with astounding speed, making you think she hasn’t eaten anything all day."
    if recollection == False:
        $ leanne.weight += 0.5
    image leanne_stage6_28 = "/leanne/events/stage6/28.webp"
    scene leanne_stage6_28
    leanne "Hmm, you were right. That was pretty good. I’ll cover the bill this time. Let’s call it some insurance for keeping my little secret."
    pc "I promise I won’t tell anyone."
    image leanne_stage6_29 = "/leanne/events/stage6/29.webp"
    scene leanne_stage6_29
    leanne "And do you promise to not talk about any of our future meetings?"
    pc "What?"
    image leanne_stage6_30 = "/leanne/events/stage6/30.webp"
    scene leanne_stage6_30
    "Reaching across the table, she grabs your phone and puts in her number."
    leanne "It’s kind of nice to talk to someone who knows my big secret. It’s like getting a huge weight off of my shoulders."
    "She hands back your phone."
    leanne "You’re not against seeing me IRL again, right?"
    pc "No, of course not."
    image leanne_stage6_31 = "/leanne/events/stage6/31.webp"
    scene leanne_stage6_31
    "She lets out another laugh."
    leanne "Then it’s a date. I’ll message you when I have some free time to let off some steam."
    ##Leanne/Lyn can now send messages to the player
    image leanne_stage6_eventend = "/leanne/events/stage6/eventend.webp"
    scene leanne_stage6_eventend
    "Finishing up with the bill, you say goodbye to her and head home."
    stop music fadeout 1.0
    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
    $ leannestage6event = 0
    return

label Leanne_Stage_6_Event_2:
    ##Scene: Post-IRL Meeting Stream (Occurs the next time the player chooses to watch Leanne’s stream)
    image stream_girl_webcam_event6 = "/leanne/6/webcam.webp"
    scene stream_girl_webcam_event6
    play music "/music/leanne_stream.ogg" if_changed
    leanne "Hey everyone! Luxury Leanne here with an announcement."
    image leanne_stage6_maidmechadvd = "/leanne/events/stage6/maidmechadvd.webp"
    scene leanne_stage6_maidmechadvd
    "Pulling out the Maid Mecha DVD, she proudly holds it up to the camera."
    leanne "I managed to track down my precious treasure thanks to a little helper. Sorry to say, but the bounty is no longer available."
    "The chat erupts into a mix of congratulatory messages and cries of woe."
    image leanne_standup_event6 = "/leanne/6/standup.webp"
    scene leanne_standup_event6
    window hide
    pause
    image leanne_standupside_event6 = "/leanne/6/standup_side.webp"
    scene leanne_standupside_event6
    pause
    image leanne_typing_event6 = "/leanne/6/typing.webp"
    scene leanne_typing_event6
    leanne "Alright, alright, I'll give you all a little something to celebrate the occasion. Just give me a second."
    "Your phone receives a message."
    $ show_messenger()
    $ dialogue_one = []
    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("Are you watching the stream?", who=1)
    pause
    $ msg ("Yeah.")
    pause
    $ msg ("Tell me your username.", who=1)
    pause
    $ msg ("Why?")
    pause
    $ msg (";)", who=1)
    pause
    $ hide_messenger()
    leanne "Okay chat, what would you like to see from me tonight? No donation necessary. I'm going to pick a suggestion at random."
    ##(Note: Player is given an option between the two dances and her exercising without the need for donating first.)
    menu:
        "Dance.":
            ##Player Chooses Dance
            leanne "Oooh, sounds fun. I know just the song for it."
            image leanne_typing_event6 = "/leanne/6/typing.webp"
            scene leanne_typing_event6
            "After a few moments of typing away at her computer, Leanne turns on a royalty-free song and begins to dance."
            ##Dance animation starts.
            window hide
            $ movielength = 34
            $ movieplaying = "/images/leanne/6/dance1.webm"
            call screen custommoviescreen
            pause
            image stream_girl_webcam_event6 = "/leanne/6/webcam.webp"
            scene stream_girl_webcam_event6
            "After the song concludes, Leanne sits back down at her desk."
            leanne "That was just what I needed. Now I'm all limbered up and you all got a bit of a show. I'll have to do this again sometime."
        "Exercise.":
            ##Player Chooses Exercise
            leanne "Okay. Can't say I'm too thrilled about doing this on a full tummy, but here I go."
            ##Exercise animation starts
            window hide
            $ movielength = 25
            $ movieplaying = "/images/leanne/6/excercise.webm"
            call screen custommoviescreen
            pause
            "After completing several reps, Leanne sits back at her desk and wipes her face off with a towel."
            image stream_girl_towel_event6 = "/leanne/6/towel.webp"
            scene stream_girl_towel_event6
            leanne "I'm a little sweaty, but I think that worked. I should be ready to get back to the game now."
            image stream_girl_webcam_event6 = "/leanne/6/webcam.webp"
            scene stream_girl_webcam_event6

    "As soon as she finishes and sits back down, you receive another message."
    image leanne_towel_event6 = "/leanne/6/towel.webp"
    scene leanne_towel_event6
    $ show_messenger()
    $ dialogue_one = []
    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("Hope you enjoyed the freebie!", who=1)
    pause
    $ msg ("I did, thank you.")
    pause
    $ msg ("No problem. Enjoy the stream!", who=1)
    pause
    $ hide_messenger()
    "The stream continues as usual."
    stop music fadeout 1.0

    scene player_room
    "You receive a message. It's Leanne."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("Hope you enjoyed the stream, parasocial boy. Must be nice getting personal attention for once. 😏", who=1)
    "Before you can even type a reply, another message pops up."
    $ msg ("What, did you think I wouldn't notice you lurking in chat? Sitting there, watching me, hanging on my every word… kinda sad when you think about it. 😂", who=1)
    "You shake your head, smirking as you type."
    $ msg ("And yet, here you are, messaging me after stream. Almost like you enjoy the attention too.")
    pause
    $ msg ("Tch. Don't get cocky. I just felt bad for you. Gotta make sure my favorite lonely viewer doesn't feel too neglected. 😘", who=1)
    pause
    $ hide_messenger()

    $ leannestage6event2 = 0
    return

label Leanne_Stage_7_Event_1:
    ##Scene: Sweet Shop Hangout (Occurs on a weekend shortly after reaching stage 7)
    ##Image: Player’s room.
    $ show_messenger()
    $ dialogue_one = []
    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("You up?", who=1)
    pause
    $ msg ("Barely.")
    pause
    $ msg ("Eh, good enough. You doing anything today? I want to check out this bakery called Sugar Shop. Up for it?", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sure. Just give me a chance to get ready.")
            pause
            $ msg ("Alright, I'll see you in an hour.", who=1)
            pause
            $ msg ("But it's halfway across town.")
            pause
            $ msg ("Then you better hurry. (Winking and smiling emoji)", who=1)
            pause
            $ hide_messenger()
        "No.":
            $ msg ("Sorry, I'm a little busy today. I'll take a rain check though.")
            pause
            $ msg ("Alright. I'll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
            ##(If the player makes this choice, Leanne/Lyn will ask the same question every weekend until the player chooses yes.)

    "Rushing through your morning routine faster than you thought possible, you grab your stuff and head out the door."
    ##Image: Sweet Shop
    image leanne_stage7_sugarshop = "/leanne/events/stage7/sugarshop.webp"
    scene leanne_stage7_sugarshop
    "You make it to the Sugar Shop just in time, only to wait another fifteen minutes before she arrives."
    ##Image: Lyn with glasses and wearing a coat, sitting at a table in the Sugar Shop.
    "Lyn enters Sugar Shop with some incognito clothing."
    image leanne_stage7_arrive = "/leanne/events/stage7/arrive.webp"
    scene leanne_stage7_arrive
    "She takes off her coat and glasses."
    image leanne_stage7_arrive2 = "/leanne/events/stage7/arrive2.webp"
    scene leanne_stage7_arrive2
    leanne "Hey there. Hope I didn't keep you waiting long. I decided to take it easy today."
    image leanne_stage7_1 = "/leanne/events/stage7/1.webp"
    scene leanne_stage7_1
    "You figure it's best not to bring up your rush across town."
    pc "So what made you want to come here? From your streams I just assumed you weren't really a sweets person."
    leanne "That's because I thought greasy food would be an easy and cheap way to keep myself fed. While it has kept me pretty stocked up, I still have a bit of a sweet tooth."
    leanne "I thought I'd let myself indulge a bit today and try out some sugary pastries to plump myself up."
    pc "About that. Do you mind if I ask why you're trying to gain weight?"
    image leanne_stage7_2 = "/leanne/events/stage7/2.webp"
    scene leanne_stage7_2
    "Lyn thinks for a moment with her fingers across her chin."
    leanne "At first, it was mostly a reaction to being on the brink of starvation for so long. But I will admit, it's kind of taken on another light as I kept stuffing myself silly."
    image leanne_stage7_3 = "/leanne/events/stage7/3.webp"
    scene leanne_stage7_3
    "She leans back in her seat, making sure you can see her belly bulging out the front of her hoodie."
    leanne "My chat seems to enjoy seeing me grow bigger, so I guess I caught the same fascination. If nothing else, it'll help me stand out from the standard streaming girls."
    image leanne_stage7_4 = "/leanne/events/stage7/4.webp"
    scene leanne_stage7_4
    "Straightening her posture, she grabs a menu and looks through what the shop offers."
    leanne "Enough talk about me stuffing my face, let's actually get to it. I've saved up enough to try out a small pastry or two. Then again, if you feel like treating me to some of the more expensive treats..."
    image leanne_stage7_5 = "/leanne/events/stage7/5.webp"
    scene leanne_stage7_5
    "Though she doesn't finish her sentence, you can tell that she's using the same facial expression whenever she asks the chat for donations."
    ##(Note: Player is given the choice to order Leanne/Lyn something from the bakery with varying amounts of money associated with them. The player can also choose not to buy anything, leading to Lyn ordering a single donut for herself to snack on.
    menu:
        "Buy her loads of sweets. (-$20)":
            if money <= 19:
                "You do not have enough money to buy Leanne loads of sweets."
            else:
                if recollection == False:
                    $ money -= 20
                image leanne_stage7_8 = "/leanne/events/stage7/8.webp"
                scene leanne_stage7_8
                "Lyn devours her sweets in-between light conversation about games, anime, and random junk."
                image leanne_stage7_7 = "/leanne/events/stage7/7.webp"
                scene leanne_stage7_7
                window hide
                pause
                image leanne_stage7_9 = "/leanne/events/stage7/9.webp"
                scene leanne_stage7_9
                pause
                image leanne_stage7_10 = "/leanne/events/stage7/10.webp"
                scene leanne_stage7_10
                pause
                image leanne_stage7_6 = "/leanne/events/stage7/6.webp"
                scene leanne_stage7_6
                pause
                if recollection == False:
                    $ leanne.weight += 0.8
        "Buy her a couple sweets. (-$10)":
            if money <= 9:
                "You do not have enough money to buy Leanne loads of sweets."
            else:
                if recollection == False:
                    $ money -= 10
                image leanne_stage7_9 = "/leanne/events/stage7/9.webp"
                scene leanne_stage7_9
                "Lyn devours her sweets in-between light conversation about games, anime, and random junk."
                image leanne_stage7_10 = "/leanne/events/stage7/10.webp"
                scene leanne_stage7_10
                window hide
                pause
                image leanne_stage7_6 = "/leanne/events/stage7/6.webp"
                scene leanne_stage7_6
                pause
                if recollection == False:
                    $ leanne.weight += 0.5
        "Don't buy her sweets.":
            image leanne_stage7_6 = "/leanne/events/stage7/6.webp"
            scene leanne_stage7_6
            "Lyn devours her sweets in-between light conversation about games, anime, and random junk."
            if recollection == False:
                $ leanne.weight += 0.1
    ##(Image: Lyn devouring whatever sweet was given to her by the staff)
    image leanne_stage7_11 = "/leanne/events/stage7/11.webp"
    scene leanne_stage7_11
    leanne "Mmm, that really hit the spot."
    "She spends a few seconds tapping her hands against her stuffed belly."
    image leanne_stage7_12 = "/leanne/events/stage7/12.webp"
    scene leanne_stage7_12
    leanne "We have to try this again. Promise you'll hit me up when you're free to come here? Or even that bunny place if you're looking for a change of scenery?"
    pc "Sure, it's a date."
    image leanne_stage7_13 = "/leanne/events/stage7/13.webp"
    scene leanne_stage7_13
    "She lets out a playful laugh."
    image leanne_stage7_eventend = "/leanne/events/stage7/eventend.webp"
    scene leanne_stage7_eventend
    leanne "Okay, big boy, I think that's enough bravado for today. I'll catch you later."
    "After saying goodbye you head back home."
    stop music fadeout 1.0
    scene player_room
    "You receive a message. It's Leanne."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("So, I was digging through my old photos and found something fun…", who=1)
    "A moment later, another message pops up."
    $ msg ("Figured you might appreciate it. 😏", who=1)
    pause
    $ msg (None, who=1, pic="stage8_leanne1")
    pause
    $ msg (None, who=1, pic="stage8_leanne2")
    pause
    $ msg (None, who=1, pic="stage8_leanne3")
    pause
    $ msg ("Pretty good, right? Maybe I should bring this look back… unless you think you wouldn't be able to handle it. 😉", who=1)
    "You start typing a reply."
    $ msg ("Oh, I could handle it. The real question is, could you?")
    pause
    $ msg ("Bold. I like that. Maybe I'll just have to test you sometime. 😘", who=1)
    pause
    $ hide_messenger()

    ##(Note: After this scene, the player can choose to call up Leanne/Lyn to go to either the Sugar Shop or Bunny Bites to feed her.)
    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
    $ leannestage7event = 0
    return

label Leanne_Stage_7_Event_2:
    scene player_room
    "You were not planning to watch Leanne's stream that night, but when you see her live notification, you click on it out of habit."
    play music "/music/leanne_stream.ogg" if_changed
    image leanne_stage7_14 = "/leanne/events/stage7/14.webp"
    scene leanne_stage7_14
    "The screen loads just in time for you to witness a brutal headshot take Leanne out."
    "Her frustrated groan fills your headphones, followed by the mocking laughter of her rival, Mira."
    image leanne_stage7_15 = "/leanne/events/stage7/15.webp"
    scene leanne_stage7_15
    leanne "Oh, come on! Again?!"
    "Her chat blows up with spam."
    image leanne_stage7_16 = "/leanne/events/stage7/16.webp"
    scene leanne_stage7_16
    "Mira's name appears in the kill feed. Then, a second later, a donation message pops up on the screen."
    #"Damn, Leanne, maybe if you spent less time snacking and more time aiming, you wouldn’t be such an easy target. 😆" – MiraByte, $10
    "The chat erupts into chaos—some laughing, some defending Leanne, others egging her on."
    image leanne_stage7_17 = "/leanne/events/stage7/17.webp"
    scene leanne_stage7_17
    "Leanne forces a smirk, but you can tell she's annoyed."
    leanne "Oh wow, chat, look at that. Mira's here to grace us with her presence. What an honor."
    image leanne_stage7_18 = "/leanne/events/stage7/18.webp"
    scene leanne_stage7_18
    "She leans back in her chair, grabbing a chicken nugget from a nearby box."
    leanne "I'd respond, but, y'know, I'm too busy enjoying my snacks. Unlike some people, I know how to relax."
    image leanne_stage7_19 = "/leanne/events/stage7/19.webp"
    scene leanne_stage7_19
    "She takes an exaggerated bite, chewing loudly into the mic, making a show of her indifference."
    image leanne_stage7_20 = "/leanne/events/stage7/20.webp"
    scene leanne_stage7_20
    "Her chat spams laughing emojis, but you notice the shift in her mood. She keeps playing, but there's an edge of frustration in her movements, her focus slipping."
    stop music fadeout 1.0
    scene player_room
    "Later that night, after the stream ends, your phone buzzes."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("Ugh. That stream sucked. Need to de-stress. You busy? 😩", who=1)
    pause
    $ msg ("What happened?")
    pause
    $ msg ("Take a wild guess. Mira sniped me. Again. I need food therapy. Come keep me company? 🍕", who=1)
    pause
    $ msg ("Let me guess—you already ordered a feast?")
    pause
    $ msg ("Duh. Wouldn't be much of a de-stress session without it~ 😏", who=1)
    "You chuckle, already expecting this."
    "For the next hour, you chat back and forth as Leanne sends you pictures of her 'therapy session'—a bed filled with burger boxes."
    $ msg (None, who=1, pic="stage7_leanne1")
    pause
    $ msg (None, who=1, pic="stage7_leanne2")
    #"a selfie of her pouting dramatically with a burger in hand,
    pause
    $ msg (None, who=1, pic="stage7_leanne3")
    #"then another of her mid-bite, cheeks full as she throws up a peace sign."
    pause
    $ msg ("Mmm. This is hitting the spot. Wish you were here to feed me tho~ 😘", who=1)
    "You shake your head, smirking at your screen."
    "Eventually, she sends one last picture."
    $ msg (None, who=1, pic="stage7_leanne4")
    #a teasing shot of her sprawled out, tank top riding up just enough to reveal the soft curve of her stomach, a lazy grin on her lips.
    pause
    $ msg ("Okay. I might have overdone it. But worth it. 🤤", who=1)
    pause
    $ msg ("Def worth it.")
    pause
    $ msg ("And you love it~ Now, let me sleep a bit 😴", who=1)
    pause
    $ msg ("Night, Leanne ❤️")
    "A few minutes later, one last buzz."
    $ msg ("Thanks for always putting up with me. You're the best. 😘", who=1)
    pause
    $ hide_messenger()

    $ leannestage7event2 = 0
    return


label Leanne_Stage_8_Event_1:
    #Scene: Maid Mecha Watch Party (Occurs shortly after entering Stage 8 while the player is in their room.)
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("You free tonight? Since you went through so much trouble to get the damn thing, want to come to my place and watch the Maid Mecha DVD?", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sure, I'm game.")
            pause
            $ msg ("Cool. I'll send you the address. See you later.", who=1)
            pause
            $ hide_messenger()

        "No.":
            $ msg ("Sorry, I'm a little busy tonight.")
            pause
            $ msg ("That sucks. Alright, I'll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return

    #(NOTE: If the player chooses Yes, move directly to the next scene. If the player chooses No, the same event will occur on the following days until the Yes option is chosen.)
    #Image: Leanne’s Room, with Lyn wearing her glasses and a sweater. (NOTE, if possible replace the pink lights she uses for streaming with a more natural tone.)
    image leanne_stage8_arrive = "/leanne/events/stage8/arrive.webp"
    scene leanne_stage8_arrive
    leanne "Glad you could make it. Ready for some combat maid action?"
    "Judging by the eager smile on her face, she's ready to go regardless of your response."
    pc "Ready as I'll ever be I guess."
    image leanne_stage8_1 = "/leanne/events/stage8/1.webp"
    scene leanne_stage8_1
    leanne "Nice. I'll go get things set up. You go and order the pizza. Don't worry, I'll be the one treating this time."
    menu:
        "Order a pizza.":

            "After waiting a little while, you take the pizza from the delivery person and bring it into the room."
            image leanne_stage8_9 = "/leanne/events/stage8/9.webp"
            scene leanne_stage8_9
            leanne "Thanks for doing the heavy lifting. Here's your money back."
            "Sitting down next to Lyn, you open up the pizza box to start eating as she turns on episode one of Maid Mecha."
            if recollection == False:
                $ leanne.weight += 0.1

        "Order 5 pizzas. (-$25)":

            if money <= 24:
                "You do not have enough money to buy Lyn 5 pizzas. Instead you order one pizza."
                "After waiting a little while, you take the pizza from the delivery person and bring it into the room."
                image leanne_stage8_9 = "/leanne/events/stage8/9.webp"
                scene leanne_stage8_9
                leanne "Thanks for doing the heavy lifting. Here's your money back."
                "Sitting down next to Lyn, you open up the pizza box to start eating as she turns on episode one of Maid Mecha."
                if recollection == False:
                    $ leanne.weight += 0.1
            else:
                if recollection == False:
                    $ money -= 25
                "After waiting a little while, you answer the door for the delivery person and return to Lyn's rooms with your arms laden with pizza. Her expression is more than a little shocked."
                image leanne_stage8_2 = "/leanne/events/stage8/2.webp"
                scene leanne_stage8_2
                leanne "Dude, what the hell? I told you one pizza. You're going to make me go bankrupt at this rate."
                pc "Don't worry about the cost. I've got you covered. Think of it as just another big donation."
                image leanne_stage8_3 = "/leanne/events/stage8/3.webp"
                scene leanne_stage8_3
                "A sly smirk appears on her face."
                leanne "Alright, I see your game. You want to get a bit of a personal show."
                image leanne_stage8_4 = "/leanne/events/stage8/4.webp"
                scene leanne_stage8_4
                "Taking the top pizza off of the stack, she opens up the box and lets the warm air waft into her face. Picking up the first slice, she almost takes a bite only to stop and turn towards you."
                image leanne_stage8_5 = "/leanne/events/stage8/5.webp"
                scene leanne_stage8_5
                leanne "Go ahead and start the show. I'll keep working on these bad boys. Don't worry, I'll be sure to save you some."
                if recollection == False:
                    $ leanne.weight += 1.0

    #(Note: If player chooses option B, add weight to Leanne’s stats. The following scene plays out regardless of the player’s choice.)
    image leanne_stage8_6 = "/leanne/events/stage8/6.webp"
    scene leanne_stage8_6
    "True to Lyn's word, the show is a nail-biting epic of women in scantily clad maid uniforms duking it out with giant robots."
    "Behind the fanservice and awe-inspiring fights, you pick up on certain subtleties that enrapture your attention."
    image leanne_stage8_7 = "/leanne/events/stage8/7.webp"
    scene leanne_stage8_7
    "Before you realize it, the two of you have gone through several episodes and there isn't a single slice of pizza left."
    image leanne_stage8_8 = "/leanne/events/stage8/8.webp"
    scene leanne_stage8_8
    leanne "Going to have to call it for tonight. Did you enjoy it? Sorry I didn't pay much attention to you. The show gets me every time."
    pc "Don't worry about it. I can see why you were so passionate about it."
    leanne "I take it that means you'll be up for continuing the series another night?"
    pc "Count on it."
    image leanne_stage8_eventend = "/leanne/events/stage8/eventend.webp"
    scene leanne_stage8_eventend
    "After helping Lyn clean up, you say goodbye and head home."
    stop music fadeout 1.0
    scene player_room
    "You receive a message. It's Lyn."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("Hey, just so you know… I had a really good time with you today.", who=1)
    pause
    $ msg ("Not just the anime, but the whole thing. It was… nice. Comfortable. I don't really let people take care of me like that, but… I didn't mind it. Not with you.", who=1)
    "A short pause before another message pops up."
    $ msg ("But don't get any weird ideas, alright? I'm just being friendly. 😏", who=1)
    "You smirk and start typing."
    $ msg ("Of course. Just two friends, hanging out, feeding each other. Totally normal.")
    pause
    $ msg ("Exactly! No ulterior motives whatsoever. None. Not even a little. 😘", who=1)
    "A final message follows."
    $ msg ("…Anyway, sleep well, boy. And don't overthink it. Or do. Your call. 😉", who=1)
    pause
    $ hide_messenger()


    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
    $ leannestage8event = 0
    return

label Leanne_Stage_8_Event_2:
    scene player_room
    "You weren't planning to watch Leanne's stream tonight, but when her live notification pops up, you click on it out of habit."
    image leanne_stage8_10 = "/leanne/events/stage8/10.webp"
    scene leanne_stage8_10
    play music "/music/leanne_stream.ogg" if_changed
    "The screen loads just in time to see her crosshairs line up on a familiar name—MiraByte."
    "BAM!"
    "A clean headshot takes Mira out instantly."
    image leanne_stage8_11 = "/leanne/events/stage8/11.webp"
    scene leanne_stage8_11
    "Leanne's silence lasts only a second before a slow, devilish grin spreads across her face."
    leanne "Ohhh, chat. This just got interesting."
    image leanne_stage8_12 = "/leanne/events/stage8/12.webp"
    scene leanne_stage8_12
    "Her chat erupts."
    #"HOLY— LET’S GOOOOOOO"
    #"REVENGE ARC, BABY!"
    #"MIRA DOWN, MIRA DOWN!"
    "A few minutes later, it happens again. Leanne catches Mira off guard— BAM. A second kill."
    image leanne_stage8_13 = "/leanne/events/stage8/13.webp"
    scene leanne_stage8_13
    "She leans back, giggling."
    leanne "Ohhh, this feels good. You guys feel that? That's called justice."
    image leanne_stage8_14 = "/leanne/events/stage8/14.webp"
    scene leanne_stage8_14
    "Then comes the ultimate move—Leanne pulls up Mira's stream on her own, overlaying it for her viewers to see."
    image leanne_stage8_37 = "/leanne/events/stage8/37.webp"
    scene leanne_stage8_37
    "Mira is fuming, trying to play it cool, but her clenched jaw says otherwise."
    image leanne_stage8_15 = "/leanne/events/stage8/15.webp"
    scene leanne_stage8_15
    "Leanne smirks, opens up the donation tab, and types."
    image leanne_stage8_38 = "/leanne/events/stage8/38.webp"
    scene leanne_stage8_38
    "$5 Donation from LuxuryLeanne: \"Damn, Mira, you should eat more. Maybe you’d have the energy to dodge. Just saying~\""
    image leanne_stage8_16 = "/leanne/events/stage8/16.webp"
    scene leanne_stage8_16
    "Chat loses it."
    #"NOOOO SHE DID NOT"
    #"THE PETTINESS, I’M HERE FOR IT"
    #"Mira boutta explode"
    image leanne_stage8_39 = "/leanne/events/stage8/39.webp"
    scene leanne_stage8_39
    "Mira's eye twitches."
    mira "Don't get cocky, Leanne. You only got me because you were lucky."
    image leanne_stage8_17 = "/leanne/events/stage8/17.webp"
    scene leanne_stage8_17
    "Leanne's smirk widens."
    leanne "Oh? Luck, huh?"
    image leanne_stage8_18 = "/leanne/events/stage8/18.webp"
    scene leanne_stage8_18
    "The moment those words leave Mira's mouth, Leanne hunts her down again."
    image leanne_stage8_40 = "/leanne/events/stage8/40.webp"
    scene leanne_stage8_40
    pause
    image leanne_stage8_41 = "/leanne/events/stage8/41.webp"
    scene leanne_stage8_41
    pause
    image leanne_stage8_42 = "/leanne/events/stage8/42.webp"
    scene leanne_stage8_42
    "A third kill. Right on stream."
    image leanne_stage8_43 = "/leanne/events/stage8/43.webp"
    scene leanne_stage8_43
    "Mira's expression is pure disbelief as the killcam zooms in on her. Then, through gritted teeth, she mutters."
    image leanne_stage8_44 = "/leanne/events/stage8/44.webp"
    scene leanne_stage8_44
    mira "Just you wait, Leanne..."
    image leanne_stage8_45 = "/leanne/events/stage8/45.webp"
    scene leanne_stage8_45
    pause
    image leanne_stage8_46 = "/leanne/events/stage8/46.webp"
    scene leanne_stage8_46
    "BAM—Mira's stream abruptly shuts off."
    image leanne_stage8_19 = "/leanne/events/stage8/19.webp"
    scene leanne_stage8_19
    "Leanne loses it, cackling."
    leanne "Ohhhh, that's gonna leave a mark. Chat, did we just—did we just break her?"
    image leanne_stage8_20 = "/leanne/events/stage8/20.webp"
    scene leanne_stage8_20
    "You watch the rest of the stream until she finishes up her gaming session."
    stop music fadeout 1.0
    scene player_room
    "Later that night, after the stream ends, your phone buzzes."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("BROOOOOO 😂😂😂", who=1)
    pause
    $ msg ("I saw. That was brutal.")
    pause
    $ msg ("She RAGE QUIT. I actually made her rage quit. I'm a goddamn legend. 😎", who=1)
    pause
    $ msg ("You think she's gonna let that slide?")
    pause
    $ msg ("Pfft. What's she gonna do, try harder?", who=1)
    pause
    $ msg ("Sounds dangerous.")
    pause
    $ msg ("Oh, I hope it is. 😏", who=1)
    pause
    $ msg ("She's so mad right now. I bet she's staring at a protein shake, debating her life choices.", who=1)
    pause
    $ msg ("Bet she's plotting your downfalllllll hehe.")
    pause
    $ msg ("Let her. I'll be here, waiting.", who=1)
    pause
    $ hide_messenger()

    "An hour later you get another message from Leanne."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("Still can't believe I made her rage quit. This might be the best night of my life.", who=1)
    pause
    $ msg (None, who=1, pic="stage8_leanne4")
    #Leanne in her gaming chair, flushed from laughing, holding up a piece of cake with a victorious smirk.
    pause
    $ msg ("Celebratory bite.", who=1)
    pause
    $ hide_messenger()

    $ leannestage8event2 = 0
    return

label Leanne_Stage_8_Event_3:
    scene player_room
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("Yo, did you see what Mira did on her stream? 😑", who=1)
    pause
    $ msg ("No, what happened?")
    pause
    $ msg ("Just go check it out. I'm watching, and I don't know if I should laugh or be worried.", who=1)
    pause
    $ msg ("Alright, give me a sec.")
    pause
    $ hide_messenger()

    #[MC opens Mira’s stream]
    image leanne_stage8_21 = "/leanne/events/stage8/21.webp"
    scene leanne_stage8_21
    "The screen loads to reveal Mira in the middle of her usual high-energy broadcast, except… something's different."
    "A food donation bar sits at the bottom of the screen, listing various options: Pizza - $5, Burger - $4, Soda - $3, and an ominous “Surprise Feast” option for $20."
    image leanne_stage8_22 = "/leanne/events/stage8/22.webp"
    scene leanne_stage8_22
    "The chat is going wild, spamming donations faster than she can keep up."
    "Mira, usually composed and confident, is currently mid-bite into a massive burger, barely chewing before reaching for a large soda and taking a deep chug."
    "A pile of empty wrappers is already building up beside her."

    $ show_messenger()

    $ msg ("…Oh.")
    pause
    $ msg ("I KNOW RIGHT?!", who=1)
    pause
    $ msg ("She has a food donation button now. Just like mine.", who=1)
    pause
    $ msg ("But look at her go. She's stuffing her face like she hasn't eaten in a week. 💀", who=1)
    pause
    $ hide_messenger()

    image leanne_stage8_23 = "/leanne/events/stage8/23.webp"
    scene leanne_stage8_23
    "You watch as Mira wipes her mouth quickly, barely taking a breath before reaching for another bite."
    "Her chat is throwing messages at her from all directions."
    image leanne_stage8_24 = "/leanne/events/stage8/24.webp"
    scene leanne_stage8_24
    "Damn Mira slow down 😂" 
    "More more more! 💰💰💰" 
    "She’s gonna explode at this rate lol"

    $ show_messenger()

    $ msg ("She's really going all in…")
    pause
    $ msg ("Should I be worried?", who=1)
    pause
    $ msg ("About what?")
    pause
    $ msg ("Idk. Competition? My brand? The fact that she might actually pop on stream at this rate? 😅", who=1)
    pause
    $ msg ("Relax, Leanne. You're still bigger and cuter.")
    pause
    $ msg ("Bigger, huh? You really know how to compliment a lady. 😉", who=1)
    pause
    $ msg ("Just speaking the truth.")
    pause
    $ msg ("Heh. Well, she can keep chugging down those donations. I'll be right here, looking better while doing it. 😏", who=1)
    pause
    $ msg ("Exactly.")
    pause
    $ msg ("Anyway, keep watching. If she explodes, I wanna hear your live reaction. 😆", who=1)
    pause
    $ hide_messenger()

    image leanne_stage8_25 = "/leanne/events/stage8/25.webp"
    scene leanne_stage8_25
    "You continue watching Mira's stream until the end and then go to sleep."
    image leanne_stage8_26 = "/leanne/events/stage8/26.webp"
    scene leanne_stage8_26
    pause
    image leanne_stage8_27 = "/leanne/events/stage8/27.webp"
    scene leanne_stage8_27
    pause
    image leanne_stage8_28 = "/leanne/events/stage8/28.webp"
    scene leanne_stage8_28
    pause
    image leanne_stage8_29 = "/leanne/events/stage8/29.webp"
    scene leanne_stage8_29
    pause
    image leanne_stage8_30 = "/leanne/events/stage8/30.webp"
    scene leanne_stage8_30
    pause
    image leanne_stage8_31 = "/leanne/events/stage8/31.webp"
    scene leanne_stage8_31
    pause
    image leanne_stage8_32 = "/leanne/events/stage8/32.webp"
    scene leanne_stage8_32
    pause
    image leanne_stage8_33 = "/leanne/events/stage8/33.webp"
    scene leanne_stage8_33
    pause
    image leanne_stage8_34 = "/leanne/events/stage8/34.webp"
    scene leanne_stage8_34
    pause
    image leanne_stage8_35 = "/leanne/events/stage8/35.webp"
    scene leanne_stage8_35
    pause
    image leanne_stage8_36 = "/leanne/events/stage8/36.webp"
    scene leanne_stage8_36
    pause

    $ leannestage8event3 = 0
    return

label Leanne_Stage_9_Event:
    #Scene: Maid Mecha Marathon (Start on either Saturday or Sunday after the player has reached Stage 9)
    #Image: Player’s room.
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("Want to come over to my place and marathon the rest of Maid Mecha? Fair warning, it'll be a long haul so make sure your day is clear beforehand.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sure, I'm in. Need me to bring anything over?")
            pause
            $ msg ("Just bring yourself. I've got everything else covered.", who=1)
            pause
            $ hide_messenger()

        "No.":
            $ msg ("Sorry, I'm a little busy today.")
            pause
            $ msg ("Alright. I'll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return

    #(NOTE: If player chooses No, they will receive the same message from Lyn/Leanne every following weekend until they choose Yes. When choosing Yes the following takes place.)
    "Trekking your way over to Lyn's place, you walk inside and experience a collection of delicious smells coming from her room."
    image leanne_stage9_arrive = "/leanne/events/stage9/arrive.webp"
    scene leanne_stage9_arrive
    #Image: Leanne’s Room filled with a collection of food boxes stacked on her desk.
    "Upon seeing the large collection of food piled up on her desk, you watch as Lyn steps to the side and puts on a confident grin."
    #Image: Leanne in her sweater and glasses with a smile on her face.
    image leanne_stage9_1 = "/leanne/events/stage9/1.webp"
    scene leanne_stage9_1
    leanne "Impressed?"
    pc "Don't you think this is a little much? I thought you were still struggling with finances."
    image leanne_stage9_2 = "/leanne/events/stage9/2.webp"
    scene leanne_stage9_2
    leanne "First off, you are seriously underestimating how long this is going to take. Second, my streams have been raking in the cash so I can afford to indulge every now and then."
    "Stepping to the side, she lifts up the bottom of her sweater to let her belly peek out."
    image leanne_stage9_3 = "/leanne/events/stage9/3.webp"
    scene leanne_stage9_3
    leanne "Besides, I consider this all an investment. Now come on. Pop in the DVD while I get down to business. Don't worry, I made sure to leave plenty for you."
    image leanne_stage9_4 = "/leanne/events/stage9/4.webp"
    scene leanne_stage9_4
    "Upon starting up the next episode in the series, you pull up a chair just as Lyn opens up her first box of food."
    #(NOTE: Various images of Leanne eating different kinds of food can play as the next part plays out.)
    image leanne_stage9_5 = "/leanne/events/stage9/5.webp"
    scene leanne_stage9_5
    "As you and Lyn continue through the series, she helps herself to a different kind of binging."
    image leanne_stage9_6 = "/leanne/events/stage9/6.webp"
    scene leanne_stage9_6
    "It seems that every time you turn your head, she's devouring a new plate of food."
    image leanne_stage9_7 = "/leanne/events/stage9/7.webp"
    scene leanne_stage9_7
    "Though you manage to get a few bites in, most of your time is spent either being awestruck by the quality of the show or marveling at her ability to eat so much."
    image leanne_stage9_8 = "/leanne/events/stage9/8.webp"
    scene leanne_stage9_8
    "This marathon of watching and feasting comes to a momentary halt as you reach the homestretch of the final episodes."
    "You stand up to swap out the discs and start the final episodes only to be stopped by Lyn."
    leanne "Wait. I think I need your help."
    image leanne_stage9_9 = "/leanne/events/stage9/9.webp"
    scene leanne_stage9_9
    "Turning back to Lyn, you see that she is slouched in her chair with her belly hanging between her legs."
    "Her expression is one of complete lethargy with her fingers lazily sliding against her stuffed gut. You only now notice the massive pile of empty food containers on her table."
    pc "Woah. I didn't realize you ate that much."
    image leanne_stage9_10 = "/leanne/events/stage9/10.webp"
    scene leanne_stage9_10
    leanne "Yeah, and I'm definitely paying for it. I know this sounds strange, but could you rub my belly? Maybe it'll help ease my indigestion."
    pc "Um, sure."
    image leanne_stage9_11 = "/leanne/events/stage9/11.webp"
    scene leanne_stage9_11
    "Getting close to her, you place your hand on her gut. Feeling the taut flesh against your palm, you begin to make small, gentle circles along her skin."
    "Covering the entirety of her belly seems to do the trick, with her letting out small breaths of relief."
    leanne "Yeah, that hits the spot. Almost feels as good as-"
    image leanne_stage9_12 = "/leanne/events/stage9/12.webp"
    scene leanne_stage9_12 with vpunch
    leanne "UURPP!"
    image leanne_stage9_13 = "/leanne/events/stage9/13.webp"
    scene leanne_stage9_13
    "Lyn freezes, covering up her face as a red blush goes across her cheeks."
    menu:
        leanne "I'm so sorry. That kind of just slipped out. You must think I'm totally gross."
        "It's okay. That kind of thing happens. No need to be embarrassed.":
            image leanne_stage9_14 = "/leanne/events/stage9/14.webp"
            scene leanne_stage9_14
            leanne "Thank you for understanding."
            pc "Like I said, it's not a big deal. Probably just a sign that you enjoyed your meal and that your stomach is getting better."
            image leanne_stage9_15 = "/leanne/events/stage9/15.webp"
            scene leanne_stage9_15
            "Her face lights up with a small smile."
            leanne "Never thought about it like that. I wonder if…"
            image leanne_stage9_16 = "/leanne/events/stage9/16.webp"
            scene leanne_stage9_16
            "She trails off, her mind deep in thought."
            pc "Is everything alright?"
            image leanne_stage9_15 = "/leanne/events/stage9/15.webp"
            scene leanne_stage9_15
            "She snaps out of her train of thought."
            leanne "Yeah, I'm fine. Just thinking about something."

        "Eh, that was nothing. I've had burps much stronger than that.":
            image leanne_stage9_17 = "/leanne/events/stage9/17.webp"
            scene leanne_stage9_17
            "She gives you a confused stare, making you think you've said something completely crazy. Gradually she adopts a small smirk."
            image leanne_stage9_18 = "/leanne/events/stage9/18.webp"
            scene leanne_stage9_18
            "Grabbing her taut stomach, she begins to wildly shake it around. The constant motion eventually culminates into…"
            image leanne_stage9_19 = "/leanne/events/stage9/19.webp"
            scene leanne_stage9_19 with vpunch
            leanne "BWOOOOOOOOOOOORRRRRRRPPPP!"
            image leanne_stage9_20 = "/leanne/events/stage9/20.webp"
            scene leanne_stage9_20
            "Stunned in the wake of her massive belch, you're left to stare at her smug grin."
            leanne "How's that? Strong enough for you?"
            pc "Didn't mean to challenge you, but that was pretty impressive."
            leanne "Thank you. Makes me wonder if I could…"
            image leanne_stage9_16 = "/leanne/events/stage9/16.webp"
            scene leanne_stage9_16
            "She trails off, her mind deep in thought."
            pc "Is everything alright?"
            image leanne_stage9_15 = "/leanne/events/stage9/15.webp"
            scene leanne_stage9_15
            "She snaps out of her train of thought."
            leanne "Yeah, I'm fine. Just thinking about something."

    #(NOTE: The following plays out regardless of previous choice)
    leanne "Anyway, I think I've hit my limit for the night."
    pc "But we're so close to the end."
    image leanne_stage9_21 = "/leanne/events/stage9/21.webp"
    scene leanne_stage9_21
    "She lets out a small giggle that shakes her belly."
    leanne "Don't worry, we'll pick this up another time. I'll make it a special event. I promise."
    pc "Count on it."
    image leanne_stage9_eventend = "/leanne/events/stage9/eventend.webp"
    scene leanne_stage9_eventend
    "You clean up the mess while Lyn continues to nurse her overstuffed gut. After saying goodbye, you head home for the day for some much needed rest."

    stop music fadeout 1.0
    scene player_room
    "You receive a message. It's Lyn."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("You know, I didn't expect to enjoy that as much as I did.", who=1)
    pause
    $ msg ("The anime was great, but being fed like that? Yeah… I could get used to that. 😏", who=1)
    "You chuckle and start typing."
    $ msg ("Guess I'll have to do it again then.")
    pause
    $ msg ("Damn right you will. You've set a standard now, hope you can keep up. 😘", who=1)
    pause
    $ msg (None, who=1, pic="stage9_leanne")
    pause
    $ msg ("Sweet dreams, feeder boy. 💕", who=1)
    pause
    $ hide_messenger()

    if recollection == False:
        $ leanne.weight += 1.0
        $ daytime += 2
        $ phonecall = 1
    $ leannestage9event = 0
    return

label Leanne_Stage_9_Event_2:
    scene player_room
    "You check your phone, and curiosity gets the best of you. Mira's stream is live, and after everything that's happened, you decide to see what she's up to."
    image leanne_stage9_22 = "/leanne/events/stage9/22.webp"
    scene leanne_stage9_22
    "The moment the page loads, you're met with the sight of Mira, lips wrapped around a straw, aggressively slurping down a massive soda."
    image leanne_stage9_23 = "/leanne/events/stage9/23.webp"
    scene leanne_stage9_23
    "A pile of fast food and burgers sit in front of her."
    image leanne_stage9_24 = "/leanne/events/stage9/24.webp"
    scene leanne_stage9_24
    "She doesn't even seem fazed. If anything, she looks smug, wiping her lips with the back of her hand before glancing at the chat."
    image leanne_stage9_25 = "/leanne/events/stage9/25.webp"
    scene leanne_stage9_25
    mira "Don't act so surprised, chat. If Leanne can do it, so can I."
    image leanne_stage9_26 = "/leanne/events/stage9/26.webp"
    scene leanne_stage9_26
    "She grabs another burger and takes a big bite."
    image leanne_stage9_27 = "/leanne/events/stage9/27.webp"
    scene leanne_stage9_27
    pause
    image leanne_stage9_28 = "/leanne/events/stage9/28.webp"
    scene leanne_stage9_28
    pause
    image leanne_stage9_29 = "/leanne/events/stage9/29.webp"
    scene leanne_stage9_29
    pause
    image leanne_stage9_30 = "/leanne/events/stage9/30.webp"
    scene leanne_stage9_30
    pause
    image leanne_stage9_31 = "/leanne/events/stage9/31.webp"
    scene leanne_stage9_31
    pause
    image leanne_stage9_32 = "/leanne/events/stage9/32.webp"
    scene leanne_stage9_32
    pause
    image leanne_stage9_33 = "/leanne/events/stage9/33.webp"
    scene leanne_stage9_33
    pause
    image leanne_stage9_34 = "/leanne/events/stage9/34.webp"
    scene leanne_stage9_34
    pause
    image leanne_stage9_35 = "/leanne/events/stage9/35.webp"
    scene leanne_stage9_35
    "She talks with her mouth full, barely even pausing between chews."
    mira "Besides, I'm making bank off this. You guys love this kinda thing, huh?"
    image leanne_stage9_36 = "/leanne/events/stage9/36.webp"
    scene leanne_stage9_36
    "The chat is going wild."
    image leanne_stage9_37 = "/leanne/events/stage9/37.webp"
    scene leanne_stage9_37
    "Holy crap, she’s actually doing it."
    image leanne_stage9_38 = "/leanne/events/stage9/38.webp"
    scene leanne_stage9_38
    "LMAO she’s speedrunning obesity."
    image leanne_stage9_39 = "/leanne/events/stage9/39.webp"
    scene leanne_stage9_39
    "MiraByte? More like MiraBite."
    image leanne_stage9_40 = "/leanne/events/stage9/40.webp"
    scene leanne_stage9_40
    "LETS GOOO! Next up, a whole pizza!"
    image leanne_stage9_41 = "/leanne/events/stage9/41.webp"
    scene leanne_stage9_41
    "Your eyes drift down to the donation menu she has set up:"
    image leanne_stage9_42 = "/leanne/events/stage9/42.webp"
    scene leanne_stage9_42
    "🍕 Pizza Slice - $2 🍔 Burger - $3 🥤 Large Soda Chug - $1.50 🍟 Fries - $2 🍕 Whole Pizza - $10"
    image leanne_stage9_43 = "/leanne/events/stage9/43.webp"
    scene leanne_stage9_43
    "🍔 Triple Burger Stack - $7 🥤 Gallon of Soda - $5 🍰 Cake Slice - $3 🍰 Whole Cake - $12"
    image leanne_stage9_44 = "/leanne/events/stage9/44.webp"
    scene leanne_stage9_44
    "It's dirt cheap. No wonder chat is spamming donations like crazy."
    image leanne_stage9_45 = "/leanne/events/stage9/45.webp"
    scene leanne_stage9_45
    "Every few seconds, new orders pop up on-screen. Mira barely even acknowledges them—she just eats. Fast."
    image leanne_stage9_46 = "/leanne/events/stage9/46.webp"
    scene leanne_stage9_46
    "A fresh $5 donation rolls in. “Gallon of Soda, let’s see it!”"
    image leanne_stage9_47 = "/leanne/events/stage9/47.webp"
    scene leanne_stage9_47
    mira "Oh, you think I can't handle it?"
    image leanne_stage9_48 = "/leanne/events/stage9/48.webp"
    scene leanne_stage9_48
    "She reaches off-screen and hauls up a massive jug of soda."
    image leanne_stage9_49 = "/leanne/events/stage9/49.webp"
    scene leanne_stage9_49
    pause
    image leanne_stage9_50 = "/leanne/events/stage9/50.webp"
    scene leanne_stage9_50
    pause
    image leanne_stage9_51 = "/leanne/events/stage9/51.webp"
    scene leanne_stage9_51
    pause
    image leanne_stage9_52 = "/leanne/events/stage9/52.webp"
    scene leanne_stage9_52
    pause
    image leanne_stage9_53 = "/leanne/events/stage9/53.webp"
    scene leanne_stage9_53
    "Without hesitation, she starts chugging."
    image leanne_stage9_54 = "/leanne/events/stage9/54.webp"
    scene leanne_stage9_54
    "The chat loses it, spamming emojis and laughing as she downs mouthful after mouthful."
    image leanne_stage9_55 = "/leanne/events/stage9/55.webp"
    scene leanne_stage9_55
    pause
    image leanne_stage9_56 = "/leanne/events/stage9/56.webp"
    scene leanne_stage9_56
    pause
    image leanne_stage9_57 = "/leanne/events/stage9/57.webp"
    scene leanne_stage9_57
    pause
    image leanne_stage9_58 = "/leanne/events/stage9/58.webp"
    scene leanne_stage9_58
    pause
    image leanne_stage9_59 = "/leanne/events/stage9/59.webp"
    scene leanne_stage9_59
    "A few seconds in, she pulls away, gasping for breath, a dribble of soda running down her chin."
    image leanne_stage9_60 = "/leanne/events/stage9/60.webp"
    scene leanne_stage9_60
    mira "Ugh—okay, that was a lot."
    image leanne_stage9_61 = "/leanne/events/stage9/61.webp"
    scene leanne_stage9_61
    "She coughs, wiping her mouth."
    image leanne_stage9_62 = "/leanne/events/stage9/62.webp"
    scene leanne_stage9_62
    "Then, smirking, she pats her stomach."
    image leanne_stage9_63 = "/leanne/events/stage9/63.webp"
    scene leanne_stage9_63
    mira "Hope you guys are enjoying the show."
    "More donations flood in."
    image leanne_stage9_64 = "/leanne/events/stage9/64.webp"
    scene leanne_stage9_64
    "You glance at the viewer count—her numbers are skyrocketing."
    image leanne_stage9_65 = "/leanne/events/stage9/65.webp"
    scene leanne_stage9_65
    "Mira's doing this for the money. For the views."
    image leanne_stage9_66 = "/leanne/events/stage9/66.webp"
    scene leanne_stage9_66
    "But as she takes another big bite, eyes glinting with something unreadable, you start to wonder… how far is she willing to go?"

    "Your phone buzzes."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("You seeing this? 😳", who=1)
    pause
    $ msg ("She's gonna explode at this rate. 😂", who=1)
    pause
    $ msg ("Should I be worried?", who=1)
    "You type back."
    $ msg ("Nah, she'll burn out. You're bigger and cuter anyway. 😉")
    pause
    $ msg ("But I gotta admit, this is pretty hot, it puts me in the mood.", who=1)
    pause
    $ msg ("Really?")
    pause
    $ msg (None, who=1, pic="stage9_leanne2")
    pause
    $ hide_messenger()

    "You close the stream and go to sleep."
    $ leannestage9event2 = 0
    return

label Leanne_Stage_10_Event:
    #Scene: Maid Mecha Finale (Occurs on a weekend after Leanne reaches enough weight for Stage 10)
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("The time has finally come! I've got all the provisions ready for the big finale. You free tonight to finish off Maid Mecha?", who=1)
    pause
    menu:
        "I'm in!":
            $ msg ("I'm in. Same time and place?")
            pause
            $ msg ("You know it. Don't be late.", who=1)
            pause
            $ hide_messenger()

        "Sorry, I'm busy tonight.":
            $ msg ("Sorry, I'm busy tonight.")
            pause
            $ msg ("Well shit. Alright, I'll hit you up some other time.", who=1)
            pause
            $ hide_messenger()
            return
    #(NOTE: If player chooses B), they will receive the same message from Leanne every following weekend until they choose A). When choosing A) the following takes place.)
    "Preparing yourself as best you can, you make the trek over to Lyn's place."
    #Image: Leanne’s room with Leanne dressed in her glasses and sweater.
    image leanne_stage10_arrive = "/leanne/events/stage10/arrive.webp"
    scene leanne_stage10_arrive
    "Upon entering Lyn's room, you're somewhat confused at the lack of piles of food. Your reaction doesn't go unnoticed."
    leanne "Awww, are you disappointed you won't get to see me pig out?"
    pc "More surprised after what you did last time we did a marathon."
    leanne "Things are a little different for this session. We only have a handful of episodes left, so I figured we'd make our snacking short and sweet."
    image leanne_stage10_1 = "/leanne/events/stage10/1.webp"
    scene leanne_stage10_1
    #Image: Leanne holding up two bowls of ice cream, one much larger than the other.
    "As to accentuate her point, Lyn reaches over to grab something and pull it to your attention."
    "It takes you a second to realize what she is holding as the sweet treat is covered generously with all manner of calorific garnish."
    "Your eyes go wide as you look upon the mountain of ice cream and toppings in front of you."
    "Still trying to take in the full image of the monstrous dessert, you almost miss the much more sensible bowl of ice cream in Lyn's other hand."
    leanne "Ta dah! A sweet treat for a sweet finale. I'm assuming you know which one is yours?"
    pc "Of course. I'll get the show started up."
    image leanne_stage10_2 = "/leanne/events/stage10/2.webp"
    scene leanne_stage10_2
    "Pressing play on the DVD and sitting down next to Lyn once more, you settle in for the finale."
    "What plays out is a culmination of plot points and character growth that makes you barely touch your ice cream."
    "You're overcome with a mix of emotions as the final battle concludes, subjecting you to an ending that's bittersweet, yet satisfactory."
    "Upon watching the credits one final time, you turn towards Lyn."
    image leanne_stage10_3 = "/leanne/events/stage10/3.webp"
    scene leanne_stage10_3
    pc "That was everything you hyped it up to be and more."
    leanne "Told you."
    image leanne_stage10_4 = "/leanne/events/stage10/4.webp"
    scene leanne_stage10_4
    "Glancing away from her face, you look down to see that she's completely destroyed the enormous serving of ice cream."
    pc "I see you enjoyed your dessert."
    leanne "Can you blame me? I got so excited I just needed something to keep my mouth from hanging open all the time. Sorry, I did mean to give you a taste. Want to try some?"
    pc "Sure. Do you have more in your freezer or do I need to- "
    image leanne_stage10_5 = "/leanne/events/stage10/5.webp"
    scene leanne_stage10_5
    "Your words become muffled as Lyn leans forward to lock her lips with yours."
    "The lingering sweetness on her mouth is nothing compared to the sensation of warmth you feel as she continues to embrace you."
    "Leaving you dumbfounded, she leans back and smiles."
    image leanne_stage10_6 = "/leanne/events/stage10/6.webp"
    scene leanne_stage10_6
    leanne "Pretty tasty, huh?"
    pc "Where did that come from?"
    leanne "Aww, you didn't like your treat?"
    pc "That's not what I-"
    "She reaches out to give you a small bump to the shoulder."
    leanne "Relax. Just having a little fun. Think of it as a little incentive to make sure you come back for whatever show I pick out next. That is, if you want to keep doing this with me."
    pc "I doubt anything can live up to what I just saw, but I'm more than willing to be proven wrong."
    leanne "Then it's a date."
    image leanne_stage10_eventend = "/leanne/events/stage10/eventend.webp"
    scene leanne_stage10_eventend
    "Helping Lyn clean up the empty bowls, you head home with your thoughts lingering on her impromptu kiss the entire way there."
    if recollection == False:
        $ leanne.weight += 0.3
        $ daytime += 1
        $ phonecall = 1
    $ leannestage10event = 0
    return

label Leanne_Stage_10_Event_2:
    "Your phone buzzes with a message from Lyn."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("Bro, are you seeing what Mira's doing?? 🤨", who=1)
    pause
    $ hide_messenger()

    "You blink, confused, before opening her stream." 
    image leanne_stage10_7 = "/leanne/events/stage10/7.webp"
    scene leanne_stage10_7
    "The moment it loads, you see Mira."
    "She’s standing this time, not seated, showing off a sleek, form-fitting black dress that hugs every curve like it was made for her." 
    image leanne_stage10_8 = "/leanne/events/stage10/8.webp"
    scene leanne_stage10_8
    "Her hair is pinned up with a few playful strands framing her face, and her glossy lips curl into a smirk as she faces the camera."
    mira "Yeah, yeah, I know," 
    image leanne_stage10_9 = "/leanne/events/stage10/9.webp"
    scene leanne_stage10_9
    "She says with a twirl, giving the chat a slow, deliberate spin." 
    "The camera picks up the subtle bounce of her hips, the soft press of her stomach beneath the fabric." 
    mira "This is a special occasion dress. Or, y’know, a ‘look-how-good-I-look-even-after-devouring-an-entire-feast’ kinda dress."
    image leanne_stage10_11 = "/leanne/events/stage10/11.webp"
    scene leanne_stage10_11
    "Her chat erupts:"
    "You DRESSED UP for this??"
    "Mira lookin dangerous tonight."
    "Who let her be this fine."
    "You didn’t have to SLAY us like that queen."
    "Ayo that dress clingin for life rn."
    image leanne_stage10_10 = "/leanne/events/stage10/10.webp"
    scene leanne_stage10_10
    mira "You guys like it? Thought I’d show off a little… figured I deserved to. I have been putting in work lately." 
    mira "More than most of you ever could."
    image leanne_stage10_12 = "/leanne/events/stage10/12.webp"
    scene leanne_stage10_12
    "Then she does another pose, the fabric of her dress visibly straining around her middle." 
    mira "And don’t act surprised it fits tighter. This dress used to be loose, y’know." 
    mira "Must’ve shrunk in the wash or something…"
    image leanne_stage10_13 = "/leanne/events/stage10/13.webp"
    scene leanne_stage10_13
    "More teasing messages flood in."
    "Ok but that pose??"
    "Mira STOP you’re gonna break the internet."
    "She KNOWS she’s fine and it's killing me."
    "This stream illegal in some countries fr."
    image leanne_stage10_14 = "/leanne/events/stage10/14.webp"
    scene leanne_stage10_14
    "She finally sits down—carefully—grabbing her headset and sliding into gamer mode with a laugh."
    image leanne_stage10_15 = "/leanne/events/stage10/15.webp"
    scene leanne_stage10_15
    mira "Alright, now that I’ve tortured you all, time to eat."
    image leanne_stage10_16 = "/leanne/events/stage10/16.webp"
    scene leanne_stage10_16

    $ show_messenger()
    $ msg ("This is insane. It's like she's in some kinda competition. With herself. 🤔", who=1)
    image leanne_stage10_17 = "/leanne/events/stage10/17.webp"
    scene leanne_stage10_17
    pause
    $ msg ("You sure she's not just hungry?")
    image leanne_stage10_18 = "/leanne/events/stage10/18.webp"
    scene leanne_stage10_18
    pause
    $ msg ("She's literally got a whole menu up now. People donate, she eats. Just like me. 🙃", who=1)
    image leanne_stage10_19 = "/leanne/events/stage10/19.webp"
    scene leanne_stage10_19
    pause
    $ msg ("Guess she figured out what gets views.")
    image leanne_stage10_20 = "/leanne/events/stage10/20.webp"
    scene leanne_stage10_20
    pause
    $ msg ("It's just so weird. She used to dunk on me for this.", who=1)
    image leanne_stage10_21 = "/leanne/events/stage10/21.webp"
    scene leanne_stage10_21
    pause
    $ hide_messenger()

    "You glance back at Mira's stream."
    image leanne_stage10_22 = "/leanne/events/stage10/22.webp"
    scene leanne_stage10_22
    "She's just finished an entire burger."
    "Then, she smirks at the camera, wiping her lips."
    mira "You guys better keep up those donations,"
    mira "I'm just getting started."
    image leanne_stage10_23 = "/leanne/events/stage10/23.webp"
    scene leanne_stage10_23

    $ show_messenger()
    $ msg ("Maybe she's trying to beat you at your own game.")
    image leanne_stage10_24 = "/leanne/events/stage10/24.webp"
    scene leanne_stage10_24
    pause
    $ msg ("Pfft. No chance. I've been doing this forever.", who=1)
    image leanne_stage10_25 = "/leanne/events/stage10/25.webp"
    scene leanne_stage10_25
    pause
    $ msg ("Yeah, but... if she keeps this up, people might start comparing you two even more.")
    image leanne_stage10_26 = "/leanne/events/stage10/26.webp"
    scene leanne_stage10_26
    "Leanne doesn't reply right away. You imagine her sitting at her desk, chewing on her lip, deep in thought. Finally, your phone buzzes again."
    $ msg ("OH SHIT I JUST HAD AN IDEA…", who=1)
    image leanne_stage10_27 = "/leanne/events/stage10/27.webp"
    scene leanne_stage10_27
    $ msg ("Yeah? What will you do?")
    image leanne_stage10_28 = "/leanne/events/stage10/28.webp"
    scene leanne_stage10_28
    "She replies in a rush"
    $ msg ("Thanks for the talk, I gotta do something, ttyl~ ❤️", who=1)
    image leanne_stage10_29 = "/leanne/events/stage10/29.webp"
    scene leanne_stage10_29
    "You stare at her last message. Something about it feels off. She's up to something—but what?"
    "For now, you shrug it off. Whatever it is, you're sure you'll find out soon enough."
    $ hide_messenger()
    image leanne_stage10_30 = "/leanne/events/stage10/30.webp"
    scene leanne_stage10_30
    "You glance back at Mira's stream for a minute before going to bed."

    if recollection == False:
        $ daytime += 1
    $ leannestage10event2 = 0
    return

label Leanne_Stage_11_Event_1:
    "Your phone buzzes with a message from Lyn just as you're settling in for the night."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("Heyyyy~ Guess what? 👀", who=1)
    pause
    $ msg ("You ate too much again?")
    pause
    $ msg ("Rude! But no. Well… not yet 😏", who=1)
    pause
    $ msg ("I'm doing a special stream tonight. You better watch~", who=1)
    pause
    $ msg ("Special how?")
    pause
    $ msg ("You'll see. Just be there. It's for you~ ❤️", who=1)
    "You raise an eyebrow at the teasing message, but before you can ask anything else, she sends a winking emoji and goes offline."
    $ msg ("😉", who=1)
    pause
    $ hide_messenger()

    "Curious, you pull up her stream when it starts."
    "The moment the screen loads, the chat is already exploding with hype."
    image leanne_stage11_7 = "/leanne/events/stage11/7.webp"
    scene leanne_stage11_7
    play music "/music/leanne_stream.ogg" if_changed
    #“Special stream?! Let’s goooooo!”
    #“Bet she’s doing something crazy tonight.”
    #“Mira better watch out lmao.”
    "Lyn appears on-screen, leaning lazily into her gaming chair, a knowing smirk on her face."
    image leanne_stage11_8 = "/leanne/events/stage11/8.webp"
    scene leanne_stage11_8
    "She's wearing a snug crop top that does little to hide just how much she's been indulging lately."
    image leanne_stage11_9 = "/leanne/events/stage11/9.webp"
    scene leanne_stage11_9
    "She shifts in her seat, letting her thick thighs spread slightly as she rests a hand on her belly."
    image leanne_stage11_10 = "/leanne/events/stage11/10.webp"
    scene leanne_stage11_10
    leanne "Alright, chat. I know you're all dying to know what's so special about tonight's stream,"
    leanne "So let's talk about our dear Mira, yeah?"
    image leanne_stage11_11 = "/leanne/events/stage11/11.webp"
    scene leanne_stage11_11
    "The chat explodes again."
    #“Oh shit, here we go.”
    #“The drama continues!”
    #“Mira bout to get cooked.”

    image leanne_stage11_12 = "/leanne/events/stage11/12.webp"
    scene leanne_stage11_12
    "Lyn chuckles, reaching off-screen to grab a large soda, taking a slow sip before continuing."
    image leanne_stage11_13 = "/leanne/events/stage11/13.webp"
    scene leanne_stage11_13
    pause
    image leanne_stage11_14 = "/leanne/events/stage11/14.webp"
    scene leanne_stage11_14
    leanne "So, chat, you guys saw how Mira suddenly added that little 'food donation' thing to her stream, right?"
    image leanne_stage11_15 = "/leanne/events/stage11/15.webp"
    scene leanne_stage11_15
    "The chat floods with messages."
    #“Yeah, she was stuffing her face like crazy.”
    #“She’s trying to catch up to you, Leanne.”
    #“Tbh, she looked kinda hot ngl.”

    image leanne_stage11_16 = "/leanne/events/stage11/16.webp"
    scene leanne_stage11_16
    "Lyn raises an eyebrow, feigning offense."
    leanne "Kinda?"
    image leanne_stage11_17 = "/leanne/events/stage11/17.webp"
    scene leanne_stage11_17
    "She leans back, stretching."
    leanne "Well, that's cute and all. But you guys think she can really outdo me? Me?"
    image leanne_stage11_18 = "/leanne/events/stage11/18.webp"
    scene leanne_stage11_18
    "The chat explodes with laughter and support."
    #“HELL NO.”
    #“Leanne supremacy.”
    #“Mira’s got nothing on you.”

    image leanne_stage11_19 = "/leanne/events/stage11/19.webp"
    scene leanne_stage11_19
    leanne "That's what I thought. Soooo… I got an idea."
    image leanne_stage11_20 = "/leanne/events/stage11/20.webp"
    scene leanne_stage11_20
    "She leans forward, eyes twinkling mischievously."
    leanne "How about we settle this? A little competition, just me and Mira. A good old-fashioned eating challenge."
    image leanne_stage11_21 = "/leanne/events/stage11/21.webp"
    scene leanne_stage11_21
    "Lyn smirks, letting the excitement build."
    "The chat erupts."
    #“NO WAY.”
    #“OMG YES.”
    #“STREAM WAR LET’S GOOOOO.”

    image leanne_stage11_22 = "/leanne/events/stage11/22.webp"
    scene leanne_stage11_22
    leanne "I haven't told Mira yet, but don't worry. She'll hear about it soon enough."
    image leanne_stage11_23 = "/leanne/events/stage11/23.webp"
    scene leanne_stage11_23
    "She winks at the camera."
    image leanne_stage11_24 = "/leanne/events/stage11/24.webp"
    scene leanne_stage11_24
    leanne "Let's see if she's got the guts to go up against me~"
    image leanne_stage11_25 = "/leanne/events/stage11/25.webp"
    scene leanne_stage11_25
    "As the chat continues to lose its mind, your phone buzzes again."

    $ show_messenger()
    $ msg ("You enjoying the show? 😘", who=1)
    pause
    $ msg ("You're evil lol. This is gonna be insane.")
    pause
    $ msg ("Hehe", who=1)
    pause
    $ hide_messenger()

    "You click off her stream and then you head to bed."

    stop music fadeout 1.0

    if recollection == False:
        $ daytime += 1
    $ leannestage11event = 0
    return

label Leanne_Stage_11_Event_2:
    #Scene: Stream Gone Wrong (Occurs shortly after reaching stage 11)
    "You decide to watch Leanne’s stream."
    image stream_girl_stuffed_event11 = "/leanne/11/stuffed.webp"
    scene stream_girl_stuffed_event11
    play music "/music/leanne_stream.ogg" if_changed
    "Upon tuning in, you can’t help noticing something is different. The donate five pizzas button is noticeably absent and there’s a feeling of dread that hangs over your mind."
    "As you linger on these strange emotions, Leanne walks into view and sits down."
    leanne "Hey everyone! Luxury Leanne here and better than ever."
    image leanne_stage11_bratouch = "/leanne/events/stage11/bratouch.webp"
    scene leanne_stage11_bratouch
    "Though she tries to hide it, her hands are constantly clasping at parts of her outfit to keep it together."
    leanne "I’m back with more Carl on Duty today. I’ve already eaten a little before the stream, but if you want to make sure I’m good and fed, feel free to donate a pizza or two my way."
    "Should you donate?"
    menu:
        "Yes. (-$5)":
            if recollection == False:
                $ money -= 5
            image stream_girl_stuffed2_event11 = "/leanne/11/stuffed2.webp"
            scene stream_girl_stuffed2_event11
            "The usual excitement in Leanne’s eyes when she receives a pizza donation is noticeably a little dimmer."
            leanne "Oops! Sorry. Almost didn’t see that one. I’ll go ahead and order the pizza now. Don’t worry, you’ll get your dance still. Just after I finish this map and get my food."
            "Waiting for a few moments on the edge of your seat, you watch with bated breath as Leanne gets up from her desk and returns with a pizza box."
            leanne "Okay, let’s do this."
            image stream_girl_eating_event11 = "/leanne/11/eating.webp"
            scene stream_girl_eating_event11
            "After taking a deep breath Leanne opens up the box and starts to devour the pizza slice by slice."
            image stream_girl_eating2_event11 = "/leanne/11/eating2.webp"
            scene stream_girl_eating2_event11
            "The worry that was previously shown on her face is replaced with joy as she continues to eat through the greasy meal."
            image stream_girl_eating3_event11 = "/leanne/11/eating3.webp"
            scene stream_girl_eating3_event11
            "By the time she finishes off the entire pizza, she’s back to her usual, cheery self."
            image stream_girl_stuffed_happy_event11 = "/leanne/11/stuffed_happy.webp"
            scene stream_girl_stuffed_happy_event11
            leanne "That was just what I needed. Thank you."
            image stream_girl_stuffed3_event11 = "/leanne/11/stuffed3.webp"
            scene stream_girl_stuffed3_event11
            "Holding onto her stuffed gut, she gets up from her seat."
            leanne "As a sign of my appreciation, let me show off a new dance I came up with. Hope you like it."
            window hide
            $ movielength = 31
            $ movieplaying = "/images/leanne/events/stage11/dancecustom.webm"
            call screen custommoviescreen
            "She begins to vigorously shake her hips back and forth. You can hear her belly sloshing about through the screen, getting faster and faster as she continues to dance to the beat."
            "Powering through her own feelings of being full, she tries her hardest to get through the dance. This combination of her tight outfit and chubby body eventually lead to…"
            #Image: Leanne standing in the middle of her room with her bare breasts popped right out of her shirt.
            image leanne_stage11_boobsslip = "/leanne/events/stage11/boobsslip.webp"
            scene leanne_stage11_boobsslip
            window hide
            pause
            "As her bosom rips through her top, she stands there in complete silence. Her stunned state gives both you and the rest of her chat ample time to look at her exposed nipples."
            image leanne_stage11_streamquit = "/leanne/events/stage11/streamquit.webp"
            scene leanne_stage11_streamquit
            window hide
            pause
            "A deluge of donation notifications finally breaks Leanne out of her stupor. Lunging forward, she abruptly shuts off the stream."
            stop music fadeout 1.0
            "More than a little concerned, you decide to message her."

            $ show_messenger()

            $ dialogue_one = []

            $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
            $ msg ("Is everything okay?")
            pause
            $ msg ("No! I probably just nuked my entire channel for that little slip up. I kept telling myself that I needed to buy a better fitting streaming outfit, but I thought that tighter fabric would be more enticing.", who=1)
            pause
            $ msg ("Calm down. It was an honest mistake. I’m sure you’ll be fine.")
            pause
            $ msg ("You’re probably right. I’ll try to talk to someone on tech support to get this worked out.", who=1)
            pause
            $ msg ("There you go. Everything will turn out okay.")
            pause
            $ msg ("I’m not so sure about that. I want to talk to you about something.", who=1)
            pause
            $ msg ("Not over text or the phone, but in person. Can you message me the next time you’re free to meet up?", who=1)
            pause
            $ msg ("Sure thing. I’ll keep you posted.")
            pause
            $ msg ("Thank you.", who=1)
            pause
            $ hide_messenger()

            #(NOTE: After this, the player will no longer be able to watch Leanne’s streams.)

        "No.":
            image stream_girl_stuffed2_event11 = "/leanne/11/stuffed2.webp"
            scene stream_girl_stuffed2_event11
            "The stream goes as normal, albeit with Leanne moving a bit more sluggishly. Perhaps a little tired from her pre-game meal, she ends the stream early and calls it a night."
            #(NOTE: If the player chooses B) No then the scene will play out again every time then tune into the stream until they choose A) Yes.)
            stop music fadeout 1.0
            return

    $ leannestage11event2 = 0
    return

label Leanne_Stage_11_Event_3:
    #Scene: Post-Stream Accident Meet Up
    #(NOTE: After the previous scene of Leanne’s accident on stream, the player will be given the option to meet up with her during their free time. Choosing to hang out with her during that time will result in the following.)
    #Image: Player’s room.
    pc "I should really get back to Leanne. I'm worried about her."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
    $ msg ("I'm free right now. Did you want to have that meeting?")
    pause
    $ msg ("Sure. Let's meet up at Bunny Bites.", who=1)
    pause
    $ msg ("Promise you won't be late?", who=1)
    pause
    $ msg ("Promise.")
    pause
    $ hide_messenger()

    "Getting your stuff together, you go to Bunny Bites."
    #Image: Bunny Bites booth seat with Leanne dressed in her incognito mode outfit.
    image leanne_stage11_arrive = "/leanne/events/stage11/arrive.webp"
    scene leanne_stage11_arrive
    "You arrive at the diner to see Lyn sitting by herself in a booth. More than a little concerned that she actually showed up on time for once, you sit down with her."
    leanne "Thank you for coming. It means a lot to me."
    pc "It's the least I can do for a friend. So, what did you want to talk about?"
    image leanne_stage11_1 = "/leanne/events/stage11/1.webp"
    scene leanne_stage11_1
    "She remains silent for a few seconds, her fingers tapping against the table."
    leanne "The accident during my last stream…it made me consider some things. The only reason I had that little boob slip was because I was trying to please my audience."
    leanne "What they expect is a bubbly streamer girl with a big appetite and big personality. I just got a little too carried away trying to play up the act."
    pc "You did nothing wrong. Trying to show your appreciation to your fans is nothing to be ashamed of."
    image leanne_stage11_2 = "/leanne/events/stage11/2.webp"
    scene leanne_stage11_2
    "She pauses for another moment, wiping a single tear from her face."
    leanne "But lying to their faces is. I'm not the person they see during the streams. Hell, you know how far I've gone to try and garner sympathy."
    leanne "It leaves me feeling empty. It's like I have two sides of myself that are fighting to take control of my life."
    image leanne_stage11_3 = "/leanne/events/stage11/3.webp"
    scene leanne_stage11_3
    "Chewing on her lips, she leans across the table to look you in the eyes."
    leanne "I'm torn between Leanne, the popular streamer who thrives on viewer interaction and Lyn the introverted nerd who'd rather have a calm night at home."
    leanne "I honestly don't know what would be better for me. Sometimes I have to ask myself, who am I?"
    "She looks at you as if expecting an answer. You can tell by the way she's staring at you that you have to choose your next words very carefully."
    menu:
        "You're Lyn.":
            if recollection == False:
                $ leannechoice = 1
                $ leanne.name = 'Lyn'
                $ Lynname = 'Lyn'
            pc "You're Lyn. A woman who did what she needed to do to get by."
            image leanne_stage11_4 = "/leanne/events/stage11/4.webp"
            scene leanne_stage11_4
            "Lyn sits back in her seat, staring at you."
            pc "However, I think it's time you told everyone the truth."
            pc "Not just about the boyfriend thing, but about who you really are. If they really are your fans, they will be willing to hear you out and accept you for you."
            "A small smile forms on Lyn's face. Without warning, she lunges forward to embrace you in a hug."
            image leanne_stage11_6 = "/leanne/events/stage11/6.webp"
            scene leanne_stage11_6
            leanne "Thank you."
            "Backing away from the hug, she gathers up her stuff and begins to walk out of the diner."
            image leanne_stage11_eventend = "/leanne/events/stage11/eventend.webp"
            scene leanne_stage11_eventend
            pc "Where are you going?"
            leanne "To take care of some things. I'm going to take a short break from streaming for a while. I'll give you an update on when I'm back. Thanks again for everything."
            "Watching her leave, you ponder what you may have done to her with a few words. Hoping for the best, you get up from the table and make your way home."

        "You're Leanne.":
            if recollection == False:
                $ leannechoice = 2
                $ Lynname = 'Leanne'
                $ leanne.name = 'Leanne'
            pc "You're Leanne. One of the most entertaining streamers I've ever seen."
            image leanne_stage11_4 = "/leanne/events/stage11/4.webp"
            scene leanne_stage11_4
            "Leanne sits back in her seat, staring at you."
            pc "Sure you had to tell a few lies along the way, but that was all part of constructing this persona."
            pc "I've been watching you long enough to see how much passion you put into your streams. Don't give up on it just because of a single slip up."
            pc "Luxury Leanne's fans are eager for the day they get to see her doing what she loves again."
            "A small smile forms on Leanne's face. Without warning, she lunges forward to embrace you in a hug."
            image leanne_stage11_6 = "/leanne/events/stage11/6.webp"
            scene leanne_stage11_6
            leanne "Thank you."
            "Backing away from the hug, she gathers up her stuff and begins to walk out of the restaurant."
            image leanne_stage11_eventend = "/leanne/events/stage11/eventend.webp"
            scene leanne_stage11_eventend
            pc "Where are you going?"
            leanne "To take care of some things. I'm going to take a short break from streaming for a while. I'll give you an update on when I'm back. Thanks again for everything."
            "Watching her leave, you ponder what you may have done to her with a few words. Hoping for the best, you get up from the table and make your way home."
    $ leannestage11event3 = 0
    if recollection == False:
        $ daycount = 0
        $ daytime += 1
        jump freetime
    return

label Leanne_Stage_11_Event_4:
    #Mira Solo Stream - Event 1
    "You open Mira’s stream out of curiosity."
    image leanne_stage11_26 = "/leanne/events/stage11/26.webp"
    scene leanne_stage11_26
    "Ever since Leanne got banned, she’s been soaking up all the attention, her viewership skyrocketing."
    "The moment the stream loads, you’re greeted with a close-up of Mira, lounging confidently in her gaming chair, her hair a little messier than usual."
    image leanne_stage11_27 = "/leanne/events/stage11/27.webp"
    scene leanne_stage11_27
    "A half-finished burger rests in her hand, her lips glistening from the last bite."
    image leanne_stage11_28 = "/leanne/events/stage11/28.webp"
    scene leanne_stage11_28
    "She barely acknowledges it as she reads chat, smirking."
    image leanne_stage11_29 = "/leanne/events/stage11/29.webp"
    scene leanne_stage11_29
    mira "Alright, alright, I get it."
    image leanne_stage11_30 = "/leanne/events/stage11/30.webp"
    scene leanne_stage11_30
    "Mira chuckles, licking a bit of sauce off her thumb."
    image leanne_stage11_31 = "/leanne/events/stage11/31.webp"
    scene leanne_stage11_31
    pause
    image leanne_stage11_32 = "/leanne/events/stage11/32.webp"
    scene leanne_stage11_32
    mira "You guys love this new 'content' huh? What, did you all forget I'm actually good at games too?"
    "Chat scrolls by at rapid speed."
    image leanne_stage11_34 = "/leanne/events/stage11/34.webp"
    scene leanne_stage11_34
    "Mira about to outgrow Leanne fr 🍔🍕🍟" 
    "The queen of gaming AND eating? We winning." 
    "You always make fun of Leanne but look at you now lmao." 
    "Tbh you look kinda cute with a lil extra on you."
    image leanne_stage11_35 = "/leanne/events/stage11/35.webp"
    scene leanne_stage11_35
    "Mira scoffs, rolling her eyes."
    mira "Please. I can still kick your asses in-game while stuffing my face. Unlike a certain someone, I don’t get slower when I eat."
    "As she talks, a donation alert flashes on-screen."
    "$20 from Viewer: ‘More fries, please. 😉’"
    image leanne_stage11_36 = "/leanne/events/stage11/36.webp"
    scene leanne_stage11_36
    "Mira raises a brow, then shrugs."
    mira "Fine, fine. Since you paid for it."
    image leanne_stage11_37 = "/leanne/events/stage11/37.webp"
    scene leanne_stage11_37
    "She grabs a handful of fries from a container and tosses them into her mouth, chewing lazily."
    image leanne_stage11_38 = "/leanne/events/stage11/38.webp"
    scene leanne_stage11_38
    pause
    image leanne_stage11_39 = "/leanne/events/stage11/39.webp"
    scene leanne_stage11_39
    mira "Happy? You guys are so weird."
    menu:
        "Donate (-$25)":
            if money <= 24:
                "Another donation alert pops up almost instantly."
                #$25 from ‘BigEaterFan’: ‘Bet you can’t finish half the pizza in one minutes. 😏’
                "Mira blinks at the message, then scoffs."
                mira "Oh, you think I can’t?"
                "Without another word, she digs in, shoveling slices into her mouth aggressively."
                "The chat erupts."
                #"YO WTF 💀💀💀" "Mira going feral lmao" "Bro, she didn’t even chew." "Okay I see why Leanne was mad now 💀"
                "Mira wipes her mouth with the back of her hand, letting out a small, satisfied hum."
                mira "There. That good enough for you?"
                "She leans closer to the camera, licking the last bit of cheese from her fingertip, her gaze flicking toward chat."
                mira "Bet you guys are losing your minds right now."
                "More donation messages flood in, each one encouraging her to eat more, try different things, or outright teasing her about keeping up with Leanne. Mira just grins."
                mira "Alright, fine. Let’s see what you guys got. Keep ‘em coming. I’m in a good mood tonight."
                "Her smirk widens as she leans back slightly, stretching with a satisfied sigh."
                mira "Hope you guys can afford to keep up with ME. And trust me... I'm only getting started."
            else:
                $ money -= 25
                image leanne_stage11_40 = "/leanne/events/stage11/40.webp"
                scene leanne_stage11_40
                "You hesitate for a moment before deciding to join in. You type in a donation message and send it off."
                image leanne_stage11_41 = "/leanne/events/stage11/41.webp"
                scene leanne_stage11_41
                "$25 from You: ‘Let’s see how fast you can finish that burger. Bet you can’t do it in one minute. 😏’"
                image leanne_stage11_42 = "/leanne/events/stage11/42.webp"
                scene leanne_stage11_42
                "Mira blinks as the alert pops up, then scoffs."
                mira "Oh, you think I can’t?"
                image leanne_stage11_43 = "/leanne/events/stage11/43.webp"
                scene leanne_stage11_43
                "She picks up the remaining half of her burger and, without another word, starts devouring it aggressively."
                image leanne_stage11_44 = "/leanne/events/stage11/44.webp"
                scene leanne_stage11_44
                "The chat erupts."
                image leanne_stage11_45 = "/leanne/events/stage11/45.webp"
                scene leanne_stage11_45
                "YO WTF 💀💀💀"
                image leanne_stage11_46 = "/leanne/events/stage11/46.webp"
                scene leanne_stage11_46
                "Mira going feral lmao"
                image leanne_stage11_47 = "/leanne/events/stage11/47.webp"
                scene leanne_stage11_47
                "Bro, she didn’t even chew."
                image leanne_stage11_48 = "/leanne/events/stage11/48.webp"
                scene leanne_stage11_48
                "Okay I see why Leanne was mad now 💀"
                image leanne_stage11_49 = "/leanne/events/stage11/49.webp"
                scene leanne_stage11_49
                pause
                image leanne_stage11_50 = "/leanne/events/stage11/50.webp"
                scene leanne_stage11_50
                "Mira wipes her mouth with the back of her hand, letting out a small, satisfied hum."
                image leanne_stage11_51 = "/leanne/events/stage11/51.webp"
                scene leanne_stage11_51
                mira "There. That good enough for you?"
                "She leans closer to the camera, licking the last bit of sauce from her fingertip, her gaze flicking toward chat."
                image leanne_stage11_52 = "/leanne/events/stage11/52.webp"
                scene leanne_stage11_52
                "She stands up"
                image leanne_stage11_53 = "/leanne/events/stage11/53.webp"
                scene leanne_stage11_53
                mira "Bet you guys are losing your minds right now."
                image leanne_stage11_54 = "/leanne/events/stage11/54.webp"
                scene leanne_stage11_54
                "More donation messages flood in, each one encouraging her to eat more, try different things, or outright teasing her about keeping up with Leanne. Mira just grins."
                image leanne_stage11_55 = "/leanne/events/stage11/55.webp"
                scene leanne_stage11_55
                mira "Alright, fine. Let’s see what you guys got. Keep ‘em coming. I’m in a good mood tonight."
                "Her smirk widens as she reaches for the camera."
                image leanne_stage11_56 = "/leanne/events/stage11/56.webp"
                scene leanne_stage11_56
                mira "Let’s see if you can actually keep up with me."

        "Don't Donate.":
            "Another donation alert pops up almost instantly."
            #$25 from ‘BigEaterFan’: ‘Bet you can’t finish half the pizza in one minutes. 😏’
            "Mira blinks at the message, then scoffs."
            mira "Oh, you think I can’t?"
            "Without another word, she digs in, shoveling slices into her mouth aggressively."
            "The chat erupts."
            #"YO WTF 💀💀💀" "Mira going feral lmao" "Bro, she didn’t even chew." "Okay I see why Leanne was mad now 💀"
            "Mira wipes her mouth with the back of her hand, letting out a small, satisfied hum."
            mira "There. That good enough for you?"
            "She leans closer to the camera, licking the last bit of cheese from her fingertip, her gaze flicking toward chat."
            mira "Bet you guys are losing your minds right now."
            "More donation messages flood in, each one encouraging her to eat more, try different things, or outright teasing her about keeping up with Leanne. Mira just grins."
            mira "Alright, fine. Let’s see what you guys got. Keep ‘em coming. I’m in a good mood tonight."
            "Her smirk widens as she leans back slightly, stretching with a satisfied sigh."
            mira "Hope you guys can afford to keep up with ME. And trust me... I'm only getting started."
    
    image leanne_stage11_57 = "/leanne/events/stage11/57.webp"
    scene leanne_stage11_57
    "You watch the rest of the stream until she finishes eating all the things viewers donated for."
    "You decide to go to bed."
    "This is the final Mira event in this update."
    $ leannestage11event4 = 0
    if recollection == False:
        $ daytime += 1
        jump freetime
    return

label Leanne_Stage_11_Event_5:
    #Mira Solo Stream - Event 2
    "You open Mira’s stream, settling in as the screen loads."
    "The viewership counter is climbing fast—she's clearly thriving with all the attention."
    "As the stream comes into focus, you see her sitting comfortably, sipping on a large soda with a half-eaten burger resting on the desk in front of her."
    "Her expression is confident as she scrolls through chat, her fingers lazily tapping against her cup."
    "You type “Hi Mira” in chat which she replies to."
    mira "Oh? Look who decided to show up again. [playername], glad to see you here."
    "She smirks, taking another sip."
    mira "Didn’t think you'd keep coming back. What, you enjoying the show?"
    "She winks at the camera before chuckling to herself."
    "Chat, as usual, is moving at lightning speed."
    #"Mira already snacking? Stream just started lol." "She's looking bigger again 👀" "Damn she’s really outpacing Leanne at this rate." "Mira, be honest, do you even cook or just live on donations now? 😂"
    "Mira raises an eyebrow at that last comment."
    mira "Excuse you, I can cook. I just prefer not to, because why would I when you guys keep paying for my meals?"
    "As if on cue, a loud donation alert rings through the stream."
    #$50 from ‘DanceEnthusiast’: ‘Alright, enough eating for a sec—let’s see a little dance.’
    "Mira stops mid-bite, blinking at the screen."
    mira "...Seriously? That’s what you wanna spend your money on?"
    "She leans back, tapping her fingers on the desk, pretending to think it over. Then she smirks."
    mira "Alright, fine. But you better appreciate this."
    "She pushes her chair back and stands up, stretching a little before striking a playful pose."
    "The chat instantly explodes."
    #"AYOOO NO WAY SHE AGREED" "Mira dancing live? This is a historical event." "She better not half-ass this."
    "Mira rolls her eyes but grins."
    "A catchy beat starts playing as she sways her hips, rolling into a smooth, teasing dance."
    "She keeps it light, throwing in a few dramatic flourishes and exaggerated expressions, making a show of it."
    "Halfway through, she spins and gives a playful over-the-shoulder glance at the camera, smirking as she sees the chat absolutely losing it."
    #"HOLY SH*T LET'S GOOO" "Okay that was actually kinda 🔥." "Mira secretly been practicing???"
    "After a minute, she flops back into her chair, grabbing her soda and taking a long sip as if she just ran a marathon."
    mira "There. Hope you enjoyed your money’s worth,"
    "she teases, tapping the donation alert."
    mira "You guys are ridiculous."
    "More donations roll in, some praising her, others already requesting another dance."
    "Mira just shakes her head with a laugh."
    mira "Yeah, yeah. Keep dreamin’. Anyway, let’s get back to what I do best—eating and carrying noobs in games."
    "The stream continues, but one thing is clear: Mira is loving every second of the attention."
    "You watch the rest of the stream until she finishes eating all the things viewers donated for."
    "You decide to go to bed."

    if recollection == False:
        $ daytime += 1
    $ leannestage11event5 = 0
    return

label Leanne_Stage_11_Event_6:
    #Mira Solo Stream - Event 3
    "You open Mira’s stream, already curious about what chaos she’s up to tonight."
    "As the screen loads, you see her leaning back in her chair, a confident smirk on her face."
    "The remnants of a fast-food feast are scattered around her desk—empty wrappers, a half-finished drink, and a large takeout bag still filled with who knows what."
    mira "Alright, alright, I see the donations coming in already."
    "Mira laughs, stretching her arms."
    mira "You guys are really trying to test me tonight, huh? Think you can break me? We’ll see about that."
    "Chat scrolls wildly."
    #"Mira, you’re actually eating more every stream wtf 😳" "Queen of gaming AND eating, we love to see it." "I got $20 on her tapping out before the hour’s up." "She needs an eating challenge stream fr."
    "Mira raises a brow as another donation alert pops up."
    #$50 from HotSauceKing: ‘Bet you can’t handle my special challenge. Extra-spicy wings, no drinks allowed.🔥’
    mira "Oh, you guys are evil tonight."
    "She reaches off-screen and pulls up a takeout box, flipping it open to reveal a pile of wings slathered in an ominous-looking red sauce."
    mira "Alright, chat. You think I can’t handle some heat? Please."
    "She grabs a wing and takes a confident bite. Almost immediately, she pauses, blinking rapidly."
    "Chat explodes."
    #"LMAO SHE UNDERESTIMATED IT 💀" "Oh no no no she’s struggling" "Regret is setting in 😂"
    "Mira exhales sharply, her face scrunching up for a second before she forces a smirk."
    mira "Okay. That’s definitely hot. But I’m not tapping out."
    "She pushes through, finishing wing after wing, her breath getting heavier, her eyes watering slightly."
    "By the time she’s done, she looks visibly flustered but victorious."
    mira "Alright, HotSauceKing, you got me a little,"
    mira "But next time? You better bring something actually challenging."
    "Another donation alert pings."
    #$75 from BigEaterFan: ‘One extra-large burrito, five minutes. No breaks. Let’s see what you got.’
    mira "Oh, you guys are really out for blood tonight. Fine. Bring it on."
    "She pulls out an absolute beast of a burrito from the takeout bag, unwrapping it slowly for the camera."
    mira "Look at this thing. You guys are ridiculous. But alright, let’s do this."
    "A timer appears on-screen as she takes the first massive bite, chewing quickly."
    "The chat goes insane."
    #"No way she finishes that in time." "SHE’S ACTUALLY GOING FOR IT 😳" "Mira vs Food when?"
    "Bite after bite, Mira powers through, looking determined yet slightly overwhelmed."
    "The timer ticks down—two minutes left, one minute, thirty seconds."
    "The last bite goes in just as the timer hits five minutes."
    "She leans back, looking absolutely stuffed, letting out a slow exhale before smirking at the camera."
    mira "That all you got, chat? I told you, you can’t break me."
    "More donations flood in, some praising her, others queuing up even more ridiculous challenges."
    "Mira chuckles, patting her stomach lightly."
    mira "Alright, alright, you guys are crazy. But I like a challenge. Keep ‘em coming—I’m not done yet."
    "She leans forward, eyes glinting mischievously."
    mira "Hope your wallets can keep up, though. Because I can do this all night."
    "You watch the rest of the stream until she finishes eating all the things viewers donated for."
    "You decide to go to bed."

    if recollection == False:
        $ daytime += 1
    $ leannestage11event6 = 0
    return

label Leanne_Stage_11_Event_7:
    #Mira Solo Stream - Event 4
    "You open Mira’s stream, already expecting another night of chaos."
    "As the screen loads, you see her lounging in her chair, one arm resting on her stomach, her other hand idly scrolling through chat."
    "There’s an open pizza box beside her, and she casually grabs another slice, taking a big bite without a second thought."
    mira "Alright, alright,"
    mira "let’s see what nonsense you guys are up to tonight."
    "The chat scrolls wildly, messages flying by at an insane speed."
    #“Mira, real talk, you’ve been looking bigger lately 👀” “Are you gaining on purpose???” “Leanne who? Mira’s taking over.” “No way she hasn’t noticed LMAO”
    "Mira pauses mid-bite, raising a brow as she sees the messages piling up."
    "She smirks, chewing slowly before swallowing."
    mira "You guys are nosy as hell, huh?"
    "She leans forward, resting her chin in her hand."
    mira "What, you all take a little break from harassing Leanne just to start on me instead?"
    "Chat explodes again."
    #“So you have noticed?!” “She’s dodging the question 💀” “No way you can eat like this every night and NOT gain” “Mira pls just admit it”
    "Mira clicks her tongue, shaking her head."
    mira "Fine, fine. I’ll be real with you guys. Have I noticed? Maybe."
    "She shifts slightly in her chair, a playful glint in her eyes."
    mira "Am I worried about it? Not even a little."
    "She grabs another slice, twirling it in her fingers."
    mira "What, you guys don’t like a little extra cushion? Makes gaming comfier, y’know."
    "She grins, taking a big bite, chewing deliberately as chat floods with reactions."
    #“SHE SAID IT” “Extra cushion, huh? 👀” “Mira embracing the gains LET’S GOOOO” “New arc unlocked: The Mira Bulk”
    "Mira finishes her slice, dusting her hands off before stretching lazily."
    mira "You guys are obsessed, seriously. I swear, you all pay more attention to my body than I do."
    "She laughs, shaking her head."
    mira "But whatever. If you’re that into it, keep watching. Maybe I’ll surprise you."
    "The chat explodes again, some cheering, some teasing, and others already making predictions about how much bigger she might get."
    "Mira just smirks, clearly enjoying the attention, before shifting the focus back to her game."
    "You watch the rest of the stream until she finishes eating all the things viewers donated for."
    "You decide to go to bed."

    if recollection == False:
        $ daytime += 1
    $ leannestage11event7 = 0
    return

label Leanne_Stage_11_Event_8:
    "You open Mira’s stream late into the night, and the moment it loads, you can tell she’s had quite the feast."
    "She’s leaned back in her chair, her hoodie slightly unzipped, revealing just how full she looks."
    "Wrappers, cups, and stray fries litter her desk—evidence of a long night of indulgence."
    mira "Ughhh... you guys really did it tonight,"
    "she groans, stretching slightly before resting a hand on her stomach."
    mira "I’m so full… like, actually, I don’t think I can move."
    "Chat immediately starts teasing her."
    #"Mira, you look DONE lmao 😂" "Tapping out already? You weak?" "SHE’S RUBBING HER BELLY AYO 😳" "You earned it, queen, take a nap on stream."
    "Mira lazily smirks, rubbing slow circles on her stomach without thinking."
    mira "Shut up, I earned this, okay? I destroyed every challenge tonight. You guys can’t even act like I didn’t."
    "A donation alert pops up."
    #$25 from TooMuchFood: ‘Damn, Mira, you gonna be able to get out of that chair? 😏’
    "She rolls her eyes, suppressing a yawn."
    mira "Pfft. Maybe. If I even try. Might just sleep here, who knows."
    "She leans forward slightly, but then groans and flops back again."
    mira "Nope. Not happening. This is my life now. Just me and my food coma."
    "Chat explodes in laughter and teasing messages."
    #"Mira’s officially defeated. GG." "New stream title: ‘Mira Gets Stuck in Chair Live on Stream’ 💀" "We love a stuffed, sleepy queen."
    "Mira lets out another dramatic sigh before yawning mid-sentence."
    mira "Alright, alright… You guys are just so hilarious tonight. But whatever, I did win, so it’s fine. No complaints from me."
    "She lazily waves a hand toward the camera, her eyes drooping slightly."
    mira "Gonna hang out for a bit longer, but I swear, if one more of you donates food, I’m banning you. For real this time."
    "She grins, clearly not serious."
    "The stream lingers on, Mira getting progressively sleepier, occasionally responding to messages with half-mumbled words before finally sighing."
    mira "Alright, I’m calling it here before I pass out. You guys got your show, now let me rest."
    "She flashes a lazy peace sign, stifles another yawn, and ends the stream, leaving behind a chat full of laughing viewers and donation alerts still rolling in."
    "You decide to go to bed."

    if recollection == False:
        $ daytime += 1
    $ leannestage11event8 = 0
    return

label Leanne_Stage_12_Event_1:
    if leannechoice == 1:
        #Scene: Lyn’s Return
        #(NOTE: The following should occur when the player is in his room a few weeks after making the Lyn/Leanne decision)
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Lyn', dialogue=dialogue_one)
        $ msg ("Hi there. I know it’s been a while since we last talked. I think I’m about ready to make my return, but I want to make sure you’re there for it. Can you watch tonight?", who=1)
        pause
        menu:
            "I’ll be there.":
                $ msg ("I’ll be there.")
                pause
                $ msg ("You promise?", who=1)
                pause
                $ msg ("You can count on me.")
                pause
                $ msg ("THANK YOU SO SO MUCH x)! Here’s the link for tonight’s stream. It’s going to be a little different than usual. See you there.", who=1)
                pause
                $ hide_messenger()
            "I’m sorry, I have plans this evening.":
                $ msg ("I’m sorry, I have plans this evening.")
                pause
                $ msg ("That’s okay. I’ll message you again some other time to see when you’re free.", who=1)
                pause
                $ hide_messenger()
                return
                #(NOTE: If the player chooses this option, Lyn will message them each following day until B) is chosen)

        if recollection == False:
            $ leanne.stage = 12
            $ leanne.weight = 116
        "Upon receiving the link, you click on it and are met with a screen asking if you’re 18 years or older."
        "Taking another glance at the website, you realize that it’s not for Fidget."
        "Instead, you’ve been directed to EroticaBase, a very infamous porn video site."
        "Wondering what exactly Lyn has planned, you confirm your details and get comfortable while you wait for the stream to begin."
        image lyn_stage12_1 = "/leanne/events/stage12/lyn1.webp"
        scene lyn_stage12_1
        play music "/music/leanne_stream.ogg" if_changed
        "As the stream starts up, you’re met with an unfamiliar sight."
        "It takes a minute to recognize her with her brown hair, drab clothes, and extra weight, but you finally identify the woman on screen as Lyn."
        image lyn_stage12_2 = "/leanne/events/stage12/lyn2.webp"
        scene lyn_stage12_2
        "Her new appearance is quickly pointed out by the viewers that start to filter in."
        "Questions begin to fill up the chat wondering where she’s been. Momentarily ignoring them, Lyn takes a deep breath and begins to speak."
        image lyn_stage12_3 = "/leanne/events/stage12/lyn3.webp"
        scene lyn_stage12_3
        leanne "Hello, everyone. This is Luxury Leanne, or at least the woman that calls herself that. I know you're all wondering where I've been."
        leanne "The answer is that I’ve been taking a break to reassess how I do streams and, more importantly, who I am."
        image lyn_stage12_4 = "/leanne/events/stage12/lyn4.webp"
        scene lyn_stage12_4
        leanne "The conclusion I’ve come to is that I don’t want to pretend to be something I’m not anymore. This means telling you the truth."
        leanne "That story I told you all about my ex-boyfriend leaving me was a complete lie. I made it up to try and garner your sympathy."
        leanne "At that time, I used the excuse that it was okay as long as it helped me put food on my plate, but that doesn’t mean it was right. From the bottom of my heart, I’m sorry."
        image lyn_stage12_5 = "/leanne/events/stage12/lyn5.webp"
        scene lyn_stage12_5
        "Lyn pauses for a few moments, holding back tears as she carefully watches the chat."
        "While a few of the viewers log out after leaving some less than savory comments, a good portion still sticks around."
        "A few moments later, the nasty remarks are buried underneath a flood of comments happy to see her again and accepting her apology."
        "The people that stay behind seem to give Lyn enough motivation to continue."
        image lyn_stage12_6 = "/leanne/events/stage12/lyn6.webp"
        scene lyn_stage12_6
        leanne "Thank you all for being so kind. From this point forward, I want to be honest with you."
        leanne "Not as some persona named Luxury Leanne who’s larger than life. I want you all to see the real me, Lyn."
        image lyn_stage12_7 = "/leanne/events/stage12/lyn7.webp"
        scene lyn_stage12_7
        "Scooting back from her desk, Lyn makes sure the camera can see her entire body as she guides her hand towards her crotch."
        leanne "To do this, I feel like I need to reveal everything I am to you. I hope this will suffice."
        image lyn_stage12_8 = "/leanne/events/stage12/lyn8.webp"
        scene lyn_stage12_8
        window hide
        pause
        "Pulling down her pants is more than enough to drastically change the mood of the stream."
        "You’re given the reason she chose EroticaBase for her return as she drags down her panties to reveal her exposed womanhood."
        if persistent.masturbation:
            scene black with dissolve
            "Lyn pleasures herself on stream."
            image lyn_stage12_12 = "/leanne/events/stage12/lyn12.webp"
            scene lyn_stage12_12
            "When Lyn finally recovers and pulls up her pants, she once more pushes her chair up to her desk."
            leanne "I hope that was enough to prove my point. I’ll be making a post about the details of my return on my socials soon."
            leanne "For now I’ll be signing off. Thank you all again for supporting me. I hope to see you soon."
            stop music fadeout 1.0
            scene player_room
            "Not long after the stream ends, you receive another message from Lyn."
            $ show_messenger()

            $ dialogue_one = []

            $ switch_dialogue(name='Lyn', dialogue=dialogue_one)
            $ msg ("Do you think it went well?", who=1)
            pause
            $ msg ("It certainly got people’s attention. Are you sure this is what you want to do?")
            pause
            $ msg ("Not entirely. But it's a step forward. Would you be able to meet up with me sometime? I feel like I need to talk to you in person again.", who=1)
            pause
            $ msg ("It’s a date.")
            pause
            $ msg ("Thanks! See you then.", who=1)
            pause
            $ hide_messenger()

            $ leannestage12event = 0
            if recollection == False:
                $ daytime += 1
                $ phonecall = 1
                #Unlocks Lyn Undress in the stats page.
                $ renpy.notify("Lyn Undress option unlocked in stats screen.")
                window hide
                pause
            return
        image lyn_stage12_9 = "/leanne/events/stage12/lyn9.webp"
        scene lyn_stage12_9
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage12/lyn10.webm" loop
        show movie with dissolve
        pause
        "Keeping her vision focused on the camera and the chat, Lyn begins to rub against her labia. Her finger movements show no hesitation as she proceeds to pleasure herself."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage12/lyn10_2.webm" loop
        show movie with dissolve
        window hide
        pause
        "As her speed increases, she begins to let out a series of moans."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage12/lyn10.webm" loop
        show movie with dissolve
        "Over the course of her masturbation session, she keeps her vision set on her screen, as if locking eyes with all of the people watching her moment of vulnerability."
        window hide
        pause
        stop movie
        image lyn_stage12_11 = "/leanne/events/stage12/lyn11.webp"
        scene lyn_stage12_11
        "She manages to keep her gaze on the screen up until her moment of climax. Her eyes are forced closed as she lets out a euphoric cry."
        "When the moment passes, she takes a few seconds to sit back in her chair to wait for the lingering ecstasy to dissipate."
        image lyn_stage12_12 = "/leanne/events/stage12/lyn12.webp"
        scene lyn_stage12_12
        "When Lyn finally recovers and pulls up her pants, she once more pushes her chair up to her desk."
        leanne "I hope that was enough to prove my point. I’ll be making a post about the details of my return on my socials soon."
        leanne "For now I’ll be signing off. Thank you all again for supporting me. I hope to see you soon."
        stop music fadeout 1.0
        scene player_room
        "Not long after the stream ends, you receive another message from Lyn."
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Lyn', dialogue=dialogue_one)
        $ msg ("Do you think it went well?", who=1)
        pause
        $ msg ("It certainly got people’s attention. Are you sure this is what you want to do?")
        pause
        $ msg ("Not entirely. But it's a step forward. Would you be able to meet up with me sometime? I feel like I need to talk to you in person again.", who=1)
        pause
        $ msg ("It’s a date.")
        pause
        $ msg ("Thanks! See you then.", who=1)
        pause
        $ hide_messenger()

        $ leannestage12event = 0
        if recollection == False:
            $ daytime += 1
            $ phonecall = 1
            #Unlocks Lyn Undress in the stats page.
            $ renpy.notify("Lyn Undress option unlocked in stats screen.")
            window hide
            pause
        return

    elif leannechoice == 2:
        #Scene: Leanne’s Return
        #(NOTE: The following should occur when the player is in his room a few weeks after making the Lyn/Leanne decision)
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
        $ msg ("Long time no speak, my biggest fan! Thinking of making my big return tonight, but I want to make sure you’re there for it. You free?", who=1)
        pause
        menu:
            "I’ll be there.":
                $ msg ("I’ll be there.")
                pause
                $ msg ("For real?", who=1)
                pause
                $ msg ("You can count on me.")
                pause
                $ msg ("NICE! Here’s the link to the stream. Trust me, you don’t want to miss it.", who=1)
                pause
                $ hide_messenger()
            "I’m sorry, I have plans this evening.":
                $ msg ("I’m sorry, I have plans this evening.")
                pause
                $ msg ("That sucks. Ah well. I’ll hit you up again later.", who=1)
                pause
                $ hide_messenger()
                return
                #(NOTE: If the player chooses this option, Lyn will message them each following day until B) is chosen)

        if recollection == False:
            $ leanne.stage = 12
            $ leanne.weight = 116
        "Upon receiving the link, you click on it and are met with a screen asking if you’re 18 years or older."
        "Taking another glance at the website, you realize that you’re not on Fidget."
        "Instead, you’ve been directed to EroticaBase, a very infamous porn video site."
        "Wondering what exactly Leanne has planned, you confirm your details and get comfortable while you wait for the stream to begin."
        image leanne_stage12_1 = "/leanne/events/stage12/leanne1.webp"
        scene leanne_stage12_1
        play music "/music/leanne_stream.ogg" if_changed
        "As the stream starts up, you’re met with a familiar sight."
        "Though Leanne’s gained quite a bit of extra weight since you last saw her."
        "It works alongside the bright shade of pink in her hair and skimpy outfit to ensure your attention is completely focused on her."
        image leanne_stage12_2 = "/leanne/events/stage12/leanne2.webp"
        scene leanne_stage12_2
        "While she waits for more people to join, she seems to be fidgeting with anticipation, occasionally shooting a wide grin towards the camera."
        "Questions begin to fill up the chat wondering where she’s been, but she only addresses her audience after the viewer count becomes high enough."
        image leanne_stage12_3 = "/leanne/events/stage12/leanne3.webp"
        scene leanne_stage12_3
        leanne "Hey there, loyal fans! Luxury Leanne here ready for her big return. You're probably all wondering where I've been."
        leanne "Well, aside from dealing with the hassle that is Fidget’s terms of service to get my channel back, I’ve taken some time to re-assess who I am."
        image leanne_stage12_4 = "/leanne/events/stage12/leanne4.webp"
        scene leanne_stage12_4
        leanne "The conclusion I’ve come to is that I love doing these streams. It’s through all of your support that I’ve been able to feasibly make a living doing this."
        leanne "In return, I want to make sure to return your kindness by being the best streamer I can be!"
        image leanne_stage12_5 = "/leanne/events/stage12/leanne5.webp"
        scene leanne_stage12_5
        "Leanne pauses for a few moments, letting the chat scroll before her eyes."
        "Her words throw the audience into a frenzy, each and every one of them eager to express their excitement for her return."
        "Underneath a flood of virtual cheers, Leanne’s grin becomes even wider."
        image leanne_stage12_6 = "/leanne/events/stage12/leanne6.webp"
        scene leanne_stage12_6
        leanne "Thank you all so much! I promise to make it up to you with a bigger and better Luxury Leanne."
        leanne "While I have some exciting projects in mind for the future, for now let me show you why I’m not streaming on my usual channel."
        image leanne_stage12_7 = "/leanne/events/stage12/leanne7.webp"
        scene leanne_stage12_7
        "Scooting back from her desk, Leanne effortlessly removes all of her clothing to leave herself completely naked. As to be expected, this drives the chat crazy."
        leanne "Yeah, can’t do this on Fidget. Figured my little slip up during my previous stream was a sign to branch out in terms of content."
        leanne "While I was going to just finger myself for my loyal viewers, I decided that wasn’t enough."
        image leanne_stage12_8 = "/leanne/events/stage12/leanne8.webp"
        scene leanne_stage12_8
        if persistent.masturbation:
            scene black with dissolve
            "Leanne pleasures herself on stream."
            image leanne_stage12_12 = "/leanne/events/stage12/leanne12.webp"
            scene leanne_stage12_12
            "When Leanne finally recovers, she shoots the chat another smile. Rolling back up to the desk, she wipes down her toy with a towel and places it in full view of her audience."
            leanne "I think that was more than enough to prove my point. At the very least, I would hope you enjoyed that session at least half as much as I did."
            leanne "As for the details of my return to streaming, I’ll be making a post on my socials in the near future. For now, this is Luxury Leanne signing off!"
            stop music fadeout 1.0
            scene player_room
            "Not long after the stream ends, you receive another message from Leanne."
            $ show_messenger()

            $ dialogue_one = []

            $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
            $ msg ("So, what did you think?", who=1)
            pause
            $ msg ("It certainly got people’s attention. Are you sure this is what you want to do?")
            pause
            $ msg ("Nope, but it feels good so I’m still going for it. That being said, I wouldn’t mind chatting about it with you over some good food. Catch you IRL sometime?", who=1)
            pause
            $ msg ("It’s a date.")
            pause
            $ msg ("I’ll hold you to that.", who=1)
            pause
            $ hide_messenger()

            $ leannestage12event = 0
            if recollection == False:
                $ daytime += 1
                $ phonecall = 1
                #Unlocks Leanne Undress in the stats page.
                $ renpy.notify("Leanne Undress option unlocked in stats screen.")
                window hide
                pause
            return
        "Reaching below her desk, she sits back up to show off the girthy dildo in her hands."
        leanne "If I’m going to do this, I wanted it to be just as big and bombastic as myself. But enough talk, let’s get to the main event."
        image leanne_stage12_9 = "/leanne/events/stage12/leanne9.webp"
        scene leanne_stage12_9
        "Keeping her vision focused on the camera and the chat, Leanne slowly slides the dildo into her waiting womanhood."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage12/leanne10.webm" loop
        show movie with dissolve
        window hide
        pause
        "Despite her eagerness, you can still spot some hesitation as she gradually pushes the toy in further and further."
        "When she finally manages to sink it all the way, that nervousness disappears in favor of an eager grin."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage12/leanne10_2.webm" loop
        show movie with dissolve
        window hide
        pause
        "She starts to move the dildo back and forth; her eyes glancing between it and the camera. Becoming more accustomed to the sensations, she gradually increases her speed."
        "Putting her all into her self-pleasure, she keeps her vision focused on her chat as she begins to let out a cacophony of moans."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage12/leanne10.webm" loop
        show movie with dissolve
        "Over the entire course of her masturbation session, she keeps her vision set on her screen, as if locking eyes will all of the people watching her moment of indulgence."
        stop movie
        image leanne_stage12_11 = "/leanne/events/stage12/leanne11.webp"
        scene leanne_stage12_11
        "She manages to keep her gaze on the camera until the moment she climaxes. Her eyes are forced closed as she lets out a euphoric cry."
        "When the moment passes, she takes a few seconds to sit back in her chair to wait for the lingering ecstasy to dissipate."
        image leanne_stage12_12 = "/leanne/events/stage12/leanne12.webp"
        scene leanne_stage12_12
        "When Leanne finally recovers, she shoots the chat another smile. Rolling back up to the desk, she wipes down her toy with a towel and places it in full view of her audience."
        leanne "I think that was more than enough to prove my point. At the very least, I would hope you enjoyed that session at least half as much as I did."
        leanne "As for the details of my return to streaming, I’ll be making a post on my socials in the near future. For now, this is Luxury Leanne signing off!"
        stop music fadeout 1.0
        scene player_room
        "Not long after the stream ends, you receive another message from Leanne."
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
        $ msg ("So, what did you think?", who=1)
        pause
        $ msg ("It certainly got people’s attention. Are you sure this is what you want to do?")
        pause
        $ msg ("Nope, but it feels good so I’m still going for it. That being said, I wouldn’t mind chatting about it with you over some good food. Catch you IRL sometime?", who=1)
        pause
        $ msg ("It’s a date.")
        pause
        $ msg ("I’ll hold you to that.", who=1)
        pause
        $ hide_messenger()

        $ leannestage12event = 0
        if recollection == False:
            $ daytime += 1
            $ phonecall = 1
            #Unlocks Leanne Undress in the stats page.
            $ renpy.notify("Leanne Undress option unlocked in stats screen.")
            window hide
            pause
        return

label Leanne_Stage_12_Event_2:
    if leannechoice == 1:
        #(NOTE: The following takes place when the player is in his room after Lyn’s return stream)
        #Image: Player’s room.
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Lyn', dialogue=dialogue_one)
        $ msg ("Sorry to bother you, but are you free for the meetup I asked about?", who=1)
        pause
        menu:
            "Sure, I’m free.":
                $ msg ("Sure, I’m free.")
                pause
                $ msg ("Thank you. I’ll see you at the Sugar Shop.", who=1)
                pause
                $ hide_messenger()
            "Sorry, I’m busy.":
                $ msg ("Sorry, I’m busy.")
                pause
                $ msg ("That’s okay. We can do it some other time.", who=1)
                pause
                $ hide_messenger()
                return
                #(NOTE: If the player chooses this option, Lyn will message them each following day until B) is chosen)

        image lyn_stage12_13 = "/leanne/events/stage12/lyn13.webp"
        scene lyn_stage12_13
        "Making your way over to the Sugar Shop, you find Lyn sitting at her usual table."
        "Taking the chair across from her, you still find it weird to see her without her pink hair or her usual anxiousness from the worry of being seen by her fans in public."
        image lyn_stage12_14 = "/leanne/events/stage12/lyn14.webp"
        scene lyn_stage12_14
        leanne "Thank you again for coming today. It means a lot to me."
        pc "Not a problem. What did you want to talk about?"
        leanne "I mostly wanted to thank you for encouraging me to show my audience my true self. I’ve never felt so free before."
        pc "I’ll say. Are you really sure this is how you want to go? Streaming yourself doing…that?"
        image lyn_stage12_15 = "/leanne/events/stage12/lyn15.webp"
        scene lyn_stage12_15
        leanne "Yes, but it won’t be the only thing I do. I’ll be saving streams like that for special occasions. Since my Fidget account is back, I’ll be going back to my usual gaming sessions."
        leanne "Not to mention, I have some ideas of how I want to try some different types of entertainment out."
        pc "What did you have in mind?"
        image lyn_stage12_16 = "/leanne/events/stage12/lyn16.webp"
        scene lyn_stage12_16
        "Before Lyn can answer, a server comes by to drop off a load of different sweets on the table. Thanking the server for the treats, she turns her attention back towards you."
        image lyn_stage12_17 = "/leanne/events/stage12/lyn17.webp"
        scene lyn_stage12_17
        leanne "I hope you don’t mind, but I made an order before you arrived."
        leanne "I plan to make eating sweets on stream something I do on the regular, as both a treat for myself and my viewers. As a reward for all your help, allow me to give you a private show."
        image lyn_stage12_18 = "/leanne/events/stage12/lyn18.webp"
        scene lyn_stage12_18
        "At first Lyn tries to savor each bite of the sweets to enjoy the exquisite flavor."
        image lyn_stage12_19 = "/leanne/events/stage12/lyn19.webp"
        scene lyn_stage12_19
        "After getting a sample of each of the offerings, a growl from her belly pushes her towards a more direct goal of satisfying her hunger."
        image lyn_stage12_20 = "/leanne/events/stage12/lyn20.webp"
        scene lyn_stage12_20
        "Eating much faster than the last time she treated you to a private show, she puts her enlarged belly to good use as she absolutely demolishes the treats until nothing is left."
        image lyn_stage12_21 = "/leanne/events/stage12/lyn21.webp"
        scene lyn_stage12_21
        "As the powdered sugar settles, you’re left with the sight of empty serving platters and a very stuffed Lyn."
        leanne "Sorry. I meant to leave at least some for you to try. Guess I got a little carried away."
        pc "That’s okay. The show was more than enough. You’ve really gotten good at this."
        image lyn_stage12_22 = "/leanne/events/stage12/lyn22.webp"
        scene lyn_stage12_22
        leanne "Thanks. Hopefully I can get even better with more training. Well, as long as I have someone to help me."
        "The look she gives is more than enough to clue you in to what she’s inferring."
        pc "I’d be more than happy to assist."
        image lyn_stage12_23 = "/leanne/events/stage12/lyn23.webp"
        scene lyn_stage12_23
        leanne "Thank you. I’ll send you some details later. For now, I’ll focus on my return to streaming. Oh, and don’t worry about the bill."
        leanne "The donations I got from my return stream was more than enough to pay for this indulgence ten times over."
        "Thanking Lyn for the meal and show, you part ways."
        if recollection == False:
            $ daytime += 1
            $ phonecall = 1
            $ leanne.weight += 1
        $ leannestage12event2 = 0
        return

    elif leannechoice == 2:
        #(NOTE: The following takes place when the player is in his room after Leanne’s return stream) 
        #Image: Player’s room. 
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
        $ msg ("Remember that meet up you promised? I’ve got some time if you’re available.", who=1)
        pause
        menu:
            "Sure, I’m free.":
                $ msg ("Sure, I’m free.")
                pause
                $ msg ("Nice. Let’s meet up at Bunny Bites. I’ll have something special for you.", who=1)
                pause
                $ hide_messenger()
            "Sorry, I’m busy.":
                $ msg ("Sorry, I’m busy.")
                pause
                $ msg ("That sucks. Alright, some other day then.", who=1)
                pause
                $ hide_messenger()
                return
                #(NOTE: If the player chooses this option, Lyn will message them each following day until B) is chosen)

        image leanne_stage12_13 = "/leanne/events/stage12/leanne13.webp"
        scene leanne_stage12_13
        play music "/music/bunny_bites.ogg" if_changed
        "When you arrive at Bunny Bites, it doesn’t take long to find Leanne."
        "It’s quite the sight to behold as you sit across from her, unable to take your eyes off her vibrant hair color and revealing outfit."
        "No longer wearing glasses in public lets you see that she’s very eager to meet the gaze of anyone in the restaurant that so much as glances at her revealing attire."
        image leanne_stage12_14 = "/leanne/events/stage12/leanne14.webp"
        scene leanne_stage12_14
        leanne "Glad you could make it."
        pc "Are you really okay being seen like this? You were pretty hard set on people not finding out your identity before."
        leanne "That was the old me. Luxury Leanne on the other hand is more than happy to show herself off to the public."
        leanne "At the end of the day, I’m a performer and it’s my duty to catch the attention of the masses."
        image leanne_stage12_15 = "/leanne/events/stage12/leanne15.webp"
        scene leanne_stage12_15
        leanne "This is all thanks to you. If it weren’t for your advice, I would have never been confident enough to accept who I really am."
        leanne "I’ve finally let my true self take control and I’m not going back now."
        pc "Does that include doing more streams like…that?"
        image leanne_stage12_16 = "/leanne/events/stage12/leanne16.webp"
        scene leanne_stage12_16
        leanne "Oh, has my biggest fan become obsessed with seeing just how degenerate I can be?"
        leanne "Maybe you think that by helping me out that you’ll get a private session with your favorite streamer?"
        pc "That’s not what I-"
        leanne "Hehe, just messing around with you. That being said, I do have a reward for you being such a big help. Ah, here it comes now."
        image leanne_stage12_17 = "/leanne/events/stage12/leanne17.webp"
        scene leanne_stage12_17
        "A group of waitresses descend upon our table to drop off enough food to make up a feast."
        "After the waitresses depart, a few of her fans recognize her."
        image leanne_stage12_18 = "/leanne/events/stage12/leanne18.webp"
        scene leanne_stage12_18
        "Leanne is sure to give them a few photographs of herself along with links to her various social accounts."
        image leanne_stage12_19 = "/leanne/events/stage12/leanne19.webp"
        scene leanne_stage12_19
        "When her fans leave, all that’s left is you, Leanne, and a massive amount of food."
        leanne "I hope you’re ready for some entertainment. All of this fat isn’t just to help me stand out. Luxury Leanne is ready to show you everything she’s got."
        image leanne_stage12_20 = "/leanne/events/stage12/leanne20.webp"
        scene leanne_stage12_20
        "As if being controlled by an animalistic hunger, Leanne lunges forward to attack her meal."
        image leanne_stage12_21 = "/leanne/events/stage12/leanne21.webp"
        scene leanne_stage12_21
        "The way she eats makes it clear that she’s developed quite the appetite to go alongside her added heft."
        image leanne_stage12_22 = "/leanne/events/stage12/leanne22.webp"
        scene leanne_stage12_22
        "You can only watch in amazement as she effortlessly tears through plates of food at a breakneck pace."
        "While it’s all very impressive, there’s only so far she can go before reality sets in, and she hits her limit."
        image leanne_stage12_23 = "/leanne/events/stage12/leanne23.webp"
        scene leanne_stage12_23
        leanne "Whoo. I might have BWOOOOORRRP gone a little overboard."
        pc "Are you okay?"
        image leanne_stage12_24 = "/leanne/events/stage12/leanne24.webp"
        scene leanne_stage12_24
        leanne "Yeah, I'll be fine. Just going to be a minute before I move again. This was good practice for what I have planned in the future."
        pc "What do you mean?"
        image leanne_stage12_25 = "/leanne/events/stage12/leanne25.webp"
        scene leanne_stage12_25
        "She smiles at you as she continues to rub her gut."
        leanne "Oh, you’ll see. For now I can tell you that I plan to go back to my regular streams in the near future."
        leanne "While I have you, would you mind if I call you up every now and then to help me out with some of my more “out there” ideas?"
        image leanne_stage12_26 = "/leanne/events/stage12/leanne26.webp"
        scene leanne_stage12_26
        window hide
        pause
        image leanne_stage12_27 = "/leanne/events/stage12/leanne27.webp"
        scene leanne_stage12_27
        pc "I’ll try my best."
        image leanne_stage12_25 = "/leanne/events/stage12/leanne25.webp"
        scene leanne_stage12_25
        leanne "Nice. You can go on ahead of me. I’ll take care of the bill. Until next time, this is Luxury Leanne signing off."
        "Unable to stop yourself from copying Leanne’s smile upon hearing her trademark send off, you bid her farewell before leaving the diner."
        stop music fadeout 1.0
        if recollection == False:
            $ daytime += 1
            $ phonecall = 1
            $ leanne.weight += 1
        $ leannestage12event2 = 0
        return

label Leanne_Stage_12_Event_3:
    if leannechoice == 1:
        #Scene: Lyn’s First Regular Stream Back
        #(NOTE: Occurs after the player meets up with Lyn at the Sugar Shop and chooses the option to watch her stream.)
        image Lyn_webcam_event12 = "/leanne/12/Lyn_webcam.webp"
        scene Lyn_webcam_event12
        play music "/music/leanne_stream.ogg" if_changed
        "Tuning in to Lyn's stream, you're lucky enough to catch the beginning of her return stream."
        leanne "Hello, everyone, and welcome to the stream. I know it's been a while and you have a lot of questions."
        image Lyn_side_event12 = "/leanne/12/Lyn_side.webp"
        scene Lyn_side_event12
        leanne "I’ve made a couple of posts on my socials to explain what’s been going on and what my plans for the future are."
        leanne "That being said, things will be like they were before with my regular sessions of Carl on Duty alongside some new projects I have in mind."
        "Leaning in the side of her seat, Lyn points towards where the donate pizza icon appears on the screen."
        leanne "And just like before, you can send in donations to feed me pizza and receive a little show in return."
        leanne "This is especially true for anyone that wants to do the five pizza button. With all of that out of the way,"
        image Lyn_happy_event12 = "/leanne/12/Lyn_happy.webp"
        scene Lyn_happy_event12
        leanne "let’s see if I can shake the rust off of things. I’ll be honest, it’s been a while since I last touched this game so I might be a little out of practice."
        "Should you donate?"
        #CHOICE: A) No, just watch, B) Donate a single pizza (-$5), or C) Donate five pizzas (-$25)
        menu:
            "No, just watch.":
                image Lyn_gaming_event12 = "/leanne/12/Lyn_gaming.webp"
                scene Lyn_gaming_event12
                "You watch Lyn stream for a bit."
                "Though she seems to struggle a lot more than she used to, the presence of the chat is more than enough to keep her spirits up through each loss over the course of the session."
                image Lyn_goodbye_event12 = "/leanne/12/Lyn_goodbye.webp"
                scene Lyn_goodbye_event12
                leanne "That’ll do it for me tonight. Thank you everyone for watching. See you next time!"
                "The stream ends."
                stop music fadeout 1.0
                $ leannestage12event3 = 0
                if recollection == False:
                    $ daytime += 1
                    jump freetime
                return
            "Donate a single pizza. (-$5)":
                if money <= 4:
                    "You do not have enough money to buy Lyn 5 pizzas. You can earn money by working at the diner."
                    image Lyn_gaming_event12 = "/leanne/12/Lyn_gaming.webp"
                    scene Lyn_gaming_event12
                    "You watch Lyn stream for a bit."
                    "Though she seems to struggle a lot more than she used to, the presence of the chat is more than enough to keep her spirits up through each loss over the course of the session."
                    image Lyn_goodbye_event12 = "/leanne/12/Lyn_goodbye.webp"
                    scene Lyn_goodbye_event12
                    leanne "That’ll do it for me tonight. Thank you everyone for watching. See you next time!"
                    "The stream ends."
                    stop music fadeout 1.0
                    $ leannestage12event3 = 0
                    if recollection == False:
                        $ daytime += 1
                        jump freetime
                    return
                if recollection == False:
                    $ money -= 5
                image Lyn_happy_event12 = "/leanne/12/Lyn_happy.webp"
                scene Lyn_happy_event12
                leanne "Thank you for the donation. I’ll go ahead and order the pizza right away."
                image Lyn_pizzabox_event12 = "/leanne/12/Lyn_pizzabox.webp"
                scene Lyn_pizzabox_event12
                "About ten minutes later, a pizza arrives at the door."
                image Lyn_pizza1_event12 = "/leanne/12/Lyn_pizza1.webp"
                scene Lyn_pizza1_event12
                "Bringing the box over to her desk, Lyn proceeds to devour the entire thing as if it was a small snack to her."
                image Lyn_goodbye_event12 = "/leanne/12/Lyn_goodbye.webp"
                scene Lyn_goodbye_event12
                leanne "That was a nice treat. Thank you again."
                "You watch the rest of the stream until she finishes up her gaming session and then you head to bed."
                stop music fadeout 1.0
                $ leannestage12event3 = 0
                if recollection == False:
                    $ leanne.weight += 0.5
                    $ daytime += 1
                    jump freetime
                return
            "Donate five pizzas. (-$25)":
                if money <= 24:
                    "You do not have enough money to buy Lyn 5 pizzas. You can earn money by working at the diner."
                    image Lyn_gaming_event12 = "/leanne/12/Lyn_gaming.webp"
                    scene Lyn_gaming_event12
                    "You watch Lyn stream for a bit."
                    "Though she seems to struggle a lot more than she used to, the presence of the chat is more than enough to keep her spirits up through each loss over the course of the session."
                    image Lyn_goodbye_event12 = "/leanne/12/Lyn_goodbye.webp"
                    scene Lyn_goodbye_event12
                    leanne "That’ll do it for me tonight. Thank you everyone for watching. See you next time!"
                    "The stream ends."
                    stop music fadeout 1.0
                    $ leannestage12event3 = 0
                    if recollection == False:
                        $ daytime += 1
                        jump freetime
                    return
                if recollection == False:
                    $ money -= 25
                image Lyn_happy_event12 = "/leanne/12/Lyn_happy.webp"
                scene Lyn_happy_event12
                leanne "Thank you so very much for the generous donation. While I wait for the pizzas to arrive, let me give you a little treat."
                image Lyn_standing_event12 = "/leanne/12/Lyn_standing.webp"
                scene Lyn_standing_event12
                leanne "Alright. What would you like me to do?"
                #CHOICE: A) Dance or B) Exercise
                #(NOTE: Can add more choices as the stages progress if possible to add new animations)
                menu:
                    "Dance.":
                        "Starting up a royalty free song on her speakers, Lyn begins to dance around to the rhythm of the beat."
                        $ movielength = 43
                        $ movieplaying = "/images/leanne/12/Lyn_dance.webm"
                        call screen custommoviescreen
                        window hide
                        pause
                        "Though she struggles to move with her extra weight, she still keeps up a modest smile as she finishes up her routine."

                    "Exercise.":
                        "Looking reluctant at first, Lyn eventually pushes herself to begin exercising."
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/leanne/12/Lyn_exercise.webm" loop
                        show movie with dissolve
                        window hide
                        pause
                        "Though it's clear that she's struggling through the extertion, she tries to keep up a smile for her viewers as she works through the routine."
                        stop movie

                image Lyn_towel_event12 = "/leanne/12/Lyn_towel.webp"
                scene Lyn_towel_event12
                leanne "That was a bit of a workout. Thankfully, I think the pizzas just arrived to help me refuel."
                image Lyn_pizzastack_event12 = "/leanne/12/Lyn_pizzastack.webp"
                scene Lyn_pizzastack_event12
                leanne "This all looks so good. Let me try to work through these as I play."
                image Lyn_pizza2_event12 = "/leanne/12/Lyn_pizza2.webp"
                scene Lyn_pizza2_event12
                "Though her gaming skill declines as she eats, she doesn’t seem to care."
                image Lyn_pizza3_event12 = "/leanne/12/Lyn_pizza3.webp"
                scene Lyn_pizza3_event12
                "She eagerly downs each slice like she’s on the brink of starvation. One after another the boxes are emptied out as her belly fills up with pizza."
                image Lyn_stuffed1_event12 = "/leanne/12/Lyn_stuffed1.webp"
                scene Lyn_stuffed1_event12
                "Finishing up the last slice, Lyn leans back in her seat as she absentmindedly rubs her overstuffed stomach."
                image Lyn_stuffed2_event12 = "/leanne/12/Lyn_stuffed2.webp"
                scene Lyn_stuffed2_event12
                leanne "Whoo. That really hit the spot."
                image Lyn_stuffed3_event12 = "/leanne/12/Lyn_stuffed3.webp"
                scene Lyn_stuffed3_event12
                leanne "I think that’s going to do it for me tonight. Thank you all for stopping by. See you next time!"
                stop music fadeout 1.0
                $ leannestage12event3 = 0
                if recollection == False:
                    $ leanne.weight += 1.5
                    $ daytime += 1
                    jump freetime
                return

    elif leannechoice == 2:
        #(NOTE: The following occurs after the player’s meet up with Leanne at Bunny Bites and he chooses to watch her stream).
        image Leanne_webcam_event12 = "/leanne/12/Leanne_webcam.webp"
        scene Leanne_webcam_event12
        play music "/music/leanne_stream.ogg" if_changed
        "You tune in just in time to catch Leanne's first regular stream after her hiatus."
        leanne "Hey there, everyone! This is Luxury Leanne welcoming you back for her grand re-debut."
        image Leanne_side_event12 = "/leanne/12/Leanne_side.webp"
        scene Leanne_side_event12
        leanne "If any of you are wondering where I’ve been for so long, you can just read the post on my socials."
        leanne "TLDR: I'm back and better than ever. Now, before I get back to crushing noobs in Carl on Duty..."
        "Leaning to the side, Leanne makes a big show of pointing out the pizza icon on the screen."
        leanne "The pizza button is back and better than ever. If you want a show of me stuffing my face, feel free to send in some cash."
        image Leanne_happy_event12 = "/leanne/12/Leanne_happy.webp"
        scene Leanne_happy_event12
        leanne "With that out of the way, let’s get to tonight’s main event."
        "Will you donate?"
        #CHOICE: A) No, just watch, B) Donate a single pizza (-$5), or C) Donate five pizzas (-$25)
        menu:
            "No, just watch.":
                image Leanne_gaming_event12 = "/leanne/12/Leanne_gaming.webp"
                scene Leanne_gaming_event12
                "You watch Leanne stream for a bit. Between light-hearted commentary with the chat, she absolutely destroys most of the matches she's in."
                "Her impressive display of skill is accompanied by a number of jokes and quips from her to keep her viewers entertained."
                "She manages to keep up this energy up until the very end of the stream."
                image Leanne_goodbye_event12 = "/leanne/12/Leanne_goodbye.webp"
                scene Leanne_goodbye_event12
                leanne "Think that’s going to do it for me tonight. Until next time, this is Luxury Leanne signing off!"
                "The stream ends."
                stop music fadeout 1.0
                $ leannestage12event3 = 0
                if recollection == False:
                    $ daytime += 1
                    jump freetime
                return
            "Donate a single pizza. (-$5)":
                if money <= 4:
                    "You do not have enough money to buy Leanne 5 pizzas. You can earn money by working at the diner."
                    image Leanne_gaming_event12 = "/leanne/12/Leanne_gaming.webp"
                    scene Leanne_gaming_event12
                    "You watch Leanne stream for a bit. Between light-hearted commentary with the chat, she absolutely destroys most of the matches she's in."
                    "Her impressive display of skill is accompanied by a number of jokes and quips from her to keep her viewers entertained."
                    "She manages to keep up this energy up until the very end of the stream."
                    image Leanne_goodbye_event12 = "/leanne/12/Leanne_goodbye.webp"
                    scene Leanne_goodbye_event12
                    leanne "Think that’s going to do it for me tonight. Until next time, this is Luxury Leanne signing off!"
                    "The stream ends."
                    stop music fadeout 1.0
                    $ leannestage12event3 = 0
                    if recollection == False:
                        $ daytime += 1
                        jump freetime
                    return
                if recollection == False:
                    $ money -= 5
                image Leanne_smile_event12 = "/leanne/12/Leanne_smile.webp"
                scene Leanne_smile_event12
                leanne "Thanks for the pizza. I’ll order right away."
                image Leanne_pizzabox_event12 = "/leanne/12/Leanne_pizzabox.webp"
                scene Leanne_pizzabox_event12
                "About ten minutes later, a pizza arrives at the door."
                image Leanne_pizza1_event12 = "/leanne/12/Leanne_pizza1.webp"
                scene Leanne_pizza1_event12
                "Bringing the box over to her desk, Leanne proceeds to devour the entire thing as if it was a small snack to her."
                image Leanne_goodbye_event12 = "/leanne/12/Leanne_goodbye.webp"
                scene Leanne_goodbye_event12
                leanne "There, that should keep me going. Thanks again, loyal viewer."
                "You watch the rest of the stream until she finishes up her gaming session and then you head to bed."
                stop music fadeout 1.0
                $ leannestage12event3 = 0
                if recollection == False:
                    $ leanne.weight += 0.5
                    $ daytime += 1
                    jump freetime
                return
            "Donate five pizzas. (-$25)":
                if money <= 24:
                    "You do not have enough money to buy Leanne 5 pizzas. You can earn money by working at the diner."
                    image Leanne_gaming_event12 = "/leanne/12/Leanne_gaming.webp"
                    scene Leanne_gaming_event12
                    "You watch Leanne stream for a bit. Between light-hearted commentary with the chat, she absolutely destroys most of the matches she's in."
                    "Her impressive display of skill is accompanied by a number of jokes and quips from her to keep her viewers entertained."
                    "She manages to keep up this energy up until the very end of the stream."
                    image Leanne_goodbye_event12 = "/leanne/12/Leanne_goodbye.webp"
                    scene Leanne_goodbye_event12
                    leanne "Think that’s going to do it for me tonight. Until next time, this is Luxury Leanne signing off!"
                    "The stream ends."
                    stop music fadeout 1.0
                    $ leannestage12event3 = 0
                    if recollection == False:
                        $ daytime += 1
                        jump freetime
                    return
                if recollection == False:
                    $ money -= 25
                image Leanne_smile_event12 = "/leanne/12/Leanne_smile.webp"
                scene Leanne_smile_event12
                leanne "Wow, really? That's awesome! Pizzas have been ordered. All that's left is to pass the time with a little fun."
                image Leanne_standing_event12 = "/leanne/12/Leanne_standing.webp"
                scene Leanne_standing_event12
                leanne "Okay, lucky viewer, what would you like me to do?"
                #CHOICE: A) Dance or B) Exercise
                #(NOTE: Can add more choices as the stages progress if possible to add new animations)
                menu:
                    "Dance.":
                        "Starting up a royalty free song on her speaker, Leanne begins to dance around to the rhythm of the beat."
                        $ movielength = 35
                        $ movieplaying = "/images/leanne/12/Leanne_dance.webm"
                        call screen custommoviescreen
                        window hide
                        pause
                        "Through the constant shaking of her body, she proves how comfortable she is showing off how she can swing her extra weight around."
                    "Exercise.":
                        "Though there’s a momentary look of hesitation, Leanne eventually starts her exercise routine."
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/leanne/12/Leanne_exercise.webm" loop
                        show movie with dissolve
                        "In a matter of moments sweat begins to bead down her pudgy flesh."
                        window hide
                        pause
                        "She struggles to get through the routine, but she remains motivated from the reactions she receives from the chat."
                        stop movie

                image Leanne_towel_event12 = "/leanne/12/Leanne_towel.webp"
                scene Leanne_towel_event12
                leanne "Hope you enjoyed it. I know I did. Ah, looks like the pizzas just arrived. Hang on a sec and I’ll be right back."
                image Leanne_pizzastack_event12 = "/leanne/12/Leanne_pizzastack.webp"
                scene Leanne_pizzastack_event12
                leanne "Mmmm, so good. I’ll chow down on these as I play."
                image Leanne_pizza2_event12 = "/leanne/12/Leanne_pizza2.webp"
                scene Leanne_pizza2_event12
                "Despite how focused she appears to be in absolutely destroying the greasy meal, her gaming skills remain consistently impressive."
                image Leanne_pizza3_event12 = "/leanne/12/Leanne_pizza3.webp"
                scene Leanne_pizza3_event12
                "She eagerly downs each slice like she’s on the brink of starvation. One after another the boxes are emptied out as her belly fills up with pizza."
                image Leanne_stuffed1_event12 = "/leanne/12/Leanne_stuffed1.webp"
                scene Leanne_stuffed1_event12
                "Finishing up the last slice, Leanne leans back in her seat as she absentmindedly rubs her overstuffed stomach."
                image Leanne_stuffed2_event12 = "/leanne/12/Leanne_stuffed2.webp"
                scene Leanne_stuffed2_event12
                leanne "Nothing like gaming and good UUURRP pizza to close out the night."
                image Leanne_stuffed3_event12 = "/leanne/12/Leanne_stuffed3.webp"
                scene Leanne_stuffed3_event12
                leanne "Catch you all later. This is Luxury Leanne signing off."
                "The stream ends."
                stop music fadeout 1.0
                $ leannestage12event3 = 0
                if recollection == False:
                    $ leanne.weight += 1.5
                    $ daytime += 1
                    jump freetime
                return


label Leanne_Stage_13_Event:
    if leannechoice == 1:
        #Scene: Lyn Home Date
        #(NOTE: The following should occur once the player reaches Lyn Stage 13 and he’s in his room.)
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Lyn', dialogue=dialogue_one)
        $ msg ("I managed to get my hands on another rare anime DVD. Would you like to come over and watch it with me?", who=1)
        pause
        menu:
            "Sure, sounds like fun.":
                $ msg ("Sure, sounds like fun.")
                pause
                $ msg ("See you tonight then.", who=1)
                pause
                $ hide_messenger()
            "Not right now.":
                $ msg ("Not right now.")
                pause
                $ msg ("Okay. Some other time then.", who=1)
                pause
                $ hide_messenger()
                return
                #(NOTE: If the player chooses this option, Lyn will message them each following day until B) is chosen)
        "When the appropriate time comes, you make your way over to Lyn’s house."
        image lyn_stage13_1 = "/leanne/events/stage13/Lyn1.webp"
        scene lyn_stage13_1
        "Although she greets you with open arms, it’s still strange to see her without her trademark pink hair color."
        "Regardless, you give her a hug on the way in and follow her to the bedroom."
        image lyn_stage13_2 = "/leanne/events/stage13/Lyn2.webp"
        scene lyn_stage13_2
        leanne "I hope you’re ready for some tears. Highschool Heartbreakers can be pretty stressful on a person’s emotions."
        pc "I think I can handle it. Let’s get the show rolling."
        "The boasting of your emotional fortitude lasts up until episode three."
        image lyn_stage13_3 = "/leanne/events/stage13/Lyn3.webp"
        scene lyn_stage13_3
        "As the credits roll, it takes everything in your power to hold back the tears. Turning to the side, you see that Lyn isn’t doing much better."
        pc "Are you okay?"
        image lyn_stage13_4 = "/leanne/events/stage13/Lyn4.webp"
        scene lyn_stage13_4
        leanne "Yeah, it’s just no matter how many times I watch that episode, it always gets me."
        pc "Do you want to take a break?"
        image lyn_stage13_5 = "/leanne/events/stage13/Lyn5.webp"
        scene lyn_stage13_5
        leanne "That’s probably a good idea. You sit tight here. I’ll bring over some snacks."
        image lyn_stage13_6 = "/leanne/events/stage13/Lyn6.webp"
        scene lyn_stage13_6
        "You manage to wipe the tears from your eyes just in time to see Lyn return with a platter full of sweets."
        pc "That’s quite a lot of treats."
        image lyn_stage13_7 = "/leanne/events/stage13/Lyn7.webp"
        scene lyn_stage13_7
        leanne "Really? To be honest this has just been part of my daily snacking portions. It helps me maintain my preferred size."
        pc "If you don’t mind me asking, is this really what you want?"
        image lyn_stage13_8 = "/leanne/events/stage13/Lyn8.webp"
        scene lyn_stage13_8
        leanne "What do you mean?"
        pc "I know you’ve told me this before, but I want to make sure you’re still certain."
        pc "Are you okay stuffing yourself like this? Do you really want to be at this size?"
        image lyn_stage13_9 = "/leanne/events/stage13/Lyn9.webp"
        scene lyn_stage13_9
        "Lyn thinks for a few moments in silence, making you think that you might have gone too far."
        image lyn_stage13_10 = "/leanne/events/stage13/Lyn10.webp"
        scene lyn_stage13_10
        leanne "Well, I'm not the only one who appreciates my larger body."
        leanne "I’ve gotten multiple viewers messaging me saying how inspiring it is to have a heavier woman be a popular streamer."
        image lyn_stage13_11 = "/leanne/events/stage13/Lyn11.webp"
        scene lyn_stage13_11
        leanne "Not to mention, I kind of like the extra padding."
        leanne "It feels like I always have a collection of plush toys on hand to squeeze whenever I’m feeling nervous or just want to touch something soft."
        image lyn_stage13_12 = "/leanne/events/stage13/Lyn12.webp"
        scene lyn_stage13_12
        leanne "That probably sounds weird, doesn’t it?"
        pc "No. I kind of get what you mean."
        image lyn_stage13_13 = "/leanne/events/stage13/Lyn13.webp"
        scene lyn_stage13_13
        leanne "Then, would you mind helping me? I want to keep gaining, but I always fall a little short of the mark. Do you think you could feed me?"
        pc "It would be my pleasure."
        image lyn_stage13_14 = "/leanne/events/stage13/Lyn14.webp"
        scene lyn_stage13_14
        "Taking the platter from Lyn, you pick out a few sweets."
        image lyn_stage13_15 = "/leanne/events/stage13/Lyn15.webp"
        scene lyn_stage13_15
        "The start of the session goes well enough, with her graciously accepting anything brought to her face. You make good progress, but eventually run into a hurdle."
        image lyn_stage13_16 = "/leanne/events/stage13/Lyn16.webp"
        scene lyn_stage13_16
        "Halfway through the platter, you notice that she begins to slow down."
        image lyn_stage13_17 = "/leanne/events/stage13/Lyn17.webp"
        scene lyn_stage13_17
        "Though there are still pleased hums that come from her mouth as she eats each pastry, you can tell that she’s gradually becoming slower."
        image lyn_stage13_18 = "/leanne/events/stage13/Lyn18.webp"
        scene lyn_stage13_18
        "Nonetheless, you continue to feed her until the entire platter is emptied out."
        image lyn_stage13_19 = "/leanne/events/stage13/Lyn19.webp"
        scene lyn_stage13_19
        "Though it takes quite a bit of convincing, Lyn finally manages to swallow the last crumb."
        pc "You did a great job."
        image lyn_stage13_20 = "/leanne/events/stage13/Lyn20.webp"
        scene lyn_stage13_20 with vpunch
        leanne "Thank BWOOOORRRPPP you."
        image lyn_stage13_21 = "/leanne/events/stage13/Lyn21.webp"
        scene lyn_stage13_21
        leanne "Oh, excuse me. I think that was a little too much for me."
        pc "That’s okay. You just sit there and relax. I’ll handle the cleanup."
        image lyn_stage13_22 = "/leanne/events/stage13/Lyn22.webp"
        scene lyn_stage13_22
        leanne "Thank you. You’re the best."
        image lyn_stage13_23 = "/leanne/events/stage13/Lyn23.webp"
        scene lyn_stage13_23
        "You leave after picking up the remnants of Lyn’s stuffing session."
        if recollection == False:
            $ daytime += 1
            $ phonecall = 1
            $ leanne.weight += 1.5
        $ leannestage13event = 0
        return
    elif leannechoice == 2:
        #Scene: Leanne Home Date
        #(NOTE: The following occurs once the player reaches Leanne Stage 13 and he’s in his room.)
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
        $ msg ("Hey there! Remember back when we first met and I completely destroyed you in Carl on Duty? You up for a rematch at my place?", who=1)
        pause
        menu:
            "Sure, sounds like fun.":
                $ msg ("Sure, sounds like fun.")
                pause
                $ msg ("See you tonight then.", who=1)
                pause
                $ hide_messenger()
            "Not right now.":
                $ msg ("Not right now.")
                pause
                $ msg ("Alright. I’ll hit you up some other time.", who=1)
                pause
                $ hide_messenger()
                return
                #(NOTE: If the player chooses this option, Lyn will message them each following day until B) is chosen)
        "When the appropriate time comes, you head to Leanne’s house."
        image leanne_stage13_1 = "/leanne/events/stage13/Leanne1.webp"
        scene leanne_stage13_1
        "Although she greets you with open arms, you still find it strange to see her wearing her streaming outfit while the camera is off."
        "Regardless, you give her a hug on the way in and follow her to the bedroom."
        image leanne_stage13_2 = "/leanne/events/stage13/Leanne2.webp"
        scene leanne_stage13_2
        leanne "I hope you’ve been practicing. Don’t want you giving the excuse that you’re rusty when I win."
        pc "I could say the same for you. Let’s see what you got."
        image leanne_stage13_3 = "/leanne/events/stage13/Leanne3.webp"
        scene leanne_stage13_3
        "Your boast of skill doesn’t last very long. Match after match Leanne absolutely dominates."
        "No matter what tactic you use, she seems to always have a way to counterattack."
        pc "Can’t believe I forgot that you do this pretty much every night."
        image leanne_stage13_4 = "/leanne/events/stage13/Leanne4.webp"
        scene leanne_stage13_4
        leanne "Got to make sure I keep myself practiced for my viewers. So, you up for one more?"
        pc "Is it alright if I take a break? I think I’m a little tired of you beating me."
        image leanne_stage13_5 = "/leanne/events/stage13/Leanne5.webp"
        scene leanne_stage13_5
        leanne "Aww, you’re no fun. Alright, we’ll stop for now. I could use some snacks. Sit tight here."
        image leanne_stage13_6 = "/leanne/events/stage13/Leanne6.webp"
        scene leanne_stage13_6
        "You manage to get rid of the soreness in your wrists by the time Leanne returns with a table full of fast food."
        pc "That’s quite a lot."
        image leanne_stage13_7 = "/leanne/events/stage13/Leanne7.webp"
        scene leanne_stage13_7
        leanne "Eh, this is nothing. All part of my routine of maintaining my body."
        pc "If you don’t mind me asking, is this really what you want?"
        image leanne_stage13_8 = "/leanne/events/stage13/Leanne8.webp"
        scene leanne_stage13_8
        leanne "What do you mean?"
        pc "I know you told me this before, but I want to make sure you’re still certain."
        pc "Are you okay stuffing yourself like this? Do you really want to live larger than life in both size and personality?"
        image leanne_stage13_9 = "/leanne/events/stage13/Leanne9.webp"
        scene leanne_stage13_9
        "Leanne thinks for a few moments in silence, making you think that you might have gone too far."
        image leanne_stage13_10 = "/leanne/events/stage13/Leanne10.webp"
        scene leanne_stage13_10
        leanne "I won’t deny that my pudgy tummy makes it hard to find outfits that fit me and adheres to Fidget’s TOS."
        leanne "That being said, I think it more than makes up for it by helping me stand out from other streamers."
        image leanne_stage13_11 = "/leanne/events/stage13/Leanne11.webp"
        scene leanne_stage13_11
        leanne "Besides, it feels really good being Luxury Leanne. During my off time, I had plenty of opportunities to explore the special features of carrying around so much extra weight."
        leanne "The added flab really makes certain activities more enjoyable. Know what I mean?"
        pc "I think so."
        image leanne_stage13_12 = "/leanne/events/stage13/Leanne12.webp"
        scene leanne_stage13_12
        leanne "I knew I could count on you. Anyway, mind helping me shove these down my throat?"
        leanne "Figured it would make for a good reward for my recent wins. That is unless you want to try beating me again."
        pc "No, I accept defeat. To the victor goes the spoils."
        leanne "That’s the spirit. Now get to work. I’ve got quite the appetite after that gaming session."
        image leanne_stage13_13 = "/leanne/events/stage13/Leanne13.webp"
        scene leanne_stage13_13
        "Taking the food from Leanne, you start to lift the burgers to her mouth. She uses this opportunity to show off how hungry she is as she tears through the greasy meat."
        image leanne_stage13_14 = "/leanne/events/stage13/Leanne14.webp"
        scene leanne_stage13_14
        "Though her pace is fast, you’re still a bit cautious to not overdo it. Leanne is quick to let you know that’s not the kind of service she’s looking for."
        image leanne_stage13_15 = "/leanne/events/stage13/Leanne15.webp"
        scene leanne_stage13_15
        "Slowing down for just a second earns you a series of muffled protests from Leanne."
        image leanne_stage13_16 = "/leanne/events/stage13/Leanne16.webp"
        scene leanne_stage13_16
        "Following her orders, you attempt to keep pace with her hunger as she uses her free hands to grope her stomach."
        "Through her constant orders to keep feeding her, she somehow manages to work through all the food."
        image leanne_stage13_17 = "/leanne/events/stage13/Leanne17.webp"
        scene leanne_stage13_17
        "Just as your stamina is about to go out, Leanne manages to swallow up the last bite of meat."
        image leanne_stage13_18 = "/leanne/events/stage13/Leanne18.webp"
        scene leanne_stage13_18
        pc "That was impressive."
        image leanne_stage13_19 = "/leanne/events/stage13/Leanne19.webp"
        scene leanne_stage13_19 with vpunch
        leanne "Thank BWOOOORRRPPP you."
        image leanne_stage13_20 = "/leanne/events/stage13/Leanne20.webp"
        scene leanne_stage13_20
        leanne "I’ve had a lot of practice. Mind picking up? I’m a little indisposed right now."
        pc "You got it."
        image leanne_stage13_21 = "/leanne/events/stage13/Leanne21.webp"
        scene leanne_stage13_21
        leanne "And that’s why you’re my number one fan."
        image leanne_stage13_22 = "/leanne/events/stage13/Leanne22.webp"
        scene leanne_stage13_22
        "After picking up the remnants of Leanne’s stuffing session, you say goodbye and leave."
        if recollection == False:
            $ daytime += 1
            $ phonecall = 1
            $ leanne.weight += 1.5
        $ leannestage13event = 0
        return

label Leanne_Stage_13_Event_2:
    if leannechoice == 1:
        #Scene: Lyn Bedroom Tour
        #(NOTE: The following should occur after the player reaches Lyn stage 13 and decides to watch a livestream)
        image lyn_stage13_24 = "/leanne/events/stage13/Lyn24.webp"
        scene lyn_stage13_24
        play music "/music/leanne_stream2.ogg" if_changed
        "You tune into the stream to see that she's broadcasting from a different room."
        "While the view is new to the chat, it's something you've seen more than a few times during visits to her house."
        leanne "Hello everyone and welcome to the stream. As you can probably see, I'm in a different location that my usual broadcasts."
        image lyn_stage13_25 = "/leanne/events/stage13/Lyn25.webp"
        scene lyn_stage13_25
        "Moving around, Lyn shows off her room from different angles with a camera on her a selfie stick."
        image lyn_stage13_26 = "/leanne/events/stage13/Lyn26.webp"
        scene lyn_stage13_26
        leanne "Thanks to all of your support, I managed to make enough money to afford another streaming set up for my bedroom."
        image lyn_stage13_27 = "/leanne/events/stage13/Lyn27.webp"
        scene lyn_stage13_27
        window hide
        pause
        image lyn_stage13_28 = "/leanne/events/stage13/Lyn28.webp"
        scene lyn_stage13_28
        leanne "I'll still be using my office from time to time, but I'll swap between here and there on occasion to keep things interesting."
        image lyn_stage13_29 = "/leanne/events/stage13/Lyn29.webp"
        scene lyn_stage13_29
        leanne "I hope you enjoyed the short tour of my room. Now let's get on with the stream."
        image lyn_stage13_30 = "/leanne/events/stage13/Lyn30.webp"
        scene lyn_stage13_30
        "Lyn's regular streaming show goes as planned, save for different people chiming in to ask various questions about everything in her room."
        "You watch all the way to the end and then go to sleep."
        $ leannestage13event2 = 0
        return
    elif leannechoice == 2:
        #Scene: Leanne Bedroom Tour
        #(NOTE: The following should occur after the player reaches Leanne stage 13 and decides to watch a livestream)
        image leanne_stage13_23 = "/leanne/events/stage13/Leanne23.webp"
        scene leanne_stage13_23
        play music "/music/leanne_stream2.ogg" if_changed
        "You tune into the stream to see that Leanne is broadcasting from her bedroom."
        "While the view is new to the chat, it's something you've seen more than a few times during visits to her house."
        leanne "Hey everyone! Luxury Leanne here coming at you live from the scenic vista of my bedroom."
        image leanne_stage13_24 = "/leanne/events/stage13/Leanne24.webp"
        scene leanne_stage13_24
        "Moving around, Leanne shows off her room from different angles with a camera on her a selfie stick."
        image leanne_stage13_25 = "/leanne/events/stage13/Leanne25.webp"
        scene leanne_stage13_25
        leanne "In return for all of your support and donations, I thought I'd splurge a little and get a new setup for my bedroom."
        image leanne_stage13_26 = "/leanne/events/stage13/Leanne26.webp"
        scene leanne_stage13_26
        window hide
        pause
        image leanne_stage13_27 = "/leanne/events/stage13/Leanne27.webp"
        scene leanne_stage13_27
        leanne "I'll still use my office, but this place should make certain “special” streams a lot more interesting."
        image leanne_stage13_28 = "/leanne/events/stage13/Leanne28.webp"
        scene leanne_stage13_28
        leanne "But that's all for another time. For now, let's get to the game."
        image leanne_stage13_29 = "/leanne/events/stage13/Leanne29.webp"
        scene leanne_stage13_29
        "Leanne's regular stream goes as planned, save for different viewers chiming in to ask various questions about everything in her room."
        "You watch all the way to the end and then go to sleep."
        $ leannestage13event2 = 0
        return

label Leanne_Stage_13_Event_3:
    if leannechoice == 1:
        #Lyn Stage 13 Event 3
        #Scene: Lyn’s First Feeding Stream
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
        $ msg ("I have a special stream I want to do, but I’m going to need some help. Are you free this evening?", who=1)
        pause
        menu:
            "I'm free. What do I need to do?":
                $ msg ("I'm free. What do I need to do?")
                pause
                $ msg ("Thank you. Just meet me at my place this evening. I'll explain everything when you get here.", who=1)
                pause
                $ hide_messenger()
            "Sorry, I'm busy":
                $ msg ("Sorry, I'm busy")
                pause
                $ msg ("Okay. I'll try some other time then.", who=1)
                pause
                $ hide_messenger()
                return
                #(NOTE: If the player chooses this option, Lyn will message them each following day until B) is chosen)

        image lyn_stage13_31 = "/leanne/events/stage13/Lyn31.webp"
        scene lyn_stage13_31
        "Upon arriving at Lyn's house, You greet her with open arms." 
        image lyn_stage13_32 = "/leanne/events/stage13/Lyn32.webp"
        scene lyn_stage13_32
        "While she reciprocates the hug, it's clear by the look on her face that something is bothering her."
        pc "Is everything okay?"
        image lyn_stage13_33 = "/leanne/events/stage13/Lyn33.webp"
        scene lyn_stage13_33
        leanne "Yeah. I'm just a little nervous about tonight. It's the first time I'm doing a stream like this."
        pc "What did you have in mind?"
        image lyn_stage13_34 = "/leanne/events/stage13/Lyn34.webp"
        scene lyn_stage13_34
        "After a few moments of silence to collect her thoughts, Lyn leans in to tell me her plan." 
        "At first you are a little shocked at her request." 
        image lyn_stage13_35 = "/leanne/events/stage13/Lyn35.webp"
        scene lyn_stage13_35
        "However, You can tell that despite her fears that she still wants to go through with it." 
        "Upon hearing exactly what she wants me to do, You give your answer."
        pc "Alright, I'm in."
        image lyn_stage13_36 = "/leanne/events/stage13/Lyn36.webp"
        scene lyn_stage13_36
        leanne "Thank you so much for understanding. I'll be starting up the stream shortly so just stay comfortable for a bit while I get everything set up."
        image lyn_stage13_37 = "/leanne/events/stage13/Lyn37.webp"
        scene lyn_stage13_37
        "You patiently sit as Lyn gets everything ready for the stream." 
        "You're a little fascinated by the inner workings of her stream, but only as far as you can understand." 
        "Once the cameras and supplies are in place, all that's left is for Lyn to get herself ready."
        image lyn_stage13_38 = "/leanne/events/stage13/Lyn38.webp"
        scene lyn_stage13_38
        "After slipping into a set of pink undergarments, Lyn steps back into the room and stands in front of you."
        image lyn_stage13_39 = "/leanne/events/stage13/Lyn39.webp"
        scene lyn_stage13_39
        leanne "How do I look?"
        pc "Really cute."
        image lyn_stage13_40 = "/leanne/events/stage13/Lyn40.webp"
        scene lyn_stage13_40
        leanne "Thank you. I know I've shown a lot more on camera before, but this kind of feels even more revealing. Does that make sense?"
        pc "I'm sure that'll clear up once we get started. Are you ready?"
        image lyn_stage13_41 = "/leanne/events/stage13/Lyn41.webp"
        scene lyn_stage13_41
        "Taking a deep breath, Lyn nods her head."
        leanne "I think so. Let's do this."
        image lyn_stage13_42 = "/leanne/events/stage13/Lyn42.webp"
        scene lyn_stage13_42
        "Taking her usual spot, Lyn starts up a stream and begins to broadcast on Eroticabase."
        leanne "Hello everyone. Thank you for joining today's special stream." 
        leanne "Before we begin I would like to introduce you to my helper for the day: [playername]."
        image lyn_stage13_43 = "/leanne/events/stage13/Lyn43.webp"
        scene lyn_stage13_43
        "Upon hearing your cue, you lean into view and wave towards the screen."
        leanne "Please treat him well throughout the stream. I'm certainly going to need him to help me with this."
        image lyn_stage13_44 = "/leanne/events/stage13/Lyn44.webp"
        scene lyn_stage13_44
        "Reaching offscreen, Lyn grabs a platter of sweets and holds it up so the viewers can see."
        leanne "Tonight, I'm going to be doing a stuffing stream. [playername] is going to assist me to make sure I swallow every last bite. Are you ready?"
        pc "Whenever you are."
        leanne "Then let's begin."
        image lyn_stage13_45 = "/leanne/events/stage13/Lyn45.webp"
        scene lyn_stage13_45
        "Making sure the camera has a good view, you begin to hand feed the sweets to Lyn." 
        "Though she's a little nervous at first, her shivers dissipate after she sinks her teeth into the first cupcake." 
        image lyn_stage13_46 = "/leanne/events/stage13/Lyn46.webp"
        scene lyn_stage13_46
        "You continue to feed her from the platter, always waiting for her to finish chewing before bringing another one up to her lips." 
        "The gradual pace helps her through the sugary feast and gives the viewers plenty of time to admire her body."
        image lyn_stage13_47 = "/leanne/events/stage13/Lyn47.webp"
        scene lyn_stage13_47
        "As we get closer and closer to the end, Lyn begins to rub her belly to deal with her filling gut." 
        "You deliberately slow your pace to not overwhelm her, but you manage to gradually work through the collection."
        image lyn_stage13_48 = "/leanne/events/stage13/Lyn48.webp"
        scene lyn_stage13_48
        "Though she struggles, she's given a morale boost via words of encouragement from both you and the chat." 
        "Pushing herself to the very limit, she manages to make it through the entire feast."
        image lyn_stage13_49 = "/leanne/events/stage13/Lyn49.webp"
        scene lyn_stage13_49
        "Upon finishing off the last bite and cleaning the icing from her lips, Lyn carefully pushes her belly up against her desk and looks into the camera."
        image lyn_stage13_50 = "/leanne/events/stage13/Lyn50.webp"
        scene lyn_stage13_50
        leanne "I hope you all enjoyed the show. It was really fun getting to eat so many sweets." 
        image lyn_stage13_51 = "/leanne/events/stage13/Lyn51.webp"
        scene lyn_stage13_51
        leanne "I'll have to try this again sometime. For now though, I think I'm going to sign off to deal with the side effects. Thank you everyone for tuning in."

        image lyn_stage13_52 = "/leanne/events/stage13/Lyn52.webp"
        scene lyn_stage13_52
        "Ending the stream, Lyn turns around to look at you."
        pc "You did an excellent job. It was really impressive how you were able to eat all of that."
        image lyn_stage13_53 = "/leanne/events/stage13/Lyn53.webp"
        scene lyn_stage13_53
        leanne "I only managed to do it because you were here."
        pc "I was more than happy to help."
        leanne "If that's the case…would you mind helping me with something else?"
        image lyn_stage13_54 = "/leanne/events/stage13/Lyn54.webp"
        scene lyn_stage13_54
        "As you ponder what she means, you give a hard, long look at the sheepish expression on her face." 
        "Looking at the way her body trembles as she continues to massage her belly, you can take a wild guess to figure out what she wants."
        pc "Are you sure you want to go through with this?"
        image lyn_stage13_55 = "/leanne/events/stage13/Lyn55.webp"
        scene lyn_stage13_55
        leanne "Yes, I am."
        "Hearing the conviction behind her voice, you approach her and remove your clothes." 
        image lyn_stage13_56 = "/leanne/events/stage13/Lyn56.webp"
        scene lyn_stage13_56
        "As Lyn takes off her clothes, you have a momentary discussion on how to move forward."
        image lyn_stage13_57 = "/leanne/events/stage13/Lyn57.webp"
        scene lyn_stage13_57
        "Deciding that she's in no condition to make any movements on her own, You volunteer to take the lead."
        image lyn_stage13_58 = "/leanne/events/stage13/Lyn58.webp"
        scene lyn_stage13_58
        "Moving over to the couch, she bends over, ready for you to pump into her plump behind."
        image lyn_stage13_59 = "/leanne/events/stage13/Lyn59.webp"
        scene lyn_stage13_59
        "With everything in place, you admire her fat bloated body for a bit before moving behind her."
        image lyn_stage13_60 = "/leanne/events/stage13/Lyn60.webp"
        scene lyn_stage13_60
        window hide
        pause
        image lyn_stage13_61 = "/leanne/events/stage13/Lyn61.webp"
        scene lyn_stage13_61
        "Grabbing hold of Lyn's belly, you guide your cock into her waiting pussy."
        image lyn_stage13_sex_start = "/leanne/events/stage13/Lyn_sex_start.webp"
        scene lyn_stage13_sex_start
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage13/Lyn_sex_1.webm" loop
        show movie with dissolve
        "Getting a good grip on her hips, you proceed to thrust in and out of her."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage13/Lyn_sex_2.webm" loop
        show movie with dissolve
        "Her sweaty fat body grinding against your waist captures you in a lusty trance."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage13/Lyn_sex_3.webm" loop
        "Her bloated soft belly and breasts jiggling and swinging with every thrust."
        show movie with dissolve
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage13/Lyn_sex_4.webm" loop
        "Her breathing becoming heavier, her moans becoming more audible."
        show movie with dissolve
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage13/Lyn_sex_5.webm" loop
        show movie with dissolve
        "As you become more accustomed to each other, you decide to speed up your thrusts."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage13/Lyn_sex_6.webm" loop
        show movie with dissolve
        "While thrusting, you feel Lyn reaching her limits, her moans becoming more frequent and louder."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage13/Lyn_sex_7.webm" loop
        show movie with dissolve
        "Her body twitching and jiggling more and more."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage13/Lyn_sex_8.webm" loop
        show movie with dissolve
        "Her climaxing, twitching body also brings you to your point of explosive relief."
        window hide
        pause
        stop movie
        image lyn_stage13_62 = "/leanne/events/stage13/Lyn62.webp"
        scene lyn_stage13_62
        "Just before you orgasm, you pull out to cum all over her big behind."
        image lyn_stage13_63 = "/leanne/events/stage13/Lyn63.webp"
        scene lyn_stage13_63
        "Coming down from her orgasm, Lyn turns around."
        leanne "That was…amazing. Are you feeling alright?"
        pc "Honestly a little sore, but I think it was more than worth it."
        image lyn_stage13_64 = "/leanne/events/stage13/Lyn64.webp"
        scene lyn_stage13_64
        leanne "I'm glad to hear that. Give me a few seconds to catch my breath and I'll help you clean up."
        pc "Take your time. I'm in no rush."
        "Waiting for your bodies to recover, you gradually clean up the mess and put your clothes back on."
        image lyn_stage13_65 = "/leanne/events/stage13/Lyn65.webp"
        scene lyn_stage13_65
        "Finished with the cleanup, you give Lyn a small kiss to the cheek to say goodbye before you take my leave." 
        $ leannestage13event3 = 0
        if recollection == False:
            $ daytime += 1
            $ phonecall = 1
            $ leanne.weight += 1
        return

    elif leannechoice == 2:
        #Leanne Stage 13 Event 3
        #Scene: Leanne’s First Feeding Stream
        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Leanne', dialogue=dialogue_one)
        $ msg ("I've got a special stream in mind, but I'm going to need some help. You available tonight?", who=1)
        pause
        menu:
            "I'm free. What do I need to do?":
                $ msg ("I'm free. What do I need to do?")
                pause
                $ msg ("Just come over to my place. I'll have everything we need.", who=1)
                pause
                $ hide_messenger()
            "Sorry, I'm busy":
                $ msg ("Sorry, I'm busy")
                pause
                $ msg ("Shoot. Okay, some other time then.", who=1)
                pause
                $ hide_messenger()
                return
                #(NOTE: If the player chooses this option, Lyn will message them each following day until B) is chosen)

        image leanne_stage13_30 = "/leanne/events/stage13/Leanne30.webp"
        scene leanne_stage13_30
        "Upon arriving at Leanne's house, you go to greet her with open arms."
        image leanne_stage13_31 = "/leanne/events/stage13/Leanne31.webp"
        scene leanne_stage13_31
        "While she reciprocates the hug, it's clear that she's up to something."
        image leanne_stage13_32 = "/leanne/events/stage13/Leanne32.webp"
        scene leanne_stage13_32
        pc "Is everything okay?"
        leanne "Oh, everything is just fine. I'm just a little excited about tonight. Should be a real showstopper."
        pc "What did you have in mind?"
        image leanne_stage13_33 = "/leanne/events/stage13/Leanne33.webp"
        scene leanne_stage13_33
        "After a few moments of silence to make your mind wonder, Leanne leans in to tell you her plan." 
        "At first you were a little shocked at what she tells you. However, the outlandish request isn't something you can't do." 
        "Not to mention, you are more than a little curious to try it out. A little nervous about the finer details, you regardless nod your head in agreement."
        pc "Alright, I'm in."
        image leanne_stage13_34 = "/leanne/events/stage13/Leanne34.webp"
        scene leanne_stage13_34
        leanne "I knew I could count on you. I'll be starting up the stream shortly. Sit tight while I get everything ready."
        image leanne_stage13_35 = "/leanne/events/stage13/Leanne35.webp"
        scene leanne_stage13_35
        "You patiently sit as Leanne sets up the stream." 
        "You're a little fascinated by the inner workings of her equipment, but only as far as you can understand." 
        "Once the cameras and supplies are in place, all that's left is for Leanne to get herself ready."
        image leanne_stage13_36 = "/leanne/events/stage13/Leanne36.webp"
        scene leanne_stage13_36
        "Leanne steps back into the room wearing a very revealing cow bikini and cow ears."
        image leanne_stage13_37 = "/leanne/events/stage13/Leanne37.webp"
        scene leanne_stage13_37
        leanne "How do I look?"
        pc "Incredibly sexy."
        image leanne_stage13_38 = "/leanne/events/stage13/Leanne38.webp"
        scene leanne_stage13_38
        leanne "Thank you, thank you. It's taken a lot of training and binge eating to look this good." 
        leanne "Hopefully my viewers will be just as entranced as you are. You ready?"
        "You pause and take a deep breath."
        pc "As I'll ever be."
        image leanne_stage13_39 = "/leanne/events/stage13/Leanne39.webp"
        scene leanne_stage13_39
        leanne "Good. Now just relax and remember the plan. This is going to be awesome."
        image leanne_stage13_40 = "/leanne/events/stage13/Leanne40.webp"
        scene leanne_stage13_40
        "Taking her usual spot, Leanne turns on her pink lights and starts up the stream to broadcast on Eroticabase."
        leanne "Hello viewers. This is Luxury Leanne coming at you live with an extra special stream." 
        leanne "Before we begin I would like to introduce you to my little helper for today: [playername]."
        image leanne_stage13_41 = "/leanne/events/stage13/Leanne41.webp"
        scene leanne_stage13_41
        "Upon hearing my cue, You lean into view and wave towards the screen."
        image leanne_stage13_42 = "/leanne/events/stage13/Leanne42.webp"
        scene leanne_stage13_42
        leanne "He's been ordered to help me out with today's stream in return for getting to spend the evening with his favorite streamer." 
        leanne "Now as for tonight's show…"
        image leanne_stage13_43 = "/leanne/events/stage13/Leanne43.webp"
        scene leanne_stage13_43
        "Reaching offscreen, Leanne grabs the feeding tube and one of the many tubs of ice cream she had bought for the occasion."
        leanne "That's right, tonight is going to be the much requested stuffing stream."
        image leanne_stage13_44 = "/leanne/events/stage13/Leanne44.webp"
        scene leanne_stage13_44
        leanne "[playername], you ready?"
        pc "Yes, ma'm."
        leanne "Then let's get started!"
        image leanne_stage13_45 = "/leanne/events/stage13/Leanne45.webp"
        scene leanne_stage13_45
        "Making sure the camera has a good view, Leanne pops the tube into her mouth and signals for you to begin." 
        "At first you try to take things slow, letting the ice cream chug down the hose at a gradual pace."
        image leanne_stage13_46 = "/leanne/events/stage13/Leanne46.webp"
        scene leanne_stage13_46
        "Leanne effortlessly slurps up the sweet slurry, managing to get through the first tub in record time."
        image leanne_stage13_47 = "/leanne/events/stage13/Leanne47.webp"
        scene leanne_stage13_47
        "Though your intention is to keep going slow, it's clear that Leanne has other plans."
        image leanne_stage13_48 = "/leanne/events/stage13/Leanne48.webp"
        scene leanne_stage13_48
        "With a snap of her fingers, Leanne pushes you to up your speed." 
        image leanne_stage13_49 = "/leanne/events/stage13/Leanne49.webp"
        scene leanne_stage13_49
        "Daring to slow down for even a second leads her to slap her belly to try and hurry you up."
        image leanne_stage13_50 = "/leanne/events/stage13/Leanne50.webp"
        scene leanne_stage13_50
        "Though it's a bit of a struggle, the chat is happy to chime in with morale boosts for both Leanne and youself." 
        image leanne_stage13_51 = "/leanne/events/stage13/Leanne51.webp"
        scene leanne_stage13_51
        "Being able to keep up with her pace, you end up pouring down two tubs of ice cream down the tube at once."
        image leanne_stage13_52 = "/leanne/events/stage13/Leanne52.webp"
        scene leanne_stage13_52
        "You're left amazed as she chugs down the entire downpour of sweetness, letting out pleased hums as her fingers rub her overstuffed belly."
        image leanne_stage13_53 = "/leanne/events/stage13/Leanne53.webp"
        scene leanne_stage13_53
        "Upon emptying out the last drop of ice cream from the hose, Leanne dismisses you with a wave of her hand."
        image leanne_stage13_54 = "/leanne/events/stage13/Leanne54.webp"
        scene leanne_stage13_54
        "Pulling the tube out of her mouth and handing it over to you, she scoots herself back to her desk and looks into the camera."
        image leanne_stage13_55 = "/leanne/events/stage13/Leanne55.webp"
        scene leanne_stage13_55 with vpunch
        leanne "I hope you're all BWOOOOOORRRP enjoying the show." 
        image leanne_stage13_56 = "/leanne/events/stage13/Leanne56.webp"
        scene leanne_stage13_56
        leanne "Always fun to really pig out in front of so many loyal fans. I'll have to do this again some time."
        image leanne_stage13_57 = "/leanne/events/stage13/Leanne57.webp"
        scene leanne_stage13_57
        "Keeping one eye on the chat, Leanne turns herself around to stare at me."
        leanne "That being said, the show isn't over yet."
        image leanne_stage13_58 = "/leanne/events/stage13/Leanne58.webp"
        scene leanne_stage13_58
        leanne "[playername], come here. I think it's time I get a reward for all of my hard work." 
        "Even knowing what she has in mind, it still takes a moment for what she says to register in your head." 
        "Remembering the part you have to play, you take off all your clothes and approach her." 
        image leanne_stage13_59 = "/leanne/events/stage13/Leanne59.webp"
        scene leanne_stage13_59
        "Getting up from her seat, Leanne grabs my hand to put me in her place." 
        image leanne_stage13_60 = "/leanne/events/stage13/Leanne60.webp"
        scene leanne_stage13_60
        "I'm only given a few moments to stare at the over excited chat before my view of the screen is blocked by her chubby rear." 
        image leanne_stage13_61 = "/leanne/events/stage13/Leanne61.webp"
        scene leanne_stage13_61
        "With barely a warning, she brings her body down to sit on my lap." 
        "Letting out a gasp from the sudden impact, I endure her weight as she gets into position."
        image leanne_stage13_62 = "/leanne/events/stage13/Leanne62.webp"
        scene leanne_stage13_62
        leanne "Hope you're ready. I have a lot of sugar to burn off."
        image leanne_stage13_sex_start = "/leanne/events/stage13/Leanne_sex_start.webp"
        scene leanne_stage13_sex_start
        "Upon hearing your go ahead to continue, Leanne plunges your dick into her womanhood."
        $ renpy.movie_cutscene("/images/leanne/events/stage13/Leanne_sex_1.webm", stop_music=False)
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/leanne/events/stage13/Leanne_sex_2.webm" loop
        show movie with dissolve
        "The pleasure you feel from the mere act of insertion is multiplied tenfold as she begins to grind against you." 
        "Riding your cock with rapid movements sends ripples through her pudgy body, much to the delight of her viewers." 
        "Perhaps getting a little too obsessed with putting on a show and reaching her climax, she shows no restraint as she continues to push down on you." 
        "Unable to fully deal with the surge of stimulations you end up cumming first. Thankfully, she follows only a few moments later."
        window hide
        pause
        stop movie
        image leanne_stage13_63 = "/leanne/events/stage13/Leanne63.webp"
        scene leanne_stage13_63
        "Coming down from her climax, Leanne leans back and buries you in her back flab." 
        image leanne_stage13_64 = "/leanne/events/stage13/Leanne64.webp"
        scene leanne_stage13_64
        "Feeling you struggle underneath, she relents in standing up to avoid smothering you any further."
        leanne "Whoo, I hope you all enjoyed that. I know I certainly did." 
        image leanne_stage13_65 = "/leanne/events/stage13/Leanne65.webp"
        scene leanne_stage13_65
        leanne "That will do it for tonight's show. This is Luxury Leanne, signing off!"
        image leanne_stage13_66 = "/leanne/events/stage13/Leanne66.webp"
        scene leanne_stage13_66
        "Reaching out to end the stream, she turns around to stare at your face."
        image leanne_stage13_67 = "/leanne/events/stage13/Leanne67.webp"
        scene leanne_stage13_67
        leanne "You okay? I didn't mean to be so rough with you."
        pc "I'm fine. Just…give me a minute to catch my breath."
        image leanne_stage13_68 = "/leanne/events/stage13/Leanne68.webp"
        scene leanne_stage13_68
        leanne "Take your time. We can clean up when you're ready."
        "Waiting until you regain my strength, Leanne hands you your clothes alongside some cleaning products to take care of the mess." 
        image leanne_stage13_69 = "/leanne/events/stage13/Leanne69.webp"
        scene leanne_stage13_69
        "Once you're finished, she rewards you with a kiss on the cheek before sending you home for the night." 
        $ leannestage13event3 = 0
        if recollection == False:
            $ daytime += 1
            $ phonecall = 1
            $ leanne.weight += 1
        return

label Halloween_Event:
    "You tune into the special costume contest stream."
    image halloween_1 = "/seasonal/halloween/1.webp"
    scene halloween_1
    play music "/music/leanne_stream2.ogg" if_changed
    leanne "Hey, everyone! Luxury Leanne here coming at you live from the beautiful Veldhaven historic manor."
    leanne "Today, I got a super special stream for you all. We rented this place to host a costume contest."
    image halloween_2 = "/seasonal/halloween/2.webp"
    scene halloween_2
    leanne "Now look at this place. It is massive! Fit for a queen of my size."
    leanne "And talking about queens, I'll be your queen today. Queen Leanne the Gluttonous."
    image halloween_3 = "/seasonal/halloween/3.webp"
    scene halloween_3
    leanne "Now, let's get the show rolling and find the contestants. We have a lot of great people with great costumes joining us today."
    leanne "And the best thing is, you guys can vote for the winner. What does the winner win? That is a surprise."
    image halloween_4 = "/seasonal/halloween/4.webp"
    scene halloween_4
    leanne "So, our first contestant here is Bonnie. Some of you might already know Bonnie."
    leanne "She sells the best chocolates in the world. I enjoyed those a bit too much lately."
    bonnie "Hello everyone!"
    image halloween_5 = "/seasonal/halloween/5.webp"
    scene halloween_5
    leanne "So, Bonnie, I have to say, you look stunning. I love your costume. This is exactly what this stream is about."
    leanne "Now, tell us, what is your outfit about, and why should people vote for you?"
    bonnie "I'm glad you like it, Leanne. I put a lot of hours into it."
    image halloween_6 = "/seasonal/halloween/6.webp"
    scene halloween_6
    bonnie "I wanted this outfit to be themed around things we all love. In my shop, I sell sweets that make people happy."
    bonnie "Nothing is better than seeing a customer leave with a smile. Now, what else is loved universally? Breasts."
    bonnie "So, I decided to combine the two things that spark joy."
    image halloween_7 = "/seasonal/halloween/7.webp"
    scene halloween_7
    bonnie "But it is not all about the breasts. I also have some adorable sweets and animals all over my dress."
    bonnie "I hope you don't mind me advertising here. Please visit my store. I'm confident you'll love the chocolates."
    image halloween_8 = "/seasonal/halloween/8.webp"
    scene halloween_8
    leanne "Thank you, Bonnie. To drive the point home, look at this work of art she is hiding behind her apron."
    leanne "I don't know about you guys, but you don't develop such a round tummy if the food is terrible."
    leanne "Take a closeup of this. While I'm well underway to developing such a nice round gut myself, I can't help but feel envious of your size and shape."
    leanne "It's a true testament to how delicious your chocolates are."
    image halloween_9 = "/seasonal/halloween/9.webp"
    scene halloween_9
    "Leanne then turns around Bonnie to show off her big bottom."
    leanne "And look at these buns, so full and round."
    image halloween_10 = "/seasonal/halloween/10.webp"
    scene halloween_10
    leanne "Thank you, Bonnie. I'm sure the audience loves your look."
    leanne "I won't hold you any longer, let's find the next contestant."
    bonnie "Don't forget to visit my humble shop!"
    image halloween_11 = "/seasonal/halloween/11.webp"
    scene halloween_11
    leanne "I have spotted our next contestant. Let's go up to her."
    image halloween_12 = "/seasonal/halloween/12.webp"
    scene halloween_12
    leanne "Hello there, Nice looking outfit! What is your name?"
    rebecca "Hey, I'm Rebecca. Do you know where the chocolates are?"
    leanne "Yes, I do. But before I'll tell you, you'll have to show off your outfit to the audience and tell them why they should vote for you."
    image halloween_13 = "/seasonal/halloween/13.webp"
    scene halloween_13
    rebecca "Audience?! Is this thing live?"
    leanne "Yes, we are currently live. Did you not read the invitation letter?"
    rebecca "I only read the part about Bonnie's chocolates and needing an outfit to enter."
    image halloween_14 = "/seasonal/halloween/14.webp"
    scene halloween_14
    rebecca "So I decided to go as a fierce purple fox. People always told me that I was sneaky, sly, and opportunistic."
    rebecca "So, a fox costume fits my character, I would say."
    image halloween_15 = "/seasonal/halloween/15.webp"
    scene halloween_15
    rebecca "And look, I even have a cute purple tail."
    rebecca "Look, I'll make it really simple for you guys. If you vote for me, I won't kidnap and torture you."
    rebecca "I'm just kidding, of course."
    image halloween_16 = "/seasonal/halloween/16.webp"
    scene halloween_16
    rebecca "Now tell me, streamer-lady. Where are those chocolates? I need them!"
    leanne "Thank you, Rebecca. The chocolates are next to the donuts and ice cream to the left of the stairs."
    image halloween_17 = "/seasonal/halloween/17.webp"
    scene halloween_17
    leanne "Come over here, I found our next contestant."
    leanne "It is a good thing I'm streaming on EroticaBase today, because our next contestant leaves little to the imagination."
    image halloween_18 = "/seasonal/halloween/18.webp"
    scene halloween_18
    leanne "I have to say, this sexy, scary look looks phenomenal on you."
    leanne "Please explain to the audience why you should win the costume contest."
    image halloween_19 = "/seasonal/halloween/19.webp"
    scene halloween_19
    maya "Hey guys, my name is Maya. I hope you all are enjoying the stream so far."
    maya "I think it is pretty obvious why I should win Leanne. Who doesn't want the sexy succubus to win?"
    maya "But for the people who still need convincing, I would like to show you what my outfit is all about."
    image halloween_20 = "/seasonal/halloween/20.webp"
    scene halloween_20
    leanne "Ooh, we are getting a live striptease."
    maya "As a succubus, it is my duty to seduce."
    image halloween_21 = "/seasonal/halloween/21.webp"
    scene halloween_21
    maya "I'll sweeten the deal for you guys. If I win, I'll take off this final piece of clothing."
    image halloween_22 = "/seasonal/halloween/22.webp"
    scene halloween_22
    leanne "Thank you, Maya. That was an amazing show."
    maya "Bye bye."
    leanne "Now, we have to talk about the sponsor of this event."
    image halloween_23 = "/seasonal/halloween/23.webp"
    scene halloween_23
    leanne "The sponsor of this event is FOH Meal Boxes."
    leanne "While many meal box services exist, FOH has an entirely new approach to this space."
    leanne "FOH recognizes that their meals are so good and addicting that they will increase your portions weekly while keeping the same price."
    leanne "With a nearly 100 percent retention of customers, they offer a full refund if you find yourself hungry."
    leanne "And that is not all; they promise that within three months, you'll be twice the person you were before."
    image halloween_24 = "/seasonal/halloween/24.webp"
    scene halloween_24
    leanne "Order now with code LuxLeanne for a fantastic deal on their annual plan. 30 percent off, plus a personalized funnel feeding plan to speed up your path to plush."
    leanne "They are so confident in their product that they will now do a live demonstration."
    image halloween_25 = "/seasonal/halloween/25.webp"
    scene halloween_25
    rebecca "Let me go! You’re taking this stupid costume contest roleplay too far. I just want my chocolates."
    leanne "As you can see, Rebecca is not yet convinced about the product."
    leanne "I'm sure that will change after the demonstration."
    image halloween_26 = "/seasonal/halloween/26.webp"
    scene halloween_26
    "You watch as the two mysterious women shove a large funnel into Rebecca's mouth."
    "Rebecca's face painted with surprise as she is forced to accept the foreign tube now pushed passed her lips."
    "A thick liquid can be seen slowly traveling down the tube and into Rebecca's awaiting maw."
    "As it starts to make its way past her lips her cheeks bulge and she starts to drink down the concoction."
    image halloween_27 = "/seasonal/halloween/27.webp"
    scene halloween_27
    "Within a matter of moments Rebecca’s form starts to swell before your very eyes."
    "Her body bulges and pushes against her confines and ever tightening clothes as she guzzles down more of the substance."
    "The pace increases and you can hear the groaning of material that binds her until.."
    "*POP*"
    image halloween_28 = "/seasonal/halloween/28.webp"
    scene halloween_28
    "Rebecca's enlarged ass and thighs finally burst through the black shorts and sections of rope that once constricted them."
    "Leaving her now prominent belly and small black underwear on full display."
    "She laboriously finishes the rest of the liquid in the funnel before the two mysterious women remove the rest of the rope binding her."
    image halloween_29 = "/seasonal/halloween/29.webp"
    scene halloween_29
    "Within a manner of minutes Rebecca's small but shapely form has been replaced with one that would rival the size of even Leanne herself."
    "It seems Rebecca is as shocked at the results as you are as she grabs, pokes, and prods her new found curves."
    image halloween_30 = "/seasonal/halloween/30.webp"
    scene halloween_30
    leanne "Wow look at you, come back over here so chat and myself can get a better look at you."
    leanne "A big improvement I'd say. You might even be bigger than me in a few places; a girl can get jealous, ya know?"
    "It seems Leanne shares your opinion of the size of Rebecca's larger, sexier form. She caresses the fox girl's bloated belly while eyeing her ample cleavage and enlarged assets. "
    leanne "Care to say anything to the folks at home about what just happened?"
    "Rebecca seems a bit out of it, taking a few seconds to process Leanne's question before she speaks."
    rebecca "T-that was so... Hot! I've never felt so g-good. The taste... the feeling...I felt so full, so good, but I just wanted more.. to not stop."
    rebecca "I didn't know I could feel that way about anything other than chocolate."
    image halloween_31 = "/seasonal/halloween/31.webp"
    scene halloween_31
    leanne "Well there you have a successful demonstration of FOH meal box services, guaranteed to have you bursting out of your clothes within your first week or your money back."
    leanne "Remember to use my code LuxLeanne for a discount on their annual year plan."
    leanne "Let's give our guests at home a better look at the results from today's sponsor."
    "Leanne puts her hand on Rebecca's waist and moves her to a better angle in front of the camera, while Rebecca spins around."
    image halloween_32 = "/seasonal/halloween/32.webp"
    scene halloween_32
    window hide
    pause
    image halloween_33 = "/seasonal/halloween/33.webp"
    scene halloween_33
    "The chat erupts in a flood of emotes and praise at the sight of Rebecca's colossal ass."
    leanne "And what a look."
    leanne "As much as I'm sure you loved our seeing {i}more{/i} of our last contestant it's time to move on."
    image halloween_34 = "/seasonal/halloween/34.webp"
    scene halloween_34
    leanne "Next contestant spotted. What do you say, chat? Shall we go on over?"
    image halloween_35 = "/seasonal/halloween/35.webp"
    scene halloween_35
    leanne "Our next contestant here works for the establishment that sells the greasiest food in town, trust me I should know with the amount of time I've spent there recently."
    "Leanne looks suggestively towards the camera for a second and winks. You can't help but feel that little line was meant specifically for her {i}biggest fan{/i}."
    leanne "It's Marie, the local manager at your favorite place with hot girls dressed in bunny girl costumes."
    image halloween_36 = "/seasonal/halloween/36.webp"
    scene halloween_36
    leanne "Say Marie tell the stream a bit about your outfit here today?"
    marie "U-uh, right sure. H-hello there everyone. I wanted to go with something more exotic, graceful, and beautiful for today's contest."
    marie "I figured there would be no better choice than a belly dancer's outfit."
    image halloween_37 = "/seasonal/halloween/37.webp"
    scene halloween_37
    leanne "Well, I have to say you really made a great choice."
    marie "Oh, thank yo-"
    image halloween_38 = "/seasonal/halloween/38.webp"
    scene halloween_38
    leanne "I mean, look at the size of this thing. Why wouldn't you want to show off your best asset, am I right?"
    "Marie seems a bit uncharacteristically flustered as Leanne processed to rub and caress the chunky brunette's gut."
    marie "Uh.."
    leanne "Well I don't believe I need to ask you why chat should send a vote your way this thing is the only answer they need."
    image halloween_39 = "/seasonal/halloween/39.webp"
    scene halloween_39
    "Marie seems unsure of what to make of the pink-haired streamer's boldness."
    "With praise and treatment she would normally be showering at others, she's clearly not used to having this turned around on her."
    marie "Uh well t-thank you Leanne."
    image halloween_40 = "/seasonal/halloween/40.webp"
    scene halloween_40
    leanne "Well Marie, any last words for our viewers at home before we move on to our final contestant?"
    "Having finally regained a bit more of her usual composure."
    marie "I would say to any of those in chat, come on down to Bunny Bites and we'll treat you right."
    marie "I hope to see some of you real soon, thanks for having me, Leanne."
    image halloween_53 = "/seasonal/halloween/53.webp"
    scene halloween_53
    leanne "Alright chat looks like we just spotted our last contestant."
    leanne "I hope to enjoy the view up front as much as I've enjoyed it from behind."
    image halloween_54 = "/seasonal/halloween/54.webp"
    scene halloween_54
    "Leanne makes her presence known as the busty, scantily clad figure turns to face her."
    leanne "Hey there, you're definitely a nun I would break a vow or two for."
    leanne "Looks like the only sin I've committed is not getting her sooner to appreciate it."
    leanne "Mind telling me your name Mother Superior?"
    "The seductively dressed holy women smiles flirtatiously."
    luna "You're not so bad yourself, the name's Luna."
    image halloween_55 = "/seasonal/halloween/55.webp"
    scene halloween_55
    leanne "Well Luna, I don't believe I've seen you around town before, what do you do?"
    luna "I am the owner and director of the hospital here in town."
    luna "And the principal investigator for the clinical research we do there."
    image halloween_56 = "/seasonal/halloween/56.webp"
    scene halloween_56
    leanne "Clinical research, huh?"
    leanne "That must be hard but rewarding work."
    luna "It can be for sure. We are currently developing a drug with the hopes to reduce or eliminate the effects of many breast related issues and diseases."
    image halloween_57 = "/seasonal/halloween/57.webp"
    scene halloween_57
    leanne "Wow, that sounds amazing. How's that going?"
    luna "Pretty great as you can see."
    "Luna turns to face directly toward the camera and motions to her overflowing bust."
    leanne "What do you mean?"
    luna "Well the drug has the added side effect of increasing fat distribution and acuminating it mostly in the subjects’ breasts."
    image halloween_58 = "/seasonal/halloween/58.webp"
    scene halloween_58
    "She puffs out her chest putting her hands behind her head to emphasize her ample assets."
    luna "As you can see it's been working wonders."
    image halloween_59 = "/seasonal/halloween/59.webp"
    scene halloween_59
    "The busty nun then does a little twirling giving the stream a full view of her curvaceous figure."
    image halloween_60 = "/seasonal/halloween/60.webp"
    scene halloween_60
    "Leanne cups one of the massive mounds and lifts it slightly."
    leanne "I'll say I mean look at the size of these things, and they feel so full and heavy.."
    leanne "I might have some debauchery and sinning to do if these massive fun bags are waiting for me at confession."
    "Luna simply smiles clearly pleased with the admiration and praise her favorite subjects are receiving."
    image halloween_61 = "/seasonal/halloween/61.webp"
    scene halloween_61
    leanne "Unfortunately, it's that time again, chat. We have to say goodbye to our last contestant, Luna."
    leanne "But fear not, if you wish to see her or any others again make sure to vote to choose our winner."
    leanne "Your queen guarantees both you at home and our first place contestant will love the reward that goes to the winner."
    image halloween_52 = "/seasonal/halloween/52.webp"
    scene halloween_52
    leanne "So now that we have spoken to all the contestants."
    leanne "It is time for you, the audience to pick the winner."
    "A poll opens up on the screen."
    "Leanne seems to have increased your voting power by a 1000x."
    menu:
        "Whould should I pick?"
        "Bonnie":
            image halloween_bonnie_win = "/seasonal/halloween/bonnie_win.webp"
            scene halloween_bonnie_win
            bonnie "Thank you so much for picking me."
            bonnie "Please come by my store, I'll be running a discount to celebrate this win."
            $ win = 1
        "Rebecca":
            image halloween_rebecca_win = "/seasonal/halloween/rebecca_win.webp"
            scene halloween_rebecca_win
            rebecca "Hey, I won!"
            rebecca "I mean, of course I won."
            $ win = 2
        "Maya":
            image halloween_maya_win = "/seasonal/halloween/maya_win.webp"
            scene halloween_maya_win
            maya "I'm glad you all picked me as the winner."
            maya "Please come by Velvet Shadows sometime."
            $ win = 3
        "Marie":
            image halloween_marie_win = "/seasonal/halloween/marie_win.webp"
            scene halloween_marie_win
            marie "I'm so happy to win this."
            marie "Thank you guys, Bunny Bites is always open for you."
            $ win = 4
        "Luna":
            image halloween_luna_win = "/seasonal/halloween/luna_win.webp"
            scene halloween_luna_win
            luna "Nice, I see there are some boob lovers in the audience."
            luna "I bet you all want to see these puppies grow even more."
            $ win = 5

    image halloween_41 = "/seasonal/halloween/41.webp"
    scene halloween_41
    leanne "While we set up the prize, it is time for a sponsor spot."
    image halloween_42 = "/seasonal/halloween/42.webp"
    scene halloween_42
    leanne "Have you ever felt like most of the foods mass is wasted when eaten?"
    leanne "Have you wished that nearly all the food you eat is transformed into layers of soft fat, instead of literally going down the toilet?"
    leanne "Or have you wished that instead of stuffing yourself for months, the stuffings had an immediate effect on your curves?"
    image halloween_43 = "/seasonal/halloween/43.webp"
    scene halloween_43
    leanne "Well, I got the solution for you!"
    leanne "The Insta-Gain 5000 pill!"
    leanne "With a near 100 percent efficiency, the Insta-Gain 5000 will convert all the mass of the food to subcautious fat deposits."
    image halloween_44 = "/seasonal/halloween/44.webp"
    scene halloween_44
    leanne "No longer do you have to work on yourself for months to become the fat ass you so deserve to be."
    leanne "As the Insta-Gain 5000 pill will almost instantly turn your degistive system into overdrive to process all the food."
    leanne "Not only do you gain all these amazing benefits, but it will also save you a big amount of money."
    image halloween_45 = "/seasonal/halloween/45.webp"
    scene halloween_45
    leanne "Those months of excessive ordering will no longer be needed to become the softest version of yourself."
    leanne "With a few good stuffings and some Insta-Gain 5000 pills, you'll be there in no time."
    image halloween_46 = "/seasonal/halloween/46.webp"
    scene halloween_46
    leanne "Let me demonstrate."
    image halloween_47 = "/seasonal/halloween/47.webp"
    scene halloween_47
    "The camera pans over to a overly stuffed woman."
    leanne "As you can see, she has been stuffed to the limit, I don't think I have ever seen anyone as stuffed like this."
    leanne "Now this is where the magic happens."
    image halloween_48 = "/seasonal/halloween/48.webp"
    scene halloween_48
    "The woman pops a pill into her mouth."
    image halloween_49 = "/seasonal/halloween/49.webp"
    scene halloween_49
    "A few seconds later somethings seems to happen to her."
    $ renpy.movie_cutscene("/images/seasonal/halloween/vid1.webm", stop_music=False)
    image halloween_50 = "/seasonal/halloween/50.webp"
    scene halloween_50
    leanne "As you can see, the results are incredible."
    image halloween_51 = "/seasonal/halloween/51.webp"
    scene halloween_51
    leanne "Order yours now!"

    if win == 1:
        #BONNIE WIN
        image halloween_bonnie1 = "/seasonal/halloween/bonnie1.webp"
        scene halloween_bonnie1
        leanne "Thank you again to our sponsor."
        leanne "And we are back with the first place winner, the ever lovable and sweet Bonnie!"
        image halloween_bonnie2 = "/seasonal/halloween/bonnie2.webp"
        scene halloween_bonnie2
        "She turns to reveal Bonnie standing up naked with a large hose inserted into her mouth."
        leanne "You voted for her and here she is."
        image halloween_bonnie3 = "/seasonal/halloween/bonnie3.webp"
        scene halloween_bonnie3
        "The pink-haired streamer moving a hand to Bonnie's ample butt, giving it a firm smack."
        leanne "I hear this gluttonous little piggy has a sweet tooth that puts all others to shame."
        leanne "So our sponsor has come up with something special just for her."
        leanne "Mixing three of their most fattening chocolatey blends together, sure to supersize any chocoholic in no time."
        image halloween_bonnie4 = "/seasonal/halloween/bonnie4.webp"
        scene halloween_bonnie4
        "Leanne's words cause a moan to emanate from the gluttonous brunette."
        "A whirring sound can be heard as Leanne gives the signal to start and the machine kicks to life."
        "Bonnie's eyes roll back and she starts sucking down the onslaught of fattening chocolate."
        "Her neck bulges as she gulps between breaths to accommodate the sheer volume of chocolate flooding into her swelling stomach."
        "Her ass rapidly piles on fat as you can see her hips and ass peek out behind her ever increasing form even when viewing her from the front."
        $ renpy.movie_cutscene("/images/seasonal/halloween/bonnie5.webm", stop_music=False)
        $ renpy.movie_cutscene("/images/seasonal/halloween/bonnie6.webm", stop_music=False)
        $ renpy.movie_cutscene("/images/seasonal/halloween/bonnie7.webm", stop_music=False)
        image halloween_bonnie8 = "/seasonal/halloween/bonnie8.webp"
        scene halloween_bonnie8
        "Bonnie keeps growing larger, heavier until her titanic butt pulls her down to the ground with its sheer weight."
        "Causing an audible crash as her soft backside hits the ground and visibly shakes the camera."
        "Her stretched belly and bulging thighs left on clear display, rising multiple feet off the ground absolutely packed with fat."
        image halloween_bonnie9 = "/seasonal/halloween/bonnie9.webp"
        scene halloween_bonnie9
        "The beached baker is unable to move herself more than a few inches up and she tries to fruitlessly sit up, pinned under the sheer size of her belly."
        image halloween_bonnie10 = "/seasonal/halloween/bonnie10.webp"
        scene halloween_bonnie10
        "Leanne returns to frame barely needing to bend down as she rests a hand on the bloated brunette's form."
        leanne "Well it looks like this gluttonous little piggy upgraded herself to full blown beached whale."
        leanne "I'd ask how amazing that felt but it's clear from the look on Bonnie's face that she's a bit too full to speak at the moment."
        "Bonnie lets out a loud burp and grunts in acknowledgement. Too full and pinned down by her own fat to think about much other than taking it easy."
        leanne "Well, I hope you all enjoyed the stream, I know our first place winner sure did. this has been your one and only Queen Leanne the Gluttonous signing off!"
    elif win == 2:
        image halloween_rebecca1 = "/seasonal/halloween/rebecca1.webp"
        scene halloween_rebecca1
        leanne "And now we are back with the moment you've all been waiting for!"
        image halloween_rebecca2 = "/seasonal/halloween/rebecca2.webp"
        scene halloween_rebecca2
        "The pink-hair streamer reveals to the camera a naked Rebecca taking up the middle of a large sofa with a tube inserted into her mouth hanging from the ceiling."
        leanne "As you can see behind me Rebecca here is looking to make a repeat performance of improvements her earlier feat had on her once slim body."
        image halloween_rebecca3 = "/seasonal/halloween/rebecca3.webp"
        scene halloween_rebecca3
        "She steps closer to emphasize her point, resting a hand on Rebecca's now large exposed breast."
        leanne "If she thought the first time was good, Rebecca is sure to have a near orgasmic experience when we let her try today’s prize."
        leanne "FOH's new Chocoaddicts Surprise, for when you're chocolate cravings are near endless."
        image halloween_rebecca4 = "/seasonal/halloween/rebecca4.webp"
        scene halloween_rebecca4
        "You can see Rebecca squirm in anticipation as she eagerly awaits the taste of her liquidy treat."
        "The liquid slowly makes its way down the funnel as it starts to pick up pace. You can see Rebecca visibly fatten before your eyes."
        "Her body rapidly fills with fat as her fat ass, wide hips, and colossal belly start to engulf the sofa she is seated on."
        $ renpy.movie_cutscene("/images/seasonal/halloween/rebecca5.webm", stop_music=False)
        $ renpy.movie_cutscene("/images/seasonal/halloween/rebecca6.webm", stop_music=False)
        $ renpy.movie_cutscene("/images/seasonal/halloween/rebecca7.webm", stop_music=False)
        image halloween_rebecca8 = "/seasonal/halloween/rebecca8.webp"
        scene halloween_rebecca8
        "Rebecca has a divine look on her face as she finishes the massive supply of chocolatey liquid. Her body has swelled with fat taking up most of the space on the once large three person couch."
        "Now the couch now left heaving under Rebecca's sustainable weight with only enough room for a person her original size at the start of the stream."
        "You would guess Rebecca is at least three times the woman she came in as, with a pillowy belly that oozes over her knees while seated."
        image halloween_rebecca9 = "/seasonal/halloween/rebecca9.webp"
        scene halloween_rebecca9
        rebecca "That was so much hotter, and better than the first time. Nothing has ever felt {i}that{/i} good..."
        rebecca "A girl could get addicted to this kind of treatment."
        image halloween_rebecca10 = "/seasonal/halloween/rebecca10.webp"
        scene halloween_rebecca10
        leanne "Wow! Look at the size of this belly. It alone has to weigh more than I do."
        image halloween_rebecca11 = "/seasonal/halloween/rebecca11.webp"
        scene halloween_rebecca11
        leanne "Now chat I think it's time to wrap it up here. I've got to show a little appreciation to our large lady here, one queen to another."
        leanne "With that I say, this has been your one and only Queen Leanne the Gluttonous signing off!"
    elif win == 3:
        #MAYA WIN
        image halloween_maya1 = "/seasonal/halloween/maya1.webp"
        scene halloween_maya1
        leanne "You loved her, you voted for her, let's check in with our sexy succubus Maya!"
        image halloween_maya2 = "/seasonal/halloween/maya2.webp"
        scene halloween_maya2
        "Leanne turns to reveal Maya with a hose attached to a mask and her hands bound behind her head."
        "Maya's ample naked body on full display, her costume reduced to only her horns and dark makeup."
        image halloween_maya3 = "/seasonal/halloween/maya3.webp"
        scene halloween_maya3
        leanne "Our naughty little succubus has been trying to drain all she can for you all night chat, but don't worry your queen is here to save you."
        leanne "I have exactly the right punishment for this vixen thanks to our sponsor."
        leanne "FOH specializes in advanced feeding services that are designed to bring out maximum pleasure with fattening results."
        leanne "I think the Blissfully Big Boned feeding package should be perfect to quench the thirst of our beautiful temptress here."
        leanne "It's designed to help tingle all the pleasure centers of the brain and provide you with the ultimate eating experience."
        image halloween_maya4 = "/seasonal/halloween/maya4.webp"
        scene halloween_maya4
        "Leanne leaves the frame ready to overload Maya's senses with a truly unique experience."
        "She gives the signal and a white liquid comes splashing down the tube straight past the tattooed women's lips."
        "Maya moans in pleasure as the liquid is pumped into her gullet."
        "Her thick curves bulge out in every direction as she starts rapidly filling up the large three person couch she's seated on."
        "Maya's breasts surging, growing larger and fatter, obscuring her view of her growing stomach as it steadily increases in size."
        "Her belly pushing further and further out almost as if it was trying to equally match her quivering breasts as a means to support them."
        "The dark haired girl's ass takes up more and more of the seated space as her hips surge further out to each of her sides."
        $ renpy.movie_cutscene("/images/seasonal/halloween/maya5.webm", stop_music=False)
        $ renpy.movie_cutscene("/images/seasonal/halloween/maya6.webm", stop_music=False)
        $ renpy.movie_cutscene("/images/seasonal/halloween/maya7.webm", stop_music=False)
        image halloween_maya8 = "/seasonal/halloween/maya8.webp"
        scene halloween_maya8
        "The entire time Maya can be heard with moans of pleasure and acceptance of her punishment until finally she finishes the liquid."
        "Her doughy bedlike belly now resting just at the knee, just slightly out pacing her massive breasts."
        image halloween_maya9 = "/seasonal/halloween/maya9.webp"
        scene halloween_maya9
        "Maya's ass now takes up a bit more than two spaces of the three person couch as it groans under her weight as she adjusts her newly acquired mass."
        "Her once curvy form is that of an absolute goddess, bulging, sizable, and breathtaking."
        image halloween_maya10 = "/seasonal/halloween/maya10.webp"
        scene halloween_maya10
        "Leanne: Oops chat, I think it might have fired. Because this girl just went from naughty succubus to an absolute sex bomb queen of the damned."
        leanne "I don't think there's anything I can do to save you from her now. Well your majesty, is there anything you would like to say to your loyal supporters and subjects?"
        maya "I feel absolutely devilish, your queen has grown immense and she demands tribute."
        maya "I expect to see you all come down to see me at Velvet Shadows, I guarantee you won't be able to take your eyes off me."
        leanne "Well there you have it, chat, your queen has spoken."
        leanne "Maybe I'll get Maya to help me work a bit on my own form, from one queen to another this is Queen Leanne the Gluttonous signing off!"
    elif win == 4:
        #MARIE WIN
        image halloween_marie1 = "/seasonal/halloween/marie1.webp"
        scene halloween_marie1
        leanne "Thanks to our sponsor for that and now it's time for the main event."
        image halloween_marie2 = "/seasonal/halloween/marie2.webp"
        scene halloween_marie2
        "Leanne takes a step back to reveal Marie naked strapped to a chair with a large funnel in her mouth."
        leanne "Our little first place winner here is a little indisposed as you can see. So, you'll have to forgive her for being a little quiet."
        image halloween_marie3 = "/seasonal/halloween/marie3.webp"
        scene halloween_marie3
        leanne "I'm sure you all remember the treatment Rebecca got during one of our sponsor segments."
        leanne "Since you voted for our first place belly dancer Marie we figured we would give you more of what you want."
        image halloween_marie4 = "/seasonal/halloween/marie4.webp"
        scene halloween_marie4
        "Leanne moves over and the camera raises to give an overhead view of Marie as she waits for her prize."
        leanne "Let's see what an extra large dose of FOH's Big Chonker Slurry can do for our first place winner!"
        "The liquid quickly runs down from overhead and starts to fill its eager target's mouth."
        "Marie's stomach starts to swell much quicker and with greater effect than the last time you saw it in action."
        $ renpy.movie_cutscene("/images/seasonal/halloween/marie5.webm", stop_music=False)
        $ renpy.movie_cutscene("/images/seasonal/halloween/marie6.webm", stop_music=False)
        $ renpy.movie_cutscene("/images/seasonal/halloween/marie7.webm", stop_music=False)
        image halloween_marie8 = "/seasonal/halloween/marie8.webp"
        scene halloween_marie8
        "Marie's stomach has taken the brunt of the fattening."
        "Swelling to the size of a yoga ball; she smiles in bliss towards the camera, it's now much more evident how much fatter her face and double chin have become."
        image halloween_marie9 = "/seasonal/halloween/marie9.webp"
        scene halloween_marie9
        marie "That was amazing..."
        marie "This piggy has never felt more like herself, thanks to all of you that voted to make this girl go whole hog."
        marie "Now I think it's time for this pig to laze around."
        image halloween_marie10 = "/seasonal/halloween/marie10.webp"
        scene halloween_marie10
        leanne "That display of gluttony was absolutely amazing!"
        leanne "I think it might be time for this big ol' belly to receive some rubs wouldn't you say piggy?"
        "Marie just quietly grunts and lets out an oink of acknowledgement."
        leanne "Thanks for tuning in! Until next time this has been your one and only Queen Leanne the Gluttonous signing off!"
    elif win == 5:
        #LUNA WIN
        image halloween_luna1 = "/seasonal/halloween/luna1.webp"
        scene halloween_luna1
        leanne "Alright everyone, after that sponsored break we are back with our winner Luna!"
        image halloween_luna2 = "/seasonal/halloween/luna2.webp"
        scene halloween_luna2
        leanne "Luna here has a great pair of already massive tits."
        leanne "And since you at home voted for the girl with so much up top I figure we all would enjoy the surprise I mentioned for the winner of our little competition here."
        image halloween_luna3 = "/seasonal/halloween/luna3.webp"
        scene halloween_luna3
        "Leanne reaches a hand over to Luna's exposed breast and cups the heavy mass raising it slightly."
        leanne "Oof, massive is right this girl has an amazing pair let me tell you."
        leanne "Well what do you say Luna, chat? Would you like to see these puppies be larger and even more impressive?"
        "Chat erupts into a cacophony of hearts and praise as they eagerly agree to the idea of Luna's already ample chest expanding even further."
        leanne "I thought you might like that."
        leanne "You've already seen what our sponsor is capable of today so, it should come as no surprise to anyone that they also have a solution for those looking for a bit more up top and fast."
        luna "I couldn't think of a better prize, my breasts are my favorite part of my body. I'm so ready for this!"
        image halloween_luna4 = "/seasonal/halloween/luna4.webp"
        scene halloween_luna4
        "Luna is handed a small pill by the pink-haired streamer, and Leanne quickly makes herself scarce."
        "Like magic right before your eyes Luna's already impressive bust surges forward."
        "The jiggling masses hit with multiple waves of growth until they finally come to a rest heavily on the nearby table."
        $ renpy.movie_cutscene("/images/seasonal/halloween/luna5.webm", stop_music=False)
        $ renpy.movie_cutscene("/images/seasonal/halloween/luna6.webm", stop_music=False)
        $ renpy.movie_cutscene("/images/seasonal/halloween/luna7.webm", stop_music=False)
        image halloween_luna8 = "/seasonal/halloween/luna8.webp"
        scene halloween_luna8
        "If Luna's breasts were massive before, they have since dwarfed that entirely with their current size."
        "Her large chest would likely hang down past her navel coming to a rest on her thighs if not currently be held up by a large table."
        image halloween_luna9 = "/seasonal/halloween/luna9.webp"
        scene halloween_luna9
        "The sheer size of Luna's chest can not be understated, her bean bag sized udders now cover the entirety of the table in front of her."
        image halloween_luna10 = "/seasonal/halloween/luna10.webp"
        scene halloween_luna10
        "Leanne quickly appears back in frame and cups one of Luna's enlarged breasts."
        leanne "There you have it! A fitting prize for our first place winner. Hope you all enjoyed it at home as much as I did."
        luna "A-and me..."
        leanne "This has been your one and only Queen Leanne the Gluttonous signing off!"

    if leannechoice == 2:
        image halloween_leanne_end = "/seasonal/halloween/leanne_end.webp"
        scene halloween_leanne_end
        "A loud crash and bang can be heard sending you into a panic as you hear two cats hiss at one another outside your house."
        "It’s at this time you realize that you’d fallen asleep while watching Leanne’s stream on fidget."
        "The few late nights you’ve had and lack of sleep staying up trying to get a bit better at Carl of Duty to be able to better compete with Leanne clearly catching up to you."
        "You must have dreamed the entire costume stream… that explains… a few things…"
        "You make a mental note to maybe not watch one of Leanne’s streams if you’re tired and are just better off catching up on some sleep."
    elif leannechoice == 1:
        image halloween_lyn_end = "/seasonal/halloween/lyn_end.webp"
        scene halloween_lyn_end
        "A loud crash and bang can be heard sending you into a panic as you hear two cats hiss at one another outside your house."
        "It’s at this time you realize that you’d fallen asleep while watching Lyn’s stream on fidget."
        "The few late nights you’ve had and lack of sleep staying up trying to get a bit better at Carl of Duty to be able to better compete with Lyn clearly catching up to you."
        "You must have dreamed the entire costume stream… that explains… a few things…"
        "You make a mental note to maybe not watch one of Lyn’s streams if you’re tired and are just better off catching up on some sleep."
    stop music fadeout 1.0
    return
