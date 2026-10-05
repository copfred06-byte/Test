label Vicky_study_1:
    image vicky_study_arrive1 = "/vicky/[vicky.stage]/study_arrive1.webp"
    scene vicky_study_arrive1
    "When you arrive in the study room, Vicky is already there waiting for you."
    image vicky_study_arrive2 = "/vicky/[vicky.stage]/study_arrive2.webp"
    scene vicky_study_arrive2
    vicky "Um, what took you so long?"
    image vicky_study_food1 = "/vicky/[vicky.stage]/study_food1.webp"
    scene vicky_study_food1
    pc "Well I had to get these."
    vicky "Ooooh, brain food!"
    pc "Right."
    image vicky_study_eat1 = "/vicky/[vicky.stage]/study_eat1.webp"
    scene vicky_study_eat1
    "As you begin to outline your presentation topic, Vicky sits back and contributes nothing, munching on the provided snacks until the end of class."
    "After class ends, you pack up and head home."
    $ vicky_study_times = 1
    $ vicky.weight += 0.3
    return

label Vicky_study_2:
    image vicky_study_arrive3 = "/vicky/[vicky.stage]/study_arrive3.webp"
    scene vicky_study_arrive3
    "You arrive in the study room."
    image vicky_study_food1 = "/vicky/[vicky.stage]/study_food1.webp"
    scene vicky_study_food1
    "Resolute to not let Vicky's laziness get you down, you just ignore her and hit the books hard, intent on nailing this presentation."
    "..."
    "An hour in, you're getting terribly bored. The whole advantage of group work is that you have someone to talk to in hopes of making the often dull subject matter tolerable."
    "Screw it, you're going to talk to her about the project. Whether or not she has any valuable input, it has to be better than this damn silence!"
    image vicky_study_eat2 = "/vicky/[vicky.stage]/study_eat2.webp"
    scene vicky_study_eat2
    "You clear your throat before speaking."
    pc "Right, so here's how I'm thinking we do this: I'll cover the relevant historical context and citations and you can present present our thesis and our closing argument. Does that work for you?"
    "..."
    image vicky_study_talk1 = "/vicky/[vicky.stage]/study_talk1.webp"
    scene vicky_study_talk1
    "Vicky looks up at you, clearly snapping out of some daydream."
    vicky "Huh? Uh sure, sounds great."
    image vicky_study_food2 = "/vicky/[vicky.stage]/study_food2.webp"
    scene vicky_study_food2
    "Helpful as always..."
    "Well, it's better than nothing, you suppose." 
    "After that enlightening exchange, neither of you say a word for the rest of the period."
    "Once class is over, you pack up and head home."
    $ vicky_study_times = 2
    $ vicky.weight += 0.5
    return

label Vicky_study_3:
    image vicky_study_arrive4 = "/vicky/[vicky.stage]/study_arrive4.webp"
    scene vicky_study_arrive4
    if vicky.stage >= 4:
        "You arrive in the study room to see Vicky rumaging through the supplies."
        "Her growing behind pointing right at you while she claims her sweets."
        image vicky_study_arrive5 = "/vicky/[vicky.stage]/study_arrive5.webp"
        scene vicky_study_arrive5
        vicky "Hey, let's get started on the project."
        "As if she is going to contribute anything."
        "You quickly get to work. You want to finish this assignment before you head home."
    else:
        "You arrive in the study room and quickly get to work. You want to finish this assignment before you head home."
        "It should be doable, if not for the spoiled, redheaded obstacle sitting across from you."
    image vicky_study_phone1 = "/vicky/[vicky.stage]/study_phone1.webp"
    scene vicky_study_phone1
    "Unfortunately, Vicky seems to have decided that this is the perfect moment to have a loud phone conversation with a friend."
    "You can barely focus as she laughs and gossips with the person on the other end. Is this some cruel punishment for wishing she weren't so quiet yesterday?"
    image vicky_study_phone2 = "/vicky/[vicky.stage]/study_phone2.webp"
    scene vicky_study_phone2
    "Eventually, you can't take it anymore. You have to say something."
    vicky "UGH yeah, my parents are the same way. They went to Prague and only left me like 10k in spending money? What is this, the Depression?"
    pc "Sorry Vicky, but could you maybe go into the hall if you're gonna talk on the phone? It's making it hard to concentrate."
    image vicky_study_phone3 = "/vicky/[vicky.stage]/study_phone3.webp"
    scene vicky_study_phone3
    vicky "Well, deal with it! Am I just supposed to like sit here in silence for the whole period?"
    "If only..."
    image vicky_study_phone4 = "/vicky/[vicky.stage]/study_phone4.webp"
    scene vicky_study_phone4
    vicky "Mmph, shorry about that. No, nothing."
    "Realizing you're not gonna make any more progress in this discussion, you just get back to work and try to ignore her conversation."
    image vicky_study_feed1 = "/vicky/study_feed1.webp"
    scene vicky_study_feed1
    "SNAP SNAP"
    "As Vicky snaps her fingers to get your attention, you look up at her, visibly annoyed."
    image vicky_study_feed2 = "/vicky/[vicky.stage]/study_feed2.webp"
    scene vicky_study_feed2
    "She doesn't say anything, as she's talking on the phone, but it's pretty easy to figure out what she wants."
    image vicky_study_feed3 = "/vicky/[vicky.stage]/study_feed3.webp"
    scene vicky_study_feed3
    window hide
    pause
    image vicky_study_feed4 = "/vicky/[vicky.stage]/study_feed4.webp"
    scene vicky_study_feed4
    "You sigh as you grab a donut and get up."
    image vicky_study_feed5 = "/vicky/[vicky.stage]/study_feed5.webp"
    scene vicky_study_feed5
    "Of course, one donut turns to two, two to four, four to eight, and before you know it, Vicky's phone call and the class are over."
    image vicky_study_feed6 = "/vicky/[vicky.stage]/study_feed6.webp"
    scene vicky_study_feed6
    "The presentation nowhere near done, it looks like you'll be doing some last minute homework tonight."
    "You head home immediately, wanting to get this done as soon as possible."
    $ vicky_study_times = 3
    $ vicky.weight += 0.8
    return

label Vicky_study_4:
    #[in class, Daisy enters]
    call rngteachingscene
    teacher "Now, before we begin, we have a team ready to present their assignment."
    teacher "Vicky, [playername], could you please come to the front of the class?"
    image vicky_study_presentation1 = "/vicky/[vicky.stage]/study_presentation1.webp"
    scene vicky_study_presentation1
    "As usual, Vicky presents 'her part' of the project with total confidence, despite not helping out at all during the research portion."
    image vicky_study_presentation2 = "/vicky/[vicky.stage]/study_presentation2.webp"
    scene vicky_study_presentation2
    "As for you, despite knowing the topic front to back, your delivery is more than a little dry and you have to refer to your cue cards."
    "This would be a lot easier if you hadn't stayed up all night finishing the assignment..."
    image vicky_study_presentation3 = "/vicky/[vicky.stage]/study_presentation3.webp"
    scene vicky_study_presentation3
    "Once that's done, you take Vicky's measurements, which she then tells to the rest of the class."
    if persistent.imperial:
        $ imperialweight = (vicky.weight * 2.2)
        vicky "I currently weigh [imperialweight:.02f]lbs, my belly measures [vicky.waist_size:.02f]inches and my butt measures [vicky.ass_size:.02f]inches."
        vicky "Finally, my breasts are [vicky.breast_cup] cup and measure [vicky.breast_size:.02f]inches."
    else:
        $ metricwaist_size = (vicky.waist_size * 2.54)
        $ metricbreast_size = (vicky.breast_size * 2.54)
        $ metricass_size = (vicky.ass_size * 2.54)
        vicky "I currently weigh [vicky.weight:.02f]kg, my belly measures [metricwaist_size:.02f]cm and my butt measures [metricass_size:.02f]cm."
        vicky "Finally, my breasts are [vicky.breast_cup] cup and measure [metricbreast_size:.02f]cm."
    teacher "Excellent work, Vicky. [playername]...you're improving."
    teacher "The two of you can return to your seats now."
    ###Regular feeding class###
    return

label Vicky_Intro1:
    #Vicky intro: (should occur during a class)
    "As you listen to Daisy's lecture, you're suddenly distracted by someone whispering in the classroom."
    "You look around to see where it's coming from."
    image vicky_stage_1_event_7 = "/vicky/events/stage1/7.webp"
    scene vicky_stage_1_event_7
    $ unknownname = 'Tall redhead'
    "You spot the source of the noise on the other side of the class, some redhead busy chatting with her friend."
    unknown "(inaudible) Ms. Tanwen... (inaudible) like totally... (inaudible) pig (laughs)"
    "It seems like Daisy hasn't noticed them."
    $ unknownname = 'Unknown'
    "You like to mind your own business, but this noise is preventing you from paying attention to the class..."
    pc "SHHHHHHH!"
    image vicky_stage_1_event_8 = "/vicky/events/stage1/8.webp"
    scene vicky_stage_1_event_8
    "Your loud shush startles the redhead, who jumps back in her seat, causing enough noise for Daisy to finally take notice."
    image caroline_stage1_22 = "/caroline/events/stage1/22.webp"
    scene caroline_stage1_22
    teacher "Vicky, please quiet down, people are trying to learn. With your grades, you ought to do the same."
    vicky "But I-ugh, whatever..."
    image vicky_stage_1_event_9 = "/vicky/events/stage1/9.webp"
    scene vicky_stage_1_event_9
    "As Daisy goes back to teaching, the redhead glares at you, clearly not happy."
    $ vickyintro1 = 0
    return

label Vicky_Intro2:
    #First meeting with Vicky:
    image vicky_stage_1_event_1 = "/vicky/events/stage1/1.webp"
    scene vicky_stage_1_event_1
    "As you head for the door at the end of class, someone bumps into you."
    $ unknownname = 'Nikki?'
    pc "Oof!"
    image vicky_stage_1_event_2 = "/vicky/events/stage1/2.webp"
    scene vicky_stage_1_event_2
    unknown "Hey, watch where you're going!"
    pc "Sorry about that..."
    image vicky_stage_1_event_3 = "/vicky/events/stage1/3.webp"
    scene vicky_stage_1_event_3
    "It's that one girl who was noisy during class. What was her name again? Oh right, it was..."
    pc "...Nikki, I wasn't-"
    $ unknownname = 'Unknown'
    image vicky_stage_1_event_4 = "/vicky/events/stage1/4.webp"
    scene vicky_stage_1_event_4
    vicky "Vicky, my name is Vicky, like Victoria, like the queen."
    pc "Uhhh right, sorry Vicky. I was distracted."
    image vicky_stage_1_event_5 = "/vicky/events/stage1/5.webp"
    scene vicky_stage_1_event_5
    vicky "Ugh, whatever."
    image vicky_stage_1_event_6 = "/vicky/events/stage1/6.webp"
    scene vicky_stage_1_event_6
    pc "Nice girl."
    $ vickyintro2 = 0
    return

label Vicky_Intro3:
    #Second meeting with Vicky (should occur before class)
    "You check your phone as you wait for class to start."
    "Suddenly, you hear someone cough, clearly trying to get your attention."
    image vicky_stage_1_event_10 = "/vicky/events/stage1/10.webp"
    scene vicky_stage_1_event_10
    "It's that girl, Vicky."
    vicky "Heyyy!"
    pc "Um, hey Vicky, how's it going?"
    image vicky_stage_1_event_11 = "/vicky/events/stage1/11.webp"
    scene vicky_stage_1_event_11
    vicky "Oh I'm doing great, thanks-"
    vicky "Uh, what was your name again?"
    pc "[playername]"
    image vicky_stage_1_event_12 = "/vicky/events/stage1/12.webp"
    scene vicky_stage_1_event_12
    vicky "-[playername], right! How are you doing?"
    pc "Fine, I guess."
    vicky "Good, good! That's great!"
    image vicky_stage_1_event_13 = "/vicky/events/stage1/13.webp"
    scene vicky_stage_1_event_13
    "..."
    image vicky_stage_1_event_14 = "/vicky/events/stage1/14.webp"
    scene vicky_stage_1_event_14
    vicky "Well, catch you later [playername]!"
    image vicky_stage_1_event_15 = "/vicky/events/stage1/15.webp"
    scene vicky_stage_1_event_15
    pc "Right..."
    "What was that all about?"
    $ vickyintro3 = 0
    return

label Vicky_Stage_1_Event:
    #First project with Vicky:
    #Session 1:
    scene player_room
    "You make your way down to the university."
    scene university_outside
    "Arriving to class, you take your seat."
    play music "/music/university.ogg" if_changed
    call rngteachingscene
    "Once again, you've been paired up with one of your classmates."
    "Your partner this time is..."
    pc "Vicky?!"
    image vicky_stage_1_event_16 = "/vicky/events/stage1/16.webp"
    scene vicky_stage_1_event_16
    vicky "Ugh, him?"
    teacher "What was that, Vicky?"
    image vicky_stage_1_event_17 = "/vicky/events/stage1/17.webp"
    scene vicky_stage_1_event_17
    vicky "Nothing, Miss Tanwen!"
    teacher "In that case, you and [playername] can grab the necessary documents and supplies, and head to a study room to begin work."
    "You head to a study room to get started on your project."
    image vicky_stage_1_event_18 = "/vicky/events/stage1/18.webp"
    scene vicky_stage_1_event_18
    pc "Alright, let's see what we have to do."
    "Assignment: Detail the socioeconomic factors which explain the changing perception of fat at different periods in history."
    image vicky_stage_1_event_19 = "/vicky/events/stage1/19.webp"
    scene vicky_stage_1_event_19
    vicky "Like, what the hell does that have to do with all that food?"
    pc "I'm not sure. Brain food, I guess?"
    vicky "Let me try one."
    image vicky_stage_1_event_20 = "/vicky/events/stage1/20.webp"
    scene vicky_stage_1_event_20
    vicky "Mmm, pretty good."
    pc "Cool. Anyways, we should probably split the work for this. I can cover Mesopotamia to the Renaissance while you do the Renaissance to today, does that sound good?"
    image vicky_stage_1_event_21 = "/vicky/events/stage1/21.webp"
    scene vicky_stage_1_event_21
    "It's like she didn't hear a word you just said."
    pc "Vicky?"
    image vicky_stage_1_event_22 = "/vicky/events/stage1/22.webp"
    scene vicky_stage_1_event_22
    vicky "Huh? Oh yeah, I'm listening—Um...What are we talking about?"
    "You get the feeling this isn't going to be easy."
    pc "I was just saying you can cover the 20th and 21st century while I do the rest. Does that work for you?"
    image vicky_stage_1_event_23 = "/vicky/events/stage1/23.webp"
    scene vicky_stage_1_event_23
    vicky "Mhm, yeah, totally."
    "She's still looking at her phone..."
    pc "Right then, time to get to work!"
    image vicky_stage_1_event_24 = "/vicky/events/stage1/24.webp"
    scene vicky_stage_1_event_24
    "You read and annotate the provided texts, figuring out what's important to your project. Meanwhile, Vicky doesn't seem to do much of anything."
    "Eventually, class ends and you pack your things up."
    image vicky_stage_1_event_25 = "/vicky/events/stage1/25.webp"
    scene vicky_stage_1_event_25
    pc "Alright, I'll see you tomorrow. Be sure to start working on your part."
    vicky "Whatever..."
    "You head home."
    $ vickystage1event = 0
    stop music fadeout 1.0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        $ vicky.weight += 1
        jump freetime
    return

label Vicky_Stage_1_Event_2:
    #Session 2:
    image vicky_stage_1_event_26 = "/vicky/events/stage1/26.webp"
    scene vicky_stage_1_event_26
    play music "/music/university.ogg" if_changed
    "You hit the books to prepare your notes for this project. However, you can't help but notice that Vicky once again isn't working."
    pc "Hey Vicky, you make any progress on your part of the project last night?"
    image vicky_stage_1_event_27 = "/vicky/events/stage1/27.webp"
    scene vicky_stage_1_event_27
    vicky "No, sorry, I was busy."
    pc "Right, well you should probably get on that, then."
    image vicky_stage_1_event_28 = "/vicky/events/stage1/28.webp"
    scene vicky_stage_1_event_28
    vicky "Ugh, what's the rush? It's not like it's due this week!"
    pc "It is, though..."
    vicky "Whatever, just, like, worry about your part and I'll worry about mine, okay?"
    image vicky_stage_1_event_29 = "/vicky/events/stage1/29.webp"
    scene vicky_stage_1_event_29
    "Another successful interaction with your lovely partner."
    image vicky_stage_1_event_30 = "/vicky/events/stage1/30.webp"
    scene vicky_stage_1_event_30
    "A while later, you're feeling a bit peckish. You could certainly go for one of those donuts."
    image vicky_stage_1_event_31 = "/vicky/events/stage1/31.webp"
    scene vicky_stage_1_event_31 with vpunch
    "SMACK"
    pc "What the hell?"
    image vicky_stage_1_event_32 = "/vicky/events/stage1/32.webp"
    scene vicky_stage_1_event_32
    vicky "Do you really think someone who looks like you should be helping themself to donuts?"
    pc "'Someone who looks like me'? What, trim and ripped as hell?"
    image vicky_stage_1_event_33 = "/vicky/events/stage1/33.webp"
    scene vicky_stage_1_event_33
    "Vicky hesitates"
    vicky "Y—yeah! I mean, you don't want to ruin your figure, right?"
    image vicky_stage_1_event_34 = "/vicky/events/stage1/34.webp"
    scene vicky_stage_1_event_34
    pc "Thanks for the concern..."
    "You head back home."
    $ vickystage1event2 = 0
    stop music fadeout 1.0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        $ vicky.weight += 1
        jump freetime
    return


label Vicky_Stage_1_Event_3:
    #Session 3:
    play music "/music/university.ogg" if_changed
    "Time for another study session. Hopefully your partner has gotten her ass into gear."
    image vicky_stage_1_event_35 = "/vicky/events/stage1/35.webp"
    scene vicky_stage_1_event_35
    pc "Alright, since the presentation is tomorrow I think we should practice today so we know what we're doing."
    image vicky_stage_1_event_36 = "/vicky/events/stage1/36.webp"
    scene vicky_stage_1_event_36
    vicky "Whatever."
    "Her enthusiasm is infectious."
    pc "I'll go first."
    image vicky_stage_1_event_37 = "/vicky/events/stage1/37.webp"
    scene vicky_stage_1_event_37
    "Although she clearly doesn't care, Vicky at least has the decency to pay attention to your presentation."
    "However, some of your findings seem to pique her interest."
    pc "—by comparison, feudal societies generally viewed fat as a sign of nobility."
    image vicky_stage_1_event_38 = "/vicky/events/stage1/38.webp"
    scene vicky_stage_1_event_38
    pc "Nobles, who were waited on by servants and received tribute from their subjects, were the only people who had what was viewed as the luxury of getting fat." 
    pc "Meanwhile their subjects, having given most of what they earned to their lords and ladies, remained thin living on what was left."
    "She listened intently to the rest of your presentation, seemingly captivated by the material."
    pc "—and that's all I've got!"
    image vicky_stage_1_event_39 = "/vicky/events/stage1/39.webp"
    scene vicky_stage_1_event_39
    "Vicky gives you an enthusiastic round of applause. Funny, you don't think you've ever seen her smile before."
    vicky "That was totally great!"
    pc "Hey, thanks! Do you want to present your part now?"
    image vicky_stage_1_event_40 = "/vicky/events/stage1/40.webp"
    scene vicky_stage_1_event_40
    vicky "Oh, I didn't do it."
    "There's a long and awkward pause."
    pc "You WHAT?"
    image vicky_stage_1_event_41 = "/vicky/events/stage1/41.webp"
    scene vicky_stage_1_event_41
    vicky "Ugh, not this again..."
    pc "You do realize the presentation's tomorrow, right?"
    vicky "And I couldn't care less!"
    image vicky_stage_1_event_42 = "/vicky/events/stage1/42.webp"
    scene vicky_stage_1_event_42
    pc "But—but—"
    "You try to argue, but she's completely ignoring you now."
    "Frustrated, you head home."
    pc "If you want something done right, do it yourself."
    $ vickystage1event3 = 0
    stop music fadeout 1.0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        $ vicky.weight += 1
        jump freetime
    return


label Vicky_Stage_1_Event_4:
    #Presentation:
    scene player_room
    "After staying up all night, you had a decent write-up of Vicky's part of the presentation."
    scene university_outside
    "It was a little shoddy, sure, but if she didn't like it she should've done it herself."
    image vicky_stage_1_event_43 = "/vicky/events/stage1/43.webp"
    scene vicky_stage_1_event_43
    play music "/music/university.ogg" if_changed
    "You show up to class, tired but prepared."
    pc "Hey Vicky, I typed up your part of the presentation, that way you actually have something to talk about."
    "She doesn't reply."
    pc "No need to thank me or anything..."
    image vicky_stage_1_event_44 = "/vicky/events/stage1/44.webp"
    scene vicky_stage_1_event_44
    vicky "Ummm why is my half so much smaller?"
    pc "Well I didn't have time to go into as much detail. Yknow, since I had to do it overnight?"
    image vicky_stage_1_event_45 = "/vicky/events/stage1/45.webp"
    scene vicky_stage_1_event_45
    "Suddenly, Vicky snatches the notes for your half of the presentation from you."
    pc "Hey that's—"
    call rngteachingscene
    teacher "Vicky, [playername], are you ready to present?"
    "Vicky cuts you off before you can get a word in."
    image vicky_stage_1_event_46 = "/vicky/events/stage1/46.webp"
    scene vicky_stage_1_event_46
    vicky "Yes, Miss Tanwen!"
    "You want to say something, but you also don't want to make a scene."
    image vicky_stage_1_event_47 = "/vicky/events/stage1/47.webp"
    scene vicky_stage_1_event_47
    "Surprisingly, Vicky presents your findings in a mostly eloquent fashion. If she hadn't stolen your work, you'd almost be impressed."
    vicky "—by comparison, feudal societies generally viewed fat as a sign of nobility."
    image vicky_stage_1_event_48 = "/vicky/events/stage1/48.webp"
    scene vicky_stage_1_event_48
    "As she wraps up her part of the presentation, the class gives her a round of applause, much like the one you received from Vicky just yesterday."
    teacher "Very good, Vicky. You get an A! Now, please provide your measurements."
    image vicky_stage_1_event_49 = "/vicky/events/stage1/49.webp"
    scene vicky_stage_1_event_49
    "Vicky's smug look is replaced by confusion at Daisy's request."
    vicky "My...measurements? Like, what does that have to do with the project?"
    teacher "It's just standard procedure for the department, I need to put something down on the form."
    vicky "Ummm okay?"
    image vicky_stage_1_event_50 = "/vicky/events/stage1/50.webp"
    scene vicky_stage_1_event_50
    "Vicky checks and announces her measurements to the class, seemingly without shame."
    $ vicky_stats_visible = 1
    "Vicky has been added to the stats menu."
    teacher "Alright then [playername], it's your turn to present."
    image vicky_stage_1_event_51 = "/vicky/events/stage1/51.webp"
    scene vicky_stage_1_event_51
    "Your presentation doesn't go well. You aren't very familiar with the material, and there isn't much meat to the topic." 
    "You finish rather abruptly as you simply run out of content. You quickly sit back down at your desk."
    call rngteachingscene
    teacher "Is that all?"
    pc "Uhhh yes."
    call rngteachingscene
    teacher "I see...Well, I won't lie [playername], your presentation is lacking. The topic is underdeveloped and your delivery is uncertain. So unfortunately, I'm giving you a C+."
    pc "Yes, Miss Tanwen..."
    call rngteachingscene
    teacher "Cheer up, there's always next time! If you want to improve, you could ask your partner for advice, she's an excellent presenter!"
    "Somehow, that statement doesn't cheer you up."
    pc "Yes, Miss Tanwen..."
    image vicky_stage_1_event_52 = "/vicky/events/stage1/52.webp"
    scene vicky_stage_1_event_52
    "Defeated, you don't really pay attention to the rest of class."
    "You head home."
    $ vickystage1event4 = 0
    stop music fadeout 1.0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        $ vicky.weight += 1
        jump freetime
    return

label Vicky_Stage_2_Event:
    #Stage 2: (This should occur the next time you choose to do a group project with Vicky after the first presentation.)
    if recollection == False:
        $ vicky.stage = 2
        $ vicky.breast_cup = "34G"
        $ vicky.breast_size = 41.2
        $ vicky.ass_size = 46.0
        $ vicky.waist_size = 29.7
        $ vicky.leanweight = 74.5
        $ vicky.weight = 98
    "Against your better judgement, you decide to work with Vicky again."
    play music "/music/university.ogg" if_changed
    scene university_sitdown
    "But before going to join her in the study room, you consider your situation." 
    "You're going to make it clear to her that you refuse to be used like that again."
    scene university_sitdown_front
    "You'll let last time slide, as long as she starts pulling her weight. Otherwise, you'll tell Daisy the truth."
    "Just as you begin to feel certain about taking this course of action, you notice something's up."
    pc "Where's my phone?"
    "You shrug, figuring you must've left it in your locker. You head to join Vicky in the study room."
    "Your face falls as you enter and see what Vicky's doing."
    image vicky_stage_2_event_1 = "/vicky/events/stage2/1.webp"
    scene vicky_stage_2_event_1
    pc "Hey, that's my phone!"
    vicky "Mhm! You should really lock it, yknow."
    pc "What are you—"
    image vicky_stage_2_event_2 = "/vicky/events/stage2/2.webp"
    scene vicky_stage_2_event_2
    vicky "I figured you'd think of telling Miss Tanwen, so I just needed some...insurance!"
    pc "What..."
    image vicky_stage_2_event_3 = "/vicky/events/stage2/3.webp"
    scene vicky_stage_2_event_3
    "Vicky hands you your phone. There's a text conversation open on it with a new contact called 'V <3'." 
    "The convo is made up of screenshot after screenshot of other text conversations along with a bunch of other images."
    image vicky_stage_2_event_4 = "/vicky/events/stage2/4.webp"
    scene vicky_stage_2_event_4
    vicky "There's a lot of personal stuff in here." 
    vicky "Wouldn't it be, like, SO embarrassing if someone knew you were chatting with all these...really big girls?"
    "You scoff at what she's implying."
    pc "Are you trying to blackmail me? Go right ahead, tell everyone about what I'm into, I don't care!"
    vicky "Just a sec, there's more..."
    image vicky_stage_2_event_5 = "/vicky/events/stage2/5.webp"
    scene vicky_stage_2_event_5
    pc "Oh god, not that!"
    pc "Anything but that!"
    image vicky_stage_2_event_6 = "/vicky/events/stage2/6.webp"
    scene vicky_stage_2_event_6
    vicky "That's right! Eesh, imagine if Miss Tanwen—sorry, I mean *Daisy* saw that!"
    pc "What do you want?"
    vicky "Here's the deal: You keep doing all the work on these projects, and anything else I ask you to, and I won't show this to everyone."
    pc "Fine, fine, you win!"
    image vicky_stage_2_event_7 = "/vicky/events/stage2/7.webp"
    scene vicky_stage_2_event_7
    vicky "Great! Now, first I'd like you to take me to lunch."
    pc "Alright..."
    "The two of you head to Bunny Bites."
    image vicky_stage_2_event_8 = "/vicky/events/stage2/8.webp"
    scene vicky_stage_2_event_8
    vicky "I'm totally excited to try this place."
    pc "Can we just get this over with?"
    image vicky_stage_2_event_9 = "/vicky/events/stage2/9.webp"
    scene vicky_stage_2_event_9
    vicky "*tsk* Rude!"
    "Marie soon comes to take your order."
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Oh hey [playername], how's it going? What can I get you today?"
    pc "Hey Marie, nothing for me,thanks. But she'll—"
    image vicky_stage_2_event_10 = "/vicky/events/stage2/10.webp"
    scene vicky_stage_2_event_10
    vicky "Hi, I'm Vicky, you must be Marie. I've, like, heard SO much about you!" 
    vicky "I actually can't decide what to have, what do you recommend?"
    marie "Well if you can't decide, I'd recommend the party platter, it's got a bit of everything."
    vicky "That sound totally perfect, thanks!"
    "Marie heads off to get Vicky's order, which is soon ready."
    image vicky_stage_2_event_11 = "/vicky/events/stage2/11.webp"
    scene vicky_stage_2_event_11
    vicky "Mmm, this looks SO good!"
    image vicky_stage_2_event_12 = "/vicky/events/stage2/12.webp"
    scene vicky_stage_2_event_12
    "It now occurs to you for the first time that Vicky has a lot more appetite than most bitchy rich girls."
    image vicky_stage_2_event_13 = "/vicky/events/stage2/13.webp"
    scene vicky_stage_2_event_13
    "Quite a lot more, actually..."
    image vicky_stage_2_event_14 = "/vicky/events/stage2/14.webp"
    scene vicky_stage_2_event_14
    "She makes quick work of the generous platter."
    image vicky_stage_2_event_15 = "/vicky/events/stage2/15.webp"
    scene vicky_stage_2_event_15
    vicky "Oooooh, that was amazing..."
    pc "Great, are we done here?"
    image vicky_stage_2_event_16 = "/vicky/events/stage2/16.webp"
    scene vicky_stage_2_event_16
    vicky "Come on, don't pretend you didn't like that. I know you like watching pretty girls eat until they're nice and full. And, honestly..."
    vicky "I do, too."
    pc "What?"
    image vicky_stage_2_event_17 = "/vicky/events/stage2/17.webp"
    scene vicky_stage_2_event_17
    vicky "You see [playername], your presentation gave me a lot to think about. I want to be like those nobles." 
    vicky "No, I *deserve* to be like those nobles. I deserve to be waited on and paid tribute to. I deserve to be kept fed and satisfied."
    image vicky_stage_2_event_18 = "/vicky/events/stage2/18.webp"
    scene vicky_stage_2_event_18
    vicky "And you, you're my loyal subject. It's your job to keep me fed and satisfied, even if it means you have to go hungry."
    "You think to yourself:"
    pc "God, why'd she have to make that sound so hot?"
    image vicky_stage_2_event_19 = "/vicky/events/stage2/19.webp"
    scene vicky_stage_2_event_19
    "Vicky laughs."
    vicky "That look tells me all I need to know."
    image vicky_stage_2_event_20 = "/vicky/events/stage2/20.webp"
    scene vicky_stage_2_event_20
    vicky "Later, loser."
    "Once she's gone, you pay the bill and head home."
    if recollection == False:
        $ money -= 10
    "Vicky can now visit Bunny Bites."
    "This is Vicky's final event in this update, her story will continue next update."
    $ vickystage2event = 0
    stop music fadeout 1.0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        $ vicky.weight += 1
        jump freetime
    return
