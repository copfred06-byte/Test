label Hari_study_1:
    play music "/music/hari.ogg" if_changed
    if hari.stage >= 4:
        image hari_study_arrive = "/hari/[hari.stage]/study_arrive.webp"
        scene hari_study_arrive
        "Picking up the supplies from Daisy, you head to the study room."
        image hari_study_sitting = "/hari/[hari.stage]/study_sitting.webp"
        scene hari_study_sitting
        hari "Hello [playername]."
        pc "Hey Hari. Ready for the study session?"
        hari "You bet."
        image hari_study_eat1 = "/hari/[hari.stage]/study_eat1.webp"
        scene hari_study_eat1
        "As you take on the task of unpacking the food and taking notes, she proceeds to scarf down the entire meal."
        "She manages to finish off the snacks with plenty of time to spare."
        image hari_study_aftereat = "/hari/[hari.stage]/study_aftereat.webp"
        scene hari_study_aftereat
        hari "Those were pretty good. I wonder what Ms. Tanwen will give us next time."
        if haristory <= 5 and hari.stage >= 7:
            menu:
                "Ask Hari about herself.":
                    "You decide to ask Hari about herself."
                    hari "I… guess I'll tell you a bit about myself."
                    "Hari talks a bit about herself."
                    $ haristory += 1
                    #Unlocks more Hari story in the stats page.
                    $ renpy.notify("New Hari story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Hari anything."
        elif haristory <= 4 and hari.stage >= 6:
            menu:
                "Ask Hari about herself.":
                    "You decide to ask Hari about herself."
                    hari "I… guess I'll tell you a bit about myself."
                    "Hari talks a bit about herself."
                    $ haristory += 1
                    #Unlocks more Hari story in the stats page.
                    $ renpy.notify("New Hari story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Hari anything."
        elif haristory <= 3 and hari.stage >= 5:
            menu:
                "Ask Hari about herself.":
                    "You decide to ask Hari about herself."
                    hari "I… guess I'll tell you a bit about myself."
                    "Hari talks a bit about herself."
                    $ haristory += 1
                    #Unlocks more Hari story in the stats page.
                    $ renpy.notify("New Hari story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Hari anything."
        elif haristory <= 2 and hari.stage >= 4:
            menu:
                "Ask Hari about herself.":
                    "You decide to ask Hari about herself."
                    hari "I… guess I'll tell you a bit about myself."
                    "Hari talks a bit about herself."
                    $ haristory += 1
                    #Unlocks more Hari story in the stats page.
                    $ renpy.notify("New Hari story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Hari anything."
        elif haristory <= 1 and hari.stage >= 3:
            menu:
                "Ask Hari about herself.":
                    "You decide to ask Hari about herself."
                    hari "I… guess I'll tell you a bit about myself."
                    "Hari talks a bit about herself."
                    $ haristory += 1
                    #Unlocks more Hari story in the stats page.
                    $ renpy.notify("New Hari story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Hari anything."
        elif haristory == 0 and hari.stage >= 2:
            menu:
                "Ask Hari about herself.":
                    "You decide to ask Hari about herself."
                    hari "I… guess I'll tell you a bit about myself."
                    "Hari talks a bit about herself."
                    $ haristory += 1
                    #Unlocks more Hari story in the stats page.
                    $ renpy.notify("New Hari story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Hari anything."
        image hari_study_standing = "/hari/[hari.stage]/study_standing.webp"
        scene hari_study_standing
        "After cleaning up the leftover boxes, the two of you part ways."
    else:
        #(NOTE: The repeatable study sessions will be split into three parts, A, B, and C. Should the player choose to go through all three previous scenes over the course of a single week, Part D, the presentation, will occur that Friday before Daisy’s Friday Feeding session.)
        #Scene: Study Session (Version 1 Part A) (Occurs from stages 1-8)
        image hari_study_sitting2 = "/hari/[hari.stage]/study_sitting2.webp"
        scene hari_study_sitting2
        "Picking up the supplies from Daisy, you head to the study room and sit down across from Hari."
        image hari_study_eat1 = "/hari/[hari.stage]/study_eat1.webp"
        scene hari_study_eat1
        "As you take on the task of unpacking the food and taking notes, she proceeds to scarf down the entire meal."
        "Though it takes a while, she manages to finish it off just as time expires."
        image hari_study_aftereat = "/hari/[hari.stage]/study_aftereat.webp"
        scene hari_study_aftereat
        hari "I… guess I’ll see you next time."
        image hari_study_standing = "/hari/[hari.stage]/study_standing.webp"
        scene hari_study_standing
        "After cleaning up the leftover boxes, the two of you part ways."
    $ hari_study_times = 1
    if hari.stage >= 7:
        $ hari.weight += 0.6
    elif hari.stage >= 4:
        $ hari.weight += 0.4
    else:
        $ hari.weight += 0.2
    return

label Hari_study_2:
    play music "/music/hari.ogg" if_changed
    if hari.stage >= 4:
        #(NOTE: The following should occur if the player runs into study session version 2 part A on a previous day in the same week)
        image hari_study_sitting = "/hari/[hari.stage]/study_sitting.webp"
        scene hari_study_sitting
        "You arrive at the study room and are greeted with a shaky smile."
        hari "Heh, I guess Ms. Tanwen increased the size of the portions again."
        pc "Think you can handle it?"
        hari "I’ll give it my best shot."
        image hari_study_eat1 = "/hari/[hari.stage]/study_eat1.webp"
        scene hari_study_eat1
        "Like before Hari eats through the supplies while you take notes."
        "Though the servings are larger than before, she manages to work through the entire spread just as the bell rings."
        image hari_study_aftereat = "/hari/[hari.stage]/study_aftereat.webp"
        scene hari_study_aftereat
        pc "Good work today."
        hari "Thank you."
        image hari_study_standing = "/hari/[hari.stage]/study_standing.webp"
        scene hari_study_standing
        "After helping Hari clean up, you head home for the day."
    else:
        #(NOTE: The following should occur if the player runs into study session version 1 part A on a previous day in the same week)
        image hari_study_arrive = "/hari/[hari.stage]/study_arrive.webp"
        scene hari_study_arrive
        "Bringing in the session’s snack supply, to notice Hari get a bit anxious as she looks over the haul."
        image hari_study_sitting2 = "/hari/[hari.stage]/study_sitting2.webp"
        scene hari_study_sitting2
        pc "Is everything alright?"
        hari "Y-yeah. It’s fine. I’m sure I can do it."
        image hari_study_eat1 = "/hari/[hari.stage]/study_eat1.webp"
        scene hari_study_eat1
        "Just as before Hari eats through the supplies while you take notes."
        "Though the servings are larger than before, she seems to be pushing herself further in order to keep up the pace."
        "Just as she places the final snack in her mouth, the bell rings."
        image hari_study_aftereat = "/hari/[hari.stage]/study_aftereat.webp"
        scene hari_study_aftereat
        pc "Good work today."
        hari "Um, thank you."
        image hari_study_standing = "/hari/[hari.stage]/study_standing.webp"
        scene hari_study_standing
        "After helping Hari clean up, you head home for the day."
    $ hari_study_times = 2
    if hari.stage >= 7:
        $ hari.weight += 0.9
    elif hari.stage >= 4:
        $ hari.weight += 0.6
    else:
        $ hari.weight += 0.3
    return

label Hari_study_3:
    play music "/music/hari.ogg" if_changed
    if hari.stage >= 4:
        #(NOTE: The following should occur if the player runs into study session version 2 part A and B on previous days in the same week.)
        image hari_study_arrive = "/hari/[hari.stage]/study_arrive.webp"
        scene hari_study_arrive
        "Though it takes a bit of effort, you manage to haul over the large supply of snacks into the study room."
        image hari_study_sitting3 = "/hari/[hari.stage]/study_sitting3.webp"
        scene hari_study_sitting3
        "Though your initial arrival is greeted by a small smile, it quickly changes into a look of awe as she sees the food supply."
        hari "Ms. Tanwen doesn’t let up, does she?"
        pc "I can always go back and ask her to give us a smaller serving."
        hari "You don’t have to do that. Besides…I want to see if I can really do it."
        image hari_study_eat3 = "/hari/[hari.stage]/study_eat3.webp"
        scene hari_study_eat3
        "Just as before, you assist Hari as she goes through the food."
        image hari_study_eat2 = "/hari/[hari.stage]/study_eat2.webp"
        scene hari_study_eat2
        "Though she attempts to work her way through the stash, reality sets in."
        "Her initially quick pace falters as she reaches the end, leaving her a few bites short of finishing off the feast when the bell rings."
        image hari_study_eat4 = "/hari/[hari.stage]/study_eat4.webp"
        scene hari_study_eat4
        hari "I was so close."
        pc "It was still pretty impressive and more than enough for a presentation. That is, if you’re willing to do one tomorrow."
        image hari_study_eat5 = "/hari/[hari.stage]/study_eat5.webp"
        scene hari_study_eat5
        hari "After all we’ve done, it would be kind of a waste not to at least try for the extra credit. Let’s do it."
        "Cleaning up the empty wrappers and dropping off the leftover snacks to Daisy, the two of you head home."
    else:
        #(NOTE: The following should occur if the player runs into study session version 1 part A and B on previous days in the same week.)
        image hari_study_arrive = "/hari/[hari.stage]/study_arrive.webp"
        scene hari_study_arrive
        "Though it takes a bit of effort, you manage to haul over a large supply of snacks into the study room."
        image hari_study_sitting3 = "/hari/[hari.stage]/study_sitting3.webp"
        scene hari_study_sitting3
        "Though your initial arrival is greeted by a small smile, it quickly changes into a look of awe as she sees the food supply."
        hari "D-does Ms. Tanwen really expect me to eat all of that?"
        pc "You were able to finish the others, so I’m assuming so. I can ask her to change it to something smaller if you want."
        hari "No, it’s fine. I’ll…try my best."
        image hari_study_eat3 = "/hari/[hari.stage]/study_eat3.webp"
        scene hari_study_eat3
        "Just as before, you assist Hari as she goes through the food."
        image hari_study_eat2 = "/hari/[hari.stage]/study_eat2.webp"
        scene hari_study_eat2
        "Though she attempts to keep up a fast pace to deal with the surplus of snacks, she’s only able to push herself so far."
        "Inevitably, she’s forced to slow down, incapable of finishing the supply before the bell rings."
        image hari_study_eat4 = "/hari/[hari.stage]/study_eat4.webp"
        scene hari_study_eat4
        hari "I’m sorry I couldn't finish it all."
        pc "It’s fine. We still have plenty of data to present to the class. Do you think you’re up for another presentation?"
        image hari_study_eat5 = "/hari/[hari.stage]/study_eat5.webp"
        scene hari_study_eat5
        "Hari takes a deep breath."
        hari "I…think so. I managed to survive last time so I should be fine."
        "Cleaning up the empty wrappers and dropping off the leftover stacks to Daisy, the two of you head home."
    $ hari_study_times = 3
    if hari.stage >= 7:
        $ hari.weight += 1.5
    elif hari.stage >= 4:
        $ hari.weight += 1.0
    else:
        $ hari.weight += 0.5
    return

label Hari_study_4:
    if hari.stage >= 4:
        #Scene: Friday Presentation (Version 2) (Occurs from Stage 4+)
        #(NOTE: The following should occur after the player has done parts A,B, and C of the Version 2 Study Session events in the same week. If so, this should happen after Daisy’s initial morning greeting during a Friday Class)
        call rngteachingscene from _call_rngteachingscene_267
        teacher "Before we get to the main portion of today's lesson, I believe someone has a presentation they would like to give."
        teacher "Could you please stand up and show the class what you have?"
        image hari_study_presentation1 = "/hari/[hari.stage]/study_presentation1.webp"
        scene hari_study_presentation1
        "Following Hari up to the front of the class, you begin the presentation."
        "Though Hari does need your help from time to time, she manages to do the bulk of the presentation by herself."
        "After going through a review of the different snacks, you wait until Hari gives you the okay before moving forward."
        image hari_study_measure = "/hari/[hari.stage]/study_measure.webp"
        scene hari_study_measure
        "With measuring tape in hand, you cautiously record Hari's new sizes. When you're finished, Hari takes up the duty of informing the class."
        if persistent.imperial:
            $ imperialweight = (hari.weight * 2.2)
            hari "I currently weigh [imperialweight:.02f] lbs. My belly is [hari.waist_size:.02f] inches and my butt is [hari.ass_size:.02f] inches."
            hari "Finally, my breasts are [hari.breast_cup] cup and measure [hari.breast_size:.02f] inches."
        else:
            $ metricwaist_size = (hari.waist_size * 2.54)
            $ metricbreast_size = (hari.breast_size * 2.54)
            $ metricass_size = (hari.ass_size * 2.54)
            hari "I currently weigh [hari.weight:.02f] kg. My belly is [metricwaist_size:.02f] cm and my butt is [metricass_size:.02f] cm."
            hari "Finally, my breasts are [hari.breast_cup] cup and measure [metricbreast_size:.02f] cm."
        teacher "Excellent job. You may return to your seats. I'll be sure to add the extra credit to your grades."
        #(NOTE: The rest of the usual, Friday class should play out from here).
    else:
        #Scene: Friday Presentation (Version 1) (Occurs from Stages 1-3)
        #(NOTE: The following should occur after the player had done parts A,B, and C of the Version 1 Study Session events in the same week. If so, this should happen after Daisy’s initial morning greeting during a Friday Class)
        call rngteachingscene from _call_rngteachingscene_268
        teacher "Before we get to the main portion of today's lesson, I believe someone has a presentation they would like to give."
        teacher "Could you please stand up and show the class what you have?"
        image hari_study_presentation1 = "/hari/[hari.stage]/study_presentation1.webp"
        scene hari_study_presentation1
        "Following Hari up to the front of the class, you begin the presentation."
        "Whenever Hari stumbles on her words, you're quick to help her out."
        "After going through your reviews of the different snacks, you wait until Hari gives you the okay before moving forward."
        image hari_study_measure = "/hari/[hari.stage]/study_measure.webp"
        scene hari_study_measure
        "With measuring tape in hand, you cautiously record Hari's new sizes. When you're finished, Hari takes up the duty of informing the class."
        if persistent.imperial:
            $ imperialweight = (hari.weight * 2.2)
            hari "I-I currently weigh [imperialweight:.02f] lbs. My belly is [hari.waist_size:.02f] inches."
            hari "My…butt is [hari.ass_size:.02f] inches. And my…breasts are [hari.breast_cup] cup and measure [hari.breast_size:.02f] inches."
        else:
            $ metricwaist_size = (hari.waist_size * 2.54)
            $ metricbreast_size = (hari.breast_size * 2.54)
            $ metricass_size = (hari.ass_size * 2.54)
            hari "I-I currently weigh [hari.weight:.02f] kg. My belly is [metricwaist_size:.02f] cm."
            hari "My…butt is [metricass_size:.02f] cm. And my…breasts are [hari.breast_cup] cup and measure [metricbreast_size:.02f] cm."
        teacher "Excellent job. You may return to your seats. I'll be sure to add the extra credit to your grades."
        #(NOTE: The rest of the usual, Friday class should play out from here).
    return

label Hari_cards:
    #(NOTE: The following should occur as a random event during a study session after the stage 2 events)
    #IMAGE: Hari sitting in the study room.
    "Picking up a strangely small supplies of snacks from Daisy, you go to the study room to meet up with Hari."
    hari "Is that…really all she gave us this time?"
    pc "I guess she must have run out of snacks or something."
    #IMAGE: The player sitting across from Hari.
    "Hari very easily eats through the small sampling, leaving the two of you with plenty of free time."
    pc "Do you want to do anything?"
    #IMAGE: Smiling Hari with a Cutie Card Clash cards in her hands.
    "Reaching into her bag, Hari pulls out two decks of cards."
    hari "Would you…like to play a game of Cutie Card Clash?"
    "With nothing else to do, you decide to go along with her suggestion despite having only a vague understanding of the game."
    #(NOTE: The outcome of the game will be random)
    $ rng = renpy.random.randint(1,3)
    if rng == 1:
        #Outcome A) Hari wins
        #IMAGE: Smiling Hari with a hand of cards
        "Through a combination of Hari’s skills and your lack of understanding how the game is meant to be played, she easily claims victory."
        hari "That was fun. Want to go again? I promise I’ll go easy on you."
        "You’re thankfully saved from further losses thanks to the ringing of the bell."
        pc "Looks like we’ve got to get going. Maybe next time."
    elif rng == 2:
        #Outcome B) The player wins
        "Mostly through dumb luck, you manage to win the game against Hari."
        hari "Wow, you really got me. Want to go again?"
        "You’re prevented from taking up her rematch offer as the bell rings."
        hari "Shoot. Guess we’ll have to do this some other time."
    elif rng == 3:
        #Outcome C) Draw game
        "Your shaky understanding of the game nonetheless proves to be enough to keep the match going for the duration of the study session."
        "Unfortunately, this also means that you’re unable to finish the game before the bell rings."
        hari "I didn’t realize how long we were playing. Guess we’ll have to call it a draw for now."
    #(NOTE: Regardless of the outcome, the following should play out.)
    "Putting away the cards and disposing the empty snack wrappers, you head home for the day."
    return


#Hari Events
label Hari_Stage_0_Event:
    #Scene: Hari’s Introduction
    #(NOTE: The following should occur after Daisy’s Stage 3 event after one of Daisy’s regular classes)
    scene university_empty
    play music "/music/university.ogg" if_changed
    "While everyone takes their leave, you pack you bag at a snails pace while thinking about today's lesson."
    "Having a burning question regarding the day’s lesson, you approach Daisy’s desk after class."
    image hari_stage0_1 = "/hari/events/stage0/1.webp"
    scene hari_stage0_1
    "After turning back to the front you’re surprised to see she’s already talking with someone."
    "It’s a female student that you haven’t noticed before."
    image hari_stage0_2 = "/hari/events/stage0/2.webp"
    scene hari_stage0_2
    "Though that could be explained with her drab fashion, you find it hard to believe that you’ve gone this long without seeing her head of platinum blonde hair."
    "While trying to figure out how you haven’t noticed her before, you can’t help listening in on their conversation."
    image hari_stage0_3 = "/hari/events/stage0/3.webp"
    scene hari_stage0_3
    teacher "I’m not sure how you heard, but yes. I’m planning to implement a new teaching program in the near future."
    $ unknownname = 'Blonde Student'
    unknown "Can’t you…delay it? Or at least give me an option if I want to do it by myself?"
    teacher "I’m afraid that would defeat the purpose. After all, I want to use this opportunity to learn what it’s like to have a-"
    image hari_stage0_4 = "/hari/events/stage0/4.webp"
    scene hari_stage0_4
    "Daisy stops speaking as both she and the student finally notice you standing there."
    teacher "Sorry, I didn’t see you. Did you have a question?"
    pc "Er, yeah, but I’ve kind of forgotten it. Sorry."
    teacher "That’s alright. It’s important for a teacher to be open to their student’s questions."
    pc "What were you talking about?"
    image hari_stage0_5 = "/hari/events/stage0/5.webp"
    scene hari_stage0_5
    teacher "Ah, this young lady was speaking to me about an upcoming lesson plan. Why don’t you introduce yourselves?"
    pc "Okay. My name is [playername]."
    "The female student remains silent for a while until Daisy gives her a slight nudge to her shoulder."
    image hari_stage0_6 = "/hari/events/stage0/6.webp"
    scene hari_stage0_6
    unknown "My name is…Hari."
    pc "That’s a pretty name."
    image hari_stage0_7 = "/hari/events/stage0/7.webp"
    scene hari_stage0_7
    "She turns away from you, obviously embarrassed."
    hari "I...I’ve got to go."
    image hari_stage0_8 = "/hari/events/stage0/8.webp"
    scene hari_stage0_8
    "Before you can say anything else, Hari darts out of the room."
    image hari_stage0_9 = "/hari/events/stage0/9.webp"
    scene hari_stage0_9
    teacher "Hmm, that is a bit worrying."
    pc "Did I say something wrong?"
    image hari_stage0_10 = "/hari/events/stage0/10.webp"
    scene hari_stage0_10
    teacher "No. Hari is a little shy is all. It doesn’t help that she’s been struggling with the lessons lately."
    pc "That sounds awful."
    teacher "Yes, but it’s something that can be easily remedied with a change in methods."
    "Recalling the last time that Daisy modified her lesson plan, you can’t help showing the worry on your face."
    teacher "Just trust me that everything will work out. I’ll see you later."
    scene university_leave
    stop music fadeout 1.0
    "Unsure of what Daisy might have planned, you regardless leave the room and head home."

    $ unknownname = 'Unknown'
    $ haristage0event = 0
    return

label Group_Project_start:
    #Scene: Group Project Introduction
    #(NOTE: The following should occur after Hari’s introduction, after Daisy goes through her usual routine on a Monday class.)
    #IMAGE: Daisy standing in front of the classroom.
    call rngteachingscene from _call_rngteachingscene_269
    play music "/music/university.ogg" if_changed
    teacher "Now that we have my measurements out of the way, it’s time that I shake things up for our lesson plan."
    teacher "Starting today, I’ll be offering the choice to participate in group study sessions."
    "An audible groan can be heard going through the room."
    call rngteachingscene from _call_rngteachingscene_270
    teacher "Now don’t be so doom and gloom. I promise that this will give you an extraordinary perspective on our lessons."
    fs "What makes you say that?"
    teacher "Because this will be far different than any other project you’ve done before. The first step will be to get together with your partner."
    call rngteachingscene from _call_rngteachingscene_271
    teacher "From there, you will be required to work together over the next three days to come up with a presentation that you will give to the class on Friday."
    teacher "After the initial project is finished, you are free to work with your partner on future study groups or you can swap out for someone else whenever you like."
    call rngteachingscene from _call_rngteachingscene_272
    teacher "However, the caveat will be that if you pick a new partner, you will have to stick with them for the full week and give a presentation at the end to prove that you’re compatible."
    teacher "That should do for the bulk of the explanation, but I will be more than happy to answer any follow up questions that come up. For now, let’s get started with the assignments."
    call Caroline_Intro4 from _call_Caroline_Intro4
    image hari_stage0_11 = "/hari/events/stage0/11.webp"
    scene hari_stage0_11
    "While the rest of the class already left, you go find your partner."
    "You find Hari sitting in the corner, trying to go unnoticed amidst the activity."
    "Recalling your first interaction with her, you try to move as calmly as possible to avoid scaring her."
    pc "Excuse me, Hari?"
    image hari_stage0_12 = "/hari/events/stage0/12.webp"
    scene hari_stage0_12
    hari "Y-Yes?"
    pc "We’re going to be working in the study sessions together. Is that alright?"
    image hari_stage0_13 = "/hari/events/stage0/13.webp"
    scene hari_stage0_13
    "She pauses for a moment, letting her fingers clench her sweater."
    hari "That sounds…fine."
    pc "Alright then. We’ll get started on the project tomorrow."
    image hari_stage0_14 = "/hari/events/stage0/14.webp"
    scene hari_stage0_14
    hari "Okay."
    "Finishing your awkward introduction with Hari, you head home for the day."
    stop music fadeout 1.0
    if recollection == False:
        $ groupprojectstart = 0
        $ strip = 0
        $ daytime = 2
    return

label Hari_Stage_1_Event_1:
    #Scene: Hari Group Study Session 1
    #(NOTE: The following should occur when the player chooses to do a study session for the first time)
    #IMAGE: Hari sitting at the desk in the study session room
    scene player_room
    "As you make your way to school, the recent change to Daisy's lesson plan still on your mind."
    scene university_outside
    "Thinking out loud to yourself."
    pc "A group project, huh?"
    "Given the already awkward way your school relationship has started with Hari, you hope whatever the assignment is won't add anymore stress for your already meek and shy blonde partner."
    "After all, if you're going to work together you need to be able to at least hold a conversation."
    scene university_looking_into_class2
    "After meeting in Daisy’s class to work out the details and gather supplies, you split off to go to your assigned room for the project."
    image hari_study_arrive_event1 = "/hari/1/study_arrive.webp"
    scene hari_study_arrive_event1
    play music "/music/hari.ogg" if_changed
    "When you arrive, Hari is already waiting there for you."
    image hari_study_sitting2_event1 = "/hari/1/study_sitting2.webp"
    scene hari_study_sitting2_event1
    pc "Hello Hari, how are you?"
    hari "…fine."
    "Though it’s obvious she’s still more than a little uneasy about the situation, you persist and sit down across from her."
    image hari_stage1_1 = "/hari/events/stage1/1.webp"
    scene hari_stage1_1
    pc "Let’s start with going over what we’re supposed to do for our presentation. Is that alright?"
    hari "Y-yes."
    image hari_stage1_2 = "/hari/events/stage1/2.webp"
    scene hari_stage1_2
    "Opening up the study package, you find a piece of paper alongside a selection of different snack foods."
    "Unsurprised by the junk food considering the kind of class Daisy is teaching, you place them across the desk."
    image hari_stage1_3 = "/hari/events/stage1/3.webp"
    scene hari_stage1_3
    hari "What does the paper say we have to do?"
    pc "Let me check. It looks like…we’re doing a snack taste test."
    image hari_stage1_4 = "/hari/events/stage1/4.webp"
    scene hari_stage1_4
    hari "What does that have to do with the project?"
    pc "It’s to gauge the side effects of what they can do to a person’s body."
    hari "I-is that right?"
    pc "Yeah. If you’re not comfortable doing it I can eat the-"
    "You’re cut off as you notice something written on the paper."
    "The assignment specifically calls for Hari to be the one to sample the snacks while you record the results."
    image hari_stage1_5 = "/hari/events/stage1/5.webp"
    scene hari_stage1_5
    "While you’re thinking about how to best tell her the news, she waves to get your attention."
    hari "Well, what does it say?"
    pc "Um, that you have to be the one to eat the snacks."
    image hari_stage1_6 = "/hari/events/stage1/6.webp"
    scene hari_stage1_6
    "Hari recoils in her seat and turns away from you."
    hari "W-why does it have to be me?"
    pc "It doesn’t say. That’s just what Ms. Tanwen has written down on here."
    hari "W-well, can’t you do it? She doesn’t have to know it was me."
    pc "She’s going to expect us to give a presentation on Friday. If you can’t answer her questions, she’s going to find out."
    image hari_stage1_7 = "/hari/events/stage1/7.webp"
    scene hari_stage1_7
    "With a depressed sigh, Hari turns back to you."
    hari "O-okay, what do I need to do?"
    pc "Just start eating and tell me what you think of each of the snacks."
    hari "Okay, I’ll try my best."
    image hari_stage1_8 = "/hari/events/stage1/8.webp"
    scene hari_stage1_8
    "Hesitantly picking out something from the collection of junk food, Hari nibbles away at it with a glacial pace."
    pc "How does it taste?"
    image hari_stage1_9 = "/hari/events/stage1/9.webp"
    scene hari_stage1_9
    hari "Good."
    pc "Just good?"
    hari "I’m sorry. I don’t know how else you want me to describe it."
    pc "We’re going to need to give more than that if we want to pass the…"
    image hari_stage1_10 = "/hari/events/stage1/10.webp"
    scene hari_stage1_10
    "You stop yourself as you see her body shudder. Calming yourself down, you try to speak again."
    pc "I’m sorry. Take as much time as you need."
    image hari_stage1_11 = "/hari/events/stage1/11.webp"
    scene hari_stage1_11
    hari "I-I’ll do my best."
    image hari_stage1_12 = "/hari/events/stage1/12.webp"
    scene hari_stage1_12
    "The rest of the study session is filled with the sound of Hari’s small bites of food and comments that range from describing the snacks from good to fine."
    image hari_stage1_13 = "/hari/events/stage1/13.webp"
    scene hari_stage1_13
    "By the time the session has ended, Hari has barely finished half of the servings. As soon as the bell rings, she’s quick to grab her things and stands up."
    hari "S-sorry, I’ll see you next time."
    image hari_stage1_14 = "/hari/events/stage1/14.webp"
    scene hari_stage1_14
    "Before you have a chance to say goodbye, she rushes out the door."
    "Preparing yourself for an arduous workload of picking up the slack, you clean up the leftover wrappers and head home."
    stop music fadeout 1.0
    if recollection == False:
        $ haristage1event = 0
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Hari_Stage_1_Event_2:
    #Scene: Hari Group Study Session 2
    scene player_room
    "Slightly worried, you make your way down to the university."
    scene university_outside
    "Unsure if you should expect your blonde partner to show up after the events of last time."
    image hari_study_sitting2_event1 = "/hari/1/study_sitting2.webp"
    scene hari_study_sitting2_event1
    play music "/music/hari.ogg" if_changed
    "Returning to the group study room, you’re surprised to see Hari again after the way she ran out the previous day."
    pc "Hello."
    hari "…hi."
    image hari_stage1_15 = "/hari/events/stage1/15.webp"
    scene hari_stage1_15
    "Figuring that you’re not going to get much else out of her, you sit down and prepare the study materials."
    "Opening up the box to put out the snacks, you realize that Daisy’s given you even more than the previous day."
    "Unsure how Hari is going to get through the small feast, regardless you finish putting out the snacks and get your pen ready to write down your observations."
    image hari_stage1_16 = "/hari/events/stage1/16.webp"
    scene hari_stage1_16
    pc "Okay, how does that one taste?"
    hari "It’s…fine, I guess."
    "You suppress your disappointment as you write down the emotionless response."
    "Though you want to give Hari the space she needs to be comfortable, you’re well aware that both of your grades are dependent on this project."
    "Concerned about what failing could mean for your agreement with the university, you decide to try to do something to motivate her."
    pc "Do they really taste that bad?"
    image hari_stage1_17 = "/hari/events/stage1/17.webp"
    scene hari_stage1_17
    "Hari stops eating to stare at you."
    hari "What?"
    pc "Considering how slowly you’re eating; I have to assume that the snacks don’t taste very good."
    pc "If you want, I can tell Ms. Tanwen and try to see if we can get something else."
    image hari_stage1_18 = "/hari/events/stage1/18.webp"
    scene hari_stage1_18
    hari "T-then what would we do with these snacks?"
    pc "I don’t know, probably just throw them out."
    image hari_stage1_19 = "/hari/events/stage1/19.webp"
    scene hari_stage1_19
    hari "No, you don’t have to do that."
    pc "You shouldn’t have to force yourself to eat something that tastes awful."
    pc "That being said, the sooner I can tell Ms. Tanwen, the more time we’ll have to work on a replacement project."
    pc "I just hope that she gives us an extension."
    image hari_stage1_20 = "/hari/events/stage1/20.webp"
    scene hari_stage1_20
    "Leaning across the desk, you reach out to grab the snack from her hands."
    image hari_stage1_21 = "/hari/events/stage1/21.webp"
    scene hari_stage1_21
    "Just before your fingers can touch the cake, Hari shoves it into her mouth and begins to chew."
    image hari_stage1_22 = "/hari/events/stage1/22.webp"
    scene hari_stage1_22
    pc "What was that about?"
    hari "…creamy."
    pc "Excuse me?"
    image hari_stage1_23 = "/hari/events/stage1/23.webp"
    scene hari_stage1_23
    hari "This cake. It has a creamy filling. A-and the texture is very fluffy."
    "Sitting back down in your seat, you begin to take notes."
    pc "What about the others?"
    image hari_stage1_24 = "/hari/events/stage1/24.webp"
    scene hari_stage1_24
    "Hari grabs another and bites down to flood her mouth with raspberry jam."
    image hari_stage1_25 = "/hari/events/stage1/25.webp"
    scene hari_stage1_25
    hari "This one is…really sweet and fruity. Could use a bit of powdered sugar to really perfect it. Is that alright?"
    pc "You’re doing excellent. Keep going."
    image hari_stage1_26 = "/hari/events/stage1/26.webp"
    scene hari_stage1_26
    "Though you do make a lot more progress than the previous day, you still run out of time before Hari can finish off the last of the snacks."
    hari "I’m sorry I couldn’t eat them all."
    pc "That’s okay. We have one more day to prepare for the presentation. I know we can do it."
    hari "If you say so."
    image hari_stage1_27 = "/hari/events/stage1/27.webp"
    scene hari_stage1_27
    "After helping you clean up the leftovers of your study session, Hari leaves the room."
    "Heading out soon after her, you go home thinking about how you’re going to manage to finish the project by Friday."
    stop music fadeout 1.0
    if recollection == False:
        $ haristage1event2 = 0
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Hari_Stage_1_Event_3:
    #Scene: Hari Study Session 3
    image hari_stage1_28 = "/hari/events/stage1/28.webp"
    scene hari_stage1_28
    play music "/music/university.ogg" if_changed
    "You arrive to class to collect the materials for the group study session, only to find them missing."
    pc "Ms. Tanwen, where are the supplies?"
    teacher "Oh, your partner stopped by before class to grab them. She should already be waiting for you in your assigned room."
    "Curious, you walk out into the hall and towards your usual study area. You open up the door to see…"
    image hari_stage1_29 = "/hari/events/stage1/29.webp"
    scene hari_stage1_29
    play music "/music/hari.ogg" if_changed
    "What you find is the bizarre sight of Hari frantically stuffing snacks into her face."
    "She doesn’t stop until you get her attention by clearing your throat."
    image hari_stage1_30 = "/hari/events/stage1/30.webp"
    scene hari_stage1_30
    "Realizing that she’s no longer alone, she freezes and turns her attention towards you."
    hari "Um, how long have you been standing there?"
    pc "I just got here. What are you doing?"
    image hari_stage1_31 = "/hari/events/stage1/31.webp"
    scene hari_stage1_31
    hari "I…thought I’d get an early start to try and make up for the first two days."
    hari "Don’t worry, I’ve already written down my opinions on everything I’ve eaten so far. Are you mad?"
    pc "No, of course not."
    image hari_stage1_32 = "/hari/events/stage1/32.webp"
    scene hari_stage1_32
    "Sitting down across from her, you pick up the worksheet and get ready to take notes."
    pc "Keep going. I’ll be right here to write everything down."
    hari "O-okay. I’ll do my best."
    image hari_stage1_33 = "/hari/events/stage1/33.webp"
    scene hari_stage1_33
    "True to her word, Hari shows off a new level of enthusiasm as she quickly devours each of the snacks."
    image hari_stage1_34 = "/hari/events/stage1/34.webp"
    scene hari_stage1_34
    "In-between her frantic chewing sessions, she’s able to give you detailed reviews of every part of her feast."
    image hari_stage1_35 = "/hari/events/stage1/35.webp"
    scene hari_stage1_35
    "Preoccupied with copying down her observations and being amazed at her unleashed appetite, you fail to notice the moment that Hari finishes off the last snack."
    image hari_stage1_36 = "/hari/events/stage1/36.webp"
    scene hari_stage1_36
    "Swallowing her last mouthful of food, Hari leans back in her seat to catch her breath."
    pc "Good job. This should be more than enough to complete the project."
    image hari_stage1_37 = "/hari/events/stage1/37.webp"
    scene hari_stage1_37
    "Hari hazards to put on a small smile."
    hari "Thank you."
    pc "Now all we have to do it work on the presentation."
    image hari_stage1_38 = "/hari/events/stage1/38.webp"
    scene hari_stage1_38
    hari "T-the presentation?"
    pc "Yeah. Ms. Tanwen did say we would have to report our findings to the class tomorrow."
    image hari_stage1_39 = "/hari/events/stage1/39.webp"
    scene hari_stage1_39
    hari "Tomorrow? Can’t we just hand in a written report?"
    pc "Sorry, but she specified that she wanted it done in front of the entire class."
    image hari_stage1_40 = "/hari/events/stage1/40.webp"
    scene hari_stage1_40
    "She pauses for a moment, looking like there’s a war raging in side of her head."
    hari "Would you…be alright talking to the class? I’m not comfortable with public speaking."
    pc "I’d be more than happy to oblige. Especially since you’ve already put in a lot of work for the project."
    image hari_stage1_41 = "/hari/events/stage1/41.webp"
    scene hari_stage1_41
    "The small smile appears on her face again."
    hari "Thank you."
    "Cleaning up the leftovers of your study session, the two of you head home to prepare for the next day’s presentation."
    stop music fadeout 1.0
    if recollection == False:
        $ haristage1event3 = 0
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Hari_Stage_1_Event_4:
    #Scene: Hari’s First Presentation
    #(NOTE: The following should occur on the Friday of Hari’s study session week, prior to Daisy’s usual, in-class stuffing session.)
    #IMAGE: The classroom with Daisy standing at the front.
    image uni_sexy_teacher_arrive = "/teacher/[teacher.stage]/0/arrive.webp"
    scene uni_sexy_teacher_arrive
    play music "/music/university.ogg" if_changed
    "You arrive to class and take your seat just as Daisy comes in."
    image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
    scene uni_sexy_teacher_greet
    teacher "Good morning, students."
    s "Good morning, Ms. Tanwen."
    call rngteachingscene from _call_rngteachingscene_273
    teacher "Before we begin our usual, Friday lesson plan, we have a pair of students ready to give us a presentation."
    teacher "[playername] and Hari, please come up to the front of the class to show us what you have learned."
    image hari_stage1_42 = "/hari/events/stage1/42.webp"
    scene hari_stage1_42
    "Standing up and walking towards the front, you turn around to see Hari hesitantly trudge her way over to you."
    image hari_stage1_43 = "/hari/events/stage1/43.webp"
    scene hari_stage1_43
    "With her standing at your side, you give her a smile in an attempt to calm her nerves. Turning forward, you address the class."
    image hari_study_presentation1_event1 = "/hari/1/study_presentation1.webp"
    scene hari_study_presentation1_event1
    pc "For our project, we were tasked with trying out a sample of different snacks and recording our thoughts on them."
    pc "For instance, the raspberry fluff cakes were-"
    image hari_stage1_44 = "/hari/events/stage1/44.webp"
    scene hari_stage1_44
    teacher "Pardon me, but who was in charge of the taste testing?"
    pc "Hari."
    teacher "Then don’t you think that she should be the one to tell us about the actual process?"
    pc "Is that really necessary?"
    teacher "If you want to get a good grade it is."
    pc "Ms. Tanwen, please. I’m sure I can handle this on my-"
    image hari_stage1_45 = "/hari/events/stage1/45.webp"
    scene hari_stage1_45
    "Hari stops you by tugging at your sleeve."
    hari "I-it’s okay. I can do it."
    pc "Are you sure?"
    hari "No, but I’ll do my best."
    image hari_stage1_46 = "/hari/events/stage1/46.webp"
    scene hari_stage1_46
    "Taking the center spot, Hari takes a deep breath and begins to speak."
    hari "A-as [playername] was saying, the raspberry fluff cake had a very sweet, satisfying filling that was, um, paired well with the fluffy texture."
    hari "I-in direct contrast, there were the salty pretzels that were, uh, quite savory when they went down my tongue."
    "Hari continues to dryly list off how she feels about every snack food she tried."
    "Though it’s not the most entertaining of presentations, it does the job."
    "She struggles a bit here and there, but your presence seems to give her the confidence she needs to keep on going."
    image hari_stage1_47 = "/hari/events/stage1/47.webp"
    scene hari_stage1_47
    hari "A-and finally there were the chocolate cupcakes. Their, um, rich flavor was perfectly paired with the numerous sprinkles on top."
    hari "…"
    hari "That’s…all for our presentation."
    image hari_stage1_48 = "/hari/events/stage1/48.webp"
    scene hari_stage1_48
    "After giving the class a small bow, Hari attempts to walk back to her desk, only to be stopped by Daisy."
    teacher "Where do you think you’re going, young lady?"
    image hari_stage1_49 = "/hari/events/stage1/49.webp"
    scene hari_stage1_49
    hari "B-back to my seat."
    teacher "You’re not finished yet though. We still need to get your measurements."
    hari "My what?"
    teacher "You spent the last few days eating snacks, so I have to assume that there’s been a change in your body weight."
    teacher "You did remember to write down your initial measurements, correct?"
    hari "Y-yes."
    teacher "Then by all means, please show the class. If you need assistance, I’m sure [playername] can help you out."
    pc "What do you mean?"
    image hari_stage1_50 = "/hari/events/stage1/50.webp"
    scene hari_stage1_50
    "Daisy pulls open a drawer of her desk and hands you a measuring tape."
    teacher "Here you are. You should be able to record her measurements accurately with this."
    pc "Ms. Tanwen, you don’t really expect Hari to-"
    image hari_stage1_51 = "/hari/events/stage1/51.webp"
    scene hari_stage1_51
    hari "I’ll do it."
    pc "Are you sure?"
    hari "Y-yeah. It’s for the class, right?"
    "Though her body is shaking, you see a strange conviction behind her eyes. Not sure what’s gotten into her, you regardless move forward with tape in hand."
    image hari_study_measure_event1 = "/hari/1/study_measure.webp"
    scene hari_study_measure_event1
    window hide
    pause
    "Hari lets out a small yelp as you proceed to start measuring her."
    "Looking between her trembling form and the look on the students’ faces, you wonder how long she’ll be able to last."
    image hari_stage1_52 = "/hari/events/stage1/52.webp"
    scene hari_stage1_52
    "While you consider stopping, you freeze as you notice a nervous smile gradually appears on Hari’s face the longer the session goes on."
    "More than a little confused, you continue to record her measurements."
    $ hari_stats_visible = 1
    image hari_stage1_53 = "/hari/events/stage1/53.webp"
    scene hari_stage1_53
    teacher "Hari, would you kindly tell the class your new measurements?"
    if persistent.imperial:
        $ imperialweight = (hari.weight * 2.2)
        hari "Um, sure. I currently weigh [imperialweight:.02f] lbs. M-my belly is [hari.waist_size:.02f] inches while my…butt is [hari.ass_size:.02f] inches."
    else:
        $ metricwaist_size = (hari.waist_size * 2.54)
        $ metricass_size = (hari.ass_size * 2.54)
        hari "Um, sure. I currently weigh [hari.weight:.02f] kg. M-my belly is [metricwaist_size:.02f] cm while my…butt is [metricass_size:.02f] cm."
    image hari_stage1_54 = "/hari/events/stage1/54.webp"
    scene hari_stage1_54
    teacher "And what about your cup size."
    hari "It’s a…[hari.breast_cup] cup."
    image hari_stage1_55 = "/hari/events/stage1/55.webp"
    scene hari_stage1_55
    teacher "Most excellent. [playername], make sure you get all of this down in-case you need it for a future project."
    "Hari has been added to the stats screen."
    hari "M-ms. Tanwen, am I done now?"
    teacher "Yes, you may return to your seat. You did an excellent job. Perfect scores for the both of you."
    image hari_stage1_56 = "/hari/events/stage1/56.webp"
    scene hari_stage1_56
    "Hari once more puts on her small smile."
    hari "Thank you."
    image hari_stage1_57 = "/hari/events/stage1/57.webp"
    scene hari_stage1_57
    "Watching Hari quickly shuffle back to her seat, you return to your desk for the rest of class."

    #(NOTE: The regular Friday class should continue from here. The following should play out just as the player is leaving the classroom.)
    call rngteachingscene from _call_rngteachingscene_274
    teacher "Let me free up my belly and we can get started on today’s feeding session."
    $ strip += 1
    window hide
    pause
    $ strip += 1
    pause
    $ strip += 1
    pause
    $ strip += 1
    pause
    teacher "Let’s see what you’ve brought me to eat over the weekend."
    image uni_sexy_teacher_food_teaching1 = "/teacher/[teacher.stage]/[strip]/food_teaching1.webp"
    scene uni_sexy_teacher_food_teaching1
    teacher "So many great choices! Since I consider Friday as part of the weekend, I’ll start eating a little bit of this."
    teacher "What should I start with?"
    call foodchoice from _call_foodchoice_4
    image uni_sexy_teacher_food_teaching2 = "/teacher/[teacher.stage]/[strip]/food_teaching2.webp"
    scene uni_sexy_teacher_food_teaching2
    teacher "Pretty good. What’s next?"
    call foodchoice from _call_foodchoice_5
    image uni_sexy_teacher_stuffed_half = "/teacher/[teacher.stage]/[strip]/stuffed_half.webp"
    scene uni_sexy_teacher_stuffed_half
    teacher "Feeling a little bloated, but I can keep going. Are there any other requests?"
    call foodchoice from _call_foodchoice_6
    image uni_sexy_teacher_stuffed = "/teacher/[teacher.stage]/[strip]/stuffed.webp"
    scene uni_sexy_teacher_stuffed
    teacher "That’ll do it for me. I’ll finish off the rest of this over the weekend. See you all Monday!"

    "Just as you’re about to step out into the hall, you feel a familiar tug at your sleeve."
    image hari_stage1_58 = "/hari/events/stage1/58.webp"
    scene hari_stage1_58
    hari "Thank you for helping me out earlier. It was really nice working with you."
    pc "No, thank you. You did most of the hard work. I’m hoping we can team up again sometime."
    image hari_stage1_59 = "/hari/events/stage1/59.webp"
    scene hari_stage1_59
    hari "Do…do you mean it?"
    pc "Of course."
    image hari_stage1_60 = "/hari/events/stage1/60.webp"
    scene hari_stage1_60
    "Smiling once more, Hari comes in for a quick, yet friendly hug."
    window hide
    pause
    image hari_stage1_61 = "/hari/events/stage1/61.webp"
    scene hari_stage1_61
    "Before you can ask any further questions, she runs off down the hall to avoid an awkward conversation."
    "Shrugging your shoulders knowing that’s just how she is, you head home for the day."
    stop music fadeout 1.0
    if recollection == False:
        $ haristage1event4 = 0
        $ hari.weight += 2
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Hari_Stage_1_Event_5:
    #Scene: First Post-Presentation Study Session
    image hari_study_arrive_event1 = "/hari/1/study_arrive.webp"
    scene hari_study_arrive_event1
    play music "/music/hari.ogg" if_changed
    "Picking up another package of junk food from Daisy, you arrive to find Hari sitting in the study room."
    pc "Hello Hari."
    image hari_study_sitting_event1 = "/hari/1/study_sitting.webp"
    scene hari_study_sitting_event1
    "For the first time, she greets you with an excited smile."
    hari "Hello [playername]. It’s good to see you again."
    image hari_stage1_62 = "/hari/events/stage1/62.webp"
    scene hari_stage1_62
    "Taking your seat across from her, you start to put out the study materials."
    pc "You seem a bit more eager today."
    image hari_stage1_63 = "/hari/events/stage1/63.webp"
    scene hari_stage1_63
    hari "I guess…it has to do with that presentation. I’ve never really been comfortable with speaking in front of people in the past."
    pc "What made our presentation so different?"
    hari "I’m not entirely sure. Maybe…I just felt strangely comfortable talking about my body like that. Or maybe…it was because you were there."
    image hari_stage1_64 = "/hari/events/stage1/64.webp"
    scene hari_stage1_64
    "Moments after the words leave her mouth, Hari recoils back into her seat."
    hari "S-sorry. I didn’t mean to make things awkward like that."
    pc "It’s alright. I enjoyed working with you too."
    hari "T-thank you. Um, let’s get along with today’s study materials."
    image hari_study_eat1_event1 = "/hari/1/study_eat1.webp"
    scene hari_study_eat1_event1
    "Perhaps to avoid further conversation, Hari rips into the collection of snacks."
    image hari_stage1_65 = "/hari/events/stage1/65.webp"
    scene hari_stage1_65
    "So engrossed with stuffing her face, her words are a mess as she tries to describe each flavor."
    "Though it’s a bit of a struggle, you do manage to write down her notes after a few clarification questions."
    image hari_stage1_66 = "/hari/events/stage1/66.webp"
    scene hari_stage1_66
    "Cleaning up after yourselves, you and Hari begin to leave."
    hari "It was, um, nice working with you again. See you later."
    pc "Later."
    stop music fadeout 1.0
    #IMAGE: Empty study room.
    #"Just as you’re about to leave, you notice a stray wrapper on the ground that you missed. As you crouch down to pick it up, you notice something shiny nearby."
    #IMAGE: Cutie Card Clash rare card
    #"Picking up the card in your hand, you see the depiction of a cute animal."
    #"While you can’t make out what the various numbers and terms on the card mean, you see the name “Cutie Card Clash” printed on the back."
    #"Curious if someone might have dropped it, you stick it in your pocket for safe keeping and head home."


    #Scene: Hari Card Return
    #(NOTE: The following should occur the next time the player has a study session with Hari after the previous, stage 2 event)
    #IMAGE: Hari slouched in her seat in the study room.
    #"You arrive to the study room to find Hari, slouched in her seat."
    #"Her usual nervousness has been replaced with a more melancholic mood as you notice her eyes continue to survey the ground below."
    #pc "Hello Hari."
    #IMAGE: Hari looking up at the player.
    #hari "Oh…hi."
    #pc "Is everything okay?"
    #hari "Um, yeah. It’s fine. Nothing you have to worry about."
    #IMAGE: The player sitting across from Hari in the study room.
    #"Not believing Hari for a second, you sit down across from her."
    #pc "If something is bothering you, then you can tell me. We can’t really work together if we don’t help each other out every now and then."
    #"It takes a few moments of fidgeting with her fingers before Hari replies."
    #hari "I…lost something a while back. I was hoping I would be able to find it in here since it’s the last place I saw it, but there’s no trace of it."
    #"Recalling what you found earlier, you pull out the card and hold it up."
    #pc "Is this what you’re talking about?"
    #IMAGE: Happy Hari holding onto the card.
    #"Letting out a gasp, Hari reaches out to take the card from you."
    #hari "Yes, this is it! Where did you find it?"
    #pc "I found it on the floor after our last study session. Is it important?"
    #hari "Yes. It’s a very rare card. It comes from a limited set of booster packs. The odds of pulling it are one in…"
    #IMAGE: Sad Hari holding onto the card.
    #"Hari trails off as she seems to remember something."
    #hari "It’s nothing special. You don’t have to worry about it. It’s just some dumb hobby of mine."
    #pc "I would like to hear about it. The card looks pretty interesting."
    #IMAGE: Hari looking at the player.
    #hari "R-really?"
    #pc "Yeah."
    #hari "Um, okay. Well you see the game works like this."
    #IMAGE: Hair excitedly talking to the player.
    #"Though she’s still a bit nervous at first, Hari picks up the pace of her speech the further she goes into detail."
    #"While you do lose track of what she’s saying amidst the different rules, you try to remain patient with her and listen."
    #"You come out of the explanation still unsure what the card game is, but you are happy to see Hari being so forward with her interests."
    #hari "And that’s the basics of it. What do you think?"
    #pc "You’re pretty knowledgeable about this stuff. You must have been playing the game for a long time."
    #IMAGE: Sad Hari looking down at the desk.
    #hari "I was…but I gave it up long ago. That card you saw was from a booster pack I bought on a whim after the presentation."
    #hari "I got caught up by the excitement and felt like treating myself."
    #pc "There’s nothing wrong with that. You’re allowed to like what you like."
    #IMAGE: Happy Hari staring at the player.
    #hari "Thank you. Would you like for me to go into more detail about the card game?"
    #pc "Er, maybe we should save that for another time. For now, we should probably focus on the study session."
    #hari "Right. Let’s get to it."
    #"Rushing through your study session with Hari, you managed to finish the assignment just in time before you head home."
    if recollection == False:
        $ hari_study_times += 1
        $ hari.weight += 0.2
        $ haristage1event5 = 0
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Hari_Stage_2_Event_1:
    #Scene: Hari Asks for a Date
    #(NOTE: The following should occur shortly after the player reaches Hari stage 2 and they choose to do a study session with her.)
    image hari_study_sitting2_event2 = "/hari/2/study_sitting2.webp"
    scene hari_study_sitting2_event2
    play music "/music/hari.ogg" if_changed
    pc "Hey Hari."
    hari "Um, hello [playername]. How are you?"
    pc "I’m alright, but it’s you I’m worried about. You look more nervous than usual."
    image hari_stage2_1 = "/hari/events/stage2/1.webp"
    scene hari_stage2_1
    hari "Y-yes I’m doing just fine. Nothing to worry about. Let’s, uh, just focus on our work for today."
    image hari_study_eat1_event2 = "/hari/2/study_eat1.webp"
    scene hari_study_eat1_event2
    "Rather than question Hari’s extra odd behavior, you set to work recording her thoughts as she goes through the day’s snacks."
    image hari_stage2_2 = "/hari/events/stage2/2.webp"
    scene hari_stage2_2
    "Every so often, you catch her glancing at you with the same, nervous expression."
    "Though you want to ask her about why she’s acting like this, her speech is limited to her opinions on the various foods and loud chewing noises."
    image hari_stage2_3 = "/hari/events/stage2/3.webp"
    scene hari_stage2_3
    "Finishing up with the day’s lesson and cleaning up the resulting wrappers, you get up to leave."
    hari "Hold on. There’s…something I wanted to talk to you about."
    pc "What’s that? Is it something to do with the lesson?"
    hari "No I…"
    image hari_stage2_4 = "/hari/events/stage2/4.webp"
    scene hari_stage2_4
    "She pauses for a moment, tapping her fingers against the desk as she tries to build up the confidence to speak her mind."
    hari "Would you like to…go out to eat with me?"
    pc "Like a date?"
    image hari_stage2_5 = "/hari/events/stage2/5.webp"
    scene hari_stage2_5
    "Your response makes her understandably flustered."
    hari "N-no. It’s, um, more of a way to…study other foods for class. Do you think we could go sometime?"
    pc "I don’t see why not."
    image hari_stage2_6 = "/hari/events/stage2/6.webp"
    scene hari_stage2_6
    hari "That’s…great. Message me whenever you’re free to go."
    image hari_stage2_7 = "/hari/events/stage2/7.webp"
    scene hari_stage2_7
    "Hari leaves the room in a mad dash, fueled by her own embarrassment."
    "Still trying to figure out what she’s trying to do, you regardless make a mental note to contact her after class one day to take her up on the offer."
    stop music fadeout 1.0
    #(NOTE: After this scene, the option, Take Hari Out to Eat should appear whenever the player is in their room.)
    if recollection == False:
        $ hari_study_times += 1
        $ hari.weight += 0.2
        $ haristage2event = 0
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Hari_Stage_2_Event_2:
    #Scene: Hari Bunny Bites Date
    #(NOTE: The following should occur once the player picks the Take Hari Out to Eat Option)
    #IMAGE: The player’s room.
    "You decide that now’s a good time to message Hari about hanging out."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Hari', dialogue=dialogue_one)
    $ msg ("Did you still want to meet up somewhere to eat?")
    pause
    $ msg ("Yes.", who=1)
    pause
    $ msg ("Did you have anywhere specific in mind?")
    pause
    $ msg ("No.", who=1)
    pause
    $ msg ("Alright, how about you tell me what kind of food you’re looking for? That’ll make the decision easier.")
    pause
    $ msg ("Maybe someplace where I can eat something that doesn’t cost too much that will really fill us up?", who=1)
    pause
    $ msg ("What about Bunny Bites?")
    pause
    $ msg ("What’s that?", who=1)
    pause
    $ msg ("It’s a pretty popular diner in town.")
    pause
    $ msg ("With a lot of people?", who=1)
    pause
    $ msg ("I don’t think we have to worry too much about that. They’re pretty slow this time of day.")
    pause
    $ msg ("Okay. If you say so. I’ll meet you there.", who=1)
    pause
    $ hide_messenger()

    image hari_stage2_8 = "/hari/events/stage2/8.webp"
    scene hari_stage2_8
    play music "/music/bunny_bites.ogg" if_changed
    "Arriving at Bunny Bites you walk in with Hari and sit down."
    image hari_stage2_9 = "/hari/events/stage2/9.webp"
    scene hari_stage2_9
    "While you get settled and look over the menu, you notice that she keeps darting her eyes back and forth across the diner."
    pc "Is everything okay?"
    image hari_stage2_10 = "/hari/events/stage2/10.webp"
    scene hari_stage2_10
    hari "This is supposed to be the least busy time of day? It’s still pretty crowded."
    pc "Do other people really make you that uncomfortable?"
    hari "A little, yes."
    pc "You have nothing to worry about. Everyone here is pretty nice. Not to mention the food is-"
    image cafe_marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene cafe_marie_serving2
    "While you’re speaking, one of the waitresses walks up to the table."
    marie "Hi and welcome to Bunny Bites. What can I get you?"
    pc "Oh, I’ll just have a soda and a slice of pizza."
    marie "Okay. And what can I get you miss?"
    image hari_stage2_11 = "/hari/events/stage2/11.webp"
    scene hari_stage2_11
    "For a moment Hari looks like a deer caught in the headlights."
    image hari_stage2_12 = "/hari/events/stage2/12.webp"
    scene hari_stage2_12
    "She eventually raises a shaky finger and points it towards something on the menu."
    image cafe_marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene cafe_marie_serving2
    marie "Are you sure that’s what you want?"
    image hari_stage2_13 = "/hari/events/stage2/13.webp"
    scene hari_stage2_13
    hari "Y-yes."
    "After responding, Hari quickly hands her menu over to the waitress without a second glance."
    image cafe_marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene cafe_marie_serving2
    marie "You must be pretty hungry. Alright, I’ll be back shortly with your food."
    image hari_stage2_14 = "/hari/events/stage2/14.webp"
    scene hari_stage2_14
    pc "Are you sure you’re okay?"
    image hari_stage2_15 = "/hari/events/stage2/15.webp"
    scene hari_stage2_15
    hari "Not really. Like I said, I’m not the best when it comes to talking to other people."
    pc "That was just one server. How is that different from when you did the presentation back in class?"
    hari "I don’t know. My body just kind of freezes up when I’m put on the spot like that. I’m sorry."
    pc "It’s fine. You don’t need to force yourself. Although do you even know what you ordered?"
    image hari_stage2_16 = "/hari/events/stage2/16.webp"
    scene hari_stage2_16
    hari "…no."
    pc "That’s okay. I’ve been here enough times to know that most of their food is good."
    pc "This is actually where I got those chicken nuggets for Ms. Tanwen’s class feeding."
    image hari_stage2_17 = "/hari/events/stage2/17.webp"
    scene hari_stage2_17
    hari "Those did look pretty tasty. I’ll trust you then."
    "Though you try to pass the time with conversation, Hari seems just as shy as ever."
    image hari_stage2_18 = "/hari/events/stage2/18.webp"
    scene hari_stage2_18
    "She does try to listen to you, but she can’t help looking over her shoulder every so often as if she’s under the impression that she’s being spied on."
    image hari_stage2_19 = "/hari/events/stage2/19.webp"
    scene hari_stage2_19
    "Her expression changes to one of shock as she notices something coming up from behind you."
    image hari_stage2_20 = "/hari/events/stage2/20.webp"
    scene hari_stage2_20
    "While you’re given your conservative meal, you watch with a same level of awe as Hari as she’s given a massive platter of food."
    image cafe_marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene cafe_marie_serving2
    marie "I hope you enjoy. We haven’t had someone order the Glutton Gorger meal in a while. If you can’t finish it, just let me know and I’ll get you some to go boxes."
    image hari_stage2_20 = "/hari/events/stage2/20.webp"
    scene hari_stage2_20
    "The waitress departs, leaving you alone with Hari and the massive spread of food."
    pc "If you don’t want to eat all of this, we can send it back."
    image hari_stage2_21 = "/hari/events/stage2/21.webp"
    scene hari_stage2_21
    hari "No! We can’t do that. They probably worked really hard on this."
    pc "It’s really no big deal. Besides, do you really think you’ll be able to eat all of that?"
    image hari_stage2_22 = "/hari/events/stage2/22.webp"
    scene hari_stage2_22
    "Hari goes silent again as she stares down at her food. After a few moments of internal debate, she begins to dig in."
    image hari_stage2_23 = "/hari/events/stage2/23.webp"
    scene hari_stage2_23
    "You watch as Hari sinks her teeth into the food for an experimental bite. The small nibble turns into something a bit more unhinged once she gets to taste the meal."
    image hari_stage2_24 = "/hari/events/stage2/24.webp"
    scene hari_stage2_24
    "Whether it’s to avoid the awkward conversation with the servers or just because she really is that hungry, she goes at the feast with reckless abandon."
    image hari_stage2_25 = "/hari/events/stage2/25.webp"
    scene hari_stage2_25
    "Entranced by the sight of her frantic eating, you barely even touch your own food."
    image hari_stage2_26 = "/hari/events/stage2/26.webp"
    scene hari_stage2_26
    "Though Hari’s efforts are commendable, she eventually reaches her breaking point. Dropping the food on the table, she leans back to nurse her overstuffed belly."
    pc "Are you okay?"
    image hari_stage2_27 = "/hari/events/stage2/27.webp"
    scene hari_stage2_27
    hari "Y-yeah. I think I just ate too much. I’m sorry if I made a scene."
    pc "It was actually pretty impressive seeing you eat like that."
    image hari_stage2_28 = "/hari/events/stage2/28.webp"
    scene hari_stage2_28
    "The comment seems to do the trick in bringing a smile to her face."
    hari "Thank you."
    pc "I’ll talk to the server and get the rest boxed up for you."
    hari "I appreciate it. I’ll pay the bill. It only feels right considering how much I ordered."
    pc "Only if you promise you’ll let me buy the next time we do this."
    image hari_stage2_29 = "/hari/events/stage2/29.webp"
    scene hari_stage2_29
    hari "Next time?"
    pc "Yeah. That is, if you want to come here again."
    hari "I’ll…think about it."
    image hari_stage2_30 = "/hari/events/stage2/30.webp"
    scene hari_stage2_30
    "With her vague committal to future plans made, you aid her in packing up the food before you go your separate ways."
    stop music fadeout 1.0

    scene player_room
    "You receive a message. It’s Hari."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Hari', dialogue=dialogue_one)
    $ msg ("Thank you for tonight. I had a really nice time.", who=1)
    pause
    $ msg ("Me too. I’m glad you enjoyed yourself.")
    pause
    $ msg ("I did. I was nervous at first, but it was… nice. I’m looking forward to our next time.", who=1)
    "A short pause, then another message pops up."
    $ msg ("Maybe somewhere quieter next time. That would be more comfortable.", who=1)
    pause
    $ hide_messenger()

    $ haristage2event2 = 0
    if recollection == False:
        $ hari.weight += 1
        $ daytime += 1
        jump freetime
    return



label Hari_Stage_3_Event_1:
    #Scene: Stage 3 Casual Conversation
    #(NOTE: The following should occur when the player chooses a study session with Hari after reaching stage 3 with her)
    image hari_stage3_1 = "/hari/events/stage3/1.webp"
    scene hari_stage3_1
    play music "/music/hari.ogg" if_changed
    "You arrive at the study room after collecting an unusually small amount of snacks from Daisy."
    hari "Is that all?"
    pc "Yeah, guess Ms. Tanwen must have run out or something."
    hari "Well, I suppose that will make the assignment easier."
    image hari_stage3_2 = "/hari/events/stage3/2.webp"
    scene hari_stage3_2
    "While the assignment doesn’t take long to complete, that also means that you and Hari are left sitting alone without much to talk about once she’s done with the small spread of junk food."
    image hari_stage3_3 = "/hari/events/stage3/3.webp"
    scene hari_stage3_3
    "Desperate to find something to talk about, you bring up the first thing that comes to mind."
    pc "Back at Bunny Bites, it was really incredible how you managed to eat all of that food."
    image hari_stage3_4 = "/hari/events/stage3/4.webp"
    scene hari_stage3_4
    pc "Have you always been able to do stuff like that?"
    "Her expression doesn’t seem to warrant an answer as you’re left to simmer in your own poor choice."
    pc "I’m sorry. I didn’t mean to say something to offend you."
    image hari_stage3_5 = "/hari/events/stage3/5.webp"
    scene hari_stage3_5
    hari "It’s fine, really. I-I’m sure it’s not every day that you see a woman eat like that. Well, besides Ms. Tanwen I guess."
    "You decide its best for now not to mention the obvious exceptions."
    image hari_stage3_6 = "/hari/events/stage3/6.webp"
    scene hari_stage3_6
    hari "To be honest, I’ve always had that kind of appetite. Especially when I was younger. I just… haven’t felt comfortable binging like that in a long time."
    pc "Why’s that?"
    image hari_stage3_7 = "/hari/events/stage3/7.webp"
    scene hari_stage3_7
    "Hari remains silent, clearly not comfortable going into detail."
    pc "I guess I’ve asked too many questions. Tell you what, how about you ask me something?"
    image hari_stage3_8 = "/hari/events/stage3/8.webp"
    scene hari_stage3_8
    hari "Anything?"
    "You nod your head, although you can’t help feeling a bit of regret as you do it."
    hari "Okay, then. Um, you seem pretty close with Ms.Tanwen. Is there…something going on between the two of you?"
    #CHOICE: A) I’m one of her favorite students or B) We’re friends
    menu:
        "I’m one of her favorite students.":
            image hari_stage3_9 = "/hari/events/stage3/9.webp"
            scene hari_stage3_9
            hari "Really?"
            pc "Yeah. I think she keeps giving me extra assignments just because she wants to see how far I can go."
            hari "You do seem to know a lot about nutrition. It’s been a big help with the projects."
            image hari_stage3_10 = "/hari/events/stage3/10.webp"
            scene hari_stage3_10
            hari "But is that really all that’s going on? Are the two of you…you know-"
        "We’re friends.":
            image hari_stage3_9 = "/hari/events/stage3/9.webp"
            scene hari_stage3_9
            hari "Really?"
            pc "Yeah. We sometimes meet up with each other after class."
            hari "I see…"
            "Hari clenches her fingers for a moment."
            image hari_stage3_10 = "/hari/events/stage3/10.webp"
            scene hari_stage3_10
            hari "You’re free to do what you want. You’re both adults at the end of the day after all. That being the case, are you and Ms. Tanwen-"
    #(NOTE: Regardless of the player’s choice, the following should play out.)
    image hari_stage3_11 = "/hari/events/stage3/11.webp"
    scene hari_stage3_11
    "Hari’s uncomfortable question is interrupted by the ring of the bell."
    pc "I guess that’s our signal to leave."
    image hari_stage3_12 = "/hari/events/stage3/12.webp"
    scene hari_stage3_12
    hari "Right, right. I’ll talk to you later."
    "Before Hari has a chance to ask anything else, you rush out of the room and head home."
    stop music fadeout 1.0
    if recollection == False:
        $ hari_study_times += 1
        $ haristage3event = 0
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Hari_Stage_3_Event_2:
    #Scene: Risqué Lingerie Reveal
    #(NOTE: The following should occur when the player does a study session with Hari after she reaches stage 3)
    image hari_stage3_13 = "/hari/events/stage3/13.webp"
    scene hari_stage3_13
    play music "/music/hari.ogg" if_changed
    "Upon arriving to the study room, you see that Hari is already there."
    "While you typically find her sitting patiently for the session to begin, you can’t help noticing how she squirms in her seat."
    "You get her attention by clearing your throat."
    image hari_stage3_14 = "/hari/events/stage3/14.webp"
    scene hari_stage3_14
    "Hari lets out a yelp once she notices your presence."
    pc "Sorry, I didn’t mean to scare you. Is everything okay?"
    image hari_stage3_15 = "/hari/events/stage3/15.webp"
    scene hari_stage3_15
    hari "Y-yeah, I’m fine. Let’s get started on today’s assignment."
    pc "If something’s bothering you, there’s no issue with telling me."
    hari "Nothing is wrong, really. Let’s just…get to work on the assignment."
    image hari_stage3_16 = "/hari/events/stage3/16.webp"
    scene hari_stage3_16
    "Heeding her request, you unbox the first few snacks and hand them over to her."
    image hari_stage3_17 = "/hari/events/stage3/17.webp"
    scene hari_stage3_17
    "As she consumes the junk food, you begin to notice that her once baggy clothing is a little bit tighter around her body."
    image hari_stage3_18 = "/hari/events/stage3/18.webp"
    scene hari_stage3_18
    "Thinking about how much she’s been binge eating in and outside of class, you’re not surprised. Although you do question how she’s able to keep going."
    image hari_stage3_19 = "/hari/events/stage3/19.webp"
    scene hari_stage3_19
    "A ripping noise makes both you and Hari freeze."
    pc "Hari, what was that?"
    hari "N-nothing. I think I just need to take a break from eating to-"
    "Another sound of fabric tearing is heard."
    image hari_stage3_20 = "/hari/events/stage3/20.webp"
    scene hari_stage3_20
    hari "That was, um, my backpack. It’s been through a lot lately. I-I’ve been meaning to get a new one for a while and-"
    image hari_stage3_21 = "/hari/events/stage3/21.webp"
    scene hari_stage3_21
    "In an instant, Hari’s sweater tears apart. Bracing yourself against the pieces of fabric as they are flung across the room, you look back to see an uncharacteristic skimpy bra hugging Hari’s breasts."
    pc "Hari, what are you wearing?"
    image hari_stage3_22 = "/hari/events/stage3/22.webp"
    scene hari_stage3_22
    hari "I-it’s um, um…I’ve got to go."
    "In a rush to get out of the room, Hari adds to her torment as more tears echo through the room."
    image hari_stage3_23 = "/hari/events/stage3/23.webp"
    scene hari_stage3_23
    "Following in the wake of the destruction of Hari’s pants, you’re given a good look at her matching pair of panties."
    image hari_stage3_24 = "/hari/events/stage3/24.webp"
    scene hari_stage3_24
    play music "/music/sadness.ogg" if_changed
    "No longer obscured, her body is exposed to show off the bits of chub that are the assumed suspects for her clothing malfunction."
    "Though Hari begins to tear up, she remains standing there, trying and failing to be as still as a statue as nervous shudders take over her body."
    pc "Are you okay?"
    image hari_stage3_25 = "/hari/events/stage3/25.webp"
    scene hari_stage3_25
    hari "N-no."
    pc "What happened?"
    image hari_stage3_26 = "/hari/events/stage3/26.webp"
    scene hari_stage3_26
    "Hari pauses to let the tears flow down her cheeks."
    hari "I’m so stupid. I should have known that this would happen if I kept stuffing myself like a pig. Why didn’t I stop myself?"
    pc "Hey, don’t beat yourself up about it. I’m just as much to blame for pushing you to keep eating."
    image hari_stage3_27 = "/hari/events/stage3/27.webp"
    scene hari_stage3_27
    hari "You don’t understand, this is the way I used to be. I’m the only one at fault. You must think I’m some kind of freak."
    pc "I don’t think that at all."
    image hari_stage3_28 = "/hari/events/stage3/28.webp"
    scene hari_stage3_28
    "Hari continues to softly sob, unconvinced by your words."
    pc "Hang on. Let me see if I can find something to cover you up."
    "Searching through the room, you eventually stumble on a closet filled with blankets."
    "Though you suspect that Daisy might have purposefully planted them here for this kind of occasion, you regardless bring one of them over to Hari."
    pc "Here, this should do until we can find something else."
    image hari_stage3_29 = "/hari/events/stage3/29.webp"
    scene hari_stage3_29
    "Hari begrudgingly accepts the blanket and wraps it around her body."
    hari "Thank you."
    pc "You know, if you’re that worried about your body, I think there’s a gym in town that’s free to use for students."
    hari "But what if someone sees me?"
    pc "You have nothing to worry about. I’m sure everyone is there for the same reason of wanting to stay in shape. There’s no shame in that."
    hari "Would you… go there with me sometime?"
    pc "You can count on it."
    image hari_stage3_30 = "/hari/events/stage3/30.webp"
    scene hari_stage3_30
    "A small smile breaks through Hari’s worry."
    hari "I would appreciate that."
    pc "So what do we do now?"
    image hari_stage3_31 = "/hari/events/stage3/31.webp"
    scene hari_stage3_31
    hari "I left a change of clothes back in my car. I’ll try to sneak over and grab them while everyone else is in class and then change in the bathroom."
    pc "Best of luck to you."
    image hari_stage3_32 = "/hari/events/stage3/32.webp"
    scene hari_stage3_32
    hari "I’ll do my best."
    image hari_stage3_33 = "/hari/events/stage3/33.webp"
    scene hari_stage3_33
    "Helping Hari sneak out of the room; you return to clean up the leftover boxes and shredded clothes."
    "While you tidy up, you can’t help wondering why someone like Hari would wear such skimpy undergarments."
    "Thinking of how difficult it could be to try and get an answer from her, you refocus yourself on the task at hand so that you can leave the room spotless before heading home."
    stop music fadeout 1.0
    if recollection == False:
        $ hari_study_times += 1
        $ hari.weight += 1
        $ haristage3event2 = 0
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Hari_Stage_4_Event_1:
    #Scene: Hari Gym Visit
    #(NOTE: The following should occur when the player is in their room after reaching Hari stage 4)
    #IMAGE: The player’s room.
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Hari', dialogue=dialogue_one)
    $ msg ("Sorry to bother you, but could you help me with something? I was thinking about what you said the other day. I think I’m ready to start going to the gym. Do you think you could join me for my first visit?", who=1)
    pause
    #CHOICE: A) Sorry, I have other plans or B) Sure, I’ll meet you there.
    menu:
        "Sure, I’ll meet you there.":
            $ msg ("Sure, I’ll meet you there.")
            pause
            $ msg ("Thank you. See you soon.", who=1)
            pause
            $ hide_messenger()
        "Sorry, I have other plans.":
            $ msg ("Sorry, I have other plans.")
            pause
            $ msg ("That’s okay. Sorry to bother you. We can go together some other time.", who=1)
            pause
            $ hide_messenger()
            #(NOTE: If the player chooses this option, Hari will message them each following day until they choose option B)
            return

    image hari_stage4_1 = "/hari/events/stage4/1.webp"
    scene hari_stage4_1
    play music "/music/gym.ogg" if_changed
    "Changing into your workout clothes, you head over to the gym. When you arrive, you find Hari nervously standing by herself."
    hari "Thank you for coming."
    pc "Anything for a friend. Did you have an idea of where you wanted to start?"
    image hari_stage4_2 = "/hari/events/stage4/2.webp"
    scene hari_stage4_2
    hari "Not really. I was hoping that you could suggest something for me."
    pc "I don’t know. Was there any kind of physical activity that you liked to do as a kid?"
    image hari_stage4_3 = "/hari/events/stage4/3.webp"
    scene hari_stage4_3
    "Hari takes her time trying to come up with an answer. While you wait, you notice her eyes shift to focus on the mat in the center."
    pc "Do you want to do some gymnastics?"
    image hari_stage4_4 = "/hari/events/stage4/4.webp"
    scene hari_stage4_4
    hari "Um, well, I did do a little bit when I was younger."
    pc "That sounds perfect."
    hari "Not exactly. I’m still unsure if I want to do anything in front of so many people."
    image hari_stage4_5 = "/hari/events/stage4/5.webp"
    scene hari_stage4_5
    "Turning away from Hari, the only people you see are a couple of women running on the treadmills at a snail’s pace as they watch movies on their phones."
    image hari_stage4_6 = "/hari/events/stage4/6.webp"
    scene hari_stage4_6
    pc "It will be fine, trust me. I’ll be with you every step of the way."
    hari "Alright, if you say so."
    image hari_stage4_7 = "/hari/events/stage4/7.webp"
    scene hari_stage4_7
    "Hari walks onto the mat and waits."
    hari "What should I do first?"
    pc "It’s your exercise regimen, so start with whatever feels natural to you."
    hari "Okay. I think I remember a short routine my old coach taught me."
    image hari_stage4_8 = "/hari/events/stage4/8.webp"
    scene hari_stage4_8
    "Taking a deep breath, Hari begins to stretch out her limbs to get ready for her session."
    image hari_stage4_9 = "/hari/events/stage4/9.webp"
    scene hari_stage4_9
    window hide
    pause
    image hari_stage4_10 = "/hari/events/stage4/10.webp"
    scene hari_stage4_10
    "For the first time, you notice how flexible she seems to be."
    image hari_stage4_11 = "/hari/events/stage4/11.webp"
    scene hari_stage4_11
    hari "How do I look?"
    pc "Impressive. I didn’t think you could move your body like that."
    image hari_stage4_12 = "/hari/events/stage4/12.webp"
    scene hari_stage4_12
    "Your comment seems to trigger a smile on her face."
    hari "This is actually just the start. Here, let me show you something a bit more involved."
    image hari_stage4_13 = "/hari/events/stage4/13.webp"
    scene hari_stage4_13
    "Getting a running start, Hari leaps towards the ground. Just as it looks like she’s about to fall, she instead stands herself up on her hands."
    image hari_stage4_14 = "/hari/events/stage4/14.webp"
    scene hari_stage4_14
    "She remains like that for a few seconds, using the time to stretch out her legs to show off. When she finally decides to finish and tumble back down, you can’t help from clapping in applause."
    image hari_stage4_15 = "/hari/events/stage4/15.webp"
    scene hari_stage4_15
    pc "That was amazing."
    "A blush forms on her face, yet you see a smile in replacement of her usual, anxious expression."
    hari "Really? It wasn't anything that special. Most of the kids in my class could do it."
    pc "Don’t sell yourself so short. That was an impressive feat."
    hari "Thank you."
    image hari_stage4_16 = "/hari/events/stage4/16.webp"
    scene hari_stage4_16
    "Hari’s elated expression lasts up until she notices the ladies from before turning towards her."
    hari "Um, would it be alright if we ended the session early? I think I’ve had enough for today."
    pc "Okay. Did you want to do anything else?"
    image hari_stage4_17 = "/hari/events/stage4/17.webp"
    scene hari_stage4_17
    "Hari fidgets with her fingers for a bit."
    hari "Maybe we could…go back to my place and watch a movie? It might be a nice break for our bodies after exercising."
    "While neither of you have worked up a sweat, you can tell that Hari is eager to leave."
    pc "Okay then. Let me get changed first and we can go."
    hari "Alright. Sounds good."
    stop music fadeout 1.0
    image hari_stage4_18 = "/hari/events/stage4/18.webp"
    scene hari_stage4_18
    "Changing into your regular clothes, you ride along in Hari’s car to reach her apartment."
    image hari_stage4_19 = "/hari/events/stage4/19.webp"
    scene hari_stage4_19
    play music "/music/date_cozy.ogg" if_changed
    "Stepping into Hari’s apartment, you feel a sense of coziness that is necessary for a person to live in such a small space."
    "This extends to her room as you walk in to see the various plushies spread throughout."
    image hari_stage4_20 = "/hari/events/stage4/20.webp"
    scene hari_stage4_20
    "While they’re cute enough to get your attention, your eyes eventually wander towards something sticking out from beneath the bed."
    image hari_stage4_21 = "/hari/events/stage4/21.webp"
    scene hari_stage4_21
    "Before you can get a good look at it, Hari rushes over to push it back beneath the mattress."
    pc "What was that?"
    image hari_stage4_22 = "/hari/events/stage4/22.webp"
    scene hari_stage4_22
    hari "Um, just a dust bunny. I don’t have guests over that often so I might have neglected to clean a bit."
    pc "It doesn’t look like it. Those plushies of yours seem well taken care of."
    image hari_stage4_23 = "/hari/events/stage4/23.webp"
    scene hari_stage4_23
    "Your comment eases her into a warmer expression once more."
    hari "You’re right. I’ve had these for a long time now and I don’t intend to give them up anytime soon."
    hari "They’ve always been around to cheer me up when I have a bad day."
    hari "Anyway, I’m sure you don’t want to hear a grown woman talk about her dolls. You can decide on the movie. I’m going to go make us a bowl of popcorn."
    image hari_stage4_24 = "/hari/events/stage4/24.webp"
    scene hari_stage4_24
    "When Hari returns, you start up a generic action flick and sit down with her."
    image hari_stage4_25 = "/hari/events/stage4/25.webp"
    scene hari_stage4_25
    "Conversation is minimal due to occasional munching on the snacks mixed with losing yourself to the schlocky movie."
    "While it’s mind numbingly simple entertainment, it nonetheless makes for a pleasant evening."
    image hari_stage4_26 = "/hari/events/stage4/26.webp"
    scene hari_stage4_26
    "As the credits roll, you turn back towards Hari to see her reaction."
    "Instead, you can’t help noticing that she managed to empty out the entire popcorn bowl over the course of the film."
    pc "I guess you were pretty hungry after the workout."
    image hari_stage4_27 = "/hari/events/stage4/27.webp"
    scene hari_stage4_27
    hari "Sorry, I can make you more if you want."
    pc "No big deal. What did you think of the movie?"
    hari "It was okay, but the acting was…interesting?"
    pc "It’s alright. You can call it bad. Not like the actors are here anyway."
    image hari_stage4_28 = "/hari/events/stage4/28.webp"
    scene hari_stage4_28
    hari "If you knew it was bad, why did you put it on?"
    pc "Even if it’s bad, it’s still entertaining, don’t you think?"
    image hari_stage4_29 = "/hari/events/stage4/29.webp"
    scene hari_stage4_29
    hari "I…think I understand what you’re talking about. In any case, I really appreciate you hanging out with me today."
    pc "Not a problem. I can tag along if you ever need to go to the gym again."
    hari "That’s not necessary. I’ll just try to go when there’s not a lot of people."
    pc "Are you sure?"
    image hari_stage4_30 = "/hari/events/stage4/30.webp"
    scene hari_stage4_30
    hari "Yeah. I’ve been getting a little bolder lately thanks to you. I’m really glad we got paired up for Ms. Tanwen’s class."
    pc "I should be the one thanking you since you’re doing most of the work."
    image hari_stage4_31 = "/hari/events/stage4/31.webp"
    scene hari_stage4_31
    "Hari lets out a little giggle."
    hari "I’ll try to keep that in mind."
    image hari_stage4_32 = "/hari/events/stage4/32.webp"
    scene hari_stage4_32
    "Eventually you say goodbye to Hari and head for home."
    stop music fadeout 1.0

    scene player_room

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Hari', dialogue=dialogue_one)
    $ msg ("Thank you for today. I was not sure how I would feel about the gym, but it was… enjoyable.", who=1)
    pause
    $ msg ("You did great. I’m still impressed by how flexible you are.")
    pause
    $ msg ("It was unexpected. I suppose I have a natural talent for it.", who=1)
    pause
    $ msg (None, who=1, pic="stage4_hari")
    pause
    $ msg ("I may not be fast or strong, but I do have my advantages.", who=1)
    pause
    $ msg ("I can see that. You’re full of surprises.")
    pause
    $ msg ("I will try not to let that go to my head. Good night.", who=1)
    pause
    $ hide_messenger()

    $ haristage4event = 0
    if recollection == False:
        $ hari.weight += 0.5
        $ daytime += 1
        $ phonecall = 1
    return

label Hari_Stage_4_Event_2:
    #Scene: Asking Hari About Her Work
    #(NOTE: The following should occur shortly after reaching Hari Stage 4 when the player chooses to do a study session with her)
    play music "/music/hari.ogg" if_changed
    image hari_study_sitting_event4 = "/hari/4/study_sitting.webp"
    scene hari_study_sitting_event4
    "You arrive at the study room and are greeted with a rare smile from Hari."
    hari "Hello."
    pc "Hey Hari. You ready for today’s session?"
    hari "I sure am."
    image hari_study_eat1_event4 = "/hari/4/study_eat1.webp"
    scene hari_study_eat1_event4
    "Just like you’ve done many times before, you lay out the snacks for Hari. While she eats, you dutifully record her thoughts."
    image hari_study_eat2_event4 = "/hari/4/study_eat2.webp"
    scene hari_study_eat2_event4
    "While everything is going smoothly, you can’t help noticing how much faster she goes through the snacks."
    image hari_study_aftereat_event4 = "/hari/4/study_aftereat.webp"
    scene hari_study_aftereat_event4
    "Watching her finish off the last of the study materials, a question comes to mind."
    pc "Are you eating enough outside of class?"
    image hari_stage4_33 = "/hari/events/stage4/33.webp"
    scene hari_stage4_33
    hari "Yes, what makes you say that?"
    pc "You seem pretty hungry these days. I’m worried that maybe you’re running low on funds or something."
    image hari_stage4_34 = "/hari/events/stage4/34.webp"
    scene hari_stage4_34
    hari "Oh, everything is fine. My folks handle most of the expenses with my apartment and food while I’m attending university."
    hari "They want to make sure I have everything I need to focus on my studies. Although I do have a part time job to pay off some of my other stuff like my plush dolls."
    pc "You didn’t tell me you had a job. What do you do?"
    image hari_stage4_35 = "/hari/events/stage4/35.webp"
    scene hari_stage4_35
    "Hari hesitates for a moment."
    image hari_stage4_36 = "/hari/events/stage4/36.webp"
    scene hari_stage4_36
    hari "I’m a…freelance writer."
    pc "Really? That sounds pretty interesting. What kind of things do you write about? Horror? Fantasy? Romance?"
    image hari_stage4_37 = "/hari/events/stage4/37.webp"
    scene hari_stage4_37
    hari "Um, something kind of like romance I guess."
    "You seem to have hit a dead end on the conversation as she seems unwilling to talk anymore about it. Rather than push the issue, you decide to change topics."
    pc "Outside of these sessions, how have you been doing in class?"
    image hari_stage4_38 = "/hari/events/stage4/38.webp"
    scene hari_stage4_38
    hari "Fine. But…"
    pc "But what?"
    image hari_stage4_39 = "/hari/events/stage4/39.webp"
    scene hari_stage4_39
    hari "Well you see, there’s a few things from the latest chapter that I can’t quite get my head around."
    pc "If that’s the case, I would be more than willing to help you out."
    hari "Oh, you don’t have to do that. You already help me enough during class."
    pc "I insist. You’ve been helping me so much with this, the least I can do is return the favor."
    image hari_stage4_40 = "/hari/events/stage4/40.webp"
    scene hari_stage4_40
    hari "Well…alright. I’m a little busy this evening but give me a call another time and I’ll see when we can meet up."
    pc "You got it."
    "The two of you manage to clean up everything just as the bell rings and you have to head home."
    #(NOTE: After this scene, the option should pop up whenever the player is in their room to visit Hari at her house for a study session, leading to the following scene.)
    stop music fadeout 1.0
    if recollection == False:
        $ hari_study_times += 1
        $ haristage4event2 = 0
        $ hari.weight += 0.5
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Hari_Stage_4_Event_3:
    #Scene: Hari’s Secret Discovered
    #(NOTE: The following should occur when the player is in their room and they choose the option to visit Hari’s house for a study session.)
    #IMAGE: The player’s room.
    "With free time on your hands, you decide to message Hari for an at home study session."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Hari', dialogue=dialogue_one)
    $ msg ("I’m free today if you want to go over the material together.")
    pause
    $ msg ("I don’t know if now is a good time for that.", who=1)
    pause
    $ msg ("Why? Is something wrong?")
    pause
    $ msg ("No.", who=1)
    pause
    $ msg ("What do you mean?")
    pause
    $ msg ("On second thought, sure. Come on over in a little bit. I just need to tidy up first.", who=1)
    pause
    $ msg ("Okay, see you then.")
    pause
    $ hide_messenger()

    "Picking up your things, you head over to Hari’s apartment."
    image hari_stage4_41 = "/hari/events/stage4/41.webp"
    scene hari_stage4_41
    play music "/music/date_cozy.ogg" if_changed
    "Upon your arrival, you look around to see not much is different. Wondering just how bad it was before you arrived, you put it off in favor of not seeming rude."
    hari "Thank you for coming over. Maybe now I’ll finally be able to wrap my head around this stuff."
    image hari_stage4_42 = "/hari/events/stage4/42.webp"
    scene hari_stage4_42
    pc "Not a problem, let’s see what we have."
    image hari_stage4_43 = "/hari/events/stage4/43.webp"
    scene hari_stage4_43
    "Sitting down with Hari, you go over the material several times."
    image hari_stage4_44 = "/hari/events/stage4/44.webp"
    scene hari_stage4_44
    "Though progress is slow, the two of you seem to be making steady progress."
    image hari_stage4_45 = "/hari/events/stage4/45.webp"
    scene hari_stage4_45
    window hide
    pause
    image hari_stage4_46 = "/hari/events/stage4/46.webp"
    scene hari_stage4_46
    "In-between these moments of brilliance you manage to get Hari to smile and be a lot more sociable than usual."
    image hari_stage4_47 = "/hari/events/stage4/47.webp"
    scene hari_stage4_47
    "The study session comes to a halt as you hear a growl emanate from Hari’s stomach."
    hari "I’m sorry."
    pc "It’s okay. I can go grab us some snacks if you want. After all of this, I think we’ve more than earned it."
    image hari_stage4_48 = "/hari/events/stage4/48.webp"
    scene hari_stage4_48
    hari "No, you stay here. I’ll grab it. Just wait here. I promise I’ll try to pick out something tasty."
    image hari_stage4_49 = "/hari/events/stage4/49.webp"
    scene hari_stage4_49
    pc "Take your time."
    image hari_stage4_50 = "/hari/events/stage4/50.webp"
    scene hari_stage4_50
    "Left by yourself, your eyes eventually wander across the room."
    "Thinking back to her earlier excuse, you can’t help noticing random scraps of paper on the ground and dust littering some of the shelves."
    image hari_stage4_20 = "/hari/events/stage4/20.webp"
    scene hari_stage4_20
    "As you look around trying to figure out what she meant when she said she was cleaning up first, you spot something sticking out from beneath her bed."
    "Curious, you grasp the edge of the object and pull it out."
    image hari_stage4_51 = "/hari/events/stage4/51.webp"
    scene hari_stage4_51
    "What you hold in your hands appears to be a pornographic magazine about plump woman."
    image hari_stage4_52 = "/hari/events/stage4/52.webp"
    scene hari_stage4_52
    "Driven by curiosity, you open up the page to see the previously slim woman on the cover to be twice her previous size."
    "The next pages are filled with similarly large women that range in wardrobe from elegant dresses to skimpy lingerie, and even nothing at all."
    "Some of the glamour shots show off scenes of the ladies gorging themselves on feasts that wouldn’t look out of place in Daisy’s classroom."
    stop music fadeout 1.0
    "Too busy gawking at what you see, you fail to notice Hari as she enters the room."
    play music "/music/sadness.ogg" if_changed
    image hari_stage4_53 = "/hari/events/stage4/53.webp"
    scene hari_stage4_53
    "The sound of a bowl hitting the floor gets your attention away from the magazine."
    image hari_stage4_54 = "/hari/events/stage4/54.webp"
    scene hari_stage4_54
    "Looking up, you see Hari standing there with popcorn spread around her feet. For a moment the two of you just stand there as you take in the situation."
    pc "Hari, I-"
    image hari_stage4_55 = "/hari/events/stage4/55.webp"
    scene hari_stage4_55
    "Rushing forward, Hari snatches the magazine out of your hands and holds it close to her chest."
    hari "I…think you should go."
    pc "But I-"
    image hari_stage4_56 = "/hari/events/stage4/56.webp"
    scene hari_stage4_56
    hari "Just go!"
    "Seeing the tears stream down her face, you realize it would be a futile effort to try and talk to her right now. Grabbing your things, you quickly leave the apartment and head home."
    scene player_room
    "Arriving back at your house, you instinctively pull out your phone to contact her."
    "Remembering the kind of person Hari is, you think it’s best to give her some time to recover before trying to talk to her again."
    #(NOTE: After this, Hari should be absent from the repeatable events and the option to do study sessions with her during class. They will resume after the stage 8 event)
    stop music fadeout 1.0
    if recollection == False:
        $ hari_mad = 1
        $ daycount2 = 0
        $ hari.weight = 72
        $ haristage4event3 = 0
        $ daytime += 1
        jump freetime
    return

label Hari_Stage_5_Event:
    #Scene: Call to Make Up with Hari
    #(NOTE: The following should occur one week after Hari’s stage 5 event when the player is in their room)
    scene player_room
    "Something causes you to think back to your last run-in with Hari."
    "While you think you’ve given her enough time, you’re still not sure how to breach the topic of what you found in her room."
    "You realize it’s going to take some carefully considered words to overcome this hurdle of awkwardness."
    #(NOTE: After this, the option to call up Hari to apologize should appear if the player’s charisma is high enough. The following should occur when the player chooses that option.)
    "As you dial up Hari’s number, you realize that it’s unlikely that she’ll actually pick up."
    "That makes it all the more surprising when you hear her voice respond."
    hari "H-hello?"
    pc "Hari, it’s me, [playername]. I want to talk about what happened at your place. Can we meet and talk somewhere?"
    "There’s an unsettling silence. You expect that at any moment that she’ll hang up."
    hari "…okay. W-would you be okay with meeting at the Sugar Shop?"
    pc "Sure. I’ll see you there."
    hari "A-alright."
    image hari_stage5_1 = "/hari/events/stage5/1.webp"
    scene hari_stage5_1
    play music "/music/date_cozy.ogg" if_changed
    "Arriving at the shop, you manage to spot Hari sitting at a table in the corner."
    "Locking eyes with her, the two of you seem to wordlessly share the same sense of anxiety."
    "Pushing yourself to continue, you make your way towards her and sit down in the opposite seat."
    image hari_stage5_2 = "/hari/events/stage5/2.webp"
    scene hari_stage5_2
    pc "Hey."
    hari "…hey."
    image hari_stage5_3 = "/hari/events/stage5/3.webp"
    scene hari_stage5_3
    "A few awkward moments pass before you can bring yourself to speak."
    pc "I would like to start by saying that I’m sorry. I shouldn’t have been looking through your things like that."
    "Though she remains silent, Hari regardless keeps her eyes on you."
    pc "That beings said, you have nothing to be ashamed of."
    image hari_stage5_4 = "/hari/events/stage5/4.webp"
    scene hari_stage5_4
    "Her head perks up a bit."
    pc "Everyone has their wants and needs. There’s nothing wrong with that. As long as you’re not hurting anyone, you’re allowed to like what you like."
    image hari_stage5_5 = "/hari/events/stage5/5.webp"
    scene hari_stage5_5
    hari "D-do you really mean that?"
    pc "Of course. I don’t see you differently because you have something like that. You’re still the same woman I know from class that I enjoy hanging out with."
    image hari_stage5_6 = "/hari/events/stage5/6.webp"
    scene hari_stage5_6
    hari "E-even if there’s…other things that I’m into?"
    pc "Yes."
    image hari_stage5_7 = "/hari/events/stage5/7.webp"
    scene hari_stage5_7
    "A wide smile spread across Hari’s face."
    image hari_stage5_8 = "/hari/events/stage5/8.webp"
    scene hari_stage5_8
    "Without warning she lunges forward to embrace you in a warm hug."
    hari "Thank you."
    pc "Er, no problem."
    image hari_stage5_9 = "/hari/events/stage5/9.webp"
    scene hari_stage5_9
    "Sitting back down in her seat, Hari proceeds to wipe tears from her eyes."
    pc "Sorry if I made that awkward."
    image hari_stage5_10 = "/hari/events/stage5/10.webp"
    scene hari_stage5_10
    hari "No, it’s fine. You can’t believe how relieving that was to hear. My mind has been going crazy thinking about that ever since we last met."
    pc "Sorry I took so long to get back to you."
    hari "I’m just as much to blame. Guess we both had a bit of anxiety when it came to talking to each other again. Let me make it up to you. Are you hungry?"
    image hari_stage5_11 = "/hari/events/stage5/11.webp"
    scene hari_stage5_11
    "Perhaps bolstered by her conversation with you, Hari proceeds to call over the server and orders up a variety of sweets."
    image hari_stage5_12 = "/hari/events/stage5/12.webp"
    scene hari_stage5_12
    "When the treats arrive, you manage to grab a few for herself before she dives in."
    image hari_stage5_13 = "/hari/events/stage5/13.webp"
    scene hari_stage5_13
    "As you watch her stuff herself silly, you witness a sense of joy overtake her body that you’ve never seen before."
    image hari_stage5_14 = "/hari/events/stage5/14.webp"
    scene hari_stage5_14
    "So engrossed by her uplifted mood and massive intake of food, you mainly nibble on a donut as you wait for her to finish."
    image hari_stage5_15 = "/hari/events/stage5/15.webp"
    scene hari_stage5_15
    "Finishing off the last of her indulgent meal, Hari leans back to massage her belly."
    image hari_stage5_16 = "/hari/events/stage5/16.webp"
    scene hari_stage5_16
    hari "That was a bit much, but it was so satisfying."
    pc "I’ll say. Thank you for the food."
    image hari_stage5_17 = "/hari/events/stage5/17.webp"
    scene hari_stage5_17
    hari "No, thank you for being a good friend."
    image hari_stage5_18 = "/hari/events/stage5/18.webp"
    scene hari_stage5_18
    "You spend the next hour chatting with Hari, catching up on what you’ve missed in the time you’ve been apart."
    image hari_stage5_19 = "/hari/events/stage5/19.webp"
    scene hari_stage5_19
    "Once she’s finally digested enough to move again, the two of you share one more hug before leaving the Sugar Shop."
    image hari_stage5_20 = "/hari/events/stage5/20.webp"
    scene hari_stage5_20
    window hide
    pause
    image hari_stage5_21 = "/hari/events/stage5/21.webp"
    scene hari_stage5_21
    #(NOTE: After this scene, Hari should be available for all of her repeatable events again, study sessions, Bunny Bites visits, the gym, etc.)
    stop music fadeout 1.0
    if recollection == False:
        $ hari.weight += 1
        $ hari_mad = 0
        $ haristage5event = 0
        $ daytime += 1
        $ phonecall = 1
    return

label Hari_Stage_6_Event_1:
    play music "/music/hari.ogg" if_changed
    #Scene: Hari’s Fetish Questions
    #(NOTE: The following should occur shortly after reaching Hari Stage 6 and the player chooses to do a study session with her.)
    image hari_study_sitting_event6 = "/hari/6/study_sitting.webp"
    scene hari_study_sitting_event6
    pc "Hey Hari."
    hari "Hey."
    image hari_stage6_1 = "/hari/events/stage6/1.webp"
    scene hari_stage6_1
    "An unsettling silence settles over the room as you lay out the snacks."
    "While this isn’t entirely new considering who you’re with, you do feel that something is different."
    pc "Is everything okay?"
    image hari_stage6_2 = "/hari/events/stage6/2.webp"
    scene hari_stage6_2
    hari "Uh, yeah. I’m…a little preoccupied with something."
    pc "What’s that?"
    image hari_stage6_3 = "/hari/events/stage6/3.webp"
    scene hari_stage6_3
    "Hari remains silent for a moment."
    image hari_stage6_4 = "/hari/events/stage6/4.webp"
    scene hari_stage6_4
    hari "You know about that…thing you found in my room?"
    pc "Kind of hard to forget."
    hari "That’s, um, just the tip of the iceberg when it comes to my…interests."
    pc "Where are you going with this?"
    "Hari takes a deep breath."
    image hari_stage6_5 = "/hari/events/stage6/5.webp"
    scene hari_stage6_5
    hari "Would you be willing to come over to my place sometime soon? I’d feel a lot more comfortable talking about this there."
    pc "Sure thing. Just text me the next time you’re available."
    hari "Thank you. Could you please hand me that donut? I’ve probably eaten up our time enough."
    image hari_study_eat1_event6 = "/hari/6/study_eat1.webp"
    scene hari_study_eat1_event6
    "Hari easily makes up for her conversation by finishing off the junk food in no time flat."
    "You manage to just barely keep up with her to record the observations just as the bell rings."
    image hari_study_aftereat_event6 = "/hari/6/study_aftereat.webp"
    scene hari_study_aftereat_event6
    hari "You go on ahead. I’ll clean up this time."
    pc "Thank you. Whenever you’re ready to talk, just let me know."
    hari "Thank you."
    "Leaving Hari to take care of the mess, you head home."
    stop music fadeout 1.0
    if recollection == False:
        $ hari.weight += 0.5
        $ hari_study_times += 1
        $ haristage6event = 0
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Hari_Stage_6_Event_2:
    #Scene: Hari Talks About her Fetishes
    #(NOTE: The following should occur when the player is in their room shortly after the previous scene)
    #IMAGE: Player’s room.
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Hari', dialogue=dialogue_one)
    $ msg ("I think I’m ready to have that talk I mentioned. Can you meet at my house today?", who=1)
    pause
    #CHOICE: A) Sorry, I’m busy or B) Sure, I’ll be right over
    menu:
        "Sure, I’ll be right over.":
            $ msg ("Sure, I’ll be right over.")
            pause
            $ msg ("Ok. I’ll see you then.", who=1)
            pause
            $ hide_messenger()
        "Sorry, I’m busy.":
            $ msg ("Sorry, I’m busy.")
            pause
            $ msg ("I understand. I’ll try again some other time.", who=1)
            pause
            $ hide_messenger()
            #(NOTE: If the player chooses this option, Hari will message them each following day until they choose option B)
            return

    image hari_stage6_6 = "/hari/events/stage6/6.webp"
    scene hari_stage6_6
    play music "/music/date_cozy.ogg" if_changed
    "Entering the apartment, Hari greets you with a small wave."
    pc "Are you sure you’re okay with this?"
    image hari_stage6_7 = "/hari/events/stage6/7.webp"
    scene hari_stage6_7
    hari "Not entirely."
    pc "You don’t have to do this if it makes you uncomfortable."
    image hari_stage6_8 = "/hari/events/stage6/8.webp"
    scene hari_stage6_8
    hari "No, this has to be done."
    image hari_stage6_9 = "/hari/events/stage6/9.webp"
    scene hari_stage6_9
    "Gesturing for you to sit on the bed, she reaches beneath the mattress to pull out a familiar sight."
    image hari_stage6_10 = "/hari/events/stage6/10.webp"
    scene hari_stage6_10
    "Though she shows off the familiar cover for a moment, it doesn’t take long for her to sheepishly press it against her chest in embarrassment."
    image hari_stage6_11 = "/hari/events/stage6/11.webp"
    scene hari_stage6_11
    hari "This is the first time that I’ve shown this to someone. I was even able to keep it secret from my parents back when I lived at home."
    pc "That’s not too out of the ordinary. A lot of people have stashes like that."
    image hari_stage6_12 = "/hari/events/stage6/12.webp"
    scene hari_stage6_12
    hari "Even you?"
    #CHOICE: A) No, I just look up stuff on the internet or B) I keep a collection somewhere in my room.
    menu:
        "No, I just look up stuff on the internet.":
            hari "Oh…I guess that makes sense. I think I prefer to have it in my hands though."
        "I keep a collection in my room.":
            hari "Y-you don’t say."
    #(NOTE: Regardless of choice, the following dialogue should play out.)
    hari "Regardless, I doubt people have things that are as…niche as mine."
    image hari_stage6_13 = "/hari/events/stage6/13.webp"
    scene hari_stage6_13
    "Begrudgingly, Hari opens up the magazine and turns it to show it off to you."
    "As her fingers turn through the pages, you once more look upon scenes of fat women in various, gluttony fueled situations."
    "Eventually her nerves get the better of her, forcing her to close the magazine once more."
    image hari_stage6_14 = "/hari/events/stage6/14.webp"
    scene hari_stage6_14
    hari "T-this is the kind of things I’m into."
    pc "How long have you been looking at this stuff?"
    "She puts away the magazine and hesitates for a moment."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/hari/events/stage6/33.webm" loop
    show movie with dissolve
    hari "Ever since I turned 18. I was going through some websites trying to find…material for stress relief and stumbled upon a video of a woman stuffing herself."
    hari "When I found it, I watched it on repeat to try and figure out why I felt so obsessed with it."
    pc "Are you into women?"
    hari "No. Well, I don’t think so at least. I’ve never been with one."
    pc "Then what was it?"
    hari "I still wasn’t sure. After going over the video so many times, I ended up seeking others to try and figure out what was wrong with me."
    stop movie
    image hari_stage6_15 = "/hari/events/stage6/15.webp"
    scene hari_stage6_15
    "She takes a step towards you."
    hari "But that wasn’t enough. I sought out blogs, art, and even erotica to further explore this feeling."
    hari "While I could never reignite that initial spark from the original video, they helped me to figure out what exactly my body wants."
    pc "What’s that?"
    image hari_stage6_16 = "/hari/events/stage6/16.webp"
    scene hari_stage6_16
    "She steps up to be mere inches from your face."
    hari "Pure, unrestrained hedonism. There’s something about the idea of getting to just enjoy every carnal desire of your body that just makes me want to…want to…"
    "Hari pauses, only know realizing how close she is to you and the way her body is shaking."
    image hari_stage6_17 = "/hari/events/stage6/17.webp"
    scene hari_stage6_17
    "Taking a deep breath to calm herself down, Hari sits down beside you."
    hari "Sorry. I got a little overexcited. You must think I’m extra weird now."
    pc "Not at all. Everyone has their own, strange fetishes."
    image hari_stage6_18 = "/hari/events/stage6/18.webp"
    scene hari_stage6_18
    hari "Yeah, but how many of them fantasize about stuffing their face like a fat, greedy pig?"
    pc "Well…I do."
    image hari_stage6_19 = "/hari/events/stage6/19.webp"
    scene hari_stage6_19
    "Hari picks up her head to stare at you."
    hari "What?"
    pc "I said, I’m into girls gaining weight."
    image hari_stage6_20 = "/hari/events/stage6/20.webp"
    scene hari_stage6_20
    hari "You’re serious? This isn’t some kind of prank, right?"
    pc "It’s the truth. Honestly it’s the main reason I do so well in Daisy’s, I mean, Ms. Tanwen’s class."
    image hari_stage6_21 = "/hari/events/stage6/21.webp"
    scene hari_stage6_21
    hari "That…makes sense. Wait, when we were doing our study sessions, did you…enjoy watching me stuff myself with snacks?"
    pc "Yeah, but I didn’t think you would appreciate me telling you that out loud."
    hari "No. Well, maybe I would. I’m not sure."
    pc "What do you mean?"
    image hari_stage6_22 = "/hari/events/stage6/22.webp"
    scene hari_stage6_22
    "Hari fidgets for a moment."
    hari "For a while, I’ve had some…ideas that I’ve wanted to try out, but they require two people. Maybe, just maybe, if I had someone who could help me out then I could…"
    "Though she doesn’t say it, you can figure out some of what Hari means. Seeing the way her body trembles, you decide to take a leap of faith."
    pc "I’ll do it."
    image hari_stage6_23 = "/hari/events/stage6/23.webp"
    scene hari_stage6_23
    hari "What?"
    pc "I’ll help you out with fulfilling your ideas. It’s the least I can do considering what we’ve been through."
    "A smile stretches across Hari’s face."
    image hari_stage6_24 = "/hari/events/stage6/24.webp"
    scene hari_stage6_24
    "Without warning, Hari lunges forward to pull you into a hug."
    image hari_stage6_25 = "/hari/events/stage6/25.webp"
    scene hari_stage6_25
    "Still reeling from the sudden embrace, you are left off guard as she continues forward to plant a quick kiss on your lips."
    image hari_stage6_26 = "/hari/events/stage6/26.webp"
    scene hari_stage6_26
    "A few seconds later, Hari realizes what she’s done. Pulling herself away, she shuffles over to the other side of the bed."
    hari "Sorry, I think I got caught up in the moment."
    pc "It’s okay. It’s not like I hated it."
    image hari_stage6_27 = "/hari/events/stage6/27.webp"
    scene hari_stage6_27
    hari "I’ll try to keep myself under control when we try out my…experiment."
    pc "Does that mean you’ll accept my help?"
    image hari_stage6_28 = "/hari/events/stage6/28.webp"
    scene hari_stage6_28
    hari "Y-yeah but give me some time. I want to make sure I have everything I need first."
    pc "I’ll be ready anytime you are."
    image hari_stage6_29 = "/hari/events/stage6/29.webp"
    scene hari_stage6_29
    "Hari turns back to you to show off a small smile."
    hari "Thank you."
    image hari_stage6_30 = "/hari/events/stage6/30.webp"
    scene hari_stage6_30
    "While Hari stands up, you notice just how much larger her butt has grown."
    image hari_stage6_31 = "/hari/events/stage6/31.webp"
    scene hari_stage6_31
    hari "Sorry to boot you out, but would you mind giving me some time alone? I need a chance to process all of this."
    pc "Not a problem. I’ll see you later."
    image hari_stage6_32 = "/hari/events/stage6/32.webp"
    scene hari_stage6_32
    hari "Yeah. See you then."
    "With the feeling of the kiss lingering on your lips, you leave her apartment."

    stop music fadeout 1.0
    if recollection == False:
        $ haristage6event2 = 0
        $ hari.weight += 0.5
        $ daytime += 1
        $ phonecall = 1
    return

label Hari_Stage_7_Event:
    #Scene: Hari’s First Fantasy
    #(NOTE: The following should occur shortly after reaching Hari stage 10 when the player is in their room.)
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Hari', dialogue=dialogue_one)
    $ msg ("I think I’m ready.", who=1)
    pause
    $ msg ("Ready for what?")
    pause
    $ msg ("Ready to try out one of my fantasies. I know this is a little sudden, but could you come over tonight?", who=1)
    pause
    #CHOICE: A) Sorry, tonight isn’t good for me or B) Sure, I’ll be right over
    menu:
        "Sure, I’ll be right over.":
            $ msg ("Sure, I’ll be right over.")
            pause
            $ msg ("Okay. See you then.", who=1)
            pause
            $ hide_messenger()
        "Sorry, tonight isn’t good for me.":
            $ msg ("Sorry, tonight isn’t good for me.")
            pause
            $ msg ("Okay. We can try again some other time.", who=1)
            pause
            $ hide_messenger()
            #(NOTE: If the player chooses this option, Hari will message them each following day until they choose option B)
            return

    image hari_stage7_1 = "/hari/events/stage7/1.webp"
    scene hari_stage7_1
    "Arriving at Hari’s apartment, the expression you see on her makes it look likes she’s ready to run away at a moment’s notice."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/hari/events/stage7/2.webm" loop
    show movie with dissolve
    pc "We don’t have to do this if you don’t want to. We can just hang out and watch a movie again."
    hari "No. I…want to do this. I’m sure of it."
    pc "In that case, where would you like me to start?"
    "She takes a deep breath."
    hari "I left a couple boxes of donuts in the kitchen. Could you go grab them while I change?"
    stop movie
    image hari_stage7_3 = "/hari/events/stage7/3.webp"
    scene hari_stage7_3
    "Nodding your head in agreement, you do as she says and retrieve the box."
    image hari_stage7_4 = "/hari/events/stage7/4.webp"
    scene hari_stage7_4
    "When you arrive, you see that Hari’s choice of wardrobe is a skimpy outfit that leaves very little to the imagination."
    "Judging by the way she squirms, she’s more than a little anxious about your reaction."
    pc "Why are you dressed like that?"
    image hari_stage7_5 = "/hari/events/stage7/5.webp"
    scene hari_stage7_5
    hari "It’s, um, part of the fantasy. I promise it will make more sense after we get things started."
    pc "Okay. Where do you want me?"
    image hari_stage7_6 = "/hari/events/stage7/6.webp"
    scene hari_stage7_6
    hari "Please sit down on the bed."
    image hari_stage7_7 = "/hari/events/stage7/7.webp"
    scene hari_stage7_7
    "A moment after you take your seat, Hari shuffles over to sit down next to you."
    image hari_stage7_8 = "/hari/events/stage7/8.webp"
    scene hari_stage7_8
    hari "Okay then. Now I want you to feed me."
    pc "The whole thing?"
    image hari_stage7_9 = "/hari/events/stage7/9.webp"
    scene hari_stage7_9
    hari "Yes. I don’t want you to stop until I’ve eaten every bite. Do you understand?"
    pc "You can count on me."
    image hari_stage7_10 = "/hari/events/stage7/10.webp"
    scene hari_stage7_10
    "As nervous as she appears, Hari seems relieved to hear your words."
    hari "You can start whenever you’re ready."
    image hari_stage7_11 = "/hari/events/stage7/11.webp"
    scene hari_stage7_11
    "As instructed, you pull out the first donut and hold it up to her face."
    image hari_stage7_12 = "/hari/events/stage7/12.webp"
    scene hari_stage7_12
    "Due to her nervousness, she slowly nibbles away at the sweet treat."
    image hari_stage7_13 = "/hari/events/stage7/13.webp"
    scene hari_stage7_13
    "Though it takes a while for her to finish the first one, she seems to pick up speed as you hold up her second."
    image hari_stage7_14 = "/hari/events/stage7/14.webp"
    scene hari_stage7_14
    "From there, it appears that her ravenous appetite kicks in to full gear. She begins to eat whatever you hand her at a quickening pace."
    "While you’re busy focusing on keeping up with her, you nearly miss the moment that you empty out one of the boxes."
    image hari_stage7_15 = "/hari/events/stage7/15.webp"
    scene hari_stage7_15
    "Turning back to Hari, you see the results of her binge feast in the form of a sizable belly bulge between her legs."
    pc "Hari, do you feel alright? That was a lot of food. We can stop now if you want."
    hari "Noooo…"
    image hari_stage7_16 = "/hari/events/stage7/16.webp"
    scene hari_stage7_16
    "Hari turns to you, showing off a side of her that is far removed from her usually reserved self."
    pc "Hari?"
    hari "Don’t stop now. Not when I’m so close to my true indulgence. Come on. Give this perverted piggy exactly what she wants."
    image hari_stage7_17 = "/hari/events/stage7/17.webp"
    scene hari_stage7_17
    "Heeding her pleas, you open up the second box and began to feed her."
    image hari_stage7_18 = "/hari/events/stage7/18.webp"
    scene hari_stage7_18
    "Despite how much she’s already devoured, she still gobbles up the sweets you hold up to her mouth."
    "Too busy focusing on stuffing her face, you fail to notice what else she’s doing."
    "That is until she interrupts her feeding with a soft moan from her lips."
    if persistent.masturbation:
        scene black with dissolve
        "Hari had a good time."
    else:
        image hari_stage7_19 = "/hari/events/stage7/19.webp"
        scene hari_stage7_19
        "Titling your gaze downwards reveals the source of the noise."
        #VID MAYBE?
        "While her mouth busies itself with pleasing her appetite, her fingers work hard to take care of her other need."
        "Though you want to stop and stare, you recall why she invited you over in the first place."
        "Between holding out more donuts for her to chew on, you keep glancing back to watch her indulge herself."
        "Just as you manage to feed her the final donut, she finds her release."
        image hari_stage7_20 = "/hari/events/stage7/20.webp"
        scene hari_stage7_20
        "In the wake of her orgasm, you watch Hari fall backwards onto the bed. For a moment she just lays there, breathing heavily as her entire body shudders."
        pc "Hari, are you okay?"
    image hari_stage7_21 = "/hari/events/stage7/21.webp"
    scene hari_stage7_21
    "Hari sucks in a mouthful of air."
    hari "That…was…amazing."
    pc "Was it everything you hoped it would be?"
    hari "And then some. Sorry if I acted a little strange there. I was just…so happy to finally let loose."
    image hari_stage7_22 = "/hari/events/stage7/22.webp"
    scene hari_stage7_22
    "Though she still shakes a bit, she manages to sit herself up."
    hari "Thank you so much for letting me finally experience something like that firsthand."
    pc "I honestly didn’t do much outside of what my job is during our study sessions."
    hari "We can do more if you like."
    "You’re suddenly stunned by the eagerness in her voice."
    pc "What do you mean?"
    image hari_stage7_23 = "/hari/events/stage7/23.webp"
    scene hari_stage7_23
    "Hari lets out a playful giggle."
    hari "Maybe it’s better to save it for next time. For now, would you mind helping me clean up?"
    pc "Not a problem."
    image hari_stage7_24 = "/hari/events/stage7/24.webp"
    scene hari_stage7_24
    "As you pick up the empty boxes, you look back to watch Hari squeeze into her clothes."
    image hari_stage7_25 = "/hari/events/stage7/25.webp"
    scene hari_stage7_25
    "Seeing the smile lingering on her face, you can’t forget the other side of her you saw today."
    "Noticing the way you stare at her; she looks back to give you a devilish grin."
    image hari_stage7_26 = "/hari/events/stage7/26.webp"
    scene hari_stage7_26
    "Unsure of what you just unleashed, you say your goodbye and head for home."

    stop music fadeout 1.0
    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
        $ hari.weight += 1
        $ haristage7event = 0
        #Unlocks Hari Undress in the stats page.
        $ renpy.notify("Hari Undress option unlocked in stats screen.")
        window hide
        pause
    return
