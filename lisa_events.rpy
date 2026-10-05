#Lisa Events
label Lisa_Stage_0_Event:
    ##Text message ###
    "You receive a message on your phone from Marie."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Marie', dialogue=dialogue_one)
    $ msg ("Hello [playername].", who=1)
    pause
    $ msg ("We have a free shift going that should be pretty quiet.", who=1)
    pause
    $ msg ("I was wondering if you would be interested in picking it up and working with Lisa?", who=1)
    pause
    $ msg ("Sure, I'll be there in a minute.")
    pause
    $ msg ("Great, see you soon.", who=1)
    pause
    $ hide_messenger()

    ###Bunny bites###
    image lisa_stage_0_event_1 = "/lisa/events/stage0/1.webp"
    scene lisa_stage_0_event_1
    play music "/music/bunny_bites.ogg" if_changed
    "Walking in it seems pretty quiet today."
    pc "Hello?"
    image lisa_stage_0_event_2 = "/lisa/events/stage0/2.webp"
    scene lisa_stage_0_event_2
    lisa "Oh sorry, I didn’t hear you come in."
    image lisa_stage_0_event_3 = "/lisa/events/stage0/3.webp"
    scene lisa_stage_0_event_3
    lisa "So Marie said she had run through everything with you, how are you feeling?"
    pc "Yeah good, ready to start working."
    lisa "Great, well today is probably going to be a quiet one."
    image lisa_stage_0_event_4 = "/lisa/events/stage0/4.webp"
    scene lisa_stage_0_event_4
    lisa "Do you think you can handle the till and customers orders, I’ll manage everything else and run the food out to them."
    pc "Yeah that sounds great."
    image lisa_stage_0_event_5 = "/lisa/events/stage0/5.webp"
    scene lisa_stage_0_event_5
    "Going behind the counter, you wait for the customers to start arriving."
    if recollection == False:
        $ rngworkgirl = 2
        $ lisa_work_today = 1
        $ marie_work_today = 1
        $ amber_work_today = 1
        $ bonnie_work_today = 1
        call work_randomizer from _call_work_randomizer_40
        "A while later."
        call work_randomizer from _call_work_randomizer_41
        "You work your ass off until closing time."
    else:
        "You work until closing time."

    ##Lisa appears at the till ###
    image lisa_stage_0_event_6 = "/lisa/events/stage0/6.webp"
    scene lisa_stage_0_event_6
    lisa "I think we can close for today."
    lisa "You did great!"
    pc "Thanks."
    image lisa_stage_0_event_7 = "/lisa/events/stage0/7.webp"
    scene lisa_stage_0_event_7
    "Closing up for the day, you notice Lisa next to you."
    lisa "So, I guess this is the first time you have been here at closing time?"
    pc "Yeah."
    image lisa_stage_0_event_8 = "/lisa/events/stage0/8.webp"
    scene lisa_stage_0_event_8
    lisa "Ok, there isn’t anything major that you will need to do here."
    lisa "Just a case of cleaning everything ready for tomorrow."
    pc "Sounds simple enough."
    image lisa_stage_0_event_9 = "/lisa/events/stage0/9.webp"
    scene lisa_stage_0_event_9
    lisa "It is, we keep the supplies back there in the store room."
    lisa "But it’s just a case of sweeping up, mopping and wiping down."
    pc "Sweep, mop, wipe."
    image lisa_stage_0_event_10 = "/lisa/events/stage0/10.webp"
    scene lisa_stage_0_event_10
    lisa "You got it."
    lisa "It’s all food safe so nothing to worry about there either."
    lisa "The only other thing is totalling up the till and putting the money in the safe."
    lisa "But I don't think you will have to worry about that, at least for now."
    pc "Ok, I think I can handle cleaning up here if you want to do that."
    lisa "Sounds good to me."
    image lisa_stage_0_event_11 = "/lisa/events/stage0/11.webp"
    scene lisa_stage_0_event_11
    "Grabbing the mop you take your time cleaning the restaurant while Lisa finishes up the admin."

    ###Lisa in normal clothes.###
    image lisa_stage_0_event_12 = "/lisa/events/stage0/12.webp"
    scene lisa_stage_0_event_12
    lisa "Looks spotless."
    pc "Thanks."
    image lisa_stage_0_event_13 = "/lisa/events/stage0/13.webp"
    scene lisa_stage_0_event_13
    lisa "I think that’s everything we need to do."
    lisa "I don't know if Marie has any more training planned, but I think you are ready to start working here."
    pc "Great."
    image lisa_stage_0_event_14 = "/lisa/events/stage0/14.webp"
    scene lisa_stage_0_event_14
    lisa "Yeah, just let us know when you want to work and we can sort it out."
    pc "Will do. Thanks Lisa."
    lisa "Bye."
    if recollection == False:
        $ money += 10
        "You earned ten dollars."
        $ daytime += 1
        $ hari_work_today = 0
        $ marie_work_today = 0
        $ lisa_work_today = 0
        $ amber_work_today = 0
        $ luna_work_today = 0
        $ daisy_work_today = 0
        $ leanne_work_today = 0
        $ bonnie_work_today = 0
        $ librarian_work_today = 0
        $ cayenne_work_today = 0
        $ maya_work_today = 0
        $ katrine_work_today = 0
        $ trista_work_today = 0
        $ caroline_work_today = 0
        $ roxie_work_today = 0
        $ natalie_work_today = 0
        $ charlene_work_today = 0
        $ sally_work_today = 0
        $ britta_work_today = 0
        $ rebecca_work_today = 0
        $ mylenna_work_today = 0
        $ worked_today = 1
    $ lisastage0event = 0
    stop music fadeout 1.0
    return

label Lisa_Stage_1_Event_1:
    ## Lisa 1.1 - Stock take ##
    #### While working a regular shift ###
    ###Lisa joins you at the counter in an empty restaurant ###
    image lisa_stage_1_event_1 = "/lisa/events/stage1/1.webp"
    scene lisa_stage_1_event_1
    play music "/music/bunny_bites.ogg" if_changed
    lisa "Hey [playername], how is it going?"
    pc "Seems pretty slow today."
    lisa "Yeah, I was thinking the same thing."
    lisa "I was going to do a stock take, see what we need to order."
    image lisa_stage_1_event_2 = "/lisa/events/stage1/2.webp"
    scene lisa_stage_1_event_2
    lisa "Since it's kind of dead around here, want to join me and I can show you how to do it?"
    pc "Sure thing, it would be good to learn more about how things work around here."
    lisa "Great, I will just pop a sign on the door and we can get started."

    ### Back room ####
    image lisa_stage_1_event_3 = "/lisa/events/stage1/3.webp"
    scene lisa_stage_1_event_3
    "Putting a back in 5 minutes sign on the front door, you join Lisa in the stock room."
    lisa "So, the first thing we need to do is get an accurate count of what is in here."
    lisa "We have this sheet here which has the minimum number we need. So if it is less than that number, we need to order some."
    pc "Sounds simple enough."
    image lisa_stage_1_event_4 = "/lisa/events/stage1/4.webp"
    scene lisa_stage_1_event_4
    lisa "It’s super simple so don't worry, it can just take a while to get it done."
    lisa "Right then, let’s start with burger buns, how many do we have?"
    "Looking through the shelf you find a couple of boxes."
    image lisa_stage_1_event_5 = "/lisa/events/stage1/5.webp"
    scene lisa_stage_1_event_5
    pc "Looks like two unopened boxes and one that is half full."
    lisa "Perfect, the minimum we need is 4 boxes. So that item goes on the order list."
    lisa "What about napkins."
    pc "Seems like we have about 3 boxes."
    image lisa_stage_1_event_6 = "/lisa/events/stage1/6.webp"
    scene lisa_stage_1_event_6
    lisa "There are loads per box so we don't need to worry about them."
    lisa "What about…take away boxes, they should be up there too."
    pc "One box, looks mostly full for the pizza size ones and then one box and a few extras for the little burger style ones."
    lisa "Ok great, we have been selling a lot of those this week so it is no surprise we need more."
    lisa "Next."
    image lisa_stage_1_event_7 = "/lisa/events/stage1/7.webp"
    scene lisa_stage_1_event_7
    "Running through the long list of items you help Lisa complete the stock check."
    "You make short work of the job with you checking stock levels and Lisa writing them down."
    "Filling the last of the form in, you head back out to the restaurant."

    ### Back out by the counter ###
    image lisa_stage_1_event_8 = "/lisa/events/stage1/8.webp"
    scene lisa_stage_1_event_8
    lisa "Phew, I think we have earned a quick break before we reopen."
    lisa "I’m going to chuck a couple of burgers on, why don't you grab a table."

    ### At a table ###
    image lisa_stage_1_event_9 = "/lisa/events/stage1/9.webp"
    scene lisa_stage_1_event_9
    "Finding a table, a few minutes later Lisa joins you. Placing down two burgers and fries for you both."
    image lisa_stage_1_event_10 = "/lisa/events/stage1/10.webp"
    scene lisa_stage_1_event_10
    lisa "Thanks for your help today, it went by much quicker than usual."
    pc "No need to thank me, I appreciate you taking the time to show me how to do it."
    image lisa_stage_1_event_11 = "/lisa/events/stage1/11.webp"
    scene lisa_stage_1_event_11
    "Taking a bite out of her burger, Lisa smiles back at you."
    pc "So, what do you do when you are not working here?"
    image lisa_stage_1_event_12 = "/lisa/events/stage1/12.webp"
    scene lisa_stage_1_event_12
    lisa "Oh… not much really."
    pc "No hobbies or things you do for fun?"
    lisa "Well, I like photography but haven’t done much with it lately."
    lisa "I mostly sit around playing video games and watching sports, which is a bit boring."
    pc "That doesn’t sound boring to me, it sounds like a great time."
    image lisa_stage_1_event_13 = "/lisa/events/stage1/13.webp"
    scene lisa_stage_1_event_13
    lisa "You like them too?"
    pc "More of the video games than sport, but yeah I play all the time."
    pc "Or I did when I had time, been quite busy lately. We should totally play together sometime."
    lisa "I’d love too, what sort of things do you…"
    "Your conversation is interrupted by a knock from the door."
    image lisa_stage_1_event_14 = "/lisa/events/stage1/14.webp"
    scene lisa_stage_1_event_14
    lisa "Damn, well I guess we should probably get back to work anyway."
    image lisa_stage_1_event_15 = "/lisa/events/stage1/15.webp"
    scene lisa_stage_1_event_15
    "Scoffing the last burger, you worry she is going to choke but it seems like working here has made her an expert at eating quickly between customers."
    image lisa_stage_1_event_16 = "/lisa/events/stage1/16.webp"
    scene lisa_stage_1_event_16
    pc "Thanks for the burgers."
    lisa "No problem, we should pick this up later."
    ### Go back to working a regular shift.###
    if recollection == True:
        stop music fadeout 1.0
    $ lisastage1event = 0
    return


label Lisa_Stage_1_Event_2:
    #First weekend sitdown with Lisa
    image lisa_idle_workattire_event1 = "/lisa/1/idle_workattire.webp"
    scene lisa_idle_workattire_event1
    play music "/music/bunny_bites.ogg" if_changed
    lisa "Could you stay and hang out with me for a bit before leaving?"
    pc "Sure!"
    image lisa_afterwork_sitdown1_event1 = "/lisa/1/afterwork_sitdown1.webp"
    scene lisa_afterwork_sitdown1_event1
    "Lisa sits down in one of the booths."
    lisa "Ahhh, it feels good to relax after a long day of work."
    image lisa_afterwork_sitdown2_event1 = "/lisa/1/afterwork_sitdown2.webp"
    scene lisa_afterwork_sitdown2_event1
    lisa "Well, I've still got a bit of cleaning to do, but that's no big deal."
    lisa "Hey, can you keep a secret?"
    image lisa_afterwork_sitdown3_event1 = "/lisa/1/afterwork_sitdown3.webp"
    scene lisa_afterwork_sitdown3_event1
    lisa "I need your word that you won't repeat this to anyone."
    pc "I won't tell anyone, you can trust me."
    image lisa_afterwork_sitdown4_event1 = "/lisa/1/afterwork_sitdown4.webp"
    scene lisa_afterwork_sitdown4_event1
    lisa "Alright sooooo...I'm lesbian."
    lisa "And I have a huge crush on both Marie and Amber."
    image lisa_afterwork_sitdown5_event1 = "/lisa/1/afterwork_sitdown5.webp"
    scene lisa_afterwork_sitdown5_event1
    lisa "The way they smile, the way they walk, even the way their faces look when they're sad or angry."
    lisa "I just can't stop thinking about them and I know I should because there's no way either of them likes me back."
    image lisa_afterwork_sitdown6_event1 = "/lisa/1/afterwork_sitdown6.webp"
    scene lisa_afterwork_sitdown6_event1
    pc "Well, you don't know that."
    pc "Maybe one of them likes you too."
    lisa "Do you think so?"
    pc "Well, I can't really say, but there's one way to find out. Talk to them about it - about your feelings for them."
    lisa "Thanks for the advice, I need to build courage to have that conversation, but I think I can do it."
    pc "I believe you can do it too."
    lisa "Thanks, that means a lot. Now could you help me clean up?"
    pc "Yeah, of course."
    "Lisa and you clean up the whole place."
    image lisa_afterwork_sitdown7_event1 = "/lisa/1/afterwork_sitdown7.webp"
    scene lisa_afterwork_sitdown7_event1
    lisa "Thanks for the help."
    lisa "And thanks for the impromptu pep talk."
    pc "For sure, I'm always here if you need a talk."
    lisa "You're such a sweetheart haha. Have a good night, [playername]."
    pc "Good night, Lisa."
    stop music fadeout 1.0
    $ lisastage1event2 = 0
    return

label Lisa_Stage_2_Event_1:
    ## Lisa 2.1 Menu choices ##
    #### At the end of working a regular shift with Lisa sat at the table with a menu##
    image lisa_stage_2_event_13 = "/lisa/events/stage2/13.webp"
    scene lisa_stage_2_event_13
    play music "/music/bunny_bites.ogg" if_changed
    "Cleaning up after a long day, you notice Lisa deep in thought at one of the tables."
    "Deciding to see if she is ok, you make your way over."
    image lisa_stage_2_event_14 = "/lisa/events/stage2/14.webp"
    scene lisa_stage_2_event_14
    pc "Hey Lisa, everything ok?"
    lisa "Oh hi, yeah everything is fine."
    lisa "Marie asked me to go through the menu and look for anyways to update it."
    pc "In what way?"
    image lisa_stage_2_event_15 = "/lisa/events/stage2/15.webp"
    scene lisa_stage_2_event_15
    lisa "Like changes to existing items or maybe some new things, but I am struggling to come up with much."
    pc "Want any help?"
    lisa "Sure that would be great."
    image lisa_stage_2_event_16 = "/lisa/events/stage2/16.webp"
    scene lisa_stage_2_event_16
    "Lisa takes you through everything she has so far."
    lisa "Removing items is easy, we can just look at what isn’t selling and stop selling them."
    pc "Like the fish tacos."
    lisa "Exactly, although I think that’s only on the menu because I once told Marie I liked them."
    lisa "But it doesn't seem like anyone else does."
    pc "What about the spaghetti, doesn't seem like many people order that."
    image lisa_stage_2_event_17 = "/lisa/events/stage2/17.webp"
    scene lisa_stage_2_event_17
    lisa "True, but it just feels like something we should offer, doesn't it?"
    pc "I know what you mean, but if it’s not selling is it worth it?"
    lisa "You have a good point."
    "Drawing a line through it Lisa updates the menu."
    image lisa_stage_2_event_18 = "/lisa/events/stage2/18.webp"
    scene lisa_stage_2_event_18
    lisa "Now we just need to think of some things to add."
    "Thinking for a few minutes, it's easy to see why she was struggling."
    pc "This is surprisingly difficult."
    lisa "I know right."
    pc "Pizza sells well, what about Calzones?"
    image lisa_stage_2_event_19 = "/lisa/events/stage2/19.webp"
    scene lisa_stage_2_event_19
    lisa "We tried that, most people just ordered the pizza anyway."
    pc "Oh ok."
    pc "Maybe it’s good as it is. People know what to expect when they come here."
    lisa "True, but I think it could still do with something extra?"
    pc "What about desserts?"
    image lisa_stage_2_event_20 = "/lisa/events/stage2/20.webp"
    scene lisa_stage_2_event_20
    lisa "I love desserts, but last time we tried we were kind of out competed by the number of other shops that sell them."
    pc "Could it be worth another go?"
    lisa "Yeah, and if nothing else it will give me a reason to eat them."
    lisa "I’ll put a couple down and Marie can always take them off if she doesn't like the idea."
    image lisa_stage_2_event_21 = "/lisa/events/stage2/21.webp"
    scene lisa_stage_2_event_21
    "Taking a few more minutes, you both go through the menu but no more inspiration hits."
    pc "I am sorry, I think that is all I have."
    image lisa_stage_2_event_22 = "/lisa/events/stage2/22.webp"
    scene lisa_stage_2_event_22
    lisa "No problem, I am probably overthinking it anyway."
    lisa "I just really wanted to do a good job for Marie."
    image lisa_stage_2_event_23 = "/lisa/events/stage2/23.webp"
    scene lisa_stage_2_event_23
    lisa "Thanks for your help though."
    pc "No problem."
    "Finishing up cleaning the restaurant you head home for the night."
    stop music fadeout 1.0
    $ lisastage2event = 0
    return


label Lisa_Stage_2_Event_2:
    image lisa_idle_workattire_event2 = "/lisa/2/idle_workattire.webp"
    scene lisa_idle_workattire_event2
    play music "/music/bunny_bites.ogg" if_changed
    lisa "Could you stay and hang out with me for a bit before leaving?"
    pc "Sure!"
    image lisa_afterwork_sitdown1_event2 = "/lisa/2/afterwork_sitdown1.webp"
    scene lisa_afterwork_sitdown1_event2
    "Lisa sits down in one of the booths."
    lisa "Ahhh it feels good to relax after a long day of work."
    image lisa_afterwork_sitdown2_event2 = "/lisa/2/afterwork_sitdown2.webp"
    scene lisa_afterwork_sitdown2_event2
    lisa "Well I've still got a bit of cleaning to do but that's no big deal."
    pc "You look like you want to ask me something."
    image lisa_afterwork_sitdown3_event2 = "/lisa/2/afterwork_sitdown3.webp"
    scene lisa_afterwork_sitdown3_event2
    lisa "Well, I really wanted to ask if you'd like to go for a drink, maybe after we finish cleaning?"
    pc "Sure Lisa, I'd love that, just name the place and I'll be there."
    image lisa_afterwork_sitdown4_event2 = "/lisa/2/afterwork_sitdown4.webp"
    scene lisa_afterwork_sitdown4_event2
    lisa "It’s a cocktail lounge not far from here, I think you'd like it."
    image lisa_afterwork_sitdown5_event2 = "/lisa/2/afterwork_sitdown5.webp"
    scene lisa_afterwork_sitdown5_event2
    pc "Sounds good, you've got yourself a date!"
    image lisa_afterwork_sitdown6_event2 = "/lisa/2/afterwork_sitdown6.webp"
    scene lisa_afterwork_sitdown6_event2
    "Lisa and you clean up the whole place."
    image lisa_afterwork_sitdown7_event2 = "/lisa/2/afterwork_sitdown7.webp"
    scene lisa_afterwork_sitdown7_event2
    lisa "I'll see you at the cocktail lounge."
    pc "See you there."
    stop music fadeout 1.0
    image lisa_stage_2_event_1 = "/lisa/events/stage2/1.webp"
    scene lisa_stage_2_event_1
    play music "<loop 0.2 from 39>/music/generic_date.ogg" if_changed fadein 1.0
    "When you arrive at the cocktail lounge, you find that Lisa is already there and has gotten a table."
    "She even ordered food and drinks for the two of you. You're surprised to see her order beer for herself, for some reason you had her down as a cocktail type of girl."
    "There's a plate with four burgers."
    image lisa_stage_2_event_2 = "/lisa/events/stage2/2.webp"
    scene lisa_stage_2_event_2
    "Even though you're not very hungry you thank Lisa for the gesture and start sipping on your own beer."
    pc "So, any updates on the situation with the girls? Have you told them about your crush yet?"
    image lisa_stage_2_event_3 = "/lisa/events/stage2/3.webp"
    scene lisa_stage_2_event_3
    "Lisa looks up nervously from the burger she's just taken a bite out of. She chews and swallows before explaining."
    lisa "Well...I dropped a few hints the other day. Complimenting Amber's hair, a suggestive wink at Marie, but I don't know if they picked up on it."
    image lisa_stage_2_event_4 = "/lisa/events/stage2/4.webp"
    scene lisa_stage_2_event_4
    "Lisa looks embarrassed."
    lisa "I haven't really been able to talk to them since. I'm too scared."
    pc "Don't be, everything's gonna be fine."
    image lisa_stage_2_event_5 = "/lisa/events/stage2/5.webp"
    scene lisa_stage_2_event_5
    lisa "I hope so..."
    "Lisa is clearly nervous about this so you decide to change the subject."
    pc "So, if you had to eat only one food for the rest of your life what would it be?"
    image lisa_stage_2_event_6 = "/lisa/events/stage2/6.webp"
    scene lisa_stage_2_event_6
    "Pretty lame, but it seemed to take Lisa's mind off her anxieties."
    lisa "Oh, definitely chocolate! I love love love chocolate!"
    pc "Have you been to the Sweet Shop? They've got some really great stuff there."
    lisa "I've never been but my friend said it was really good. She got this cake from there and it had like two types of chocolate frosting and sprinkles and..."
    image lisa_stage_2_event_7 = "/lisa/events/stage2/7.webp"
    scene lisa_stage_2_event_7
    "The two of you keep talking for a while as you eat. Or rather while Lisa eats, since you're not hungry."
    "Realizing you haven't touched a burger, you decide to offer it to Lisa."
    image lisa_stage_2_event_8 = "/lisa/events/stage2/8.webp"
    scene lisa_stage_2_event_8
    "But when you look down at the plate, it's empty!"
    image lisa_stage_2_event_9 = "/lisa/events/stage2/9.webp"
    scene lisa_stage_2_event_9
    "You look back at Lisa and the last burger that she's currently placing into her mouth."
    image lisa_stage_2_event_10 = "/lisa/events/stage2/10.webp"
    scene lisa_stage_2_event_10
    lisa "Ahhh, that was great. I'd order some dessert but then you'd have to roll me home haha."
    "You try not to stare too long at her bloated tummy as she rubs it."
    image lisa_stage_2_event_11 = "/lisa/events/stage2/11.webp"
    scene lisa_stage_2_event_11
    lisa "Well, I should probably get going. Thanks so much for the company, I'll see you at work!"
    pc "Yep, see you later, Lisa."
    image lisa_stage_2_event_12 = "/lisa/events/stage2/12.webp"
    scene lisa_stage_2_event_12
    "She leaves money for the bill. Then she walks away, cradling her gut."
    stop music fadeout 1.0

    if recollection == False:
        $ lisa.weight += 0.5
    $ lisastage2event2 = 0
    return


label Lisa_Stage_3_Event_1:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Lisa', dialogue=dialogue_one)
    $ msg ("Hi, [playername]. Could you come to my house? I have something I want to talk with you about.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sure. What is the address?")
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright. Another time.", who=1)
            pause
            $ hide_messenger()
            return
    "Lisa sends over her address and you start to make your way over to her."
    image lisa_home_arrive_event3 = "/lisa/3/home_arrive.webp"
    scene lisa_home_arrive_event3
    lisa "Hey, [playername]. Thanks for coming on such short notice."
    pc "No problem, what did you want to talk about?"
    image lisa_home_question_event3 = "/lisa/3/home_question.webp"
    scene lisa_home_question_event3
    lisa "Do you remember me talking about having a crush on the girls?"
    pc "Yes. Did you talk to them about it?"
    lisa "I did. The response was quite surprising."
    lisa "Amber said that she never really thought about being with a woman and she isn't sure if she is open to such a thing."
    lisa "While Marie first needed some time to think about it, but later came back to me that she felt embarrassed to admit it but she likes bigger woman."
    lisa "She asked me if I would be open to gain a bit of weight. She thinks we could be together if I had a bit more meat on my bones."
    pc "That is surprising. What do you think?"
    lisa "That is why I asked you here. I decided that I will try gaining a few pounds to see how it feels and hopefully get together with Marie."
    lisa "But I need your help to gain weight. I need you to encourage and push me to eat and drink more."
    lisa "I know it is weird, but I really want this."
    pc "I will gladly help you."
    lisa "I knew I could count on you. Thank you!"
    lisa "So in order to get started I bought some meal packages from Bonnie's shop."
    "She grabs the meal packages and sits down on her sofa."
    image lisa_home_eating_event3 = "/lisa/3/home_eating.webp"
    scene lisa_home_eating_event3
    "Lisa starts chewing through the sweets she bought."
    "During her feeding you try your best to make the process as fast and as frictionless as possible by handing her the food whenever her hands are empty."
    image lisa_home_strip_event3 = "/lisa/3/home_strip.webp"
    scene lisa_home_strip_event3
    lisa "Let me open up these pants to make some room for more food."
    "Lisa opens up her pants to let out her slightly bloated-looking belly."
    "It is clear that Lisa is serious about being willing to gain weight for Marie."
    lisa "Now, let's continue the feeding."
    image lisa_home_stripeating_event3 = "/lisa/3/home_stripeating.webp"
    scene lisa_home_stripeating_event3
    "Her pace never really slows down. She is determined to finish what she bought."
    "Sadly, after a few more minutes you hand her the final item."
    image lisa_home_stuffed_event3 = "/lisa/3/home_stuffed.webp"
    scene lisa_home_stuffed_event3
    window hide
    pause
    lisa "I think this was a good start."
    "Lisa looks satisfied with her bloated belly."
    lisa "Are you available to do this more often?"
    pc "Yes. Just text me whenever you want to do this."
    lisa "Thank you. Now I will have to digest this food baby for a while."
    "You help clean up the left behind food packages and then say your goodbyes."
    #unlocks repeatable feeding at Lisa her home.
    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
        $ lisa.weight += 0.5
    $ lisastage3event = 0
    return

label Lisa_Stage_3_Event_2:
    ## Lisa stage 3.2 technical difficulties ##
    #### Going into work with Lisa at the front desk###
    image lisa_stage_3_event_1 = "/lisa/events/stage3/1.webp"
    scene lisa_stage_3_event_1
    play music "/music/bunny_bites.ogg" if_changed
    lisa "Stupid thing!"
    pc "Hey Lisa, what’s going on?"
    image lisa_stage_3_event_2 = "/lisa/events/stage3/2.webp"
    scene lisa_stage_3_event_2
    lisa "The till is being its typically stupid self, useless hunk of junk."
    lisa "I keep telling Marie to get us the new model but she doesn't."
    lisa "And now the entire system has gone down and I can't get through to the help desk and Marie isn’t answering her phone."
    pc "It will be ok, don't worry."
    pc "There are some notepads under the counter."
    pc "This happened to me a while ago and Marie just said to use them to take orders manually."
    image lisa_stage_3_event_3 = "/lisa/events/stage3/3.webp"
    scene lisa_stage_3_event_3
    lisa "Really, oh ok. I should have guessed she would have a back up."
    lisa "But Marie has usually been here to sort it herself."
    image lisa_stage_3_event_4 = "/lisa/events/stage3/4.webp"
    scene lisa_stage_3_event_4
    lisa "So thanks, I have been fighting this thing all morning."
    pc "Want me to take over then, sounds like you could do with a break."
    image lisa_stage_3_event_5 = "/lisa/events/stage3/5.webp"
    scene lisa_stage_3_event_5
    lisa "That would be amazing, thank you."

    ### images of a work day ###
    image lisa_stage_3_event_6 = "/lisa/events/stage3/6.webp"
    scene lisa_stage_3_event_6
    "With the till down, it takes a bit longer to fulfil orders in the slight chaos of the day."
    image lisa_stage_3_event_7 = "/lisa/events/stage3/7.webp"
    scene lisa_stage_3_event_7
    "However, with you writing them down and Lisa dealing with the food you make a good team."
    image lisa_stage_3_event_8 = "/lisa/events/stage3/8.webp"
    scene lisa_stage_3_event_8
    "Despite the added difficulty, everything seems to work out for the day."

    if recollection == False:
        $ money += 10
        "You earned ten dollars."

    ### lisa at the desk ###
    image lisa_stage_3_event_9 = "/lisa/events/stage3/9.webp"
    scene lisa_stage_3_event_9
    lisa "Phew, we are officially closed."
    pc "That was a bit crazy, but I think we managed fine."
    image lisa_stage_3_event_10 = "/lisa/events/stage3/10.webp"
    scene lisa_stage_3_event_10
    lisa "Yeah, we did great."
    lisa "Fancy going out tonight, I wouldn’t mind letting someone else bring me food for a change."
    pc "Sure, that sounds good to me."
    image lisa_stage_3_event_11 = "/lisa/events/stage3/11.webp"
    scene lisa_stage_3_event_11
    lisa "Great, let's get cleaned up here and head out."
    image lisa_stage_3_event_12 = "/lisa/events/stage3/12.webp"
    scene lisa_stage_3_event_12
    "Quickly sweeping the floor and wiping down the tables you and Lisa head out."
    image lisa_stage_3_event_13 = "/lisa/events/stage3/13.webp"
    scene lisa_stage_3_event_13
    pause
    stop music fadeout 1.0

    ### inside same location as stage 2 ###
    image lisa_stage_3_event_14 = "/lisa/events/stage3/14.webp"
    scene lisa_stage_3_event_14
    play music "<loop 0.2 from 39>/music/generic_date.ogg" if_changed fadein 1.0
    pause
    image lisa_stage_3_event_15 = "/lisa/events/stage3/15.webp"
    scene lisa_stage_3_event_15
    "Quickly finding a table, you order some drinks and food."
    image lisa_stage_3_event_16 = "/lisa/events/stage3/16.webp"
    scene lisa_stage_3_event_16
    lisa "So, do you have any fun plans for the weekend?"
    pc "Not really, although you never know what might happen."
    lisa "So you are a spontaneous kind of person?"
    pc "Sometimes, I just mean it has been hard to predict what is going to happen these days."
    image lisa_stage_3_event_17 = "/lisa/events/stage3/17.webp"
    scene lisa_stage_3_event_17
    lisa "I know what you mean, things seem to have been really busy lately."
    lisa "But you go to the university in town right, how are your classes going?"
    pc "Pretty well recently, guess I have finally found something that interests me."
    lisa "That’s great, it is always good to find something you are genuinely interested in."
    image lisa_stage_3_event_18 = "/lisa/events/stage3/18.webp"
    scene lisa_stage_3_event_18
    "Your small talk is interrupted as a plate of food arrives, a series of burgers being placed in front of Lisa."
    image lisa_stage_3_event_19 = "/lisa/events/stage3/19.webp"
    scene lisa_stage_3_event_19
    lisa "I hope you don't mind?"
    pc "No, not at all."
    image lisa_stage_3_event_20 = "/lisa/events/stage3/20.webp"
    scene lisa_stage_3_event_20
    "Taking a bite out of a burger Lisa mumbles in delight."
    lisa "These are so good!"
    pc "Better than the ones we sell?"
    image lisa_stage_3_event_21 = "/lisa/events/stage3/21.webp"
    scene lisa_stage_3_event_21
    lisa "No comment…"
    pc "What about you, any plans?"
    image lisa_stage_3_event_22 = "/lisa/events/stage3/22.webp"
    scene lisa_stage_3_event_22
    lisa "Probably go and see the family, it's been a few weeks."
    pc "Do they live here in town?"
    lisa "Some of them, most of my brothers have moved elsewhere though."
    pc "Sounds like you have a pretty big family."
    image lisa_stage_3_event_23 = "/lisa/events/stage3/23.webp"
    scene lisa_stage_3_event_23
    lisa "Yeah, four brothers and one sister."
    lisa "I’m the youngest, but there is only about a year between each of us so my oldest brother is only 6 years older."
    lisa "It was a bit of a crazy house growing up, I just felt bad for my mum."
    pc "A lot of kids to wrangle."
    image lisa_stage_3_event_24 = "/lisa/events/stage3/24.webp"
    scene lisa_stage_3_event_24
    lisa "Yeah, plus I think she really wanted another girly daughter. But, I ended up taking after my brothers more than her."
    lisa "She wanted to get me into figure skating like her and my sister."
    image lisa_stage_3_event_25 = "/lisa/events/stage3/25.webp"
    scene lisa_stage_3_event_25
    pc "How did that go?"
    image lisa_stage_3_event_26 = "/lisa/events/stage3/26.webp"
    scene lisa_stage_3_event_26
    lisa "Unfortunately for her, I had more…violent intentions so got into hockey instead."
    pc "I didn't take you for the violent type."
    lisa "Oh I'm not, or at least I hope I am not."
    lisa "I Just had a lot of frustration growing up, four brothers and a sister, and as the youngest my mum always wanted to make me her little princess."
    pc "I guess you weren't interested in that?"
    image lisa_stage_3_event_27 = "/lisa/events/stage3/27.webp"
    scene lisa_stage_3_event_27
    lisa "When I was five sure but I always had more in common with my brothers, in more than one way."
    lisa "But that is enough about me, what about you?"
    pc "Much more boring, only child so not much to say."
    pc "A lot of video games, books and using my imagination."
    image lisa_stage_3_event_28 = "/lisa/events/stage3/28.webp"
    scene lisa_stage_3_event_28
    lisa "Sounds nice if you ask me, don't have to fight over who gets the dodgy third party controller."
    lisa "So what do you play?"
    image lisa_stage_3_event_29 = "/lisa/events/stage3/29.webp"
    scene lisa_stage_3_event_29
    "Lisa eats another burger as if it is a small snack."
    pc "Anything really."
    image lisa_stage_3_event_30 = "/lisa/events/stage3/30.webp"
    scene lisa_stage_3_event_30
    lisa "NHL?"
    pc "Haven’t played it before but I’m sure I can pick it up well enough to beat you."
    image lisa_stage_3_event_31 = "/lisa/events/stage3/31.webp"
    scene lisa_stage_3_event_31
    lisa "That's fighting talk, you're on."
    lisa "Next time you come over, I’ll show you who the real boss is around here."
    pc "That would be Marie, right?"
    image lisa_stage_3_event_32 = "/lisa/events/stage3/32.webp"
    scene lisa_stage_3_event_32
    lisa "Always trying to be a smartass."
    pc "Sorry, can't help it."
    image lisa_stage_3_event_33 = "/lisa/events/stage3/33.webp"
    scene lisa_stage_3_event_33
    "Lisa quickly eats her last burger."
    pc "How about I get you a second round of burgers, to make up for being stuck with me as company."
    image lisa_stage_3_event_34 = "/lisa/events/stage3/34.webp"
    scene lisa_stage_3_event_34
    "Looking down at her empty plates, Lisa puts a hand on her already stuffed belly."
    lisa "I don't know, I am already feeling full."
    pc "I thought you wanted help, for Marie?"
    image lisa_stage_3_event_35 = "/lisa/events/stage3/35.webp"
    scene lisa_stage_3_event_35
    lisa "Oh I do, but I also don't want to go absolutely crazy."
    lisa "That was already double what I usually eat."
    lisa "But I appreciate that you are looking out for me, I guess I am still getting used to things and the idea of gaining weight on purpose."
    image lisa_stage_3_event_36 = "/lisa/events/stage3/36.webp"
    scene lisa_stage_3_event_36
    lisa "I realise this is probably confusing given what I have been asking of you, feeding me at my place."
    lisa "Being completely honest I broke a button off my favourite jeans this morning trying to put them on, it made me realise how much I have gained recently."
    "It is clear that while she has feelings for Marie and plans to gain, she still seems a little conflicted about it."
    pc "You don't have to apologise to me, I only want to help you."
    image lisa_stage_3_event_37 = "/lisa/events/stage3/37.webp"
    scene lisa_stage_3_event_37
    lisa "I know and that's super sweet and I am really grateful to have you as a friend."
    lisa "You have really been there when I need someone to talk to, I hope you know how much that means to me."
    pc "That’s what friends are for, right?"
    image lisa_stage_3_event_38 = "/lisa/events/stage3/38.webp"
    scene lisa_stage_3_event_38
    lisa "Anyway, it is getting late and I guess I have some thinking to do."
    lisa "Thanks for tonight, I really enjoyed it."
    pc "I had fun, thanks for inviting me."
    image lisa_stage_3_event_39 = "/lisa/events/stage3/39.webp"
    scene lisa_stage_3_event_39
    "Saying your goodbyes, you head home for the night."
    stop music fadeout 1.0
    if recollection == False:
        $ lisa.weight += 0.5
    $ lisastage3event2 = 0
    return

label Lisa_Stage_4_Event_1:
    ## Lisa stage 4.1 - variation on feeding event ##
    ### Regular text message for feeding event at her place.###
    "You make your way to Lisa’s home."
    image lisa_stage_4_event_76 = "/lisa/events/stage4/76.webp"
    scene lisa_stage_4_event_76
    lisa "Hey [playername], thanks for coming."
    lisa "Did you bring the extra food?"
    pc "Yes I did."
    image lisa_stage_4_event_77 = "/lisa/events/stage4/77.webp"
    scene lisa_stage_4_event_77
    lisa "Great, let's get started then."
    image lisa_stage_4_event_78 = "/lisa/events/stage4/78.webp"
    scene lisa_stage_4_event_78
    "Sitting down next to her, you hesitate for a moment."
    lisa "Everything ok?"
    pc "Yeah, I just wanted to check you were ok with this."
    image lisa_stage_4_event_79 = "/lisa/events/stage4/79.webp"
    scene lisa_stage_4_event_79
    lisa "Why wouldn’t I be?"
    pc "You said before you were having a hard time with it, so I just wanted to make sure you still wanted this."
    lisa "Oh, you don't need to worry about that."
    image lisa_stage_4_event_80 = "/lisa/events/stage4/80.webp"
    scene lisa_stage_4_event_80
    lisa "I think I was just having a hard time coming to terms with how fast my body was changing."
    lisa "It was honestly a little unsettling, but now I kind of like it."
    image lisa_stage_4_event_81 = "/lisa/events/stage4/81.webp"
    scene lisa_stage_4_event_81
    lisa "Plus, Marie can barely keep her eyes off me."
    image lisa_stage_4_event_82 = "/lisa/events/stage4/82.webp"
    scene lisa_stage_4_event_82
    lisa "Even when I am serving I can feel her staring at me, she is so easy to tease."
    image lisa_stage_4_event_83 = "/lisa/events/stage4/83.webp"
    scene lisa_stage_4_event_83
    lisa "It’s like, Oops, let me check that for you sir."
    image lisa_stage_4_event_84 = "/lisa/events/stage4/84.webp"
    scene lisa_stage_4_event_84
    "Lisa bends over away from you, pretending to pick something up off a table and giving you a perfect view of her growing ass."
    image lisa_stage_4_event_85 = "/lisa/events/stage4/85.webp"
    scene lisa_stage_4_event_85
    lisa "Or my favourite, I just need to grab…"
    image lisa_stage_4_event_86 = "/lisa/events/stage4/86.webp"
    scene lisa_stage_4_event_86
    "Reaching past you to grab an imaginary object you get a perfect view down her loose fitting top."
    image lisa_stage_4_event_87 = "/lisa/events/stage4/87.webp"
    scene lisa_stage_4_event_87
    lisa "Although that one definitely works better in this compared to the suit we wear at work."
    pc "Uh yeah…"
    image lisa_stage_4_event_88 = "/lisa/events/stage4/88.webp"
    scene lisa_stage_4_event_88
    lisa "Geez, you are as bad as her."
    pc "Sorry…"
    lisa "Don't be, it's super fun and kind of strokes the ego a little to be able to fry your pathetic little man brain."
    pc "I’ll have you know, it's a pathetic regular sized man brain."
    image lisa_stage_4_event_89 = "/lisa/events/stage4/89.webp"
    scene lisa_stage_4_event_89
    "Rolling her eyes Lisa smiles at you."
    image lisa_stage_4_event_90 = "/lisa/events/stage4/90.webp"
    scene lisa_stage_4_event_90
    lisa "Come on then, what are you waiting for. Let's get this show on the road."
    lisa "I have a sexy brunette to impress with my chunky thighs."
    image lisa_stage_4_event_91 = "/lisa/events/stage4/91.webp"
    scene lisa_stage_4_event_91
    "Handing over the large bag of sweets, Lisa makes short work of them."
    image lisa_stage_4_event_92 = "/lisa/events/stage4/92.webp"
    scene lisa_stage_4_event_92
    "After a couple of minutes she reaches down, unbuttoning her pants."
    image lisa_stage_4_event_93 = "/lisa/events/stage4/93.webp"
    scene lisa_stage_4_event_93
    lisa "Oooh, that is better."
    image lisa_stage_4_event_94 = "/lisa/events/stage4/94.webp"
    scene lisa_stage_4_event_94
    lisa "Seems like these jeans won't be lasting much longer either."
    image lisa_stage_4_event_95 = "/lisa/events/stage4/95.webp"
    scene lisa_stage_4_event_95
    "Leaning back Lisa gives her belly more room as she lounges on her sofa."
    image lisa_stage_4_event_96 = "/lisa/events/stage4/96.webp"
    scene lisa_stage_4_event_96
    lisa "Thanks for today, and for checking up on me again."
    lisa "But you don't have to worry about me, I am fully on board the weight gain train."
    lisa "That is, if you want to continue to come and feed me like this?"
    pc "Absolutely!"
    image lisa_stage_4_event_97 = "/lisa/events/stage4/97.webp"
    scene lisa_stage_4_event_97
    lisa "Great, well I’ll text you next time I need a feeder buddy to come and help me."
    "Helping clean up the empty packets you head home."
    if recollection == False:
        $ lisa.weight += 0.5
    $ lisastage4event = 0
    return


label Lisa_Stage_4_Event_2:
    #### working a normal shift with Lisa.###
    image lisa_stage_4_event_1 = "/lisa/events/stage4/1.webp"
    scene lisa_stage_4_event_1
    play music "/music/bunny_bites.ogg" if_changed
    "Clearing up a table you notice Lisa watching you."
    lisa "Hey, are those fries free?"
    pc "Looks like it."
    image lisa_stage_4_event_2 = "/lisa/events/stage4/2.webp"
    scene lisa_stage_4_event_2
    "Handing over the large fries Lisa smiles as she begins to eat them."
    image lisa_stage_4_event_3 = "/lisa/events/stage4/3.webp"
    scene lisa_stage_4_event_3
    stop music fadeout 1.0
    "But a few moments later you notice the lights dim before going off entirely."
    lisa "What was that?"
    pc "Did we blow a fuse?"
    image lisa_stage_4_event_4 = "/lisa/events/stage4/4.webp"
    scene lisa_stage_4_event_4
    "Looking out the window you can see the lights are also off across the road."
    pc "Maybe it's a power cut, seems like it's the entire street."
    image lisa_stage_4_event_5 = "/lisa/events/stage4/5.webp"
    scene lisa_stage_4_event_5
    lisa "What do we do?"
    pc "I’m not sure."
    lisa "Ok, I will phone Marie. Can you go and check for flashlights in the store room?"
    pc "Sure thing."
    image lisa_stage_4_event_6 = "/lisa/events/stage4/6.webp"
    scene lisa_stage_4_event_6
    "Going into the store room you have a look for some flashlights."
    image lisa_stage_4_event_7 = "/lisa/events/stage4/7.webp"
    scene lisa_stage_4_event_7
    "After a couple of minutes you find one stuck behind one of the boxes."

    ### lisa arrives ###
    image lisa_stage_4_event_8 = "/lisa/events/stage4/8.webp"
    scene lisa_stage_4_event_8
    lisa "Hey, find any?"
    pc "I found one, but it is kinda old."
    image lisa_stage_4_event_9 = "/lisa/events/stage4/9.webp"
    scene lisa_stage_4_event_9
    lisa "That's ok, I just spoke to Marie and apparently power has gone off for the entire centre of town."
    pc "So what do we do now, I don't think we can serve people like this."
    lisa "Marie said to just give people takeaway boxes for food if they were eating and we can close up early."
    lisa "So I’ve done that, luckily it wasn’t too busy anyway."
    pc "Great, so I guess we have a free evening."
    image lisa_stage_4_event_10 = "/lisa/events/stage4/10.webp"
    scene lisa_stage_4_event_10
    lisa "Yeah, fancy going out for a drink?"
    pc "Sure, although won't the cocktail lounge be affected too?"
    image lisa_stage_4_event_11 = "/lisa/events/stage4/11.webp"
    scene lisa_stage_4_event_11
    lisa "Oh yeah, I didn’t think about that."
    pc "What about that place on the edge of town?"
    image lisa_stage_4_event_12 = "/lisa/events/stage4/12.webp"
    scene lisa_stage_4_event_12
    lisa "The one next to the train station?"
    pc "Yeah, I have never been to it before but we could give it a try."
    image lisa_stage_4_event_13 = "/lisa/events/stage4/13.webp"
    scene lisa_stage_4_event_13
    lisa "I…uhh."
    pc "What, you haven't gotten drunk there and done something to get yourself banned have you?"
    lisa "No it's not that, that place is kind of run by my sister."
    pc "Oh, do you two not get on?"
    image lisa_stage_4_event_14 = "/lisa/events/stage4/14.webp"
    scene lisa_stage_4_event_14
    lisa "We do get on but she can be a little judgemental or abrasive."
    pc "That's ok, I won't take offence."
    lisa "No, not usually about other people, about me."
    pc "Really? Well I am sure we can think of something else."
    image lisa_stage_4_event_15 = "/lisa/events/stage4/15.webp"
    scene lisa_stage_4_event_15
    lisa "It’s ok, I was already planning on stopping by to see her this week anyway."
    pc "If you are sure?"
    lisa "Trust me, I am used to it by now."
    image lisa_stage_4_event_16 = "/lisa/events/stage4/16.webp"
    scene lisa_stage_4_event_16
    lisa "Let's go."

    ### New pub ###
    image lisa_stage_4_event_17 = "/lisa/events/stage4/17.webp"
    scene lisa_stage_4_event_17
    play music "<loop 0.2 from 39>/music/generic_date.ogg" if_changed fadein 1.0
    "Walking into the pub, it doesn’t seem busy here even though the car park was full."
    image lisa_stage_4_event_18 = "/lisa/events/stage4/18.webp"
    scene lisa_stage_4_event_18
    lisa "Hi Mandy."
    mandy "I told you it was only a matter of time!"
    image lisa_stage_4_event_19 = "/lisa/events/stage4/19.webp"
    scene lisa_stage_4_event_19
    lisa "Not this again."
    mandy "Finally found someone, I knew you were not really a lesbian."
    lisa "Mandy!"
    pc "We are just friends."
    image lisa_stage_4_event_20 = "/lisa/events/stage4/20.webp"
    scene lisa_stage_4_event_20
    mandy "Really?"
    lisa "Yes!"
    mandy "Why, what's wrong with my sister?"
    pc "Nothing."
    mandy "So why haven’t you asked her out?"
    lisa "Because I am not attracted to men."
    image lisa_stage_4_event_21 = "/lisa/events/stage4/21.webp"
    scene lisa_stage_4_event_21
    mandy "You always say that."
    lisa "It is almost like it's the truth."
    mandy "One day you will meet a man who sweeps you off your feet and you will see what you have been missing."
    lisa "Don't hold your breath."
    image lisa_stage_4_event_22 = "/lisa/events/stage4/22.webp"
    scene lisa_stage_4_event_22
    "Thankfully at that moment another customer arrived, allowing the two of you to escape and find a table."

    ###Sat at table###
    image lisa_stage_4_event_23 = "/lisa/events/stage4/23.webp"
    scene lisa_stage_4_event_23
    lisa "I'm going to need a drink if she is going to be like that all night."
    lisa "Want me to get you one as well?"
    pc "Sure."
    image lisa_stage_4_event_24 = "/lisa/events/stage4/24.webp"
    scene lisa_stage_4_event_24
    "Going up to the bar, Lisa pours your drinks herself before returning to the table."
    image lisa_stage_4_event_25 = "/lisa/events/stage4/25.webp"
    scene lisa_stage_4_event_25
    pc "Are you sure that's ok to do?"
    lisa "Oh, I come here all the time and my sister is the owner so what is she going to do?"
    lisa "Besides, she is the one that is making me drink, so it’s her own fault."
    lisa "Sorry about her being so crazy."
    pc "No need to apologise to me, it seems like she was harder on you."
    image lisa_stage_4_event_26 = "/lisa/events/stage4/26.webp"
    scene lisa_stage_4_event_26
    lisa "Yeah, for whatever reason she still thinks I need to find a man to fix my life for me."
    pc "Even though she knows about you liking women."
    lisa "Yeah, I guess you could call it sibling rivalry, refusing to think she is wrong."
    pc "So, she doesn’t know about you and Marie?"
    image lisa_stage_4_event_27 = "/lisa/events/stage4/27.webp"
    scene lisa_stage_4_event_27
    lisa "God no, I’d need a lot more of these before I tell her anything about my love life."
    lisa "Speaking of."
    image lisa_stage_4_event_28 = "/lisa/events/stage4/28.webp"
    scene lisa_stage_4_event_28
    "Draining the rest of the glass, Lisa pours herself another drink."
    image lisa_stage_4_event_29 = "/lisa/events/stage4/29.webp"
    scene lisa_stage_4_event_29
    lisa "So what about you, I see you flirting with our customers."
    pc "Is that ok?"
    lisa "Absolutely, and you have good taste."
    lisa "That gym chick Trista and I can't tell you how many times I have wished Bonnie was interested in me."
    pc "Really?"
    image lisa_stage_4_event_30 = "/lisa/events/stage4/30.webp"
    scene lisa_stage_4_event_30
    lisa "Yeah, she is so sweet and who wouldn’t want an unlimited supply of chocolate."
    lisa "Although before I got to know you better I was a bit worried."
    pc "Worried?"
    lisa "I got the feeling a lot of the customers we get come in because it was a female only staff."
    lisa "I thought you were just here to flirt and get laid, which would put them off."
    lisa "But you have actually been really nice and it's been a weight off our shoulders to have another member of staff."
    pc "Thank you, I really did need the job."
    lisa "Well, it worked out for us all."

    ### Mandy appears ###
    image lisa_stage_4_event_31 = "/lisa/events/stage4/31.webp"
    scene lisa_stage_4_event_31
    mandy "So, do you two lovebirds want some food?"
    image lisa_stage_4_event_32 = "/lisa/events/stage4/32.webp"
    scene lisa_stage_4_event_32
    "Rolling her eyes Lisa seems to bite her tongue not to fire something back."
    lisa "Sure thing, can I get a burger, fries and a side of onion rings."
    image lisa_stage_4_event_33 = "/lisa/events/stage4/33.webp"
    scene lisa_stage_4_event_33
    mandy "Ok, and for your partner?"
    pc "I’m ok, I don't think I am…."
    image lisa_stage_4_event_34 = "/lisa/events/stage4/34.webp"
    scene lisa_stage_4_event_34
    lisa "He will have the same."
    image lisa_stage_4_event_35 = "/lisa/events/stage4/35.webp"
    scene lisa_stage_4_event_35
    "Looking at Lisa, you can tell she wants you to accept it."
    pc "Sure, that sounds good to me."
    image lisa_stage_4_event_36 = "/lisa/events/stage4/36.webp"
    scene lisa_stage_4_event_36
    mandy "Two burgers, fries and onion rings coming up."
    lisa "Thanks sis."

    ###Mandy leaves###
    image lisa_stage_4_event_37 = "/lisa/events/stage4/37.webp"
    scene lisa_stage_4_event_37
    pc "Everything ok?"
    lisa "Sorry, I am just really hungry and need to keep eating more for…you know."
    pc "So why not order more?"
    image lisa_stage_4_event_38 = "/lisa/events/stage4/38.webp"
    scene lisa_stage_4_event_38
    lisa "I…Mandy has also been getting on me about my weight."
    lisa "Which is a bit rich coming from her. You should have seen how fat she was when we were teenagers and she didn’t care then."
    pc "So you want my food too?"
    image lisa_stage_4_event_39 = "/lisa/events/stage4/39.webp"
    scene lisa_stage_4_event_39
    lisa "If you don't mind?"
    pc "Not at all."
    lisa "Thanks, you are a star and don't worry I’ll cover the cost."
    lisa "You want another drink?"
    image lisa_stage_4_event_40 = "/lisa/events/stage4/40.webp"
    scene lisa_stage_4_event_40
    "Looking down at your still half full glass you shake your head as Lisa heads up for another."

    ###Food on the table ###
    image lisa_stage_4_event_41 = "/lisa/events/stage4/41.webp"
    scene lisa_stage_4_event_41
    "A few minutes later your meals arrive with fresh refills and Lisa digs in."
    image lisa_stage_4_event_42 = "/lisa/events/stage4/42.webp"
    scene lisa_stage_4_event_42
    "Demolishing her burger and fries in record time she makes sure Mandy isn’t watching and switches the plates around."
    image lisa_stage_4_event_43 = "/lisa/events/stage4/43.webp"
    scene lisa_stage_4_event_43
    "Only now as she leans back can you notice her stomach starting to bulge from all the food and drink."
    image lisa_stage_4_event_44 = "/lisa/events/stage4/44.webp"
    scene lisa_stage_4_event_44
    "You continue making small talk about work and life as Lisa eats."
    image lisa_stage_4_event_45 = "/lisa/events/stage4/45.webp"
    scene lisa_stage_4_event_45
    "But it isn’t long before you can see her squirming slightly in her seat."
    pc "Everything ok?"
    image lisa_stage_4_event_46 = "/lisa/events/stage4/46.webp"
    scene lisa_stage_4_event_46
    lisa "Sorry, all that drink is starting to make itself known and I really need to pee."
    lisa "But I don't want to leave you here alone with Mandy, she has a tendency to pounce when I am not around."
    pc "Go, I will be fine."
    image lisa_stage_4_event_47 = "/lisa/events/stage4/47.webp"
    scene lisa_stage_4_event_47
    lisa "Great, because I am about to pee myself. Be right back and don't do anything to get her attention!"

    ###Lisa leaves ###
    image lisa_stage_4_event_48 = "/lisa/events/stage4/48.webp"
    scene lisa_stage_4_event_48
    "Watching Lisa rush off it’s mere seconds before Mandy arrives as she predicted."
    image lisa_stage_4_event_49 = "/lisa/events/stage4/49.webp"
    scene lisa_stage_4_event_49
    mandy "So how is the date going?"
    pc "We are just friends."
    mandy "So just friend, how do you know my sister?"
    pc "We work together."
    mandy "You work with her at Bunny Bites, with Marie?"
    pc "You know Marie?"
    image lisa_stage_4_event_50 = "/lisa/events/stage4/50.webp"
    scene lisa_stage_4_event_50
    mandy "I used to work with Lisa there, until I realised what Marie was doing."
    pc "What Marie was doing?"
    mandy "Fattening us all up, I gained so much weight when I worked there."
    mandy "It was the fattest I had ever been, all her free gifts and ‘wrong orders’ she used to give to us in our breaks."
    pc "I am sure she was just being nice."
    mandy "She wasn’t and now it seems she has moved onto Lisa as the next target."
    pc "Target?"
    image lisa_stage_4_event_51 = "/lisa/events/stage4/51.webp"
    scene lisa_stage_4_event_51
    mandy "Are you part parrot or something."
    mandy "You must have noticed the extra weight Lisa has been putting on working there, and it's only getting worse."
    mandy "You need to keep an eye on Marie and look after Lisa."
    pc "Lisa is capable of looking after herself and besides I think she still looks great."
    image lisa_stage_4_event_52 = "/lisa/events/stage4/52.webp"
    scene lisa_stage_4_event_52
    mandy "I knew it, you are on a date."
    pc "It’s not a date, I just meant it as a compliment."
    image lisa_stage_4_event_53 = "/lisa/events/stage4/53.webp"
    scene lisa_stage_4_event_53
    mandy "Yeah right, look you need to show her a good time tonight."
    pc "What?"
    mandy "Show her what she is missing, I know she would be happier if she could just find a man to settle down with."

    ###Lisa returns###
    image lisa_stage_4_event_54 = "/lisa/events/stage4/54.webp"
    scene lisa_stage_4_event_54
    lisa "What is going on here?"
    mandy "Nothing, just getting to know your boyfriend a bit more."
    image lisa_stage_4_event_55 = "/lisa/events/stage4/55.webp"
    scene lisa_stage_4_event_55
    lisa "Mandy, he is just a friend. Can you please just leave him alone."
    mandy "Sheesh, just looking out for you sis."
    lisa "Yeah well while you are looking, can you look for some chocolate, brownies, and ice cream for us."
    mandy "Ugh fine!"
    image lisa_stage_4_event_56 = "/lisa/events/stage4/56.webp"
    scene lisa_stage_4_event_56
    mandy "Remember what I said."

    ###Mandy leaves ###
    image lisa_stage_4_event_57 = "/lisa/events/stage4/57.webp"
    scene lisa_stage_4_event_57
    pc "She is a little intense."
    lisa "You don't have to tell me."
    lisa "She is only a year older than me and acts like she is so much smarter than me."
    pc "Has she always been like that?"
    image lisa_stage_4_event_58 = "/lisa/events/stage4/58.webp"
    scene lisa_stage_4_event_58
    lisa "Yeah, but it got worse after she met her fiance."
    lisa "They are like the perfect film couple, highschool sweethearts that think it's that easy for everyone."
    pc "Well, you have Marie now."
    image lisa_stage_4_event_59 = "/lisa/events/stage4/59.webp"
    scene lisa_stage_4_event_59
    lisa "I will soon, sooner after a few more of these."
    image lisa_stage_4_event_60 = "/lisa/events/stage4/60.webp"
    scene lisa_stage_4_event_60
    "As she speaks, two giant platters of chocolate brownies and icecream are pushed onto the table."
    lisa "Mmm, these are always so good."
    pc "This is a lot, did you plan on having mine again."
    image lisa_stage_4_event_61 = "/lisa/events/stage4/61.webp"
    scene lisa_stage_4_event_61
    lisa "Yes, but I’ll need you to pretend it is yours so feel free to have some."
    lisa "I can't eat this much chocolate as quickly as I did the burgers."
    image lisa_stage_4_event_62 = "/lisa/events/stage4/62.webp"
    scene lisa_stage_4_event_62
    "Picking up the spoon you take tiny bites from around the edge as Lisa dives into her’s."
    image lisa_stage_4_event_63 = "/lisa/events/stage4/63.webp"
    scene lisa_stage_4_event_63
    "All this talk about Marie and relationships seems to have supercharged her desire to get bigger as she shovels the gooey chocolate into her mouth."
    image lisa_stage_4_event_64 = "/lisa/events/stage4/64.webp"
    scene lisa_stage_4_event_64
    "Mouthful after mouthful of the sweet goodness disappears down her throat and into her growing stomach."
    image lisa_stage_4_event_65 = "/lisa/events/stage4/65.webp"
    scene lisa_stage_4_event_65
    "Barely saying anything, she is consumed by her desire to eat."
    image lisa_stage_4_event_66 = "/lisa/events/stage4/66.webp"
    scene lisa_stage_4_event_66
    "Finishing off her mountain of desserts she already looks ready to burst."
    image lisa_stage_4_event_67 = "/lisa/events/stage4/67.webp"
    scene lisa_stage_4_event_67
    "But outstretching her hand she quickly swaps the plates and starts again."
    image lisa_stage_4_event_68 = "/lisa/events/stage4/68.webp"
    scene lisa_stage_4_event_68
    "Splitting your attention between watching Lisa eat and looking out for her sister, you are thankful for a steady stream of customers keeping her attention."
    image lisa_stage_4_event_69 = "/lisa/events/stage4/69.webp"
    scene lisa_stage_4_event_69
    window hide
    pause
    image lisa_stage_4_event_70 = "/lisa/events/stage4/70.webp"
    scene lisa_stage_4_event_70
    "Hearing a metallic clinic Lisa has finished, laying her spoon down triumphantly."
    lisa "Oh god, I think I overdid it."
    lisa "My stomach is so tight, I think I might be sick."
    lisa "That was so much chocolate."
    pc "That was impressive, if only Marie could see you now."
    lisa "I look so gross like this, covered in chocolate and barely moving like some kind of slob."
    lisa "We need to get out of here before Mandy see’s me like this."
    image lisa_stage_4_event_71 = "/lisa/events/stage4/71.webp"
    scene lisa_stage_4_event_71
    "Looking around the place is surprisingly empty and Mandy must be out the back."
    pc "Seems like the coast is clear."
    image lisa_stage_4_event_72 = "/lisa/events/stage4/72.webp"
    scene lisa_stage_4_event_72
    lisa "Uggh, help me get up, but first."
    "The results of her binge are clear as her denim shorts now sharply cut into her large pale orb like gut."
    "Lisa reaches down fumbling with the button on her shorts before finally managing to unfasten them, leaving her bloated form on full display."
    image lisa_stage_4_event_73 = "/lisa/events/stage4/73.webp"
    scene lisa_stage_4_event_73
    "Helping Lisa to her feet she just about manages to walk her way to the exit unassisted despite her giant stomach."

    ###Outside ####
    image lisa_stage_4_event_74 = "/lisa/events/stage4/74.webp"
    scene lisa_stage_4_event_74
    lisa "I think I need to go home. I enjoyed tonight though."
    pc "Me too."
    lisa "Really, all you did was get accosted by my sister and watch me stuff myself with a month's worth of chocolate."
    pc "It was nice to spend time with you."
    #lisa "You are too sweet."
    #"Leaning up you feel her rock hard stomach push against you as she kisses you on the cheek."
    image lisa_stage_4_event_75 = "/lisa/events/stage4/75.webp"
    scene lisa_stage_4_event_75
    lisa "See you at work."
    pc "Bye Lisa."
    stop music fadeout 1.0

    if recollection == False:
        $ lisa.weight += 1
        $ daytime = 4
    $ lisastage4event2 = 0
    return

label LisaStage4Phone:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Lisa', dialogue=dialogue_one)
    $ msg ("Hey, just wanted to say thanks again for yesterday.", who=1)
    pause
    $ msg ("Sorry about my sister...and pigging out like that in front of you.", who=1)
    pause
    $ msg ("No need to apologise.")
    pause
    $ msg ("You handled it pretty well, most people get easily intimidated by Mandy.", who=1)
    pause
    $ msg ("I can't see why...")
    pause
    $ msg ("Either way, we should visit that place again.", who=1)
    pause
    $ msg ("The food is good and I get the friends and family discount.", who=1)
    pause
    $ msg ("Sounds good to me.")
    pause
    $ hide_messenger()

    $ lisastage4phone = 0
    return


label Lisa_Stage_5_Event:
    ###Lisa check in event###
    image lisa_stage_5_event_1 = "/lisa/events/stage5/1.webp"
    scene lisa_stage_5_event_1
    play music "/music/bunny_bites.ogg" if_changed
    "As the dinner empties of its last customers you spot Lisa helping herself to some leftover fries at the front desk."
    image lisa_stage_5_event_2 = "/lisa/events/stage5/2.webp"
    scene lisa_stage_5_event_2
    "Lost in her own little world you figure now would be as good of a time as any to check in on her for Marie."
    "Although you would have to be careful with how you worded this."
    image lisa_stage_5_event_3 = "/lisa/events/stage5/3.webp"
    scene lisa_stage_5_event_3
    pc "Hey Lisa, how are you doing?"
    lisa "Hey, good thanks."
    lisa "That rush was a bit hectic, it's weird how fast it can go quiet in here though."
    image lisa_stage_5_event_4 = "/lisa/events/stage5/4.webp"
    scene lisa_stage_5_event_4
    pc "Yeah, real ups and downs."
    "Pausing for a moment as you try to find a way of asking her about her weight without insulting her its clear she can tell somethings up."
    image lisa_stage_5_event_5 = "/lisa/events/stage5/5.webp"
    scene lisa_stage_5_event_5
    lisa "Something I can help you with?"
    pc "No, well maybe. I was just wondering.."
    image lisa_stage_5_event_6 = "/lisa/events/stage5/6.webp"
    scene lisa_stage_5_event_6
    lisa "About my recent weight gain?"
    image lisa_stage_5_event_7 = "/lisa/events/stage5/7.webp"
    scene lisa_stage_5_event_7
    "Reaching down Lisa places her hands on her enlarged breasts."
    pc "Kind of, I'm not judging. In fact it's kind of the opposite."
    image lisa_stage_5_event_8 = "/lisa/events/stage5/8.webp"
    scene lisa_stage_5_event_8
    lisa "You like it too don't you?"
    pc "Kind of, is that a problem for you?"
    image lisa_stage_5_event_9 = "/lisa/events/stage5/9.webp"
    scene lisa_stage_5_event_9
    lisa "No, why would it be a problem."
    pc "I don't know, I was just wondering how you were feeling about it."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/lisa/events/stage5/vid1.webm" loop
    show movie with dissolve
    lisa "I think I might have overdone it at the beginning."
    lisa "I really felt myself getting unfit when I first started packing on the pounds for Marie."
    lisa "But then I was talking to a couple of the customers about it and Trista helped me figure out a good routine to stay healthy."
    pc "So you are doing it for Marie?"
    stop movie
    image lisa_stage_5_event_10 = "/lisa/events/stage5/10.webp"
    scene lisa_stage_5_event_10
    lisa "Yeah, I thought you knew?"
    pc "You have mentioned it, but I just mean is it what you want?"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/lisa/events/stage5/vid2.webm" loop
    show movie with dissolve
    lisa "Oh, you know I am kind of figuring that out still."
    lisa "I really like Marie and want her to like me. She just makes me feel so special, I would do anything for her."
    lisa "Plus I have never really worried too much about my weight in the past so this is kind of new to me."
    lisa "My mum and sister are both on the larger side, and they never seemed to care or have any problems with it."
    lisa "So I don't see any reason why I should care about anyone else except what Marie wants."
    pc "That's actually a pretty good way of looking at it."
    stop movie
    image lisa_stage_5_event_11 = "/lisa/events/stage5/11.webp"
    scene lisa_stage_5_event_11
    lisa "Well maybe I care about what you think a little too."
    lisa "But I don't think you will be complaining about it either."
    pc "No complaints from me, I just want you to be happy."
    image lisa_stage_5_event_12 = "/lisa/events/stage5/12.webp"
    scene lisa_stage_5_event_12
    lisa "I am whenever I’m with Marie."
    "Hearing the door open behind you, it seems todays work isn’t over yet."
    image lisa_stage_5_event_13 = "/lisa/events/stage5/13.webp"
    scene lisa_stage_5_event_13
    "Shoving the last handful of fries into her mouth, Lisa goes to seat the new arrivals."
    image lisa_stage_5_event_14 = "/lisa/events/stage5/14.webp"
    scene lisa_stage_5_event_14
    pause

    #CUSTOMER comes in
    if recollection == False:
        $ lisa.weight += 1
    else:
        stop music fadeout 1.0
    $ lisastage5event = 0
    return


label Lisa_Stage_6_Event:
    ## Lisa stage 6 stock take (Also after Marie stage 4 if possible) ##
    ###After working a regular shift, Lisa joins you at the desk###
    image lisa_stage_6_event_1 = "/lisa/events/stage6/1.webp"
    scene lisa_stage_6_event_1
    play music "/music/bunny_bites.ogg" if_changed
    lisa "Phew, what a day."
    pc "It has been pretty busy today."
    lisa "I know, I'm exhausted."
    pc "If you want, I can clean and close up."
    image lisa_stage_6_event_2 = "/lisa/events/stage6/2.webp"
    scene lisa_stage_6_event_2
    lisa "It’s nice of you to offer, but Marie asked me to check our stock."
    pc "Didn’t Amber just do a stock check?"
    lisa "Yeah, but things got a bit messy after that delivery error and some of the numbers of what we have are higher than they really are."
    "You wonder if Ambers snacking has anything to do with that."
    pc "I don't mind doing that as well, I have been shown how to do it."
    image lisa_stage_6_event_3 = "/lisa/events/stage6/3.webp"
    scene lisa_stage_6_event_3
    lisa "Are you sure, I was kind of just complaining."
    lisa "Today has dragged a little because I have a date with Marie later."
    pc "A date?"
    image lisa_stage_6_event_4 = "/lisa/events/stage6/4.webp"
    scene lisa_stage_6_event_4
    lisa "Yeah, it’s our first one actually."
    lisa "I’m super excited but also a little nervous."
    image lisa_stage_6_event_5 = "/lisa/events/stage6/5.webp"
    scene lisa_stage_6_event_5
    lisa "What if I screw it up and Marie doesn’t like me?"
    pc "If you have a date with her, I think that means she already likes you."
    pc "And you have known each other for a while, so I wouldn’t worry about messing anything up. Just be yourself and have fun."
    lisa "You’re probably right, I’m definitely overthinking it."
    image lisa_stage_6_event_6 = "/lisa/events/stage6/6.webp"
    scene lisa_stage_6_event_6
    lisa "But what if I am not big enough yet?"
    pc "What?"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/lisa/events/stage6/vid1.webm" loop
    show movie with dissolve
    lisa "Marie wanted me to gain weight, what if I haven't gained enough."
    lisa "I knew I shouldn’t have gone to the gym this week."
    lisa "And I saw Amber had made some extra burgers yesterday and I didn’t have any."
    lisa "How can I turn up to our first date looking this skinny."
    lisa "I need to eat something, you have to help me!"
    pc "Lisa, you look great and I am sure Marie appreciates the work you have put in."
    pc "You don't need to panic, but I would be lying if I didn’t think Marie would like you being bigger."
    pc "Why don't we go do the stock take, there is plenty in there if you feel the need to eat something."
    stop movie
    image lisa_stage_6_event_7 = "/lisa/events/stage6/7.webp"
    scene lisa_stage_6_event_7
    lisa "Right, that sounds good."
    pc "I’ll close up, if you want to get a head start."

    ###storage room###
    image lisa_stage_6_event_8 = "/lisa/events/stage6/8.webp"
    scene lisa_stage_6_event_8
    "Closing up you quickly clear away all the plates and rubbish before heading into the storage room."
    image lisa_stage_6_event_9 = "/lisa/events/stage6/9.webp"
    scene lisa_stage_6_event_9
    "Walking in you see Lisa already halfway through a box of doughnuts, it wasn’t quite what you meant by head start."
    "Grabbing the clipboard you inspect it, although the numbers seem to be different from when you did it last time."
    pc "Hey, do you know if anyone has done a check since we did it together?"
    image lisa_stage_6_event_10 = "/lisa/events/stage6/10.webp"
    scene lisa_stage_6_event_10
    lisa "No, that would have been the last time anyone did one."
    pc "Ok thanks."
    "Part of you begins to suspect Marie has been tampering with it, either to hide how much they have all been eating."
    "Or maybe to require more stock checks, knowing that being alone with all this food more often was going to have an obvious effect on Amber and Lisa’s waistline."
    image lisa_stage_6_event_11 = "/lisa/events/stage6/11.webp"
    scene lisa_stage_6_event_11 with vpunch
    lisa "Urrrp, sorry."
    image lisa_stage_6_event_12 = "/lisa/events/stage6/12.webp"
    scene lisa_stage_6_event_12
    "It seems Lisa was done with the box of doughnuts."
    "Checking the form you begin to do a stock check against the numbers written on the form."
    "Some were higher that you corrected, while those that were lower offered a unique opportunity to help Lisa with her plan."
    pc "Looks like we have more burgers than we thought."
    image lisa_stage_6_event_13 = "/lisa/events/stage6/13.webp"
    scene lisa_stage_6_event_13
    "Looking up from another half finished box of snacks, Lisa had seemingly been in a world of her own."
    lisa "I think Marie has increased the amount we bought."
    lisa "We seem to have been selling more of them and basically everything else recently."
    "Given the increasing size and appetites of many of the customers, that should have come as no surprise."
    pc "I can update the number…or if you want I could leave it the same and you could have them. We should have more than enough."
    image lisa_stage_6_event_14 = "/lisa/events/stage6/14.webp"
    scene lisa_stage_6_event_14
    lisa "That’s a great idea, I’ll go set up the kitchen!"
    image lisa_stage_6_event_15 = "/lisa/events/stage6/15.webp"
    scene lisa_stage_6_event_15
    "Continuing the rest of the checks, you periodically pile up the extra food."
    "It seems like a lot of things have been under reported, but it doesn't take you much time to do the stock check at all."
    image lisa_stage_6_event_16 = "/lisa/events/stage6/16.webp"
    scene lisa_stage_6_event_16
    "After taking it out into the kitchen, you start mopping and cleaning up the restaurant."
    "It’s pretty quiet except for the constant sizzling and banging of pans in the kitchen."
    image lisa_stage_6_event_17 = "/lisa/events/stage6/17.webp"
    scene lisa_stage_6_event_17
    "A few minutes later you see the kitchen doors swing open and Lisa emerges with a a lot of food."
    image lisa_stage_6_event_18 = "/lisa/events/stage6/18.webp"
    scene lisa_stage_6_event_18
    "Carrying it to a table she is barely seated before she starts to shove the food into her mouth."
    image lisa_stage_6_event_19 = "/lisa/events/stage6/19.webp"
    scene lisa_stage_6_event_19
    "You continue mopping the same spot, unable to take your eyes away as her binge speeds up."
    image lisa_stage_6_event_20 = "/lisa/events/stage6/20.webp"
    scene lisa_stage_6_event_20
    "Watching on in awe, Lisa devours more and more food, totally forgetting you are even there."
    image lisa_stage_6_event_21 = "/lisa/events/stage6/21.webp"
    scene lisa_stage_6_event_21
    "More and more food disappears into her bulging belly, until finally all the food is gone."
    image lisa_stage_6_event_22 = "/lisa/events/stage6/22.webp"
    scene lisa_stage_6_event_22
    "Leaning back, Lisa rubs her giant stomach as you both regain your senses."
    pc "Want me to clean that up, while you digest that meal."
    image lisa_stage_6_event_23 = "/lisa/events/stage6/23.webp"
    scene lisa_stage_6_event_23
    lisa "That would be great."
    lisa "I don't think I have ever felt this full."
    pc "So what are your plans with Marie?"
    image lisa_stage_6_event_24 = "/lisa/events/stage6/24.webp"
    scene lisa_stage_6_event_24
    lisa "Oh crap, I didn’t think about that."
    pc "Hope it's nothing to energetic."
    lisa "No…it's worse."
    image lisa_stage_6_event_25 = "/lisa/events/stage6/25.webp"
    scene lisa_stage_6_event_25
    lisa "We are going to that new restaurant in town and I totally forgot."
    lisa "How am I going to manage to eat anything else, I'm so full but don't want to disappoint her."
    pc "Maybe some of it will go down by then?"
    lisa "It's like 20 minutes, I really screwed up."
    image lisa_stage_6_event_26 = "/lisa/events/stage6/26.webp"
    scene lisa_stage_6_event_26
    lisa "No, it's ok. I can manage, it will be fine."
    lisa "Although I had better head out soon if I want to make it there in time."
    pc "Don't worry about this place, I’ll clean up the kitchen and everything out here."
    image lisa_stage_6_event_27 = "/lisa/events/stage6/27.webp"
    scene lisa_stage_6_event_27
    lisa "Are you sure, I kind of made a bit of a mess back there."
    pc "Go, I’ll be fine."
    image lisa_stage_6_event_28 = "/lisa/events/stage6/28.webp"
    scene lisa_stage_6_event_28
    lisa "Thanks, you're amazing."
    image lisa_stage_6_event_29 = "/lisa/events/stage6/29.webp"
    scene lisa_stage_6_event_29
    "Groaning, Lisa just about gets to her feet, slowly shuffling towards the changing room."
    image lisa_stage_6_event_30 = "/lisa/events/stage6/30.webp"
    scene lisa_stage_6_event_30
    "Tidying up after her massive binge she emerges from the changing room, her clothes barely fitting around her body as she leaves for her date."
    image lisa_stage_6_event_31 = "/lisa/events/stage6/31.webp"
    scene lisa_stage_6_event_31
    pause
    image lisa_stage_6_event_32 = "/lisa/events/stage6/32.webp"
    scene lisa_stage_6_event_32
    "It takes some time to clean up the kitchen, but eventually you are done and leave for the night, locking up."
    stop music fadeout 1.0

    ###Home###
    scene player_room
    "Arriving home, you kick off your shoes and take a seat on the couch."
    "Feeling a vibration in your pocket, you pull out your phone to see a text from Marie."
    ###Text###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Marie', dialogue=dialogue_one)
    $ msg ("Thank you!", who=1)
    pause
    $ msg (None, who=1, pic="stage6_lisa1")
    pause
    $ msg (None, who=1, pic="stage6_lisa2")
    pause
    $ msg (None, who=1, pic="stage6_lisa3")
    pause
    "The outfit she was wearing barely kept her decent in such a public location, but you guess she didn’t have much that would fit in her current state."
    "It doesn’t seem like Lisa will have to worry about Marie being into her tonight."
    $ hide_messenger()

    $ lisastage6event = 0
    return

label Lisa_Stage_7_Event:
    ### Lisa stage 7 ###
    ###After regular work shift##
    play music "/music/bunny_bites.ogg" if_changed
    image lisa_stage_7_event_1 = "/lisa/events/stage7/1.webp"
    scene lisa_stage_7_event_1
    "Finishing up your shift, you are about to leave when you spot Lisa in one of the booths."
    pc "Hey Lisa, I am about to head out. Are you ok to close?"
    ###Lisa eating, face already smeared with sauce or something###
    image lisa_stage_7_event_2 = "/lisa/events/stage7/2.webp"
    scene lisa_stage_7_event_2
    lisa "Mmm,...Yeah."
    lisa "All good with me."
    "Taking another large bite out of a burger she barely seems to acknowledge you."
    image lisa_stage_7_event_3 = "/lisa/events/stage7/3.webp"
    scene lisa_stage_7_event_3
    pc "Everything ok?"
    lisa "Yeah, it's great."
    lisa "Actually, I…never mind."
    pc "You know you can talk to me about anything."
    image lisa_stage_7_event_4 = "/lisa/events/stage7/4.webp"
    scene lisa_stage_7_event_4
    lisa "I know, it's just a little…inappropriate."
    pc "Inappropriate?"
    image lisa_stage_7_event_5 = "/lisa/events/stage7/5.webp"
    scene lisa_stage_7_event_5
    "Blushing, Lisa shoves her burger into her mouth."
    lisa "Fine, join me."
    image lisa_stage_7_event_6 = "/lisa/events/stage7/6.webp"
    scene lisa_stage_7_event_6
    "Sliding into the booth Lisa continues to eat as she tries to drum up the confidence to talk about whatever is on her mind."
    image lisa_stage_7_event_7 = "/lisa/events/stage7/7.webp"
    scene lisa_stage_7_event_7
    lisa "Ok, we are friends right?"
    pc "Absolutely, why do you have to ask?"
    lisa "Well, this isn’t really a workplace conversation."
    lisa "I…"
    lisa "Marie and I…"
    lisa "We…."
    pc "Whatever it is, you can talk to me about it."
    image lisa_stage_7_event_8 = "/lisa/events/stage7/8.webp"
    scene lisa_stage_7_event_8
    lisa "We had sex."
    pc "Oh ok, is that bad?"
    image lisa_stage_7_event_9 = "/lisa/events/stage7/9.webp"
    scene lisa_stage_7_event_9
    lisa "No, it's amazing, so ... amazing."
    lisa "Honestly, it was the best sex I have ever had in my life."
    lisa "You should have seen her, she was obsessed."
    lisa "I have never been with someone who wanted me as badly as Marie."
    lisa "The things she did to me, the way she treated me, it was so hot."
    image lisa_stage_7_event_10 = "/lisa/events/stage7/10.webp"
    scene lisa_stage_7_event_10
    "Going quiet, she takes another bite out of a burger."
    pc "So why the hesitation to talk about it?"
    image lisa_stage_7_event_11 = "/lisa/events/stage7/11.webp"
    scene lisa_stage_7_event_11
    lisa "I'm just not one to talk about sex openly, especially with guys."
    lisa "But that's all I can think about."
    lisa "That and gaining even more for her, I want to dedicate all my free time to eating."
    lisa "So I can blow up even more and have even more fun with Marie."
    lisa "If you think she would like that?"
    pc "I think she would love that."
    image lisa_stage_7_event_12 = "/lisa/events/stage7/12.webp"
    scene lisa_stage_7_event_12
    lisa "I have never wanted something or someone as bad as this either."
    pc "I'm happy for you, you both deserve to be happy and loved."
    lisa "Thanks, although that is far sweeter than anything I was talking about."
    pc "Ok, you deserve to be happy and have as many eye rolling orgasms as you can get out of each other?"
    image lisa_stage_7_event_13 = "/lisa/events/stage7/13.webp"
    scene lisa_stage_7_event_13
    lisa "Ok, that was much worse..."
    image lisa_stage_7_event_14 = "/lisa/events/stage7/14.webp"
    scene lisa_stage_7_event_14
    "Going quiet again, Lisa stuffs multiple handfuls of fries into her mouth at once."
    pc "So what now?"
    image lisa_stage_7_event_15 = "/lisa/events/stage7/15.webp"
    scene lisa_stage_7_event_15
    lisa "I guess I'll keep eating, we have another date next week and I would love to be even bigger for her."
    lisa "I have butterflies in my stomach just thinking about it."
    pc "Is there anything I can do to help?"
    lisa "Nothing you are not doing already. I just really wanted to talk to someone about it."
    lisa "But you are really the only other person that knows about me and Marie…or at least knows about all of it."
    pc "I’m always happy to talk if you want to, if you feel comfortable with it."
    image lisa_stage_7_event_16 = "/lisa/events/stage7/16.webp"
    scene lisa_stage_7_event_16
    lisa "I do, I feel like I can tell you anything."
    lisa "You are a great friend."
    pc "Back at you, although I am sure Amber would be willing to chat about it too."
    image lisa_stage_7_event_17 = "/lisa/events/stage7/17.webp"
    scene lisa_stage_7_event_17
    lisa "I know, I am just worried she will find it weird even if she doesn't say anything."
    lisa "She deserves to know though, she is one of my best friends and I know she wouldn’t judge me for it."
    pc "Amber certainly isn’t the sort of person to do that."
    image lisa_stage_7_event_18 = "/lisa/events/stage7/18.webp"
    scene lisa_stage_7_event_18
    "Finishing off the last burger, Lisa has managed to eat the entire meal while you have been chatting."
    image lisa_stage_7_event_19 = "/lisa/events/stage7/19.webp"
    scene lisa_stage_7_event_19
    lisa "Well I guess I should clean the diner."
    image lisa_stage_7_event_20 = "/lisa/events/stage7/20.webp"
    scene lisa_stage_7_event_20
    "Standing up, you see Lisa’s bloated belly for the first time in all its glory."
    lisa "Ooof, I am beyond full right now."
    pc "Why don't I clean up and you take a minute."
    image lisa_stage_7_event_21 = "/lisa/events/stage7/21.webp"
    scene lisa_stage_7_event_21
    lisa "Thanks, I think I need it."
    image lisa_stage_7_event_22 = "/lisa/events/stage7/22.webp"
    scene lisa_stage_7_event_22
    "Slumping back down into the booth, Lisa takes a moment to rest as you clean up the diner."
    image lisa_stage_7_event_23 = "/lisa/events/stage7/23.webp"
    scene lisa_stage_7_event_23
    "A few minutes later you return to find Lisa leaning on to the table."
    image lisa_stage_7_event_24 = "/lisa/events/stage7/24.webp"
    scene lisa_stage_7_event_24
    "Walking out with her giant belly on display, you lock up together before heading home."
    stop music fadeout 1.0
    if recollection == False:
        $ lisa.weight += 1
    $ lisastage7event = 0
    return

label Lisa_Stage_7_Event_2:
    ### Lisa stage 7.2 - End of shift variation ###
    ##After shift##
    "Cleaning down, you are about to close for the evening when you hear something from the changing rooms."
    pc "Hello, is someone in there?"
    lisa "[playername]? It’s Lisa."
    pc "Is everything ok in there?"
    lisa "No, I…"
    lisa "Are there any customers left?"
    pc "No, why?"
    "A few moments later, you see the door open and a half dressed Lisa emerges."
    lisa "I broke my pants, I couldn’t get them on over my belly."
    pc "Oh."
    lisa "It’s so embarrassing, last week I ripped by bunny suit and this week I pop a button off my jeans."
    pc "Would it make you feel better if I told you that I think Marie would find this incredibly hot."
    lisa "It might, do you think she would like to see it?"
    "Taking out her phone, Lisa pushes her stomach out and snaps a picture of her broken and barely fitting clothes."
    lisa "But seriously, what am I going to do?"
    lisa "I can't go out there looking like this."
    pc "I live nearby, I probably have a sweater you can borrow."
    lisa "I'm not sure you have anything that would fit me at this point."
    pc "You could tie it around your waist?"
    lisa "It’s better than nothing I suppose."
    pc "It’s dark, no one will see."
    "Locking up the restaurant, you head back to your place with Lisa."

    ###PC house##
    pc "Feel free to make yourself comfortable, I’ll go and find something."
    lisa "Thanks."
    "Going upstairs, you rummage around your dresser."
    "Finding an oversized hoodie, you grab it and head downstairs."
    ###Lisa standing naked in your lounge###
    "Walking in, you are surprised to see Lisa standing naked in your lounge, a phone in her hand as she snaps pictures of herself."
    pc "I…uh, found this."
    ###Lisa covering herself with her arms ###
    lisa "[playername]!"
    lisa "I’m so sorry, I didn’t hear you."
    "Grabbing her underwear, Lisa tries to make herself decent again."
    ###Lisa in her underwear###
    lisa "I…Marie replied and then I thought you were going to be gone later."
    pc "You don't have to apologise."
    pc "I take it, those photos were for Marie?"
    lisa "Yeah, you were right about her liking that photo and I wanted to send her more."
    lisa "I guess I got a bit carried away."
    pc "Like I said, it’s no problem."
    lisa "Is that…because you like to see me gain too?"
    pc "What?"
    lisa "I’ve noticed that you really seem to know what Marie likes, almost as if you like it too?"
    pc "I’m not sure what to say."
    lisa "It’s ok if you do."
    lisa "It would certainly explain a lot."
    pc "I guess, yeah I do."
    pc "But I don’t want to make you uncomfortable."
    pc "I know you are not into me, so there has never been anything with it more than helping you when you asked for it."
    "You are not sure if you have said too much when Lisa starts laughing."
    lisa "Relax, jeez. It’s totally fine."
    pc "You're sure?"
    lisa "Yeah, besides, I am the one who was naked in your house."
    lisa "If anyone should be apologising for making someone uncomfortable it should be me."
    pc "So…does this change anything?"
    lisa "Between us, why would it?"
    lisa "Except, I can have way more fun teasing you now I know."
    lisa "Assuming you are ok with it?"
    pc "I think I can handle it."
    pc "But why would you want to?"
    lisa "It’s fun, flirting and making people awkward. It’s the best of both worlds."
    pc "I…I'm not sure what that means."
    pc "Here is the hoodie by the way."
    lisa "Thanks…think I might need my other clothes first."
    pc "Not that I am kicking you out right now if you fancy hanging out for a little bit."
    pc "I was probably just going to have a quiet night, watch a film or something?"
    lisa "Yeah sure, maybe we could order some food too."
    pc "Sounds good to me."
    ##Lisa smirking##
    lisa "I bet it does."
    pc "I didn’t…I just meant."
    lisa "So unbelievably easy, teasing you is going to be so much fun."
    pc "I’ll go get the menu, why don't you pick out something to watch."
    "Grabbing the menu, Lisa puts on a sports film for you both to watch."
    "Relaxing on the sofa together, the food soon arrives."
    ##Table covered in food##
    pc "Did we really order this much?"
    lisa "I may have added a couple of extra things before we submitted it."
    lisa "I was kind of planning on a binge sometime this week so why not tonight."
    pc "Especially since I offered to pay?"
    lisa "I get food, you get a show, Marie gets a fat and bloated girlfriend. It’s a win, win win."
    "Grabbing the first part of her meal, Lisa digs in as you sit back to watch the rest of the move."
    "It doesn’t take her long to finish her first plate and quickly goes in for seconds."
    "Your attention is split between the movie and Lisa’s buffet."
    "Burgers, fries, onion rings and more all disappearing into her hungry mouth."
    "It was a good job you had already seen the film before, it gave you more time to watch her stomach grow."
    "By the end of the film, the table was clear."
    lisa "Pfff, that was a good film but I am so full right now I don't really remember what happened."
    lisa "I could fall asleep right here."
    "Rubbing her giant and distended belly, Lisa seems at peace with the world."
    "However, a few moments later you hear her phone vibrate."
    pc "What are the chances that’s Marie?"
    lisa "Oh, she would love to see me like this."
    lisa "Crap!"
    lisa "I can’t believe I have done this again!"
    pc "What’s wrong?"
    lisa "It’s Mandy. We are supposed to be going out for her fiance’s birthday."
    pc "When?"
    lisa "Right now, I am already late."
    "Standing up, Lisa starts to get dressed. Although if her clothes didn’t fit her earlier there was no chance they would now."
    lisa "God, and it’s at this BBQ place which is known for massive portions."
    pc "Maybe you could cancel, say you are not feeling well?"
    lisa "No, my sister would know it was a lie,I saw her this morning."
    lisa "Plus, this place has a waiting list of like two months."
    lisa "I’m seriously going to explode if I eat any more."
    lisa "Although it serves Marie right though."
    pc "What?"
    lisa "She was supposed to come with me tonight but chickened out."
    lisa "Guess it’s her loss, not able to see me stuff myself even more…ughh, if I can."
    lisa "Sorry to leave you with the mess."
    pc "No, it’s alright. I’ll tidy up."
    lisa "Thanks, I had fun tonight."
    pc "Me too, enjoy your BBQ."
    lisa "Try not to pop you mean."
    lisa "Thanks, anyway. See you around."
    pc "Bye Lisa."
    "Watching her leave, she had even forgotten your hoodie, not that it would do much good now anyway."
    "She might have gotten away with it earlier, but there was no way people wouldn’t notice her now."
    "Cleaning up your food, you get ready to call it a night."

    "Feeling a vibration in your pocket, you pull out your phone to see a text from Lisa."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Lisa', dialogue=dialogue_one)
    $ msg ("Ughh, I survived…barely.", who=1)
    pause
    $ msg ("I Sent these to Marie, I figured you might like a copy too ;).", who=1)
    pause
    $ msg (None, who=1, pic="stage7_lisa1")
    pause
    $ msg (None, who=1, pic="stage7_lisa2")
    pause
    $ msg ("Next time we hang out like that, can you ask me what my plans are first.", who=1)
    pause
    $ msg ("Sure thing, although you act like this isn’t what you want too.")
    pause
    $ msg ("Hey, I am supposed to be the one teasing you.", who=1)
    pause
    $ msg ("But now I think I'm going to go and sleep for the next few days until this goes down.", who=1)
    pause
    $ msg ("Goodnight Lisa.")
    pause
    $ hide_messenger()
    stop music fadeout 1.0
    if recollection == False:
        $ lisa.weight += 1
        $ daytime = 4
    $ lisastage7event2 = 0
    return


label Lisa_repeatable_pub:
    #REPEATABLE VERSION OF OUTDOOR CAFE:
    scene pub
    "You head to the usual pub where you and Lisa hang out after work."
    image lisa_pub1 = "/lisa/[lisa.stage]/pub1.webp"
    scene lisa_pub1
    "She's already there at your usual table and waves at you as soon as you walk in the door."
    lisa "Hey there! Sorry I ordered appetizers for us but then I got hungry and ate them all. Then I ordered this."
    image lisa_pub2 = "/lisa/[lisa.stage]/pub2.webp"
    scene lisa_pub2
    "You look down at the burger Lisa is currently holding. You notice the second plate under the one she's currently using, implying that this is her second helping."
    "This gives you an idea. You order a couple burgers but you don't touch them. You just watch Lisa enjoy her food."
    image lisa_pub3 = "/lisa/[lisa.stage]/pub3.webp"
    scene lisa_pub3
    lisa "You're being pretty quiet."
    pc "Oh I just had a long day."
    lisa "Mmph, tell me about it *urp!* I've been starving since this afternoon!"
    "Finally she finishes off her burger and fries. It's time to put your plan into action, all you have to do is pretend you're full and offer her-"
    image lisa_pub4 = "/lisa/[lisa.stage]/pub4.webp"
    scene lisa_pub4
    lisa "Hey are you gonna finish those?"
    pc "Uhhh no?"
    lisa "Cool, can I have them?"
    pc "Sure!"
    "Well that was easy..."
    image lisa_pub5 = "/lisa/[lisa.stage]/pub5.webp"
    scene lisa_pub5
    "Lisa grabs the burgers right out of your plate and starts eating fervently, holding a burger in each hand."
    "She seems to delight in making a mess as she eats, grease dripping on her as she feasts."
    image lisa_pub6 = "/lisa/[lisa.stage]/pub6.webp"
    scene lisa_pub6
    "Finally, she leans back in her chair, letting out a sigh of satisfaction."
    lisa "Oh wow, I am STUFFED. Good thing I don't eat like that every day or I'd get seriously plump haha."
    #"Just then she seems to have a thought. She keeps talking in a lower tone of voice, as if to yourself like you weren't there."
    #lisa "I wonder if Amber or Marie like girls that are a bit thicker..."
    #"She bites her lip and goes back to her regular tone."
    lisa "I think I'll take a look at the dessert menu."
    image lisa_pub7 = "/lisa/[lisa.stage]/pub7.webp"
    scene lisa_pub7
    "One chocolate lava cake later, Lisa was well and truly full. Too tired to even wipe the chocolate smeared around her mouth, she just sits there breathing shallowly as she rubs her belly."
    "If you didn't know any better you could've sworn her clothes actually got tighter from the cake."
    image lisa_pub8 = "/lisa/[lisa.stage]/pub8.webp"
    scene lisa_pub8
    lisa "URRRRRP, god that was amazing. We have got to do this more often."
    pc "Definitely..."
    image lisa_pub9 = "/lisa/[lisa.stage]/pub9.webp"
    scene lisa_pub9
    "You help Lisa out of her seat and pay the bill. Once you've exited the pub and said your goodbyes, you watch her walk (or rather waddle) off into the night."
    $ lisa.weight += 0.5
    return

label Lisa_home:
    #REPEATABLE HOME EVENT - TRIGGERED BY HER CALLING YOU TO FEED HER FOR MARIE
    "You make your way over to Lisa's home."
    image lisa_home_arrive = "/lisa/[lisa.stage]/home_arrive.webp"
    scene lisa_home_arrive
    lisa "Hey, [playername]. Thanks for coming."
    image lisa_home_question = "/lisa/[lisa.stage]/home_question.webp"
    scene lisa_home_question
    lisa "Did you bring extra food?"
    pc "Yes, I did."
    lisa "Great. Let's get started then."
    image lisa_home_eating = "/lisa/[lisa.stage]/home_eating.webp"
    scene lisa_home_eating
    "Lisa makes short work of all the sweets you hand to her."
    "You aren't sure if it is love that drives her increasing appetite or if she is growing to be more greedy."
    image lisa_home_strip = "/lisa/[lisa.stage]/home_strip.webp"
    scene lisa_home_strip
    lisa "My belly needs all the room it can get."
    "She opens up her jeans to reveal her slightly bloated belly."
    lisa "Let's fill this baby up, shall we?"
    image lisa_home_stripeating = "/lisa/[lisa.stage]/home_stripeating.webp"
    scene lisa_home_stripeating
    "Without a second thought Lisa starts chewing through the rest of all the food."
    "Clearly determined she doesn't slow down until the final bit of food is eaten."
    image lisa_home_stuffed = "/lisa/[lisa.stage]/home_stuffed.webp"
    scene lisa_home_stuffed
    window hide
    pause
    if lisaundressoption == 0 and lisa.stage == 11:
        $ lisaundressoption = 1
        #Unlocks Lisa Undress in the stats page.
        $ renpy.notify("Lisa Undress option unlocked in stats screen.")
        window hide
        pause
    lisa "Oh, that feels good!"
    lisa "Thank you once again. I'm sure Marie will enjoy seeing me grow."
    "You help clean up the left behind food packages and then say your goodbyes."
    $ lisa.weight += 0.5
    return


    "You make your way over to Lisa's home."

    image lisa_home_arrive = "/lisa/[lisa.stage]/home_arrive.webp"
    scene lisa_home_arrive
    if lisa.stage <= 4:
        lisa "Hey, thanks for coming."
        image lisa_home_question = "/lisa/[lisa.stage]/home_question.webp"
        scene lisa_home_question
        lisa "Do you want a drink or anything?"
        pc "No, I'm ok but thanks for the offer."
        image lisa_home_sitting = "/lisa/[lisa.stage]/home_sitting.webp"
        scene lisa_home_sitting
        lisa "Great. I guess we can get started now."
        lisa "I bought some food back from Bunny Bites."
    elif lisa.stage == 5:
        lisa "Hey, thanks for coming over again."
        image lisa_home_question = "/lisa/[lisa.stage]/home_question.webp"
        scene lisa_home_question
        lisa "I appreciate you probably have other things you would rather do."
        pc "It’s always fun hanging out with you, so I really don't mind."
        image lisa_home_sitting = "/lisa/[lisa.stage]/home_sitting.webp"
        scene lisa_home_sitting
        lisa "Great. Foods in the usual place."
    elif lisa.stage >= 6:
        lisa "Hey, thanks for coming over again."
        image lisa_home_question = "/lisa/[lisa.stage]/home_question.webp"
        scene lisa_home_question
        lisa "Did you pick up the extra food?"
        pc "I did, feeling hungry tonight?"
        image lisa_home_sitting = "/lisa/[lisa.stage]/home_sitting.webp"
        scene lisa_home_sitting
        if lisa.stage == 6:
            lisa "Yes, but also me and Marie might have something planned."
            lisa "I want to be bigger next time I see her."
        elif lisa.stage >= 7:
            lisa "More like I'm feeling determined, I really want to balloon for Marie.”"
            lisa "I have been enjoying my time with her so much lately, I can't wait to get even bigger for her!"
        pc "Great, shall we get started then?"
        lisa "Absolutely."

    ##Table with food.##
    if lisa.stage <= 4:
        pc "What do you fancy?"
        lisa "The burgers are always good."
        #PIC NEEDED
        "Grabbing the first burger, you hand it to her."
        "Eating quickly, Lisa makes short work of the first burger."
        lisa "How about those nuggets next?"
        #PIC NEEDED
        "Listening to her, you grab the box of nuggets and slowly begin feeding them to her."
        "Making small talk you try to keep her distracted as you feed her."
        #PIC NEEDED
        "Soon, almost all the food has disappeared."
        lisa "Oooh, starting to get full now."
        image lisa_home_strip = "/lisa/[lisa.stage]/home_strip.webp"
        scene lisa_home_strip
        "Leaning back, Lisa opens up her jeans to reveal her slightly bloated belly."
        #PIC NEEDED
        lisa "Let’s keep going shall we?"
        #PIC NEEDED
        "As she dives back in, you aren’t sure if it is love or gluttony that drives her increasing appetite."
        "Without a second thought Lisa starts chewing through the rest of all the food."
        #PIC NEEDED
        "Clearly determined she doesn't slow down until the final bit of food is eaten."
        #PIC NEEDED
        lisa "My stomach is so tight."
        pc "You did well, that was a lot of food."
        #PIC NEEDED
        lisa "Thanks, I hope it is enough for Marie."
        lisa "Although I am not sure I will ever get used to feeling this full."
        lisa "Right now though, I think I need to collapse on my bed and not move for a few hours and let this go down."
        #PIC NEEDED
        lisa "Thank you once again. I’m sure Marie will enjoy seeing me grow."
    elif lisa.stage == 5:
        pc "What do you fancy?"
        lisa "How about we start with some pizza this time."
        "Grabbing a slice of pizza, you hand it to her."
        "Eating quickly, Lisa makes short work of the first few slices."
        lisa "I’m definitely getting better at this, those barely made a dent."
        lisa "How about some onion rings?"
        "Listening to her, you grab the box of onion rings and slowly begin feeding them to her."
        "Making small talk you try to keep her distracted as you feed her."
        "Soon, almost all the food has disappeared."
        lisa "I can’t believe how much I have eaten already."
        lisa "I’m sure it was about now I used to have to slow down because I was getting so full."
        lisa "Although while I still have room, the same can not be said for my jeans."
        "Leaning back, Lisa opens up her jeans to reveal her slightly bloated belly."
        lisa "Let’s keep going shall we?"
        "As she dives back in, you aren’t sure if it is love or gluttony that drives her increasing appetite."
        "Without a second thought Lisa starts eating through the rest of the food."
        "Clearly determined she doesn't slow down until the final bit of food is eaten."
        lisa "Mmmm…so full."
        lisa "I can’t wait till Marie sees me like this herself."
        lisa "Looks like we are out of food though."
        pc "Maybe I should bring extra next time."
        lisa "I think this is more than enough."
        "Despite saying that, you can see she is tempted by the idea but don't press her on it just yet."
        lisa "Thank you once again. I’m sure Marie will enjoy seeing me grow."
    elif lisa.stage == 6:
        pc "What do you fancy?"
        lisa "Why don't you pick this time?"
        "Grabbing a burger, you hand it to her."
        "Eating quickly, Lisa makes short work it and you quickly hold up the next."
        "Taking a more active role than usual, you keep her eating which she seems to appreciate."
        lisa "Mmm, starting to get full."
        pc "Plenty more food to go though."
        lisa "Good, let me just."
        "Leaning back, Lisa opens up her jeans to reveal her slightly bloated belly."
        lisa "That’s better. Let’s keep going shall we?"
        "Listening to her, you grab a box of onion rings and begin feeding them to her."
        "Making small talk you try to keep her distracted as you feed her."
        "Soon, the table is empty and Lisa has eaten all her arranged food."
        lisa "My belly is so bloated."
        pc "We still have the stuff I brought with me."
        lisa "I don't know how much more I can manage."
        lisa "But let’s keep going."
        "Reaching into the bag, you pull out one of the sweet treats you brought with you."
        lisa "Oooh, I’ll always have room for dessert."
        "Without a second thought Lisa starts eating through the rest of the food."
        "Clearly determined she doesn't slow down until the final bit of food is eaten."
        lisa "Wow, that was so much food."
        lisa "I can’t believe I managed to eat all of that."
        lisa "Do you think I am big enough for Marie yet?"
        pc "I don't know if there is a safe answer for me to say to that."
        lisa "Good call, let’s do this again soon."
    elif lisa.stage >= 7:
        pc "Is this more than last time?"
        lisa "Maybe…"
        "From the look on Lisa’s face this is definitely more than last time."
        pc "What did you want to start with?"
        lisa "Why don't you pick and…"
        lisa "I don't want you to stop until everything is gone."
        pc "Are you sure, this is a lot of food."
        lisa "Duh, that’s the point."
        pc "You know Marie would love to do this with you as well."
        lisa "I know, but I like surprising her with just how much I can eat on our dates."
        lisa "So come on, start feeding me!"
        "Grabbing a burger, you hand it to her."
        "Eating quickly, Lisa makes short work of it and you quickly hold up the next."
        "Taking a more active role than usual, you keep her eating which she seems to appreciate."
        "It doesn’t take long for most of the food to disappear into Lisa’s growing tummy."
        lisa "I don't know why I even bother with these things."
        "Standing up, Lisa removes her jeans before lounging back."

        ###I am thinking it could be a new position / actual feeding minigame after this point?###
        lisa "That’s better. Let’s keep going shall we?"
        "Grabbing a burger Lisa lets you feed it to her directly this time."
        lisa "Mmm, make me big and fat for Marie!"
        #[Feed / dont feed]#
        lisa "This is much better than feeding myself."
        #[Feed / dont feed]#
        lisa "Look at how big my belly is, I barely recognise myself these days."
        #[Feed / dont feed]#
        lisa "Feed me for Marie."
        #[Feed / dont feed]#
        lisa "I don't know how much more I can eat."
        "Lisa’s stomach is definitely bigger than when you started."
        #[Feed / dont feed]#
        lisa "Ughh, starting to ache down there."
        #[Feed / dont feed]#
        lisa "I think I am at my limit."
        pc "I think you can manage one more thing."
        lisa "You are right, for Marie."
        #[Feed / dont feed]#
        lisa "Oooh, that was so much food."
        lisa "I feel so big and bloated, my belly aches so much now."
        pc "You did a good job, Marie will be impressed on your next date."
        lisa "I hope so."

        #BELLYRUB
        "Gently touching her stomach, you rub in soothing circles."
        pc "You look so full."
        lisa "Oooh, keep going, that feels kind of good."
        lisa "Like a soothing massage after eating all that food."
        lisa "You can do my feet next if you want?"
        pc "I think I'll leave that to you."
        lisa "Ok, this feels nice though."
        pc "Think you can manage a bit more now?"
        lisa "I think so."

    "You help clean up the left behind food packages and then say your goodbyes."
    return

label Lisa_BB_Extra:
    "You decide to pay the difference yourself."
    $ money -= 5
    image cafe_lisa_extrafood = "/lisa/[lisa.stage]/cafe_extrafood.webp"
    scene cafe_lisa_extrafood
    lisa "Whoa, this is way more than I ordered."
    pc "My bad. It's already been paid for so do you just want it anyway?"
    lisa "Well, I won't say no to free food!"
    pc "Awesome, enjoy."
    lisa "Thanks!"
    if lisa.stage >= 11:
        image cafe_lisa_struggle = "/lisa/[lisa.stage]/cafe_struggle.webp"
        scene cafe_lisa_struggle
        "You notice that Lisa was able to eat all the extra food you made for her."
        "It is amazing how much the short woman is able to eat."
        image cafe_lisa_struggle_belly = "/lisa/[lisa.stage]/cafe_struggle_belly.webp"
        scene cafe_lisa_struggle_belly
        "Looking down, you see where all that food went."
        "Her belly must have grown to twice the size while she was here."
    else:
        image cafe_lisa_struggle = "/lisa/[lisa.stage]/cafe_struggle.webp"
        scene cafe_lisa_struggle
        "You notice Lisa struggling to eat all of the extra food."
    return

label Lisa_BB_Prize:
    image cafe_lisa_prize1 = "/lisa/[lisa.stage]/cafe_prize1.webp"
    scene cafe_lisa_prize1
    "Creating a sizable feast, you approach Lisa."
    pc "Congratulations, you are the winner of this week's prize!"
    image cafe_lisa_prize2 = "/lisa/[lisa.stage]/cafe_prize2.webp"
    scene cafe_lisa_prize2
    if lisaprizefirsttime == 1:
        lisa "Are you sure, I thought it was just for the customers?"
        pc "Nope, every order counts."
        lisa "Ok, well I am not going to complain."
        lisa "It's still free right, even for us?"
        pc "Absolutely."
        lisa "Great!"
        image cafe_lisa_prize3 = "/lisa/[lisa.stage]/cafe_prize3.webp"
        scene cafe_lisa_prize3
        "Bringing the food over to the table, Lisa slowly begins to eat the giant mound in front of her."
        image cafe_lisa_prize4 = "/lisa/[lisa.stage]/cafe_prize4.webp"
        scene cafe_lisa_prize4
        "Picking up a burger she slowly chews her way through it, she doesnt appear to be in a hurry today."
        "Moving on, she picks and chooses her food, eating as if it just another meal."
        image cafe_lisa_prize5 = "/lisa/[lisa.stage]/cafe_prize5.webp"
        scene cafe_lisa_prize5
        "However, it isn't too long before she reaches her limit and is forced to stop eating."
        image cafe_lisa_prize6 = "/lisa/[lisa.stage]/cafe_prize6.webp"
        scene cafe_lisa_prize6
        pc "How was the food?"
        lisa "Good, although far too much of it."
        lisa "I can see why it would bring in the customers though, smart idea by Marie."
        pc "I'll pack the rest up so you can take it home with you."
        lisa "Thanks."
        $ lisaprizefirsttime = 0
    else:
        lisa "Again, did Marie have something to do with this?"
        pc "Completely random."
        lisa "Oh, well. I kind of liked the idea she was doing this to fatten me up even more."
        "You don't doubt that had something to do with Marie making this contest in the first place."
        image cafe_lisa_prize3 = "/lisa/[lisa.stage]/cafe_prize3.webp"
        scene cafe_lisa_prize3
        "Bringing the food over to the table, Lisa immediately digs in."
        image cafe_lisa_prize4 = "/lisa/[lisa.stage]/cafe_prize4.webp"
        scene cafe_lisa_prize4
        "Picking up a burger takes large bites out of it, her eating really seems to have increased in recent days."
        "Moving on, she picks up some slices of Pizza, then fries and onion rings."
        "Forcing herself to eat, she begins to slow as her stomach swells uncomfortably."
        image cafe_lisa_prize5 = "/lisa/[lisa.stage]/cafe_prize5.webp"
        scene cafe_lisa_prize5
        "Eventually she grinds to a halt, puffing out her cheeks and leaning back, stuffed.."
        image cafe_lisa_prize6 = "/lisa/[lisa.stage]/cafe_prize6.webp"
        scene cafe_lisa_prize6
        pc "How was the food?"
        lisa "I want to keep eating more for Marie, but I don't think I could fit another bite inside me."
        pc "I'll pack the rest up so you can take it home with you."
        lisa "Thanks, I definitely need to let this go down before I eat anything else though."
    image cafe_lisa_prize7 = "/lisa/[lisa.stage]/cafe_prize7.webp"
    scene cafe_lisa_prize7
    "Returning a few minutes later, you hand Lisa two large bags of food to take home with her."
    "Watching her leave. you return to the front counter and continue working."
    return
