label Rebecca_Stage_2_Event:
    ###Rebecca Stage 2 (First solo stage? For replays)###
    ### Scene image - In PC room scene like normal ###
    "You receive a message on your phone from an unknown number."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Unknown', dialogue=dialogue_one)
    $ msg ("Hey, it's [playername] right?", who=1)
    pause
    $ msg ("Found your phone number in my diary. You remember our little proposition?", who=1)
    pause
    $ msg ("Swing round my place later, I might need a hand with something. Rebecca.", who=1)
    pause
    $ hide_messenger()
    #[GAME – YES / Not tonight options]
    #IF YES
    menu:
        "Not tonight.":
            "You decide not to visit Rebecca."
            return
        "Visit Rebecca.":
            "You save Rebecca's number and get yourself ready to head out."

    ###Outside Rebecca's shop ###
    scene city
    "Approaching the building you start to feel a little conflicted. Should you be helping Rececca so soon after becoming Bonnie's partner?"
    "Although in a way, it is now technically your shop too."
    "As long as you don't do anything to jeopardise it, there should be no reason to worry."
    ###Rebecca behind the counter of her shop ###
    image rebecca_stage_2_event_1 = "/rebecca/events/stage2/1.webp"
    scene rebecca_stage_2_event_1
    rebecca "Hello again. Glad you could make it."
    pc "I have to admit, I was a little surprised to be hearing from you so soon."
    rebecca "Don't play coy with me, you were the one who left your number in my notebook remember."
    pc "I guess that's true, what can I help you with?"
    image rebecca_stage_2_event_2 = "/rebecca/events/stage2/2.webp"
    scene rebecca_stage_2_event_2
    rebecca "Not here, you never know who is listening."
    pc "Listening?"
    "Nodding with her head towards the door, she quickly flips the sign on the door to closed."
    ###Rebecca’s house on the sofa ####
    image rebecca_stage_2_event_3 = "/rebecca/events/stage2/3.webp"
    scene rebecca_stage_2_event_3
    "Following Rebecca through her house she motions for you to sit down."
    image rebecca_stage_2_event_4 = "/rebecca/events/stage2/4.webp"
    scene rebecca_stage_2_event_4
    rebecca "Corporate spies are everywhere, you never know who is out to get your recipes."
    pc "Sure…"
    rebecca "Which is why I brought you here."
    pc "Me, I'm not a spy?"
    image rebecca_stage_2_event_5 = "/rebecca/events/stage2/5.webp"
    scene rebecca_stage_2_event_5
    rebecca "No I know, I mean…I was."
    rebecca "Or I was attempting to be, unsuccessfully it would seem."
    rebecca "I watched you closely when you were here last time, yet even with the ingredients and measurements memorised, I couldn't replicate those delicious…creamy…chocolates."
    "It seems even the mention of those chocolates is enough to distract her as she stares off into the distance for a moment."
    pc "I thought you agreed not to sell them?"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/rebecca/events/stage2/idle.webm" loop
    show movie with dissolve
    rebecca "I did and I wasn't trying to. I was… trying to remake them for myself."
    rebecca "I've never had anything like them, the impact they can have on a person."
    rebecca "But despite my experience, despite knowing the recipe, I still failed to come close even after dozens of batches."
    pc "If you know the recipe, why am I here?"
    rebecca "I need you to make more, to watch you work and see what you do."
    rebecca "Either I am making a mistake, or there is something special about you."
    pc "Special?"
    rebecca "Or at least special in the way you make the chocolates."
    pc "This is all sounding a bit weird, you are not about to say the secret ingredient is love or something?"
    rebecca "Of course not, but even you have to admit the reactions to your chocolates have been particularly strong."
    pc "I just thought they were good chocolates."
    stop movie
    image rebecca_stage_2_event_6 = "/rebecca/events/stage2/6.webp"
    scene rebecca_stage_2_event_6
    rebecca "They are, trust me."
    rebecca "But something else is going on, I can feel it."
    pc "Well, I guess I have already agreed to make you chocolates when you want them."

    ###Rebecca’s kitchen with her ####
    image rebecca_stage_2_event_7 = "/rebecca/events/stage2/7.webp"
    scene rebecca_stage_2_event_7
    "Grabbing the pan you are met with a familiar feeling, although it's a bit strange."
    "From the house to the equipment, everything is almost identical to when you do this for Bonnie, just slightly off."
    image rebecca_stage_2_event_8 = "/rebecca/events/stage2/8.webp"
    scene rebecca_stage_2_event_8
    "Standing ahead of you, Rebecca watches your every move just as Bonnie would."
    "Although her gaze is far more analytical than that of your partner."
    "Taking more care and time with each step, you try to demonstrate your techniques."
    "That way she could replicate them later on, giving herself an endless supply of these treats to gorge herself with."
    image rebecca_stage_2_event_9 = "/rebecca/events/stage2/9.webp"
    scene rebecca_stage_2_event_9
    "As much as she had made fun of Bonnie, she was well on her way to following her into weight gain."
    image rebecca_stage_2_event_10 = "/rebecca/events/stage2/10.webp"
    scene rebecca_stage_2_event_10
    rebecca "Interesting, I still don't know why you do it that way."
    rebecca "It seems counterintuitive to everything I have learned."
    pc "I don't know, I just mostly followed the instructions?"
    image rebecca_stage_2_event_11 = "/rebecca/events/stage2/11.webp"
    scene rebecca_stage_2_event_11
    rebecca "Instructions?"
    rebecca "Please don't tell me this has all come from some book."
    pc "Yeah, plus some tweaks from what I have learned from Bonnie."
    pc "In fact, I think it was one of your old books."
    image rebecca_stage_2_event_12 = "/rebecca/events/stage2/12.webp"
    scene rebecca_stage_2_event_12
    rebecca "Sweet tooths!"
    rebecca "I should have recognised the recipe, but how did you find it?"
    image rebecca_stage_2_event_13 = "/rebecca/events/stage2/13.webp"
    scene rebecca_stage_2_event_13
    rebecca "That series is very rare and hard to come by."
    rebecca "I had looked for a copy for years before eventually I found it…"
    image rebecca_stage_2_event_14 = "/rebecca/events/stage2/14.webp"
    scene rebecca_stage_2_event_14
    rebecca "You go to the university in town don't you?"
    pc "Yeah, I saw the book number thing and just went to the library."
    image rebecca_stage_2_event_15 = "/rebecca/events/stage2/15.webp"
    scene rebecca_stage_2_event_15
    rebecca "Interesting, I still don't know why of all places a second rate university in a town like this has a copy."
    "Part of you wonders if Daisy had something to do with that, given she was the one who pointed you in the direction of the second book."
    image rebecca_stage_2_event_16 = "/rebecca/events/stage2/16.webp"
    scene rebecca_stage_2_event_16
    rebecca "I swear, I did all of this last time."
    rebecca "It just makes no sense. Basic ingredients, basic skills from someone with little to no education or talent."
    pc "Thanks…"
    rebecca "Just analysing the situation and at the moment, the variables don't match up."
    pc "Well, they are done if you want to try them."
    image rebecca_stage_2_event_17 = "/rebecca/events/stage2/17.webp"
    scene rebecca_stage_2_event_17
    "At the mere suggestion of eating more chocolates you see her eyes light up, darting to the tray."
    rebecca "No…I shouldn't"
    pc "But how else will you know if they are the same?"
    image rebecca_stage_2_event_18 = "/rebecca/events/stage2/18.webp"
    scene rebecca_stage_2_event_18
    rebecca "But…"
    "The analytical side of her mind had been in charge while you were making them, but now that they were done you could see the same hunger in her eyes from last time."
    image rebecca_stage_2_event_19 = "/rebecca/events/stage2/19.webp"
    scene rebecca_stage_2_event_19
    "Taking the first chocolate Rebecca pauses, clearly trying to control herself before popping it into her mouth."
    image rebecca_stage_2_event_20 = "/rebecca/events/stage2/20.webp"
    scene rebecca_stage_2_event_20
    rebecca "Mmmmm!"
    rebecca "Just so good, It doesn't…I can't…"
    image rebecca_stage_2_event_21 = "/rebecca/events/stage2/21.webp"
    scene rebecca_stage_2_event_21
    "Lost for words she gazes down at the chocolates on her counter."
    image rebecca_stage_2_event_22 = "/rebecca/events/stage2/22.webp"
    scene rebecca_stage_2_event_22
    "Unable to fight the desire to eat them, Rebecca almost dives for the other chocolates as she begins to stuff her mouth full of them."
    "Her insatiable appetite for your chocolates once more taking over, just as it had last time."
    image rebecca_stage_2_event_23 = "/rebecca/events/stage2/23.webp"
    scene rebecca_stage_2_event_23
    "One after another they disappear, the fattening treats devoured before your eyes."
    rebecca "Mhhhm, so good."
    image rebecca_stage_2_event_24 = "/rebecca/events/stage2/24.webp"
    scene rebecca_stage_2_event_24
    "Starting on the next tray she continues to eat."
    image rebecca_stage_2_event_25 = "/rebecca/events/stage2/25.webp"
    scene rebecca_stage_2_event_25
    "Despite being small individually, Rebecca's belly was starting to grow as they piled up inside her."
    image rebecca_stage_2_event_26 = "/rebecca/events/stage2/26.webp"
    scene rebecca_stage_2_event_26
    window hide
    pause
    image rebecca_stage_2_event_27 = "/rebecca/events/stage2/27.webp"
    scene rebecca_stage_2_event_27
    pause
    image rebecca_stage_2_event_28 = "/rebecca/events/stage2/28.webp"
    scene rebecca_stage_2_event_28
    "At her rapid pace it doesn't take long for them all to be gone, what took Bonnie a week to eat disappearing in mere minutes."
    image rebecca_stage_2_event_29 = "/rebecca/events/stage2/29.webp"
    scene rebecca_stage_2_event_29
    "Slumping to the floor Rebecca comes back to her senses, rubbing her distended stomach."
    rebecca "I don't understand."
    rebecca "It's like nothing I have ever seen before, never felt before."
    rebecca "The ingredients and cooking method are the same, the only difference is…"
    image rebecca_stage_2_event_30 = "/rebecca/events/stage2/30.webp"
    scene rebecca_stage_2_event_30
    "Turning to look at you she has a strange look on her face, creeping you out a little bit."
    rebecca "You, it has to be you!"
    pc "What has to be me?"
    rebecca "The only variable that is different between now and my tests is you."
    pc "So what?"
    image rebecca_stage_2_event_31 = "/rebecca/events/stage2/31.webp"
    scene rebecca_stage_2_event_31
    rebecca "I don't know yet, but I will find out soon."
    rebecca "Although, I might need some help to fully understand what is going on."
    pc "Ok, but this is getting a bit weird again. Figure out what?"
    rebecca "Not weird, interesting."
    image rebecca_stage_2_event_32 = "/rebecca/events/stage2/32.webp"
    scene rebecca_stage_2_event_32
    "Standing up with a new energy, she all but shoves you out of the door."
    rebecca "I need time to think and arrange some things."
    pc "I…ok"
 
    ###Outside###
    scene city_night
    "Well that was strange and much less fun than your evenings with Bonnie."
    "Although, if she really can figure out what is happening, maybe you could use it for other things."
    "Either way, with her lack of control you were certain this would be the smallest Rebecca would ever be again."
    if recollection == False:
        $ rebecca.weight += 2
        $ daytime += 1
        $ phonecall = 1
    $ rebeccastage2event = 0
    return


label Rebecca_Stage_3_Event:
    ##After working with Bonnie to make chocolates.##
    scene city_night
    "Stepping out of the shop, you breathe in the evening air."
    "Working with Bonnie always put you in a good mood, for obvious reasons."
    image rebecca_stage_3_event_1 = "/rebecca/events/stage3/1.webp"
    scene rebecca_stage_3_event_1
    "In front of you, movement catches your eye as a figure seems to walk towards and then turn away from the shop."
    image rebecca_stage_3_event_2 = "/rebecca/events/stage3/2.webp"
    scene rebecca_stage_3_event_2
    "Looking closer, you notice Rebecca. She seems to be talking to herself, debating something."
    "Before you can approach, she turns on her heels and with a lingering look towards the shop she walks away."
    "Was she avoiding you…or the chocolates?"
    image rebecca_stage_3_event_3 = "/rebecca/events/stage3/3.webp"
    scene rebecca_stage_3_event_3
    "Deciding to play devils advocate, you quickly head back into the shop and grab a few boxes of the new chocolates."
    "You always made too many anyway."
    ##Outside Cafe scene ###
    image rebecca_stage_3_event_4 = "/rebecca/events/stage3/4.webp"
    scene rebecca_stage_3_event_4
    "Catching up with Rebecca, you follow her back towards the main street."
    image rebecca_stage_3_event_5 = "/rebecca/events/stage3/5.webp"
    scene rebecca_stage_3_event_5
    "You see her heading into the cafe."
    image rebecca_stage_3_event_6 = "/rebecca/events/stage3/6.webp"
    scene rebecca_stage_3_event_6
    "Through the window, you see her order a large slice of cake and take a seat."
    menu:
        "Leave her be.":
            ##If leave her be###
            scene city_night
            "You decide that if she wanted to say hello, she would have."
            "Carrying the chocolates back, you are sure Daisy would love these extra chocolates anyway."
            #[Adds 5 meals].
            $ foodheld += 5
            return
        "Go and say hello.":
            ##If go and say hi##
            "You decide to go and say hello."
    image rebecca_stage_3_event_7 = "/rebecca/events/stage3/7.webp"
    scene rebecca_stage_3_event_7
    pc "I thought that was you."
    rebecca "Oh…[playername]."
    pc "Mind if I join you?"
    rebecca "I suppose not."
    pc "So doing some evening shopping?"
    image rebecca_stage_3_event_8 = "/rebecca/events/stage3/8.webp"
    scene rebecca_stage_3_event_8
    rebecca "What?"
    pc "Sorry, I was just wondering what might have brought you into town."
    pc "It's a bit of a walk from your place isn't it?"
    image rebecca_stage_3_event_9 = "/rebecca/events/stage3/9.webp"
    scene rebecca_stage_3_event_9
    rebecca "Oh yes, I had…a meeting nearby."
    pc "Ah ok, anything I can help with?"
    rebecca "No…or at least not yet."
    image rebecca_stage_3_event_10 = "/rebecca/events/stage3/10.webp"
    scene rebecca_stage_3_event_10
    "As you talk, you can see her eyes occasionally flicking over to the boxes of chocolates you have placed on the table."
    "Is it fear in her eyes…or lust?"
    image rebecca_stage_3_event_11 = "/rebecca/events/stage3/11.webp"
    scene rebecca_stage_3_event_11
    rebecca "What about you?"
    pc "Oh, I was just helping Bonnie out."
    pc "We've been selling a lot the past few days."
    image rebecca_stage_3_event_12 = "/rebecca/events/stage3/12.webp"
    scene rebecca_stage_3_event_12
    rebecca "Are those…the chocolates?"
    pc "They are…would you like some?"
    rebecca "No, I can't eat any more of them!"
    pc "Are you sure I can't tempt you?"
    image rebecca_stage_3_event_13 = "/rebecca/events/stage3/13.webp"
    scene rebecca_stage_3_event_13
    "Opening the lid of a box you gently push it towards her."
    rebecca "I…."
    rebecca "I know what you are doing."
    image rebecca_stage_3_event_14 = "/rebecca/events/stage3/14.webp"
    scene rebecca_stage_3_event_14
    rebecca "You are doing it on purpose, are you trying to get your own back on me for what I did with Bonnie?"
    rebecca "I thought we had a deal."
    rebecca "Please, you don't need to ruin my waistline as well."
    image rebecca_stage_3_event_15 = "/rebecca/events/stage3/15.webp"
    scene rebecca_stage_3_event_15
    "Even as she speaks, she salivates, her eyes locked on the chocolates."
    pc "I don't know what you mean."
    pc "They are just, chocolates."
    pc "Silky smooth, sugary, creamy and delicious chocolates."
    "You can see Rebecca's resolve weakening."
    image rebecca_stage_3_event_16 = "/rebecca/events/stage3/16.webp"
    scene rebecca_stage_3_event_16
    "With a final push you nudge the box closer to her and she immediately grabs one."
    "Stuffing it into her mouth, she lets out a primal moan of delight."
    image rebecca_stage_3_event_17 = "/rebecca/events/stage3/17.webp"
    scene rebecca_stage_3_event_17
    rebecca "Yesss!"
    rebecca "Too good, I…"
    "But one taste is never enough for her."
    image rebecca_stage_3_event_18 = "/rebecca/events/stage3/18.webp"
    scene rebecca_stage_3_event_18
    "Going in for more, Rebecca grabs handfuls at a time."
    "Shoving them into her mouth she noisily eats, moaning and snarling as she stuffs her face."
    image rebecca_stage_3_event_19 = "/rebecca/events/stage3/19.webp"
    scene rebecca_stage_3_event_19
    "With an animalistic intensity she tears into the other boxes, shovelling them into her chocolate smeared mouth."
    "Mashed together in fistfuls at a time, she devours the calorie laden treats."
    "Even with the other women you have seen stuff their faces, this was an intensity you have never witnessed before."
    "It's almost as if she was completely out of control."
    image rebecca_stage_3_event_20 = "/rebecca/events/stage3/20.webp"
    scene rebecca_stage_3_event_20
    rebecca "I can't stop, I need more!"
    "Grabbing another box, it seems she can't get enough of them."
    image rebecca_stage_3_event_21 = "/rebecca/events/stage3/21.webp"
    scene rebecca_stage_3_event_21
    "In less than a minute she has emptied the boxes, thousands of calories sitting inside her stuffed belly."
    image rebecca_stage_3_event_22 = "/rebecca/events/stage3/22.webp"
    scene rebecca_stage_3_event_22
    rebecca "What have you done to me?"
    rebecca "I used to be a respectable scientist, but now look at me."
    image rebecca_stage_3_event_23 = "/rebecca/events/stage3/23.webp"
    scene rebecca_stage_3_event_23
    rebecca "I couldn't even concentrate on my work earlier because all I could think about was getting more!"
    "If it was anyone else you might have felt bad, but this woman did literally kidnap you and almost ruin Bonnie's shop."
    ###Hanna approaches the table ###
    image rebecca_stage_3_event_24 = "/rebecca/events/stage3/24.webp"
    scene rebecca_stage_3_event_24
    "Coughing politely, the server gets your attention."
    waitress "I'm sorry, but I am going to need to ask you both to leave."
    waitress "We don't allow outside food to be eaten on the premises."
    image rebecca_stage_3_event_25 = "/rebecca/events/stage3/25.webp"
    scene rebecca_stage_3_event_25
    waitress "And…your…eating noises, have upset some of the other customers."
    "Only now do the pair of you realise that everyone in the store is staring at you."
    "The room witnessing Rebecca's complete loss of control."
    rebecca "I'm sorry, I…"
    image rebecca_stage_3_event_26 = "/rebecca/events/stage3/26.webp"
    scene rebecca_stage_3_event_26
    "With chocolate still smearing her mouth, Rebecca gets up quickly and leaves."
    scene city_night
    "Leaving the server a large tip as an apology, you make your way home."
    "Did you go too far this time?"
    if recollection == False:
        $ rebecca.weight += 3
        $ daytime += 1
    $ rebeccastage3event = 0
    return


label RebeccaStage3Phone:
    ###Next day or the next time you finish working with Bonnie if you chose to go into the cafe###
    ###You get a text from Rebecca###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Rebecca', dialogue=dialogue_one)
    $ msg ("Hello [playername].", who=1)
    pause
    $ msg ("I'm planning another experiment.", who=1)
    pause
    $ msg ("Is there any chance you can send some chocolates to my house?", who=1)
    pause
    $ msg ("Sure thing, although you could just come in and pick them up.")
    pause
    $ msg ("I'm busy.", who=1)
    pause
    $ msg ("We also sell them on the website.")
    pause
    $ msg ("I know.", who=1)
    pause
    $ msg ("But we don't want Bonnie to know do we?", who=1)
    pause
    $ msg ("What's with all the questions, are you going to send them or not?", who=1)
    pause
    $ msg ("Sure thing, I'll send them over later today.")
    pause
    $ msg ("Perfect.", who=1)
    pause
    $ hide_messenger()

    #Not text message#
    "Well, it doesn't seem like your cafe escapade has dented your relationship with Rebecca."
    $ rebeccastage3phone = 0
    return

