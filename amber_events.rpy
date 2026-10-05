##AMBER EVENTS
label Amber_Stage_0_Event:
    ##Text message ###
    "You receive a message on your phone from Marie."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Marie', dialogue=dialogue_one)
    $ msg ("Hello [playername].", who=1)
    pause
    $ msg ("It’s Marie again, we have another slow day if you want to pop in again?", who=1)
    pause
    $ msg ("Sure, I'll be there in a minute.")
    pause
    $ msg ("Great, see you soon.", who=1)
    pause
    $ hide_messenger()

    ###Bunny bites###
    image amber_stage_0_event_1 = "/amber/events/stage0/1.webp"
    scene amber_stage_0_event_1
    play music "/music/bb_amber.ogg" if_changed
    "Walking in it seems pretty quiet today."
    ###Marie in her usual non-work clothes.###
    image amber_stage_0_event_2 = "/amber/events/stage0/2.webp"
    scene amber_stage_0_event_2
    marie "[playername], thank you for coming."
    pc "No problem, everything ok?"
    image amber_stage_0_event_3 = "/amber/events/stage0/3.webp"
    scene amber_stage_0_event_3
    marie "Oh yeah, sorry I am just heading out to run some errands while we are quiet."
    marie "But don't worry, I am leaving you in the incredibly capable hands of Amber."
    ##Amber appears in uniform ###
    image amber_stage_0_event_4 = "/amber/events/stage0/4.webp"
    scene amber_stage_0_event_4
    amber "Hi."
    pc "Hey, Amber good to see you again."
    image amber_stage_0_event_5 = "/amber/events/stage0/5.webp"
    scene amber_stage_0_event_5
    marie "Great, you two have fun and I’ll be back before the evening shift."
    amber "See you later Marie."
    image amber_stage_0_event_6 = "/amber/events/stage0/6.webp"
    scene amber_stage_0_event_6
    "Leaving you both to it, you are left in the quiet and now slightly awkward restaurant."
    pc "So…"
    image amber_stage_0_event_7 = "/amber/events/stage0/7.webp"
    scene amber_stage_0_event_7
    amber "Yeah sorry, I’ll be honest you are the first person I have had to train here."
    pc "Oh ok, well don't feel nervous. Marie showed me a lot of what I need to do last time."
    amber "I’m sure I am supposed to be the one telling you that."
    amber "But that is good to know, why don't we have a quick runthrough of what you did last time."
    pc "Sure thing."
    image amber_stage_0_event_8 = "/amber/events/stage0/8.webp"
    scene amber_stage_0_event_8
    "Moving over to the till you try to remember everything Marie told you before."
    amber "Looks like you have gotten the hang of it."
    amber "Another tip is that the items are ordered from most ordered to least ordered, top to bottom."
    amber "As you can see burgers are at the very top along with fries and soda."
    pc "That makes a lot of sense."
    amber "Marie set it up and it is super useful."
    amber "Also, this button here takes you to another menu of some of our meal deals or we sometimes have food challenges on."
    amber "You can find them here, along with the staff discount."
    pc "Staff discount?"
    image amber_stage_0_event_9 = "/amber/events/stage0/9.webp"
    scene amber_stage_0_event_9
    amber "Marie didn’t tell you?"
    amber "We have a pretty substantial discount here, I think it’s why the three of us come here so often."
    amber "We can even have free meals sometimes."
    pc "That sounds like a great perk of working here."
    image amber_stage_0_event_10 = "/amber/events/stage0/10.webp"
    scene amber_stage_0_event_10
    amber "It is, sometimes too good."
    pc "Too good?"
    image amber_stage_0_event_11 = "/amber/events/stage0/11.webp"
    scene amber_stage_0_event_11
    amber "Oh, don't worry about that."
    "Hearing the door enter a customer has come in."
    ###Thinking it's the librarian? - so doesn't matter when people start this chain of events since she doesn't gain###
    image amber_stage_0_event_12 = "/amber/events/stage0/12.webp"
    scene amber_stage_0_event_12
    amber "Perfect, why don't you have a go at ringing up your first customer."
    amber "I’ll be right here if you struggle with anything."
    image cafe_librarian_talk = "/librarian/cafe_talk.webp"
    scene cafe_librarian_talk
    pc "Hello and welcome to Bunny Bites, can I take your order please?"
    customer "Can I get a slice of pizza and a drink please?"
    pc "Sure thing, what size drink would you like?"
    customer "Regular please."
    pc "Would you like anything else?"
    customer "No, I think that is everything."
    "With Marie’s and Ambers help it is easy to find the right buttons on the till."
    pc "Great, please take a seat and your food will be right out."
    customer "Thanks."
    image amber_stage_0_event_13 = "/amber/events/stage0/13.webp"
    scene amber_stage_0_event_13
    amber "You’re a natural."
    pc "Thanks."
    image amber_stage_0_event_14 = "/amber/events/stage0/14.webp"
    scene amber_stage_0_event_14
    amber "Now, it isn’t just the till you will have to deal with."
    amber "Other tasks include cleaning up, taking plates from customers tables and just keeping everything flowing."
    amber "Sometimes customers will even ask for things while you are out on the floor doing other jobs, so it's important to be able to multitask."
    amber "But I think that will do for today, I expect things will pick up again soon."
    pc "Are you sure, I am happy to stick around if you need it?"
    image amber_stage_0_event_15 = "/amber/events/stage0/15.webp"
    scene amber_stage_0_event_15
    amber "That’s great, but I think we have it covered for today."
    amber "I appreciate the offer though."
    pc "No problem, see you around Amber."
    amber "Bye."
    if recollection == False:
        $ money += 10
        "You earned ten dollars."
        $ daytime += 1
        $ worked_today = 1
    $ amberstage0event = 0
    stop music fadeout 1.0
    return


label Amber_Stage_1_Event_1:
    ## Amber 1.1 lunch break ##
    #### While working a regular shift ###
    ###Amber appear holding two plates with burgers ###
    image amber_stage_1_event_1 = "/amber/events/stage1/1.webp"
    scene amber_stage_1_event_1
    play music "/music/bb_amber.ogg" if_changed
    amber "Hey."
    amber "Seems like we don't have many customers, want to take a quick break with me?"
    pc "That would be great."
    amber "Why don’t we grab a table, get off our feet for a change."

    ###Sit in a booth with her###
    image amber_stage_1_event_2 = "/amber/events/stage1/2.webp"
    scene amber_stage_1_event_2
    amber "I know things have been a bit hectic around here since you started."
    amber "But you have been doing great, and taken a lot off our plate, so to speak."
    pc "No problem, I should be thanking you for the job."
    pc "Although, I got the impression you usually only hire women."
    image amber_stage_1_event_3 = "/amber/events/stage1/3.webp"
    scene amber_stage_1_event_3
    amber "Not always, but we have kind of got a reputation around town given our outfits."
    amber "In the past we have had some applicants from guys that just want to stare at us all day instead of working."
    pc "Well, I hope I have been pulling my weight around here and haven’t given you that sort of opinion of myself."
    image amber_stage_1_event_4 = "/amber/events/stage1/4.webp"
    scene amber_stage_1_event_4
    amber "No not at all, in fact some of us were wondering if you were into women at all."
    amber "But then Lisa said you had been flirting with one of the customers."
    pc "Oh, sorry."
    image amber_stage_1_event_5 = "/amber/events/stage1/5.webp"
    scene amber_stage_1_event_5
    amber "No, you don't need to apologise."
    amber "It is totally fine, and between you and me, tips from flirting is how I paid off my student debt."
    amber "As long as it's only a little flirting and doesn’t impact the work, I don't see why we can't have a little fun."
    image amber_stage_1_event_6 = "/amber/events/stage1/6.webp"
    scene amber_stage_1_event_6
    "Meeting your eyes for a moment, there is a bit of an awkward pause in the conversation."
    image amber_stage_1_event_7 = "/amber/events/stage1/7.webp"
    scene amber_stage_1_event_7
    "Amber looks away from you with a slight blush on her face."
    image amber_stage_1_event_8 = "/amber/events/stage1/8.webp"
    scene amber_stage_1_event_8
    "Grabbing her burger, Amber stuffs it into her mouth as if to fill the silence."
    pc "So anyway, what did you study?"
    image amber_stage_1_event_9 = "/amber/events/stage1/9.webp"
    scene amber_stage_1_event_9
    amber "Mmm?"
    pc "You said you had student debt?"
    image amber_stage_1_event_10 = "/amber/events/stage1/10.webp"
    scene amber_stage_1_event_10
    amber "Oh right, yeah I studied fashion at the university in town."
    amber "I love making clothes, I even designed our outfits here."
    pc "Really, they look great!"
    amber "Thanks, they were super fun to design."
    amber "I didn’t originally make them this tight, but Marie insisted they were."
    amber "I guess she knew the power they would have in bringing in new customers."
    pc "Are you ok with that?"
    image amber_stage_1_event_11 = "/amber/events/stage1/11.webp"
    scene amber_stage_1_event_11
    amber "At the start I was a little embarrassed, but in a weird way it's made me more confident."
    amber "Plus, it's kind of fun and way more interesting than just wearing a shirt and jeans."
    image amber_stage_1_event_12 = "/amber/events/stage1/12.webp"
    scene amber_stage_1_event_12
    amber "What about you, what do you do for fun?"
    pc "Oh, not that much at the moment."
    pc "I have only just moved back to town and I’m still getting myself settled."
    pc "But I take some classes at your old university."
    image amber_stage_1_event_13= "/amber/events/stage1/13.webp"
    scene amber_stage_1_event_13
    amber "I didn’t realise you were new to town, makes sense why you were looking for a job."
    amber "It's a great university, the teachers are very knowledgeable and dedicated to their crafts."
    amber "At least the ones I had."
    pc "Yeah…I get that impression too."
    "Hearing the door open, a customer arrives."
    image amber_stage_1_event_14 = "/amber/events/stage1/14.webp"
    scene amber_stage_1_event_14
    amber "I guess we better get back to work."
    amber "Why don't you take their order and I will go back and wash these up."
    pc "Sure thing."
    ### Customer order and end shift / continue afterwards ####

    if recollection == True:
        stop music fadeout 1.0
    $ amberstage1event = 0
    return

label Amber_Stage_1_Event_2:
    #First Sitdown in the weekend with Amber
    image amber_idle_workattire_event = "/amber/1/idle_workattire.webp"
    scene amber_idle_workattire_event
    play music "/music/bb_amber.ogg" if_changed
    amber "Hey, do you want to hang out a bit before going home?"
    pc "Sure, that sounds great."
    image amber_afterwork_sitdown1_event = "/amber/1/afterwork_sitdown1.webp"
    scene amber_afterwork_sitdown1_event
    "Amber sits down in one of the booths."
    amber "Sure feels good to be done for the day."
    image amber_afterwork_sitdown2_event = "/amber/1/afterwork_sitdown2.webp"
    scene amber_afterwork_sitdown2_event
    amber "I still have to clean up a bit, but that's not too bad."
    amber "By the way, I never thanked you for helping us all out by taking the job here."
    image amber_afterwork_sitdown3_event = "/amber/1/afterwork_sitdown3.webp"
    scene amber_afterwork_sitdown3_event
    amber "It was way too much work for the three of us."
    amber "And...let's just say tensions were starting to run high between us."
    image amber_afterwork_sitdown4_event = "/amber/1/afterwork_sitdown4.webp"
    scene amber_afterwork_sitdown4_event
    amber "But now you're here and we're all getting along great!"
    amber "It's great being able to come to work without feeling totally drained of energy all the time."
    image amber_afterwork_sitdown5_event = "/amber/1/afterwork_sitdown5.webp"
    scene amber_afterwork_sitdown5_event
    amber "And whenever I'm feeling down, I've got you to talk to!"
    amber "I've gotta say, you're a really great listener."
    image amber_afterwork_sitdown6_event = "/amber/1/afterwork_sitdown6.webp"
    scene amber_afterwork_sitdown6_event
    amber "Anyway, that's all I wanted to say. Sorry if I made it awkward."
    pc "No, not at all! I'm glad you're happy here."
    amber "Aw, thanks. Hey, could you help me clean this place up?"
    pc "Sure!"
    "Amber and you clean up the whole place."
    image amber_afterwork_sitdown7_event = "/amber/1/afterwork_sitdown7.webp"
    scene amber_afterwork_sitdown7_event
    amber "Thanks for the help."
    amber "I'll try not to bug you with my issues in the future."
    pc "No, don't be silly. I'm always here to talk if you need to."
    amber "Well, that's good to know. Thanks. Have a good night."
    if recollection == True:
        stop music fadeout 1.0
    $ amberstage1event2 = 0
    return

label Amber_Stage_2_Event_1:
    ## Amber 2.1 Delivery issue ##
    #### During a weekend shift with Amber ###
    ###After serving a customer, Amber comes in holding a box ###
    image amber_stage_2_event_11 = "/amber/events/stage2/11.webp"
    scene amber_stage_2_event_11
    play music "/music/bb_amber.ogg" if_changed
    pc "Hey Amber, what's this?"
    amber "Not what I ordered, Marie is going to kill me."
    pc "What do you mean?"
    image amber_stage_2_event_12 = "/amber/events/stage2/12.webp"
    scene amber_stage_2_event_12
    amber "It's the weekly delivery of supplies, but something has gone wrong."
    amber "Almost nothing we ordered came and now we just have a bunch of random junk."
    image amber_stage_2_event_13 = "/amber/events/stage2/13.webp"
    scene amber_stage_2_event_13
    amber "What am I supposed to do with a box of 500 cream cakes that go off in 3 days."
    "You are sure you could think of something, but you decide not to say that."
    image amber_stage_2_event_14 = "/amber/events/stage2/14.webp"
    scene amber_stage_2_event_14
    pc "It's ok, by the sounds of it they messed it up not you. Marie will totally understand."
    pc "Besides, she and Lisa had been looking to try out some new items on the menu."
    image amber_stage_2_event_15 = "/amber/events/stage2/15.webp"
    scene amber_stage_2_event_15
    amber "Really?"
    pc "Yeah, you can't help it if someone else messes up, right?"
    amber "Thanks, you always know just what to say."
    amber "If nothing else, we can probably give away some of these things as free samples."
    pc "See, it's not so bad."
    image amber_stage_2_event_16 = "/amber/events/stage2/16.webp"
    scene amber_stage_2_event_16
    amber "Ok, I am going to call Marie. Are you ok with everything here?"
    pc "Yeah I'll be fine, don't worry."

    ###Go back to working regular shift.###
    if recollection == False:
        call work_randomizer from _call_work_randomizer_3
    ###After shift, same day Amber comes up to you after closing looking a little bloated holding some snacks (not stuff usually sold at Bunny bites) ###

    image amber_stage_2_event_17 = "/amber/events/stage2/17.webp"
    scene amber_stage_2_event_17
    amber "Hey, thanks again for your help earlier."
    amber "I guess I was just feeling a little stressed and have a lot on my mind."
    pc "Do you want to talk about it?"
    image amber_stage_2_event_18 = "/amber/events/stage2/18.webp"
    scene amber_stage_2_event_18
    amber "No!"
    "Blushing from her abruptness, it is clear it's not something she feels comfortable about just yet."
    image amber_stage_2_event_19 = "/amber/events/stage2/19.webp"
    scene amber_stage_2_event_19
    amber "But thank you, and good news with the delivery."
    amber "Marie phoned them up and the correct items should be arriving tomorrow so we won't be without food for the customers."
    amber "She also liked the idea of us giving out this stuff as free samples, and even better than that, said we could all eat as much of it as we want."
    image amber_stage_2_event_20 = "/amber/events/stage2/20.webp"
    scene amber_stage_2_event_20
    amber "Those cream cakes are lovely and whatever these are, are also pretty good."
    "From the look on her face and her straining outfit, it seems Amber has already been helping herself to the free supplies."
    pc "I'll have to try them sometime."
    amber "Better be quick, I know Lisa is going to love these as well."
    image amber_stage_2_event_21 = "/amber/events/stage2/21.webp"
    scene amber_stage_2_event_21
    amber "Anyway, I'll go tidy up out back if you are good in here?"
    pc "Yeah sure."
    "Cleaning up the restaurant, you head home for the night."
    if recollection == False:
        $ money += 10
        "You earned ten dollars."
        $ amber.weight += 0.2
    else:
        stop music fadeout 1.0
    $ amberstage2event = 0
    return


label Amber_Stage_2_Event_2:
    #Amber ask you if you want to go with her for drink to the bar after working in the weekend.
    #You agree and you meet up at the bar, you realize the bar is a stripclub which surprises you.
    #Amber tells you that she feels safe her because the owner is a good friend of hers and whenever she had men bothering her she got help here from all the ladies.
    #You talk a bit more about work before going home

    #Unlocks repeatable bar visits where she drink a lot of sweet drinks that make her gain weight
    ###Scene 2: Stripclubbar (Meeting Amber)###
    image amber_idle_workattire_event2 = "/amber/2/idle_workattire.webp"
    scene amber_idle_workattire_event2
    play music "/music/bb_amber.ogg" if_changed
    amber "Hey, do you mind staying for a little bit? I want to talk to you about something."
    pc "For sure."
    image amber_afterwork_sitdown1_event2 = "/amber/2/afterwork_sitdown1.webp"
    scene amber_afterwork_sitdown1_event2
    "Amber sits down in one of the booths."
    amber "Ahhh, another day done."
    image amber_afterwork_sitdown2_event2 = "/amber/2/afterwork_sitdown2.webp"
    scene amber_afterwork_sitdown2_event2
    amber "Just need to clean up a lil bit, shouldn't be too bad."
    pc "So, what did you want to talk to me about?"
    image amber_afterwork_sitdown3_event2 = "/amber/2/afterwork_sitdown3.webp"
    scene amber_afterwork_sitdown3_event2
    amber "Well, I was wondering if you'd like to go out for a drink after we finish closing up?"
    pc "That sounds great. Did you have a place in mind?"
    image amber_afterwork_sitdown4_event2 = "/amber/2/afterwork_sitdown4.webp"
    scene amber_afterwork_sitdown4_event2
    amber "Yeah. It's a bar not far from here that I think you'll like. My friend works there. If she's on tonight, maybe I'll introduce you."
    image amber_afterwork_sitdown5_event2 = "/amber/2/afterwork_sitdown5.webp"
    scene amber_afterwork_sitdown5_event2
    pc "It's a date, then."
    image amber_afterwork_sitdown6_event2 = "/amber/2/afterwork_sitdown6.webp"
    scene amber_afterwork_sitdown6_event2
    amber "Well, let's get this place cleaned up first."
    pc "Of course."
    "Amber and you clean up the whole place."
    image amber_afterwork_sitdown7_event2 = "/amber/2/afterwork_sitdown7.webp"
    scene amber_afterwork_sitdown7_event2
    amber "Alright, meet me at the bar in an hour."
    pc "See you there."
    stop music fadeout 1.0

    image amber_stage_2_event_1 = "/amber/events/stage2/1.webp"
    scene amber_stage_2_event_1
    play music "/music/stripclub.ogg" if_changed
    amber "Hey! I like that shirt you're wearing!"
    pc "Hey, Amber, and uhhh thanks. You know, this doesn't look like a regular bar..."
    image amber_stage_2_event_2 = "/amber/events/stage2/2.webp"
    scene amber_stage_2_event_2
    "Amber laughs and then gives you a playful tap on the shoulder."
    amber "Well, what does it look like to you?"
    pc "Well, judging by the naked woman dancing on that pole, I'd say it was a sports bar."
    image amber_stage_2_event_3 = "/amber/events/stage2/3.webp"
    scene amber_stage_2_event_3
    amber "Oh, veeery funny. Well, this may surprise you, but it's actually a strip club. Welcome to Velvet Shadows!"
    pc "I have heard about this place at the university... I got this card. I guess I can finally find out what the deal with it is."
    pc "Drinks?"
    "You and Amber walk over to the bar and wait for service. A half naked bartender turns to face the two of you."
    image amber_stage_2_event_4 = "/amber/events/stage2/4.webp"
    scene amber_stage_2_event_4
    bartender "So, what can I get for you two?"
    pc "Ladies first."
    image amber_stage_2_event_5 = "/amber/events/stage2/5.webp"
    scene amber_stage_2_event_5
    amber "Uhh, since when did you become such a charming gentleman?"
    pc "What do you mean? People are always talking about how much of a gentle soul I am."
    "Amber rolls her eyes."
    image amber_stage_2_event_6 = "/amber/events/stage2/6.webp"
    scene amber_stage_2_event_6
    amber "Get me a cosmopolitan. It's been a long day."
    bartender "And how about you, handsome?"
    pc "I'll have a lager, please."
    bartender "Coming right up!"
    image amber_stage_2_event_7 = "/amber/events/stage2/7.webp"
    scene amber_stage_2_event_7
    "As the bartender turns around to make Amber's cocktail, your eyes can't help but linger on her curvaceous ass."
    image amber_stage_2_event_8 = "/amber/events/stage2/8.webp"
    scene amber_stage_2_event_8
    amber "Enjoying the show?"
    pc "Err, sorry, Amber. I don't know what came over me."
    image amber_stage_2_event_9 = "/amber/events/stage2/9.webp"
    scene amber_stage_2_event_9
    amber "Don't worry, I don't mind a little competition."
    amber "Wait til you meet my friend, I don't think she's here today, but she kind of runs this place and she's goddamn gorgeous."
    pc "How do you know each other?"
    image amber_stage_2_event_10 = "/amber/events/stage2/10.webp"
    scene amber_stage_2_event_10
    amber "Well, I've known her for many years and she's always been there for me."
    amber "She's especially good at dealing with creeps, so that's sort of what started our friendship."
    amber "And it's not just me, she's helped tons of other women who are going through hardships. She's a great woman."
    pc "She certainly sounds like one, I can't wait to meet her."
    image amber_stage_2_event_22 = "/amber/events/stage2/22.webp"
    scene amber_stage_2_event_22
    "The conversation shifts topic and you talk about work and life in general, while drinking your cold beer."
    image amber_stage_2_event_23 = "/amber/events/stage2/23.webp"
    scene amber_stage_2_event_23
    amber "Thanks for the cocktail, tough guy."
    "Amber says with a playful smile as she gives you a kiss on the cheek and walks out of the stripclub."
    stop music fadeout 1.0

    $ amberstage2event2 = 0
    return

label Amber_Stage_3_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Amber', dialogue=dialogue_one)
    $ msg ("Heyyy. So, I was wondering if you wanted to hang out today?", who=1)
    pause
    $ msg ("There's this great cafe near my place.", who=1)
    menu:
        "Hang out with Amber.":
            $ msg ("Yeah, sure. When do you want to meet?")
            pause
            $ msg ("If you're not busy then how about right now?", who=1)
            pause
            $ msg ("That works for me. See you then!")
            pause
            $ hide_messenger()
        "Do something else.":
            $ msg ("Maybe another time, I'm quite busy today.")
            pause
            $ msg ("No worries, talk to you later.", who=1)
            pause
            $ hide_messenger()
            return

    image amber_stage_3_event_1 = "/amber/events/stage3/1.webp"
    scene amber_stage_3_event_1
    "You head over to the café. When you get there, Amber is admiring the selection of pastries on offer."
    "She snaps out of her doughnut daydream when she notices you."
    image amber_stage_3_event_2 = "/amber/events/stage3/2.webp"
    scene amber_stage_3_event_2
    amber "Oh, hey! I was just looking at these doughnuts..."
    pc "Yeah, they look pretty tasty."
    amber "Tell me about it. I wish I could have some."
    pc "Well, what's stopping you?"
    image amber_stage_3_event_3 = "/amber/events/stage3/3.webp"
    scene amber_stage_3_event_3
    amber "I don't know. I feel like maybe I need to cut back on the junk food."
    pc "Don't be silly. You shouldn't deprive yourself of things that make you happy."
    amber "You think so?"
    pc "For sure! Get whatever you like. I'm buying!"
    image amber_stage_3_event_4 = "/amber/events/stage3/4.webp"
    scene amber_stage_3_event_4
    "Amber looks up at you and smiles. She's blushing a little bit."
    amber "... Oh, what the hell. You're right. You only live once!"
    image amber_stage_3_event_5 = "/amber/events/stage3/5.webp"
    scene amber_stage_3_event_5
    "She orders a large platter of pastries and a large coffee. You notice that she's quite generous with the coffee cream as well."
    "When it's your turn to order, you're only hungry for maybe a couple of doughnuts, but you've got an idea..."
    pc "I'll have what she's having, please."
    image amber_stage_3_event_6 = "/amber/events/stage3/6.webp"
    scene amber_stage_3_event_6
    "The two of you find a table and you watch her chow down on her pastries as you nibble at your own platter, enjoying a few pastries but leaving most of them untouched."
    image amber_stage_3_event_7 = "/amber/events/stage3/7.webp"
    scene amber_stage_3_event_7
    amber "Mmmph. Thanks for talking me into ordering all of these. They're delicious, URP!"
    pc "They sure are..."
    image amber_stage_3_event_8 = "/amber/events/stage3/8.webp"
    scene amber_stage_3_event_8
    "Soon enough Amber's plate is empty and she's licking her fingers clean of any frosting. More than satisfied she lets out an..."
    image amber_stage_3_event_9 = "/amber/events/stage3/9.webp"
    scene amber_stage_3_event_9
    amber "HOOOOOURRRRRRRRP"
    image amber_stage_3_event_10 = "/amber/events/stage3/10.webp"
    scene amber_stage_3_event_10
    amber "Wow, excuse me. That was really really good. How did you like your-"
    image amber_stage_3_event_11 = "/amber/events/stage3/11.webp"
    scene amber_stage_3_event_11
    "Amber stops talking as she sees your platter of doughnuts, basically untouched save for the two or three that you ate."
    image amber_stage_3_event_12 = "/amber/events/stage3/12.webp"
    scene amber_stage_3_event_12
    "She looks at you, slightly embarrassed."
    amber "Ummm, are you gonna finish those?"
    pc "No. Why? Do you want them?"
    amber "Maybe..."
    pc "Sure, go ahead!"
    image amber_stage_3_event_13 = "/amber/events/stage3/13.webp"
    scene amber_stage_3_event_13
    "Amber gives you a greedy grin as she brings your plate over to her side of the table and digs in."
    image amber_stage_3_event_14 = "/amber/events/stage3/14.webp"
    scene amber_stage_3_event_14
    "So she ate..."
    image amber_stage_3_event_15 = "/amber/events/stage3/15.webp"
    scene amber_stage_3_event_15
    "And ate..."
    image amber_stage_3_event_16 = "/amber/events/stage3/16.webp"
    scene amber_stage_3_event_16
    "And ate some more."
    image amber_stage_3_event_17 = "/amber/events/stage3/17.webp"
    scene amber_stage_3_event_17
    "Finally, she leaned back into her seat with a satisfied look on her face."
    image amber_stage_3_event_18 = "/amber/events/stage3/18.webp"
    scene amber_stage_3_event_18
    amber "W-wow, I never thought I could *hic!* eat that much. It felt good though."
    image amber_stage_3_event_19 = "/amber/events/stage3/19.webp"
    scene amber_stage_3_event_19
    "As she looks at you, the realization of what she's just done seems to dawn on her as she looks embarrassed."
    amber "Ummm, I should go. It was nice seeing you!"
    image amber_stage_3_event_20 = "/amber/events/stage3/20.webp"
    scene amber_stage_3_event_20
    "Without another word said she gets up and leaves."
    pc "Well, that was interesting..."
    if recollection == False:
        $ amber.weight += 0.5
        $ daytime += 1
        $ phonecall = 1
    $ amberstage3event = 0
    return

label Amber_Stage_4_Event:
    image amber_stage_4_event_1 = "/amber/events/stage4/1.webp"
    scene amber_stage_4_event_1
    play music "/music/bb_amber.ogg" if_changed
    "Two hours into luchtime, service seems to have slowed down to a crawl."
    "People aren't getting their food and a couple of customers have complained to you."
    image amber_stage_4_event_2 = "/amber/events/stage4/2.webp"
    scene amber_stage_4_event_2
    "You apologize and go talk to Amber to find out what's going on. But then you realize you don't see her anywhere."
    pc "Huh, that's weird."
    image amber_stage_4_event_3 = "/amber/events/stage4/3.webp"
    scene amber_stage_4_event_3
    "You go check the back. She's not in the restroom or the breakroom."
    "Finally, you check the storage room."
    image amber_stage_4_event_4 = "/amber/events/stage4/4.webp"
    scene amber_stage_4_event_4
    "And there she is, chowing down on two burgers without a care in the world. She doesn't even notice you come in."
    pc "Man, she is really going to town on those burgers..."
    "You cough to get her attention."
    image amber_stage_4_event_5 = "/amber/events/stage4/5.webp"
    scene amber_stage_4_event_5
    "She looks up at you, eyes wide as she's clearly surprised and a little embarrassed to have been caught like this."
    image amber_stage_4_event_6 = "/amber/events/stage4/6.webp"
    scene amber_stage_4_event_6
    amber "Oh, hey [playername]. I was just-UUUUURP-having some lunch."
    pc "Uhhh, Amber, you realize you're still on shift, right? People have been waiting for their food for a while now..."
    image amber_stage_4_event_7 = "/amber/events/stage4/7.webp"
    scene amber_stage_4_event_7
    "Amber stands up, a look of shock on her face as it turns beet red."
    amber "Gosh, I'm so sorry! I just can't seem to h-hic!-help myself lately."
    "She runs out without another word and gets back to work."
    "The rest of your shift goes by without incident and before you know it, you're closing up."
    image amber_stage_4_event_8 = "/amber/events/stage4/8.webp"
    scene amber_stage_4_event_8
    "As you mop the floor, you see Amber sitting at one of the booths on the phone. She seems upset."
    amber "Yeah...too much...maybe...diet..."
    "You can't make out what she's saying."
    image amber_stage_4_event_9 = "/amber/events/stage4/9.webp"
    scene amber_stage_4_event_9
    "Then she stops talking for a while, just listening to the person on the other end of the line. She seems cheered up as she allows herself a smile."
    amber "Alright, thanks for the talk. Bye bye."
    image amber_stage_4_event_10 = "/amber/events/stage4/10.webp"
    scene amber_stage_4_event_10
    "She gets up and walks towards you."
    image amber_stage_4_event_11 = "/amber/events/stage4/11.webp"
    scene amber_stage_4_event_11
    amber "That was Maya. I was telling her that after what happened today I think I should go on a diet. I'm really sorry about that, by the way."
    pc "Nah, don't worry about it. So, are you going to?"
    image amber_stage_4_event_12 = "/amber/events/stage4/12.webp"
    scene amber_stage_4_event_12
    amber "Am I gonna what?"
    pc "Go on a diet."
    image amber_stage_4_event_13 = "/amber/events/stage4/13.webp"
    scene amber_stage_4_event_13
    amber "Oh, no. She talked me out of it. Said I shouldn't stop myself from doing things I enjoy."
    pc "Well, I've gotta say that I agree."
    image amber_stage_4_event_14 = "/amber/events/stage4/14.webp"
    scene amber_stage_4_event_14
    amber "Yeah? Even after what happened today?"
    pc "Totally. I don't have a problem with you eating on the job, as long as you're actually working."
    pc "And if you're ever hungry on shift, just come see me at the counter and I'll get you something. You don't need to hide in the storage room haha."
    image amber_stage_4_event_15 = "/amber/events/stage4/15.webp"
    scene amber_stage_4_event_15
    "Amber smiles at you. Your support clearly means a lot to her."
    amber "Thanks, [playername]..."
    image amber_stage_4_event_16 = "/amber/events/stage4/16.webp"
    scene amber_stage_4_event_16
    amber "Our customers sometimes leave complete and untouched meals. Would you be so kind as to give those to me while we are working together?"
    amber "Working here always makes me hungry and it's such a waste to throw those perfectly good meals in the bin."
    pc "Sure, I will keep an eye out."
    amber "Thank you."
    image amber_stage_4_event_17 = "/amber/events/stage4/17.webp"
    scene amber_stage_4_event_17
    amber "Well, I better get going. Have a good night!"
    pc "You too, thanks!"
    "Once you've finished closing up, you head home."
    stop music fadeout 1.0
    if recollection == False:
        $ money += 10
        "You earned ten dollars."
        $ amber.weight += 2
    $ amberstage4event = 0
    return

label Amber_Stage_5_Event_1:
    ###Amber check in event###
    image amber_stage_5_event_1 = "/amber/events/stage5/1.webp"
    scene amber_stage_5_event_1
    play music "/music/bb_amber.ogg" if_changed
    "During a lull in the customers, you decide to check out the stock room."
    image amber_stage_5_event_2 = "/amber/events/stage5/2.webp"
    scene amber_stage_5_event_2
    "Walking in you find Amber doing a stock take, or more accurately eating the stock."
    image amber_stage_5_event_3 = "/amber/events/stage5/3.webp"
    scene amber_stage_5_event_3
    "Looking slightly surprised she quickly drops whatever she was about to eat back into the box."
    amber "[playername], sorry you surprised me."
    pc "Sorry, didn't mean to make you jump."
    pc "How are we looking for supplies?"
    image amber_stage_5_event_4 = "/amber/events/stage5/4.webp"
    scene amber_stage_5_event_4
    amber "I think we should have enough until the next supply shipment arrives next week."
    "Now alone with her, you realise now might be the best time to check in on her for Marie."
    image amber_stage_5_event_5 = "/amber/events/stage5/5.webp"
    scene amber_stage_5_event_5
    amber "Did you need anything from here?"
    pc "I was just going to do a stock take, seems you have beaten me to it."
    amber "Yeah, the early bird gets the worm."
    "Or looking around the room, the cookies, cakes and left overs."
    image amber_stage_5_event_6 = "/amber/events/stage5/6.webp"
    scene amber_stage_5_event_6
    "Shuffling awkwardly Amber clearly notices you looking around at her empty snacking pile."
    amber "Sorry, I got a bit hungry when I was in here."
    pc "You don't have to apologise to me, as long as the customers have enough you can eat as much as you want."
    amber "Thanks, you and Marie have been so kind to me about it."
    pc "It?"
    image amber_stage_5_event_7 = "/amber/events/stage5/7.webp"
    scene amber_stage_5_event_7
    amber "My, uh…weight gain."
    pc "Oh, that's ok."
    pc "But if you don't mind me asking, is everything ok?"
    amber "What do you mean?"
    pc "I mean, sometimes people can use eating as a coping mechanism and I just wanted to check you were doing ok."
    pc "I mean it's been a pretty recent change, hasn't it?"
    image amber_stage_5_event_8 = "/amber/events/stage5/8.webp"
    scene amber_stage_5_event_8
    amber "Oh, that's sweet. I don't know how I got so lucky with all you guys."
    amber "But yeah everythings…fine…"
    image amber_stage_5_event_9 = "/amber/events/stage5/9.webp"
    scene amber_stage_5_event_9
    "Despite the comment you can tell she is hiding something."
    pc "Are you sure, you know you can talk to me about anything."
    image amber_stage_5_event_10 = "/amber/events/stage5/10.webp"
    scene amber_stage_5_event_10
    amber "I know, but I just don't know if it's …too much."
    pc "You don't have to worry about that, if there is anything I can help you with I'd love too."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage5/vid1.webm" loop
    show movie with dissolve
    amber "I don't know…ok, just please don't judge me."
    amber "I've kind of been…inspired by some of the customers."
    pc "Inspired?"
    amber "I'm sure I can't be the only one noticing several of the regulars are getting bigger."
    amber "Even Marie and Lisa have gained weight."
    pc "So seeing everyone else grow made you want to gain weight?"
    amber "I have kind of always wanted too, it…excited me."
    stop movie
    image amber_stage_5_event_11 = "/amber/events/stage5/11.webp"
    scene amber_stage_5_event_11
    "Blushing deeply Amber stares at the floor."
    amber "Oh, this is so embarrassing."
    image amber_stage_5_event_12 = "/amber/events/stage5/12.webp"
    scene amber_stage_5_event_12
    amber "You must think I am so weird."
    pc "Not at all, I don't think it's as rare around here as you might think."
    image amber_stage_5_event_13 = "/amber/events/stage5/13.webp"
    scene amber_stage_5_event_13
    amber "Really?"
    pc "Yeah, but what made you want to gain now?"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage5/vid2.webm" loop
    show movie with dissolve
    amber "I just saw everyone else growing and no one seemed to notice or care."
    amber "I always thought it would ruin my life if I gave in and did it, but then everyone else was fine."
    amber "It didn't seem to change how anyone treated those who had gotten bigger."
    amber "So I figured I could maybe do it a little bit and see."
    stop movie
    image amber_stage_5_event_14 = "/amber/events/stage5/14.webp"
    scene amber_stage_5_event_14
    "Grabbing her belly, she looks down with a new fondness."
    amber "But I guess I got a bit carried away and now look at me, so big and round."
    image amber_stage_5_event_15 = "/amber/events/stage5/15.webp"
    scene amber_stage_5_event_15
    amber "I just couldn't help myself. It felt so good to give in and just eat as much as I could."
    amber "Sorry, this is probably way too much information."
    pc "No, actually I like it too."
    image amber_stage_5_event_16 = "/amber/events/stage5/16.webp"
    scene amber_stage_5_event_16
    amber "You are just saying that, look at you. You are all skin and bone."
    pc "No, I mean I like it when women get bigger."
    image amber_stage_5_event_17 = "/amber/events/stage5/17.webp"
    scene amber_stage_5_event_17
    amber "Oh…is that why you started accepting my offers to go out drinking?"
    pc "It didn’t hurt."
    image amber_stage_5_event_18 = "/amber/events/stage5/18.webp"
    scene amber_stage_5_event_18
    amber "Really, you like this too!"
    "It's clear Amber is excited to have found a kindred spirit."
    pc "Guilty as charged."
    image amber_stage_5_event_19 = "/amber/events/stage5/19.webp"
    scene amber_stage_5_event_19
    amber "This is so amazing, I always felt like a bit of a weirdo."
    amber "No offence."
    pc "No offence taken, I am just glad you are happy."
    image amber_stage_5_event_20 = "/amber/events/stage5/20.webp"
    scene amber_stage_5_event_20
    amber "I am, and even more so now."
    amber "It feels so nice to have someone to talk to about this."
    amber "It has been fun sneaking around, but it also felt a little dishonest."
    amber "I am worried I was taking advantage of Marie by eating so much, and you by making you do the extra work while I have been in here."
    pc "I don't mind and I am positive Marie doesn't either."
    amber "Thank you, it means so much you came to speak to me about it."
    image amber_stage_5_event_21 = "/amber/events/stage5/21.webp"
    scene amber_stage_5_event_21
    amber "Although one of us should probably get back out there before the customers leave."
    amber "I’ll just finish up here."
    pc "Ok sure, let me know if you need anything."
    image amber_stage_5_event_22 = "/amber/events/stage5/22.webp"
    scene amber_stage_5_event_22
    amber "Will do."
    amber "Thanks [playername]."

    ##Serve a customer and shift ends.###
    if recollection == False:
        $ amber.weight += 1
    else:
        stop music fadeout 1.0
    $ amberstage5event = 0
    return

label Amber_Stage_5_Event_2:
    ## Amber 5.2 - Mall underwear shopping event. ##
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Amber', dialogue=dialogue_one)
    $ msg ("Hey, I know this might be a little strange.", who=1)
    pause
    $ msg ("But I wasn’t sure who else to ask, would you want to go shopping with me at the mall?", who=1)
    pause
    $ msg ("I need some new underwear.", who=1)
    pause
    $ msg ("You want me to go underwear shopping with you?")
    pause
    $ msg ("You don't have to, I could just use a second opinion.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sure, I’ll get ready and meet you there.")
            pause
            $ msg ("See you soon.", who=1)
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Sorry, kinda busy today.")
            pause
            $ msg ("No problem, maybe some other time.", who=1)
            pause
            $ hide_messenger()
            return

    "Grabbing your keys, you head out to the mall to meet Amber."
    image amber_stage_5_event_23 = "/amber/events/stage5/23.webp"
    scene amber_stage_5_event_23
    "When arriving to the mall, you see Amber waiting for you in front of the building."
    ###Mall entrance ###
    image amber_stage_5_event_24 = "/amber/events/stage5/24.webp"
    scene amber_stage_5_event_24
    amber "Hey, thanks for coming."
    pc "No problem, although I am a little surprised you asked me."
    amber "Honestly, I was planning on coming with Maya but her boss cancelled her time off."
    pc "What about Lisa or Marie?"
    amber "I don't know if I am ready to talk to them about this yet."
    pc "This?"
    image amber_stage_5_event_25 = "/amber/events/stage5/25.webp"
    scene amber_stage_5_event_25
    amber "This."
    image amber_stage_5_event_26 = "/amber/events/stage5/26.webp"
    scene amber_stage_5_event_26
    "Grabbing her belly, it's clear what she means."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage5/vid3.webm" loop
    show movie with dissolve
    amber "You are kind of the only one I have told about it."
    amber "Although, I’m sure they have all noticed the extra weight I have put on."
    amber "But I don't know how to deal with any awkward questions they might have."
    amber "It was kind of easier with you, because we haven’t really been friends for that long. No offence."
    pc "Don't worry, I get it. I am sure they would all be supportive as well though."
    amber "I know you are right, I'm just working up the courage to tell them."
    pc "Ok, so what is the plan?"
    stop movie
    image amber_stage_5_event_27 = "/amber/events/stage5/27.webp"
    scene amber_stage_5_event_27
    amber "I was at the cafe in town and saw an advert for a plus size store here I thought I would check out."
    amber "But I wanted some company, and a second opinion couldn’t hurt."
    pc "And you are comfortable with it being me?"
    image amber_stage_5_event_28 = "/amber/events/stage5/28.webp"
    scene amber_stage_5_event_28
    amber "Why wouldn’t I be?"
    pc "I don't know, just doesn't seem like an activity many people would bring a guy to if they weren’t dating them."
    image amber_stage_5_event_29 = "/amber/events/stage5/29.webp"
    scene amber_stage_5_event_29
    amber "Oh, I guess I didn’t really think about it too much."
    amber "I just know you won't be judgemental and I always feel super comfortable talking to you."
    image amber_stage_5_event_30 = "/amber/events/stage5/30.webp"
    scene amber_stage_5_event_30
    amber "Sorry if that makes things awkward."
    pc "It doesn’t, I am happy to help."
    image amber_stage_5_event_31 = "/amber/events/stage5/31.webp"
    scene amber_stage_5_event_31
    amber "Great, thanks."
    amber "I think it's over here."

    ####Clothing store###
    image amber_stage_5_event_32 = "/amber/events/stage5/32.webp"
    scene amber_stage_5_event_32
    play music "/music/clothingstore.ogg" if_changed
    amber "These look nice, what do you think?"
    pc "I uh…they look fine."
    amber "Yeah, you’re right. It's hard to tell without putting them on."
    image amber_stage_5_event_33 = "/amber/events/stage5/33.webp"
    scene amber_stage_5_event_33
    amber "I think the changing rooms are over there."
    image amber_stage_5_event_34 = "/amber/events/stage5/34.webp"
    scene amber_stage_5_event_34
    amber "Wait here, I’ll be right out."
    image amber_stage_5_event_35 = "/amber/events/stage5/35.webp"
    scene amber_stage_5_event_35
    "Awkwardly standing around as Amber changes, you are kind of glad no one else is here."
    image amber_stage_5_event_36 = "/amber/events/stage5/36.webp"
    scene amber_stage_5_event_36
    amber "Is the coast clear?"
    pc "There is no one around if that’s what you mean."
    amber "Great."
    image amber_stage_5_event_37 = "/amber/events/stage5/37.webp"
    scene amber_stage_5_event_37
    amber "Now what do you think?"
    pc "You look…they look great."
    image amber_stage_5_event_38 = "/amber/events/stage5/38.webp"
    scene amber_stage_5_event_38
    amber "Right, and they are pretty comfortable too."
    amber "Not too tight and pretty stretchy which is good."
    image amber_stage_5_event_39 = "/amber/events/stage5/39.webp"
    scene amber_stage_5_event_39
    "Modelling her new underwear, you do your best not to stare too hard as you admire her body."
    amber "Next!"
    image amber_stage_5_event_40 = "/amber/events/stage5/40.webp"
    scene amber_stage_5_event_40
    "Disappearing back into the changing room, she emerges in a new set."
    image amber_stage_5_event_41 = "/amber/events/stage5/41.webp"
    scene amber_stage_5_event_41
    window hide
    pause
    image amber_stage_5_event_42 = "/amber/events/stage5/42.webp"
    scene amber_stage_5_event_42
    amber "This bra is incredible, it’s so supportive and doesn’t pinch me at all."
    image amber_stage_5_event_43 = "/amber/events/stage5/43.webp"
    scene amber_stage_5_event_43
    "Grabbing her breasts, she pushes them together. Was she doing this on purpose?"
    amber "What do you think, do you like them?"
    pc "Looks very…supportive."
    amber "And you should feel how soft it is."
    image amber_stage_5_event_44 = "/amber/events/stage5/44.webp"
    scene amber_stage_5_event_44
    "Moving closer, Amber takes your hand and places it onto her chest."
    pc "Yeah, it feels good."
    "Blushing, Amber clearly enjoys the attention as you gently stroke her breasts."
    $ unknownname = 'Shopkeeper'
    unknown "Everything ok over there."
    image amber_stage_5_event_45 = "/amber/events/stage5/45.webp"
    scene amber_stage_5_event_45
    amber "Shit."
    image amber_stage_5_event_46 = "/amber/events/stage5/46.webp"
    scene amber_stage_5_event_46
    "Grabbing you, she pulls you into the changing room with her."
    image amber_stage_5_event_47 = "/amber/events/stage5/47.webp"
    scene amber_stage_5_event_47
    "But losing your footing, you fall onto the floor with Amber landing on top of you."
    image amber_stage_5_event_48 = "/amber/events/stage5/48.webp"
    scene amber_stage_5_event_48
    amber "Yeah, I’m fine."
    unknown"Well let me know if you need anything dearie."
    image amber_stage_5_event_49 = "/amber/events/stage5/49.webp"
    scene amber_stage_5_event_49
    "As you lay there, you can feel Amber’s almost naked body pressing down on you, your faces close together."
    image amber_stage_5_event_50 = "/amber/events/stage5/50.webp"
    scene amber_stage_5_event_50
    $ unknownname = 'Unknown'
    "The rush of excitement of almost being caught causing both your hearts to race, you can feel her chest rising and falling."
    image amber_stage_5_event_51 = "/amber/events/stage5/51.webp"
    scene amber_stage_5_event_51
    "Staring at each other in silence for a few moments, Amber leans in and kisses you."
    image amber_stage_5_event_52 = "/amber/events/stage5/52.webp"
    scene amber_stage_5_event_52
    amber "Maybe I did have ulterior motives for inviting you today."
    pc "I’m not complaining."
    image amber_stage_5_event_53 = "/amber/events/stage5/53.webp"
    scene amber_stage_5_event_53
    amber "So you like me?"
    pc "I do, but I got the impression you just wanted to be friends?"
    amber "Can’t a girl change her mind?"
    image amber_stage_5_event_54 = "/amber/events/stage5/54.webp"
    scene amber_stage_5_event_54
    amber "Anyway, I am feeling pretty hungry."
    image amber_stage_5_event_55 = "/amber/events/stage5/55.webp"
    scene amber_stage_5_event_55
    amber "Let me get changed and we can find somewhere to eat if you want too."
    image amber_stage_5_event_56 = "/amber/events/stage5/56.webp"
    scene amber_stage_5_event_56
    "Buying her new outfits, you head out to find somewhere to eat."
    stop music fadeout 1.0

    ###Mall restaurant / cafeteria###
    image amber_stage_5_event_57 = "/amber/events/stage5/57.webp"
    scene amber_stage_5_event_57
    amber "This place looks good."
    pc "Can’t say I have ever eaten here before."
    amber "Me either, these days I just get most of my food at work."
    image amber_stage_5_event_58 = "/amber/events/stage5/58.webp"
    scene amber_stage_5_event_58
    waitress "How can I help?"
    amber "Hi, can I get two of your belly burster burritos."
    image amber_stage_5_event_59 = "/amber/events/stage5/59.webp"
    scene amber_stage_5_event_59
    amber "With an extra large lemonade, some fries and ooh that pizza smells great so can I get two slices of that."
    "It’s clear the server is surprised by the amount of food but places the order without saying anything."
    "Ordering your food, you help Amber carry her feast to a table and sit down."
    image amber_stage_5_event_60 = "/amber/events/stage5/60.webp"
    scene amber_stage_5_event_60
    pc "That’s a lot of food."
    amber "I know."
    image amber_stage_5_event_61 = "/amber/events/stage5/61.webp"
    scene amber_stage_5_event_61
    "Smiling back at you, Amber digs into one of the large burritos."
    image amber_stage_5_event_62 = "/amber/events/stage5/62.webp"
    scene amber_stage_5_event_62
    amber "Mmm, this is so good. Maybe I should have ordered three."
    pc "Do you think you could even eat three?"
    image amber_stage_5_event_63 = "/amber/events/stage5/63.webp"
    scene amber_stage_5_event_63
    amber "Mmm, I don't know but it would be fun to find out."
    amber "Fun for both of us, if you were telling the truth the other day."
    pc "I absolutely was."
    image amber_stage_5_event_64 = "/amber/events/stage5/64.webp"
    scene amber_stage_5_event_64
    "Biting into her burrito she is making steady work on the thing."
    image amber_stage_5_event_65 = "/amber/events/stage5/65.webp"
    scene amber_stage_5_event_65
    amber "I’m glad you caught me, and that I even had enough courage to invite you today after Maya couldn’t make it."
    pc "Me too."
    pc "Can I ask, how do you know her?"
    amber "She is a friend, she helped me out when I really needed it."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage5/vid4.webm" loop
    show movie with dissolve
    amber "My ex used to take me to her club so that I would be forced to watch him getting lap dances from all the women there."
    amber "I think he liked the thought of me being jealous, or that he was trying to make me feel like I was nothing to him."
    pc "Sounds like a jerk."
    amber "Yeah, but he was hot and I was stupidly naive. A tale as old as time."
    amber "Thankfully Maya could tell I really wasn’t happy with it."
    amber "She slipped me a card for the place and said I should come back on my own sometime."
    amber "I don't know what made me, but I am glad I went to see her."
    amber "She helped me realise that I wasn’t happy and that being in the wrong relationship was worse than not being in one at all."
    pc "Sounds like good advice and a good friend."
    amber "She is almost like a sister to me now."
    amber "After she gave me the courage to break up with him, I realised that all my friends were really his friends."
    amber "So I ended up spending a lot of time with Maya at the club, or at Bunny bites."
    stop movie
    image amber_stage_5_event_66 = "/amber/events/stage5/66.webp"
    scene amber_stage_5_event_66
    "Pausing for a moment, she takes a sip of her drink."
    amber "Do you really like me?"
    image amber_stage_5_event_67 = "/amber/events/stage5/67.webp"
    scene amber_stage_5_event_67
    "The question catches you off guard as Amber takes another big bite, her eyes watching you."
    pc "I do, is that ok?"
    image amber_stage_5_event_68 = "/amber/events/stage5/68.webp"
    scene amber_stage_5_event_68
    amber "Obviously, I kissed you, remember?"
    amber "I was just worried I had put you on the spot while I was literally on top of you."
    amber "Which was also kind of fun, all that time in the gym has been paying off for you."
    pc "Thanks, but I kind of guess you have been enjoying the opposite."
    image amber_stage_5_event_69 = "/amber/events/stage5/69.webp"
    scene amber_stage_5_event_69
    amber "Are you calling me fat?"
    pc "I…uh…"
    image amber_stage_5_event_70 = "/amber/events/stage5/70.webp"
    scene amber_stage_5_event_70
    amber "Because please do, although I am far too skinny still. Don't you agree?"
    pc "I think you look good now, but it would be hot to see you even bigger."
    amber "As you wish, or maybe more correctly as we wish."
    image amber_stage_5_event_71 = "/amber/events/stage5/71.webp"
    scene amber_stage_5_event_71
    "Taking another bite Amber finishes off the first of the giant burritos, her stomach already looking much rounder than it had before."
    image amber_stage_5_event_72 = "/amber/events/stage5/72.webp"
    scene amber_stage_5_event_72
    amber "Oooh, that was bigger than I expected. I don’t know if I have room for any more."
    amber "Do I really have to eat it?"
    "You can tell from her playful attitude that it’s very much what she wants."
    pc "We wouldn’t want to waste any food would we?"
    image amber_stage_5_event_73 = "/amber/events/stage5/73.webp"
    scene amber_stage_5_event_73
    "Smiling, Amber is happy to see you play along before remembering to seem upset about that information."
    image amber_stage_5_event_74 = "/amber/events/stage5/74.webp"
    scene amber_stage_5_event_74
    "Taking a hearty bite, Amber winks back at you to confirm your suspicions."
    "This was a new side of Amber you hadn’t seen before, but maybe it had always been there."
    image amber_stage_5_event_75 = "/amber/events/stage5/75.webp"
    scene amber_stage_5_event_75
    "Barely saying another word, you each stare at each other as Amber devours the rest of her meal."
    image amber_stage_5_event_76 = "/amber/events/stage5/76.webp"
    scene amber_stage_5_event_76
    "Her clothes and stomach stretching to accommodate the accurately named Belly burster."
    image amber_stage_5_event_77 = "/amber/events/stage5/77.webp"
    scene amber_stage_5_event_77
    window hide
    pause
    image amber_stage_5_event_78 = "/amber/events/stage5/78.webp"
    scene amber_stage_5_event_78
    "With a final groan, Amber finishes off her food. Looking rather more round than she had earlier."
    amber "Oh god, this feels good and bad at the same time."
    pc "Sure you wouldn’t like another burrito, you did say you might?"
    image amber_stage_5_event_79 = "/amber/events/stage5/79.webp"
    scene amber_stage_5_event_79
    amber "Please no.."
    amber "Besides, I have other plans for when we get back that I would like to still be able to move for."
    image amber_stage_5_event_80 = "/amber/events/stage5/80.webp"
    scene amber_stage_5_event_80
    amber "Which speaking of, how about we head back to mine?"
    pc "If you can even move."
    amber "Mmm, don't even tease me with sentences like that."
    amber "I’ve already worked myself up enough, stuffing myself stupid."
    image amber_stage_5_event_81 = "/amber/events/stage5/81.webp"
    scene amber_stage_5_event_81
    "Helping Amber to her feet you follow her back to her place as somewhat of a slower pace than usual."

    ###Ambers place.###
    image amber_stage_5_event_82 = "/amber/events/stage5/82.webp"
    scene amber_stage_5_event_82
    amber "Make yourself at home, I’ll be right back."
    image amber_stage_5_event_83 = "/amber/events/stage5/83.webp"
    scene amber_stage_5_event_83
    "Grabbing a seat on the couch, you wait for Amber."
    image amber_stage_5_event_84 = "/amber/events/stage5/84.webp"
    scene amber_stage_5_event_84
    "A couple of minutes later she comes back out dressed in her new underwear."
    "They look a lot tighter than they did in the shop."
    image amber_stage_5_event_85 = "/amber/events/stage5/85.webp"
    scene amber_stage_5_event_85
    amber "Now what do you really think?"
    pc "I think you look amazing."
    amber "Really, well I think there is only one problem."
    image amber_stage_5_event_86 = "/amber/events/stage5/86.webp"
    scene amber_stage_5_event_86
    "Walking over to you, she gently lowers herself until she is sitting on your lap facing you."
    image amber_stage_5_event_87 = "/amber/events/stage5/87.webp"
    scene amber_stage_5_event_87
    "Her heavy bloated belly pressing on your lap as she wraps her arms around you."
    image amber_stage_5_event_88 = "/amber/events/stage5/88.webp"
    scene amber_stage_5_event_88
    amber "You are wearing far too many clothes."
    pc "I…before we go any further I feel like I should say that I’m seeing other people too."
    image amber_stage_5_event_89 = "/amber/events/stage5/89.webp"
    scene amber_stage_5_event_89
    amber "So?"
    pc "After what you said about your ex, I thought you were only interested in monogamy or didn’t like the fact he was with other women?"
    image amber_stage_5_event_90 = "/amber/events/stage5/90.webp"
    scene amber_stage_5_event_90
    amber "No, It wasn’t that he was into other women, it was that he wanted me to be jealous."
    amber "He was manipulating me, making me feel like nothing to him."
    amber "But I know that’s not true with you."
    image amber_stage_5_event_91 = "/amber/events/stage5/91.webp"
    scene amber_stage_5_event_91
    amber "You actually listen to me, help me out when I need it, and spend time to make sure I’m ok."
    amber "You have already given me more than he ever did."
    pc "So you are ok with it?"
    amber "As long as there is enough of you to go around, absolutely."
    image amber_stage_5_event_92 = "/amber/events/stage5/92.webp"
    scene amber_stage_5_event_92
    amber "But now I want you to feed me!"
    amber "I want you to force me to eat, force me to get bigger and bigger."
    amber "I want you to feed me so much even my new clothes don't fit me any more."
    image amber_stage_5_event_93 = "/amber/events/stage5/93.webp"
    scene amber_stage_5_event_93
    amber "I want you to ruin my body, have me grow so much so fast that my belly is covered in stretchmarks."
    image amber_stage_5_event_94 = "/amber/events/stage5/94.webp"
    scene amber_stage_5_event_94
    amber "And then I want you to fuck me."
    image amber_stage_5_event_96 = "/amber/events/stage5/96.webp"
    scene amber_stage_5_event_96
    "Holding up a bag of sweets, it seems she is as into this idea as you are."
    image amber_stage_5_event_97 = "/amber/events/stage5/97.webp"
    scene amber_stage_5_event_97
    "Standing up, Amber replaces you on the sofa."
    image amber_stage_5_event_98 = "/amber/events/stage5/98.webp"
    scene amber_stage_5_event_98
    "Grabbing the first sweet treat you place it into her mouth and she eats it obediently."
    amber "Mmm, more please."
    image amber_stage_5_event_99 = "/amber/events/stage5/99.webp"
    scene amber_stage_5_event_99
    "Rubbing her bloated stomach you feed her another."
    image amber_stage_5_event_100 = "/amber/events/stage5/100.webp"
    scene amber_stage_5_event_100
    "Gently rubbing her straining belly, you feed her the rest of the treats, Amber moaning with each one you force into her greedy mouth."
    image amber_stage_5_event_101 = "/amber/events/stage5/101.webp"
    scene amber_stage_5_event_101
    "After feeding her all the sweets you rub and lift her huge belly with both hands."
    "Looking closely it looks like her skin is starting to form marks from the rapid growth she has experienced."
    image amber_stage_5_event_102 = "/amber/events/stage5/102.webp"
    scene amber_stage_5_event_102
    amber "Looks like I’ve eaten everything."
    pc "Looks that way."
    amber "I’m so full, but I want more."
    amber "But I guess I’ll settle for something else."
    image amber_stage_5_event_103 = "/amber/events/stage5/103.webp"
    scene amber_stage_5_event_103
    "As she takes of her bra, you take off your own clothes."
    image amber_stage_5_event_104 = "/amber/events/stage5/104.webp"
    scene amber_stage_5_event_104
    window hide
    pause
    if persistent.nosexscene == True:
        scene black
        "You and Amber had a wonderful time together."
        image amber_stage_5_event_111 = "/amber/events/stage5/111.webp"
        scene amber_stage_5_event_111
        "It wasn’t what you had imagined would happen today, but you were not complaining."
        if amberundressoption == 0:
            $ amberundressoption = 1
            #Unlocks Amber Undress in the stats page.
            $ renpy.notify("Amber Undress option unlocked in stats screen.")
            window hide
            pause
        if recollection == False:
            $ amber.weight += 1
            $ daytime = 4
            $ phonecall = 1
        $ amberstage5event2 = 0
        return
    image amber_stage_5_event_105 = "/amber/events/stage5/105.webp"
    scene amber_stage_5_event_105
    "Laying down on the sofa, Amber climbs on top, moaning in delight as you enter her."
    image amber_stage_5_event_106 = "/amber/events/stage5/106.webp"
    scene amber_stage_5_event_106
    amber "Fuck me, that feels good."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage5/sex1.webm" loop
    show movie with dissolve
    "Starting off gentle, you let her do a lot of the work while enjoying the sight of her giant belly bouncing up and down on you."
    amber "Oh yeah, talk dirty to me."
    pc "Talk dirty to you?"
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage5/sex2.webm" loop
    show movie with dissolve
    amber "You know what I want."
    amber "Am I a greedy pig."
    pc "The biggest greedy pig."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage5/sex3.webm" loop
    show movie with dissolve
    amber "Oh yeah, am I your best, fattest, most obedient pig."
    amber "Are you going to force me to eat another burrito, making me eat even when I say I can't fit any more inside me."
    amber "I want you to make me as big as a whale, never stop feeding me."
    amber "Feed me till I explode."
    "It's clear Amber’s fantasy is driving her wild."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage5/sex4.webm" loop
    show movie with dissolve
    amber "Oh fuck yeah, keep going."
    "Grabbing onto her, you manoeuvre yourself around to give you more control."
    "Quickening your thrusts, Amber moans deeply."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage5/sex5.webm" loop
    show movie with dissolve
    amber "I don't want to be able to walk."
    amber "I want to be your fat blob, to be fed more and more and more every day."
    pc "Yeah, is that what you want, to become so big you can't even leave the house."
    amber "Fuck yes!"
    pc "To only exist to eat and grow."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage5/sex6.webm" loop
    show movie with dissolve
    amber "Yes, yes yes!"
    "Screaming out in pleasure, you feel Amber orgasm with you still inside her."
    stop movie
    $ renpy.movie_cutscene("/images/amber/events/stage5/sex7.webm", stop_music=False)
    image amber_stage_5_event_107 = "/amber/events/stage5/107.webp"
    scene amber_stage_5_event_107
    "The contractions of her body sending you over the edge as you cum inside her."
    image amber_stage_5_event_108 = "/amber/events/stage5/108.webp"
    scene amber_stage_5_event_108
    "Collapsing onto the sofa a sweaty mess, Amber smiles weakly back up at you."
    amber "Wow."
    pc "That was amazing."
    image amber_stage_5_event_109 = "/amber/events/stage5/109.webp"
    scene amber_stage_5_event_109
    amber "I don't think I can move, my brain has melted."
    amber "Holy shit, that felt a million times better than the last time I had sex."
    amber "Seriously, my head is floating."
    pc "Are you going to be ok?"
    image amber_stage_5_event_110 = "/amber/events/stage5/110.webp"
    scene amber_stage_5_event_110
    amber "Ok? I’m perfect, you’re perfect."
    "Taking a few minutes to enjoy the moment, you chat for a little bit before leaving Amber and heading home."
    image amber_stage_5_event_111 = "/amber/events/stage5/111.webp"
    scene amber_stage_5_event_111
    "It wasn’t what you had imagined would happen today, but you were not complaining."
    if amberundressoption == 0:
        $ amberundressoption = 1
        #Unlocks Amber Undress in the stats page.
        $ renpy.notify("Amber Undress option unlocked in stats screen.")
        window hide
        pause

    scene player_room
    "Later that night you receive a message from Amber."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Amber', dialogue=dialogue_one)
    $ msg ("Today was so fun, thanks for being there for me.", who=1)
    pause
    $ msg ("No need to thank me, I had fun too.")
    pause
    $ msg ("I'd love to do it again sometime, if you want?")
    pause
    $ msg ("Are you kidding me, I absolutely want to do it again.", who=1)
    pause
    $ msg ("I'd do it every day if I could.", who=1)
    pause
    $ msg ("Want me to come over tomorrow?")
    pause
    $ msg ("Sadly, I am busy tomorrow.", who=1)
    pause
    $ msg ("But here is something to keep you going till next time.", who=1)
    pause
    $ msg (None, who=1, pic="stage5_amber")
    pause
    $ hide_messenger()

    if recollection == False:
        $ amber.weight += 1
        $ daytime = 4
        $ phonecall = 1
    $ amberstage5event2 = 0
    return


label Amber_Stage_6_Event:
    ###Amber stage 6###
    ##After working a late shift with Amber####
    image amber_idle_workattire_stage6 = "/amber/6/idle_workattire.webp"
    scene amber_idle_workattire_stage6
    amber "Hey, wanna join me for drinks tonight?"
    menu:
        "Join her.":
            amber "Great, I’ll just go get changed."
        "Go home.":
            amber "Another time then."
            return

    ##Club###
    scene stripclub
    play music "/music/stripclub.ogg" if_changed
    "Arriving at the club, you go to the bar to get a drink."
    image amber_stage_6_event_1 = "/amber/events/stage6/1.webp"
    scene amber_stage_6_event_1
    amber "Mmm, I should have eaten before we came out."
    pc "Feeling hungry?"
    amber "Not exactly."
    amber "Let’s grab our drinks and find somewhere to chat."
    image amber_stage_6_event_2 = "/amber/events/stage6/2.webp"
    scene amber_stage_6_event_2
    "Grabbing your beers, Amber leads you to a more secluded area."
    image amber_stage_6_event_3 = "/amber/events/stage6/3.webp"
    scene amber_stage_6_event_3
    pc "So how have you been?"
    amber "Good, really good actually."
    amber "Do you… happen to notice anything new?"
    pc "You changed your hair?"
    image amber_stage_6_event_4 = "/amber/events/stage6/4.webp"
    scene amber_stage_6_event_4
    amber "I'm fat!"
    amber "Look at me, my belly rolls, my thighs."
    image amber_stage_6_event_5 = "/amber/events/stage6/5.webp"
    scene amber_stage_6_event_5
    amber "I’ve eaten myself out of shape and almost outgrown my entire wardrobe."
    amber "It is so hot to see what I have done to myself."
    image amber_stage_6_event_6 = "/amber/events/stage6/6.webp"
    scene amber_stage_6_event_6
    pc "Sounds like you have been enjoying it."
    image amber_stage_6_event_7 = "/amber/events/stage6/7.webp"
    scene amber_stage_6_event_7
    amber "I have, but…have you?"
    pc "I’d be lying if I said I hadn’t."
    pc "Watching you gain and eat at work is kind of a tease, in the best way possible."
    image amber_stage_6_event_8 = "/amber/events/stage6/8.webp"
    scene amber_stage_6_event_8
    amber "Does it turn you on to see me stuff myself to my limit?"
    pc "It does."
    image amber_stage_6_event_9 = "/amber/events/stage6/9.webp"
    scene amber_stage_6_event_9
    amber "Good, because it turns me on too."
    amber "Especially if I have an audience, one who knows what I am doing to myself."
    image amber_stage_6_event_10 = "/amber/events/stage6/10.webp"
    scene amber_stage_6_event_10
    amber "Although, I’ve been kind of wondering where we stand?"
    pc "What do you mean?"
    amber "I mean us, like what are we relationship wise?"
    image amber_stage_6_event_11 = "/amber/events/stage6/11.webp"
    scene amber_stage_6_event_11
    pc "Oh, umm…"
    image amber_stage_6_event_12 = "/amber/events/stage6/12.webp"
    scene amber_stage_6_event_12
    amber "Don't worry, I know there are others in your life and I don't want to be exclusive with you."
    amber "Like I know you and Marie have a thing right, plus some of the customers seem really familiar with you."
    amber "But with this shared interest, I like working with you and being friends outside of our…other activities."
    pc "I love spending time with you too, honestly I am happy to be whatever you want."
    pc "Just friends, friends with benefits or more."
    image amber_stage_6_event_13 = "/amber/events/stage6/13.webp"
    scene amber_stage_6_event_13
    amber "I definitely don't want to be just friends, I don't think friends get to be stuffed by their just friends."
    amber "That sounds good though, keeping things casual."
    pc "Can I ask what brought these questions on?"
    image amber_stage_6_event_14 = "/amber/events/stage6/14.webp"
    scene amber_stage_6_event_14
    amber "I’ve just been feeling super confident lately."
    amber "I don't know if it’s from the weight gain or just the kind of confidence that’s come from being completely sexually open with someone."
    amber "It’s made me feel like maybe I want more."
    pc "More out of our relationship?"
    image amber_stage_6_event_15 = "/amber/events/stage6/15.webp"
    scene amber_stage_6_event_15
    amber "I meant more relationships, although I wouldn’t say no to more of us."
    pc "I wouldn’t be upset with more of us either, or more specifically more of you."
    ##Amber blushing##
    image amber_stage_6_event_16 = "/amber/events/stage6/16.webp"
    scene amber_stage_6_event_16
    amber "Shut up."
    amber "But thank you."
    pc "So have you got your eyes on someone else?"
    image amber_stage_6_event_17 = "/amber/events/stage6/17.webp"
    scene amber_stage_6_event_17
    amber "Not right now, but there is this guy in my gym who loves to watch me do pushups."
    pc "Really."
    amber "Yeah, although he’s kind of a weirdo. Keeps turning up where I work too."
    amber "He even came here, but all he could talk about was how much he loved to see me gain weight."
    pc "Very funny, but you were the one who brought it up, remember."
    amber "True."
    image amber_stage_6_event_18 = "/amber/events/stage6/18.webp"
    scene amber_stage_6_event_18
    amber "Would you want to maybe, head back to my place and keep the fun going?"
    pc "Absolutely!"
    image amber_stage_6_event_19 = "/amber/events/stage6/19.webp"
    scene amber_stage_6_event_19
    "Downing whatever was left in your drinks, you go back to Amber's apartment with her."
    stop music fadeout 1.0

    ##Ambers apartment##
    image amber_stage_6_event_20 = "/amber/events/stage6/20.webp"
    scene amber_stage_6_event_20
    amber "Make yourself comfortable, I will be right back."
    pc "Sure thing."
    image amber_stage_6_event_21 = "/amber/events/stage6/21.webp"
    scene amber_stage_6_event_21
    "Sitting on the couch, you wonder what Amber could have planned."
    image amber_stage_6_event_22 = "/amber/events/stage6/22.webp"
    scene amber_stage_6_event_22
    "A few minutes later it becomes clear as Amber returns, with a big cake."
    amber "I thought we could have some extra fun tonight, since we both know what we are in for."
    image amber_stage_6_event_23 = "/amber/events/stage6/23.webp"
    scene amber_stage_6_event_23
    "Lying down on the sofa Amber picks up the first slice of cake, licking the cream from the top she eyes you seductively."
    image amber_stage_6_event_24 = "/amber/events/stage6/24.webp"
    scene amber_stage_6_event_24
    "Walking over you grab another piece of cake and hold it up to her mouth."
    amber "Mmm, I knew this was a good idea."
    image amber_stage_6_event_25 = "/amber/events/stage6/25.webp"
    scene amber_stage_6_event_25
    "Biting down on the slice, you can tell how much she enjoys it as she moans with her full mouth."
    image amber_stage_6_event_26 = "/amber/events/stage6/26.webp"
    scene amber_stage_6_event_26
    amber "More, make me your little piggy."
    pc "I’ll make you my big piggy."
    amber "Mmm, even better."
    image amber_stage_6_event_27 = "/amber/events/stage6/27.webp"
    scene amber_stage_6_event_27
    "Grabbing another piece you push it towards her empty mouth."
    image amber_stage_6_event_28 = "/amber/events/stage6/28.webp"
    scene amber_stage_6_event_28
    "Despite her best efforts it's too big and you make quite the mess of her face as she greedily accepts the newest slice."
    image amber_stage_6_event_29 = "/amber/events/stage6/29.webp"
    scene amber_stage_6_event_29
    "You force her to keep eating, bite after bite, slice after slice."
    image amber_stage_6_event_30 = "/amber/events/stage6/30.webp"
    scene amber_stage_6_event_30
    amber "Mmm, starting to get full."
    pc "But there is so much left, you wouldn’t want it to go stale."
    image amber_stage_6_event_31 = "/amber/events/stage6/31.webp"
    scene amber_stage_6_event_31
    amber "Do you want me to eat it all?"
    pc "I think it would be a waste not to."
    image amber_stage_6_event_32 = "/amber/events/stage6/32.webp"
    scene amber_stage_6_event_32
    "Amber takes off her panties and cradles her bulging belly."
    amber "Well, I wouldn’t want to disappoint you."
    amber "Do as you want with me, I know I can eat it and satisfy you with my hunger."
    "You start to get the feeling that Amber enjoys playing the role of a helpless sub to you."
    pc "In that case, you should keep eating!"
    image amber_stage_6_event_33 = "/amber/events/stage6/33.webp"
    scene amber_stage_6_event_33
    "Holding up another cake Amber smiles as you get her game and force her to keep eating."
    image amber_stage_6_event_34 = "/amber/events/stage6/34.webp"
    scene amber_stage_6_event_34
    "With a fiery passion, Amber keeps munching on the cake you push into her face."
    image amber_stage_6_event_35 = "/amber/events/stage6/35.webp"
    scene amber_stage_6_event_35
    amber "Mmmm, getting really full now."
    image amber_stage_6_event_36 = "/amber/events/stage6/36.webp"
    scene amber_stage_6_event_36
    pc "I know what might help."
    image amber_stage_6_event_37 = "/amber/events/stage6/37.webp"
    scene amber_stage_6_event_37
    "Taking a momentary break you start to rub her bloated belly, hoping to make her feel better."
    amber "Mmm, that feels good."
    image amber_stage_6_event_38 = "/amber/events/stage6/38.webp"
    scene amber_stage_6_event_38
    "Only giving her a momentary break you decide to change positions."
    "Getting up on the sofa, you straddle her giant mound of a belly."
    ###Thinking of a top down angle of you feeding her, almost riding her.###
    image amber_stage_6_event_39 = "/amber/events/stage6/39.webp"
    scene amber_stage_6_event_39
    pc "Just a few more pieces."
    "Not waiting for an answer, you take another piece and hold it in front of her to eat."
    image amber_stage_6_event_40 = "/amber/events/stage6/40.webp"
    scene amber_stage_6_event_40
    "Obediently opening her mouth you continue to stuff Amber until all the cake is gone."
    pc "Definitely a big piggy!"
    image amber_stage_6_event_41 = "/amber/events/stage6/41.webp"
    scene amber_stage_6_event_41
    amber "So full…and needy."
    image amber_stage_6_event_42 = "/amber/events/stage6/42.webp"
    scene amber_stage_6_event_42
    "Placing a hand on her taut belly, you can feel it straining under the weight of itself and all the cake Amber had just eaten."
    image amber_stage_6_event_43 = "/amber/events/stage6/43.webp"
    scene amber_stage_6_event_43
    "Her recent rapid growth giving rise to red streaks all across her massive gut."
    image amber_stage_6_event_44 = "/amber/events/stage6/44.webp"
    scene amber_stage_6_event_44
    "Beneath you, Amber moans in pleasure as she plays with her breasts and fondles her giant belly."
    image amber_stage_6_event_45 = "/amber/events/stage6/45.webp"
    scene amber_stage_6_event_45
    amber "Why do you still have clothes on?"
    if persistent.nosexscene == True:
        scene black
        "You and Amber had a wonderful time together."
        image amber_stage_6_event_47 = "/amber/events/stage6/47.webp"
        scene amber_stage_6_event_47
        amber "We should definitely do that again."
        image amber_stage_6_event_48 = "/amber/events/stage6/48.webp"
        scene amber_stage_6_event_48
        "Helping clean up the mess you had created, you excuse yourself and head home."
        if recollection == False:
            $ amber.weight += 1
            $ daytime = 4
        $ amberstage6event = 0
        return
    image amber_stage_6_event_46 = "/amber/events/stage6/46.webp"
    scene amber_stage_6_event_46
    "Taking her advice you quickly strip and reposition yourself."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage6/amber1.webm" loop
    show movie with dissolve
    "Holding her legs, you thrust inside her."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage6/amber2.webm" loop
    show movie with dissolve
    amber "Oh fuck, I feel so tight like this."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage6/amber3.webm" loop
    show movie with dissolve
    "Moving back and forth you can feel Amber moving underneath you."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage6/amber4.webm" loop
    show movie with dissolve
    "With every move you can see her mountainous belly shaking despite how full it looks."
    "You notice an increased jiggle in her thighs as you thrust back and forth."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/amber/events/stage6/amber5.webm" loop
    show movie with dissolve
    "Clearly already turned on by her feeding, Amber soon starts to moan loudly as she approaches an orgasm."
    "Picking up the pace her moans only get louder until you both climax together."
    $ renpy.movie_cutscene("/images/amber/events/stage6/amber6.webm", stop_music=False)
    stop movie
    image amber_stage_6_event_47 = "/amber/events/stage6/47.webp"
    scene amber_stage_6_event_47
    amber "Fuck, that was even better than I imagined."
    amber "We should definitely do that again."
    image amber_stage_6_event_48 = "/amber/events/stage6/48.webp"
    scene amber_stage_6_event_48
    "Helping clean up the mess you had created, you excuse yourself and head home."

    scene player_room
    "Later that night you receive a message from Amber."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Amber', dialogue=dialogue_one)
    $ msg ("Thanks for cleaning up while I was in the shower.", who=1)
    pause
    $ msg ("Although, next time you should feel free to join me in there.", who=1)
    pause
    $ msg (None, who=1, pic="stage6_amber1")
    pause
    $ msg ("Are you sure there is room?")
    pause
    $ msg ("Not for much longer if you keep feeding me like this.", who=1)
    pause
    $ msg (None, who=1, pic="stage6_amber2")
    pause
    $ msg ("But I am sure we can squeeze you in somewhere.", who=1)
    pause
    $ hide_messenger()

    if recollection == False:
        $ amber.weight += 1
        $ daytime = 4
    $ amberstage6event = 0
    return

label Amber_Stage_7_Event:
    ## Walking into Velvet shadows##
    "Walking towards the bar, you notice a familiar face."
    pc "Hey Amber, I didn't expect you to be here."
    amber "Hey, what are you doing here?"
    pc "Fancied a drink and thought I might see how Maya was doing."
    pc "What about you?"
    amber "Ogling the pretty ladies."
    amber "But seriously, I came to see Maya too but she doesn't appear to be working today."
    pc "Well, lucky we are both here then, fancy getting a drink together?"
    amber "Actually, I am kind of in the middle of something."
    amber "I was hoping to get some feedback from Maya but guess that will have to wait."
    pc "Anything I can help with?"
    amber "Maybe, although no offence your fashion choices are not exactly…interesting."
    pc "Nothing wrong with a five pack of shirts, sometimes they even do six."
    "Amber shakes her head jokingly, although it wasn't far from the truth."
    amber "I can always just ignore you and get another opinion from Maya another time."
    pc "Exactly."
    amber "They are back at my place if you want to come."
    pc "Sure."
    "Walking back to Ambers, you make small talk but she doesn't fill you in on what you are doing yet."

    ###Ambers apartment ###
    amber "Ok, go grab a seat and I will be right out."
    pc "Sure thing."
    "Making yourself comfortable, Amber returns a few minutes later carrying some outfits."
    amber "So, Marie has asked me to redesign the uniforms we wear at work."
    amber "Apparently, the old ones can't quite handle how much we have all grown."
    amber "I've had to repair Lisa's suit like 4 times this month already."
    amber "Although, I am sure you have been paying plenty of attention to that fact."
    pc "No comment…"
    amber "As I thought."
    amber "I've been able to adjust mine as I have gained and manually stretched the fabric."
    amber "But the original suit still has its limits, which I am rapidly approaching."
    "She seems lost in her own thoughts for a moment."
    amber "It was super nice of Marie to ask me instead of hiring someone else."
    amber "So I want to do a good job, but I was hoping Maya might have been able to give me an idea of which one of these I should go with."
    amber "So, what do you think?"
    "Holding up the outfits one after another, you are starting to see why you might not have been the best person to ask."
    pc "Uhhh, I am not sure."
    pc "Maybe if you put them on, I might be able to visualise them better?"
    amber "You just want to see me naked…Not that I mind, but stay focused!"
    "Getting undressed, Amber goes through each of the outfits in turn."
    "Walking around, she occasionally poses to give you a good look at her in them."
    pc "I like that second one, although how comfortable is it?"
    amber "They are all super comfortable, by design of course."
    amber "They should also manage to put up with my binges more than the current suits."
    amber "Although, I don't know that for certain."
    amber "Since you are here, maybe we could test that tonight?"

    ##Amber walks close to you##
    amber "Having all this attention on me has got me thinking all kinds of crazy things."
    "Leaning in Amber kisses you deeply."
    "Reaching up, your hands start to explore her body, feeling the soft fabric against your hands."
    amber "Mmmm, we should save this for desert."
    "Breaking off the kiss, she looks you in the eyes."
    amber "Let's order some food first, in fact I'll let you order."
    amber "Order as much as you want, for me that is."
    "Pulling out your phone, you place an order while Amber tidies away the other outfits."
    "It doesn't take long for the delivery to arrive, and pulling out the food makes you wonder if you have gone too far."
    amber "Is that all for me?"
    pc "Is that a problem?"
    amber "I don't know, I don't think I have ever eaten this much before."
    pc "Sounds like the perfect test, now why don't you take a seat?"
    "Blushing, a clearly excited amber takes your place as her demeanour switches into a far more submissive one."
    "Grabbing the first Burrito you hold it infront of her mouth."
    "Leaning in Amber bites into it obediently."
    "Behind the pliant demeanour, you can see the real hunger in her eyes."
    pc "Come on faster, you have so much food you have to eat."
    amber "Mmmm, I like it when you take charge."
    "Biting messily at the burrito she chomps through it, her mouth never empty for more than a second."
    "Keeping it up, you next hold up a burger."
    pc "Plenty more where this comes from."
    "Biting into it as you feed her, she is already making a mess of herself."
    "But judging from the look in her eyes, it was only adding to the appeal for her."
    "Continuing the food onslaught, you replace the now eaten burger with a rough handful of fries, then onion rings."
    "Forcing a handful of chicken nuggets into her mouth, she is barely able to chew but that was no reason to let up."
    pc "Come on, eat faster!"
    pc "Or do you not want to do this?"
    "Picking up her pace once again, the answer is clear?"
    "Another two burgers disappeared into her growing stomach, now starting to complain as it was forced to rapidly swell."
    amber "Ughh, I just need a minute."
    pc "Are you done, do you not want any more?"
    amber "No please, I want more."
    amber "I'll be good, please!"
    "Hearing her plead like that to be fed, was a pleasure to hear."
    pc "Good."
    "Grabbing the last of the burritos, you force the end of it into her mouth."
    "Amber is doing her best to keep going, but clearly the onslaught of food was starting to take its toll."
    pc "You are doing well, but there is plenty more for you to eat."
    amber "I'm too full."
    pc "But there is so much left, you wouldn't want to disappoint me would you?"
    amber "No."
    "Grabbing the last dozen chicken nuggets, you make her eat them one after another without a break."
    amber "My stomach is so tight."
    "Looking down, you can see why. Her midriff is several times larger than when you started."
    "But as much as she might be protesting, you can tell it was all part of her act."
    pc "I know, but this was your idea so there is no stopping now."
    amber "I can't, i'm going to burst."
    pc "I don't think that's true, you're a greedy pig who can keep eating until I tell her to stop, aren't you?"
    amber "Yes."
    "Picking up the last of the fries and onion rings you keep Amber eating."
    "More and more food being pushed into her, despite her false and erotically charged plea's for you to stop."
    amber "Please, I can't eat any more."
    pc "Are you sure?"
    pc "We don't want to waste any food do we?"
    amber "I…"
    pc "Tell me what you are."
    amber "I'm a greedy pig."
    pc "And what do greedy pigs do?"
    amber "Please don't make me eat any more."
    pc "What do greedy pigs do?"
    amber "We eat."
    pc "Exactly."
    "Holding up a fresh burger you can see the genuine hesitation on her face now."
    "But any reluctance or second thoughts were lost to the opportunity of living her wildest fantasies."
    amber "I'll be good and finish it all."
    "Picking up a heavily laden piece of the cheese pizza, you lift it to her lips."
    pc "Just a few more bites and you will be done."
    "Biting into it, her mouth chews slowly."
    pc "Maybe this will help."
    "Reaching down, you slowly rub her stomach."
    "Almost purring, she keeps eating."
    "Holding up the next slice she obediently eats at your whim."
    "But opening her legs beneath her monstrous belly, her eyes tell you what she wants."
    "Reaching down as she continues eating, your hand rubs between her legs."
    "You can already feel her wetness through the suit."
    pc "Just two more slices of pizza."
    amber "Uggh, I'm so, so full."
    "Despite the protests, as you hold up the slice of pizza she opens her mouth."
    "Chewing slowly and lazily, Amber moans through the mouthful of pizza as you continue to play with her."
    pc "Does it feel good to be this big and fat?"
    amber "Yes, please, it's so good."
    pc "Have you been a good piggy?"
    "Whimpering softly, Amber swallows another mouthful of pizza."
    amber "Mmmm, yes!"
    pc "Do you think you deserve to cum?"
    amber "Please!"
    "Picking up the pace it doesn't take much to send Amber over the edge."
    "Screaming out in pleasure, her body bucks wildly."
    "Shuddering, her face flushes bright red and she wobbles on the sofa."
    amber "Oh my god."
    amber "Fuck me, that was incredible."
    "Falling back on the sofa, she cradles her massively stuffed body."
    "Picking up the last piece you decide Amber has had enough and eat it yourself."
    amber "I have never cum like that before."
    amber "Fuck, I think I almost passed out. That was so hot."
    pc "And more good news, the suit survived."
    amber "Honestly, I couldn't care less right now."
    "Cleaning up the mess, you notice Amber disappearing into her bathroom."
    "A few moments later, she emerges holding a set of scales."
    amber "Let's see the damage shall we."
    "Stepping on the scales, you see her smile."
    amber "Uhh…do you think you can help?"
    pc "Help?"
    amber "I can't see the number, my belly is too big."
    amber "Which is an amazing feeling, I never thought I would get this big."
    if persistent.imperial:
        $ imperialweight = (leanne.weight * 2.2)
        "Leaning over you read the number [imperialweight]lbs."
    else:
        "Leaning over you read the number [amber.weight]kg."
    amber "Really!"
    amber "God, I have gained so much weight this week."
    amber "Although I guess a lot will be digested soon."
    "Slumping back onto her couch Amber yawns as she lies down."
    amber "Ughhh, but right now I feel too big and heavy to do anything other than sleep."
    amber "Thanks for tonight, it was even better than I imagined it…somehow."
    pc "I'm glad you enjoyed yourself."
    amber "I did and I can't wait to do it again."
    pc "Someone is eager, although you better watch out otherwise you will need another new outfit soon."
    amber "That's the plan."
    "Rubbing her belly, you leave Amber to sleep off her giant stuffing."
    "Seeing yourself out, you head home."
    if recollection == False:
        $ amber.weight += 1
        $ daytime = 4
    $ amberstage7event = 0
    return

label Amber_bar_new:
    play music "/music/stripclub.ogg" if_changed
    if amber.stage == 3:
        ##Stage 3##
        ###At club ###
        image amber_club1 = "/amber/[amber.stage]/club1.webp"
        scene amber_club1
        "Walking into the bar, you can see Amber smiling at you and waving you over."
        image amber_club2 = "/amber/[amber.stage]/club2.webp"
        scene amber_club2
        pc "Hey, you look great. I love your outfit."
        amber "Thanks, I like your shirt."
        pc "Not quite as flashy though."
        amber "I think it makes you look very handsome."
        image amber_club3 = "/amber/[amber.stage]/club3.webp"
        scene amber_club3
        amber "Shall we get some drinks?"
        pc "Yeah sure, I'll just have a house larger."
        amber "Really having a wild one tonight."
        pc "What can I say, I am a creature of habit."
        image amber_club4 = "/amber/[amber.stage]/club4.webp"
        scene amber_club4
        amber "I'm the same when it comes to takeaways."
        amber "I always think about ordering something new, but you can't beat a triple bacon cheese burger."
        pc "I always like the first half, but those are so big."
        pc "Plus, I feel so full and kind of gross afterwards."
        amber "I kind of like it."
        pc "What?"
        ###Amber blushing ###
        image amber_club5 = "/amber/[amber.stage]/club5.webp"
        scene amber_club5
        amber "Oh, no I just meant I like the burger."
        amber "Should we get some drinks?"
        pc "Yeah, that would be great."
        scene stripclub_order
        "Ordering some drinks, you stand and chat at the bar for a while."
        image amber_club6 = "/amber/[amber.stage]/club6.webp"
        scene amber_club6
        "It's nice to catch up with Amber away from work for a change."
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
        image amber_club7 = "/amber/[amber.stage]/club7.webp"
        scene amber_club7
        amber "I think I'll get one last beer, I'm feeling a bit full."
        pc "Sounds good to me, although I was thinking about ordering some food."
        amber "Don't tempt me…"
        pc "We have been on our feet all day, no harm in a snack right?"
        "It doesn't take much to convince Amber."
        image amber_club8 = "/amber/[amber.stage]/club8.webp"
        scene amber_club8
        "Ordering yourself a burger, Amber gets two despite saying she was feeling full."
        image amber_club9 = "/amber/[amber.stage]/club9.webp"
        scene amber_club9
        "Biting into it the slightly tipsy Amber can't help but moan a little."
        amber "These are so good."
        image amber_club10 = "/amber/[amber.stage]/club10.webp"
        scene amber_club10
        "Devouring her burgers, Amber lets out a satisfied breath."
        amber "Ok, I needed that."
        amber "But, I think I am going to call it a night."
        amber "Thanks for the fun time, it was nice to catch up!"
        pc "Yeah, I enjoyed it."
        image amber_club11 = "/amber/[amber.stage]/club11.webp"
        scene amber_club11
        amber "See ya later."
        "You return home."
        stop music fadeout 1.0
        return
    elif amber.stage == 4:
        ##Stage 4##
        ###At club ###
        image amber_club1 = "/amber/[amber.stage]/club1.webp"
        scene amber_club1
        "Walking into the bar, you can see Amber smiling at you."
        image amber_club2 = "/amber/[amber.stage]/club2.webp"
        scene amber_club2
        pc "Hey, how are you doing?"
        amber "Good thanks, feels like it's been a long day though."
        pc "Yeah, we were pretty busy today."
        amber "Those heels really dig into you after a few hours."
        pc "Yeah, I don't envy the three of you having to wear them all day."
        amber "I mean we kind of chose to wear them, but yeah they can be killer."
        image amber_club3 = "/amber/[amber.stage]/club3.webp"
        scene amber_club3
        amber "Although, it's not the only thing that has been feeling tight these days."
        pc "What do you mean?"
        amber "Oh nothing…"
        image amber_club4 = "/amber/[amber.stage]/club4.webp"
        scene amber_club4
        amber "Do you want to order?"
        pc "Yeah sure."
        scene stripclub_order
        "Ordering some drinks, you stand and chat at the bar for a while."
        image amber_club5 = "/amber/[amber.stage]/club5.webp"
        scene amber_club5
        "It's nice to catch up with Amber away from work for a change."
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
        image amber_club6 = "/amber/[amber.stage]/club6.webp"
        scene amber_club6
        #Belly 0.1
        amber "I think I've got room for one more, unless you want to order some food to go with them?"
        pc "Yeah, that sounds perfect."
        amber "Great, I'll order them."
        image amber_club7 = "/amber/[amber.stage]/club7.webp"
        scene amber_club7
        "Ordering Amber gets herself three burgers and fries despite saying she was feeling full."
        image amber_club8 = "/amber/[amber.stage]/club8.webp"
        scene amber_club8
        "Biting into it, the slightly tipsy Amber can't help but moan a little."
        amber "These are so good."
        image amber_club9 = "/amber/[amber.stage]/club9.webp"
        scene amber_club9
        #Belly 0.15
        amber "I know I shouldn't, they are so fattening."
        amber "But there is just something so satisfying about a greasy meal after drinking."
        "Staring at her burger, she seems to be really contemplating it."
        pc "Everything ok?"
        ##Amber blushing##
        image amber_club10 = "/amber/[amber.stage]/club10.webp"
        scene amber_club10
        amber "Sorry, got lost in my own thoughts for a moment."
        image amber_club11 = "/amber/[amber.stage]/club11.webp"
        scene amber_club11
        #Belly 0.25
        "Devouring her burgers, Amber lets out a satisfied breath."
        image amber_club12 = "/amber/[amber.stage]/club12.webp"
        scene amber_club12
        #Belly 0.3
        #Upper protrude 0.5
        amber "Ok, I needed that."
        amber "But, all that food has made me sleepy."
        pc "It is getting late."
        image amber_club13 = "/amber/[amber.stage]/club13.webp"
        scene amber_club13
        amber "Thanks for the fun time again."
        pc "Yeah, I enjoyed it."
        pc "It's nice to catch up and see you out of uniform."
        ###Amber blushing again.##
        image amber_club14 = "/amber/[amber.stage]/club14.webp"
        scene amber_club14
        amber "Oh…"
        pc "No sorry…I didn't mean it like that."
        amber "No it's ok…I…it's probably just the alcohol."
        image amber_club15 = "/amber/[amber.stage]/club15.webp"
        scene amber_club15
        amber "I should get going."
        pc "Yeah, see you again."
        amber "See ya later."
        "You return home."
        stop music fadeout 1.0
        return
    elif amber.stage == 5:
        ##Stage 5 - With sex if after 5.2, without if before ###
        #Belly 0.1
        image amber_club1 = "/amber/[amber.stage]/club1.webp"
        scene amber_club1
        "Walking into the bar, you can see Amber smiling at you."
        image amber_club2 = "/amber/[amber.stage]/club2.webp"
        scene amber_club2
        "A couple of empty bottles and a plate with crumbs sit next to her on the counter."
        image amber_club3 = "/amber/[amber.stage]/club3.webp"
        scene amber_club3
        pc "Hey, how are you doing?"
        amber "Good thanks, looking forward to just relaxing and letting loose a little."
        pc "Stressful day at work?"
        amber "No, it was actually pretty good."
        amber "Having you there made it more bearable."
        pc "Thanks, I got really lucky with you all didn't I."
        image amber_club4 = "/amber/[amber.stage]/club4.webp"
        scene amber_club4
        amber "What, a restaurant where the hot waitresses stuff their faces."
        amber "I bet you feel lucky."
        pc "Says the one who brought it up to me?"
        amber "I guess we are all pretty lucky."
        pc "Have you spoken to Marie and Lisa about it yet?"
        amber "Not yet, maybe tomorrow."
        image amber_club5 = "/amber/[amber.stage]/club5.webp"
        scene amber_club5
        amber "Anyway, should we get some drinks?"
        pc "Yeah sure, a house lager would be great."
        scene stripclub_order
        "Ordering some drinks, you stand and chat at the bar for a while."
        image amber_club6 = "/amber/[amber.stage]/club6.webp"
        scene amber_club6
        "It's nice to catch up with Amber away from work."
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
        if amberstage5event2 == 0:
            ###Sex variation ###
            image amber_club7 = "/amber/[amber.stage]/club7.webp"
            scene amber_club7
            #Belly 0.2
            amber "It's getting pretty late, should we order some food before the kitchen closes?"
            pc "Yeah, I could eat."
            image amber_club8 = "/amber/[amber.stage]/club8.webp"
            scene amber_club8
            amber "Maybe we can get them to go and continue this back at my place?"
            amber "I live nearby, if you want to join me?"
            pc "Absolutely."
            scene stripclub_order2
            "Grabbing some burgers to take away, you both head to Amber place."
            image amber_club9 = "/amber/[amber.stage]/club9.webp"
            scene amber_club9
            "Walking and eating, Amber manages to demolish her four burgers before you even get there."
            "It's impressive how quickly she can put those giant burgers away."
            stop music fadeout 1.0
            call Amber_home_new
            return
        else:
            ###Non sex variation ###
            image amber_club7 = "/amber/[amber.stage]/club7.webp"
            scene amber_club7
            #Belly 0.2
            amber "It's getting pretty late, should we order some food before the kitchen closes?"
            pc "Yeah, I could eat."
            amber "Great, I'll order them"
            image amber_club10 = "/amber/[amber.stage]/club10.webp"
            scene amber_club10
            "Ordering, Amber gets herself four burgers and some fries."
            image amber_club11 = "/amber/[amber.stage]/club11.webp"
            scene amber_club11
            "It seems like the more she opens up to you, the more she feels comfortable stuffing herself around you."
            "Biting into it the slightly tipsy Amber can't help but moan a little."
            amber "These are so good. I swear I could eat a dozen easily."
            image amber_club12 = "/amber/[amber.stage]/club12.webp"
            scene amber_club12
            #Belly 0.3
            amber "Which I suppose wouldn't be something you are against seeing."
            pc "I'm sure we can ask the waitress back."
            amber "You wish, I don't want to have to waddle back home tonight."
            image amber_club13 = "/amber/[amber.stage]/club13.webp"
            scene amber_club13
            "Devouring her burgers, Amber lets out a satisfied breath."
            amber "Ok, I needed that."
            image amber_club14 = "/amber/[amber.stage]/club14.webp"
            scene amber_club14
            amber "Nice and full."
            "Patting her bloated stomach, Amber seems very content."
            pc "I was thinking I should head home soon, it is getting late."
            image amber_club15 = "/amber/[amber.stage]/club15.webp"
            scene amber_club15
            amber "Yeah, probably a good idea."
            amber "Thanks for the fun time again."
            pc "Yeah, I enjoyed it."
            amber "See ya later."
            "You return home."
            stop music fadeout 1.0
            return
    elif amber.stage == 6:
        ##Stage 6 ###
        ##Amber already slightly bloated ##
        #Belly 0.15
        image amber_club1 = "/amber/[amber.stage]/club1.webp"
        scene amber_club1
        "Walking into the bar, you can see Amber smiling at you."
        image amber_club2 = "/amber/[amber.stage]/club2.webp"
        scene amber_club2
        "A couple of empty bottles and a plate with crumbs sit next to her on the counter."
        image amber_club3 = "/amber/[amber.stage]/club3.webp"
        scene amber_club3
        pc "Hey, how are you doing?"
        amber "Good thanks, looking forward to just relaxing and letting loose a little."
        pc "Stressful day at work?"
        amber "No, it was actually pretty good."
        amber "Having you there made it more bearable."
        pc "Thanks, although I don't know if I deserve credit for that."
        pc "I got really lucky with the three of you didn't I?"
        image amber_club4 = "/amber/[amber.stage]/club4.webp"
        scene amber_club4
        amber "What, a restaurant where the hot waitresses stuff their faces in front of you."
        amber "I wonder why you feel lucky."
        pc "Says the one who brought it up to me?"
        amber "I didn't bring it up to you."
        pc "I caught you stuffing yourself in the store room…"
        image amber_club5 = "/amber/[amber.stage]/club5.webp"
        scene amber_club5
        amber "I…ok, maybe I did in a way."
        amber "I guess we are all pretty lucky."
        pc "Have you spoken to Marie and Lisa about it yet?"
        amber "Not yet, maybe tomorrow."
        image amber_club6 = "/amber/[amber.stage]/club6.webp"
        scene amber_club6
        amber "Anyway, should we get some drinks?"
        pc "Yeah sure."
        scene stripclub_order
        "Ordering some drinks, you stand and chat at the bar for a while."
        image amber_club7 = "/amber/[amber.stage]/club7.webp"
        scene amber_club7
        "It's nice to catch up with Amber away from work."
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
        image amber_club8 = "/amber/[amber.stage]/club8.webp"
        scene amber_club8
        #Belly 0.25
        amber "It's getting pretty late, should we order some food before the kitchen closes?"
        pc "Yeah, I could eat."
        image amber_club9 = "/amber/[amber.stage]/club9.webp"
        scene amber_club9
        amber "Maybe we can get them to go and continue this back at my place?"
        amber "I live nearby, if you want to join me?"
        pc "Absolutely."
        scene stripclub_order2
        "Grabbing some burgers to take away, you both head to Amber place."
        image amber_club10 = "/amber/[amber.stage]/club10.webp"
        scene amber_club10
        #Belly 0.3
        "Walking and eating, Amber manages to demolish her four burgers before you even get there."
        "The pair of you barely said a word, her mouth full of meaty cheeseburgers the entire time."
        stop music fadeout 1.0
        call Amber_home_new
        return
    elif amber.stage == 7:
        ##Stage 7 ###
        ###Amber bloated, as much as she usually is at the end.###
        #Belly 0.3
        image amber_club1 = "/amber/[amber.stage]/club1.webp"
        scene amber_club1
        "Walking into the bar, you can see Amber smiling at you."
        image amber_club2 = "/amber/[amber.stage]/club2.webp"
        scene amber_club2
        "A bunch of bottles and a stack of three empty plates sit next to her."
        image amber_club3 = "/amber/[amber.stage]/club3.webp"
        scene amber_club3
        "It's clear from her bloated stomach, she was getting started early today."
        pc "Hey, how are you doing?"
        amber "Amazing, I've been feeling really good lately."
        pc "Could it have something to do with this?"
        image amber_club4 = "/amber/[amber.stage]/club4.webp"
        scene amber_club4
        "Leaning down you gently grab her stomach causing her to blush deeply."
        ###Blushing Amber###
        image amber_club5 = "/amber/[amber.stage]/club5.webp"
        scene amber_club5
        amber "Not here…but yes, maybe it does."
        amber "Life has certainly been more…interesting lately."
        pc "That's one way of putting it."
        pc "But it feels like there is still plenty of room in there."
        image amber_club6 = "/amber/[amber.stage]/club6.webp"
        scene amber_club6
        "Not waiting for an answer, you order Amber another four burgers and some drinks."
        image amber_club7 = "/amber/[amber.stage]/club7.webp"
        scene amber_club7
        amber "What are you doing, I'm already so full."
        amber "I can't eat that much."
        pc "I know you can, besides you wouldn't want me to miss out seeing you stuff yourself would you?"
        pc "A captive audience just to watch you eat and eat and eat?"
        image amber_club8 = "/amber/[amber.stage]/club8.webp"
        scene amber_club8
        amber "Behave!"
        "It's clear from the deep blush that she is enjoying the thought of it too."
        image amber_club9 = "/amber/[amber.stage]/club9.webp"
        scene amber_club9
        "Watching her eat, you stand and chat at the bar for a while."
        image amber_club10 = "/amber/[amber.stage]/club10.webp"
        scene amber_club10
        #Belly 0.4
        "It's nice to catch up with Amber, although most of your attention is spent on her growing stomach."
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
        image amber_club11 = "/amber/[amber.stage]/club11.webp"
        scene amber_club11
        #Belly 0.5
        "Finally, she finishes her plate of burgers, her belly filled to the brim."
        amber "Done, now can we get out of here and go back to mine?"
        image amber_club12 = "/amber/[amber.stage]/club12.webp"
        scene amber_club12
        amber "Having you watch me stuff myself in public…I need you right now!"
        pc "Sure you don't want another round of burgers?"
        "Almost pulling you out of the bar, Amber leads you to her home."
        stop music fadeout 1.0
        call Amber_home_new
        return
    elif amber.stage == 8:
        ##Stage 8 ###
        image amber_club1 = "/amber/[amber.stage]/club1.webp"
        scene amber_club1
        "Walking into the bar, you can see Amber smiling at you."
        "Unlike you have come to expect, you notice there are no plates or glasses near her."
        image amber_club2 = "/amber/[amber.stage]/club2.webp"
        scene amber_club2
        pc "Hey, how are you doing?"
        amber "Great thanks, you?"
        pc "Yeah, better now."
        pc "Is everything ok?"
        image amber_club3 = "/amber/[amber.stage]/club3.webp"
        scene amber_club3
        amber "Yeah why?"
        pc "No plates, or have they already cleared them away."
        amber "Have I really become that predictable?"
        amber "Can't a girl enjoy herself without eating a mountain of burgers."
        pc "Some can, but I am not sure you're one of them…"
        image amber_club4 = "/amber/[amber.stage]/club4.webp"
        scene amber_club4
        amber "Rude…but not wrong."
        amber "Maybe I am in the mood for something else, like having a certain someone feed me instead of eating myself."
        pc "I approve of this plan, assuming I'm the one that gets to feed you."
        image amber_club5 = "/amber/[amber.stage]/club5.webp"
        scene amber_club5
        amber "How about we get some drinks first?"
        pc "Yeah sure."
        scene stripclub_order
        "Ordering some drinks, you stand and chat at the bar for a while."
        image amber_club6 = "/amber/[amber.stage]/club6.webp"
        scene amber_club6
        "It's nice to catch up with Amber. Although, it's clear she is just waiting for you to take the lead and order food to take away."
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
        image amber_club7 = "/amber/[amber.stage]/club7.webp"
        scene amber_club7
        #Belly 0.1
        "She seems a bit restless, so you enjoy toying with her a little bit longer before she breaks."
        amber "It's getting pretty late, should we order some food before the kitchen closes?"
        "Checking your watch, they are probably not closing for another hour."
        pc "I wondered how long it would take for you to ask."
        amber "Oh, shut up and order me some burgers."
        scene stripclub_order2
        "Ordering a dozen burgers to take away, you both head to Amber place."
        stop music fadeout 1.0
        call Amber_home_new
        return
    elif amber.stage >= 9:
        ##Stage 9+ ###
        image amber_club1 = "/amber/[amber.stage]/club1.webp"
        scene amber_club1
        #Belly 0.3
        "Walking into the bar, you can see Amber smiling at you."
        image amber_club2 = "/amber/[amber.stage]/club2.webp"
        scene amber_club2
        "A stack of three empty plates and a few bottles sit next to her."
        image amber_club3 = "/amber/[amber.stage]/club3.webp"
        scene amber_club3
        "It's clear from her bloated stomach, she was getting started early today."
        image amber_club4 = "/amber/[amber.stage]/club4.webp"
        scene amber_club4
        pc "Hey, how are you doing?"
        amber "Good, looking forward to later tonight."
        pc "Why, what happens then?"
        image amber_club5 = "/amber/[amber.stage]/club5.webp"
        scene amber_club5
        amber "Shut up and buy me a drink."
        pc "What no foreplay?"
        amber "This entire evening is foreplay."
        pc "Oh yeah, is that right?"
        pc "Watching you stuff your face until you are even bursting out of your new clothes."
        pc "We only just bought them, are they feeling tight already?"
        image amber_club6 = "/amber/[amber.stage]/club6.webp"
        scene amber_club6
        "Leaning down you gently grab her stomach causing her to blush deeply."
        ###Amber blushing###
        image amber_club7 = "/amber/[amber.stage]/club7.webp"
        scene amber_club7
        amber "They are, especially my underwear."
        amber "I can't believe how quickly I'm growing."
        amber "It's like every day I gain weight and I can't stop myself from loving it."
        scene stripclub_order
        "Releasing her belly for now, you order Amber another eight burgers and some drinks."
        image amber_club8 = "/amber/[amber.stage]/club8.webp"
        scene amber_club8
        amber "That's too much!"
        pc "I guess we will see what is stronger, your stomach, or your sex drive."
        pc "We are not leaving until you finish all of those, and maybe a couple more drinks on top."
        image amber_club9 = "/amber/[amber.stage]/club9.webp"
        scene amber_club9
        "Blushing deeply, Amber nods obediently."
        image amber_club10 = "/amber/[amber.stage]/club10.webp"
        scene amber_club10
        #Belly 0.35
        "Watching her begin to eat, you stand and chat at the bar for a while."
        image amber_club11 = "/amber/[amber.stage]/club11.webp"
        scene amber_club11
        #Belly 0.4
        "It's nice to catch up with Amber, although she is finding it difficult to think of anything with her horny and addled mind."
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
        image amber_club12 = "/amber/[amber.stage]/club12.webp"
        scene amber_club12
        #Belly 0.45
        "Finally, she finishes her first four burgers, her belly bulging much larger already."
        image amber_club13 = "/amber/[amber.stage]/club13.webp"
        scene amber_club13
        amber "I don't think I can eat any more."
        image amber_club14 = "/amber/[amber.stage]/club14.webp"
        scene amber_club14
        "Picking up a burger, you force it towards her mouth."
        "Wide eyed, she is shocked you are willing to do this in public."
        image amber_club15 = "/amber/[amber.stage]/club15.webp"
        scene amber_club15
        "With no choice, she bites into it and you see Amber's eyes roll back into her head."
        "It's obvious how much she is enjoying it as you feed her, anyone could see the two of you."
        "Anyone who looked over would see you stuffing her, fattening her up."
        "After the first burger, Amber decides to keep eating for herself."
        image amber_club16 = "/amber/[amber.stage]/club16.webp"
        scene amber_club16
        #Belly 0.6
        "Eventually, all the burgers are gone and Amber looks fit to burst any moment."
        amber "Oooah, that was too much!"
        pc "Are you sure, I think you still have some room in there."
        amber "I can't, I mean it!"
        image amber_club17 = "/amber/[amber.stage]/club17.webp"
        scene amber_club17
        amber "Now can we get out of here and go back to mine?"
        amber "I'm not sure if I feel like I am going to explode or cum right now!"
        "Almost pulling you out of the bar, Amber leads you home."
        stop music fadeout 1.0
        call Amber_home_new
        return



label Amber_home_new:
    if amber.stage == 5:
        ###Amber place ###
        #Belly 0.3
        image amber_home1 = "/amber/[amber.stage]/home1.webp"
        scene amber_home1
        amber "Home sweet home."
        amber "Make yourself comfortable, and I'll do the same."
        image amber_home2 = "/amber/[amber.stage]/home2.webp"
        scene amber_home2
        "Sitting on the couch, Amber starts stripping."
        image amber_home3 = "/amber/[amber.stage]/home3.webp"
        scene amber_home3
        amber "What's the matter? I know you have been wanting to see me naked all evening."
        image amber_home4 = "/amber/[amber.stage]/home4.webp"
        scene amber_home4
        amber "You could barely keep your eyes off my belly when we were walking home."
        image amber_home5 = "/amber/[amber.stage]/home5.webp"
        scene amber_home5
        amber "Does it turn you on to see me so full and fat."
        image amber_home6 = "/amber/[amber.stage]/home6.webp"
        scene amber_home6
        window hide
        pause
        image amber_home7 = "/amber/[amber.stage]/home7.webp"
        scene amber_home7
        "Reaching out a hand, you gently press on her firm belly, filled to the brim with beer and burgers."
        pc "You know it does."
        amber "Good because it turns me on too."
        image amber_home8 = "/amber/[amber.stage]/home8.webp"
        scene amber_home8
        "Kissing you passionately, Amber moans softly as your hands explore her body."
        image amber_home9 = "/amber/[amber.stage]/home9.webp"
        scene amber_home9
        amber "But I want to get so much bigger."
        if persistent.nosexscene == True:
            scene black with dissolve
            "Amber and I had a great time together."
            "You head home for the night."
            $ amber.weight += 0.6
            stop music fadeout 1.0
            return
        else:
            image amber_home10 = "/amber/[amber.stage]/home10.webp"
            scene amber_home10
            "Dropping onto the couch, Amber gets on all fours."
        image amber_home11 = "/amber/[amber.stage]/home11.webp"
        scene amber_home11
        amber "Waiting for an invitation?"
        image amber_home12 = "/amber/[amber.stage]/home12.webp"
        scene amber_home12
        "Approaching her from behind, you gently cup her stomach."
        amber "That feels good, my stomach is so firm right now."
        image amber_home13 = "/amber/[amber.stage]/home13.webp"
        scene amber_home13
        amber "But it won't be for long if I keep eating like I did tonight."
        image amber_home_sex = "/amber/[amber.stage]/home_sex.webp"
        scene amber_home_sex
        "Grabbing her soft hips you slide into her, causing Amber to moan."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/5/home_sex1.webm" loop
        show movie with dissolve
        "Moving her body back and forth, you can feel how tight and wet she is around your cock."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/5/home_sex2.webm" loop
        show movie with dissolve
        "With each thrust her belly shakes, only heightening the experience and pleasure."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/5/home_sex3.webm" loop
        show movie with dissolve
        amber "Oh yeah, keep going. I'm close."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/5/home_sex4.webm" loop
        show movie with dissolve
        "With a few last thrusts, you both orgasm together."
        window hide
        pause
        stop movie
        image amber_home_aftersex1 = "/amber/[amber.stage]/home_aftersex1.webp"
        scene amber_home_aftersex1
        "Laying back on the sofa, Amber breaths heavily."
        image amber_home_aftersex2 = "/amber/[amber.stage]/home_aftersex2.webp"
        scene amber_home_aftersex2
        amber "That was amazing."
        image amber_home_aftersex3 = "/amber/[amber.stage]/home_aftersex3.webp"
        scene amber_home_aftersex3
        "Recovering and cleaning up your mess, you head home for the night."
        $ amber.weight += 0.6
        stop music fadeout 1.0
        return
    elif amber.stage == 6:
        ###Amber place ###
        image amber_home1 = "/amber/[amber.stage]/home1.webp"
        scene amber_home1
        #Belly 0.5
        "Walking in, Amber points to the couch."
        amber "Shall we have some fun?"
        image amber_home2 = "/amber/[amber.stage]/home2.webp"
        scene amber_home2
        "Pushing you onto the couch, Amber starts stripping."
        image amber_home3 = "/amber/[amber.stage]/home3.webp"
        scene amber_home3
        amber "Is this what you want?"
        image amber_home4 = "/amber/[amber.stage]/home4.webp"
        scene amber_home4
        "Taking off her dress, she shows off her growing stomach."
        image amber_home5 = "/amber/[amber.stage]/home5.webp"
        scene amber_home5
        amber "I know you love this, how big I am getting."
        amber "I bet you can barely resist it, do you want to touch it?"
        image amber_home7 = "/amber/[amber.stage]/home7.webp"
        scene amber_home7
        "Reaching out a hand, you gently press on her firm belly, filled to the brim with beer and burgers."
        pc "You look amazing."
        image amber_home9 = "/amber/[amber.stage]/home9.webp"
        scene amber_home9
        amber "I do…but I also look far too skinny, wouldn't you agree."
        pc "Absolutely."
        image amber_home8 = "/amber/[amber.stage]/home8.webp"
        scene amber_home8
        "Kissing you passionately, Amber moans softly as your hands explore her body."
        if persistent.nosexscene == True:
            scene black with dissolve
            "Amber and I had a great time together."
            "You head home for the night."
            $ amber.weight += 0.8
            stop music fadeout 1.0
            return
        else:
            image amber_home10 = "/amber/[amber.stage]/home10.webp"
            scene amber_home10
            "Dropping onto the couch, Amber gets on all fours."
        image amber_home11 = "/amber/[amber.stage]/home11.webp"
        scene amber_home11
        window hide
        pause
        image amber_home_sex = "/amber/[amber.stage]/home_sex.webp"
        scene amber_home_sex
        "Grabbing her soft hips you slide into her, causing Amber to moan."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/6/home_sex1.webm" loop
        show movie with dissolve
        amber "Fuck yeah, am I your fat little play thing?"
        amber "Do you want to feed me, make me so big and fat all the time."
        "Moving her body back and forth, you can feel how tight and wet she is around your cock."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/6/home_sex2.webm" loop
        show movie with dissolve
        "With each thrust her belly shakes, only heightening the experience and pleasure."
        amber "Oh yeah, keep going. I'm close."
        pc "I bet you would like that, to be so round and chubby."
        amber "More than chubby, I want to be massive."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/6/home_sex3.webm" loop
        show movie with dissolve
        pc "A whale then, so big you break the sofa, so big you don't even fit on it any more."
        amber "Yess!"
        amber "I want to be massive, a giant ball of fat for you to fuck!"
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/6/home_sex4.webm" loop
        show movie with dissolve
        amber "God, I'm going to cum!"
        "With a few last thrusts, you both orgasm together."
        window hide
        pause
        stop movie
        image amber_home_aftersex1 = "/amber/[amber.stage]/home_aftersex1.webp"
        scene amber_home_aftersex1
        "Laying back on the sofa, Amber breaths heavily."
        image amber_home_aftersex2 = "/amber/[amber.stage]/home_aftersex2.webp"
        scene amber_home_aftersex2
        amber "That was amazing."
        image amber_home_aftersex3 = "/amber/[amber.stage]/home_aftersex3.webp"
        scene amber_home_aftersex3
        "Recovering and cleaning up your mess, you head home for the night."
        $ amber.weight += 0.8
        stop music fadeout 1.0
        return
    elif amber.stage == 7:
        ###Amber place ###
        image amber_home1 = "/amber/[amber.stage]/home1.webp"
        scene amber_home1
        #Belly 0.5
        amber "Let's get you out of those clothes, and into me."
        image amber_home2 = "/amber/[amber.stage]/home2.webp"
        scene amber_home2
        "Both of you strip quickly."
        image amber_home3 = "/amber/[amber.stage]/home3.webp"
        scene amber_home3
        amber "Fuck, I'm so full."
        image amber_home4 = "/amber/[amber.stage]/home4.webp"
        scene amber_home4
        pc "You're getting so big!"
        image amber_home5 = "/amber/[amber.stage]/home5.webp"
        scene amber_home5
        "Reaching out a hand, you gently press on her firm belly, filled to the brim with beer and burgers."
        image amber_home6 = "/amber/[amber.stage]/home6.webp"
        scene amber_home6
        "Kissing you passionately, Amber moans softly as your hands explore her body."
        if persistent.nosexscene == True:
            scene black with dissolve
            "Amber and I had a great time together."
            "You head home for the night."
            $ amber.weight += 0.8
            stop music fadeout 1.0
            return
        else:
            image amber_home7 = "/amber/[amber.stage]/home7.webp"
            scene amber_home7
            "Dropping onto the couch, Amber gets on all fours, pulling you close to her."
        image amber_home8 = "/amber/[amber.stage]/home8.webp"
        scene amber_home8
        window hide
        pause
        image amber_home_sex = "/amber/[amber.stage]/home_sex.webp"
        scene amber_home_sex
        "Grabbing her soft hips you slide into her, causing Amber to moan."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/7/home_sex1.webm" loop
        show movie with dissolve
        pc "You look so big."
        amber "I've gained so much weight, but I want even more!"
        amber "My belly is so full, but I want to be this big all the time."
        amber "I love this feeling!"
        "Moving her body back and forth, you can feel how tight and wet she is around your cock."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/7/home_sex2.webm" loop
        show movie with dissolve
        "With each thrust her belly shakes, only heightening the experience and pleasure."
        amber "Oh yeah, keep going. I'm close."
        pc "Does it turn you on to think about how much you have gained already?"
        pc "To think about how skinny you were and what you did to your body."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/7/home_sex3.webm" loop
        show movie with dissolve
        pc "You look completely different, your so much bigger, wider, fatter!"
        amber "Fuck yeah, but it's only the start!"
        amber "I'm going to gorge myself on food, eat all day every day."
        amber "I'm going to make myself massive."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/7/home_sex4.webm" loop
        show movie with dissolve
        amber "Oh shit, I think I am going to cum."
        pc "Cum for me, think about how big you will be."
        "With a few last thrusts, you both orgasm together."
        window hide
        pause
        stop movie
        image amber_home_aftersex1 = "/amber/[amber.stage]/home_aftersex1.webp"
        scene amber_home_aftersex1
        "Laying back on the sofa, Amber breaths heavily."
        image amber_home_aftersex2 = "/amber/[amber.stage]/home_aftersex2.webp"
        scene amber_home_aftersex2
        amber "That was amazing."
        image amber_home_aftersex3 = "/amber/[amber.stage]/home_aftersex3.webp"
        scene amber_home_aftersex3
        "Recovering and cleaning up your mess, you head home for the night."
        $ amber.weight += 0.8
        stop music fadeout 1.0
        return
    elif amber.stage == 8:
        ###Amber place ###
        image amber_home1 = "/amber/[amber.stage]/home1.webp"
        scene amber_home1
        #Belly 0.1
        amber "Home sweet home."
        image amber_home2 = "/amber/[amber.stage]/home2.webp"
        scene amber_home2
        "Sitting on the couch, Amber starts stripping"
        image amber_home3 = "/amber/[amber.stage]/home3.webp"
        scene amber_home3
        amber "Mmm, all I can think about are those burgers."
        pc "Sure there is nothing else?"
        image amber_home4 = "/amber/[amber.stage]/home4.webp"
        scene amber_home4
        amber "Maybe my desert…"
        pc "I take it, that me?"
        image amber_home5 = "/amber/[amber.stage]/home5.webp"
        scene amber_home5
        amber "Maybe…"
        ###Amber kneeling in front of you leaning forwards almost BJ angle###
        image amber_home6 = "/amber/[amber.stage]/home6.webp"
        scene amber_home6
        "She kneels before you naked."
        amber "Now, feed me please!"
        image amber_home7 = "/amber/[amber.stage]/home7.webp"
        scene amber_home7
        "Taking out the burger, you sensually hold it up to her mouth."
        "Biting into it, Amber's eyes flutter as the hot fatty meat melts on her tongue."
        "Holding it in place she eats quickly and finishes the first one off."
        image amber_home8 = "/amber/[amber.stage]/home8.webp"
        scene amber_home8
        #Belly 0.2
        pc "I hope you are hungry, plenty more to go."
        amber "Mmm, feed me, stuff me full!"
        ###Amber sitting on the floor ####
        image amber_home9 = "/amber/[amber.stage]/home9.webp"
        scene amber_home9
        "One by one you feed Amber the burgers, grease spilling out her mouth and down onto her growing belly."
        image amber_home10 = "/amber/[amber.stage]/home10.webp"
        scene amber_home10
        window hide
        pause
        image amber_home11 = "/amber/[amber.stage]/home11.webp"
        scene amber_home11
        "Each calorie laden treat causes her to grow larger and moan louder."
        #Belly 0.5
        image amber_home12 = "/amber/[amber.stage]/home12.webp"
        scene amber_home12
        window hide
        pause
        image amber_home13 = "/amber/[amber.stage]/home13.webp"
        scene amber_home13
        "With one burger to go, she lets out a pained or horny whine."
        amber "I'm too full, I can't eat any more."
        pc "Just one more to go."
        amber "I'll burst."
        pc "Good."
        image amber_home14 = "/amber/[amber.stage]/home14.webp"
        scene amber_home14
        "Pressing it to her lips Amber bites into the burger, her chewing laboured."
        image amber_home15 = "/amber/[amber.stage]/home15.webp"
        scene amber_home15
        #Belly 0.6
        "As she swallows the last bites, you reach down and play with her belly, once more filled to capacity with burgers."
        "Rubbing her bloated belly, she moans with pleasure."
        amber "That feels good."
        image amber_home16 = "/amber/[amber.stage]/home16.webp"
        scene amber_home16
        "Kissing you passionately,you can taste the grease on her lips as she climbs onto the couch."
        if persistent.nosexscene == True:
            scene black with dissolve
            "Amber and I had a great time together."
            "You head home for the night."
            $ amber.weight += 1
            stop music fadeout 1.0
            return
        else:
            image amber_home17 = "/amber/[amber.stage]/home17.webp"
            scene amber_home17
            window hide
            pause
            image amber_home18 = "/amber/[amber.stage]/home18.webp"
            scene amber_home18
            "Moving around behind her, you grab her increasingly flabby rear."
        image amber_home_sex = "/amber/[amber.stage]/home_sex.webp"
        scene amber_home_sex
        "Admiring the changes in her body, you slide into Amber causing her to moan."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/8/home_sex1.webm" loop
        show movie with dissolve
        "Moving her body back and forth, you can feel how tight and wet she is around your cock."
        amber "I'm so full…it aches."
        pc "Good, feel how big you are, how much your stomach is stretched."
        pc "I want this to be how you feel every day."
        pc "I want to come around and feed you till you are bursting full."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/8/home_sex2.webm" loop
        show movie with dissolve
        "With each thrust her belly shakes, only heightening the experience and pleasure."
        amber "Oh yeah, keep going. I'm close."
        amber "I want that, I want to be fed all day."
        amber "I want to get huge, fatter then I even imagined."
        amber "I want to be made to eat, no choice but to eat more and get stuffed beyond my limits."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/8/home_sex3.webm" loop
        show movie with dissolve
        amber "I don't want to be able to stop, I want to be forced to eat until I ache so badly from all the food I've eaten."
        pc "Yeah, you would like that."
        pc "To have no control, to be made to eat?"
        pc "To just get fatter and fatter every single day."
        pc "The only thing you do is eat and fuck."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/amber/8/home_sex4.webm" loop
        show movie with dissolve
        amber "I'm going to cum!"
        "With a few last thrusts, you both orgasm together."
        window hide
        pause
        stop movie
        image amber_home_aftersex1 = "/amber/[amber.stage]/home_aftersex1.webp"
        scene amber_home_aftersex1
        "Laying back on the sofa, Amber breaths heavily."
        image amber_home_aftersex2 = "/amber/[amber.stage]/home_aftersex2.webp"
        scene amber_home_aftersex2
        amber "That was amazing."
        image amber_home_aftersex3 = "/amber/[amber.stage]/home_aftersex3.webp"
        scene amber_home_aftersex3
        "Recovering and cleaning up your mess, you head home for the night."
        $ amber.weight += 1
        stop music fadeout 1.0
        return
    elif amber.stage >= 9:
        ###Amber place ###
        image amber_home1 = "/amber/[amber.stage]/home1.webp"
        scene amber_home1
        #Belly 0.6
        amber "Let's get you out of those clothes, and into me."
        image amber_home2 = "/amber/[amber.stage]/home2.webp"
        scene amber_home2
        "Both of you strip quickly."
        image amber_home3 = "/amber/[amber.stage]/home3.webp"
        scene amber_home3
        window hide
        pause
        image amber_home4 = "/amber/[amber.stage]/home4.webp"
        scene amber_home4
        amber "Fuck, I'm so full."
        image amber_home5 = "/amber/[amber.stage]/home5.webp"
        scene amber_home5
        pc "You're getting so big!"
        image amber_home6 = "/amber/[amber.stage]/home6.webp"
        scene amber_home6
        "Reaching out a hand, you gently press on her firm belly, filled to the brim with beer and burgers."
        image amber_home7 = "/amber/[amber.stage]/home7.webp"
        scene amber_home7
        "Kissing you passionately, Amber moans softly as your hands explore her body."
        $ stuffed = 1
        menu:
            "Feed Amber":
                if foodheld <= 0:
                    "You do not have anymore food with you to feed Amber with."
                    if persistent.nosexscene == True:
                        scene black with dissolve
                        "Amber and I had a great time together."
                        "You head home for the night."
                        stop music fadeout 1.0
                        $ amber.weight += 1
                        $ bellyrub = 0
                        $ stuffed = 0
                        return
                    else:
                        amber "Now I need you to fuck me, I've been aching in another way all evening."
                        $ amber.weight += 1
                else:
                    "Despite your eagerness, you want to see Amber really push her limits tonight."
                    image amber_home8 = "/amber/[amber.stage]/home8.webp"
                    scene amber_home8
                    pc "I don't think you have eaten enough."
                    amber "You can't be serious, there is no way I can eat any more."
                    pc "I think you can."
                    "Pulling out a bag of sweet treats from Bonnie's shop, you see Amber's defences falter."
                    image amber_home9 = "/amber/[amber.stage]/home9_1.webp"
                    scene amber_home9
                    "The couch creaks under her weight as she sits down."
                    "As full as she already is, you notice her horny gluttonous mind taking over as she excitingly waits for you to push her limits."
                    show screen amberfullness
                    "You unwrap the first treat."
                    image amber_home10 = "/amber/[amber.stage]/home10.webp"
                    scene amber_home10
                    $ foodheld -= 1
                    amber "Mmm, so good."

                    #[Feeding minigame - Not sure how many button presses you want to include? I’ve done a bunch but the later ones might only be needed for later versions where her capacity has gone up?]
                    call amber_home_feeding
                    pause
                    $ amber.weight += (amber.fullness / 2)
                    $ amber.weight += 0.5
                    $ amber.fullness = 0
                    hide screen amberfullness
                    pause
                    image amber_home11_stuffed = "/amber/[amber.stage]/home11_[stuffed].webp"
                    scene amber_home11_stuffed
                    #Belly 1.0
                    #Upper 1.0
                    amber "Mmm, you are ruthless, feeding me, fattening me up for your own enjoyment."
                    amber "I love when you take control, just look at how big you have made me."
                    if persistent.nosexscene == True:
                        scene black with dissolve
                        "Amber and I had a great time together."
                        "You head home for the night."
                        stop music fadeout 1.0
                        $ bellyrub = 0
                        $ stuffed = 0
                        return
                    else:
                        amber "But now I need you to fuck me, I've been aching in another way all evening."
            "Have sex with Amber":
                if persistent.nosexscene == True:
                    scene black with dissolve
                    "Amber and I had a great time together."
                    "You head home for the night."
                    stop music fadeout 1.0
                    $ amber.weight += 1
                    $ bellyrub = 0
                    $ stuffed = 0
                    return
                else:
                    amber "Now I need you to fuck me, I've been aching in another way all evening."
                    $ amber.weight += 1
        image amber_home12_stuffed = "/amber/[amber.stage]/home12_[stuffed].webp"
        scene amber_home12_stuffed
        "Dropping onto the couch, Amber gets on all fours, pulling you close to her."
        image amber_home13_stuffed = "/amber/[amber.stage]/home13_[stuffed].webp"
        scene amber_home13_stuffed
        window hide
        pause
        image amber_home_sex = "/amber/[amber.stage]/home_sex.webp"
        scene amber_home_sex
        "Grabbing her soft hips you slide into her, causing Amber to moan."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if amber.stage == 9:
            play movie "/images/amber/9/home_sex1.webm" loop
        elif amber.stage == 10:
            play movie "/images/amber/10/home_sex1.webm" loop
        elif amber.stage == 11:
            play movie "/images/amber/11/home_sex1.webm" loop
        elif amber.stage == 12:
            play movie "/images/amber/12/home_sex1.webm" loop
        elif amber.stage == 13:
            play movie "/images/amber/13/home_sex1.webm" loop
        show movie with dissolve
        "Moving her body back and forth, you can feel how tight and wet she is around your cock."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if amber.stage == 9 and stuffed == 2:
            play movie "/images/amber/9/home_sex2_stuffed.webm" loop
        elif amber.stage == 9:
            play movie "/images/amber/9/home_sex2.webm" loop
        elif amber.stage == 10 and stuffed == 2:
            play movie "/images/amber/10/home_sex2_stuffed.webm" loop
        elif amber.stage == 10:
            play movie "/images/amber/10/home_sex2.webm" loop
        elif amber.stage == 11 and stuffed == 2:
            play movie "/images/amber/11/home_sex2_stuffed.webm" loop
        elif amber.stage == 11:
            play movie "/images/amber/11/home_sex2.webm" loop
        elif amber.stage == 12 and stuffed == 2:
            play movie "/images/amber/12/home_sex2_stuffed.webm" loop
        elif amber.stage == 12:
            play movie "/images/amber/12/home_sex2.webm" loop
        elif amber.stage == 13 and stuffed == 2:
            play movie "/images/amber/13/home_sex2_stuffed.webm" loop
        elif amber.stage == 13:
            play movie "/images/amber/13/home_sex2.webm" loop
        show movie with dissolve
        "With each thrust her belly shakes, only heightening the experience and pleasure."
        amber "Oh yeah, keep going. I'm already close."
        "With every thrust her firm and hanging belly slaps against her thighs."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if amber.stage == 9 and stuffed == 2:
            play movie "/images/amber/9/home_sex3_stuffed.webm" loop
        elif amber.stage == 9:
            play movie "/images/amber/9/home_sex3.webm" loop
        elif amber.stage == 10 and stuffed == 2:
            play movie "/images/amber/10/home_sex3_stuffed.webm" loop
        elif amber.stage == 10:
            play movie "/images/amber/10/home_sex3.webm" loop
        elif amber.stage == 11 and stuffed == 2:
            play movie "/images/amber/11/home_sex3_stuffed.webm" loop
        elif amber.stage == 11:
            play movie "/images/amber/11/home_sex3.webm" loop
        elif amber.stage == 12 and stuffed == 2:
            play movie "/images/amber/12/home_sex3_stuffed.webm" loop
        elif amber.stage == 12:
            play movie "/images/amber/12/home_sex3.webm" loop
        elif amber.stage == 13 and stuffed == 2:
            play movie "/images/amber/13/home_sex3_stuffed.webm" loop
        elif amber.stage == 13:
            play movie "/images/amber/13/home_sex3.webm" loop
        show movie with dissolve
        "Picking up the pace your movements send shockwaves through her blubbery body."
        "Amber's moaning gets louder and louder as you pump into her plump body."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if amber.stage == 9:
            play movie "/images/amber/9/home_sex4.webm" loop
        elif amber.stage == 10:
            play movie "/images/amber/10/home_sex4.webm" loop
        elif amber.stage == 11:
            play movie "/images/amber/11/home_sex4.webm" loop
        elif amber.stage == 12:
            play movie "/images/amber/12/home_sex4.webm" loop
        elif amber.stage == 13:
            play movie "/images/amber/13/home_sex4.webm" loop
        show movie with dissolve
        "With a few last thrusts, you both orgasm together."
        window hide
        pause
        stop movie
        image amber_home_aftersex1_stuffed = "/amber/[amber.stage]/home_aftersex1_[stuffed].webp"
        scene amber_home_aftersex1_stuffed
        "Laying back on the sofa, Amber breaths heavily."
        image amber_home_aftersex2_stuffed = "/amber/[amber.stage]/home_aftersex2_[stuffed].webp"
        scene amber_home_aftersex2_stuffed
        amber "That was amazing."
        image amber_home_aftersex1_stuffed = "/amber/[amber.stage]/home_aftersex3_[stuffed].webp"
        scene amber_home_aftersex1_stuffed
        "Recovering and cleaning up your mess, you head home for the night."
        stop music fadeout 1.0
        $ bellyrub = 0
        $ stuffed = 0
        return



label amber_bar:
    image amber_club_arrive = "/amber/[amber.stage]/club_arrive.webp"
    scene amber_club_arrive
    play music "/music/stripclub.ogg" if_changed
    "You arrive at the bar and see Amber in her clubbing outfit."
    amber "Hey! You're wearing that same shirt again!"
    pc "Yeah, it's my clubbing shirt!"
    "Weird thing to say, but it was a better explanation than the fact that you wore it because you knew she liked it."
    amber "Well, I think it makes you look very handsome. What do you think of mine?"
    pc "You look amazing like always!"
    image amber_club1 = "/amber/[amber.stage]/club1.webp"
    scene amber_club1
    "You can tell that Amber is very pleased by your compliment. With a big smile on her face, she guides you towards the bar."
    amber "A Tequila Sunrise for me and a lager for this guy, please."
    pc "Hey, you remembered my order from last time."
    image amber_club2 = "/amber/[amber.stage]/club2.webp"
    scene amber_club2
    amber "When you're a waitress it kind of becomes second nature haha."
    "The two of you chat while you sip on your lager. Over the course of the night you both have several more drinks, especially Amber who is really indulging her sweet tooth tonight."
    image amber_club3 = "/amber/[amber.stage]/club3.webp"
    scene amber_club3
    "Later..."
    pc "So then I said \"no sir, the fries cost extra!\""
    "Amber lets out a loud and obnoxious laugh which could only come out of a drunk person. Normally you'd be embarrassed but you're also quite pickled."
    if amber.stage >= 3:
        amber "I tell you what, how about we continue this at my place? It's fairly close by."
        pc "Sure, why not?"
        amber "But first I wanna stop for some fast food. I am starving!"
        stop music fadeout 1.0
        call amber_home from _call_amber_home
        return
    amber "I think I have had enough alcohol. I should get going. Thanks for the fun night!"
    pc "See ya later, Amber!"
    "You return home."
    stop music fadeout 1.0
    return

label Amber_BB_Extra:
    "You decide to pay the difference yourself."
    $ money -= 5
    image cafe_amber_extrafood = "/amber/[amber.stage]/cafe_extrafood.webp"
    scene cafe_amber_extrafood
    if amber.stage >= 7:
        amber "Mmm, that's quite a bit of food, thank you!"
        image cafe_amber_eating = "/amber/[amber.stage]/cafe_eating.webp"
        scene cafe_amber_eating
        "She immediately digs in, clearly eager to pig out. She's really forgotten her table manners recently..."
        amber "Mmph, you know *urp!* if I didn't know any better, I'd think you were trying to *slurp* fatten me up."
        "You give her a sly smile."
        pc "I have no clue what you mean."
        "Amber laughs before letting out a belch."
        image cafe_amber_burp = "/amber/[amber.stage]/cafe_burp.webp"
        scene cafe_amber_burp
        amber "*UUUUURP* Oof, excuse me!"
        image cafe_amber_struggle = "/amber/[amber.stage]/cafe_struggle.webp"
        scene cafe_amber_struggle
        "As she finishes off her meal, she leans back in her seat with a satisfied smile. You go over to check on her."
        amber "That was *hic!* amazing. You better watch out, a girl could get used to being spoiled like this. And then what would you do?"
        pc "I guess I'd have to start spoiling you even more."
        amber "Ha, that's not a bad idea. See you around, [playername]."
        pc "Bye Amber."
        return
    amber "Uhh, I think there has been a mistake. I didn't order this much food."
    pc "Oops, sorry about that. It's already been paid for though so do you want it anyway?"
    amber "Sure, why not?"
    pc "In that case, I hope you enjoy the food."
    amber "Thank you!"
    image cafe_amber_struggle = "/amber/[amber.stage]/cafe_struggle.webp"
    scene cafe_amber_struggle
    "You notice Amber struggling to eat all of the extra food."
    return

label Amber_BB_Prize:
    image cafe_amber_prize1 = "/amber/[amber.stage]/cafe_prize1.webp"
    scene cafe_amber_prize1
    "Creating a sizable feast, you approach Amber."
    image cafe_amber_prize2 = "/amber/[amber.stage]/cafe_prize2.webp"
    scene cafe_amber_prize2
    pc "Congratulations, you are the winner of this week's prize!"
    if amberprizefirsttime == 1:
        amber "The prize Marie set up?"
        pc "Exactly."
        amber "I didn't think we could win those since we are staff?"
        pc "I think any order can technically win it, it is completely random."
        amber "Great, thanks I guess."
        image cafe_amber_prize3 = "/amber/[amber.stage]/cafe_prize3.webp"
        scene cafe_amber_prize3
        "Despite her calm demeanour, you can see a sense of excitement in Amber's face."
        image cafe_amber_prize4 = "/amber/[amber.stage]/cafe_prize4.webp"
        scene cafe_amber_prize4
        "Stacking the food on the table, Amber begins to eat her giant meal."
        "Diving in, she makes quick work of the food although her pace begins to slow down."
        image cafe_amber_prize5 = "/amber/[amber.stage]/cafe_prize5.webp"
        scene cafe_amber_prize5
        "Her bulging belly unable to keep up with how fast she was stuffing the food in her mouth."
        image cafe_amber_prize6 = "/amber/[amber.stage]/cafe_prize6.webp"
        scene cafe_amber_prize6
        "Despite her best efforts it is simply too much food for one person and she leans back defeated and extremely full."
        image cafe_amber_prize7 = "/amber/[amber.stage]/cafe_prize7.webp"
        scene cafe_amber_prize7
        pc "How was the food?"
        amber "Mmm, good but I can't eat another bite."
        pc "I'll pack the rest up so you can take it home with you."
        amber "Thanks."
        amber "There is no rush though, I don't think I can move right now."
        $ amberprizefirsttime = 0
    elif amber.stage <= 6:
        amber "Again?"
        pc "Seems like you have been lucky recently."
        amber "Perfect, I can't wait!"
        image cafe_amber_prize3 = "/amber/[amber.stage]/cafe_prize3.webp"
        scene cafe_amber_prize3
        "Smiling, Amber is clearly excited and looks at the food hungrily."
        image cafe_amber_prize4 = "/amber/[amber.stage]/cafe_prize4.webp"
        scene cafe_amber_prize4
        "Stacking the food on the table, Amber begins to eat her giant meal."
        "Diving in, she seems to have learned from last time and is eating at a more reasonable pace."
        image cafe_amber_prize5 = "/amber/[amber.stage]/cafe_prize5.webp"
        scene cafe_amber_prize5
        "Stuffing more and more food into her mouth, her stomach swells as she forces it to keep growing."
        image cafe_amber_prize6 = "/amber/[amber.stage]/cafe_prize6.webp"
        scene cafe_amber_prize6
        "However, the prize is simply too much food for one person and she leans back defeated and extremely full."
        image cafe_amber_prize7 = "/amber/[amber.stage]/cafe_prize7.webp"
        scene cafe_amber_prize7
        pc "How was the food?"
        amber "Mmm, so good."
        amber "I'm just disappointed I couldn't eat even more of it."
        pc "I'll pack the rest up so you can take it home with you."
        amber "Thanks."
        amber "There is no rush though, I want to enjoy this feeling a bit longer."
    elif amber.stage >= 7:
        amber "Mmm, I sure have been lucky lately."
        amber "Not that I am complaining, the opposite if anything."
        image cafe_amber_prize3 = "/amber/[amber.stage]/cafe_prize3.webp"
        scene cafe_amber_prize3
        "Smiling, Amber is clearly excited and looks at the food hungrily."
        image cafe_amber_prize4 = "/amber/[amber.stage]/cafe_prize4.webp"
        scene cafe_amber_prize4
        "Stacking the food on the table, Amber begins to eat her giant meal."
        "Eating at a steady pace, you watch the food disappear into her greedy mouth."
        "Making no effort to be quiet or hide her gluttony, Amber seems to be enjoying the looks from some of the other customers."
        image cafe_amber_prize5 = "/amber/[amber.stage]/cafe_prize5.webp"
        scene cafe_amber_prize5
        if amber.stage >= 12:
            "You keep an eye on Amber's belly as she fills up with all the food you brought her."
            image cafe_amber_prize9 = "/amber/[amber.stage]/cafe_prize9.webp"
            scene cafe_amber_prize9
            "Stuffing more and more food into her mouth, her stomach swells as she forces it to keep growing."
            image cafe_amber_prize10 = "/amber/[amber.stage]/cafe_prize10.webp"
            scene cafe_amber_prize10
            "Amber's insatiable appetite seems to have no limits as her belly grows bigger and bigger."
            image cafe_amber_prize6 = "/amber/[amber.stage]/cafe_prize6.webp"
            scene cafe_amber_prize6
            "With the table cleared and her stomach looking ready to burst, Amber seems to be pleased with herself."
            image cafe_amber_prize7 = "/amber/[amber.stage]/cafe_prize7.webp"
            scene cafe_amber_prize7
            pc "How was the food?"
            amber "Mmm, so so good."
            amber "Are you proud of me?."
            menu:
                "Push her to eat more.":
                    pc "I know you can eat more than this still."
                    image cafe_amber_prize12 = "/amber/[amber.stage]/cafe_prize12.webp"
                    scene cafe_amber_prize12
                    amber "I really can't, maybe next time."
                    pc "If you want to make me proud you take some food with you home to eat for me."
                    "She seems to ponder for a moment."
                    amber "Alright, bring me some food to take home."
                    image cafe_amber_prize8 = "/amber/[amber.stage]/cafe_prize8.webp"
                    scene cafe_amber_prize8
                    "Returning a few minutes later, you hand Amber two large bags of food to take home with her."
                    "Walking slowly, the stuffed Amber leaves and you return to the front counter."
                    return
                "Tell her you are proud of her.":
                    pc "Good girl, I'm proud of you."
                    image cafe_amber_prize13 = "/amber/[amber.stage]/cafe_prize13.webp"
                    scene cafe_amber_prize13
                    "Her face lights up with joy as you praise her."
                    amber "Next time I'll try to eat even more for you."
                    amber "I can't wait."
                    image cafe_amber_prize11 = "/amber/[amber.stage]/cafe_prize11.webp"
                    scene cafe_amber_prize11
                    "She gets up and slowly waddles out as you return to the front counter."
                    return

        else:
            "Stuffing more and more food into her mouth, her stomach swells as she forces it to keep growing."
            "With the table almost clear and her stomach looking ready to burst, Amber is forced to throw in the towel."
            image cafe_amber_prize6 = "/amber/[amber.stage]/cafe_prize6.webp"
            scene cafe_amber_prize6
            "The prize is simply too much food for one person and she leans back defeated and extremely full."
            image cafe_amber_prize7 = "/amber/[amber.stage]/cafe_prize7.webp"
            scene cafe_amber_prize7
            pc "How was the food?"
            amber "Mmm, so good."
            amber "I'm just disappointed I couldn't eat even more of it."
            amber "One day I'll be able to finish this in one sitting."
            pc "I'll pack the rest up so you can take it home with you."
            amber "Thanks."
    image cafe_amber_prize8 = "/amber/[amber.stage]/cafe_prize8.webp"
    scene cafe_amber_prize8
    "Returning a few minutes later, you hand Amber two large bags of food to take home with her."
    "Walking slowly, the stuffed Amber leaves and you return to the front counter."
    return