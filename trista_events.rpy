label trista_gym_1:
    if strength <= 11:
        ###Entering gym with Trista using the weights###
        image trista_gym_dumbel = "/trista/[trista.stage]/gym_dumbel.webp"
        scene trista_gym_dumbel
        "Walking into the gym you spot Trista using the weights."
        "Even with the heavier weights she makes it look effortless, her strong arms lifting them easily."
        "Maybe she would be a good gym partner."
        "I should probably get a bit stronger before offering to help her though."
        "Strength of 12 is required to work out with Trista."
        scene gym
        "You work out for a bit on your own."
        $ strength += 1
        "Strength increased by one point."
        "You take a quick shower and head home."
        stop music fadeout 1.0
        $ trista_gym_today = 1
        return

    if strength >= 12 and trista.stage == 1:
        image trista_gym_dumbel2 = "/trista/[trista.stage]/gym_dumbel2.webp"
        scene trista_gym_dumbel2
        "Hey, looks like Trista is working out today. She is making those dumbbells look weightless."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/1/gym_dumbel_vid4.webm" loop
        show movie with dissolve
        "After the last few sessions, you are feeling more confident in your own abilities."
        "But having a gym buddy who really knows what they are doing couldn’t hurt."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/1/gym_dumbel_vid2.webm" loop
        show movie with dissolve
        "Walking up to Trista she is so involved with her workout she doesn’t even notice."
        pc "Hey, Trista. How are you?"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/1/gym_dumbel_vid3.webm" loop
        show movie with dissolve
        trista "Good, getting in an extra set today."
        trista "It is always good to push yourself, in life but also the gym."
        pc "You make it all look easy. Got any tips?"
        stop movie
        image trista_gym_sitting = "/trista/[trista.stage]/gym_sitting.webp"
        scene trista_gym_sitting
        trista "Sure thing, let’s see what we are working with."
        image trista_gym_standing3 = "/trista/[trista.stage]/gym_standing3.webp"
        scene trista_gym_standing3
        "Moving over she indicates for you to take the bench."
        image trista_gym_benchpress = "/trista/[trista.stage]/gym_benchpress.webp"
        scene trista_gym_benchpress
        "Standing behind the bench, Trista spots you as you do a set of lifts."
        "With the cute but fierce blonde looking on, you try to look casual but definitely feel relieved after the last one."
        trista "Not bad, but remember not to lock your elbows between lifts."
        trista "That is an easy way to hurt yourself if you do it with a heavier weight especially."
        pc "Ok, thanks for the help."
        trista "Here, why don’t I show you."
        image trista_gym_benchpress2 = "/trista/[trista.stage]/gym_benchpress2.webp"
        scene trista_gym_benchpress2
        "Repaying the favour you help Trista do a set too, not that it seems like she needs it."
        image trista_gym_standing2 = "/trista/[trista.stage]/gym_standing2.webp"
        scene trista_gym_standing2
        trista "Phew, I can really feel my muscles burning now."
        trista "Thanks for that. I'm able to push harder with someone looking out for me."
        pc "Anytime."
        image trista_gym_animated1 = "/trista/[trista.stage]/gym_animated1.webp"
        scene trista_gym_animated1
        "Doing some more gentle stretches to warm down, you see Trista pick up a set of hand weights."
        image trista_gym_animated2 = "/trista/[trista.stage]/gym_animated2.webp"
        scene trista_gym_animated2
        "Positioning herself on top of an exercise ball, she lifts the weights out to her sides."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/1/gym_animated4.webm" loop
        show movie with dissolve
        window hide
        pause
        "The routine giving you a perfect view of her flexing muscles in her tight gym clothes."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/1/gym_animated3.webm" loop
        show movie with dissolve
        window hide
        pause
        "Leaving Trista to it you continue your workout before heading home after a quick shower."
        stop movie
        scene gym
        $ strength += 1
        if katrine.stage >= trista.stage:
            $ trista.weight += 0.2
        "Strength increased by one point."
        stop music fadeout 1.0
        $ trista_gym_today = 1
        return

    if trista.stage == 2:
        image trista_gym_dumbel2 = "/trista/[trista.stage]/gym_dumbel2.webp"
        scene trista_gym_dumbel2
        "Entering the gym, you spot Trista is working out on the weights."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/2/gym_dumbel_vid4.webm" loop
        show movie with dissolve
        "Her years of training was helping her make the heavy the dumbbells look weightless."
        "Deciding to see if she wants to pair up again, you walk up to her."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/2/gym_dumbel_vid2.webm" loop
        show movie with dissolve
        pc "Hey Trista, how are you?"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/2/gym_dumbel_vid5.webm" loop
        show movie with dissolve
        trista "Good, thanks."
        trista "Making the most of the gym while its quiet."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/2/gym_dumbel_vid3.webm" loop
        show movie with dissolve
        pc "You make it all look easy, got any tips?"
        trista "Sure thing, hop on the bench and let me get a look at you."
        stop movie
        image trista_gym_standing3 = "/trista/[trista.stage]/gym_standing3.webp"
        scene trista_gym_standing3
        "Moving over she indicates for you to take her spot."
        image trista_gym_benchpress = "/trista/[trista.stage]/gym_benchpress.webp"
        scene trista_gym_benchpress
        "Standing behind the bench, Trista spots you as you do a set of lifts."
        "With the cute but fierce blonde looking on, you try to look casual but definitely feel relieved after the last one."
        trista "You are definitely getting the hang of it, but your arms are shaking a little bit."
        trista "Maybe try a lower weight but more reps, until you can do that easily and move up."
        pc "Sure thing, that sounds good."
        image trista_gym_benchpress2 = "/trista/[trista.stage]/gym_benchpress2.webp"
        scene trista_gym_benchpress2
        "Repaying the favour, you spot for Trista who completes her set easily."
        image trista_gym_standing2 = "/trista/[trista.stage]/gym_standing2.webp"
        scene trista_gym_standing2
        trista "Thanks for that, I am able to push harder with someone looking out for me."
        pc "Anytime."
        image trista_gym_animated1 = "/trista/[trista.stage]/gym_animated1.webp"
        scene trista_gym_animated1
        "Doing some more gentle stretches to warm down, you see Trista pick up a set of hand weights."
        image trista_gym_animated2 = "/trista/[trista.stage]/gym_animated2.webp"
        scene trista_gym_animated2
        "Positioning herself on top of an exercise ball, she lifts the weights out to her sides."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/2/gym_animated4.webm" loop
        show movie with dissolve
        window hide
        pause
        "The routine giving you a perfect view of her flexing muscles in her tight gym clothes."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/2/gym_animated3.webm" loop
        show movie with dissolve
        window hide
        pause
        "Leaving Trista to it you continue your workout before heading home after a quick shower."
        stop movie
        scene gym
        if katrine.stage >= trista.stage:
            $ trista.weight += 0.3
        $ strength += 1
        "Strength increased by one point."
        stop music fadeout 1.0
        $ trista_gym_today = 1
        return

    if trista.stage == 3:
        image trista_gym_dumbel2 = "/trista/[trista.stage]/gym_dumbel2.webp"
        scene trista_gym_dumbel2
        "Entering the gym, you spot Trista is working out on the weights."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/3/gym_dumbel_vid1.webm" loop
        show movie with dissolve
        "Her years of training was helping her make the heavy the dumbbells look weightless."
        "Deciding to see if she wants to pair up again, you walk up to her"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/3/gym_dumbel_vid2.webm" loop
        show movie with dissolve
        pc "Hey Trista, how are you?"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/3/gym_dumbel_vid3.webm" loop
        show movie with dissolve
        trista "Good, almost done with this set if you want me to spot for you again?"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/3/gym_dumbel_vid4.webm" loop
        show movie with dissolve
        "Finishing her reps, she replaces the dumbbell on the rack."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/3/gym_dumbel_vid5.webm" loop
        show movie with dissolve
        window hide
        pause
        stop movie
        image trista_gym_standing3 = "/trista/[trista.stage]/gym_standing3.webp"
        scene trista_gym_standing3
        "Moving over she indicates for you to set up on the bench."
        image trista_gym_benchpress = "/trista/[trista.stage]/gym_benchpress.webp"
        scene trista_gym_benchpress
        "Trista spots you as you do a set of lifts, it feels a little easier this time."
        trista "You are definitely getting the hang of it."
        image trista_gym_benchpress2 = "/trista/[trista.stage]/gym_benchpress2.webp"
        scene trista_gym_benchpress2
        "Repaying the favour, you help Trista do another set."
        $ strength += 1
        "Strength increased by one point."
        image trista_gym_standing2 = "/trista/[trista.stage]/gym_standing2.webp"
        scene trista_gym_standing2
        trista "Thanks for that, I am able to push harder with someone looking out for me."
        trista "Mind helping me at the bag again?"
        pc "Sure thing."
        image trista_gym_boxing2 = "/trista/[trista.stage]/gym_boxing2.webp"
        scene trista_gym_boxing2
        "Grabbing the bag you do your best to hold it still as Trista goes through her routine."
        image trista_gym_boxing1 = "/trista/[trista.stage]/gym_boxing1.webp"
        scene trista_gym_boxing1
        "Swinging her leg round you feel it hitting the bag powerfully."
        "For the next 20 minutes she spins and kicks towards you with perfect rhythm and a fierce power."
        image trista_gym_standing4 = "/trista/[trista.stage]/gym_standing4.webp"
        scene trista_gym_standing4
        trista "I think that will do for now, I could do with a break for some food."
        trista "Thanks for your help today."
        pc "No problem."
        image trista_gym_eat1 = "/trista/[trista.stage]/gym_eat1.webp"
        scene trista_gym_eat1
        "Going behind the gym counter she begins piling up various snacks and drinks."
        "Not wanting to leave just yet you move over to the treadmills and go for a casual jog while watching Trista eating."
        image trista_gym_eat2 = "/trista/[trista.stage]/gym_eat2.webp"
        scene trista_gym_eat2
        "You stumble a few times as you are distracted by the snacks she is putting away."
        if katrine.stage >= trista.stage:
            $ trista.weight += 0.5
        "Eventually she finishes snacking and you head to the showers."
        stop music fadeout 1.0
        $ trista_gym_today = 1
        return

    if trista.stage <= 6 and trista.stage >= 4:
        image trista_gym_dumbel2 = "/trista/[trista.stage]/gym_dumbel2.webp"
        scene trista_gym_dumbel2
        "Entering the gym, you spot Trista is working out on the weights."
        if trista.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/4/gym_dumbel_vid1.webm" loop
            show movie with dissolve
        elif trista.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/gym_dumbel_vid1.webm" loop
            show movie with dissolve
        elif trista.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/gym_dumbel_vid1.webm" loop
            show movie with dissolve
        "Her years of training was helping her make the heavy the dumbbells look weightless."
        "Deciding to see if she wants to pair up again, you walk up to her."
        stop movie
        if trista.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/4/gym_dumbel_vid2.webm" loop
            show movie with dissolve
        elif trista.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/gym_dumbel_vid2.webm" loop
            show movie with dissolve
        elif trista.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/gym_dumbel_vid2.webm" loop
            show movie with dissolve
        pc "Hey Trista, how are you?"
        stop movie
        if trista.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/4/gym_dumbel_vid3.webm" loop
            show movie with dissolve
        elif trista.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/gym_dumbel_vid3.webm" loop
            show movie with dissolve
        elif trista.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/gym_dumbel_vid3.webm" loop
            show movie with dissolve
        trista "Feeling really good, possibly the best I ever have."
        trista "That competition will be a piece of cake if I keep my training up."
        pc "That’s awesome, the other competitors won’t know what hit them."
        stop movie
        if trista.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/4/gym_dumbel_vid4.webm" loop
            show movie with dissolve
        elif trista.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/gym_dumbel_vid4.webm" loop
            show movie with dissolve
        elif trista.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/gym_dumbel_vid4.webm" loop
            show movie with dissolve
        trista "It comes with practice, you are starting to show that too."
        trista "You have come on a lot since our first sessions together."
        pc "Thanks, I owe that to you."
        stop movie
        if trista.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/4/gym_dumbel_vid5.webm" loop
            show movie with dissolve
        elif trista.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/gym_dumbel_vid5.webm" loop
            show movie with dissolve
        elif trista.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/gym_dumbel_vid5.webm" loop
            show movie with dissolve
        trista "Well, no reason to stop pushing yourself."
        stop movie
        image trista_gym_sitting = "/trista/[trista.stage]/gym_sitting.webp"
        scene trista_gym_sitting
        trista "Maybe we should finally up you to the next weights?"
        pc "Sure."
        image trista_gym_standing3 = "/trista/[trista.stage]/gym_standing3.webp"
        scene trista_gym_standing3
        "Moving over she indicates for you to take the bench while she changes the weights out."
        image trista_gym_benchpress = "/trista/[trista.stage]/gym_benchpress.webp"
        scene trista_gym_benchpress
        "Trista spots you as you do a set of lifts."
        "Trista is right, despite the heavier weights it feels a lot easier than it did the first time you worked out with her."
        trista "You are definitely getting the hang of it."
        image trista_gym_benchpress2 = "/trista/[trista.stage]/gym_benchpress2.webp"
        scene trista_gym_benchpress2
        "Repaying the favour you help Trista do a set too."
        $ strength += 1
        "Strength increased by one point."
        image trista_gym_standing2 = "/trista/[trista.stage]/gym_standing2.webp"
        scene trista_gym_standing2
        trista "Thanks for that, I am able to push harder with someone looking out for me."
        trista "Mind helping me at the bag again?"
        pc "Sure thing."
        image trista_gym_boxing2 = "/trista/[trista.stage]/gym_boxing2.webp"
        scene trista_gym_boxing2
        "Grabbing the bag you do your best to hold it still as Trista goes through her routine."
        image trista_gym_boxing1 = "/trista/[trista.stage]/gym_boxing1.webp"
        scene trista_gym_boxing1
        "Swinging her leg round you feel it hitting the bag powerfully."
        "For the next 20 minutes she spins and kicks towards you with perfect rhythm and a fierce power."
        image trista_gym_standing4 = "/trista/[trista.stage]/gym_standing4.webp"
        scene trista_gym_standing4
        trista "I think that will do for now, I could do with a break for some food."
        trista "Thanks for your help today [playername]."
        pc "No problem."
        image trista_gym_eat1 = "/trista/[trista.stage]/gym_eat1.webp"
        scene trista_gym_eat1
        "Going behind the gym counter she begins piling up various snacks and drinks."
        "Not wanting to leave just yet you move over to the treadmills and go for a casual jog while watching Trista eating."
        image trista_gym_eat2 = "/trista/[trista.stage]/gym_eat2.webp"
        scene trista_gym_eat2
        "You stumble a few times as you are distracted by the snacks she is putting away."
        "Finishing her pizza she reaches for an extra large drink. It seems like Trista is eating more and more lately."
        image trista_gym_eat3 = "/trista/[trista.stage]/gym_eat3.webp"
        scene trista_gym_eat3
        "Even from your current position you think you can see her belly growing, but it could just be your imagination."
        if katrine.stage >= trista.stage:
            $ trista.weight += 0.5
        "Eventually she finishes snacking and you head to the showers."
        stop music fadeout 1.0
        $ trista_gym_today = 1
        return

    if trista.stage == 7:
        image trista_gym_dumbel2 = "/trista/[trista.stage]/gym_dumbel2.webp"
        scene trista_gym_dumbel2
        "Entering the gym, you spot Trista is working out on the weights."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/7/gym_dumbel_vid5.webm" loop
        show movie with dissolve
        "Her years of training was helping her make the heavy the dumbbells look weightless."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/7/gym_dumbel_vid2.webm" loop
        show movie with dissolve
        "Deciding to see if she wants to pair up again, you walk up to her."
        pc "Hey, Trista. How are you?"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/7/gym_dumbel_vid3.webm" loop
        show movie with dissolve
        trista "Good, getting in an extra set today instead of cardio."
        pc "Instead of cardio?"
        trista "Cardio burns calories, trying to optimise my bulking stage."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/7/gym_dumbel_vid4.webm" loop
        show movie with dissolve
        "Looking at her body it's clear that she is bulking up well."
        stop movie
        image trista_gym_standing3 = "/trista/[trista.stage]/gym_standing3.webp"
        scene trista_gym_standing3
        "Moving over she indicates for you to take the bench."
        "Trista spots you as you do a set of lifts."
        image trista_gym_benchpress = "/trista/[trista.stage]/gym_benchpress.webp"
        scene trista_gym_benchpress
        "Lifting the weights is almost second nature by this point."
        trista "You are definitely getting to the point we might have to get some bigger weights on these."
        $ strength += 1
        "Strength increased by one point."
        image trista_gym_benchpress2 = "/trista/[trista.stage]/gym_benchpress2.webp"
        scene trista_gym_benchpress2
        "Repaying the favour you help Trista do a set too, not that it seems like she needs it."
        "Despite her recent weight gain, she hasn’t lost any of her strength."
        image trista_gym_standing2 = "/trista/[trista.stage]/gym_standing2.webp"
        scene trista_gym_standing2
        trista "Thanks for that. I'm able to push harder with someone looking out for me."
        trista "Mind helping me at the bag again?"
        pc "Sure thing."
        image trista_gym_boxing2 = "/trista/[trista.stage]/gym_boxing2.webp"
        scene trista_gym_boxing2
        "Grabbing the bag you do your best to hold it still as Trista goes through her routine."
        image trista_gym_boxing1 = "/trista/[trista.stage]/gym_boxing1.webp"
        scene trista_gym_boxing1
        "Swinging her leg round you feel it hitting the bag powerfully."
        "For the next twenty minutes she spins and kicks towards you with perfect rhythm and a fierce power."
        image trista_gym_standing4 = "/trista/[trista.stage]/gym_standing4.webp"
        scene trista_gym_standing4
        trista "I think that will do for now, I could do with a break for some food."
        trista "Thanks for you help today [playername]."
        pc "No problem."
        image trista_gym_eat1 = "/trista/[trista.stage]/gym_eat1.webp"
        scene trista_gym_eat1
        "Going behind the gym counter Trista pulls out a full cheese pizza and begins eating it."
        "Not wanting to leave just yet you move over to the treadmills and go for a casual jog while watching Trista eating."
        "You stumble a few times as you are distracted by the snacks she is putting away."
        image trista_gym_eat2 = "/trista/[trista.stage]/gym_eat2.webp"
        scene trista_gym_eat2
        "Finishing her pizza Trista keeps grazing on more and more snacks and drinks, it barely looks like she is registering what she is eating."
        image trista_gym_eat3 = "/trista/[trista.stage]/gym_eat3.webp"
        scene trista_gym_eat3
        "Even from your current position you think you can see her belly growing, but it could just be your imagination."
        if katrine.stage >= trista.stage:
            $ trista.weight += 0.5
        "Eventually she finishes snacking and you head to the showers."
        stop music fadeout 1.0
        $ trista_gym_today = 1
        return

    if trista.stage == 8:
        image trista_gym_dumbel2 = "/trista/[trista.stage]/gym_dumbel2.webp"
        scene trista_gym_dumbel2
        "Entering the gym, you spot Trista is working out on the weights."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/8/gym_dumbel_vid5.webm" loop
        show movie with dissolve
        "Despite her weight gain, it doesn’t seem to be stopping her lifting well."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/8/gym_dumbel_vid2.webm" loop
        show movie with dissolve
        "Deciding to see if she wants to pair up again, you walk up to her."
        pc "Hey, Trista. How are you?"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/8/gym_dumbel_vid3.webm" loop
        show movie with dissolve
        trista "Good, getting in an extra set today instead of cardio."
        pc "Still maximising your bulking?"
        trista "You betcha."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/8/gym_dumbel_vid4.webm" loop
        show movie with dissolve
        "Looking at her body it's clear that she is definitely bulking up well."
        stop movie
        image trista_gym_standing3 = "/trista/[trista.stage]/gym_standing3.webp"
        scene trista_gym_standing3
        "Moving over she indicates for you to take the bench."
        image trista_gym_benchpress = "/trista/[trista.stage]/gym_benchpress.webp"
        scene trista_gym_benchpress
        "Trista spots you as you do a set of lifts."
        "Lifting the weights is almost second nature by this point."
        $ strength += 1
        "Strength increased by one point."
        trista "Impressive, you have gotten used to the new weights really quickly."
        image trista_gym_benchpress2 = "/trista/[trista.stage]/gym_benchpress2.webp"
        scene trista_gym_benchpress2
        "Repaying the favour you help Trista do a set too, not that it seems like she needs it."
        "Despite her recent weight gain, she hasn’t lost any of her strength."
        image trista_gym_standing2 = "/trista/[trista.stage]/gym_standing2.webp"
        scene trista_gym_standing2
        trista "Thanks for that. I'm able to push harder with someone looking out for me."
        trista "Mind helping me at the bag again?"
        pc "Sure thing."
        ###At punching bag###
        image trista_gym_boxing2 = "/trista/[trista.stage]/gym_boxing2.webp"
        scene trista_gym_boxing2
        "Grabbing the bag you do your best to hold it still as Trista goes through her routine."
        image trista_gym_boxing1 = "/trista/[trista.stage]/gym_boxing1.webp"
        scene trista_gym_boxing1
        "Swinging her leg round you feel it hitting the bag powerfully."
        "For the next fifteen minutes she spins and kicks towards you with perfect rhythm and a fierce power."
        "Unlike her lifting, the extra weight on her body is taking a toll as she is forced to cut her routine short."
        image trista_gym_standing4 = "/trista/[trista.stage]/gym_standing4.webp"
        scene trista_gym_standing4
        trista "I think that will do for now, I could do with a break for some food."
        trista "Fancy helping me out with that too?"
        pc "Absolutely."
        image trista_gym_beforefeeding = "/trista/[trista.stage]/gym_beforefeeding.webp"
        scene trista_gym_beforefeeding
        "Moving over to the table Trista grabs a pile of donut boxes."
        pc "Here let me help."
        $ stuffed = 1
        show screen tristafullness
        call trista_gym_feeding from _call_trista_gym_feeding
        pause
        hide screen tristafullness
        pause
        trista "You’re a great trainer, exactly what I need to reach the next level."
        if katrine.stage >= trista.stage:
            $ trista.weight += (trista.fullness / 2)
        $ trista.fullness = 0
        "Eventually she finishes snacking and you head to the showers."
        $ stuffed = 0
        stop music fadeout 1.0
        $ trista_gym_today = 1
        return

    if trista.stage == 9:
        ####Stage 9a #### - NEW
        image trista_gym_dumbel2 = "/trista/[trista.stage]/gym_dumbel2.webp"
        scene trista_gym_dumbel2
        "Entering the gym, you spot Trista is working out on the weights."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/9/gym_dumbel_vid4.webm" loop
        show movie with dissolve
        "Raising the dumbbell with one hand, you can see a doughnut in the other."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/9/gym_dumbel_vid1.webm" loop
        show movie with dissolve
        "Each time she completes a set of reps, she seems to take a bite."
        "Watching her finish the doughnut you go to see if she wants to pair up again."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/9/gym_dumbel_vid2.webm" loop
        show movie with dissolve
        pc "Hey Trista, how are you?"
        trista "I'm ok thanks."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/9/gym_dumbel_vid3.webm" loop
        show movie with dissolve
        trista "Although I think I have been letting myself down with my weights training."
        trista "Definitely noticed a drop in my performance lately."
        pc "I think you could still wipe the floor with me."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/9/gym_dumbel_vid5.webm" loop
        show movie with dissolve
        pc "But want to partner up again?"
        stop movie
        image trista_gym_sitting = "/trista/[trista.stage]/gym_sitting.webp"
        scene trista_gym_sitting
        trista "Sure thing, I could do with a breather so why don’t you take a set first."
        image trista_gym_standing3 = "/trista/[trista.stage]/gym_standing3.webp"
        scene trista_gym_standing3
        "Moving over she indicates for you to take the bench."
        image trista_gym_benchpress = "/trista/[trista.stage]/gym_benchpress.webp"
        scene trista_gym_benchpress
        "Walking around the back of the bench, Trista spots for you."
        "Lifting the weights is almost second nature by this point."
        trista "You are definitely getting to the point we might have to get some bigger weights on these."
        image trista_gym_benchpress2 = "/trista/[trista.stage]/gym_benchpress2.webp"
        scene trista_gym_benchpress2
        "Repaying the favour you help Trista do a set too."
        ###more sweaty Trista than usual.###
        "For the first time you can see her struggling a little."
        "Before she could lift these with no problem, but now you can hear her breathing heavily and puffing out her cheeks as she lifts the bar."
        image trista_gym_standing2 = "/trista/[trista.stage]/gym_standing2.webp"
        scene trista_gym_standing2
        trista "There we go, another set down."
        $ strength += 1
        "Strength increased by one point."
        trista "Thanks for that, I am able to push harder with someone looking out for me."
        trista "Mind helping me at the bag again?"
        pc "Sure thing."
        ###At punching bag – still sweating###
        image trista_gym_boxing2 = "/trista/[trista.stage]/gym_boxing2.webp"
        scene trista_gym_boxing2
        "Grabbing the bag you do your best to hold it still as Trista goes through her routine."
        image trista_gym_boxing1 = "/trista/[trista.stage]/gym_boxing1.webp"
        scene trista_gym_boxing1
        "Swinging her leg round you feel it hitting the bag powerfully."
        "For 10 minutes she spins and kicks towards you with perfect rhythm and a fierce power."
        "The extra weight on her body is clearly slowing her down until she has to take a breather."
        image trista_gym_exhausted = "/trista/[trista.stage]/gym_exhausted.webp"
        scene trista_gym_exhausted
        "Bending over, she breaths heavily as you let her catch her breath."
        trista "That's weird, I don't feel like I went that much harder but I guess I must have."
        trista "But no pain, no gain."
        image trista_gym_standing4 = "/trista/[trista.stage]/gym_standing4.webp"
        scene trista_gym_standing4
        trista "Although my muscles are feeling a little tight, would you mind helping me stretch?"
        pc "Uh, sure."
        image trista_stage9_event_1 = "/trista/events/stage9/1.webp"
        scene trista_stage9_event_1
        "Laying on her back, Trista raises her legs up for you to help stretch."
        "It was nothing new given she had been doing this for you for weeks."
        image trista_stage9_event_2 = "/trista/events/stage9/2.webp"
        scene trista_stage9_event_2
        "Pushing her legs back you help her stretch."
        "Standing back up she seems much happier."
        image trista_stage9_event_3 = "/trista/events/stage9/3.webp"
        scene trista_stage9_event_3
        trista "Thanks for that, but for now I could do with a break for some food."
        trista "Fancy helping me out with that too?"
        pc "Sure thing."
        image trista_gym_beforefeeding = "/trista/[trista.stage]/gym_beforefeeding.webp"
        scene trista_gym_beforefeeding
        "Moving over to the table Trista grabs a pile of donut boxes."
        $ stuffed = 1
        show screen tristafullness
        call trista_gym_feeding from _call_trista_gym_feeding_1
        pause
        hide screen tristafullness
        pause
        trista "Mmm, that was good."
        trista "Thanks for your help today."
        if katrine.stage >= trista.stage:
            $ trista.weight += (trista.fullness / 2)
        $ trista.fullness = 0
        pc "No worries, see you around Trista."
        $ stuffed = 0
        stop music fadeout 1.0
        $ trista_gym_today = 1
        return

    if trista.stage >= 10:
        ####Stage 10a+ #### - NEW
        image trista_gym_dumbel2 = "/trista/[trista.stage]/gym_dumbel2.webp"
        scene trista_gym_dumbel2
        "Entering the gym, you spot Trista is working out on the weights."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if trista.stage == 10:
            play movie "/images/trista/10/gym_dumbel_vid1.webm" loop
        elif trista.stage == 11:
            play movie "/images/trista/11/gym_dumbel_vid1.webm" loop
        elif trista.stage == 12:
            play movie "/images/trista/12/gym_dumbel_vid1.webm" loop
        elif trista.stage == 13:
            play movie "/images/trista/13/gym_dumbel_vid1.webm" loop
        show movie with dissolve
        "Raising the dumbbell with one hand, you can see a doughnut in the other."
        "Each time she completes a rep, she takes another bite."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if trista.stage == 10:
            play movie "/images/trista/10/gym_dumbel_vid3.webm" loop
        elif trista.stage == 11:
            play movie "/images/trista/11/gym_dumbel_vid3.webm" loop
        elif trista.stage == 12:
            play movie "/images/trista/12/gym_dumbel_vid3.webm" loop
        elif trista.stage == 13:
            play movie "/images/trista/13/gym_dumbel_vid3.webm" loop
        show movie with dissolve
        "Watching her finish the doughnut you go to see if she wants to pair up again."
        pc "Hey Trista, how are you?"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if trista.stage == 10:
            play movie "/images/trista/10/gym_dumbel_vid2.webm" loop
        elif trista.stage == 11:
            play movie "/images/trista/11/gym_dumbel_vid2.webm" loop
        elif trista.stage == 12:
            play movie "/images/trista/12/gym_dumbel_vid2.webm" loop
        elif trista.stage == 13:
            play movie "/images/trista/13/gym_dumbel_vid2.webm" loop
        show movie with dissolve
        trista "Feeling pretty good actually, disappointed but focused."
        trista "Just got to keep pushing to improve."
        pc "That’s an admirable way of looking at it."
        trista "Thanks, want to work out together again?"
        stop movie
        image trista_gym_sitting = "/trista/[trista.stage]/gym_sitting.webp"
        scene trista_gym_sitting
        trista "I could do with a breather if you want to go first."
        image trista_gym_standing3 = "/trista/[trista.stage]/gym_standing3.webp"
        scene trista_gym_standing3
        "Moving over she indicates for you to take the bench."
        image trista_gym_benchpress = "/trista/[trista.stage]/gym_benchpress.webp"
        scene trista_gym_benchpress
        "Walking around the back of the bench, Trista spots for you."
        "Lifting the weights is almost second nature by this point."
        trista "You are doing really well, you won't need me soon."
        pc "Even if I don't need you, I'll always be up for working out together."
        pc "At least now I'm less nervous about spotting for you though."
        image trista_gym_benchpress2 = "/trista/[trista.stage]/gym_benchpress2.webp"
        scene trista_gym_benchpress2
        "Repaying the favour, you help Trista with her set too."
        "You notice the weights she uses are less than her usual ones."
        image trista_gym_standing2 = "/trista/[trista.stage]/gym_standing2.webp"
        scene trista_gym_standing2
        trista "There we go, another set down."
        $ strength += 1
        "Strength increased by one point."
        pc "You working out on the bag again?"
        trista "If you don't mind?"
        pc "Of course not."
        ###At punching bag ###
        image trista_gym_boxing2 = "/trista/[trista.stage]/gym_boxing2.webp"
        scene trista_gym_boxing2
        "Grabbing the bag you hold it still as Trista goes through her routine."
        image trista_gym_boxing1 = "/trista/[trista.stage]/gym_boxing1.webp"
        scene trista_gym_boxing1
        "Swinging her leg round you feel it hitting the bag powerfully."
        "For 10 minutes she spins and kicks towards you with perfect rhythm and a fierce power."
        "The extra weight on her body is clearly slowing her down until she has to take a breather."
        image trista_gym_exhausted = "/trista/[trista.stage]/gym_exhausted.webp"
        scene trista_gym_exhausted
        "Bending over, she breaths heavily as you let her catch her breath."
        trista "Definitely not at the top of my game yet, but I'll get back up there."
        image trista_gym_standing4 = "/trista/[trista.stage]/gym_standing4.webp"
        scene trista_gym_standing4
        trista "For now though, we should move onto a different kind of training."
        pc "Sure thing."
        image trista_gym_beforefeeding = "/trista/[trista.stage]/gym_beforefeeding.webp"
        scene trista_gym_beforefeeding
        "Moving over to the table Trista grabs a pile of donut boxes."
        $ stuffed = 1
        show screen tristafullness
        call trista_gym_feeding from _call_trista_gym_feeding_2
        pause
        hide screen tristafullness
        pause
        trista "Mmm, that was good."
        trista "Might not be at peak fighting strength, but I have never felt so full and so good being this big before."
        trista "Just to see how far I have come, how much I can eat and pack in these days."
        image trista_gym_afterfeeding2 = "/trista/[trista.stage]/gym_afterfeeding2_[stuffed].webp"
        scene trista_gym_afterfeeding2
        $ trista.weight += (trista.fullness / 2)
        $ trista.fullness = 0
        pc "It's impressive."

        #LATER
        image trista_gym_undress1 = "/trista/[trista.stage]/gym_undress1.webp"
        scene trista_gym_undress1
        "Locking your eyes you can see a different type of hunger in her eyes."
        image trista_gym_undress2 = "/trista/[trista.stage]/gym_undress2.webp"
        scene trista_gym_undress2
        "With her bloated belly sticking out of her, she lets her tight clothes fall to the floor."
        image trista_gym_undress3 = "/trista/[trista.stage]/gym_undress3.webp"
        scene trista_gym_undress3
        window hide
        pause
        image trista_gym_undress4 = "/trista/[trista.stage]/gym_undress4.webp"
        scene trista_gym_undress4
        trista "Don't worry, I locked the door."
        image trista_gym_sex1 = "/trista/[trista.stage]/gym_sex1.webp"
        scene trista_gym_sex1
        "Trista walks up to you and pushes you down to the floor."
        if persistent.nosexscene == True:
            scene black
            "You and Trista had a wonderful time together."
            $ stuffed = 0
            stop music fadeout 1.0
            $ trista_gym_today = 1
            return
        image trista_gym_sex2 = "/trista/[trista.stage]/gym_sex2.webp"
        scene trista_gym_sex2
        "As you lay on the ground, she gets above you to give you a good look of her big bloated belly and her juicy wet pussy."
        image trista_gym_sex3 = "/trista/[trista.stage]/gym_sex3.webp"
        scene trista_gym_sex3
        "You get rid of your clothes before Trista lands down her huge body on top of your dick."
        image trista_gym_sex4 = "/trista/[trista.stage]/gym_sex4.webp"
        scene trista_gym_sex4
        "Rubbing your hands over her belly, Trista could only groan under the weight of her own gluttony."
        image trista_gym_sex5 = "/trista/[trista.stage]/gym_sex5.webp"
        scene trista_gym_sex5
        "After a while Trista leans back to get in position."
        "You decide to get a good grip on her large soft thighs."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if trista.stage == 10:
            play movie "/images/trista/10/gym_sex_animation1.webm" loop
        elif trista.stage == 11:
            play movie "/images/trista/11/gym_sex_animation1.webm" loop
        elif trista.stage == 12:
            play movie "/images/trista/12/gym_sex_animation1.webm" loop
        elif trista.stage == 13:
            play movie "/images/trista/13/gym_sex_animation1.webm" loop
        show movie with dissolve
        "Her thighs shaking on either side of you as you feel her weight press down on you with every move."
        trista "I bet you love this, seeing me shake like this."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if trista.stage == 10:
            play movie "/images/trista/10/gym_sex_animation2.webm" loop
        elif trista.stage == 11:
            play movie "/images/trista/11/gym_sex_animation2.webm" loop
        elif trista.stage == 12:
            play movie "/images/trista/12/gym_sex_animation2.webm" loop
        elif trista.stage == 13:
            play movie "/images/trista/13/gym_sex_animation2.webm" loop
        show movie with dissolve
        trista "Look at what you did to me, you have made my ass so fat and jiggly."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if trista.stage == 10:
            play movie "/images/trista/10/gym_sex_animation3.webm" loop
        elif trista.stage == 11:
            play movie "/images/trista/11/gym_sex_animation3.webm" loop
        elif trista.stage == 12:
            play movie "/images/trista/12/gym_sex_animation3.webm" loop
        elif trista.stage == 13:
            play movie "/images/trista/13/gym_sex_animation3.webm" loop
        show movie with dissolve
        "With so much food packed into her huge gut you are amazed she can still move so much."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        if trista.stage == 10:
            play movie "/images/trista/10/gym_sex_animation4.webm" loop
        elif trista.stage == 11:
            play movie "/images/trista/11/gym_sex_animation4.webm" loop
        elif trista.stage == 12:
            play movie "/images/trista/12/gym_sex_animation4.webm" loop
        elif trista.stage == 13:
            play movie "/images/trista/13/gym_sex_animation4.webm" loop
        show movie with dissolve
        "Picking up the pace, she starts moaning louder, clearly indicating she is close."
        window hide
        pause
        trista "Fuuuck!"
        stop movie
        image trista_gym_sex6 = "/trista/[trista.stage]/gym_sex6.webp"
        scene trista_gym_sex6 with vpunch
        "Feeling the pleasure build inside of you, you both orgasm at the same time."
        image trista_gym_sex7 = "/trista/[trista.stage]/gym_sex7.webp"
        scene trista_gym_sex7
        trista "Wow, that was amazing."
        "You cleanup the mess and head home."
        #[Sex scene in the main part of the gym with stuffed Trista.]
        $ stuffed = 0
        stop music fadeout 1.0
        $ trista_gym_today = 1
        return
    stop music fadeout 1.0
    $ trista_gym_today = 1
    return


label trista_gym_2:
    if strength <= 11:
        ###Entering gym with Trista using the weights###
        image trista_gym_dumbel = "/trista/[trista.stage]/gym_dumbel.webp"
        scene trista_gym_dumbel
        "Walking into the gym you spot Trista using the weights."
        "Even with the heavier weights she makes it look effortless, her strong arms lifting them easily."
        "Maybe she would be a good gym partner."
        "I should probably get a bit stronger before offering to help her though."
        "Strength of 12 is required to work out with Trista."
        scene gym
        "You work out for a bit on your own."
        $ strength += 1
        "Strength increased by one point."
        "You take a quick shower and head home."
        $ trista_gym_today = 1
        return

    if strength >= 12 and trista.stage == 1:
        image trista_gym_dumbel2 = "/trista/[trista.stage]/gym_dumbel2.webp"
        scene trista_gym_dumbel2
        "Hey, looks like Trista is working out today. She is making those dumbbells look weightless."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/1/gym_dumbel_vid4.webm" loop
        show movie with dissolve
        "After the last few sessions, you are feeling more confident in your own abilities."
        "But having a gym buddy who really knows what they are doing couldn't hurt."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/1/gym_dumbel_vid2.webm" loop
        show movie with dissolve
        "Walking up to Trista she is so involved with her workout she doesn't even notice."
        pc "Hey, Trista. How are you?"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/1/gym_dumbel_vid3.webm" loop
        show movie with dissolve
        trista "Good, getting in an extra set today."
        trista "It is always good to push yourself, in life but also the gym."
        pc "You make it all look easy. Got any tips?"
        stop movie
        image trista_gym_sitting = "/trista/[trista.stage]/gym_sitting.webp"
        scene trista_gym_sitting
        trista "Sure thing, let's see what we are working with."
        image trista_gym_standing3 = "/trista/[trista.stage]/gym_standing3.webp"
        scene trista_gym_standing3
        "Moving over she indicates for you to take the bench."
        image trista_gym_benchpress = "/trista/[trista.stage]/gym_benchpress.webp"
        scene trista_gym_benchpress
        "Standing behind the bench, Trista spots you as you do a set of lifts."
        "With the cute but fierce blonde looking on, you try to look casual but definitely feel relieved after the last one."
        trista "Not bad, but remember not to lock your elbows between lifts."
        trista "That is an easy way to hurt yourself if you do it with a heavier weight especially."
        pc "Ok, thanks for the help."
        trista "Here, why don’t I show you."
        image trista_gym_benchpress2 = "/trista/[trista.stage]/gym_benchpress2.webp"
        scene trista_gym_benchpress2
        "Repaying the favour you help Trista do a set too, not that it seems like she needs it."
        image trista_gym_standing2 = "/trista/[trista.stage]/gym_standing2.webp"
        scene trista_gym_standing2
        trista "Phew, I can really feel my muscles burning now."
        trista "Thanks for that. I'm able to push harder with someone looking out for me."
        pc "Anytime."
        image trista_gym_animated1 = "/trista/[trista.stage]/gym_animated1.webp"
        scene trista_gym_animated1
        "Doing some more gentle stretches to warm down, you see Trista pick up a set of hand weights."
        image trista_gym_animated2 = "/trista/[trista.stage]/gym_animated2.webp"
        scene trista_gym_animated2
        "Positioning herself on top of an exercise ball, she lifts the weights out to her sides."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/1/gym_animated4.webm" loop
        show movie with dissolve
        window hide
        pause
        "The routine giving you a perfect view of her flexing muscles in her tight gym clothes."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/1/gym_animated3.webm" loop
        show movie with dissolve
        window hide
        pause
        "Leaving Trista to it you continue your workout before heading home after a quick shower."
        stop movie
        scene gym
        $ strength += 1
        "Strength increased by one point."

    if trista.stage == 2:
        image trista_gym_running = "/trista/[trista.stage]/gym_running.webp"
        scene trista_gym_running
        "Entering the gym, you spot Trista is working out on the treadmill."
        "Her stride pattern rhythmically pounding on the machine as she runs."
        "Deciding to see if she wants to pair up again, you walk up to her."
        image trista_gym_running2 = "/trista/[trista.stage]/gym_running2.webp"
        scene trista_gym_running2
        pc "Hey, Trista. How are you?"
        trista "Hey [playername] about to set a new personal best."
        "Finishing up her run, the treadmill slows and she steps off."
        image trista_gym_record = "/trista/[trista.stage]/gym_record.webp"
        scene trista_gym_record
        trista "Yes! Just cut 3 seconds off my 5k time."
        pc "Impressive."
        image trista_gym_standing1 = "/trista/[trista.stage]/gym_standing1.webp"
        scene trista_gym_standing1
        trista "Not sure if that was sarcastic or not, but trust me small gains like that add up."
        pc "I meant it genuinely."
        trista "Oh, thanks."
        trista "Want some pointers on this machine too?"
        pc "Sure, I won’t say no to some more help."
        image trista_gym_running3 = "/trista/[trista.stage]/gym_running3.webp"
        scene trista_gym_running3
        "Getting on the machine you know you can't match Trista’s pace so don't even try."
        "Running along Trista gives you some pointers on your stride length and how to maximise your consistency in pace."
        "It feels like a lot longer than 5k but you finish your workout."
        $ strength += 1
        "Strength increased by one point."
        image trista_gym_standing5 = "/trista/[trista.stage]/gym_standing5.webp"
        scene trista_gym_standing5
        trista "That's a pretty good time for a beginner."
        pc "Thanks, I think."
        trista "Don't worry, you will pick up the pace in no time."
        trista "If you are sticking around, mind spotting for me on something else?"
        pc "Sure, happy to help."
        image trista_stage2_event_34 = "/trista/events/stage2/34.webp"
        scene trista_stage2_event_34
        trista "Just going to do some chin ups."
        pc "What do I need to do?"
        trista "Just stand there and look pretty, but catch me if I fall."
        image trista_gym_pullup = "/trista/[trista.stage]/gym_pullup.webp"
        scene trista_gym_pullup
        "Jumping up Trista grabs the bar, pulling herself up."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/2/gym_pullup_vid1.webm" loop
        show movie with dissolve
        "You can see her arm muscles tensing as she repeatedly lifts herself into the air, using her own bodyweight to train her muscles."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/2/gym_pullup_vid3.webm" loop
        show movie with dissolve
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/2/gym_pullup_vid4.webm" loop
        show movie with dissolve
        "Standing behind her, you get a great view as she repeats the motion over and over."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/2/gym_pullup_vid5.webm" loop
        show movie with dissolve
        "After a few more she jumps down looking pumped."
        stop movie
        image trista_gym_standing7 = "/trista/[trista.stage]/gym_standing7.webp"
        scene trista_gym_standing7
        trista "Thanks for that, it’s one of those things I don’t really feel comfortable doing in an empty gym."
        pc "Happy to help you anytime you need it."
        trista "Thanks, I appreciate it."
        trista "But I better get some actual work done now."
        image trista_gym_animated1 = "/trista/[trista.stage]/gym_animated1.webp"
        scene trista_gym_animated1
        "Doing some more gentle stretches to warm down, you see Trista pick up a set of hand weights."
        image trista_gym_animated2 = "/trista/[trista.stage]/gym_animated2.webp"
        scene trista_gym_animated2
        "Positioning herself on top of an exercise ball, she lifts the weights out to her sides."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/2/gym_animated3.webm" loop
        show movie with dissolve
        window hide
        pause
        "The routine giving you a perfect view of her flexing muscles in her tight gym clothes."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/2/gym_animated4.webm" loop
        show movie with dissolve
        window hide
        pause
        "Her body growing and becoming more distracting with each passing week."
        "Leaving Trista to it you continue your workout before heading home after a quick shower."
        stop movie
        scene gym

    elif trista.stage == 3:
        image trista_gym_running = "/trista/[trista.stage]/gym_running.webp"
        scene trista_gym_running
        "Entering the gym, you spot Trista is working out on the treadmill."
        "Her stride pattern rhythmically pounding on the machine as she runs."
        "You decide to see if she wants to pair up again."
        image trista_gym_running2 = "/trista/[trista.stage]/gym_running2.webp"
        scene trista_gym_running2
        pc "Hey, Trista. How are you?"
        trista "Just about to finish if you are after the treadmill."
        trista "Missed my target this week, so I’m doing another Kilometre."
        pc "No problem. Happy to wait."
        image trista_gym_running = "/trista/[trista.stage]/gym_running.webp"
        scene trista_gym_running
        "Watching her run you try not to be too obvious as you admire her body."
        image trista_gym_standing1 = "/trista/[trista.stage]/gym_standing1.webp"
        scene trista_gym_standing1
        "Finishing her run, Trista jumps off the machine, wiping away sweat as she does so."
        trista "Want me to help you again?"
        pc "Sure, that sounds good."
        image trista_gym_running3 = "/trista/[trista.stage]/gym_running3.webp"
        scene trista_gym_running3
        "Getting on the machine you know you can't match Trista’s pace so don't even try."
        "Running along Trista gives you some pointers on your stride length and how to maximise your consistency in pace."
        "You complete your 5k; it's starting to feel a bit easier."
        $ strength += 1
        "Strength increased by one point."
        image trista_gym_standing5 = "/trista/[trista.stage]/gym_standing5.webp"
        scene trista_gym_standing5
        trista "That's a pretty good time, still some more room for improvement."
        trista "But I would say you are at least average now."
        pc "Thanks...."
        trista "I meant that as a compliment, average for a gym person is what I meant."
        trista "So that probably means you are better than like 65 percent of people out there."
        pc "Sounds a lot better when you put it that way."
        trista "All your hard work is paying off."
        trista "If you are sticking around, mind spotting for me when I do some pull ups?"
        pc "Sure, happy to help."
        image trista_gym_pullup = "/trista/[trista.stage]/gym_pullup.webp"
        scene trista_gym_pullup
        "Jumping up Trista grabs the bar, pulling herself up."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/3/gym_pullup_vid1.webm" loop
        show movie with dissolve
        "You can see her arm muscles tensing as she repeatedly lifts herself into the air, using her own bodyweight to train her muscles."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/3/gym_pullup_vid3.webm" loop
        show movie with dissolve
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/3/gym_pullup_vid4.webm" loop
        show movie with dissolve
        "Standing behind her, you get a great view as she repeats the motion over and over."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/5/gym_pullup_vid4.webm" loop
        show movie with dissolve
        "After a few more she jumps down looking pumped."
        stop movie
        image trista_gym_standing7 = "/trista/[trista.stage]/gym_standing7.webp"
        scene trista_gym_standing7
        trista "Thanks for that, it’s one of those things I don’t really feel comfortable doing in an empty gym."
        pc "Happy to help you anytime you need it."
        trista "Thanks, I appreciate it."
        trista "But I better get some actual work done now."
        image trista_gym_animated1 = "/trista/[trista.stage]/gym_animated1.webp"
        scene trista_gym_animated1
        "Doing some more gentle stretches to warm down, you see Trista pick up a set of hand weights."
        image trista_gym_animated2 = "/trista/[trista.stage]/gym_animated2.webp"
        scene trista_gym_animated2
        "Positioning herself on top of an exercise ball, she lifts the weights out to her sides."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/3/gym_animated3.webm" loop
        show movie with dissolve
        window hide
        pause
        "The routine giving you a perfect view of her flexing muscles in her tight gym clothes."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/3/gym_animated4.webm" loop
        show movie with dissolve
        window hide
        pause
        "Her body growing and becoming more distracting with each passing week."
        "Leaving Trista to it you continue your workout before heading home after a quick shower."
        stop movie
        scene gym

    elif trista.stage == 4 or trista.stage == 5 or trista.stage == 6:
        image trista_gym_running = "/trista/[trista.stage]/gym_running.webp"
        scene trista_gym_running
        "Entering the gym, you spot Trista is working out on the treadmill."
        "Her stride pattern rhythmically pounding on the machine as she runs."
        "You decide to see if she wants to pair up again."
        image trista_gym_running2 = "/trista/[trista.stage]/gym_running2.webp"
        scene trista_gym_running2
        pc "Hey, Trista. How are you?"
        trista "Just about to finish."
        trista "Missed my target this week so doing another kilometer."
        pc "No problem. Happy to wait."
        image trista_gym_running = "/trista/[trista.stage]/gym_running.webp"
        scene trista_gym_running
        "Watching her run you try not to be too obvious as you admire her body."
        "Judging by the extra jiggle, it's clear her recent eating habits are having an impact on her figure, not that it was a bad look for her."
        image trista_gym_standing1 = "/trista/[trista.stage]/gym_standing1.webp"
        scene trista_gym_standing1
        "Finishing her run, Trista jumps off the machine, wiping away sweat as she does so."
        trista "Want me to help you again?"
        pc "Sure, that sounds good."
        image trista_gym_running3 = "/trista/[trista.stage]/gym_running3.webp"
        scene trista_gym_running3
        "Getting on the machine you are getting closer to Trista's speed, but still have some way to go."
        "Although if she keeps slowing down, maybe you will meet in the middle eventually."
        "Running along Trista gives you some pointers on your stride length and how to maximise your consistency in pace."
        "You complete your 5k; it's starting to feel a bit easier."
        $ strength += 1
        "Strength increased by one point."
        image trista_gym_standing5 = "/trista/[trista.stage]/gym_standing5.webp"
        scene trista_gym_standing5
        trista "That's a pretty good time, still some more room for improvement."
        pc "Thanks, definitely feeling stronger lately."
        trista "That's good. All your hard work is paying off."
        trista "If you are sticking around, mind spotting for me when I do some pull ups?"
        pc "Absolutely."
        image trista_gym_pullup = "/trista/[trista.stage]/gym_pullup.webp"
        scene trista_gym_pullup
        "Jumping up Trista grabs the bar, pulling herself up."
        if trista.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/4/gym_pullup_vid1.webm" loop
            show movie with dissolve
            "Standing behind her, you get a great view as she repeats the motion over and over."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/4/gym_pullup_vid3.webm" loop
            show movie with dissolve
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/4/gym_pullup_vid2.webm" loop
            show movie with dissolve
            "Despite her confident appearance earlier, you can see she is finding it harder than usual."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/4/gym_pullup_vid4.webm" loop
            show movie with dissolve
            "It shouldn’t have been a surprise, given her growing weight."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/4/gym_pullup_vid5.webm" loop
            show movie with dissolve
        elif trista.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/gym_pullup_vid1.webm" loop
            show movie with dissolve
            "Standing behind her, you get a great view as she repeats the motion over and over."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/gym_pullup_vid3.webm" loop
            show movie with dissolve
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/gym_pullup_vid2.webm" loop
            show movie with dissolve
            "Despite her confident appearance earlier, you can see she is finding it harder than usual."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/gym_pullup_vid4.webm" loop
            show movie with dissolve
            "It shouldn’t have been a surprise, given her growing weight."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/gym_pullup_vid5.webm" loop
            show movie with dissolve
        elif trista.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/gym_pullup_vid1.webm" loop
            show movie with dissolve
            "Standing behind her, you get a great view as she repeats the motion over and over."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/gym_pullup_vid3.webm" loop
            show movie with dissolve
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/gym_pullup_vid2.webm" loop
            show movie with dissolve
            "Despite her confident appearance earlier, you can see she is finding it harder than usual."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/gym_pullup_vid4.webm" loop
            show movie with dissolve
            "It shouldn’t have been a surprise, given her growing weight."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/gym_pullup_vid5.webm" loop
            show movie with dissolve
        "After a few more she jumps down looking a bit tired."
        stop movie
        image trista_gym_standing7 = "/trista/[trista.stage]/gym_standing7.webp"
        scene trista_gym_standing7
        trista "Phew, that was harder than I remember."
        trista "Guess I shouldn’t be surprised with the bulking and muscles I am building."
        trista "Thanks for your help again."
        pc "Happy to help you anytime you need it."
        trista "I appreciate it."
        trista "See you for our usual session."
        pc "I’ll be there."
        trista "Looking forward to it."
        image trista_gym_animated1 = "/trista/[trista.stage]/gym_animated1.webp"
        scene trista_gym_animated1
        "Doing some more gentle stretches to warm down, you see Trista pick up a set of hand weights."
        image trista_gym_animated2 = "/trista/[trista.stage]/gym_animated2.webp"
        scene trista_gym_animated2
        "Positioning herself on top of an exercise ball, she lifts the weights out to her sides."
        if trista.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/4/gym_animated3.webm" loop
            show movie with dissolve
            window hide
            pause
            "The routine giving you a perfect view of her flexing muscles in her tight gym clothes."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/4/gym_animated4.webm" loop
            show movie with dissolve
        elif trista.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/gym_animated3.webm" loop
            show movie with dissolve
            window hide
            pause
            "The routine giving you a perfect view of her flexing muscles in her tight gym clothes."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/gym_animated4.webm" loop
            show movie with dissolve
        elif trista.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/gym_animated3.webm" loop
            show movie with dissolve
            window hide
            pause
            "The routine giving you a perfect view of her flexing muscles in her tight gym clothes."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/gym_animated4.webm" loop
            show movie with dissolve
        window hide
        pause
        "Her body growing and becoming more distracting with each passing week."
        "Leaving Trista to it you continue your workout before heading home after a quick shower."
        stop movie
        scene gym

    elif trista.stage == 7:
        image trista_gym_running = "/trista/[trista.stage]/gym_running.webp"
        scene trista_gym_running
        "Entering the gym, you spot Trista is working out on the treadmill."
        "You notice an empty burger box and several discard drinks around the treadmill."
        "Her stride pattern rhythmically pounding on the machine as she runs."
        "You decide to see if she wants to pair up again."
        image trista_gym_running2 = "/trista/[trista.stage]/gym_running2.webp"
        scene trista_gym_running2
        pc "Hey, Trista. How are you?"
        trista "Just about to finish."
        trista "Only doing a bit of cardio today so won't be long."
        pc "No problem. Happy to wait."
        image trista_gym_running = "/trista/[trista.stage]/gym_running.webp"
        scene trista_gym_running
        "Watching her run you try not to be too obvious as you admire her body."
        "Judging by the extra jiggle, it's clear her recent eating habits are having an impact on her figure, not that it was a bad look for her."
        image trista_gym_standing1 = "/trista/[trista.stage]/gym_standing1.webp"
        scene trista_gym_standing1
        "Finishing her run, Trista jumps off the machine, wiping away sweat as she does so."
        trista "Want me to help you again?"
        pc "Sure, that sounds good."
        image trista_gym_running3 = "/trista/[trista.stage]/gym_running3.webp"
        scene trista_gym_running3
        "Getting on the machine you know you almost match the speed Trista was managing, or at least the pace she is doing lately."
        "You complete your 5k with ease."
        $ strength += 1
        "Strength increased by one point."
        image trista_gym_standing5 = "/trista/[trista.stage]/gym_standing5.webp"
        scene trista_gym_standing5
        trista "That's a pretty good time, still some more room for improvement."
        pc "Thanks, definitely feeling stronger lately."
        trista "That's good. All your hard work is paying off."
        trista "If you are sticking around, mind spotting for me when I do some pull ups?"
        pc "Absolutely."
        image trista_gym_pullup = "/trista/[trista.stage]/gym_pullup.webp"
        scene trista_gym_pullup
        "Jumping up Trista grabs the bar, pulling herself up."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/7/gym_pullup_vid1.webm" loop
        show movie with dissolve
        "Standing behind her, you get a great view of her sizeable and supple looking ass."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/7/gym_pullup_vid3.webm" loop
        show movie with dissolve
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/7/gym_pullup_vid2.webm" loop
        show movie with dissolve
        "There is a definite slowness to her movements as Trista grunts slightly with each one."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/7/gym_pullup_vid4.webm" loop
        show movie with dissolve
        "Her focus on her legs and increasing size causing her some serious issues."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/7/gym_pullup_vid5.webm" loop
        show movie with dissolve
        "After just a handful of pullups she jumps down looking tired."
        stop movie
        image trista_gym_standing7 = "/trista/[trista.stage]/gym_standing7.webp"
        scene trista_gym_standing7
        trista "Phew, that’s a good workout."
        trista "Thanks for your help again."
        pc "Happy to help you anytime you need it."
        image trista_gym_animated1 = "/trista/[trista.stage]/gym_animated1.webp"
        scene trista_gym_animated1
        "Doing some more gentle stretches to warm down, you see Trista pick up a set of hand weights."
        image trista_gym_animated2 = "/trista/[trista.stage]/gym_animated2.webp"
        scene trista_gym_animated2
        "Positioning herself on top of an exercise ball, she lifts the weights out to her sides."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/7/gym_animated3.webm" loop
        show movie with dissolve
        window hide
        pause
        "The routine giving you a perfect view of her flexing muscles in her tight gym clothes."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/7/gym_animated4.webm" loop
        show movie with dissolve
        window hide
        pause
        "Her body growing and becoming more distracting with each passing week."
        stop movie
        image trista_gym_standing2 = "/trista/[trista.stage]/gym_standing2.webp"
        scene trista_gym_standing2
        trista "So, are you ready to repay the favour with a different kind of one-on-one training?"
        pc "It would only be fair, considering all the attention you have given me."
        trista "Well, first maybe we should boost my calorie’s before we burn them off."
        trista "I’m sure we can find a way of making it just as fun."
        image trista_gym_beforefeeding = "/trista/[trista.stage]/gym_beforefeeding.webp"
        scene trista_gym_beforefeeding
        "Moving over to the table Trista grabs a pile of donut boxes."
        pc "Here let me help."
        $ stuffed = 1
        show screen tristafullness
        call trista_gym_feeding from _call_trista_gym_feeding_3
        pause
        hide screen tristafullness
        pause
        trista "You’re a great trainer, exactly what I need to reach the next level."
        "Finishing up you help Trista tidy away the empty boxes and head home."

    elif trista.stage == 8:
        image trista_gym_running = "/trista/[trista.stage]/gym_running.webp"
        scene trista_gym_running
        "Entering the gym, you spot Trista is working out on the treadmill."
        "You notice an empty burger box and several discard drinks around the treadmill."
        "Her stride pattern is clearly slower and heavier than it has been before."
        "You decide to see if she wants to pair up again."
        image trista_gym_running2 = "/trista/[trista.stage]/gym_running2.webp"
        scene trista_gym_running2
        pc "Hey, Trista. How are you?"
        trista "Just about to finish."
        trista "Only doing a bit of cardio today so won't be long."
        pc "No problem. Happy to wait."
        image trista_gym_running = "/trista/[trista.stage]/gym_running.webp"
        scene trista_gym_running
        "Watching her run you try not to be too obvious as you admire her body."
        "Her recent eating habits are having a clear impact on her figure."
        image trista_gym_standing1 = "/trista/[trista.stage]/gym_standing1.webp"
        scene trista_gym_standing1
        "Finishing her run, Trista jumps off the machine, wiping away sweat as she does so."
        trista "Want me to help you again?"
        pc "Sure, that sounds good."
        image trista_gym_running3 = "/trista/[trista.stage]/gym_running3.webp"
        scene trista_gym_running3
        "Getting on the machine you complete your run easily."
        $ strength += 1
        "Strength increased by one point."
        image trista_gym_standing5 = "/trista/[trista.stage]/gym_standing5.webp"
        scene trista_gym_standing5
        trista "That's a pretty good time, getting close to my personal best."
        pc "Thanks, definitely feeling stronger lately."
        trista "That's good. All your hard work is paying off."
        image trista_stage8_113 = "/trista/events/stage8/113.webp"
        scene trista_stage8_113
        "You notice Trista glance at the pull up bar she usually uses at this point."
        image trista_stage8_114 = "/trista/events/stage8/114.webp"
        scene trista_stage8_114
        "But instead of saying anything she just smiles a bit awkwardly at you."
        trista "Thanks for the work out, it's always nice to have someone else in here with me."
        pc "Anytime."
        image trista_stage8_115 = "/trista/events/stage8/115.webp"
        scene trista_stage8_115
        trista "You want some help on the weights?"
        pc "Sure, that would be great."
        image trista_gym_benchpress = "/trista/[trista.stage]/gym_benchpress.webp"
        scene trista_gym_benchpress
        "Standing behind the bench, Trista spots you as you do a set of reps."
        trista "Good form."
        image trista_gym_standing3 = "/trista/[trista.stage]/gym_standing3.webp"
        scene trista_gym_standing3
        pc "Thanks, want me to spot you?"
        trista "No, that's ok. Think I just need to do some push ups or something to finish up."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/events/stage8/gym1.webm" loop
        show movie with dissolve
        window hide
        pause
        "Getting on her hands and knees, Trista begins doing push ups."
        "Her growing ass rising and falling into the air, the unmistakable wobble of a fattening body accompanying it."
        "After a few more, she breaths out in relief and stands up."
        stop movie
        image trista_stage8_116 = "/trista/events/stage8/116.webp"
        scene trista_stage8_116
        trista "I think that does it for now."
        image trista_gym_animated1 = "/trista/[trista.stage]/gym_animated1.webp"
        scene trista_gym_animated1
        "Doing some more gentle stretches to warm down, you see Trista pick up a set of hand weights."
        image trista_gym_animated2 = "/trista/[trista.stage]/gym_animated2.webp"
        scene trista_gym_animated2
        "Positioning herself on top of an exercise ball, she lifts the weights out to her sides."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/8/gym_animated3.webm" loop
        show movie with dissolve
        window hide
        pause
        "The routine giving you a perfect view of her flexing muscles in her tight gym clothes."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/8/gym_animated4.webm" loop
        show movie with dissolve
        window hide
        pause
        "Her body growing and becoming more distracting with each passing week."
        stop movie
        image trista_gym_standing2 = "/trista/[trista.stage]/gym_standing2.webp"
        scene trista_gym_standing2
        trista "Fancy helping me out again with my bulking again?"
        image trista_gym_beforefeeding = "/trista/[trista.stage]/gym_beforefeeding.webp"
        scene trista_gym_beforefeeding
        "Moving over to the table Trista grabs a pile of donut boxes."
        pc "Here let me help."
        $ stuffed = 1
        show screen tristafullness
        call trista_gym_feeding from _call_trista_gym_feeding_4
        pause
        hide screen tristafullness
        pause
        trista "You're a great trainer, exactly what I need to reach the next level."
        "Finishing up you help Trista tidy away the empty boxes and head home."

    elif trista.stage == 9:
        ####Stage 9b #### NEW
        image trista_gym_running = "/trista/[trista.stage]/gym_running.webp"
        scene trista_gym_running
        "Entering the gym, you spot Trista is working out on the treadmill."
        "Her stride pattern a little asymmetrical and heavier than it has been before."
        "You notice the usual mess of empty burger boxes and discard drinks around the treadmill."
        "Deciding to see if she wants to pair up again, you walk up to her."
        image trista_gym_running2 = "/trista/[trista.stage]/gym_running2.webp"
        scene trista_gym_running2
        pc "Hey Trista, how are you?"
        trista "Just about to finish."
        trista "Only doing a bit of cardio today so won't be long."
        pc "No problem, happy to wait."
        image trista_gym_running = "/trista/[trista.stage]/gym_running.webp"
        scene trista_gym_running
        "Watching her run you try not to be too obvious as you admire her body."
        "Her recent eating habits are having a clear impact on Trista’s figure, her still toned but much larger rear bouncing with each step."
        image trista_gym_standing1 = "/trista/[trista.stage]/gym_standing1.webp"
        scene trista_gym_standing1
        "Finishing off Trista jumps off the machine, wiping away a heavy layer of sweat as she does so."
        trista "Want me to help you again?"
        pc "Sure, that sounds good."
        image trista_gym_running3 = "/trista/[trista.stage]/gym_running3.webp"
        scene trista_gym_running3
        "Getting on the machine you set off as Trista grabs another drink."
        #PIC NEEDED
        "With your improved fitness you run along easily, giving you plenty of time to watch Trista eat."
        #PIC NEEDED
        "With how big her ass was getting, you wonder how long it will be before she can't even fit on the treadmill."
        "Finishing your run, you feel your fitness has increased."
        $ strength += 1
        "Strength increased by one point."
        image trista_gym_standing5 = "/trista/[trista.stage]/gym_standing5.webp"
        scene trista_gym_standing5
        trista "Thats a pretty good time, less than 30 seconds off what I managed this morning."
        pc "Thanks, definitely feeling fitter lately."
        trista "Thats good, all your hard work is paying off."
        trista "Think its time for some core workout though."
        ##usual bonnie workout animation but with Trista###
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/9/gym_animated5.webm" loop
        show movie with dissolve
        window hide
        pause
        "Grabbing a yoga ball, Trista just about manages to do a set of sit ups."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/9/gym_animated6.webm" loop
        show movie with dissolve
        window hide
        pause
        "The ball under her clearly struggling slightly to support her."
        "After a few more she stands back up, almost losing her balance."
        stop movie
        image trista_gym_standing7 = "/trista/[trista.stage]/gym_standing7.webp"
        scene trista_gym_standing7
        trista "I think I have earned a quick food break if you want to join me."
        pc "Sure thing, happy to help."
        trista "I bet you are."
        $ stuffed = 1
        show screen tristafullness
        call trista_gym_feeding from _call_trista_gym_feeding_5
        pause
        hide screen tristafullness
        pause
        "Finishing up you help Trista tidy away the empty wrappers and head home."
        if katrine.stage >= trista.stage:
            $ trista.weight += (trista.fullness / 2)
        $ trista.fullness = 0
        $ stuffed = 0
        stop music fadeout 1.0
        $ trista_gym_today = 1
        return

    elif trista.stage >= 10:
        ####Stage 10b+ #### NEW
        "Entering the gym, you spot Trista is working out on the treadmill."
        "Her stride pattern a little asymmetrical and heavier than it has been before."
        "You notice the usual mess of empty burger boxes and discard drinks around the treadmill."
        "Deciding to see if she wants to pair up again, you walk up to her."
        ###Sweaty Trista##
        pc "Hey Trista, how are you?"
        trista "I’m…ok…thanks."
        "Despite her sentence, she is clearly struggling to keep up her pace."
        "Watching her run you admire her body, her sizable rear now jiggling much more than it had before."
        "Her binges and bulking really taking their toll on her once trim and muscular body."
        "Finishing her run a tired looking Trista steps off the machine, wiping away a heavy layer of sweat as she does so."
        trista "I’ll be able to help you in a minute."
        trista "Just need a quick breather."
        pc "No worries, I think I can handle the treadmill for now."
        trista "Great."
        "Getting on the machine you see Trista grab another drink."
        "Sitting on the side she slurps down her drink watching you run."
        "With your improved fitness it doesn’t take you long to finish with some ease."
        $ strength += 1
        "Strength increased by one point."
        pc "Want me to help you with anything?"
        trista "Probably going to work on my core."
        ##usual bonnie workout animation but with Trista###
        "Grabbing a yoga ball, Trista just about manages to do a set of sit ups."
        "The ball under her clearly struggling to support her."
        "After a few more she stands back up, almost losing her balance."
        "Puffing out her cheeks she goes back down and begins doing some push ups."
        ##Lisa push up animation##
        "From behind her you admire Trista’s ass and body as she lifts it into the air."
        "After just a few she stands up again."
        trista "That was a good workout but I think my body could do with a rest."
        trista "I’m going to hop in the sauna if you want to join."
        pc "Absolutely."
        ##Sauna##
        play music "/music/sauna.ogg" if_changed
        "Walking into the Sauna, Trista strips naked and relaxes on one of the benches."
        "Joining her, your eyes explore each other, the sweat glistening on your bodies as things heat up."
        "You can’t hide your arousal as you take in Trista’s naked and fat body."
        "A body that was growing by your hand, with each doughnut you force into her greedy mouth."
        trista "Seems like someone enjoys the Sauna."
        "Saying nothing else Trista gets up before getting onto her knees between your legs."
        "Placing her hand gently on your erect penis she begins stroking it, enjoying your moans of pleasure."
        ##BJ animation?##
        "Placing her hand lower you feel her soft lips wrap themselves around you."
        "Moving her head back and forth you struggle to control yourself, trying to prolong the pleasure."
        "Eventually you can take it no more and erupt over her face."
        trista "Mmm, that was fun."
        "Cleaning her face off in a towel, you watch her start to get dressed."
        trista "Would love to stay longer, but I have another client coming in shortly."
        trista "Feel free to stay as long as you like."
        "Giving yourself a couple more minutes to enjoy the Sauna you head back home."

    if katrine.stage >= trista.stage:
        if trista.stage >= 7:
            $ trista.weight += (trista.fullness / 2)
        else:
            $ trista.weight += 0.5
    $ trista.fullness = 0
    $ stuffed = 0
    stop music fadeout 1.0
    $ trista_gym_today = 1
    return

label trista_date:
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    if trista.stage >= 2 and tristastage3event == 1:
        ###Arriving at the gym###
        image trista_gym_dumbel = "/trista/[trista.stage]/gym_dumbel.webp"
        scene trista_gym_dumbel
        "Walking in you spot Trista lifting some weights."
        pc "Hey, Trista."
        image trista_gym_sitting = "/trista/[trista.stage]/gym_sitting.webp"
        scene trista_gym_sitting
        trista "Hey, [playername]. Hope you are ready to sweat."
        trista "I know you are new to this but I'm not going to be taking it easy on you."
        pc "I'm good to go."
        trista "Great. Let's start with some cardio to warm up."

        ####At treadmill####
        image trista_gym_running3 = "/trista/[trista.stage]/gym_running3.webp"
        scene trista_gym_running3
        trista "I think a quick five kilometre run should do."
        "Setting the speed fairly low, Trista talks you through the run."
        "Watching you she gives you some tips on stride pattern and breathing to help your form."
        "It takes a bit of effort but you soon finish your run."
        image trista_gym_standing5 = "/trista/[trista.stage]/gym_standing5.webp"
        scene trista_gym_standing5
        trista "Well done. For a beginner that wasn't that bad."
        pc "Thanks, I think."
        image trista_gym_drink = "/trista/[trista.stage]/gym_drink.webp"
        scene trista_gym_drink
        "Grabbing a drink for you Trista hands it to you while drinking from her own large drink."
        trista "Need to stay hydrated."
        if tristastory == 0:
            "Slurping it down Trista finishes her own larger drink."
            menu:
                "Ask Trista about herself.":
                    "You decide to ask Trista about herself."
                    trista "I don't talk much about myself to others."
                    trista "But okay, if you want to know."
                    "Trista talks a bit about herself."
                    $ tristastory += 1
                    #Unlocks more Trista story in the stats page.
                    $ renpy.notify("New Trista story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Trista anything."
        else:
            "Slurping it down Trista finishes her own larger drink."
        "Right then, let's do some weight work."

        ### On the weight bench###
        image trista_gym_standing6 = "/trista/[trista.stage]/gym_standing6.webp"
        scene trista_gym_standing6
        trista "Let's start you off easy with a few sets of low weights."
        pc "Sounds good to me."
        image trista_gym_lifting1 = "/trista/[trista.stage]/gym_lifting1.webp"
        scene trista_gym_lifting1
        "As you begin your reps you can see Trista open a big box of donuts."
        "Again, while you work she gives you tips between filling her mouth."
        image trista_gym_standing1 = "/trista/[trista.stage]/gym_standing1.webp"
        scene trista_gym_standing1
        trista "Okay, that should do for now."
        trista "We can start upping the weights slowly over time."
        trista "Now I think we should do a warm down and check out for flexibility."

        ###Yoga mat / just on the floor.###
        image trista_gym_yoga1 = "/trista/[trista.stage]/gym_yoga1.webp"
        scene trista_gym_yoga1
        trista "Okay, lay down there and pick your left leg up."
        "Laying down on your back you lift your leg up in the air."
        image trista_gym_yoga2 = "/trista/[trista.stage]/gym_yoga2.webp"
        scene trista_gym_yoga2
        "Taking hold of it, Trista pushes it towards you with her weight."
        "It feels a bit odd but in a good way, her body almost pressing up against yours in her tight gym clothing."
        trista "Alright, now the other."
        image trista_gym_yoga3 = "/trista/[trista.stage]/gym_yoga3.webp"
        scene trista_gym_yoga3
        "Repeating the process she leans in towards you, almost looking you in the eyes."
        "You seem to catch each other's attention before the doorbell rings, breaking the moment."
        image trista_gym_yoga4 = "/trista/[trista.stage]/gym_yoga4.webp"
        scene trista_gym_yoga4
        trista "That's got to be Marie again."
        pc "Marie?"
        trista "Yeah. Ever since she agreed to sponsor the event she has been sending me deliveries each week."
        image trista_gym_yoga5 = "/trista/[trista.stage]/gym_yoga5.webp"
        scene trista_gym_yoga5
        trista "I'll be right back."
        "Standing up you wait for her to return."
        image trista_gym_yoga6 = "/trista/[trista.stage]/gym_yoga6.webp"
        scene trista_gym_yoga6
        "Walking back in, Trista returns with a two takeaway bags."
        trista "I don't know why she sends so much. I've told her she doesn't need to."
        image trista_gym_yoga7 = "/trista/[trista.stage]/gym_yoga7.webp"
        scene trista_gym_yoga7
        trista "Mind if I take my lunch break? Don't want this to go cold."
        trista "You could join me if you like?"
        pc "Sure thing."

        ###Move to somewhere to sit###
        image trista_gym_yoga8 = "/trista/[trista.stage]/gym_yoga8.webp"
        scene trista_gym_yoga8
        "Sitting next to her you make small talk as she dives into her meal."
        "It doesn't take long for her to devour the pizza."
        trista "Mmm, best pizza in town."
        image trista_gym_yoga9 = "/trista/[trista.stage]/gym_yoga9.webp"
        scene trista_gym_yoga9
        "Moving on, she starts working on the burger, occasionally pausing to add a handful of fries or even nuggets to her binge."
        "You can already see her stomach growing from the large meal as she continues to eat."
        image trista_gym_yoga10 = "/trista/[trista.stage]/gym_yoga10.webp"
        scene trista_gym_yoga10
        "Soon all that's left if a selection of empty boxes, the high calorie meal now sitting heavily in Trista's growing belly."
        trista "Oooh, that was good."
        image trista_gym_yoga11 = "/trista/[trista.stage]/gym_yoga11.webp"
        scene trista_gym_yoga11
        trista "Although, as my client I should tell you to make sure not to eat like that."
        if katrine.stage >= trista.stage:
            $ trista.weight += 1
        trista "I thankfully have a metabolism that can deal with it and spend most of my free time working out."
        pc "I don't think I could eat that much even if I tried."
        trista "That's probably a good thing."
        trista "But for now, I think our session is over."
        trista "Thanks for coming over and chatting. I had fun."
        pc "Me too. See you around, Trista."
        stop music fadeout 1.0

    elif trista.stage == 3 and tristastage3event == 0:
        ###Arriving at the gym###
        image trista_gym_dumbel = "/trista/[trista.stage]/gym_dumbel.webp"
        scene trista_gym_dumbel
        "Walking in you spot Trista lifting some weights."
        pc "Hey, Trista."
        image trista_gym_sitting = "/trista/[trista.stage]/gym_sitting.webp"
        scene trista_gym_sitting
        trista "Hey, [playername]. Hope you are ready to sweat."
        trista "I know you are new to this but I'm not going to be taking it easy on you."
        pc "I'm good to go."
        trista "Great. Let's start with some cardio to warm up."

        ####At treadmill####
        image trista_gym_running3 = "/trista/[trista.stage]/gym_running3.webp"
        scene trista_gym_running3
        trista "I think a quick five kilometre run should do."
        "Setting the speed fairly low, Trista talks you through the run."
        "Watching you she gives you some tips on stride pattern and breathing to help your form."
        "It takes a bit of effort but you soon finish your run."
        image trista_gym_standing5 = "/trista/[trista.stage]/gym_standing5.webp"
        scene trista_gym_standing5
        trista "Well done. For a beginner that wasn't that bad."
        pc "Thanks, I think."
        image trista_gym_drink = "/trista/[trista.stage]/gym_drink.webp"
        scene trista_gym_drink
        "Grabbing a drink for you, Trista hands it to you while drinking from her own large drink."
        trista "Need to stay hydrated."
        if tristastory == 0:
            "Slurping it down Trista finishes her own larger drink."
            menu:
                "Ask Trista about herself.":
                    "You decide to ask Trista about herself."
                    trista "I don't talk much about myself to others."
                    trista "But okay, if you want to know."
                    "Trista talks a bit about herself."
                    $ tristastory += 1
                    #Unlocks more Trista story in the stats page.
                    $ renpy.notify("New Trista story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Trista anything."
        else:
            "Slurping it down Trista finishes her own larger drink."
        "Right then, let's do some weight work."

        ### On the weight bench###
        image trista_gym_standing6 = "/trista/[trista.stage]/gym_standing6.webp"
        scene trista_gym_standing6
        trista "Let's start you off easy with a few sets of low weights."
        pc "Sounds good to me."
        image trista_gym_lifting1 = "/trista/[trista.stage]/gym_lifting1.webp"
        scene trista_gym_lifting1
        "As you begin your reps you can see Trista open a box of donuts."
        "While you work out she gives you tips between filling her mouth."
        image trista_gym_standing1 = "/trista/[trista.stage]/gym_standing1.webp"
        scene trista_gym_standing1
        trista "Okay, that should do for now."
        trista "We can start upping the weights slowly over time."
        trista "Now I think we should do a warm down and check out for flexibility."

        ###Yoga mat / just on the floor.###
        image trista_gym_yoga1 = "/trista/[trista.stage]/gym_yoga1.webp"
        scene trista_gym_yoga1
        trista "Okay, lay down there and pick your left leg up."
        "Laying down on your back you lift your leg up in the air."
        image trista_gym_yoga2 = "/trista/[trista.stage]/gym_yoga2.webp"
        scene trista_gym_yoga2
        "Taking hold of it, Trista pushes it towards you with her weight."
        "It feels a bit odd but in a good way, her body almost pressing up against yours in her tight gym clothing."
        trista "Alright, now the other."
        image trista_gym_yoga3 = "/trista/[trista.stage]/gym_yoga3.webp"
        scene trista_gym_yoga3
        "Repeating the process she leans in towards you, almost looking you in the eyes."
        "You seem to catch each others attention before the doorbell rings, breaking the moment."
        image trista_gym_yoga4 = "/trista/[trista.stage]/gym_yoga4.webp"
        scene trista_gym_yoga4
        trista "That's probably Marie again."
        image trista_gym_yoga5 = "/trista/[trista.stage]/gym_yoga5.webp"
        scene trista_gym_yoga5
        trista "I'll be right back."
        "Standing up you wait for her to return."
        image trista_gym_yoga6 = "/trista/[trista.stage]/gym_yoga6.webp"
        scene trista_gym_yoga6
        "Walking back in, Trista returns with a two takeaway bags."
        trista "I don't know why she sends so much, I have told her she doesn't need to."
        trista "I almost feel guilty about how much food I'm getting out of that place."
        image trista_gym_yoga7 = "/trista/[trista.stage]/gym_yoga7.webp"
        scene trista_gym_yoga7
        trista "Mind if I take my lunch break? Don't want this to go cold."
        trista "You could join me if you like?"
        pc "Sure thing."

        ###Move to somewhere to sit###
        image trista_gym_yoga8 = "/trista/[trista.stage]/gym_yoga8.webp"
        scene trista_gym_yoga8
        "Sitting next to her you make small talk as she dives into her meal."
        "It doesn't take long for her to devour the pizza."
        trista "Mmm, best pizza in town."
        image trista_gym_yoga9 = "/trista/[trista.stage]/gym_yoga9.webp"
        scene trista_gym_yoga9
        "Moving on, she starts working on the burgers, occasionally pausing to add a handful of fries or even nuggets to her binge."
        "You can already see her stomach growing from the large meal as she continues to eat."
        image trista_gym_yoga10 = "/trista/[trista.stage]/gym_yoga10.webp"
        scene trista_gym_yoga10
        "But soon all that's left is a selection of empty boxes, the high calorie meal now sitting heavily in Trista's growing belly."
        trista "Oooh, that was good."
        image trista_gym_yoga11 = "/trista/[trista.stage]/gym_yoga11.webp"
        scene trista_gym_yoga11
        trista "But for now, I think our session is over, unless maybe you would like to join me in the sauna."
        if katrine.stage >= trista.stage:
            $ trista.weight += 1
        pc "Definitely, I think I could use some heat to help me warm down."
        "Smiling Trista leads you to the sauna."
        stop music fadeout 1.0

        ### In Sauna###
        image trista_sauna_enter = "/trista/[trista.stage]/sauna_enter.webp"
        scene trista_sauna_enter
        play music "/music/sauna.ogg" if_changed
        "Standing by the door, you hear a click as Trista locks the door."
        trista "Don't want any unwanted visitors do we."
        image trista_sauna_undress = "/trista/[trista.stage]/sauna_undress.webp"
        scene trista_sauna_undress
        "Slowly starting to undress you follow her lead."
        if persistent.nosexscene == True:
            scene black
            "You and Trista had a wonderful time together."
            image trista_sauna_aftersex = "/trista/[trista.stage]/sauna_aftersex.webp"
            scene trista_sauna_aftersex
            trista "That was amazing, you really know how to please a woman."
            pc "And you know how to rock your body."
            trista "We need to do this more often."
            "After a while both of you decide to head out and go home."
            stop music fadeout 1.0
            $ trista_gym_today = 1
            return
        image trista_sauna_beforesex = "/trista/[trista.stage]/sauna_beforesex.webp"
        scene trista_sauna_beforesex
        window hide
        pause
        "Trista turns around to show you her big butt."
        "Her juicy round ass seems to slowly draws you in."
        image trista_sauna_sex1 = "/trista/[trista.stage]/sauna_sex1.webp"
        scene trista_sauna_sex1
        window hide
        pause
        "You kneel down and plant your face in between her soft ass cheeks."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/3/sauna_sex1_video.webm" loop
        show movie with dissolve
        window hide
        pause
        trista "That's it, keep it going."
        trista "Right there-{w} OHHHH!"
        trista "HOLY FUCK!!"
        "Trista collapses for a moment before standing up again, she only wants one thing from you."
        stop movie
        image trista_sauna_sex2 = "/trista/[trista.stage]/sauna_sex2.webp"
        scene trista_sauna_sex2
        trista "Go ahead, take me from behind."
        "You gladly accept her request as you line up your rock hard dick with her wet pussy."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/3/sauna_sex2_video.webm" loop
        show movie with dissolve
        window hide
        pause
        "While rocking you hips back and forth Trista her huge ass seems to absorb most of the impact from your thrusts."
        window hide
        pause
        "After a few minutes you feel the pressure build up, not long after that you climax while pressing you body against her soft behind."
        stop movie
        image trista_sauna_aftersex = "/trista/[trista.stage]/sauna_aftersex.webp"
        scene trista_sauna_aftersex
        trista "That was amazing, you really know how to please a woman."
        pc "And you know how to rock your body."
        trista "We need to do this more often."
        "After a while both of you decide to head out and go home."

    elif trista.stage == 4:
        ###Arriving at the gym###
        image trista_gym_dumbel = "/trista/[trista.stage]/gym_dumbel.webp"
        scene trista_gym_dumbel
        "Walking in you spot Trista lifting some weights."
        pc "Hey, Trista."
        image trista_gym_sitting = "/trista/[trista.stage]/gym_sitting.webp"
        scene trista_gym_sitting
        trista "Hey, [playername]. Hope you are ready to sweat."
        pc "I'm good to go."
        trista "Great, let's start with the usual cardio to warm up."

        ####At treadmill####
        image trista_gym_running3 = "/trista/[trista.stage]/gym_running3.webp"
        scene trista_gym_running3
        trista "I think a quick five kilometre run should do."
        "Setting the speed to medium, Trista talks you through the run."
        "Now you are starting to get the hang of it, she has less to point out."
        image trista_gym_eat4 = "/trista/[trista.stage]/gym_eat4.webp"
        scene trista_gym_eat4
        "Instead she seems to be filling the time cramming random snacks into her mouth as you run."
        "It takes a bit of effort but you soon finish your run."
        image trista_gym_standing5 = "/trista/[trista.stage]/gym_standing5.webp"
        scene trista_gym_standing5
        trista "Well done. I think you beat your time from last week."
        pc "Thanks. Wouldn't have gotten this far without your help."
        image trista_gym_drink = "/trista/[trista.stage]/gym_drink.webp"
        scene trista_gym_drink
        "Grabbing a drink for you, Trista hands it to you while drinking from her own large drink."
        trista "Need to stay hydrated."
        if tristastory <= 1:
            "Slurping it down Trista finishes her own larger drink."
            menu:
                "Ask Trista about herself.":
                    "You decide to ask Trista about herself."
                    trista "I don't talk much about myself to others."
                    trista "But okay, if you want to know."
                    "Trista talks a bit about herself."
                    $ tristastory += 1
                    #Unlocks more Trista story in the stats page.
                    $ renpy.notify("New Trista story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Trista anything."
        else:
            "Slurping it down Trista finishes her own larger drink."
        "Right then, let's do some weight work."

        ### On the weight bench###
        image trista_gym_standing6 = "/trista/[trista.stage]/gym_standing6.webp"
        scene trista_gym_standing6
        trista "You should start with a few sets of low weights."
        pc "Sounds good to me."
        image trista_gym_lifting1 = "/trista/[trista.stage]/gym_lifting1.webp"
        scene trista_gym_lifting1
        "As you begin your reps you can see Trista open a box of donuts."
        "You are not sure if her mouth has been empty the entire time you have been here."
        "Continuing to work out, you finish your sets."
        image trista_gym_standing1 = "/trista/[trista.stage]/gym_standing1.webp"
        scene trista_gym_standing1
        trista "Okay, that should do for now."
        trista "We can start upping the weights slowly over time."
        trista "Now I think we should do a warm down."

        ###Yoga mat / just on the floor.###
        image trista_gym_yoga1 = "/trista/[trista.stage]/gym_yoga1.webp"
        scene trista_gym_yoga1
        trista "Okay, lay down there and pick your left leg up."
        "Laying down on your back you lift your leg up in the air."
        image trista_gym_yoga2 = "/trista/[trista.stage]/gym_yoga2.webp"
        scene trista_gym_yoga2
        "Taking hold of it, Trista pushes it towards you with her weight."
        "It feels a bit odd but in a good way, her body almost pressing up against yours in her tight gym clothing."
        "This week you notice her leaning in even closer, your faces almost touching."
        "Was it the extra weight on Trista, or maybe you were getting more flexible."
        image trista_gym_yoga3 = "/trista/[trista.stage]/gym_yoga3.webp"
        scene trista_gym_yoga3
        "Repeating it with the other leg Trista looks towards the door as if expecting something."
        "Had she been conditioned by Marie's feedings to expect a big meal now?"
        "Thinking about it, they had arrived at almost the same moment for the last weeks, months."
        "It was no wonder she would have learned to expect something."
        pc "You ok?"
        image trista_gym_yoga4 = "/trista/[trista.stage]/gym_yoga4.webp"
        scene trista_gym_yoga4
        trista "Sorry yeah, just a bit hungry all of a sudden."
        pc "Want to order some food in, I'm free for a bit if you want to chat."
        trista "Yeah that would be great, I did say I needed to up my calorie intake."
        "Phoning the restaurant Marie was all too happy to arrange another delivery."
        "Soon the doorbell rings."
        image trista_gym_yoga5 = "/trista/[trista.stage]/gym_yoga5.webp"
        scene trista_gym_yoga5
        trista "That must be Marie. I'll be right back."
        image trista_gym_yoga6 = "/trista/[trista.stage]/gym_yoga6.webp"
        scene trista_gym_yoga6
        "Trista soon returns with two big takeaway bags."
        image trista_gym_food1 = "/trista/food1.webp"
        scene trista_gym_food1
        "Setting it out, it was even more than normal."
        "Opening it up she pulls out three double cheeseburgers, three large servings of fries, two large servings of onion rings, a share box of chicken nuggets and one extra large pizza."
        trista "This all looks amazing, Marie does a great job."

        ###Move to somewhere to sit###
        image trista_gym_yoga8 = "/trista/[trista.stage]/gym_yoga8.webp"
        scene trista_gym_yoga8
        "Sitting next to her you make small talk as she dives into her meal."
        "It doesn't take long for her to devour the pizza."
        trista "Mmm, best pizza in town."
        image trista_gym_yoga9 = "/trista/[trista.stage]/gym_yoga9.webp"
        scene trista_gym_yoga9
        "Moving on, she starts working on the burgers, occasionally pausing to add a handful of fries or even nuggets to her binge."
        "You can already see her stomach growing from the large meal as she continues to eat."
        "One burger, then the other and finally the third all disappear."
        "It seems like Trista has no limit to the amount she could eat, her growing stomach bottomless, unlike her new figure."
        image trista_gym_yoga10 = "/trista/[trista.stage]/gym_yoga10.webp"
        scene trista_gym_yoga10
        "Soon all that's left is a selection of empty boxes, the high calorie meal now sitting heavily in Trista's bloated belly."
        trista "Oooh, that was good."
        "Leaning back Trista pats her swollen stomach happily."
        image trista_gym_yoga11 = "/trista/[trista.stage]/gym_yoga11.webp"
        scene trista_gym_yoga11
        trista "But for now, I think our session is over, unless maybe you would like to join me in the sauna again."
        pc "Definitely, I think I could use some heat to help me warm down."
        "Smiling, Trista leads you to the Sauna."
        stop music fadeout 1.0
        image trista_sauna_enter = "/trista/[trista.stage]/sauna_enter.webp"
        scene trista_sauna_enter
        play music "/music/sauna.ogg" if_changed
        "Standing by the door, you hear a click as Trista locks the door."
        trista "Don't want any unwanted visitors do we."
        image trista_sauna_undress = "/trista/[trista.stage]/sauna_undress.webp"
        scene trista_sauna_undress
        "Slowly starting to undress you follow her lead."
        if persistent.nosexscene == True:
            scene black
            "You and Trista had a wonderful time together."
            image trista_sauna_aftersex = "/trista/[trista.stage]/sauna_aftersex.webp"
            scene trista_sauna_aftersex
            trista "That was amazing, you really know how to please a woman."
            pc "And you know how to rock your body."
            trista "We need to do this more often."
            "After a while both of you decide to head out and go home."
            stop music fadeout 1.0
            $ trista_gym_today = 1
            return
        image trista_sauna_beforesex = "/trista/[trista.stage]/sauna_beforesex.webp"
        scene trista_sauna_beforesex
        window hide
        pause
        "Trista turns around to show you her big butt."
        "Her juicy round ass seems to slowly draws you in."
        image trista_sauna_sex1 = "/trista/[trista.stage]/sauna_sex1.webp"
        scene trista_sauna_sex1
        window hide
        pause
        "You kneel down and plant your face in between her soft ass cheeks."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/4/sauna_sex1_video.webm" loop
        show movie with dissolve
        window hide
        pause
        trista "That's it, keep it going."
        trista "Right there-{w} OHHHH!"
        trista "HOLY FUCK!!"
        "Trista collapses for a moment before standing up again, she only wants one thing from you."
        stop movie
        image trista_sauna_sex2 = "/trista/[trista.stage]/sauna_sex2.webp"
        scene trista_sauna_sex2
        trista "Go ahead, take me from behind."
        "You gladly accept her request as you line up your rock hard dick with her wet pussy."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/trista/4/sauna_sex2_video.webm" loop
        show movie with dissolve
        window hide
        pause
        "While rocking you hips back and forth Trista her huge ass seems to absorb most of the impact from your thrusts."
        window hide
        pause
        "After a few minutes you feel the pressure build up, not long after that you climax while pressing you body against her soft behind."
        stop movie
        image trista_sauna_aftersex = "/trista/[trista.stage]/sauna_aftersex.webp"
        scene trista_sauna_aftersex
        trista "That was amazing, you really know how to please a woman."
        pc "And you know how to rock your body."
        trista "We need to do this more often."
        "After a while both of you decide to head out and go home."
        if katrine.stage >= trista.stage:
            $ trista.weight += 1

    else:
        ###Arriving at the gym###
        image trista_gym_dumbel = "/trista/[trista.stage]/gym_dumbel.webp"
        scene trista_gym_dumbel
        "Walking in you spot Trista lifting some weights."
        pc "Hey, Trista."
        image trista_gym_sitting = "/trista/[trista.stage]/gym_sitting.webp"
        scene trista_gym_sitting
        trista "Hey, [playername]. Hope you are ready to sweat."
        pc "I'm good to go."
        trista "Great, let's start with the usual cardio to warm up."

        ####At treadmill####
        image trista_gym_running3 = "/trista/[trista.stage]/gym_running3.webp"
        scene trista_gym_running3
        trista "I think a five kilometre run should do."
        "Setting the speed to medium, Trista talks you through the run."
        "Now you are starting to get the hang of it, she has less to point out."
        image trista_gym_eat4 = "/trista/[trista.stage]/gym_eat4.webp"
        scene trista_gym_eat4
        "Instead she seems to be filling the time cramming random snacks into her mouth as you run."
        "Now you are finding it a bit easier. You can spend more time watching her as you complete your run."
        image trista_gym_standing5 = "/trista/[trista.stage]/gym_standing5.webp"
        scene trista_gym_standing5
        trista "Well done. I think you beat your time from last week."
        pc "Thanks. Wouldn't have gotten this far without your help."
        image trista_gym_drink = "/trista/[trista.stage]/gym_drink.webp"
        scene trista_gym_drink
        "Grabbing a drink for you, Trista hands it to you while drinking from her own large drink."
        trista "Need to stay hydrated."
        if tristastory <= 6 and trista.stage >= 11:
            "Slurping it down Trista finishes her own larger drink."
            menu:
                "Ask Trista about herself.":
                    "You decide to ask Trista about herself."
                    trista "I don't talk much about myself to others."
                    trista "But okay, if you want to know."
                    "Trista talks a bit about herself."
                    $ tristastory += 1
                    #Unlocks more Trista story in the stats page.
                    $ renpy.notify("New Trista story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Trista anything."
        elif tristastory <= 5 and trista.stage >= 9:
            "Slurping it down Trista finishes her own larger drink."
            menu:
                "Ask Trista about herself.":
                    "You decide to ask Trista about herself."
                    trista "I don't talk much about myself to others."
                    trista "But okay, if you want to know."
                    "Trista talks a bit about herself."
                    $ tristastory += 1
                    #Unlocks more Trista story in the stats page.
                    $ renpy.notify("New Trista story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Trista anything."
        elif tristastory <= 4 and trista.stage >= 8:
            "Slurping it down Trista finishes her own larger drink."
            menu:
                "Ask Trista about herself.":
                    "You decide to ask Trista about herself."
                    trista "I don't talk much about myself to others."
                    trista "But okay, if you want to know."
                    "Trista talks a bit about herself."
                    $ tristastory += 1
                    #Unlocks more Trista story in the stats page.
                    $ renpy.notify("New Trista story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Trista anything."
        elif tristastory <= 3 and trista.stage >= 7:
            "Slurping it down Trista finishes her own larger drink."
            menu:
                "Ask Trista about herself.":
                    "You decide to ask Trista about herself."
                    trista "I don't talk much about myself to others."
                    trista "But okay, if you want to know."
                    "Trista talks a bit about herself."
                    $ tristastory += 1
                    #Unlocks more Trista story in the stats page.
                    $ renpy.notify("New Trista story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Trista anything."
        elif tristastory <= 2 and trista.stage >= 5:
            "Slurping it down Trista finishes her own larger drink."
            menu:
                "Ask Trista about herself.":
                    "You decide to ask Trista about herself."
                    trista "I don't talk much about myself to others."
                    trista "But okay, if you want to know."
                    "Trista talks a bit about herself."
                    $ tristastory += 1
                    #Unlocks more Trista story in the stats page.
                    $ renpy.notify("New Trista story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Trista anything."
        else:
            "Slurping it down Trista finishes her own larger drink."
        "Right then, let's do some weight work."

        ### On the weight bench###
        image trista_gym_standing6 = "/trista/[trista.stage]/gym_standing6.webp"
        scene trista_gym_standing6
        trista "Let's start you off with a few basic sets."
        pc "Sounds good to me."
        image trista_gym_lifting1 = "/trista/[trista.stage]/gym_lifting1.webp"
        scene trista_gym_lifting1
        "As you begin your reps, you can see Trista open up a box of donuts."
        "You are not sure if her mouth has been empty the entire time you have been here."
        "Continuing to work out, you take your time giving Trista more time to keep stuffing herself."
        image trista_gym_standing1 = "/trista/[trista.stage]/gym_standing1.webp"
        scene trista_gym_standing1
        trista "Okay, that should do for now."
        trista "Now I think we should do a warm down."

        ###Yoga mat / just on the floor.###
        image trista_gym_yoga1 = "/trista/[trista.stage]/gym_yoga1.webp"
        scene trista_gym_yoga1
        trista "Okay, lay down there and pick your left leg up."
        "Laying down on your back you lift your leg up in the air."
        image trista_gym_yoga2 = "/trista/[trista.stage]/gym_yoga2.webp"
        scene trista_gym_yoga2
        "Taking hold of it, Trista pushes it towards you with her weight."
        image trista_gym_yoga3 = "/trista/[trista.stage]/gym_yoga3.webp"
        scene trista_gym_yoga3
        "The usually toned abs, you used to feel, are replaced by a bit of a softer feeling."
        image trista_gym_yoga4 = "/trista/[trista.stage]/gym_yoga4.webp"
        scene trista_gym_yoga4
        "Finishing off your stretches Trista stands up excitedly."
        trista "I'm feeling peckish again, fancy ordering in?"
        pc "Absolutely."
        image trista_gym_yoga5 = "/trista/[trista.stage]/gym_yoga5.webp"
        scene trista_gym_yoga5
        "Phoning the restaurant Marie was all too happy to arrange another delivery."
        "Soon the doorbell rings."
        image trista_gym_yoga5 = "/trista/[trista.stage]/gym_yoga5.webp"
        scene trista_gym_yoga5
        trista "That must be Marie. I'll be right back."
        image trista_gym_yoga6 = "/trista/[trista.stage]/gym_yoga6.webp"
        scene trista_gym_yoga6
        "Trista soon returns with two big takeaway bags."
        image trista_gym_food2 = "/trista/food2.webp"
        scene trista_gym_food2
        "Setting it out, it was even more than normal."
        "Opening it up, she pulls out three double cheeseburgers, three large servings of fries, two large servings of onion rings, a share box of chicken nuggets and two extra large pizzas."
        trista "This all looks amazing. Marie does a great job."

        ###Move to somewhere to sit###
        image trista_gym_yoga8 = "/trista/[trista.stage]/gym_yoga8.webp"
        scene trista_gym_yoga8
        "Sitting next to her you make small talk as she dives into her meal."
        "It doesn't take long for her to devour the first pizza."
        trista "Mmm, best pizza in town."
        image trista_gym_yoga9 = "/trista/[trista.stage]/gym_yoga9.webp"
        scene trista_gym_yoga9
        "Moving on, she starts working on the burgers, occasionally pausing to add a handful of fries or even nuggets to her binge."
        "You can already see her stomach growing from the large meal as she continues to eat."
        "One burger, then the other and finally the third all disappear."
        "It seems like Trista has no limit to the amount she can eat. Her growing stomach bottomless, unlike her new figure."
        "Grabbing the second extra large cheese pizza, Trista begins methodically eating through it."
        "Despite how much she has already eaten and her swollen stomach, she finishes that too."
        image trista_gym_yoga10 = "/trista/[trista.stage]/gym_yoga10.webp"
        scene trista_gym_yoga10
        "All that's left is a selection of empty boxes - the high-calorie meal now sitting heavily in Trista's bloated belly."
        trista "Oooh, that was good."
        "Leaning back Trista pats her swollen stomach happily."
        "Taking a few minutes she gently rubs her stomach, before looking over at you."
        image trista_gym_yoga11 = "/trista/[trista.stage]/gym_yoga11.webp"
        scene trista_gym_yoga11
        "Smiling Trista slowly stands and heads towards the sauna."
        if katrine.stage >= trista.stage:
            $ trista.weight += 1
        "Not needing another invitation you head towards it too."
        stop music fadeout 1.0
        image trista_sauna_enter = "/trista/[trista.stage]/sauna_enter.webp"
        scene trista_sauna_enter
        play music "/music/sauna.ogg" if_changed
        "Standing by the door, you hear a click as Trista locks the door."
        trista "Don't want any unwanted visitors do we."
        if trista.stage >= 10:
            image trista_sauna_undress1 = "/trista/[trista.stage]/sauna_undress1.webp"
            scene trista_sauna_undress1
            "Slowly starting to undress you follow her lead."
            image trista_sauna_undress2 = "/trista/[trista.stage]/sauna_undress2.webp"
            scene trista_sauna_undress2
            window hide
            pause
        else:
            image trista_sauna_undress = "/trista/[trista.stage]/sauna_undress.webp"
            scene trista_sauna_undress
            "Slowly starting to undress you follow her lead."
        if persistent.nosexscene == True:
            scene black
            "You and Trista had a wonderful time together."
            image trista_sauna_aftersex = "/trista/[trista.stage]/sauna_aftersex.webp"
            scene trista_sauna_aftersex
            trista "That was amazing, you really know how to please a woman."
            pc "And you know how to rock your body."
            trista "We need to do this more often."
            "After a while both of you decide to head out and go home."
            stop music fadeout 1.0
            $ trista_gym_today = 1
            return
        image trista_sauna_beforesex = "/trista/[trista.stage]/sauna_beforesex.webp"
        scene trista_sauna_beforesex
        window hide
        pause
        "Trista turns around to show you her big butt."
        "Her juicy round ass seems to slowly draws you in."
        image trista_sauna_sex1 = "/trista/[trista.stage]/sauna_sex1.webp"
        scene trista_sauna_sex1
        window hide
        pause
        "You kneel down and plant your face in between her soft ass cheeks."
        if trista.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/sauna_sex1_video.webm" loop
            show movie with dissolve
        elif trista.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/sauna_sex1_video.webm" loop
            show movie with dissolve
        elif trista.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/7/sauna_sex1_video.webm" loop
            show movie with dissolve
        elif trista.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/8/sauna_sex1_video.webm" loop
            show movie with dissolve
        elif trista.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/9/sauna_sex1_video.webm" loop
            show movie with dissolve
        elif trista.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/10/sauna_sex1_video.webm" loop
            show movie with dissolve
        elif trista.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/11/sauna_sex1_video.webm" loop
            show movie with dissolve
        elif trista.stage == 12:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/12/sauna_sex1_video.webm" loop
            show movie with dissolve
        elif trista.stage == 13:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/13/sauna_sex1_video.webm" loop
            show movie with dissolve
        window hide
        pause
        trista "That's it, keep it going."
        trista "Right there-{w} OHHHH!"
        trista "HOLY FUCK!!"
        "Trista collapses for a moment before standing up again, she only wants one thing from you."
        stop movie
        image trista_sauna_sex2 = "/trista/[trista.stage]/sauna_sex2.webp"
        scene trista_sauna_sex2
        trista "Go ahead, take me from behind."
        "You gladly accept her request as you line up your rock hard dick with her wet pussy."
        window hide
        pause
        if trista.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/5/sauna_sex2_video.webm" loop
            show movie with dissolve
        elif trista.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/6/sauna_sex2_video.webm" loop
            show movie with dissolve
        elif trista.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/7/sauna_sex2_video.webm" loop
            show movie with dissolve
        elif trista.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/8/sauna_sex2_video.webm" loop
            show movie with dissolve
        elif trista.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/9/sauna_sex2_video.webm" loop
            show movie with dissolve
        elif trista.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/10/sauna_sex2_video.webm" loop
            show movie with dissolve
        elif trista.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/11/sauna_sex2_video.webm" loop
            show movie with dissolve
        elif trista.stage == 12:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/12/sauna_sex2_video.webm" loop
            show movie with dissolve
        elif trista.stage == 13:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/13/sauna_sex2_video.webm" loop
            show movie with dissolve
        window hide
        pause
        "While rocking you hips back and forth Trista her huge ass seems to absorb most of the impact from your thrusts."
        if trista.stage == 10:
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/10/sauna_sex3_video.webm" loop
            show movie with dissolve
            "Her soft thighs and bloated belly jiggling with every push."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/10/sauna_sex4_video.webm" loop
            show movie with dissolve
            "While she was once all lean and muscular, her whole body has now turned into a blubbery mess."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/10/sauna_sex5_video.webm" loop
            show movie with dissolve
            window hide
            pause
        elif trista.stage == 11:
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/11/sauna_sex3_video.webm" loop
            show movie with dissolve
            "Her soft thighs and bloated belly jiggling with every push."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/11/sauna_sex4_video.webm" loop
            show movie with dissolve
            "While she was once all lean and muscular, her whole body has now turned into a blubbery mess."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/11/sauna_sex5_video.webm" loop
            show movie with dissolve
            window hide
            pause
        elif trista.stage == 12:
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/12/sauna_sex3_video.webm" loop
            show movie with dissolve
            "Her soft thighs and bloated belly jiggling with every push."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/12/sauna_sex4_video.webm" loop
            show movie with dissolve
            "While she was once all lean and muscular, her whole body has now turned into a blubbery mess."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/12/sauna_sex5_video.webm" loop
            show movie with dissolve
            window hide
            pause
        elif trista.stage == 13:
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/13/sauna_sex3_video.webm" loop
            show movie with dissolve
            "Her soft thighs and bloated belly jiggling with every push."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/13/sauna_sex4_video.webm" loop
            show movie with dissolve
            "While she was once all lean and muscular, her whole body has now turned into a blubbery mess."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/trista/13/sauna_sex5_video.webm" loop
            show movie with dissolve
            window hide
            pause
        "After a few minutes you feel the pressure build up, not long after that you climax while pressing you body against her soft behind."
        stop movie
        image trista_sauna_aftersex = "/trista/[trista.stage]/sauna_aftersex.webp"
        scene trista_sauna_aftersex
        trista "That was amazing, you really know how to please a woman."
        pc "And you know how to rock your body."
        trista "We need to do this more often."
        "After a while both of you decide to head out and go home."
    stop music fadeout 1.0
    $ trista_gym_today = 1
    return

label trista_introduction:
    image trista_intro1 = "/trista/1/intro1.webp"
    scene trista_intro1
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    "You see a girl kicking a boxing bag."
    pc "She looks fierce."
    image trista_intro2 = "/trista/1/intro2.webp"
    scene trista_intro2
    "Her boxing technique is impeccable."
    "And her body looks slim and fit."
    image trista_intro3 = "/trista/1/intro3.webp"
    scene trista_intro3
    "After staring at the girl for a while, she seemed to notice you."
    "You quickly act normal and walk up to her."
    image trista_intro4 = "/trista/1/intro4.webp"
    scene trista_intro4
    trista "Hey, you must be new, I haven't seen you around here before."
    pc "Oh yeah I'm new here, I was looking for a local place to build some muscle."
    image trista_intro5 = "/trista/1/intro5.webp"
    scene trista_intro5
    trista "You came to the right place, I'm Trista the owner of this place."
    pc "Nice to meet you Trista, I'm [playername]."
    trista "Welcome to my humble gym, feel free to come here as often as you like, I don't charge for a membership."
    trista "And if you need help, just ask me."
    pc "Thank you Trista, will do."
    $ gymunlock = 1
    scene gym
    "You workout for a bit."
    $ strength += 1
    "Strength increased by one point."
    stop music fadeout 1.0
    return

label Trista_Stage_1_Event:
    scene gym
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    "Looks like no one is here today."
    if recollection == False:
        $ strength += 1
    "You work out and gain 1 strength."
    "You are about to leave when you hear a thump in the backroom."
    pc "Hello?"
    image trista_stage1_event_1 = "/trista/events/stage1/1.webp"
    scene trista_stage1_event_1
    trista "Oh, hey [playername]."
    trista "Sorry. I didn't know anyone was in here."
    pc "No worries, just heard a noise and wanted to check if everything was ok."
    image trista_stage1_event_2 = "/trista/events/stage1/2.webp"
    scene trista_stage1_event_2
    trista "Yeah, everything is fine - just getting some supplies out of storage."
    trista "How are you doing anyway, are your workouts going ok?"
    pc "Yeah, this place is great."
    image trista_stage1_event_3 = "/trista/events/stage1/3.webp"
    scene trista_stage1_event_3
    trista "Thanks, it was my dad's originally, and his dad's before him."
    trista "It's probably a bit old fashioned compared to the newer extreme gyms popping up all over the place."
    pc "There is a lot to be said for the simpler and traditional ways of doing things."
    trista "Exactly!"
    image trista_stage1_event_4 = "/trista/events/stage1/4.webp"
    scene trista_stage1_event_4
    trista "So, I’ve been noticing you and Katrine spending a lot of time together."
    pc "Yeah, it's always good to have a gym buddy to help."
    trista "Although it looks like you are on your own today."
    trista "I thought she was making good progress, but lately her focus seems to have been lost."
    pc "I think she just hurt her shoulder, so she is taking it easy."
    image trista_stage1_event_5 = "/trista/events/stage1/5.webp"
    scene trista_stage1_event_5
    trista "I hope it's nothing serious."
    trista "You should tell her the sauna works wonders on muscle damage."
    trista "But anyway, I should let you get back to your workout."
    pc "Actually I've just finished. Do you need a hand with anything?"
    image trista_stage1_event_6 = "/trista/events/stage1/6.webp"
    scene trista_stage1_event_6
    trista "Well, if you don’t mind, I'm just bringing in some boxes and could do with an extra pair of hands."
    pc "Sure thing."
    image trista_stage1_event_7 = "/trista/events/stage1/7.webp"
    scene trista_stage1_event_7
    "Grabbing a few boxes you help Trista restock the refreshments."
    "Setting the last box down you notice a chart, it seems to be keeping tabs on Trista’s own body measurements."
    $ trista_stats_visible = 1
    "Trista has been added to the stats menu."
    image trista_stage1_event_8 = "/trista/events/stage1/8.webp"
    scene trista_stage1_event_8
    trista "Thanks for the help."
    pc "No problem, you planning something big? This is a lot of supplies."
    image trista_stage1_event_9 = "/trista/events/stage1/9.webp"
    scene trista_stage1_event_9
    trista "Well, competition season is almost here, so I'm expecting a few more people to be around soon."
    trista "Or at the very least it’s a good stockpile for me to start working out with."
    pc "Competition season?"
    trista "Yeah, kickboxing. Competitions run throughout the year but now we are coming up to the serious ones."
    trista "All the qualifiers for the main regional competition start now."
    trista "So everyone will be fighting it out for a place to qualify."
    pc "Sounds stressful."
    trista "Not at all, I've been doing them every year since I was little."
    trista "Although this is the first year where I think I have a real shot."
    image trista_stage1_event_10 = "/trista/events/stage1/10.webp"
    scene trista_stage1_event_10
    trista "You have any interest in competing?"
    pc "Not really, just working out to stay healthy at the moment."
    trista "Well, that's a good reason. If you did want to compete just let me know."
    trista "Maybe we can train together some time and I can see your progress first hand."
    pc "Sure. That would be good."
    stop music fadeout 1.0

    $ tristastage1event = 0
    return

label Trista_Stage_2_Event:
    ###“Go to gym option” - After hitting stage 2

    ###In gym with Trista at punching bag####
    image trista_stage2_event_1 = "/trista/events/stage2/1.webp"
    scene trista_stage2_event_1
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    "Hey, it's Trista."
    "She looks even more fierce than usual."
    pc "Hey, Trista. Everything okay?"
    image trista_stage2_event_2 = "/trista/events/stage2/2.webp"
    scene trista_stage2_event_2
    trista "No. The stupid idiots got their gym shut down."
    trista "How am I supposed to qualify for regionals now?"
    image trista_stage2_event_3 = "/trista/events/stage2/3.webp"
    scene trista_stage2_event_3
    "Shouting loudly, Trista gives the bag a strong kick. Her form is still perfect."
    pc "I'm sorry to hear that. Are there no other competitions?"
    image trista_stage2_event_4 = "/trista/events/stage2/4.webp"
    scene trista_stage2_event_4
    trista "Not that I would be able to get into this late."
    trista "I had been signed up for this months ago."
    pc "Surely there must be other competitors that were hoping to go to that event as well?"
    trista "Misery loves company."
    pc "No, I mean; why not host it here?"
    image trista_stage2_event_5 = "/trista/events/stage2/5.webp"
    scene trista_stage2_event_5
    trista "Wait, you are right!"
    trista "[playername], you are a genius!"
    pc "I do have my moments."
    image trista_stage2_event_6 = "/trista/events/stage2/6.webp"
    scene trista_stage2_event_6
    trista "Although I would need to be registered with the official league in order to count as a qualifying event."
    trista "Plus, I would need a sponsor."
    pc "What about Bonnie's sweet shop, or Bunny Bites?"
    image trista_stage2_event_7 = "/trista/events/stage2/7.webp"
    scene trista_stage2_event_7
    trista "A local business would look good."
    trista "Maybe you could help me speak to them about it?"
    pc "I don’t see why not."
    trista "You would be doing me a massive favour."
    pc "Well, you do let me train here for free."
    image trista_stage2_event_8 = "/trista/events/stage2/8.webp"
    scene trista_stage2_event_8
    trista "True. I guess we can call it even."
    trista "Although, I let everyone train here free. Maybe we could sweeten the deal with a little one on one training?"
    pc "I won't say no to that."
    image trista_stage2_event_9 = "/trista/events/stage2/9.webp"
    scene trista_stage2_event_9
    trista "Awesome! I'll add you to the schedule."
    trista "Should we head out to The Sugar Shop and Bunny Bites now?"
    pc "Sure thing, we can go to Bonnie's on the way to Bunny Bites."
    trista "Let me get some other clothes, be right back."

    ###Bonnies sweet shop, Bonnie behind the counter in orange jumper####
    image bonnie_sweetshop2 = "/bonnie/[bonnie.stage]/sweetshop2.webp"
    scene bonnie_sweetshop2
    stop music fadeout 1.0
    bonnie "Hey, [playername]. What can I get you today?"
    pc "Hey, Bonnie. I was actually wondering if you could help my friend Trista here."
    bonnie "Hey Trista, sure I can help."
    image trista_stage2_event_10 = "/trista/events/stage2/10.webp"
    scene trista_stage2_event_10
    trista "Hi. I am looking for a sponsor for an event at the gym and [playername] said you might be interested."
    image bonnie_sweetshop = "/bonnie/[bonnie.stage]/sweetshop.webp"
    scene bonnie_sweetshop
    bonnie "Sure. Although, I don't typically sell the sort of things most gym goers are after."
    image trista_stage2_event_11 = "/trista/events/stage2/11.webp"
    scene trista_stage2_event_11
    trista "That's a good point. You don't happen to do any low-calorie or protein bar things?"
    image bonnie_sweetshop3 = "/bonnie/[bonnie.stage]/sweetshop3.webp"
    scene bonnie_sweetshop3
    bonnie "Sorry, I don’t."
    bonnie "Just a good old fashioned bakery."
    bonnie "Here, why don’t I give you a sample box and then you can decide if it's what you want to serve at the event?"
    trista "Sure thing."
    image trista_stage2_event_12 = "/trista/events/stage2/12.webp"
    scene trista_stage2_event_12
    "After collecting a few chocolates Bonnie hands the box over to Trista."
    trista "I'm not usually one for sweet treats, but let's see."
    image trista_stage2_event_13 = "/trista/events/stage2/13.webp"
    scene trista_stage2_event_13
    "Taking a bite you see Trista’s expression change completely as she quickly eats another."
    trista "Wow, these are really good."
    image trista_stage2_event_14 = "/trista/events/stage2/14.webp"
    scene trista_stage2_event_14
    "Picking up another Trista continues making her way through the box of sweet treats."
    bonnie "I'm glad you like them."
    image trista_stage2_event_15 = "/trista/events/stage2/15.webp"
    scene trista_stage2_event_15
    "Finishing off the box, Trista seems to regain her senses."
    trista "I do, but I think you might have been right about the sponsorship."
    image bonnie_sweetshop3 = "/bonnie/[bonnie.stage]/sweetshop3.webp"
    scene bonnie_sweetshop3
    bonnie "No worries. If you ever do want any for yourself do come back though."
    image trista_stage2_event_16 = "/trista/events/stage2/16.webp"
    scene trista_stage2_event_16
    trista "Thanks. I will."
    trista "I guess we should move on."
    image bonnie_sweetshop = "/bonnie/[bonnie.stage]/sweetshop.webp"
    scene bonnie_sweetshop
    pc "Thanks, Bonnie."
    bonnie "No problem. See you guys later."

    #### Outside ####
    image trista_stage2_event_17 = "/trista/events/stage2/17.webp"
    scene trista_stage2_event_17
    trista "Well, they were good, but not the right sponsor for a sports event."
    pc "Shall we try Bunny Bites then?"
    trista "Definitely."

    ###Bunny bites – in booth###
    image trista_stage2_event_18 = "/trista/events/stage2/18.webp"
    scene trista_stage2_event_18
    play music "/music/bunny_bites.ogg" if_changed
    trista "I used to come in here all the time."
    pc "They do good food."
    trista "And the sexy staff and their outfits aren’t bad either."
    image trista_stage2_event_19 = "/trista/events/stage2/19.webp"
    scene trista_stage2_event_19
    trista "Just a shame I’ve never seen you in one of those when you’re working here."
    pc "Not sure they have one in my size."
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Hi guys. How can I help you today?"
    trista "Hey, Marie, you're manager, right? Can I ask you something?"
    marie "Sure am. I'd ask if there was something wrong with the food, but you haven't eaten yet."
    image trista_stage2_event_20 = "/trista/events/stage2/20.webp"
    scene trista_stage2_event_20
    trista "No, it's nothing like that."
    trista "I'm hosting an event at my gym and I am looking for a local sponsor, if you are interested?"
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "I am, but I don’t know if we can afford to sponsor anything."
    image trista_stage2_event_21 = "/trista/events/stage2/21.webp"
    scene trista_stage2_event_21
    trista "Oh no, I'm not looking for money."
    trista "It's just some rules that say I have to have one. Supposed to make us more official-looking."
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Oh, so do you just need some advertising things?"
    trista "And maybe some food on the day if that’s not too much to ask."
    marie "It’s the least we could do for the extra publicity."
    trista "Amazing. Thank you. So, what sorts of food do you want to serve?"
    marie "I’ll leave that up to you."
    marie "In fact, why don’t I go grab some samples and you can tell me what you think is best."
    trista "Well, actually, I...."
    marie "I’ll be right back with your food."
    "Before Trista can object, Marie has already disappeared back into the kitchen."
    image trista_stage2_event_22 = "/trista/events/stage2/22.webp"
    scene trista_stage2_event_22
    trista "She knows I have been here loads of times before."
    trista "I don’t know why I would need a tester."
    pc "I mean, if it's free food it's hard to complain."
    image trista_stage2_event_23 = "/trista/events/stage2/23.webp"
    scene trista_stage2_event_23
    trista "True, and I did work up an appetite this morning I suppose."
    "A few minutes later Marie returns, filling the table with what looked like one of anything they could make."
    image trista_stage2_event_24 = "/trista/events/stage2/24.webp"
    scene trista_stage2_event_24
    trista "Wow, this is a lot."
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Just come to see me before the event and let me know what you want us to bring."
    "Winking at you Marie leaves the two of you alone with the mountain of food."
    image trista_stage2_event_25 = "/trista/events/stage2/25.webp"
    scene trista_stage2_event_25
    "Picking up the first chicken nugget Trista places it in her mouth."
    trista "Mmm, this place always did have the best nuggets."
    image trista_stage2_event_26 = "/trista/events/stage2/26.webp"
    scene trista_stage2_event_26
    "Despite her comments about the amount of food, Trista wasted no time diving in."
    "Both hands in motion she began picking at the foods."
    image trista_stage2_event_27 = "/trista/events/stage2/27.webp"
    scene trista_stage2_event_27
    "Fries, onion rings, burgers and slices of pizza disappearing into her hungry mouth."
    image trista_stage2_event_28 = "/trista/events/stage2/28.webp"
    scene trista_stage2_event_28
    "Soon just a single burger remained as Trista leaned back away from the table."
    trista "Uuggh, I don’t think I can eat another bite."
    pc "It's just one more burger, you can do it."
    image trista_stage2_event_29 = "/trista/events/stage2/29.webp"
    scene trista_stage2_event_29
    "Leaning forwards Trista picks up the burger looking at it reluctantly."
    image trista_stage2_event_30 = "/trista/events/stage2/30.webp"
    scene trista_stage2_event_30
    "Taking small bites, she slowly works her way through it until she has done it. The table is empty."
    image trista_stage2_event_31 = "/trista/events/stage2/31.webp"
    scene trista_stage2_event_31
    trista "Ughhhh."
    trista "I don’t think I can move."
    image trista_stage2_event_32 = "/trista/events/stage2/32.webp"
    scene trista_stage2_event_32
    "Patting her distended stomach, her appetite seems satiated for now."
    "Sitting there for a few minutes to recover, Trista seems in a bit of a daze after stuffing herself to her limit."
    "But eventually she comes around and you agree to call it a day."

    ###Outside###
    image trista_stage2_event_33 = "/trista/events/stage2/33.webp"
    scene trista_stage2_event_33
    "Helping Trista to her feet you head home."
    "You feel happy to have helped solve Trista’s competition issues and watch her binge."
    stop music fadeout 1.0
    if recollection == False:
        $ trista.weight += 1.5
    $ tristastage2event = 0
    return

label Trista_Stage_3_Event:
    #“Go to gym option”
    image trista_stage3_event_1 = "/trista/events/stage3/1.webp"
    scene trista_stage3_event_1
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    trista "Hey, [playername]. Just in time."
    pc "Hey. Just in time for what?"
    image trista_stage3_event_2 = "/trista/events/stage3/2.webp"
    scene trista_stage3_event_2
    trista "I was just thinking I need someone to help me train."
    pc "Uhh, sure. What do you need me to do?"
    image trista_stage3_event_3 = "/trista/events/stage3/3.webp"
    scene trista_stage3_event_3
    trista "Can you help me with the bag?"

    ###Trista at punch bag###
    image trista_stage3_event_4 = "/trista/events/stage3/4.webp"
    scene trista_stage3_event_4
    trista "I just need you to hold it still so when I hit it, it doesn’t swing back towards me."
    pc "Sure thing."
    image trista_stage3_event_5 = "/trista/events/stage3/5.webp"
    scene trista_stage3_event_5
    "Grabbing the bag you do your best to hold it still as Trista goes through her routine."
    image trista_stage3_event_6 = "/trista/events/stage3/6.webp"
    scene trista_stage3_event_6
    "Swinging her leg round you feel it hitting the bag powerfully."
    image trista_stage3_event_7 = "/trista/events/stage3/7.webp"
    scene trista_stage3_event_7
    "For the next twenty minutes she spins and kicks towards you with perfect rhythm and a fierce power."
    image trista_stage3_event_8 = "/trista/events/stage3/8.webp"
    scene trista_stage3_event_8
    trista "I think that will do for now. I could do with a break for some food."
    image trista_stage3_event_9 = "/trista/events/stage3/9.webp"
    scene trista_stage3_event_9
    "Going behind the gym counter, she begins piling up donut boxes and drinks."
    image trista_stage3_event_10 = "/trista/events/stage3/10.webp"
    scene trista_stage3_event_10
    "Opening the first box she begins to eat."
    trista "Thank you again for your idea of hosting the competition here."
    pc "No problem. How is all that going?"
    image trista_stage3_event_11 = "/trista/events/stage3/11.webp"
    scene trista_stage3_event_11
    trista "Well, with so many of the other competitors still needing to find one, they basically had to accept my proposal."
    pc "That’s great."
    trista "Yeah. Now I just have to get myself ready."
    image trista_stage3_event_12 = "/trista/events/stage3/12.webp"
    scene trista_stage3_event_12
    "Grabbing another donut, Trista shovels them into her mouth."
    image trista_stage3_event_13 = "/trista/events/stage3/13.webp"
    scene trista_stage3_event_13
    "Looking over her you can definitely see a little extra weight on her body."
    image trista_stage3_event_14 = "/trista/events/stage3/14.webp"
    scene trista_stage3_event_14
    "But looking up you accidentally meet her eyes, causing her to smile."
    trista "Like what you see?"
    pc "Sorry. Just wondering where you put all those snacks."
    image trista_stage3_event_15 = "/trista/events/stage3/15.webp"
    scene trista_stage3_event_15
    trista "Haha, I almost believe that."
    image trista_stage3_event_16 = "/trista/events/stage3/16.webp"
    scene trista_stage3_event_16
    "Tipping the crumbs into her mouth she reaches for another."
    image trista_stage3_event_17 = "/trista/events/stage3/17.webp"
    scene trista_stage3_event_17
    trista "I need to maintain my calorie intake otherwise I risk losing muscle mass."
    trista "One of the bonuses of not doing bodybuilding. I do not envy those guys."
    image trista_stage3_event_18 = "/trista/events/stage3/18.webp"
    scene trista_stage3_event_18
    "You watch on as one by one, Trista works through her mountain of donuts."
    image trista_stage3_event_20 = "/trista/events/stage3/20.webp"
    scene trista_stage3_event_20
    "Soon they are all gone, the boxes empty and Trista’s toned belly full."
    image trista_stage3_event_21 = "/trista/events/stage3/21.webp"
    scene trista_stage3_event_21
    trista "Right then. You ready for round two?"
    pc "Yeah, sure."

    ###Back at punch bag###
    image trista_stage3_event_22 = "/trista/events/stage3/22.webp"
    scene trista_stage3_event_22
    "Stepping back in the ring you help Trista with her workout again."
    image trista_stage3_event_23 = "/trista/events/stage3/23.webp"
    scene trista_stage3_event_23
    "Despite a slightly bloated belly, it seems she has lost none of her power or agility."
    image trista_stage3_event_24 = "/trista/events/stage3/24.webp"
    scene trista_stage3_event_24
    "The last kick shaking you as you try to help absorb her kick."
    image trista_stage3_event_25 = "/trista/events/stage3/25.webp"
    scene trista_stage3_event_25
    trista "Whooo, that felt good, really good."
    pc "No problem. Glad I could help."
    image trista_stage3_event_26 = "/trista/events/stage3/26.webp"
    scene trista_stage3_event_26
    trista "Well, maybe you could help me out with something else."
    trista "Working out always gets me worked up, if you know what I mean."
    image trista_stage3_event_27 = "/trista/events/stage3/27.webp"
    scene trista_stage3_event_27
    trista "Or maybe it's just the company."
    pc "I…"
    image trista_stage3_event_28 = "/trista/events/stage3/28.webp"
    scene trista_stage3_event_28
    "Walking towards the sauna, Trista motions for you to follow."
    trista "Why don't we find a way to relax together?"
    stop music fadeout 1.0
    if persistent.nosexscene == True:
        scene black
        "You and Trista had a wonderful time together."
        image trista_stage3_event_37 = "/trista/events/stage3/37.webp"
        scene trista_stage3_event_37
        trista "That was amazing. You really know how to please a woman."
        pc "And you know how to rock your body."
        trista "We need to do this more often."
        "After a while both of you decide to head out and go home."
        if recollection == False:
            $ trista.weight += 1
            #Unlocks Trista Undress in the stats page.
            $ renpy.notify("Trista Undress option unlocked in stats screen.")
            window hide
            pause
        $ tristastage3event = 0
        return

    #[Sex scene in Sauna]
    image trista_stage3_event_29 = "/trista/events/stage3/29.webp"
    scene trista_stage3_event_29
    play music "/music/sauna.ogg" if_changed
    "Standing by the door, you hear a click as Trista locks the door."
    trista "Don't want any unwanted visitors, do we?"
    image trista_stage3_event_30 = "/trista/events/stage3/30.webp"
    scene trista_stage3_event_30
    "Slowly starting to undress you follow her lead."
    image trista_stage3_event_31 = "/trista/events/stage3/31.webp"
    scene trista_stage3_event_31
    "Trista turns around to show you her big butt."
    "Her juicy round ass seems to slowly draws you in."
    image trista_stage3_event_32 = "/trista/events/stage3/32.webp"
    scene trista_stage3_event_32
    "You kneel down and plant your face in between her soft asscheeks."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/trista/events/stage3/33.webm" loop
    show movie with dissolve
    window hide
    pause
    trista "That's it. Keep it going."
    trista "Right there-{w} OHHHH!"
    trista "HOLY FUCK!!"
    "Trista collapses for a moment before standing up again. She only wants one thing from you."
    stop movie
    image trista_stage3_event_34 = "/trista/events/stage3/34.webp"
    scene trista_stage3_event_34
    trista "Go ahead. Take me from behind."
    "You gladly accept her request as you line up your rock hard dick with her wet pussy."
    window hide
    pause
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/trista/events/stage3/35.webm" loop
    show movie with dissolve
    window hide
    pause
    "While rocking your hips back and forth, Trista’s huge ass seems to absorb most of the impact from your thrusts."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/trista/events/stage3/36.webm" loop
    show movie with dissolve
    window hide
    pause
    "After a few minutes you feel the pressure build up. Not long after that you climax while pressing your body against her soft behind."
    stop movie
    image trista_stage3_event_37 = "/trista/events/stage3/37.webp"
    scene trista_stage3_event_37
    trista "That was amazing. You really know how to please a woman."
    pc "And you know how to rock your body."
    trista "We need to do this more often."
    "After a while both of you decide to head out and go home."
    $ tristastage3event = 0
    if recollection == False:
        $ trista.weight += 1
        #Unlocks Trista Undress in the stats page.
        $ renpy.notify("Trista Undress option unlocked in stats screen.")
        window hide
        pause
    stop music fadeout 1.0
    return

label TristaStage3Phone:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Trista', dialogue=dialogue_one)
    $ msg ("I missed you today for your session.", who=1)
    pause
    $ msg ("Sorry, something came up.")
    pause
    $ msg ("Well, hopefully this can motivate you to make sure you never miss another session.", who=1)
    pause
    if trista.stage <= 4:
        $ msg (None, who=1, pic="stage3_trista")
    elif trista.stage <= 6:
        $ msg (None, who=1, pic="stage5_trista")
    elif trista.stage <= 8:
        $ msg (None, who=1, pic="stage7_trista")
    elif trista.stage <= 10:
        $ msg (None, who=1, pic="stage9_trista")
    else:
        $ msg (None, who=1, pic="stage11_trista")
    pause
    $ msg ("You know how to motivate someone.")
    pause
    $ msg ("Good, I'll see you next week then.", who=1)
    pause
    $ hide_messenger()

    $ tristastage3phone = 0
    return


label Trista_Stage_4_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Katrine', dialogue=dialogue_one)
    $ msg ("Hey. Fancy going to Bunny Bites?", who=1)
    pause
    $ msg ("We can treat it like a date?", who=1)
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

    #### Katrine in booth at bunny bites in gym attire with food on the table###
    image trista_stage4_event_1 = "/trista/events/stage4/1.webp"
    scene trista_stage4_event_1
    play music "/music/bunny_bites.ogg" if_changed
    "Walking into the diner you spot Katrine already in one of the booths."
    pc "Hey, Katrine."
    image trista_stage4_event_2 = "/trista/events/stage4/2.webp"
    scene trista_stage4_event_2
    katrine "Hi. How are you?"
    pc "I'm good, thanks. You?"
    katrine "Yeah, me too. A little swamped with work."
    image trista_stage4_event_3 = "/trista/events/stage4/3.webp"
    scene trista_stage4_event_3
    katrine "I hope you don’t mind, I ordered before you got here."
    katrine "I’ve actually been here since lunchtime working and couldn’t help myself."
    image trista_stage4_event_4 = "/trista/events/stage4/4.webp"
    scene trista_stage4_event_4
    "Picking up the burger she takes another bite out of it."
    pc "Working on anything interesting?"
    image trista_stage4_event_5 = "/trista/events/stage4/5.webp"
    scene trista_stage4_event_5
    katrine "Actually, yeah. We are doing a piece on local businesses."
    katrine "Looking at how small businesses like this can do well against larger companies by having a sense of community."
    image trista_stage4_event_6 = "/trista/events/stage4/6.webp"
    scene trista_stage4_event_6
    "Grabbing a few fries she throws them into her mouth before continuing."
    image trista_stage4_event_7 = "/trista/events/stage4/7.webp"
    scene trista_stage4_event_7
    katrine "It's like the sweets shop in town does well because people know how good the sweets are and they feel less mass-produced than big businesses."
    pc "Yeah. There is a lot to be said for the homemade feeling."
    katrine "Exactly. There is this..."



    ###Trista arriving, maybe in gym clothes or martial arts outfit###
    image trista_stage4_event_8 = "/trista/events/stage4/8.webp"
    scene trista_stage4_event_8
    trista "[playername], I'm glad I ran into you!"
    katrine "Oh. Hi, Trista."

    ###Trista joins the table###
    image trista_stage4_event_9 = "/trista/events/stage4/9.webp"
    scene trista_stage4_event_9
    trista "I won! I'm through to the regionals!"
    pc "Congratulations."
    trista "I wouldn’t have even had the idea without you suggesting it, so thank you!"
    pc "It's no problem. Just a thought I had."
    image trista_stage4_event_10 = "/trista/events/stage4/10.webp"
    scene trista_stage4_event_10
    katrine "Well done. You deserve it."
    trista "Thanks. Maybe one day you could win something too."
    katrine "Well, I don't really work out to..."
    image trista_stage4_event_11 = "/trista/events/stage4/11.webp"
    scene trista_stage4_event_11
    trista "Have you guys eaten?"
    katrine "Well, we were in the middle of someth-"
    trista "Ah, no worries. I'll go and order now."

    ###Trista leaves the table###
    image trista_stage4_event_12 = "/trista/events/stage4/12.webp"
    scene trista_stage4_event_12
    katrine "Can you believe her? Just coming like that."
    pc "Maybe it’s the adrenaline."
    pc "I'm sure she doesn’t mean to."
    image trista_stage4_event_13 = "/trista/events/stage4/13.webp"
    scene trista_stage4_event_13
    katrine "You definitely give people too much benefit of the doubt."
    pc "Anyway, what were you saying?"
    katrine "Honestly I can't remember."
    pc "But you are enjoying your job more now though?"
    image trista_stage4_event_14 = "/trista/events/stage4/14.webp"
    scene trista_stage4_event_14
    katrine "Yeah, exactly. I guess it's more fun to write about people's experiences instead of a summary of some spreadsheet report."
    pc "So, do you think that you will look for more of this type of stuff?"
    katrine "Definitely, I think..."

    ###Trista returns to the table###
    image trista_stage4_event_15 = "/trista/events/stage4/15.webp"
    scene trista_stage4_event_15
    trista "Sorry guys, but I was starving."
    trista "Plus, I need to start preparing for regionals, which I qualified for today."
    image trista_stage4_event_16 = "/trista/events/stage4/16.webp"
    scene trista_stage4_event_16
    katrine "You know what? I think I'm going to go and do some work at home."
    katrine "It was nice seeing you, [playername]."
    pc "You too, Katrine."
    trista "See you around, Katrine."
    image trista_stage4_event_17 = "/trista/events/stage4/17.webp"
    scene trista_stage4_event_17
    "Without replying, Katrine leaves you with Trista in the restaurant."
    image trista_stage4_event_18 = "/trista/events/stage4/18.webp"
    scene trista_stage4_event_18
    trista "She has been working too hard lately."
    trista "And not working out enough."
    trista "Speaking of, I really need to start getting serious, today was much harder than I thought it might be."
    pc "Stiff competition."
    image trista_stage4_event_19 = "/trista/events/stage4/19.webp"
    scene trista_stage4_event_19
    trista "Exactly, and this was just the qualifiers."
    trista "I didn't expect there to be so many competitors. I guess the sport is getting more popular."
    trista "If I want to stand a chance I need to up my game, which starts now."
    image trista_stage4_event_20 = "/trista/events/stage4/20.webp"
    scene trista_stage4_event_20
    "A few moments later, Trista's food arrives, covering the table in a ridiculous amount of delicious food."
    pc "That’s a lot of food."
    image trista_stage4_event_21 = "/trista/events/stage4/21.webp"
    scene trista_stage4_event_21
    trista "I know, but if i'm going to be training all day every day I will need a lot of calories."
    trista "Some professionals eat eight meals a day to keep their bodies in shape."
    trista "And I still have to get to their level, so I will probably need even more."
    image trista_stage4_event_22 = "/trista/events/stage4/22.webp"
    scene trista_stage4_event_22
    "Grabbing the first burger Trista digs into it hungrily, eating it all in only a few bites."
    trista "So I hope you don’t mind if I start eating more in our training sessions."
    image trista_stage4_event_23 = "/trista/events/stage4/23.webp"
    scene trista_stage4_event_23
    "Grabbing the next burger, she repeats the process as she crams as many calories in as she can."
    pc "No. In fact, I'm happy to help out however I can."
    trista "Perfect. I may need that."
    image trista_stage4_event_24 = "/trista/events/stage4/24.webp"
    scene trista_stage4_event_24
    "Watching her eat you are amazed at the speed at which Trista puts the food away."
    image trista_stage4_event_25 = "/trista/events/stage4/25.webp"
    scene trista_stage4_event_25
    "Even after consuming enough to feed a family she still shows no sign of slowing."
    image trista_stage4_event_26 = "/trista/events/stage4/26.webp"
    scene trista_stage4_event_26
    "What Daisy said about it taking twenty minutes for your brain to know you are full must be right."
    image trista_stage4_event_27 = "/trista/events/stage4/27.webp"
    scene trista_stage4_event_27
    "Soon the table is empty as Trista leans back in the booth, satisfied and stuffed."
    trista "That should fuel me for today."
    trista "Fancy coming to the gym?"
    pc "No, I think I'm good for today. But thanks for the offer."
    image trista_stage4_event_28 = "/trista/events/stage4/28.webp"
    scene trista_stage4_event_28
    trista "I'm going to head home then. Have a nice evening, [playername]."
    image trista_stage4_event_29 = "/trista/events/stage4/29.webp"
    scene trista_stage4_event_29
    "Standing with some difficulty Trista cranes her back before heading out."

    ####Outside###
    "Well, that wasn't exactly how you thought it would go after Katrine messaged you."
    "But if Trista is going to start eating like that regularly, you are glad it did."
    "You just hope Katrine isn’t too annoyed."
    stop music fadeout 1.0
    if recollection == False:
        $ trista.weight += 1
        $ katrine.weight += 0.5
        $ daytime += 1
        $ phonecall = 1
    $ tristastage4event = 0
    return


label Trista_Stage_6_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Trista', dialogue=dialogue_one)
    $ msg ("Time for our weekly session.", who=1)
    pause
    menu:
        "Workout with Trista.":
            $ hide_messenger()
        "Do something else.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    ###In gym###
    scene gym
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    "Walking into the gym for your normal workout session with Trista you can tell something is immediately different."
    "A smell of hot cheese, pepperoni, and fresh baked dough reaches your nose."
    image trista_stage6_event_1 = "/trista/events/stage6/1.webp"
    scene trista_stage6_event_1
    "There on the counter you can see a giant stack of pizza."
    ###Trista appears###
    image trista_stage6_event_2 = "/trista/events/stage6/2.webp"
    scene trista_stage6_event_2
    trista "Hey, [playername]."
    pc "Hi, Trista. Hosting a party?"
    image trista_stage6_event_3 = "/trista/events/stage6/3.webp"
    scene trista_stage6_event_3
    trista "Sure am! Although you're the only one invited."
    pc "I'm honored.{w} What's the plan?"
    trista "I'm doing carbo-loading."
    pc "Carbo-loading?"
    image trista_stage6_event_4 = "/trista/events/stage6/4.webp"
    scene trista_stage6_event_4
    trista "Yeah. It's something endurance athletes do."
    trista "It's kind of my secret weapon for the regional championships."
    trista "Most of the other competitors don’t think about the fact that there are multiple rounds and don’t train for stamina."
    pc "So you are trying to outlast your opponents?"
    image trista_stage6_event_5 = "/trista/events/stage6/5.webp"
    scene trista_stage6_event_5
    trista "Sort of. I can still beat them one on one like normal."
    trista "It's more about the end of the competition."
    trista "When everyone else is tired after their multiple fights I will be fighting fit and full of energy."
    pc "Smart. So, what do you need from me?"
    image trista_stage6_event_6 = "/trista/events/stage6/6.webp"
    scene trista_stage6_event_6
    trista "I just need you to keep me eating, even if I say I’m full. I want it all! {w}Think you can handle it?"
    pc "Definitely."
    ###Move to somewhere she can sit, maybe on side of boxing ring, not sure?####
    image trista_stage6_event_7 = "/trista/events/stage6/7.webp"
    scene trista_stage6_event_7
    "Opening the first pizza box you hand Trista her first slice."
    image trista_stage6_event_8 = "/trista/events/stage6/8.webp"
    scene trista_stage6_event_8
    trista "Mmm, this pizza is amazing."
    image trista_stage6_event_9 = "/trista/events/stage6/9.webp"
    scene trista_stage6_event_9
    "In just a few bites the first slice is gone and Trista holds out her waiting hand."
    pc "Can I have a piece?"
    trista "Nope! {w}This all has my name on it!"
    image trista_stage6_event_10 = "/trista/events/stage6/10.webp"
    scene trista_stage6_event_10
    pc "Alright, you passed my test."
    "Another slice is passed over, then another and another."
    "Trista is making short work of the large pizzas."
    image trista_stage6_event_11 = "/trista/events/stage6/11.webp"
    scene trista_stage6_event_11
    "But as the second box joins the empty pile she pauses for a moment."
    image trista_stage6_event_12 = "/trista/events/stage6/12.webp"
    scene trista_stage6_event_12
    "Not wanting her to slow down you hold out a slice of the third."
    trista "I just need a moment."
    image trista_stage6_event_13 = "/trista/events/stage6/13.webp"
    scene trista_stage6_event_13
    "You can see why; her flat stomach now starting to bulge outwards from her binge."
    image trista_stage6_event_14 = "/trista/events/stage6/14.webp"
    scene trista_stage6_event_14
    pc "Just doing my job, ma'am."
    pc "You said for me to keep you eating, so keep going."
    trista "You're right..."
    image trista_stage6_event_15 = "/trista/events/stage6/15.webp"
    scene trista_stage6_event_15
    "Taking large bites out of each slice Trista forces herself to keep eating."
    image trista_stage6_event_16 = "/trista/events/stage6/16.webp"
    scene trista_stage6_event_16
    "Opening the fourth pizza box it's clear she is starting to struggle, her enlarged gut struggling to find any more room."
    image trista_stage6_event_17 = "/trista/events/stage6/17.webp"
    scene trista_stage6_event_17
    window hide
    pause
    image trista_stage6_event_18 = "/trista/events/stage6/18.webp"
    scene trista_stage6_event_18
    "Slowly chewing her way through the pizza Trista lets out a heavy exhausted sounding sigh."
    trista "I think that’s enough for me."
    pc "Come on, only half a pizza left of this one."
    image trista_stage6_event_19 = "/trista/events/stage6/19.webp"
    scene trista_stage6_event_19
    "Giving in Trista lets you hand her another slice despite her better judgement."
    image trista_stage6_event_20 = "/trista/events/stage6/20.webp"
    scene trista_stage6_event_20
    "But as the empty pizza box joins the pile you open the next one."
    trista "I thought that was the last one."
    pc "Come on, just one more slice."
    trista "Ughhh, I don’t know."
    image trista_stage6_event_21 = "/trista/events/stage6/21.webp"
    scene trista_stage6_event_21
    "Not taking no for an answer you almost force the slice into her mouth before she takes it off you and begrudgingly starts eating."
    image trista_stage6_event_22 = "/trista/events/stage6/22.webp"
    scene trista_stage6_event_22
    trista "Urgh, I'm so full."
    image trista_stage6_event_23 = "/trista/events/stage6/23.webp"
    scene trista_stage6_event_23
    "Full might have been an understatement going off how much her belly had swelled."
    image trista_stage6_event_24 = "/trista/events/stage6/24.webp"
    scene trista_stage6_event_24
    "You can see her tight gym clothes doing their best to hold it in."
    pc "You are on the final stretch."
    image trista_stage6_event_25 = "/trista/events/stage6/25.webp"
    scene trista_stage6_event_25
    "Taking another slice out, you hand it to her. Are you being too ruthless?"
    trista "I don’t know if I can."
    pc "Just one more slice."
    image trista_stage6_event_26 = "/trista/events/stage6/26.webp"
    scene trista_stage6_event_26
    trista "You have already said that."
    pc "Push yourself. You can eat more."
    image trista_stage6_event_27 = "/trista/events/stage6/27.webp"
    scene trista_stage6_event_27
    "Again Trista gives into your encouragement and begins forcing the slice into her mouth."
    image trista_stage6_event_28 = "/trista/events/stage6/28.webp"
    scene trista_stage6_event_28
    "But as she finishes this slice Trista can't help but let out a moan as she cradles her bloated stomach."
    trista "Ok, that’s definitely my limit."
    "Closing the pizza box you marvel at how much she had managed to force into her stomach."
    image trista_stage6_event_29 = "/trista/events/stage6/29.webp"
    scene trista_stage6_event_29
    pc "You're a champ."
    trista "Ughhh, you are pretty ruthless, but effective."
    pc "Too much?"
    trista "No, it was perfect."
    image trista_stage6_event_30 = "/trista/events/stage6/30.webp"
    scene trista_stage6_event_30
    trista "I think I need to have a rest so that probably does it for today."
    pc "Want a hand getting home?"
    trista "Yeah, that would be great."
    stop music fadeout 1.0

    ###Trista’s home###
    image trista_stage6_event_31 = "/trista/events/stage6/31.webp"
    scene trista_stage6_event_31
    "Walking into Trista’s house you help the stuffed woman to her own bed."
    trista "Thanks for your help with everything."
    image trista_stage6_event_32 = "/trista/events/stage6/32.webp"
    scene trista_stage6_event_32
    pc "You did great today."
    trista "All thanks to you."
    pc "Hey, you supplied the pizza."
    pc "All I did was help with the motivation."
    trista "And that's the most important part."
    pc "Alright, I'll get out of here to let you digest..."
    image trista_stage6_event_33 = "/trista/events/stage6/33.webp"
    scene trista_stage6_event_33
    trista "Wait!"
    trista "I mean, I'm not kicking you out."
    image trista_stage6_event_34 = "/trista/events/stage6/34.webp"
    scene trista_stage6_event_34
    trista "In fact, maybe I could convince you to stay?"
    pc "When you put it that way..."
    trista "Perhaps we could burn a few of these calories after all."
    "You are caught in a daze from Trista's half naked state and tempting suggestion."
    #[Sex scene in Trista’s house with her bloated.] – Let me know if this is too much work, doesn’t come up in this set of events but could do in her specific events maybe?
    image trista_stage6_event_35 = "/trista/events/stage6/35.webp"
    scene trista_stage6_event_35
    window hide
    pause
    "You watch as she quickly strips out of her tight leggings, leaving her thick thighs and plump ass slightly obscured from view due to her engorged stomach."
    "You regain your senses enough to respond to her invitation."
    pc "I love that idea."
    pc "But... {w}do you think you might be too full?"
    trista "I don't know..."
    image trista_stage6_event_36 = "/trista/events/stage6/36.webp"
    scene trista_stage6_event_36
    trista "Do I look too full to you?"
    "She quickly shifts positions, pushing her prominent food-laden gut out, with desire hanging off every word."
    pc "Damn, woman!"
    window hide
    pause
    pc "Let me take a moment to appreciate you!"
    image trista_stage6_event_37 = "/trista/events/stage6/37.webp"
    scene trista_stage6_event_37
    trista "You might be able to appreciate me better up close."
    pc "I'm going to trust you on this one."
    "Trista quickly closes the gap between you. She firmly plants her soft lips upon yours, as you readily embrace each other."
    image trista_stage6_event_38 = "/trista/events/stage6/38.webp"
    scene trista_stage6_event_38
    window hide
    pause
    trista "Mmm."
    trista "Now, let's get rid of this shirt."
    image trista_stage6_event_39 = "/trista/events/stage6/39.webp"
    scene trista_stage6_event_39
    "Doing as you were instructed, you now stand shirtless. Trista's hand gently admires the effect your joint training sessions have had on your body."
    window hide
    pause
    pc "I liked that shirt."
    trista "But I don't like being the only naked one in the room."
    pc "I'm halfway there."
    if persistent.nosexscene == True:
        scene black
        "You and Trista had a wonderful time together."
        image trista_stage6_event_47 = "/trista/events/stage6/47.webp"
        scene trista_stage6_event_47 with fade
        trista "Thanks for today!"
        pc "I should be thanking you."
        trista "You had fun?"
        pc "So much."
        trista "Does that mean we can do it again?"
        pc "Absolutely!"
        if recollection == False:
            $ trista.weight += 1
            $ phonecall = 1
            $ daytime += 1
        $ tristastage6event = 0
        return
    image trista_stage6_event_40 = "/trista/events/stage6/40.webp"
    scene trista_stage6_event_40
    window hide
    pause
    trista "I can help."
    "Trista slowly descends downward. Teasingly she frees you from your jeans, her breath lingering upon your rigid member."
    image trista_stage6_event_41 = "/trista/events/stage6/41.webp"
    scene trista_stage6_event_41 with dissolve
    trista "Now, this is the sight a girl likes to see!"
    pc "A hard cock?"
    trista "It's flattering knowing it got this way because of me."
    image trista_stage6_event_42 = "/trista/events/stage6/42.webp"
    scene trista_stage6_event_42
    "Seemingly satisfied with your lack of clothes and level of 'engagement', she stands back up and moves over toward the bed."
    window hide
    pause
    trista "Now, do you think we could work around this gut?"
    pc "We could try..."
    image trista_stage6_event_43 = "/trista/events/stage6/43.webp"
    scene trista_stage6_event_43
    pc "...this!"
    "You quickly lift the bloated blonde up allowing her to brace her added heft on the bed. Desire overtaking you both you hastily enter her."
    window hide
    pause
    trista "I think you're onto something!"
    pc "I'll try not to jostle you too much."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/trista/events/stage6/44.webm" loop
    show movie with dissolve
    window hide
    pause
    pc "How's this?"
    trista "Perfect."
    trista "It helps that you're big and strong."
    pc "You're light as a pillow."
    trista "{i}*Giggles*{/i}"
    trista "I think it goes, 'light as a feather'."
    pc "But you're a bit larger than a feather."
    trista "Yeah?"
    pc "Just a little."
    window hide
    pause
    trista "This feels incredible."
    pc "Are you ready for more?"
    trista "You really think you can move me faster than this?"
    trista "You're holding up my weight!"
    pc "Easy. {w}The question is whether you're up for it."
    trista "You underestimate me."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/trista/events/stage6/45.webm" loop
    show movie with dissolve
    "Galvanized by lust you instantly increase the pace of your thrusts, willfully accepting an opportunity to play into Trista's competitive side."
    trista "Ohhh fuck!"
    window hide
    pause
    trista "How are you holding me up for so long?"
    pc "All thanks to my wonderful trainer."
    trista "Wow, she sounds great."
    pc "She's sexy as hell."
    pc "And so is your belly from this angle."
    trista "Yeah? {w}How does it look?"
    pc "Like it's at full capacity."
    trista "Uh! {w}Do you like it?"
    pc "It's not the only thing filled."
    trista "You're getting close?"
    pc "Very!"
    trista "Same! {w}Maybe we can... {p}at the same time..."
    pc "Yesss!"
    pc "Where do you want it?"
    trista "You keep looking at my tummy, so..."
    pc "Perfect!"
    trista "Yessss!"
    window hide
    pause
    stop movie
    image trista_stage6_event_46 = "/trista/events/stage6/46.webp"
    scene trista_stage6_event_46
    "Unable to support herself any longer, she falls back onto the bed."
    "Your eyes are glued to her overburdened gut as your arousal peaks. You unleash a huge load all over her belly and breasts."
    window hide
    pause
    trista "Holy shit!"
    trista "You really were full."
    pc "Not anymore."
    pc "Let me get you a towel."
    image trista_stage6_event_47 = "/trista/events/stage6/47.webp"
    scene trista_stage6_event_47

    trista "Thanks for today!"
    pc "I should be thanking you."
    trista "You had fun?"
    pc "So much."
    trista "Does that mean we can do it again?"
    pc "Absolutely!"
    if recollection == False:
        $ trista.weight += 1
        $ daytime += 1
        $ phonecall = 1
    $ tristastage6event = 0
    return

label Trista_Stage_7_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Trista', dialogue=dialogue_one)
    $ msg ("Time for our weekly session if you are free?", who=1)
    pause
    menu:
        "Workout with Trista.":
            $ hide_messenger()
        "Do something else.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    ###Trista on treadmill###
    image trista_stage7_event_1 = "/trista/events/stage7/1.webp"
    scene trista_stage7_event_1
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    "Walking into the gym you spot Trista jogging on the treadmill."
    "Her recent weight gain was giving you plenty to look at as you approach from behind."
    image trista_stage7_event_2 = "/trista/events/stage7/2.webp"
    scene trista_stage7_event_2
    pc "Hey, Trista."
    trista "Hey, [playername]. Give me two minutes for my post-workout walk."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/trista/events/stage7/3.webm" loop
    show movie with dissolve
    window hide
    pause
    "Standing behind her you try not to stare at her plump rear too obviously."

    ###Trista next to treadmill ###
    stop movie
    image trista_stage7_event_4 = "/trista/events/stage7/4.webp"
    scene trista_stage7_event_4
    trista "Hey, thought I would get a quick workout in before it gets here."
    pc "Gets here?"
    image trista_stage7_event_5 = "/trista/events/stage7/5.webp"
    scene trista_stage7_event_5
    trista "Yeah. I ordered some food. Hasn't arrived yet."
    trista "I really need to kick it into next gear again in terms of eating and working out."
    image trista_stage7_event_6 = "/trista/events/stage7/6.webp"
    scene trista_stage7_event_6
    trista "I have been getting some training in at home and I've made some good progress, but I want to really push myself today."
    pc "Sure. I can help with that."
    trista "Great. But first, mind helping me with the bag till my food arrives?"

    ### At the punching bag ####
    image trista_stage7_event_7 = "/trista/events/stage7/7.webp"
    scene trista_stage7_event_7
    "Grabbing the bag you do your best to hold it still as Trista goes through her routine."
    "Swinging her leg around, you feel it hitting the bag powerfully."
    "For the next fifteen minutes she spins and kicks towards you with perfect rhythm and a fierce power."
    image trista_stage7_event_8 = "/trista/events/stage7/8.webp"
    scene trista_stage7_event_8
    trista "Oh, I just got a text that my food is outside."
    image trista_stage7_event_9 = "/trista/events/stage7/9.webp"
    scene trista_stage7_event_9
    trista "Be right back."
    "Taking a moment to towel down the equipment and tidy up after yourself you go back into the main area."
    image trista_stage7_event_10 = "/trista/events/stage7/10.webp"
    scene trista_stage7_event_10
    "Walking out you see Trista preparing a mountain of burgers."
    image trista_stage7_event_11 = "/trista/events/stage7/11.webp"
    scene trista_stage7_event_11
    trista "Can you believe they thought I was having a party?"
    pc "Uh, yeah, I wonder why they thought that."
    ###Move to somewhere she can sit, same place as for the Pizza’s####
    image trista_stage7_event_12 = "/trista/events/stage7/12.webp"
    scene trista_stage7_event_12
    trista "Same plan as last time: You unwrap them and I'll eat them."
    pc "How many are you planning on eating?"
    image trista_stage7_event_13 = "/trista/events/stage7/13.webp"
    scene trista_stage7_event_13
    trista "All of them, silly."
    pc "All of them? That's a lot of burgers!"
    image trista_stage7_event_14 = "/trista/events/stage7/14.webp"
    scene trista_stage7_event_14
    trista "That's the point. Now come on. I thought you were supposed to be the one pushing my limits."
    trista "I don’t plan on stopping until they are all gone."
    image trista_stage7_event_15 = "/trista/events/stage7/15.webp"
    scene trista_stage7_event_15
    "Grabbing the first double cheeseburger you hand it to Trista."
    "It looks like Trista is psyching herself up like an actual workout before she grabs the burger."
    image trista_stage7_event_16 = "/trista/events/stage7/16.webp"
    scene trista_stage7_event_16
    "In what feels like a matter of seconds the burger is hungrily devoured by Trista with a speed that surprises you."
    image trista_stage7_event_17 = "/trista/events/stage7/17.webp"
    scene trista_stage7_event_17
    trista "Come on! Next!"
    pc "Sorry."
    image trista_stage7_event_18 = "/trista/events/stage7/18.webp"
    scene trista_stage7_event_18
    "Quickly grabbing the next burger you hand it to her as she repeats the process."
    "No longer surprised you are ready when she has finished the second just as quickly."
    image trista_stage7_event_19 = "/trista/events/stage7/19.webp"
    scene trista_stage7_event_19
    "Another is eaten. Then another and another."
    image trista_stage7_event_20 = "/trista/events/stage7/20.webp"
    scene trista_stage7_event_20
    "Trista is making quick work of the mountain of burgers as she basically inhales them."
    "Pieces of lettuce falling from her mouth, but Trista doesn’t care."
    image trista_stage7_event_21 = "/trista/events/stage7/21.webp"
    scene trista_stage7_event_21
    "With half a dozen burgers crammed into her mouth you can already see her stomach growing again."
    "Her tight abs struggling to hide her expanding midsection."
    image trista_stage7_event_22 = "/trista/events/stage7/22.webp"
    scene trista_stage7_event_22
    "Handing Trista the next one she takes a bite, pausing to thump her chest as she begins to struggle with how fast she is eating."
    "Over the next ten minutes her speed falls considerably even as she powers through more than half of the burgers."
    image trista_stage7_event_23 = "/trista/events/stage7/23.webp"
    scene trista_stage7_event_23
    "She’s an eating machine, mechanically chewing and swallowing the vast quantity of food."
    image trista_stage7_event_24 = "/trista/events/stage7/24.webp"
    scene trista_stage7_event_24
    "Her stomach bulging considerably as you watch her chewing through the latest burger."
    image trista_stage7_event_25 = "/trista/events/stage7/25.webp"
    scene trista_stage7_event_25
    trista "How many left?"
    pc "Five, including this one."
    image trista_stage7_event_26 = "/trista/events/stage7/26.webp"
    scene trista_stage7_event_26
    "By this point Trista is clearly having some issues, with each burger almost taking a full minute to eat."
    "Handing her another, you keep the conveyor belt of fatty and calorie-rich meals going."
    image trista_stage7_event_27 = "/trista/events/stage7/27.webp"
    scene trista_stage7_event_27 with vpunch
    trista "Buuurp!"
    image trista_stage7_event_28 = "/trista/events/stage7/28.webp"
    scene trista_stage7_event_28
    "Taking a moment, Trista leans forward and you wonder if she is about to be sick."
    image trista_stage7_event_29 = "/trista/events/stage7/29.webp"
    scene trista_stage7_event_29
    "Her stomach now expanded massively to the point where you think you can hear it almost groaning. Or maybe that was the impending indigestion."
    image trista_stage7_event_30 = "/trista/events/stage7/30.webp"
    scene trista_stage7_event_30
    "Wiping beads of sweat from her forehead Trista outstretches her hand."
    "But even you can't help but think this might be pushing it too far."
    trista "Come on. Give me more burgers."
    image trista_stage7_event_31 = "/trista/events/stage7/31.webp"
    scene trista_stage7_event_31
    "Listening to her you hand her another and watch as she methodically bites her way through it."
    image trista_stage7_event_32 = "/trista/events/stage7/32.webp"
    scene trista_stage7_event_32
    "Placing one hand on her bloated stomach she beckons for the next burger which you hand over."
    trista "Another!"
    image trista_stage7_event_33 = "/trista/events/stage7/33.webp"
    scene trista_stage7_event_33
    "With a look of pure determination on her face, you hand the last burgers one after another."
    image trista_stage7_event_34 = "/trista/events/stage7/34.webp"
    scene trista_stage7_event_34
    trista "Ughh, I…."
    "Pausing Trista puffs out her cheeks as she rubs her distended belly again."
    image trista_stage7_event_35 = "/trista/events/stage7/35.webp"
    scene trista_stage7_event_35
    pc "This is the last one. Almost done!"
    trista "Puhhh."
    image trista_stage7_event_36 = "/trista/events/stage7/36.webp"
    scene trista_stage7_event_36
    "Unable to talk Trista looks ready to burst at any moment as she crams the burger into her mouth."
    "With a few laboured bites she had done it, the mountain of burgers consumed."
    image trista_stage7_event_37 = "/trista/events/stage7/37.webp"
    scene trista_stage7_event_37
    "The party’s worth of food now sitting in her giant stomach."
    image trista_stage7_event_38 = "/trista/events/stage7/38.webp"
    scene trista_stage7_event_38
    trista "I… oh god."
    image trista_stage7_event_39 = "/trista/events/stage7/39.webp"
    scene trista_stage7_event_39
    "Laying back Trista gives you a perfect view of her bloated stomach as she groans loudly."
    image trista_stage7_event_40 = "/trista/events/stage7/40.webp"
    scene trista_stage7_event_40
    "Her stomach catching up with her after her burger binge."
    image trista_stage7_event_41 = "/trista/events/stage7/41.webp"
    scene trista_stage7_event_41
    trista "I think this outdoes even the pizza last time."
    pc "That was impressive."
    trista "Impressive? That was just training."
    trista "But my stomach is so tight."
    image trista_stage7_event_42 = "/trista/events/stage7/42.webp"
    scene trista_stage7_event_42
    "You watch as Trista rubs circles around her engorged belly. You can’t help but to gravitate towards the swollen orb."
    pc "Need a hand?"
    trista "Oh, that would be great."
    image trista_stage7_event_43 = "/trista/events/stage7/43.webp"
    scene trista_stage7_event_43
    "Moving over, you place your hands on her rock-hard stomach."
    "You can tell it's packed to the limit, not an inch to spare."
    "Rubbing in small circles you hear Trista moan in pleasure."
    image trista_stage7_event_44 = "/trista/events/stage7/44.webp"
    scene trista_stage7_event_44
    trista "Oh, that feels amazing. Keep going!"
    "While you gently knead her bloated stomach, she continues to moan loudly."
    "After cleaning up, you head home."
    stop music fadeout 1.0

    #I am thinking this leads to a sex scene in the gym, but I don’t know if this many variations in sex scenes is too much. It could be the same poses as the one in her bed but in the gym? Or feel free to add a bit where you help her get home like the last pizza event and repeat the bloated sex scene from that one again or she pulls you into the Sauna.
    if recollection == False:
        $ trista.weight += 1
        $ daytime += 1
        $ phonecall = 1
    $ tristastage7event = 0
    return

label Trista_Stage_8_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Trista', dialogue=dialogue_one)
    $ msg ("Hey. Fancy coming over a bit earlier for our session?", who=1)
    pause
    $ msg ("I could use a hand with something.", who=1)
    pause
    menu:
        "Workout with Trista.":
            $ hide_messenger()
        "Do something else.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    ###Trista’s gym###
    image trista_stage8_event_1 = "/trista/events/stage8/1.webp"
    scene trista_stage8_event_1
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    "Arriving you can see some of the equipment still packed away."
    "What is she planning? The place looks barely open."
    image trista_stage8_event_2 = "/trista/events/stage8/2.webp"
    scene trista_stage8_event_2
    trista "Hey. Glad you could make it."
    trista "I'm trying out something special today if you fancy helping me."
    pc "What is it?"
    image trista_stage8_event_3 = "/trista/events/stage8/3.webp"
    scene trista_stage8_event_3
    trista "Well, I read online about this amazing new diet."
    trista "It’s a 10k diet and it's supposed to be really good."
    pc "10K?"
    image trista_stage8_event_4 = "/trista/events/stage8/4.webp"
    scene trista_stage8_event_4
    trista "Yeah, so apparently if you eat ten thousand calories in one day and then fast for the next couple of days it sends your body into a primal setting."
    trista "It's supposed to supercharge your ability to turn mass into muscles."
    pc "Ten thousand calories?"
    image trista_stage8_event_5 = "/trista/events/stage8/5.webp"
    scene trista_stage8_event_5
    trista "Yeah, you are right - maybe that's not enough."
    image trista_stage8_event_6 = "/trista/events/stage8/6.webp"
    scene trista_stage8_event_6
    trista "Maybe we should aim for twenty thousand!"
    trista "I've already got a head start with my pre-breakfast meal."
    image trista_stage8_event_7 = "/trista/events/stage8/7.webp"
    scene trista_stage8_event_7
    "You look behind her and see an empty pile of boxes."
    image trista_stage8_event_8 = "/trista/events/stage8/8.webp"
    scene trista_stage8_event_8
    trista "I think that was about five hundred calories and that was nothing."
    trista "With all our training I barely feel like I've eaten anything."
    pc "So what's next? Breakfast?"
    image trista_stage8_event_9 = "/trista/events/stage8/9.webp"
    scene trista_stage8_event_9
    trista "Yep. I'm thinking of heading into town to that café if you want to join."
    pc "What sort of trainer would I be if I said no?"
    stop music fadeout 1.0
    ###Cafe with Trista###
    image trista_stage8_event_10 = "/trista/events/stage8/10.webp"
    scene trista_stage8_event_10
    "Finding yourselves a booth, Trista begins looking through the menu."
    trista "These all sound great and the calorie counts are nice and high."
    image trista_stage8_event_11 = "/trista/events/stage8/11.webp"
    scene trista_stage8_event_11
    "Walking up to the counter you watch as Trista orders and soon comes back with a tray laden with pastries."
    image trista_stage8_event_12 = "/trista/events/stage8/12.webp"
    scene trista_stage8_event_12
    trista "I couldn’t decide so I got one of everything."
    image trista_stage8_event_13 = "/trista/events/stage8/13.webp"
    scene trista_stage8_event_13
    "Grabbing the first pastry Trista digs in, the large baked good reduced to crumbs in seconds."
    image trista_stage8_event_14 = "/trista/events/stage8/14.webp"
    scene trista_stage8_event_14
    "Picking the next up she repeats it, seemingly on a mission to eat them all as quickly as possible."
    image trista_stage8_event_15 = "/trista/events/stage8/15.webp"
    scene trista_stage8_event_15
    "One by one they disappear as Trista fills her stomach until they are all gone."
    image trista_stage8_event_16 = "/trista/events/stage8/16.webp"
    scene trista_stage8_event_16
    trista "They were nice, light bite to start the day."
    "You can't help but feel a need to see her eat those words, or perhaps much more food."
    "Ever since her burger stuffing you have been dreaming of pushing her to similar limits again. Maybe today would be that day."
    pc "In that case I'll be right back."
    image trista_stage8_event_17 = "/trista/events/stage8/17.webp"
    scene trista_stage8_event_17
    "Going up to the counter you place another order, a duplicate of what Trista had already eaten."
    image trista_stage8_event_18 = "/trista/events/stage8/18.webp"
    scene trista_stage8_event_18
    trista "What are these?"
    pc "Well, you seemed to take the last lot in easily enough. It's training, right?"
    pc "Isn't that why I'm here? To make you push your limits?"
    image trista_stage8_event_19 = "/trista/events/stage8/19.webp"
    scene trista_stage8_event_19
    trista "I knew I could count on you."
    trista "But it won't always be this easy. I want to find my limit today!"
    trista "So that means that even when I'm telling you to stop, I want you to push me to keep eating."
    trista "No matter what, keep me eating till we hit that 10k goal."
    pc "I think I can manage that."
    image trista_stage8_event_20 = "/trista/events/stage8/20.webp"
    scene trista_stage8_event_20
    "Grabbing the first of the new pastries Trista starts on the next wave of indulgence."
    image trista_stage8_event_21 = "/trista/events/stage8/21.webp"
    scene trista_stage8_event_21
    "It doesn’t take long for these to disappear either."
    image trista_stage8_event_22 = "/trista/events/stage8/22.webp"
    scene trista_stage8_event_22
    "Sitting back after her double helping you can already see a slight bloating to her filling stomach."
    image trista_stage8_event_23 = "/trista/events/stage8/23.webp"
    scene trista_stage8_event_23
    trista "That was good, although I think I've had enough pastries for now."
    trista "Why don’t we head back to mine and maybe keep this going."
    pc "Sounds good to me."
    image trista_stage8_event_24 = "/trista/events/stage8/24.webp"
    scene trista_stage8_event_24
    trista "Let's stop by at Bonnie's first. Her sweets are the perfect high-calorie treat right now."

    ###Bonnies, with bonnie behind the counter###
    image bonnie_sweetshop3 = "/bonnie/[bonnie.stage]/sweetshop3.webp"
    scene bonnie_sweetshop3
    pc "Hi, Bonnie."
    bonnie "Hi, [playername]. Nice to see you again."
    bonnie "What can I get you?"
    pc "Can I get some of our special treats?"
    image bonnie_sweetshop2 = "/bonnie/[bonnie.stage]/sweetshop2.webp"
    scene bonnie_sweetshop2
    bonnie "Sure thing. I think I have some left over."
    bonnie "Here you go."
    "Taking the chocolates you wave goodbye to Bonnie and carry on with Trista to her place."

    ###Tristas house – Not sure where you would want to do this in her house###
    image trista_stage8_event_25 = "/trista/events/stage8/25.webp"
    scene trista_stage8_event_25
    trista "These smell so good! I can't wait to try them!"
    pc "I thought you weren’t much of a sweets sort of person."
    image trista_stage8_event_26 = "/trista/events/stage8/26.webp"
    scene trista_stage8_event_26
    trista "I wasn’t, until you took me to Bonnie's a few weeks ago."
    trista "Ever since I've been having weekly cravings for these things."
    pc "Well, I'm glad you like them."
    image trista_stage8_event_27 = "/trista/events/stage8/27.webp"
    scene trista_stage8_event_27
    trista "But for now it's not about if I like them, it's about eating them."
    trista "So why don't you come on over and help me out?"

    #[Feeding minigame]
    image trista_stage8_event_102 = "/trista/events/stage8/102.webp"
    scene trista_stage8_event_102
    "You grab a box of chocolates, sit next to her and hold a chocolate in front of her mouth."
    "Trista starts eating the chocolates as if her life depended on it."
    trista "A bit faster, please. I don't have all day to eat these."
    trista "You are going to need to get better at this if we are going to hit 10k today."
    image trista_stage8_event_103 = "/trista/events/stage8/103.webp"
    scene trista_stage8_event_103
    "You push her back on the couch and grab another box of chocolates."
    trista "Wait, what are you doing?"
    pc "You wanted to be fed faster."
    image trista_stage8_event_104 = "/trista/events/stage8/104.webp"
    scene trista_stage8_event_104
    "You then sit on top of her and feed her the chocolates one by one."
    image trista_stage8_event_105 = "/trista/events/stage8/105.webp"
    scene trista_stage8_event_105
    trista "Oh yes, this is it. Keep them coming."
    "One by one you feed her the delicious chocolates."
    image trista_stage8_event_106 = "/trista/events/stage8/106.webp"
    scene trista_stage8_event_106
    "Between boxes you take a moment to rub her belly."
    image trista_stage8_event_107 = "/trista/events/stage8/107.webp"
    scene trista_stage8_event_107
    "Her stomach starts to bloat up after a few boxes are emptied into it."
    trista "I really can't eat anymore."
    pc "Just a few more."
    "You make sure she finishes the current box of chocolates."
    "After finishing the chocolate she sits upright to stretch her muscles."

    #After game
    image trista_stage8_event_28 = "/trista/events/stage8/28.webp"
    scene trista_stage8_event_28
    trista "Wow, those were a lot more filling than I thought they would be."
    trista "I think I'm going to take a nap to let some of them digest."
    image trista_stage8_event_29 = "/trista/events/stage8/29.webp"
    scene trista_stage8_event_29
    "Curling up on the sofa Trista falls asleep as you turn the TV on quietly and let her rest."
    "Watching her breathing peacefully her bloated stomach rises and falls."
    "How much more could you fit in it today, you wondered."

    image trista_stage8_event_30 = "/trista/events/stage8/30.webp"
    scene trista_stage8_event_30
    "Letting Trista sleep for an hour you gently wake her with a cup of coffee and some snacks from her cupboards."
    image trista_stage8_event_31 = "/trista/events/stage8/31.webp"
    scene trista_stage8_event_31
    trista "Ughh, what time is it?"
    pc "Lunch time. Fancy going to Bunny Bites?"
    trista "I'm still a little full from this morning."
    pc "Come on. You are the one who said you want to try this diet."
    pc "You can't give up after only a few hours."
    image trista_stage8_event_32 = "/trista/events/stage8/32.webp"
    scene trista_stage8_event_32
    trista "You are right. I don't know what came over me. Guess I'm still waking up."
    trista "Let's go."

    ###Bunny bites in booth with Trista####
    image trista_stage8_event_33 = "/trista/events/stage8/33.webp"
    scene trista_stage8_event_33
    play music "/music/bunny_bites.ogg" if_changed
    pc "So, what is your usual order here?"
    trista "Most of the time I get a pizza, maybe a burger, some fries and a soda to go with it."
    pc "That’s a fair amount, but maybe we should go a bit bigger today."
    image trista_stage8_event_34 = "/trista/events/stage8/34.webp"
    scene trista_stage8_event_34
    trista "This is my third meal of the day and it's only noon."
    pc "True. But that's only double the amount of food you usually eat."
    image trista_stage8_event_35 = "/trista/events/stage8/35.webp"
    scene trista_stage8_event_35
    pc "If you are aiming for ten thousand calories that’s five times what most people eat."
    trista "True. I hadn't thought about it that way."
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    "Soon Marie arrives to take your order. You use this time to order for Trista."
    pc "Hey, Marie. Can we get two large pizzas, two burger menus with fries and onion rings, one big chicken wrap, a nugget menu and three sodas, please?"
    marie "Sure thing. It will be right out."
    image trista_stage8_event_36 = "/trista/events/stage8/36.webp"
    scene trista_stage8_event_36
    trista "Was that all for me?"
    pc "Yes. You wanted to push yourself, right?"
    trista "I did, but that was a lot of food."
    image trista_stage8_event_37 = "/trista/events/stage8/37.webp"
    scene trista_stage8_event_37
    "A short while later the waitress returns and the table is covered in Trista’s extra large meal."
    image trista_stage8_event_38 = "/trista/events/stage8/38.webp"
    scene trista_stage8_event_38
    "Picking up the first piece of pepperoni pizza, Trista places it into her mouth."
    image trista_stage8_event_39 = "/trista/events/stage8/39.webp"
    scene trista_stage8_event_39
    "Despite the size of the meal and everything she has eaten, Trista still seems to enjoy it."
    image trista_stage8_event_40 = "/trista/events/stage8/40.webp"
    scene trista_stage8_event_40
    "Watching Trista over the next half hour, you enjoy seeing her demolish the first pizza, the fries and half of the second pizza."
    image trista_stage8_event_41 = "/trista/events/stage8/41.webp"
    scene trista_stage8_event_41
    "But it's clear the dense heavy food and day of binging is catching up to her."
    image trista_stage8_event_42 = "/trista/events/stage8/42.webp"
    scene trista_stage8_event_42
    window hide
    pause
    image trista_stage8_event_43 = "/trista/events/stage8/43.webp"
    scene trista_stage8_event_43
    pc "Come on! You can do it!"
    "You try to cheer her on and it seems to work for a moment as she finishes the rest of the slice of pizza quickly."
    image trista_stage8_event_44 = "/trista/events/stage8/44.webp"
    scene trista_stage8_event_44
    trista "I'm so full."
    pc "This is what you wanted. You can't stop now."
    image trista_stage8_event_45 = "/trista/events/stage8/45.webp"
    scene trista_stage8_event_45
    trista "I'm not stopping. Just need a minute."
    image trista_stage8_event_46 = "/trista/events/stage8/46.webp"
    scene trista_stage8_event_46
    "Leaning back Trista repositions herself to give her bloated stomach some extra room."
    image trista_stage8_event_47 = "/trista/events/stage8/47.webp"
    scene trista_stage8_event_47
    "Rubbing it gently you can see her eyeing up the rest of the food."
    image trista_stage8_event_48 = "/trista/events/stage8/48.webp"
    scene trista_stage8_event_48
    "After a few minutes Trista leans forward and grabs one of the large burgers."
    image trista_stage8_event_49 = "/trista/events/stage8/49.webp"
    scene trista_stage8_event_49
    "Digging into it she takes large bites, methodically chewing but clearly not enjoying it as much as she would have normally."
    image trista_stage8_event_50 = "/trista/events/stage8/50.webp"
    scene trista_stage8_event_50
    "It takes some time but eventually two burgers and two sodas are drained."
    image trista_stage8_event_51 = "/trista/events/stage8/51.webp"
    scene trista_stage8_event_51
    "But once again Trista is forced to stop as her still growing stomach reaches its limit."
    image trista_stage8_event_52 = "/trista/events/stage8/52.webp"
    scene trista_stage8_event_52
    trista "I don’t think I can eat this much."
    pc "Don't give up. There is no rush, so you can take all the time you need."
    image trista_stage8_event_53 = "/trista/events/stage8/53.webp"
    scene trista_stage8_event_53
    "Sighing heavily, Trista sinks back into the seat."
    image trista_stage8_event_54 = "/trista/events/stage8/54.webp"
    scene trista_stage8_event_54
    "Her slouched and almost spread eagle posture only made her stomach stick out more."
    image trista_stage8_event_55 = "/trista/events/stage8/55.webp"
    scene trista_stage8_event_55
    "Resting a hand on her stomach she sits in almost silence, the minutes ticking by as Trista’s stomach grumbled."
    image trista_stage8_event_56 = "/trista/events/stage8/56.webp"
    scene trista_stage8_event_56
    "Eventually Trista sits upright again, reaching for the nuggets."
    image trista_stage8_event_57 = "/trista/events/stage8/57.webp"
    scene trista_stage8_event_57
    "It takes almost an hour for Trista to finish her nuggets, taking regular breaks between mouthfuls."
    image trista_stage8_event_58 = "/trista/events/stage8/58.webp"
    scene trista_stage8_event_58
    "But true to her word she keeps going and soon only half a pizza remains."
    image trista_stage8_event_59 = "/trista/events/stage8/59.webp"
    scene trista_stage8_event_59
    trista "OOOH, I feel like a balloon."
    pc "Almost there."
    trista "I don't think I can... Could we just take this home?"
    pc "It's just half a pizza. Besides, we still have some other things waiting back home."
    image trista_stage8_event_60 = "/trista/events/stage8/60.webp"
    scene trista_stage8_event_60
    trista "More?!"
    pc "You can have a break first if you finish this pizza."
    image trista_stage8_event_61 = "/trista/events/stage8/61.webp"
    scene trista_stage8_event_61
    "Starting to eat again, Trista looks physically tired despite having been sitting the entire time."
    image trista_stage8_event_62 = "/trista/events/stage8/62.webp"
    scene trista_stage8_event_62
    "Like before minutes pass between bites as Trista fights to keep going."
    image trista_stage8_event_63 = "/trista/events/stage8/63.webp"
    scene trista_stage8_event_63
    "But finally she is done - the last of the pizza crammed into her beyond stuffed belly."
    trista "Oh god."
    image trista_stage8_event_64 = "/trista/events/stage8/64.webp"
    scene trista_stage8_event_64
    trista "I feel like I'm going to explode."
    trista "I need to sleep this off…and stay away from sharp objects."
    image trista_stage8_event_65 = "/trista/events/stage8/65.webp"
    scene trista_stage8_event_65
    "Helping Trista to her feet you both head back to her place."
    image trista_stage8_event_66 = "/trista/events/stage8/66.webp"
    scene trista_stage8_event_66
    window hide
    pause
    stop music fadeout 1.0

    ###Trista’s place, put her on the bed###
    image trista_stage8_event_67 = "/trista/events/stage8/67.webp"
    scene trista_stage8_event_67
    "Walking into her house, Trista has barely closed the door when she starts to take off her clothes."
    image trista_stage8_event_68 = "/trista/events/stage8/68.webp"
    scene trista_stage8_event_68
    trista "I hope you don't mind. Those clothes were way too tight after all that."
    image trista_stage8_event_69 = "/trista/events/stage8/69.webp"
    scene trista_stage8_event_69
    trista "I just need five minutes."
    pc "Well, if you are going to sleep it off, we may as well add a bit more training."
    image trista_stage8_event_70 = "/trista/events/stage8/70.webp"
    scene trista_stage8_event_70
    trista "What?"
    pc "We still have some chocolates left over."
    pc "Won't matter much since you are going to sleep it all off, right?"
    image trista_stage8_event_71 = "/trista/events/stage8/71.webp"
    scene trista_stage8_event_71
    trista "I guess…"

    #[Stuffing minigame again. This time starts with the bar almost full and reaches the limit but you keep feeding her three or four past the limit.]
    image trista_stage8_event_109 = "/trista/events/stage8/109.webp"
    scene trista_stage8_event_109
    "You grab the box of chocolates and start to feed them to her."
    pc "Come on, Trista. You aren't going to quit, are you?"
    "Begrudgingly she starts to eat the chocolates."
    image trista_stage8_event_110 = "/trista/events/stage8/110.webp"
    scene trista_stage8_event_110
    "Clearly tired of carrying all the extra weight in her belly, she moves over to lie on her side."
    trista "I'm so full. I really need to take a nap."
    pc "Come on. You need to finish these first before taking a nap."
    image trista_stage8_event_111 = "/trista/events/stage8/111.webp"
    scene trista_stage8_event_111
    "While feeding her, you make sure to rub her big bloated belly."
    pc "I'm sure there is some more room in there."
    image trista_stage8_event_112 = "/trista/events/stage8/112.webp"
    scene trista_stage8_event_112
    trista "How many are there left?"
    pc "Six more. You can do it."
    "You really feel like you have to push the chocolates into her mouth in order for her to eat them now."
    "But after a few minutes she finally ate them all."

    image trista_stage8_event_72 = "/trista/events/stage8/72.webp"
    scene trista_stage8_event_72
    "Having been stuffed to the limit again, Trista falls asleep cradling her giant stomach."
    image trista_stage8_event_73 = "/trista/events/stage8/73.webp"
    scene trista_stage8_event_73
    "Looking at it now, it's hard to imagine how flat it was this morning."
    image trista_stage8_event_74 = "/trista/events/stage8/74.webp"
    scene trista_stage8_event_74
    "Sitting next to her you watch some more TV to pass the time."

    ###Trista house####
    "You let Trista sleep for a couple of hours, until its time for her next feeding."
    "Unknown to her, you put your plan into action while she was asleep, but now it was time to wake her."

    ###Trista bedroom – her waking up###
    image trista_stage8_event_75 = "/trista/events/stage8/75.webp"
    scene trista_stage8_event_75
    pc "Hey, Trista, if you want to reach the goal, you are going to need to wake up."
    trista "Mmmm, okay... Yeah..."
    trista "I'm feeling a bit better now."
    pc "Good to hear. The food just arrived."
    image trista_stage8_event_76 = "/trista/events/stage8/76.webp"
    scene trista_stage8_event_76
    trista "What?"
    image trista_stage8_event_77 = "/trista/events/stage8/77.webp"
    scene trista_stage8_event_77
    "You show her the stack of five extra-large pizzas sitting on her table."
    trista "You can't be serious?"
    pc "This should be enough for today."
    image trista_stage8_event_78 = "/trista/events/stage8/78.webp"
    scene trista_stage8_event_78
    trista "There is no way I can eat that much on top of everything I've eaten already."
    pc "I thought you wanted to win this competition. You told me to keep pushing you."
    trista "I did. It's just... Look at my stomach."
    image trista_stage8_event_79 = "/trista/events/stage8/79.webp"
    scene trista_stage8_event_79
    "Indicating to her stomach you can clearly see what she means."
    "Despite having slept for a couple of hours, her stomach had barely gone down at all in size."
    pc "Well, it's up to you. I won't stop you if you want to give up."
    "Those last words had the desired effect as you see Trista’s eyes narrow."
    image trista_stage8_event_80 = "/trista/events/stage8/80.webp"
    scene trista_stage8_event_80
    trista "I don’t quit anything."
    trista "Give me the goddamn pizza."

    ###Sitting on couch with Trista###
    image trista_stage8_event_81 = "/trista/events/stage8/81.webp"
    scene trista_stage8_event_81
    "Taking the first slice Trista starts on her fifth meal of the day."
    image trista_stage8_event_82 = "/trista/events/stage8/82.webp"
    scene trista_stage8_event_82
    "Despite the initial vigour it doesn’t take long for her to slow down again."
    "Even with her desire to keep eating, there is only so much one person can eat in one day."
    image trista_stage8_event_83 = "/trista/events/stage8/83.webp"
    scene trista_stage8_event_83
    "Bite after bite the slices keep disappearing."
    image trista_stage8_event_84 = "/trista/events/stage8/84.webp"
    scene trista_stage8_event_84
    "It takes a while, but soon Trista is three pizzas in and clearly struggling."
    pc "Come on. You can do it."
    image trista_stage8_event_85 = "/trista/events/stage8/85.webp"
    scene trista_stage8_event_85
    trista "I can do it!"
    image trista_stage8_event_86 = "/trista/events/stage8/86.webp"
    scene trista_stage8_event_86
    "Grabbing two slices she speeds up her eating, cramming more and more of the cheesy pizza in her mouth."
    image trista_stage8_event_87 = "/trista/events/stage8/87.webp"
    scene trista_stage8_event_87
    "Her stomach was growing even more than it had earlier."
    image trista_stage8_event_88 = "/trista/events/stage8/88.webp"
    scene trista_stage8_event_88
    "Was this the largest it had ever been before?"
    image trista_stage8_event_89 = "/trista/events/stage8/89.webp"
    scene trista_stage8_event_89
    trista "That’s four. But I think that’s my limit."
    pc "You sure? I thought you weren't a quitter?"
    image trista_stage8_event_90 = "/trista/events/stage8/90.webp"
    scene trista_stage8_event_90
    trista "I'm not, but this is just too much."
    pc "So you are a quitter?"
    trista "I don't want to be, but I just can't eat any more."
    pc "I think you can."
    image trista_stage8_event_91 = "/trista/events/stage8/91.webp"
    scene trista_stage8_event_91
    "Picking up a slice yourself you hold it in front of her mouth."
    image trista_stage8_event_92 = "/trista/events/stage8/92.webp"
    scene trista_stage8_event_92
    "Reluctantly, Trista takes a bite from it as you begin massaging her massive belly."
    "Moving it closer with each bite she obediently keeps eating."
    image trista_stage8_event_93 = "/trista/events/stage8/93.webp"
    scene trista_stage8_event_93
    "One by one you hold up the slices as she gives you a pleading look, but she doesn’t complain again."
    image trista_stage8_event_94 = "/trista/events/stage8/94.webp"
    scene trista_stage8_event_94
    "Soon it's all gone except the last slice."
    trista "I…I can't."
    pc "It's just one more slice. You can manage that."
    trista "I'm so full."
    image trista_stage8_event_95 = "/trista/events/stage8/95.webp"
    scene trista_stage8_event_95
    "Rubbing her stomach, it's rock solid, but she was so close to being done."
    pc "I think I can feel some room in there."
    image trista_stage8_event_96 = "/trista/events/stage8/96.webp"
    scene trista_stage8_event_96
    "Moving her mouth Trista takes another bite, groaning slightly as she does so."
    "With a little help from you, Trista finishes the slice. She had done it."
    image trista_stage8_event_97 = "/trista/events/stage8/97.webp"
    scene trista_stage8_event_97
    pc "There we go. Wasn't too bad, was it?"
    image trista_stage8_event_98 = "/trista/events/stage8/98.webp"
    scene trista_stage8_event_98
    trista "I didn’t think it was possible to be this full."
    image trista_stage8_event_99 = "/trista/events/stage8/99.webp"
    scene trista_stage8_event_99
    pc "Looks like your training is paying off."
    image trista_stage8_event_100 = "/trista/events/stage8/100.webp"
    scene trista_stage8_event_100
    trista "I hope so."
    pc "Going to keep doing this diet?"
    trista "Ughh, right now I don’t even want to think about any more food."
    pc "Well, I think you did great and those other competitors don't stand a chance."
    trista "Thanks, but I think this is enough for today, or maybe this month."
    trista "For now I think I'm going to sleep till next week."

    ###Outside###
    image trista_stage8_event_101 = "/trista/events/stage8/101.webp"
    scene trista_stage8_event_101
    "After helping Trista to bed you head home."
    "What a day! You couldn't think of anything you would rather have done today."
    if recollection == False:
        $ trista.weight += 2
        $ daytime = 4
        $ phonecall = 1
    $ tristastage8event = 0
    return

label TristaStage8Phone:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Trista', dialogue=dialogue_one)
    $ msg ("Uggh, what happened yesterday.", who=1)
    pause
    $ msg ("I feel kind of gross.", who=1)
    pause
    $ msg ("I think you might have gone a bit overboard with the diet plan.")
    pause
    $ msg ("You are telling me, I’m still so bloated.", who=1)
    pause
    $ msg (None, who=1, pic="stage8_trista")
    pause
    $ msg ("So, not thinking of carrying on the 10k diet?")
    pause
    $ msg ("No, that does it for me and fad diets.", who=1)
    pause
    $ msg ("Back to regular working out and eating regular meals.", who=1)
    pause
    $ msg ("See you for our regular session this week?", who=1)
    pause
    $ msg ("Definitely.")
    pause
    $ hide_messenger()
    window hide

    $ tristastage8phone = 0
    return

label Trista_Stage_10_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Trista', dialogue=dialogue_one)
    $ msg ("Hey, [playername]. Ready for our weekly work out?", who=1)
    pause
    menu:
        "Workout with Trista.":
            $ hide_messenger()
        "Do something else.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright, another time.", who=1)
            pause
            $ hide_messenger()
            return

    ### Gym with Trista behind counter snacking on something ###
    image trista_stage10_event_1 = "/trista/events/stage10/1.webp"
    scene trista_stage10_event_1
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    "Arriving at the gym, you spot Trista at the counter. She looks a little sad."
    image trista_stage10_event_2 = "/trista/events/stage10/2.webp"
    scene trista_stage10_event_2
    pc "Hey, Trista. Everything okay?"
    trista "Yeah, I guess, just a little down. I didn't win the nationals, didn't really get close."
    pc "I'm sorry to hear that."
    image trista_stage10_event_3 = "/trista/events/stage10/3.webp"
    scene trista_stage10_event_3
    trista "It's okay. I think I overdid the carb loading."
    trista "I couldn’t believe how much the scale said I was at the weigh in."
    trista "I've never been this heavy in my life. I was the largest and heaviest one in the whole competition."
    pc "Just more potential for the next championship."
    image trista_stage10_event_4 = "/trista/events/stage10/4.webp"
    scene trista_stage10_event_4
    trista "Maybe…"
    pc "Maybe? I thought you didn’t quit?"
    image trista_stage10_event_5 = "/trista/events/stage10/5.webp"
    scene trista_stage10_event_5
    trista "It's not that. It's... kind of embarrassing."
    pc "What?"
    image trista_stage10_event_6 = "/trista/events/stage10/6.webp"
    scene trista_stage10_event_6
    trista "I feel great and I kind of loved the extra attention I got at the competition."
    trista "People couldn't keep their eyes off me. I thought it was because they were shocked or making fun of me."
    trista "But then a few of them asked me out. I thought people would have been put off, but it seems like people still find me attractive."
    pc "That’s because you are."
    image trista_stage10_event_7 = "/trista/events/stage10/7.webp"
    scene trista_stage10_event_7
    trista "Oh, shut up, you... but thank you."
    pc "So what now?"
    image trista_stage10_event_8 = "/trista/events/stage10/8.webp"
    scene trista_stage10_event_8
    trista "Well, it wasn’t just the guys that were watching me, there were some sponsors that reached out too."
    pc "That's amazing! Are they going to help with your kickboxing?"
    trista "Not exactly."
    trista "There was this guy, he apparently represents a lot of competitive eaters. Weirdly he saw me and Katrine eating at the beach the other week too."
    pc "Competitive eating?"
    image trista_stage10_event_9 = "/trista/events/stage10/9.webp"
    scene trista_stage10_event_9
    trista "Yeah. And he thinks I have what it takes to be a great one."
    pc "You did break the record at the beach on your first try, but can you make money doing it?"
    trista "Yeah. Apparently companies will pay big money for these events, and sponsors will pay to get their branding next to the likely winner."
    pc "That's amazing! It is a bit of a departure from kickboxing though."
    image trista_stage10_event_10 = "/trista/events/stage10/10.webp"
    scene trista_stage10_event_10
    trista "It is. But honestly, I just love competitions - trying to be the best at something."
    trista "And I really think I can be great at this."
    pc "You don’t have to tell me, I've seen our training."
    image trista_stage10_event_11 = "/trista/events/stage10/11.webp"
    scene trista_stage10_event_11
    trista "That’s kind of what I wanted to talk to you about."
    trista "You have been amazing at training me and I’d love it if you wanted to keep working with me."
    trista "I realise it’s a bit weird, so if you don’t want to I understand."
    pc "I'd love to. Whatever you want to do, I support you."
    image trista_stage10_event_12 = "/trista/events/stage10/12.webp"
    scene trista_stage10_event_12
    trista "Thank you."
    image trista_stage10_event_13 = "/trista/events/stage10/13.webp"
    scene trista_stage10_event_13
    "Trista leans forward and gives you a kiss on the cheek."
    image trista_stage10_event_14 = "/trista/events/stage10/14.webp"
    scene trista_stage10_event_14
    pc "So what now?"
    trista "I guess we start training."
    pc "Could head back to Bunny Bites and see what they have to offer?"
    image trista_stage10_event_15 = "/trista/events/stage10/15.webp"
    scene trista_stage10_event_15
    trista "Sure thing. I'm actually pretty hungry."
    stop music fadeout 1.0

    ###Bunny bites in booth with Trista###
    image trista_stage10_event_16 = "/trista/events/stage10/16.webp"
    scene trista_stage10_event_16
    play music "/music/bunny_bites.ogg" if_changed
    "Arriving at Bunny Bites you grab a table and Marie quickly comes over to take your order."
    trista "Hi. Can I get ten burgers, ten servings of fries and ten sodas, please?"
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Sure. I'll be right back with your food."
    image trista_stage10_event_17 = "/trista/events/stage10/17.webp"
    scene trista_stage10_event_17
    pc "That was a lot of soda. Think you can manage it?"
    trista "One way to find out, right? Got to keep pushing myself."
    image trista_stage10_event_18 = "/trista/events/stage10/18.webp"
    scene trista_stage10_event_18
    "Soon the waitress returns with Trista’s large meal."
    image trista_stage10_event_19 = "/trista/events/stage10/19.webp"
    scene trista_stage10_event_19
    "Grabbing the first burger Trista gives you a look over the table before diving into her feast."
    image trista_stage10_event_20 = "/trista/events/stage10/20.webp"
    scene trista_stage10_event_20
    trista "Mmm, so good."
    "In just a few bites the first burger is gone, her speed even quicker than it had been before."
    image trista_stage10_event_21 = "/trista/events/stage10/21.webp"
    scene trista_stage10_event_21
    "Picking up the next burger it quickly follows the first, then another and another."
    image trista_stage10_event_22 = "/trista/events/stage10/22.webp"
    scene trista_stage10_event_22
    "Grabbing a handful of fries Trista shoves them in haphazardly as she still chews the burger."
    image trista_stage10_event_23 = "/trista/events/stage10/23.webp"
    scene trista_stage10_event_23
    "She is making good progress, but as the eighth burger is finished she is forced to pause."
    image trista_stage10_event_24 = "/trista/events/stage10/24.webp"
    scene trista_stage10_event_24
    "She opens up her jeans to give her already bloated belly some more room."
    pc "How you doing?"
    image trista_stage10_event_25 = "/trista/events/stage10/25.webp"
    scene trista_stage10_event_25
    trista "Good. Starting to feel a bit full now though."
    pc "Only a couple of burgers left."
    image trista_stage10_event_26 = "/trista/events/stage10/26.webp"
    scene trista_stage10_event_26
    "Spurred on by your encouragement Trista makes short work of the rest of the fries and burgers."
    image trista_stage10_event_27 = "/trista/events/stage10/27.webp"
    scene trista_stage10_event_27
    trista "Oooh, definitely feeling a bit full now."
    pc "You have done great, just the soda to go."
    image trista_stage10_event_28 = "/trista/events/stage10/28.webp"
    scene trista_stage10_event_28
    trista "I don’t know, this is a lot. We haven’t really done much training with liquids."
    pc "Don’t think about it, just one drink after another. Maybe use this to see how much you can fit in there."
    trista "You're right. Let's give this a go."
    image trista_stage10_event_29 = "/trista/events/stage10/29.webp"
    scene trista_stage10_event_29
    "The first soda is quickly drunk by Trista, who had been sipping from it during the meal."
    image trista_stage10_event_30 = "/trista/events/stage10/30.webp"
    scene trista_stage10_event_30
    "Her stomach is already showing the signs of her meal. How much bigger will it get with all this soda?"
    image trista_stage10_event_31 = "/trista/events/stage10/31.webp"
    scene trista_stage10_event_31
    trista "That was pretty easy. I can drink quicker than I can eat."
    image trista_stage10_event_32 = "/trista/events/stage10/32.webp"
    scene trista_stage10_event_32
    "Grabbing the other sodas, Trista sucks them dry one after another."
    image trista_stage10_event_33 = "/trista/events/stage10/33.webp"
    scene trista_stage10_event_33
    "However, she is soon starting to regret those confident words as her growing stomach really begins to balloon out of her."
    image trista_stage10_event_34 = "/trista/events/stage10/34.webp"
    scene trista_stage10_event_34
    trista "Oooh, I didn’t think about how bloated this would all make me."
    "Pressing on her taut stomach, Trista gives it a quick jiggle."
    image trista_stage10_event_35 = "/trista/events/stage10/35.webp"
    scene trista_stage10_event_35 with vpunch
    trista "Buuurp."
    image trista_stage10_event_36 = "/trista/events/stage10/36.webp"
    scene trista_stage10_event_36
    trista "Excuse me. There is just so much air in me."
    pc "You can do it. Don't be defeated by the drinks. You already did the hard part with the burgers."
    trista "I may have spoken too soon about that."
    image trista_stage10_event_37 = "/trista/events/stage10/37.webp"
    scene trista_stage10_event_37
    "Slowly sipping from the straw on the sixth soda, it's clear she is starting to really struggle."
    "You have seen her eat mountains of food in the past, but this time her stomach seems to grow the fastest as the gas and liquid rushes down her throat."
    image trista_stage10_event_38 = "/trista/events/stage10/38.webp"
    scene trista_stage10_event_38
    trista "Oooh."
    "Trying to shake her stomach again to get some more gas out, Trista finds it is now as hard as a rock."
    "The liquid has rushed in and filled all the possible space."
    pc "Just a couple more."
    image trista_stage10_event_39 = "/trista/events/stage10/39.webp"
    scene trista_stage10_event_39
    "Forcing herself to continue Trista is clearly not enjoying this, but she is determined to finish."
    "Slowly slurping, she is relieved to hear the gurgles of an empty soda cup. She has done it."
    image trista_stage10_event_40 = "/trista/events/stage10/40.webp"
    scene trista_stage10_event_40
    trista "Oh god. This feels way worse than real food."
    image trista_stage10_event_41 = "/trista/events/stage10/41.webp"
    scene trista_stage10_event_41
    "Leaning back, Trista pats her stomach, sounding like a taut liquid filled drum."
    trista "Now I really feel and look like a balloon."
    image trista_stage10_event_42 = "/trista/events/stage10/42.webp"
    scene trista_stage10_event_42
    pc "You did it though."
    trista "I did, didn't I?"
    image trista_stage10_event_43 = "/trista/events/stage10/43.webp"
    scene trista_stage10_event_43
    "Smiling, Trista leans back, contently rubbing her stomach as she tries to calm the ocean of liquid inside her."
    "Letting her sit there you admire her belly again, before she opens her eyes to look at you."
    image trista_stage10_event_44 = "/trista/events/stage10/44.webp"
    scene trista_stage10_event_44
    trista "You like this, don't you?"
    pc "What?"
    trista "Watching me eat, stuffing myself to my absolute limit."
    pc "I…do you?"
    image trista_stage10_event_45 = "/trista/events/stage10/45.webp"
    scene trista_stage10_event_45
    trista "I do like the attention, it's nice to feel wanted."
    trista "I was trying to figure out why you want to help so much."
    pc "Just because I enjoy it doesn’t mean I wouldn’t have helped you otherwise."
    image trista_stage10_event_46 = "/trista/events/stage10/46.webp"
    scene trista_stage10_event_46
    trista "Well, I think I have something else you can help with if you want to head back to mine."
    pc "Absolutely."
    stop music fadeout 1.0

    ###Trista’s house hallway###
    image trista_stage10_event_47 = "/trista/events/stage10/47.webp"
    scene trista_stage10_event_47
    "Walking into her house, Trista has barely closed the door when she starts stripping."
    window hide
    pause
    image trista_stage10_event_48 = "/trista/events/stage10/48.webp"
    scene trista_stage10_event_48
    pause
    image trista_stage10_event_49 = "/trista/events/stage10/49.webp"
    scene trista_stage10_event_49
    pause
    image trista_stage10_event_50 = "/trista/events/stage10/50.webp"
    scene trista_stage10_event_50
    trista "That's better. I needed to get those off my belly."
    ###Trista’s house hallway###
    image trista_stage10_event_51 = "/trista/events/stage10/51.webp"
    scene trista_stage10_event_51
    trista "In fact, I think I have a little bit more room after the walk."
    trista "Why don't you grab something from the kitchen and join me on the bed?"

    image trista_stage10_event_52 = "/trista/events/stage10/52.webp"
    scene trista_stage10_event_52
    pc "Is this what you had in mind?"
    trista "You must be a mind reader."
    image trista_stage10_event_53 = "/trista/events/stage10/53.webp"
    scene trista_stage10_event_53
    trista "I could use your help."
    pc "My pleasure."
    image trista_stage10_event_54 = "/trista/events/stage10/54.webp"
    scene trista_stage10_event_54
    trista "Oh, you really do enjoy this, don't you?"
    trista "I can feel exactly how much pressed against my leg."
    trista "I guess we'll have to do something about it..."
    if persistent.nosexscene == True:
        scene black with dissolve
        "Trista and you had a great time together."
        if recollection == False:
            $ trista.weight += 2
            $ daytime += 1
            $ phonecall = 1
        $ tristastage10event = 0
        return
    image trista_stage10_event_55 = "/trista/events/stage10/55.webp"
    scene trista_stage10_event_55
    trista "...like this!"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/trista/events/stage10/56.webm" loop
    show movie with dissolve
    window hide
    pause
    pc "Damn, woman!"
    trista "How's this for a thank you?"
    pc "You're making me feel like all my hard work has paid off."
    trista "Excellent!"
    window hide
    pause
    trista "Although..."
    trista "...you might still need to encourage me here."
    trista "I'm starting to lose steam."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/trista/events/stage10/57.webm" loop
    show movie with dissolve
    window hide
    pause
    pc "You got this, girl!"
    pc "They say a little physical activity helps aid digestion, and we are going to need to take advantage of everything we can to help up your stomach capacity if we want you to be competitive."
    trista "I love it."
    trista "But I'm still so full..."
    trista "I'm slowing down!"
    pc "That's okay, but keep going."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/trista/events/stage10/58.webm" loop
    show movie with dissolve
    window hide
    pause
    trista "Every muscle... burning."
    pc "You're a legend."
    trista "Whew! Can't talk... must breathe."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/trista/events/stage10/59.webm" loop
    show movie with dissolve
    window hide
    pause
    trista "How does - huff - that feel?"
    pc "Incredible."
    trista "Good!"
    window hide
    pause
    trista "I just had a thought."
    trista "You know how big my belly is right now?"
    pc "I'm looking right at it."
    trista "When you finish..."
    trista "Could you try to cover it?"
    trista "Just unload all over it."
    pc "Absolutely."
    stop movie
    image trista_stage10_event_60 = "/trista/events/stage10/60.webp"
    scene trista_stage10_event_60
    "Fit to burst you quickly pull out and glaze the beached blonde, giving her exactly what she wanted."
    window hide
    pause
    trista "Ohhhh! That's it!"
    trista "You covered me."
    trista "Now I won't get any stretch marks."
    trista "Let me rub it in..."
    image trista_stage10_event_61 = "/trista/events/stage10/61.webp"
    scene trista_stage10_event_61
    trista "That was amazing."
    trista "I can't wait to do this more often, stuffing myself just for you."
    pc "And the sponsorship money."
    image trista_stage10_event_62 = "/trista/events/stage10/62.webp"
    scene trista_stage10_event_62
    trista "Right, the competitions too. Soon I'll be a champion eater and you will be my sexy little plaything."

    ###Outside###
    "Leaving the stuffed Trista in her bed you head home."
    "You can't wait to see what she has in store in the future."
    if recollection == False:
        $ trista.weight += 2
        $ daytime += 1
        $ phonecall = 1
    $ tristastage10event = 0
    return

label Trista_BB_Extra:
    if trista.stage <= 4:
        trista "Wow, that's a lot. You joining me?"
        trista "I didn't order this much."
        pc "Oh, sorry for the mix up. Are you ok to have this order at no extra cost?"
        trista "Uh, sure. Free food is free food, right? Can't complain."
        pc "In that case, enjoy your meal."
        trista "Thanks."
        image cafe_trista_struggle = "/trista/[trista.stage]/cafe_struggle.webp"
        scene cafe_trista_struggle
        "A short while later you can see Trista struggling to finish the extra food you gave her."
    elif trista.stage >= 5 and trista.stage <= 8:
        trista "I think there has been another mistake. I didn't order this much."
        pc "Oh, are you ok to have this order at no extra cost?"
        image cafe_trista_extrafood_talk = "/trista/[trista.stage]/cafe_extrafood_talk.webp"
        scene cafe_trista_extrafood_talk
        trista "Yes! This is perfect!"
        trista "If you happen to make any other mistakes I won't say no."
        trista "Particularly if they happen to involve another burger or two."
        pc "I'll see what I can do. Enjoy your meal."
        trista "Thanks."
        "Going back into the kitchen you order a couple of extra burgers for Trista."
        image cafe_trista_struggle = "/trista/[trista.stage]/cafe_struggle.webp"
        scene cafe_trista_struggle
        "A short while later you can see Trista finishing off the extra food you gave her."
        "Despite looking fit to burst she just kept eating, even finishing the extra portions you made her."
    else:
        trista "I didn't order this much, but if it's another mistake I will gladly take it."
        pc "Yes, sorry, it is."
        trista "No need to apologise, it's half the reason I came here."
        image cafe_trista_extrafood_talk = "/trista/[trista.stage]/cafe_extrafood_talk.webp"
        scene cafe_trista_extrafood_talk
        trista "But did this mistake happen to include the extra burgers you usually bring me?"
        pc "Uhh... yes, I guess it does."
        trista "Great."
        pc "Enjoy your meal."
        trista "I will do. Thanks."
        image cafe_trista_struggle = "/trista/[trista.stage]/cafe_struggle.webp"
        scene cafe_trista_struggle
        "A short while later you can see Trista stuffing herself with the extra food you gave her."
        "Despite her already giant belly, it doesn't look like the extra food was much of a struggle for her."
    return

label Trista_BB_Prize:
    image cafe_trista_prize1 = "/trista/[trista.stage]/cafe_prize1.webp"
    scene cafe_trista_prize1
    "Creating a sizable feast, you approach Trista."
    image cafe_trista_prize2 = "/trista/[trista.stage]/cafe_prize2.webp"
    scene cafe_trista_prize2
    pc "Congratulations, you have won our weekly prize!"
    if tristaprizefirsttime == 1:
        trista "Lucky me…but what prize?"
        pc "Every order gets an automatic entry into a prize pool."
        pc "The winner gets as much free food as they can eat."
        trista "As much as I want?"
        pc "Exactly."
        trista "Well, bring it on then!"
        image cafe_trista_prize3 = "/trista/[trista.stage]/cafe_prize3.webp"
        scene cafe_trista_prize3
        "Placing the food on the table, Trista smiles as it keeps coming."
        image cafe_trista_prize4 = "/trista/[trista.stage]/cafe_prize4.webp"
        scene cafe_trista_prize4
        "Picking up a slice of Pizza, Trista digs into her free meal."
        "Stuffing it in, Trista eats rapidly."
        image cafe_trista_prize5 = "/trista/[trista.stage]/cafe_prize5.webp"
        scene cafe_trista_prize5
        "Her stomach is quickly growing as she eats more and more."
        image cafe_trista_prize6 = "/trista/[trista.stage]/cafe_prize6.webp"
        scene cafe_trista_prize6
        "Despite her best efforts, Trista eventually grinds to a halt as she leans back, completely full."
        image cafe_trista_prize7 = "/trista/[trista.stage]/cafe_prize7.webp"
        scene cafe_trista_prize7
        pc "How was the food?"
        trista "Really good, although I am surprised I couldn't manage more."
        trista "I guess my big breakfast and post workout snack were more filling than I thought."
        pc "I'll pack the rest up so you can take it home with you."
        trista "That's perfect, I know I'll be ready for another round in a couple of hours."
        image cafe_trista_prize8 = "/trista/[trista.stage]/cafe_prize8.webp"
        scene cafe_trista_prize8
        "Returning a few minutes later, you hand Trista two large bags of food to take home with her."
        "A rather stuffed Trista leaves you to carry on with the rest of your work."
        $ tristaprizefirsttime = 0
    elif trista.stage <= 7:
        trista "Again, you must be my lucky charm."
        trista "Bring on the feast, I know I can do better than last time!"
        image cafe_trista_prize3 = "/trista/[trista.stage]/cafe_prize3.webp"
        scene cafe_trista_prize3
        "Placing the food on the table, Trista smiles as it keeps coming."
        image cafe_trista_prize4 = "/trista/[trista.stage]/cafe_prize4.webp"
        scene cafe_trista_prize4
        "Picking up a slice of Pizza, Trista digs into her free meal."
        "Stuffing it in, Trista eats rapidly, her hands grabbing for more even as she chews the previous bite."
        image cafe_trista_prize5 = "/trista/[trista.stage]/cafe_prize5.webp"
        scene cafe_trista_prize5
        "You can see her stomach growing as she eats more and more."
        image cafe_trista_prize6 = "/trista/[trista.stage]/cafe_prize6.webp"
        scene cafe_trista_prize6
        "With almost the entire table emptied, Trista eventually grinds to a halt as she leans back, completely full."
        image cafe_trista_prize7 = "/trista/[trista.stage]/cafe_prize7.webp"
        scene cafe_trista_prize7
        pc "How was the food?"
        trista "Really good, although I definitely got more in than last time."
        trista "Next time you might even need to make extra."
        pc "I'll pack the rest up so you can take it home with you."
        trista "That's perfect, I know I'll be ready for another round in a couple of hours."
        image cafe_trista_prize8 = "/trista/[trista.stage]/cafe_prize8.webp"
        scene cafe_trista_prize8
        "Returning a few minutes later, you hand Trista two large bags of food to take home with her."
        "A rather stuffed Trista leaves you to carry on with the rest of your work."
    elif trista.stage >= 8:
        trista "Just what I needed, this place is amazing!"
        trista "This time I'm going to finish it!"
        image cafe_trista_prize3 = "/trista/[trista.stage]/cafe_prize3.webp"
        scene cafe_trista_prize3
        "Placing the food on the table, Trista smiles as it keeps coming."
        image cafe_trista_prize4 = "/trista/[trista.stage]/cafe_prize4.webp"
        scene cafe_trista_prize4
        "Picking up a slice of Pizza, Trista digs into her free meal."
        "Stuffing it in, Trista almost seems frustrated by her own slow rate of chewing."
        "Holding up slices of pizza with both hands, she greedily alternates taking bites out of them."
        image cafe_trista_prize5 = "/trista/[trista.stage]/cafe_prize5.webp"
        scene cafe_trista_prize5
        "Despite her stomach looking ready to explode, Trista clears the table."
        image cafe_trista_prize6 = "/trista/[trista.stage]/cafe_prize6.webp"
        scene cafe_trista_prize6
        pause
        image cafe_trista_prize7 = "/trista/[trista.stage]/cafe_prize7.webp"
        scene cafe_trista_prize7
        pc "How was the food?"
        trista "Really good, but you said it was unlimited right?"
        pc "I did."
        trista "In that case, I'll need another two burgers, some onion rings and a milkshake…no two milkshakes."
        pc "Returning to the kitchen, you quickly get the extra food processed and throw some chicken nuggets in as an extra."
        image cafe_trista_prize9 = "/trista/[trista.stage]/cafe_prize9.webp"
        scene cafe_trista_prize9
        "Returning to the table, Trista smiles as you approach."
        pc "Here are your extra's."
        trista "Perfect."
        image cafe_trista_prize10 = "/trista/[trista.stage]/cafe_prize10.webp"
        scene cafe_trista_prize10
        "Grabbing the burger she takes a hearty bite, determined to stuff herself to her absolute limit once more."
        image cafe_trista_prize11 = "/trista/[trista.stage]/cafe_prize11.webp"
        scene cafe_trista_prize11
        "A few minutes later, Trista is finally full as she lays back in the seat."
        pc "Is that everything?"
        trista "Yeah, that will do for today."
        image cafe_trista_prize12 = "/trista/[trista.stage]/cafe_prize12.webp"
        scene cafe_trista_prize12
        "Leaving her to recover, a while later the stuffed Trista leaves you to carry on with the rest of your work."
    return