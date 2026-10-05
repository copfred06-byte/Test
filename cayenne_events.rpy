#Cayenne Events
label Cayenne_Stage_1_Event_1:
    #Scene: Cayenne’s First Bunny Bites Visit
    #(NOTE: The following should occur during one of the player’s shifts at Bunny Bites)
    image cafe_cayenne_arrive_event1 = "/cayenne/1/cafe_arrive.webp"
    scene cafe_cayenne_arrive_event1
    if rngworkgirl == 1:
        play music "/music/bb_amber.ogg" if_changed
    else:
        play music "/music/bunny_bites.ogg" if_changed
    "A customer arrives."
    $ unknownname = 'Mysterious Woman'
    image cafe_cayenne_talk_event1 = "/cayenne/1/cafe_talk.webp"
    scene cafe_cayenne_talk_event1
    "A woman with long brown hair and a simple, green dress approaches."
    "Reaching into her purse, she very meticulously pulls out a collection of bills and coins to place on the counter in front of you."
    unknown "Can I please have a small soda and a slice of pizza?"
    "Taking a moment to count her money, you come upon a grim realization of what you have to do."
    pc "I'm sorry, miss, but this isn't enough."
    image cayenne_stage1_1 = "/cayenne/events/stage1/1.webp"
    scene cayenne_stage1_1
    unknown "Oh…I’m sorry."
    pc "Hold on, let me see if I can find you something smaller on the kid’s menu or-"
    image cayenne_stage1_2 = "/cayenne/events/stage1/2.webp"
    scene cayenne_stage1_2
    "Before you can continue, Amber taps you on the shoulder to get your attention."
    amber "It’s alright. Go ahead and give her the employee discount."
    pc "Are you sure?"
    amber "Positive. She’s a regular around here. Don’t worry about the price difference."
    image cafe_cayenne_talk_event1 = "/cayenne/1/cafe_talk.webp"
    scene cafe_cayenne_talk_event1
    "Nodding in agreement with Amber, you turn back to address the woman."
    pc "I beg your pardon, but I think we can work with what you have. You said you wanted a small soda and slice of pizza?"
    unknown "Yes, please. Thank you very much."
    pc "I’ll go ahead and get started then. Have a seat and I’ll bring the food out to you."
    image cayenne_stage1_3 = "/cayenne/events/stage1/3.webp"
    scene cayenne_stage1_3
    "Putting the small meal together fairly quickly, you carry it over to her table."
    pc "Here you are, miss. Enjoy."
    unknown "Thank you very much."
    image cayenne_stage1_4 = "/cayenne/events/stage1/4.webp"
    scene cayenne_stage1_4
    "As she begins to dig into her food, you turn to leave. Catching a glimpse of Amber and recalling what she said, curiosity convinces you to linger for a bit."
    pc "Would you mind if I join you?"
    image cayenne_stage1_5 = "/cayenne/events/stage1/5.webp"
    scene cayenne_stage1_5
    "The woman pauses eating for a moment. Expecting at any moment to be viciously denied, she instead shrugs her shoulders."
    unknown "I guess that’s alright."
    image cayenne_stage1_6 = "/cayenne/events/stage1/6.webp"
    scene cayenne_stage1_6
    play music "/music/date_cozy.ogg" if_changed
    "Taking a seat across from her, you decide to ask one of the more obvious questions."
    pc "So how do you know Amber? Are you one of the employees here? I’m fairly new."
    image cayenne_stage1_7 = "/cayenne/events/stage1/7.webp"
    scene cayenne_stage1_7
    "The woman stops drinking as she thinks of how to respond."
    unknown "Amber is just being nice. We’re friends from a while back and she’s aware of the financial difficulties I’m going through."
    pc "I’m sorry. I didn’t mean to put you in such an awkward position."
    image cayenne_stage1_8 = "/cayenne/events/stage1/8.webp"
    scene cayenne_stage1_8
    "The woman puts on a smile to try to ease your nerves."
    unknown "It’s okay. You’re just doing your job after all. Besides, you seem pretty nice, and you make a decent meal."
    "Letting her finish the rest of her drink in peace, you thank her for her business before bussing the table."
    image cayenne_stage1_9 = "/cayenne/events/stage1/9.webp"
    scene cayenne_stage1_9
    unknown "Thank you very much for the food, Amber."
    amber "Anytime."
    unknown "And thank YOU for keeping me company."
    pc "You’re welcome. Come back soon!"
    "The woman leaves the diner, giving you a chance to get back to work."
    if recollection == True:
        stop music fadeout 1.0
    else:
        stop music fadeout 1.0
        if rngworkgirl == 1:
            play music "/music/bb_amber.ogg" if_changed
        else:
            play music "/music/bunny_bites.ogg" if_changed
    $ unknownname = 'Unknown'
    $ cayennestage1event = 0
    return

label Cayenne_Stage_1_Event_2:
    #Scene: Cayenne Bunny Bites Visit Hobbies
    #(NOTE: The following should occur when the player is working after Cayenne’s first visit to Bunny Bites)
    image cafe_cayenne_arrive_event1 = "/cayenne/1/cafe_arrive.webp"
    scene cafe_cayenne_arrive_event1
    if rngworkgirl == 1:
        play music "/music/bb_amber.ogg" if_changed
    else:
        play music "/music/bunny_bites.ogg" if_changed
    "A customer arrives."
    $ unknownname = 'Mysterious Woman'
    image cafe_cayenne_talk_event1 = "/cayenne/1/cafe_talk.webp"
    scene cafe_cayenne_talk_event1
    unknown "Hello again, er, [playername] was it?"
    pc "Yup, that’s me. What can I get for you?"
    "Just like before, the woman reaches into her pockets to dig out the exact change for her meal."
    unknown "Same thing as last time, please."
    pc "Can do. Have a seat and I’ll be right with you."
    image cayenne_stage1_3 = "/cayenne/events/stage1/3.webp"
    scene cayenne_stage1_3
    "Making her meal, you arrive at her table to drop it off."
    pc "Here you are, enjoy."
    unknown "Aren’t you going to join me like last time?"
    pc "I wasn’t planning on it, but if you want me to I have some time to kill."
    image cayenne_stage1_10 = "/cayenne/events/stage1/10.webp"
    scene cayenne_stage1_10
    play music "/music/date_cozy.ogg" if_changed
    "Taking the seat across from her, you watch her savor every last bite of her meal."
    "Trying to fill the air with something other than her chewing noises, you decide to try to start a conversation."
    pc "If you don’t mind me asking, what do you do for a living?"
    image cayenne_stage1_11 = "/cayenne/events/stage1/11.webp"
    scene cayenne_stage1_11
    "The woman stops eating to shoot you an annoyed look."
    unknown "I’d rather not talk about it."
    pc "Sorry. Okay then, what do you like to do for fun?"
    image cayenne_stage1_12 = "/cayenne/events/stage1/12.webp"
    scene cayenne_stage1_12
    "The question seems to perk her up a bit."
    unknown "Well, I do enjoy exercising."
    pc "Really? Anything specific?"
    unknown "Mostly the standard stuff, but my favorite method is when I get to do it by dancing."
    pc "That sounds fun."
    unknown "Yeah, I’ve been practicing ever since I was a little girl. It and one other hobby took up the majority of my free time before I had to worry about money issues."
    pc "What’s the other hobby?"
    image cayenne_stage1_13 = "/cayenne/events/stage1/13.webp"
    scene cayenne_stage1_13
    unknown "It’s a little embarrassing, but I’m a bit obsessed with history. Especially stuff from ancient Egypt."
    pc "I don’t know why you think that’s anything to be ashamed of."
    image cayenne_stage1_14 = "/cayenne/events/stage1/14.webp"
    scene cayenne_stage1_14
    unknown "It is when all you can think about is how the culture came up with such strange and unusual customs."
    unknown "Not to mention the pantheon of their deities. Everything from the well-known Ra, to the less popular gods like Min and Heset."
    "The small explanation turns into a full on lecture about the history and mythology of Egypt."
    "By the way she continues on, you can see just how knowledgeable she is on the topic."
    image cayenne_stage1_10 = "/cayenne/events/stage1/10.webp"
    scene cayenne_stage1_10
    "Eventually her body forces her to finish her meal to regain her energy before it’s time for her to go."
    image cayenne_stage1_9 = "/cayenne/events/stage1/9.webp"
    scene cayenne_stage1_9
    unknown "Thank you for the meal and for listening to me gush about my hobbies."
    pc "Anytime."
    if recollection == True:
        stop music fadeout 1.0
    else:
        stop music fadeout 1.0
        if rngworkgirl == 1:
            play music "/music/bb_amber.ogg" if_changed
        else:
            play music "/music/bunny_bites.ogg" if_changed
    $ unknownname = 'Unknown'
    $ cayennestage1event2 = 0
    return

label Cayenne_Stage_1_Event_3:
    #Scene: Cayenne Bunny Bites 3rd Visit Weight Gain Aversion
    image cafe_cayenne_arrive_event1 = "/cayenne/1/cafe_arrive.webp"
    scene cafe_cayenne_arrive_event1
    if rngworkgirl == 1:
        play music "/music/bb_amber.ogg" if_changed
    else:
        play music "/music/bunny_bites.ogg" if_changed
    "A customer arrives."
    $ unknownname = 'Mysterious Woman'
    image cafe_cayenne_talk_event1 = "/cayenne/1/cafe_talk.webp"
    scene cafe_cayenne_talk_event1
    unknown "Hello again, [playername]."
    pc "Good to see you. Can I fix you up with the usual?"
    image cayenne_stage1_18 = "/cayenne/events/stage1/18.webp"
    scene cayenne_stage1_18
    unknown "Actually, I was hoping for something a little lighter today. Can I get a water and a small sub?"
    pc "It’s a little more expensive than the other meal. Is that alright?"
    unknown "That should be fine."
    pc "Okay. Have a seat and I’ll be right with you."
    image cayenne_stage1_15 = "/cayenne/events/stage1/15.webp"
    scene cayenne_stage1_15
    "Making her meal, you place it on the table and sit across from her."
    pc "So what’s on your mind today?"
    image cayenne_stage1_16 = "/cayenne/events/stage1/16.webp"
    scene cayenne_stage1_16
    play music "/music/date_cozy.ogg" if_changed
    "She pauses for a moment as she picks up her meal, clearly in no rush to dig in."
    unknown "I’m a little concerned about my weight."
    pc "Why? I think you look great."
    image cayenne_stage1_17 = "/cayenne/events/stage1/17.webp"
    scene cayenne_stage1_17
    unknown "Thank you, but it’s more of what I fear will happen if I keep eating cheap, greasy food. I passed by this woman earlier today that was three times my size."
    unknown "Don’t get me wrong, I have nothing against larger people. However, I don’t think I could ever stand having to carry around so much extra heft everywhere I went."
    unknown "It’s one of the main reasons I exercise so often."
    pc "Just make sure you don’t push yourself too hard. Your body still needs rest and food to properly function."
    unknown "I’ll keep that in mind. Thank you for your concern."
    image cayenne_stage1_9 = "/cayenne/events/stage1/9.webp"
    scene cayenne_stage1_9
    "Finishing up her meal, the woman thanks you and the other servers for the food before heading out."
    if recollection == True:
        stop music fadeout 1.0
    else:
        stop music fadeout 1.0
        if rngworkgirl == 1:
            play music "/music/bb_amber.ogg" if_changed
        else:
            play music "/music/bunny_bites.ogg" if_changed
    $ unknownname = 'Unknown'
    $ cayennestage1event3 = 0
    return

label Cayenne_Stage_1_Event_4:
    #Scene: Cayenne 4th Bunny Bites Visit Heritage Test
    image cafe_cayenne_arrive_event1 = "/cayenne/1/cafe_arrive.webp"
    scene cafe_cayenne_arrive_event1
    if rngworkgirl == 1:
        play music "/music/bb_amber.ogg" if_changed
    else:
        play music "/music/bunny_bites.ogg" if_changed
    "A customer arrives."
    $ unknownname = 'Mysterious Woman'
    image cafe_cayenne_talk_event1 = "/cayenne/1/cafe_talk.webp"
    scene cafe_cayenne_talk_event1
    pc "Good to see you again. What can I get you?"
    "She smiles as she pulls out her usual collection of coins and bills to place them on the counter."
    unknown "I think today I’ll have a slice of pizza and a soda."
    pc "What about your health concerns?"
    image cayenne_stage1_18 = "/cayenne/events/stage1/18.webp"
    scene cayenne_stage1_18
    unknown "I have to cut back on my spending a bit longer. I’m close to reaching my goal."
    pc "Alright. Have a seat and I’ll be right with you."
    image cayenne_stage1_3 = "/cayenne/events/stage1/3.webp"
    scene cayenne_stage1_3
    "After making the food, you once more join her at her table."
    pc "Here you are."
    unknown "Thank you very much."
    image cayenne_stage1_12 = "/cayenne/events/stage1/12.webp"
    scene cayenne_stage1_12
    play music "/music/date_cozy.ogg" if_changed
    pc "If you don’t mind me asking, what exactly were you talking about when you mentioned reaching your goal?"
    unknown "Well, you know how I said I was kind of a history nerd? That’s not just for the ancient past."
    unknown "For the longest time I’ve wondered about my own ancestry. So much of it my parents have left in the dark. I’ve finally figured out a way to learn more about my family."
    pc "Is that what you’ve been saving money for?"
    image cayenne_stage1_14 = "/cayenne/events/stage1/14.webp"
    scene cayenne_stage1_14
    unknown "Correct. I’m going to use the extra cash to do a heritage check."
    pc "What are you hoping to find?"
    unknown "Nothing major really. Probably just that I’m the descendant of some farmers or that I have a long lost relative living in Germany or something."
    unknown "Regardless of my results, it should sate my curiosity."
    image cayenne_stage1_9 = "/cayenne/events/stage1/9.webp"
    scene cayenne_stage1_9
    "Moving on to sating her hunger for food rather than knowledge, the woman thanks you for the meal and leaves."
    if recollection == True:
        stop music fadeout 1.0
    else:
        stop music fadeout 1.0
        if rngworkgirl == 1:
            play music "/music/bb_amber.ogg" if_changed
        else:
            play music "/music/bunny_bites.ogg" if_changed
    $ unknownname = 'Unknown'
    $ cayennestage1event4 = 0
    return

label Cayenne_Stage_1_Event_5:
    #Scene: Cayenne’s 5th Bunny Bites Visit Inheritance Reveal
    #(NOTE: The following should occur as a random event when the player works at Bunny Bites, but it should be activated at least a week after Cayenne’s 4th visit.)
    image cayenne_stage1_19 = "/cayenne/events/stage1/19.webp"
    scene cayenne_stage1_19
    if rngworkgirl == 1:
        play music "/music/bb_amber.ogg" if_changed
    else:
        play music "/music/bunny_bites.ogg" if_changed
    "A familiar customer arrives, demanding your attention with her more extravagant appearance."
    $ unknownname = 'Mysterious Woman'
    image cayenne_stage1_20 = "/cayenne/events/stage1/20.webp"
    scene cayenne_stage1_20
    unknown "Hello again, [playername]. Today, I’ll take one large soda and a full sized pizza."
    pc "That’s quite the change. What’s going on?"
    unknown "I’ll tell you once I get my food. See you at the usual spot."
    image cayenne_stage1_21 = "/cayenne/events/stage1/21.webp"
    scene cayenne_stage1_21
    "Quickly putting the meal together, you hurry to place the food on the woman's table and sit across from her."
    image cayenne_stage1_22 = "/cayenne/events/stage1/22.webp"
    scene cayenne_stage1_22
    play music "/music/date_cozy.ogg" if_changed
    "Before you can ask her anything, the woman helps herself to a slice of pizza. Judging by the way she’s eating, it appears as if she was on the brink of starvation."
    "You finally get your chance to speak once she pauses after eating half of the pizza."
    image cayenne_stage1_23 = "/cayenne/events/stage1/23.webp"
    scene cayenne_stage1_23
    pc "Are you feeling alright?"
    unknown "Better than ever. You remember that heritage test I told you about?"
    unknown "Well, I got the results back along with a call from an agency representing one of my deceased ancestors."
    pc "I’m so sorry."
    image cayenne_stage1_24 = "/cayenne/events/stage1/24.webp"
    scene cayenne_stage1_24
    unknown "You don’t have to be. I’ve never met them and it’s because of them that I’m getting a big, fat inheritance."
    unknown "I won’t say the exact number, but just know that it’s enough for me to not have to work another day in my life. Things are finally looking up for me."
    pc "I’m so glad to hear. It’s like you’ve won the lottery."
    unknown "Yeah, and all I have to do is-"
    image cayenne_stage1_25 = "/cayenne/events/stage1/25.webp"
    scene cayenne_stage1_25
    "The woman pauses for a moment in thought."
    pc "Is everything alright?"
    image cayenne_stage1_26 = "/cayenne/events/stage1/26.webp"
    scene cayenne_stage1_26
    unknown "Um, yeah. Just, er, thinking about some legal stuff that’s part of the inheritance. Anyway, would you mind helping me box up the rest of this to go?"
    image cayenne_stage1_27 = "/cayenne/events/stage1/27.webp"
    scene cayenne_stage1_27
    "After helping the woman with her to go order, she starts to take her leave. Upon placing a nice tip in your hands, she waves goodbye and heads out the door."
    if recollection == False:
        $ money += 20
        "You earned twenty dollars."
    $ unknownname = 'Unknown'
    if recollection == False:
        $ cayenne.weight = 53
        $ cayenne.stage = 2
        stop music fadeout 1.0
        if rngworkgirl == 1:
            play music "/music/bb_amber.ogg" if_changed
        else:
            play music "/music/bunny_bites.ogg" if_changed
    else:
        stop music fadeout 1.0
    $ cayennestage1event5 = 0
    return

label Cayenne_Stage_2_Event:
    #Scene: Cayenne’s First Tutoring Session
    #(NOTE: The following should occur after Cayenne’s initial round of Bunny Bites visits and the player has gone through the event where Daisy tells them to start tutoring. The following should occur in the player’s room after Daisy’s request)
    #CHOICE: Go to tutor session.
    "Deciding to take up the tutoring request, you message Daisy."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Daisy', dialogue=dialogue_one)
    $ msg ("I’m ready to take on that tutoring job you mentioned.")
    pause
    $ msg ("Perfect timing. She’s ready as well. Head to the address.", who=1)
    pause
    $ msg ("I’ll let her know you’re coming and send along some study materials.", who=1)
    pause
    $ hide_messenger()

    "Curious as to what Daisy is talking about, you head out towards the address."
    image cayenne_stage2_1 = "/cayenne/events/stage2/1.webp"
    scene cayenne_stage2_1
    "Arriving at the address, you remember this being a really expensive part of town. Located in the city center, you have to assume that the apartments cost a fortune."
    "You begin to wonder about the kind of person you’re about to meet. You shudder as you think of running into a spoiled rich kid that will make your life a living hell."
    "Bracing yourself for the worst, you walk up and knock on the door."
    image cayenne_stage2_2 = "/cayenne/events/stage2/2.webp"
    scene cayenne_stage2_2
    play music "/music/cayenne.ogg" if_changed
    "As the door opens, you’re surprised to see a familiar face."
    unknown "What are you doing here?"
    pc "I’m…here for a tutoring session?"
    image cayenne_stage2_3 = "/cayenne/events/stage2/3.webp"
    scene cayenne_stage2_3
    unknown "Wait, so you work at Bunny Bites and for the university?"
    pc "Not exactly. Daisy, I mean, Ms. Tanwen asked me to help you out with your at home education. She told me you were struggling with your nutritional studies."
    unknown "I guess that’s fine. Although you’re still the last person I would expect. At least being familiar with each other should make things easier."
    pc "That’s only kind of true. I still don’t know your name."
    image cayenne_stage2_4 = "/cayenne/events/stage2/4.webp"
    scene cayenne_stage2_4
    unknown "Oh, guess I never made a proper introduction. My name is Cayenne. Come on in and we can get started."
    "Considering how much Cayenne spoke about her money issues, you’re surprised to see that the apartment is fairly sizable with plenty of newly bought furniture and appliances."
    image cayenne_stage2_5 = "/cayenne/events/stage2/5.webp"
    scene cayenne_stage2_5
    "Giving a second glance at her showy outfit, you wonder how she could afford all of this until you recall your last meeting at the diner."
    pc "This was all bought with your inheritance?"
    cayenne "That’s right. I get a deposit into my account every week to spend however I please. The only catch is that I need to keep up my grades in Ms. Tanwen’s class."
    pc "Why?"
    image cayenne_stage2_6 = "/cayenne/events/stage2/6.webp"
    scene cayenne_stage2_6
    "Cayenne shrugs."
    cayenne "Something to do with nutrition being a big part of my family’s history I think."
    cayenne "In any case, it feels like I’m trying to learn another language with how difficult the material is to digest. Hopefully things should be a lot easier now that I have some help."
    pc "That’s the spirit. So, where would you like to start?"
    cayenne "Probably with the packet of study supplies they gave me. It was delivered right after Ms. Tanwen called me about today’s tutoring session. Follow me."
    image cayenne_stage2_7 = "/cayenne/events/stage2/7.webp"
    scene cayenne_stage2_7
    "Walking over to the kitchen, you spot the supplies in the form of a box on a nearby counter."
    pc "They sent you all this just for a study session? What’s inside?"
    cayenne "Not sure. This stuff got here shortly before you arrived, so I haven’t had a chance to look yet. Let me see."
    "Reaching into the box, she pulls out a packet of papers."
    image cayenne_stage2_8 = "/cayenne/events/stage2/8.webp"
    scene cayenne_stage2_8
    cayenne "Hmm, looks like the first thing I need to do is…write down my measurements? What kind of class is this?"
    pc "Ms. Tanwen has a very…unique way of teaching."
    cayenne "Whatever. I have to go through with it if I want to keep the money, so might as well get it done."
    image cayenne_stage2_9 = "/cayenne/events/stage2/9.webp"
    scene cayenne_stage2_9
    "Peeking over her shoulder, you manage to get a glimpse at her measurements as she writes them down."
    $ cayenne_stats_visible = 1
    "Cayenne has been added to the Stats Screen."
    image cayenne_stage2_10 = "/cayenne/events/stage2/10.webp"
    scene cayenne_stage2_10
    cayenne "Now that’s out the way, the next thing they want me to do is open up this box."
    image cayenne_stage2_11 = "/cayenne/events/stage2/11.webp"
    scene cayenne_stage2_11
    "Picking out a tightly wrapped box from the stack of supplies, Cayenne opens it up to reveal a collection of chocolates."
    cayenne "Okay, I changed my mind. Your teacher is the best."
    pc "Did she mention what you’re supposed to do with them?"
    cayenne "I’m assuming I have to eat them but let me double check."
    image cayenne_stage2_12 = "/cayenne/events/stage2/12.webp"
    scene cayenne_stage2_12
    "Picking up her work sheet again, Cayenne scans the page for her assignment."
    cayenne "Looks like I have to try each one and rank them depending on how much I enjoy them. Alright, let me start with…"
    image cayenne_stage2_13 = "/cayenne/events/stage2/13.webp"
    scene cayenne_stage2_13
    "Picking up the first chocolate from the box, Cayenne places it in her mouth and begins to write."
    cayenne "Oh, this one is really creamy."
    image cayenne_stage2_14 = "/cayenne/events/stage2/14.webp"
    scene cayenne_stage2_14
    "Swallowing the piece, she picks up another one from the box to follow."
    cayenne "And this one has a very sweet strawberry taste in the middle. What else do they have?"
    image cayenne_stage2_15 = "/cayenne/events/stage2/15.webp"
    scene cayenne_stage2_15
    "At some point, Cayenne loses sight of the assignment as she shoves chocolate into her mouth with reckless abandon."
    image cayenne_stage2_16 = "/cayenne/events/stage2/16.webp"
    scene cayenne_stage2_16
    "While this hurts her ability to judge each individual morsel, the pleased hums that leaves her lips prove that she’s enjoying herself."
    image cayenne_stage2_17 = "/cayenne/events/stage2/17.webp"
    scene cayenne_stage2_17
    "It’s only after eating the last piece does Cayenne come to her senses."
    cayenne "Oops, guess I kind of got carried away. I’ll just write down that each of them was delicious."
    pc "Is that all they sent you?"
    image cayenne_stage2_18 = "/cayenne/events/stage2/18.webp"
    scene cayenne_stage2_18
    cayenne "Hold on, there’s one more thing. They said I should practice tasting different kinds of meals. They’ve included the number and location of different eateries in town."
    pc "Daisy, I mean, Ms. Tanwen probably expects you to eat something with each tutoring session."
    image cayenne_stage2_19 = "/cayenne/events/stage2/19.webp"
    scene cayenne_stage2_19
    cayenne "Why’s that?"
    pc "Food is a big part of the class. It makes sense that she would want you to have experience with a wide range of the different meals we talk about."
    image cayenne_stage2_20 = "/cayenne/events/stage2/20.webp"
    scene cayenne_stage2_20
    cayenne "I see your point. Guess next time we do this I’ll hold off on eating dinner. In any case, thanks for coming over to help me study."
    pc "Anytime."
    "Tossing out the empty box and saying goodbye to Cayenne, you head out the door."
    image cayenne_stage2_21 = "/cayenne/events/stage2/21.webp"
    scene cayenne_stage2_21
    stop music fadeout 1.0
    "Just as you’re about to start walking home, you receive a message from Daisy."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Daisy', dialogue=dialogue_one)
    $ msg ("So, how did the tutoring session go?", who=1)
    pause
    $ msg ("Alright I guess. She seems to be grasping the basics well enough. Don’t know why you need me to tutor her.")
    pause
    $ msg ("I assure you that she needs the extra help. You’ll understand with time.", who=1)
    pause
    $ msg ("For now, just keep making regular visits to her house. Wouldn’t want your student slipping in her grades.", who=1)
    pause
    $ hide_messenger()
    "Feeling a bit wary of whatever Daisy has planned for Cayenne, you go home for the evening."
    $ cayennestage2event = 0
    if recollection == False:
        $ cayenne.stage = 3
        $ cayenne.weight = 56
        $ daytime += 1
        jump freetime
    return

label Cayenne_Stage_3_Event:
    #Scene: Cayenne Dance Introduction
    #(NOTE: The following should occur when the player goes to Cayenne’s house after she reaches Stage 3)
    image cayenne_stage3_1 = "/cayenne/events/stage3/1.webp"
    scene cayenne_stage3_1
    play music "/music/cayenne.ogg" if_changed
    "Calling up Cayenne for another tutoring session, you arrive at her house just as she’s putting out her study materials."
    pc "Hello, Cayenne."
    image cayenne_stage3_2 = "/cayenne/events/stage3/2.webp"
    scene cayenne_stage3_2
    cayenne "Hi there. Glad you could make it. I’m ready to start when you are."
    "Going over the usual study material, you eventually reach the food tasting section."
    "Opening up the box reveals a series of pastries covered in a strange, extra sweet smell."
    image cayenne_stage3_3 = "/cayenne/events/stage3/3.webp"
    scene cayenne_stage3_3
    cayenne "These all look pretty tasty. Let’s get started."
    image cayenne_stage3_4 = "/cayenne/events/stage3/4.webp"
    scene cayenne_stage3_4
    "Cayenne enthusiastically downs the first pastry without much trouble."
    image cayenne_stage3_5 = "/cayenne/events/stage3/5.webp"
    scene cayenne_stage3_5
    "The delicious flavor allows her to work through the bulk of the meal."
    image cayenne_stage3_6 = "/cayenne/events/stage3/6.webp"
    scene cayenne_stage3_6
    "However, she requires your motivation to keep her going to finish the rest."
    image cayenne_stage3_7 = "/cayenne/events/stage3/7.webp"
    scene cayenne_stage3_7
    "Through your combined efforts, she manages to eat the entire collection."
    pc "Are you feeling alright? That was a lot of food."
    image cayenne_stage3_8 = "/cayenne/events/stage3/8.webp"
    scene cayenne_stage3_8
    cayenne "Better than ever actually. I don’t know what was in those things, but I feel so energetic. Makes me want to just get up and do something fun."
    pc "Like what?"
    image cayenne_stage3_9 = "/cayenne/events/stage3/9.webp"
    scene cayenne_stage3_9
    "After thinking for a moment, a smile spreads on Cayenne’s face."
    cayenne "I have the perfect idea. Wait right here."
    image cayenne_stage3_10 = "/cayenne/events/stage3/10.webp"
    scene cayenne_stage3_10
    "Slipping into her room for a moment, she returns wearing an outfit that tightly hugs her body."
    image cayenne_stage3_11 = "/cayenne/events/stage3/11.webp"
    scene cayenne_stage3_11
    cayenne "What do you think? I just bought it last week."
    pc "It looks amazing."
    cayenne "Thank you. Although, I didn’t just buy it for its looks. Allow me to demonstrate."
    "With a press of a button on her phone, music begins to drift into the room."
    "Tapping your foot along to the beat, you watch as Cayenne shoots you a smile before she starts to move as well."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/cayenne/events/stage3/12.webm" loop
    show movie with dissolve
    "Becoming one with the beat of the song, Cayenne dances across the room."
    "You’re put into a trance-like state as you watch her body’s sultry movements."
    "Noticing the way you look at her, Cayenne keeps up her smile as she finishes up her routine."
    window hide
    pause
    stop movie
    image cayenne_stage3_13 = "/cayenne/events/stage3/13.webp"
    scene cayenne_stage3_13
    pc "That was amazing."
    cayenne "You seem surprised. I told you dancing was one of my hobbies."
    pc "Yeah, but you never told me you were this good."
    cayenne "As much as I’d like to take all the credit, I think there was something in the pastries that gave me an extra rush of energy."
    cayenne "Wonder if it was some special kind of sugar or something."
    image cayenne_stage3_14 = "/cayenne/events/stage3/14.webp"
    scene cayenne_stage3_14
    cayenne "Anyway, let’s call that a reward for you helping me out. See you next time."
    "Waving goodbye, you head back home."
    stop music fadeout 1.0
    scene player_room
    "You receive a message. It’s Cayenne."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Cayenne', dialogue=dialogue_one)
    $ msg ("Hope you enjoyed the show, because I know I did. 😉", who=1)
    pause
    $ msg ("Not every day I let someone spoil me like that… don’t get used to it. Or do. Your call. 😏", who=1)
    "You chuckle and start typing."
    $ msg ("I don’t think I’ll ever get tired of spoiling you.")
    "A moment later, another message pops up."
    $ msg ("Good answer. And since you were such a good audience…", who=1)
    pause
    $ msg (None, who=1, pic="stage3_cayenne")
    pause
    $ msg ("Damn, Cayenne…")
    pause
    $ msg ("Speechless? Thought so. 😘", who=1)
    pause
    $ hide_messenger()

    #(NOTE: After this scene the option for Cayenne to dance during regular tutoring sessions should become available)
    $ cayennestage3event = 0
    if recollection == False:
        $ cayenne.weight += 1
        $ daytime += 1
        jump freetime
    return

label Cayenne_Stage_4_Event:
    #Scene: Post-Stuffing Masturbation
    #(NOTE: The following should occur once Cayenne reaches stage 4 and the player goes to a tutoring session)
    image cayenne_stage4_1 = "/cayenne/events/stage4/1.webp"
    scene cayenne_stage4_1
    play music "/music/cayenne.ogg" if_changed
    "Making your way to Cayenne’s place for the usual tutoring session, she welcomes you inside and brings you to the kitchen."
    image cayenne_stage4_2 = "/cayenne/events/stage4/2.webp"
    scene cayenne_stage4_2
    "As you arrive, you can’t help noticing that the usual study materials are a lot bigger than usual."
    pc "Did Ms. Tanwen send you all this?"
    image cayenne_stage4_3 = "/cayenne/events/stage4/3.webp"
    scene cayenne_stage4_3
    cayenne "Yeah. She said I was doing so well that it’s time for me to move on to some extra credit."
    "Both of you more than a little curious about what Daisy is planning, Cayenne starts unloading the box on the table."
    image cayenne_stage4_4 = "/cayenne/events/stage4/4.webp"
    scene cayenne_stage4_4
    "Inside you find the same extra sweet smelling pastries as before, this time in a much larger number."
    cayenne "These things again?"
    pc "Is there something wrong?"
    image cayenne_stage4_5 = "/cayenne/events/stage4/5.webp"
    scene cayenne_stage4_5
    cayenne "Er, no. I’m just trying to figure out how I’m going to eat all of them in one sitting."
    pc "We’ve been practicing for stuff like this. I know you can do it."
    image cayenne_stage4_6 = "/cayenne/events/stage4/6.webp"
    scene cayenne_stage4_6
    "Though there’s a bit of hesitation, Cayenne eventually responds with a nervous smile."
    cayenne "You’re right. Let’s get started."
    image cayenne_stage4_7 = "/cayenne/events/stage4/7.webp"
    scene cayenne_stage4_7
    "Though she’s slow to start, Cayenne only needs to take one bite to throw off any concerns."
    image cayenne_stage4_8 = "/cayenne/events/stage4/8.webp"
    scene cayenne_stage4_8
    "Once more becoming enamored with the flavor, she begins to stuff the pastries into her mouth with reckless abandon."
    image cayenne_stage4_9 = "/cayenne/events/stage4/9.webp"
    scene cayenne_stage4_9
    "As you watch her try to eat through the entire spread, you see her start to slow down as she reaches the halfway point and her belly begins to bulge out."
    image cayenne_stage4_10 = "/cayenne/events/stage4/10.webp"
    scene cayenne_stage4_10
    cayenne "I don’t know how much more I can take. Could you give me a hand?"
    pc "You can count on me."
    image cayenne_stage4_11 = "/cayenne/events/stage4/11.webp"
    scene cayenne_stage4_11
    "Trying to work to the best of your abilities, you take over pushing each pastry past her lips."
    "Pausing to give her a chance to chew and savor the taste, you instinctively reach your fingers out and begin rubbing her belly."
    image cayenne_stage4_12 = "/cayenne/events/stage4/12.webp"
    scene cayenne_stage4_12
    "While she’s surprised at first, the relief she feels from your touch convinces her to let you continue."
    "Through your combined efforts, Cayenne manages to swallow down the very last lump of sugar and icing."
    image cayenne_stage4_13 = "/cayenne/events/stage4/13.webp"
    scene cayenne_stage4_13
    pc "We did it!"
    cayenne "Y-yeah, we sure did."
    pc "Is everything okay?"
    image cayenne_stage4_14 = "/cayenne/events/stage4/14.webp"
    scene cayenne_stage4_14
    cayenne "Yes, just, um, a little indigestion I think. Would you mind walking to the store around the corner? I’m out of antacids. I promise I’ll pay you back."
    pc "Alright I’ll be back as soon as I can."
    image cayenne_stage4_15 = "/cayenne/events/stage4/15.webp"
    scene cayenne_stage4_15
    "Determined to help to aid Cayenne’s unsettled stomach, you bolt out the door."
    "Just as you’re about to round the corner, you realize that you left your phone behind and have no idea the kind of brand she wants."
    image cayenne_stage4_16 = "/cayenne/events/stage4/16.webp"
    scene cayenne_stage4_16
    "Turning on your heels, you make your way back to her apartment. Finding the door unlocked, you step inside."
    "Before you have a chance to call out to Cayenne to find her, you spot her through a crack in the door leading to the kitchen area."
    if persistent.masturbation:
        scene black with dissolve
        "Cayenne had a good time."
    else:
        image cayenne_stage4_17 = "/cayenne/events/stage4/17.webp"
        scene cayenne_stage4_17
        "You freeze as still as a statue as you witness Cayenne rubbing her fingers against her womanhood."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage4/18.webm" loop
        show movie with dissolve
        window hide
        pause
        "While one of her hands focuses on masturbating, the other goes across her body to squeeze anything it can reach."
        "As her fingers grasp her stuffed belly, she lets out a hiss of pleasure that pushes her to up her speed."
        "Though you try to remain quiet, you end up pushing a little too hard against the door and tumble into the room."
        stop movie
    image cayenne_stage4_19 = "/cayenne/events/stage4/19.webp"
    scene cayenne_stage4_19
    cayenne "[playername]!"
    pc "I’m so sorry. I didn’t mean to spy on you like that. I’ll leave the room to let you finish and get dressed."
    image cayenne_stage4_20 = "/cayenne/events/stage4/20.webp"
    scene cayenne_stage4_20
    cayenne "No."
    pc "No?"
    cayenne "I…don’t want you to leave."
    pc "What are you talking about?"
    image cayenne_stage4_21 = "/cayenne/events/stage4/21.webp"
    scene cayenne_stage4_21
    "Though she struggles to find the words, she eventually speaks."
    image cayenne_stage4_22 = "/cayenne/events/stage4/22.webp"
    scene cayenne_stage4_22
    cayenne "I want you to stay and watch while I…take care of this."
    pc "Are you sure?"
    cayenne "…yes. Please have a seat."
    "Unsure of exactly what’s going on, you regardless do as she says and take a seat."
    if persistent.masturbation:
        scene black with dissolve
        "Cayenne had a good time."
    else:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage4/23.webm" loop
        show movie with dissolve
        window hide
        pause
        "In contrast to her earlier efforts, Cayenne’s self-stimulation eases back to a slow pace."
        "Though you can tell that she’s a little nervous about her audience of one, the pleasure helps her return to her former speed."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage4/24.webm" loop
        show movie with dissolve
        window hide
        pause
        "Unconcerned with what you think, she proceeds to let out a string of euphoric moans as she moves her fingers faster and faster."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage4/25.webm" loop
        show movie with dissolve
        window hide
        pause
        "Giving it her all to reach her climax, she gives her belly one last squeeze moments before she reaches her orgasm."
        stop movie
        image cayenne_stage4_26 = "/cayenne/events/stage4/26.webp"
        scene cayenne_stage4_26
        "As the last echoes of her moan dissipate from the house, all that’s left is a look of satisfaction in her eyes."
    image cayenne_stage4_27 = "/cayenne/events/stage4/27.webp"
    scene cayenne_stage4_27
    cayenne "That felt amazing. Thank you for playing along with me."
    pc "I guess I should be thanking you. What possessed you to do something like this?"
    image cayenne_stage4_28 = "/cayenne/events/stage4/28.webp"
    scene cayenne_stage4_28
    cayenne "I think it has something to do with the pastries and a extra sweet smelling ingredient in it. I felt it last time they were sent to me."
    cayenne "I didn’t know what to do with the extra energy, so I tried to burn it off with that dance."
    cayenne "Guess it took a larger dose for me to figure out how I was supposed to take care of it."
    pc "Sorry, I didn’t think Ms. Tanwen would go so far just for your lessons."
    image cayenne_stage4_29 = "/cayenne/events/stage4/29.webp"
    scene cayenne_stage4_29
    cayenne "It’s okay. The food was really good and I…enjoyed myself."
    pc "I’ll still try to see if she can avoid sending this kind of stuff unannounced in the future."
    image cayenne_stage4_30 = "/cayenne/events/stage4/30.webp"
    scene cayenne_stage4_30
    cayenne "I would appreciate it. That being said, would you be willing to be a ‘spectator’ every now and then after a stuffing session?"
    cayenne "I don’t know why, but something about it makes it feel even better."
    pc "I guess? It’s still a little weird, but I’ll do it."
    image cayenne_stage4_31 = "/cayenne/events/stage4/31.webp"
    scene cayenne_stage4_31
    cayenne "Thank you."
    "Leaving Cayenne to clean up herself and the kitchen, you leave her house."
    image cayenne_stage4_32 = "/cayenne/events/stage4/32.webp"
    scene cayenne_stage4_32
    stop music fadeout 1.0
    "Still curious about the “unique” choice in cuisine, you decide to message Daisy about it."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Daisy', dialogue=dialogue_one)
    $ msg ("Hey, what’s up with the pastries you sent Cayenne?")
    pause
    $ msg ("I’d ask which ones, but I think I know the particular sweets you’re talking about.", who=1)
    pause
    $ msg ("It’s not right to be sending that kind of stuff to her without notice.")
    pause
    $ msg ("That’s why I sent the smaller batch at first. I thought it would be enough to ease her into a larger portion.", who=1)
    pause
    $ msg ("That still doesn’t explain why you sent it in the first place.")
    pause
    $ msg ("It’s a secret :).", who=1)
    pause
    $ msg ("A secret?")
    pause
    $ msg ("Yes, a special one that is very important to her development. For now, you’ll just have to take my word for it. That girl has a very important purpose.", who=1)
    pause
    $ msg ("To test out new teaching techniques?")
    pause
    $ msg ("Not exactly. You’ll find out later, I promise.", who=1)
    pause
    $ hide_messenger()
    "Chalking it up to just Daisy being her strange self, you put away your phone and head home."

    scene player_room

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Cayenne', dialogue=dialogue_one)
    $ msg ("So… about earlier. You enjoyed the show, didn’t you? Don’t lie. 😉", who=1)
    "A second message follows almost immediately."
    $ msg ("Not sure what was in those sweets, but wow… let’s just say I had a long night. Hope you’re satisfied, leaving me like that. 😏", who=1)
    "You hesitate before replying."
    $ msg ("Didn’t expect things to turn out like that… but I won’t pretend I didn’t like what I saw.")
    "A new message pops up."
    $ msg ("Good. Then you’ll love this.", who=1)
    pause
    $ msg (None, who=1, pic="stage4_cayenne")
    pause
    $ msg ("Bet you wish you stayed a little longer. 😘", who=1)
    pause
    $ hide_messenger()

    #(NOTE: After this event, the option for the player to watch Cayenne masturbate after her regular stuffing sessions should become available.)
    if recollection == False:
        $ cayenne.weight += 1
        $ cayennestage4event = 0
        #Unlocks Cayenne Undress in the stats page.
        $ renpy.notify("Cayenne Undress option unlocked in stats screen.")
        window hide
        pause
        $ daytime += 1
        jump freetime
    return

label Cayenne_Stage_5_Event:
    #Scene: donut Stuffing and Sex Scene
    #(NOTE: The following should occur after Cayenne reaches stage 5 and the player chooses tutoring session)
    image cayenne_stage5_1 = "/cayenne/events/stage5/1.webp"
    scene cayenne_stage5_1
    play music "/music/cayenne.ogg" if_changed
    "Arriving at Cayenne’s house, she greets you as you come to the door."
    pc "Hey Cayenne. Ready for today’s tutoring session?"
    image cayenne_stage5_2 = "/cayenne/events/stage5/2.webp"
    scene cayenne_stage5_2
    cayenne "About that, things are a little…different this time."
    pc "What do you mean?"
    cayenne "It’s about the study materials. Come with me and I’ll show you."
    "Following Cayenne’s lead, you walk towards her couch to find…"
    image cayenne_stage5_3 = "/cayenne/events/stage5/3.webp"
    scene cayenne_stage5_3
    "You look on in disbelief at the spread of donuts laid out across her couch."
    "Recognizing it as the very same ones from the Sugar Shop, you don’t have to ask where it came from."
    pc "Does Ms. Tanwen expect you to eat all of this?"
    cayenne "That’s what the study packet said. Even with your help I’m not sure if I can even eat half of this."
    pc "You don’t have to do this if you don’t want to."
    image cayenne_stage5_4 = "/cayenne/events/stage5/4.webp"
    scene cayenne_stage5_4
    cayenne "Doesn’t seem like I have much of a choice considering this is paying for my house. Think you can help me out?"
    pc "I’ll do my best."
    image cayenne_stage5_5 = "/cayenne/events/stage5/5.webp"
    scene cayenne_stage5_5
    "Taking up the task of handing her donuts, you watch as she starts off by slowly nibbling at the pastries."
    "It’s through this that you get to see the moment her concern becomes overridden with delight as her tongue is overwhelmed by the sweet flavor."
    image cayenne_stage5_6 = "/cayenne/events/stage5/6.webp"
    scene cayenne_stage5_6
    "As she increases her speed, she accidentally knocks over an emptied box out onto the floor."
    image cayenne_stage5_7 = "/cayenne/events/stage5/7.webp"
    scene cayenne_stage5_7
    "Uncaring of the sticky glaze clinging to her hands, she continues to stuff herself."
    "Though at first you’re only able to help by keeping up with her appetite, at a certain point you realize she requires more direct assistance."
    image cayenne_stage5_8 = "/cayenne/events/stage5/8.webp"
    scene cayenne_stage5_8
    "Heeding the look of need in her eyes, you climb up onto the couch with Cayenne with the remaining donuts in hand."
    "While you massage her exposed, stuffed belly, you gently shove the remaining pastries into her mouth."
    image cayenne_stage5_9 = "/cayenne/events/stage5/9.webp"
    scene cayenne_stage5_9
    "Though it’s a bit of a struggle, the two of you manage to just barely finish off the last bite."
    image cayenne_stage5_10 = "/cayenne/events/stage5/10.webp"
    scene cayenne_stage5_10
    pc "You did great. Looks like all that hard work has been paying off."
    image cayenne_stage5_11 = "/cayenne/events/stage5/11.webp"
    scene cayenne_stage5_11
    "Cayenne is too preoccupied with breathing heavily as she massages her stomach. Gradually, her fingers drift towards her groin."
    "Body trembling from some unknown force, you watch as she rids herself of her clothing right in front of you."
    if persistent.masturbation:
        scene black with dissolve
        "Cayenne had a good time."
    else:
        image cayenne_stage5_12 = "/cayenne/events/stage5/12.webp"
        scene cayenne_stage5_12
        "While one hand continues to squeeze her belly, the other fully gives into her desires as she begins to furiously masturbate."
        image cayenne_stage5_13 = "/cayenne/events/stage5/13.webp"
        scene cayenne_stage5_13
        "You’ve seen this before, but never have you witnessed such a thirst for pleasure in her eyes."
        "As you continue to watch her display of depravity, you eventually lock eyes with her."
    image cayenne_stage5_14 = "/cayenne/events/stage5/14.webp"
    scene cayenne_stage5_14
    "As your gazes meet, she stops moving. Chewing on her lips, she eventually speaks to you."
    cayenne "I can’t quite reach. [playername], I want you to do it."
    pc "What do you mean?"
    image cayenne_stage5_15 = "/cayenne/events/stage5/15.webp"
    scene cayenne_stage5_15
    "Though there is a moment of hesitation, her need to satiate herself makes her speak."
    cayenne "I want you…inside me."
    "Seeing the look of conviction in her eyes, you heed her wish. Taking off your clothes, you join her on the couch."
    if persistent.nosexscene:
        scene black with dissolve
        "Cayenne and you had a good time."
    else:
        image cayenne_stage5_16 = "/cayenne/events/stage5/16.webp"
        scene cayenne_stage5_16
        "You grab Cayenne by her legs and lift her up to where you are able to enter her while standing."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage5/17.webm" loop
        show movie with dissolve
        window hide
        pause
        "Though it’s a little hard to see where you’re going with her food baby in the way, you manage to slide your member inside of her."
        "Holding onto her legs for support, you proceed to thrust back and forth. Each push is met with a moan from either Cayenne or yourself."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage5/18.webm" loop
        show movie with dissolve
        window hide
        pause
        "Getting used to the sensation of her belly pushing down on your member, you begin to increase your speed."
        "Keeping yourself going just long enough for Cayenne to find her release, you inevitably fill her womanhood with your cum."
        stop movie
        $ renpy.movie_cutscene("/images/cayenne/events/stage5/19.webm")
        image cayenne_stage5_20 = "/cayenne/events/stage5/20.webp"
        scene cayenne_stage5_20
        "Pulling out of Cayenne, you join her on the couch to work through your lingering ecstasy."
        "Though you’re still enjoying the lingering bliss, you can’t help noticing the donut glaze that worked its way onto your body during your moment of passion."
        "Looking over her body, you see similar sticky spots spread across her flesh."
        pc "Do you want to clean up? I think you got a little messy."
    image cayenne_stage5_21 = "/cayenne/events/stage5/21.webp"
    scene cayenne_stage5_21
    cayenne "You’re probably right. But I’m a little worn out after that. Mind helping me into the shower?"
    pc "Sure thing."
    image cayenne_stage5_22 = "/cayenne/events/stage5/22.webp"
    scene cayenne_stage5_22
    "Holding onto each other’s bodies, you and Cayenne manage to make your way into the shower."
    "Turning on the water, the two of you work to rid yourself of any lingering stickiness."
    image cayenne_stage5_23 = "/cayenne/events/stage5/23.webp"
    scene cayenne_stage5_23
    cayenne "So…how was it?"
    pc "What do you mean?"
    cayenne "I’m talking about being with someone after she made a complete pig of herself."
    pc "To be honest, it was pretty hot."
    image cayenne_stage5_24 = "/cayenne/events/stage5/24.webp"
    scene cayenne_stage5_24
    cayenne "Really? Guess it takes all types. I’m assuming you wouldn’t be against doing this again in the future?"
    pc "Not at all. Especially if it helps you with your studies."
    cayenne "A weird way to put it, but I appreciate it."
    image cayenne_stage5_25 = "/cayenne/events/stage5/25.webp"
    scene cayenne_stage5_25
    "After you and Cayenne clean yourselves up, you get dressed and head for home."
    stop music fadeout 1.0
    #(NOTE: From this point forward, the player should be able to have sex with Cayenne during the regular tutoring sessions after she stuffs herself.)
    $ cayennestage5event = 0
    if recollection == False:
        $ cayenne.weight += 1
        $ daytime += 1
        jump freetime
    return

label Cayenne_Stage_6_Event:
    #Scene: Weight Gain Realization
    #(NOTE: The following should occur when the player goes to tutor Cayenne after she reaches stage 6)
    image cayenne_stage6_1 = "/cayenne/events/stage6/1.webp"
    scene cayenne_stage6_1
    "Arriving at Cayenne’s house, you knock on the door."
    cayenne "Who is it?"
    pc "[playername]. I’m here for another tutoring session."
    cayenne "Hold on."
    "Though you hear Cayenne walk up to the door and unlock it, she proceeds to retreat back into the house."
    "You’re left in a state of confusion before she calls out to you."
    cayenne "Come in! The door is unlocked. You’ll find me upstairs."
    image cayenne_stage6_2 = "/cayenne/events/stage6/2.webp"
    scene cayenne_stage6_2
    play music "/music/cayenne.ogg" if_changed
    "Curious as to what she’s doing, you regardless open the door and head inside."
    "Still unsure what exactly she’s doing, you head up to find Cayenne in her bedroom."
    image cayenne_stage6_3 = "/cayenne/events/stage6/3.webp"
    scene cayenne_stage6_3
    "When you spot her, you can’t help gawking at what she’s wearing."
    cayenne "I take it you like my outfit?"
    pc "It’s certainly eye catching. Where did you even get this?"
    image cayenne_stage6_4 = "/cayenne/events/stage6/4.webp"
    scene cayenne_stage6_4
    cayenne "It was a gift from the people who looked up my heritage. Apparently it has some kind of special significance with my ancestors."
    cayenne "Glad to see that my family has good taste when it comes to fashion. Anyway, what do we have for the tutoring session this time around?"
    pc "Let me see…"
    image cayenne_stage6_5 = "/cayenne/events/stage6/5.webp"
    scene cayenne_stage6_5
    "Opening up the box for the study session, you pull out a number of sizable sandwiches."
    cayenne "Mmm, those look pretty good."
    pc "They might get a little messy with all of the sauces on it. Are you sure you want to eat these wearing something like that?"
    cayenne "That’s a good point. Besides, this outfit is kind of tight anyway. Give me a second."
    image cayenne_stage6_6 = "/cayenne/events/stage6/6.webp"
    scene cayenne_stage6_6
    "After undressing herself, Cayenne strolls over to you."
    cayenne "With or without the outfit, I still look good. Feel free to stare while we take on this challenge together."
    "You find it best not to mention the extra weight you can see hanging from her mid-section and around her backside."
    "Wondering if she’s completely ignorant to her chubbier features, you regardless hand over the first sandwich."
    image cayenne_stage6_7 = "/cayenne/events/stage6/7.webp"
    scene cayenne_stage6_7
    "Accepting the first sub, she shows the results of your constant tutoring sessions by wolfing the thing down as fast as she can."
    image cayenne_stage6_8 = "/cayenne/events/stage6/8.webp"
    scene cayenne_stage6_8
    "Though she pauses for a moment to catch her breath, it doesn’t take long before she’s reaching out for the second sandwich and then the third."
    "Slowing down as she pushes herself through the final serving, she eventually manages to gobble up the last few crumbs."
    image cayenne_stage6_9 = "/cayenne/events/stage6/9.webp"
    scene cayenne_stage6_9
    "Letting out a satisfied breath, Cayenne sits on the edge of her bed."
    cayenne "Pretty impressive, huh?"
    pc "Absolutely amazing if you ask me."
    cayenne "Amazing enough to deserve a reward?"
    "Though she doesn’t outright say it, you can tell what she means. Heeding the wave of her fingers, you undress and join her on the bed."
    if persistent.nosexscene:
        scene black with dissolve
        "Cayenne and you had a good time."
    else:
        image cayenne_stage6_10 = "/cayenne/events/stage6/10.webp"
        scene cayenne_stage6_10
        #IMAGE/ANIMATION: The player having sex with Cayenne on the bed with him on top.X
        "Laying Cayenne down on the mattress, you place your hands on her hands as you slide your member inside of her."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage6/11.webm" loop
        show movie with dissolve
        window hide
        pause
        "Rocking your hips back and forth to give her the pleasure she seeks has the adverse effect of jostling her belly up against you."
        "Though you find the sensation pleasurable, you can’t help asking yourself if she’s aware of her jiggling gut."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage6/12.webm" loop
        show movie with dissolve
        window hide
        pause
        "Regardless, you continue to thrust to appease your desires."
        "Just as you’re about to release, Cayenne reaches out to grab your waist to pull you in for the final push needed to get you both to orgasm."
        stop movie
        image cayenne_stage6_13 = "/cayenne/events/stage6/13.webp"
        scene cayenne_stage6_13
        "Upon your release, you roll off of her body and onto the bed."
        "Taking your time to recover from the session of intimacy, you remain mostly oblivious to the moment Cayenne gets herself off the mattress."
    image cayenne_stage6_14 = "/cayenne/events/stage6/14.webp"
    scene cayenne_stage6_14
    "Still a little tired, you remain there under the assumption she’s either cleaning herself up or seeing if she can grab more food."
    "Your lethargy lasts until you hear her start to grunt in frustration. Lifting up your head, you watch as she tries and fails to put her outfit back on."
    image cayenne_stage6_15 = "/cayenne/events/stage6/15.webp"
    scene cayenne_stage6_15
    cayenne "What the hell? This fit just a little while ago."
    pc "Do you need some help?"
    cayenne "I should be fine. I just have to-"
    "A rip echoes through the room, making Cayenne quickly drop the clothes before she can cause any more damage."
    image cayenne_stage6_16 = "/cayenne/events/stage6/16.webp"
    scene cayenne_stage6_16
    "Moving away from the ruined outfit, Cayenne places her hand on her belly. Sliding it across the taut orb, she figures out the direct cause of her issue."
    pc "Is everything okay?"
    image cayenne_stage6_17 = "/cayenne/events/stage6/17.webp"
    scene cayenne_stage6_17
    cayenne "I’m not sure. I think it would be best for us to hold off on tutoring sessions for a bit."
    pc "What about your inheritance?"
    cayenne "I’m not completely giving up. I’ll message Ms. Tanwen and ask if I can have some time off to deal with this."
    pc "Does that mean you don’t want me coming over anymore?"
    cayenne "For now, but I’ll stay in touch. I’ll contact you when I’m ready to start again."
    "Getting back into your clothes and helping Cayenne put on something big enough for her belly bulge, you head back home."
    stop music fadeout 1.0
    #(NOTE: After this, Cayenne will be unavailable for tutoring sessions and Bunny Bites visits. She should still be able to visit the player in the gym. After about a week she should progress to the next stage.)
    $ cayennestage6event = 0
    if recollection == False:
        $ cayenne.weight += 1
        $ cayenneleave = 1
        $ daycount3 = 0
        $ daytime += 1
        jump freetime
    return

label Cayenne_Stage_7_Event:
    #Scene: Weight Loss Failure
    #(NOTE: The following should occur when the player is in his room after Cayenne reaches stage 7)
    #IMAGE: Player’s room.
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Cayenne', dialogue=dialogue_one)
    $ msg ("Hey, can you come over to my place today?", who=1)
    pause
    $ msg ("Are you ready to restart the tutoring sessions?")
    pause
    $ msg ("Not quite. I was actually looking for an exercise partner. Think you can help me out?", who=1)
    pause
    #CHOICE: A) Sorry, not today or B) Sure, I’ll be right over
    menu:
        "Sure, I’ll be right over.":
            $ msg ("Sure, I’ll be right over.")
            pause
            $ msg ("See you then.", who=1)
            pause
            $ hide_messenger()
        "Sorry, not today.":
            $ msg ("Sorry, not today.")
            pause
            $ msg ("Alright, I’ll try you some other time.", who=1)
            pause
            $ hide_messenger()
            return

    image cayenne_stage7_1 = "/cayenne/events/stage7/1.webp"
    scene cayenne_stage7_1
    play music "/music/cayenne.ogg" if_changed
    "Arriving at Cayenne’s place, you knock on the door. She greets you with a welcoming smile and her body dressed in her exercise clothing."
    cayenne "Thanks for coming by. Working out is a lot easier when someone is around to keep me company."
    image cayenne_stage7_2 = "/cayenne/events/stage7/2.webp"
    scene cayenne_stage7_2
    "Leading you into the living room, Cayenne begins to stretch."
    cayenne "I plan on going all out today, so it’s important to make sure my body is limber."
    pc "What did you have in mind?"
    image cayenne_stage7_3 = "/cayenne/events/stage7/3.webp"
    scene cayenne_stage7_3
    cayenne "I managed to find a list of exercise routines that are supposed to guarantee weight loss. They’re a little strenuous, so I’d advise you to warm up too."
    cayenne "Otherwise you won’t be able to keep up with-"
    image cayenne_stage7_4 = "/cayenne/events/stage7/4.webp"
    scene cayenne_stage7_4
    "Cayenne is interrupted by a knock at her door."
    cayenne "Weird, I wasn’t expecting anyone else. Would you mind getting that?"
    pc "Sure thing."
    image cayenne_stage7_5 = "/cayenne/events/stage7/5.webp"
    scene cayenne_stage7_5
    "Leaving Cayenne to finish stretching, you make your way over to the door."
    "While you don’t find any person waiting outside, you do see a certain something left by the doorstep. Unsure of what exactly to do with them, you decide to bring them inside."
    image cayenne_stage7_6 = "/cayenne/events/stage7/6.webp"
    scene cayenne_stage7_6
    cayenne "So who was at the door?"
    pc "No one. Just these boxes."
    cayenne "Wait, is that…?"
    image cayenne_stage7_7 = "/cayenne/events/stage7/7.webp"
    scene cayenne_stage7_7
    "Opening up the topmost box, Cayenne reveals a collection of the very same donuts that Daisy has been providing for the tutoring sessions."
    pc "Ms. Tanwen must have sent these. I thought she would have at least given you more time."
    "While you attempt to close the box and get back to the task at hand, Cayenne stops you."
    image cayenne_stage7_8 = "/cayenne/events/stage7/8.webp"
    scene cayenne_stage7_8
    "Keeping her hand in place to prevent you from closing the box, she stares upon the collection of sugary sweets."
    "Before you can ask what’s going on, she removes the box from your hands."
    image cayenne_stage7_9 = "/cayenne/events/stage7/9.webp"
    scene cayenne_stage7_9
    "Throwing aside any notion of self-control, Cayenne dives into the box. One after the other, the donuts get shoved into her mouth."
    "By the way she’s going through them, it appears as if she hasn’t eaten anything all day. Clearing out the box in record time, she locks eyes with you."
    image cayenne_stage7_10 = "/cayenne/events/stage7/10.webp"
    scene cayenne_stage7_10
    cayenne "Give me the others."
    pc "But what about your diet? What about the exercise? Aren’t you worried about gaining-"
    image cayenne_stage7_11 = "/cayenne/events/stage7/11.webp"
    scene cayenne_stage7_11
    cayenne "I said, give them to me!"
    image cayenne_stage7_12 = "/cayenne/events/stage7/12.webp"
    scene cayenne_stage7_12
    "For fear of being further reprimanded, you do as she asks and lay the boxes out for her."
    image cayenne_stage7_13 = "/cayenne/events/stage7/13.webp"
    scene cayenne_stage7_13
    "You have to move fast to keep up with her ravenous hunger, her expression one of complete surrender to her appetite."
    "Though she doesn’t speak, the sounds of her constant chewing and pleased hums fill the room."
    image cayenne_stage7_14 = "/cayenne/events/stage7/14.webp"
    scene cayenne_stage7_14
    "This unnatural scene of gluttony hits its apex as she purposefully rolls onto the ground to crawl her way over to the last box."
    image cayenne_stage7_15 = "/cayenne/events/stage7/15.webp"
    scene cayenne_stage7_15
    "Completely deprived of her former resolve to lose weight, she lifts up the top to lick her lips at the sight of the sugary morsels."
    image cayenne_stage7_16 = "/cayenne/events/stage7/16.webp"
    scene cayenne_stage7_16
    "Before she dives her head in, she turns her gaze towards you."
    cayenne "I want you."
    pc "What do you mean?"
    image cayenne_stage7_17 = "/cayenne/events/stage7/17.webp"
    scene cayenne_stage7_17
    "Reaching back, Cayenne pulls her shorts and panties down to leave her backside completely exposed."
    if persistent.nosexscene:
        scene black with dissolve
        "Cayenne and you had a good time."
    else:
        image cayenne_stage7_18 = "/cayenne/events/stage7/18.webp"
        scene cayenne_stage7_18
        cayenne "I want you to fuck me while I eat."
        "By her tone and the look in her eyes, you can tell that she’s completely serious. Unable to resist your own urges, you do as she says and get in position."
        image cayenne_stage7_19 = "/cayenne/events/stage7/19.webp"
        scene cayenne_stage7_19
        "As soon as you slide your cock into her womanhood, Cayenne dives her head into the box to begin scarfing down the donuts."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage7/vid1.webm" loop
        show movie with dissolve
        window hide
        pause
        "Moving your hips back and forth, you reach out to keep a tight grip on her hips to remain steady throughout the process."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage7/vid2.webm" loop
        show movie with dissolve
        window hide
        pause
        "You sink your fingers into the thick blubber around her hips to meet her needs and appreciate what all of your tutoring sessions have done."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage7/vid3.webm" loop
        show movie with dissolve
        window hide
        pause
        "Your movements prove effective in forcing her to occasionally stop chewing to let out a muffled collection of moans."
        "During the entire ordeal, you keep an eye on just how many donuts are left."
        stop movie
        image cayenne_stage7_20 = "/cayenne/events/stage7/20.webp"
        scene cayenne_stage7_20
        "You manage to last just long enough for her to lick up the last few drops of icing."
    image cayenne_stage7_21 = "/cayenne/events/stage7/21.webp"
    scene cayenne_stage7_21
    "Finishing up your impromptu session of passion, Cayenne gestures for you to join her on the floor."
    "It appears that her former ferocity has been somewhat sated by the session of indulgence. Even still, you can see a look of doubt lingering in her eyes."
    cayenne "Thank you. I don’t know what came over me."
    pc "Are you okay?"
    image cayenne_stage7_22 = "/cayenne/events/stage7/22.webp"
    scene cayenne_stage7_22
    cayenne "Yeah. I think my body just went into overdrive after I deprived it of food and pleasure for so long."
    cayenne "At least, that’s my hypothesis. In any case, I should probably restart the tutoring sessions."
    cayenne "Maybe I’ll learn how to control myself better. In any case, thanks for coming over. Even if it wasn’t in the way I intended, you helped a lot."
    pc "Anytime."
    image cayenne_stage7_23 = "/cayenne/events/stage7/23.webp"
    scene cayenne_stage7_23
    "Helping Cayenne pick up the leftover mess, you head home for the evening."
    stop music fadeout 1.0
    #(NOTE: After this scene Cayenne should be available for tutoring sessions and Bunny Bites visits again.)
    if recollection == False:
        $ cayenne.weight = 77
        $ daytime += 1
        $ phonecall = 1
        $ cayenneleave = 0
    $ cayennestage7event = 0
    return

label Cayenne_Stage_8_Event:
    #Scene: Post-Stuffing Shower Command
    #(NOTE: The following should take place during one of Cayenne’s tutoring sessions after reaching stage 8)
    image cayenne_stage8_1 = "/cayenne/events/stage8/1.webp"
    scene cayenne_stage8_1
    play music "/music/cayenne.ogg" if_changed
    window hide
    pause
    image cayenne_stage8_2 = "/cayenne/events/stage8/2.webp"
    scene cayenne_stage8_2
    "Upon arriving at Cayenne’s place, you knock on the door to be greeted by a smile and a hug from her."
    image cayenne_stage8_3 = "/cayenne/events/stage8/3.webp"
    scene cayenne_stage8_3
    cayenne "Glad you could make it today."
    pc "Thank you for having me. So, are you ready for another study session?"
    cayenne "Actually, I had something else in mind. Think of it like doing an experiment for extra credit."
    image cayenne_stage8_4 = "/cayenne/events/stage8/4.webp"
    scene cayenne_stage8_4
    "Waiting for you there is an intimidating stack of pizza boxes on the couch."
    pc "Is this all for you?"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/cayenne/events/stage8/vid1.webm" loop
    show movie with dissolve
    cayenne "I mean, if you want to save some for yourself go ahead, but yes."
    pc "You’re really giving it your all, aren’t you?"
    cayenne "It’s more like, I’m curious to see what’s been pushing me towards this lifestyle. It’s safe to say that this isn’t just a matter of me wanting to keep my inheritance anymore."
    stop movie
    image cayenne_stage8_5 = "/cayenne/events/stage8/5.webp"
    scene cayenne_stage8_5
    window hide
    pause
    image cayenne_stage8_6 = "/cayenne/events/stage8/6.webp"
    scene cayenne_stage8_6
    "Stripping herself down, Cayenne takes one of the pizza boxes and sits down on the couch."
    pc "Why did you do that?"
    image cayenne_stage8_7 = "/cayenne/events/stage8/7.webp"
    scene cayenne_stage8_7
    cayenne "All part of my experiment. Now if you don’t mind, could you please feed me?"
    "Unsure exactly what she’s planning, you regardless join her on the couch."
    image cayenne_stage8_8 = "/cayenne/events/stage8/8.webp"
    scene cayenne_stage8_8
    "Taking your place next to Cayenne, you proceed to hold a pizza up to her mouth."
    "She eagerly nibbles through her first serving, not even waiting to finish chewing before she gestures for you to give her another one."
    image cayenne_stage8_9 = "/cayenne/events/stage8/9.webp"
    scene cayenne_stage8_9
    "Over and over you repeat the process, trying to keep pace with her hunger."
    image cayenne_stage8_10 = "/cayenne/events/stage8/10.webp"
    scene cayenne_stage8_10
    "As you continue to feed her, you can’t help noticing how she tries to slide some of the leftover sauce across her body."
    "Though you’re curious as to why she’s doing this, you regardless move forward with the goal of keeping her belly satisfied."
    image cayenne_stage8_11 = "/cayenne/events/stage8/11.webp"
    scene cayenne_stage8_11
    "Eventually Cayenne gives the order for you to stop. Even still, you’re amazed by how much she manages to eat from the collection."
    cayenne "That was great. I’ll definitely have to order those again."
    pc "You’ve really gotten good at wolfing those down."
    image cayenne_stage8_12 = "/cayenne/events/stage8/12.webp"
    scene cayenne_stage8_12
    cayenne "Thank you, but that was merely the start of my experiment."
    pc "What do you mean?"
    image cayenne_stage8_13 = "/cayenne/events/stage8/13.webp"
    scene cayenne_stage8_13
    "Cayenne pauses for a moment to grin at you."
    cayenne "Follow me."
    image cayenne_stage8_14 = "/cayenne/events/stage8/14.webp"
    scene cayenne_stage8_14
    "Cayenne leads you into her bathroom, where upon she enters the shower and gestures for you to join her."
    image cayenne_stage8_15 = "/cayenne/events/stage8/15.webp"
    scene cayenne_stage8_15
    cayenne "Come on now. Take off those clothes and come in. You’re going to need to really get in there to clean off all this sauce."
    pc "What are you trying to-"
    image cayenne_stage8_16 = "/cayenne/events/stage8/16.webp"
    scene cayenne_stage8_16
    cayenne "No more questions, just actions. Understood?"
    pc "I…guess?"
    image cayenne_stage8_17 = "/cayenne/events/stage8/17.webp"
    scene cayenne_stage8_17
    "Following Cayenne’s orders, you strip down and join her in the shower. Closing the door behind you, she turns on the water and hands you the soap."
    cayenne "Make sure you get in there deep. I know there’s a lot of me to wash."
    image cayenne_stage8_18 = "/cayenne/events/stage8/18.webp"
    scene cayenne_stage8_18
    "Sliding the soap along her body, you try your best to wash the grease from her skin."
    "Every so often Cayenne chimes in to direct you where to go. Though you’re still unsure why you’re doing this, you appreciate the opportunity to get hands on with her body."
    image cayenne_stage8_19 = "/cayenne/events/stage8/19.webp"
    scene cayenne_stage8_19
    "You move behind her to give her breasts some extra cleaning attention."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/cayenne/events/stage8/20.webm" loop
    show movie with dissolve
    window hide
    pause
    "You manage to clean almost every part of her, save for one specific area."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/cayenne/events/stage8/21.webm" loop
    show movie with dissolve
    cayenne " know you love these soft titties, but you missed cleaning down there."
    cayenne "Well, go ahead. Every part of me needs attention. Although, I would prefer if you were to be gentle."
    pc "Um, alright."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/cayenne/events/stage8/23.webm" loop
    show movie with dissolve
    "Wrapping your arms around her, you reach below her stuffed gut to reach her womanhood."
    "Slowly sliding your fingers across her labia, you hear her let out a series of satisfied moans."
    cayenne "Yes, that’s the spot. Keep going."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/cayenne/events/stage8/24.webm" loop
    show movie with dissolve
    "As you continue to finger her, she in turn rewards you by giving attention to your rigid member."
    "Using the added heft that has been layered onto her backside, she proceeds to slide your cock between her butt cheeks over and over again."
    "Moving in unison with you, she increases her speed to make you cry out in pleasure. Hearing her start to moan soon after, you focus your attention on her clit to appease her desires."
    window hide
    pause
    stop movie
    image cayenne_stage8_25 = "/cayenne/events/stage8/25.webp"
    scene cayenne_stage8_25
    "When the two of you find your release, the fluids that come out are swiftly washed away by the running water."
    image cayenne_stage8_26 = "/cayenne/events/stage8/26.webp"
    scene cayenne_stage8_26
    "Cayenne stumbles into your arms, but you manage to keep her standing by using all of your strength."
    image cayenne_stage8_27 = "/cayenne/events/stage8/27.webp"
    scene cayenne_stage8_27
    cayenne "That was even better than I could have hoped. Excellent work."
    pc "Thank you. I take it that the experiment was a success?"
    cayenne "And then some. I’ll definitely have to explore this further. For now though, would you mind handing me the soap? I think I need to start over again."
    image cayenne_stage8_28 = "/cayenne/events/stage8/28.webp"
    scene cayenne_stage8_28
    "Cleaning yourselves off properly this time, you get dressed and head home for the day."
    stop music fadeout 1.0

    scene player_room
    "You receive a message. It’s Cayenne."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Cayenne', dialogue=dialogue_one)
    $ msg ("That was… different. I’m not used to being taken care of like that.", who=1)
    "A pause, then another message."
    $ msg ("Not that I’m complaining. You’re making it real hard to keep up this whole ‘tough girl’ act. 😏", who=1)
    "You smirk as you type a reply."
    $ msg ("Maybe I just like seeing you melt a little.")
    "A new message pops up."
    $ msg ("Melt, huh? Keep this up and you might get to see even more…", who=1)
    pause
    $ msg (None, who=1, pic="stage8_cayenne")
    pause
    $ msg ("Guess I’ll let you spoil me a little longer. 😘", who=1)
    pause
    $ hide_messenger()

    $ cayennestage8event = 0
    if recollection == False:
        $ cayenne.weight += 1
        $ daytime += 1
        jump freetime
    return

label Cayenne_Stage_9_Event:
    #Scene: Slushie Stuffing
    #(NOTE: The following should occur when the player is in their room after reaching Cayenne Stage 9)
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Cayenne', dialogue=dialogue_one)
    $ msg ("I passed an idea over with Ms. Tanwen for an extra credit assignment, but I’m going to need some help. Do you have some free time today?", who=1)
    pause
    #CHOICE: A) Sorry, I’m busy or B) Sure, when do you want me to come over?
    menu:
        "Sure, when do you want me to come over?":
            $ msg ("Sure, when do you want me to come over?")
            pause
            $ msg ("Actually, I need you to run me a little errand first.", who=1)
            pause
            $ msg ("What do you mean?")
            pause
            $ msg ("Go to this address and pick up an order for me. It should be under my name, and I’ll pay for it ahead of time. Make sure you get to my place quick before they melt.", who=1)
            pause
            $ msg ("I’m on my way.")
            pause
            $ hide_messenger()
        "Sorry, I’m busy":
            $ msg ("Sorry, I’m busy")
            pause
            $ msg ("That’s alright. We can try again some other time.", who=1)
            pause
            $ hide_messenger()
            return

    "Putting away your phone and getting yourself ready, you make your way over to the address."
    image cayenne_stage9_1 = "/cayenne/events/stage9/1.webp"
    scene cayenne_stage9_1
    "Though it takes a bit of effort, you manage to haul Cayenne’s order over to the house."
    "Multiple times you’re tempted to sample some of it to quench your thirst, but there’s a feeling in the back of your head that keeps you from drinking."
    "Getting a feeling similar to a collar being pulled around your neck every time you entertain the idea of helping yourself to the order."
    "you manage to make it to Cayenne’s house and knock on the door with your foot."
    image cayenne_stage9_2 = "/cayenne/events/stage9/2.webp"
    scene cayenne_stage9_2
    play music "/music/cayenne.ogg" if_changed
    "Just as you feel like your strength is about to give out, Cayenne opens up the door."
    image cayenne_stage9_3 = "/cayenne/events/stage9/3.webp"
    scene cayenne_stage9_3
    "Seeing you struggle with the cumbersome load, she reaches out to take some of the burden off of your shoulders."
    cayenne "Sorry, I didn’t realize that it would be this much when I made the order. Come on in and we’ll get this all sorted out."
    pc "Thank you."
    image cayenne_stage9_4 = "/cayenne/events/stage9/4.webp"
    scene cayenne_stage9_4
    "Following Cayenne inside, you carry the order to the kitchen area and spread it along a table."
    image cayenne_stage9_5 = "/cayenne/events/stage9/5.webp"
    scene cayenne_stage9_5
    "Partially tired from the effort, you sit down for a much needed rest. You watch as Cayenne wastes little time helping herself to the first slushie."
    image cayenne_stage9_6 = "/cayenne/events/stage9/6.webp"
    scene cayenne_stage9_6
    cayenne "Mmm, this really hits the spot. I absolutely love the banana flavor. Then again, the cherry and blue raspberry are pretty good as well. Or maybe the cola one is best?"
    pc "Are you really going to stuff yourself with all of these?"
    cayenne "I’ll have to be careful to not drink too fast to avoid brain freeze, but I think I can manage."
    image cayenne_stage9_7 = "/cayenne/events/stage9/7.webp"
    scene cayenne_stage9_7
    "She finishes off the first cup."
    image cayenne_stage9_8 = "/cayenne/events/stage9/8.webp"
    scene cayenne_stage9_8
    cayenne "Especially when each of them is this tasty. Hand me the grape flavor. I haven’t tried that one yet."
    image cayenne_stage9_9 = "/cayenne/events/stage9/9.webp"
    scene cayenne_stage9_9
    "Following her orders, you continue to hand over more cups to aid in her effort to sample each and every type."
    image cayenne_stage9_10 = "/cayenne/events/stage9/10.webp"
    scene cayenne_stage9_10
    cayenne "All of these flavors taste so good. I don’t know if I’ll be able to pick a favorite. You think Ms. Tanwen will accept the assignment if I just say they’re all good?"
    pc "I think you might have spilled a little on your clothes."
    image cayenne_stage9_11 = "/cayenne/events/stage9/11.webp"
    scene cayenne_stage9_11
    cayenne "That’s okay. I don’t need them right now anyway. In fact, let me get undressed."
    image cayenne_stage9_12 = "/cayenne/events/stage9/12.webp"
    scene cayenne_stage9_12
    window hide
    pause
    image cayenne_stage9_13 = "/cayenne/events/stage9/13.webp"
    scene cayenne_stage9_13
    "Freed from her clothes, Cayenne doubles her efforts to drink down the frozen treats."
    image cayenne_stage9_14 = "/cayenne/events/stage9/14.webp"
    scene cayenne_stage9_14
    window hide
    pause
    image cayenne_stage9_15 = "/cayenne/events/stage9/15.webp"
    scene cayenne_stage9_15
    "With nothing left to hold it back, her belly is free to bulge out to contain her liquid feast."
    image cayenne_stage9_16 = "/cayenne/events/stage9/16.webp"
    scene cayenne_stage9_16
    "As her gut begins to sag between her legs, she pauses to speak once more."
    image cayenne_stage9_17 = "/cayenne/events/stage9/17.webp"
    scene cayenne_stage9_17
    cayenne "Come over here and rub my belly."
    "Realizing it’s less of a suggestion and more of a command, you do as your told and step forward."
    image cayenne_stage9_18 = "/cayenne/events/stage9/18.webp"
    scene cayenne_stage9_18
    "Taking your position next to her, you massage her swollen gut."
    image cayenne_stage9_19 = "/cayenne/events/stage9/19.webp"
    scene cayenne_stage9_19
    "Your efforts allow her to push through the final stretch of drinks to fill out her mid-section even further."
    image cayenne_stage9_20 = "/cayenne/events/stage9/20.webp"
    scene cayenne_stage9_20
    "Feeling her belly slosh around with every push of your hands, you begin to wonder if she can really finish off the entire order."
    image cayenne_stage9_21 = "/cayenne/events/stage9/21.webp"
    scene cayenne_stage9_21
    cayenne "That’s enough."
    pc "You can’t drink anymore?"
    image cayenne_stage9_22 = "/cayenne/events/stage9/22.webp"
    scene cayenne_stage9_22
    cayenne "Oh I have plenty of space leftover. I just need to get ready for the most important part of the experiment. Grab those remaining cups and meet me on the couch."
    image cayenne_stage9_23 = "/cayenne/events/stage9/23.webp"
    scene cayenne_stage9_23
    "Following Cayenne into the living room with the drinks in hand, you watch as she takes her place in the center of the cushions."
    image cayenne_stage9_24 = "/cayenne/events/stage9/24.webp"
    scene cayenne_stage9_24
    "Spreading out her legs to let her belly droop between her thighs, she grabs one of the cups to resume chugging it down."
    image cayenne_stage9_25 = "/cayenne/events/stage9/25.webp"
    scene cayenne_stage9_25
    cayenne "Looks like I’m just about ready. [playername], I want you to take care of my other needs. Preferably with your mouth."
    pc "Where is this coming from?"
    image cayenne_stage9_26 = "/cayenne/events/stage9/26.webp"
    scene cayenne_stage9_26
    "For just a moment you see a glare in Cayenne’s eyes."
    cayenne "You heard me. Get down and put that mouth of yours to work like a good boy."
    image cayenne_stage9_27 = "/cayenne/events/stage9/27.webp"
    scene cayenne_stage9_27
    "You hesitate for a moment to figure out what’s going on. The longer you take, the more you see the stern expression on her face begin to drift into a more apologetic look."
    "Wondering if this is all part of Cayenne’s experiment, you finally reply."
    pc "Very well. Hold still."
    image cayenne_stage9_28 = "/cayenne/events/stage9/28.webp"
    scene cayenne_stage9_28
    cayenne "Excellent. Make sure you leave the drinks within reach before you get down there."
    pc "Of course."
    if persistent.nosexscene:
        scene black with dissolve
        "Cayenne and you had a good time."
    else:
        image cayenne_stage9_29 = "/cayenne/events/stage9/29.webp"
        scene cayenne_stage9_29
        "Lifting her belly up above your head, you slide yourself between her legs to get at her womanhood."
        "Bracing yourself for the impact, you allow her gut to come falling down on your back."
        image cayenne_stage9_30 = "/cayenne/events/stage9/30.webp"
        scene cayenne_stage9_30
        "Bearing the weight of her belly fat, you hold on tight to her waist as you push forward to drag your tongue across her labia."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage9/sex1.webm" loop
        show movie with dissolve
        "You know you’re doing something right as you hear moans begin to intersperse her sips."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage9/sex2.webm" loop
        show movie with dissolve
        "Moving in a little closer, you focus your attention on her clit in an attempt to finish alongside her feast."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/cayenne/events/stage9/sex3.webm" loop
        show movie with dissolve
        "She’s only stopped from taking the last few sips needed to finish her slushie thanks to the resulting cry of ecstasy you feel as she reaches her climax."
        window hide
        pause
        stop movie
        image cayenne_stage9_31 = "/cayenne/events/stage9/31.webp"
        scene cayenne_stage9_31
        window hide
        pause
        image cayenne_stage9_32 = "/cayenne/events/stage9/32.webp"
        scene cayenne_stage9_32
        "Removing yourself from Cayenne’s nether region, you stand up to watch as she pours last few drops down her throat."
        image cayenne_stage9_33 = "/cayenne/events/stage9/33.webp"
        scene cayenne_stage9_33
        cayenne "That was better than I expected. Come have a seat. You’ve earned yourself a rest."
        "Heeding both her and your own exhaustion, you sit down next to her."
    image cayenne_stage9_34 = "/cayenne/events/stage9/34.webp"
    scene cayenne_stage9_34
    "As you lean back, she hands you one of the remaining slushies."
    "Taking a sip to replenish your energy, you decide to ask her something."
    #CHOICE: A) How did I do? or B) Since when did you get so bossy?
    menu:
        "How did I do?":
            image cayenne_stage9_35 = "/cayenne/events/stage9/35.webp"
            scene cayenne_stage9_35
            cayenne "You did wonderfully. Sorry if I was a bit rough with you. It was all part of my little experiment."
        "Since when did you get so bossy?":
            image cayenne_stage9_35 = "/cayenne/events/stage9/35.webp"
            scene cayenne_stage9_35
            cayenne "Sorry if I was a little mean to you. I was trying out a kind of experiment."

    #(NOTE: The following dialog should play after either choice)
    pc "What kind of experiment?"
    image cayenne_stage9_36 = "/cayenne/events/stage9/36.webp"
    scene cayenne_stage9_36
    cayenne "There’s been this feeling I’ve been getting every time I give you an order. It’s like a type of satisfaction similar to when I either eat or have sex."
    cayenne "A little hard to explain, I know, but I’m just as in the dark as you are. My hope was that I would figure out something by being a little more dominant."
    pc "And the results?"
    image cayenne_stage9_37 = "/cayenne/events/stage9/37.webp"
    scene cayenne_stage9_37
    "Cayenne shrugs."
    cayenne "I’m still just as clueless as ever, but at least it made for a fun time. Mind if we do something like this again?"
    pc "Sure, just maybe do delivery next time to save my back."
    image cayenne_stage9_38 = "/cayenne/events/stage9/38.webp"
    scene cayenne_stage9_38
    cayenne "Can do."
    "Finishing your drink and helping Cayenne throw away the empty cups, you head home for the day."
    stop music fadeout 1.0

    if recollection == False:
        $ cayenne.weight += 1
        $ daytime += 1
        $ phonecall = 1
    $ cayennestage9event = 0
    return

#label Cayenne_Stage_10_Event:

    #Cayenne Stage 10 event
    #Scene: Introduction of Cayenne’s Servants.
    #(NOTE: The following should occur when the player is in his room after reaching stage 10 with Cayenne and being introduced to the Followers of Heset)
    "I receive a message from Daisy."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Daisy', dialogue=dialogue_one)
    $ msg ("Are you going to be doing your tutoring session anytime soon?", who=1)
    pause
    $ msg ("I was thinking about it. Why?")
    pause
    $ msg ("Let me get something straight. How persuasive are you with Cayenne?", who=1)
    pause
    #CHOICE: A) Sorry, I’m busy or B) Sure, when do you want me to come over?
    menu:
        "I think I’m pretty convincing.":
            $ msg ("I think I’m pretty convincing.")
            pause
            $ msg ("Good. I’ll give a call to Cayenne for a special tutoring session today.", who=1)
            pause
            $ msg ("Wait, why now?")
            pause
            $ msg ("You’ll see very soon. Now get going. It sets a bad standard for a teacher to be tardy for their student.", who=1)
            pause
            $ hide_messenger()
        "Not very much.":
            $ msg ("Not very much.")
            pause
            $ msg ("That is a shame. Try to work on your communication skills and I’ll get back to you on this.")
            pause
            $ hide_messenger()
            return

    "Confused at exactly what’s going on, you make your way over to Cayenne’s house."
    #IMAGE: Cayenne standing at the door to her house.
    "Knocking on the door, Cayenne greets you with her usual smile."
    cayenne "I just got the call from Ms. Tanwen about the impromptu study session. Any idea what’s going on?"
    pc "Not a clue. You tend to get used to her ‘unique’ teaching methods."
    cayenne "I’m still waiting for the study materials to arrive, but we can get a head start. Follow me."
    #IMAGE: Cayenne sitting on her living room couch with a single box of doughnuts.
    pc "Where did you get these?"
    cayenne "Same as most people that aren’t enrolled in a strange study program. I ordered them myself."
    cayenne "I know it’s nothing compared to the usual study session amounts, but it should make for a good starting point."
    pc "Why not just wait until the materials arrive?"
    "Cayenne grasps her belly and pushes it outwards."
    cayenne "I don’t think this thing can wait any longer."
    pc "If you say so. Let’s go ahead and get started then."
    #IMAGE: Cayenne eating doughnuts on the couch.
    "With that little bit of provocation, Cayenne proceeds to help herself to the doughnuts."
    "Comparing it to her initial feedings, you can see the drastic improvements she’s made to her ability to stuff her face."
    "In no time at all she finishes off the box."
    cayenne "That was a pretty good treat. I think it’s time for my reward, don’t you?"
    #IMAGE: Naked Cayenne laying across the couch and masturbating.
    "Not waiting for your response, Cayenne proceeds to undress herself. Laying herself down on the couch, she uses one hand to massage her body while the other begins to rub herself."
    "Looking into your eyes, she licks her lips as a sign for you to join her. Just as you’re about to undress to give her what she wants, there’s a knock at the door."
    cayenne "I’m guessing that’s the study material. Would you mind getting that? I’m a little busy at the moment."
    "Leaving Cayenne to continue indulging herself, you go to answer the door."
    #IMAGE: The helpers Gebi (Brown hair in ponytail with white skin) and Nuit (Long Black hair with dark sin) standing outside the door of Cayenne’s house wearing long coats or something to obscure their helper outfits)
    "Opening up the door, you freeze as you lock eyes with the two women standing before you."
    "If the coats adorning their bodies aren’t enough to raise a red flag, the eerily familiar looking face masks that leave only their eyes and hair visible make you consider slamming the door on them."
    "Perhaps sensing your concern, they step forward to bow and stand in the entryway."
    $ unknownname = 'Cultist with brown hair'
    unknown "Hello, [playername]. It is a pleasure to meet you."
    $ unknownname = 'Cultist with black hair'
    unknown "Yes, it is excellent to see the person that Daisy finds so much potential in."
    pc "Er, thanks? I guess that answers where you two came from. But it doesn’t tell me why you’re-"
    "Before you can get another word out, the two women push past you to enter the living room. Hearing Cayenne let out a distressed shout, you rush over to see what’s going on."
    #IMAGE: Cayenne standing in the living room trying to cover up her naked body with the Helpers standing beside her with their Followers outfits on display.
    "Returning to the living room, you arrive to see Cayenne making a poor attempt to obscure her naked figure."
    "In direct contrast, the strange women seem to have no problem shedding their coats to reveal their unique choice in wardrobe."
    "As strange as the outfits appear, the impact is somewhat softened by the fact that you recognize them as being similar to the Followers of Heset’s ceremonial outfits."
    cayenne "Who are you and why are you in my house?"
    gebi "My name is Gebi."
    nuit "And I am Nuit."
    gnn "We have come to serve you, Mistress Cayenne."
    cayenne "That doesn’t really explain anything. Give me one good reason why I shouldn’t call the cops on you."
    gebi "Please, we do not mean any harm."
    nuit "We are only here to assist with your development."
    cayenne "My what?"
    #IMAGE: Same as before, but with Nuit holding the empty box of doughnuts.
    "Stepping away for a moment, Nuit grabs the empty box of doughnuts."
    nuit "You have made ample progress so far, but there is still so much more for you to learn."
    gebi "[playername] has been doing an excellent job by himself. However, the time has come for us to lend our skills to you."
    "The mention of your name immediately turns Cayenne’s attention towards you in search of answers."
    cayenne "[playername], do you have any idea what’s going on?"
    "As much as you want to reveal everything to her, you decide to choose your next few words carefully."
    pc "I don’t know everything, but I can confirm that they are connected to Ms. Tanwen and that they’re only here to help."
    "Though it takes a moment, Cayenne swallows the answer and turns towards the Helpers."
    cayenne "When you said you’re here to assist me, do you mean you came over to aid with my study sessions?"
    gebi "That is correct. Merely give the order and we shall continue where your friend here has left off with your latest feast."
    nuit "While we believe in the power of following fate, we shall not force this upon you."
    gnn "Tell us. What is your choice, Mistress Cayenne?"
    "Turning away from the women, Cayenne looks to you for an answer."
    "It’s only through a combination of your built up trust with her and your ability to read her emotions that you’re able to properly respond by a simple nod of your head."
    "Making the same gesture to confirm, she turns back to face the Helpers, no longer trying to hide her nude form."
    cayenne "Where do we begin?"
    gebi "I believe this couch would be a good starting point. Nuit, would you please grab the provisions?"
    nuit "Of course."
    gebi "Excellent. Mistress, please follow me."
    #IMAGE: Cayenne sitting on the couch with Gebi kneeling in front of her. Nuit should be to the side with a stack of doughnut boxes.
    "Setting Cayenne down on the couch cushions, Gebi kneels down on the floor before her. Just as the Helper gets into position, Nuitt returns with a stack of doughnut boxes."
    nuit "These are your favorite, correct?"
    cayenne "Yeah."
    gebi "Then we shall proceed."
    "Cayenne reaches out for the first box, only for Nuit to step out of reach."
    cayenne "Wait, I thought you wanted me to eat. I can’t do that if I can’t reach any doughnuts."
    nuit "There is no need for you to feed yourself when we are here, Mistress."
    gebi "Yes. We will be sure to take care of your needs."
    cayenne "Alright, if you say so."
    nuit "[playername], I must ask for you to observe so that you may better serve our mistress in the future."
    pc "Only if she’s okay with it."
    cayenne "Yeah, it’s fine. You being here might actually make it easier for me."
    #IMAGE: Gebi feeding Cayenne doughnuts on the couch.
    "Accepting the first box from Nuit, Gebi proceeds to stuff doughnuts into Cayenne’s mouth."
    "You’ve done this many times before yourself, however the Helper’s movements seem almost robotic with how deliberate they are."
    "As soon as one box is emptied out, Nuit is able to pass over the next with perfect timing."
    "Glancing away from the seemingly well-rehearsed routine, you see a specific look in Cayenne’s eyes that usually comes with these stuffing sessions."
    "Before she can ask for it or before you can even think to broach the topic, Gebi takes the initiative."
    #IMAGE: Gebi continuing to feed Cayenne while simultaneously fingering her vagina.
    "Without skipping a beat, Gebi slides her hand beneath Cayenne’s belly to begin stimulating her womanhood."
    "Stopping just long enough to allow Cayenne to let out a moan, the Helper uses her free hand to push in another doughnut."
    "With the same precision as before, Gebi is able to focus on the exact spots she needs to, all the while continuing to stuff Cayenne’s face."
    "In record time, you hear Cayenne let out a euphoric cry as her body is overcome with orgasmic shivers."
    #IMAGE: Cayenne slouched in her position on the couch with a doughnut in her mouth and Nuit and Gebi standing next to her.
    "As Cayenne comes down from her climax, Gebi gives her one last doughnut to chew on before standing up."
    gebi "You appear to be progressing nicely, Mistress."
    "Cayenne lets out a muffled series of words. While you can’t quite make it out, you have to assume its some form of thanks."
    nuit "I shall be taking over from here. Gebi, would you please retrieve the rest of the supplies?"
    gebi "Certainly."
    nuit "Mistress, I must ask for you to lay down on the couch for the next step."
    cayenne "Alright."
    #IMAGE: Cayenne lying down on the couch with Nuit sitting squatting down to rub her belly.
    "As Cayenne gets into position, Nuit takes it upon herself to ease the digestion process."
    "Gently placing her fingers along Cayenne’s belly, the Helper proceeds to caress the swollen gut to ease her burden."
    "The relaxed sighs that leave Cayenne’s lips as she continues proves that the massage is working to put the woman in a state of relaxation."
    "It’s because of this bliss that you are the first to notice Gebi return with more food."
    #IMAGE: Nuit feeding Cayenne on the couch.
    "Accepting the food from Gebi, Nuit proceeds to resume feeding Cayenne."
    "Just like before, she’s able to time herself perfectly between when Cayenne needs to breath and when her mouth is eager for more food."
    "As her belly continues to swell over the course of the feast, Nuit is sure to constantly reach down to rub the swelling orb to keep it satisfied."
    nuit "Is everything to your liking, mistress?"
    cayenne "The food is wonderful. But I need more."
    nuit "Sustenance?"
    cayenne "No…pleasure."
    gebi "Then I would be more than happy to take care of that for you."
    #IMAGE: Gebi eating out Cayenne while Nuit continues the feeding session.
    "While Nuit continues to shovel food into Cayenne’s mouth, Gebi climbs up onto the couch."
    "Spreading open Cayenne’s legs and diving beneath her stomach, the Helper proceeds to suck and drag against her mistress’s pussy."
    "Yet again, Cayenne’s feast is interrupted by a series of moans. You can only watch as Cayenne is subjected to a state of complete hedonism."
    "Your fingers clench as you resist your own urges to join in."
    "Just as Nuit is able to push in the last morsel of food, Gebi give the last bit of stimulation needed for Cayenne to reach her second release."
    #IMAGE: Cayenne sitting on the couch with Nuit and Gebi standing before her.
    "Waiting for Cayenne to recover from the experience, Nuit and Gebi help her into a sitting position."
    gebi "I do hope you found our services satisfactory, Mistress."
    cayenne "That and more."
    nuit "Excellent. Then if there is nothing else, we will be taking our leave for today."
    cayenne "But you just got here."
    gebi "We must return to make our report with our master. Do not fear, we will see each other again."
    cayenne "Okay, guess I’ll see you then."
    #IMAGE: Nuit and Gebi standing in front of the player in the living room with Cayenne on the couch.
    "Leaving Cayenne to sleep off the after effects of the feeding session, Nuit and Gebi approach you."
    nuit "We must thank you for your work with Mistress Cayenne up to this point."
    gebi "Yes. We hope that you will continue to aid her on the path to her evolution."
    pc "Evolution?"
    nuit "All shall be revealed later."
    gebi "For now, keep up your work. Mistress Cayenne is not the only person fate has decided to be integral to our success."
    "Left with more questions than answers, you watch as the Helpers take their leave. Thinking it best to give Cayenne time to sleep, you head home for the day."

    $ unknownname = 'Unknown'
    $ cayennestage10event = 0
    return

label Cayenne_Home:
    #Scene: Repeatable Tutoring Sessions
    #(NOTE: This scene will be constantly updated over the course of Cayenne’s story to add things like different foods to eat and sex positions.)
    image cayenne_home_arrive = "/cayenne/[cayenne.stage]/home_arrive.webp"
    scene cayenne_home_arrive
    play music "/music/cayenne.ogg" if_changed
    "After making the call, you head over to Cayenne’s house."
    cayenne "Good to see you again."
    image cayenne_home_talk = "/cayenne/[cayenne.stage]/home_talk.webp"
    scene cayenne_home_talk
    pc "Hello Cayenne. Are you ready for today’s tutoring session?"
    cayenne "You bet. I have all the study materials ready to go. Let’s get started."
    image cayenne_home_book = "/cayenne/[cayenne.stage]/home_book.webp"
    scene cayenne_home_book
    "You spend some time going over the lesson materials with Cayenne. In the process, you feel like you’ve improved your own knowledge."
    #"Your intelligence has increased."
    image cayenne_home_choice = "/cayenne/[cayenne.stage]/home_choice.webp"
    scene cayenne_home_choice
    cayenne "I think that’s about all I can learn from books alone. Do you think we can do a hands on lesson?"

    #CHOICE: A) Sorry, we’ll have to save it for another time or B) Alright, what would you like to eat?
    menu:
        "Alright, what would you like to eat?":
            image cayenne_home_dress1 = "/cayenne/[cayenne.stage]/home_dress1.webp"
            scene cayenne_home_dress1
            cayenne "Let me grab my eating outfit first."
            "Cayenne leaves you for a minute before returning in her outfit."
            image cayenne_home_dress2 = "/cayenne/[cayenne.stage]/home_dress2.webp"
            scene cayenne_home_dress2
        "Sorry, we’ll have to save it for another time.":
            cayenne "Shame, but I understand. I’ll see you later."
            "Picking up the study materials, you say goodbye to Cayenne and head home."
            $ daytime += 1
            jump freetime


    cayenne "Let me see what Ms. Tanwen sent me."
    image cayenne_home_meal1 = "/cayenne/[cayenne.stage]/home_meal1.webp"
    scene cayenne_home_meal1
    #(NOTE: For variety, the image should swap between different types of meals for each time the player chooses this option. The same text should play out regardless of whichever food item is chosen.)
    "Spreading out the food for the study session, you watch as Cayenne begins her feast."
    image cayenne_home_meal2 = "/cayenne/[cayenne.stage]/home_meal2.webp"
    scene cayenne_home_meal2
    "Though she struggles at certain points, you manage to help her get through the bulk of it."
    "The combined effort helps her to finish off every last bite."
    image cayenne_home_meal3 = "/cayenne/[cayenne.stage]/home_meal3.webp"
    scene cayenne_home_meal3
    cayenne "I think that’s everything that was in the box."
    if cayennestory <= 4 and cayenne.stage >= 11:
        menu:
            "Ask Cayenne about herself.":
                "You decide to ask Cayenne about herself."
                cayenne "My past?"
                cayenne "Sure, while I love history, my own is not too exciting."
                "Cayenne talks a bit about herself."
                $ cayennestory += 1
                #Unlocks more Cayenne story in the stats page.
                $ renpy.notify("New Cayenne story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Cayenne anything."
    elif cayennestory == 3 and cayenne.stage >= 10:
        menu:
            "Ask Cayenne about herself.":
                "You decide to ask Cayenne about herself."
                cayenne "My past?"
                cayenne "Sure, while I love history, my own is not too exciting."
                "Cayenne talks a bit about herself."
                $ cayennestory += 1
                #Unlocks more Cayenne story in the stats page.
                $ renpy.notify("New Cayenne story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Cayenne anything."
    elif cayennestory == 2 and cayenne.stage >= 8:
        menu:
            "Ask Cayenne about herself.":
                "You decide to ask Cayenne about herself."
                cayenne "My past?"
                cayenne "Sure, while I love history, my own is not too exciting."
                "Cayenne talks a bit about herself."
                $ cayennestory += 1
                #Unlocks more Cayenne story in the stats page.
                $ renpy.notify("New Cayenne story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Cayenne anything."
    elif cayennestory == 1 and cayenne.stage >= 6:
        menu:
            "Ask Cayenne about herself.":
                "You decide to ask Cayenne about herself."
                cayenne "My past?"
                cayenne "Sure, while I love history, my own is not too exciting."
                "Cayenne talks a bit about herself."
                $ cayennestory += 1
                #Unlocks more Cayenne story in the stats page.
                $ renpy.notify("New Cayenne story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Cayenne anything."
    elif cayennestory == 0:
        menu:
            "Ask Cayenne about herself.":
                "You decide to ask Cayenne about herself."
                cayenne "My past?"
                cayenne "Sure, while I love history, my own is not too exciting."
                "Cayenne talks a bit about herself."
                $ cayennestory += 1
                #Unlocks more Cayenne story in the stats page.
                $ renpy.notify("New Cayenne story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Cayenne anything."
    cayenne "Was there anything else for this study session?"

    menu:
        "Give her more food.":
            "Taking out your own food, you ask her to keep going."
            image cayenne_home_meal4 = "/cayenne/[cayenne.stage]/home_meal4.webp"
            scene cayenne_home_meal4
            "She hesitates for a moment but continues her study session regardless."
            image cayenne_home_meal5 = "/cayenne/[cayenne.stage]/home_meal5.webp"
            scene cayenne_home_meal5
            "Just like before, she manages to eat every last bite."
            $ stuffed = 1
            call rngeatingcayennehomefoodchoice from _call_rngeatingcayennehomefoodchoice_4
            cayenne "Is there any more? I think I can handle it, but I doubt I’ll be able to do much afterwards other than pass out."
            show screen cayennefullness
            $ cayenne.fullness = 1
            call cayenne_home_feeding from _call_cayenne_home_feeding_4
            pause
            $ cayenne.weight += (cayenne.fullness / 4)
            $ cayenne.fullness = 0
            $ lastfooditem = 0
            hide screen cayennefullness
            pause
            cayenne "Whoo, that was a lot of food."
            if stuffed == 3:
                "Swallowing the last bite, Cayenne asks you to bring her over to the couch."
                "The moment her head hits the pillow, she drifts off into a well deserved nap."
                scene city
                "Making sure she’s comfortable, you head for home."
                $ stuffed = 0
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime
            elif stuffed == 2:
                "Cayenne asks you to bring her over to the couch."
                "The moment her head hits the pillow, she drifts off into a well deserved nap."
                scene city
                "Making sure she’s comfortable, you head for home."
                $ stuffed = 0
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime
            elif stuffed == 1:
                cayenne "Any ideas on how to work this off?"
        "No, that’s it.":
            cayenne "Any ideas on how to work this off?"




    #CHOICE: A) A massage, B) Dancing, C) Masturbation, or D) Sex
    menu:
        "A massage.":
            cayenne "I was hoping for something a little more involved, but I see your point. Mind helping me out?"
            image cayenne_home_massage1 = "/cayenne/[cayenne.stage]/home_massage1.webp"
            scene cayenne_home_massage1
            $ stuffed = 0
            "Taking your place alongside Cayenne on the couch, you slide her hands along her gut to help with her digestion."
            image cayenne_home_massage2 = "/cayenne/[cayenne.stage]/home_massage2.webp"
            scene cayenne_home_massage2
            "Taking your place alongside Cayenne on the couch, you slide her hands along her gut to help with her digestion."
            "Once you’ve helped her settle her stomach, you say goodbye and take your leave."
            stop music fadeout 1.0
            $ daytime += 1
            jump freetime
        "Dancing." if cayennestage3event == 0:
            #(NOTE: should be made available after Cayenne’s stage 3 event)
            cayenne "Sounds like a plan. Wait in the living room. I’ll be right back."
            image cayenne_home_dance1 = "/cayenne/[cayenne.stage]/home_dance1.webp"
            scene cayenne_home_dance1
            $ stuffed = 0
            "Taking a moment to change into her dance outfit, she returns to flaunt her body in front of you."
            cayenne "Ready when you are."
            "Starting up the appropriate music, you watch as Cayenne begins to dance."
            if cayenne.stage == 3:
                $ renpy.movie_cutscene("/images/cayenne/3/home_dance2.webm")
            elif cayenne.stage == 4:
                $ renpy.movie_cutscene("/images/cayenne/4/home_dance2.webm")
            elif cayenne.stage == 5:
                $ renpy.movie_cutscene("/images/cayenne/5/home_dance2.webm")
            elif cayenne.stage == 6:
                $ renpy.movie_cutscene("/images/cayenne/6/home_dance2.webm")
            elif cayenne.stage == 7:
                $ renpy.movie_cutscene("/images/cayenne/7/home_dance2.webm")
            elif cayenne.stage == 8:
                $ renpy.movie_cutscene("/images/cayenne/8/home_dance2.webm")
            elif cayenne.stage == 9:
                $ renpy.movie_cutscene("/images/cayenne/9/home_dance2.webm")
            elif cayenne.stage == 10:
                $ renpy.movie_cutscene("/images/cayenne/10/home_dance2.webm")
            elif cayenne.stage == 11:
                $ renpy.movie_cutscene("/images/cayenne/11/home_dance2.webm")
            image cayenne_home_dance3 = "/cayenne/[cayenne.stage]/home_dance3.webp"
            scene cayenne_home_dance3
            "Even with the added weight from her latest binge session, she proves that she’s more than capable of elegant motions that move along with the beat."
            "So entranced by her dance, it comes as a complete surprise to you when the performance ends."
            "Upon hearing your applause, Cayenne takes a bow."
            cayenne "Thank you, thank you. You’re too kind."
            "Continuing your applause for a bit longer, you say your goodbye and head for home."
            stop music fadeout 1.0
            $ daytime += 1
            jump freetime
        #"Masturbation." if cayennestage4event == 0:
            #(NOTE: should be made available after Cayenne’s stage 4 event)
            "The crude suggestion nonetheless seems to agree with her."
            cayenne "Guess if you’ve seen me once, the other times aren’t as jarring. Alright, help me out of my clothes. I don’t know how much longer I can restrain myself."
            #IMAGE: Naked Cayenne on her couch, masturbating.
            $ stuffed = 0
            "Taking off Cayenne’s clothes seems to also remove all of her inhibitions as she begins to touch herself."
            "While one hand focuses on rubbing her womanhood, the other pokes and prods at the results of her latest feeding session."
            "Though you’re limited to just watching the display, your mere presence seems to enhance her experience."
            "Reaching the apex of her pleasure, your ears tingle as she cries out and reaches her climax."
            #IMAGE: Naked Cayenne sitting on the couch.
            cayenne "I really needed that. Thanks for keeping me company for both the food and my extracurriculars."
            "Helping Cayenne pick up the leftover food, you head for home."
            stop music fadeout 1.0
            $ daytime += 1
            jump freetime
        "Sex." if cayennestage5event == 0:
            if persistent.nosexscene == True:
                "You have sex scenes disabled in preferences, now leaving Cayenne's home."
                stop music fadeout 1.0
                return
            #(NOTE: Should be made available after Cayenne’s stage 5 event. Cayenne will randomly choose between different positions depending on how far the player has progressed with her.)
            cayenne "A little upfront aren’t you? Not that I’m complaining, but I still think I should be the one to choose how we do it."
    pc "What did you have in mind?"
    stop music fadeout 1.0
    #RANDOM PICK: Cayenne’s choices. 1) Cayenne leaning over the side of the bed with the player in the lead, 2) Cayenne on all fours while she eats from a box of donuts 3) Shower sex 4) Cayenne on her bed with her on top
    if cayenne.stage >= 9:
        $ rng = renpy.random.randint(1,3)
    #elif cayenne.stage == 8:
    #    $ rng = renpy.random.randint(1,3)
    elif cayenne.stage == 7:
        $ rng = renpy.random.randint(1,2)
    else:
        $ rng = 1

    if rng == 1:
        #Cayenne Choice 1) Cayenne leaning over the side of the bed with the player in the lead (Available at the start after the stage 5 event)
        cayenne "I want to do something, but I’m not sure I have the energy to take the lead this time. Would you please bring me over to my bed?"
        "Bringing Cayenne up to her room, you help her undress. Taking off your own clothes, you get in position according to her specifications."
        image cayenne_home_sex1 = "/cayenne/[cayenne.stage]/home_sex1.webp"
        scene cayenne_home_sex1
        $ stuffed = 0
        "Leaning her over the side of the bed, you get on your knees and press your face into her womanhood."
        if cayenne.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/5/home_sex1_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/6/home_sex1_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/7/home_sex1_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/8/home_sex1_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/9/home_sex1_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/10/home_sex1_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/11/home_sex1_video.webm" loop
            show movie with dissolve
        window hide
        pause
        "Dragging your tongue along her folds and sucking on her clit, you revel in the feeling of shivers going through her body."
        "Though your efforts start to make her moan, you’re stopped from going any further as she pulls away."
        cayenne "I can’t take it anymore. I want you inside me, now."
        stop movie
        image cayenne_home_sex2 = "/cayenne/[cayenne.stage]/home_sex2.webp"
        scene cayenne_home_sex2
        "Doing as she commands, you turn her over to the side and spread her legs."
        if cayenne.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/5/home_sex2_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/6/home_sex2_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/7/home_sex2_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/8/home_sex2_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/9/home_sex2_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/10/home_sex2_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/11/home_sex2_video.webm" loop
            show movie with dissolve
        window hide
        pause
        "Exerting yourself to keep her body in place, you proceed to shove your cock into her waiting pussy."
        "While the position provides ample pleasure, you’re not sure how long your strength can hold out. Just as your stamina is about to fail you, you both reach your climax."
        stop movie
        image cayenne_home_aftersex1 = "/cayenne/[cayenne.stage]/home_aftersex1.webp"
        scene cayenne_home_aftersex1
        "Collapsing from the exertion, you cuddle up with Cayenne on the bed. Eventually you recover enough stamina to get up and head back home."
        stop music fadeout 1.0
        $ daytime += 1
        jump freetime
    elif rng == 2:
        #Cayenne Choice 2) Cayenne on all fours while she eats from a box of donuts (Available after stage 7 event)
        cayenne "I think I have some room for dessert. Go grab the box of donuts in the kitchen and bring it here. This little piggy needs a treat for her reward."
        image cayenne_home_sex5 = "/cayenne/[cayenne.stage]/home_sex5.webp"
        scene cayenne_home_sex5
        $ stuffed = 0
        "Placing the open box in front of her, you approach Cayenne from behind as she begins to eat."
        if cayenne.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/7/home_sex5_video1.webm" loop
            show movie with dissolve
            "Shoving your cock into her womanhood doesn’t stop her feeding session, even as you proceed to slide in and out of her."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/7/home_sex5_video2.webm" loop
            show movie with dissolve
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/7/home_sex5_video3.webm" loop
            show movie with dissolve
        if cayenne.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/8/home_sex5_video1.webm" loop
            show movie with dissolve
            "Shoving your cock into her womanhood doesn’t stop her feeding session, even as you proceed to slide in and out of her."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/8/home_sex5_video2.webm" loop
            show movie with dissolve
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/8/home_sex5_video3.webm" loop
            show movie with dissolve
        if cayenne.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/9/home_sex5_video1.webm" loop
            show movie with dissolve
            "Shoving your cock into her womanhood doesn’t stop her feeding session, even as you proceed to slide in and out of her."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/9/home_sex5_video2.webm" loop
            show movie with dissolve
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/9/home_sex5_video3.webm" loop
            show movie with dissolve
        if cayenne.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/10/home_sex5_video1.webm" loop
            show movie with dissolve
            "Shoving your cock into her womanhood doesn’t stop her feeding session, even as you proceed to slide in and out of her."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/10/home_sex5_video2.webm" loop
            show movie with dissolve
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/10/home_sex5_video3.webm" loop
            show movie with dissolve
        if cayenne.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/11/home_sex5_video1.webm" loop
            show movie with dissolve
            "Shoving your cock into her womanhood doesn’t stop her feeding session, even as you proceed to slide in and out of her."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/11/home_sex5_video2.webm" loop
            show movie with dissolve
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/11/home_sex5_video3.webm" loop
            show movie with dissolve
        window hide
        pause
        "The only thing that brings her rapid chewing to an end is an orgasmic cry just as she finishes off the last donut."
        stop movie
        image cayenne_home_sex6 = "/cayenne/[cayenne.stage]/home_sex6.webp"
        scene cayenne_home_sex6
        window hide
        pause
        image cayenne_home_aftersex6 = "/cayenne/[cayenne.stage]/home_aftersex6.webp"
        scene cayenne_home_aftersex6
        cayenne "Mmm, I am one pleased piggy."
        "Cleaning up the aftermath and getting dressed, you leave Cayenne to digest her extra serving of food."
        stop music fadeout 1.0
        $ daytime += 1
        jump freetime
    elif rng == 4:
        #Cayenne Choice 3) Shower sex (Available after stage 8 event)
        cayenne "Come with me to the bathroom. I think I need a thorough cleaning."
        $ stuffed = 0
        "Letting Cayenne take the lead, you undress and join her in the shower."
        #IMAGE/ANIMATION: The player standing behind Cayenne as he scrubs her body.
        cayenne "Make sure you don’t miss a single spot."
        "Heeding her command, you make sure you slide your hands across every inch of her body."
        "From her breasts to her belly folds, you don’t leave a single spot untouched."
        "Just as you’re about to reach for her backside, she takes the reigns to reward you for your work."
        #IMAGE/ANIMATION: The player having sex with Cayenne from behind.”
        "Providing sufficient attention to Cayenne, she proceeds to slide your member between her ass cheeks."
        "Pushing your cock into her waiting womanhood, she starts you off with a shake of her hips."
        "Following her lead, you grab hold of her waist and begin to jolt forward."
        "Giving her everything she desires and then some, she eventually bring both of you to orgasm."
        #IMAGE: The player and Cayenne embracing each other in the shower.
        "You spend the rest of your time cleaning up before you have to go back home for the night."
        stop music fadeout 1.0
        $ daytime += 1
        jump freetime
    elif rng == 3:
        #Cayenne Choice 4) Cayenne on her bed with her on top (Available after the stage 9 event)
        cayenne "Mind carrying me over to my bed? I need to save my energy for the position I have in mind."
        "Helping her up off the couch, you make your way to the bedroom and undress before joining her on the mattress."
        image cayenne_home_sex3 = "/cayenne/[cayenne.stage]/home_sex3.webp"
        scene cayenne_home_sex3
        $ stuffed = 0
        "Spreading you out on the bed, she climbs on top of you to slide your member into her waiting womanhood."
        if cayenne.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/9/home_sex3_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/10/home_sex3_video.webm" loop
            show movie with dissolve
        elif cayenne.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/11/home_sex3_video.webm" loop
            show movie with dissolve
        window hide
        pause
        "Beginning to move her hips, your ears are treated to the sound of her moans coinciding with the constant slaps of her belly with each repetition."
        "Holding onto her arms to keep her stable allows her to move faster and faster."
        "The room echoes with your combined moans as you eventually fill her trembling womanhood with your seed."
        stop movie
        image cayenne_home_sex4 = "/cayenne/[cayenne.stage]/home_sex4.webp"
        scene cayenne_home_sex4
        "Exhausted from the effort and earlier stuffing session, Cayenne falls back onto you."
        "For a while the two of you just lay there to enjoy each other’s company. Eventually you part from one another to get dressed and then you head out."
        stop music fadeout 1.0
        $ daytime += 1
        jump freetime
