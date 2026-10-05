# Daisy her Sex scene at her home
label daisy_home:
    image daisy_home_greet1 = "/teacher/[teacher.stage]/0/home_greet1.webp"
    scene daisy_home_greet1
    play music "/music/daisy.ogg" if_changed
    teacher "I’m so glad you came over."
    pc "Thank you for the invitation."
    image daisy_home_greet2 = "/teacher/[teacher.stage]/0/home_greet2.webp"
    scene daisy_home_greet2
    teacher "Please come in and make yourself at home."
    image daisy_home_greet3 = "/teacher/[teacher.stage]/0/home_greet3.webp"
    scene daisy_home_greet3
    if teacherstory <= 6 and teacher.stage >= 16:
        menu:
            "Ask Daisy about herself.":
                "You decide to ask Daisy about herself."
                teacher "I wouldn't mind telling my favorite student a bit about myself."
                "Daisy talks a bit about herself."
                $ teacherstory += 1
                #Unlocks more Daisy story in the stats page.
                $ renpy.notify("New Daisy story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Daisy anything."
    elif teacherstory == 5 and teacher.stage >= 14:
        menu:
            "Ask Daisy about herself.":
                "You decide to ask Daisy about herself."
                teacher "I wouldn't mind telling my favorite student a bit about myself."
                "Daisy talks a bit about herself."
                $ teacherstory += 1
                #Unlocks more Daisy story in the stats page.
                $ renpy.notify("New Daisy story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Daisy anything."
    elif teacherstory == 4 and teacher.stage >= 12:
        menu:
            "Ask Daisy about herself.":
                "You decide to ask Daisy about herself."
                teacher "I wouldn't mind telling my favorite student a bit about myself."
                "Daisy talks a bit about herself."
                $ teacherstory += 1
                #Unlocks more Daisy story in the stats page.
                $ renpy.notify("New Daisy story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Daisy anything."
    elif teacherstory == 3 and teacher.stage >= 11:
        menu:
            "Ask Daisy about herself.":
                "You decide to ask Daisy about herself."
                teacher "I wouldn't mind telling my favorite student a bit about myself."
                "Daisy talks a bit about herself."
                $ teacherstory += 1
                #Unlocks more Daisy story in the stats page.
                $ renpy.notify("New Daisy story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Daisy anything."
    elif teacherstory == 2 and teacher.stage >= 9:
        menu:
            "Ask Daisy about herself.":
                "You decide to ask Daisy about herself."
                teacher "I wouldn't mind telling my favorite student a bit about myself."
                "Daisy talks a bit about herself."
                $ teacherstory += 1
                #Unlocks more Daisy story in the stats page.
                $ renpy.notify("New Daisy story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Daisy anything."
    elif teacherstory == 1 and teacher.stage >= 7:
        menu:
            "Ask Daisy about herself.":
                "You decide to ask Daisy about herself."
                teacher "I wouldn't mind telling my favorite student a bit about myself."
                "Daisy talks a bit about herself."
                $ teacherstory += 1
                #Unlocks more Daisy story in the stats page.
                $ renpy.notify("New Daisy story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Daisy anything."
    elif teacherstory == 0:
        menu:
            "Ask Daisy about herself.":
                "You decide to ask Daisy about herself."
                teacher "I wouldn't mind telling my favorite student a bit about myself."
                "Daisy talks a bit about herself."
                $ teacherstory += 1
                #Unlocks more Daisy story in the stats page.
                $ renpy.notify("New Daisy story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Daisy anything."
    teacher "Now then, what would you like to do?"
    menu:
        "I want to feed you." if foodheld >= 1:
            show screen teacherfullness
            $ stuffed = 0
            teacher "I suppose there’s nothing wrong with doing a little extra credit over the weekend. Very well, let’s get started."
            image daisy_home_food = "/teacher/[teacher.stage]/0/home_food.webp"
            scene daisy_home_food
            pause
            call rngeatingdaisyhome from _call_rngeatingdaisyhome_4
            window hide
            pause
            $ foodheld -= 1
            $ teacher.fullness += 0.5
            image daisy_home_feeding_choice = "/teacher/[teacher.stage]/[stuffed]/home_feeding_choice.webp"
            scene daisy_home_feeding_choice
            teacher "Thank you very much for the food. I can keep going if you want."
            call daisy_home_feeding from _call_daisy_home_feeding_4
            if stuffed == 0:
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime
            teacher "That really hit the BWOOOOOORRRP spot."
            image daisy_home_drink = "/teacher/[teacher.stage]/[stuffed]/home_drink.webp"
            scene daisy_home_drink
            teacher "Daisy finishes off her indulgent binging by slurping down an entire soda."
            $ teacher.weight += (teacher.fullness / 2)
            $ teacher.fullness = 0
            if stuffed == 2:
                image daisy_home_foodcoma = "/teacher/[teacher.stage]/2/home_foodcoma.webp"
                scene daisy_home_foodcoma
                "After finishing her drink, Daisy flops down on the couch and falls into a food coma."
                hide screen teacherfullness
                $ stuffed = 0
                "Not wanting to disturb her, you clean up and head home."
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime
            if stuffed == 1:
                teacher "Thanks for all the great-"
                image daisy_home_burp = "/teacher/[teacher.stage]/1/home_burp.webp"
                scene daisy_home_burp with vpunch
                teacher "UUURRP food."
                hide screen teacherfullness
                $ stuffed = 0
                teacher "That really hit to spot."
                ######NEEDS MORE WORK
                "Work in Progress."
                "After having fun with Daisy you go back home."
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime
            else:
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime
        "Show me your outfits.":
            teacher "Ah, I hoped you would ask. I have just the one in mind. Wait right here."
            call Daisy_Home_Outfits from _call_Daisy_Home_Outfits
            stop music fadeout 1.0
            $ daytime += 1
            jump freetime
        "Would you like to have sex?":
            if persistent.nosexscene == True:
                "You have sex scenes disabled in preferences, now leaving Daisy's home."
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime
            call Daisy_Home_Sex from _call_Daisy_Home_Sex_3
            stop music fadeout 1.0
            $ daytime += 1
            jump freetime

label Daisy_Home_Outfits:
    #SHOW CLOTHES
    $ rng = renpy.random.randint(1,6)
    #Cow
    if rng == 1:
        image daisy_home_clothes_cow1 = "/teacher/[teacher.stage]/0/home_clothes_cow1.webp"
        scene daisy_home_clothes_cow1
        "After waiting a moment, Daisy returns wearing a comfortable looking cow pattern sweater."
        teacher "What do you think? I know it isn’t the most revealing of outfits, but it has its charm don’t you think?"
        image daisy_home_clothes_cow2 = "/teacher/[teacher.stage]/0/home_clothes_cow2.webp"
        scene daisy_home_clothes_cow2
        teacher "That being said, it is a little stuffy sometimes. What do you say to showing this cowgirl a good time?"
        menu:
            "Let’s have sex":
                if persistent.nosexscene == True:
                    "You have sex scenes disabled in preferences, now leaving daisy her home."
                    return
                call Daisy_Home_Sex from _call_Daisy_Home_Sex_4
                return
            "Head home":
                #PIC NEEDED
                "Daisy lets out a small sigh."
                teacher "Ah well, maybe next time."
                "I head home for the day."
                return
    #Super hero
    if rng == 2:
        image daisy_home_clothes_hero1 = "/teacher/[teacher.stage]/0/home_clothes_hero1.webp"
        scene daisy_home_clothes_hero1
        "Daisy returns with a confident stride to show off a skintight, black and blue leotard."
        teacher "I really like this one. It makes me feel like a superhero. Although, I think the only fitting name for me after this semester is over will be Super Fatty."
        image daisy_home_clothes_hero2 = "/teacher/[teacher.stage]/0/home_clothes_hero2.webp"
        scene daisy_home_clothes_hero2
        teacher "Before that, what say you to doing battle with your personal heroine?"
        menu:
            "Let’s have sex":
                if persistent.nosexscene == True:
                    "You have sex scenes disabled in preferences, now leaving daisy her home."
                    return
                call Daisy_Home_Sex from _call_Daisy_Home_Sex_5
                return
            "Head home":
                #PIC NEEDED
                "Daisy lets out a small sigh."
                teacher "Ah well, maybe next time."
                "I head home for the day."
                return
    #Robe
    if rng == 3:
        image daisy_home_clothes_gown1 = "/teacher/[teacher.stage]/0/home_clothes_gown1.webp"
        scene daisy_home_clothes_gown1
        "Daisy returns wearing a silk robe with a flower pattern."
        teacher "Ah, the perfect weekend attire. So soft and smooth against my body."
        image daisy_home_clothes_gown2 = "/teacher/[teacher.stage]/0/home_clothes_gown2.webp"
        scene daisy_home_clothes_gown2
        teacher "Not to mention, it’s pretty easy to open up to let my belly get some fresh air."
        image daisy_home_clothes_gown3 = "/teacher/[teacher.stage]/0/home_clothes_gown3.webp"
        scene daisy_home_clothes_gown3
        teacher "There’s also the added benefit of leaving other parts free from things like underwear or restraint. Do you know what I mean?"
        menu:
            "Let’s have sex":
                if persistent.nosexscene == True:
                    "You have sex scenes disabled in preferences, now leaving daisy her home."
                    return
                call Daisy_Home_Sex from _call_Daisy_Home_Sex_6
                return
            "Head home":
                #PIC NEEDED
                "Daisy lets out a small sigh."
                teacher "Ah well, maybe next time."
                "I head home for the day."
                return
    #Devil
    if rng == 4:
        image daisy_home_clothes_devil1 = "/teacher/[teacher.stage]/0/home_clothes_devil1.webp"
        scene daisy_home_clothes_devil1
        "Daisy returns wearing a demonic costume that sends a shiver down my spine."
        teacher "Do you like it? I sometimes get tired of playing the good teacher."
        image daisy_home_clothes_devil2 = "/teacher/[teacher.stage]/0/home_clothes_devil2.webp"
        scene daisy_home_clothes_devil2
        teacher "This one really brings out my more devilish side. What do you say I show you just how sinful I can be?"
        menu:
            "Let’s have sex":
                if persistent.nosexscene == True:
                    "You have sex scenes disabled in preferences, now leaving daisy her home."
                    return
                call Daisy_Home_Sex from _call_Daisy_Home_Sex_7
                return
            "Head home":
                #PIC NEEDED
                "Daisy lets out a small sigh."
                teacher "Ah well, maybe next time."
                "I head home for the day."
                return
    #Bunny
    if rng == 5:
        image daisy_home_clothes_bunny1 = "/teacher/[teacher.stage]/0/home_clothes_bunny1.webp"
        scene daisy_home_clothes_bunny1
        "Daisy comes back wearing a bunny outfit that leaves very little to the imagination."
        image daisy_home_clothes_bunny2 = "/teacher/[teacher.stage]/0/home_clothes_bunny2.webp"
        scene daisy_home_clothes_bunny2
        teacher "Got this one special from the Triangle Club. It’s both comfortable and functional."
        image daisy_home_clothes_bunny3 = "/teacher/[teacher.stage]/0/home_clothes_bunny3.webp"
        scene daisy_home_clothes_bunny3
        teacher "It’s perfectly built for both building up your partner’s lust and then letting them work it all out with my body."
        teacher "What do you say? Do you want to give it a spin?"
        menu:
            "Let’s do it":
                if persistent.nosexscene == True:
                    "You have sex scenes disabled in preferences, now leaving daisy her home."
                    return
                "Daisy lets out a laugh."
                teacher "I was hoping you would say that. Get undressed and sit on the couch so this bunny can show you how she hops."
                image daisy_home_clothes_bunny4 = "/teacher/[teacher.stage]/0/home_clothes_bunny4.webp"
                scene daisy_home_clothes_bunny4
                "Following her instructions, you get into position. Soon after, she climbs up on the cushions with you and proceeds to slide herself down onto your rigid member."
                "For a moment she just stays there, leaning back to let you feel the heft of her body as she balances upon your dick. Looking over her shoulder, she shoots you a grin."
                teacher "Come on. Let me see what you got."
                image daisy_home_clothes_bunny5 = "/teacher/[teacher.stage]/0/home_clothes_bunny5.webp"
                scene daisy_home_clothes_bunny5
                "Following her lead, you begin to rapidly thrust inside of her. Each shove is met with the sound of straining leather as her fat body tries to escape from her costume."
                "This sound is soon drowned out by your moans as you go faster and faster in an effort to breed like literal rabbits."
                "Inevitably, the two of you find release and slump against each other on the couch."
                teacher "That was great. So glad I bought this outfit."
                "After cleaning up, you head home for the day."
                return
            "No thank you. I think I’ll just head home":
                #PIC NEEDED
                "Daisy lets out a small sigh."
                teacher "Shame, I was really hoping to give this thing a test run. Ah well, maybe next time."
                "You head home for the day."
                return
    #Lingerie
    if rng == 6:
        image daisy_home_clothes_lingerie1 = "/teacher/[teacher.stage]/0/home_clothes_lingerie1.webp"
        scene daisy_home_clothes_lingerie1
        "After waiting a moment, Daisy returns wearing a set of black lingerie."
        image daisy_home_clothes_lingerie2 = "/teacher/[teacher.stage]/0/home_clothes_lingerie2.webp"
        scene daisy_home_clothes_lingerie2
        teacher "What do you think? I mostly just use these as sleepwear, but I don’t really sleep in them much when I have special guests over."
        image daisy_home_clothes_lingerie3 = "/teacher/[teacher.stage]/0/home_clothes_lingerie3.webp"
        scene daisy_home_clothes_lingerie3
        teacher "Especially when I get to show them certain angles. They just can’t help themselves from keeping me up all night long. Do you know what I mean?"
        menu:
            "Let’s do it":
                if persistent.nosexscene == True:
                    "You have sex scenes disabled in preferences, now leaving daisy her home."
                    return
                teacher "Come here, lover boy."
                image daisy_home_clothes_lingerie4 = "/teacher/[teacher.stage]/0/home_clothes_lingerie4.webp"
                scene daisy_home_clothes_lingerie4
                "Standing you up from the couch, Daisy helps you out of your clothing and pulls you against her body."
                "Pressing your chest against her back, she turns around to meet you with a deep kiss."
                "Intertwining your tongues as your hands grasp what you can of each other’s bodies is more than enough to get you both in the mood for what comes next."
                image daisy_home_clothes_lingerie5 = "/teacher/[teacher.stage]/0/home_clothes_lingerie5.webp"
                scene daisy_home_clothes_lingerie5
                "Keeping a tight grip on one another, you make your way over to the couch."
                "After getting into the right position, Daisy lowers herself down onto your rigid member. With a shake of her hips, she orders you to begin."
                image daisy_home_clothes_lingerie6 = "/teacher/[teacher.stage]/0/home_clothes_lingerie6.webp"
                scene daisy_home_clothes_lingerie6
                "Perhaps a little overzealous, you begin to rapidly thrust inside of her. The vigorous movement mixed with her added heft pops apart the bottom part of her outfit."
                "Too absorbed by lust to care, you and Daisy continue to indulge yourselves with each other’s bodies until you both reach the climax."
                teacher "Shame about the outfit, but I’d say it was more than worth it. Come back some other time and I might try this one out again."
                "After washing yourselves off and throwing out the torn remains of Daisy’s outfit, you head home."
                return
            "No thank you. I think I’ll just head home":
                #PIC NEEDED
                "Daisy lets out a small sigh."
                teacher "Shame, I was really hoping to give this thing a test run. Ah well, maybe next time."
                "You head home for the day."
                return

    #Sex scene starts here
label Daisy_Home_Sex:
    "She smirks at you."
    teacher "Well, aren't we naughty? Very well. How would you like to do it?"
    menu:
        "Vaginal.":
            image daisy_home_sex_vaginal1 = "/teacher/[teacher.stage]/0/home_sex_vaginal1.webp"
            scene daisy_home_sex_vaginal1
            "Throwing off each other's clothing in a fit a passion, you make your way over to the couch."
            "Going down first, Daisy drags you onto her naked body to allow you to feel her chubby belly press up against you."
            "Guiding your hips, she slides you into her dripping womanhood."
            teacher "Go ahead. Show me what you've learned."
            pc "Yes, Ms. Tanwen, I mean, Daisy."
            image daisy_home_sex_vaginal2 = "/teacher/[teacher.stage]/0/home_sex_vaginal2.webp"
            scene daisy_home_sex_vaginal2
            "Though the start is more than a little awkward, the unease washes away as you begin to thrust inside of her."
            "You're further entranced by her body with each shake of your hips, pressing your body up against her breasts and belly in an effort to sate both of your needs."
            "You manage to keep her steady as you reach towards her backside to give her meaty ass cheeks a good squeeze."
            "This overwhelming abundance of sensations as you fully give yourself to her ends upon you filling her with a load of cum."
        "Oral.":
            teacher "Oh, you want to do a different kind of feeding, huh? Alright, but I think it's only fair if I let you eat first. Come over here."
            "Stripping you of your clothing, Daisy slips out of her outfit and commands you to kneel on the ground."
            image daisy_home_sex_oral1 = "/teacher/[teacher.stage]/0/home_sex_oral1.webp"
            scene daisy_home_sex_oral1
            "Meeting Daisy behind the couch, you do as you're told as she leans over to present her backside."
            "Pressing your face up against her thick ass cheeks, you eventually maneuver your way towards her vagina."
            "Licking up the lingering wetness around her labia, you continue to drag your tongue across her womanhood."
            "You know you're doing something right from the soft moans that parse her lips."
            "Focusing you attention on her clit, you continue to suck and rub until you feel her flabby body jiggle from her release."
            teacher "Mmmm, I hope you enjoyed your meal at least half as much as I did. You must be pretty pent up after that. Let’s switch over."
            image daisy_home_sex_oral2 = "/teacher/[teacher.stage]/0/home_sex_oral2.webp"
            scene daisy_home_sex_oral2
            "Standing up straight, you watch as Daisy turns around and gets on her knees. Opening up her mouth, she swallows up your cock."
            "Grasping onto your legs for support, she continuously bobs her head back and forth."
            "The pure ecstasy you feel as she continues to drag her tongue along your shaft is added onto by the sight of her fat body shaking wildly from her enthusiastic movements."
            "Unable to contain yourself much longer, you hold onto her shoulders and release a load of cum."
            "Though she tries to swallow up every drop, more than a few globs leak out to drip onto her chest."
    image daisy_home_aftersex = "/teacher/[teacher.stage]/0/home_aftersex.webp"
    scene daisy_home_aftersex
    teacher "Looks like we made a bit of a mess, but it was more than worth it. You can go ahead and take the shower first. I think that about does it for me today."
    "After cleaning yourself off and giving Daisy a parting kiss, you head back to your house."
    return
    #Sex scene ends here

label Luna_home_new:
    image luna_home_arrive1 = "/luna/[luna.stage]/home_arrive1.webp"
    scene luna_home_arrive1
    luna "Hey!"
    pc "Hey Luna, how are you doing?"
    luna "I'm doing very well now that you are here."
    image luna_home_arrive2 = "/luna/[luna.stage]/home_arrive2.webp"
    scene luna_home_arrive2
    luna "Come on in."
    image luna_home_arrive3 = "/luna/[luna.stage]/home_arrive3.webp"
    scene luna_home_arrive3
    "You follow Luna towards her living room area."
    image luna_home_arrive4 = "/luna/[luna.stage]/home_arrive4.webp"
    scene luna_home_arrive4
    if lunastory <= 4 and luna.stage >= 10:
        call lunastoryask
    elif lunastory <= 3 and luna.stage >= 8:
        call lunastoryask
    elif lunastory <= 2 and luna.stage >= 6:
        call lunastoryask
    elif lunastory <= 1 and luna.stage >= 5:
        call lunastoryask
    elif lunastory == 0 and luna.stage >= 3:
        call lunastoryask
    else:
        "You talk a bit about how Luna's work is going."

    image luna_home_showoff1 = "/luna/[luna.stage]/home_showoff1.webp"
    scene luna_home_showoff1
    luna "What do you think about my outfit?"
    menu:
        "I love the outfit.":
            image luna_home_showoff2 = "/luna/[luna.stage]/home_showoff2.webp"
            scene luna_home_showoff2
            luna "I bought it just for you."
            "She turns around to show you."
            window hide
            pause
            image luna_home_showoff3 = "/luna/[luna.stage]/home_showoff3.webp"
            scene luna_home_showoff3
            window hide
            pause
            luna "Let's take it off though."
        "I bet you look even better without.":
            luna "In that case, lets get rid of these clothes."
    
    if luna.stage <= 6:
        image luna_home_undress1 = "/luna/[luna.stage]/home_undress1.webp"
        scene luna_home_undress1
        "She slowly removes her gown to show you her pink lingerie underneath."
        image luna_home_undress2 = "/luna/[luna.stage]/home_undress2.webp"
        scene luna_home_undress2
        window hide
        pause
        image luna_home_undress3 = "/luna/[luna.stage]/home_undress3.webp"
        scene luna_home_undress3
        window hide
        pause
    elif luna.stage >= 7 and luna.stage <= 9:
        image luna_home_undress1 = "/luna/[luna.stage]/home_undress1.webp"
        scene luna_home_undress1
        "She slowly removes her garter belt."
        image luna_home_undress2 = "/luna/[luna.stage]/home_undress2.webp"
        scene luna_home_undress2
        window hide
        pause
    elif luna.stage == 10 or luna.stage == 11:
        image luna_home_undress1 = "/luna/[luna.stage]/home_undress1.webp"
        scene luna_home_undress1
        "She slowly removes her purple dress to let out her big breasts."
        image luna_home_undress2 = "/luna/[luna.stage]/home_undress2.webp"
        scene luna_home_undress2
        window hide
        pause
        image luna_home_undress3 = "/luna/[luna.stage]/home_undress3.webp"
        scene luna_home_undress3
        window hide
        pause
    elif luna.stage >= 12:
        image luna_home_undress1 = "/luna/[luna.stage]/home_undress1.webp"
        scene luna_home_undress1
        "She slowly removes her dress to reveal her huge breasts."
        image luna_home_undress2 = "/luna/[luna.stage]/home_undress2.webp"
        scene luna_home_undress2
        window hide
        pause
        image luna_home_undress3 = "/luna/[luna.stage]/home_undress3.webp"
        scene luna_home_undress3
        window hide
        pause
        image luna_home_undress4 = "/luna/[luna.stage]/home_undress4.webp"
        scene luna_home_undress4
        window hide
        pause
    luna "So, I thought we should just get straight to it. What do you think?"
    menu:
        "Feed her.":
            call luna_feed_home
            return
        "Sexytime on couch.":
            call luna_home_couch
            return

label luna_home_couch:
    image luna_home_couch1 = "/luna/[luna.stage]/home_couch1.webp"
    scene luna_home_couch1
    luna "Come sit down on the couch."
    image luna_home_couch2 = "/luna/[luna.stage]/home_couch2.webp"
    scene luna_home_couch2
    luna "Get a good look of my big growing boobs."
    luna "They have gotten so much bigger so quickly."
    image luna_home_couch3 = "/luna/[luna.stage]/home_couch3.webp"
    scene luna_home_couch3
    "Appreciating her giant melons, you know they are not the only part of her that has grown a lot recently."
    window hide
    pause
    image luna_home_couch4 = "/luna/[luna.stage]/home_couch4.webp"
    scene luna_home_couch4
    luna "But, they are not big enough."
    window hide
    pause
    luna "So, you better keep up the effort to keep me full and satisfied."
    image luna_home_couch5 = "/luna/[luna.stage]/home_couch5.webp"
    scene luna_home_couch5
    "She moves to sit on your lap and kiss you passionately."
    image luna_home_couch6 = "/luna/[luna.stage]/home_couch6.webp"
    scene luna_home_couch6
    window hide
    pause
    image luna_home_couch7 = "/luna/[luna.stage]/home_couch7.webp"
    scene luna_home_couch7
    window hide
    pause
    image luna_home_couch8 = "/luna/[luna.stage]/home_couch8.webp"
    scene luna_home_couch8
    "As you continue to make out, she pushes you down and moves on top of you."
    image luna_home_couch9 = "/luna/[luna.stage]/home_couch9.webp"
    scene luna_home_couch9
    luna "How does it feel, having all of this extra weight on top of you?"
    luna "All this food you fed me, now pinning you down."
    image luna_home_couch10 = "/luna/[luna.stage]/home_couch10.webp"
    scene luna_home_couch10
    "She leans back in to continue making out."
    image luna_home_couch11 = "/luna/[luna.stage]/home_couch11.webp"
    scene luna_home_couch11
    luna "Do I feel something big and hard there?"
    if luna.stage <= 9:
        image luna_home_couch12 = "/luna/[luna.stage]/home_couch12.webp"
        scene luna_home_couch12
        "She quickly takes off her bra to reveal her soft round tits."
    if persistent.nosexscene == True:
        luna "Lets have some fun together."
        scene black with dissolve
        "Luna and you had an amazing time together."
        return
    image luna_home_couch13 = "/luna/[luna.stage]/home_couch13.webp"
    scene luna_home_couch13
    luna "Wow, someone is happy to see me."
    luna "So big!"
    image luna_home_couch14 = "/luna/[luna.stage]/home_couch14.webp"
    scene luna_home_couch14
    window hide
    pause
    menu:
        "Blowjob." if disable == 1:
            #Here goes the blowjob
            ""
            #ANIMATION NEEDED
            menu:
                "Cum.":
                    #ANIMATION NEEDED
                    ""
                    #PIC NEEDED
                    ""
                    #PIC NEEDED
                    ""
                    image luna_home_couch18 = "/luna/[luna.stage]/home_couch18.webp"
                    scene luna_home_couch18
                    ""
                    image luna_home_couch19 = "/luna/[luna.stage]/home_couch19.webp"
                    scene luna_home_couch19
                    ""
                    #Animation NEEDED
                    ""
                    #PIC NEEDED
                    return
                "Change activity.":
                    ""
        "Handjob.":
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            if luna.stage == 3:
                play movie "/images/luna/3/home_sex9.webm" loop
            elif luna.stage == 4:
                play movie "/images/luna/4/home_sex9.webm" loop
            elif luna.stage == 5:
                play movie "/images/luna/5/home_sex9.webm" loop
            elif luna.stage == 6:
                play movie "/images/luna/6/home_sex9.webm" loop
            elif luna.stage == 7:
                play movie "/images/luna/7/home_sex9.webm" loop
            elif luna.stage == 8:
                play movie "/images/luna/8/home_sex9.webm" loop
            elif luna.stage == 9:
                play movie "/images/luna/9/home_sex9.webm" loop
            elif luna.stage == 10:
                play movie "/images/luna/10/home_sex9.webm" loop
            elif luna.stage == 11:
                play movie "/images/luna/11/home_sex9.webm" loop
            elif luna.stage == 12:
                play movie "/images/luna/12/home_sex9.webm" loop
            show movie with dissolve
            window hide
            pause
            "She slowly strokes your cock up and down."
            luna "How does that feel?"
            pc "It feel great, but I want you."
            stop movie
    image luna_home_couch15 = "/luna/[luna.stage]/home_couch15.webp"
    scene luna_home_couch15
    luna "Oh, and what do you want to do with me?"
    image luna_home_couch16 = "/luna/[luna.stage]/home_couch16.webp"
    scene luna_home_couch16
    window hide
    pause
    #menu:
    #    "Stay on the couch.":
    #        #Stay in this label
    #        ""
    #    "Go to the bedroom.":
    #        #jump to the bedroom label
    #        jump luna_home_bedroom
    menu:
        "Eat her pussy.":
            luna "You want a taste of me, good choice."
            image luna_home_couch17 = "/luna/[luna.stage]/home_couch17.webp"
            scene luna_home_couch17
            "She takes of her panties."
            window hide
            pause
            image luna_home_couch18 = "/luna/[luna.stage]/home_couch18.webp"
            scene luna_home_couch18
            "She climbs back on you with her wet pussy above your head."
            image luna_home_couch19 = "/luna/[luna.stage]/home_couch19.webp"
            scene luna_home_couch19
            window hide
            pause
            "She slowly lowers herself onto your face."
            image luna_home_couch29 = "/luna/[luna.stage]/home_couch29.webp"
            scene luna_home_couch29
            window hide
            pause
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            if luna.stage == 3:
                play movie "/images/luna/3/home_sex7.webm" loop
            elif luna.stage == 4:
                play movie "/images/luna/4/home_sex7.webm" loop
            elif luna.stage == 5:
                play movie "/images/luna/5/home_sex7.webm" loop
            elif luna.stage == 6:
                play movie "/images/luna/6/home_sex7.webm" loop
            elif luna.stage == 7:
                play movie "/images/luna/7/home_sex7.webm" loop
            elif luna.stage == 8:
                play movie "/images/luna/8/home_sex7.webm" loop
            elif luna.stage == 9:
                play movie "/images/luna/9/home_sex7.webm" loop
            elif luna.stage == 10:
                play movie "/images/luna/10/home_sex7.webm" loop
            elif luna.stage == 11:
                play movie "/images/luna/11/home_sex7.webm" loop
            elif luna.stage == 12:
                play movie "/images/luna/12/home_sex7.webm" loop
            show movie with dissolve
            "She starts moving her hips while you eat her out."
            window hide
            pause
            "Looking up, you see her fat tits jiggling with every movement."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            if luna.stage == 3:
                play movie "/images/luna/3/home_sex8.webm" loop
            elif luna.stage == 4:
                play movie "/images/luna/4/home_sex8.webm" loop
            elif luna.stage == 5:
                play movie "/images/luna/5/home_sex8.webm" loop
            elif luna.stage == 6:
                play movie "/images/luna/6/home_sex8.webm" loop
            elif luna.stage == 7:
                play movie "/images/luna/7/home_sex8.webm" loop
            elif luna.stage == 8:
                play movie "/images/luna/8/home_sex8.webm" loop
            elif luna.stage == 9:
                play movie "/images/luna/9/home_sex8.webm" loop
            elif luna.stage == 10:
                play movie "/images/luna/10/home_sex8.webm" loop
            elif luna.stage == 11:
                play movie "/images/luna/11/home_sex8.webm" loop
            elif luna.stage == 12:
                play movie "/images/luna/12/home_sex8.webm" loop
            show movie with dissolve
            "With every move of your tongue, you hear Luna moan."
            window hide
            pause
            stop movie
        "Have her ride you.":
            luna "You read my mind."
            image luna_home_couch17 = "/luna/[luna.stage]/home_couch17.webp"
            scene luna_home_couch17
            "She takes of her panties."
            window hide
            pause
            "She then proceeds to get back on top of you."
    image luna_home_couch20 = "/luna/[luna.stage]/home_couch20.webp"
    scene luna_home_couch20
    window hide
    pause
    image luna_home_couch21 = "/luna/[luna.stage]/home_couch21.webp"
    scene luna_home_couch21
    luna "I want your big cock inside me."
    luna "I can't wait any longer."
    image luna_home_couch22 = "/luna/[luna.stage]/home_couch22.webp"
    scene luna_home_couch22
    "She lowers herself onto your dick."
    image luna_home_couch23 = "/luna/[luna.stage]/home_couch23.webp"
    scene luna_home_couch23
    luna "OH YES!, it feels sooo good."
    image luna_home_couch28 = "/luna/[luna.stage]/home_couch28.webp"
    scene luna_home_couch28
    "With your cock fully inside her she takes a moment to adjust herself before moving her hips up and down."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    if luna.stage == 3:
        play movie "/images/luna/3/home_sex10.webm" loop
    elif luna.stage == 4:
        play movie "/images/luna/4/home_sex10.webm" loop
    elif luna.stage == 5:
        play movie "/images/luna/5/home_sex10.webm" loop
    elif luna.stage == 6:
        play movie "/images/luna/6/home_sex10.webm" loop
    elif luna.stage == 7:
        play movie "/images/luna/7/home_sex10.webm" loop
    elif luna.stage == 8:
        play movie "/images/luna/8/home_sex10.webm" loop
    elif luna.stage == 9:
        play movie "/images/luna/9/home_sex10.webm" loop
    elif luna.stage == 10:
        play movie "/images/luna/10/home_sex10.webm" loop
    elif luna.stage == 11:
        play movie "/images/luna/11/home_sex10.webm" loop
    elif luna.stage == 12:
        play movie "/images/luna/12/home_sex10.webm" loop
    show movie with dissolve
    "Riding you passionately, her sweaty body turns into a jiggly mess."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    if luna.stage == 3:
        play movie "/images/luna/3/home_sex11.webm" loop
    elif luna.stage == 4:
        play movie "/images/luna/4/home_sex11.webm" loop
    elif luna.stage == 5:
        play movie "/images/luna/5/home_sex11.webm" loop
    elif luna.stage == 6:
        play movie "/images/luna/6/home_sex11.webm" loop
    elif luna.stage == 7:
        play movie "/images/luna/7/home_sex11.webm" loop
    elif luna.stage == 8:
        play movie "/images/luna/8/home_sex11.webm" loop
    elif luna.stage == 9:
        play movie "/images/luna/9/home_sex11.webm" loop
    elif luna.stage == 10:
        play movie "/images/luna/10/home_sex11.webm" loop
    elif luna.stage == 11:
        play movie "/images/luna/11/home_sex11.webm" loop
    elif luna.stage == 12:
        play movie "/images/luna/12/home_sex11.webm" loop
    show movie with dissolve
    "Her enormous heavy breasts flopping up and down with every thrust."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    if luna.stage == 3:
        play movie "/images/luna/3/home_sex13.webm" loop
    elif luna.stage == 4:
        play movie "/images/luna/4/home_sex13.webm" loop
    elif luna.stage == 5:
        play movie "/images/luna/5/home_sex13.webm" loop
    elif luna.stage == 6:
        play movie "/images/luna/6/home_sex13.webm" loop
    elif luna.stage == 7:
        play movie "/images/luna/7/home_sex13.webm" loop
    elif luna.stage == 8:
        play movie "/images/luna/8/home_sex13.webm" loop
    elif luna.stage == 9:
        play movie "/images/luna/9/home_sex13.webm" loop
    elif luna.stage == 10:
        play movie "/images/luna/10/home_sex13.webm" loop
    elif luna.stage == 11:
        play movie "/images/luna/11/home_sex13.webm" loop
    elif luna.stage == 12:
        play movie "/images/luna/12/home_sex13.webm" loop
    show movie with dissolve
    window hide
    pause
    luna "OH FUCK!"
    luna "Your huge cock feels so good inside me."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    if luna.stage == 3:
        play movie "/images/luna/3/home_sex12.webm" loop
    elif luna.stage == 4:
        play movie "/images/luna/4/home_sex12.webm" loop
    elif luna.stage == 5:
        play movie "/images/luna/5/home_sex12.webm" loop
    elif luna.stage == 6:
        play movie "/images/luna/6/home_sex12.webm" loop
    elif luna.stage == 7:
        play movie "/images/luna/7/home_sex12.webm" loop
    elif luna.stage == 8:
        play movie "/images/luna/8/home_sex12.webm" loop
    elif luna.stage == 9:
        play movie "/images/luna/9/home_sex12.webm" loop
    elif luna.stage == 10:
        play movie "/images/luna/10/home_sex12.webm" loop
    elif luna.stage == 11:
        play movie "/images/luna/11/home_sex12.webm" loop
    elif luna.stage == 12:
        play movie "/images/luna/12/home_sex12.webm" loop
    show movie with dissolve
    window hide
    pause
    "Hypnotized by her fat boobs swinging around, you can only imagine how big they will get."
    "All the fattening foods, the copious amounts of calories, going to making her breasts even bigger."
    stop movie
    image luna_home_couch24 = "/luna/[luna.stage]/home_couch24.webp"
    scene luna_home_couch24
    "Soon Luna has to take a break as she is completely out of breath."
    luna "Oh god, all this extra weight makes this a lot harder."
    luna "Also a lot more fun."
    image luna_home_couch25 = "/luna/[luna.stage]/home_couch25.webp"
    scene luna_home_couch25
    "With your dick still in her, she shifts around to lean back on the couch cushions."
    window hide
    pause
    image luna_home_couch26 = "/luna/[luna.stage]/home_couch26.webp"
    scene luna_home_couch26
    window hide
    pause
    image luna_home_couch27 = "/luna/[luna.stage]/home_couch27.webp"
    scene luna_home_couch27
    luna "That's better."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    if luna.stage == 3:
        play movie "/images/luna/3/home_sex1.webm" loop
    elif luna.stage == 4:
        play movie "/images/luna/4/home_sex1.webm" loop
    elif luna.stage == 5:
        play movie "/images/luna/5/home_sex1.webm" loop
    elif luna.stage == 6:
        play movie "/images/luna/6/home_sex1.webm" loop
    elif luna.stage == 7:
        play movie "/images/luna/7/home_sex1.webm" loop
    elif luna.stage == 8:
        play movie "/images/luna/8/home_sex1.webm" loop
    elif luna.stage == 9:
        play movie "/images/luna/9/home_sex1.webm" loop
    elif luna.stage == 10:
        play movie "/images/luna/10/home_sex1.webm" loop
    elif luna.stage == 11:
        play movie "/images/luna/11/home_sex1.webm" loop
    elif luna.stage == 12:
        play movie "/images/luna/12/home_sex1.webm" loop
    show movie with dissolve
    "She quickly resumes her movements."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    if luna.stage == 3:
        play movie "/images/luna/3/home_sex2.webm" loop
    elif luna.stage == 4:
        play movie "/images/luna/4/home_sex2.webm" loop
    elif luna.stage == 5:
        play movie "/images/luna/5/home_sex2.webm" loop
    elif luna.stage == 6:
        play movie "/images/luna/6/home_sex2.webm" loop
    elif luna.stage == 7:
        play movie "/images/luna/7/home_sex2.webm" loop
    elif luna.stage == 8:
        play movie "/images/luna/8/home_sex2.webm" loop
    elif luna.stage == 9:
        play movie "/images/luna/9/home_sex2.webm" loop
    elif luna.stage == 10:
        play movie "/images/luna/10/home_sex2.webm" loop
    elif luna.stage == 11:
        play movie "/images/luna/11/home_sex2.webm" loop
    elif luna.stage == 12:
        play movie "/images/luna/12/home_sex2.webm" loop
    show movie with dissolve
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    if luna.stage == 3:
        play movie "/images/luna/3/home_sex3.webm" loop
    elif luna.stage == 4:
        play movie "/images/luna/4/home_sex3.webm" loop
    elif luna.stage == 5:
        play movie "/images/luna/5/home_sex3.webm" loop
    elif luna.stage == 6:
        play movie "/images/luna/6/home_sex3.webm" loop
    elif luna.stage == 7:
        play movie "/images/luna/7/home_sex3.webm" loop
    elif luna.stage == 8:
        play movie "/images/luna/8/home_sex3.webm" loop
    elif luna.stage == 9:
        play movie "/images/luna/9/home_sex3.webm" loop
    elif luna.stage == 10:
        play movie "/images/luna/10/home_sex3.webm" loop
    elif luna.stage == 11:
        play movie "/images/luna/11/home_sex3.webm" loop
    elif luna.stage == 12:
        play movie "/images/luna/12/home_sex3.webm" loop
    show movie with dissolve
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    if luna.stage == 3:
        play movie "/images/luna/3/home_sex4.webm" loop
    elif luna.stage == 4:
        play movie "/images/luna/4/home_sex4.webm" loop
    elif luna.stage == 5:
        play movie "/images/luna/5/home_sex4.webm" loop
    elif luna.stage == 6:
        play movie "/images/luna/6/home_sex4.webm" loop
    elif luna.stage == 7:
        play movie "/images/luna/7/home_sex4.webm" loop
    elif luna.stage == 8:
        play movie "/images/luna/8/home_sex4.webm" loop
    elif luna.stage == 9:
        play movie "/images/luna/9/home_sex4.webm" loop
    elif luna.stage == 10:
        play movie "/images/luna/10/home_sex4.webm" loop
    elif luna.stage == 11:
        play movie "/images/luna/11/home_sex4.webm" loop
    elif luna.stage == 12:
        play movie "/images/luna/12/home_sex4.webm" loop
    show movie with dissolve
    "She speeds up her thrusts as her moans gets louder."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    if luna.stage == 3:
        play movie "/images/luna/3/home_sex5.webm" loop
    elif luna.stage == 4:
        play movie "/images/luna/4/home_sex5.webm" loop
    elif luna.stage == 5:
        play movie "/images/luna/5/home_sex5.webm" loop
    elif luna.stage == 6:
        play movie "/images/luna/6/home_sex5.webm" loop
    elif luna.stage == 7:
        play movie "/images/luna/7/home_sex5.webm" loop
    elif luna.stage == 8:
        play movie "/images/luna/8/home_sex5.webm" loop
    elif luna.stage == 9:
        play movie "/images/luna/9/home_sex5.webm" loop
    elif luna.stage == 10:
        play movie "/images/luna/10/home_sex5.webm" loop
    elif luna.stage == 11:
        play movie "/images/luna/11/home_sex5.webm" loop
    elif luna.stage == 12:
        play movie "/images/luna/12/home_sex5.webm" loop
    show movie with dissolve
    window hide
    pause
    luna "OOOHH, I'M SO CLOSE!"
    luna "CUM WITH ME BABE!"
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    if luna.stage == 3:
        play movie "/images/luna/3/home_sex6.webm" loop
    elif luna.stage == 4:
        play movie "/images/luna/4/home_sex6.webm" loop
    elif luna.stage == 5:
        play movie "/images/luna/5/home_sex6.webm" loop
    elif luna.stage == 6:
        play movie "/images/luna/6/home_sex6.webm" loop
    elif luna.stage == 7:
        play movie "/images/luna/7/home_sex6.webm" loop
    elif luna.stage == 8:
        play movie "/images/luna/8/home_sex6.webm" loop
    elif luna.stage == 9:
        play movie "/images/luna/9/home_sex6.webm" loop
    elif luna.stage == 10:
        play movie "/images/luna/10/home_sex6.webm" loop
    elif luna.stage == 11:
        play movie "/images/luna/11/home_sex6.webm" loop
    elif luna.stage == 12:
        play movie "/images/luna/12/home_sex6.webm" loop
    show movie with dissolve
    window hide
    pause
    "With a final few trusts, both of you orgasm at the same time."
    stop movie
    scene black with dissolve
    "After coming back to your senses you clean up and head home."
    return


    


##Luna interactive home sex scene
label luna_home:
    image luna_home_greet = "/luna/[luna.stage]/home_greet.webp"
    scene luna_home_greet
    luna "Hey!"
    pc "Hey Luna, how are you doing?"
    luna "I'm doing very well now that you are here."
    luna "Come on in."
    image luna_home_sitting = "/luna/[luna.stage]/home_sitting.webp"
    scene luna_home_sitting
    if lunastory <= 4 and luna.stage >= 10:
        call lunastoryask
    elif lunastory <= 3 and luna.stage >= 8:
        call lunastoryask
    elif lunastory <= 2 and luna.stage >= 6:
        call lunastoryask
    elif lunastory <= 1 and luna.stage >= 5:
        call lunastoryask
    elif lunastory == 0 and luna.stage >= 3:
        call lunastoryask
    luna "So, I thought we should just get straight to it. What do you think?"
    menu:
        "Yeah, let's have some fun together!":
            luna "In that case, lets get rid of these clothes."
            call luna_sex_home from _call_luna_sex_home

        "I think you should eat some food first." if foodheld >= 1:
            luna "Well, now that you say it, I am quite hungry."
            call luna_feed_home from _call_luna_feed_home
    return


#Luna Her feeding scene at her home
label luna_feed_home:
    show screen lunafullness
    image luna_home_feeding_start = "/luna/[luna.stage]/home_feeding_start.webp"
    scene luna_home_feeding_start
    luna "I hoped you would say that, I'm really hungry."
    $ stuffed = 1
    call rngeatinglunahome from _call_rngeatinglunahome_4
    window hide
    pause
    $ foodheld -= 1
    $ luna.fullness += 0.5
    call luna_home_feeding from _call_luna_home_feeding_4
    image luna_home_feeding_drink = "/luna/[luna.stage]/home_feeding_drink_[stuffed].webp"
    scene luna_home_feeding_drink
    "She places a big cup of soda between her breasts, pushing them together with her arms to hold up her drinking cup."
    luna "Some delicious soda to finish with."
    $ luna.weight += (luna.fullness / 2)
    $ luna.fullness = 0
    hide screen lunafullness
    if stuffed == 3 or stuffed == 2:
        image luna_home_feeding_sleep1 = "/luna/[luna.stage]/home_feeding_sleep1_[stuffed].webp"
        scene luna_home_feeding_sleep1
        "Luna lies down on her bed and immediately falls asleep."
        image luna_home_feeding_sleep2 = "/luna/[luna.stage]/home_feeding_sleep2_[stuffed].webp"
        scene luna_home_feeding_sleep2
        "While sleeping she starts snoring quite loudly."
        "I clean up all of the empty food packaging, and head home."
        scene city_night
        $ stuffed = 0
        return
    else:
        image luna_home_feeding_end = "/luna/[luna.stage]/home_feeding_end.webp"
        scene luna_home_feeding_end
        "She stands up and walks over to the couch."
    call luna_home_couch
    return

#Luna her interactable sex scene at her home
label luna_sex_home:
    image luna_home_stripping = "/luna/[luna.stage]/home_stripping.webp"
    scene luna_home_stripping
    window hide
    pause
    $ stuffed = 0
    luna "Do you like my lingerie?"
    menu:
        "Yes, I do.":
            image luna_home_lingerie_showoff1 = "/luna/[luna.stage]/home_lingerie_showoff1.webp"
            scene luna_home_lingerie_showoff1
            window hide
            pause
            luna "I bought it just for you."
            luna "I hope you like it from the back too."
            image luna_home_lingerie_showoff2 = "/luna/[luna.stage]/home_lingerie_showoff2.webp"
            scene luna_home_lingerie_showoff2
            window hide
            pause
            luna "Let's take off the rest."

        "I think you look even better without.":
            luna "Good thing I wasn't done stripping yet."

    image luna_home_stripping2 = "/luna/[luna.stage]/home_stripping2.webp"
    scene luna_home_stripping2
    window hide
    pause
    "She took off her bra to show off her huge breasts."
    image luna_home_stripped = "/luna/[luna.stage]/home_stripped.webp"
    scene luna_home_stripped

    #Cuts out the sex scene if nosex is selected.
    if persistent.nosexscene == True:
        luna "Lets have some fun together."
        scene black with dissolve
        "You and Luna had a fantasic evening together."
        image luna_home_tosleep = "/luna/[luna.stage]/home_tosleep.webp"
        scene luna_home_tosleep
        window hide
        pause
        "While falling asleep you see Luna coming back to bed, she looks like an angel."
        luna "Sleep well, [playername]."
        scene black with dissolve
        "You sleep until the next morning."
        image luna_home_sleeping1 = "/luna/[luna.stage]/home_sleeping1.webp"
        scene luna_home_sleeping1 with dissolve
        window hide
        pause
        pc "Luna looks so peaceful."
        pc "I should get clothed."
        image luna_home_sleeping2 = "/luna/[luna.stage]/home_sleeping2.webp"
        scene luna_home_sleeping2
        window hide
        pause
        "Luna starts waking up while you put on your clothes."
        image luna_home_wakeup = "/luna/[luna.stage]/home_wakeup.webp"
        scene luna_home_wakeup
        luna "Good morning, how late is it?"
        pc "It's 8AM right now."
        luna "8AM! I'm sorry but you need to leave."
        image luna_home_bye = "/luna/[luna.stage]/home_bye.webp"
        scene luna_home_bye
        "You grab all your stuff."
        luna "Thank you for the awesome night, I'll call you soon."
        pc "Bye, Luna."
        luna "Bye bye."
        "You go home."

        return

    ##Sex scene starts here
    luna "What position do you want to start with?"
    menu:
        "Doggystyle":
            luna "Good choice!"
            image luna_home_doggy = "/luna/[luna.stage]/home_doggy.webp"
            scene luna_home_doggy
            window hide
            pause
            luna "My pussy is ready for you."
            image luna_home_doggy1 = "/luna/[luna.stage]/home_doggy1.webp"
            scene luna_home_doggy1
            window hide
            pause
            luna "Pleasuring me first, like a real gentleman."
            "Luna moaned with pleasure while you licked her pussy."
            luna "Come give me your meat."
            image luna_home_doggy3 = "/luna/[luna.stage]/home_doggy3.webp"
            scene luna_home_doggy3
            window hide
            pause
            "You insert your throbbing cock into Luna's wet pussy."
            luna "So hard and warm."
            image luna_home_doggy2 = "/luna/[luna.stage]/home_doggy2.webp"
            scene luna_home_doggy2
            window hide
            pause
            "You feel luna's big tits, they feel really soft."
            luna "They feel bigger, don't they? They have grown a lot since we met each other."
            menu:

                "Have anal sex":
                    image luna_home_doggy5 = "/luna/[luna.stage]/home_doggy5.webp"
                    scene luna_home_doggy5
                    window hide
                    pause
                    luna "Oh, that's a bit of surprise."
                    luna "Keep going though, this feels great."
                    image luna_home_doggy4 = "/luna/[luna.stage]/home_doggy4.webp"
                    scene luna_home_doggy4
                    window hide
                    pause
                    if luna.stage == 3:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/3/home_doggy4_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 4:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/4/home_doggy4_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 5:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/5/home_doggy4_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 6:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/6/home_doggy4_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 7:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/7/home_doggy4_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 8:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/8/home_doggy4_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 9:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/9/home_doggy4_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 10:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/10/home_doggy4_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 11:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/11/home_doggy4_video.webm" loop
                        show movie with dissolve
                    pause
                    "You decide to speed it up a little."
                    "Luna screams with pleasure while you feel like you are going to cum."
                    stop movie
                    luna "Go lie there, I will take it from here."
                    image luna_home_96 = "/luna/[luna.stage]/home_96.webp"
                    scene luna_home_96
                    window hide
                    pause
                    "Luna puts her round juicy ass in your face and starts rubbing your cock."
                    pc "Oh yeah, just like that."
                    image luna_home_69 = "/luna/[luna.stage]/home_69.webp"
                    scene luna_home_69
                    window hide
                    pause
                    luna "Keep licking down there."
                    "After some good rubbing you start cumming on Luna's chest."
                    luna "Help me finish too."
                    image luna_home_finishing = "/luna/[luna.stage]/home_finishing.webp"
                    scene luna_home_finishing
                    window hide
                    pause
                    "Luna pushes you down and sits on you."
                    "Luna screams in pleasure while she has an orgasm."
                    image luna_home_finished = "/luna/[luna.stage]/home_finished.webp"
                    scene luna_home_finished
                    window hide
                    pause
                    luna "That was amazing, we should do this more often."
                    luna "Let me clean up this mess you made."
                    "You lie down on the bed and slowly fall asleep."
                    image luna_home_tosleep = "/luna/[luna.stage]/home_tosleep.webp"
                    scene luna_home_tosleep
                    window hide
                    pause
                    "While falling asleep you see Luna coming back to bed, she looks like an angel."
                    luna "Sleep well, [playername]."
                    scene black with dissolve
                    "You fall asleep."
                    call luna_morning_home from _call_luna_morning_home_5
                    return

                "Change position":
                    "What position?"
                    menu:
                        "Missionary":
                            luna "I love missionary, let me get ready."
                            "Luna lays down on the bed."
                            image luna_home_missionary = "/luna/[luna.stage]/home_missionary.webp"
                            scene luna_home_missionary
                            window hide
                            pause
                            luna "I'm ready for you."
                            "You go and have sex with Luna."
                            image luna_home_missionary1 = "/luna/[luna.stage]/home_missionary1.webp"
                            scene luna_home_missionary1
                            window hide
                            pause
                            "You start thrusting slowly while holding her hands."
                            image luna_home_missionary3 = "/luna/[luna.stage]/home_missionary3.webp"
                            scene luna_home_missionary3
                            window hide
                            pause
                            "Luna moans while you start thrusting a bit faster."
                            "You watch Luna's breasts going up and down while thrusting."
                            image luna_home_missionary2 = "/luna/[luna.stage]/home_missionary2.webp"
                            scene luna_home_missionary2
                            window hide
                            pause
                            "You come down to her and begin to carress her hair."
                            luna "You won't believe how good this feels."
                            image luna_home_missionary4 = "/luna/[luna.stage]/home_missionary4.webp"
                            scene luna_home_missionary4
                            window hide
                            pause
                            "You start to thrust even faster."
                            "Luna screams in pleasure while having an orgasm."
                            "You pull out and cum on her chest."
                            image luna_home_finished = "/luna/[luna.stage]/home_finished.webp"
                            scene luna_home_finished
                            window hide
                            pause
                            luna "That was amazing, we should do this more often."
                            luna "Let me clean up this mess you made."
                            "You lie down on the bed and slowly fall asleep."
                            image luna_home_tosleep = "/luna/[luna.stage]/home_tosleep.webp"
                            scene luna_home_tosleep
                            window hide
                            pause
                            "While falling asleep you see Luna coming back to bed, she looks like an angel."
                            luna "Sleep well, [playername]."
                            scene black with dissolve
                            "You fall asleep."
                            call luna_morning_home from _call_luna_morning_home
                            return

                        "Cowgirl":
                            luna "I love it when I get to take the lead."
                            luna "Go lie down on the bed."
                            image luna_home_cowgirl1 = "/luna/[luna.stage]/home_cowgirl1.webp"
                            scene luna_home_cowgirl1
                            window hide
                            pause
                            "Luna puts your dick in her pussy and slowly sits down on your lap."
                            luna "That feels great."
                            image luna_home_cowgirl4 = "/luna/[luna.stage]/home_cowgirl4.webp"
                            scene luna_home_cowgirl4
                            window hide
                            pause
                            "Luna starts riding your dick."
                            pc "Keep going, you are doing fantastic."
                            image luna_home_cowgirl3 = "/luna/[luna.stage]/home_cowgirl3.webp"
                            scene luna_home_cowgirl3
                            window hide
                            pause
                            "While Luna is riding you, you have perfect view of Luna's big tits bouncing up and down."
                            image luna_home_cowgirl2 = "/luna/[luna.stage]/home_cowgirl2.webp"
                            scene luna_home_cowgirl2
                            window hide
                            pause
                            luna "Oh My God! This is sooo good!"
                            "Luna starts rubbing her clit while riding you."
                            image luna_home_cowgirl5 = "/luna/[luna.stage]/home_cowgirl5.webp"
                            scene luna_home_cowgirl5
                            window hide
                            pause
                            "Luna collapses on you while she has an orgasm."
                            "She screams from pleasure and then kisses you."
                            luna "That was amazing, sorry for suffocating you with these tits."
                            luna "Let's make sure you are finished too. Give me your dick."
                            "Luna lies down on the bed with her mouth open."
                            image luna_home_missionary5 = "/luna/[luna.stage]/home_missionary5.webp"
                            scene luna_home_missionary5
                            window hide
                            pause
                            "You insert your penis into her mouth."
                            pc "Fuck, baby! Your mouth feels so good."
                            "After some oral sex you pull out of her mouth and cum on her chest."
                            image luna_home_finished = "/luna/[luna.stage]/home_finished.webp"
                            scene luna_home_finished
                            window hide
                            pause
                            luna "That was amazing, we should do this more often."
                            luna "Let me clean up this mess you made."
                            "You lie down on the bed and slowly fall asleep."
                            image luna_home_tosleep = "/luna/[luna.stage]/home_tosleep.webp"
                            scene luna_home_tosleep
                            window hide
                            pause
                            "While falling asleep you see Luna coming back to bed, she looks like an angel."
                            luna "Sleep well, [playername]."
                            scene black with dissolve
                            "You fall asleep."
                            call luna_morning_home from _call_luna_morning_home_1
                            return

                "Try an exotic position" if kamasutravol1 == 1:
                    image luna_home_doggy6 = "/luna/[luna.stage]/home_doggy6.webp"
                    scene luna_home_doggy6
                    window hide
                    pause
                    "You try out some positions you read about in the kamasutra book."
                    luna "Woah, I didn't know you were into exotic poses."
                    image luna_home_exotic1 = "/luna/[luna.stage]/home_exotic1.webp"
                    scene luna_home_exotic1
                    window hide
                    pause
                    if luna.stage == 3:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/3/home_exotic1_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 4:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/4/home_exotic1_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 5:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/5/home_exotic1_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 6:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/6/home_exotic1_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 7:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/7/home_exotic1_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 8:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/8/home_exotic1_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 9:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/9/home_exotic1_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 10:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/10/home_exotic1_video.webm" loop
                        show movie with dissolve
                    elif luna.stage == 11:
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/luna/11/home_exotic1_video.webm" loop
                        show movie with dissolve
                    pause
                    luna "I love this."
                    "The intercourse between you and Luna started to look like dance."
                    stop movie
                    image luna_home_exotic3 = "/luna/[luna.stage]/home_exotic3.webp"
                    scene luna_home_exotic3
                    window hide
                    pause
                    "You started to thrust faster."
                    luna "Yes, take me harder!"
                    image luna_home_exotic2 = "/luna/[luna.stage]/home_exotic2.webp"
                    scene luna_home_exotic2
                    window hide
                    pause
                    "Luna turned around to make out while having sex."
                    "Both of you orgasm while being at each other's lips."
                    "All this incredible hot sex made you forget to pull out before cumming."
                    image luna_home_tosleep = "/luna/[luna.stage]/home_tosleep.webp"
                    scene luna_home_tosleep
                    window hide
                    pause
                    luna "Don't worry about cumming inside me. I'm on birth control."
                    "Your performance has exhausted you so much that you fall asleep instantly."
                    luna "Sleep well, [playername]."
                    scene black with dissolve
                    "You fall asleep."
                    call luna_morning_home from _call_luna_morning_home_2
                    return


        "Missionary":
            luna "I love missionary, let me get ready."
            "Luna lays down on the bed."
            image luna_home_missionary = "/luna/[luna.stage]/home_missionary.webp"
            scene luna_home_missionary
            window hide
            pause
            luna "I'm ready for you."
            "You go and have sex with Luna."
            image luna_home_missionary1 = "/luna/[luna.stage]/home_missionary1.webp"
            scene luna_home_missionary1
            window hide
            pause
            "You start thrusting slowly while holding her hands."
            image luna_home_missionary3 = "/luna/[luna.stage]/home_missionary3.webp"
            scene luna_home_missionary3
            window hide
            pause
            "Luna moans while you start thrusting a bit faster."
            "You watch Luna's breasts going up and down while thrusting."
            image luna_home_missionary2 = "/luna/[luna.stage]/home_missionary2.webp"
            scene luna_home_missionary2
            window hide
            pause
            "You come down to her and begin to carress her hair."
            luna "You won't believe how good this feels."
            image luna_home_missionary4 = "/luna/[luna.stage]/home_missionary4.webp"
            scene luna_home_missionary4
            window hide
            pause
            "You start to thrust even faster."
            "Luna screams in pleasure while having an orgasm."
            "You pull out and cum on her chest."
            image luna_home_finished = "/luna/[luna.stage]/home_finished.webp"
            scene luna_home_finished
            window hide
            pause
            luna "That was amazing, we should do this more often."
            luna "Let me clean up this mess you made."
            "You lie down on the bed and slowly fall asleep."
            image luna_home_tosleep = "/luna/[luna.stage]/home_tosleep.webp"
            scene luna_home_tosleep
            window hide
            pause
            "While falling asleep you see Luna coming back to bed, she looks like an angel."
            luna "Sleep well, [playername]."
            scene black with dissolve
            "You fall asleep."
            call luna_morning_home from _call_luna_morning_home_3
            return

        "Cowgirl":
            luna "I love it when I get to take the lead."
            luna "Go lie down on the bed."
            image luna_home_cowgirl1 = "/luna/[luna.stage]/home_cowgirl1.webp"
            scene luna_home_cowgirl1
            window hide
            pause
            "Luna puts your dick in her pussy and slowly sits down on your lap."
            luna "That feels great."
            image luna_home_cowgirl4 = "/luna/[luna.stage]/home_cowgirl4.webp"
            scene luna_home_cowgirl4
            window hide
            pause
            "Luna starts riding your dick."
            pc "Keep going, you are doing fantastic."
            image luna_home_cowgirl3 = "/luna/[luna.stage]/home_cowgirl3.webp"
            scene luna_home_cowgirl3
            window hide
            pause
            "While Luna is riding you, you have perfect view of Luna's big tits bouncing up and down."
            image luna_home_cowgirl2 = "/luna/[luna.stage]/home_cowgirl2.webp"
            scene luna_home_cowgirl2
            window hide
            pause
            luna "Oh My God! This is sooo good!"
            "Luna starts rubbing her clit while riding you."
            image luna_home_cowgirl5 = "/luna/[luna.stage]/home_cowgirl5.webp"
            scene luna_home_cowgirl5
            window hide
            pause
            "Luna collapses on you while she has an orgasm."
            "She screams from pleasure and then kisses you."
            luna "That was amazing, sorry for suffocating you with these tits."
            luna "Let's make sure you are finished too. Give me your dick."
            "Luna lies down on the bed with her mouth open."
            image luna_home_missionary5 = "/luna/[luna.stage]/home_missionary5.webp"
            scene luna_home_missionary5
            window hide
            pause
            "You insert your penis into her mouth."
            pc "Fuck, baby! Your mouth feels so good."
            "After some oral sex you pull out of her mouth and cum on her chest."
            image luna_home_finished = "/luna/[luna.stage]/home_finished.webp"
            scene luna_home_finished
            window hide
            pause
            luna "That was amazing, we should do this more often."
            luna "Let me clean up this mess you made."
            "You lie down on the bed and slowly fall asleep."
            image luna_home_tosleep = "/luna/[luna.stage]/home_tosleep.webp"
            scene luna_home_tosleep
            window hide
            pause
            "While falling asleep you see Luna coming back to bed, she looks like an angel."
            luna "Sleep well, [playername]."
            scene black with dissolve
            "You fall asleep."
            call luna_morning_home from _call_luna_morning_home_4
            return


    return

label luna_morning_home:
    $ lunamorningrng = renpy.random.randint(1,2)
    if lunamorningrng >= 2:
        "You slowly wake up after feeling some movement next to you."
        image luna_home_morningsex1 = "/luna/[luna.stage]/home_morning_1.webp"
        scene luna_home_morningsex1
        window hide
        pause
        "Luna looks at you with a fiery look full of desire. You immediately realize what she wants."
        image luna_home_morningsex2 = "/luna/[luna.stage]/home_morning_2.webp"
        scene luna_home_morningsex2
        window hide
        pause
        "Without saying a single thing Luna slowly moves her body on top of you."
        image luna_home_morningsex3 = "/luna/[luna.stage]/home_morning_3.webp"
        scene luna_home_morningsex3
        window hide
        pause
        "She moves her body closer to your face - giving you a good view of her huge breasts."
        image luna_home_morningsex4 = "/luna/[luna.stage]/home_morning_4.webp"
        scene luna_home_morningsex4
        window hide
        pause
        "Getting closer to your face, Luna gets closer to your face."
        image luna_home_morningsex5 = "/luna/[luna.stage]/home_morning_5.webp"
        scene luna_home_morningsex5
        window hide
        pause
        "After her pussy reaches your face, you start licking it."
        "While licking, Luna's body begins to shake with pleasure, ultimately resulting in her reaching her climax."
        "Exhausted by the amazing night and licking you pass out again."
        scene black with dissolve
        "You sleep until the next morning."
        image luna_home_sleeping1 = "/luna/[luna.stage]/home_sleeping1.webp"
        scene luna_home_sleeping1 with dissolve
        window hide
        pause
        pc "Luna looks so peaceful."
        pc "I should get clothed."
        image luna_home_sleeping2 = "/luna/[luna.stage]/home_sleeping2.webp"
        scene luna_home_sleeping2
        window hide
        pause
        "Luna starts waking up while you put on your clothes."
        image luna_home_wakeup = "/luna/[luna.stage]/home_wakeup.webp"
        scene luna_home_wakeup
        luna "Good morning, how late is it?"
        pc "It's 8 o'clock right now."
        luna "8 o'clock! I'm sorry but you need to leave."
        image luna_home_bye = "/luna/[luna.stage]/home_bye.webp"
        scene luna_home_bye
        "You grab all your stuff."
        luna "Thank you for the awesome night, I'll call you soon."
        pc "Bye, Luna."
        luna "Bye bye."
        "You go home."
        return

    else:
        image luna_home_sleeping1 = "/luna/[luna.stage]/home_sleeping1.webp"
        scene luna_home_sleeping1 with dissolve
        window hide
        pause
        pc "Luna looks so peaceful."
        pc "I should get clothed."
        image luna_home_sleeping2 = "/luna/[luna.stage]/home_sleeping2.webp"
        scene luna_home_sleeping2
        window hide
        pause
        "Luna starts waking up while you put on your clothes."
        image luna_home_wakeup = "/luna/[luna.stage]/home_wakeup.webp"
        scene luna_home_wakeup
        luna "Good morning, how late is it?"
        pc "It's 8AM right now."
        luna "8AM! I'm sorry but you need to leave."
        image luna_home_bye = "/luna/[luna.stage]/home_bye.webp"
        scene luna_home_bye
        "You grab all your stuff."
        luna "Thank you for the awesome night, I'll call you soon."
        pc "Bye, Luna."
        luna "Bye bye."
        "You go home."
        return

    ## Sex scene ends here

label katrine_sex_home:
    window hide
    image katrine_home_strip1 = "/katrine/[katrine.stage]/home_strip1.webp"
    scene katrine_home_strip1
    if katrine.stage <= 7:
        "Katrine walks towards her bed, turns around and rips open her blouse, revealing her round breasts."
    else:
        "Katrine walks towards her bed, turns around and rips open her dress, revealing her round breasts."
    katrine "I know you like seeing these."
    image katrine_home_strip2 = "/katrine/[katrine.stage]/home_strip2.webp"
    scene katrine_home_strip2
    if katrine.stage <= 7:
        "She then starts pulling down her skirt."
    else:
        "She then starts taking off her dress."
    image katrine_home_strip3 = "/katrine/[katrine.stage]/home_strip3.webp"
    scene katrine_home_strip3
    "Soon her stockings are the only thing she is still wearing."
    image katrine_home_doggybed = "/katrine/[katrine.stage]/home_doggybed.webp"
    scene katrine_home_doggybed
    katrine "So, what are you waiting for? Get yourself over here."
    $ lastfooditem = 0
    $ stuffed = 1
    if katrinestage4event == 0 and katrine.stage <= 6:
        image katrine_home_beforefeeding = "/katrine/[katrine.stage]/home_beforefeeding.webp"
        scene katrine_home_beforefeeding
        katrine "Oooh, some food foreplay. Yes please!"
        show screen katrinefullness
        call katrine_home_feeding from _call_katrine_home_feeding
        pause
        $ katrine.weight += (katrine.fullness / 3)
        $ katrine.fullness = 0
        hide screen katrinefullness
        pause

    elif katrine.stage >= 8:
        image katrine_home_beforefeeding = "/katrine/[katrine.stage]/home_beforefeeding.webp"
        scene katrine_home_beforefeeding
        katrine "Oooh, some food foreplay. Yes please!"
        show screen katrinefullness
        call katrine_home_feeding from _call_katrine_home_feeding_1
        pause
        $ katrine.weight += (katrine.fullness / 3)
        $ katrine.fullness = 0
        hide screen katrinefullness
        pause

    if stuffed == 3:
        window hide
        image katrine_home_afterfeeding = "/katrine/[katrine.stage]/home_afterfeeding.webp"
        scene katrine_home_afterfeeding
        $ stuffed = 0
        $ bellyrub = 1
        pc "You're so damn cute."
        katrine "Why?"
        pc "You look like the birthday girl who tried to finish her cake."
        image katrine_home_stuffedsex1 = "/katrine/[katrine.stage]/home_stuffedsex1.webp"
        scene katrine_home_stuffedsex1
        katrine "No, I'm the birthday girl who {i}did{/i} finish all her cake!"
        katrine "And I can't believe you're into this as much as I am."
        pc "What can I say?"
        if persistent.nosexscene == True:
            scene black
            "You and Katrine had a wonderful time together."
            "You clean up the place and kiss Katrine good night before going home."

            return
        katrine "Now it's your turn to eat!"
        if katrine.stage <= 7:
            pc "What about-"
            katrine "Don't worry about my stockings, just rip them open."
        image katrine_home_stuffedsex2 = "/katrine/[katrine.stage]/home_stuffedsex2.webp"
        scene katrine_home_stuffedsex2
        if katrine.stage <= 7:
            "You rip open her stockings to reveal your own meal."
        window hide
        pause
        pc "Wow, you're soaking."
        katrine "Everything about today has turned me on."
        katrine "Especially you."
        image katrine_home_stuffedsex3 = "/katrine/[katrine.stage]/home_stuffedsex3.webp"
        scene katrine_home_stuffedsex3
        window hide
        pause
        katrine "Ohhhh you're so good at that!"
        if katrine.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/4/home_stuffedsex3_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/5/home_stuffedsex3_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/6/home_stuffedsex3_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/7/home_stuffedsex3_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/8/home_stuffedsex3_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/9/home_stuffedsex3_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/10/home_stuffedsex3_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/11/home_stuffedsex3_video.webm" loop
            show movie with dissolve
        window hide
        pause
        katrine "Ohhhh!"
        katrine "I'm close!"
        katrine "Oh, right there!"
        katrine "Right there-{w} OHHHHHH!"
        katrine "[playername]!!!!!"
        stop movie
        image katrine_home_stuffedsex4 = "/katrine/[katrine.stage]/home_stuffedsex4.webp"
        scene katrine_home_stuffedsex4
        window hide
        pause
        katrine "[playername]."
        pc "Yes?"
        katrine "Yes."
        image katrine_home_stuffedsex5 = "/katrine/[katrine.stage]/home_stuffedsex5.webp"
        scene katrine_home_stuffedsex5
        window hide
        pause
        katrine "Hi."
        pc "Hello there!"
        katrine "Guess what?"
        pc "Tell me."
        katrine "Lie down. {w}It's your turn."
        image katrine_home_stuffedsex6 = "/katrine/[katrine.stage]/home_stuffedsex6.webp"
        scene katrine_home_stuffedsex6
        window hide
        pause
        katrine "Oh, you're ready for me!"
        image katrine_home_stuffedsex7 = "/katrine/[katrine.stage]/home_stuffedsex7.webp"
        scene katrine_home_stuffedsex7
        window hide
        pause
        katrine "I was going to use my tits to get you started, but it looks like there's no need."
        pc "Aww."
        katrine "Would you like that?"
        pc "Very much."
        katrine "I'll remember that for next time."
        katrine "But right now-"
        image katrine_home_stuffedsex8 = "/katrine/[katrine.stage]/home_stuffedsex8.webp"
        scene katrine_home_stuffedsex8
        katrine "It's time for the main course!"
        window hide
        pause
        pc "I can't argue with that."
        katrine "In fact, that's what I am now, isn't it?"
        katrine "I'm no longer just a snack."
        pc "Damn right."
        if katrine.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/4/home_stuffedsex9.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Tell me, [playername]."
            katrine "Tell me what I am."
            pc "You are absolutely the main course!"
            pc "And if I'm lucky... {w}you'll also be dessert!"
            katrine "Oh, you're lucky alright."
            katrine "How does that feel?"
            pc "Amazing."
            katrine "I was hoping you'd say like an appetizer."
            katrine "Because..."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/4/home_stuffedsex10.webm" loop
            show movie with dissolve
            window hide
            pause
            pc "Fuck me!"
            katrine "You like that?"
            pc "Damn, woman!"
            pc "How did I get this lucky?"
            katrine "I'm just trying to return the favor."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/4/home_stuffedsex11.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Ohhh, you're going to finish me off twice!"
            pc "Is that all?"
            katrine "Naughty boy!"
            katrine "I can't have all the fun!"
            pc "That's not something you need to worry about."
            pc "Although... {w}I kind of wish you had a mirror in here so I could see your backside."
            katrine "Want me to spin around?"
            katrine "Reverse cowgirl isn't the easiest position, but I could try it."
            pc "No, I'd rather imagine it."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/4/home_stuffedsex12.webm" loop
            show movie with dissolve
        elif katrine.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/5/home_stuffedsex9.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Tell me, [playername]."
            katrine "Tell me what I am."
            pc "You are absolutely the main course!"
            pc "And if I'm lucky... {w}you'll also be dessert!"
            katrine "Oh, you're lucky alright."
            katrine "How does that feel?"
            pc "Amazing."
            katrine "I was hoping you'd say like an appetizer."
            katrine "Because..."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/5/home_stuffedsex10.webm" loop
            show movie with dissolve
            window hide
            pause
            pc "Fuck me!"
            katrine "You like that?"
            pc "Damn, woman!"
            pc "How did I get this lucky?"
            katrine "I'm just trying to return the favor."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/5/home_stuffedsex11.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Ohhh, you're going to finish me off twice!"
            pc "Is that all?"
            katrine "Naughty boy!"
            katrine "I can't have all the fun!"
            pc "That's not something you need to worry about."
            pc "Although... {w}I kind of wish you had a mirror in here so I could see your backside."
            katrine "Want me to spin around?"
            katrine "Reverse cowgirl isn't the easiest position, but I could try it."
            pc "No, I'd rather imagine it."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/5/home_stuffedsex12.webm" loop
            show movie with dissolve
        elif katrine.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/6/home_stuffedsex9.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Tell me, [playername]."
            katrine "Tell me what I am."
            pc "You are absolutely the main course!"
            pc "And if I'm lucky... {w}you'll also be dessert!"
            katrine "Oh, you're lucky alright."
            katrine "How does that feel?"
            pc "Amazing."
            katrine "I was hoping you'd say like an appetizer."
            katrine "Because..."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/6/home_stuffedsex10.webm" loop
            show movie with dissolve
            window hide
            pause
            pc "Fuck me!"
            katrine "You like that?"
            pc "Damn, woman!"
            pc "How did I get this lucky?"
            katrine "I'm just trying to return the favor."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/6/home_stuffedsex11.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Ohhh, you're going to finish me off twice!"
            pc "Is that all?"
            katrine "Naughty boy!"
            katrine "I can't have all the fun!"
            pc "That's not something you need to worry about."
            pc "Although... {w}I kind of wish you had a mirror in here so I could see your backside."
            katrine "Want me to spin around?"
            katrine "Reverse cowgirl isn't the easiest position, but I could try it."
            pc "No, I'd rather imagine it."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/6/home_stuffedsex12.webm" loop
            show movie with dissolve
        elif katrine.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/7/home_stuffedsex9.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Tell me, [playername]."
            katrine "Tell me what I am."
            pc "You are absolutely the main course!"
            pc "And if I'm lucky... {w}you'll also be dessert!"
            katrine "Oh, you're lucky alright."
            katrine "How does that feel?"
            pc "Amazing."
            katrine "I was hoping you'd say like an appetizer."
            katrine "Because..."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/7/home_stuffedsex10.webm" loop
            show movie with dissolve
            window hide
            pause
            pc "Fuck me!"
            katrine "You like that?"
            pc "Damn, woman!"
            pc "How did I get this lucky?"
            katrine "I'm just trying to return the favor."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/7/home_stuffedsex11.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Ohhh, you're going to finish me off twice!"
            pc "Is that all?"
            katrine "Naughty boy!"
            katrine "I can't have all the fun!"
            pc "That's not something you need to worry about."
            pc "Although... {w}I kind of wish you had a mirror in here so I could see your backside."
            katrine "Want me to spin around?"
            katrine "Reverse cowgirl isn't the easiest position, but I could try it."
            pc "No, I'd rather imagine it."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/7/home_stuffedsex12.webm" loop
            show movie with dissolve
        elif katrine.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/8/home_stuffedsex9.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Tell me, [playername]."
            katrine "Tell me what I am."
            pc "You are absolutely the main course!"
            pc "And if I'm lucky... {w}you'll also be dessert!"
            katrine "Oh, you're lucky alright."
            katrine "How does that feel?"
            pc "Amazing."
            katrine "I was hoping you'd say like an appetizer."
            katrine "Because..."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/8/home_stuffedsex10.webm" loop
            show movie with dissolve
            window hide
            pause
            pc "Fuck me!"
            katrine "You like that?"
            pc "Damn, woman!"
            pc "How did I get this lucky?"
            katrine "I'm just trying to return the favor."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/8/home_stuffedsex11.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Ohhh, you're going to finish me off twice!"
            pc "Is that all?"
            katrine "Naughty boy!"
            katrine "I can't have all the fun!"
            pc "That's not something you need to worry about."
            pc "Although... {w}I kind of wish you had a mirror in here so I could see your backside."
            katrine "Want me to spin around?"
            katrine "Reverse cowgirl isn't the easiest position, but I could try it."
            pc "No, I'd rather imagine it."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/8/home_stuffedsex12.webm" loop
            show movie with dissolve
        elif katrine.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/9/home_stuffedsex9.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Tell me, [playername]."
            katrine "Tell me what I am."
            pc "You are absolutely the main course!"
            pc "And if I'm lucky... {w}you'll also be dessert!"
            katrine "Oh, you're lucky alright."
            katrine "How does that feel?"
            pc "Amazing."
            katrine "I was hoping you'd say like an appetizer."
            katrine "Because..."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/9/home_stuffedsex10.webm" loop
            show movie with dissolve
            window hide
            pause
            pc "Fuck me!"
            katrine "You like that?"
            pc "Damn, woman!"
            pc "How did I get this lucky?"
            katrine "I'm just trying to return the favor."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/9/home_stuffedsex11.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Ohhh, you're going to finish me off twice!"
            pc "Is that all?"
            katrine "Naughty boy!"
            katrine "I can't have all the fun!"
            pc "That's not something you need to worry about."
            pc "Although... {w}I kind of wish you had a mirror in here so I could see your backside."
            katrine "Want me to spin around?"
            katrine "Reverse cowgirl isn't the easiest position, but I could try it."
            pc "No, I'd rather imagine it."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/9/home_stuffedsex12.webm" loop
            show movie with dissolve
        elif katrine.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/10/home_stuffedsex9.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Tell me, [playername]."
            katrine "Tell me what I am."
            pc "You are absolutely the main course!"
            pc "And if I'm lucky... {w}you'll also be dessert!"
            katrine "Oh, you're lucky alright."
            katrine "How does that feel?"
            pc "Amazing."
            katrine "I was hoping you'd say like an appetizer."
            katrine "Because..."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/10/home_stuffedsex10.webm" loop
            show movie with dissolve
            window hide
            pause
            pc "Fuck me!"
            katrine "You like that?"
            pc "Damn, woman!"
            pc "How did I get this lucky?"
            katrine "I'm just trying to return the favor."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/10/home_stuffedsex11.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Ohhh, you're going to finish me off twice!"
            pc "Is that all?"
            katrine "Naughty boy!"
            katrine "I can't have all the fun!"
            pc "That's not something you need to worry about."
            pc "Although... {w}I kind of wish you had a mirror in here so I could see your backside."
            katrine "Want me to spin around?"
            katrine "Reverse cowgirl isn't the easiest position, but I could try it."
            pc "No, I'd rather imagine it."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/10/home_stuffedsex12.webm" loop
            show movie with dissolve
        elif katrine.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/11/home_stuffedsex10.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Tell me, [playername]."
            katrine "Tell me what I am."
            pc "You are absolutely the main course!"
            pc "And if I'm lucky... {w}you'll also be dessert!"
            katrine "Oh, you're lucky alright."
            katrine "How does that feel?"
            pc "Amazing."
            katrine "I was hoping you'd say like an appetizer."
            katrine "Because..."
            pc "Fuck me!"
            katrine "You like that?"
            pc "Damn, woman!"
            pc "How did I get this lucky?"
            katrine "I'm just trying to return the favor."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/11/home_stuffedsex11.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Ohhh, you're going to finish me off twice!"
            pc "Is that all?"
            katrine "Naughty boy!"
            katrine "I can't have all the fun!"
            pc "That's not something you need to worry about."
            pc "Although... {w}I kind of wish you had a mirror in here so I could see your backside."
            katrine "Want me to spin around?"
            katrine "Reverse cowgirl isn't the easiest position, but I could try it."
            pc "No, I'd rather imagine it."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/11/home_stuffedsex12.webm" loop
            show movie with dissolve
        window hide
        pause
        katrine "Ohhh! {w}Why's that?"
        katrine "Are you imagining it even bigger than it is?"
        pc "I saw it coming in here, and it was nothing to complain about."
        katrine "Yeah? {w}Was it big?"
        pc "That doesn't describe it."
        katrine "Was it huge?"
        pc "Getting closer."
        katrine "Well, it could get even bigger. {p}Would you like that?"
        pc "Mmm hmm!"
        katrine "What's that? {w}Uhh! {w}I didn't hear you!"
        pc "Yesss!"
        katrine "Tell me!"
        pc "YESSSS!"
        pc "I love your huge fat ass!"
        katrine "Ohhh! {w}Are you going to finish with me?"
        pc "FUCK!"
        katrine "YESSSSSSSSSSS!"
        window hide
        pause
        stop movie
        "You clean up the place and kiss Katrine goodbye before going home."
        return

    else:

        "Moving over you join Katrine on the bed."
        "Deciding to get straight to business you quickly undress, watched by Katrine's hungry gaze."
        image katrine_home_sex2 = "/katrine/[katrine.stage]/home_sex2.webp"
        scene katrine_home_sex2
        "Placing your hands on her body, Katrine gasps in pleasure."
        "Playing with her gently, you can hear her breathing getting quick and raspy."
        katrine "Mmm, you make me so horny."
        if katrine.stage >= 3:
            katrine "And so hungry too."
        elif katrine.stage == 8:
            katrine "Mmm, why do I always get hungry when we are about to have sex."
            pc "I do have some eclairs if you want them?"
            katrine "Don't tempt me, I'm supposed to be dieting..."
            katrine "They look so good though, I'm sure one wont do any damage...maybe two."
        else:
            katrine "But I can't have all the fun."
        $ stuffed = 0
        $ bellyrub = 1
        if persistent.nosexscene == True:
            scene black with dissolve
            "You and Katrine had a wonderful time together."
            "You clean up the place and kiss Katrine good night before going home."

            return
        pause
        if katrine.stage >= 3:
            image katrine_home_sex3 = "/katrine/[katrine.stage]/home_sex3.webp"
            scene katrine_home_sex3
            "Hearing her say that, you immediatly know what to do."
            "You grab a few eclairs and push them into her waiting mouth."
            katrine "You know how to spoil me."
            katrine "But I can't have all the fun."
        image katrine_home_sex5 = "/katrine/[katrine.stage]/home_sex5.webp"
        scene katrine_home_sex5
        "Standing up she returns the favour, grabbing your already hard cock."
        if katrine.stage == 2:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/2/home_sex5_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 3:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/3/home_sex5_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/4/home_sex5_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/5/home_sex5_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/6/home_sex5_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/7/home_sex5_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/8/home_sex5_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/9/home_sex5_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/10/home_sex5_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 11:
            "Instead of her usual handjob she starts with, she puts your dick into her gaping belly button."
            katrine "You know, I wondered if I had gotten fat enough to have you fuck my belly button."
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/11/home_sex5_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 12:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/12/home_sex5_video.webm" loop
            show movie with dissolve
        if katrine.stage <= 10:
            "As Katrine moves her soft hands along your cock, you can feel yourself approaching climax."
        elif katrine.stage >= 11:
            "She start to jiggle her belly around slightly to create friction between her belly button and your dick."
            katrine "It still is a bit small for this, but it works."
            pc "More reason to keep shoveling food into your greedy mouth."
        stop movie
        image katrine_home_sex4 = "/katrine/[katrine.stage]/home_sex4.webp"
        scene katrine_home_sex4
        "Pushing you over on the bed, it seems Katrine has had enough foreplay."
        image katrine_home_sex1 = "/katrine/[katrine.stage]/home_sex1.webp"
        scene katrine_home_sex1
        "Sliding herself onto you, you can feel how aroused she is."
        if katrine.stage == 2:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/2/home_sex1_video1.webm" loop
            show movie with dissolve
            katrine "Oh god, this feels amazing."
            "Thrusting into her, you feel her growing body bouncing on top of you."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/2/home_sex1_video2.webm" loop
            show movie with dissolve
            "Her new curves and fat only making it harder not to cum quickly."
            window hide
            pause
            katrine "Fuck, I'm getting close."
            katrine "Keep going, I want you to cum with me."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/2/home_sex1_video3.webm" loop
            show movie with dissolve
        elif katrine.stage == 3:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/3/home_sex1_video1.webm" loop
            show movie with dissolve
            katrine "Oh god, this feels amazing."
            "Thrusting into her, you feel her growing body bouncing on top of you."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/3/home_sex1_video2.webm" loop
            show movie with dissolve
            "Her new curves and fat only making it harder not to cum quickly."
            window hide
            pause
            katrine "Fuck, I'm getting close."
            katrine "Keep going, I want you to cum with me."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/3/home_sex1_video3.webm" loop
            show movie with dissolve
        elif katrine.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/4/home_sex1_video1.webm" loop
            show movie with dissolve
            katrine "Oh god, this feels amazing."
            "Thrusting into her, you feel her growing body bouncing on top of you."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/4/home_sex1_video2.webm" loop
            show movie with dissolve
            "Her new curves and fat only making it harder not to cum quickly."
            window hide
            pause
            katrine "Fuck, I'm getting close."
            katrine "Keep going, I want you to cum with me."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/4/home_sex1_video3.webm" loop
            show movie with dissolve
        elif katrine.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/5/home_sex1_video1.webm" loop
            show movie with dissolve
            katrine "Oh god, this feels amazing."
            "Thrusting into her, you feel her growing body bouncing on top of you."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/5/home_sex1_video2.webm" loop
            show movie with dissolve
            "Her new curves and fat only making it harder not to cum quickly."
            window hide
            pause
            katrine "Fuck, I'm getting close."
            katrine "Keep going, I want you to cum with me."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/5/home_sex1_video3.webm" loop
            show movie with dissolve
        elif katrine.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/6/home_sex1_video1.webm" loop
            show movie with dissolve
            katrine "Oh god, this feels amazing."
            "Thrusting into her, you feel her growing body bouncing on top of you."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/6/home_sex1_video2.webm" loop
            show movie with dissolve
            "Her new curves and fat only making it harder not to cum quickly."
            window hide
            pause
            katrine "Fuck, I'm getting close."
            katrine "Keep going, I want you to cum with me."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/6/home_sex1_video3.webm" loop
            show movie with dissolve
        elif katrine.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/7/home_sex1_video1.webm" loop
            show movie with dissolve
            katrine "Oh god, this feels amazing."
            "Thrusting into her, you feel her growing body bouncing on top of you."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/7/home_sex1_video2.webm" loop
            show movie with dissolve
            "Her new curves and fat only making it harder not to cum quickly."
            window hide
            pause
            katrine "Fuck, I'm getting close."
            katrine "Keep going, I want you to cum with me."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/7/home_sex1_video3.webm" loop
            show movie with dissolve
        elif katrine.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/8/home_sex1_video1.webm" loop
            show movie with dissolve
            katrine "Oh god, this feels amazing."
            "Thrusting into her, you feel her growing body bouncing on top of you."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/8/home_sex1_video2.webm" loop
            show movie with dissolve
            "Her new curves and fat only making it harder not to cum quickly."
            window hide
            pause
            katrine "Fuck, I'm getting close."
            katrine "Keep going, I want you to cum with me."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/8/home_sex1_video3.webm" loop
            show movie with dissolve
        elif katrine.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/9/home_sex1_video1.webm" loop
            show movie with dissolve
            katrine "Oh god, this feels amazing."
            "Thrusting into her, you feel her growing body bouncing on top of you."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/9/home_sex1_video2.webm" loop
            show movie with dissolve
            "Her new curves and fat only making it harder not to cum quickly."
            window hide
            pause
            katrine "Fuck, I'm getting close."
            katrine "Keep going, I want you to cum with me."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/9/home_sex1_video3.webm" loop
            show movie with dissolve
        elif katrine.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/10/home_sex1_video1.webm" loop
            show movie with dissolve
            katrine "Oh god, this feels amazing."
            "Thrusting into her, you feel her growing body bouncing on top of you."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/10/home_sex1_video2.webm" loop
            show movie with dissolve
            "Her new curves and fat only making it harder not to cum quickly."
            window hide
            pause
            katrine "Fuck, I'm getting close."
            katrine "Keep going, I want you to cum with me."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/10/home_sex1_video3.webm" loop
            show movie with dissolve
        elif katrine.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/11/home_sex1_video1.webm" loop
            show movie with dissolve
            katrine "Oh god, this feels amazing."
            "Thrusting into her, you feel her growing body bouncing on top of you."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/11/home_sex1_video2.webm" loop
            show movie with dissolve
            "Her new curves and fat only making it harder not to cum quickly."
            window hide
            pause
            katrine "Fuck, I'm getting close."
            katrine "Keep going, I want you to cum with me."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/11/home_sex1_video3.webm" loop
            show movie with dissolve
        elif katrine.stage == 12:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/12/home_sex1_video1.webm" loop
            show movie with dissolve
            katrine "Oh god, this feels amazing."
            "Thrusting into her, you feel her growing body bouncing on top of you."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/12/home_sex1_video2.webm" loop
            show movie with dissolve
            "Her new curves and fat only making it harder not to cum quickly."
            window hide
            pause
            katrine "Fuck, I'm getting close."
            katrine "Keep going, I want you to cum with me."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/12/home_sex1_video3.webm" loop
            show movie with dissolve
        window hide
        pause
        katrine "Yes, yes YES!"
        katrine "I’m cumming!"
        stop movie
        image katrine_home_aftersex = "/katrine/[katrine.stage]/home_aftersex.webp"
        scene katrine_home_aftersex
        "Falling back into her bed, you both enjoy the moment."
        katrine "That was great."
        "You clean up the place and kiss Katrine good night before going home."
        return
