label katrine_gym_1:
    #Temporary
    if katrine.stage >= 10:
        image katrine_gym_dumbel = "/katrine/[katrine.stage]/gym_dumbel.webp"
        scene katrine_gym_dumbel
        "Hey it's Katrine, she is working out with the weight sets."
        "You walk up to her."
        image katrine_gym_dumbel2 = "/katrine/[katrine.stage]/gym_dumbel2.webp"
        scene katrine_gym_dumbel2
        pc "Hey Katrine, how are you?"
        image katrine_gym_sitting = "/katrine/[katrine.stage]/gym_sitting.webp"
        scene katrine_gym_sitting
        katrine "Hey there, I'm doing well thanks."
        katrine "Want to work out together?"
        pc "Sure thing."
        "Moving over to the treadmill you start jogging together."
        image katrine_gym_running = "/katrine/[katrine.stage]/gym_running.webp"
        scene katrine_gym_running
        "Next to you Katrine looks like she is getting used to her heavier body, running at a slower pace but not forcing herself like she did before."
        "You keep up with the casual pace easily as you work out together."
        "You feel like your core muscles have gotten stronger from the run."
        $ strength += 1
        "Strength increased by one point."
        image katrine_gym_standing2 = "/katrine/[katrine.stage]/gym_standing2.webp"
        scene katrine_gym_standing2
        katrine "That really worked up a sweat. Can you grab me a drink?"
        pc "Sure thing."
        if trista.stage >= 10:
            image trista_gym_shop1 = "/trista/[trista.stage]/gym_shop1.webp"
            scene trista_gym_shop1
            pc "Hey, Trista. Can I get a large soda, please?"
            trista "Sure thing. Here you go."
            image trista_gym_shop2 = "/trista/[trista.stage]/gym_shop2.webp"
            scene trista_gym_shop2
        else:
            image trista_gym_shop = "/trista/[trista.stage]/gym_shop.webp"
            scene trista_gym_shop
            pc "Hey, Trista. Can I get a large soda, please?"
            trista "Sure thing. Here you go."
        pc "Thanks, Trista."
        trista "No problem."
        image katrine_gym_drink = "/katrine/[katrine.stage]/gym_drink.webp"
        scene katrine_gym_drink
        katrine "Thanks for the drink."
        if katrine.stage <= (trista.stage + 1):
            $ katrine.weight += 0.3
        katrine "I'm going to go take a shower. Thanks for the workout today."
        pc "No problem."
        "Going for a quick shower you make your way to the sauna afterwards."
        scene sauna
        play music "/music/sauna.ogg" if_changed
        "Thankfully it's empty, but after a few minutes you hear a knock on the door."
        image katrine_sauna_arrive = "/katrine/[katrine.stage]/sauna_arrive.webp"
        scene katrine_sauna_arrive
        katrine "Mind if I join you?"
        pc "Not at all."
        image katrine_sauna_sitting = "/katrine/[katrine.stage]/sauna_sitting.webp"
        scene katrine_sauna_sitting
        "Sitting down next to you, Katrine removes her towel."
        "You do your best not to stare, but it's hard not to look at her curves."
        katrine "Nice and hot in here, really helps my muscles after a tough workout."
        image katrine_sauna_stretch = "/katrine/[katrine.stage]/sauna_stretch.webp"
        scene katrine_sauna_stretch
        "As if to emphasise the point Katrine stretches out, giving you a good view of her naked body."
        "Catching you looking at her, Katrine smiles at you."
        image katrine_sauna_sitting2 = "/katrine/[katrine.stage]/sauna_sitting2.webp"
        scene katrine_sauna_sitting2
        katrine "Well I don't think it's fair if only one of us is naked."
        "Dropping your towel on the floor you repay Katrine the favour."
        "Sitting naked you enjoy each other's company for a while."
        pc "Think I'm going to head home, thanks for today Katrine."
        image katrine_sauna_standing = "/katrine/[katrine.stage]/sauna_standing.webp"
        scene katrine_sauna_standing
        katrine "Are you sure you want to do that?"
        katrine "It seems we have the place to ourselves..."
        image katrine_sauna_hug = "/katrine/[katrine.stage]/sauna_hug.webp"
        scene katrine_sauna_hug
        "Standing up Katrine approaches you, pressing her naked body against yours."
        pc "Maybe I could stay for a bit longer."
        image katrine_sauna_kiss = "/katrine/[katrine.stage]/sauna_kiss.webp"
        scene katrine_sauna_kiss
        katrine "My hero."
        if persistent.nosexscene == True:
            scene black with dissolve
            "Katrine and you have some fun together in the sauna."
            image katrine_sauna_aftersex = "/katrine/[katrine.stage]/sauna_aftersex.webp"
            scene katrine_sauna_aftersex
            pc "That felt great."
            katrine "Yes, the only thing that could make it better would be something sweet."
            if foodheld >= 1:
                menu:
                    "Give Katrine a bag of fattening sweets.":
                        pc "I might have something."
                        image katrine_sauna_beforeeat = "/katrine/[katrine.stage]/sauna_beforeeat.webp"
                        scene katrine_sauna_beforeeat
                        katrine "Really, I wouldn’t say no if you do."
                        image katrine_sauna_eat = "/katrine/[katrine.stage]/sauna_eat.webp"
                        scene katrine_sauna_eat
                        "Handing her the snack she enjoys the sweet treats."
                        $ foodheld -= 1
                        if katrine.stage <= (trista.stage + 1):
                            $ katrine.weight += 0.4
                        image katrine_sauna_sitting = "/katrine/[katrine.stage]/sauna_sitting.webp"
                        scene katrine_sauna_sitting
                        "Sitting around for another few minutes you decide to head home."
                        katrine "See ya around [playername]."
                        stop music fadeout 1.0
                        $ katrine_gym_today = 1
                        return
                    "Don't give Katrine a bag of fattening sweets.":
                        image katrine_sauna_sitting = "/katrine/[katrine.stage]/sauna_sitting.webp"
                        scene katrine_sauna_sitting
                        "Sitting around for another few minutes you decide to head home."
                        katrine "See ya around [playername]."
                        stop music fadeout 1.0
                        $ katrine_gym_today = 1
                        return
            else:
                image katrine_sauna_sitting = "/katrine/[katrine.stage]/sauna_sitting.webp"
                scene katrine_sauna_sitting
                "Sitting around for another few minutes you decide to head home."
                katrine "See ya around [playername]."
                stop music fadeout 1.0
                $ katrine_gym_today = 1
                return

        #[Sex scene starts here]
        image katrine_sauna_doggy = "/katrine/[katrine.stage]/sauna_doggy.webp"
        scene katrine_sauna_doggy
        window hide
        pause
        pc "Well that's just not fair."
        pc "What if we get caught?"
        pc "I don't want to get kicked out of this place."
        katrine "Stop teasing me!"
        image katrine_sauna_sex1 = "/katrine/[katrine.stage]/sauna_sex1.webp"
        scene katrine_sauna_sex1
        window hide
        pause
        pc "Alright, the quicker we finish, the less likely we get caught."
        katrine "We've never been caught!"
        pc "We have never been reported. {w}There's a difference!"
        if katrine.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/10/sauna_sex1_video.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Less talking, you're going to get tired!"
            pc "Oh, I can do this all day."
            katrine "Don't ruin the moment!"
            pc "What if I tell you how insanely sexy you look right now?"
            katrine "Uh! {w}I'm listening."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/10/sauna_sex2_video.webm" loop
            show movie with dissolve
            window hide
            pause
            pc "The way your booty shakes..."
            pc "All the work you're doing here is really paying off."
            katrine "Oh yeah?"
            pc "And I got to say, I really love being the one who gets to appreciate it."
            katrine "You're also- {w}uh!{w} -the one who helped sculpt this body!"
            katrine "But you'd rather that angle, huh?"
            pc "Why do you say that?"
            katrine "Because my front side is not nearly as toned."
            katrine "What are you-"
            pc "I'm flipping you over!"
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/10/sauna_sex3_video.webm" loop
            show movie with dissolve
        elif katrine.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/11/sauna_sex1_video.webm" loop
            show movie with dissolve
            window hide
            pause
            katrine "Less talking, you're going to get tired!"
            pc "Oh, I can do this all day."
            katrine "Don't ruin the moment!"
            pc "What if I tell you how insanely sexy you look right now?"
            katrine "Uh! {w}I'm listening."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/11/sauna_sex2_video.webm" loop
            show movie with dissolve
            window hide
            pause
            pc "The way your booty shakes..."
            pc "All the work you're doing here is really paying off."
            katrine "Oh yeah?"
            pc "And I got to say, I really love being the one who gets to appreciate it."
            katrine "You're also- {w}uh!{w} -the one who helped sculpt this body!"
            katrine "But you'd rather that angle, huh?"
            pc "Why do you say that?"
            katrine "Because my front side is not nearly as toned."
            katrine "What are you-"
            pc "I'm flipping you over!"
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/katrine/11/sauna_sex3_video.webm" loop
            show movie with dissolve
        #[Sex scene ends here]
        window hide
        pause
        "Flipping her over you get a better view of her growing belly move as you thrust into her."
        katrine "Why?"
        pc "Because this is my favorite view."
        katrine "But you can see my belly."
        pc "And I can look in your eyes."
        katrine "But you're staring at my tummy."
        pc "Yeah, I like that too."
        katrine "Do you like how big it is?"
        pc "I love it."
        katrine "Do you want it to be bigger?"
        pc "I wouldn't mind."
        katrine "Do you want me to stop working out?"
        pc "No, I love how toned you're getting."
        katrine "So...{w} you like me toned, and soft?"
        pc "Like a real woman.{w} You have every kind of curve."
        katrine "Curves on curves, that's me!"
        pc "Oh, fuck!"
        katrine "Are you going to-"
        pc "Yes!"
        katrine "Inside me!"
        window hide
        pause
        stop movie
        image katrine_sauna_aftersex = "/katrine/[katrine.stage]/sauna_aftersex.webp"
        scene katrine_sauna_aftersex
        katrine "That was amazing."
        pc "I can't believe no one walked in."
        katrine "That’s part of the thrill right."
        pc "I didn’t know you were into that sort of thing."
        katrine "There’s a lot you don’t know about what I’m into…"
        katrine "The only thing that could make this better would be if I had brought a snack with me."
        katrine "For some reason sex always makes me hungry."
        if foodheld >= 1:
            menu:
                "Give Katrine a bag of fattening sweets.":
                    pc "I might have something."
                    $ foodheld -= 1
                    image katrine_sauna_beforeeat = "/katrine/[katrine.stage]/sauna_beforeeat.webp"
                    scene katrine_sauna_beforeeat
                    katrine "I wouldn’t say no if you do."
                    image katrine_sauna_eat = "/katrine/[katrine.stage]/sauna_eat.webp"
                    scene katrine_sauna_eat
                    "Handing over the sweet treats Katrine leans back as she starts eating."
                    katrine "Ok, now this is perfect."
                    if katrine.stage <= (trista.stage + 1):
                        $ katrine.weight += 0.4
                    image katrine_sauna_sitting = "/katrine/[katrine.stage]/sauna_sitting.webp"
                    scene katrine_sauna_sitting
                    "Sitting around for another few minutes you decide to head home."
                    katrine "See ya around [playername]."
                    stop music fadeout 1.0
                    $ katrine_gym_today = 1
                    return
                "Don't give Katrine a bag of fattening sweets.":
                    image katrine_sauna_sitting = "/katrine/[katrine.stage]/sauna_sitting.webp"
                    scene katrine_sauna_sitting
                    "Sitting around for another few minutes you decide to head home."
                    katrine "See ya around [playername]."
                    stop music fadeout 1.0
                    $ katrine_gym_today = 1
                    return
        else:
            image katrine_sauna_sitting = "/katrine/[katrine.stage]/sauna_sitting.webp"
            scene katrine_sauna_sitting
            "Sitting around for another few minutes you decide to head home."
            katrine "See ya around [playername]."
            stop music fadeout 1.0
            $ katrine_gym_today = 1
            return


    ## Dumbbell lifting animation 1###
    image katrine_gym_weights = "/katrine/[katrine.stage]/gym_weights.webp"
    scene katrine_gym_weights
    if katrine.stage <= 6:
        "Walking into the gym you can see someone on the weights bench."
    elif katrine.stage >= 7:
        "Walking into the gym you can see someone lifting weights."
    "Looks like Katrine is working out today as well."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    if katrine.stage == 1:
        play movie "/images/katrine/1/gym_weights_vid1.webm" loop
    elif katrine.stage == 2:
        play movie "/images/katrine/2/gym_weights_vid1.webm" loop
    elif katrine.stage == 3:
        play movie "/images/katrine/3/gym_weights_vid1.webm" loop
    elif katrine.stage == 4:
        play movie "/images/katrine/4/gym_weights_vid1.webm" loop
    elif katrine.stage == 5:
        play movie "/images/katrine/5/gym_weights_vid1.webm" loop
    elif katrine.stage == 6:
        play movie "/images/katrine/6/gym_weights_vid1.webm" loop
    elif katrine.stage == 7:
        play movie "/images/katrine/7/gym_weights_vid1.webm" loop
    elif katrine.stage == 9:
        play movie "/images/katrine/9/gym_weights_vid1.webm" loop
    elif katrine.stage == 10:
        play movie "/images/katrine/10/gym_weights_vid1.webm" loop
    elif katrine.stage == 11:
        play movie "/images/katrine/11/gym_weights_vid1.webm" loop
    show movie with dissolve
    if katrine.stage <= 6:
        "Approaching her you can see her lifting the heavy dumbbell easily."
    elif katrine.stage >= 7:
        "Approaching her you can see her lifting two heavy dumbbells."
    if katrine.stage <= 4 or katrine.stage >= 9:
        pc "Hey Katrine, how are you?"
    if katrine.stage == 1:
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/1/gym_weights_vid4.webm" loop
        show movie with dissolve
        katrine "Oh, hey [playername]."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/1/gym_weights_vid2.webm" loop
        show movie with dissolve
        katrine "Just working on my arms, I still need to lose some fat on my body if I am going to hit my targets."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/1/gym_weights_vid3.webm" loop
        show movie with dissolve
        katrine "You want the bench?"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/1/gym_weights_vid5.webm" loop
        show movie with dissolve
        pc "No, I was actually wondering if you wanted to work out together?"
        stop movie
        image katrine_gym_sitting2 = "/katrine/[katrine.stage]/gym_sitting2.webp"
        scene katrine_gym_sitting2
        katrine "Oh, yeah that would be nice."
        katrine "I was about to move onto some Cardio if you want to join?"
    elif katrine.stage == 2:
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/2/gym_weights_vid4.webm" loop
        show movie with dissolve
        katrine "Hey, feeling good thanks."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/2/gym_weights_vid2.webm" loop
        show movie with dissolve
        katrine "Want to work out together again?"
        pc "Sure thing."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/2/gym_weights_vid3.webm" loop
        show movie with dissolve
        katrine "Great, let me finish up and why don’t we run together?"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/2/gym_weights_vid5.webm" loop
        show movie with dissolve
        "Continuing her reps, you can see her muscles tensing as she raises the heavy weights up and down."
        stop movie
        image katrine_gym_sitting2 = "/katrine/[katrine.stage]/gym_sitting2.webp"
        scene katrine_gym_sitting2
        katrine "That should do it, thanks for waiting."
    elif katrine.stage == 3 or katrine.stage == 4:
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if katrine.stage == 3:
            play movie "/images/katrine/3/gym_weights_vid4.webm" loop
        elif katrine.stage == 4:
            play movie "/images/katrine/4/gym_weights_vid4.webm" loop
        show movie with dissolve
        katrine "Hey there [playername]."
        katrine "Honestly, feeling kind of frustrated."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if katrine.stage == 3:
            play movie "/images/katrine/3/gym_weights_vid2.webm" loop
        elif katrine.stage == 4:
            play movie "/images/katrine/4/gym_weights_vid2.webm" loop
        show movie with dissolve
        pc "Frustrated?"
        katrine "Yeah, just feel like I keep missing my targets and like things are getting away from me."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if katrine.stage == 3:
            play movie "/images/katrine/3/gym_weights_vid3.webm" loop
        elif katrine.stage == 4:
            play movie "/images/katrine/4/gym_weights_vid3.webm" loop
        show movie with dissolve
        pc "I’m sorry to hear that."
        katrine "It’s not your fault, and nothing a good workout can’t fix."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if katrine.stage == 3:
            play movie "/images/katrine/3/gym_weights_vid5.webm" loop
        elif katrine.stage == 4:
            play movie "/images/katrine/4/gym_weights_vid5.webm" loop
        show movie with dissolve
        katrine "At least I can hit my targets here."
        stop movie
        image katrine_gym_sitting2 = "/katrine/[katrine.stage]/gym_sitting2.webp"
        scene katrine_gym_sitting2
        katrine "Fancy a quick jog?"
        pc "Sure thing."
    elif katrine.stage == 5 or katrine.stage == 6:
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if katrine.stage == 5:
            play movie "/images/katrine/5/gym_weights_vid4.webm" loop
        elif katrine.stage == 6:
            play movie "/images/katrine/6/gym_weights_vid4.webm" loop
        show movie with dissolve
        katrine "Hey [playername], ready for another workout?"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if katrine.stage == 5:
            play movie "/images/katrine/5/gym_weights_vid2.webm" loop
        elif katrine.stage == 6:
            play movie "/images/katrine/6/gym_weights_vid2.webm" loop
        show movie with dissolve
        pc "Would be a strange place to come if I wasn’t."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if katrine.stage == 5:
            play movie "/images/katrine/5/gym_weights_vid3.webm" loop
        elif katrine.stage == 6:
            play movie "/images/katrine/6/gym_weights_vid3.webm" loop
        show movie with dissolve
        katrine "Just finishing up my set if you want to workout together?"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if katrine.stage == 5:
            play movie "/images/katrine/5/gym_weights_vid5.webm" loop
        elif katrine.stage == 6:
            play movie "/images/katrine/6/gym_weights_vid5.webm" loop
        show movie with dissolve
        pc "Of course, always happy to workout with you."
        stop movie
        image katrine_gym_sitting2 = "/katrine/[katrine.stage]/gym_sitting2.webp"
        scene katrine_gym_sitting2
        katrine "Great, fancy some cardio?"
        pc "Sounds good to me."
    elif katrine.stage == 7:
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/7/gym_weights_vid3.webm" loop
        show movie with dissolve
        katrine "Hey there, how are you?"
        pc "I am good thanks, fancy another workout?"
        katrine "One step ahead of you."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/7/gym_weights_vid2.webm" loop
        show movie with dissolve
        katrine "I feel like I’ve been lacking in my efforts lately so just going to do a few more."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/7/gym_weights_vid5.webm" loop
        show movie with dissolve
        "Watching her lift the weights, you can see her arm muscles straining as she guides the weights past her growing figure."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/7/gym_weights_vid4.webm" loop
        show movie with dissolve
        window hide
        pause
        stop movie
        image katrine_gym_standing4 = "/katrine/[katrine.stage]/gym_standing4.webp"
        scene katrine_gym_standing4
        katrine "That should do."
        katrine "Fancy another run?"
        pc "Sounds good to me."
    elif katrine.stage == 9:
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/9/gym_weights_vid3.webm" loop
        show movie with dissolve
        katrine "Ughh!"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/9/gym_weights_vid2.webm" loop
        show movie with dissolve
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/9/gym_weights_vid5.webm" loop
        show movie with dissolve
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/9/gym_weights_vid4.webm" loop
        show movie with dissolve
        "Grunting, she completes a few more reps before dumping the weights on the floor."
        stop movie
        image katrine_gym_standing4 = "/katrine/[katrine.stage]/gym_standing4.webp"
        scene katrine_gym_standing4
        pc "Are you ok?"
        katrine "Phew, sorry about that."
        image katrine_gym_sitting2 = "/katrine/[katrine.stage]/gym_sitting2.webp"
        scene katrine_gym_sitting2
        "Sitting down on the bench, Katrine takes a moment to recover."
        katrine "I have really been struggling to get back to where I was."
        katrine "All that time away from the gym has hit me hard."
        pc "Don’t push yourself too hard, don’t want to cause an injury."
        image katrine_gym_sitting3 = "/katrine/[katrine.stage]/gym_sitting3.webp"
        scene katrine_gym_sitting3
        katrine "I know, it’s just a bit frustrating."
        katrine "Right, no time to sit here feeling sorry for myself."
        katrine "I was about to go for a run if you want to join?"
        pc "Sure thing."
    elif katrine.stage >= 10:
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if katrine.stage == 10:
            play movie "/images/katrine/10/gym_weights_vid3.webm" loop
        elif katrine.stage == 11:
            play movie "/images/katrine/11/gym_weights_vid3.webm" loop
        show movie with dissolve
        katrine "Feeling good thanks."
        katrine "Just about to move to the treadmill if you want to join?"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if katrine.stage == 10:
            play movie "/images/katrine/10/gym_weights_vid2.webm" loop
        elif katrine.stage == 11:
            play movie "/images/katrine/11/gym_weights_vid2.webm" loop
        show movie with dissolve
        pc "Yeah, that would be great."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if katrine.stage == 10:
            play movie "/images/katrine/10/gym_weights_vid5.webm" loop
        elif katrine.stage == 11:
            play movie "/images/katrine/11/gym_weights_vid5.webm" loop
        show movie with dissolve
        katrine "Cool, just want to do a couple more."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if katrine.stage == 10:
            play movie "/images/katrine/10/gym_weights_vid4.webm" loop
        elif katrine.stage == 11:
            play movie "/images/katrine/11/gym_weights_vid4.webm" loop
        show movie with dissolve
        "Watching her lift the weights, you can see her arm muscles straining as she guides the weights past her growing figure."
        stop movie
        image katrine_gym_standing4 = "/katrine/[katrine.stage]/gym_standing4.webp"
        scene katrine_gym_standing4
        katrine "That should do."

    ##On treadmills##
    image katrine_gym_running2 = "/katrine/[katrine.stage]/gym_running2.webp"
    scene katrine_gym_running2
    "Moving over to the Treadmill you start jogging together."
    if katrine.stage == 1:
        "Katrine makes it look easy, but you manage to do a reasonable job of keeping up with her."
    elif katrine.stage == 2:
        "Next to you Katrine makes it look easy, but you manage to do a decent job."
    elif katrine.stage == 3 or katrine.stage == 4:
        "Katrine makes it look easy, but you manage to do a good job."
    elif katrine.stage == 5 or katrine.stage == 6:
        "The brunette usually out paces you, but today you seem to be setting a similar time and speed."
        "Maybe she was taking it easier than usual, or maybe all those burgers were finally catching up with her workouts."
        image katrine_gym_running3 = "/katrine/[katrine.stage]/gym_running3.webp"
        scene katrine_gym_running3
        "It was hard to ignore the extra wobble in her legs, belly and arms."
    elif katrine.stage == 7:
        "The brunette usually out paces you, but lately her speed has been dropping."
        image katrine_gym_running3 = "/katrine/[katrine.stage]/gym_running3.webp"
        scene katrine_gym_running3
        "Her once toned and muscular frame is now significantly larger."
        image katrine_gym_running4 = "/katrine/[katrine.stage]/gym_running4.webp"
        scene katrine_gym_running4
        "The extra wobble in her legs, belly and arms gives you plenty to look at."
    elif katrine.stage == 9:
        image katrine_gym_running3 = "/katrine/[katrine.stage]/gym_running3.webp"
        scene katrine_gym_running3
        "Next to you Katrine tries to set off at her old pace, but it doesn’t take long for her to be forced to slow the treadmill down."
        image katrine_gym_running4 = "/katrine/[katrine.stage]/gym_running4.webp"
        scene katrine_gym_running4
        pause
        image katrine_gym_running5 = "/katrine/[katrine.stage]/gym_running5.webp"
        scene katrine_gym_running5
        "Breathing heavily, she looks tired after just a few minutes."
        image katrine_gym_running6 = "/katrine/[katrine.stage]/gym_running6.webp"
        scene katrine_gym_running6
        "Her large body bouncing around and causing her some trouble as she keeps running."
        "You keep up with her pace easily as you work out together."
    elif katrine.stage >= 10:
        "Unlike previous attempts it seems Katrine is starting off slower today."
        image katrine_gym_running3 = "/katrine/[katrine.stage]/gym_running3.webp"
        scene katrine_gym_running3
        "Maybe she has finally come to terms with her bigger body and isn’t forcing it to keep up with her old workouts."
        image katrine_gym_running4 = "/katrine/[katrine.stage]/gym_running4.webp"
        scene katrine_gym_running4
        "She definitely seems a lot happier and less exhausted today."

    "You feel like your core muscles have gotten stronger from the run."
    call strengthup from _call_strengthup

    image katrine_gym_standing = "/katrine/[katrine.stage]/gym_standing.webp"
    scene katrine_gym_standing
    if katrine.stage <= 8:
        katrine "That really worked up a sweat. Can you grab me a drink?"
        pc "Sure thing."
    elif katrine.stage == 9:
        katrine "Oooh, my legs feel like jelly."
        katrine "I just need a minute."
        pc "Want me to get you a drink?"
        katrine "That would be great, thanks."
    elif katrine.stage >= 10:
        katrine "That was fun, thank you."
        pc "No need to thank me, I always enjoy our workouts."
        katrine "Oh, I am sure you do."
        image katrine_gym_sexy1 = "/katrine/[katrine.stage]/gym_sexy1.webp"
        scene katrine_gym_sexy1
        katrine "Maybe it’s more than the workout, maybe it’s what we get up to afterwards."
        image katrine_gym_sexy2 = "/katrine/[katrine.stage]/gym_sexy2.webp"
        scene katrine_gym_sexy2
        katrine "Or could it be, you like seeing my growing body pushed to its limits?"
        pc "I….uh."
        #PIC NEEDED
        "Smiling at you, Katrine walks past towards the counter."
        #PIC NEEDED
        "Going behind the counter she grabs a few extra-large sodas."
        katrine "Working out makes me so thirsty…"
        #PIC NEEDED
        "Picking up the first drink Katrine sucks it down in one go."
        #PIC NEEDED
        "Grabbing another she continues to drink, her stomach growing with each passing second."
        #PIC NEEDED
        "A third and fourth follow, her belly bloating out more and more."
        #PIC NEEDED
        "Her chubby stomach pushing out against her restrictive clothing as she forced the soda in."
        #PIC NEEDED
        "With a final effort she empties the fifth giant cup, leaving her looking massively bloated."
        #PIC NEEDED
        katrine "Uuurp!"
        #PIC NEEDED
        katrine "Excuse me."
        #PIC NEEDED
        "Gently slapping her taut stomach, it sounds as tight as a drum inside her."

        ###Katrine back close to you.”###
        katrine "Did you enjoy that?"
        pc "You look amazing."
        katrine "Oh yeah, you haven’t seen anything yet."
        "Leaning in close to you, you can feel her giant and solid stomach pressing against you."
        ###pov shot looking down at her belly between you.###
        "Looking down your amazed at its size, almost bursting out of her clothes."
        katrine "Why don’t we go somewhere more private and maybe I’ll let you enjoy this thing."
        "Grabbing your hand Katrine leads you away to the Sauna."

    if katrine.stage <= 9:
        if trista.stage >= 10:
            image trista_gym_shop1 = "/trista/[trista.stage]/gym_shop1.webp"
            scene trista_gym_shop1
            pc "Hey, Trista. Can I get a large soda, please?"
            trista "Sure thing. Here you go."
            image trista_gym_shop2 = "/trista/[trista.stage]/gym_shop2.webp"
            scene trista_gym_shop2
        else:
            image trista_gym_shop = "/trista/[trista.stage]/gym_shop.webp"
            scene trista_gym_shop
            pc "Hey, Trista. Can I get a large soda, please?"
            trista "Sure thing. Here you go."
        pc "Thanks, Trista."
        trista "No problem."
        image katrine_gym_drink = "/katrine/[katrine.stage]/gym_drink.webp"
        scene katrine_gym_drink
    if katrine.stage == 1:
        katrine "Thanks for the drink."
        image katrine_gym_standing3 = "/katrine/[katrine.stage]/gym_standing3.webp"
        scene katrine_gym_standing3
        katrine "That is me done for the day."
    elif katrine.stage >= 2 and katrine.stage <= 6:
        katrine "Thanks, really worked up a thirst."
        katrine "I should know better by now, but it just always slips my mind."
        katrine "Guess I just got too focused on working out."
        pc "Don’t worry about it."
        image katrine_gym_standing2 = "/katrine/[katrine.stage]/gym_standing2.webp"
        scene katrine_gym_standing2
        katrine "Sadly I think that is all I have time for today."
    elif katrine.stage == 7 or katrine.stage == 9:
        if katrine.stage == 7:
            katrine "Thanks, I really worked up a thirst."
            image katrine_gym_drink2 = "/katrine/[katrine.stage]/gym_drink2.webp"
            scene katrine_gym_drink2
            katrine "Speaking of, I need to get going shortly."
        elif katrine.stage == 9:
            katrine "Thanks for the drink."
            image katrine_gym_drink2 = "/katrine/[katrine.stage]/gym_drink2.webp"
            scene katrine_gym_drink2
            katrine "Think I am going to call it a day."
        katrine "But maybe I’ll pay another visit to the Sauna first, if you want to join?"
        katrine "Who knows what might happen."
        "Walking away from you, Katrine gives you a look over her shoulder."


    if katrine.stage <= 9:
        if katrine.stage <= (trista.stage + 1):
            $ katrine.weight += 0.2
    elif katrine.stage >= 10:
        if katrine.stage <= (trista.stage + 1):
            $ katrine.weight += 0.5

    if katrine.stage <= 6:
        katrine "I'm going to go take a shower. Thanks for the workout today."

    if katrine.stage == 1:
        pc "See ya later Katrine."
        "You have a nice cold shower and head home."
        stop music fadeout 1.0
        $ katrine_gym_today = 1
        return
    elif katrine.stage >= 2 and katrine.stage <= 6:
        pc "No problem."
        "Going for a quick shower you make your way to the sauna afterwards."
        scene sauna
        play music "/music/sauna.ogg" if_changed
        "Thankfully it's empty, but after a few minutes you hear a knock on the door."
        image katrine_sauna_arrive = "/katrine/[katrine.stage]/sauna_arrive.webp"
        scene katrine_sauna_arrive
        katrine "Mind if I join you?"
        pc "Not at all."
        image katrine_sauna_sitting = "/katrine/[katrine.stage]/sauna_sitting.webp"
        scene katrine_sauna_sitting
        "Sitting down next to you, Katrine removes her towel."
        if katrine.stage == 2 or katrine.stage == 3 or katrine.stage == 4:
            "You do your best not to stare, but it's hard not to look at her curves."
        if katrine.stage == 2:
            image katrine_sauna_sitting2 = "/katrine/[katrine.stage]/sauna_sitting2.webp"
            scene katrine_sauna_sitting2
            katrine "Nice and hot in here, really helps my muscles after a tough workout."
            pc "Yeah, it's good to relax after a workout."
            "You both relax in the sauna for a while before you decide to leave."
            pc "I better get going, nice to see you Katrine."
            katrine "See ya [playername]."
            stop music fadeout 1.0
            $ katrine_gym_today = 1
            return
        elif katrine.stage >= 3 and katrine.stage <= 6:
            image katrine_sauna_stretch = "/katrine/[katrine.stage]/sauna_stretch.webp"
            scene katrine_sauna_stretch
            if katrine.stage == 3 or katrine.stage == 4:
                katrine "I’m so glad Trista has this place, the heat really makes me feel good and relaxed after an intense workout."
                "As if to emphasise the point Katrine stretches out, giving you a good view of her naked body."
            elif katrine.stage == 5 or katrine.stage == 6:
                "Looking over her glistening body, you can really appreciate her weight gain."
                "The extra curves in all the right places."
            "Catching you looking at her, Katrine smiles at you."
            image katrine_sauna_sitting2 = "/katrine/[katrine.stage]/sauna_sitting2.webp"
            scene katrine_sauna_sitting2
            katrine "Well I don't think it's fair if only one of us is naked."
            if katrine.stage == 3 or katrine.stage == 4:
                "Dropping your towel on the floor you repay Katrine the favour."
                "Sitting naked you enjoy each other's company for a while."
                pc "Think I'm going to head home, thanks for today Katrine."
                image katrine_sauna_standing = "/katrine/[katrine.stage]/sauna_standing.webp"
                scene katrine_sauna_standing
                katrine "Are you sure you want to do that?"
                katrine "It seems we have the place to ourselves..."
                image katrine_sauna_hug = "/katrine/[katrine.stage]/sauna_hug.webp"
                scene katrine_sauna_hug
                "Standing up Katrine approaches you, pressing her naked body against yours."
                pc "Maybe I could stay for a bit longer."
                image katrine_sauna_kiss = "/katrine/[katrine.stage]/sauna_kiss.webp"
                scene katrine_sauna_kiss
                katrine "My hero."
            elif katrine.stage == 5 or katrine.stage == 6:
                image katrine_sauna_standing2 = "/katrine/[katrine.stage]/sauna_standing2.webp"
                scene katrine_sauna_standing2
                "Moving over to you, Katrine slowly takes off your towel."
                image katrine_sauna_standing3 = "/katrine/[katrine.stage]/sauna_standing3.webp"
                scene katrine_sauna_standing3
                katrine "That’s better."
                image katrine_sauna_sitting3 = "/katrine/[katrine.stage]/sauna_sitting3.webp"
                scene katrine_sauna_sitting3
                "Laying a hand on your thigh, she slowly explores your naked body."
                image katrine_sauna_sitting4 = "/katrine/[katrine.stage]/sauna_sitting4.webp"
                scene katrine_sauna_sitting4
                "Repaying the favour you explore her growing body, playing with her breasts and belly."
                image katrine_sauna_kiss = "/katrine/[katrine.stage]/sauna_kiss.webp"
                scene katrine_sauna_kiss
                "Leaning in, she kisses you passionately while pressing her hot body against yours."
            call katrine_sex_sauna from _call_katrine_sex_sauna
            stop music fadeout 1.0
            $ katrine_gym_today = 1
            return
        elif katrine.stage == 7 or katrine.stage == 9:
            scene sauna
            play music "/music/sauna.ogg" if_changed
            "Going for a very quick shower you head to find Katrine in the Sauna."
            "Walking in she gives you a smile."
            katrine "Glad you could make it, I’ve been so lonely."
            "Kissing you, she manoeuvres herself around you in the tight conditions."
            call katrine_sex_sauna from _call_katrine_sex_sauna_1
            stop music fadeout 1.0
            $ katrine_gym_today = 1
            return
        elif katrine.stage >= 10:
            scene sauna
            play music "/music/sauna.ogg" if_changed
            "Stepping into the Sauna Katrine locks it behind you."
            "Stripping out of her restrictive clothing allows you see really see her belly in all it’s glory."
            katrine "Well, what are you waiting for?"

            #[Sex scene]

            ###Potentially custom sex scene where you finish on her bloated stomach?###
            pc "That was amazing."
            katrine "Wow, better than usual."
            katrine "You are really into this aren’t you."
            pc "Guilty as charged."
            katrine "Well, I guess it’s a good think I enjoy it too now."
            katrine "Especially if I get to continue enjoying you like that as well."
            "Sitting around for another few minutes you decide to head home."
            katrine "As fun as that was, I better get going."
            katrine "Cya around [playername]"
            pc "Thanks Katrine, see you next time."
            $ katrine_gym_today = 1
            stop music fadeout 1.0
            return
        $ katrine_gym_today = 1
        stop music fadeout 1.0
        return
    $ katrine_gym_today = 1
    stop music fadeout 1.0
    return

label katrine_gym_2:
    image katrine_gym_running = "/katrine/[katrine.stage]/gym_running.webp"
    scene katrine_gym_running
    "Walking into the gym you can see someone on the treadmill."
    "Looks like Katrine is working out today as well."
    if katrine.stage <= 6:
        "Approaching her you can see her pace slowing as she completes her run."
    elif katrine.stage == 7 or katrine.stage == 9:
        "Approaching her you can see her pace slowing as she completes her run, or maybe that was just her pace these days."
        if katrine.stage == 9:
            "The extra curves and layer of fat on her body throwing off her stride pattern."
            "Seemingly giving up, Katrine stops her run early and steps off the machine."
    elif katrine.stage >= 10:
        "Approaching you can see her lightly jogging along at her own pace."
    if katrine.stage <= 2 or katrine.stage == 5 or katrine.stage == 6:
        pc "Hey, Katrine. How are you?"
    elif katrine.stage == 3 or katrine.stage == 4 or katrine.stage == 7 or katrine.stage >= 9:
        pc "Hey, Katrine."

    if katrine.stage == 1:
        katrine "Hey [playername], I’m doing well thanks."
        image katrine_gym_standing2 = "/katrine/[katrine.stage]/gym_standing2.webp"
        scene katrine_gym_standing2
        katrine "Training hard to lose some of this extra weight."
        katrine "I'm glad you're here. Want to work out together?"
    elif katrine.stage == 2:
        image katrine_gym_standing3 = "/katrine/[katrine.stage]/gym_standing3.webp"
        scene katrine_gym_standing3
        katrine "Hey there yourself, I’m doing well thanks."
        katrine "Although I am still trying to lose these last few pounds."
        katrine "I was about to do some lifts if you want to join?"
    elif katrine.stage == 3 or katrine.stage == 4:
        katrine "Hey, one second, about to finish."
        image katrine_gym_standing3 = "/katrine/[katrine.stage]/gym_standing3.webp"
        scene katrine_gym_standing3
        katrine "I was just thinking I should find someone to spot for me, if you want to work out together?"
    elif katrine.stage == 5 or katrine.stage == 6:
        image katrine_gym_standing3 = "/katrine/[katrine.stage]/gym_standing3.webp"
        scene katrine_gym_standing3
        katrine "Hey, trying to make up for some missed gym sessions."
        katrine "Since you are here, want to work out together?"
    elif katrine.stage == 7:
        image katrine_gym_running = "/katrine/[katrine.stage]/gym_running.webp"
        scene katrine_gym_running
        katrine "Hey… sorry, can you just give me a moment."
        "It was unusual to hear her so out of breath, she was clearly working hard today."
        "After a few more moments she stops the treadmill, stepping off it and looking exhausted."
        image katrine_gym_standing2 = "/katrine/[katrine.stage]/gym_standing2.webp"
        scene katrine_gym_standing2
        katrine "Sorry about that."
        pc "Are you ok?"
        katrine "Yeah, I feel great, why?"
        pc "No reason, just checking."
        katrine "That’s kind, time for some weightlifting?"
    elif katrine.stage == 9:
        katrine "Hey, how are you doing?"
        pc "I’m good thanks, you?"
        katrine "Struggling, to be honest."
        pc "Is everything ok?"
        katrine "No, I can’t lose this weight."
        katrine "I swear, I work out for hours and then step on the scales and my weight has gone up, not down!"
        pc "Maybe its muscle, like what Trista is doing?"
        katrine "I actually hadn’t thought about that."
        katrine "But look at me, it doesn’t look like muscle, it looks like fat and a lot of it."
        pc "You look amazing."
        katrine "You would say that, but thanks."
        katrine "Since you are here, want to work out together?"
    elif katrine.stage >= 10:
        katrine "Hey [playername], ready for another workout?"
        pc "You sound happy, and yeah sure thing."
        katrine "Yeah, I have been feeling a lot less stressed."
        "Finishing her jog she steps off looking more relaxed than you had seen her lately."
        image katrine_gym_standing3 = "/katrine/[katrine.stage]/gym_standing3.webp"
        scene katrine_gym_standing3
        katrine "Mind helping me with some weights work?"
    pc "Sure thing."
    "Moving over to the weights she spots for you first."
    image katrine_gym_benchpress = "/katrine/[katrine.stage]/gym_benchpress.webp"
    scene katrine_gym_benchpress

    if katrine.stage <= 4:
        ##[Thinking the next line could depend on strength level, with a good, average and bad result]
        ###Bad###
        if strength <= 12:
            "You just about manage to lift the weights, Katrine has to do a lot of the work for you though."
            katrine "I think you might need a bit more practice, but keep going and you will be as strong as me in no time."

        ####Average###
        elif strength >= 13 and strength <= 24:
            "It takes a bit of effort but you manage to do your full routine."
            katrine "Nice form, you look like a natural."

        ###Good###
        elif strength >= 25:
            "You lift the weights with no issues. Katrine is clearly impressed with your strength."
            katrine "You made that look easy. You're stronger than you look."

        call strengthup from _call_strengthup_1
    elif katrine.stage == 5 or katrine.stage == 6:
        "Lifting the weights up, you manage to complete your set easily."
        "All this work at the gym is clearly paying off."
        call strengthup from _call_strengthup_2
        katrine "You made that look easy, I don’t think you even need me here."
        pc "Even if I don’t need you, I still want you."
        katrine "Thanks, I really do like working out together."
        pc "Same, so I think it’s your turn if you want a go?"
    elif katrine.stage == 7:
        "You easily lift the weights, all the time you have spent here working with Trista has really paid off."
        katrine "You are a lot stronger than when we started, it's impressive."
        katrine "Maybe you should use a heavier weight?"
        call strengthup from _call_strengthup_3
    elif katrine.stage == 9:
        "You easily lift the weights while trying not to be too distracted by Katrine."
        call strengthup from _call_strengthup_4
    elif katrine.stage >= 10:
        "You easily lift the weights, it’s like second nature at this point."
        call strengthup from _call_strengthup_5

    "Wiping down the bench Katrine takes your place as you spot for her."
    image katrine_gym_benchpress2 = "/katrine/[katrine.stage]/gym_benchpress2.webp"
    scene katrine_gym_benchpress2
    if katrine.stage <= 6:
        "Placing your hand under the bar you help take some of the weight as she does her set."

    if katrine.stage <= 2 or katrine.stage == 5 or katrine.stage == 6:
        "She quickly finishes up her routine."
    elif katrine.stage == 3 or katrine.stage == 4:
        "For the first time it feels like you are helping, or maybe you just have the confidence that you can if you need too."
        "Doing a few more reps, Katrine quickly finishes up her routine."
    elif katrine.stage == 7:
        "It's clear her over indulgence and less gym time are having an impact on her."
        "Placing your hand under the bar you take a fair share of the weight as she does her set."
    elif katrine.stage == 9:
        "Lifting the weights is a bit of a struggle for Katrine."
        "Her overindulgence is clearly impacting her, although she can still lift more than you did when you first started."
        "Placing your hand under the bar you take a fair share of the weight as she does her set."
    elif katrine.stage >= 10:
        "She seems to be using a slightly lighter weight today and doesn’t need your help."
        "Raising the bar into the air she completes her set easily."

    image katrine_gym_standing3 = "/katrine/[katrine.stage]/gym_standing3.webp"
    scene katrine_gym_standing3
    katrine "Thanks, you are a good partner."
    if katrine.stage == 1:
        pc "I didn't do anything special. Happy to help you work out whenever though."
    elif katrine.stage == 2:
        pc "I didn't do anything special, happy to help."
    elif katrine.stage == 3 or katrine.stage == 4:
        pc "I didn't do anything special."
    elif katrine.stage == 5 or katrine.stage == 6:
        pc "Happy to help."
        katrine "Why don’t I reward you, I was about to head to bunny bites if you want to join?"
        katrine "My treat for looking out for me."
    elif katrine.stage == 7 or katrine.stage >= 10:
        pc "I didn't do anything special, happy to help you work out as always."
        katrine "Are you hungry, I could do with a bite to eat."
        "You hadn’t intended to cut your workout so short, but why not."
        pc "Now that you mention it, I could eat too."
    elif katrine.stage == 9:
        pc "No problem, happy to help you work out as always."
        pc "If that’s the end of your routine, fancy going out to eat?"
        katrine "I would, but I still have a lot of work to do if I want to beat Trista and lose this weight."
        katrine "Maybe another time?"
        pc "Sure thing."
        image katrine_gym_running = "/katrine/[katrine.stage]/gym_running.webp"
        scene katrine_gym_running
        "Watching Katrine get back on the treadmill she seems determined to keep going today."
        "Doing some simple stretches you watch her run for a few minutes before heading to the shower."
        $ katrine_gym_today = 1
        stop music fadeout 1.0
        return


    if katrine.stage <= 4:
        katrine "Well, I better get back to some more cardio if I want to lose this extra weight."
        pc "You look great to me, are you sure that is necessary?"
        image katrine_gym_standing = "/katrine/[katrine.stage]/gym_standing.webp"
        scene katrine_gym_standing
        katrine "I might not look fat, but I'm heavy as a stone."
        katrine "Try to carry me, you will see."
        image katrine_gym_carry = "/katrine/[katrine.stage]/gym_carry.webp"
        scene katrine_gym_carry
        "You move over to carry Katrine."
        katrine "Don’t worry about letting me fall if you can't carry me."
        "You try to carry Katrine."

        $ carry_weight = (strength * 1) + 70
        if katrine.weight > carry_weight:
            #If fail
            image katrine_gym_carry_fail = "/katrine/[katrine.stage]/gym_carry_fail.webp"
            scene katrine_gym_carry_fail
            "You fail to carry Katrine."
            katrine "As expected, I have been gaining too much weight lately."
            katrine "I really need to eat less and workout more."
            katrine "I'm going to do another few miles on the treadmill."
            image katrine_gym_running = "/katrine/[katrine.stage]/gym_running.webp"
            scene katrine_gym_running
            "Katrine leaves you to it and continues her workout alone."
            "Train up your strength to carry Katrine."
            $ katrine_gym_today = 1
            stop music fadeout 1.0
            return
        elif carry_weight >= katrine.weight:
            #If pass
            image katrine_gym_carry_success = "/katrine/[katrine.stage]/gym_carry_success.webp"
            scene katrine_gym_carry_success
            "You lift Katrine into the air in your arms."
            katrine "Wow, you are much stronger than you look."
            pc "Or maybe you are not as heavy as you think you are."
            image katrine_gym_standing2 = "/katrine/[katrine.stage]/gym_standing2.webp"
            scene katrine_gym_standing2
            katrine "Maybe you're right, I've been working out quite a lot lately."
            if katrine.stage <= 2:
                katrine "Fancy going out for a bite to eat? Working out always makes me hungry."
                pc "Sure thing, there is this great burger place in town."
                katrine "Sounds good to me."
            elif katrine.stage == 3 or katrine.stage == 4:
                katrine "Fancy going out for a bite to eat again?"
                katrine "I’ve been craving those burgers from Bunny bites."
                pc "Sure thing"
    "You follow Katrine to Bunny Bites."


    ###Bunny bites in booth with Marie at table/leaving###
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    play music "/music/bunny_bites.ogg" if_changed
    if katrine.stage <= 6:
        marie "Hi. Can I take your order?"
        katrine "Can I get three cheeseburgers and a milkshake, please?"
        pc "I’ll just have the one burger."
    elif katrine.stage == 7:
        marie "Hi. Can I take your order please?"
        katrine "Can I get a single cheeseburger and a milkshake please."
        pc "I’ll just have the one burger as well."
    elif katrine.stage >= 10:
        marie "Hi. Can I take your order please?"
        katrine "Can I get three burgers, some fries, onion rings and a milkshake please."
        pc "I’ll just have the one burger."
    marie "Sure, no problem. I'll bring your food out when it's ready."
    image katrine_cafe_aftergymboothtalk = "/katrine/[katrine.stage]/cafe_aftergymboothtalk.webp"
    scene katrine_cafe_aftergymboothtalk
    "You and Katrine make small talk for a few minutes until your food arrives."
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Here you go. Enjoy your meal."
    pc "Thanks, Marie."
    if katrine.stage >= 10:
        image katrine_cafe_aftergymfood1 = "/katrine/[katrine.stage]/cafe_aftergymfood1.webp"
        scene katrine_cafe_aftergymfood1
        "Beginning to place the plates down, the table is soon covered in more than you ordered."
        katrine "I don’t think this is our order."
        image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
        scene marie_serving2
        marie "Oh, I’m sorry about that."
        marie "The till has been acting weird today, that is our mistake."
        katrine "Don’t worry about it."
        marie "There is no charge, so feel free to eat as much as you want."
        image katrine_cafe_aftergymfood2 = "/katrine/[katrine.stage]/cafe_aftergymfood2.webp"
        scene katrine_cafe_aftergymfood2
        "Leaving you before Katrine can argue, you can see Katrine eagerly eyeing the food."
        katrine "I know I shouldn’t, but it all looks so good."
        katrine "Maybe just a few extra bites."
        image katrine_cafe_aftergymfood3 = "/katrine/[katrine.stage]/cafe_aftergymfood3.webp"
        scene katrine_cafe_aftergymfood3
        "Picking up her burger, Katrine bites into it and all thoughts of a few extra bites goes out the window."
        "With the veritable buffet in front of her, she quickly begins to stuff her face."
        image katrine_cafe_aftergymfood4 = "/katrine/[katrine.stage]/cafe_aftergymfood4.webp"
        scene katrine_cafe_aftergymfood4
        "Biting into her burger she grabs fries, onions rings and chicken nuggets with the other."
        "Stuffing them into her already full mouth with reckless abandonment."
        image katrine_cafe_aftergymfood5 = "/katrine/[katrine.stage]/cafe_aftergymfood5.webp"
        scene katrine_cafe_aftergymfood5
        "In a surprisingly short amount of time the table is empty."
        image katrine_cafe_aftergymfood6 = "/katrine/[katrine.stage]/cafe_aftergymfood6.webp"
        scene katrine_cafe_aftergymfood6
        "Katrines stomach is bulging and full."
        image katrine_cafe_aftergymfood7 = "/katrine/[katrine.stage]/cafe_aftergymfood7.webp"
        scene katrine_cafe_aftergymfood7
        katrine "I might have overdone that a little bit."
        katrine "Although I am sure you loved that."
        pc "That was kind of hot."
        "Smiling back at you it's clear Katrine takes that as a compliment."
        katrine "Oooh, I'm so full. But I really need to get back to do some work."
        image katrine_cafe_aftergymfood8 = "/katrine/[katrine.stage]/cafe_aftergymfood8.webp"
        scene katrine_cafe_aftergymfood8
        katrine "Sorry to leave but thank you for coming here and eating with me."
        pc "Anytime, I enjoyed it."
        image katrine_cafe_aftergymfood9 = "/katrine/[katrine.stage]/cafe_aftergymfood9.webp"
        scene katrine_cafe_aftergymfood9
        katrine "I'm sure you did."
        pc "See you later Katrine."
        stop music fadeout 1.0
        $ katrine_gym_today = 1
        if katrine.stage <= (trista.stage + 1):
            $ katrine.weight += 0.8
        $ daytime += 1
        stop music fadeout 1.0
        jump freetime


    image katrine_cafe_aftergymboothfood = "/katrine/[katrine.stage]/cafe_aftergymboothfood.webp"
    scene katrine_cafe_aftergymboothfood
    if katrine.stage <= 2 or katrine.stage == 5 or katrine.stage == 6:
        katrine "These burgers look great."
    elif katrine.stage == 3 or katrine.stage == 4:
        katrine "Mmm, they smell just as good as I remember."
    elif katrine.stage == 7:
        "Picking up her burger, Katrine looks a little disappointed at the size of her meal."
    image katrine_cafe_aftergymboothfoodeating = "/katrine/[katrine.stage]/cafe_aftergymboothfoodeating.webp"
    scene katrine_cafe_aftergymboothfoodeating
    if katrine.stage <= 6:
        "Picking up the first burger Katrine begins chomping through her burgers."
        "It doesn't take her long to finish all three and her drink."
    elif katrine.stage == 7:
        "It doesn't take her long to finish it and her drink."
    image katrine_cafe_aftergymboothtalk = "/katrine/[katrine.stage]/cafe_aftergymboothtalk.webp"
    scene katrine_cafe_aftergymboothtalk
    if katrine.stage <= 2:
        katrine "I really needed that. I have been holding out on eating like that all week, still trying to lose a bit of weight."
        pc "No need to starve yourself, you look great."
        image katrine_cafe_aftergymboothtalk2 = "/katrine/[katrine.stage]/cafe_aftergymboothtalk2.webp"
        scene katrine_cafe_aftergymboothtalk2
        katrine "Really?"
    elif katrine.stage == 3 or katrine.stage == 4:
        katrine "I really needed that."
        katrine "This final bit of weight just doesn’t want to leave me."
        katrine "I have been trying not to eat things like that, but sometimes it’s good to give into temptation."
        pc "It’s good to enjoy the little things in life."
        katrine "Definitely."
    elif katrine.stage == 5 or katrine.stage == 6:
        katrine "I really needed that, working out always gives me an appetite."
    elif katrine.stage == 7:
        pc "No need to starve yourself, you look great."
        katrine "Really?"
        katrine "No, I can't. But thank you for the support."

    if katrine.stage <= 4:
        katrine "Well, as long as you can carry me I won't starve myself."
    image katrine_cafe_aftergymleave = "/katrine/[katrine.stage]/cafe_aftergymleave.webp"
    scene katrine_cafe_aftergymleave
    if katrine.stage <= 6:
        katrine "But now I really need to get back to work. Thank you for coming here and eating with me."
    elif katrine.stage == 7:
        katrine "Sorry to leave but I really need to get back to work, thank you for coming here and eating with me."
    pc "Anytime. I enjoyed it."
    stop music fadeout 1.0
    $ katrine_gym_today = 1
    if katrine.stage == 7:
        if katrine.stage <= (trista.stage + 1):
            $ katrine.weight += 0.3
    else:
        if katrine.stage <= (trista.stage + 1):
            $ katrine.weight += 0.5
    $ daytime += 1
    stop music fadeout 1.0
    jump freetime

label katrine_date:

    if katrine.stage == 7:
        image katrine_stage7_event_44 = "/katrine/events/stage7/44.webp"
        scene katrine_stage7_event_44
        "Arriving at the café a little early, you spot Katrine already sitting in one of the booths."
        image katrine_date_talk = "/katrine/[katrine.stage]/date_talk.webp"
        scene katrine_date_talk
        pc "Hey, Katrine. You are here early."
        katrine "Yeah, sorry. Been avoiding Trista a bit. Realised there aren't many places I go other than the gym."
        pc "You don't need to avoid her, I'm sure she doesn't mean to be rude."
        katrine "I know. It's not just that though."
        pc "Want me to order you something?"
        image katrine_stage7_event_43 = "/katrine/events/stage7/43.webp"
        scene katrine_stage7_event_43
        katrine "No, it's okay. I'm good with just a coffee today."
        pc "You sure? My treat."
        katrine "Yeah, I'm sure. I could just use the company."
        image katrine_stage7_event_45 = "/katrine/events/stage7/45.webp"
        scene katrine_stage7_event_45
        "Making small talk for a while you are happy to see her starting to cheer up."
        "A little bit later you hear a noise coming from her stomach."
        katrine "Sorry. My stomach doesn't like dieting either."
        pc "You sure you don't want anything?"
        image katrine_stage7_event_42 = "/katrine/events/stage7/42.webp"
        scene katrine_stage7_event_42
        katrine "Maybe one wouldn’t hurt."
        "Going up to the counter you order Katrine one of her favourites and bring it back to her."
        image katrine_date_eat3 = "/katrine/[katrine.stage]/date_eat3.webp"
        scene katrine_date_eat3
        "Picking it up Katrine savours it as she eats it slowly, each bite careful to not lose a crumb."
        "Finishing it she looks happier already."
        image katrine_date_leave = "/katrine/[katrine.stage]/date_leave.webp"
        scene katrine_date_leave
        if katrine.stage <= (trista.stage + 1):
            $ katrine.weight += 0.5
        katrine "That was great, but why don't we get out of here?"
        pc "Sure thing."
        image katrine_date_takehome = "/katrine/[katrine.stage]/date_takehome.webp"
        scene katrine_date_takehome
        "Katrine holds you by the hand as she leads towards her apartment."

        ####Katrines apartment###
        image katrine_home_greet = "/katrine/[katrine.stage]/home_greet.webp"
        scene katrine_home_greet
        image katrine_home_hug = "/katrine/[katrine.stage]/home_hug.webp"
        scene katrine_home_hug
        "Walking in you take off your shoes and turn and pull her towards you, knowing what to expect by now from her."
        image katrine_home_kiss = "/katrine/[katrine.stage]/home_kiss.webp"
        scene katrine_home_kiss
        "Planting her lips on yours she leads you towards the bed."

        ##[Sex scene]
        call katrine_sex_home from _call_katrine_sex_home_3
        return

    scene date_cafe
    "Arriving at the cafe a little early, it doesn't look like Katrine is here yet."

    if katrine.stage <= 3:
        "You grab yourself one of the booths near the door."
    elif katrine.stage == 4:
        "That gives you time to put your plan into action. Going up to the counter you are familiar with Katrine's usual order."
        "This time you make sure to add a couple of extra pastries, the highest calorie ones including some oozing with full fat whipped cream."
        "Carrying the tray over to the table you wait for her to arrive."
    elif katrine.stage >= 5 and katrine.stage <= 7:
        "As has become the usual you head up and order Katrine her coffee and pastries, making sure to get her plenty of each."
        "Carrying the tray over to the table you wait for her to arrive."
    elif katrine.stage == 8:
        "Going up to the counter, you order Katrine a coffee and some pastries."
        "Carrying the tray over to the table, you wait for her to arrive."
    elif katrine.stage <= 10:
        "Going up to the counter, you order Katrine a coffee and a large pile of pastries."
        "Carrying the heavy tray over to the table, you wait for her to arrive."
    else:
        "Going up to the counter, you order Katrine her coffee and pastries, making sure to get her plenty."
        "Carrying the tray over to the table, you wait for her to arrive."

    if katrine.stage == 1:
        "A few minutes later you spot Katrine walking in, this is probably the first time you have seen her out of her gym wear."
    else:
        "A few minutes later you spot Katrine walking in."

    image katrine_date_arrive = "/katrine/[katrine.stage]/date_arrive.webp"
    scene katrine_date_arrive

    if katrine.stage == 1:
        pc "Hey, Katrine. You look nice."
        katrine "Thank you, I just about managed to find something that isn't just for the gym."
    elif katrine.stage <= 8:
        pc "Hey, Katrine. You look nice."
        if katrine.stage <= 3:
            katrine "Thank you. You look good yourself."
        elif katrine.stage == 4:
            katrine "Thank you. Sorry I'm late."
        elif katrine.stage >= 5:
            katrine "Thank you, so do you."
    elif katrine.stage == 9:
        pc "Hey, Katrine."
        katrine "Hey. Thanks for ordering - I'm famished."
    elif katrine.stage >= 10:
        pc "Hey, Katrine. You look nice."
        katrine "Thank you, so do you."

    image katrine_date_talk = "/katrine/[katrine.stage]/date_talk.webp"
    scene katrine_date_talk

    if katrine.stage <= 3:
        "You both get a coffee while waiting for the food, making small talk."
        "After a while the food arrives."
    elif katrine.stage == 4:
        pc "No problem. I thought I would get our order in while I waited."
        katrine "Thanks. That's so thoughtful."
        katrine "Oooh, these look good. Although, there are a lot today."
        pc "Sorry. I wasn't sure which ones you normally get, so I might have gone a little overboard."
        katrine "No problem. It's the thought that counts."
    elif katrine.stage == 5:
        pc "Thank you. I thought I would get our order in while I waited."
        katrine "Amazing! My stomach has been growling all the way over here."
    elif katrine.stage == 6:
        katrine "Amazing! You have read my mind with the pastries."
    elif katrine.stage == 8:
        pc "So, how have you been?"
        katrine "A little better. I have been distracting myself with work."
        katrine "Took an extra couple of shifts teaching at the library."
        pc "How is that going?"
    elif katrine.stage == 9:
        katrine "So, have you been up to much recently?"
        pc "Nothing major, working at the cafe, classes and a couple of extra things here and there."
        katrine "Do those things involve that nice lady from the chocolate shop?"
        pc "Bonnie? Yeah. I've been helping out in her shop."
    elif katrine.stage == 10:
        pc "So, how have you been?"
        katrine "Really good, it feels like my passion for writting has really come back recently."
        katrine "Ever since you got me to consider writing about food it's been so much more fun."
        pc "That's great to hear."
    else:
        katrine "Amazing! You have read my mind with the pastries."

    image katrine_date_eat1 = "/katrine/[katrine.stage]/date_eat1.webp"
    scene katrine_date_eat1

    if katrine.stage == 1:
        "Watching Katrine eat her pastries you chat about her work, the gym and other things she has been up to."
        pc "How is your work going?"
    elif katrine.stage == 2:
        "Watching Katrine eat her pastries you chat about her work, the gym and other things she has been up to."
        pc "How is that piece on the underground coming along?"
    elif katrine.stage == 3:
        "Watching Katrine eat her pastries you chat about her work, the gym and other things she has been up to."
        pc "Anything interesting going on with you?"
    elif katrine.stage == 4:
        "Picking up the first of the pastries you chat with her about her work, the gym and other things she has been up to."
    elif katrine.stage == 5:
        "Grabbing the first pastry Katrine begins to eat as you make small talk for a while."
        pc "Anything interesting going on with you?"
    elif katrine.stage == 6:
        "Grabbing the first one Katrine begins to eat as you make small talk for a while before it comes around to her job."
        pc "Anything interesting going on with you?"
    elif katrine.stage == 8:
        "Grabbing the first pastry Katrine takes a bite before continuing."
        katrine "It's going well. Some of the old folks are actually picking up a thing or two."
        katrine "Although Sue is still trying to set me up with her grandson."
        pc "Something I need to be worried about?"
    elif katrine.stage == 9:
        "Grabbing the first pastry Katrine takes a bite before continuing."
        katrine "So are you two a thing?"
        katrine "Don't worry, I'm pretty open-minded about things like that."
        pc "Uhh... Yeah, I guess we are. And you are okay with that?"
    elif katrine.stage == 10:
        "Grabbing the first pastry, Katrine takes a bite before continuing."
        katrine "I've already had a couple of people ask me for reviews."
        katrine "Only local takeaways, but it's a start."
    else:
        "Grabbing the first one, Katrine begins to eat as you make small talk for a while."

    image katrine_date_eat2 = "/katrine/[katrine.stage]/date_eat2.webp"
    scene katrine_date_eat2

    if katrine.stage == 1:
        katrine "It's going ok, freelance can be a bit difficult but I have a couple of emails I need to follow up on."
        katrine "Making the most of the extra time off to go to the gym."
        pc "Yeah, we should work out more together."
    elif katrine.stage == 2:
        katrine "Good, well it's a bit boring really."
        katrine "I keep finding myself snacking or finding things to eat instead of focusing on it."
        pc "Procrastination can be hard to avoid."
    elif katrine.stage == 3:
        katrine "Maybe. I have to pop by the library later."
        katrine "I'm supposed to be helping out teaching a writing class."
        pc "That sounds interesting."
        katrine "Yeah. It's good to meet new people too."
    elif katrine.stage == 4:
        "Despite the extra pastries, the table is cleared in no time at all."
    elif katrine.stage == 5:
        katrine "No. Still taking a bit of a break from writing."
        katrine "I have a couple of offers but nothing is peaking my interest."
    elif katrine.stage == 6:
        katrine "Yeah, that female fitness piece. The only trouble I'm having is where to start."
        katrine "There is so much potential it's almost overwhelming."
        pc "Well, they are lucky to have you."
        pc "Just write what you would want to read."
    elif katrine.stage == 8:
        katrine "Hardly. He has barely left school. Besides, I think she believes I made you up to avoid her questions."
        katrine "If she keeps it up, I might have to get you to join me to prove you exist."
        pc "I'd be happy to. Would be good to meet the famous Sue."
    elif katrine.stage == 9:
        katrine "Yeah. Why wouldn't I be? Nothing wrong with open relationships."
        pc "Ok, if you are sure. Maybe I can introduce you at some point."
    elif katrine.stage == 10:
        katrine "Plus, the free samples they have been sending over are worth the effort on their own."
        pc "It's good to see you enjoying your work again."
    else:
        "You manage to steal some glances at her stomach as she eats."

    image katrine_date_eat3 = "/katrine/[katrine.stage]/date_eat3.webp"
    scene katrine_date_eat3

    if katrine.stage == 1:
        katrine "Sure thing, I’d like that. But you need to get a bit faster before I can call you my gym buddy."
        "Katrine smiles at you after her joke, before looking surprised as she goes to grab another pastry."
    elif katrine.stage == 2:
        katrine "Especially living so close to this place, I swear I can smell these things from my apartment."
        pc "Maybe you can use them as motivation, a reward for getting writing done?"
        katrine "That's a great idea, it works for the gym."
    elif katrine.stage == 3:
        katrine "Although, a lot of them are old people. I think they are just lonely."
        katrine "There's this lady; Sue. I made the mistake of telling her I liked donuts."
        katrine "Now everytime I go, she turns up with a dozen for me and tells me I need more meat on my bones."
        pc "Sounds like a woman after my own heart."
        "Rolling her eyes Katrine smiles at your joke."
    elif katrine.stage == 4:
        "If anything the new sweet and creamy pastries only seemed to make her more interested in eating them."
    elif katrine.stage == 5:
        pc "You deserve a break."
        katrine "Thank you. It has definitely made me feel less stressed about everything."
    elif katrine.stage == 6:
        katrine "That's a good idea. It is my hobby too."
        katrine "Sometimes I overthink these things."
    elif katrine.stage == 8:
        katrine "I think she would like that."
        katrine "You two would get on like a house on fire."
    elif katrine.stage == 9:
        katrine "You starting a harem?"
        pc "I... uh..."
        katrine "Oh, calm down. I'm just joking. Or am I?"
    elif katrine.stage == 10:
        katrine "Yeah. It's been a major stress reliever."
        "Grabbing another pastry, Katrine continues to chat to you about her work for a while."
    else:
        "Now back to eating as much as she wants, her belly seems to grow each time you see her."
        #"Swallowing the last bite, Katrine wipes her lips clean."

    if katrinestory <= 4 and katrine.stage >= 10:
        menu:
            "Ask Katrine about herself.":
                "You decide to ask Katrine about herself."
                katrine "You want to know more about me?"
                katrine "Okay then, I would love to talk about myself."
                "Katrine talks a bit about herself."
                $ katrinestory += 1
                #Unlocks more Katrine story in the stats page.
                $ renpy.notify("New Katrine story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Katrine anything."
    elif katrinestory <= 3 and katrine.stage >= 8:
        menu:
            "Ask Katrine about herself.":
                "You decide to ask Katrine about herself."
                katrine "You want to know more about me?"
                katrine "Okay then, I would love to talk about myself."
                "Katrine talks a bit about herself."
                $ katrinestory += 1
                #Unlocks more Katrine story in the stats page.
                $ renpy.notify("New Katrine story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Katrine anything."
    elif katrinestory <= 2 and katrine.stage >= 6:
        menu:
            "Ask Katrine about herself.":
                "You decide to ask Katrine about herself."
                katrine "You want to know more about me?"
                katrine "Okay then, I would love to talk about myself."
                "Katrine talks a bit about herself."
                $ katrinestory += 1
                #Unlocks more Katrine story in the stats page.
                $ renpy.notify("New Katrine story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Katrine anything."
    elif katrinestory <= 1 and katrine.stage >= 4:
        menu:
            "Ask Katrine about herself.":
                "You decide to ask Katrine about herself."
                katrine "You want to know more about me?"
                katrine "Okay then, I would love to talk about myself."
                "Katrine talks a bit about herself."
                $ katrinestory += 1
                #Unlocks more Katrine story in the stats page.
                $ renpy.notify("New Katrine story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Katrine anything."
    elif katrinestory == 0 and katrine.stage >= 2:
        menu:
            "Ask Katrine about herself.":
                "You decide to ask Katrine about herself."
                katrine "You want to know more about me?"
                katrine "Okay then, I would love to talk about myself."
                "Katrine talks a bit about herself."
                $ katrinestory += 1
                #Unlocks more Katrine story in the stats page.
                $ renpy.notify("New Katrine story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Katrine anything."

    image katrine_date_eat_empty = "/katrine/[katrine.stage]/date_eat_empty.webp"
    scene katrine_date_eat_empty
    if katrine.stage <= (trista.stage + 1):
        $ katrine.weight += 0.8

    if katrine.stage == 1:
        katrine "Wow, I can't believe I ate all those."
        katrine "I was supposed to take some back with me for later."
        katrine "I hope you don’t mind me pigging out like that."
        pc "Not at all, I enjoyed our conversation."
    elif katrine.stage == 2:
        "Moving her hand back to the table for another baked good, she is surprised again to see it empty."
        katrine "Wow, did I really eat all those pastries already."
        katrine "I guess time flies when you are having fun."
        katrine "I might have to get some more to take back with me."
        pc "Don't want to work on an empty stomach."
        katrine "Yes, although I hope you don’t mind me pigging out like that again."
        pc "Not at all, I enjoyed our conversation."
    elif katrine.stage == 3:
        "But moving her hand back to the table for another baked good, she is surprised to see it empty."
        katrine "I always lose track of what I'm eating when I'm with you."
        katrine "I keep telling myself I need to take some back with me for later."
        katrine "Maybe I should start ordering them to go so I'm not tempted to eat them all."
        katrine "I do still feel bad about how much I stuff myself around you."
        katrine "Although I doubt we would have managed this many dates if you minded me eating like this."
        pc "You know I don't. I think it was one of the first things we talked about when we met."
    elif katrine.stage == 4:
        "Moving her hand back to the table for another baked good, only to find it empty."
        katrine "I guess I was hungrier than I thought."
        katrine "I was supposed to take some with me for later."
        katrine "Although I'm going back to the library to teach again tomorrow, so I'm sure Sue will have more donuts for me there."
        katrine "If I was the suspisious type, I'd be starting to wonder if the two of you are working together."
        pc "No. Although, that's not a bad idea."
        pc "I think I might have to pay the library a visit and look for donut delivering old ladies."
        katrine "I'm sure she would love you."
    elif katrine.stage == 5:
        katrine "Wow, that was even quicker than normal."
        katrine "I blame you. Your pastry choices are too good."
        katrine "Those new toffee cream eclairs you have been getting me are just too delicious to stop myself."
        katrine "I even had a dream about them yesterday."
        pc "Dreaming about pastries? Did they happen to include a certain someone?"
        katrine "No, just a never ending pile of delicious treats to stuff myself with."
        pc "I don't know whether to be insulted or not. Am I going to end up losing you to them?"
        katrine "Losing me to them? Please. You have already lost and it wasn't even close."
    elif katrine.stage == 6:
        "Moving her hand back to the table for another baked good, she finds it empty."
        katrine "Although that could be part of the problem."
        pc "What do you mean?"
        katrine "I've just been eating constantly. I guess it's a nervous habit."
        katrine "But it means I keep needing to go and buy more food and procrastinating from writing."
        katrine "Not that this is the first time. I really need to pay more attention to what I'm eating when I'm with you."
        pc "I’ll take that as a compliment."
    elif katrine.stage == 8:
        "Moving her hand back to the table for another baked good, she finds it empty."
        katrine "Especially if she knew how many treats you have been buying me."
        katrine "With all the extra sessions she has been feeding me all week."
        katrine "If I'm not careful they will have to roll me home by the time she is done with me."
        pc "I’m sure she is just being nice."
        katrine "Yeah. That's the problem. Very hard to say no to a sweet old lady like her."
    elif katrine.stage == 9:
        "Moving her hand back to the table for another baked good, she finds it empty."
        katrine "There I go again, stuffing my face without noticing."
    elif katrine.stage == 10:
        "Moving her hand back to the table for another baked good, she finds it empty."
        katrine "Mmm, those were good."
        katrine "I should do a review of this place sometime. I mean, I've eaten enough of their food to know how good it is."
        pc "That's a great idea. I'm sure they would appreciate it."
        katrine "Although, I don't want our go-to date café to become too popular so we can't get in."
    else:
        katrine "Wow. Those were amazing as always."

    image katrine_date_leave = "/katrine/[katrine.stage]/date_leave.webp"
    scene katrine_date_leave

    if katrine.stage == 1:
        katrine "Thanks, I had fun too but I should get back to it."
        katrine "Make sure you come and say hi next time you are at the gym."
        image katrine_date_bye = "/katrine/[katrine.stage]/date_bye.webp"
        scene katrine_date_bye
        "Waving goodbye to Katrine you head back home."
        return
    elif katrine.stage == 2:
        katrine "Thanks, I had fun too."
    elif katrine.stage == 3:
        katrine "I guess that's true. I should have taken that as a sign."
        katrine "It's nice to be able to enjoy myself without having to worry about that."
    elif katrine.stage == 4:
        katrine "Thanks. I had fun."
    elif katrine.stage == 5:
        katrine "But if you want a consolation prize, we could maybe head back to my place again?"
    elif katrine.stage == 6:
        katrine "You should, not many things win over food."
    elif katrine.stage == 8:
        katrine "Those were amazing as always."
        katrine "But now I fancy burning some of those pastries off in an equally fun way."
    elif katrine.stage == 9:
        katrine "But now I fancy burning some of those pastries off in an equally fun way."
    elif katrine.stage == 10:
        katrine "But now I fancy burning some of those pastries off in an equally fun way."
    else:
        katrine "But now I fancy burning some of those pastries off in an equally fun way."


    ###Katrine nervous look##
    if katrine.stage <= 4:
        katrine "Would you want to come back to my place for a bit?"
        pc "I’d love to."
    elif katrine.stage == 5:
        pc "I’d love to."
    elif katrine.stage == 6:
        katrine "Would you want to come back to my place again?"
        pc "I’d love to."
    else:
        katrine "That is if you want to come back to my place again?"
        pc "Absolutely!"


    ###Outside café with Katrine###
    image katrine_date_takehome = "/katrine/[katrine.stage]/date_takehome.webp"
    scene katrine_date_takehome
    "Katrine holds you by the hand as she leads towards her apartment."

    ####Katrines apartment###
    image katrine_home_greet = "/katrine/[katrine.stage]/home_greet.webp"
    scene katrine_home_greet
    if katrine.stage == 2:
        pc "Nice place you have here."
    elif katrine.stage == 3 or katrine.stage == 4:
        "Walking in you take off your shoes and head towards the sofa before Katrine interrupts you."
    else:
        image katrine_home_hug = "/katrine/[katrine.stage]/home_hug.webp"
        scene katrine_home_hug
        "Walking in you take off your shoes and turn and pull her towards you, knowing what to expect by now from her."
        image katrine_home_kiss = "/katrine/[katrine.stage]/home_kiss.webp"
        scene katrine_home_kiss
        "Planting her lips on yours she leads you towards the bed."

        ##[Sex scene]
        call katrine_sex_home from _call_katrine_sex_home
        return

    image katrine_home_hug = "/katrine/[katrine.stage]/home_hug.webp"
    scene katrine_home_hug
    "Turning to look at her, you feel the heat of her body as she presses up against you."
    katrine "I hope you don’t think this too forward of me."
    katrine "But I've been fantasising about this all day."
    if katrine.stage == 2:
        pc "It's definitely not too forward."
    image katrine_home_kiss = "/katrine/[katrine.stage]/home_kiss.webp"
    scene katrine_home_kiss
    "Planting her lips on yours she leads you towards the bed."

    ##[Sex scene]
    call katrine_sex_home from _call_katrine_sex_home_1
    return

label katrine_sex_sauna:
    if persistent.nosexscene == True:
        scene black with dissolve
        "Katrine and you have some fun together in the sauna."
        image katrine_sauna_aftersex = "/katrine/[katrine.stage]/sauna_aftersex.webp"
        scene katrine_sauna_aftersex
        pc "That felt great."
        call katrine_feed_sauna from _call_katrine_feed_sauna
        return

    #[Sex scene starts here]
    image katrine_sauna_doggy = "/katrine/[katrine.stage]/sauna_doggy.webp"
    scene katrine_sauna_doggy
    window hide
    pause
    pc "Well that's just not fair."
    pc "What if we get caught?"
    pc "I don't want to get kicked out of this place."
    katrine "Stop teasing me!"
    image katrine_sauna_sex1 = "/katrine/[katrine.stage]/sauna_sex1.webp"
    scene katrine_sauna_sex1
    window hide
    pause
    pc "Alright, the quicker we finish, the less likely we get caught."
    katrine "We've never been caught!"
    pc "We have never been reported. {w}There's a difference!"
    if katrine.stage == 1:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/1/sauna_sex1_video.webm" loop
    elif katrine.stage == 2:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/2/sauna_sex1_video.webm" loop
    elif katrine.stage == 3:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/3/sauna_sex1_video.webm" loop
    elif katrine.stage == 4:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/4/sauna_sex1_video.webm" loop
    elif katrine.stage == 5:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/5/sauna_sex1_video.webm" loop
    elif katrine.stage == 6:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/6/sauna_sex1_video.webm" loop
    elif katrine.stage == 7:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/7/sauna_sex1_video.webm" loop
    elif katrine.stage == 8:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/8/sauna_sex1_video.webm" loop
    elif katrine.stage == 9:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/9/sauna_sex1_video.webm" loop
    elif katrine.stage == 10:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/10/sauna_sex1_video.webm" loop
    elif katrine.stage == 11:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/11/sauna_sex1_video.webm" loop
    show movie with dissolve
    window hide
    pause
    katrine "Less talking, you're going to get tired!"
    pc "Oh, I can do this all day."
    katrine "Don't ruin the moment!"
    pc "What if I tell you how insanely sexy you look right now?"
    katrine "Uh! {w}I'm listening."
    window hide
    pause
    stop movie
    if katrine.stage == 1:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/1/sauna_sex2_video.webm" loop
    elif katrine.stage == 2:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/2/sauna_sex2_video.webm" loop
    elif katrine.stage == 3:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/4/sauna_sex2_video.webm" loop
    elif katrine.stage == 4:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/4/sauna_sex2_video.webm" loop
    elif katrine.stage == 5:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/5/sauna_sex2_video.webm" loop
    elif katrine.stage == 6:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/6/sauna_sex2_video.webm" loop
    elif katrine.stage == 7:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/7/sauna_sex2_video.webm" loop
    elif katrine.stage == 8:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/8/sauna_sex2_video.webm" loop
    elif katrine.stage == 9:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/9/sauna_sex2_video.webm" loop
    elif katrine.stage == 10:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/10/sauna_sex2_video.webm" loop
    elif katrine.stage == 11:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/11/sauna_sex2_video.webm" loop
    show movie with dissolve
    window hide
    pause
    pc "The way your booty shakes..."
    pc "All the work you're doing here is really paying off."
    katrine "Oh yeah?"
    pc "And I got to say, I really love being the one who gets to appreciate it."
    katrine "But you'd rather that angle, huh?"
    pc "Why do you say that?"
    katrine "Because my front side is not nearly as toned."
    pc "I don’t care about that."
    katrine "What are you-"
    pc "I'm flipping you over!"
    stop movie
    if katrine.stage == 1:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/1/sauna_sex3_video.webm" loop
    elif katrine.stage == 2:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/2/sauna_sex3_video.webm" loop
    elif katrine.stage == 3:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/3/sauna_sex3_video.webm" loop
    elif katrine.stage == 4:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/4/sauna_sex3_video.webm" loop
    elif katrine.stage == 5:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/5/sauna_sex3_video.webm" loop
    elif katrine.stage == 6:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/6/sauna_sex3_video.webm" loop
    elif katrine.stage == 7:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/7/sauna_sex3_video.webm" loop
    elif katrine.stage == 8:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/8/sauna_sex3_video.webm" loop
    elif katrine.stage == 9:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/9/sauna_sex3_video.webm" loop
    elif katrine.stage == 10:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/10/sauna_sex3_video.webm" loop
    elif katrine.stage == 11:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/katrine/11/sauna_sex3_video.webm" loop
    show movie with dissolve
    #[Sex scene ends here]
    window hide
    pause
    "Flipping her over you get a better view of her growing belly move as you thrust into her."
    katrine "Why?"
    pc "Because this is my favorite view."
    if katrine.stage <= 3:
        pc "I love to look into your eyes."
        katrine "Well in that case, my eyes are up here."
        pc "Sorry, just admiring your body."
        katrine "Yeah, you like my body?"
        pc "I love it."
    elif katrine.stage >= 4 and katrine.stage <= 7:
        pc "I love to look into your eyes."
        katrine "But you're staring at my tummy."
        pc "Yeah, I like that too."
        pc "Just admiring your body."
        katrine "Yeah, you like my body?"
        pc "I love it."
    elif katrine.stage >= 8:
        katrine "But you can see my belly."
        pc "And I can look in your eyes."
        katrine "But you're staring at my tummy."
        pc "Yeah, I like that too."
        katrine "Do you like how big it is?"
        pc "I love it."
        katrine "Do you want it to be bigger?"
        pc "I wouldn't mind."
        katrine "Do you want me to stop working out?"
        pc "No, I love how toned you're getting."
        katrine "So...{w} you like me toned, and soft?"
        pc "Like a real woman.{w} You have every kind of curve."
        katrine "Curves on curves, that's me!"
    pc "Oh, fuck!"
    katrine "Are you going to-"
    pc "Yes!"
    katrine "Inside me!"
    window hide
    pause
    stop movie
    image katrine_sauna_aftersex = "/katrine/[katrine.stage]/sauna_aftersex.webp"
    scene katrine_sauna_aftersex
    katrine "That was amazing."
    pc "I can't believe no one walked in."
    katrine "That’s part of the thrill right."
    if katrine.stage <= 4:
        pc "I didn’t know you were into that sort of thing."
        katrine "There’s a lot you don’t know about what I’m into…"
    katrine "The only thing that could make this better would be if I had brought a snack with me."
    katrine "For some reason sex always makes me hungry."
    call katrine_feed_sauna from _call_katrine_feed_sauna_1
    return

label katrine_intro_outside:
    scene outside
    "You go for a relaxing walk around your neighbourhood."
    "Despite living here for a while, you still don’t know many of your neighbours."
    "You wonder who else might live around here."
    image outside_katrine_exhausted = "/katrine/events/stage1/outside_katrine_exhausted.webp"
    scene outside_katrine_exhausted
    pc "Hey, it's that woman again."
    if charisma >= 7:
        pc "I wonder if I should go and speak to her, she is looking a little tired."
        menu:
            "Yes":
                pc "Hi, sorry to interupt but are you ok?"
                $ unknownname = 'Sporty brunette'
                image outside_katrine_firstconvo = "/katrine/events/stage1/outside_katrine_firstconvo.webp"
                scene outside_katrine_firstconvo
                unknown "Hey, yeah I'm ok thanks."
                unknown "But it was sweet of you to check on me."
                unknown "Think I took that last mile a little fast."
                pc "Well, I'm glad you are ok."
                image outside_katrine_firstconvo2 = "/katrine/events/stage1/outside_katrine_firstconvo2.webp"
                scene outside_katrine_firstconvo2
                unknown "Although I forgot my drink and I'm a little hungry."
                unknown "I'm still a bit new to town so I don't know many places or people around here yet."
                pc "There is this great little diner around the corner, if that's alright?"
                unknown "That sounds perfect, would you like to join me?"
                pc "Sure, I'd love to."
                image katrine_cafe_aftergymbooth_talk = "/katrine/[katrine.stage]/cafe_aftergymboothtalk.webp"
                scene katrine_cafe_aftergymbooth_talk
                play music "/music/bunny_bites.ogg" if_changed
                unknown "This place looks good, the food smells amazing."
                pc "Yeah, I really like it here."
                pc "I'm [playername] by the way."
                katrine "Nice to meet you, I'm Katrine."
                $ unknownname = 'Unknown'
                katrine "So have you lived here long?"
                pc "Yeah, I lived here most of my life, until about three years ago."
                pc "After I graduated highschool I left town for a while. I guess I was looking to travel and gain a new perspective on the world."
                pc "I know; corny and cliché, but I was young and I enjoyed the sense of freedom and accomplishment it gave me."
                pc "I just recently got back a month ago, since I was looking to go to the local university in town."
                pc "Some things have changed since I have been away but I know my way around enough to help out a new face in town."
                katrine "Well, it's lucky I bumped into a local, maybe you can show me around sometime."
                image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
                scene marie_serving2
                marie "Hi guys, are you ready to order?"
                katrine "Sure thing. Can I get three burgers, two servings of fries and a large soda, please?"
                "Wow that’s a lot, you wouldn’t have thought someone like her would eat that much."
                pc "Can I just get one burger, please?"
                marie "Coming right up."
                image katrine_cafe_aftergymbooth_talk2 = "/katrine/[katrine.stage]/cafe_aftergymboothtalk2.webp"
                scene katrine_cafe_aftergymbooth_talk2
                katrine "I hope you don’t mind me pigging out a little."
                katrine "Working out always makes my appetite go crazy."
                pc "No, not at all. In fact I like it when a woman isn’t afraid to enjoy her food."
                image katrine_stage1_event_1 = "/katrine/events/stage1/1.webp"
                scene katrine_stage1_event_1
                katrine "Well, you have come to the right place."
                katrine "I love to eat, it's part of the reason I work out so much."
                pc "How so?"
                image katrine_stage1_event_2 = "/katrine/events/stage1/2.webp"
                scene katrine_stage1_event_2
                katrine "Well, the two most important parts of being healthy and losing weight is dieting and exercise."
                katrine "But I hate dieting, there is far too much good food out there to restrict yourself."
                katrine "So instead, I just work out extra hard each week. Then I can eat what I want."
                katrine "Although, I still think I could do to lose a bit more."
                pc "I'm not sure about that, I think you look amazing."
                image katrine_stage1_event_3 = "/katrine/events/stage1/3.webp"
                scene katrine_stage1_event_3
                katrine "Thanks, it's all down to hard work."
                katrine "Before I started working out last year, I kept piling on the pounds."
                katrine "My metabolism was really good when I was younger, so I had terrible eating habits."
                if persistent.imperial:
                    katrine "This time last year I weighed 250 pounds!"
                else:
                    katrine "This time last year I weighed 110kgs!"
                pc "I'm sure you looked great even then. Do you have a goal weight you are working towards?"
                image katrine_stage1_event_4 = "/katrine/events/stage1/4.webp"
                scene katrine_stage1_event_4
                if persistent.imperial:
                    $ imperialweight = (katrine.weight * 2.2)
                    katrine "Right now I weigh [imperialweight:.02f] lbs, and I think I’d like to lose another 10 lbs."
                    katrine "Thankfully my bust hasn’t changed that much even with weight loss."
                    katrine "They are a [katrine.breast_cup] cup or [katrine.breast_size] inches, while my butt measures [katrine.ass_size] inches and waist [katrine.waist_size] inches."
                else:
                    $ metricbreast_size = (katrine.breast_size * 2.54)
                    $ metricwaist_size = (katrine.waist_size * 2.54)
                    $ metricass_size = (katrine.ass_size * 2.54)
                    katrine "Right now I weigh [katrine.weight:.02f]kg, and I think I’d like to lose another 4 or 5 kg."
                    katrine "Thankfully my bust hasn’t changed that much even with weight loss."
                    katrine "They are a [katrine.breast_cup] cup or [metricbreast_size:.02f] cm, while my butt measures [metricass_size:.02f] cm and waist [metricwaist_size:.02f] cm."
                katrine "So I can't complain about my body, just a bit heavier than I’d like to be."
                image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
                scene marie_serving2
                marie "Here is your food, enjoy."
                image katrine_cafe_aftergymboothfood = "/katrine/[katrine.stage]/cafe_aftergymboothfood.webp"
                scene katrine_cafe_aftergymboothfood
                katrine "Thanks, this food looks amazing."
                image katrine_cafe_aftergymboothfoodeating = "/katrine/[katrine.stage]/cafe_aftergymboothfoodeating.webp"
                scene katrine_cafe_aftergymboothfoodeating
                "Picking up her burgers you watch Katrine demolish all three in no time at all."
                pc "Careful you don’t choke."
                image katrine_stage1_event_5 = "/katrine/events/stage1/5.webp"
                scene katrine_stage1_event_5
                katrine "Sorry, I'm not normally like this with people I've just met."
                katrine "But I feel really comfortable around you for some reason."
                katrine "Which could be dangerous if I keep bumping into you here."
                pc "Well, despite that I hope this isn't the last time I see you."
                katrine "Me too, if I'm not here I'm usually in the gym."
                katrine "Would you want to work out together some time? I go to Trista’s gym in town."
                pc "Yeah, that would be great. I'd love to work out with you sometime."
                image katrine_stage1_event_6 = "/katrine/events/stage1/6.webp"
                scene katrine_stage1_event_6
                katrine "That's perfect. Well, maybe I will see you around another time."
                katrine "For now, I think I better finish my run to work off the extra calories."
                image katrine_cafe_aftergymleave = "/katrine/[katrine.stage]/cafe_aftergymleave.webp"
                scene katrine_cafe_aftergymleave
                katrine "But don’t be a stranger."
                pc "Have a great day, Katrine."
                $ katrine_stats_visible = 1
                $ katrine.weight += 1
                "Katrine has been added to the stats menu."
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime

            "No":
                scene outside
                "I finish my walk outside and head home."
                $ daytime += 1
                jump freetime
    else:
        pc "I wish i had the charisma to talk to her (7 charisma required)."
        scene outside
        "I finish my walk outside and head home."
        $ daytime += 1
        jump freetime

label Katrine_Introduction:
    call bbworking
    play music "/music/bunny_bites.ogg" if_changed
    call work_arrive from _call_work_arrive
    "You start working the counter."
    image cafe_katrine_arrive = "/katrine/[katrine.stage]/cafe_arrive.webp"
    scene cafe_katrine_arrive
    "A customer arrives."
    pc "Hey, it's Katrine."
    image cafe_katrine_talk = "/katrine/[katrine.stage]/cafe_talk.webp"
    scene cafe_katrine_talk
    katrine "Hey [playername], how are you doing?"
    pc "I am good thanks, what about you?"
    katrine "I'm good too."
    pc "What would you like to order?"
    katrine "I would like to order two burgers with fries, please."
    pc "Coming right up, please find a nice place to sit down."
    katrine "Thank you."
    image cafe_katrine_ass = "/katrine/[katrine.stage]/cafe_ass.webp"
    scene cafe_katrine_ass
    "Katrine goes to walk away before turning back, clearly considering saying something."
    pc "Everything ok with your order?"
    image katrine_stage1_event_7 = "/katrine/events/stage1/7.webp"
    scene katrine_stage1_event_7
    katrine "Yes, it's not that."
    katrine "I know we only just met, but I really enjoyed our time together the other day."
    katrine "I was wondering if you were free after work and, maybe wanted to go on a date with me?"
    pc "Yeah, I’d love to."
    image katrine_stage1_event_8 = "/katrine/events/stage1/8.webp"
    scene katrine_stage1_event_8
    katrine "Great, there is a little café in town on main street I go to quite often."
    pc "Sure, see you there."
    "You create her food."
    image cafe_katrine_booth = "/katrine/[katrine.stage]/cafe_booth.webp"
    scene cafe_katrine_booth
    pc "Here you go, have a nice meal."
    katrine "Thank you."
    call bbworking
    "You work hard the rest of your shift but keep looking at the clock, waiting for the shift to be over."
    "Handing over, you rush to meet Katrine in the café she mentioned."
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


    ### In café ###
    scene date_cafe
    stop music fadeout 1.0
    "You arrive at the café."
    "Looking around It looks like Katrine isn’t here yet, you sit in one of the booths."
    "A few minutes later you spot Katrine walking towards you."
    image katrine_date_arrive = "/katrine/[katrine.stage]/date_arrive.webp"
    scene katrine_date_arrive
    pc "Hey Katrine, you look nice."
    katrine "Thank you, is it too much?"
    pc "Not at all."
    image katrine_date_talk = "/katrine/[katrine.stage]/date_talk.webp"
    scene katrine_date_talk
    "She quickly grabs a coffee and orders some pastries before joining you in the booth."
    katrine "I come here way too often, but the pastries are just too good to stay away."
    pc "Despite being new to town, you seem to know all the best spots."
    katrine "Yeah, probably because I eat out so often, I keep meaning to cut back."
    pc "It's good to try new things."
    "After a while Katrine's pastries arrive at the table."
    image katrine_date_eat1 = "/katrine/[katrine.stage]/date_eat1.webp"
    scene katrine_date_eat1
    "Katrine raises one of the pastries to her mouth and takes a big bite."
    katrine "True, plus I’m a terrible cook so there is no way I could make anything this nice."
    pc "Are you interested in learning to cook?"
    katrine "Not really, plus I don’t have much time between working out and just regular working."
    pc "What is that you do?"
    katrine "I’m a writer."
    pc "Oh cool, fiction or nonfiction?"
    image katrine_date_eat2 = "/katrine/[katrine.stage]/date_eat2.webp"
    scene katrine_date_eat2
    katrine "Sorry, I didn’t mean books. I write articles for websites online."
    katrine "Freelance mainly, whatever pays the bills."
    pc "That’s interesting, what sort of things do you cover?"
    katrine "Anything and everything. I haven’t really found my niche or anything that grabs me fully."
    pc "It can be hard to find your passion."
    image katrine_date_eat3 = "/katrine/[katrine.stage]/date_eat3.webp"
    scene katrine_date_eat3
    "Katrine nods as she eats another of her pastries."
    "Over the next hour you both make small talk about her job, the gym and other things."
    "Throughout, Katrine is constantly working her way through the large selection of pastries she bought."
    image katrine_date_eat_empty = "/katrine/[katrine.stage]/date_eat_empty.webp"
    scene katrine_date_eat_empty
    "After a while you see her go to grab another, only to be surprised to find the table empty."
    katrine "Wow, I can't believe I ate them all."
    katrine "I was supposed to take some back with me for later."
    katrine "I hope you don’t mind me pigging out like that."
    pc "Not at all, I enjoyed our conversation."
    image katrine_date_leave = "/katrine/[katrine.stage]/date_leave.webp"
    scene katrine_date_leave
    katrine "Thanks, you're sweet."
    katrine "But I should get back, still have some work to do."
    "Both of you stand up to leave."

    ###Outside café with Katrine###
    image katrine_date_bye = "/katrine/[katrine.stage]/date_bye.webp"
    scene katrine_date_bye
    katrine "We should do this another time."
    katrine "Here’s my number."
    "You quickly add her number to your phone and send her a message so she has yours."
    katrine "See you around."

    $ katrine.weight += 1
    $ katrineintroduction = 0
    return

label Katrine_Stage_1_Event:
    ###Gym, Katrine on the treadmill ###
    image katrine_gym_running_event1 = "/katrine/1/gym_running.webp"
    scene katrine_gym_running_event1
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    "Hey it's Katrine, she is running fast on the treadmill."
    "I should go over and say hi."
    pc "Hey Katrine."
    katrine "Hey [playername], thirty seconds and I'll be done."

    ##Katrine stood next to the treadmill###
    image katrine_gym_standing_event1 = "/katrine/1/gym_standing.webp"
    scene katrine_gym_standing_event1
    katrine "What's up?"
    pc "Nothing much, just wanted to say hi and see how you are doing."
    katrine "Well, I was about to move over to the weights if you want to work out together?"
    pc "Sure thing."
    katrine "Can you spot me?"
    image katrine_gym_benchpress2_event1 = "/katrine/1/gym_benchpress2.webp"
    scene katrine_gym_benchpress2_event1
    "Standing behind the barbell you help Katrine do a set of reps."
    pc "Good job."
    katrine "Thanks, but I think you helped a lot."
    image katrine_stage1_event_9 = "/katrine/events/stage1/9.webp"
    scene katrine_stage1_event_9
    "Standing there you notice her rubbing her shoulder."
    pc "Everything ok?"
    katrine "I definitely felt something twinge in my shoulder."
    image katrine_gym_standing3_event1 = "/katrine/1/gym_standing3.webp"
    scene katrine_gym_standing3_event1
    katrine "That should probably do for now, don’t want to pull anything."
    pc "Good idea, could just be dehydrated since you are working so hard."
    katrine "That’s true, mind grabbing me a soda?"
    pc "Sure thing."
    image trista_gym_shop_event1 = "/trista/1/gym_shop.webp"
    scene trista_gym_shop_event1
    pc "Hi Trista, can I get a large soda please."
    trista "Sure thing."
    ###Gym with Katrine – maybe her holding her shoulder###
    image katrine_stage1_event_10 = "/katrine/events/stage1/10.webp"
    scene katrine_stage1_event_10
    pc "Here you are."
    katrine "Thanks."
    image katrine_gym_drink_event1 = "/katrine/1/gym_drink.webp"
    scene katrine_gym_drink_event1
    katrine "So I was thinking of going to the sauna if you wanted to join me?"
    pc "Absolutely."
    stop music fadeout 1.0

    ###Sauna ###
    image katrine_sauna_arrive_event1 = "/katrine/1/sauna_arrive.webp"
    scene katrine_sauna_arrive_event1
    play music "/music/sauna.ogg" if_changed
    katrine "Nice and hot in here."
    katrine "I really like it, plus it should do my muscles wonders after that workout."
    katrine "Since it's just us, you don’t mind if I…."
    image katrine_sauna_sitting_event1 = "/katrine/1/sauna_sitting.webp"
    scene katrine_sauna_sitting_event1
    "Slowly removing her towel Katrine relaxes next to you completely naked."
    "You do your best not to stare and try to distract yourself."
    pc "How is your shoulder feeling?"
    image katrine_stage1_event_11 = "/katrine/events/stage1/11.webp"
    scene katrine_stage1_event_11
    katrine "It's still a little tight to be honest."
    pc "Would it help if I massaged it?"
    katrine "I wouldn't say no to a free massage."
    image katrine_stage1_event_12 = "/katrine/events/stage1/12.webp"
    scene katrine_stage1_event_12
    "Turning away from you, you begin to gently rub her shoulder."
    katrine "Oh yeah, that feels amazing."
    "Leaning back again a few minutes later Katrine seems a lot more relaxed."
    image katrine_sauna_sitting_event1 = "/katrine/1/sauna_sitting.webp"
    scene katrine_sauna_sitting_event1
    katrine "That was great, thank you."
    pc "Any time."
    katrine "Speaking of, I should probably get out of here."
    katrine "I'll see you around."
    pc "Definitely."
    if recollection == False:
        $ katrinestage1event = 0
        #Unlocks Katrine Undress in the stats page.
        $ renpy.notify("Katrine Undress option unlocked in stats screen.")
        window hide
        pause
        $ katrine.weight += 1
    stop music fadeout 1.0
    return


label Katrine_Stage_2_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Katrine', dialogue=dialogue_one)
    $ msg ("Hey. Fancy joining me at the café again?", who=1)
    pause
    $ msg ("We could call it a date if you like?", who=1)
    pause
    menu:
        "Go on a date with Katrine.":
            $ hide_messenger()
        "Do something else.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    ### In café, Katrine already in booth ###
    image katrine_stage2_event_1 = "/katrine/events/stage2/1.webp"
    scene katrine_stage2_event_1
    "You arrive at the café."
    "Looking around you spot Katrine in the usual booth with a pile of pastries and coffee."
    image katrine_stage2_event_2 = "/katrine/events/stage2/2.webp"
    scene katrine_stage2_event_2
    pc "Hey, Katrine. Sorry I'm late."
    katrine "Thank you. Don't worry, you are not late. I was early."
    pc "How are you?"
    katrine "I'm good, thanks. A little hungry, which is probably why I beat you here."
    image katrine_date_eat1_event2 = "/katrine/2/date_eat1.webp"
    scene katrine_date_eat1_event2
    "As if to emphasise the point she raises a pastry and starts eating it."
    pc "So, what's new with you?"
    katrine "Not much. Still working out in my free time."
    katrine "Did an extra-long session this morning so this is my reward."
    image katrine_date_eat2_event2 = "/katrine/2/date_eat2.webp"
    scene katrine_date_eat2_event2
    "Picking up one of the pastries she takes a big bite out of it smiling at you, or maybe the pastry."
    katrine "Other than that, started writing a piece for someone on the state of the underground train system in town."
    pc "That sounds...interesting?"
    image katrine_stage2_event_3 = "/katrine/events/stage2/3.webp"
    scene katrine_stage2_event_3
    katrine "I wish. It's so dull. They want all this information about logistics and user numbers in it."
    katrine "On the plus side it makes going to the gym even more appealing."
    pc "I can think of worse ways of procrastinating."
    katrine "Exactly. Although, I shouldn't complain about getting work."
    katrine "I just wish it was a bit more interesting."
    pc "You never know what your next story might be."
    image katrine_date_eat3_event2 = "/katrine/2/date_eat3.webp"
    scene katrine_date_eat3_event2
    "Katrine smiles at you as she eats another of her pastries."
    "Over the next hour you both make small talk about her job, the gym and other things as you enjoy each other’s company."
    "Throughout, Katrine is constantly working her way through the large selection of pastries she bought."
    image katrine_date_eat_empty_event2 = "/katrine/2/date_eat_empty.webp"
    scene katrine_date_eat_empty_event2
    katrine "Wow, I can't believe I ate all those again."
    katrine "I was supposed to take some back with me for later."
    katrine "I hope you don’t mind me pigging out like that."
    pc "Not at all, I enjoyed our conversation."
    image katrine_stage2_event_4 = "/katrine/events/stage2/4.webp"
    scene katrine_stage2_event_4
    katrine "Thanks, I really like our dates."
    katrine "I don’t get to speak to many people."
    katrine "Plus being new in town it can make you feel a little bit lonely."
    pc "Well, I’m happy to have run into you. I enjoy these too."
    image katrine_date_leave_event2 = "/katrine/2/date_leave.webp"
    scene katrine_date_leave_event2
    katrine "Would you want to come back to my place for a bit?"
    pc "I’d love to."
    image katrine_date_takehome_event2 = "/katrine/2/date_takehome.webp"
    scene katrine_date_takehome_event2
    "Katrine holds you by the hand as she leads towards her apartment."

    ####Katrines apartment###
    image katrine_home_greet_event2 = "/katrine/2/home_greet.webp"
    scene katrine_home_greet_event2
    pc "Nice place you have here."
    image katrine_home_hug_event2 = "/katrine/2/home_hug.webp"
    scene katrine_home_hug_event2
    "Turning to look at her, you feel the heat of her body as she presses up against you."
    katrine "I hope you don’t think this too forward of me."
    katrine "But I've been fantasising about this all day."
    pc "It's definitely not too forward."
    image katrine_home_kiss_event2 = "/katrine/2/home_kiss.webp"
    scene katrine_home_kiss_event2
    "Planting her lips on yours she leads you towards the bed."

    if recollection == False:
        call katrine_sex_home from _call_katrine_sex_home_2
        $ katrinestage2event = 0
        $ trista.weight = 78
        $ katrine.weight += 0.5
        $ daytime += 1
        $ phonecall = 1
    return


label Katrine_Stage_3_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Katrine', dialogue=dialogue_one)
    $ msg ("Hey, [playername]. Fancy joining me at the gym?", who=1)
    pause
    $ msg ("Going to stop by at Bunny Bites first though. I skipped breakfast.", who=1)
    pause
    menu:
        "Join Katrine.":
            $ hide_messenger()
        "Do something else.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    ###Bunny bites###
    image katrine_stage3_event_1 = "/katrine/events/stage3/1.webp"
    scene katrine_stage3_event_1
    play music "/music/bunny_bites.ogg" if_changed
    "Walking in you see Katrine already sitting in one of the booths."
    "Joining her she smiles as she notices you approach."
    image katrine_stage3_event_2 = "/katrine/events/stage3/2.webp"
    scene katrine_stage3_event_2
    katrine "Hey, [playername]. I hope you don't mind, but I already ordered."
    pc "It's okay. I'm not really hungry. I just came to see you."
    "Soon a waitress arrives and the table is covered in food."
    image katrine_stage3_event_3 = "/katrine/events/stage3/3.webp"
    scene katrine_stage3_event_3
    pc "This is a lot of food."
    katrine "Sorry. Like I said, I skipped breakfast and we are about to work out."
    katrine "I figure it doesn’t matter how much I eat now since I will have worked it all off in a couple of hours."
    pc "That’s one way of looking at it."
    image katrine_stage3_event_4 = "/katrine/events/stage3/4.webp"
    scene katrine_stage3_event_4
    "Picking up the first burger, Katrine chomps down on her pre-workout feast."
    katrine "Our waitress was checking you out."
    pc "Makes sense. {w}We're friends."
    katrine "So, what's new with you?"
    pc "Not much. Mainly university stuff and working here."

    image katrine_stage3_event_5 = "/katrine/events/stage3/5.webp"
    scene katrine_stage3_event_5
    "Slurping noisily from her large soda Katrine nods along to what you are saying."
    katrine "Yeah? {w}Have any of these girls made a move on you yet?"
    pc "I didn't realize you were the jealous type."
    katrine "I'm not, just curious. {w}But maybe they are, since they both keep looking over here."

    pc "You must be better at picking up on such things than I am."
    pc "Anyway, what's new with you?"
    katrine "Well, I've been working on some pieces for the local newspaper."
    image katrine_stage3_event_6 = "/katrine/events/stage3/6.webp"
    scene katrine_stage3_event_6
    "Pausing Katrine throws a couple of nuggets into her open mouth."
    katrine "Mmmm, and then just working out."
    katrine "Although I missed a couple of sessions last week and I think I'm feeling it."
    pc "How so?"
    katrine "Nothing major. Just feeling a little bit more sluggish than normal."
    image katrine_stage3_event_7 = "/katrine/events/stage3/7.webp"
    scene katrine_stage3_event_7
    "As she moves onto her second burger, you wonder if it has more to do with her eating habits than missing working out."
    image katrine_stage3_event_8 = "/katrine/events/stage3/8.webp"
    scene katrine_stage3_event_8
    "Making small talk for the next thirty minutes you watch intently as Katrine makes her way through the table of food."
    image katrine_stage3_event_9 = "/katrine/events/stage3/9.webp"
    scene katrine_stage3_event_9
    "She sure can eat."
    image katrine_stage3_event_10 = "/katrine/events/stage3/10.webp"
    scene katrine_stage3_event_10
    "Sitting back Katrine looks relaxed, despite her clearly larger stomach."
    katrine "Should we go to the gym then?"
    pc "Don’t you want a minute to digest that?"
    image katrine_stage3_event_11 = "/katrine/events/stage3/11.webp"
    scene katrine_stage3_event_11
    katrine "Oh, I'm used to it. I quite often eat before I work out."
    katrine "I know you are not meant to, but it never seems to do me any harm."
    katrine "Plus, I hate feeling hungry. And who wants to work out hungry?"
    pc "No one."
    image katrine_stage3_event_12 = "/katrine/events/stage3/12.webp"
    scene katrine_stage3_event_12
    katrine "Exactly."
    "Standing awkwardly you follow Katrine out of the restaurant and towards the gym."
    stop music fadeout 1.0

    ###Gym, Katrine Bloated.”
    image katrine_stage3_event_13 = "/katrine/events/stage3/13.webp"
    scene katrine_stage3_event_13
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    katrine "Think I'm going to start with the weights if you want to spot for me?"
    pc "Sure."
    image katrine_stage3_event_14 = "/katrine/events/stage3/14.webp"
    scene katrine_stage3_event_14
    "Positioning yourself behind Katrine you help her do a set of reps."
    "Despite her conviction that eating didn’t have an impact on her, it was clear she was having a bit more trouble than usual."
    "Trying not to discourage her, you take up your fair share of the weight to make it a bit easier for her."
    image katrine_stage3_event_15 = "/katrine/events/stage3/15.webp"
    scene katrine_stage3_event_15
    katrine "Thanks. Want me to repay the favour?"
    pc "Sure."
    ###Not sure what angle you would want to do or if this is even possible?###
    image katrine_stage3_event_16 = "/katrine/events/stage3/16.webp"
    scene katrine_stage3_event_16
    "Laying down on the bench you look up towards the weights, only to see your view slightly obscured."
    "Above your vision you can't help but see Katrine's enlarged gut."
    image katrine_stage3_event_17 = "/katrine/events/stage3/17.webp"
    scene katrine_stage3_event_17
    "From her position behind the bench it seems her recent indulgence has had a favourable impact on her waist."
    image katrine_stage3_event_18 = "/katrine/events/stage3/18.webp"
    scene katrine_stage3_event_18
    "But not wanting to draw attention to it, you quickly grab the bar and begin to do your set of reps."
    image katrine_stage3_event_19 = "/katrine/events/stage3/19.webp"
    scene katrine_stage3_event_19
    katrine "Wow, you made that look easy."
    pc "Thanks. Working out with you has definitely helped motivate me."
    scene gym
    "You work out for the next hour on various machines before heading to the sauna to relax."
    stop music fadeout 1.0

    ###Sauna###
    scene sauna
    play music "/music/sauna.ogg" if_changed
    "Thankfully, it's empty. But after a few minutes you hear a knock on the door."
    image katrine_stage3_event_20 = "/katrine/events/stage3/20.webp"
    scene katrine_stage3_event_20
    katrine "Mind if I join you?"
    pc "Not at all."
    image katrine_stage3_event_21 = "/katrine/events/stage3/21.webp"
    scene katrine_stage3_event_21
    "Sitting down next to you, Katrine removes her towel."
    "You do your best not to stare, but it's hard not to look at her curves."
    katrine "Nice and hot in here. Really helps my muscles after a tough workout."
    image katrine_stage3_event_22 = "/katrine/events/stage3/22.webp"
    scene katrine_stage3_event_22
    "As if to emphasise the point Katrine stretches out, giving you a good view of her naked body."
    "Catching you looking at her, Katrine smiles at you."
    image katrine_stage3_event_23 = "/katrine/events/stage3/23.webp"
    scene katrine_stage3_event_23
    katrine "Well, I don't think it's very fair if only one of us is naked."
    "Dropping your towel on the floor you repay Katrine the favour."
    "Sitting naked you enjoy each other's company for a while."
    pc "Think I'm going to head home. Thanks for today, Katrine."
    image katrine_stage3_event_24 = "/katrine/events/stage3/24.webp"
    scene katrine_stage3_event_24
    katrine "Are you sure you want to do that?"
    katrine "It seems we have the place to ourselves..."
    image katrine_sauna_hug_event3 = "/katrine/3/sauna_hug.webp"
    scene katrine_sauna_hug_event3
    "Standing up Katrine approaches you, pressing her naked body against yours."
    pc "Maybe I could stay for a bit longer."
    image katrine_sauna_kiss_event3 = "/katrine/3/sauna_kiss.webp"
    scene katrine_sauna_kiss_event3
    katrine "My hero."
    if persistent.nosexscene == True:
        scene black
        "You and Katrine had a wonderful time together."
        image katrine_stage3_event_26 = "/katrine/events/stage3/26.webp"
        scene katrine_stage3_event_26
        katrine "I can't believe how much you were enjoying that."
        katrine "I've never felt that wanted before."
        pc "Then you haven't been paying attention."

        katrine "The only thing that could make this better would be if I had brought a snack with me."
        katrine "For some reason sex always makes me hungry."
        pc "I think I've got something."
        image katrine_stage3_event_27 = "/katrine/events/stage3/27.webp"
        scene katrine_stage3_event_27
        katrine "I wasn’t actually serious…but if you do happen to have something I won't say no."
        pc "Sure thing."
        katrine "You-"
        pc "Yeah?"
        katrine "Nothing."
        katrine "You just make me happy."
        image katrine_stage3_event_28 = "/katrine/events/stage3/28.webp"
        scene katrine_stage3_event_28
        "Handing over the sweet treats Katrine leans back as she starts eating."
        katrine "Ok, now this is perfect."

        "After watching Katrine finish off the treats, you head home."
        "You will have to make sure to always have some extra snacks if you and Katrine keep doing that."
        if recollection == False:
            $ katrine.weight += 0.5
            $ daytime += 1
            $ phonecall = 1
        $ katrinestage3event = 0
        stop music fadeout 1.0
        return

    image katrine_stage3_event_30 = "/katrine/events/stage3/30.webp"
    scene katrine_stage3_event_30
    window hide
    pause
    pc "Well, that's just not fair."
    pc "What if we get caught?"
    pc "I don't want to get kicked out of this place."
    katrine "Stop teasing me!"
    image katrine_stage3_event_29 = "/katrine/events/stage3/29.webp"
    scene katrine_stage3_event_29
    window hide
    pause
    pc "Alright, the quicker we finish, the less likely we get caught."
    katrine "We've never been caught!"
    pc "We have never been reported. {w}There's a difference!"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/katrine/events/stage3/31.webm" loop
    show movie with dissolve
    window hide
    pause
    katrine "Less talking, you're going to get tired!"
    pc "Oh, I can do this all day."
    katrine "Don't ruin the moment!"
    pc "What if I tell you how insanely sexy you look right now?"
    katrine "Uh! {w}I'm listening."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/katrine/events/stage3/32.webm" loop
    show movie with dissolve
    window hide
    pause
    pc "The way your booty shakes..."
    pc "All the work you're doing here is really paying off."
    katrine "Oh yeah?"
    pc "And I got to say, I really love being the one who gets to appreciate it."
    katrine "But you'd rather that angle, huh?"
    pc "Why do you say that?"
    katrine "Because my front side is not nearly as toned."
    pc "I don’t care about that."
    katrine "What are you-"
    pc "I'm flipping you over!"
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/katrine/events/stage3/33.webm" loop
    show movie with dissolve
    "Flipping her over you get a better view of her growing belly move as you thrust into her."
    window hide
    pause
    katrine "Why?"
    pc "Because this is my favorite view."
    pc "I love to look into your eyes."
    katrine "Well in that case, my eyes are up here."
    pc "Sorry. Just admiring your body."
    katrine "Yeah? You like my body?"
    pc "I love it."
    pc "Oh, fuck!"
    katrine "Are you going to-"
    pc "Yes!"
    katrine "Inside me!"
    window hide
    pause
    stop movie
    ###After sex scene###
    image katrine_stage3_event_25 = "/katrine/events/stage3/25.webp"
    scene katrine_stage3_event_25
    katrine "That was amazing."
    pc "I can't believe no one walked in."
    image katrine_stage3_event_26 = "/katrine/events/stage3/26.webp"
    scene katrine_stage3_event_26
    katrine "That's part of the thrill, right?"
    pc "I didn’t know you were into that sort of thing."
    katrine "There’s a lot you don’t know about what I’m into…"
    katrine "The only thing that could make this better would be if I had brought a snack with me."
    katrine "For some reason sex always makes me hungry."
    pc "I think I've got something."
    image katrine_stage3_event_27 = "/katrine/events/stage3/27.webp"
    scene katrine_stage3_event_27
    katrine "I wasn’t actually serious…but if you do happen to have something I won't say no."
    pc "Sure thing."
    katrine "You-"
    pc "Yeah?"
    katrine "Nothing."
    katrine "You just make me happy."
    image katrine_stage3_event_28 = "/katrine/events/stage3/28.webp"
    scene katrine_stage3_event_28
    if recollection == False:
        $ foodheld -= 1
    "Handing over the sweet treats Katrine leans back as she starts eating."
    katrine "Ok, now this is perfect."

    "After watching Katrine finish off the treats, you head home."
    "You will have to make sure to always have some extra snacks if you and Katrine keep doing that."
    if recollection == False:
        $ katrine.weight += 0.5
        $ daytime += 1
        $ phonecall = 1
    $ katrinestage3event = 0
    stop music fadeout 1.0
    return


label Katrine_Stage_4_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Katrine', dialogue=dialogue_one)
    $ msg ("Hey, [playername]. Fancy going to Velvet Shadows with me tonight?", who=1)
    pause
    menu:
        "Join Katrine.":
            $ hide_messenger()
        "Do something else.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    image katrine_stage4_event_1 = "/katrine/events/stage4/1.webp"
    scene katrine_stage4_event_1
    play music "/music/stripclub.ogg" if_changed
    "Arriving at Velvet Shadows, you see Katrine waving at you from the bar."
    image katrine_stage4_event_2 = "/katrine/events/stage4/2.webp"
    scene katrine_stage4_event_2
    katrine "Hey! Nice to see you again."
    pc "Yeah, you too. How are you?"
    katrine "I'm good, thanks."
    pc "I didn't take you for being a strip club type of person."
    image katrine_stage4_event_3 = "/katrine/events/stage4/3.webp"
    scene katrine_stage4_event_3
    katrine "I'm not, really. I just know Trista doesn't like this place."
    pc "You two still not getting on?"
    katrine "Not really."
    pc "Mind if I ask why?"
    image katrine_stage4_event_4 = "/katrine/events/stage4/4.webp"
    scene katrine_stage4_event_4
    katrine "I think I'm going to need a few more of these first."
    pc "Great idea."
    pc "By the way, I haven't shared my appreciation of this dress yet."
    katrine "You like?"
    pc "I love."
    image katrine_stage4_event_2 = "/katrine/events/stage4/2.webp"
    scene katrine_stage4_event_2
    katrine "I'm glad, because I'm about to bore you by complaining about her."
    pc "That is not going to be a problem."
    katrine "Where have you been all my life?"
    "Ordering a couple of drinks you keep them flowing as Katrine laments her frustrations to you over the next couple of hours."
    image katrine_stage4_event_5 = "/katrine/events/stage4/5.webp"
    scene katrine_stage4_event_5
    "It's clear the alcohol is starting to hit her as she begins to tipsily repeat things she said an hour earlier."
    katrine "Trista is so annoying, she even complained to me about how much I'm eating."
    katrine "Like it's any of her business especially since it's not like I’ve gained any weight."
    katrine "It's like she only ever thinks of herself and just keeps butting into things like our date."
    image katrine_stage4_event_6 = "/katrine/events/stage4/6.webp"
    scene katrine_stage4_event_6
    "Pausing, Katrine smiles to herself."
    katrine "Butting, get it?"
    pc "Ok, I think you might have had enough for tonight."
    image katrine_stage4_event_7 = "/katrine/events/stage4/7.webp"
    scene katrine_stage4_event_7
    katrine "Come on, just a bad joke. Although it is getting late."
    image katrine_stage4_event_8 = "/katrine/events/stage4/8.webp"
    scene katrine_stage4_event_8
    "Standing up you see Katrine wobble slightly."
    katrine "Woo, sorry. Think the alcohol is hitting."
    pc "Should you eat something?"
    image katrine_stage4_event_9 = "/katrine/events/stage4/9.webp"
    scene katrine_stage4_event_9
    katrine "That's probably a good idea. Plus, I'm pretty hungry."
    pc "Do you want to stop off at Bunny Bites?"
    image katrine_stage4_event_10 = "/katrine/events/stage4/10.webp"
    scene katrine_stage4_event_10
    katrine "No, I've got some stuff at home if you want to join me there?"
    pc "Sure thing."
    "You help keep Katrine steady as she wobbles her way home."
    "After a more challenging walk than you are used to, you finally make it to her apartment and quickly head inside."
    stop music fadeout 1.0

    ###Katrine’s place####
    image katrine_stage4_event_11 = "/katrine/events/stage4/11.webp"
    scene katrine_stage4_event_11
    katrine "There should be some leftovers in the kitchen."
    pc "I don’t see any."
    image katrine_stage4_event_12 = "/katrine/events/stage4/12.webp"
    scene katrine_stage4_event_12
    katrine "Oh, that's right, I ate them before going out."
    katrine "Damn it! Maybe we should have gone to Bunny Bites."
    pc "Don’t worry, I think I have something."
    image katrine_stage4_event_13 = "/katrine/events/stage4/13.webp"
    scene katrine_stage4_event_13
    "After putting Katrine's hungry mind at ease by being prepared for a situation like this, you notice that your tipsy gym partner has started to derobe - revealing a provocative sight."
    katrine "Really? Well, why don't you bring them over here?"
    "Moving over you join Katrine in the bedroom."

    #[Stuffing mini game followed by sex scene]
    image katrine_stage4_event_14 = "/katrine/events/stage4/14.webp"
    scene katrine_stage4_event_14
    katrine "I like the way you look at me."
    image katrine_stage4_event_15 = "/katrine/events/stage4/15.webp"
    scene katrine_stage4_event_15
    katrine "So, what are you waiting for? Get yourself over here."
    pc "My pleasure."
    katrine "So, what do you have for me?"
    #STUFFING MINI GAME START

    image katrine_stage4_event_feed1_1 = "/katrine/events/stage4/feed1_1.webp"
    scene katrine_stage4_event_feed1_1
    katrine "Oooh, some food foreplay. Yes, please!"
    image katrine_stage4_event_feed2_1 = "/katrine/events/stage4/feed2_1.webp"
    scene katrine_stage4_event_feed2_1
    katrine "Yes, I'd love to eat more. There is still plenty of room."
    image katrine_stage4_event_feed3_1 = "/katrine/events/stage4/feed3_1.webp"
    scene katrine_stage4_event_feed3_1
    katrine "Mmm, this is perfect."
    pc "Do you want me to bring you some milk?"
    katrine "Are you a mind reader?"
    image katrine_stage4_event_feed4_1 = "/katrine/events/stage4/feed4_1.webp"
    scene katrine_stage4_event_feed4_1
    "Her belly starts to look bigger from all the food."
    image katrine_stage4_event_feed4_2 = "/katrine/events/stage4/feed4_2.webp"
    scene katrine_stage4_event_feed4_2
    katrine "[playername], please don't stop."
    image katrine_stage4_event_feed2_2 = "/katrine/events/stage4/feed2_2.webp"
    scene katrine_stage4_event_feed2_2
    katrine "Yes, keep feeding me."
    image katrine_stage4_event_feed1_2 = "/katrine/events/stage4/feed1_2.webp"
    scene katrine_stage4_event_feed1_2
    katrine "Keep going, please don't stop feeding me."
    image katrine_stage4_event_feed3_2 = "/katrine/events/stage4/feed3_2.webp"
    scene katrine_stage4_event_feed3_2
    "Her belly is looking bigger from all the food, but she doesn’t seem to care."
    image katrine_stage4_event_feed3_3 = "/katrine/events/stage4/feed3_3.webp"
    scene katrine_stage4_event_feed3_3
    katrine "Mmm, I can't believe how good this feels. My belly is feeling so tight."
    image katrine_stage4_event_feed2_3 = "/katrine/events/stage4/feed2_3.webp"
    scene katrine_stage4_event_feed2_3
    katrine "Pff, I feel so stuffed, but the food is so good."
    image katrine_stage4_event_feed1_3 = "/katrine/events/stage4/feed1_3.webp"
    scene katrine_stage4_event_feed1_3
    katrine "Oooh, this is so amazing. But I'm not sure I can eat any more."
    pc "I think you can eat one more thing."
    katrine "Ok, you're right. One more thing, but then I'm going to need attention of a different kind."
    image katrine_stage4_event_feed4_3 = "/katrine/events/stage4/feed4_3.webp"
    scene katrine_stage4_event_feed4_3

    #STUFFING MINI GAME END
    katrine "That's it, I can't eat more than this."
    image katrine_stage4_event_16 = "/katrine/events/stage4/16.webp"
    scene katrine_stage4_event_16
    pc "You're so damn cute."
    katrine "Ughh, I feel so full."
    image katrine_stage4_event_17 = "/katrine/events/stage4/17.webp"
    scene katrine_stage4_event_17
    katrine "Now it's your turn to eat!"
    pc "What about-"
    katrine "Don't worry about my stockings, just rip them open."
    if persistent.nosexscene == True:
        scene black
        "You and Katrine had a wonderful time together."
        "You clean up the place and kiss Katrine good night before going home."
        if recollection == False:
            $ katrine.weight += 1
            $ daytime += 1
            $ phonecall = 1
        $ katrinestage4event = 0
        return
    image katrine_stage4_event_18 = "/katrine/events/stage4/18.webp"
    scene katrine_stage4_event_18
    "You rip open her fishnet stockings to reveal your own meal."
    window hide
    pause
    pc "Wow, you're soaking."
    katrine "Everything about tonight has turned me on."
    katrine "Especially you."

    image katrine_stage4_event_19 = "/katrine/events/stage4/19.webp"
    scene katrine_stage4_event_19
    window hide
    pause
    katrine "Ohhhh, you're so good at that!"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/katrine/events/stage4/20.webm" loop
    show movie with dissolve
    window hide
    pause
    katrine "Best night ever!"
    katrine "Ohhhh!"
    katrine "How are you so good at this?"
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/katrine/events/stage4/21.webm" loop
    show movie with dissolve
    window hide
    pause
    katrine "I'm close!"
    katrine "Oh, right there!"
    katrine "Right there-{w} OHHHHHH!"
    katrine "[playername]!!!!!"
    stop movie
    image katrine_stage4_event_22 = "/katrine/events/stage4/22.webp"
    scene katrine_stage4_event_22
    window hide
    pause
    katrine "How-"
    katrine "What-"
    katrine "[playername]."
    pc "Yes?"
    katrine "Yes."
    image katrine_stage4_event_23 = "/katrine/events/stage4/23.webp"
    scene katrine_stage4_event_23
    window hide
    pause
    katrine "Hi."
    pc "Hello there!"
    katrine "Guess what?"
    pc "Tell me."
    katrine "Lie down. {w}It's your turn."
    image katrine_stage4_event_24 = "/katrine/events/stage4/24.webp"
    scene katrine_stage4_event_24
    window hide
    pause
    katrine "Oh, you're ready for me!"
    image katrine_stage4_event_25 = "/katrine/events/stage4/25.webp"
    scene katrine_stage4_event_25
    window hide
    pause
    katrine "I was going to use my tits to get you started, but it looks like there's no need."
    pc "Aww."
    katrine "Would you like that?"
    pc "Very much."
    katrine "I'll remember that for next time."
    katrine "But right now-"
    image katrine_stage4_event_26 = "/katrine/events/stage4/26.webp"
    scene katrine_stage4_event_26
    katrine "It's time for the main course!"
    window hide
    pause
    pc "I can't argue with that."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/katrine/events/stage4/27.webm" loop
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
    play movie "/images/katrine/events/stage4/28.webm" loop
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
    play movie "/images/katrine/events/stage4/29.webm" loop
    show movie with dissolve
    window hide
    pause
    katrine "Ohhh, you're going to finish me off twice tonight!"
    pc "Is that all?"
    katrine "Naughty boy!"
    katrine "I can't have all the fun!"
    pc "That's not something you need to worry about."
    pc "Although... {w}I kind of wish you had a mirror in here so I could see your backside."
    katrine "This feels amazing, but I know how much you like my ass."
    katrine "Reverse cowgirl isn't the easiest position, but I could try it."
    pc "No, I'd rather imagine it."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/katrine/events/stage4/30.webm" loop
    show movie with dissolve
    window hide
    pause
    katrine "You want to imagine my ass as it bounces up and down?"
    pc "Mmm hmm!"
    katrine "What’s that? Uhh! You like this?"
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
    image katrine_stage4_event_23 = "/katrine/events/stage4/23.webp"
    scene katrine_stage4_event_23
    "Collapsing back on the bed, you can see a content look in Katrine's eyes."
    katrine "Mmm, that was good."
    katrine "Although, you could be a bit meaner?"
    pc "You want me to be mean?"
    katrine "Maybe a little, just roleplay a bit."
    pc "Roleplay? I wouldn’t have guessed you were into that?"
    katrine "You would be surprised what I am into."
    pc "Oh really!?"
    pc "Like being fed during sex?"
    katrine "Totally, it’s just so hot to be fed like a Greek goddess or something."
    katrine "But more than that, like the other day…."
    katrine "I imagined what it would be like to be much bigger, like truly massive."
    katrine "What if I just gave in? Ate until I could eat no more?"
    "Katrine seems lost in her own world for a little bit before realising what she had just said."
    "You are not sure if she meant to say that out loud or just in her head."
    katrine "Oh, sorry. I didn't really mean that."
    katrine "Wow, I must have drunk more than I realised."
    pc "You don't have to apologise. I'm happy to give anything a try."
    katrine "Thanks. But seriously, don't worry about it."
    katrine "Forget I said anything, just the booze talking."
    "You clean up the place and kiss Katrine good night before going home."
    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
        $ katrine.weight += 1
    $ katrinestage4event = 0
    return


label Katrine_Stage_5_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Katrine', dialogue=dialogue_one)
    $ msg ("Hey, [playername]. Fancy joining me at Bunny Bites before working out.", who=1)
    pause
    menu:
        "Join Katrine.":
            $ hide_messenger()
        "Do something else.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    image katrine_stage5_event_1 = "/katrine/events/stage5/1.webp"
    scene katrine_stage5_event_1
    play music "/music/bunny_bites.ogg" if_changed
    "Walking into Bunny Bites you notice Katrine already sat in one of the booths."
    image katrine_stage5_event_2 = "/katrine/events/stage5/2.webp"
    scene katrine_stage5_event_2
    katrine "Hey, [playername]. How are you?"
    pc "I'm good, thanks. You?"
    katrine "Yeah, I'm good, actually."
    image katrine_stage5_event_3 = "/katrine/events/stage5/3.webp"
    scene katrine_stage5_event_3
    katrine "Submitted that story I was telling you about before and it's gone down really well."
    pc "That's amazing! I'm really happy for you."
    katrine "Thanks! It made me remember why I love to write."
    pc "So what's next on the agenda?"
    image katrine_stage5_event_4 = "/katrine/events/stage5/4.webp"
    scene katrine_stage5_event_4
    katrine "Nothing major at the moment. Think I could do with a few days off."
    pc "You deserve it."
    image katrine_stage5_event_5 = "/katrine/events/stage5/5.webp"
    scene katrine_stage5_event_5
    "Making small talk for a short while, a waitress soon delivers another large meal to your table."
    image katrine_stage5_event_6 = "/katrine/events/stage5/6.webp"
    scene katrine_stage5_event_6
    katrine "It’s a good thing you are not put off by women eating big meals."
    katrine "I've been living off reheated pasta for the last few days when working flat out."
    katrine "So I have been looking forward to another reward like this."
    image katrine_stage5_event_7 = "/katrine/events/stage5/7.webp"
    scene katrine_stage5_event_7
    "Grabbing the first burger Katrine can't help but moan in delight as she takes a bite."
    image katrine_stage5_event_8 = "/katrine/events/stage5/8.webp"
    scene katrine_stage5_event_8
    "Her attention now split between you and her food, you definitely feel like the meal is getting more of it than you."
    "Not that you mind."
    image katrine_stage5_event_9 = "/katrine/events/stage5/9.webp"
    scene katrine_stage5_event_9
    "Slurping the last of her large soda Katrine lets out a content sigh."
    katrine "I really needed that."
    image katrine_stage5_event_10 = "/katrine/events/stage5/10.webp"
    scene katrine_stage5_event_10
    katrine "But I guess it's time to pay off that meal."
    pc "Pay off?"
    image katrine_stage5_event_11 = "/katrine/events/stage5/11.webp"
    scene katrine_stage5_event_11
    katrine "Work off, in the gym."
    pc "Oh, right."
    "You follow a visually stuffed Katrine to the gym. Making note that she very slightly has started to waddle in her glutted state."
    stop music fadeout 1.0

    ###Gym, near the treadmill with Katrine maybe still looking a little bloated.”
    image katrine_stage5_event_12 = "/katrine/events/stage5/12.webp"
    scene katrine_stage5_event_12
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    katrine "Figure the treadmill might be a good place to start with some cardio."
    pc "Sure thing."
    image katrine_stage5_event_13 = "/katrine/events/stage5/13.webp"
    scene katrine_stage5_event_13
    "Starting her run on the treadmill it's easy to see Katrine is having more trouble than usual."
    image katrine_stage5_event_14 = "/katrine/events/stage5/14.webp"
    scene katrine_stage5_event_14
    "Her full and bloated body making it more difficult to hit her usual speeds."
    "Sweat begins to pour off her as she forces herself to keep going, but after only ten minutes she is forced to stop, breathing heavily."
    image katrine_stage5_event_15 = "/katrine/events/stage5/15.webp"
    scene katrine_stage5_event_15
    katrine "Oooh, is it me or is it hotter than normal in here?"
    pc "Maybe a little."
    image katrine_stage5_event_16 = "/katrine/events/stage5/16.webp"
    scene katrine_stage5_event_16
    katrine "Must be. Think you can get a drink? I think I need some more energy."
    pc "Sure thing."

    ###Trista behind the counter looking unimpressed###
    image katrine_stage5_event_17 = "/katrine/events/stage5/17.webp"
    scene katrine_stage5_event_17
    pc "Hi, Trista. Can I get a large soda, please?"
    trista "Sure thing."

    ###Katrine appears holding a snack####
    image katrine_stage5_event_18 = "/katrine/events/stage5/18.webp"
    scene katrine_stage5_event_18
    katrine "Hey, any chance you can make it an extra large?"
    trista "Are you sure that’s a good idea?"
    image katrine_stage5_event_19 = "/katrine/events/stage5/19.webp"
    scene katrine_stage5_event_19
    katrine "What does that mean?" ##Scowling at Trista###
    trista "I'm just saying that by the looks of it, you have been eating and drinking more calories than you are working off lately."
    image katrine_stage5_event_20 = "/katrine/events/stage5/20.webp"
    scene katrine_stage5_event_20
    katrine "Excuse me?"
    trista "What? I'm not judging, but you are not exactly as slim as you were when you started."
    image katrine_stage5_event_21 = "/katrine/events/stage5/21.webp"
    scene katrine_stage5_event_21
    katrine "You're one to talk. I'm surprised you even fit through the door with that ass!"
    trista "Ha, that just shows how little you really understand."
    image katrine_stage5_event_22 = "/katrine/events/stage5/22.webp"
    scene katrine_stage5_event_22
    trista "This isn't fat. It's muscle mass, ready to be transformed into pure power."
    trista "It’s a necessary step for any champion."
    katrine "Whatever you say, but I'm just as fit as I ever was."
    katrine "In fact, I'll prove it. My usual 1k time is under five minutes."
    image katrine_stage5_event_23 = "/katrine/events/stage5/23.webp"
    scene katrine_stage5_event_23
    katrine "[playername], you time me and we will all see I'm still as fast and as fit."
    "Getting out your phone you got to set a timer for five minutes as Katrine moves back to the treadmill."
    "But after you show them both the timer, you subtly add a couple of extra minutes just in case."
    image katrine_stage5_event_24 = "/katrine/events/stage5/24.webp"
    scene katrine_stage5_event_24
    "Grabbing the extra large soda from the stand Katrine sucks it down in a single go."
    katrine "Right then, you ready?"
    pc "Yep."
    image katrine_stage5_event_25 = "/katrine/events/stage5/25.webp"
    scene katrine_stage5_event_25
    "With the press of a button the treadmill starts up and Katrine’s one kilometre run with it."
    image katrine_stage5_event_26 = "/katrine/events/stage5/26.webp"
    scene katrine_stage5_event_26
    "To start with, everything was going well, but soon you could see the exertion on her face as she tried to keep up her pace."
    "Slowly but surely her speed decreases, even having to slow the machine slightly."
    image katrine_stage5_event_27 = "/katrine/events/stage5/27.webp"
    scene katrine_stage5_event_27
    "Her extra weight was clearly affecting her as she did her best to keep going."
    pc "Come on, Katrine. You can do this."
    "But looking at the time, it was a good thing you added those extra minutes as the five minute mark soon passes."
    image katrine_stage5_event_28 = "/katrine/events/stage5/28.webp"
    scene katrine_stage5_event_28
    "But with seconds to spare Katrine breathlessly hits the 1km mark, the alarm on your phone sounding moments after the machine had stopped."
    katrine "See…I…Still…Got it."
    katrine "Maybe like, ten seconds slower, maybe fifteen."
    image katrine_stage5_event_29 = "/katrine/events/stage5/29.webp"
    scene katrine_stage5_event_29
    "Wiping away a layer of sweat from her red face, it is clear that the run has had an impact on her."
    katrine "I think I'm just tired today."
    image katrine_stage5_event_30 = "/katrine/events/stage5/30.webp"
    scene katrine_stage5_event_30
    trista "Suuure. Well, you certainly proved me wrong." ###Sarcastic / eye rolling expression###
    image katrine_stage5_event_31 = "/katrine/events/stage5/31.webp"
    scene katrine_stage5_event_31
    "Looking your way Trista gives you a little nod as if asking you to join her."
    "Behind her you can see a table laid out with a large number of snacks again."
    image katrine_stage5_event_32 = "/katrine/events/stage5/32.webp"
    scene katrine_stage5_event_32
    katrine "Pfff. Man, that was tough though."
    pc "Are you ok?"
    katrine "Yeah, fine. Must have just overworked myself."
    pc "You had been working hard on that written piece too."
    image katrine_stage5_event_33 = "/katrine/events/stage5/33.webp"
    scene katrine_stage5_event_33
    katrine "Yeah, that's a good point. Plus, skipping the gym a few times because of... work probably means I lost a bit of my edge."
    katrine "Or maybe it was my diet, I wasn't eating that well lately."
    image katrine_stage5_event_34 = "/katrine/events/stage5/34.webp"
    scene katrine_stage5_event_34
    katrine "For now though, I think I'm going to head back to Bunny Bites. Nothing like a run to work up an appetite."
    "You wonder how she could still be hungry after everything she ate less than two hours ago."
    image katrine_stage5_event_35 = "/katrine/events/stage5/35.webp"
    scene katrine_stage5_event_35
    katrine "You want to join me?"
    pc "I think I still need to get my workout in first if I want to keep up with you."
    image katrine_stage5_event_36 = "/katrine/events/stage5/36.webp"
    scene katrine_stage5_event_36
    katrine "Suit yourself. See you around, [playername]."

    ###Trista next to counter with a bunch of snacks###
    image katrine_stage5_event_37 = "/katrine/events/stage5/37.webp"
    scene katrine_stage5_event_37
    "Waiting for Katrine to leave you quickly join Trista, who is already snacking away."
    pc "Hey, Trista, did you need a hand with something?"
    image katrine_stage5_event_38 = "/katrine/events/stage5/38.webp"
    scene katrine_stage5_event_38
    trista "Sure do. I need your help eating."
    pc "Uhhh…"
    "Had she just said that, or was it just wishful thinking?"
    image katrine_stage5_event_39 = "/katrine/events/stage5/39.webp"
    scene katrine_stage5_event_39
    trista "Come on, don’t be weird about it."
    trista "I need to eat more and more to pack on the weight to transfer it to muscle mass."
    pc "I can definitely help with that, but what do you want me to do?"
    trista "Well, as with anything, efficiency is key."
    trista "I just need you to open the boxes and hand me things so that I can pack in as much as quickly as I can in twenty minutes."
    pc "So that your stomach doesn't have time to tell your brain you're full, right?"
    image katrine_stage5_event_40 = "/katrine/events/stage5/40.webp"
    scene katrine_stage5_event_40
    trista "I'm impressed. Not just a pretty face."
    pc "I occasionally pay attention in class, a lot more lately."
    trista "Well, that might come in handy. Now, get over here and help me."

    #[Stuffing mini game]
    image katrine_stage5_event_44 = "/katrine/events/stage5/44.webp"
    scene katrine_stage5_event_44
    trista "Mmm. Now, this is efficient training."
    image katrine_stage5_event_45 = "/katrine/events/stage5/45.webp"
    scene katrine_stage5_event_45
    trista "Mmm, they taste amazing. Keep going, I need all the calories I can get."
    image katrine_stage5_event_46 = "/katrine/events/stage5/46.webp"
    scene katrine_stage5_event_46
    trista "Yes, keep feeding me. Fill me up to my capacity."
    image katrine_stage5_event_47 = "/katrine/events/stage5/47.webp"
    scene katrine_stage5_event_47
    trista "Plenty of room left. Don't stop feeding me!"
    image katrine_stage5_event_48 = "/katrine/events/stage5/48.webp"
    scene katrine_stage5_event_48
    "Her belly is growing bigger from this latest binge, but she clearly wants you to continue."
    image katrine_stage5_event_49 = "/katrine/events/stage5/49.webp"
    scene katrine_stage5_event_49
    trista "My belly is feeling full, but let’s keep going. Need to push my limits!"
    image katrine_stage5_event_50 = "/katrine/events/stage5/50.webp"
    scene katrine_stage5_event_50
    trista "I feel so stuffed, but no pain no gains."
    image katrine_stage5_event_51 = "/katrine/events/stage5/51.webp"
    scene katrine_stage5_event_51
    window hide
    pause
    image katrine_stage5_event_52 = "/katrine/events/stage5/52.webp"
    scene katrine_stage5_event_52
    pause
    image katrine_stage5_event_53 = "/katrine/events/stage5/53.webp"
    scene katrine_stage5_event_53
    pause
    image katrine_stage5_event_54 = "/katrine/events/stage5/54.webp"
    scene katrine_stage5_event_54
    trista "Ok, I think I’m at my limit now. We might have to stop."
    pc "I think you can eat one more thing. You wanted to push your limits, right?"
    trista "Ok, you're right. I can squeeze in one more."
    image katrine_stage5_event_55 = "/katrine/events/stage5/55.webp"
    scene katrine_stage5_event_55
    "Finishing up, her belly has grown substantially from when you started. Packed tight with fattening treats."

    #After Stuffing
    image katrine_stage5_event_41 = "/katrine/events/stage5/41.webp"
    scene katrine_stage5_event_41
    trista "Wow, I'm so full."
    trista "You are pretty good at that, almost like you have had practice."
    pc "Well, I do manage to feed myself most days."
    image katrine_stage5_event_42 = "/katrine/events/stage5/42.webp"
    scene katrine_stage5_event_42
    trista "Well, if you are ok with it I would love to have you help me train for this."
    pc "If all I have to do is hand you food, then sure, I'd be happy to help."
    image katrine_stage5_event_43 = "/katrine/events/stage5/43.webp"
    scene katrine_stage5_event_43
    trista "Great! See you around."

    ###Outside####
    "That was amazing. You can't wait to help Trista eat again."
    stop music fadeout 1.0
    #Unlocks Trista stuffing scene at gym after workout.
    if recollection == False:
        $ trista.weight += 1
        $ katrine.weight += 0.5
        $ daytime += 1
        $ phonecall = 1
    $ katrinestage5event = 0
    return

label KatrineStage5Phone:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Katrine', dialogue=dialogue_one)
    $ msg ("Do you think I am getting fat?", who=1)
    pause
    $ msg (None, who=1, pic="stage5_katrine")
    pause
    $ msg ("Maybe Trista is right?", who=1)
    pause
    $ msg ("You look beautiful.")
    pause
    $ msg ("You're too sweet.", who=1)
    pause
    $ msg ("But you're right, I am sure it's just Trista getting into my head.", who=1)
    pause
    $ msg ("Thanks, hope you are having a good day!", who=1)
    pause
    $ hide_messenger()

    $ katrinestage5phone = 0
    return


label Katrine_Stage_6_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Katrine', dialogue=dialogue_one)
    $ msg ("Hey, [playername]. Want to go to the café?", who=1)
    pause
    $ msg ("Let's call it a date.", who=1)
    pause
    menu:
        "Join Katrine.":
            $ hide_messenger()
        "Do something else.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    ###Cafe into with just PC###
    scene date_cafe
    "Arriving a couple of minutes early you grab a booth and wait for Katrine."
    "It doesn’t take long for Katrine to arrive."
    image katrine_date_arrive_event6 = "/katrine/6/date_arrive.webp"
    scene katrine_date_arrive_event6
    pc "Hey, Katrine."
    katrine "Hey. Have you ordered yet?"
    pc "No. I'm not hungry, so just get whatever you want."
    katrine "Ok, sure."
    image katrine_stage6_event_29 = "/katrine/events/stage6/29.webp"
    scene katrine_stage6_event_29
    "Looking over at the menu, you notice her considering her options for the first time."
    pc "Anything wrong?"
    image katrine_stage6_event_30 = "/katrine/events/stage6/30.webp"
    scene katrine_stage6_event_30
    katrine "No. I just can't believe what Trista said about me gaining weight."
    katrine "You don’t think I have, do you?"
    image katrine_stage6_event_31 = "/katrine/events/stage6/31.webp"
    scene katrine_stage6_event_31
    "Leaning back Katrine gives you a good view of her body, as if the gains she had undergone were so small they would be hard to notice."
    "Despite wanting to tell the truth, you know the answer to this question is always no."
    pc "No, I don't think so. Even if you did, it looks good on you."
    image katrine_stage6_event_32 = "/katrine/events/stage6/32.webp"
    scene katrine_stage6_event_32
    katrine "You are right. It's definitely just Trista projecting her own weight gain onto me."
    katrine "It's like she is totally oblivious to her own weight gain. Can you imagine?"
    pc "Yeah…right."
    image katrine_stage6_event_33 = "/katrine/events/stage6/33.webp"
    scene katrine_stage6_event_33
    "Thinking for a moment you watch Katrine go up and order her usually large set of pastries and coffee."
    "Returning a few moments later she places them all on the table."
    image katrine_stage6_event_38 = "/katrine/events/stage6/38.webp"
    scene katrine_stage6_event_38
    katrine "Well, since I've not gained, there's no reason to starve myself, right?"
    pc "No, that would be a bit extreme."
    "Starting to eat you are happy to see a smile reappearing on Katrine's face as she enjoys her sweet treats."
    pc "So, what have you been up to recently?"
    image katrine_stage6_event_34 = "/katrine/events/stage6/34.webp"
    scene katrine_stage6_event_34
    katrine "Oh, actually I got contacted to write a piece on female fitness for a magazine based here in town."
    pc "That's great! I can't think of anyone better."
    katrine "Yeah. It's super fun to be writing about something I care about again."
    image katrine_stage6_event_39 = "/katrine/events/stage6/39.webp"
    scene katrine_stage6_event_39
    "Taking another bite she seems oblivious to the strangeness of her talking fitness while stuffing her face."
    katrine "It's a bit more personal this one. They want some stories about how to stay motivated."
    katrine "Which is easy for me because it's all about doing it to treat yourself with something else."
    pc "True. It does help to have something to keep you going week after week."
    image katrine_stage6_event_35 = "/katrine/events/stage6/35.webp"
    scene katrine_stage6_event_35
    katrine "So why do you work out? What keeps you going?"
    pc "Uh, I'm not really sure."
    pc "I guess I don't do it as religiously as you do. I just do it when I want to, so maybe my motivation is just feeling like it?"
    katrine "That might be a little wishy washy for this piece."
    pc "That’s why you’re the writer."
    image katrine_stage6_event_40 = "/katrine/events/stage6/40.webp"
    scene katrine_stage6_event_40
    "Over the next hour you watch Katrine eat and make small talk."
    image katrine_stage6_event_36 = "/katrine/events/stage6/36.webp"
    scene katrine_stage6_event_36
    "It doesn’t take her long to demolish the rest of her pastries, her belly bulging slightly in her tight dress."
    image katrine_stage6_event_37 = "/katrine/events/stage6/37.webp"
    scene katrine_stage6_event_37
    katrine "So, I was wondering if you wanted to head to Velvet Shadows tonight?"
    pc "Sure. I'll see you tonight then."
    image katrine_stage6_event_41 = "/katrine/events/stage6/41.webp"
    scene katrine_stage6_event_41
    "You say goodbye to Katrine and take a quick shower before heading to Velvet Shadows."

    ### Nightlcub with usual crowd###
    image katrine_stage6_event_1 = "/katrine/events/stage6/1.webp"
    scene katrine_stage6_event_1
    play music "/music/stripclub.ogg" if_changed
    "You meet Katrine in Velvet Shadows."
    pc "Hey, Katrine. You look amazing."
    katrine "Thank you. Let's sit at the bar."
    image katrine_stage6_event_2 = "/katrine/events/stage6/2.webp"
    scene katrine_stage6_event_2
    bartender "Hi. How can I help?"
    katrine "Can we get two beers, please?"
    bartender "Sure thing. Do you have a champions card?"
    image katrine_stage6_event_3 = "/katrine/events/stage6/3.webp"
    scene katrine_stage6_event_3
    katrine "Champions card?"
    bartender "Sorry. Each month we run a contest to get free drinks."
    bartender "All you have to do is beat the challenge set by the previous winners."
    image katrine_stage6_event_4 = "/katrine/events/stage6/4.webp"
    scene katrine_stage6_event_4
    katrine "What's the challenge? I'm sure we can beat it, right, [playername]?"
    bartender "It's a drinking challenge. It starts at five beers in twenty minutes, but currently it's ten beers."
    image katrine_stage6_event_5 = "/katrine/events/stage6/5.webp"
    scene katrine_stage6_event_5
    katrine "So just drink ten beers now and then everything is free the rest of the month?"
    bartender "Yep. But be quick; someone can take this challenge at any time and increase the number of drinks."
    image katrine_stage6_event_6 = "/katrine/events/stage6/6.webp"
    scene katrine_stage6_event_6
    katrine "Well, that should be easy. Get the drinks ready."
    bartender "Sure thing. Ten beers coming right up."
    image katrine_stage6_event_7 = "/katrine/events/stage6/7.webp"
    scene katrine_stage6_event_7
    katrine "I'm going to need to come here more often if this is a regular thing."
    bartender "Here are your drinks."
    image katrine_stage6_event_8 = "/katrine/events/stage6/8.webp"
    scene katrine_stage6_event_8
    "Katrine goes to hand you a drink before the bartender stops her."
    bartender "Sorry if I wasn’t clear, it's an individual challenge."
    image katrine_stage6_event_9 = "/katrine/events/stage6/9.webp"
    scene katrine_stage6_event_9
    katrine "Wait, so I have to drink all ten beers?"
    bartender "Yes. Unless you want to pay for them all."
    katrine "I guess it's a good thing I did this a lot in college."
    image katrine_stage6_event_10 = "/katrine/events/stage6/10.webp"
    scene katrine_stage6_event_10
    "Grabbing the first beer, Katrine watches as the timer is started and puts the beer to her lips."
    image katrine_stage6_event_11 = "/katrine/events/stage6/11.webp"
    scene katrine_stage6_event_11
    "The first one disappears in just a few seconds as she sucks it down greedily."
    image katrine_stage6_event_12 = "/katrine/events/stage6/12.webp"
    scene katrine_stage6_event_12
    "By the fourth there is some visible discomfort on her face as Katrine chugs."
    image katrine_stage6_event_13 = "/katrine/events/stage6/13.webp"
    scene katrine_stage6_event_13
    "On the fifth she is finally forced to pause for the first time."
    image katrine_stage6_event_14 = "/katrine/events/stage6/14.webp"
    scene katrine_stage6_event_14 with vpunch
    katrine "Buuurpp."
    image katrine_stage6_event_15 = "/katrine/events/stage6/15.webp"
    scene katrine_stage6_event_15
    katrine "Ugh, they are so gassy."
    katrine "I feel like I'm blowing up with air."
    image katrine_stage6_event_16 = "/katrine/events/stage6/16.webp"
    scene katrine_stage6_event_16
    "Looking down, it's clear to see why. Her expanded stomach is growing with each mouthful of gassy beer."
    pc "Come on, you can do it. You are more than halfway there."
    katrine "I remember why I stopped doing these, especially after the last time."
    pc "Last time?"
    katrine "It was a drinking contest with some friends. They loved how much I could drink."
    katrine "So they kept entering me into them, one after another."
    image katrine_stage6_event_17 = "/katrine/events/stage6/17.webp"
    scene katrine_stage6_event_17
    "Grabbing the glass she quickly finishes another one off and goes for the next."
    image katrine_stage6_event_18 = "/katrine/events/stage6/18.webp"
    scene katrine_stage6_event_18
    katrine "Eventually, I was so bloated, I burst right out of my tight dress."
    katrine "They never let me forget that, but I did win the contest."
    "Picking up the next glass Katrine tips it back slowly."
    "One by one she continues to empty the drinks, her stomach continuing to expand."
    image katrine_stage6_event_19 = "/katrine/events/stage6/19.webp"
    scene katrine_stage6_event_19 with vpunch
    katrine "Burrrpp."
    image katrine_stage6_event_20 = "/katrine/events/stage6/20.webp"
    scene katrine_stage6_event_20
    katrine "Ugh, that’s nine and I think I'm going to be sick."
    pc "You still have five minutes and it's just one more."
    image katrine_stage6_event_21 = "/katrine/events/stage6/21.webp"
    scene katrine_stage6_event_21
    "Grabbing her bloated belly, Katrine is looking quite uncomfortable."
    katrine "I don't think I can. I'm so full of beer and air."
    pc "Just one more. You are almost there."
    image katrine_stage6_event_22 = "/katrine/events/stage6/22.webp"
    scene katrine_stage6_event_22
    "Picking up the last beer Katrine raises it to her mouth."
    "Slowly the liquid drains from the glass."
    image katrine_stage6_event_23 = "/katrine/events/stage6/23.webp"
    scene katrine_stage6_event_23
    "With a few minutes to spare Katrine places the last glass down triumphantly."
    pc "Well done!"
    image katrine_stage6_event_24 = "/katrine/events/stage6/24.webp"
    scene katrine_stage6_event_24
    katrine "Ughh."
    image katrine_stage6_event_25 = "/katrine/events/stage6/25.webp"
    scene katrine_stage6_event_25 with vpunch
    katrine "Buuurrrrrppppp."
    katrine "Thanks."
    image katrine_stage6_event_26 = "/katrine/events/stage6/26.webp"
    scene katrine_stage6_event_26
    "Placing her hands on her giant stomach it's clear despite winning she doesn’t feel too good."
    bartender "Congratulations! You drink for free for the rest of the month."
    image katrine_stage6_event_27 = "/katrine/events/stage6/27.webp"
    scene katrine_stage6_event_27
    katrine "Thanks. Although, I think this might be enough for tonight."
    katrine "I'm definitely out of practice."
    katrine "Sorry to call our night early, but I think I better go find somewhere to lie down."
    image katrine_stage6_event_28 = "/katrine/events/stage6/28.webp"
    scene katrine_stage6_event_28
    pc "It's no problem, I enjoyed our night together."
    katrine "Thanks, me too."
    stop music fadeout 1.0
    if recollection == False:
        $ daytime += 1
        $ katrine.weight += 1
        $ phonecall = 1
    $ katrinestage6event = 0
    return

label KatrineStage6Phone:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Katrine', dialogue=dialogue_one)
    $ msg ("Sorry for ditching you last night, I really didn’t feel good.", who=1)
    pause
    $ msg ("I was so bloated I could barely get to sleep.", who=1)
    pause
    $ msg ("It’s like all the liquid sloshed around in me.", who=1)
    pause
    $ msg ("No need to apologise, I just hope you are feeling better now?")
    pause
    $ msg ("Much, thanks.", who=1)
    pause
    $ msg ("Maybe we can have another date soon so I can make it up to you?", who=1)
    pause
    $ msg (None, who=1, pic="stage6_katrine")
    pause
    $ msg ("You don't have to tempt me twice.")
    pause
    $ msg ("Great, I’ll let you know next time I am free.", who=1)
    pause
    $ hide_messenger()

    $ katrinestage6phone = 0
    return

label Katrine_Stage_7_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Katrine', dialogue=dialogue_one)
    $ msg ("Hey, [playername]. Want to join me at Velvet Shadows?", who=1)
    pause
    $ msg ("I could use someone to talk to.", who=1)
    pause
    menu:
        "Join Katrine.":
            $ hide_messenger()
        "Do something else.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    ###Nightclub with Katrine already at the bar.####
    image katrine_stage7_event_1 = "/katrine/events/stage7/1.webp"
    scene katrine_stage7_event_1
    play music "/music/stripclub.ogg" if_changed
    "Walking in, you spot Katrine sitting at the bar - a few empty glasses standing next to her already."
    pc "Hey, Katrine. Everything okay?"
    image katrine_stage7_event_2 = "/katrine/events/stage7/2.webp"
    scene katrine_stage7_event_2
    katrine "No, it's not."
    katrine "Trista was right."
    pc "About what?"
    image katrine_stage7_event_3 = "/katrine/events/stage7/3.webp"
    scene katrine_stage7_event_3
    katrine "Isn't it obvious? Look at me."
    katrine "I have gained weight and not just a tiny bit, but a lot."
    image katrine_stage7_event_4 = "/katrine/events/stage7/4.webp"
    scene katrine_stage7_event_4
    katrine "I can't believe I have been so oblivious to it. I didn't realise till I weighed myself for my article."
    pc "So what if you have? You still look amazing."
    image katrine_stage7_event_5 = "/katrine/events/stage7/5.webp"
    scene katrine_stage7_event_5
    katrine "Really?"
    pc "Absolutely."
    katrine "But that isn’t the point."
    image katrine_stage7_event_6 = "/katrine/events/stage7/6.webp"
    scene katrine_stage7_event_6
    katrine "I knew I had been overeating a bit, but just thought I could work it all off."
    katrine "How can I write a story about female fitness like this?"
    pc "Maybe you could use it for inspiration?"
    image katrine_stage7_event_7 = "/katrine/events/stage7/7.webp"
    scene katrine_stage7_event_7
    katrine "That's not a bad idea, actually!"
    katrine "It's actually perfect! I could do a journey on my weight loss."
    katrine "It will be a source of inspiration for myself, although I'm not sure if I can manage it."
    pc "You look great as you are, so don't push yourself too hard."
    if persistent.imperial:
        pc "But didn’t you also say you were 250 pounds before? You managed to lose a lot of that."
    else:
        pc "But didn’t you also say you were 110 kilograms before? You managed to lose a lot of that."
    image katrine_stage7_event_8 = "/katrine/events/stage7/8.webp"
    scene katrine_stage7_event_8
    katrine "You are right again. Although, it is a bit frustrating to have gained it all back."
    katrine "Not that the eating wasn't fun, but this isn’t anything I haven’t done before."
    katrine "It will probably take a lot more effort, and probably some stupid dieting."
    pc "Still not a fan of dieting?"
    image katrine_stage7_event_9 = "/katrine/events/stage7/9.webp"
    scene katrine_stage7_event_9
    katrine "What, being hungry all the time and not being able to eat anything you want to?"
    katrine "It's like a personal hell, but I guess it's one I have to put up with."
    pc "Well, like I said, don't push yourself too hard."
    image katrine_stage7_event_10 = "/katrine/events/stage7/10.webp"
    scene katrine_stage7_event_10
    katrine "I can manage it, just a couple of months to get back to where I was."
    katrine "It could be even less if I work out twice as hard as I had been."
    "Pausing for a moment your conversation is interrupted by a loud gurgle from Katrine's stomach."
    image katrine_stage7_event_11 = "/katrine/events/stage7/11.webp"
    scene katrine_stage7_event_11
    katrine "Sorry." ###Blushing###
    pc "Sounds like your stomach doesn’t agree."
    katrine "I may have skipped dinner because I was panicking about my weight."
    pc "You don’t need to panic."
    image katrine_stage7_event_12 = "/katrine/events/stage7/12.webp"
    scene katrine_stage7_event_12
    katrine "I know. In a weird way, I kind of enjoy being larger."
    katrine "Maybe my diet can start tomorrow. I am pretty hungry."
    image katrine_stage7_event_13 = "/katrine/events/stage7/13.webp"
    scene katrine_stage7_event_13
    katrine "Fancy a bite to eat at Bunny Bites?"
    pc "Sure thing."
    "With concerns over her weight put aside for now, you eagerly usher your ever growing gym partner out the door."
    "With thoughts of Katrine’s anticipated binge on your mind, you both make your way to Bunny Bites."
    stop music fadeout 1.0

    ### Bunny Bites in booth with Katrine ###
    image katrine_stage7_event_14 = "/katrine/events/stage7/14.webp"
    scene katrine_stage7_event_14
    play music "/music/bunny_bites.ogg" if_changed
    katrine "Everything smells so much better when you are hungry."
    katrine "What should I get for my last meal? It's all so tempting."
    pc "Last meal? Sounds a bit dramatic."
    pc "But why not treat yourself?"
    image katrine_stage7_event_15 = "/katrine/events/stage7/15.webp"
    scene katrine_stage7_event_15
    katrine "Mmmm, treat myself."
    "Soon a waitress arrives to take your order."

    ###Marie at table###
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    katrine "Can I get a whole pizza, a double cheeseburger, some fries, onion rings, a milkshake and a large soda, please?"
    pc "I'll just get a burger and fries, please."
    marie "Coming right up."
    ###Marie leaves table###
    image katrine_stage7_event_16 = "/katrine/events/stage7/16.webp"
    scene katrine_stage7_event_16
    katrine "Was that too much?"
    pc "No. Think of it as two meals' worth since you skipped lunch."
    image katrine_stage7_event_17 = "/katrine/events/stage7/17.webp"
    scene katrine_stage7_event_17
    katrine "True. Maybe I should have ordered more then."
    "A few minutes later the table is covered in Katrine's food, but it's more than she ordered."

    ###Marie back at table###
    image katrine_stage7_event_18 = "/katrine/events/stage7/18.webp"
    scene katrine_stage7_event_18
    katrine "Whoa, this is more than I ordered. I think the orders might have got mixed up."
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "I'm so sorry about the mix-up. Don't worry about paying for anything you didn't order, it's on the house."
    katrine "Well, I don't want to say no to free food."
    marie "Okay, great. Sorry again. I will go and find out what happened to your order."
    "It wouldn't take a genius to figure out what had happened knowing Marie."

    ###Just you and Katrine in booth###
    image katrine_stage7_event_19 = "/katrine/events/stage7/19.webp"
    scene katrine_stage7_event_19
    pc "Well, you did think you should have ordered more."
    katrine "Not this much extra though."
    katrine "Mmm, but this all smells so good. I don't know where to start."
    image katrine_stage7_event_20 = "/katrine/events/stage7/20.webp"
    scene katrine_stage7_event_20
    "Grabbing the burger Katrine takes a hearty bite out of it before cramming fries and onion rings in."
    image katrine_stage7_event_21 = "/katrine/events/stage7/21.webp"
    scene katrine_stage7_event_21
    "It's clear her hunger is overpowering her reluctance as she grabs a slice of pizza with her other hand."
    image katrine_stage7_event_22 = "/katrine/events/stage7/22.webp"
    scene katrine_stage7_event_22
    "Soon the first burger, fries and half the pizza have disappeared into her growing stomach."
    image katrine_stage7_event_23 = "/katrine/events/stage7/23.webp"
    scene katrine_stage7_event_23
    "Pausing for a moment Katrine leans over and grabs a soda, sucking it down in one go."
    image katrine_stage7_event_24 = "/katrine/events/stage7/24.webp"
    scene katrine_stage7_event_24
    "Adjusting herself in the booth to give her belly more room she grabs another slice of pizza."
    image katrine_stage7_event_25 = "/katrine/events/stage7/25.webp"
    scene katrine_stage7_event_25
    "Sitting in almost silence you watch Katrine gorge herself on her meal."
    image katrine_stage7_event_26 = "/katrine/events/stage7/26.webp"
    scene katrine_stage7_event_26
    "It doesn’t take long for the rest of the giant meal to disappear as Katrine leans back."
    image katrine_stage7_event_27 = "/katrine/events/stage7/27.webp"
    scene katrine_stage7_event_27
    katrine "I can’t believe I ate it all."
    pc "Seemed like you really enjoyed it though."
    katrine "I did. Sorry for the lack of conversation."
    pc "It's okay. I'm glad you enjoyed yourself."

    ###Marie comes back to table###
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Sorry about the mix-up. Here is your order."
    katrine "What?"
    katrine "But I just ate my order."
    marie "I thought you ordered a whole pizza, a double cheeseburger, some fries, onion rings, a milkshake and a large soda?"
    katrine "I did but…"
    image katrine_stage7_event_28 = "/katrine/events/stage7/28.webp"
    scene katrine_stage7_event_28
    "Looking down Katrine grimaces slightly as she rubs her big belly."
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "If you don't want it I can throw it away."
    katrine "No, I wouldn’t want to waste food."
    image katrine_stage7_event_29 = "/katrine/events/stage7/29.webp"
    scene katrine_stage7_event_29
    "Watching the plates get piled up on the table once more Katrine was clearly concerned."
    image katrine_stage7_event_30 = "/katrine/events/stage7/30.webp"
    scene katrine_stage7_event_30
    "Despite being stuffed to the limit she reluctantly picked up the double cheeseburger and began eating again."
    "This time her eating was far slower and much more laboured."
    image katrine_stage7_event_31 = "/katrine/events/stage7/31.webp"
    scene katrine_stage7_event_31
    "Katrine may have loved food, but even so there is a limit to how much one person can eat comfortably."
    image katrine_stage7_event_32 = "/katrine/events/stage7/32.webp"
    scene katrine_stage7_event_32
    "Forcing herself to eat slowly, the entire pizza followed the burger into her still growing stomach."
    image katrine_stage7_event_33 = "/katrine/events/stage7/33.webp"
    scene katrine_stage7_event_33
    "Finally the fries, onion rings and soda followed. But picking up the milkshake, Katrine could take no more."
    image katrine_stage7_event_34 = "/katrine/events/stage7/34.webp"
    scene katrine_stage7_event_34
    katrine "Ughh, I'm so full. I can barely move."
    pc "It's ok, you don’t have to finish the milkshake."
    image katrine_stage7_event_35 = "/katrine/events/stage7/35.webp"
    scene katrine_stage7_event_35
    katrine "But I hate to waste food."
    pc "Maybe take it home with you."
    katrine "No, it's okay. I can do this. It's just one drink."
    image katrine_stage7_event_36 = "/katrine/events/stage7/36.webp"
    scene katrine_stage7_event_36
    "Sucking on the straw the large cup of sugary sweet contents flowed up and into her body."
    image katrine_stage7_event_37 = "/katrine/events/stage7/37.webp"
    scene katrine_stage7_event_37
    "Placing the empty cup down on the table Katrine rested her hands on her giant stomach as if trying to keep it calm after filling it to the brim."
    image katrine_stage7_event_38 = "/katrine/events/stage7/38.webp"
    scene katrine_stage7_event_38
    katrine "I'm going to need a minute."
    pc "Is it weird to be impressed by that?"
    image katrine_stage7_event_39 = "/katrine/events/stage7/39.webp"
    scene katrine_stage7_event_39
    katrine "I wish I could say that’s the first time I've eaten this much."
    pc "Really?"
    image katrine_stage7_event_40 = "/katrine/events/stage7/40.webp"
    scene katrine_stage7_event_40
    katrine "Ughh, I used to binge like this all the time when I was younger."
    katrine "I was lucky then that nothing I ate changed my waistline, unlike now."
    katrine "But that’s a problem for tomorrow."
    image katrine_stage7_event_41 = "/katrine/events/stage7/41.webp"
    scene katrine_stage7_event_41
    "Standing you help the heavily stuffed Katrine to her feet and say your goodbyes."
    stop music fadeout 1.0
    if recollection == False:
        $ katrine.weight += 1
        $ daytime += 1
        $ phonecall = 1
    $ katrinestage7event = 0
    return

label Katrine_Stage_8_Event:
    ###Outside – coming back from the university in the rain####
    image katrine_stage8_event_1 = "/katrine/events/stage8/1.webp"
    scene katrine_stage8_event_1
    pc "Hey, is that Katrine?"
    ### Katrine bent over like she is the first time you meet###
    image katrine_stage8_event_2 = "/katrine/events/stage8/2.webp"
    scene katrine_stage8_event_2
    pc "Hey, Katrine. Everything okay?"
    katrine "Yeah, just a bit tired."
    pc "What are you doing out here in weather like this?"
    image katrine_stage8_event_3 = "/katrine/events/stage8/3.webp"
    scene katrine_stage8_event_3
    katrine "I…I can't face Trista knowing she was right."
    katrine "It would just be humiliating to have to admit I gained weight to her."
    pc "You still look amazing, but let's get out of this rain."
    pc "I live nearby. Why don't you come over?"
    image katrine_stage8_event_4 = "/katrine/events/stage8/4.webp"
    scene katrine_stage8_event_4
    katrine "That would be great."

    ### In PC house###
    image katrine_stage8_event_5 = "/katrine/events/stage8/5.webp"
    scene katrine_stage8_event_5
    katrine "Wow, this place is amazing."
    pc "Thanks. It's my parents', really. I just live here."
    pc "I don’t have any spare clothes that might fit you but I have some towels in there if you want to dry off."
    image katrine_stage8_event_6 = "/katrine/events/stage8/6.webp"
    scene katrine_stage8_event_6
    "Katrine quickly disappears into the bathroom to walk out in just her underwear a few minutes later."

    ###Katrine in her underwear ###
    image katrine_stage8_event_7 = "/katrine/events/stage8/7.webp"
    scene katrine_stage8_event_7
    pc "Not quite what I was thinking, but I'm definitely not going to complain."
    katrine "Oh, behave. Nothing you haven't already seen a million times."
    image katrine_stage8_event_8 = "/katrine/events/stage8/8.webp"
    scene katrine_stage8_event_8
    katrine "Well, maybe a bit more of me than last time."
    pc "Just means more of you to admire."
    image katrine_stage8_event_9 = "/katrine/events/stage8/9.webp"
    scene katrine_stage8_event_9
    katrine "Oh, shut up. When did you become so cheesy?"
    pc "Want a cup of coffee or something?"
    image katrine_stage8_event_10 = "/katrine/events/stage8/10.webp"
    scene katrine_stage8_event_10
    katrine "That would be great, thanks."
    "Grabbing a couple of mugs you make some hot drinks for the pair of you and join her on the sofa."

    ### Katrine and PC on the Sofa###
    image katrine_stage8_event_11 = "/katrine/events/stage8/11.webp"
    scene katrine_stage8_event_11
    pc "So, how have you been - other than avoiding Trista?"
    katrine "Honestly, terrible."
    image katrine_stage8_event_12 = "/katrine/events/stage8/12.webp"
    scene katrine_stage8_event_12
    katrine "I can't believe I didn't notice the weight gain. I'm so stupid."
    pc "You aren't stupid, you must have been feeling confident in yourself."
    pc "You don’t need to apologise for feeling good."
    image katrine_stage8_event_13 = "/katrine/events/stage8/13.webp"
    scene katrine_stage8_event_13
    katrine "I suppose so. You always know what to say."
    katrine "Something else I have been struggling with."
    image katrine_stage8_event_14 = "/katrine/events/stage8/14.webp"
    scene katrine_stage8_event_14
    "Looking down it's clear Katrine is in deep thought about something troubling her."
    pc "What do you mean?"
    image katrine_stage8_event_15 = "/katrine/events/stage8/15.webp"
    scene katrine_stage8_event_15
    katrine "The articles... How can I write something on female fitness?"
    katrine "I can't even string two sentences together at the moment. I've never had writer's block this badly before."
    pc "Maybe it's because you are forcing yourself to write it."
    pc "When you have talked about other projects you always seem to be interested or motivated to write about them."
    image katrine_stage8_event_16 = "/katrine/events/stage8/16.webp"
    scene katrine_stage8_event_16
    katrine "True. Writing this has felt like confronting the truth."
    pc "The truth?"
    image katrine_stage8_event_17 = "/katrine/events/stage8/17.webp"
    scene katrine_stage8_event_17
    katrine "I hate working out, I hate dieting, I hate everything that comes with them!"
    pc "But you seemed to enjoy them?"
    katrine "I was lying to myself. The truth is that most of the time I only ever worked out so I could eat more without feeling guilty."
    katrine "I'm such a slob and I’ll be a massive hypocrite if I write this article."
    pc "Then don't write it. Do something else."
    image katrine_stage8_event_18 = "/katrine/events/stage8/18.webp"
    scene katrine_stage8_event_18
    katrine "Like what? I thought this was going to be my big breakthrough story."
    katrine "Otherwise I'll be back to writing those pieces on the underground that two people read."
    pc "What about food?"
    image katrine_stage8_event_19 = "/katrine/events/stage8/19.webp"
    scene katrine_stage8_event_19
    katrine "What do you mean?"
    pc "Why don’t you write about food?"
    katrine "You mean like a critic?"
    pc "Why not? Or anything else about it. People love good reviews they can trust."
    image katrine_stage8_event_20 = "/katrine/events/stage8/20.webp"
    scene katrine_stage8_event_20
    katrine "True. But I can't just give up on the pieces I'm supposed to be writing. I have been paid to do them."
    katrine "Although, I could just be honest and write it for those of us with a bit more jiggle in the gym."
    pc "Sure. There are probably a lot of people out there who would love to read that."
    "Your conversation is cut off again by a loud rumble from Katrine's stomach."
    image katrine_stage8_event_21 = "/katrine/events/stage8/21.webp"
    scene katrine_stage8_event_21
    katrine "Sorry. I skipped breakfast and haven't eaten anything afterwards either."
    pc "Well, I don't have much in the house, but we could order something?"
    image katrine_stage8_event_22 = "/katrine/events/stage8/22.webp"
    scene katrine_stage8_event_22
    katrine "That sounds good."
    pc "Maybe we could do a test, see if you have what it takes to be a critic?"
    image katrine_stage8_event_23 = "/katrine/events/stage8/23.webp"
    scene katrine_stage8_event_23
    katrine "How?"
    pc "See if your descriptions match those on the website of where we order from."
    pc "Speaking of which, what do you fancy?"
    image katrine_stage8_event_24 = "/katrine/events/stage8/24.webp"
    scene katrine_stage8_event_24
    katrine "There is this new Mexican place in town I've been wanting to try out."
    pc "Sure thing. Be right back."
    image katrine_stage8_event_25 = "/katrine/events/stage8/25.webp"
    scene katrine_stage8_event_25
    "Grabbing your phone you call them, placing a sizable order for the two of you."
    "Half an hour later there is a knock at the door and you are handed a pair of large bags heavy with food."
    "Taking them to Katrine you start to unpack them."
    image katrine_stage8_event_26 = "/katrine/events/stage8/26.webp"
    scene katrine_stage8_event_26
    katrine "What is all this?"
    pc "I thought you wanted to give being a food critic a go?"
    pc "Is it too much?"
    image katrine_stage8_event_27 = "/katrine/events/stage8/27.webp"
    scene katrine_stage8_event_27
    katrine "I did, but this is a lot of food."
    katrine "I might not enjoy working out that much, but I'm not sure I want to gain more weight."
    pc "I can try and get the driver back and get a refund."
    image katrine_stage8_event_28 = "/katrine/events/stage8/28.webp"
    scene katrine_stage8_event_28
    "Despite her comments you can see Katrine eyeing the food, licking her lips at the delectable smell."
    katrine "Wait... maybe we could give it a go after all."
    katrine "I mean, I can spend the next week in the gym, right?"
    pc "But you just said you didn’t like working out?"
    image katrine_stage8_event_29 = "/katrine/events/stage8/29.webp"
    scene katrine_stage8_event_29
    katrine "I don’t, or at least not as much as I convinced myself I did."
    katrine "Sorry if this is a little confusing. I'm not really sure what to think myself."
    katrine "This is all still new to me."
    pc "You don't have to apologise to me. I just want you to be happy."
    image katrine_stage8_event_30 = "/katrine/events/stage8/30.webp"
    scene katrine_stage8_event_30
    katrine "Thank you and honestly I am. It feels good to admit this to someone, even if I'm not sure about what it means yet."
    katrine "I've just been so focused on working out that I never really took the time to think about why."
    pc "Well, it sounds like you need this treat than I thought."
    katrine "You're not wrong about that. Everything has been so stressful lately."
    katrine "Okay, let's get our heads in the game. What's first?"
    pc "We have two starters: tacos and burritos."
    image katrine_stage8_event_31 = "/katrine/events/stage8/31.webp"
    scene katrine_stage8_event_31
    "Grabbing the burrito Katrine digs in."
    katrine "Mmmm, this is good."
    pc "Not sure 'good' would make for much of a review."
    image katrine_stage8_event_32 = "/katrine/events/stage8/32.webp"
    scene katrine_stage8_event_32
    "Looking over Katrine gives you a look to let you know your sarcasm isn’t funny."
    katrine "Fine, I would say it is a beautifully wrapped burrito where the rich spice mix perfectly complements the beef filling."
    katrine  "While the occasional sharpness of an olive or sweetness of a raisin cuts through to give an extra burst of flavour."
    image katrine_stage8_event_33 = "/katrine/events/stage8/33.webp"
    scene katrine_stage8_event_33
    "Taking a few more bites Katrine enjoys the burrito, finishing it quickly."
    pc "Wow, that was a good description. I’d buy one if I read that."
    image katrine_stage8_event_34 = "/katrine/events/stage8/34.webp"
    scene katrine_stage8_event_34
    katrine "Really?"
    pc "Yeah. You're a natural."
    pc "To be honest I didn’t know how to describe the taste I was experiencing. Your description really brought the burrito to life."
    katrine "Thank you... What's next?"
    "Eyeing the pile eagerly, you point out the tacos."
    image katrine_stage8_event_35 = "/katrine/events/stage8/35.webp"
    scene katrine_stage8_event_35
    "Over the next hour you help Katrine go through the buffet of tacos, burritos and other Mexican or Spanish inspired dishes."
    "The first mouthfuls of each of them slow as she savoured the taste, before quickly devouring the rest."
    image katrine_stage8_event_36 = "/katrine/events/stage8/36.webp"
    scene katrine_stage8_event_36
    "As time went on the descriptions became less and less frequent, as Katrine instead just enjoyed eating."
    image katrine_stage8_event_37 = "/katrine/events/stage8/37.webp"
    scene katrine_stage8_event_37
    "Her belly now bulging out from the highly fatty and sloppy food she was still cramming into her mouth."
    image katrine_stage8_event_38 = "/katrine/events/stage8/38.webp"
    scene katrine_stage8_event_38
    "Handing over an extra large burrito Katrine takes a bite out of it, meat and beans almost escaping out the sides of it."
    image katrine_stage8_event_39 = "/katrine/events/stage8/39.webp"
    scene katrine_stage8_event_39
    "The stomach that had once complained about being empty, now groaning under the weight of everything she was filling it with."
    image katrine_stage8_event_40 = "/katrine/events/stage8/40.webp"
    scene katrine_stage8_event_40
    "Despite its size Katrine makes short work of it, smacking her lips satisfactorily after the last bite."
    "Reaching into the bag once more you find it empty."
    "You had clearly been too busy watching Katrine eat to pay any attention to what was left."
    pc "Well, looks like that was it."
    image katrine_stage8_event_41 = "/katrine/events/stage8/41.webp"
    scene katrine_stage8_event_41
    katrine "Good, I don’t think I could eat another bite."
    image katrine_stage8_event_42 = "/katrine/events/stage8/42.webp"
    scene katrine_stage8_event_42
    pc "Feel better now?"
    image katrine_stage8_event_43 = "/katrine/events/stage8/43.webp"
    scene katrine_stage8_event_43
    katrine "Definitely."
    katrine "Although maybe there is something else I could do with."
    image katrine_stage8_event_44 = "/katrine/events/stage8/44.webp"
    scene katrine_stage8_event_44
    "Giving you a look Katrine slowly removes her bra and beckons you over."
    image katrine_stage8_event_45 = "/katrine/events/stage8/45.webp"
    scene katrine_stage8_event_45
    "You follow Katrine into your bedroom as she climbs up your bed."
    if persistent.nosexscene == True:
        scene black
        "You and Trista had a wonderful time together."
        image katrine_stage8_event_46 = "/katrine/events/stage8/46.webp"
        scene katrine_stage8_event_46
        katrine "Thanks for today, babe. That was great."
        if recollection == False:
            $ katrine.weight += 1
        $ katrinestage8event = 0
        return
    image katrine_stage8_event_47 = "/katrine/events/stage8/47.webp"
    scene katrine_stage8_event_47
    "She takes of her panties and gets in position."
    katrine "Come take me from behind."
    image katrine_stage8_event_48 = "/katrine/events/stage8/48.webp"
    scene katrine_stage8_event_48
    "You quickly undress and take position behind her."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/katrine/events/stage8/49.webm" loop
    show movie with dissolve
    window hide
    pause
    "Doing as she asks, you insert your solid dick into her."
    "You start off slow, letting both of you get used to being inside each other."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/katrine/events/stage8/50.webm" loop
    show movie with dissolve
    window hide
    pause
    "Katrine's belly sloshing around as you thrust into her."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/katrine/events/stage8/51.webm" loop
    show movie with dissolve
    window hide
    pause
    "Katrine's moans become louder with every thrust you make."
    "Finally both of you climax together."
    stop movie
    image katrine_stage8_event_46 = "/katrine/events/stage8/46.webp"
    scene katrine_stage8_event_46
    katrine "Thanks for today, babe. That was great."
    if recollection == False:
        $ katrine.weight += 1
    $ katrinestage8event = 0
    return

label Katrine_Stage_9_Event:
    #"Go to gym option” – once they are both stage 9.

    ###Gym, Trista and Katrine on treadmills###
    image katrine_stage9_event_1 = "/katrine/events/stage9/1.webp"
    scene katrine_stage9_event_1
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    "Walking in you can already hear a heated conversation happening."
    "Your two large gym buddies currently doing their best to look natural on the treadmills."
    image katrine_stage9_event_2 = "/katrine/events/stage9/2.webp"
    scene katrine_stage9_event_2
    katrine "Oh yeah, you would say that."
    trista "I'm barely breaking a sweat."
    katrine "I'm fine too. I could do this all day."
    "Despite the confidence they are both talking with, neither look like they are doing that well."
    pc "Hi guys."
    image katrine_stage9_event_3 = "/katrine/events/stage9/3.webp"
    scene katrine_stage9_event_3
    katrine "Hey, [playername], can you tell Trista here that I am just as fit as ever."
    katrine "I thought I would have proved that last time you questioned me."
    image katrine_stage9_event_4 = "/katrine/events/stage9/4.webp"
    scene katrine_stage9_event_4
    trista "That might have been true then, but you have packed on the pounds since then."
    katrine "Look who is talking. You might think it's all bulk, but it's not."
    image katrine_stage9_event_5 = "/katrine/events/stage9/5.webp"
    scene katrine_stage9_event_5
    "Opening her mouth to respond it's clear talking and running at these speeds is difficult for them both."
    "Breathing heavily they are forced to take a break from speaking to regain their breath."
    trista "Let's turn this up then if you think we both need the workout."
    image katrine_stage9_event_6 = "/katrine/events/stage9/6.webp"
    scene katrine_stage9_event_6
    "Pushing the button you watch as her speed increases, not to be outdone Katrine follows her example."
    "Now with the extra speed on top of everything, the gym falls silent other than the machines and their breathing."
    "Both of them manage to keep it up for a few minutes, but they are starting to struggle."
    image katrine_stage9_event_7 = "/katrine/events/stage9/7.webp"
    scene katrine_stage9_event_7
    "Katrine is the first to break, pushing the button to slow down the machine until it stops."
    image katrine_stage9_event_8 = "/katrine/events/stage9/8.webp"
    scene katrine_stage9_event_8
    "A very relieved looking Trista follows suit, both of them catching their breath."
    ###Both of them stood next to machines, maybe wiping themselves with towels.###
    image katrine_stage9_event_9 = "/katrine/events/stage9/9.webp"
    scene katrine_stage9_event_9
    trista "See? I told you I could outlast you."
    katrine "I only stopped because that’s the end of my workout."
    katrine "I could have kept going."
    trista "Maybe you should."
    image katrine_stage9_event_10 = "/katrine/events/stage9/10.webp"
    scene katrine_stage9_event_10
    katrine "Excuse me?"
    trista "Hey, look, I'm not trying to be mean, but it looks like you are eating more than ever and I barely see you in here anymore."
    katrine "So what? I've just been busy."
    image katrine_stage9_event_11 = "/katrine/events/stage9/11.webp"
    scene katrine_stage9_event_11
    trista "So, you have gained weight and maybe you should come by more often."
    trista "This place is always open to you."
    katrine "Really? I thought I was oblivious."
    image katrine_stage9_event_12 = "/katrine/events/stage9/12.webp"
    scene katrine_stage9_event_12
    katrine "Have you seen the size of your ass? It's starting to match your personality."
    trista "Is that the thanks I get for being honest?"
    katrine "Just repaying the favour."
    trista "The difference is I'm here working out all the time."
    image katrine_stage9_event_13 = "/katrine/events/stage9/13.webp"
    scene katrine_stage9_event_13
    trista "I can work this weight off in no time at all if I wasn’t trying to put it on."
    katrine "Yeah, well, like I said, I've just been busy. We are not all lucky enough to live in the gym."
    trista "That has nothing to do with it. It's all about mental strength and motivation."
    trista "It's why I will work off this weight in no time at all."
    image katrine_stage9_event_14 = "/katrine/events/stage9/14.webp"
    scene katrine_stage9_event_14
    katrine "Fine. If you think it's about motivation, I bet you twelve burgers that I can work off this weight before you."
    trista "Only you would bet in burgers. I thought you wanted to lose weight."
    katrine "Who said I would be the one eating them?"
    katrine "If I work off this weight before you, then you have to eat those burgers."
    image katrine_stage9_event_15 = "/katrine/events/stage9/15.webp"
    scene katrine_stage9_event_15
    trista "Make it twenty and you are on."
    katrine "Twenty-five!"
    trista "Deal!"
    image katrine_stage9_event_16 = "/katrine/events/stage9/16.webp"
    scene katrine_stage9_event_16
    katrine "I can't wait to make you eat those words and burgers."
    trista "You really think you have a chance?"
    katrine "More of a chance than you."
    image katrine_stage9_event_17 = "/katrine/events/stage9/17.webp"
    scene katrine_stage9_event_17
    trista "We will see. I won't need much time to turn all this into muscle mass."
    trista "I won't just be slim again, I’ll be in the best shape of my life."
    katrine "Sure, you keep telling yourself that."
    trista "Well then, no time like the present. Guess we better get started."
    image katrine_stage9_event_18 = "/katrine/events/stage9/18.webp"
    scene katrine_stage9_event_18
    katrine "Actually, I think I'm going to head outside. It's too nice to be inside all day."
    katrine "Fancy doing something together, [playername]?"
    pc "Sure. Maybe we could head down to the beach and relax."
    image katrine_stage9_event_19 = "/katrine/events/stage9/19.webp"
    scene katrine_stage9_event_19
    trista "That sounds like a nice idea. I can work out later."
    katrine "Well, actually, I think it was just me and-"
    trista "I'll just go grab my bathing suit and we can head out."
    ###Trista disappears###
    image katrine_stage9_event_20 = "/katrine/events/stage9/20.webp"
    scene katrine_stage9_event_20
    "Frowning, it's clear Katrine is less than pleased with Trista inviting herself along."
    pc "It’s a big beach, maybe you can get some space from her anyway."
    katrine "As long as she stops talking about our weight gain then I don’t care where she sits."
    stop music fadeout 1.0

    ###On the beach sat / led between them in Bikins###
    image katrine_stage9_event_21 = "/katrine/events/stage9/21.webp"
    scene katrine_stage9_event_21
    play music "/music/beach.ogg" if_changed
    "It seems a lot of people have had the same idea, making the most of the nice weather on the beach."
    image katrine_stage9_event_22 = "/katrine/events/stage9/22.webp"
    scene katrine_stage9_event_22
    "Finding a semi-secluded area, you decide to claim it."
    image katrine_stage9_event_23 = "/katrine/events/stage9/23.webp"
    scene katrine_stage9_event_23
    trista "Mind helping me with some sunscreen?"
    pc "Sure thing."
    image katrine_stage9_event_24 = "/katrine/events/stage9/24.webp"
    scene katrine_stage9_event_24
    "Putting some of the cream on your hands you massage it into Trista's body."
    image katrine_stage9_event_25 = "/katrine/events/stage9/25.webp"
    scene katrine_stage9_event_25
    "Taking extra time to be sure to cover every inch of her ballooning backside."
    image katrine_stage9_event_26 = "/katrine/events/stage9/26.webp"
    scene katrine_stage9_event_26
    "Out of the corner of your eye you can see Katrine watching. Is she envious of the attention Trista is getting or admiring Trista's body like you?"
    image katrine_stage9_event_27 = "/katrine/events/stage9/27.webp"
    scene katrine_stage9_event_27
    "After applying sunscreen to Trista she lays on her stomach, her ample backside on display."
    "Many of those walking past easily distracted by the sight, not that you could blame them."

    image katrine_stage9_event_28 = "/katrine/events/stage9/28.webp"
    scene katrine_stage9_event_28
    "Spending the next few hours on the beach you relax on the sand as Katrine reads a book and Trista lays in the sun."
    image katrine_stage9_event_29 = "/katrine/events/stage9/29.webp"
    scene katrine_stage9_event_29
    "The blonde-haired gym-goer snacking on a variety of things she had brought with her."
    "The quietness is eventually broken by some loud rustling of a packet next to you."
    image katrine_stage9_event_30 = "/katrine/events/stage9/30.webp"
    scene katrine_stage9_event_30
    katrine "Do you mind? I'm trying to read here."
    image katrine_stage9_event_31 = "/katrine/events/stage9/31.webp"
    scene katrine_stage9_event_31
    trista "Sorry, but I'm hungry."
    image katrine_stage9_event_32 = "/katrine/events/stage9/32.webp"
    scene katrine_stage9_event_32
    "Continuing to munch away on her big back of crisps, Trista looked unapologetic for her loud snacking."
    "Finishing her first bag she to the displeasure of Katrine immediately reached in for a second."
    image katrine_stage9_event_33 = "/katrine/events/stage9/33.webp"
    scene katrine_stage9_event_33
    katrine "Aren't you trying to lose weight? This bet will be easier to win than I thought."
    image katrine_stage9_event_34 = "/katrine/events/stage9/34.webp"
    scene katrine_stage9_event_34
    trista "What? I haven't eaten in hours."
    image katrine_stage9_event_35 = "/katrine/events/stage9/35.webp"
    scene katrine_stage9_event_35
    katrine "What do you mean? You have been eating all day."
    image katrine_stage9_event_36 = "/katrine/events/stage9/36.webp"
    scene katrine_stage9_event_36
    trista "I wouldn’t count these as eating, they are not substantial enough to fill me."
    image katrine_stage9_event_37 = "/katrine/events/stage9/37.webp"
    scene katrine_stage9_event_37
    katrine "That's because it's just junk food. It's almost designed so you can eat loads of it."
    image katrine_stage9_event_38 = "/katrine/events/stage9/38.webp"
    scene katrine_stage9_event_38
    trista "That doesn’t really matter, I can eat loads of anything."
    image katrine_stage9_event_39 = "/katrine/events/stage9/39.webp"
    scene katrine_stage9_event_39
    katrine "Oh yeah? Look at your stomach. It's so small."
    katrine "I think even in my smaller days I could out-eat you."
    trista "Is everything a competition to you?"
    katrine "You were the one talking about speaking the truth earlier."
    image katrine_stage9_event_40 = "/katrine/events/stage9/40.webp"
    scene katrine_stage9_event_40
    trista "It's definitely not the truth. I could eat you under the table with room to spare."
    "Sitting up you could tell the competitive nature of both women was taking over."
    "Luckily you had spotted just the thing on your walk across the beach."
    image katrine_stage9_event_41 = "/katrine/events/stage9/41.webp"
    scene katrine_stage9_event_41
    pc "If you want to test it, I did see a hot dog eating contest on the way over here."
    trista "Where?"
    katrine "I don’t know I…"
    image katrine_stage9_event_42 = "/katrine/events/stage9/42.webp"
    scene katrine_stage9_event_42
    trista "Oh, so it was all tough words, but you didn't mean any of it."
    trista "Reminds me of your gym habits."
    katrine "Okay, that's it! You're on!"

    #### Hotdog eating contest – not sure how you want this to look but will leave it up to you###
    image katrine_stage9_event_43 = "/katrine/events/stage9/43.webp"
    scene katrine_stage9_event_43
    "Arriving just in time for the next round Trista and Katrine quickly sign up for the hotdog eating contest."
    "Joining two other women they take their places behind a giant table full of hotdogs."
    image katrine_stage9_event_44 = "/katrine/events/stage9/44.webp"
    scene katrine_stage9_event_44
    katrine "May the best woman win."
    trista "May the best eater win."
    image katrine_stage9_event_45 = "/katrine/events/stage9/45.webp"
    scene katrine_stage9_event_45
    announcer "Alright, ladies. On your marks, get set, eat!"
    image katrine_stage9_event_46 = "/katrine/events/stage9/46.webp"
    scene katrine_stage9_event_46
    "Without wasting a second Katrine and Trista dive into the piles of hotdogs."
    "Cramming them into their mouths they barely seem to chew before swallowing."
    image katrine_stage9_event_47 = "/katrine/events/stage9/47.webp"
    scene katrine_stage9_event_47
    "It only takes a few moments but the first hotdog is eaten, the second and third already in their hands."
    image katrine_stage9_event_48 = "/katrine/events/stage9/48.webp"
    scene katrine_stage9_event_48
    "In a frenzied blur of eating, both women are quickly pulling out a lead on the other two, but are neck and neck themselves."
    image katrine_stage9_event_49 = "/katrine/events/stage9/49.webp"
    scene katrine_stage9_event_49
    "Pausing for a drink, Katrine falls behind Trista for a moment before filling her mouth with hotdogs again."
    "Back and forth the race goes between them."
    image katrine_stage9_event_50 = "/katrine/events/stage9/50.webp"
    scene katrine_stage9_event_50
    "After only a couple of minutes one of the competitors is forced to give up."
    image katrine_stage9_event_51 = "/katrine/events/stage9/51.webp"
    scene katrine_stage9_event_51
    "The other only making it a few minutes more, obviously struggling to keep pace with either Trista or Katrine."
    image katrine_stage9_event_52 = "/katrine/events/stage9/52.webp"
    scene katrine_stage9_event_52
    "Stealing glances at each other they shoot daggers, their mouths too full to speak."
    image katrine_stage9_event_53 = "/katrine/events/stage9/53.webp"
    scene katrine_stage9_event_53
    "Adjusting herself you see the first signs of discomfort from Katrine as her stomach grows."
    "You know how much they can both eat, but Trista probably had the edge on her."
    image katrine_stage9_event_54 = "/katrine/events/stage9/54.webp"
    scene katrine_stage9_event_54
    "A couple of hotdogs later you notice as Katrine splutters slightly, reaching for another drink and pausing her eating."
    image katrine_stage9_event_55 = "/katrine/events/stage9/55.webp"
    scene katrine_stage9_event_55
    trista "Haha, you can give up anytime."
    "Trista’s words were a little hard to understand as crumbs flew out of her mouth."
    katrine "No chance!"
    image katrine_stage9_event_56 = "/katrine/events/stage9/56.webp"
    scene katrine_stage9_event_56
    "Looking at the pile of hotdogs in front of her, Katrine places a hand on her stomach before grabbing another."
    image katrine_stage9_event_57 = "/katrine/events/stage9/57.webp"
    scene katrine_stage9_event_57
    "But as if to almost show her dominance, Trista smirks before grabbing two hotdogs and smashing them together, the double hotdog barely fitting in her mouth as she eats it."
    "On and on the contest goes, the number of hotdogs diminishing as both their bellies grow."
    image katrine_stage9_event_58 = "/katrine/events/stage9/58.webp"
    scene katrine_stage9_event_58
    "Now taking a commanding lead, Trista seems to be going from a position of strength to even more strength, while Katrine is losing steam."
    "Each hotdog is taking a while to force into her stomach."
    image katrine_stage9_event_59 = "/katrine/events/stage9/59.webp"
    scene katrine_stage9_event_59
    "Until after only a couple more, Katrine has to reluctantly throw in the towel. She has eaten a respectable nineteen hotdogs and come in a clear second place."
    "Leaning back Katrine grimaced, rubbing her stomach gently."
    image katrine_stage9_event_60 = "/katrine/events/stage9/60.webp"
    scene katrine_stage9_event_60
    announcer "And we have our champion! With twenty-three hotdogs eaten, the winner is Trista!"
    announcer "Just ten shy of our all-time record."
    image katrine_stage9_event_61 = "/katrine/events/stage9/61.webp"
    scene katrine_stage9_event_61
    trista "There is a record?"
    image katrine_stage9_event_62 = "/katrine/events/stage9/62.webp"
    scene katrine_stage9_event_62
    announcer "Yes. The most anyone has eaten in thirty minutes is thirty-three hotdogs."
    trista "How much time have I got left?"
    announcer "About ten minutes. Why?"
    image katrine_stage9_event_63 = "/katrine/events/stage9/63.webp"
    scene katrine_stage9_event_63
    trista "That’s easy."
    image katrine_stage9_event_64 = "/katrine/events/stage9/64.webp"
    scene katrine_stage9_event_64
    "Despite having won and being visibly stuffed, Trista reaches out and grabs another hotdog as she goes for the record."
    "Her competitive nature is not just limited towards Katrine, it seems."
    "Carrying on, the next couple of hotdogs are eaten quickly, but it is clear that her stomach is starting to reach its limits."
    image katrine_stage9_event_65 = "/katrine/events/stage9/65.webp"
    scene katrine_stage9_event_65
    "Pausing for the first time, Trista grabs her drink - taking a large gulp to help the dry bread go down."
    image katrine_stage9_event_66 = "/katrine/events/stage9/66.webp"
    scene katrine_stage9_event_66
    "Continuing on, she is starting to struggle - each one taking longer than the last."
    image katrine_stage9_event_67 = "/katrine/events/stage9/67.webp"
    scene katrine_stage9_event_67
    "By now her stomach is clearly bulging out of her - with nothing to block the view of her overindulgence."
    image katrine_stage9_event_68 = "/katrine/events/stage9/68.webp"
    scene katrine_stage9_event_68
    "Forcing herself to eat, she powers through until she finally does it. She reaches thirty-three hotdogs."
    "Puffing out her cheeks, she looks more relieved than happy to have beaten the record."
    image katrine_stage9_event_69 = "/katrine/events/stage9/69.webp"
    scene katrine_stage9_event_69
    announcer "Congratulations! You have now matched the previous record."
    image katrine_stage9_event_70 = "/katrine/events/stage9/70.webp"
    scene katrine_stage9_event_70
    trista "Ughh, matched? I thought thirty-three was the record."
    image katrine_stage9_event_71 = "/katrine/events/stage9/71.webp"
    scene katrine_stage9_event_71
    announcer "It is, so if you want to beat it I'm afraid that’s one more hotdog."
    pc "Come on, Trista! You can do it!"
    image katrine_stage9_event_72 = "/katrine/events/stage9/72.webp"
    scene katrine_stage9_event_72
    "Reaching for the next hotdog Trista looked ready to burst. It was probably a good thing she was just in her bikini."
    image katrine_stage9_event_73 = "/katrine/events/stage9/73.webp"
    scene katrine_stage9_event_73
    "Slowly taking bites out of the last hotdog it was clearly a lot of effort to force herself to keep eating."
    "But seconds before the thirty minute limit she had done it, thirty-four hotdogs!"
    image katrine_stage9_event_74 = "/katrine/events/stage9/74.webp"
    scene katrine_stage9_event_74
    "A cheer went up around the crowd as Trista was crowned the new hotdog eating record holder."
    image katrine_stage9_event_75 = "/katrine/events/stage9/75.webp"
    scene katrine_stage9_event_75
    pc "Congratulations."
    trista "Thanks, but I'm already regretting that."
    trista "I feel stuffed. I don't think there is any room left in me."
    image katrine_stage9_event_76 = "/katrine/events/stage9/76.webp"
    scene katrine_stage9_event_76
    katrine "Well, you did say you wanted something more substantial."
    trista "Don’t remind me."
    image katrine_stage9_event_77 = "/katrine/events/stage9/77.webp"
    scene katrine_stage9_event_77
    trista "I think I better head home."
    katrine "Yeah, me too."
    trista "See you later, [playername]."
    katrine "Bye guys."
    "Going your separate ways, you notice the hotdog competition offers DVDs of the contests."
    "You make sure to order yourself one to enjoy later and relive Trista's record-breaking binge."
    stop music fadeout 1.0
    if recollection == False:
        $ trista.weight += 1
        $ katrine.weight += 1
    $ katrinestage9event = 0
    return

label Katrine_Stage_10_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Katrine', dialogue=dialogue_one)
    $ msg ("Hey, [playername]. Want to go to the café with me?", who=1)
    pause
    menu:
        "Join Katrine.":
            $ hide_messenger()
        "Do something else.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    ###Cafe with Katrine in a booth###
    image katrine_stage10_event_1 = "/katrine/events/stage10/1.webp"
    scene katrine_stage10_event_1
    "Arriving at the café, you see Katrine already sitting in a booth with a pile of her favourite pastries."
    image katrine_stage10_event_2 = "/katrine/events/stage10/2.webp"
    scene katrine_stage10_event_2
    katrine "Hey, [playername]. Nice to see you."
    pc "You too. How have you been?"
    katrine "Good. Actually, really good, thanks to you."
    pc "Thanks to me?"
    image katrine_stage10_event_3 = "/katrine/events/stage10/3.webp"
    scene katrine_stage10_event_3
    katrine "Yeah, you kind of opened my eyes last time we chatted."
    katrine "Life is too short to live with regrets or limit your own happiness."
    pc "I totally agree, but what does this have to do with me?"
    image katrine_stage10_event_4 = "/katrine/events/stage10/4.webp"
    scene katrine_stage10_event_4
    katrine "Your idea of being a food critic and also helping me realise that the only reason I started working out was so I could eat more."
    katrine "It was never about the exercise, but about the food."
    katrine "I guess it just took a little bit of help to see that, and to admit to myself that maybe I should stop caring so much and putting pressure on myself to be thin."
    katrine "Especially if it's not really what I want."
    pc "So what do you want?"
    image katrine_stage10_event_5 = "/katrine/events/stage10/5.webp"
    scene katrine_stage10_event_5
    katrine "To be free to eat what I want. I guess working out was a way of achieving that."
    pc "So are you giving up the gym?"
    katrine "No. I still want to be healthy, but it takes a weight off my shoulders to know I don't have to force myself to go."
    pc "That sounds like a good balance."
    image katrine_stage10_event_6 = "/katrine/events/stage10/6.webp"
    scene katrine_stage10_event_6
    katrine "Yeah, exactly. I think it's easier to maintain instead of going all out on both things."
    pc "So, have you made up with Trista yet? Seemed a bit fierce the last few times we have been out together."
    katrine "Yeah, you are right. I should probably make up with her. In a way she was only trying to help me."
    image katrine_stage10_event_7 = "/katrine/events/stage10/7.webp"
    scene katrine_stage10_event_7
    "Finishing off her pastries, you and Katrine make small talk before heading over to Trista’s gym."

    ###In the gym, Trista on the weights####
    image katrine_stage10_event_8 = "/katrine/events/stage10/8.webp"
    scene katrine_stage10_event_8
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    "Walking into the gym you spot Trista working out on the weights."
    pc "Hey, Trista."
    image katrine_stage10_event_9 = "/katrine/events/stage10/9.webp"
    scene katrine_stage10_event_9
    trista "Hey, [playername] and Katrine."
    "Sitting up from the weights there is an awkward pause as neither Katrine or Trista wants to start the conversation."
    image katrine_stage10_event_10 = "/katrine/events/stage10/10.webp"
    scene katrine_stage10_event_10
    katrine "I'm sorry, Trista."
    trista "For what? I thought you were expecting me to apologise."
    katrine "I was. But I think we both said and did some things we regret."
    image katrine_stage10_event_11 = "/katrine/events/stage10/11.webp"
    scene katrine_stage10_event_11
    trista "Definitely. I hope you know I didn't mean anything I said personally."
    katrine "I do. I was just having a hard time accepting you might have been right."
    trista "Don’t worry, so was I."
    image katrine_stage10_event_12 = "/katrine/events/stage10/12.webp"
    scene katrine_stage10_event_12
    trista "I have been so focused on the gym and competition I guess I projected that onto you."
    trista "I just wanted what was best for you and I thought you wanted to work out like me."
    image katrine_stage10_event_13 = "/katrine/events/stage10/13.webp"
    scene katrine_stage10_event_13
    katrine "I do... did. Well, maybe not like you."
    katrine "I think I just have to admit that I'm a bit heavier these days, but that I'm also ok with it."
    trista "Really? Me too!"
    katrine "What? I thought you were turning it into muscle mass or something?"
    image katrine_stage10_event_14 = "/katrine/events/stage10/14.webp"
    scene katrine_stage10_event_14
    trista "Well, I think I went a bit far for that."
    trista "But honestly, I'm kind of past that now - focusing on the next thing."
    trista "I only pushed so hard because I want to be the best at something... That and I might have been trying to impress you."
    image katrine_stage10_event_15 = "/katrine/events/stage10/15.webp"
    scene katrine_stage10_event_15
    katrine "Impress me? Why?"
    image katrine_stage10_event_16 = "/katrine/events/stage10/16.webp"
    scene katrine_stage10_event_16
    trista "I thought you knew I liked you?"
    trista "You were new in town, it's why I invited you to the gym and let you train here for free. I wanted to get to know you."
    image katrine_stage10_event_17 = "/katrine/events/stage10/17.webp"
    scene katrine_stage10_event_17
    katrine "Really? Why didn't you say something?"
    image katrine_stage10_event_18 = "/katrine/events/stage10/18.webp"
    scene katrine_stage10_event_18
    trista "I wasn't sure if you were into me. After that, I thought I had blown it by pushing you too much about your weight."
    katrine "You should have said something. The only reason I accepted was to train with you - and the whole being-free thing definitely helped."
    "Taking a moment, it's obvious the air has been cleared between them as they admit their mutual feelings."
    "You can't help but feel like a bit of a third wheel, until you realise something."
    image katrine_stage10_event_19 = "/katrine/events/stage10/19.webp"
    scene katrine_stage10_event_19
    pc "So, I can't help but notice that neither of you won the bet."
    trista "Yeah, but I guess it doesn’t matter."
    katrine "Yeah, neither of us lost weight so no one wins."
    pc "I thought the bet was whoever didn’t lose the weight had to eat the burgers?"
    image katrine_stage10_event_20 = "/katrine/events/stage10/20.webp"
    scene katrine_stage10_event_20
    katrine "It was, I guess."
    trista "Sounds like someone wants us to pay up."
    pc "I'm just stating what the bet was."
    image katrine_stage10_event_21 = "/katrine/events/stage10/21.webp"
    scene katrine_stage10_event_21
    "Giving you a knowing look it's clear both of them know what you are up too."
    trista "Well, I'm a woman of my word if you are, Katrine. How about it?"
    katrine "Stuffing my face with delicious burgers? I can think of worse ways of spending the day."
    stop music fadeout 1.0

    ###Bunny bites in booth opposite both of them###
    image katrine_stage10_event_22 = "/katrine/events/stage10/22.webp"
    scene katrine_stage10_event_22
    play music "/music/bunny_bites.ogg" if_changed
    "Now sitting in a booth, they seem excited to get things going, despite initially trying to get out of it."
    "A few moments later Marie arrives to take their orders."
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Hi. Can I take your order?"
    pc "Can we get fifty cheeseburgers, please?"
    marie "Fifty burgers?!"
    pc "Yes, please."
    marie "Uh, sure. They will be right out."
    image katrine_stage10_event_23 = "/katrine/events/stage10/23.webp"
    scene katrine_stage10_event_23
    "Disappearing, Marie takes the larger order to the kitchen. It is probably a good thing the place is quiet today."
    image katrine_stage10_event_24 = "/katrine/events/stage10/24.webp"
    scene katrine_stage10_event_24
    "Once cooked it takes several trips for them to be carried to the table, which is now covered in a mountain of burgers."
    katrine "Wow, it’s a good thing there are two of us."
    trista "I reckon I could do it on my own."
    image katrine_stage10_event_25 = "/katrine/events/stage10/25.webp"
    scene katrine_stage10_event_25
    katrine "I think someone’s eyes are bigger than their stomach, not that I would stop you if you wanted to try."
    trista "You are not getting out of it that easy."
    image katrine_stage10_event_26 = "/katrine/events/stage10/26.webp"
    scene katrine_stage10_event_26
    katrine "Oh, I have no intentions of getting out of this. I’ve dreamt of things like this."
    trista "Well, what are we waiting for?"
    image katrine_stage10_event_27 = "/katrine/events/stage10/27.webp"
    scene katrine_stage10_event_27
    "Picking up the first burgers, they give each other a look before digging in."
    "Despite not being a speed or timed contest, it seems they are still trying to outdo each other."
    image katrine_stage10_event_28 = "/katrine/events/stage10/28.webp"
    scene katrine_stage10_event_28
    "Aggressively chewing, they make it through the first few burgers with ease."
    image katrine_stage10_event_29 = "/katrine/events/stage10/29.webp"
    scene katrine_stage10_event_29
    "But this was a marathon not a sprint, and by the tenth burger both were clearly realising that."
    image katrine_stage10_event_30 = "/katrine/events/stage10/30.webp"
    scene katrine_stage10_event_30
    "Not even halfway through their order, both women are starting to struggle - the heavy burgers filling their growing stomachs."
    image katrine_stage10_event_31 = "/katrine/events/stage10/31.webp"
    scene katrine_stage10_event_31
    "Adjusting herself in her seat, Katrine is sitting with her legs wide apart - giving her belly all the room it might need."
    image katrine_stage10_event_32 = "/katrine/events/stage10/32.webp"
    scene katrine_stage10_event_32
    "At the dozen burgers mark, the chewing and swallowing you are seeing has slowed greatly."
    image katrine_stage10_event_33 = "/katrine/events/stage10/33.webp"
    scene katrine_stage10_event_33
    "But burger after burger disappears into the pair of them - their stomachs growing with each one and sticking out further and further."
    image katrine_stage10_event_34 = "/katrine/events/stage10/34.webp"
    scene katrine_stage10_event_34
    "Approaching the twentieth burger, Katrine can eat no more - her stomach reaching its capacity."
    katrine "I…can't…eat any more."
    "Groaning, she slouches back, admitting defeat and rubbing her swollen stomach."
    image katrine_stage10_event_35 = "/katrine/events/stage10/35.webp"
    scene katrine_stage10_event_35
    trista "Oh no, you don't. You have to eat all twenty-five and there is no quitting on me."
    katrine "Trista, I can't. I'm so full!"
    trista "I'm not taking no for an answer."
    image katrine_stage10_event_36 = "/katrine/events/stage10/36.webp"
    scene katrine_stage10_event_36
    "Picking up a burger, she holds it out in front of Katrine's mouth until she takes a bite."
    image katrine_stage10_event_37 = "/katrine/events/stage10/37.webp"
    scene katrine_stage10_event_37
    katrine "Well, you are not getting out of this either."
    "Returning the favour, Katrine gently pushes a burger past Trista's lips."
    image katrine_stage10_event_38 = "/katrine/events/stage10/38.webp"
    scene katrine_stage10_event_38
    "You can barely believe your luck as you watch the two beautiful women almost force-feed each other."
    image katrine_stage10_event_39 = "/katrine/events/stage10/39.webp"
    scene katrine_stage10_event_39
    "Their bulging bellies already complaining but getting fuller with every second that passes."
    image katrine_stage10_event_40 = "/katrine/events/stage10/40.webp"
    scene katrine_stage10_event_40
    "Now that they are no longer in control of their own feeding, both are forced to pick up the pace."
    image katrine_stage10_event_41 = "/katrine/events/stage10/41.webp"
    scene katrine_stage10_event_41
    "The burgers are replaced by another and another as they keep each other eating."
    image katrine_stage10_event_43 = "/katrine/events/stage10/43.webp"
    scene katrine_stage10_event_43
    "Somehow, despite the protests, both of them manage it. The twenty-fifth and final burger is finished at almost the exact same time."
    katrine "Oh god, my stomach is so full."
    trista "Mine too, but we did it."
    image katrine_stage10_event_44 = "/katrine/events/stage10/44.webp"
    scene katrine_stage10_event_44
    katrine "I can't tell if it feels awful or amazing to be this full."
    trista "Definitely amazing. It just feels good, doesn't it?"
    image katrine_stage10_event_45 = "/katrine/events/stage10/45.webp"
    scene katrine_stage10_event_45
    pc "If you want to, why don't we head back to mine and keep the good times going?"
    katrine "Sure thing."
    trista "Sounds good to me."
    "With your lustful trance now broken after watching your two gargantuan gym partners stuff themselves to their limits, you are eager to take the bulging beauties back home."
    "After a long waddle-filled trek, you finally get through the door and usher the ladies to the pool."
    stop music fadeout 1.0

    ###PC House###
    image katrine_stage10_event_46 = "/katrine/events/stage10/46.webp"
    scene katrine_stage10_event_46
    play music "/music/beach.ogg" if_changed
    pc "Make yourselves at home."
    trista "That pool looks so inviting after a massive meal."
    katrine "It’s a shame I didn’t bring my bathing suit."
    image katrine_stage10_event_47 = "/katrine/events/stage10/47.webp"
    scene katrine_stage10_event_47
    trista "Oh, don't be such a prude. It's just us."
    image katrine_stage10_event_48 = "/katrine/events/stage10/48.webp"
    scene katrine_stage10_event_48
    "As if to emphasise the point, Trista starts stripping off and heads to the pool."
    image katrine_stage10_event_49 = "/katrine/events/stage10/49.webp"
    scene katrine_stage10_event_49
    katrine "Well, if you don't mind, [playername]."
    pc "Why would I mind?"
    image katrine_stage10_event_50 = "/katrine/events/stage10/50.webp"
    scene katrine_stage10_event_50
    "Katrine undresses and walks towards the pool before turning around."
    katrine "Aren't you joining us?"
    image katrine_stage10_event_51 = "/katrine/events/stage10/51.webp"
    scene katrine_stage10_event_51
    "You take off your clothes and jump in the pool."
    "While both women are stuffed to the brim, the water helps remove the strain of the weight on their bodies."
    image katrine_stage10_event_52 = "/katrine/events/stage10/52.webp"
    scene katrine_stage10_event_52
    "After a refreshing swim, you leave the pool to find both women looking at you seductively."
    trista "Do you want to have some fun with us?"
    katrine "It's not often that you get to have two beautiful women."
    katrine "Why don't you sit down there and let Trista take care of you?"
    if persistent.nosexscene == True:
        scene black with dissolve
        stop music fadeout 1.0
        "The three of you had a great time together."
        if recollection == False:
            $ trista.weight += 1
            $ katrine.weight += 1
            $ daytime += 1
            $ phonecall = 1
        $ katrinestage10event = 0
        return
    image katrine_stage10_event_53 = "/katrine/events/stage10/53.webp"
    scene katrine_stage10_event_53
    "You sit down in the hot tub."
    "Trista slowly comes over to you with the help of Katrine."
    image katrine_stage10_event_54 = "/katrine/events/stage10/54.webp"
    scene katrine_stage10_event_54
    "Both women join you in the hot tub."
    trista "Are you ready for me?"
    pc "Always."
    image katrine_stage10_event_55 = "/katrine/events/stage10/55.webp"
    scene katrine_stage10_event_55
    "Trista slowly envelops your stiff cock, letting the weight of her gigantic ass rest on your lap."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/katrine/events/stage10/56.webm" loop
    show movie with dissolve
    window hide
    pause
    trista "This feels so great with the added pressure of being full."
    "Trista is clearly enjoying the moment. She soon begins to moan and shake."
    trista "Oh god, I'm already coming."
    stop movie
    image katrine_stage10_event_57 = "/katrine/events/stage10/57.webp"
    scene katrine_stage10_event_57
    "While having an orgasm, Trista leans forward to fall into Katrine's arms."
    katrine "Now it's my turn."
    image katrine_stage10_event_58 = "/katrine/events/stage10/58.webp"
    scene katrine_stage10_event_58
    "Katrine moves into position with her huge stuffed belly on full display."
    "You move over to her to line up your dick with her vagina."
    image katrine_stage10_event_59 = "/katrine/events/stage10/59.webp"
    scene katrine_stage10_event_59
    "You push into her until her bulging fat belly touches yours."
    katrine "Yes! Fuck me hard!"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/katrine/events/stage10/60.webm" loop
    show movie with dissolve
    window hide
    pause
    "You begin to swing your hips back and forth."
    "Just like Trista, Katrine also quickly reaches her orgasm because of the pressure from her bloated belly."
    katrine "Holy fuck!"
    stop movie
    image katrine_stage10_event_61 = "/katrine/events/stage10/61.webp"
    scene katrine_stage10_event_61
    "After bringing Katrine to her orgasm, both girls line up with their asses towards you."
    katrine "Cover us with your cum."
    image katrine_stage10_event_62 = "/katrine/events/stage10/62.webp"
    scene katrine_stage10_event_62
    "You make sure that both girls are covered equally with some S-tier semen."
    "The three of you clean up, after which Trista and Katrine go home."
    ###In the pool with them both naked###
    #[Sex scene in pool / around pool if its possible with all 3 characters. Feel free to change this to just the bedroom if that’s better for you?]
    stop music fadeout 1.0
    if recollection == False:
        $ trista.weight += 1
        $ katrine.weight += 1
        $ daytime += 1
        $ phonecall = 1
    $ katrinestage10event = 0
    return

label Katrine_BB_Extra:
    if katrine.stage <= 5:
        katrine "Oh, I think there has been a mistake. I didn't order this much."
        pc "Oh, are you ok to have this order at no extra cost?"
        katrine "I guess that's okay. I don't want to say no to free food."
        pc "In that case, I hope you enjoy the food."
        katrine "Thanks."
        image cafe_katrine_struggle = "/katrine/[katrine.stage]/cafe_struggle.webp"
        scene cafe_katrine_struggle
        "A short while later you can see Katrine struggling to finish the extra food you gave her."
    elif katrine.stage >= 7 and katrine.stage <= 9:
        katrine "Oh, I think there has been a mistake. I didn't order this much."
        pc "Oh, are you ok to have this order at no extra cost?"
        katrine "I probably shouldn't. I'm trying to slim down."
        katrine "But did you say it was free?"
        pc "Yes. It's our mistake, so feel free to eat as much of it as you like."
        katrine "I guess I don't have to finish it all."
        image cafe_katrine_struggle = "/katrine/[katrine.stage]/cafe_struggle.webp"
        scene cafe_katrine_struggle
        "A short while later you can see Katrine finishing off the extra food you gave her."
        "Despite her comments on not finishing it all, she has not left a crumb, her tight gym clothes even tighter now."
    else:
        katrine "Oh, I think there has been a mistake. I didn't order this much."
        pc "Oh, are you ok to have this order at no extra cost?"
        katrine "This is all free?"
        katrine "It's quite a lot, but I'm sure I can manage it."
        pc "In that case, enjoy your meal."
        katrine "Thanks."
        image cafe_katrine_struggle = "/katrine/[katrine.stage]/cafe_struggle.webp"
        scene cafe_katrine_struggle
        "A short while later you see Katrine has managed to polish off all the food you gave her."
        "Her appetite has clearly increased, as has the size of her belly."
    return

label Katrine_BB_Prize:
    image cafe_katrine_prize1 = "/katrine/[katrine.stage]/cafe_prize1.webp"
    scene cafe_katrine_prize1
    "Creating a sizable feast, you approach Katrine."
    image cafe_katrine_prize2 = "/katrine/[katrine.stage]/cafe_prize2.webp"
    scene cafe_katrine_prize2
    pc "Congratulations, you have won our weekly prize!"
    if katrineprizefirsttime == 1:
        katrine "Weekly prize?"
        pc "Every order gets an automatic entry into a prize pool."
        pc "The winner gets as much free food as they can eat."
        katrine "Wow, that's amazing. There has to be a catch though?"
        pc "No catch, just an extra incentive to keep people coming back."
        katrine "Well thank you, as if I needed another reason to love this place."
        image cafe_katrine_prize3 = "/katrine/[katrine.stage]/cafe_prize3.webp"
        scene cafe_katrine_prize3
        "Placing the food on the table, Katrine is almost salivating over the various smells coming from the food."
        image cafe_katrine_prize4 = "/katrine/[katrine.stage]/cafe_prize4.webp"
        scene cafe_katrine_prize4
        "Picking up a slice of Pizza, Katrine digs into her free meal."
        "Burgers, fries and onion rings are all devoured in record time."
        image cafe_katrine_prize5 = "/katrine/[katrine.stage]/cafe_prize5.webp"
        scene cafe_katrine_prize5
        "However, it seems her eagerness catches up with her and Katrine leans back, stuffed to her limit."
        image cafe_katrine_prize6 = "/katrine/[katrine.stage]/cafe_prize6.webp"
        scene cafe_katrine_prize6
        pc "How was the food?"
        katrine "Oooh, maybe this prize wasn't such a good deal."
        katrine "My stomach is so full, I think I got a bit carried away."
        pc "I'll pack the rest up so you can take it home with you."
        katrine "I don't know if I'll even be able to eat it back home."
        katrine "But I suppose I don't want it to go to waste."
        image cafe_katrine_prize7 = "/katrine/[katrine.stage]/cafe_prize7.webp"
        scene cafe_katrine_prize7
        "Returning a few minutes later, you hand Katrine two large bags of food to take home with her."
        "A rather stuffed Katrine leaves you to carry on with the rest of your work."
        $ katrineprizefirsttime = 0
    elif katrine.stage <= 7:
        katrine "Again, are you sure?"
        katrine "Is there no one else that wants it?"
        pc "It's automatic I'm afraid."
        katrine "Mmm, that's ok. Maybe if it is just one cheat day I can get away with it."
        image cafe_katrine_prize3 = "/katrine/[katrine.stage]/cafe_prize3.webp"
        scene cafe_katrine_prize3
        "Despite her reservations, as soon as the food is placed in front of her you can see Katrine eyeing it hungrily."
        image cafe_katrine_prize4 = "/katrine/[katrine.stage]/cafe_prize4.webp"
        scene cafe_katrine_prize4
        "Picking up a slice of Pizza, Katrine digs into her free meal."
        "Even though she seemed unhappy to have won, it looks like she is going to make the most of it."
        "Pizza's, burgers and fries are all eaten as if she hadn't had a meal in days."
        image cafe_katrine_prize5 = "/katrine/[katrine.stage]/cafe_prize5.webp"
        scene cafe_katrine_prize5
        "However, it seems her eagerness catches up with her and Katrine leans back, stuffed to her limit."
        pc "How was the food?"
        image cafe_katrine_prize6 = "/katrine/[katrine.stage]/cafe_prize6.webp"
        scene cafe_katrine_prize6
        katrine "I can't believe I ate that much again."
        katrine "My stomach is so full, this is going to take so much extra time to work off."
        pc "I'll pack the rest up so you can take it home with you."
        katrine "Maybe I can freeze it or something, I probably should eat any more today."
        image cafe_katrine_prize7 = "/katrine/[katrine.stage]/cafe_prize7.webp"
        scene cafe_katrine_prize7
        "Returning a few minutes later, you hand Katrine two large bags of food to take home with her."
        "A rather stuffed Katrine leaves you to carry on with the rest of your work."
    elif katrine.stage >= 8:
        katrine "I guess I was a little conflicted on what to order earlier."
        katrine "The universe has taken my diet out of my hands today."
        image cafe_katrine_prize3 = "/katrine/[katrine.stage]/cafe_prize3.webp"
        scene cafe_katrine_prize3
        "Placing the food in front of her, Katrine looks over it with a hungry stare."
        "It seems as if her new found freedom has made her happier to receive this large meal."
        image cafe_katrine_prize4 = "/katrine/[katrine.stage]/cafe_prize4.webp"
        scene cafe_katrine_prize4
        "Picking up a slice of Pizza, Katrine digs into the mountain of food in front of her."
        "Eating without any reservations she grabs handfuls of fries, stuffing them into her open mouth."
        image cafe_katrine_prize8 = "/katrine/[katrine.stage]/cafe_prize8.webp"
        scene cafe_katrine_prize8
        "Grabbing a burger she almost inhales it with an eagerness you haven't seen for a while."
        "Plate after plate empties as Katrine makes her way through the entire meal."
        image cafe_katrine_prize5 = "/katrine/[katrine.stage]/cafe_prize5.webp"
        scene cafe_katrine_prize5
        "Finally, with the table empty, she sits back rubbing her overstuffed belly."
        pc "How was the food?"
        image cafe_katrine_prize6 = "/katrine/[katrine.stage]/cafe_prize6.webp"
        scene cafe_katrine_prize6
        katrine "Did I really eat all that food?"
        katrine "I think I might explode, ooh I have ruined my stomach again."
        pc "I take it you don't want any more?"
        katrine "Please, no more."
        katrine "I shouldn't have eaten that much as it is."
        image cafe_katrine_prize9 = "/katrine/[katrine.stage]/cafe_prize9.webp"
        scene cafe_katrine_prize9
        "Sitting in the booth for a few minutes, Katrine gets up the energy to leave."
        "Watching her cradle her stuffed belly, you carry on with the rest of your work."
    return
