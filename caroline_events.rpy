label Caroline_study_1:
    ###After lesson###
    "After Daisy dismisses the class to work on their projects, you decide to work with Caroline."
    ###In project room###
    play music "/music/caroline.ogg" if_changed
    image caroline_study_arrive = "/caroline/[caroline.stage]/study_arrive.webp"
    scene caroline_study_arrive
    "Walking into the room you see Caroline going through the supplies Daisy left out for you."
    image caroline_study_sitting = "/caroline/[caroline.stage]/study_sitting.webp"
    scene caroline_study_sitting
    pc "Hi Caroline."
    caroline "Hey, I was just reading through the project."
    if caroline.stage >= 3:
        caroline "Seems like this week's macro is Sugar."
    else:
        caroline "Seems like this week's macro is Salt intake."
    pc "You still want to do the eating like last time?"
    if caroline.stage >= 4:
        caroline "Yeah, I guess. Although this isn't really how I pictured myself getting back into shape."
    else:
        caroline "Yeah, that still works out the best for me."
    image caroline_study_eat1 = "/caroline/[caroline.stage]/study_eat1.webp"
    scene caroline_study_eat1
    "Grabbing the first snack, she tears the packet open and starts eating."
    if caroline.stage >= 4:
        "Nibbling at the corner of the candy, she seems less than enthusiastic about this."
        image caroline_study_eat2 = "/caroline/[caroline.stage]/study_eat2.webp"
        scene caroline_study_eat2
        "Taking a few more bites she moves onto the next one, while handing you the half full packet."
        "Trying to estimate how much she had eaten, you note down the nutritional information."
        image caroline_study_eat3 = "/caroline/[caroline.stage]/study_eat3.webp"
        scene caroline_study_eat3
        "One by one you repeat the process, Caroline taking a few bites and you writing."
    else:
        caroline "Mmm, I will need to ask Daisy where she gets these from. They are delicious."
        "Handing you the wrapper, you note down the nutritional information."
        image caroline_study_eat2 = "/caroline/[caroline.stage]/study_eat2.webp"
        scene caroline_study_eat2
        "One by one you repeat the process, Caroline eating and you writing."
        image caroline_study_talk2 = "/caroline/[caroline.stage]/study_talk2.webp"
        scene caroline_study_talk2
        caroline "I wish there was a drink with these boxes though."
        pc "Maybe we can ask Daisy to add one."
        if caroline.stage >= 3:
            caroline "Yeah, although I'll be fine. Just all the food is making me thirsty."
        else:
            caroline "Yeah, although I'll be fine. Just all the salt is making me thirsty."
    "Finishing off the supplies, Caroline helps you tidy up the mess of wrappers."
    image caroline_study_end = "/caroline/[caroline.stage]/study_end.webp"
    scene caroline_study_end
    caroline "Looks like we are done."
    if caroline.stage >= 4:
        caroline "Are you ok if I head out a bit early?"
        pc "Yeah sure."
        pc "Nothing out of the ordinary though."
        image caroline_study_leave = "/caroline/[caroline.stage]/study_leave.webp"
        scene caroline_study_leave
        caroline "Perfect, I'll see you next time."
    else:
        caroline "How do the numbers look?"
        pc "Not sure yet, still pretty early."
        pc "Nothing out of the ordinary though."
        caroline "Great. Are you ok with the write up?"
        pc "Yep, that is all fine with me."
        image caroline_study_leave = "/caroline/[caroline.stage]/study_leave.webp"
        scene caroline_study_leave
        caroline "Perfect, I need to get going but I'll see you next time."
    pc "Bye Caroline."
    "Collecting your things, you head home."
    stop music fadeout 1.0
    $ caroline_study_times = 1
    $ caroline.weight += 0.2
    return


label Caroline_study_2:
    ###After lesson###
    "After Daisy dismisses the class to work on their projects, you decide to work with Caroline."
    ###In project room###
    play music "/music/caroline.ogg" if_changed
    image caroline_study_arrive2 = "/caroline/[caroline.stage]/study_arrive2.webp"
    scene caroline_study_arrive2
    "Walking into the room you see Caroline going through the supplies Daisy left out for you."
    image caroline_study_sitting2 = "/caroline/[caroline.stage]/study_sitting2.webp"
    scene caroline_study_sitting2
    pc "Hi Caroline."
    if caroline.stage >= 4:
        caroline "Hey, Daisy has given us a few more things today."
        caroline "You ready to get started, I need to see my coach after this."
        pc "Yeah sure, whatever you need."
        image caroline_study_eat1 = "/caroline/[caroline.stage]/study_eat1.webp"
        scene caroline_study_eat1
        "Grabbing the first snack, she tears the packet open and takes a few bites."
        "Handing you the wrapper, you note down the nutritional information."
        image caroline_study_eat2 = "/caroline/[caroline.stage]/study_eat2.webp"
        scene caroline_study_eat2
        "Grabbing another snack, she hands you the wrapper with half the contents still inside."
        image caroline_study_eat4 = "/caroline/[caroline.stage]/study_eat4.webp"
        scene caroline_study_eat4
        "One by one you repeat the process, Caroline eating and you writing."
        "Finishing off the supplies, Caroline helps you tidy up the mess of wrappers."
        image caroline_study_end = "/caroline/[caroline.stage]/study_end.webp"
        scene caroline_study_end
        pc "I think that is everything, if you need to get going?"
        caroline "Great. Are you ok with the write up?"
        pc "Yep, that is all fine with me."
        image caroline_study_leave = "/caroline/[caroline.stage]/study_leave.webp"
        scene caroline_study_leave
        caroline "Perfect, See you next time."
    else:
        caroline "Hey, I was just reading through the project."
        caroline "Seems like Daisy has been a bit more generous today."
        pc "You still want to do the eating part like last time?"
        caroline "Yeah, that still works out the best for me."
        image caroline_study_eat1 = "/caroline/[caroline.stage]/study_eat1.webp"
        scene caroline_study_eat1
        "Grabbing the first snack, she tears the packet open and starts eating."
        image caroline_study_talk1 = "/caroline/[caroline.stage]/study_talk1.webp"
        scene caroline_study_talk1
        caroline "So, how is the project from your point of view?"
        "Handing you the wrapper, you note down the nutritional information."
        pc "Seems pretty simple, write down the numbers, analyse the data, present changes to the class."
        caroline "Yeah, honestly I think I could do with something a bit more complex."
        image caroline_study_eat2 = "/caroline/[caroline.stage]/study_eat2.webp"
        scene caroline_study_eat2
        "Grabbing another snack, she hands you the wrapper again."
        pc "More complex?"
        image caroline_study_talk3 = "/caroline/[caroline.stage]/study_talk3.webp"
        scene caroline_study_talk3
        caroline "Yeah, I mean I am just eating snacks."
        caroline "Not that I should complain about getting an easy project."
        caroline "Especially once I get back to training and have less time again."
        image caroline_study_eat4 = "/caroline/[caroline.stage]/study_eat4.webp"
        scene caroline_study_eat4
        "One by one you repeat the process, Caroline eating and you writing."
        "Finishing off the supplies, Caroline helps you tidy up the mess of wrappers."
        image caroline_study_end = "/caroline/[caroline.stage]/study_end.webp"
        scene caroline_study_end
        caroline "Oooh, definitely a bit fuller today."
        pc "Seems like we are finished though."
        caroline "Great. Are you ok with the write up?"
        pc "Yep, that is all fine with me."
        image caroline_study_leave = "/caroline/[caroline.stage]/study_leave.webp"
        scene caroline_study_leave
        caroline "Perfect, I need to get going but I'll see you next time."
    pc "Bye Caroline."
    "Collecting your things, you head home."
    stop music fadeout 1.0
    $ caroline_study_times = 2
    $ caroline.weight += 0.3
    return


label Caroline_study_3:
    ###After lesson###
    "After Daisy dismisses the class to work on their projects, you decide to work with Caroline."
    ###In project room###
    play music "/music/caroline.ogg" if_changed
    image caroline_study_arrive3 = "/caroline/[caroline.stage]/study_arrive3.webp"
    scene caroline_study_arrive3
    "Walking into the room you see Caroline going through the supplies."
    if caroline.stage >= 4:
        image caroline_study_sitting3 = "/caroline/[caroline.stage]/study_sitting3.webp"
        scene caroline_study_sitting3
        caroline "Seems like Daisy really wants to see some changes in our data from today."
        pc "Hey, what do you mean?"
        caroline "The size of this box and all the treats inside it."
        image caroline_study_talk1 = "/caroline/[caroline.stage]/study_talk1.webp"
        scene caroline_study_talk1
        caroline "Guess I am going to have to try and eat them all, since that is her expectation."
        pc "Are you ok with that?"
        caroline "Yeah, I can just work out extra hard."
        image caroline_study_eat1 = "/caroline/[caroline.stage]/study_eat1.webp"
        scene caroline_study_eat1
        "Grabbing the first snack, she tears the packet open and starts eating."
        "Handing you the wrapper, you note down the nutritional information."
        image caroline_study_talk3 = "/caroline/[caroline.stage]/study_talk3.webp"
        scene caroline_study_talk3
        caroline "Do you think this will give us much to work with tomorrow?"
        pc "Maybe, the data isn't quite as good as previous weeks."
        pc "But there isn't anything to worry about."
        caroline "Great, I'm sure it is more about the process than the results anyway."
        image caroline_study_eat2 = "/caroline/[caroline.stage]/study_eat2.webp"
        scene caroline_study_eat2
        "Grabbing another snack, she hands you the wrapper again."
        pc "Have you noticed any changes in yourself?"
        image caroline_study_talk2 = "/caroline/[caroline.stage]/study_talk2.webp"
        scene caroline_study_talk2
        caroline "I've been feeling a bit more anxious."
        caroline "But I don't know if that is too much sugar, or nerves about starting to perform again."
        pc "I didn't take you as the nervous type."
        caroline "I'm not normally, guess it is just weird to have been away from working out like that before."
        caroline "I've never been injured this long before."
        image caroline_study_eat3 = "/caroline/[caroline.stage]/study_eat3.webp"
        scene caroline_study_eat3
        "One by one you repeat the process, Caroline eating and you writing."
        image caroline_study_eat4 = "/caroline/[caroline.stage]/study_eat4.webp"
        scene caroline_study_eat4
        "With the bigger box, it takes noticeably longer and Caroline seems less enthusiastic than usual."
        "Finishing off the supplies, Caroline helps you tidy up the mess of wrappers."
        image caroline_study_end_stuffed = "/caroline/[caroline.stage]/study_end_stuffed.webp"
        scene caroline_study_end_stuffed
        caroline "I'm going to have such a sugar crash later."
        caroline "I didn't think I was going to miss eating loads of salty things."
        pc "I think that is everything for today."
        image caroline_study_leave_stuffed = "/caroline/[caroline.stage]/study_leave_stuffed.webp"
        scene caroline_study_leave_stuffed
        caroline "Perfect, I'll see you for our presentation tomorrow."
    else:
        "Looks like Daisy has given you a bigger box today."
        image caroline_study_sitting3 = "/caroline/[caroline.stage]/study_sitting3.webp"
        scene caroline_study_sitting3
        pc "Hi Caroline."
        caroline "Hey, ready to continue where we left off last time?"
        caroline "Seems like Daisy has been a bit more generous today, thankfully there is even a drink in this one."
        pc "Yeah I am ready, keeping the same plan as last time?"
        caroline "Yeah, why change what isn't broken."
        image caroline_study_eat1 = "/caroline/[caroline.stage]/study_eat1.webp"
        scene caroline_study_eat1
        "Grabbing the first snack, she tears the packet open and starts eating."
        "Handing you the wrapper, you note down the nutritional information."
        image caroline_study_talk3 = "/caroline/[caroline.stage]/study_talk3.webp"
        scene caroline_study_talk3
        caroline "Do you think we will be ready to give an update tomorrow?"
        pc "Yeah, it is only a quick presentation about how things are going."
        pc "Nothing to worry about."
        caroline "Great."
        image caroline_study_eat2 = "/caroline/[caroline.stage]/study_eat2.webp"
        scene caroline_study_eat2
        "Grabbing another snack, she hands you the wrapper again."
        pc "Have you noticed any changes in yourself?"
        image caroline_study_talk2 = "/caroline/[caroline.stage]/study_talk2.webp"
        scene caroline_study_talk2
        caroline "Nope, been drinking more water but other than that no major changes."
        pc "I can make a note of it anyway."
        image caroline_study_eat3 = "/caroline/[caroline.stage]/study_eat3.webp"
        scene caroline_study_eat3
        "One by one you repeat the process, Caroline eating and you writing."
        image caroline_study_eat4 = "/caroline/[caroline.stage]/study_eat4.webp"
        scene caroline_study_eat4
        "With the bigger box, it takes noticeably longer and Caroline seems less enthusiastic than usual."
        "Finishing off the supplies, Caroline helps you tidy up the mess of wrappers."
        image caroline_study_talk2 = "/caroline/[caroline.stage]/study_talk2.webp"
        scene caroline_study_talk2
        if caroline.stage >= 3:
            caroline "Ughh, that was too much, I need to wash it down with a drink."
        else:
            caroline "Ughh, my tongue feels so dry."
            caroline "I look forwards to moving onto a different Macro soon."
        image caroline_study_drink = "/caroline/[caroline.stage]/study_drink.webp"
        scene caroline_study_drink
        "Grabbing the large drink, Caroline sucks it dry in one go."
        caroline "That is better."
        pc "I think that is everything for today."
        image caroline_study_end_stuffed = "/caroline/[caroline.stage]/study_end_stuffed.webp"
        scene caroline_study_end_stuffed
        caroline "Great. Are you ok with the write up?"
        pc "Yep, that is all fine with me."
        image caroline_study_leave_stuffed = "/caroline/[caroline.stage]/study_leave_stuffed.webp"
        scene caroline_study_leave_stuffed
        caroline "Perfect, I'll see you next time."
    pc "Bye Caroline."
    "Collecting your things, you head home."
    stop music fadeout 1.0
    $ caroline_study_times = 3
    $ caroline.weight += 0.5
    return

label Caroline_study_4:
    ##Friday lesson##
    call rngteachingscene
    teacher "Before we get to the main portion of today's lesson, I believe someone has a short presentation they would like to give."
    teacher "Caroline and [playername], would you mind coming up to the front please?"
    image caroline_study_presentation1 = "/caroline/[caroline.stage]/study_presentation1.webp"
    scene caroline_study_presentation1
    if caroline.stage >= 3:
        "Going up to the front, you and Caroline begin to talk through your work on increased sugar consumption."
    else:
        "Going up to the front, you and Caroline begin to talk through your work on increased sodium consumption."
    "Given Caroline had done all the eating, you let her take the lead on talking about changes she has seen."
    image caroline_study_presentation2 = "/caroline/[caroline.stage]/study_presentation2.webp"
    scene caroline_study_presentation2
    "Talking about the snacks and her diet, Caroline does a couple of poses to show off her body."
    image caroline_study_presentation3 = "/caroline/[caroline.stage]/study_presentation3.webp"
    scene caroline_study_presentation3
    "It seems like her dancing background puts her at ease in front of the class and it seems almost effortless for her."
    image caroline_study_presentation1 = "/caroline/[caroline.stage]/study_presentation1.webp"
    scene caroline_study_presentation1
    if persistent.imperial:
        $ imperialweight = (caroline.weight * 2.2)
        caroline "My weight is currently [imperialweight:.02f]lbs."
    else:
        caroline "My weight is currently [caroline.weight:.02f]kg."
    if caroline.stage >= 4:
        caroline "That has increased less than previous weeks, I think that will be down to my increased activity."
    else:
        caroline "That has increased, potentially due to a lack of exercise on my part and that is something we will keep in mind moving forwards."
    if persistent.imperial:
        caroline "As well as my weight, my belly has increased to [caroline.waist_size:.02f] inches, my butt is [caroline.ass_size:.02f] inches."
        caroline "Equally, my chest has grown to [caroline.breast_size:.02f] inches which makes me a [caroline.breast_cup] cup."
    else:
        $ metricwaist_size = (caroline.waist_size * 2.54)
        $ metricbreast_size = (caroline.breast_size * 2.54)
        $ metricass_size = (caroline.ass_size * 2.54)
        caroline "As well as my weight, my belly has increased to [metricwaist_size:.02f] centimeters, my butt is [metricass_size:.02f] centimeters."
        caroline "Equally, my chest has grown to [metricbreast_size:.02f] centimeters which makes me a [caroline.breast_cup] cup."
    if caroline.stage >= 4:
        caroline "So there have been some changes, but they have been at the lower end of our estimates."
    else:
        caroline "So there have been some changes, but all within our estimates."
    teacher "Excellent job, both of you. I look forward to seeing your project continue to provide interesting results."
    teacher "You can both return to your seats."
    ###Regular feeding class###
    return

label Caroline_Intro1:
    #DAISY STAGE3
    ## Event 0.1 Daisy stage / college event of your choosing.##
    ##Daisy existing lesson dialogue ##
    image caroline_stage1_17 = "/caroline/events/stage1/17.webp"
    scene caroline_stage1_17
    teacher "Next, let's discuss the real world impacts of…"
    image caroline_stage1_18 = "/caroline/events/stage1/18.webp"
    scene caroline_stage1_18
    "Stopping mid sentence Daisy is distracted as one of your classmates raises their hand."
    image caroline_stage1_19 = "/caroline/events/stage1/19.webp"
    scene caroline_stage1_19
    teacher "Oh, that is right."
    teacher "You are excused Caroline."
    image caroline_stage1_20 = "/caroline/events/stage1/20.webp"
    scene caroline_stage1_20
    "Standing, your classmate grabs her belongings and hurries out of the class."
    caroline "Thank you miss Tanwen."
    teacher "No problem and good luck."
    image caroline_stage1_21 = "/caroline/events/stage1/21.webp"
    scene caroline_stage1_21
    teacher "Now, where was I?"
    "Whispered conversations quickly start up after the break in teaching."
    fs "What, how come she gets to leave early."
    ms "I think she is on a sports scholarship, apparently she is a professional ballet dancer?"
    fs "They give scholarships for that? I would have tried harder in physical ed if I knew I could have gotten out of classes."
    image caroline_stage1_22 = "/caroline/events/stage1/22.webp"
    scene caroline_stage1_22
    teacher "Excuse me, can I get your attention back on the topic at hand please."
    "Continuing her lesson, the rest of it goes by undisrupted."
    $ carolineintro1 = 0
    return

label Caroline_Intro2:
    ##0.2 Next class or a couple later - depending on how fast you want it to be##
    scene university_sitdown
    "Arriving to class a little bit early, you take your seat."
    image caroline_stage1_1 = "/caroline/events/stage1/1.webp"
    scene caroline_stage1_1
    "Taking out your notepad, you can hear muffled rock music coming from somewhere nearby."
    image caroline_stage1_2 = "/caroline/events/stage1/2.webp"
    scene caroline_stage1_2
    "Checking it isn’t coming from your phone, you quickly discover it is coming from Caroline sitting next to you."
    pc "That sounds good, who is it?"
    image caroline_stage1_3 = "/caroline/events/stage1/3.webp"
    scene caroline_stage1_3
    "Jumping a little bit in surprise, Caroline quickly removes her headphones looking a bit sheepish."
    caroline "I’m sorry, what did you say?"
    pc "The music, I was just wondering who it was?"
    caroline "Oh, I don't know. I think I downloaded the wrong album."
    caroline "Too heavy for me, I guess I just didn’t notice when it started playing."
    image caroline_stage1_4 = "/caroline/events/stage1/4.webp"
    scene caroline_stage1_4
    "Turning off her phone she quickly throws it into her bag."
    ###Existing class / lesson##
    $ carolineintro2 = 0
    return

label Caroline_Intro3:
    ##0.3 Next class or a couple later - depending on how fast you want it to be##
    scene university_sitdown
    "Arriving to class a little bit early, you take your usual seat."
    image caroline_stage1_5 = "/caroline/events/stage1/5.webp"
    scene caroline_stage1_5
    "Getting ready for class, a slightly flustered looking Caroline rushes in."
    caroline "Am I late?"
    pc "No, Daisy isn’t here yet."
    image caroline_stage1_6 = "/caroline/events/stage1/6.webp"
    scene caroline_stage1_6
    caroline "Oh, good."
    image caroline_stage1_7 = "/caroline/events/stage1/7.webp"
    scene caroline_stage1_7
    "Sitting down next to you in a hurry, Caroline fumbles her bag sending several items to scatter across the floor from her bag."
    image caroline_stage1_8 = "/caroline/events/stage1/8.webp"
    scene caroline_stage1_8
    caroline "Shoot, sorry about that."
    pc "No problem, here let me help."
    image caroline_stage1_9 = "/caroline/events/stage1/9.webp"
    scene caroline_stage1_9
    "Kneeling down you help gather Caroline’s items."
    image caroline_stage1_10 = "/caroline/events/stage1/10.webp"
    scene caroline_stage1_10
    "Picking up the last item, it seems to be a tattoo magazine."
    pc "I didn’t take you to be into this sort of thing?"
    image caroline_stage1_11 = "/caroline/events/stage1/11.webp"
    scene caroline_stage1_11
    caroline "Oh, I…I'm not."
    caroline "That’s not mine, I am just…holding onto it for a friend."
    pc "Oh ok, some of those designs look pretty cool though."
    image caroline_stage1_12 = "/caroline/events/stage1/12.webp"
    scene caroline_stage1_12
    caroline "Yeah totally!"
    image caroline_stage1_13 = "/caroline/events/stage1/13.webp"
    scene caroline_stage1_13
    caroline "I mean, I guess they might look ok if you are into that sort of thing…which I am not."
    caroline "Thanks though."
    pc "No problem."
    pc "So, did your practice overrun, you are usually one of the first ones here?"
    image caroline_stage1_14 = "/caroline/events/stage1/14.webp"
    scene caroline_stage1_14
    caroline "What?"
    caroline "Oh, no I just lost track of time this morning."
    caroline "The clock in my shower stopped working."
    pc "You have a clock in your shower?"
    image caroline_stage1_15 = "/caroline/events/stage1/15.webp"
    scene caroline_stage1_15
    caroline "Yeah, don't you?"
    pc "No."
    image caroline_stage1_16 = "/caroline/events/stage1/16.webp"
    scene caroline_stage1_16
    caroline "Oh ok…well punctuality is key and so is being organised."
    ###Existing class / lesson##
    $ carolineintro3 = 0
    return

label Caroline_Intro4:
    ##0.4 End of Daisy event where she introduces group projects (if there is one, I cant quite remember how they are introduced, is it Hari stage 1 rather than something Daisy says?##
    "After announcing the group projects, Daisy goes through a list partnering people up."
    call rngteachingscene from _call_rngteachingscene_279
    "But as she finishes, you still don't think you heard your name being called, maybe you missed it?"
    "Gathering up your things, you head to the front to check with Daisy who your partner was."
    image caroline_stage1_23 = "/caroline/events/stage1/23.webp"
    scene caroline_stage1_23
    "Walking up you can see a couple of classmates ahead of you, it seems Caroline and Vicky were talking to her already."
    image caroline_stage1_24 = "/caroline/events/stage1/24.webp"
    scene caroline_stage1_24
    teacher "Is it really that serious?"
    vicky "It is."
    image caroline_stage1_25 = "/caroline/events/stage1/25.webp"
    scene caroline_stage1_25
    teacher "Well in that case I guess I have no other choice if you two won't work together."
    teacher "I'll see if I can find you some new partners."
    image caroline_stage1_26 = "/caroline/events/stage1/26.webp"
    scene caroline_stage1_26
    caroline "Thanks Miss Tanwen."
    teacher "No problem, I expect no more problems from you both."
    image caroline_stage1_27 = "/caroline/events/stage1/27.webp"
    scene caroline_stage1_27
    vicky "There won't be."
    image caroline_stage1_28 = "/caroline/events/stage1/28.webp"
    scene caroline_stage1_28
    "Going back to grab their things, they leave you with Daisy at the front."
    image caroline_stage1_29 = "/caroline/events/stage1/29.webp"
    scene caroline_stage1_29
    teacher "Hi [playername], how can I help?"
    pc "I was just wondering who my partner would be, I don't think I heard my name?"
    image caroline_stage1_30 = "/caroline/events/stage1/30.webp"
    scene caroline_stage1_30
    teacher "Sorry, that is my fault."
    teacher "I was just finalising yours, I have something planned I think you are especially suitable for."
    teacher "Although I might need to rethink it given two of your classmates are also now missing partners."
    pc "Is there anything I can do to help?"
    image caroline_stage1_31 = "/caroline/events/stage1/31.webp"
    scene caroline_stage1_31
    teacher "Not unless you want to do three times the work and be all their partners?"
    pc "That sounds fine to me."
    image caroline_stage1_32 = "/caroline/events/stage1/32.webp"
    scene caroline_stage1_32
    teacher "Really, it will be a lot of work and I know you have other responsibilities."
    pc "Daisy, this is the only class I take here."
    pc "I have plenty of time."
    teacher "Thank you, that takes a lot off my plate."
    ##Flirty look###
    image caroline_stage1_33 = "/caroline/events/stage1/33.webp"
    scene caroline_stage1_33
    teacher "Maybe I can do something to repay you for all your effort in helping me out."
    ##back to normal - unless you want to add even more here###
    image caroline_stage1_34 = "/caroline/events/stage1/34.webp"
    scene caroline_stage1_34
    teacher "For now though, I think I might have something planned for those two."
    teacher "Hopefully it gives them a creative outlet for their tensions with each other."
    "You are not sure what that means, but given Daisy's usual approach to teaching you are excited to see it."
    image caroline_stage1_35 = "/caroline/events/stage1/35.webp"
    scene caroline_stage1_35
    teacher "Here you have your assigned partner for now."
    "Daisy hands you a paper that has you partner up with Hari."
    teacher "That is all for today, unless you had any other questions?"
    pc "No, I can't think of anything."
    pc "Thanks Daisy."
    teacher "See you tomorrow [playername]."
    $ carolineintro4 = 0
    return

label Caroline_Stage_1_Event:
    ###Caroline looking at her phone / ignoring us.###
    play music "/music/university.ogg" if_changed
    image caroline_stage1_36 = "/caroline/events/stage1/36.webp"
    scene caroline_stage1_36
    "Arriving at your next class, you see Caroline sitting in her usual seat."
    pc "You're here early again, you must really like this class."
    ###Caroline looking at us###
    image caroline_stage1_37 = "/caroline/events/stage1/37.webp"
    scene caroline_stage1_37
    caroline "Sorry, did you say something?"
    pc "Nothing important…"
    caroline "Oh, ok..."
    "Leaving her to whatever it is she was doing, you get your things out for class."
    ##Daisy walks in##
    image caroline_stage1_38 = "/caroline/events/stage1/38.webp"
    scene caroline_stage1_38
    teacher "Hello you two."
    caroline "Good morning Miss Tanwen."
    image caroline_stage1_39 = "/caroline/events/stage1/39.webp"
    scene caroline_stage1_39
    teacher "No need to be so formal, you can call me Daisy."
    teacher "Actually, it is good to have you both here."
    teacher "I was going to pair you both together for the group projects."
    image caroline_stage1_40 = "/caroline/events/stage1/40.webp"
    scene caroline_stage1_40
    caroline "Do I have too, can't I just do it alone?"
    teacher "That defeats the purpose of group projects, don't you think?"
    teacher "Besides, I have already helped you out once."
    caroline "Sorry Miss, I'm happy to work with [playername]."
    teacher "Great, it should be an interesting project for you both to get involved with."
    image caroline_stage1_41 = "/caroline/events/stage1/41.webp"
    scene caroline_stage1_41
    "Giving you a lingering look, you get the idea it is more of a comment for you than Caroline."
    ##Class mates arriving.”
    image caroline_stage1_42 = "/caroline/events/stage1/42.webp"
    scene caroline_stage1_42
    teacher "Anyway, I need to get set up for today's lesson."
    teacher "All the information will be with your equipment when we all split up for the projects later."

    #[Regular lesson]
    call Daisy_Class_Normal

    ##After lesson###
    "After Daisy dismisses the class to work on their projects, you agree to work with Caroline today."
    ###Other class room / project room###
    play music "/music/caroline.ogg" if_changed
    image caroline_stage1_43 = "/caroline/events/stage1/43.webp"
    scene caroline_stage1_43
    "Walking into the small study room Caroline takes a seat while you go over the instructions."
    image caroline_stage1_44 = "/caroline/events/stage1/44.webp"
    scene caroline_stage1_44
    pc "Looks like we are doing a project similar to what Daisy is doing, just on a smaller scale."
    ## Caroline on her phone sitting back in her chair kind of ignoring you, maybe with a single headphone in?##
    caroline "Oh…ok."
    pc "We have a bunch of stuff in here this week we are supposed to eat."
    caroline "Sure…"
    pc "Apparently this project involves counting calories of everything we eat and then monitoring their impact on us physically or mentally."
    image caroline_stage1_45 = "/caroline/events/stage1/45.webp"
    scene caroline_stage1_45
    caroline "Should be easy, my parents have been tracking my calories since I was like 8."
    pc "Really, that sounds kind of intense?"
    ###First time Caroline pays attention, looking at us.###
    image caroline_stage1_46 = "/caroline/events/stage1/46.webp"
    scene caroline_stage1_46
    caroline "It's not that bad."
    caroline "Besides, it takes dedication to be a professional athlete."
    caroline "I wouldn't be where I am today without them pushing me and making the sacrifices they have."
    pc "True, still sounds kind of intense to me."
    image caroline_stage1_47 = "/caroline/events/stage1/47.webp"
    scene caroline_stage1_47
    caroline "I guess that means you won't ever make it as a professional ballet dancer."
    pc "Damn, I just bought the dress."
    image caroline_stage1_48 = "/caroline/events/stage1/48.webp"
    scene caroline_stage1_48
    pause
    ##Caroline smiling at us.##
    ###Caroline's friend turns up - Caroline goes back to looking serious###
    image caroline_stage1_49 = "/caroline/events/stage1/49.webp"
    scene caroline_stage1_49
    lucy "Ready to go K?"
    image caroline_stage1_50 = "/caroline/events/stage1/50.webp"
    scene caroline_stage1_50
    caroline "Hi Lucy, I'll be out in a minute."
    lucy "I'll wait out here."
    ###Lucy leaves###
    image caroline_stage1_51 = "/caroline/events/stage1/51.webp"
    scene caroline_stage1_51
    caroline "Anyway, should we get started?"
    pc "Sure, what do you fancy?"
    image caroline_stage1_52 = "/caroline/events/stage1/52.webp"
    scene caroline_stage1_52
    caroline "These look good."
    "Grabbing one of the snacks Caroline takes a few bites before putting it back in the box."
    image caroline_stage1_53 = "/caroline/events/stage1/53.webp"
    scene caroline_stage1_53
    "Grabbing another, she takes a few more bites before moving on again."
    pc "I am not sure if that is what Daisy had in mind."
    image caroline_stage1_54 = "/caroline/events/stage1/54.webp"
    scene caroline_stage1_54
    caroline "It doesn't really matter, as long as we track everything right?"
    pc "I guess, I just don't really know how much of each thing has been eaten."
    image caroline_stage1_55 = "/caroline/events/stage1/55.webp"
    scene caroline_stage1_55
    "Ignoring you, Caroline continues to take bites out of everything, she seems to be in a hurry."
    "Re-wrapping the last partially eaten snack, Caroline throws it back into the box."
    image caroline_stage1_56 = "/caroline/events/stage1/56.webp"
    scene caroline_stage1_56
    caroline "Mmm, they were good."
    caroline "Are we done for today?"
    pc "Uhh...."
    image caroline_stage1_57 = "/caroline/events/stage1/57.webp"
    scene caroline_stage1_57
    caroline "Great, I'll finish up my side of things later."
    "Standing up Caroline quickly packs her things away."
    "You can't help but feel like you are missing something."
    pc "Is everything ok?"
    image caroline_stage1_58 = "/caroline/events/stage1/58.webp"
    scene caroline_stage1_58
    caroline "With the project?"
    pc "No with you, or I guess about working with me?"
    pc "You didn't seem very happy about it when Daisy told us."
    image caroline_stage1_59 = "/caroline/events/stage1/59.webp"
    scene caroline_stage1_59
    caroline "Oh sorry, no I just have a lot on at the minute and we don't really know each other."
    caroline "I didn't want anything upsetting my routine before a big contest."
    pc "Oh ok."
    image caroline_stage1_60 = "/caroline/events/stage1/60.webp"
    scene caroline_stage1_60
    caroline "And right now, I need to get to practice."
    caroline "I'll see you later [playername]."
    image caroline_stage1_61 = "/caroline/events/stage1/61.webp"
    scene caroline_stage1_61
    "Watching her leave the room you still aren't sure if you have enough to go on in terms of the project."
    "However, it is only the first day so you can probably make up for it later if you need to."
    "Grabbing the rubbish, you pack it away and head home."
    $ carolinestage1event = 0
    stop music fadeout 1.0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        $ daycount4 = 0
        jump freetime
    return

label Caroline_Stage_1_Event_2:
    ##Option to work with Caroline at college###
    scene player_room
    "You make your way down to the university."
    scene university_outside
    "Ready to work together with your new group project partner, you head to the study room."
    ###Other class room / project room###
    play music "/music/caroline.ogg" if_changed
    image caroline_stage1_62 = "/caroline/events/stage1/62.webp"
    scene caroline_stage1_62
    "Walking into the small study room you go over the instructions from Daisy again."
    image caroline_stage1_63 = "/caroline/events/stage1/63.webp"
    scene caroline_stage1_63
    pc "Seems like the same process as last time."
    ## Caroline stood behind her chair doing some stretches##
    pc "Did you manage to get everything written up after the last time?"
    image caroline_stage1_64 = "/caroline/events/stage1/64.webp"
    scene caroline_stage1_64
    caroline "Mmm, yeah I guess."
    pc "You guess?"
    caroline "I mean yeah, I wrote everything down."
    image caroline_stage1_65 = "/caroline/events/stage1/65.webp"
    scene caroline_stage1_65
    caroline "Do you think my hair looks good like this?"
    ##Showing off her hair, maybe with a new ribbon or something in it?##
    pc "Um...yeah."
    image caroline_stage1_66 = "/caroline/events/stage1/66.webp"
    scene caroline_stage1_66
    caroline "That doesn't sound very sure."
    pc "Sorry, I just hadn't really thought about it much."
    pc "Anyway, for the project how did you want to do it this time?"
    ##Caroline doing a pose.##
    image caroline_stage1_67 = "/caroline/events/stage1/67.webp"
    scene caroline_stage1_67
    "Not getting any response, it seems Caroline is more interested in running through her routine than actually doing the work."
    pc "Caroline?"
    image caroline_stage1_68 = "/caroline/events/stage1/68.webp"
    scene caroline_stage1_68
    caroline "Mmm, yeah?"
    pc "The project?"
    caroline "Whatever you want."
    pc "I don't want to sound mean, but this is supposed to be a group project."
    pc "And it kind of feels like you don't want to be here or to help in any way."
    ###Caroline looking embarrassed / sorry.###
    image caroline_stage1_69 = "/caroline/events/stage1/69.webp"
    scene caroline_stage1_69
    caroline "Oh…I'm sorry."
    caroline "I didn't mean to be a bad partner."
    caroline "To be honest, I am kind of surprised you are taking it this seriously."
    pc "You don't think this is important?"
    caroline "No I didn't mean that…I…"
    ###Caroline sitting down opposite you.###
    image caroline_stage1_70 = "/caroline/events/stage1/70.webp"
    scene caroline_stage1_70
    caroline "Please don't take this the wrong way, but you don't strike me as someone who wants to do well in college."
    caroline "I guess, I just assumed you wouldn't care about it and so I didn't either."
    caroline "I've been in too many group's where I have been the one forced to do all the work and didn't…don't have the time to do that now."
    caroline "Although now I realise I have become the person who causes the issues, so I am sorry about that."
    "Her earnest apology has caught you a little off guard and you are not sure what to say."
    pc "It's ok, I guess I'm not really a straight A student, but I still want to try and do well."
    image caroline_stage1_71 = "/caroline/events/stage1/71.webp"
    scene caroline_stage1_71
    caroline "That is a good attitude to have."
    caroline "So what is the plan?"
    pc "Why don't we split everything 50/50, If that doesn't get in the way of your practice too much?"
    image caroline_stage1_72 = "/caroline/events/stage1/72.webp"
    scene caroline_stage1_72
    caroline "Thanks, it is kind of you to be so considerate, especially given how I have behaved."
    caroline "Although, I know I have already asked a lot of you but maybe we could switch what the 50/50 is?"
    pc "What do you mean?"
    image caroline_stage1_73 = "/caroline/events/stage1/73.webp"
    scene caroline_stage1_73
    caroline "I'm not trying to get out of anything, so feel free to say no."
    caroline "But I was wondering if I could do the eating and recording my data, while you do the write up and all that research reference stuff?"
    caroline "If that is ok?"
    "That sounds more than ok to you, but it seems a little odd for her to suggest it."
    pc "Does that work better for you?"
    image caroline_stage1_74 = "/caroline/events/stage1/74.webp"
    scene caroline_stage1_74
    caroline "Absolutely!"
    caroline "It means I can do my half of the project right now, and just record things about my body at home."
    caroline "So I will have plenty of time to practise and it doesn't take much out of my evenings."
    caroline "But again, I only want to do this if you are ok with it?"
    pc "Yeah, I am totally ok with doing the write up."
    caroline "Amazing, thank you so much."
    caroline "So, I guess I just need to start eating?"
    image caroline_stage1_75 = "/caroline/events/stage1/75.webp"
    scene caroline_stage1_75
    "Grabbing the first of the snacks Caroline pours it into her mouth before handing you the empty wrapper."
    "Taking out a notepad you write down the number of calories and nutritional information while she grabs the next food item."
    image caroline_stage1_76 = "/caroline/events/stage1/76.webp"
    scene caroline_stage1_76
    "Repeating it several times Caroline has emptied the box and you now have a long list of everything she has eaten."
    ##Caroline a little bloated ###
    image caroline_stage1_77 = "/caroline/events/stage1/77.webp"
    scene caroline_stage1_77
    caroline "Oooh, I think I ate those a little too quickly."
    caroline "Hope I don't get indigestion, might throw off my routine."
    ###Shadow / friend at the door that she looks over too.###
    image caroline_stage1_78 = "/caroline/events/stage1/78.webp"
    scene caroline_stage1_78
    pause
    image caroline_stage1_79 = "/caroline/events/stage1/79.webp"
    scene caroline_stage1_79
    caroline "Do you need me for anything else?"
    pc "No, I think that is everything for today."
    image caroline_stage1_80 = "/caroline/events/stage1/80.webp"
    scene caroline_stage1_80
    caroline "Great, are you ok if I leave a little early?"
    caroline "I have a big competition coming up and could do with all the extra training I can get?"
    pc "Sure, I think I have enough to go on."
    image caroline_stage1_81 = "/caroline/events/stage1/81.webp"
    scene caroline_stage1_81
    caroline "Awesome, I will record my information tonight and then I can give you a copy next time."
    pc "Sounds good to me, good luck."
    caroline "What…Oh, thank you!"
    pc "See you around Caroline."
    image caroline_stage1_82 = "/caroline/events/stage1/82.webp"
    scene caroline_stage1_82
    caroline "Bye [playername]."
    ###Her with Lucy just outside the classroom like you are overhearing them.###
    lucy "Why do you even waste your time with him, just pay the loser to do your work for you like I did with my partner."
    caroline "I…it's fine."
    ###alone in the room###
    image caroline_stage1_83 = "/caroline/events/stage1/83.webp"
    scene caroline_stage1_83
    "Clearing up the empty packets you head home."
    $ carolinestage1event2 = 0
    stop music fadeout 1.0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        $ daycount4 = 0
        jump freetime
    return

label Caroline_Stage_1_Event_3:
    ##Option to work with Caroline at college###
    scene player_room
    "You make your way down to the university."
    scene university_outside
    "Ready to work together with Caroline, you head to the study room."
    ###Other class room / project room###
    play music "/music/caroline.ogg" if_changed
    image caroline_stage1_84 = "/caroline/events/stage1/84.webp"
    scene caroline_stage1_84
    "Walking into the room, you can see Caroline and Lucy already waiting for you."
    lucy "I'm gonna go smoke while you two do whatever it is we are supposed to be doing for this class."
    caroline "I'll see you in a minute."
    ###Lucy leaves###
    image caroline_stage1_85 = "/caroline/events/stage1/85.webp"
    scene caroline_stage1_85
    pc "She seems nice."
    caroline "Sorry about her, the stress gets to her."
    caroline "Are you ok if we keep going with how we did it last time?"
    pc "You eating and me doing the write up?"
    image caroline_stage1_86 = "/caroline/events/stage1/86.webp"
    scene caroline_stage1_86
    caroline "Exactly and here is the data from last time."
    "Handing you a piece of paper, Caroline has taken detailed measurements for the assignment."
    
    $ caroline_stats_visible = 1
    "Caroline has been added to the stats menu."

    image caroline_stage1_87 = "/caroline/events/stage1/87.webp"
    scene caroline_stage1_87
    pc "Thank you and yeah it still works for me."
    caroline "Great, me too."
    caroline "Although I think my parents and coach would kill me if they knew how much I was eating."
    pc "If you want, we can change how we do it?"
    image caroline_stage1_88 = "/caroline/events/stage1/88.webp"
    scene caroline_stage1_88
    caroline "Oh no it's ok, I just adjust my other meals and increase my workouts."
    caroline "This is way better for me overall."
    image caroline_stage1_89 = "/caroline/events/stage1/89.webp"
    scene caroline_stage1_89
    "Picking up the first item of food Caroline starts eating, one again handing you the wrapper after she is done."
    image caroline_stage1_90 = "/caroline/events/stage1/90.webp"
    scene caroline_stage1_90
    "Repeating it a few times, she gets about halfway through before stopping."
    image caroline_stage1_91 = "/caroline/events/stage1/91.webp"
    scene caroline_stage1_91
    caroline "That should do right?"
    caroline "I don't want to eat too much right before practice."
    pc "I thought you said you wanted to keep it the same?"
    caroline "I did…but I don't know if I really should."
    pc "This was your idea, I'm just a bit confused."
    caroline "I know, I guess I should keep to my word."
    caroline "Sorry I have been so flakey."
    image caroline_stage1_92 = "/caroline/events/stage1/92.webp"
    scene caroline_stage1_92
    "Picking up the next Snack, Caroline continues to eat."
    image caroline_stage1_93 = "/caroline/events/stage1/93.webp"
    scene caroline_stage1_93
    caroline "You know, I am still kind of surprised by how thorough you want to be."
    pc "What do you mean?"
    caroline "Well to be honest, I don't really need the grade with my scholarship."
    caroline "And I got the impression you didn't either, with the way Daisy treats you."
    caroline "Not that I am judging, we are all adults here and everyone deserves to be happy, however that might be."
    pc "Oh, I…just want to do a good job."
    pc "I thought you were a straight A student anyway?"
    image caroline_stage1_94 = "/caroline/events/stage1/94.webp"
    scene caroline_stage1_94
    caroline "Oh, I am in my other classes."
    caroline "I guess…I just don't see an application for this class in my future."
    caroline "Plus, I kind of find this all a little weird, don't you?"
    pc "Weird?"
    caroline "It's kind of an odd class, stuffing our teacher and watching her get fat in front of us."
    caroline "Although I have to admit Miss Tanwen is very dedicated to her profession."
    pc "Yeah, I know what you mean."
    "You decide not to tell her quite how much you have been enjoying Daisy's class and its impact on her body."
    image caroline_stage1_95 = "/caroline/events/stage1/95.webp"
    scene caroline_stage1_95
    "Finishing off the last piece of food, Caroline hands the wrapper to you."
    image caroline_stage1_96 = "/caroline/events/stage1/96.webp"
    scene caroline_stage1_96
    caroline "All of my friends have been talking about it, some of them even think she is doing it on purpose or enjoys it."
    pc "Really…?"
    "It seems Caroline has a pretty good intuition about these things, probably safer to change the subject slightly."
    pc "So why did you choose the class?"
    image caroline_stage1_97 = "/caroline/events/stage1/97.webp"
    scene caroline_stage1_97
    caroline "It was one of the only classes that didn't clash with my training and other things."
    caroline "Plus, when I went to speak to Daisy she was just so nice and helpful that I couldn't help but feel drawn to it."
    image caroline_stage1_98 = "/caroline/events/stage1/98.webp"
    scene caroline_stage1_98
    "Thinking for a moment, she seems to be debating something internally."
    pc "Everything ok?"
    image caroline_stage1_99 = "/caroline/events/stage1/99.webp"
    scene caroline_stage1_99
    caroline "Yeah, just thinking about some of the things my friends have said."
    caroline "But don't worry about it."
    pc "I'm not even sure what I should have been worried about."
    ###Caroline smiling before looking down again.###
    image caroline_stage1_100 = "/caroline/events/stage1/100.webp"
    scene caroline_stage1_100
    caroline "Sorry about talking so much, I'm not usually like this."
    pc "Why are you sorry, I've enjoyed it."
    ## Unsure face from Caroline ##
    image caroline_stage1_101 = "/caroline/events/stage1/101.webp"
    scene caroline_stage1_101
    caroline "Really?"
    pc "Yeah, of course."
    pc "And if you ever need to chat about something, I'm happy to listen."
    ##Caroline blushing / awkward.”
    image caroline_stage1_102 = "/caroline/events/stage1/102.webp"
    scene caroline_stage1_102
    caroline "Thanks, that's…nice."
    pc "Sorry, I realise you probably have actual friends to talk about stuff with."
    pc "Not that we aren't friends, I just meant people you know better than me."
    caroline "Yeah…totally I get that, thanks anyway."
    ##Regular Caroline###
    image caroline_stage1_103 = "/caroline/events/stage1/103.webp"
    scene caroline_stage1_103
    caroline "Are we done? I could do with the extra half hour of ballet if I can get it?"
    pc "Sure thing."
    caroline "Amazing, thank you."
    pc "No problem. See you later Caroline."
    image caroline_stage1_104 = "/caroline/events/stage1/104.webp"
    scene caroline_stage1_104
    caroline "Bye."
    $ carolinestage1event3 = 0
    stop music fadeout 1.0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        $ daycount4 = 0
        jump freetime
    return

label Caroline_Stage_1_Event_4:
    ##Option to work with Caroline at college###
    scene player_room
    "You make your way down to the university."
    scene university_outside
    "Ready to work together with Caroline, you head to the study room."
    ###Other class room / project room - Caroline standing###
    play music "/music/caroline.ogg" if_changed
    image caroline_stage1_105 = "/caroline/events/stage1/105.webp"
    scene caroline_stage1_105
    "Walking into the room, you can see Caroline already waiting for you and everything is open on the table."
    caroline "Hey [playername]!"
    pc "Hi Caroline."
    image caroline_stage1_106 = "/caroline/events/stage1/106.webp"
    scene caroline_stage1_106
    caroline "Ready to get started?"
    pc "Sure I guess, you seem eager today."
    caroline "Great!"
    image caroline_stage1_107 = "/caroline/events/stage1/107.webp"
    scene caroline_stage1_107
    "Grabbing the first item she doesn't waste any time as she crams it into her mouth."
    "While still chewing the first she tears open the second packet, emptying it into her hands and giving you the wrapper."
    image caroline_stage1_108 = "/caroline/events/stage1/108.webp"
    scene caroline_stage1_108
    pc "Everything ok?"
    caroline "Mmm mmm."
    image caroline_stage1_109 = "/caroline/events/stage1/109.webp"
    scene caroline_stage1_109
    "Continuing at her fast pace Caroline barely says a word as she devours the entire set of snacks."
    "The table now cluttered with wrappers as she ate faster than you could write down the information."
    image caroline_stage1_110 = "/caroline/events/stage1/110.webp"
    scene caroline_stage1_110
    "Finishing off the last packet, Caroline takes a deep breath."
    image caroline_stage1_111 = "/caroline/events/stage1/111.webp"
    scene caroline_stage1_111
    caroline "Ok, thanks for today."
    caroline "See you soon."
    pc "Uhh…Bye."
    "Grabbing her things Caroline waves back at you before heading out the door."
    image caroline_stage1_112 = "/caroline/events/stage1/112.webp"
    scene caroline_stage1_112
    "Sitting in the empty room you are a bit stunned by the abruptness of everything that had just happened."
    "But picking up your pen you continue to take down the notes of everything Caroline had eaten."
    "A few minutes later you hear a knock at the door."
    ##Daisy appears##
    image caroline_stage1_113 = "/caroline/events/stage1/113.webp"
    scene caroline_stage1_113
    teacher "How are you two getting on?"
    pc "Oh, hi Daisy."
    pc "Caroline just stepped out for a minute too…uh."
    image caroline_stage1_114 = "/caroline/events/stage1/114.webp"
    scene caroline_stage1_114
    teacher "Don't worry, you don't need to cover for her."
    teacher "I know she has probably been a little absent lately."
    pc "No, she has been helping out a lot."
    image caroline_stage1_115 = "/caroline/events/stage1/115.webp"
    scene caroline_stage1_115
    teacher "That is good to hear."
    teacher "She has a big competition coming up that is directly linked to her scholarship here."
    teacher "Caroline is probably feeling a lot of pressure right now, so I hope that hasn't been causing any issues between you two."
    pc "Oh ok, that makes a lot of sense."
    pc "I wouldn't say it's caused problems, but it has been a bit off putting to have her leave so quickly with her friends."
    pc "I'm just glad it isn't anything to do with me."
    teacher "'Friends' is one way to put it."
    ###Daisy sitting on the table casually for the chat?##
    image caroline_stage1_116 = "/caroline/events/stage1/116.webp"
    scene caroline_stage1_116
    pc "What do you mean?"
    teacher "Sorry, I shouldn't say anything or be one to judge the company she chooses."
    teacher "But to me most of them don't really seem much like genuine friends."
    teacher "A lot them only associate with her because they want to share her fame and influence."
    teacher "It doesn't really create the best conditions for genuine friendships to develop."
    teacher "It is partly why you were my first choice for a project partner for Caroline."
    pc "But I don't care about any of that stuff?"
    image caroline_stage1_117 = "/caroline/events/stage1/117.webp"
    scene caroline_stage1_117
    teacher "Exactly, I hoped you could show her what actual friendship felt like."
    pc "I don't think she is as hopeless or unaware of that stuff as you think."
    teacher "That's good to hear, I could be overreacting."
    teacher "Just don't be too hard on her if she has to take time away for her competitions."
    teacher "I'll be taking that into consideration with her mark so you don't need to worry about that either."
    pc "Ok, thanks."
    image caroline_stage1_118 = "/caroline/events/stage1/118.webp"
    scene caroline_stage1_118
    teacher "Great, well I will let you get back to it and go check on some of the others."
    pc "Bye Daisy."
    ##Daisy leaves###
    image caroline_stage1_112 = "/caroline/events/stage1/112.webp"
    scene caroline_stage1_112
    "Finishing writing up the data from the snacks, you clear them away and head home."
    ##[Leads to repeatable project work formatted with her sitting, eating quickly and leaving.]##
    $ carolinestage1event4 = 0
    stop music fadeout 1.0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        $ daycount4 = 0
        jump freetime
    return

label Caroline_Stage_1_Event_5:
    ### at class###
    "Arriving to class, you take your seat."
    play music "/music/university.ogg" if_changed
    image caroline_stage1_119 = "/caroline/events/stage1/119.webp"
    scene caroline_stage1_119
    "Next to you, Caroline's desk remains empty even as class begins."
    "Maybe she was at a competition today?"

    #[Regular class Friday stuffing class?]
    "Today is Daisy's feeding day. What will you bring?"
    #(NOTE: The choices will determine how many feeding scenes the player gets to watch for the class. A=1, B=2, and C=3. Options B and C will only be available if the player bought the necessary supplies beforehand.)
    menu:
        "Nothing.":
            image uni_sexy_teacher_arrive = "/teacher/[teacher.stage]/0/arrive.webp"
            scene uni_sexy_teacher_arrive
            window hide
            pause
            image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
            scene uni_sexy_teacher_greet
            teacher "Good morning students."
            s "Good morning Ms. Tanwen."
            call rngteachingscene
            teacher "Today is feeding day, so give me a moment to get ready."
            $ strip += 1
            window hide
            pause
            $ strip += 1
            pause
            $ strip += 1
            pause
            $ strip += 1
            pause
            image uni_sexy_teacher_food_teaching1 = "/teacher/[teacher.stage]/[strip]/food_teaching1.webp"
            scene uni_sexy_teacher_food_teaching1
            teacher "So many great options. Let's see what I should start with."
            call foodchoice
            image uni_sexy_teacher_stuffed_half = "/teacher/[teacher.stage]/[strip]/stuffed_half.webp"
            scene uni_sexy_teacher_stuffed_half
            teacher "Delicious as always. I'll finish up the rest of this over the weekend. See you all again on Monday!"
            $ eatcount = 0
            $ strip = 0

        "A small offering. (-1 meals)" if foodheld >= 1:
            $ foodheld -= 1
            image uni_sexy_teacher_arrive = "/teacher/[teacher.stage]/0/arrive.webp"
            scene uni_sexy_teacher_arrive
            window hide
            pause
            image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
            scene uni_sexy_teacher_greet
            teacher "Good morning students."
            s "Good morning Ms. Tanwen."
            call rngteachingscene
            teacher "Today is feeding day, so give me a moment to get ready."
            $ strip += 1
            window hide
            pause
            $ strip += 1
            pause
            $ strip += 1
            pause
            $ strip += 1
            pause
            image uni_sexy_teacher_food_teaching2 = "/teacher/[teacher.stage]/[strip]/food_teaching2.webp"
            scene uni_sexy_teacher_food_teaching2
            teacher "So many great options. Let's see what I should start with."
            call foodchoice
            teacher "Mmm, that was pretty good. What's next?"
            call foodchoice
            image uni_sexy_teacher_stuffed = "/teacher/[teacher.stage]/[strip]/stuffed.webp"
            scene uni_sexy_teacher_stuffed
            teacher "Delicious as always. I'll finish up the rest of this over the weekend. See you all again on Monday!"
            $ eatcount = 0
            $ strip = 0

        "A large offering. (-3 meals)" if foodheld >= 3:
            $ foodheld -= 3
            image uni_sexy_teacher_arrive = "/teacher/[teacher.stage]/0/arrive.webp"
            scene uni_sexy_teacher_arrive
            window hide
            pause
            image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
            scene uni_sexy_teacher_greet
            teacher "Good morning students."
            s "Good morning Ms. Tanwen."
            call rngteachingscene
            teacher "Today is feeding day, so give me a moment to get ready."
            $ strip += 1
            window hide
            pause
            $ strip += 1
            pause
            $ strip += 1
            pause
            $ strip += 1
            pause
            image uni_sexy_teacher_food_teaching3 = "/teacher/[teacher.stage]/[strip]/food_teaching3.webp"
            scene uni_sexy_teacher_food_teaching3
            teacher "So many great options. Let's see what I should start with."
            call foodchoice
            teacher "Mmm, that was pretty good. What's next?"
            call foodchoice
            teacher "I'm feeling pretty stuffed, but I think I can do one more."
            call foodchoice
            image uni_sexy_teacher_stuffed_full = "/teacher/[teacher.stage]/[strip]/stuffed_full.webp"
            scene uni_sexy_teacher_stuffed_full
            teacher "Delicious as always. I'll finish up the rest of this over the weekend. See you all again on Monday!"
            $ eatcount = 0
            $ strip = 0

    image caroline_stage1_120 = "/caroline/events/stage1/120.webp"
    scene caroline_stage1_120
    "Collecting your things at the end of class, you notice Daisy approaching you."
    pc "Hi Daisy, great class today."
    image caroline_stage1_121 = "/caroline/events/stage1/121.webp"
    scene caroline_stage1_121
    teacher "Thanks, do you have a moment?"
    pc "Is everything ok?"
    image caroline_stage1_122 = "/caroline/events/stage1/122.webp"
    scene caroline_stage1_122
    teacher "I'm sure you have noticed Caroline has been absent today."
    teacher "Unfortunately, she has injured her leg."
    teacher "It's nothing serious, but she will be absent for a couple of weeks as she recovers."
    teacher "As such, I've given you both an extension on your project and don't want you to worry about doing it all by yourself while she is away."
    pc "Oh ok, is she alright, other than the obvious?"
    image caroline_stage1_123 = "/caroline/events/stage1/123.webp"
    scene caroline_stage1_123
    teacher "Yes, she seemed fine when she phoned me yesterday."
    teacher "I think it's one of those things that wouldn't necessarily impact either of us."
    teacher "as a professional dancer she needs to take extra care so it heals properly."
    pc "Ah ok, I understand."
    pc "Is there anything else I should do?"
    image caroline_stage1_124 = "/caroline/events/stage1/124.webp"
    scene caroline_stage1_124
    teacher "No, feel free to focus on other things for a couple of weeks and then she should be back and you can carry on."
    pc "Great, thanks for letting me know."
    image caroline_stage1_125 = "/caroline/events/stage1/125.webp"
    scene caroline_stage1_125
    teacher "No problem, see you soon [playername]."
    pc "Bye Daisy."
    "Heading home, you hope Caroline isn't too badly hurt."
    #[Don't see her for two weeks and remove the option to work with her]
    $ carolinestage1event5 = 0
    stop music fadeout 1.0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        $ daycount4 = 0
        jump freetime
    return

label Caroline_Stage_2_Event:
    ###Going to class###
    play music "/music/university.ogg" if_changed
    if recollection == False:
        $ caroline.stage = 2
        $ caroline.breast_cup = "34D"
        $ caroline.breast_size = 36.9
        $ caroline.ass_size = 40.1
        $ caroline.waist_size = 25.8
        $ caroline.leanweight = 61.4
        $ caroline.weight = 79
    image caroline_stage2_1 = "/caroline/events/stage2/1.webp"
    scene caroline_stage2_1
    "Arriving at class, you spot Caroline sitting in her usual seat."
    image caroline_stage2_2 = "/caroline/events/stage2/2.webp"
    scene caroline_stage2_2
    pc "Hey, glad to see you are back. how are you feeling?"
    caroline "Oh, hi [playername]."
    caroline "I'm ok thanks."
    pc "I was sorry to hear about your injury."
    image caroline_stage2_3 = "/caroline/events/stage2/3.webp"
    scene caroline_stage2_3
    caroline "Yeah, it was annoying timing really."
    pc "I kind of meant it must have hurt, I hope you are feeling better now though?"
    caroline "Oh right, yeah sure I am feeling better."
    pc "That's good, I am glad it wasn't too bad."
    caroline "Thanks."
    ##Lucy walks in##
    image caroline_stage2_4 = "/caroline/events/stage2/4.webp"
    scene caroline_stage2_4
    lucy "Geez, only been back a few minutes and already having to deal with this guy again."
    caroline "What, oh no it's ok he was just…"
    lucy "You don't have to cover for him."
    image caroline_stage2_5 = "/caroline/events/stage2/5.webp"
    scene caroline_stage2_5
    lucy "Anyway, what's up K, you back now?"
    caroline "Yeah, I still can't dance but I was going crazy being stuck in my house this whole time."
    lucy "I know what you mean, but now you are back you don't have to worry about all that."
    
    ##Daisy arrives##
    #[Regular lesson dialogue]
    call Daisy_Class_Normal

    ###After lesson -  no other options just straight into Caroline###
    image caroline_stage2_6 = "/caroline/events/stage2/6.webp"
    scene caroline_stage2_6
    play music "/music/caroline.ogg" if_changed
    "After Daisy dismisses the class to work on their projects, you decide to work with Caroline today."
    image caroline_stage2_7 = "/caroline/events/stage2/7.webp"
    scene caroline_stage2_7
    "Walking into the room you see her waiting for you."
    pc "Hey, how did you want to do it this week?"
    image caroline_stage2_8 = "/caroline/events/stage2/8.webp"
    scene caroline_stage2_8
    caroline "We can keep doing it like we were before if that is still an option?"
    caroline "I don't plan on being injured for long, so I think it makes sense to keep going like that instead of changing it now and then later."
    pc "Sure, sounds good to me."
    image caroline_stage2_9 = "/caroline/events/stage2/9.webp"
    scene caroline_stage2_9
    "Taking the first snack, Caroline opens the bag and starts eating."
    "Unlike her usual confident self, you can see her playing with the bag in her hand instead of giving it to you."
    image caroline_stage2_10 = "/caroline/events/stage2/10.webp"
    scene caroline_stage2_10
    pc "Everything ok?"
    caroline "What, oh sorry."
    "Handing over the bag she balls her hands up on the table, fidgeting slightly."
    image caroline_stage2_11 = "/caroline/events/stage2/11.webp"
    scene caroline_stage2_11
    pc "I didn't mean that, you just seem a little bit...distracted."
    caroline "Sorry, I guess I am a little bit antsy without being unable to train."
    caroline "But I won't let it affect our work together."
    pc "You don't have to worry about that and I didn't mean it like that."
    pc "I just wanted to check if you were ok?"
    pc "But equally you don't have to talk about it if you don't want to."
    image caroline_stage2_12 = "/caroline/events/stage2/12.webp"
    scene caroline_stage2_12
    caroline "Thanks, although honestly I don't really know what to say."
    caroline "I mean I'm ok and there are worse things that can happen."
    caroline "I just need to keep focusing on healing and getting better."
    image caroline_stage2_13 = "/caroline/events/stage2/13.webp"
    scene caroline_stage2_13
    "Taking the next snack she continues eating."
    pc "That sounds like a good plan."
    pc "So what do you do for fun, other than ballet?"
    ##Bit of a surprised look / contemplating##
    image caroline_stage2_14 = "/caroline/events/stage2/14.webp"
    scene caroline_stage2_14
    caroline "I…not much."
    caroline "Ever since I was a kid I have been on the fast track to where I am now."
    caroline "It means I have been fully focused on my career ever since I was little."
    caroline "Which has kind of…"
    image caroline_stage2_15 = "/caroline/events/stage2/15.webp"
    scene caroline_stage2_15
    "Grabbing another snack Caroline falls quiet as she seems deep in thought about something."
    "Not wanting to press her too much, you decide to just focus on the project."
    "Writing the details down of everything Caroline eats you complete this part of the project easily."
    image caroline_stage2_16 = "/caroline/events/stage2/16.webp"
    scene caroline_stage2_16
    caroline "I think that was the last one."
    pc "Ok cool, I think we have everything we need from today."
    caroline "Great, I have a physical therapy session in a little bit anyway."
    pc "Sure thing, do you need any help getting there or with anything else?"
    caroline "Help?"
    pc "Yeah, is there anything I can do, carry your bag or something else?"
    ###Caroline looking shy / surprised a bit.###
    image caroline_stage2_17 = "/caroline/events/stage2/17.webp"
    scene caroline_stage2_17
    caroline "I…I think I am ok."
    pc "Ok, but if there is anything you need, just let me know."
    pc "I am happy to help."
    ###Caroline goes to leave the room - then turns back around.###
    image caroline_stage2_18 = "/caroline/events/stage2/18.webp"
    scene caroline_stage2_18
    caroline "Hey [playername]."
    caroline "Thanks for being so nice to me."
    pc "No problem, what else are friends for right."
    caroline "Right…see you around."
    pc "Bye Caroline."
    $ carolinestage2event = 0
    stop music fadeout 1.0
    if recollection == False:
        $ caroline.weight += 0.2
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Caroline_Stage_2_Event_2:
    ###After lesson###
    "After Daisy dismisses the class to work on their projects, you decide to work with Caroline."
    ###In project room###
    play music "/music/caroline.ogg" if_changed
    image caroline_stage2_19 = "/caroline/events/stage2/19.webp"
    scene caroline_stage2_19
    "Walking into the room you see Caroline going through the supplies Daisy left out for you."
    pc "Hi Caroline."
    image caroline_stage2_20 = "/caroline/events/stage2/20.webp"
    scene caroline_stage2_20
    caroline "Oh, Hi."
    caroline "Ready to work on the project?"
    pc "Yeah, absolutely."
    image caroline_stage2_21 = "/caroline/events/stage2/21.webp"
    scene caroline_stage2_21
    "Sitting down opposite of you, it seems Caroline is more focused today than last time."
    pc "How are you doing?"
    caroline "Yeah, actually feeling pretty good today."
    caroline "Right then, which of these should I start with?"
    image caroline_stage2_22 = "/caroline/events/stage2/22.webp"
    scene caroline_stage2_22
    "Picking up the first item of food, she slowly begins to eat it while studying the packet."
    caroline "Mmm, I didn't realise how much salt was in these."
    caroline "Would it help if I read the numbers out to you?"
    pc "Sure, if you want too."
    image caroline_stage2_23 = "/caroline/events/stage2/23.webp"
    scene caroline_stage2_23
    "Smiling, Caroline begins to read off the nutritional information to you as she eats the snacks."
    "It takes a bit longer than usual, but feels a lot more casual than her typically distracted and rapid pace."
    image caroline_stage2_24 = "/caroline/events/stage2/24.webp"
    scene caroline_stage2_24
    caroline "Mmm, last one and these are definitely my favourite."
    "Finishing off the supplies, Caroline helps you tidy up the mess of bags and wrappers."
    image caroline_stage2_25 = "/caroline/events/stage2/25.webp"
    scene caroline_stage2_25
    caroline "So, what's next?"
    pc "Next?"
    caroline "With the project, I figured since I don't have to rush off anywhere I could help with the other parts of the project."
    caroline "That is, if you want help?"
    pc "Sure, I appreciate the offer."
    ##Caroline smiling##
    image caroline_stage2_26 = "/caroline/events/stage2/26.webp"
    scene caroline_stage2_26
    pc "I'll be honest I didn't bring in all the work I've already done."
    pc "But we can head back to mine if you want too?"
    caroline "You have your own place?"
    pc "Technically owned by my dad, but he doesn't live there."
    caroline "That would be great."
    image caroline_stage2_27 = "/caroline/events/stage2/27.webp"
    scene caroline_stage2_27
    "Packing up your stuff, you make your way home with Caroline."
    stop music fadeout 1.0

    ###Entrance###
    image caroline_stage2_28 = "/caroline/events/stage2/28.webp"
    scene caroline_stage2_28
    caroline "I didn't know you lived here!"
    pc "You say that like you know this house."
    caroline "I do, well I've seen it before."
    caroline "I live just up the road, maybe like 5 minutes from here."
    caroline "I've driven past this house loads of times."
    pc "Well, now I guess you know who lives here."
    image caroline_stage2_29 = "/caroline/events/stage2/29.webp"
    scene caroline_stage2_29
    pc "I can show you where everything is if you want?"
    caroline "Yes please."
    image caroline_stage2_30 = "/caroline/events/stage2/30.webp"
    scene caroline_stage2_30
    pc "Ok, well the lounge or living room is through there, kitchen to the right."
    pc "That door is a spare bedroom and through there you have the…"
    caroline "Pool!"
    ###Looking at the pool.###
    image caroline_stage2_31 = "/caroline/events/stage2/31.webp"
    scene caroline_stage2_31
    caroline "I always wanted a pool, but my parents wouldn't let me."
    caroline "Something about them being safety hazards for my kid brothers."
    caroline "If I'd known I would have brought my bathing suit."
    ###Looking embarrassed ##
    image caroline_stage2_32 = "/caroline/events/stage2/32.webp"
    scene caroline_stage2_32
    caroline "Sorry."
    pc "What for?"
    caroline "I'm being too familiar with you, you invited me over to do work and not play in the pool."
    "You try not to laugh, but a smile escapes."
    pc "Caroline, I don't know if anyone has told you before but you are allowed to have fun occasionally."
    pc "Plus, there is no need to be so formal with me, we're friends."
    pc "You can totally use the pool whenever you want."
    ###Caroline looking unsure.###
    image caroline_stage2_33 = "/caroline/events/stage2/33.webp"
    scene caroline_stage2_33
    caroline "I…ok."
    pc "I mean it, I barely use it so it's a bit of a waste."
    pc "If you come over again feel free to bring something to swim in, if you want."
    image caroline_stage2_34 = "/caroline/events/stage2/34.webp"
    scene caroline_stage2_34
    caroline "Thanks."
    pc "But you are right about the project, if you want to go to the lounge I'll go grab everything from my room."
    caroline "Sounds good to me."
    image caroline_stage2_35 = "/caroline/events/stage2/35.webp"
    scene caroline_stage2_35
    "You grab your books and notes for the project and head back into the lounge, finding Caroline sitting rigidly on the sofa."
    ###Books and stuff on the tables###
    image caroline_stage2_36 = "/caroline/events/stage2/36.webp"
    scene caroline_stage2_36
    "Going through everything you have done, Caroline seems genuinely impressed by your work."
    "She notices a couple of mistakes here and there, but together you make a good team."
    "Finishing up, everything seems much more organised and coherent with both of you working on it together."
    image caroline_stage2_37 = "/caroline/events/stage2/37.webp"
    scene caroline_stage2_37
    pc "Hey, it's getting a bit late. Do you want to order some food, I think we have earned it?"
    caroline "That sounds nice, although I can't remember the last time I had a takeaway."
    pc "Do you like to cook?"
    caroline "No, I barely know how to use the microwave."
    caroline "My parents have a chef, although we do eat out at restaurants quite a bit too."
    pc "Personal chef, sounds fancy."
    pc "Must be nice to be able to get whatever you want when you want, and not have to deal with the dishes."
    image caroline_stage2_38 = "/caroline/events/stage2/38.webp"
    scene caroline_stage2_38
    caroline "Yeah, although I tend to eat a lot of the same meals."
    caroline "Optimised diet for my performance and training."
    caroline "I think that is partly why I found this project so weird at the start."
    caroline "It's kind of rare for me to eat something that hasn't been specifically prescribed to me by a dietician."
    pc "I mean, we don't need to have a takeaway if that upsets your routine."
    image caroline_stage2_39 = "/caroline/events/stage2/39.webp"
    scene caroline_stage2_39
    caroline "No, sorry I didn't mean it to sound that way."
    caroline "I would love a takeaway."
    image caroline_stage2_40 = "/caroline/events/stage2/40.webp"
    scene caroline_stage2_40
    "Scrolling through the options, Caroline has trouble deciding what to get."
    "But after a few minutes the food is ordered."
    image caroline_stage2_41 = "/caroline/events/stage2/41.webp"
    scene caroline_stage2_41
    "Clearing away some of the books and notes, the food soon arrives."
    caroline "Oh no!"
    pc "Everything ok?"
    image caroline_stage2_42 = "/caroline/events/stage2/42.webp"
    scene caroline_stage2_42
    caroline "I'm so sorry, I'm so stupid, how did I not think about this earlier."
    caroline "I don't have any money on me, I can't pay for the takeaway."
    pc "No problem, I've got enough to cover it."
    caroline "But why would you do that?"
    pc "Because we are friends?"
    pc "It's only a few bucks, it's fine honestly."
    image caroline_stage2_43 = "/caroline/events/stage2/43.webp"
    scene caroline_stage2_43
    pc "You can either pay me back or maybe you can get the next one if we do this again."
    caroline "Really, are you sure you are ok with this?"
    pc "100 percent, have you never owed anyone a favour for something before?"
    caroline "Not really, my family tends to pay for most things for me and my other friends."
    pc "Oh ok, well you don't need to worry about it."
    "It's clear Caroline is still a little bit nervous about something."
    image caroline_stage2_44 = "/caroline/events/stage2/44.webp"
    scene caroline_stage2_44
    "Eating your food, a quietness surrounds you both."
    image caroline_stage2_45 = "/caroline/events/stage2/45.webp"
    scene caroline_stage2_45
    pc "Hey, why don't we put on some music?"
    pc "You can choose if you want?"
    caroline "Yeah ok."
    pc "Here let me connect the speakers to your phone."
    image caroline_stage2_46 = "/caroline/events/stage2/46.webp"
    scene caroline_stage2_46
    caroline "Wait, what?"
    "Connecting to her phone they start playing the last song she was listening to."
    "The calmness of your study session is broken by heavy metal."
    ##Caroline blushing##
    image caroline_stage2_47 = "/caroline/events/stage2/47.webp"
    scene caroline_stage2_47
    "Grabbing her phone, Caroline fumbles with it until she can pause the song."
    image caroline_stage2_48 = "/caroline/events/stage2/48.webp"
    scene caroline_stage2_48
    caroline "I'm so sorry, I…uh, it's been doing that all the time."
    caroline "I think something is broken with it."
    pc "No problem, sounds familiar."
    pc "Was that black beetle?"
    ###excited looking Caroline###
    image caroline_stage2_49 = "/caroline/events/stage2/49.webp"
    scene caroline_stage2_49
    caroline "Yeah!"
    ###Back to embarrassed looking.###
    image caroline_stage2_50 = "/caroline/events/stage2/50.webp"
    scene caroline_stage2_50
    caroline "I…uh, or at least that's what is said on my phone."
    pc "Maybe we can try music another time."
    image caroline_stage2_51 = "/caroline/events/stage2/51.webp"
    scene caroline_stage2_51
    "Going back to eating in awkward silence, you both finish your food."
    image caroline_stage2_52 = "/caroline/events/stage2/52.webp"
    scene caroline_stage2_52
    caroline "I think I should get going, it's getting late."
    pc "Sure thing, thanks for your help with everything."
    pc "The project's looking much better now."
    caroline "Yeah, although I am sure we would have been fine with what you had done already."
    "You show Caroline out."
    ###Caroline stood at the door.###
    image caroline_stage2_53 = "/caroline/events/stage2/53.webp"
    scene caroline_stage2_53
    caroline "Hey [playername]."
    pc "Yeah?"
    caroline "Thanks for tonight."
    caroline "I don't usually have that much fun working on assignments."
    image caroline_stage2_54 = "/caroline/events/stage2/54.webp"
    scene caroline_stage2_54
    caroline "It's usually just me and tutors, so it's work work work."
    pc "Well I am glad you had fun, and we managed to get some work in."
    pc "I had fun too, we should do this again."
    caroline "Definitely."
    image caroline_stage2_55 = "/caroline/events/stage2/55.webp"
    scene caroline_stage2_55
    caroline "Bye [playername]."
    pc "Bye Caroline."
    "While there might still be a lot you don't know about her, it feels like she might be opening up to you."
    $ carolinestage2event2 = 0
    stop music fadeout 1.0
    if recollection == False:
        $ caroline.weight += 0.3
        $ strip = 0
        $ daytime = 4
        jump freetime
    return

label Caroline_Stage_2_Event_3:
    #[Get a text from Caroline]
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Caroline', dialogue=dialogue_one)
    $ msg ("Hi [playername].", who=1)
    pause
    $ msg ("I was wondering if you could help me with something?", who=1)
    pause
    $ msg ("But if not, that's totally fine too.", who=1)
    pause
    menu:
        "Yes":
            $ msg ("Of course, do you want to come around mine again and we can talk?")
            pause
            $ msg ("If you want you can bring something for the pool this time.")
            pause
            $ hide_messenger()
        "No":
            $ msg ("I'm busy today, maybe another time.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    ###At your house###
    "A few minutes later, you hear a knock on the door."
    image caroline_stage2_56 = "/caroline/events/stage2/56.webp"
    scene caroline_stage2_56
    pc "Hey Caroline, come on in."
    caroline "Thanks."
    image caroline_stage2_57 = "/caroline/events/stage2/57.webp"
    scene caroline_stage2_57
    pc "How are you, is your leg feeling any better?"
    caroline "I'm good thanks."
    caroline "My leg feels fine now, I have to keep fighting the temptation to work out."
    pc "At least it doesn't hurt."
    image caroline_stage2_58 = "/caroline/events/stage2/58.webp"
    scene caroline_stage2_58
    caroline "Yeah exactly, Just a few more weeks and I'll be back to my old self."
    pc "Well if you feel like it, you can take a dip in the pool."
    pc "If that's ok for your leg?"
    image caroline_stage2_59 = "/caroline/events/stage2/59.webp"
    scene caroline_stage2_59
    caroline "Yeah, it's actually recommended."
    pc "Perfect, you know where it is right?"
    pc "I was just going to make some coffee, if you want any?"
    caroline "Yeah, do you have any tea?"
    pc "Yeah, I can make tea."
    ##Kitchen / looking out at the pool through the window.###
    image caroline_stage2_60 = "/caroline/events/stage2/60.webp"
    scene caroline_stage2_60
    "Waiting for the water to boil, you can see Caroline swimming lengths in the pool."
    "Making some coffee for yourself, you put her tea on a tray with some snacks."
    ###Outside by the pool###
    image caroline_stage2_61 = "/caroline/events/stage2/61.webp"
    scene caroline_stage2_61
    "Placing her tea on the table, she swims up to the edge of the pool near you."
    image caroline_stage2_62 = "/caroline/events/stage2/62.webp"
    scene caroline_stage2_62
    pc "Here is your tea, probably still a bit warm."
    pc "I also got some snacks, if you want any?"
    image caroline_stage2_63 = "/caroline/events/stage2/63.webp"
    scene caroline_stage2_63
    caroline "I…thanks."
    "Sipping your drinks, things get a little quiet between you."
    image caroline_stage2_64 = "/caroline/events/stage2/64.webp"
    scene caroline_stage2_64
    "It seems like Caroline goes to say something a couple of times but then doesn't."
    "Deciding to break the awkward silence you speak up first."
    pc "So what can I help with?"
    image caroline_stage2_65 = "/caroline/events/stage2/65.webp"
    scene caroline_stage2_65
    caroline "What?"
    pc "Your text, it said you wanted help with something?"
    image caroline_stage2_66 = "/caroline/events/stage2/66.webp"
    scene caroline_stage2_66
    caroline "Oh right…"
    caroline "I'm sorry, sometimes I find it hard to admit when I need help."
    caroline "Especially when it's kind of…odd."
    pc "I'm happy to help with whatever it is?"
    image caroline_stage2_67 = "/caroline/events/stage2/67.webp"
    scene caroline_stage2_67
    caroline "I…don't know how to relax."
    pc "What?"
    image caroline_stage2_68 = "/caroline/events/stage2/68.webp"
    scene caroline_stage2_68
    caroline "I have all this spare time now that I am not training, and I don't know what to do or how to spend it."
    caroline "My doctor even said that relaxing was an important part of the recovery process but It really doesn't come naturally to me."
    pc "I get that, by the sounds of it you have been training to be the best since you were a kid."
    pc "That will have probably caused certain things to become habits, like not relaxing."
    image caroline_stage2_69 = "/caroline/events/stage2/69.webp"
    scene caroline_stage2_69
    caroline "So now what?"
    pc "What sort of things do you like?"
    caroline "I don't know…"
    pc "Ok, lets try a different tactic, if you could do anything right now what would it be?"
    caroline "Probably work out, or maybe get ahead on my school work."
    pc "Mmm, this might be tougher than I thought."
    pc "Thankfully I am an expert at relaxation and up for the challenge."
    pc "The trick might be to take something you like and do something adjacent to it."
    image caroline_stage2_70 = "/caroline/events/stage2/70.webp"
    scene caroline_stage2_70
    caroline "Like what?"
    pc "Do you have any hobbies, or favourite classes?"
    image caroline_stage2_71 = "/caroline/events/stage2/71.webp"
    scene caroline_stage2_71
    caroline "I don't know, I feel so useless right now."
    caroline "My whole life has been ballet."
    caroline "Anything I did enjoy, I kind of had to leave it behind."
    caroline "My parents always wanted me to be the best at everything I ever did."
    caroline "But you can't really do that with more than one thing, so I stopped doing them."
    image caroline_stage2_72 = "/caroline/events/stage2/72.webp"
    scene caroline_stage2_72
    pc "That's ok, you can't change the past so no need to worry about it."
    pc "Why don't we start simple, I have a load of films in there."
    pc "If you want too, you go pick one, we can order some food and just relax on the sofa."
    image caroline_stage2_73 = "/caroline/events/stage2/73.webp"
    scene caroline_stage2_73
    caroline "That sounds good."
    pc "I told you I was an expert."
    "Heading to the lounge, Caroline dries off while you order food."
    image caroline_stage2_74 = "/caroline/events/stage2/74.webp"
    scene caroline_stage2_74
    "Soon it has arrived and the pair of you lounge back on the sofa."
    pc "So, found a film you like?"
    caroline "You have a lot of DVD's, but yeah I got one."
    caroline "Night of the killer chrysanthemums."
    pc "Really, I didn't pick you for the old school horror fan."
    image caroline_stage2_75 = "/caroline/events/stage2/75.webp"
    scene caroline_stage2_75
    caroline "I love these cheesy shows."
    caroline "Me and my dad used to watch one after every contest when I was little, kind of like a reward."
    caroline "Although, I don't know if it was a reward for me or him."
    pc "Sounds perfect, I hear they are making a new one as well."
    caroline "Really, I hope they don't ruin it."
    image caroline_stage2_76 = "/caroline/events/stage2/76.webp"
    scene caroline_stage2_76
    "Putting the film on, the pair of you enjoy the comical horror."
    "Laughing at the terrible special effects and sub-par acting."
    "But it wasn't the sort of film you watched as fine art."
    pc "Hey, do you want the last onion ring?"
    image caroline_stage2_77 = "/caroline/events/stage2/77.webp"
    scene caroline_stage2_77
    "Offering it to Caroline, she is about to take it before she stops."
    "Pausing the movie, she shifts to look at you directly."
    caroline "What do you want?"
    pc "For the onion ring?"
    ##Caroline smiling/laughing##
    image caroline_stage2_78 = "/caroline/events/stage2/78.webp"
    scene caroline_stage2_78
    caroline "No, like why are you being so friendly to me?"
    pc "I think the clue is the word you used, we are friends right?"
    caroline "Yeah, It's just that usually that comes with strings attached."
    pc "Oh…I'm sorry to hear that."
    pc "I hope you know that's not the case with me."
    image caroline_stage2_79 = "/caroline/events/stage2/79.webp"
    scene caroline_stage2_79
    caroline "I know, I totally get that feeling from you."
    caroline "I just… I don't know how to explain it."
    caroline "With my other friends…"
    caroline "Like, I'm not stupid and I know my other friends are not really friends."
    caroline "They have just kind of stuck around with me for so long I got used to them being there, even though they didn't behave like friends."
    caroline "Or at least the type of friends I actually want."
    pc "Don't worry, I understand what you mean."
    image caroline_stage2_80 = "/caroline/events/stage2/80.webp"
    scene caroline_stage2_80
    caroline "You do?"
    pc "Well, not totally but I get what it is like."
    pc "It can feel like you would be alone if you got rid of your friends, even though you might want to."
    pc "Kind of like you are trapped in your friendship group and if you leave it, there won't be anyone else."
    pc "I was worried about that before I moved back here on my own, but since then I have met a whole bunch of amazing people."
    pc "Obviously I am not telling you to drop your friends, but if you do I know you could make new ones really easily."
    "You are not sure if you have said too much as Caroline stays quiet for a few moments."
    image caroline_stage2_81 = "/caroline/events/stage2/81.webp"
    scene caroline_stage2_81
    caroline "Thanks."
    pc "Sorry if that was too much, is it something you have been thinking about for a while?"
    caroline "No, I think I needed to hear that."
    image caroline_stage2_82 = "/caroline/events/stage2/82.webp"
    scene caroline_stage2_82
    caroline "And kind of, I'd always been aware of it but when I got injured it became more obvious who my real friends were."
    caroline "I used to justify keeping them as friends because I told myself that I used them as much as they used me."
    caroline "A lot of them are good for my career, daughters of important people, colleagues and stuff like that."
    caroline "But since I haven't been training or competing the last few weeks, almost none of them asked me how I was doing."
    caroline "They have basically ignored me since it happened and they knew I wasn't going to be around."
    caroline "The worst thing about it though, I haven't missed them at all either."
    caroline "Does that make me a bad person?"
    image caroline_stage2_83 = "/caroline/events/stage2/83.webp"
    scene caroline_stage2_83
    "It was a lot to take in, but it was clear this had been weighing on her mind for some time."
    "Was this the real reason she had come over today, not to learn how to relax?"
    pc "Absolutely not, as the one who got hurt I dont think it's on you to reach out to them."
    pc "But maybe it would be worth talking to them, I don't want to make assumptions for people I don't really know."
    image caroline_stage2_84 = "/caroline/events/stage2/84.webp"
    scene caroline_stage2_84
    caroline "Yeah, you are right."
    caroline "I should probably speak to them again before I make any drastic decisions."
    caroline "Who knows, they might all have good reasons to not have spoken to me."
    caroline "Sorry for dropping all this on you."
    pc "It's no problem, I'll always be here if you need to talk."
    caroline "Thanks."
    image caroline_stage2_85 = "/caroline/events/stage2/85.webp"
    scene caroline_stage2_85
    "Turning the film back on, Caroline accepts the last Onion ring."
    image caroline_stage2_86 = "/caroline/events/stage2/86.webp"
    scene caroline_stage2_86
    "Sitting back, the pair of you enjoy a relaxing time together."
    image caroline_stage2_87 = "/caroline/events/stage2/87.webp"
    scene caroline_stage2_87
    caroline "That was as good as I remember."
    pc "Yeah, it's kind of one of those ageless classics."
    caroline "So bad it's good."
    pc "Exactly."
    ##Caroline looking at her phone.###
    image caroline_stage2_88 = "/caroline/events/stage2/88.webp"
    scene caroline_stage2_88
    caroline "Shoot, my mum has been phoning me."
    pc "Everything ok?"
    caroline "Yeah, I just didn't really tell her how long I was going to be out."
    image caroline_stage2_89 = "/caroline/events/stage2/89.webp"
    scene caroline_stage2_89
    caroline "I should head home anyway."
    caroline "But thank you for today, I feel…relaxed."
    pc "Then I consider it a success."
    pc "But seriously, I had fun. Feel free to come over whenever you want."
    image caroline_stage2_90 = "/caroline/events/stage2/90.webp"
    scene caroline_stage2_90
    caroline "Careful what you wish for, but thank you."
    caroline "Bye [playername]."
    "Showing Caroline out, you clean up the mess the pair of you made."
    $ carolinestage2event3 = 0
    stop music fadeout 1.0
    if recollection == False:
        $ caroline.weight += 0.5
        $ daytime = 3
        $ phonecall = 1
    return

label Caroline_Stage_2_Event_4:
    ###After lesson###
    "After Daisy dismisses the class to work on their projects, you decide to work with Caroline."
    ###In project room###
    play music "/music/caroline.ogg" if_changed
    image caroline_stage2_91 = "/caroline/events/stage2/91.webp"
    scene caroline_stage2_91
    "Walking into the room you see Caroline has already made herself comfortable."
    image caroline_stage2_92 = "/caroline/events/stage2/92.webp"
    scene caroline_stage2_92
    "The table is covered in books, notepads and noticeably more food this week."
    image caroline_stage2_93 = "/caroline/events/stage2/93.webp"
    scene caroline_stage2_93
    pc "Having a party?"
    caroline "Oh, hey."
    image caroline_stage2_94 = "/caroline/events/stage2/94.webp"
    scene caroline_stage2_94
    caroline "No, but I think I might have overdone it a bit."
    pc "Is this all from Daisy?"
    caroline "In a way."
    image caroline_stage2_95 = "/caroline/events/stage2/95.webp"
    scene caroline_stage2_95
    caroline "I really enjoyed our study session the other evening and since I can't dance I've been feeling a little bored."
    caroline "I wanted to funnel my attention and dedication into something else, like this project."
    pc "I thought you were trying to find a way of relaxing?"
    image caroline_stage2_96 = "/caroline/events/stage2/96.webp"
    scene caroline_stage2_96
    caroline "Yeah, but there is only so much sitting around I can do."
    caroline "I came in early this morning to speak with Daisy and asked her for some extra work while running some ideas by her."
    caroline "Although, I am just realising I should really have run them by you first since you are my partner."
    caroline "I'm still kind of getting used to having a partner who cares about the project as well."
    pc "No, that's all ok with me."
    pc "What did the pair of you come up with?"
    image caroline_stage2_97 = "/caroline/events/stage2/97.webp"
    scene caroline_stage2_97
    caroline "We thought up some ideas but she didn't want to deviate too much from the current assignment."
    caroline "I might have been getting a bit carried away."
    caroline "So she has just assigned us a little bit more food and each week we will have a different focus."
    caroline "Sometimes it will be higher in sugar, salt, fat or other things."
    caroline "That way we can track the variance in data points in association to these other variables and see if there are any extra patterns."
    pc "Sounds interesting to me."
    image caroline_stage2_98 = "/caroline/events/stage2/98.webp"
    scene caroline_stage2_98
    caroline "Great, I guess the only thing left is to start eating."
    image caroline_stage2_99 = "/caroline/events/stage2/99.webp"
    scene caroline_stage2_99
    "Picking up the first of many snacks, Caroline tears it open."
    image caroline_stage2_100 = "/caroline/events/stage2/100.webp"
    scene caroline_stage2_100
    "Between munching down each snack, she reads the numbers out to you once more."
    caroline "Wow these are great, I haven't had them before."
    caroline "And look, they even make raspberry flavoured ones, I should ask Daisy to get me some of those for next time."
    image caroline_stage2_101 = "/caroline/events/stage2/101.webp"
    scene caroline_stage2_101
    "Munching on another snack, Caroline seems to be enjoying herself and the abundance of sweet snacks."
    image caroline_stage2_102 = "/caroline/events/stage2/102.webp"
    scene caroline_stage2_102
    "Soon there is only one snack left, the rest of the box emptied out and now inside carolines rather full looking stomach."
    image caroline_stage2_103 = "/caroline/events/stage2/103.webp"
    scene caroline_stage2_103
    caroline "Wow, these have a lot more sugar in than the other ones."
    caroline "84 grams! not looking forward to the sugar crash later."
    image caroline_stage2_104 = "/caroline/events/stage2/104.webp"
    scene caroline_stage2_104
    "Finishing off the last sweet Caroline sits back in her seat."
    "It is clear to see the impact of the extra portions, her usually slim belly now looking tight and round."
    image caroline_stage2_105 = "/caroline/events/stage2/105.webp"
    scene caroline_stage2_105
    caroline "Mmm, that was fun."
    caroline "I can't wait to see what the results are for this week. That is bound to have had an impact."
    image caroline_stage2_106 = "/caroline/events/stage2/106.webp"
    scene caroline_stage2_106
    caroline "I think that is everything for today, right?"
    pc "Yeah, if you can get me your measurement data I'll keep compiling it."
    image caroline_stage2_107 = "/caroline/events/stage2/107.webp"
    scene caroline_stage2_107
    caroline "Sounds good to me, see you later."
    pc "Bye Caroline."
    #[Change in project work where she now eats more and gets more bloated each session.]
    $ carolinestage2event4 = 0
    stop music fadeout 1.0
    if recollection == False:
        $ caroline.weight = 82
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Caroline_Stage_3_Event:
    ###Get a text from Caroline ###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Caroline', dialogue=dialogue_one)
    $ msg ("Hey, guess who got two tickets to the new Night of the killer chrysanthemums.", who=1)
    pause
    $ msg ("Fancy joining me?", who=1)
    pause
    menu:
        "Yes":
            $ msg ("I'd love to! What time?")
            pause
            $ msg ("6.00 tonight.", who=1)
            pause
            $ msg ("I'll be there.")
            pause
            $ hide_messenger()
        "No":
            $ msg ("I'm busy today, maybe another time.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    ##Movie theatre##
    image caroline_stage3_1 = "/caroline/events/stage3/1.webp"
    scene caroline_stage3_1
    "Arriving at the movie theatre, you see Caroline waving at you enthusiastically, with a large box of popcorn in her other hand."
    image caroline_stage3_2 = "/caroline/events/stage3/2.webp"
    scene caroline_stage3_2
    caroline "You made it."
    pc "I did, I'm excited to see if they did the original justice."
    caroline "Me too, the reviews have been really good."
    caroline "Although you should never trust them."
    image caroline_stage3_3 = "/caroline/events/stage3/3.webp"
    scene caroline_stage3_3
    "Heading into the theatre you take your seats."
    image caroline_stage3_4 = "/caroline/events/stage3/4.webp"
    scene caroline_stage3_4
    "Soon the lights go down and the film start's."
    "Beside you, Caroline continues to munch away at her large popcorn, fully engrossed in the film."
    "While the acting is certainly better, you are happy to see the same campy and ridiculous overtones of the original have made it into the remake."
    "Even a couple of the actors make cameo's as the parents of their original characters."
    image caroline_stage3_5 = "/caroline/events/stage3/5.webp"
    scene caroline_stage3_5
    "Time flies by as you both enjoy the film, but soon the lights come up as the credits start rolling."
    image caroline_stage3_6 = "/caroline/events/stage3/6.webp"
    scene caroline_stage3_6
    caroline "That was amazing, I'm so glad they didn't try to make it a serious film."
    pc "Yeah, I felt like they got the balance right."
    pc "Although I kind of missed the bad CGI effects."
    caroline "Me too, but I suppose we can always watch the original if we want that."
    pc "True."
    image caroline_stage3_7 = "/caroline/events/stage3/7.webp"
    scene caroline_stage3_7
    caroline "I definitely need a drink though, all that popcorn really gave me a dry mouth."
    pc "I was thinking of heading to get some food if you wanted to join me?"
    caroline "Sure, I didn't eat before I came here."
    image caroline_stage3_8 = "/caroline/events/stage3/8.webp"
    scene caroline_stage3_8
    caroline "Where were you thinking?"
    pc "Bunny Bites?"
    caroline "Isn't that the weird palace with the waitresses in bunny outfits?"
    caroline "I am kind of surprised you would suggest there."
    pc "It's not like that, I actually work there."
    image caroline_stage3_9 = "/caroline/events/stage3/9.webp"
    scene caroline_stage3_9
    caroline "Really?"
    pc "Yeah, plus the food is actually really good."
    caroline "Well, I have been meaning to start trying new things."
    image caroline_stage3_10 = "/caroline/events/stage3/10.webp"
    scene caroline_stage3_10
    caroline "Why not, let's go."
    image caroline_stage3_11 = "/caroline/events/stage3/11.webp"
    scene caroline_stage3_11
    "Walking through town, you make it to Bunny Bites."

    ##In bunny bites###
    image caroline_stage3_12 = "/caroline/events/stage3/12.webp"
    scene caroline_stage3_12
    "You both take a seat in one of the booths."
    image caroline_stage3_13 = "/caroline/events/stage3/13.webp"
    scene caroline_stage3_13
    caroline "What would you recommend here?"
    pc "The burgers are really good, same with the chicken nuggets."
    pc "The pizza is ok, but honestly you can probably get better in town."
    image caroline_stage3_14 = "/caroline/events/stage3/14.webp"
    scene caroline_stage3_14
    caroline "Oooh, and you guys do milkshakes too!"
    pc "I don't have too much of a sweet tooth, but they sell really well so they must be good."
    ###Marie appears###
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Hi guys, are you ready to order?"
    image caroline_stage3_15 = "/caroline/events/stage3/15.webp"
    scene caroline_stage3_15
    caroline "Yes thank you."
    caroline "Can I get a double cheeseburger, some chicken nuggets, a medium soda and a large milkshake please."
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Sure thing, we actually have a deal on for a burger, drink and free fries or onion rings if you would like?"
    image caroline_stage3_15 = "/caroline/events/stage3/15.webp"
    scene caroline_stage3_15
    caroline "That sounds perfect, I'll take the onion rings if that is ok?"
    marie "Absolutely."
    "You are not aware of any deals, maybe Marie was just being nice."
    pc "Can I just get some chicken nuggets and fries please."
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Great, I'll be out with your food as soon as it's done."
    image caroline_stage3_15 = "/caroline/events/stage3/15.webp"
    scene caroline_stage3_15
    caroline "Thank you."
    image caroline_stage3_16 = "/caroline/events/stage3/16.webp"
    scene caroline_stage3_16
    "Sitting back you relax and make small talk waiting for the food to arrive."
    pc "So you said you are trying new things?"
    image caroline_stage3_17 = "/caroline/events/stage3/17.webp"
    scene caroline_stage3_17
    caroline "What…oh yeah."
    caroline "I guess I have started to realise quite how much of a bubble I have existed in since getting injured."
    caroline "In some ways I am starting to think it's been a good thing for me and given me more time to think about my life."
    pc "Sounds serious."
    image caroline_stage3_18 = "/caroline/events/stage3/18.webp"
    scene caroline_stage3_18
    caroline "Yeah, but in a good way."
    caroline "I always thought that being so dedicated to one thing would bring me all sorts of opportunities."
    image caroline_stage3_19 = "/caroline/events/stage3/19.webp"
    scene caroline_stage3_19
    caroline "And don't get me wrong, it has. I have been lucky enough to travel all over the place and see some amazing things."
    caroline "But at the same time, I've started to notice how limiting it is in other aspects of my life."
    caroline "So I have made the decision to approach my life and ballet differently going forwards."
    pc "Sounds like a big change."
    image caroline_stage3_20 = "/caroline/events/stage3/20.webp"
    scene caroline_stage3_20
    caroline "Yeah, but I think it will help me."
    image caroline_stage3_21 = "/caroline/events/stage3/21.webp"
    scene caroline_stage3_21
    "A moment later, Marie returns with your food."
    image caroline_stage3_22 = "/caroline/events/stage3/22.webp"
    scene caroline_stage3_22
    "Picking up the soda, Caroline sucks it dry in one go."
    image caroline_stage3_23 = "/caroline/events/stage3/23.webp"
    scene caroline_stage3_23
    caroline "Ahh, that's better."
    caroline "I really needed that. Now let's see if you were right about the burgers."
    image caroline_stage3_24 = "/caroline/events/stage3/24.webp"
    scene caroline_stage3_24
    "Taking her first bite you see her eyes light up as she takes another."
    image caroline_stage3_25 = "/caroline/events/stage3/25.webp"
    scene caroline_stage3_25
    caroline "Wow, these are amazing!"
    caroline "Way better than the ones we have at home."
    image caroline_stage3_26 = "/caroline/events/stage3/26.webp"
    scene caroline_stage3_26
    "Digging in, Caroline stuffs her face with the greasy food."
    image caroline_stage3_27 = "/caroline/events/stage3/27.webp"
    scene caroline_stage3_27
    "Devouring her entire meal and filling her growing belly."
    image caroline_stage3_28 = "/caroline/events/stage3/28.webp"
    scene caroline_stage3_28
    window hide
    pause
    image caroline_stage3_29 = "/caroline/events/stage3/29.webp"
    scene caroline_stage3_29
    caroline "Mmmm, you were right. This place is amazing."
    pc "I told you."
    caroline "See, this is why I need to step out of my comfort zone more often."
    image caroline_stage3_30 = "/caroline/events/stage3/30.webp"
    scene caroline_stage3_30
    "Leaning back Caroline relaxes in the booth, showing off her stuffed belly."
    image caroline_stage3_31 = "/caroline/events/stage3/31.webp"
    scene caroline_stage3_31
    caroline "Thanks for today, it was fun but I better head back home."
    pc "Thanks for the invite, I had fun too."
    caroline "Well I still owed you for the takeaway the other week."
    pc "Consider us even."
    image caroline_stage3_32 = "/caroline/events/stage3/32.webp"
    scene caroline_stage3_32
    caroline "Great, see you soon."
    pc "Bye Caroline."
    "Caroline can now visit Bunny Bites."
    "This is Caroline's final event in this update, her story will continue next update."
    stop music fadeout 1.0
    if recollection == False:
        $ caroline.weight += 1
        $ daytime = 3
        $ phonecall = 1
    $ carolinestage3event = 0
    return

label Caroline_Stage_3_Event_2:
    ##Get a text from Caroline##
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Caroline', dialogue=dialogue_one)
    $ msg ("Hi, it's Caroline again.", who=1)
    pause
    $ msg ("I was wondering if you wanted to meet up before the presentation and go through our report again?", who=1)
    pause
    $ msg ("You know, just to double check it.", who=1)
    pause
    menu:
        "Yes":
            $ msg ("Sure thing.")
            pause
            $ msg ("I was thinking of heading out for some food at Bunny bites if you want to join?")
            pause
            $ msg ("Yeah, see you there.", who=1)
            pause
            $ hide_messenger()
        "No":
            $ msg ("I'm busy today, maybe another time.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    ###Bunny bites###
    "Walking into Bunny Bites, you don't see Caroline yet so grab yourself a booth and wait."
    "It's not long before you spot her walking in."
    "Did she seem bigger than the last time you saw her?"
    "Maybe it was just the lighting?"
    caroline "Hi, thanks for the invite, I was just thinking about getting some food myself."
    pc "No problem, seemed like as good a place as any to go through things."
    caroline "Totally, plus it means I can try their burgers again."
    caroline "So how far have you got with the write up?"
    pc "Pretty far, most of it was fairly simple to write up."
    pc "Just a bunch of numbers and talking about how they change."
    pc "But I added some statistics to the methods."
    pc "They don't really show much right now, but I figure we can just repeat them for each report and it will be easier to show change."
    "Handing over your work, Caroline goes through it."
    caroline "I am impressed, this seems really thorough."
    pc "Thanks."
    caroline "There seems to be some bits missing at the end though."
    pc "Yeah, we could do with another set of measurements, if you are ok with that?"
    caroline "Of course, I've got to keep up with my part of the project."
    pc "If it's easier, we can head back to my place after we eat and quickly do it then?"
    caroline "Yeah, that sounds perfect."
    #Marie arrives at the table###
    marie "Hi, what can I get you both?"
    caroline "Hi, can I get two burgers, a large fries and soda please."
    marie "Sure thing."
    pc "Can I get a burger, fries and a soda as well."
    marie "I will be right out with your food."
    ###Marie leaves###
    pc "So how have you been?"
    caroline "Good…I think."
    pc "You don't sound too certain."
    caroline "Still getting used to things, but actually I have been feeling a lot better recently."
    caroline "I've been taking your advice to relax more."
    pc "That is good, found a new hobby or just watching films?"
    caroline "Yeah, I've been getting into painting, watercolours at the moment."
    caroline "Mainly because it's harder to see the imperfections if I mess up."
    pc "That sounds great, I'm sure you are really good at it."
    pc "Maybe you could show me some time?"
    ###Caroline blushing awkwardly###
    caroline "Uh…yeah if you want too."
    caroline "That would be nice."
    pc "Only if you want to show me though, I don't want to force you."
    caroline "No, it would be nice."
    caroline "I've never really shared my hobbies with many people."
    ###Marie returns with a lot of food###
    marie "Here you both go, here is your order."
    "Despite calling it Caroline's order, it is much more than that."
    "Piling the plates and food onto the table in front of Caroline, it's clear Marie has made another 'mistake'."
    caroline "I…um, are you sure this is ours?"
    marie "Why, did I miss something?"
    caroline "No, it's more than we ordered."
    marie "Oh sorry, our till has been really weird today."
    marie "But since it's gone through the system already, are you ok to take it at no extra cost."
    caroline "Sure, that's no problem."
    marie "Great, enjoy your meal."
    ##Marie leaves###
    "Despite the change in plans, Caroline seems happy with her meal."
    caroline "That is a bit of a result, I guess I must have done something nice recently."
    pc "Done something nice?"
    caroline "Sorry, I'm kind of a believer in Karma, where good things happen if you do nice things."
    caroline "So I guess I did something to deserve this treat."
    caroline "Or maybe the universe is paying me back for the injury."
    pc "I get that, I definitely feel like there is some truth in it."
    "Picking up a large slice of greasy cheese pizza, Caroline takes a bite."
    caroline "Mmmm, it's so bad it's good."
    "Taking another bite you watch Caroline begin her feast."
    "Picking up one treat after another she takes large bites, yet somehow keeping control of her manners."
    "Burgers, pizza slices, onion rings and chicken nuggets all devoured in a poised and almost respectable manner."
    "Beneath the table, you were able to see the slender dancer's stomach bulging more and more."
    "Each mouthful adding to her growing waist which grew with each passing moment."
    "The conversation was basically dead as she enjoyed her binge, and you enjoyed watching it."
    "After almost 30 minutes of over indulgence Caroline let out a heavy sigh, looking defeated by the mountain of food."
    caroline "You were right about this place, the food is so good."
    "Placing a hand on her enlarged gut, Caroline leans back in the booth."
    caroline "I think I'll have to get the rest to go."
    caroline "If I eat one more thing I think I might pop."
    "Despite the sentiment and groaning coming from her stomach it seems like Caroline had enjoyed that."
    pc "Want me to grab a box to take back to mine?"
    caroline "Yeah, if you don't mind."
    "Going up to the counter you grab a takeaway box or two from an entranced Marie who had clearly enjoyed the show as well."
    "Going back to the table you help Caroline pack away her food for later."
    caroline "Well, I guess we should head back to yours if we want to go through the data."
    "Helping Caroline to her feet, she cradles her large belly as the pair of you walk back to your place."
    ###player house###
    "As a bloated Caroline takes a seat on your sofa you take out your notes again."
    caroline "Oww I shouldn't have eaten all that food."
    pc "Are you feeling ok?"
    caroline "Yeah, I just realised it is going to throw off our data!"
    caroline "I didn't think about it but there is going to be a weird bump in our trends."
    pc "I'm sure that will be fine, there is always some variation in any data set."
    caroline "True, plus I am sure it will even out by the end of the project."
    caroline "Do you have a tape measure I can borrow to take the records."
    pc "Umm…good question."
    "Finding an old tape measure you hand it over to Caroline who disappears into your bathroom to measure herself."
    "Flicking through tv channels, you start to wonder what is taking her so long."
    ###At closed door / bathroom door###
    pc "Everything ok in there?"
    caroline "Oh yeah, well kind of."
    caroline "I might need a hand."
    ###Caroline walks out##
    caroline "I can't seem to be able to read the numbers because of my stomach."
    caroline "Any chance you can help me?"
    pc "Sure."
    "Kneeling on the floor, Caroline wraps the tape measure around her engorged gut."
    "The tape measure obscured from her view, you lean in closer to get the numbers."
    "With your face close to her stomach you can hear it grumbling at how much food was stored inside it."
    "The strangely intimate position letting you feel the heat from her body radiating out as you peer closer."
    pc "Looks like [caroline.waist_size] to me."
    caroline "Well, that is quite the spike in our data."
    caroline "Thanks though, I was trying to use the mirror but couldn't get the angle correctly."
    pc "No worries."
    ###On the sofa again.##
    "Returning to the lounge you plug in the new data."
    "As Caroline predicted there is now a big peak near the end."
    caroline "Well, next time I'll have to wait until after we record these numbers to eat at Bunny bites."
    caroline "You know what, I'll grab another set of data tomorrow morning before class."
    caroline "Hopefully this food baby will have gone down by then."
    pc "Sure, we already have all the formulas written down so it should be easy to recalculate everything and swap the numbers out."
    caroline "Perfect, I guess I will see you tomorrow."
    pc "You don't have to leave right now."
    pc "Have you got any plans, I was thinking of chucking on a film or something if you want to join?"
    caroline "That sounds nice."
    pc "Do you want to choose?"
    caroline "No, you can choose this time."
    "Thinking about it, you choose a feel good movie for the pair of you to watch."
    "Sitting back down you notice Caroline breaking open her left overs."
    caroline "Nugget?"
    "Taking one, you both sit back and relax while sharing the food."
    "Enjoying a quiet night together, you finish off the food and as the sun starts to set say goodbye."
    caroline "Thanks for tonight, it was fun."
    pc "Yeah I enjoyed it too."
    caroline "See you in class tomorrow."
    pc "Did you want to meet up a bit earlier?"
    caroline "That would probably be a good idea."
    caroline "Gives us a little bit more time to prepare."
    pc "In that case, see you tomorrow."
    caroline "Bye."
    $ carolinestage3event2 = 0
    return

label Caroline_Stage_3_Event_3:
    ###In class##
    "Arriving at class a little early, you see Caroline standing next to her desk."
    pc "Hey Caroline."
    caroline "Hi, ready for our presentation?"
    pc "I think so."
    caroline "Great, I just put in my new measurements and it already looks better."
    caroline "It still goes up but doesn't have the same weird spike we saw last night."
    pc "Ok, that sounds better. Should make the trends easier to compare week to week."
    caroline "Yeah, although I have some good and bad news about that."
    caroline "My leg is officially healed, I can get back to dancing!"
    pc "That's great news, I am happy for you."
    pc "But that only sounds like good news to me."
    caroline "Well, it means I shouldn't be eating as much and need to get back into shape."
    caroline "So, our data might not be as straightforward as we first thought."
    caroline "Sorry about that, I realise I have just added a ton more work to do."
    pc "No need to apologise, I am happy your leg is healed."
    pc "When it comes to the project, I am sure we can figure it out."
    pc "If I need to put in a few more hours I am happy to."
    caroline "Aw, you're the best."
    "Reaching over, Caroline hugs you tightly."
    lucy "Eww, get away from her weirdo."
    "You don't even need to turn around to know who that was."
    caroline "Hey Lucy, how have you been?"
    lucy "Good, my dad just got a promotion so we spent a week in Italy."
    caroline "I guess that's why I haven't seen you around much in class."
    lucy "Yeah, there is more to life than school, you know?"
    caroline "I'm starting too."
    lucy "See, you get me."
    lucy "Anyway, it was so nice but there was this loser guy who kept hitting on me."
    "Turning to look at you with a raised eyebrow, it is clear this is supposed to be a conversation between the two of them."
    pc "I'll let you guys catch up."
    lucy "Thanks…"
    "Sitting down at your desk, you go through your notes for the presentation."
    "It seems like all your systems worked as expected to update everything when Caroline put in the new numbers."
    "A few minutes later, Daisy arrives."
    teacher "Hello class, why don't we start today's lesson with a presentation from Caroline and [playername]."
    "Going up to the front, you stand beside her."
    caroline "So we have been studying the impact of increased consumption on our bodies."
    caroline "[playername], has been acting as more of a control measure."
    caroline "As you can see, their data barely changes."
    caroline "But for me, you will notice an increase in weight during this period of time."
    caroline "This was also paired with a period of inactivity for myself, doubling the potential impact on my body."
    caroline "It has only been a short while, but going forwards we will be investigating the impact of exercise on the rate of weight gain."
    caroline "That should give us a set of data we can compare to this one."
    teacher "That all sounds pretty thorough, and well done for thinking ahead."
    teacher "But beyond the data, how have you been feeling?"
    caroline "Pretty good overall, other than the obvious injury to my leg."
    caroline "I don't feel like my diet has changed anything in my life."
    teacher "So you haven't noticed any changes?"
    caroline "None I can say for certain are due to what I have been eating."
    teacher "That is an excellent point and something to consider about everyone's group projects."
    teacher "Sometimes trends in the data we think we see, can be due to external factors."
    teacher "As such, I would like you to keep a diary so that you can track anything you might not realise is important."
    teacher "Good work you two, thank you for your presentation."
    teacher "I look forward to seeing more, you can go back to your seats."
    "Taking your seats, Caroline gives you a thumbs up."
    #[Regular class?]
    $ carolinestage3event3 = 0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        jump freetime
    return


label Caroline_Stage_3_Event_4:
    ###At home, morning get a text from Caroline###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Caroline', dialogue=dialogue_one)
    $ msg ("Hey, sorry it is early. Are you awake?", who=1)
    pause
    $ msg ("Yeah, is everything ok?")
    pause
    $ msg ("Yeah, I was wondering if I could come over again?", who=1)
    pause
    $ msg ("Yeah sure, give me 15 minutes to tidy up a bit.")
    pause
    $ msg ("You don't need to worry about the mess.", who=1)
    pause
    $ msg ("Also…I kind of might be outside your door right now.", who=1)
    pause
    $ hide_messenger()

    "You go to text her back, before realising you could just let her in."

    ###Hallway / doorway###
    "Grabbing your clothes, you make your way to the front door."
    pc "Morning."
    caroline "I am so sorry to bother you this early."
    pc "It's fine, do you need something?"
    caroline "Just a place to hide."
    pc "Cops after you again?"
    caroline "No, it is worse, my parents."
    caroline "I told them I had to be somewhere but after I left I kind of realised I didn't have anywhere to go."
    caroline "I would have gone to town, but I realised I left my purse in my room and didn't want to go back in."
    caroline "Which kind of meant you were the only option."
    pc "I did say you were free to come over any time."
    pc "Are you sure you are ok?"
    caroline "Yeah…well maybe."
    caroline "It's just my parents, they are driving me crazy."
    pc "Well, you are free from them while you are here."
    pc "Want a cup of tea or something, the pool should be nice and warm too."
    caroline "Oohhh, that sounds amazing!"
    pc "Great, well if you want to take a dip I think I am going to have a quick shower and I will be right out with your tea."
    "Smiling, Caroline heads towards the pool."

    ###Kitchen###
    "Taking a quick shower, you go back down to the kitchen and make two cups of tea."
    "Taking them out to the pool, you find Caroline gently floating in the water."
    pc "Here is your tea."
    ###Caroline standing in the water at the edge of the pool.###
    caroline "You are too kind."
    "Pausing for a moment, she looks up to you."
    caroline "I mean that, you know that right."
    caroline "I really don't know why you have been so nice to me these last few weeks."
    caroline "I certainly didn't give you a reason too when we first met."
    pc "It's just a cup of tea."
    caroline "It's not though."
    ##Caroline getting out of pool and sitting next to you on the edge with feet in the water##
    ##Her Looking down kind of awkwardly##
    caroline "You are the only one who has really been here for me."
    caroline "All my other friends disappeared and now even my family are getting on my back about things."
    pc "I am sure they only want what is best for you."
    caroline "More like for me to be the best."
    pc "What?"
    caroline "Sorry, that's just…never mind."
    "There is an awkward pause as she gently kicks her feet in the pool water."
    pc "I don't mind if you want to talk about things."
    caroline "See, that's what I mean."
    caroline "I guess being injured and coming back into things has made me realise I'm not sure I want my old life back."
    caroline "It just feels so vapid and boring now that I have seen the other side of things and had someone looking out for me like a real friend."
    "Caroline looks down again, clearly slightly embarrassed by that omission."
    caroline "It's hard to get back into the same corner I was stuck in, even if I didn't realise at the time it was a corner."
    caroline "My parents don't know what to say, or do."
    caroline "It's like all we ever talked about was Balet, so when I was injured there was so much silence."
    caroline "Although, I think I preferred it to the judgemental comments they are making now."
    caroline "Sorry, this is probably sounding super depressing. I didn't mean to put this all on you."
    pc "No it's not depressing, it just sounds like you are figuring out what you want out of life."
    pc "If anything, I think it's kind of cool, or hopefully will be when it gets easier for you."
    "Lunging forwards, Caroline suddenly hugs you deeply."
    "Her wet body pressing against your and soaking your shirt before she releases you."
    caroline "Sorry, I'm not really a huggy person, I don't know what came over me."
    pc "It's fine, although I think I need a new shirt."
    caroline "Sorry."
    pc "Are you hungry, I was thinking about going out for a bite to eat?"
    caroline "Now you mention it, I didn't have any breakfast."
    pc "Great, you remember where the towels are if I get changed as well?"
    caroline "Yep."
    "Standing up, you follow Caroline towards your house."
    "Now behind her, you notice a small tattoo peeking out from her swimsuit."
    "Had she always had that, or was that what her parents had been judgemental about?"
    ##image of Caroline drying her hair or something?##
    "Drying yourself off and getting changed, you head out to the cafe in town for some breakfast."

    ##Cafe, standing in line##
    caroline "This place smells amazing, I didn't know this place was here."
    "Studying the menu, she seems lost for choices."
    caroline "What would you recommend?"
    pc "The pasties here are some of my favourites, like the danish."
    pc "It kind of depends on what kind of things you like?"
    caroline "I like fruit compote."
    pc "That's like jam, right?"
    "Laughing, Caroline shakes her head jokingly at your ignorance to the finer things in life."
    caroline "Yeah I guess, fancy jam."
    pc "They do a raspberry crown thing you might like."
    caroline "Sounds good to me."
    ##being served by Hanna###
    pc "Hi, can I get two danish pastries and two raspberry crowns please."
    hanna "Sure thing, you are in luck though."
    hanna "We currently have a 3 for two offer on pastries this morning."
    "Putting your pastries on a plate, you and Caroline go to find a seat."
    ##Sitting at table##
    "Taking her first bite, Caroline smiles and you can see her shoulders sink down as she enjoys her treat."
    pc "Feeling better?"
    caroline "Much, thanks."
    pc "I told you they were good."
    "Sitting quietly, you enjoy the moment as you both eat your breakfast."
    ###Not bloated, doesn't look any different just story things###
    caroline "I feel like this is the only quiet moment I have had in weeks."
    pc "It's nice to get away from it all."
    caroline "Yeah, life has been pretty hectic."
    caroline "It feels nice but kind of weird to just sit here and remember there a lots of people out there."
    pc "And you don't need to please them all."
    caroline "What?"
    pc "Sorry, I didn't mean it in a negative way."
    pc "I just feel like you are putting yourself out there and trying to make everyone happy but forgetting the most important person."
    caroline "Oh, and who is that then?"
    pc "You!"
    caroline "Me?"
    pc "Yeah, you need to remember that your choices and what you want to do is as important as pleasing anyone else."
    pc "It is your life, not theirs."
    caroline "It doesn't feel like it sometimes."
    pc "I think that is making my point for me."
    "Sitting quietly, Caroline nibbles a couple of crumbs while deep in thought."
    "Your peaceful moment is interrupted by sudden heavy metal."
    caroline "Shoot, sorry that's my phone."
    "Checking it, she sighs deeply."
    caroline "It's my mum, guess I better face the music."
    caroline "Thank you so much though, I really appreciate you listening to me."
    pc "No problem, see you soon Caroline."
    caroline "Bye [playername]."
    "Leaving, you take a leisurely walk back home."
    $ carolinestage3event4 = 0
    return

label Caroline_Stage_3_Event_5:
    ###Text from Caroline###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Caroline', dialogue=dialogue_one)
    $ msg ("I need your help, it's an emergency!", who=1)
    pause
    $ msg ("What's wrong?")
    pause
    $ msg ("It's my mum's birthday.", who=1)
    pause
    $ msg ("I thought you said it was an emergency?")
    pause
    $ msg ("It is, they said it was going to be a small get together but it's like a full on party.", who=1)
    pause
    $ msg ("I don't know if I can survive it without at least one person I like being there.", who=1)
    pause
    $ msg ("There is free food.", who=1)
    pause
    $ msg ("Sure, let me know where and when.")
    pause
    $ msg ("Uhh..kind of right now and at my house.", who=1)
    pause
    $ msg ("I'll text you my address, you're a lifesaver!", who=1)
    pause
    $ msg ("Oh, and do you have a suit?", who=1)
    pause
    $ msg ("A suit?")
    pause
    $ msg ("I'll take that as a no, wear something smart.", who=1)
    pause
    $ hide_messenger()

    ###PC house ###
    "Rummaging through your wardrobe you find a shirt and tie."
    "Hopefully it will be good enough for this party."

    ###Fancy house / garden area###
    "Following the signs put up to direct guests, you make your way around to a large garden."
    "There seem to be a lot of guests, you feel a little awkward but thankfully you notice Caroline across the lawn."
    ##Thinking Lucy and a couple of random NPC’s in a group##
    "Approaching, you see her eyes light up as she notices you."
    caroline "[playername], you made it!"
    lucy "Ughh, who invited the charity case?"
    caroline "I did."
    lucy "Why?"
    caroline "So I wouldn't have to listen to you talk about getting botox all day."
    lucy "Rude!"
    "Walking off in a huff, Lucy and her friends leave you with Caroline."
    pc "Bit more than a small get together."
    caroline "I know right, although I should have guessed."
    caroline "Thanks for coming, I assume this kind of event isn't really your scene?"
    pc "Can't say I have ever been to one, so who knows."
    caroline "I appreciate you coming to save me though."
    caroline "Oooh, and I promised free food."
    caroline "You have to try these, they are so good. I have had like two dozen already."
    "Waving over a waiter with a tray, Caroline grabs a handful of the small fancy looking pastries."
    "Picking up one, you bite into it."
    caroline "They are good right, like tiny little salmon en croute."
    pc "Yeah, I guess..."
    caroline "You are a terrible liar."
    caroline "Maybe try something else, I'm sure we can find at least one thing to your taste."
    caroline "Oooh, what about…"
    cmum "Don't you think you have had enough of those Caroline?"
    cmum "You won't get back into top form if you keep eating like that."
    caroline "I wasn't, they are for my friend here."
    cmum "Ah, and who might you be."
    cmum "Don't tell me, you are Reginalds son. I can see the resemblance."
    pc "Uhhh, no mam. I am just a friend from college."
    cmum "Ah ok, so what do your parents do?"
    cmum "Banking, stocks, what?"
    pc "Oh nothing like that, just regular people."
    cmum "That's interesting…anyway."
    cmum "You need to be watching what you eat, remember what your coach said, and your doctor."
    cmum "We let you get away with gaining some weight while you were injured but now it is straight back to it!"
    caroline "Mum!"
    cmum "What, it's no secret. Everyone can see it."
    caroline "Jesus, do you have to be so…you right no?"
    cmum "Is that anyway to speak to me in front of guests, especially on my birthday?"
    caroline "Well, why don't you go and speak to some of your guests then, instead of embarrassing me."
    cmum "Perhaps you are right, but we will talk about your behaviour later."
    "Walking off, Caroline's mum goes to greet some of her other guests."
    caroline "Sorry about that, I swear she still thinks I'm 12 and not an adult."
    pc "No problem, although I am starting to see why you needed to come around mine the other day."
    caroline "That's not even half of it."
    pc "Have you ever said anything to them, maybe let them know you don't like it?"
    caroline "No…"
    caroline "Partly because I know they are right."
    caroline "They only want what is best for me."
    caroline "I do need to get back into shape if I want to continue Ballet."
    ##Blushing / shocked she said that.##
    caroline "I mean when I continue!"
    "Your conversation is interrupted by a loud roll of thunder."
    "Above you, the sky seems to open as a deluge of rain sends guests rushing for cover."
    caroline "Over here."
    "Following Caroline, you run towards the house but can't avoid getting drenched in the sudden storm."
    "Laughing, you make it to the cover of her porch."
    caroline "Where did that come from?"
    pc "I know right."
    "Looking down your clothes are completely soaked, although it was worse for Caroline."
    "Her white clothes almost see through after being drenched."
    caroline "Oh my god."
    "Folding her arms across herself to protect her modesty, she turns around."
    "Looking upwards, you divert your eyes."
    caroline "I… I'll be right back."
    "Rushing inside, Caroline leaves you alone."
    "A few moments later, you get a text telling you to meet her around the front of the house."
    ###at front of house.###
    caroline "Is the coast clear?"
    pc "There isn't anyone around, if that's what you mean?"
    caroline "Perfect!"
    "Opening the door, you see Caroline has changed into something far more casual than her usual style."
    caroline "Let's go!"
    pc "Go where?"
    caroline "Anywhere but here."
    ###Caroline in front of you, holding your hand and leading you away.###
    "Grabbing your hand, Caroline all but pulls you down her drive and away from the party."
    ###Town shot###
    "Walking around for a little bit, you head into the cafe for a bite to eat."
    ##Town cafe - Caroline taking bites of her food occasionally###
    "Ordering food, you grab a table together."
    caroline "Uhhh, it is good to finally relax."
    pc "Do parties stress you out?"
    caroline "No, just those with my parents."
    caroline "They are always so pretentious, showing off to their friends."
    caroline "Although, I kind of get it."
    pc "Get it?"
    caroline "Yeah, they are first generation immigrants."
    caroline "So there are a lot of holdovers from back home, like they have to show off to fit in and prove themselves to the entire country."
    pc "It can't have been easy."
    caroline "Yeah, my family worked so hard to build what we have now."
    pc "I meant for you."
    caroline "Oh…yeah I guess."
    caroline "Although honestly, I shouldn't complain about it. There are a lot of people less fortunate than myself."
    pc "Doesn't stop it being stressful for you."
    caroline "Very true."
    caroline "You are surprisingly wise, give your…"
    ###Caroline gesturing at us###
    pc "My?"
    pc "You just kind of waved at all of me."
    caroline "Exactly."
    "Smiling, Caroline continues eating as you enjoy your own food."
    pc "Don't you think they will notice you are gone?"
    caroline "Maybe, but there are plenty of other guests to keep them occupied."
    caroline "I just needed a couple of hours away from it all."
    pc "Well, I am happy to be your accomplice."
    pc "Although, I already think your mum might not like me."
    caroline "Oh, if she didn't approve you would know."
    caroline "Luckily I think you caught her in a good mood."
    pc "Really?"
    caroline "Yeah, trust me."
    caroline "The first friend I took home faced an inquisition from her."
    pc "Was that Lucy?"
    caroline "God no..."
    caroline "Lucy was almost their idea."
    pc "Their idea?"
    caroline "Yeah, they made me sign up for clubs and stuff when I was little."
    caroline "Supposedly to make friends, but it was more like networking so they could find the most 'suitable' friends for me to have."
    pc "And Lucy won?"
    pc "No offence to her…"
    ###Caroline laughing / smiling##
    caroline "More her parents, they are super successful media moguls."
    caroline "It meant they were a good connection for my parents, and they thought I should be friends with Lucy so we could take over the world together."
    pc "Doesn't seem like she is that interested in taking over the world."
    caroline "No, she is almost the definition of a spoiled rich kid."
    caroline "Don't tell her I said that."
    pc "Weirdly, I don't think she would take it as an insult."
    caroline "You might be right about that."
    "Hearing her phone buzz, she picks it up and smiles."
    caroline "Her ears must have been burning."
    caroline "She is wondering where I am."
    caroline "I should probably head back, it is my mum's birthday after all."
    pc "Want me to come back with you?"
    caroline "No, that's ok. I think I can manage a couple more hours."
    caroline "Thanks for running away with me for the afternoon though."
    pc "Anytime."
    "Finishing up your food, you say goodbye to Caroline and head home."
    $ carolinestage3event5 = 0
    return

label Caroline_Stage_3_Event_6:
    ### in the usual room###
    "Arriving at the room, you are surprised to see Caroline isn't already there."
    "Your partner usually being the more punctual out of the two of you."
    "Grabbing a chair, you wait for her to arrive."
    ###Caroline arriving holding a piece of paper and looking excited###
    caroline "[playername]!"
    caroline "We finally got our grade back for the report we handed in."
    pc "How did we do?"
    caroline "We got an A, not that there was ever any doubt."
    pc "That's great, all the hard work paid off."
    caroline "Totally, and I think we deserve a reward."
    caroline "We should go somewhere fun, do something."
    pc "What about our class work?"
    caroline "We can take a day off, it isn't like we are behind on anything."
    "Part of you wonders who this new Caroline is, skipping class?"
    pc "Sounds good to me, what did you have in mind?"
    caroline "What about that bar in town, I forget what it is called."
    pc "Velvet shadows?"
    caroline "Yeah!"
    pc "Sure, I think it's open."
    "Grabbing your bags, you head into town with Caroline."

    ###Velvet shadows###
    "Entering Velvet shadows, you can see Caroline looking around."
    "It is clear from the way she is walking, this is her first time here."
    pc "I take it you haven't been here before?"
    caroline "No, wait…you have?"
    caroline "Not judging."
    pc "Yeah, I have a friend who works here."
    caroline "Really?"
    pc "Yeah, Maya is one of the dancers here."
    pc "Have you met Amber that I work with, they are good friends and so I met her through Amber."
    caroline "Oh ok…"
    ###Tattooed model dancer, does not have to be a known character.###
    "Caroline's response is cut short as she catches an eyeful of a stage dance."
    "The heavily tattooed woman on the pole catching her eye."
    pc "Not sure it is good etiquette to stare."
    ###Caroline blushing###
    caroline "What..oh I…"
    pc "Should we get a drink?"
    caroline "Yeah!"
    ##At bar##
    bartender "What can I get you love?"
    caroline "Um…what have you got?"
    bartender "The usual stuff, beers, cider, cocktails."
    bartender "Whatever you fancy, we probably have it somewhere."
    caroline "I…uh, can I get a beer."
    bartender "Sure thing."
    "Ordering yourself a Lemonade you take a seat."
    pc "Living up to your expectations?"
    caroline "The dancers are all so pretty."
    pc "I think that might be the point."
    "Picking up her drink, Caroline takes a sip."
    "By the repulsed look on her face, it is clear she isn't a fan."
    pc "Something wrong with your beer?"
    caroline "I don't think I like it."
    pc "Maybe it is off, you can probably get another."
    caroline "No, I mean beer."
    pc "Is this your first drink?"
    caroline "Yeah, kind of…"
    caroline "My parents never let me drink, even though I can legally."
    pc "I don't think you have been missing much with beer."
    pc "Most people drink it because it is cheaper than spirits or rum."
    "Taking another sip, it doesn't seem like Caroline enjoyed it more than the first."
    pc "Want to swap?"
    caroline "You don't mind?"
    pc "No, it might be a bit early for a beer but the stuff here is pretty weak."
    caroline "Thanks."
    "Swapping drinks, she seems much happier with her lemonade."
    pc "So, what made you want to rebel?"
    caroline "What?"
    pc "Your first drink, usually a bigger thing than this."
    caroline "I'm not sure."
    caroline "Just figured I would give it a try."
    caroline "If you haven't noticed I've had a bit of a sheltered upbringing."
    pc "A bit?"
    caroline "Shut up…"
    caroline "Ok, a very sheltered upbringing."
    caroline "Since getting injured and I guess being forced out of that life, part of me doesn't want to go back to it."
    caroline "I feel like I want more than what I had before, to become my own person."
    caroline "Even if it means losing everything I have worked so hard to get."
    pc "Sounds intimidating, but if it is what you want you should give it a go."
    caroline "It is what I want, and strangely it doesn't feel that intimidating."
    caroline "It is kind of freeing."
    pc "I get that, sometimes a change can be good."
    caroline "Exactly, plus everything I have done is due to like a dozen people."
    caroline "It almost feels like everything I have achieved is theirs and I have just been the instrument for them to use."
    pc "I get the feeling this has been on your mind for a while."
    caroline "Yeah, I think part of me knew it even before I was injured."
    caroline "I just kind of accepted it, thought it was part of the process."
    pc "But now you have broken out, you don't want to go back in."
    caroline "Exactly, I don't want to limit my experiences in life for one thing."
    caroline "To step out of my sheltered life and do more, experiment a little."
    pc "Sounds exciting."
    caroline "It is, it really is."
    caroline "I wake up excited to see what every new day brings."
    caroline "It is fun to not have every minute of every day scheduled weeks in advance for optimum performance."
    pc "Welcome to the club, not sure I have ever had anything scheduled for optimum performance."
    "Smiling, Caroline takes a drink."
    caroline "So, what about you?"
    pc "About me?"
    caroline "Yeah, I feel like we always end up talking about my life."
    caroline "I want to know more about you."
    pc "Honestly, I think you will probably find it boring."
    caroline "Maybe, but I still want to know."
    "Making small talk for a while, you go through your life."
    ###New character walks up to the bar (Rosie from Trista’s new story)##
    "Despite how boring it must be, she listens intently to it all."
    ### Rosie orders 11 glasses of beer and sits at the bar###
    "You are just explaining how you got your house, when you notice someone at the bar."
    "The place in front of her is filled with tall glasses.”"
    "Picking up the first, she downs it in just a few seconds before picking up the next."
    pc "I uhh, yeah so it's my dads place really."
    "Picking up the second, she downs it just as quickly."
    "A third and fourth follow fast as she chugs down the drinks."
    "Her stomach swelling rapidly from the influx of beer."
    "Despite its size, she doesn't seem to be stopping as another two cause her to bloat out even more."
    "Finally, after only a couple of minutes all the glasses are empty, her giant gut overflowing her clothes."
    "Her belly filled to the brim and then some with beer, the bubbly gas clearly causing her discomfort."
    caroline "Wow, seems like someone likes beer more than me."
    "Crap, how long have you been staring at the stranger."
    pc "Yeah, sorry it was just a bit distracting."
    caroline "I can see why, she barely even fits in those clothes any more."
    "Watching the woman shake hands with the barmaid, she leaves as quickly as she arrived."
    caroline "That was a bit odd, wasn't it?"
    pc "Definitely unusual."
    caroline "Anyway, sorry to cut our chat short but I actually do need to head back home for something."
    caroline "Haven't quite escaped the clutches of super organiser parents just yet."
    pc "No worries, I enjoyed our chat."
    caroline "Me too, it's always nice getting away from things with you."
    caroline "Although maybe next time we can try somewhere else?"
    pc "Sure thing, see you later Caroline."
    "Saying goodbye to Caroline, you head home."
    $ carolinestage3event6 = 0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Caroline_Stage_4_Event:
    ###While working at bunny bites###
    ##Caroline walks in##
    "A new customer arrives."
    "Hey it's Caroline"
    caroline "Hey!"
    pc "Hi Caroline, what can I get you today."
    caroline "I'm glad you are working today."
    caroline "I was going to phone you, but since you are here."
    caroline "Do you think you could maybe join me, or I could wait a bit until you have a break?"
    pc "It's pretty quiet at the moment, I am sure I can take my break now."
    caroline "Great!"
    ###Caroline turning away###
    pc "Caroline?"
    caroline "Oh right, my food."
    caroline "Can I get two burgers, fries and a soda please."
    pc "Sure thing, I'll come over when it's done."
    "Putting the order through, it isn't long until it is ready."
    "Grabbing it, you go over to join Caroline at a table."
    pc "Here is your food."
    caroline "Great, thanks."
    pc "So, how is everything?"
    pc "I hope nothing has happened?"
    caroline "Something has happened, but it is a good thing."
    caroline "I'm moving out!"
    pc "Amazing, do you have a place you are looking at getting?"
    caroline "Not yet, but I've made the decision to start looking."
    caroline "I have plenty of savings from my competition winnings, although places around here are pretty pricey."
    caroline "Although that isn't all the news."
    caroline "I'm quitting ballet."
    pc "Really?"
    caroline "Yeah."
    caroline "Oh, it feels so good just to say out loud."
    pc "These are some pretty big decisions."
    caroline "Yeah, but they have been kind of easy for me to make, which makes me think its the right thing to do."
    pc "Can I ask why?"
    caroline "Because I don't want to look back on my life in 20 years time and regret giving up everything else for one thing."
    caroline "Especially since it doesn't bring me joy like it used to."
    caroline "It's kind of like the mask has been lifted off my eyes and I am seeing clearly for the first time."
    pc "It sounds like this is really what you want."
    caroline "Exactly, what I want!"
    caroline "For the first time, maybe in my whole life it is just what I want."
    caroline "No parents, no coaches, fake friends or expectations."
    caroline "I get to make the choices and take control of my own life."
    pc "I'm happy for you."
    caroline "Thanks, it means a lot and I am glad to have a friend to talk to about this stuff."
    pc "So…not to bring down the mood but have you told your parents?"
    caroline "I have."
    pc "How did that go?"
    caroline "About as badly as you might expect."
    caroline "Shock, denial, trying to bribe me to keep going."
    caroline "I think they were more worried about what it might do to their image than mine."
    caroline "Although my dad had this weird heart to heart with me about being independent the other day."
    pc "I guess, as much of a change as it is for you, it's probably the same for them."
    caroline "Yeah and at least he's trying."
    caroline "Makes me hopeful that we can have some kind of normal relationship after all of this has worked out."
    pc "They are your parents, no matter what you choose they will still be there for you."
    caroline "Man, when did you get so sappy?"
    pc "Sorry."
    caroline "No, it's nice to hear and I think you are right."
    caroline "Anyway, I better get back and also let you get back to work."
    caroline "Thanks for the company."
    "Saying goodbye to Caroline, you go back to work."
    $ carolinestage4event = 0
    return

label Caroline_Stage_4_Event_2:
    ###After lesson###
    "After Daisy dismisses the class to work on their projects, you decide to work with Caroline today."
    ###In project room###
    "Approaching your usual room, you can see someone already in there."
    "It seems like Caroline's friend Lucy is waiting in there with a friend."
    caroline "Hey, what's up?"
    pc "Seems like Lucy beat us to it."
    caroline "Oh…why don't we work somewhere else instead?"
    pc "Sure, we can always check out the library."
    "Going to the library, you set up at one of the tables."
    caroline "Right then, where were we?"
    pc "Looks like there are a lot of salty snacks this week."
    pc "I guess we can track that, with the baseline of most of the other nutrients being the same."
    caroline "Sounds good to me."
    "Grabbing the first snack, Caroline starts to eat."
    caroline "I hope they don't mind us eating in here."
    pc "It is technically for a class project."
    caroline "True, can't kick us out for doing our work."
    "Finishing off the first snack, she hands you the packet to write down the nutritional information and grabs another."
    pc "I hope you don't mind me asking, is everything ok between you and Lucy?"
    pc "It kind of seemed like you didn't want to talk to her earlier."
    caroline "Yeah, sorry about that."
    caroline "My friends, or those pretending to be my friends are not too happy about me quitting."
    caroline "I think some of them believed I was going to be their golden ticket to success by just hanging around me."
    caroline "Now they kind of resent me for giving up on that."
    pc "You can't blame yourself for that."
    caroline "I know, and I kind of don't."
    caroline "Probably makes it worse for them, but it is probably a good thing."
    caroline "Now I can get on with my own life for a change."
    pc "Must be pretty weird though."
    caroline "Yeah, but honestly I kind of had a trial run when I was injured."
    caroline "They disappeared then and I didn't miss them."
    caroline "In a way I kind of wish they would disappear again now."
    caroline "Is that a horrible thing to say?"
    pc "No, I think it is fair."
    pc "Who knows, maybe some of them felt trapped too and this could help them discover who they want to be now."
    caroline "Honestly, I hadn't thought about it like that."
    caroline "I doubt it, but you never know."
    "Picking up the last snack, Caroline hands you the wrapper a few moments later."
    caroline "Looks like we're done."
    pc "Great, I'll make sure to update the spreadsheets."
    caroline "Great."
    pc "Since we are done a little bit early, fancy heading to bunny bites or something?"
    caroline "I'd love too, but sadly I have a meeting with the dean in like 15 minutes."
    pc "The dean, is everything ok?"
    caroline "Oh yeah, nothing to worry about."
    caroline "I guess I'll see you later."
    pc "Yeah sure."
    $ carolinestage4event2 = 0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        jump freetime
    return
