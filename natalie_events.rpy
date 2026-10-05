label Natalie_Milking:
    image natalie_milk_arrive = "/natalie/[natalie.stage]/milk_arrive.webp"
    scene natalie_milk_arrive
    play music "/music/natalie.ogg" if_changed
    "After finding someone to cover for her, you go with Natalie over into the milking room as you have now dubbed it."
    if nataliestory == 0:
        menu:
            "Ask Natalie about herself.":
                "You decide to ask Natalie about herself."
                natalie "I would love to tell you about myself."
                "Natalie talks a bit about herself."
                natalie "Now, I think you should tell me some more about yourself the next time we go on a date."
                $ nataliestory += 1
                #Unlocks more Natalie story in the stats page.
                $ renpy.notify("New Natalie story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Natalie anything."
    image natalie_milk_strip1 = "/natalie/[natalie.stage]/milk_strip1.webp"
    scene natalie_milk_strip1
    "Natalie strips naked, looking back at you through most of it so she can enjoy your reaction at admiring her body."
    image natalie_milk_strip2 = "/natalie/[natalie.stage]/milk_strip2.webp"
    scene natalie_milk_strip2
    window hide
    pause
    image natalie_milk_outfit = "/natalie/[natalie.stage]/milk_outfit.webp"
    scene natalie_milk_outfit
    "She then puts on her cow outfit."
    if natalie.stage == 4:
        "Natalie sure seems to enjoy wearing a cow costume for you when she does this."
    elif natalie.stage == 3:
        "Is it necessary to wear it? No, but it sure seems like Natalie enjoys wearing it for you."
    image natalie_milk_beforeboobplay = "/natalie/[natalie.stage]/milk_beforeboobplay.webp"
    scene natalie_milk_beforeboobplay
    if natalie.stage == 4:
        pc "Is my growing cow ready to produce even more delicious milk than last time?"
        natalie "Moo! I’m even bigger and even more full of milk. Why not inspect my breasts and see how much milk you think is in them this time?"
    elif natalie.stage == 3:
        pc "Is my growing cow ready to produce lots of delicious milk?"
        natalie "Moo! Why not inspect my breasts and see how much milk you think is in them?"
    image natalie_milk_boobplay = "/natalie/[natalie.stage]/milk_boobplay.webp"
    scene natalie_milk_boobplay
    window hide
    pause
    if natalie.stage == 4:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/natalie/4/milk_boobplay1_video.webm" loop
        show movie with dissolve
        "You go over and feel up Natalie’s now quite large breasts, feeling the milk sloshing around inside them, with her enjoying the attention you are giving them."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/natalie/4/milk_boobplay2_video.webm" loop
        show movie with dissolve
    elif natalie.stage == 3:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/natalie/3/milk_boobplay1_video.webm" loop
        show movie with dissolve
        "You go over and feel up Natalie’s now quite large breasts, feeling the milk sloshing around inside them, with her enjoying the attention you are giving them."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/natalie/3/milk_boobplay2_video.webm" loop
        show movie with dissolve

    window hide
    pause
    stop movie
    image natalie_milk_beforedrink = "/natalie/[natalie.stage]/milk_beforedrink.webp"
    scene natalie_milk_beforedrink
    "Natalie then goes and gets the special soda-like drink."
    image natalie_milk_drink1 = "/natalie/[natalie.stage]/milk_drink1.webp"
    scene natalie_milk_drink1
    window hide
    pause
    image natalie_milk_drink2 = "/natalie/[natalie.stage]/milk_drink2.webp"
    scene natalie_milk_drink2
    "She then drinks the whole drink in one go."
    image natalie_milk_drink3 = "/natalie/[natalie.stage]/milk_drink3.webp"
    scene natalie_milk_drink3 with vpunch
    natalie "BUUURRRP!"
    image natalie_milk_bestart = "/natalie/[natalie.stage]/milk_bestart.webp"
    scene natalie_milk_bestart
    if natalie.stage == 4:
        natalie "Sorry I can’t help but burp. Now here comes the fun part though."
        $ renpy.movie_cutscene("/images/natalie/4/milk_be_video.webm", stop_music=False)
    elif natalie.stage == 3:
        "Natalie seems to pause for a moment as it starts to take effect."
        $ renpy.movie_cutscene("/images/natalie/3/milk_be_video.webm", stop_music=False)
    image natalie_milk_beend = "/natalie/[natalie.stage]/milk_beend.webp"
    scene natalie_milk_beend
    "Her breasts grew and grew until they reached their largest size yet."
    image natalie_milk_milkstart = "/natalie/[natalie.stage]/milk_milkstart.webp"
    scene natalie_milk_milkstart
    natalie "I think I’m going to be able to produce a lot of milk this week."
    pc "I think so too."
    image natalie_milk_behind = "/natalie/[natalie.stage]/milk_behind.webp"
    scene natalie_milk_behind
    window hide
    pause
    image natalie_milk_nipple = "/natalie/[natalie.stage]/milk_nipple.webp"
    scene natalie_milk_nipple
    "She then goes over and bends down while you hook up the pumps to her nipples."
    image natalie_milk_milking = "/natalie/[natalie.stage]/milk_milking.webp"
    scene natalie_milk_milking
    pc "Are you ready?"
    natalie "Ready."
    if natalie.stage == 4:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/natalie/4/milk_milking1_video.webm" loop
        show movie with dissolve
        "You then start the pump going as her nipples are sucked on and have the milk squeezed out."
        "She lets out a moan as she begins to be milked."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/natalie/4/milk_milking2_video.webm" loop
        show movie with dissolve
        natalie "Ooh that feels so good! Having my nipples sucked and having you right next to me to watch me!"
        pc "You’re doing great Natalie, you’re already producing plenty!"
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/natalie/4/milk_milking3_video.webm" loop
        show movie with dissolve
        natalie "Just being your good, giant breasted, fat cow!"
    elif natalie.stage == 3:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/natalie/3/milk_milking1_video.webm" loop
        show movie with dissolve
        "You then start the pump going as her nipples are sucked on and have the milk squeezed out."
        "She lets out a moan as she begins to be milked."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/natalie/3/milk_milking2_video.webm" loop
        show movie with dissolve
        natalie "Ooh that feels so good! Having my nipples sucked and having you right next to me to watch me!"
        pc "You’re doing great Natalie, you’re already producing plenty!"
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/natalie/3/milk_milking3_video.webm" loop
        show movie with dissolve
        natalie "Just being your good cow!"
    window hide
    pause
    stop movie
    image natalie_milk_end = "/natalie/[natalie.stage]/milk_end.webp"
    scene natalie_milk_end
    if natalie.stage == 4:
        "Finally she stops producing milk and you shut off the pumps and Natalie picks up just one of the multiple large bottles of milk she produced."
        pc "Good work, looks like that’s at least several more free very large meals worth at Bunny Bites for you for this!"
        natalie "Perfect, I love this! I get to come see you at work and I get to eat really well while doing it."
        pc "While I get some money out of it too, even more customers are going to be very happy eating your milk ice cream."
        $ money += 30
        "You earned $30 by selling the milk."
    elif natalie.stage == 3:
        "Finally she stops producing milk and you shut off the pumps and Natalie picks up just one of the several large bottles of milk she produced."
        pc "Good work, looks like that’s at least a couple free very large meals worth at Bunny Bites for you for this!"
        natalie "Perfect, I get to come see you at work and I get to eat really well while doing it."
        pc "While I get some money out of it too and a lot of customers are going to be very happy eating your milk ice cream, we’re already off to a great start."
        $ money += 20
        "You earned $20 by selling the milk."
    stop music fadeout 1.0
    $ nataliemilkcheck = 0
    return


label Natalie_Stage_3_Event:
    "You get a text from Britta."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Britta', dialogue=dialogue_one)
    $ msg ("Hey, [playername]. This is Britta.", who=1)
    pause
    $ msg ("Would you want to come to the hospital? I have something exciting to show you.", who=1)
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


    image natalie_stage3_1 = "/natalie/events/stage3/1.webp"
    scene natalie_stage3_1
    play music "/music/britta.ogg" if_changed
    "Arriving in the hospital, you see Britta sitting in Natalie's usual spot."
    pc "Hey Britta, what is it you want to show me?"
    image natalie_stage3_2 = "/natalie/events/stage3/2.webp"
    scene natalie_stage3_2
    britta "Hey, you are probably wondering where Natalie is?"
    pc "Let me guess, she had to pump milk again?"
    britta "You are close. Come with me, I'll show you."
    "Britta leaves the receptionist counter and moves towards the elevator."
    image natalie_stage3_3 = "/natalie/events/stage3/3.webp"
    scene natalie_stage3_3
    britta "So you have probably witnessed how Natalie can't go about her day normally anymore."
    britta "Currently, she has to pump milk from her breasts every few hours."
    image natalie_stage3_4 = "/natalie/events/stage3/4.webp"
    scene natalie_stage3_4
    "Britta pushed the button for the elevator."
    britta "And I have started to lactate more and more too."
    britta "My situation is still nowhere near what Natalie is experiencing though."
    image natalie_stage3_5 = "/natalie/events/stage3/5.webp"
    scene natalie_stage3_5
    "Both of you step in the elevator."
    britta "But according to my calculations, it would be a matter of time before I experience lactation to the same degree."
    britta "And that is not all."
    britta "Natalie's milk production will keep rising as time goes by."
    image natalie_stage3_6 = "/natalie/events/stage3/6.webp"
    scene natalie_stage3_6
    britta "My data projects a near 300 percent increase in milk production is likely if all other variables stay the same."
    britta "This is a problem regarding productivity and general enjoyment of our time."
    britta "Having to spend hours pumping milk every day is not efficient."
    image natalie_stage3_7 = "/natalie/events/stage3/7.webp"
    scene natalie_stage3_7
    britta "And we aren't even talking about the sensitivity and itchiness of our breasts."
    britta "The slightest touch has an enormous effect, making her tits almost explode with milk."
    image natalie_stage3_8 = "/natalie/events/stage3/8.webp"
    scene natalie_stage3_8
    britta "I have taken it upon myself to find a solution for this problem."
    britta "And I wouldn't call you here if I didn't find one."
    image natalie_stage3_9 = "/natalie/events/stage3/9.webp"
    scene natalie_stage3_9
    play music "/music/natalie.ogg" if_changed
    "Britta opens the door to a room with all kinds of medical equipment, and Natalie is standing there wearing some kind of skimpy cow outfit."
    britta "So I asked Natalie if she wanted to test the solution."
    image natalie_stage3_10 = "/natalie/events/stage3/10.webp"
    scene natalie_stage3_10
    natalie "Hey, [playername]. I'm so glad to see you. I hope you like my outfit."
    pc "Hey, Natalie. You look absolutely stunning, as always."
    britta "Are you ready, Natalie?"
    natalie "I am."
    image natalie_stage3_11 = "/natalie/events/stage3/11.webp"
    scene natalie_stage3_11
    britta "So the solution I created has two elements to it."
    britta "First, I made a solution that reduces the sensitivity of the breasts and keeps the milk inside the breasts from shooting out with the slightest squeeze."
    image natalie_stage3_12 = "/natalie/events/stage3/12.webp"
    scene natalie_stage3_12
    "Britta then gives Natalie's breasts a slight squeeze, resulting in an almost orgasmic reaction for Natalie with her breasts just shooting out milk as if they were pressurized."
    natalie "OOOAAAH!"
    britta "As you can see, they have gotten much more sensitive since you last came here, so we needed to sort this out."
    image natalie_stage3_13 = "/natalie/events/stage3/13.webp"
    scene natalie_stage3_13
    britta "I'm sorry, Natalie, I didn't realize how bad it has gotten for you."
    natalie "Don't worry, it feels really good. It's just not practical to have this happen during the day in public."
    britta "If we had waited another month, even just friction of clothes would have this same effect on her breasts."
    image natalie_stage3_14 = "/natalie/events/stage3/14.webp"
    scene natalie_stage3_14
    britta "Now, let's administer the solution."
    britta "Natalie, please sit down in the chair."
    image natalie_stage3_15 = "/natalie/events/stage3/15.webp"
    scene natalie_stage3_15
    britta "I have tested the solution, and it is completely harmless. It uses chemicals already found in the body naturally."
    britta "These chemicals will change how your breasts store milk, the signals that normally open the flood gates will be numbed, and you will be more likely to keep the milk from escaping."
    if persistent.needles:
        "Britta applies the compound to Natalie's breasts."
    else:
        image natalie_stage3_16 = "/natalie/events/stage3/16.webp"
        scene natalie_stage3_16
        britta "Now, this might sting a little, so please relax."
        image natalie_stage3_17 = "/natalie/events/stage3/17.webp"
        scene natalie_stage3_17
        "As Britta injects the solution into Natalie's breasts, you see Natalie recoiling from the sting a bit."
    image natalie_stage3_18 = "/natalie/events/stage3/18.webp"
    scene natalie_stage3_18
    britta "Ok, that is done. Let me check your breasts real quick."
    britta "Looks good. It seems it is already way less sensitive to the touch."
    natalie "Wow, that worked fast. I can touch my breasts without them exploding with milk."
    image natalie_stage3_19 = "/natalie/events/stage3/19.webp"
    scene natalie_stage3_19
    britta "So that was the first part of the solution."
    britta "Natalie will now be able to enjoy her days to the fullest again without worrying about her breasts exploding with milk any moment."
    image natalie_stage3_20 = "/natalie/events/stage3/20.webp"
    scene natalie_stage3_20
    britta "But we aren't done yet."
    britta "These babies will still produce milk, so we need a way to extract that."
    britta "I'll be making the second part of the solution, be right back."
    image natalie_stage3_21 = "/natalie/events/stage3/21.webp"
    scene natalie_stage3_21
    natalie "I'm so happy. I can finally do everything again without worrying about all the milk everywhere."
    natalie "Do you want to play with my breasts to feel the difference?"
    pc "I would love to."
    image natalie_stage3_22 = "/natalie/events/stage3/22.webp"
    scene natalie_stage3_22
    "You start gently touching her breasts and lifting them a little."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/natalie/events/stage3/23.webm" loop
    show movie with dissolve
    "As you lift them, you feel the heavy liquid inside her breasts sloshing around."
    "But as expected, she no longer starts lactating just from touch alone."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/natalie/events/stage3/24.webm" loop
    show movie with dissolve
    "To see how effective the solution is, you squeeze her breasts together."
    "But even then, there is not a single drop of milk escaping her nipples."
    window hide
    pause
    stop movie
    image natalie_stage3_25 = "/natalie/events/stage3/25.webp"
    scene natalie_stage3_25
    pc "Wow, I'm impressed. This solution works really well."
    natalie "Now I can let you play with them all the time!"
    image natalie_stage3_26 = "/natalie/events/stage3/26.webp"
    scene natalie_stage3_26
    britta "Sorry to interrupt, but here is the second part of the solution."
    "Britta holds up a seemingly regular soda, not what you expected."
    image natalie_stage3_27 = "/natalie/events/stage3/27.webp"
    scene natalie_stage3_27
    britta "So, like I said, we still need to extract the milk."
    britta "In this second solution is a reactive agent that reacts with the chemicals in the first solution that puts the milk production system into overdrive."
    image natalie_stage3_28 = "/natalie/events/stage3/28.webp"
    scene natalie_stage3_28
    britta "Essentially making a week's worth of supply in a matter of moments."
    britta "Which would mean that if my calculations are correct, Natalie wouldn't have to milk her breasts for a whole week after we are done here."
    image natalie_stage3_29 = "/natalie/events/stage3/29.webp"
    scene natalie_stage3_29 with vpunch
    natalie "BUUURRRP!"
    image natalie_stage3_30 = "/natalie/events/stage3/30.webp"
    scene natalie_stage3_30
    natalie "I'm sorry, that isn't a very attractive thing to do."
    britta "That was expected. The drink is incredibly fizzy."
    britta "It should start reacting with the first compound in a few short moments."
    image natalie_stage3_31 = "/natalie/events/stage3/31.webp"
    scene natalie_stage3_31
    "Not even a minute later, Natalie starts to feel something in her chest."
    natalie "Wow, this sensation is as if my breasts are filling with milk in real-time."
    $ renpy.movie_cutscene("/images/natalie/events/stage3/32.webm", stop_music=False)
    image natalie_stage3_33 = "/natalie/events/stage3/33.webp"
    scene natalie_stage3_33
    "A few moments later, Natalie's breasts had grown incredibly and looked ready to explode with milk."
    natalie "Oh, this pressure, I can't believe it."
    image natalie_stage3_34 = "/natalie/events/stage3/34.webp"
    scene natalie_stage3_34
    britta "It looks to be working as I expected."
    britta "Now, all we have to do is extract the milk from the breasts."
    image natalie_stage3_35 = "/natalie/events/stage3/35.webp"
    scene natalie_stage3_35
    "Britta places her hands on Natalie's breast, but just the slight touch makes milk come out of her nipples at high pressure."
    natalie "OOOAAH!"
    britta "Like the data suggested, your breasts are at maximum capacity and ready to be milked."
    image natalie_stage3_36 = "/natalie/events/stage3/36.webp"
    scene natalie_stage3_36
    natalie "The pressure. Can we start the milking, please?"
    britta "Yes, I have all the necessary equipment here."
    image natalie_stage3_37 = "/natalie/events/stage3/37.webp"
    scene natalie_stage3_37
    britta "So I ran some simulations and discovered that the optimal position for milking is if you let your breasts hang down and let gravity do some work."
    britta "I installed a pole here that you can grab onto."
    britta "Please take position."
    image natalie_stage3_38 = "/natalie/events/stage3/38.webp"
    scene natalie_stage3_38
    "Natalie takes position to let her breasts hang downwards."
    britta "Now, [playername], If you take these cups and gently place them on Natalie's nipples, they will create an air-tight seal by sucking."
    image natalie_stage3_39 = "/natalie/events/stage3/39.webp"
    scene natalie_stage3_39
    britta "Now go ahead and release the pressure from her breasts."
    natalie "Yes please."
    image natalie_stage3_40 = "/natalie/events/stage3/40.webp"
    scene natalie_stage3_40
    "You move before Natalie and gently put the suction cup milkers on Natalie's nipples."
    image natalie_stage3_41 = "/natalie/events/stage3/41.webp"
    scene natalie_stage3_41
    "To your surprise, they immediately glue onto her nipples and start sucking milk out of her breasts."
    natalie "Oh my god, this feels so good!"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/natalie/events/stage3/42.webm" loop
    show movie with dissolve
    "The milking device looks to be a bit rough on Natalie's breasts, but it looks like she is enjoying the feeling."
    window hide
    pause
    stop movie
    image natalie_stage3_43 = "/natalie/events/stage3/43.webp"
    scene natalie_stage3_43
    "A few moments later, her breasts seemed to have stopped giving milk, and the container below is nearly completely filled."
    image natalie_stage3_44 = "/natalie/events/stage3/44.webp"
    scene natalie_stage3_44
    natalie "Look how much I produced!"
    britta "That should be a week's supply, which means you are free from the troubles you were having for a whole week."
    natalie "Would you bring this to Bunny Bites for me? We can split the profits."
    "Natalie gives you the milk."
    "The three of you talk a bit more before you head home."
    "Weekly milking unlocked."
    stop music fadeout 1.0
    if recollection == False:
        $ money += 20
        "You earned $20 by selling the milk."
        $ nataliestage3event = 0
        $ daytime += 1
        $ phonecall = 1
    return

label Natalie_Stage_4_Event_1:
    #After Luna Stage 11 Natalie Event
    #“Perhaps you should go visit Natalie at the hospital?”
    scene player_room
    "You decide to go visit Natalie and the other test subjects at the hospital."
    scene city
    "Bringing a bunch of tasty treats for them to have."
    "This certainly wouldn’t be the first time you’ve done this."
    "Luna has continued to provide you with a budget to go and get food and treats for all the test subjects."
    image natalie_stage4_1 = "/natalie/events/stage4/1.webp"
    scene natalie_stage4_1
    play music "/music/natalie.ogg" if_changed
    "Upon seeing Natalie sitting at the receptionist desk, you go over to her."
    image natalie_stage4_2 = "/natalie/events/stage4/2.webp"
    scene natalie_stage4_2
    pc "Hi Natalie! I come bearing gifts!"
    image natalie_stage4_3 = "/natalie/events/stage4/3.webp"
    scene natalie_stage4_3
    natalie "Hi! Nice to see you too, especially when you’re bringing gifts."
    natalie "Especially the ones I can eat."
    pc "Yeah, I made sure to get some of each of everyone’s favorites."
    image natalie_stage4_4 = "/natalie/events/stage4/4.webp"
    scene natalie_stage4_4
    pc "I don’t expect it to last very long though the way you girls eat."
    pc "The way that Luna is talking about her investor though I should hopefully be able to start buying and bringing a lot more for all of you."
    natalie "That would be great thanks!"
    image natalie_stage4_5 = "/natalie/events/stage4/5.webp"
    scene natalie_stage4_5
    "Natalie looks through what you brought."
    natalie "It all looks delicious!"
    pc "Not as delicious as you."
    image natalie_stage4_6 = "/natalie/events/stage4/6.webp"
    scene natalie_stage4_6
    natalie "Mmm, thanks."
    natalie "I’ll make sure some of it gets to everyone."
    pc "That would be appreciated. Last time Sally convinced me to let her take it instead."
    pc "Big mistake."
    pc "It doesn’t seem any of it made its way to any of the rest of you."
    image natalie_stage4_7 = "/natalie/events/stage4/7.webp"
    scene natalie_stage4_7
    natalie "Hah hah no, I love Sally but don’t trust her with the treats."
    natalie "I’ll make sure everyone gets some."
    image natalie_stage4_8 = "/natalie/events/stage4/8.webp"
    scene natalie_stage4_8
    natalie "Even Charlene, I know she isn’t really a test subject anymore."
    natalie "However it would still be nice to try and include her."
    pc "Agreed."
    image natalie_stage4_9 = "/natalie/events/stage4/9.webp"
    scene natalie_stage4_9
    natalie "She may not like that I keep giving her more temptation though."
    natalie "She is really struggling not to want to still eat all the time."
    pc "Do you think that is a lingering side effect of the drug?"
    image natalie_stage4_10 = "/natalie/events/stage4/10.webp"
    scene natalie_stage4_10
    natalie "No, probably more like Charlene is a lot more like the rest of us than she likes to admit and loves food."
    image natalie_stage4_11 = "/natalie/events/stage4/11.webp"
    scene natalie_stage4_11
    natalie "Anyway I get off work in 10 minutes, do you maybe want to come watch me eat all of my portion of the food?"
    pc "Sure! I can definitely wait for that."
    image natalie_stage4_12 = "/natalie/events/stage4/12.webp"
    scene natalie_stage4_12
    "Natalie smiles happily and you wait the 10 minutes while you watch Natalie interact with the patients and their family or friends coming in."
    image natalie_stage4_13 = "/natalie/events/stage4/13.webp"
    scene natalie_stage4_13
    "After her shift is over, you follow Natalie over with all the treats to the milking lab as an unoccupied place to watch Natalie eat."
    image natalie_stage4_14 = "/natalie/events/stage4/14.webp"
    scene natalie_stage4_14
    "With Natalie deciding to hold hands with you on the way there."
    image natalie_stage4_15 = "/natalie/events/stage4/15.webp"
    scene natalie_stage4_15
    "As you arrive in the milking lab, Natalie starts taking off some clothes."
    image natalie_stage4_16 = "/natalie/events/stage4/16.webp"
    scene natalie_stage4_16
    window hide
    pause
    image natalie_stage4_17 = "/natalie/events/stage4/17.webp"
    scene natalie_stage4_17
    pause
    image natalie_stage4_18 = "/natalie/events/stage4/18.webp"
    scene natalie_stage4_18
    pause
    image natalie_stage4_19 = "/natalie/events/stage4/19.webp"
    scene natalie_stage4_19
    natalie "So much better."
    natalie "While these new clothes Luna provided us are amazing, It still feels much better without them."
    image natalie_stage4_20 = "/natalie/events/stage4/20.webp"
    scene natalie_stage4_20
    window hide
    pause
    image natalie_stage4_21 = "/natalie/events/stage4/21.webp"
    scene natalie_stage4_21
    "As Natalie sits down, she starts eating the treats."
    image natalie_stage4_22 = "/natalie/events/stage4/22.webp"
    scene natalie_stage4_22
    "She seems to relax and talk to you in between bites."
    image natalie_stage4_23 = "/natalie/events/stage4/23.webp"
    scene natalie_stage4_23
    natalie "I’m supposed to have more nurse training tomorrow and it makes me really nervous."
    natalie "Eating really helps calm me down, but what really helps is having you around."
    pc "Unfortunately I don’t think I could be there when you are doing your nurse training."
    pc "Not unless you want me to come in and pretend to be injured and have you take care of me?"
    image natalie_stage4_24 = "/natalie/events/stage4/24.webp"
    scene natalie_stage4_24
    natalie "Hah hah, no please don’t do that!"
    pc "I could still have you practice on me right now though if it would help?"
    image natalie_stage4_25 = "/natalie/events/stage4/25.webp"
    scene natalie_stage4_25
    natalie "I would love that!"
    natalie "Thank you!"
    pc "Then that’s what we will do once you get done eating."
    image natalie_stage4_26 = "/natalie/events/stage4/26.webp"
    scene natalie_stage4_26
    "Natalie continues to eat while you just watch her."
    image natalie_stage4_27 = "/natalie/events/stage4/27.webp"
    scene natalie_stage4_27
    "Both of you enjoy each other’s company for a while before Natalie reluctantly stops."
    image natalie_stage4_28 = "/natalie/events/stage4/28.webp"
    scene natalie_stage4_28
    natalie "Ok, that’s enough, as much as I would like to eat more I really should save some for everyone else."
    natalie "So as far as nurse training goes, my biggest problem is I just get really nervous and think I’m doing everything wrong…and then it does go wrong."
    pc "Okay, we can work on that. Just pretend I’m a patient and remind yourself that you are here to help take care of me."
    pc "Try to focus on helping others and not what you might end up doing wrong."
    image natalie_stage4_29 = "/natalie/events/stage4/29.webp"
    scene natalie_stage4_29
    natalie "I’ll try. You just do such a good job taking care of me by the way."
    natalie "Such as continuing to bring me lovely treats to eat."
    pc "Yes, but in this case it looks like you get to take care of me now."
    pc "So let’s begin the way you would normally."
    image natalie_stage4_30 = "/natalie/events/stage4/30.webp"
    scene natalie_stage4_30
    "Natalie takes a moment to gather herself, but seems to be not too stressed as it is of course just you."
    natalie "So what seems to be the problem?"
    pc "It’s my stomach."
    pc "It hurts."
    image natalie_stage4_31 = "/natalie/events/stage4/31.webp"
    scene natalie_stage4_31
    natalie "Oh, well let’s take a look at that."
    image natalie_stage4_32 = "/natalie/events/stage4/32.webp"
    scene natalie_stage4_32
    "Natalie looks you over as you sit down on the patient’s chair, with you pretending to come up with symptoms and Natalie pretending to look you over."
    image natalie_stage4_33 = "/natalie/events/stage4/33.webp"
    scene natalie_stage4_33
    "You also can’t help but notice just how close her huge breasts are to you as she bends down to look you over."
    image natalie_stage4_34 = "/natalie/events/stage4/34.webp"
    scene natalie_stage4_34
    "Natalie smiles, aware of the reaction you seem to be having."
    natalie "Are you sure your problem isn’t somewhere lower than your stomach?"
    natalie "Something extra swollen and big?"
    pc "Oh, I would consider that to be no problem at all."
    pc "It’s just a part of me being so obviously happy to have such a great nurse."
    image natalie_stage4_35 = "/natalie/events/stage4/35.webp"
    scene natalie_stage4_35
    natalie "I don’t know about a great nurse, but a big and getting bigger nurse at least."
    pc "You’re doing great!"
    image natalie_stage4_36 = "/natalie/events/stage4/36.webp"
    scene natalie_stage4_36
    natalie "Thanks! It’s easy of course having it just be you but maybe I can just try and think of you to help calm me down when taking care of a real patient."
    pc "Whatever helps you, you’ve got this Natalie!"
    image natalie_stage4_37 = "/natalie/events/stage4/37.webp"
    scene natalie_stage4_37
    natalie "Yeah, maybe I do!"
    natalie "Thanks again so much for your help."
    natalie "Thank you for everything…you’ve really helped me in so many ways and I’ve learned so much about myself."
    pc "You’re welcome."
    image natalie_stage4_38 = "/natalie/events/stage4/38.webp"
    scene natalie_stage4_38
    "Natalie however seems to think for a long moment before answering."
    natalie "Next time though…I really want to start thanking you and helping take care of you for real."
    pc "What do you mean by that?"
    image natalie_stage4_39 = "/natalie/events/stage4/39.webp"
    scene natalie_stage4_39
    natalie "Honestly I don’t know either yet."
    natalie "There are some things I really need to tell you and I…"
    image natalie_stage4_40 = "/natalie/events/stage4/40.webp"
    scene natalie_stage4_40
    "She stops, unwilling to say anymore, but whatever it is makes her very nervous."
    "You decide not to push her on it further, which Natalie seems to appreciate."
    image natalie_stage4_41 = "/natalie/events/stage4/41.webp"
    scene natalie_stage4_41
    natalie "I’ll talk to you all about it later."
    pc "Sure, whenever you are ready."
    image natalie_stage4_42 = "/natalie/events/stage4/42.webp"
    scene natalie_stage4_42
    "Natalie puts her clothes back on before you say goodbye and take your leave."
    image natalie_stage4_43 = "/natalie/events/stage4/43.webp"
    scene natalie_stage4_43
    window hide
    pause
    image natalie_stage4_44 = "/natalie/events/stage4/44.webp"
    scene natalie_stage4_44
    pause
    stop music fadeout 1.0
    $ nataliestage4event = 0
    return

label Natalie_Stage_4_Event_2:
    "You get a phone call."
    "It’s Natalie!"
    pc "Hey Natalie!"
    image natalie_stage4_45 = "/natalie/events/stage4/45.webp"
    scene natalie_stage4_45
    natalie "Hi I was wondering if maybe…you would like to come over to my apartment?"
    natalie "Like for a date."
    image natalie_stage4_46 = "/natalie/events/stage4/46.webp"
    scene natalie_stage4_46
    natalie "There are also some things I want to tell you and…some things I want to do with you."
    natalie "Only if you want to, that is."
    "You aren’t sure just what she is talking about, but she seems nervous."
    "Whatever it is you are apparently about to find out."
    pc "Of course! I would love to."
    image natalie_stage4_47 = "/natalie/events/stage4/47.webp"
    scene natalie_stage4_47
    natalie "Really? I’ll send you the address then."
    pc "See you soon."

    scene player_room
    "You hang up and you soon receive a text from Natalie telling you her address."
    "You’ve never been to her apartment before so it’s a little surprising."
    scene city
    "You however manage to find her apartment building and then her apartment and knock on the door."

    image natalie_stage4_48 = "/natalie/events/stage4/48.webp"
    scene natalie_stage4_48
    "Natalie answers it immediately as if she has been standing at the door waiting for you to arrive."
    natalie "Hi um…you’re here."
    pc "Yes I’m here."
    "She again seems very nervous."
    image natalie_stage4_49 = "/natalie/events/stage4/49.webp"
    scene natalie_stage4_49
    natalie "Uh sorry…please come in."
    "You do so and look around a little."
    image natalie_stage4_50 = "/natalie/events/stage4/50.webp"
    scene natalie_stage4_50
    "Her apartment is actually quite small but still at least well maintained."
    "You also notice the huge feast of a lot of different foods laying out on the table, already ready."
    natalie "I made food for us."
    natalie "I wasn’t sure what you might like so I made a bunch of different things and I figured I could just eat the rest of whatever you didn’t want myself."
    natalie "While you watch as I know how much you like that."
    pc "It all looks great."
    image natalie_stage4_51 = "/natalie/events/stage4/51.webp"
    scene natalie_stage4_51
    natalie "Thanks I’m not a great cook but I tried my best."
    pc "Like I said, I’m sure it will all be great."
    natalie "Okay, well we can eat now."
    image natalie_stage4_52 = "/natalie/events/stage4/52.webp"
    scene natalie_stage4_52
    "Despite how nervous Natalie is as soon as she starts eating and really giving in, she relaxes enjoying eating all the food as well as enjoying having you watch her eat."
    image natalie_stage4_53 = "/natalie/events/stage4/53.webp"
    scene natalie_stage4_53
    "You actually end up eating plenty yourself, despite Natalie’s claims that she isn’t a great cook, the food is actually very good."
    pc "Wow, this really is all delicious Natalie."
    image natalie_stage4_54 = "/natalie/events/stage4/54.webp"
    scene natalie_stage4_54
    natalie "You really like it?"
    pc "Yeah, I definitely do."
    pc "If I had you cooking for all the girls all the time I would have no trouble fattening them up."
    image natalie_stage4_55 = "/natalie/events/stage4/55.webp"
    scene natalie_stage4_55
    natalie "Thanks, I learned how to cook from my mother."
    natalie "She was a really good home cook."
    natalie "I got a lot of recipes passed down from her."
    pc "She seems like she was a great mother."
    natalie "She was. I always wanted to be like her until…"
    image natalie_stage4_56 = "/natalie/events/stage4/56.webp"
    scene natalie_stage4_56
    "She stopped, seeming to get sad and she instead chooses to go back to focusing on eating."
    image natalie_stage4_57 = "/natalie/events/stage4/57.webp"
    scene natalie_stage4_57
    "It seems like she really wants to impress you or make you happy, because as much food as there is, Natalie eats it all."
    image natalie_stage4_58 = "/natalie/events/stage4/58.webp"
    scene natalie_stage4_58
    "Finally she finishes and she sighs now with a full belly."
    image natalie_stage4_59 = "/natalie/events/stage4/59.webp"
    scene natalie_stage4_59
    natalie "That was great. Let's go over to the sofa."
    image natalie_stage4_60 = "/natalie/events/stage4/60.webp"
    scene natalie_stage4_60
    natalie "So I invited you over because there are some things I want to talk to you about."
    natalie "Things about me that are hard for me to talk about but I really need to tell you."
    pc "Sure."
    natalie "So years ago I found out that I was…"
    natalie "Infertile."
    natalie "Like I can’t have children."
    image natalie_stage4_61 = "/natalie/events/stage4/61.webp"
    scene natalie_stage4_61
    "She stops there, looking at you worriedly at your reaction to such news."
    "You however are just worried about her and how hard that must be for her."
    pc "Oh Natalie, I’m sorry to hear that."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/natalie/events/stage4/idle.webm" loop
    show movie with dissolve
    natalie "Admittedly when I found out the news I was devastated, I had always wanted to be a mother and then to find out that I never would be-"
    natalie "I felt like there was something wrong with me, that I wasn’t a real woman, or at least not one deserving of what other women had."
    natalie "I would never be able to have children of my own or have a family with a man that I loved."
    natalie "It really affected my self esteem and self worth and it just kept getting worse."
    natalie "It affected how I thought of myself and my relationship with others."
    natalie "I ended up just being with men that were terrible for me and kept putting me down."
    natalie "That’s what I thought I deserved and I wouldn’t have to feel bad not being able to give those men any children if I ended up with them."
    natalie "Yet then I met you and you were unlike any other man I’d ever met."
    natalie "You were so sweet and I could tell you truly cared about me and I suddenly didn’t feel as broken anymore."
    natalie "Like I was truly a beautiful, desirable woman to you."
    pc "You are."
    stop movie
    image natalie_stage4_62 = "/natalie/events/stage4/62.webp"
    scene natalie_stage4_62
    natalie "Even after knowing that I’m infertile?"
    pc "Of course! You’re still the amazing, wonderful woman that I know and this doesn’t change anything about how I feel about you."
    image natalie_stage4_63 = "/natalie/events/stage4/63.webp"
    scene natalie_stage4_63
    natalie "That’s…so great to hear. I’ve just been so worried about how you would react."
    pc "Why would you think it would cause me to think any less of you?"
    pc "If anything I only think more highly of you for having to go through that."
    image natalie_stage4_64 = "/natalie/events/stage4/64.webp"
    scene natalie_stage4_64
    natalie "Well, I know it’s early in our relationship but I really, really like you and you seem to really like me and I can’t help but have certain fantasies about you."
    "Natalie then blushed about what she might have implied."
    natalie "I mean yes, I do admittedly have those kinds of fantasies about you too as I’m guessing you do about me-"
    pc "I do."
    natalie "However I meant like fantasies where we fall totally in love and decide to live together, and I would get really huge."
    natalie "You would also have other women there too like Luna or Britta or Sally or whoever else that we could all eat and grow together."
    pc "That sounds like a good fantasy."
    image natalie_stage4_65 = "/natalie/events/stage4/65.webp"
    scene natalie_stage4_65
    natalie "It does but I also have fantasies about things that simply can’t happen, like maybe one day we end up deciding to start a family together and have children."
    pc "I see."
    image natalie_stage4_66 = "/natalie/events/stage4/66.webp"
    scene natalie_stage4_66
    natalie "It’s something though that I could never personally give you but I’ve been thinking and…"
    natalie "If you did decide you wanted children maybe one of the other women that you’re with would be willing to have them for you instead."
    natalie "That way I don’t have to feel bad and maybe I could help raise them and be sort of a mother that way."
    natalie "I’m not trying to pressure you or anything but it is a potential option if that’s what you were to decide to do."
    pc "I admittedly don’t know what the future holds either so I don’t know if I can comment on that right now."
    image natalie_stage4_67 = "/natalie/events/stage4/67.webp"
    scene natalie_stage4_67
    natalie "Of course, I totally understand."
    natalie "For now I’m just happy having you and enjoying being with you."
    pc "Me too. I really want to see where we go from here and where our relationship leads."
    natalie "Same. Speaking of which, there is something else I want to talk to you about."
    natalie "I knew I needed to tell you about my infertility problem first as I was worried it might need to come up before hand."
    natalie "So…"
    image natalie_stage4_68 = "/natalie/events/stage4/68.webp"
    scene natalie_stage4_68
    natalie "I would like to start having sex with you."
    natalie "The thing is I don’t think I’m quite ready for it."
    pc "I’m not pressuring you or anything, you don’t have to until you are ready."
    image natalie_stage4_69 = "/natalie/events/stage4/69.webp"
    scene natalie_stage4_69
    natalie "I am ready!"
    natalie "Well at least emotionally I am. You truly are an amazing guy and one I truly want to give myself and my body to."
    natalie "To give pleasure and receive pleasure back."
    natalie "It’s physically I’m worried about."
    natalie "Based on what the other girls have told me…you’re um…really big."
    pc "Yes I suppose I am."
    image natalie_stage4_70 = "/natalie/events/stage4/70.webp"
    scene natalie_stage4_70
    natalie "Can I…see it?"
    pc "Sure, it’s not like I haven’t seen you naked plenty of times by now."
    pc "It’s about time I got naked for you instead."
    image natalie_stage4_71 = "/natalie/events/stage4/71.webp"
    scene natalie_stage4_71
    "You stand up and take off your clothes to reveal your naked body along with your erect penis to her."
    "Natalie looks at all of your body but then settles on staring at your penis nervously but also excitedly."
    image natalie_stage4_72 = "/natalie/events/stage4/72.webp"
    scene natalie_stage4_72
    natalie "That’s…a lot bigger than anything I’ve ever had."
    natalie "I really don’t think it would come close to fitting."
    natalie "It really is such a beautiful penis though."
    natalie "I would love to have it inside me."
    pc "I would love to have it inside you too."
    natalie "I’m just going to have to prepare myself first."
    natalie "So I’ll be used to such a size and be able to take all of it."
    image natalie_stage4_73 = "/natalie/events/stage4/73.webp"
    scene natalie_stage4_73
    "She then couldn’t help but smile."
    pc "What?"
    image natalie_stage4_74 = "/natalie/events/stage4/74.webp"
    scene natalie_stage4_74
    natalie "It’s just I’ve got so used to stuffing myself and now I’ll have to get used to stuffing myself in a different way."
    pc "I admittedly do really like stuffing you full and I’m sure I’ll like doing it in this way too."
    natalie "Yes and I really want you to, just give me a little more time to prepare."
    natalie "I’ll get some toys to use while I think of you entering me and filling me up with the real thing."
    natalie "I’ll also do my best to eat and get bigger so it’s both easier to take all of you and also because I want the sex to be more enjoyable."
    pc "Sounds great to me."
    image natalie_stage4_75 = "/natalie/events/stage4/75.webp"
    scene natalie_stage4_75
    natalie "That being said, even if I can’t have that kind of penetrative sex…I really want to pleasure you in other ways."
    pc "Mmm, just what did you have in mind?"
    natalie "I know how much you like my breasts."
    pc "I do."
    image natalie_stage4_76 = "/natalie/events/stage4/76.webp"
    scene natalie_stage4_76
    natalie "I love my huge breasts."
    natalie "How much they make me feel like a real, sexy woman."
    natalie "How they produce milk for others to enjoy and help."
    image natalie_stage4_77 = "/natalie/events/stage4/77.webp"
    scene natalie_stage4_77
    natalie "How much you like them."
    natalie "And now I’m going to love them for how much pleasure I’m able to give you with them."
    pc "I’m definitely liking what you’re suggesting."
    natalie "Lie down on my bed."
    image natalie_stage4_78 = "/natalie/events/stage4/78.webp"
    scene natalie_stage4_78
    window hide
    pause
    image natalie_stage4_79 = "/natalie/events/stage4/79.webp"
    scene natalie_stage4_79
    pause
    if persistent.nosexscene:
        scene black with dissolve
        "Natalie and you had a good time."
    else:
        image natalie_stage4_80 = "/natalie/events/stage4/80.webp"
        scene natalie_stage4_80
        "She removes her clothes and gets totally naked for you before then sandwiching your penis in between her huge breasts."
        natalie "Mmm, looks like my breasts are big enough for your beautiful penis at least."
        pc "Yeah."
        pc "So big."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/natalie/events/stage4/titfuck1.webm" loop
        show movie with dissolve
        "She is already pushing her breasts together and rubbing them against your cock, sandwiched in between her very impressive cleavage."
        natalie "This is only the start though. I’m going to grow absolutely massive breasts to bring you more and more pleasure with."
        natalie "I’m going to get so massive for you."
        natalie "I’m going to have a body we will both love, a body you can enter and make love to whenever you want."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/natalie/events/stage4/titfuck2.webm" loop
        show movie with dissolve
        pc "Oh yeah, definitely."
        natalie "I’m going to make it happen."
        natalie "You’ve helped me realize who I’m meant to be."
        natalie "A ridiculously busty, super curvy and fat woman who is proud of what she has accomplished and how much she has grown both on the inside and out."
        natalie "I’m going to enjoy every bite of food knowing it is going to help me get there."
        pc "Sounds amazing."
        pc "This actually feels amazing."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/natalie/events/stage4/titfuck3.webm" loop
        show movie with dissolve
        natalie "I’m so glad, it turns me on so much to think of bringing you pleasure."
        pc "You are."
        pc "In fact I’m about to-"
        stop movie
        image natalie_stage4_81 = "/natalie/events/stage4/81.webp"
        scene natalie_stage4_81
        "In response Natalie bends down in between her cleavage and manages to put the tip of your penis inside her mouth as you erupt inside it."
        "Letting out stream after stream of cum."
        "Which Natalie takes and drinks all of it with ease."
        image natalie_stage4_82 = "/natalie/events/stage4/82.webp"
        scene natalie_stage4_82
        natalie "Hmm, after all the delicious food I’ve eaten lately, still the best is that I finally got to taste you instead."
        pc "You did."
        pc "Thank you for that, that was incredible."
    image natalie_stage4_83 = "/natalie/events/stage4/83.webp"
    scene natalie_stage4_83
    natalie "You’re welcome, you more than deserve it and a lot more…and soon I’ll be able to give you a lot more, a lot more pleasure, and a lot more of me."
    "Natalie then sighed happily."
    natalie "I’m so glad I finally told you the truth, I don’t know why I held off for so long but now that I have I just feel so much better."
    pc "That’s great. I’m glad you told me too."
    pc "I also really hope this will help your self esteem in knowing it doesn’t change how I feel about you."
    image natalie_stage4_84 = "/natalie/events/stage4/84.webp"
    scene natalie_stage4_84
    natalie "I think it definitely will."
    natalie "That I don’t need to worry so much about something I might do or say being something you don’t like."
    natalie "That you just like me for me."
    pc "I do."
    natalie "It’s just…been so long that I’ve carried this with me and now…I feel like I can finally move on and allow myself to feel good about who I am."
    pc "So if you don’t mind me asking, just how long then have you known you were infertile?"
    image natalie_stage4_85 = "/natalie/events/stage4/85.webp"
    scene natalie_stage4_85
    natalie "It’s okay, it’s been about 10 years now."
    natalie "At the time they told me there was nothing they could do."
    natalie "I suppose it is possible things might have changed and there might be some new method that has come available since then."
    pc "Are you suggesting you might want to look into it?"
    pc "I’m totally fine either way, I would only want you to if you do."
    image natalie_stage4_86 = "/natalie/events/stage4/86.webp"
    scene natalie_stage4_86
    natalie "I don’t know."
    natalie "Maybe."
    natalie "It would be hard for me to go through again, but if there really is a chance then I would definitely want to try and pursue it."
    pc "Again it’s up to you, but I will say if you decided you wanted to, there is one thing you could do."
    pc "The hospital doesn’t really specialize in that sort of thing, but Luna or Britta might be able to help or at least know someone who might be able to look into it for you?"
    pc "It’s just an option I thought of."
    natalie "That is a really good idea…"
    "Natalie seemed to be thinking hard about it."
    image natalie_stage4_87 = "/natalie/events/stage4/87.webp"
    scene natalie_stage4_87
    "She eventually seems to reach a decision and you seem to have a pretty good idea from the way she is looking just what that decision is."
    natalie "I think I know what I want to do, but I’d really like to know what you think first before I make a final decision?"
    menu:
        "You think she should pursue new fertility options and try to get pregnant.":
            pc "First of all, I’m only answering first because I already think I know what you plan to do."
            pc "I think you want to at least try to be able to get pregnant and see if there are any fertility treatments you can take that will work, is that correct?"
            image natalie_stage4_88 = "/natalie/events/stage4/88.webp"
            scene natalie_stage4_88
            natalie "Yes…I really do."
            pc "I really don’t want you getting hurt again if the answer still turns out to be no."
            pc "However I can tell how much this means to you and even if that is still the case."
            pc "I know you would just be left always wondering if you didn’t at least try again."
            pc "I also know how happy you would be if there is something that will work for you."
            pc "So I think it’s still worth pursuing."
            image natalie_stage4_89 = "/natalie/events/stage4/89.webp"
            scene natalie_stage4_89
            natalie "You know and understand me so well."
            natalie "Thank you for letting me know what you think."
            natalie "That is also how I feel too."
            natalie "It will be difficult for me to go through, even if the answer is still no, but at least if that is still the case I will still have you to help me get through it."
            pc "Of course, I’ll do whatever I can to support and help you."
            image natalie_stage4_90 = "/natalie/events/stage4/90.webp"
            scene natalie_stage4_90
            natalie "Thank you so much!"
            natalie "This means a lot to me."
            pc "You’re welcome."
            natalie "Now that you’ve helped me make a decision…it definitely feels like the right one."
            natalie "I’ll be able to truly find out if there is any chance at all that I might be able to become pregnant and have a child of my own."
            natalie "I’ll go ask Britta or Luna if there is any way they or someone they know can maybe help."
            natalie "Then go from there."
            pc "Sounds like a plan then."
            "Natalie still looks nervous but also hopeful and as she looks at you, there is another emotion she seems to now be feeling."


        "You think she should not try and get pregnant.":
            pc "First of all, I’m only answering first because I already think I know what you plan to do."
            pc "I think you still don’t want to, is that correct?"
            image natalie_stage4_88 = "/natalie/events/stage4/88.webp"
            scene natalie_stage4_88
            natalie "Yes."
            pc "I wouldn’t want you getting hurt all over again when you’ve already been told the answer is no."
            pc "As I’ve already said it also doesn’t change how I feel about you or our relationship."
            image natalie_stage4_90 = "/natalie/events/stage4/90.webp"
            scene natalie_stage4_90
            natalie "You know and understand me so well."
            natalie "Maybe years from now I might change my mind but for now I’d rather take this opportunity now that I’ve told you to try and move on."
            natalie "To be able to focus on us and what we do have."
            pc "I agree."
            "Natalie looks grateful and relaxed and as she looks at you, there is another emotion she seems to now be feeling."

    image natalie_stage4_91 = "/natalie/events/stage4/91.webp"
    scene natalie_stage4_91
    natalie "I love you."
    pc "I love you too."
    image natalie_stage4_92 = "/natalie/events/stage4/92.webp"
    scene natalie_stage4_92
    "The two of you lean in and share a long kiss…"
    "And just enjoy the moment."
    "Both of you naked, but not at all minding the close intimacy."
    "Aware that it may be the first of many times you are together like this."
    image natalie_stage4_93 = "/natalie/events/stage4/93.webp"
    scene natalie_stage4_93
    "All moments have to end some time though and eventually the both of you finally break apart and get your clothes back on and you leave."
    image natalie_stage4_94 = "/natalie/events/stage4/94.webp"
    scene natalie_stage4_94
    window hide
    pause
    image natalie_stage4_95 = "/natalie/events/stage4/95.webp"
    scene natalie_stage4_95
    pause
    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
    $ nataliestage4event2 = 0
    return
