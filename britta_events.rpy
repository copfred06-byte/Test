label Britta_Milking:
    image britta_milk_arrive = "/britta/[britta.stage]/milk_arrive.webp"
    scene britta_milk_arrive
    play music "/music/britta.ogg" if_changed
    britta "I’m glad you came, I could use another milking."
    pc "I thought you might."
    if brittastory == 0:
        menu:
            "Ask Britta about herself.":
                "You decide to ask Britta about herself."
                britta "You want to know how I got to be a scientist in this field?"
                britta "I'll try to keep it brief."
                "Britta talks a bit about herself."
                $ brittastory += 1
                #Unlocks more Britta story in the stats page.
                $ renpy.notify("New Britta story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Britta anything."
    britta "Now that you’re becoming quite the milking expert, why don’t you tell me the process of what needs to happen."
    pc "Sure, my sexy scientist, step one is for you to take off all your clothes and get naked."
    britta "Sounds like a good first step."
    image britta_milk_strip1 = "/britta/[britta.stage]/milk_strip1.webp"
    scene britta_milk_strip1
    "She starts taking her clothes off until she is totally naked."
    image britta_milk_strip2 = "/britta/[britta.stage]/milk_strip2.webp"
    scene britta_milk_strip2
    pause
    image britta_milk_strip3 = "/britta/[britta.stage]/milk_strip3.webp"
    scene britta_milk_strip3
    britta "Like this?"
    pc "Perfect, now let’s get your milking outfit on you."
    image britta_milk_strip4 = "/britta/[britta.stage]/milk_strip4.webp"
    scene britta_milk_strip4
    "Britta then puts on her outfit and allows you to look her over."
    image britta_milk_outfit = "/britta/[britta.stage]/milk_outfit.webp"
    scene britta_milk_outfit
    pause
    image britta_milk_beforeboobplay = "/britta/[britta.stage]/milk_beforeboobplay.webp"
    scene britta_milk_beforeboobplay
    britta "I’m assuming that you’re examining my body closely to make sure it’s ready for the process."
    pc "Of course, I need to examine every sexy inch of you."
    image britta_milk_boobplay = "/britta/[britta.stage]/milk_boobplay.webp"
    scene britta_milk_boobplay
    "You then reach out your hands and press her breasts together."
    if britta.stage == 4:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/britta/4/milk_boobplay1_video.webm" loop
        show movie with dissolve
        window hide
        pause
        pc "Especially these."
        britta "How dedicated you are to the study of my breasts."
        stop movie
        image britta_milk_shake = "/britta/[britta.stage]/milk_shake.webp"
        scene britta_milk_shake
        pc "If there were college degrees you could earn for that I’d happily work on a Phd."
        britta "Then let’s give you a practical course for you to follow."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/britta/4/milk_shake_video.webm" loop
        show movie with dissolve
        "She starts moving up and down and side to side, causing her breasts to bounce all over."
        window hide
        pause
        stop movie
    image britta_milk_beforedrink = "/britta/[britta.stage]/milk_beforedrink.webp"
    scene britta_milk_beforedrink
    pc "I think I’m already learning a lot."
    image britta_milk_drink1 = "/britta/[britta.stage]/milk_drink1.webp"
    scene britta_milk_drink1
    britta "I should warn you though, your two objects of study are about to become a lot bigger and heavier, do you think you’re ready for that?"
    pc "Definitely."
    image britta_milk_drink2 = "/britta/[britta.stage]/milk_drink2.webp"
    scene britta_milk_drink2
    "She goes over and drinks the soda-like drink."
    image britta_milk_drink3 = "/britta/[britta.stage]/milk_drink3.webp"
    scene britta_milk_drink3 with vpunch
    "Before then being unable to resist letting out a very loud burp."
    image britta_milk_bestart = "/britta/[britta.stage]/milk_bestart.webp"
    scene britta_milk_bestart
    if britta.stage == 4:
        "All the two of you need to do now is wait."
        "A minute later though, Britta’s breasts start to grow and grow until finally stopping."
        $ renpy.movie_cutscene("/images/britta/4/milk_be_video.webm", stop_music=False)
    image britta_milk_beend = "/britta/[britta.stage]/milk_beend.webp"
    scene britta_milk_beend
    pc "I don’t think I’ll ever get tired of seeing yours or Natalie’s boobs grow like that so quickly."
    image britta_milk_milkstart = "/britta/[britta.stage]/milk_milkstart.webp"
    scene britta_milk_milkstart
    britta "It’s certainly quite an interesting experience, now then care to help me with my sex before the milking experiment?"
    pc "Anything I can do to help with your experiments of course."
    image britta_milk_behind = "/britta/[britta.stage]/milk_behind.webp"
    scene britta_milk_behind
    if persistent.nosexscene:
        scene black with dissolve
        "Britta and you had a good time."
    else:
        "She bends down, ready for you to enter her."
        image britta_milk_sexstart = "/britta/[britta.stage]/milk_sexstart.webp"
        scene britta_milk_sexstart
        "You do so and she happily takes it all as you continue to thrust into her."
        if britta.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/britta/4/milk_sex_video1.webm" loop
            show movie with dissolve
            window hide
            pause
            britta "Ooh, thanks for properly getting me ready to be milked."
            pc "You’re welcome."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/britta/4/milk_sex_video2.webm" loop
            show movie with dissolve
        window hide
        pause
        "The pressure begins to build and you release into her."
        stop movie
    image britta_milk_nipple = "/britta/[britta.stage]/milk_nipple.webp"
    scene britta_milk_nipple
    "After resting for a moment, you then help her get the milking device on her and turn it on."
    britta "Let’s see how well our little sex experiment worked this time."
    image britta_milk_milking = "/britta/[britta.stage]/milk_milking.webp"
    scene britta_milk_milking
    "You place the industrial strength milk pumps over her nipples and then turn the machine on."
    if britta.stage == 4:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/britta/4/milk_milking1_video.webm" loop
        show movie with dissolve
        "The machine starts chugging away and pulling on Britta’s nipples as the milk is extracted from her, her breasts bouncing and jiggling furiously as it does so."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/britta/4/milk_milking2_video.webm" loop
        show movie with dissolve
        window hide
        pause
        "You however just stand back and watch the erotic milking display, Britta’s now massive breasts getting quite the workout."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/britta/4/milk_milking3_video.webm" loop
        show movie with dissolve
    window hide
    pause
    stop movie
    image britta_milk_end = "/britta/[britta.stage]/milk_end.webp"
    scene britta_milk_end
    if britta.stage == 4:
        "Finally after it seems the machine has gotten every drop, you stop it and Britta detaches one of the milk bottles she’s produced and proudly holds it up."
        britta "Wow, very impressive amount, thank you for your help!"
        pc "Sure, happy to help."
        $ money += 30
        "You earned $30 by selling the milk."
    $ brittamilkcheck = 0
    stop music fadeout 1.0
    return



label Britta_Stage_4_Event:

    "You get a text from Britta."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Britta', dialogue=dialogue_one)
    $ msg ("Hey, [playername].", who=1)
    pause
    $ msg ("Would you want to come to the hospital?", who=1)
    menu:
        "Go to the hospital to meet Britta.":
            $ msg ("Yeah, sure. I'll be there in a few minutes.")
            pause
            $ msg ("See you soon.", who=1)
            pause
            $ hide_messenger()
        "Do something else.":
            $ msg ("Maybe another time, I'm quite busy today.")
            pause
            $ msg ("No worries, talk to you later.", who=1)
            pause
            $ hide_messenger()
            return

    image britta_stage4_1 = "/britta/events/stage4/1.webp"
    scene britta_stage4_1
    play music "/music/britta.ogg" if_changed
    "You find Britta standing at the receptionist desk that Natalie is usually working at."
    britta "Hi, I’m Brittalie, just another cute, busty, lactating, and growing receptionist for you to flirt with."
    pc "That is admittedly my favorite kind of receptionist."
    britta "I had a theory that might be the case. Natalie got off work hours ago by the way."
    pc "Not a problem. I’m sure I’ll see her some other time."
    britta "Anyway as far as why I asked you to come here."
    britta "I’m now producing enough milk that like Natalie I also now need to have most of my milk supply produced all at once instead of constantly leaking milk."
    britta "Unfortunately, having to milk myself so often is starting to affect my ability to do my work."
    pc "We certainly can’t have that with how important your work is."
    britta "Agreed. I actually find lactation to be quite interesting, especially my own, but I really don’t want it to affect my work given what we can possibly achieve with it."
    britta "Anyway simply doing the same thing that we did with Natalie should solve those issues."
    britta "I would like the same help that you’ve been giving to her whenever I need it and also whenever you are available."
    pc "Of course, whatever I can do to help."
    britta "Thank you. I will admit I’m also eager to experience it for myself due to it being ‘a pleasurable and enjoyable experience’ as Natalie keeps describing it."
    pc "Natalie really seems to like it and I really like helping her. I’m sure I will with you as well."
    image britta_stage4_2 = "/britta/events/stage4/2.webp"
    scene britta_stage4_2
    britta "Very good then, if you want to follow me."
    "You follow her through the hospital and Britta talks with you as the two of you walk."
    image britta_stage4_3 = "/britta/events/stage4/3.webp"
    scene britta_stage4_3
    britta "Doing this I think will also be good for me to experience first hand and document the milking process and hopefully help figure out just why lactation is happening to me and Natalie as a side effect."
    pc "Do you have any theories?"
    image britta_stage4_4 = "/britta/events/stage4/4.webp"
    scene britta_stage4_4
    britta "Still too many for even me to count unfortunately, but I’m trying to narrow it down. I’m currently concentrating on the fact that so far it’s only occurred with me and Natalie, which causes me to wonder why we are different."
    britta "Was it that our dose we took was somehow slightly different from the others? Is there something biologically or genetically different with us that caused it? Was it simply a random chance?"
    pc "That seems like a lot to figure out."
    image britta_stage4_5 = "/britta/events/stage4/5.webp"
    scene britta_stage4_5
    britta "For sure but I’ll figure it out, keep in mind that this happens in most drug trials with there being unforeseen potential side effects at first."
    britta "Usually it requires some tweaking to the drug to make sure it is safe for the general public."
    britta "Lactation isn’t dangerous but it would be considered an unwelcome side effect for a lot of women taking it so we would want to at least drastically decrease the chances of it happening."
    image britta_milk_arrive_event4 = "/britta/4/milk_arrive.webp"
    scene britta_milk_arrive_event4
    "By this point you and Britta arrive in the room that Britta had already set up to milk Natalie."
    britta "Here we are."
    britta "Shall we begin?"
    pc "Sure."
    image britta_milk_strip1_event4 = "/britta/4/milk_strip1.webp"
    scene britta_milk_strip1_event4
    "Britta pulls open the front of her outfit, revealing her now huge, naked breasts."
    pc "No bra?"
    britta "I already soaked through both of the bras that I had with me, like I said I really need this done now to avoid constantly leaking milk."
    pc "Well let’s get you milked so you don’t have that problem as badly anymore."
    britta "I know Natalie likes to wear a cow costume for you, but I decided I wanted to wear something a little different."
    image britta_milk_strip2_event4 = "/britta/4/milk_strip2.webp"
    scene britta_milk_strip2_event4
    "Britta pulls off the rest of her clothes and then puts on an outfit that leaves…a lot still exposed."
    image britta_milk_strip3_event4 = "/britta/4/milk_strip3.webp"
    scene britta_milk_strip3_event4
    "You certainly aren’t complaining, especially when they are mostly the parts you would want the most access to."
    image britta_milk_strip4_event4 = "/britta/4/milk_strip4.webp"
    scene britta_milk_strip4_event4
    britta "What do you think?"
    pc "Very sexy."
    image britta_milk_outfit_event4 = "/britta/4/milk_outfit.webp"
    scene britta_milk_outfit_event4
    britta "I’m glad you like it, it’s something Luna suggested I wear for you."
    pc "I’m a fan, besides with the black outfit and your white hair you still have the black and white thing like a cow going."
    image britta_stage4_12 = "/britta/events/stage4/12.webp"
    scene britta_stage4_12
    britta "True, I hadn’t thought of that, now then, care to inspect my breasts before we get started?"
    pc "Of course."
    image britta_stage4_13 = "/britta/events/stage4/13.webp"
    scene britta_stage4_13
    "You reach out your hands and squeeze them, only for a gush of milk to come out and nearly hit you in the face."
    image britta_stage4_14 = "/britta/events/stage4/14.webp"
    scene britta_stage4_14
    britta "Sorry! I probably should have calculated that they would do that on account of how much milk there is already in them."
    pc "It’s fine, I should have been the one to be more careful."
    image britta_stage4_15 = "/britta/events/stage4/15.webp"
    scene britta_stage4_15
    "Britta then sits down."
    britta "Looks like you get to play scientist on me."
    image britta_stage4_16 = "/britta/events/stage4/16.webp"
    scene britta_stage4_16
    pc "I’m certainly happy to do lots of experiments on you, that’s for sure."
    britta "Mmm, what experiments did you have in mind? Perhaps ones that involve examinations of my body and then using a certain tool of yours to probe and penetrate into me?"
    image britta_stage4_17 = "/britta/events/stage4/17.webp"
    scene britta_stage4_17
    if persistent.needles:
        "You apply the compound to Britta's breasts."
    else:
        pc "I think that can be arranged, but first we should probably get the not fun part out of the way."
        britta "Agreed, it’s already ready for you, you just need to administer it."
        image britta_stage4_18 = "/britta/events/stage4/18.webp"
        scene britta_stage4_18
        "You administer it to her with Britta bravely taking it before you move on."
        pc "Alright all done."
    image britta_stage4_19 = "/britta/events/stage4/19.webp"
    scene britta_stage4_19
    britta "Good job, also based on what happened with Natalie it shouldn’t take long. In fact I think I can already start to feel the effects. My breasts feel tighter somehow and my nipples tingle a little."
    image britta_stage4_20 = "/britta/events/stage4/20.webp"
    scene britta_stage4_20
    "She grasps at her breasts."
    image britta_milk_beforeboobplay_event4 = "/britta/4/milk_beforeboobplay.webp"
    scene britta_milk_beforeboobplay_event4
    britta "Perhaps you’d like to examine them as well?"
    pc "As a scientist I probably should, you are quite right."
    image britta_milk_boobplay_event4 = "/britta/4/milk_boobplay.webp"
    scene britta_milk_boobplay_event4
    "You grasp at and push her breasts together, being careful not to squeeze or touch them too hard in case they still end up gushing more milk out."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/britta/4/milk_boobplay1_video.webm" loop
    show movie with dissolve
    window hide
    pause
    stop movie
    image britta_milk_shake_event4 = "/britta/4/milk_shake.webp"
    scene britta_milk_shake_event4
    britta "You can be more forceful, we need to know if it’s working and I’m not going to just gush milk everywhere."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/britta/4/milk_shake_video.webm" loop
    show movie with dissolve
    "Britta decides to really test them out as she moves up and down and then side to side, causing her breasts to bounce and jiggle all over the place."
    window hide
    pause
    stop movie
    image britta_milk_beforedrink_event4 = "/britta/4/milk_beforedrink.webp"
    scene britta_milk_beforedrink_event4
    britta "Excellent, no milk coming out so it seems to be working adequately."
    pc "That’s great."
    image britta_milk_drink1_event4 = "/britta/4/milk_drink1.webp"
    scene britta_milk_drink1_event4
    britta "Hopefully no more milk related interruptions at work from now on. Right now though my breasts still do feel incredibly full so let’s get all this milk built up out of me."
    image britta_milk_drink2_event4 = "/britta/4/milk_drink2.webp"
    scene britta_milk_drink2_event4
    "She goes over and drinks the soda like drink and isn’t able to stifle a belch."
    image britta_milk_drink3_event4 = "/britta/4/milk_drink3.webp"
    scene britta_milk_drink3_event4 with vpunch
    britta "Sorry."
    pc "You’re fine, it’s all part of the scientific process."
    image britta_milk_bestart_event4 = "/britta/4/milk_bestart.webp"
    scene britta_milk_bestart_event4
    britta "You’re probably just eager to see what you know comes next."
    pc "I am."
    britta "Me too."
    "Neither of you fortunately have to wait long."
    britta "Ooh, I can already feel it coming, how big are they going to grow I wonder…ooh."
    "She stops as her breasts start to suddenly grow and expand…bigger…and bigger…until they finally stop."
    $ renpy.movie_cutscene("/images/britta/4/milk_be_video.webm", stop_music=False)
    image britta_milk_beend_event4 = "/britta/4/milk_beend.webp"
    scene britta_milk_beend_event4
    "They seem to be about twice the size they were originally."
    britta "Very nice, the size increase seems to be right along with my calculations. They also feel more full of milk than ever, but I’d like to conduct an experiment first."
    image britta_milk_milkstart_event4 = "/britta/4/milk_milkstart.webp"
    scene britta_milk_milkstart_event4
    britta "I want to see if sex first will cause me to have an increased milk production."
    pc "I’m certainly willing to test that theory out in the name of scientific research."
    britta "I’m glad you are so committed to science because I think we may need you to have sex with me each time before you milk me."
    pc "If that’s what the experiment requires."
    britta "Good thing both of us are so dedicated to science aren’t we?"
    pc "Yeah, I love doing science."
    image britta_milk_behind_event4 = "/britta/4/milk_behind.webp"
    scene britta_milk_behind_event4
    "Britta then bends down and places her hands onto a bar to keep herself from falling over with the increased weight of her breasts dangling down and you about to push against her."
    if persistent.nosexscene:
        scene black with dissolve
        "Britta and you had a good time."
    else:
        image britta_stage4_35 = "/britta/events/stage4/35.webp"
        scene britta_stage4_35
        britta "Penetrate me."
        image britta_milk_sexstart_event4 = "/britta/4/milk_sexstart.webp"
        scene britta_milk_sexstart_event4
        "You are more than happy to oblige as you take her from behind and enter her."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/britta/4/milk_sex_video1.webm" loop
        show movie with dissolve
        "As you thrust into her, her butt and greatly enlarged milk-filled breasts bounce and jiggle with each thrust."
        "Britta can’t help but moan as she enjoys the pleasure you are giving her."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/britta/4/milk_sex_video2.webm" loop
        show movie with dissolve
        window hide
        pause
        britta "Ooh, I want to milk you of your sperm before you milk me. Ejaculate it inside me."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/britta/4/milk_sex_video3.webm" loop
        show movie with dissolve
        pc "I'm getting it ready for you, ready to deposit it into your beautiful pussy."
        "At that the pressure begins to build and you release inside of her."
        window hide
        pause
        stop movie
    image britta_milk_nipple_event4 = "/britta/4/milk_nipple.webp"
    scene britta_milk_nipple_event4
    "The two of you recover for just a moment."
    britta "Mmm, now that I’ve milked you, it’s time to milk me, I think my little experiment worked too, I feel somehow even more full of milk."
    image britta_milk_milking_event4 = "/britta/4/milk_milking.webp"
    scene britta_milk_milking_event4
    "You place the industrial strength milk pumps over her nipples and then turn the machine on."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/britta/4/milk_milking1_video.webm" loop
    show movie with dissolve
    "The machine starts chugging away and pulling on Britta’s nipples as the milk is extracted from her, her breasts bouncing and jiggling furiously as it does so."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/britta/4/milk_milking2_video.webm" loop
    show movie with dissolve
    britta "Ooh, yeah, Natalie wasn’t kidding, this does feel good, not as good as sex with you but I have yet to find anything that can compare with that."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/britta/4/milk_milking3_video.webm" loop
    show movie with dissolve
    "You however just stand back and watch the erotic milking display, Britta’s now massive breasts getting quite the workout."
    window hide
    pause
    stop movie
    image britta_milk_end_event4 = "/britta/4/milk_end.webp"
    scene britta_milk_end_event4
    "Finally after it seems the machine has gotten every drop, you stop it and Britta detaches one of the milk bottles she’s produced and proudly holds it up."
    britta "Wow, very impressive amount, thank you for your help!"
    pc "Sure, happy to help."

    $ brittastage4event = 0
    if recollection == False:
        $ money += 30
        "You earned $30 by selling the milk."
        $ daytime += 1
        $ phonecall = 1
        $ brittamilkcheck = 0
    stop music fadeout 1.0
    return
