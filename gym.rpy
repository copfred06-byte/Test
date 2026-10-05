label bonnie_gym1:
    if bonniegymfirsttime == 1:
        image bonnie_gym_dumbel = "/bonnie/[bonnie.stage]/gym_dumbel.webp"
        scene bonnie_gym_dumbel
        "Is that Bonnie working out on the weights?"
        pc "Hey, Bonnie. I didn't know you worked out here?"
        image bonnie_gym_sitting = "/bonnie/[bonnie.stage]/gym_sitting.webp"
        scene bonnie_gym_sitting
        bonnie "Oh, hey, [playername]."
        bonnie "Yeah, I don't come here that often."
        pc "Well, would you like to work out together?"
        bonnie "Yeah, that would be nice."
        image bonnie_gym_standing = "/bonnie/[bonnie.stage]/gym_standing.webp"
        scene bonnie_gym_standing
        bonnie "I'm still a bit new to this, so it would be good to get some pointers if you have any?"
        pc "Sure, I'm happy to help. Although Trista would be better at giving advice if that's what you are after?"
        bonnie "True."
        bonnie "But between you and me, she can be a little intimidating."
        pc "Fair point."
        pc "Well, why don't you have another go and I’ll spot for you."
        image bonnie_gym_benchpress1 = "/bonnie/[bonnie.stage]/gym_benchpress1.webp"
        scene bonnie_gym_benchpress1
        "Standing behind the bench you watch Bonnie as she does a set of reps."
        "She doesn't have the same form as Katrine or Trista, but it is still good."
        image bonnie_gym_sitting2 = "/bonnie/[bonnie.stage]/gym_sitting2.webp"
        scene bonnie_gym_sitting2
        pc "You are pretty good, even if you doubt yourself."
        bonnie "That's nice of you to say."
        bonnie "I have never really been a gym person, so it's good to know that I'm not doing it totally wrong."
        bonnie "But why don't you show me how to do it?"
        "Moving over, she indicates for you to take the bench."
        image bonnie_gym_benchpress2 = "/bonnie/[bonnie.stage]/gym_benchpress2.webp"
        scene bonnie_gym_benchpress2
        bonnie "What do I do?"
        pc "It's easy, just stand behind the bar and be ready to support it if I struggle."
        bonnie "That's a lot of responsibility."
        pc "It will be fine, I’m still using low weights so I shouldn’t have any problems."
        "Bonnie spots you as you do a set of lifts."
        "Paying careful attention, she looks ready to jump in at any moment."
        call strengthup
        image bonnie_gym_standing = "/bonnie/[bonnie.stage]/gym_standing.webp"
        scene bonnie_gym_standing
        pc "Thanks."
        bonnie "No problem. I almost feel like a proper weight lifter now."
        bonnie "But I need to get back to the store."
        pc "Sure thing, maybe we can work out together another time?"
        bonnie "Definitely, it's more fun to do it with a friend."
        "Bonnie leaves you to carry on with the rest of your workout."
        $ bonnie_gym_today = 1
        $ bonniegymfirsttime = 0
        return

    elif bonnie.stage <= 4:
        image bonnie_gym_dumbel = "/bonnie/[bonnie.stage]/gym_dumbel.webp"
        scene bonnie_gym_dumbel
        "Is that Bonnie working out on the weights?"
        pc "Hey, Bonnie. How are you?"
        image bonnie_gym_sitting = "/bonnie/[bonnie.stage]/gym_sitting.webp"
        scene bonnie_gym_sitting
        bonnie "Hey, [playername]. I'm good thank you."
        bonnie "Just getting in my weekly workout."
        pc "Want to work out together?"
        bonnie "Definitely."
        image bonnie_gym_treadmill = "/bonnie/[bonnie.stage]/gym_treadmill.webp"
        scene bonnie_gym_treadmill
        "Moving over to the treadmill, you start chatting as you work out together."
        "Next to you Bonnie power walks, her speed slow but consistent."
        "You feel like your core muscles have gotten stronger from the run."
        call strengthup

        ###Next to treadmills###
        image bonnie_gym_standing = "/bonnie/[bonnie.stage]/gym_standing.webp"
        scene bonnie_gym_standing
        bonnie "Wow, that was great. It went by so much quicker than when I am on my own."
        pc "Yeah, it helps distract our brains I guess."
        bonnie "Well, I need to get back again. Mind helping me warm down first?"
        pc "Sure thing."
        bonnie "Great. Can you pass me that yoga ball?"
        image bonnie_gym_warmdown = "/bonnie/[bonnie.stage]/gym_warmdown.webp"
        scene bonnie_gym_warmdown
        "Grabbing the exercise ball Bonnie begins to slowly work out her body."
        if bonnie.stage == 1:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/1/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/1/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 2:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/2/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/2/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 3:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/3/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/3/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/4/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/4/gym_warmdown_top.webm" loop
            show movie with dissolve
        "She must have a surprising amount of core strength to do this, maybe she was more of a gym person than she was letting on."
        window hide
        pause
        stop movie
        image bonnie_gym_standing2 = "/bonnie/[bonnie.stage]/gym_standing2.webp"
        scene bonnie_gym_standing2
        "After a few more curls she stands up looking content."
        bonnie "Ah, that was good. My body feels looser already."
        bonnie "I'd better make a move, but I'd love to work out together again if you want to."
        pc "Sure, I had fun."
        bonnie "Great. See you around, [playername]."
        $ bonnie_gym_today = 1
        return

    elif bonnie.stage >= 5:
        image bonnie_gym_dumbel = "/bonnie/[bonnie.stage]/gym_dumbel.webp"
        scene bonnie_gym_dumbel
        "Is that Bonnie working out on the weights?"
        pc "Hey, Bonnie. How are you?"
        image bonnie_gym_sitting = "/bonnie/[bonnie.stage]/gym_sitting.webp"
        scene bonnie_gym_sitting
        bonnie "Hey, [playername]. I'm good thank you."
        bonnie "Just getting in my weekly workout."
        pc "Want to work out together?"
        bonnie "That would be lovely."
        image bonnie_gym_treadmill = "/bonnie/[bonnie.stage]/gym_treadmill.webp"
        scene bonnie_gym_treadmill
        "Moving over to the treadmill, you start chatting as you work out together."
        "Next to you Bonnie power walks as you run."
        "Her recent weight gain is easy to notice, but doesnt seem to be slowing her down."
        "You feel like your core muscles have gotten stronger from the run."
        call strengthup

        ###Next to treadmills###
        image bonnie_gym_standing = "/bonnie/[bonnie.stage]/gym_standing.webp"
        scene bonnie_gym_standing
        bonnie "Wow, that was great. It always goes quicker with you than when I am on my own."
        pc "Yeah, it’s a lot more fun to have company."
        bonnie "Speaking of, want to join me in a warm down?"
        pc "Maybe another time. Still have a bit more to do before I finish."
        bonnie "Fair enough."
        image bonnie_gym_warmdown = "/bonnie/[bonnie.stage]/gym_warmdown.webp"
        scene bonnie_gym_warmdown
        "Grabbing an exercise ball, Bonnie begins to slowly work out her body."
        if bonnie.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/5/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/5/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/6/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/6/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/7/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/7/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/8/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/8/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/9/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/9/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/10/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/10/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/11/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/11/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 12:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/12/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/12/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 13:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/13/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/13/gym_warmdown_top.webm" loop
            show movie with dissolve
        "You can see the recent weight gain is clearly impacting her ability to curl."
        "The extra bulk around her middle stopping her from being able to compact her abdomen as tightly."
        window hide
        pause
        stop movie
        image bonnie_gym_standing2 = "/bonnie/[bonnie.stage]/gym_standing2.webp"
        scene bonnie_gym_standing2
        "After a few more curls she stands up looking content."
        bonnie "Ah, that was good. My body feels looser already."
        bonnie "I need to get back again, but I'd love to work out together again if you want to."
        pc "Definitely. I always enjoy our workouts."
        bonnie "Great. See you around, [playername]."
        $ bonnie_gym_today = 1
        return


label bonnie_gym2:
    if bonniegymfirsttime == 1:
        image bonnie_gym_dumbel = "/bonnie/[bonnie.stage]/gym_dumbel.webp"
        scene bonnie_gym_dumbel
        "Is that Bonnie working out on the weights?"
        pc "Hey, Bonnie. I didn't know you worked out here?"
        image bonnie_gym_sitting = "/bonnie/[bonnie.stage]/gym_sitting.webp"
        scene bonnie_gym_sitting
        bonnie "Oh, hey, [playername]."
        bonnie "Yeah, I don't come here that often."
        pc "Well, would you like to work out together?"
        bonnie "Yeah, that would be nice."
        image bonnie_gym_standing = "/bonnie/[bonnie.stage]/gym_standing.webp"
        scene bonnie_gym_standing
        bonnie "I'm still a bit new to this, so it would be good to get some pointers if you have any?"
        pc "Sure, I'm happy to help. Although Trista would be better at giving advice if that's what you are after?"
        bonnie "True."
        bonnie "But between you and me, she can be a little intimidating."
        pc "Fair point."
        pc "Well, why don't you have another go and I’ll spot for you."
        image bonnie_gym_benchpress1 = "/bonnie/[bonnie.stage]/gym_benchpress1.webp"
        scene bonnie_gym_benchpress1
        "Standing behind the bench you watch Bonnie as she does a set of reps."
        "She doesn't have the same form as Katrine or Trista, but it is still good."
        image bonnie_gym_sitting2 = "/bonnie/[bonnie.stage]/gym_sitting2.webp"
        scene bonnie_gym_sitting2
        pc "You are pretty good, even if you doubt yourself."
        bonnie "That's nice of you to say."
        bonnie "I have never really been a gym person, so it's good to know that I'm not doing it totally wrong."
        bonnie "But why don't you show me how to do it?"
        "Moving over, she indicates for you to take the bench."
        image bonnie_gym_benchpress2 = "/bonnie/[bonnie.stage]/gym_benchpress2.webp"
        scene bonnie_gym_benchpress2
        bonnie "What do I do?"
        pc "It's easy, just stand behind the bar and be ready to support it if I struggle."
        bonnie "That's a lot of responsibility."
        pc "It will be fine, I’m still using low weights so I shouldn’t have any problems."
        "Bonnie spots you as you do a set of lifts."
        "Paying careful attention, she looks ready to jump in at any moment."
        call strengthup
        image bonnie_gym_standing = "/bonnie/[bonnie.stage]/gym_standing.webp"
        scene bonnie_gym_standing
        pc "Thanks."
        bonnie "No problem. I almost feel like a proper weight lifter now."
        bonnie "But I need to get back to the store."
        pc "Sure thing, maybe we can work out together another time?"
        bonnie "Definitely, it's more fun to do it with a friend."
        "Bonnie leaves you to carry on with the rest of your workout."
        $ bonnie_gym_today = 1
        $ bonniegymfirsttime = 0
        return

    elif bonnie.stage <= 4:
        image bonnie_gym_treadmill = "/bonnie/[bonnie.stage]/gym_treadmill.webp"
        scene bonnie_gym_treadmill
        "Is that Bonnie finishing up on the treadmill."
        pc "Hey, Bonnie. How are you?"
        bonnie "Hey there [playername]."
        bonnie "I'm doing well thanks, what about yourself?"
        pc "I'm good too thanks. Want to join me on the weights?"
        bonnie "Sure thing, I just finished up my walk."
        image bonnie_gym_benchpress1 = "/bonnie/[bonnie.stage]/gym_benchpress1.webp"
        scene bonnie_gym_benchpress1
        "Moving over to the weights you spot for her."
        "Making sure to pay attention you help guide the bar up and down for Bonnie."
        image bonnie_gym_sitting2 = "/bonnie/[bonnie.stage]/gym_sitting2.webp"
        scene bonnie_gym_sitting2
        bonnie "That was great, thank you."
        bonnie "Want me to spot you now?"
        pc "If you don't mind, that would be great."
        image bonnie_gym_benchpress2 = "/bonnie/[bonnie.stage]/gym_benchpress2.webp"
        scene bonnie_gym_benchpress2
        "Lying on the bench you complete a set of reps."
        "Bonnie keeps a careful and slightly nervous eye on you as you work out."
        call strengthup

        ###Next to bench###
        image bonnie_gym_standing = "/bonnie/[bonnie.stage]/gym_standing.webp"
        scene bonnie_gym_standing
        bonnie "You have really good form."
        pc "Thanks, although I'm sure Trista would still have some comments to improve it."
        bonnie "Well, it's always good to improve right."
        bonnie "Plus, it means you can pass them onto me."
        "She smiles at you for a moment before blushing slightly."
        bonnie "Well I better warm down and head back to the shop."
        image bonnie_gym_warmdown = "/bonnie/[bonnie.stage]/gym_warmdown.webp"
        scene bonnie_gym_warmdown
        "Grabbing an exercise ball, Bonnie begins to slowly work out her body."
        "Taking a quick break, you let yourself watch her warm down."
        if bonnie.stage == 1:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/1/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/1/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 2:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/2/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/2/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 3:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/3/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/3/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/4/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/4/gym_warmdown_top.webm" loop
            show movie with dissolve
        window hide
        pause
        stop movie
        image bonnie_gym_standing2 = "/bonnie/[bonnie.stage]/gym_standing2.webp"
        scene bonnie_gym_standing2
        "After a few more curls she stands up looking content."
        bonnie "Ah, that was good. Feels great to be a bit gentler on my muscles from time to time."
        bonnie "Thanks for the workout."
        pc "No problem, maybe we can work out together another time?"
        bonnie "Definitely, it's more fun to do it with a friend."
        "Bonnie leaves you to carry on with the rest of your workout."
        $ bonnie_gym_today = 1
        return

    elif bonnie.stage >= 5:
        image bonnie_gym_treadmill = "/bonnie/[bonnie.stage]/gym_treadmill.webp"
        scene bonnie_gym_treadmill
        "Is that Bonnie finishing up on the treadmill."
        pc "Hey, Bonnie. How are you?"
        bonnie "Hey there [playername]."
        bonnie "I'm doing well thanks, what about yourself?"
        pc "I'm good too, want to join me on the weights?"
        bonnie "Sure thing, I just finished up my walk."
        image bonnie_gym_benchpress1 = "/bonnie/[bonnie.stage]/gym_benchpress1.webp"
        scene bonnie_gym_benchpress1
        "Moving over to the weights you spot for her."
        "Making sure to pay attention to more than her straining gym clothes, you guide the bar up and down for Bonnie."
        image bonnie_gym_sitting2 = "/bonnie/[bonnie.stage]/gym_sitting2.webp"
        scene bonnie_gym_sitting2
        bonnie "That was great, thank you."
        bonnie "Want me to spot you now?"
        pc "Yeah sure."
        image bonnie_gym_benchpress2 = "/bonnie/[bonnie.stage]/gym_benchpress2.webp"
        scene bonnie_gym_benchpress2
        "Lying on the bench you complete a set of reps."
        "The sight of Bonnie's growing figure is more than enough motivation to push yourself."
        call strengthup

        ###Next to bench###
        image bonnie_gym_standing = "/bonnie/[bonnie.stage]/gym_standing.webp"
        scene bonnie_gym_standing
        bonnie "That was super quick, you must be getting stronger."
        pc "Thanks, between our workouts and the whisking I do for those chocolates, I’ll be using bigger weights in no time."
        bonnie "I can get you some heavier cooking equipment if you want me too."
        bonnie "Really make you work for them."
        pc "Thanks, but I think I'll stick to the gym for now."
        pc "Besides, I wouldn’t want to make any mistakes with the chocolates, would I?"
        "Giving you a knowing glance, Bonnie shakes her head."
        bonnie "Well, I think I am done here for today. Just got to warm down."
        pc "Okay, it was fun to work out together."
        bonnie "See you around [playername]."
        "Taking a break nearby you watch Bonnie warm down."
        image bonnie_gym_warmdown = "/bonnie/[bonnie.stage]/gym_warmdown.webp"
        scene bonnie_gym_warmdown
        "Grabbing an exercise ball, Bonnie begins to work out her body."
        if bonnie.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/5/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/5/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/6/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/6/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/7/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/7/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/8/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/8/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/9/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/9/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/10/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/10/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/11/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/11/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 12:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/12/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/12/gym_warmdown_top.webm" loop
            show movie with dissolve
        elif bonnie.stage == 13:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/13/gym_warmdown_side.webm" loop
            show movie with dissolve
            "Pulling herself up, you can see her body shifting and stretching out."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/13/gym_warmdown_top.webm" loop
            show movie with dissolve
        "Her bloated looking stomach is clearly causing her some issues as she tries to compress it."
        "Despite the extra challenge Bonnie finishes her warm down."
        window hide
        pause
        stop movie
        image bonnie_gym_standing2 = "/bonnie/[bonnie.stage]/gym_standing2.webp"
        scene bonnie_gym_standing2
        "After a few more curls she stands up looking content."
        "Giving you a wave, Bonnie leaves you to carry on with the rest of your workout."
        $ bonnie_gym_today = 1
        return

label rebecca_gym:
    if rebeccagymfirsttime == 1:
        image rebecca_gym_dumbel = "/rebecca/[rebecca.stage]/gym_dumbel.webp"
        scene rebecca_gym_dumbel
        "Is that Rebecca working out on the weights?"
        pc "Hey, Rebecca. Don't think I have seen you around before?"
        image rebecca_gym_sitting = "/rebecca/[rebecca.stage]/gym_sitting.webp"
        scene rebecca_gym_sitting
        rebecca "Hey, [playername]."
        rebecca "Yeah, it's my first time here."
        rebecca "Looks like I will be in town for longer than I thought."
        rebecca "So I figured I better find somewhere to work out."
        pc "Well, this is a great gym. Want to work out together?"
        rebecca "Sure. I don't know anyone else here."
        image rebecca_gym_running = "/rebecca/[rebecca.stage]/gym_running.webp"
        scene rebecca_gym_running
        "Moving over to the treadmill, you start working out together."
        "Rebecca slowly increases her pace over time as she pushes herself hard."
        "Unlike your other gym partners, it doesn't seem like she is one for idle chit-chat while you run."
        "Completing you run, you feel like your core muscles have gotten stronger."

        ###Next to treadmills###
        image rebecca_gym_standing = "/rebecca/[rebecca.stage]/gym_standing.webp"
        scene rebecca_gym_standing
        rebecca "That was a good workout."
        pc "Yeah, that was great."
        rebecca "Well, I have finished for today."
        pc "Okay. I guess I will see you around."
        "Rebecca leaves you to continue your workout alone."
        $ rebeccagymfirsttime = 1
        $ rebecca_gym_today = 1
        return

    else:
        image rebecca_gym_dumbel = "/rebecca/[rebecca.stage]/gym_dumbel.webp"
        scene rebecca_gym_dumbel
        "Is that Rebecca working out on the weights?"
        pc "Hey Rebecca, how are you doing?"
        image rebecca_gym_sitting = "/rebecca/[rebecca.stage]/gym_sitting.webp"
        scene rebecca_gym_sitting
        rebecca "Hey [playername]."
        rebecca "I'm good thanks, currently doing 40lb’s."
        rebecca "Just about to finish up if you want the bench?"
        pc "I thought I would check if you want to work out together?"
        rebecca "Sure, I don't know anyone else here."
        image rebecca_gym_running = "/rebecca/[rebecca.stage]/gym_running.webp"
        scene rebecca_gym_running
        "Moving over to the treadmill, you start working out together."
        "Rebecca slowly increases her pace over time as she pushes herself hard."
        "Unlike your other gym partners, it doesn't seem like she is one for idle chit-chat while you run."
        "Completing your run you feel like your core muscles have gotten stronger."

        ###Next to treadmills###
        image rebecca_gym_standing = "/rebecca/[rebecca.stage]/gym_standing.webp"
        scene rebecca_gym_standing
        rebecca "That was a good workout."
        pc "Yeah, that was great."
        rebecca "Well, I have finished for today."
        pc "Ok, I guess I'll see you around."
        "Rebbeca leaves you to continue your workout alone."
        $ rebecca_gym_today = 1
        return

label roxie_gym:
    image roxie_gym1 = "/roxie/[roxie.stage]/gym1.webp"
    scene roxie_gym1
    "Upon arriving at the gym, you see a familiar face."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/roxie/4/gym2.webm" loop
    show movie with dissolve
    "Is that Roxie working out on the weights?"
    pc "Hey Roxie, how are you doing?"
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/roxie/4/gym3.webm" loop
    show movie with dissolve
    roxie "Good, I keep getting a lot of attention every time I work out here though."
    pc "Sorry."
    stop movie
    image roxie_gym4 = "/roxie/[roxie.stage]/gym4.webp"
    scene roxie_gym4
    roxie "It’s okay, I don’t mind, I would be staring too."
    roxie "It’s obviously my big…eyes that get their attention."
    pc "Well you do have really pretty eyes."
    image roxie_gym6 = "/roxie/[roxie.stage]/gym6.webp"
    scene roxie_gym6
    roxie "True."
    roxie "Anyway I’m just trying to lift something heavier than the weights on my chest I carry around."
    pc "Looks like you might need something heavier then."
    image roxie_gym5 = "/roxie/[roxie.stage]/gym5.webp"
    scene roxie_gym5
    roxie "Very funny, they aren’t that heavy…not yet anyway."
    roxie "Would you care to spot me?"
    roxie "I want to try taking on more weight."
    pc "Sure."
    image roxie_gym7 = "/roxie/[roxie.stage]/gym7.webp"
    scene roxie_gym7
    "You spot Roxie for a while as she struggles but still manages to take on the extra weight."
    image roxie_gym8 = "/roxie/[roxie.stage]/gym8.webp"
    scene roxie_gym8
    roxie "Phew, pretty soon I’ll be lifting you and then after that maybe even one of the other test subjects."
    pc "I doubt that, they keep gaining and growing too fast."
    roxie "If we’re lucky."
    roxie "Anyway I think that is enough for now."
    roxie "I need to go eat back on all the calories I burned and then some."
    "Roxie then leaves."
    $ roxie_gym_today = 1
    return


label maya_gym1:
    if mayagymfirsttime == 1:
        image maya_gym_start = "/maya/[maya.stage]/gym_start.webp"
        scene maya_gym_start
        #Pc enters the gym. It seems that someone else is here
        maya "Hey [playername]! I didn’t know you went to this gym."
        pc "Hey Maya. Yeah it’s a nice little gym. Haven’t seen you here before."
        image maya_gym_talk = "/maya/[maya.stage]/gym_talk.webp"
        scene maya_gym_talk
        maya "I’ve been a member here for years. I like this gym since it’s never too busy. I don’t have to wait for equipment to open up."
        pc "Yeah that’s nice too. So what do you do when you're here?"
        maya "As a workout? Mostly arms, I need to make sure I can hold myself up when I’m on the pole."
        pc "Just arms, nothing else."
        maya "Pretty much I get a full body workout when I’m working."
        pc "That makes sense. So what are you doing today?"
        maya "I mainly lift weights but since you're here would mind spotting me while I do pull ups."
        pc "Would mind at all."
        maya "Great."
        image maya_gym_workout = "/maya/[maya.stage]/gym_workout.webp"
        scene maya_gym_workout
        "Maya heads over to the pull up bar and you begin to spot Maya as she does her pull ups."
        if maya.stage == 1:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/1/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/1/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 2:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/2/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/2/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 3:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/3/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/3/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/4/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/4/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/5/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/5/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/6/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/6/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/7/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/7/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/8/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/8/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/9/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/9/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/10/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/10/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/11/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/11/gym_animation_back.webm" loop
            show movie with dissolve
        "Even after more than twenty pull-ups, Maya is still keeping the same pace."
        window hide
        pause
        "After you reach the count of fourty she lets herself back to the ground."
        stop movie
        image maya_gym_end = "/maya/[maya.stage]/gym_end.webp"
        scene maya_gym_end
        maya "Phew, now that’s way better than just lifting weights."
        #Maya grabs a towel to wipe the sweat from her face.
        image maya_gym_talk2 = "/maya/[maya.stage]/gym_talk2.webp"
        scene maya_gym_talk2
        maya "Thanks for spotting me."
        pc "No problem, glad to help."
        maya "I better get going. It was nice running into you. Maybe you can spot me some other time."
        #Maya boops Pc on the nose, gathers her things and leaves. Pc finishes his workout and heads home
        $ mayagymfirsttime = 0
    else:
        #Pull ups
        image maya_gym_start = "/maya/[maya.stage]/gym_start.webp"
        scene maya_gym_start
        #Pc enter the gym. It seems that someone else is here.
        maya "Hey [playername]."
        pc "Hi Maya, what are you up to?"
        image maya_gym_talk = "/maya/[maya.stage]/gym_talk.webp"
        scene maya_gym_talk
        maya "Same old same old. Hey since you here mind spotting me again."
        pc "Love too."
        image maya_gym_workout = "/maya/[maya.stage]/gym_workout.webp"
        scene maya_gym_workout
        "Maya heads over to the pull up bar and you begin to spot Maya as she does her pull ups."
        if maya.stage == 1:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/1/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/1/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 2:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/2/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/2/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 3:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/3/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/3/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/4/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/4/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/5/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/5/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/6/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/6/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/7/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/7/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/8/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/8/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/9/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/9/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/10/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/10/gym_animation_back.webm" loop
            show movie with dissolve
        elif maya.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/11/gym_animation_front.webm" loop
            show movie with dissolve
            "You are surprised by her strength."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/maya/11/gym_animation_back.webm" loop
            show movie with dissolve
        "Even after more than twenty pull-ups, Maya is still keeping the same pace."
        window hide
        pause
        "After you reach the count of fourty she lets herself back to the ground."
        stop movie
        image maya_gym_end = "/maya/[maya.stage]/gym_end.webp"
        scene maya_gym_end
        maya "Phew, now that’s a workout. Thanks again for spotting me."
        #Maya grabs a towel to wipe the sweat from her face.
        image maya_gym_talk2 = "/maya/[maya.stage]/gym_talk2.webp"
        scene maya_gym_talk2
        pc "No problem, I really didn’t do much, but I did enjoy the view."
        maya "I bet you did. Oh shoot, I better get going. I’ll see you around."
        #Maya boops Pc on the nose, gathers her things and leaves. Pc finishes his workout and heads home
    $ maya_gym_today = 1
    $ strength += 1
    return

label maya_gym2:
    if mayagymfirsttime == 1:
        #Pc enters the gym. It seems that someone else is here
        maya "Hey [playername]! I didn’t know you went to this gym."
        pc "Hey Maya. Yeah it’s a nice little gym. Haven’t seen you here before."
        maya "I’ve been a member here for years. I like this gym since it’s never too busy. I don’t have to wait for equipment to open up."
        pc "Yeah that’s nice too. So what do you do when you're here?"
        maya "As a workout? Mostly arms, I need to make sure I can hold myself up when I’m on the pole."
        pc "Just arms, nothing else."
        maya "Pretty much I get a full body workout when I’m working."
        pc "That makes sense. So what are you doing today?"
        maya "I mainly lift weights but since you're here would mind spotting me while I do pull ups."
        pc "Would mind at all."
        maya "Great."
        "Maya heads over to the pull up bar and you begin to spot Maya as she does her pull ups."
        maya "Phew, now that’s way better than just lifting weights."
        #Maya grabs a towel to wipe the sweat from her face.
        maya "Thanks for spotting me."
        pc "No problem, glad to help."
        maya "I better get going. It was nice running into you. Maybe you can spot me some other time."
        #Maya boops Pc on the nose, gathers her things and leaves. Pc finishes his workout and heads home
        $ mayagymfirsttime = 0
    else:
        #Lifting weights
        #Pc enter the gym. It seems that someone else is here.
        maya "Hey [playername]."
        pc "Hi Maya, what are you up to?"
        maya "Same old same old. Think I’ll lift some weights today. Got to keep these arms strong. Want to join me?"
        pc "Sure."
        "You watch Maya try out different lifting techniques and try to copy her."
        maya "Phew, now that’s a workout. My arms are burning."
        #Maya grabs a towel to wipe the sweat from her face.
        pc "I feel it too. Was trying to keep up with you."
        maya "You did great. I’ve had years of working these puppies out."
        "Maya flexes her arms like she was in a strong man competition."
        maya "Thanks for keeping me company. Oh shoot, I didn't realize the time, I should get going. I’ll see you around."
        #Maya boops Pc on the nose, gathers her things and leaves. Pc finishes his workout and heads home
    $ maya_gym_today = 1
    return

label cayenne_gym:
    #(NOTE: The following repeatable event should occur at random when the player visits the gym after the Cayenne stage 2 event)
    if cayennestage6event == 1:
        #Version 1) (Available prior to Cayenne’s stage 6 event)
        image cayenne_gym_start = "/cayenne/[cayenne.stage]/gym_start.webp"
        scene cayenne_gym_start
        cayenne "Hey there! Good to see you. Since you’re here, would you mind keeping count for me while I do some squats?"
        pc "You can count on me."
        image cayenne_gym_squating = "/cayenne/[cayenne.stage]/gym_squating.webp"
        scene cayenne_gym_squating
        "Going through some stretches, Cayenne proceeds to start a session of squatting."
        if cayenne.stage == 2:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/2/gym_animation_front.webm" loop
            show movie with dissolve
            "At first you’re able to easily keep count. That is until your attention focuses elsewhere."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/2/gym_animation_back.webm" loop
            show movie with dissolve
        elif cayenne.stage == 3:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/3/gym_animation_front.webm" loop
            show movie with dissolve
            "At first you’re able to easily keep count. That is until your attention focuses elsewhere."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/3/gym_animation_back.webm" loop
            show movie with dissolve
        elif cayenne.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/4/gym_animation_front.webm" loop
            show movie with dissolve
            "At first you’re able to easily keep count. That is until your attention focuses elsewhere."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/4/gym_animation_back.webm" loop
            show movie with dissolve
        elif cayenne.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/5/gym_animation_front.webm" loop
            show movie with dissolve
            "At first you’re able to easily keep count. That is until your attention focuses elsewhere."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/5/gym_animation_back.webm" loop
            show movie with dissolve
        elif cayenne.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/6/gym_animation_front.webm" loop
            show movie with dissolve
            "At first you’re able to easily keep count. That is until your attention focuses elsewhere."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/6/gym_animation_back.webm" loop
            show movie with dissolve
        elif cayenne.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/7/gym_animation_front.webm" loop
            show movie with dissolve
            "At first you’re able to easily keep count. That is until your attention focuses elsewhere."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/7/gym_animation_back.webm" loop
            show movie with dissolve
        "Probably due to your tutoring sessions with her, she’s seemed to have gained some extra weight around her butt cheeks. This added heft is emphasized each time she goes down for a squat."
        window hide
        pause
        cayenne "Hey, you stopped counting. How many am I at?"
        pc "Er, you’re about half way there. Just keep going."
        cayenne "Will do!"
        stop movie
        image cayenne_gym_end = "/cayenne/[cayenne.stage]/gym_end.webp"
        scene cayenne_gym_end
        "Finishing off her last squat, Cayenne stands back up."
        cayenne "Whoo! That was a real work out. Okay, your turn. Let’s see what you can do."
        "In the hopes of giving just as much effort as Cayenne in your exercise routine, you push yourself through a set of squats."
        call strengthup
        cayenne "Good job. Let’s see if we can go one more next time."
        "Saying your goodbyes, Cayenne heads home."
        $ cayenne_gym_today = 1
        return

    elif cayennestage6event == 0 and cayennestage7event == 1:
        #Version 2) (Available between Cayenne’s stage 6 stage 7 event)
        #(NOTE: During this time, the likelihood of running into Cayenne at the gym should be higher to make it less likely for the player to miss the following.)
        image cayenne_gym_start = "/cayenne/[cayenne.stage]/gym_start.webp"
        scene cayenne_gym_start
        cayenne "Hey there! Good to see you. Since you’re here, would you mind keeping count for me while I do some squats? I’m going extra hard today to make up for all the weight I’ve put on."
        pc "You can count on me."
        image cayenne_gym_squat = "/cayenne/[cayenne.stage]/gym_squating.webp"
        scene cayenne_gym_squat
        "Going through some stretches, Cayenne proceeds to start a session of squatting."
        if cayenne.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/6/gym_animation_front.webm" loop
            show movie with dissolve
            "Overtime, you lose count as she seems to push herself harder than usual."
            "While her intentions are clear, you can’t help worrying if she’s going too far."
            "This is especially true considering the way her body trembles as she gets further along with her set."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/6/gym_animation_back.webm" loop
            show movie with dissolve
        elif cayenne.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/7/gym_animation_front.webm" loop
            show movie with dissolve
            "Overtime, you lose count as she seems to push herself harder than usual."
            "While her intentions are clear, you can’t help worrying if she’s going too far."
            "This is especially true considering the way her body trembles as she gets further along with her set."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/7/gym_animation_back.webm" loop
            show movie with dissolve
        "Staring at the extra weight around her backside, your concern increases with each rep."
        window hide
        pause
        cayenne "Hey, you stopped counting. How many am I at?"
        pc "Er, sorry. I lost track of which one you were on."
        cayenne "That’s alright. I can just start over."
        stop movie
        image cayenne_gym_end = "/cayenne/[cayenne.stage]/gym_end.webp"
        scene cayenne_gym_end
        "Finishing off her last squat, Cayenne stands back up. Though she tries to smile at you, you can’t help noticing the way her body shakes from the strenuous workout."
        cayenne "Alright, that was a good way to start. Now onto the next one."
        pc "Cayenne, please just take a break. I wouldn’t want to see you pass out."
        cayenne "I guess you’re right. Sorry, I got a little carried away with my weight loss goal. I’ll go have a seat. You go ahead and have your turn on the mat. I’ll keep count for you."
        image cayenne_gym_sit = "/cayenne/[cayenne.stage]/gym_sit.webp"
        scene cayenne_gym_sit
        "You perform your own series of squats, all the while keeping a close eye on Cayenne."
        call strengthup
        cayenne "Good work out there. Next time we’ll see if we can go even harder."
        "Saying your goodbyes, Cayenne heads home."
        $ cayenne_gym_today = 1
        return

    elif cayennestage7event == 0:
        #Version 3) (Available after Cayenne’s stage 7 event)
        image cayenne_gym_start = "/cayenne/[cayenne.stage]/gym_start.webp"
        scene cayenne_gym_start
        cayenne "Oh hey, perfect timing. I was about to start my squat session. Keep count for me."
        image cayenne_gym_squat = "/cayenne/[cayenne.stage]/gym_squating.webp"
        scene cayenne_gym_squat
        "Not even given a chance to speak up, you watch as Cayenne gets into position. Rather than argue, you take your place and begin to count."
        if cayenne.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/7/gym_animation_front.webm" loop
            show movie with dissolve
            "Cayenne’s enthusiasm for her exercise falls apart after only a few reps."
            "After a minute, her squat count is still in the single digits. While this makes your job easy, it also shows the strain the act is putting on her body."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/7/gym_animation_back.webm" loop
            show movie with dissolve
        elif cayenne.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/8/gym_animation_front.webm" loop
            show movie with dissolve
            "Cayenne’s enthusiasm for her exercise falls apart after only a few reps."
            "After a minute, her squat count is still in the single digits. While this makes your job easy, it also shows the strain the act is putting on her body."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/8/gym_animation_back.webm" loop
            show movie with dissolve
        elif cayenne.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/9/gym_animation_front.webm" loop
            show movie with dissolve
            "Cayenne’s enthusiasm for her exercise falls apart after only a few reps."
            "After a minute, her squat count is still in the single digits. While this makes your job easy, it also shows the strain the act is putting on her body."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/9/gym_animation_back.webm" loop
            show movie with dissolve
        elif cayenne.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/10/gym_animation_front.webm" loop
            show movie with dissolve
            "Cayenne’s enthusiasm for her exercise falls apart after only a few reps."
            "After a minute, her squat count is still in the single digits. While this makes your job easy, it also shows the strain the act is putting on her body."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/10/gym_animation_back.webm" loop
            show movie with dissolve
        elif cayenne.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/11/gym_animation_front.webm" loop
            show movie with dissolve
            "Cayenne’s enthusiasm for her exercise falls apart after only a few reps."
            "After a minute, her squat count is still in the single digits. While this makes your job easy, it also shows the strain the act is putting on her body."
            window hide
            pause
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/cayenne/11/gym_animation_back.webm" loop
            show movie with dissolve
        "You can see the main cause of her struggle with each successful squat sending waves through her thick rear."
        window hide
        pause
        "Each time she goes down, you hear a loud clap as her butt cheeks slap together. She barely manages to make it to the halfway point before she calls it quits."
        stop movie
        image cayenne_gym_sit2 = "/cayenne/[cayenne.stage]/gym_sit2.webp"
        scene cayenne_gym_sit2
        "Falling to the ground, Cayenne sits herself up and leans back to catch her breath."
        cayenne "Must not be my day. [playername], go grab me a drink. I think I’m done for now."
        image cayenne_gym_drink = "/cayenne/[cayenne.stage]/gym_drink.webp"
        scene cayenne_gym_drink
        "Though you never get around to doing your own set of squats, the combination of running off to get Cayenne’s drinks and helping her stand up serves as its own form of exercise."
        image cayenne_gym_end2 = "/cayenne/[cayenne.stage]/gym_end2.webp"
        scene cayenne_gym_end2
        cayenne "Good work. I’ll try to do better next time."
        "Saying your goodbyes, Cayenne heads home."
        $ cayenne_gym_today = 1
        return

label daisy_gym:
    if teacher.stage <= 8:
        #Version 1) Stages 1-8
        image daisy_gym_start = "/teacher/[teacher.stage]/0/gym_start.webp"
        scene daisy_gym_start
        teacher "This is a nice surprise. Always good to see a student willing to keep their physical body on par with their sharp mind. Would you like to join me on the treadmill?"
        image daisy_gym_running = "/teacher/[teacher.stage]/0/gym_running.webp"
        scene daisy_gym_running
        "Taking the treadmill next to Daisy, you turn it on and start to run."
        "Though you try to keep up, it doesn’t take long for her to rev up the speed to one of the higher settings."
        "Left to gasp and wheeze from your lack of stamina, you’re forced to get off early."
        image daisy_gym_runningback = "/teacher/[teacher.stage]/0/gym_runningback.webp"
        scene daisy_gym_runningback
        "While you take your time to sit down and catch your breath, Daisy shows no signs of slowing down."
        "Despite her constant feedings she seems perfectly capable of pushing her body to peak human performance."
        "Chugging down a bottle of water, you rejoin her in an effort to improve her leg muscles."
        call strengthup
        image daisy_gym_end = "/teacher/[teacher.stage]/0/gym_end.webp"
        scene daisy_gym_end
        teacher "Good hustle out there. Keep up the good work, but don’t forget you need to concentrate on your studies as well."
        pc "Yes, Ms. Tanwen."
        "Taking time to chat and enjoy a drink together, Daisy eventually leaves the gym."
        $ teacher_gym_today = 1
        return

    elif teacher.stage <= 12:
        #Version 2) Stage 9-12
        image daisy_gym_start = "/teacher/[teacher.stage]/0/gym_start.webp"
        scene daisy_gym_start
        teacher "Hello again. Good to see you continuing to perfect your body and mind. Would you like to join me on the treadmills again?"
        image daisy_gym_running = "/teacher/[teacher.stage]/0/gym_running.webp"
        scene daisy_gym_running
        "Taking the treadmill next to Daisy, you turn it on and start to run."
        "In spite of her constant binge eating sessions and desire to keep gaining weight, she seems more than capable of keeping pace."
        "Though she doesn’t nearly go as hard as she used to, she still lasts longer than you."
        image daisy_gym_runningback = "/teacher/[teacher.stage]/0/gym_runningback.webp"
        scene daisy_gym_runningback
        "Taking a moment to stop and catch your breath, you turn back to see Daisy still running."
        "The constant movement of her legs lets you gander at the pockets of fat clinging to her form jiggle."
        "It’s probably because of the extra pudge that she starts to slow down from sweat starting to drip across her form."
        "Not wanting to leave her alone for too long, you get back on your treadmill to finish your set."
        call strengthup
        image daisy_gym_end = "/teacher/[teacher.stage]/0/gym_end.webp"
        scene daisy_gym_end
        teacher "Whoo, that was a real workout. Going to have to keep that up if I still want to remain mobile when I get even fatter. Thanks again for joining me."
        "Taking time to chat and enjoy a drink together, Daisy eventually leaves the gym."
        $ teacher_gym_today = 1
        return

    elif teacher.stage <= 16:
        #Version 3) Stages 13-16
        image daisy_gym_start = "/teacher/[teacher.stage]/0/gym_start.webp"
        scene daisy_gym_start
        teacher "Hello [playername]. Care to join me for another session on the treadmills?"
        image daisy_gym_running = "/teacher/[teacher.stage]/0/gym_running.webp"
        scene daisy_gym_running
        "Taking the treadmill next to Daisy, you turn it on and start to run. Looking to the side, you watch as she quickly lowers the speed down to a light jog."
        "The reason is made apparent as you notice the way her body jiggles with every stomp of her legs."
        teacher "Would you mind getting me something to drink? I’m really worn out today."
        pc "Sure thing."
        image daisy_gym_runningback = "/teacher/[teacher.stage]/0/gym_runningback.webp"
        scene daisy_gym_runningback
        "Taking the time to stop and grab a bottle of water, you return to see that Daisy is already drenched in sweat from the exertion."
        "Even still, you can see that she’s trying her best to maintain a semblance of flexibility for her fat figure. Handing over the bottle, you get back on your treadmill to finish your set."
        call strengthup
        image daisy_gym_end = "/teacher/[teacher.stage]/0/gym_end.webp"
        scene daisy_gym_end
        teacher "I’m completely beat. I should probably just stick to dancing if I want to keep myself active. Less strenuous on my body without the risk of losing any weight. Thank you for your assistance."
        "Taking time to chat and enjoy a drink together, Daisy eventually leaves the gym."
        $ teacher_gym_today = 1
        return

    elif teacher.stage <= 20:
        #Version 4) Stages 17-20
        image daisy_gym_start = "/teacher/[teacher.stage]/0/gym_start.webp"
        scene daisy_gym_start
        pc "What are you doing here?"
        teacher "While I am far beyond the ability of standard exercise, it doesn’t mean I can’t enjoy the facilities here every now and then. Like say, sharing some time with my favorite student."
        image daisy_gym_running = "/teacher/[teacher.stage]/0/gym_running.webp"
        scene daisy_gym_running
        "Taking the treadmill next to Daisy, you turn it on and start to run. In direct contrast, she moves at a leisurely stroll as she seems content to just talk with you over the course of your workout."
        "You only stop once she asks for you to get her something to drink."
        image daisy_gym_runningback = "/teacher/[teacher.stage]/0/gym_runningback.webp"
        scene daisy_gym_runningback
        "When you return, you’re surprised to see sweat beading down her body."
        if teacher.stage == 17:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/teacher/17/0/gym_runningback_animation.webm" loop
            show movie with dissolve
        window hide
        pause
        "The low impact exercise still leaves her obese form to weather the brunt of the force brought upon by each shake of her flab with each step."
        "Trusting that Daisy knows not to push herself too far, you hand her the drink and get back on your treadmill to finish your session."
        call strengthup
        stop movie
        image daisy_gym_end = "/teacher/[teacher.stage]/0/gym_end.webp"
        scene daisy_gym_end
        teacher "Excellent work out there. While I might not be able to keep up with your pace, I still enjoyed our time together."
        "Taking time to chat and enjoy a drink together, Daisy eventually leaves the gym."
        $ teacher_gym_today = 1
        return

label lisa_gym1:
    if lisagymfirsttime == 1:
        image lisa_gym_lift = "/lisa/[lisa.stage]/gym_lift.webp"
        scene lisa_gym_lift
        "Is that Lisa working out on the weights?"
        pc "Hey Lisa, I didn't expect to see you here."
        image lisa_gym_talk = "/lisa/[lisa.stage]/gym_talk.webp"
        scene lisa_gym_talk
        lisa "[playername]!"
        lisa "Likewise, when did you start here?"
        pc "Pretty recently, but I have been in a few times."
        lisa "That's great, I used to come here with Marie. But with our shift pattern it can be hard to fit in time for a workout."
        pc "Yeah I can imagine."
        lisa "It has been easier since you started helping us out though."
        lisa "Since you are here, would you like to work out together?"
        pc "Yeah, that would be nice."
        image lisa_gym_start = "/lisa/[lisa.stage]/gym_start.webp"
        scene lisa_gym_start
        lisa "I'm a little rusty so no judgement alright."
        pc "I would never judge anyone, especially for working out to improve themselves."
        lisa "That's nice, to be honest it's why I come here instead of that big gym in the city."
        lisa "Too many judgemental people in there that just make me feel uncomfortable."
        pc "Yeah, this place seems to attract a much better crowd."
        lisa "True, I think Trista is a good judge of character."
        lisa "Anyway, I should really start before my muscles get too cold and I need to warm up again."
        image lisa_gym_workout = "/lisa/[lisa.stage]/gym_workout.webp"
        scene lisa_gym_workout
        "Bending over you watch as Lisa begins to do some push ups."
        if lisa.stage == 1:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/1/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 2:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/2/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 3:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/3/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/4/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/5/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/6/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/7/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/8/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/9/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/10/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/11/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 12:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/12/gym_workout_ass.webm" loop
            show movie with dissolve
        window hide
        pause
        "Her toned legs and ass rising and falling with ease as she finishes up her set."
        stop movie
        image lisa_gym_end = "/lisa/[lisa.stage]/gym_end.webp"
        scene lisa_gym_end
        lisa "So how was I, any recommendations?"
        pc "Looked good to me, seems like you know what you are doing."
        lisa "Thanks, always good to get a second opinion."
        lisa "It's been harder to be motivated working out by myself than when I was here with Marie or Amber."
        pc "No problem, I would be happy to work out together if you want to do it again."
        image lisa_gym_bye = "/lisa/[lisa.stage]/gym_bye.webp"
        scene lisa_gym_bye
        lisa "Definitely."
        lisa "But I had better head home, I need to have a shower before work."
        pc "They have showers here if you want to use one."
        lisa "That's ok, I don't really like public showers."
        pc "Sure thing, see you around Lisa."
        lisa "Bye [playername]."
        $ lisa_gym_today = 1
        $ lisagymfirsttime = 0
        return

    if lisa.stage <= 5:
        image lisa_gym_lift = "/lisa/[lisa.stage]/gym_lift.webp"
        scene lisa_gym_lift
        "Is that Lisa working out on the weights?"
        pc "Hey Lisa, how are you?"
        image lisa_gym_talk = "/lisa/[lisa.stage]/gym_talk.webp"
        scene lisa_gym_talk
        lisa "Hi [playername], pretty good actually."
        lisa "How about you?"
        pc "I’m good too."
        lisa "Perfect, fancy working out together?"
        pc "Sure thing."
        image lisa_gym_run = "/lisa/[lisa.stage]/gym_run.webp"
        scene lisa_gym_run
        "Moving over to the treadmill, you start chatting as you work out together."
        if lisa.stage >= 3:
            "Lisa runs slowly, her body becoming increasingly bouncy compared to how she looked the first time you ran into her."
            "Her once toned muscles clearly being affected by her recent gluttony."
        image lisa_gym_afterrun = "/lisa/[lisa.stage]/gym_afterrun.webp"
        scene lisa_gym_afterrun
        lisa "That was great, I’ll just do some push ups to finish."
        image lisa_gym_start = "/lisa/[lisa.stage]/gym_start.webp"
        scene lisa_gym_start
        lisa "Got to keep up the balance of cardio and muscle work."
        pc "Yeah, it's important to get a balanced workout."
        image lisa_gym_workout = "/lisa/[lisa.stage]/gym_workout.webp"
        scene lisa_gym_workout
        "Bending over you watch as Lisa begins to do some push ups."
        if lisa.stage == 1:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/1/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 2:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/2/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 3:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/3/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/4/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/5/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/6/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/7/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/8/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/9/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/10/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/11/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 12:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/12/gym_workout_ass.webm" loop
            show movie with dissolve
        window hide
        pause
        if lisa.stage >= 3:
            "Her growing ass rising and falling with ease as she finishes up her set."
            "Watching Lisa push her body, you are definitely starting to notice the impacts of all the extra food she was eating."
        else:
            "Her ass rising and falling with ease as she finishes up her set."
        stop movie
        image lisa_gym_end = "/lisa/[lisa.stage]/gym_end.webp"
        scene lisa_gym_end
        lisa "So how was I, any recommendations?"
        pc "Looked good to me, seems like you know what you are doing."
        lisa "Thanks, I really appreciate your company to keep me going."
        image lisa_gym_bye = "/lisa/[lisa.stage]/gym_bye.webp"
        scene lisa_gym_bye
        lisa "But I had better head home, see you later."
        pc "Bye Lisa."
        $ lisa_gym_today = 1
        return

    elif lisa.stage >= 6:
        image lisa_gym_lift = "/lisa/[lisa.stage]/gym_lift.webp"
        scene lisa_gym_lift
        "Is that Lisa working out on the weights?"
        pc "Hey Lisa."
        image lisa_gym_talk = "/lisa/[lisa.stage]/gym_talk.webp"
        scene lisa_gym_talk
        lisa "Hi [playername], how are you?"
        pc "I’m good thanks, how about you?"
        lisa "I'm ok, although it's been getting harder and harder to get to the gym these days."
        lisa "I just hope Marie won't be mad that I am still working out."
        pc "I don't think Marie could ever be mad at you, especially for just looking after yourself."
        lisa "Really?"
        lisa "Thank you, I think I needed to hear that."
        lisa "Fancy working out together?"
        pc "Sure thing."
        image lisa_gym_run = "/lisa/[lisa.stage]/gym_run.webp"
        scene lisa_gym_run
        "Moving over to the Treadmill, you start chatting as you work out together."
        "Next to you Lisa has been forced to change to a walk from her previous running pace."
        "Her expanding body was making it harder to run, judging from the jiggling you could see at her walking pace."
        "Lisa’s eating habits and continued feeding from you and Marie are really starting to have an impact on her body now."
        image lisa_gym_afterrun = "/lisa/[lisa.stage]/gym_afterrun.webp"
        scene lisa_gym_afterrun
        lisa "That was great, I’ll probably just do some push ups to finish."
        image lisa_gym_workout = "/lisa/[lisa.stage]/gym_workout.webp"
        scene lisa_gym_workout
        "Bending over you watch as Lisa begins to do some push ups."
        if lisa.stage == 1:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/1/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 2:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/2/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 3:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/3/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/4/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/5/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/6/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/7/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/8/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/9/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/10/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/11/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 12:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/12/gym_workout_ass.webm" loop
            show movie with dissolve
        window hide
        pause
        "Straining loudly, it clearly takes much more effort for her to push her giant body off the ground."
        "The once calm and collected Lisa now grunting and sweating with exertion after just a couple of push ups."
        stop movie
        image lisa_gym_end = "/lisa/[lisa.stage]/gym_end.webp"
        scene lisa_gym_end
        lisa "So how was I, any recommendations?"
        pc "Looked good to me, seems like you know what you are doing."
        lisa "Thanks."
        lisa "I really appreciate you helping me today."
        image lisa_gym_bye = "/lisa/[lisa.stage]/gym_bye.webp"
        scene lisa_gym_bye
        lisa "But I had better head home, see you later."
        pc "Bye Lisa."
        $ lisa_gym_today = 1
        return

label lisa_gym2:
    if lisagymfirsttime == 1:
        image lisa_gym_lift = "/lisa/[lisa.stage]/gym_lift.webp"
        scene lisa_gym_lift
        "Is that Lisa working out on the weights?"
        pc "Hey Lisa, I didn't expect to see you here."
        image lisa_gym_talk = "/lisa/[lisa.stage]/gym_talk.webp"
        scene lisa_gym_talk
        lisa "[playername]!"
        lisa "Likewise, when did you start here?"
        pc "Pretty recently, but I have been in a few times."
        lisa "That's great, I used to come here with Marie. But with our shift pattern it can be hard to fit in time for a workout."
        pc "Yeah I can imagine."
        lisa "It has been easier since you started helping us out though."
        lisa "Since you are here, would you like to work out together?"
        pc "Yeah, that would be nice."
        image lisa_gym_start = "/lisa/[lisa.stage]/gym_start.webp"
        scene lisa_gym_start
        lisa "I'm a little rusty so no judgement alright."
        pc "I would never judge anyone, especially for working out to improve themselves."
        lisa "That's nice, to be honest it's why I come here instead of that big gym in the city."
        lisa "Too many judgemental people in there that just make me feel uncomfortable."
        pc "Yeah, this place seems to attract a much better crowd."
        lisa "True, I think Trista is a good judge of character."
        lisa "Anyway, I should really start before my muscles get too cold and I need to warm up again."
        image lisa_gym_workout = "/lisa/[lisa.stage]/gym_workout.webp"
        scene lisa_gym_workout
        "Bending over you watch as Lisa begins to do some push ups."
        if lisa.stage == 1:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/1/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 2:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/2/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 3:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/3/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 4:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/4/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 5:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/5/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 6:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/6/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 7:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/7/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 8:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/8/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/9/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/10/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/11/gym_workout_ass.webm" loop
            show movie with dissolve
        elif lisa.stage == 12:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/lisa/12/gym_workout_ass.webm" loop
            show movie with dissolve
        window hide
        pause
        "Her toned legs and ass rising and falling with ease as she finishes up her set."
        stop movie
        image lisa_gym_end = "/lisa/[lisa.stage]/gym_end.webp"
        scene lisa_gym_end
        lisa "So how was I, any recommendations?"
        pc "Looked good to me, seems like you know what you are doing."
        lisa "Thanks, always good to get a second opinion."
        lisa "It's been harder to be motivated working out by myself than when I was here with Marie or Amber."
        pc "No problem, I would be happy to work out together if you want to do it again."
        image lisa_gym_bye = "/lisa/[lisa.stage]/gym_bye.webp"
        scene lisa_gym_bye
        lisa "Definitely."
        lisa "But I had better head home, I need to have a shower before work."
        pc "They have showers here if you want to use one."
        lisa "That's ok, I don't really like public showers."
        pc "Sure thing, see you around Lisa."
        lisa "Bye [playername]."
        $ lisagymfirsttime = 0
        $ lisa_gym_today = 1
        return

    if lisa.stage <= 6:
        image lisa_gym_run2 = "/lisa/[lisa.stage]/gym_run2.webp"
        scene lisa_gym_run2
        "Is that Lisa finishing up on the treadmill."
        pc "Hey Lisa, how are you?"
        image lisa_gym_talk2 = "/lisa/[lisa.stage]/gym_talk2.webp"
        scene lisa_gym_talk2
        lisa "Hey there [playername], fancy another workout?"
        pc "Definitely, want to work out on the weights?"
        lisa "Sounds good to me."
        image lisa_gym_benchpress = "/lisa/[lisa.stage]/gym_benchpress.webp"
        scene lisa_gym_benchpress
        "Moving over to the weights you spot for her."
        "Making sure to pay attention you help guide the bar up and down for Lisa."
        image lisa_gym_talk3 = "/lisa/[lisa.stage]/gym_talk3.webp"
        scene lisa_gym_talk3
        lisa "That was great, thank you."
        lisa "Want me to spot you now?"
        pc "If you don't mind, that would be great."
        image lisa_gym_benchpress2 = "/lisa/[lisa.stage]/gym_benchpress2.webp"
        scene lisa_gym_benchpress2
        "Lying on the bench you complete a set of reps."
        "Lisa seems much more comfortable spotting you than some of the others."
        call strengthup

        ###Next to bench###
        image lisa_gym_talk4 = "/lisa/[lisa.stage]/gym_talk4.webp"
        scene lisa_gym_talk4
        lisa "I didn’t expect you to lift that much so easily."
        pc "Thanks, I think."
        lisa "Sorry, I did mean it as a compliment."
        lisa "I’m just going to finish up with some stretches if you want to join?"
        pc "Yeah, that would be great."
        image lisa_gym_stretch1 = "/lisa/[lisa.stage]/gym_stretch1.webp"
        scene lisa_gym_stretch1
        "Stepping onto the mat’s Lisa goes through a series of positions, straining and pushing her muscles."
        image lisa_gym_stretch2 = "/lisa/[lisa.stage]/gym_stretch2.webp"
        scene lisa_gym_stretch2
        "Despite recent indulgences, it seems Lisa is still pretty flexible."
        image lisa_gym_bye2 = "/lisa/[lisa.stage]/gym_bye2.webp"
        scene lisa_gym_bye2
        lisa "That does it for me, see you around [playername]."
        pc "Thanks Lisa, see you soon."
        "Lisa leaves you to carry on with the rest of your workout."
        $ lisa_gym_today = 1
        return

    elif lisa.stage >= 7:
        image lisa_gym_run2 = "/lisa/[lisa.stage]/gym_run2.webp"
        scene lisa_gym_run2
        "Is that Lisa finishing up on the treadmill."
        pc "Hey Lisa, how are you?"
        image lisa_gym_talk2 = "/lisa/[lisa.stage]/gym_talk2.webp"
        scene lisa_gym_talk2
        lisa "Hey there [playername]. Fancy another workout?"
        pc "Definitely, I was going to start on the weights if that works for you?"
        lisa "Sounds good to me."
        image lisa_gym_benchpress = "/lisa/[lisa.stage]/gym_benchpress.webp"
        scene lisa_gym_benchpress
        "Moving over to the weights you spot for her."
        "Making sure to pay attention you help guide the bar up and down for Lisa."
        image lisa_gym_talk3 = "/lisa/[lisa.stage]/gym_talk3.webp"
        scene lisa_gym_talk3
        lisa "That was great, thank you."
        lisa "Want me to spot you now?"
        pc "If you don't mind, that would be great."
        image lisa_gym_benchpress2 = "/lisa/[lisa.stage]/gym_benchpress2.webp"
        scene lisa_gym_benchpress2
        "Lying on the bench you complete a set of reps."
        call strengthup

        ###Next to bench###
        image lisa_gym_talk4 = "/lisa/[lisa.stage]/gym_talk4.webp"
        scene lisa_gym_talk4
        lisa "Thanks for your help with that."
        lisa "I am going to finish up with some stretches if you want to join?"
        pc "Yeah, that would be great."
        image lisa_gym_stretch1 = "/lisa/[lisa.stage]/gym_stretch1.webp"
        scene lisa_gym_stretch1
        "Stepping onto the mat’s Lisa goes through a series of positions, straining and pushing her muscles."
        image lisa_gym_stretch2 = "/lisa/[lisa.stage]/gym_stretch2.webp"
        scene lisa_gym_stretch2
        "It's clearly getting increasingly difficult for her to reach the same positions with all the extra weight she has put on."
        image lisa_gym_stretch3 = "/lisa/[lisa.stage]/gym_stretch3.webp"
        scene lisa_gym_stretch3
        "Several of stretches now look almost impossible as layers of fat stop her from bending over as far as she used too."
        image lisa_gym_bye2 = "/lisa/[lisa.stage]/gym_bye2.webp"
        scene lisa_gym_bye2
        lisa "That does it for me, see you around [playername]."
        pc "Thanks Lisa, see you soon."
        "Lisa leaves you to carry on with the rest of your workout."
        $ lisa_gym_today = 1
        return





label hari_gym:
    #(NOTE: Hari’s gym scenes should become available after the stage 4 event)
    image hari_gym_start = "/hari/[hari.stage]/gym_start.webp"
    scene hari_gym_start
    pc "Hey, Hari!"
    hari "H-hello."
    pc "Here for another gymnastics session?"
    hari "Y-yes."
    pc "Mind if I join you?"
    hari "That would be…great."
    image hari_gym_stretch1 = "/hari/[hari.stage]/gym_stretch1.webp"
    scene hari_gym_stretch1
    "Lying down on the mat, Hari takes a deep breath before starting her routine."
    image hari_gym_stretch2 = "/hari/[hari.stage]/gym_stretch2.webp"
    scene hari_gym_stretch2
    "She starts by stretching out her limbs."
    image hari_gym_stretch3 = "/hari/[hari.stage]/gym_stretch3.webp"
    scene hari_gym_stretch3
    "Trying to copy her movements is difficult, but it comes with the benefit of increasing your own flexibility."
    image hari_gym_handstand1 = "/hari/[hari.stage]/gym_handstand1.webp"
    scene hari_gym_handstand1
    "Motivated by your presence and adrenaline, Hari proceeds to tumble across the mat."
    image hari_gym_handstand2 = "/hari/[hari.stage]/gym_handstand2.webp"
    scene hari_gym_handstand2
    "Motivated by your presence and adrenaline, Hari proceeds to tumble across the mat."
    image hari_gym_handstand3 = "/hari/[hari.stage]/gym_handstand3.webp"
    scene hari_gym_handstand3
    "After a few turns, she does a handstand that allows her to stretch out her limbs and leave you thoroughly impressed."
    image hari_gym_cartwheel = "/hari/[hari.stage]/gym_cartwheel.webp"
    scene hari_gym_cartwheel
    "After returning back to her feet, she seems to get ready for another move."
    if hari.stage == 3:
        $ renpy.movie_cutscene("/images/hari/3/gym_cartwheel_video.webm", stop_music=False)
    elif hari.stage == 4:
        $ renpy.movie_cutscene("/images/hari/4/gym_cartwheel_video.webm", stop_music=False)
    elif hari.stage == 5:
        $ renpy.movie_cutscene("/images/hari/5/gym_cartwheel_video.webm", stop_music=False)
    elif hari.stage == 6:
        $ renpy.movie_cutscene("/images/hari/6/gym_cartwheel_video.webm", stop_music=False)
    elif hari.stage == 7:
        $ renpy.movie_cutscene("/images/hari/7/gym_cartwheel_video.webm", stop_music=False)
    elif hari.stage == 8:
        $ renpy.movie_cutscene("/images/hari/8/gym_cartwheel_video.webm", stop_music=False)
    image hari_gym_cartwheel_end = "/hari/[hari.stage]/gym_cartwheel_end.webp"
    scene hari_gym_cartwheel_end
    pc "Incredible as always."
    image hari_gym_end = "/hari/[hari.stage]/gym_end.webp"
    scene hari_gym_end
    "A blush forms on Hari’s cheeks."
    hari "Thank you."
    "After cooling off your bodies with drinks and chatting for a bit, Hari leaves the gym."
    $ hari_gym_today = 1
    return

label marie_gym:
    image marie_gym_lifting = "/marie/[marie.stage]/gym_lifting.webp"
    scene marie_gym_lifting
    "Is that Marie working out on the weights?"
    pc "Hey, Marie. How are you doing?"
    image marie_gym_sitting = "/marie/[marie.stage]/gym_sitting.webp"
    scene marie_gym_sitting
    marie "Hey, [playername]. Good to see you here. I'm doing well, how are you?"
    pc "Good, I'm good too."
    image marie_gym_standing = "/marie/[marie.stage]/gym_standing.webp"
    scene marie_gym_standing
    marie "So, how about you count me doing side step squats?"
    pc "Sure, no problem."
    marie "I knew you wouldn't want to miss watching me jiggle."
    image marie_gym_animation = "/marie/[marie.stage]/gym_animation.webp"
    scene marie_gym_animation
    "Marie moves over to a spot to start her workout."
    if marie.stage == 1:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/1/gym_animation_front.webm" loop
        show movie with dissolve
        "Going from left to right, Marie makes sure to give her legs plenty of exercise."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/1/gym_animation_back.webm" loop
        show movie with dissolve
    elif marie.stage == 2:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/2/gym_animation_front.webm" loop
        show movie with dissolve
        "Going from left to right, Marie makes sure to give her legs plenty of exercise."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/2/gym_animation_back.webm" loop
        show movie with dissolve
    elif marie.stage == 3:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/3/gym_animation_front.webm" loop
        show movie with dissolve
        "Going from left to right, Marie makes sure to give her legs plenty of exercise."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/3/gym_animation_back.webm" loop
        show movie with dissolve
    elif marie.stage == 4:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/4/gym_animation_front.webm" loop
        show movie with dissolve
        "Going from left to right, Marie makes sure to give her legs plenty of exercise."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/4/gym_animation_back.webm" loop
        show movie with dissolve
    elif marie.stage == 5:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/5/gym_animation_front.webm" loop
        show movie with dissolve
        "Going from left to right, Marie makes sure to give her legs plenty of exercise."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/5/gym_animation_back.webm" loop
        show movie with dissolve
    elif marie.stage == 6:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/6/gym_animation_front.webm" loop
        show movie with dissolve
        "Going from left to right, Marie makes sure to give her legs plenty of exercise."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/6/gym_animation_back.webm" loop
        show movie with dissolve
    elif marie.stage == 7:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/7/gym_animation_front.webm" loop
        show movie with dissolve
        "Going from left to right, Marie makes sure to give her legs plenty of exercise."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/7/gym_animation_back.webm" loop
        show movie with dissolve
    elif marie.stage == 8:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/8/gym_animation_front.webm" loop
        show movie with dissolve
        "Going from left to right, Marie makes sure to give her legs plenty of exercise."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/8/gym_animation_back.webm" loop
        show movie with dissolve
    elif marie.stage == 9:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/9/gym_animation_front.webm" loop
        show movie with dissolve
        "Going from left to right, Marie makes sure to give her legs plenty of exercise."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/9/gym_animation_back.webm" loop
        show movie with dissolve
    elif marie.stage == 10:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/10/gym_animation_front.webm" loop
        show movie with dissolve
        "Going from left to right, Marie makes sure to give her legs plenty of exercise."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/10/gym_animation_back.webm" loop
        show movie with dissolve
    elif marie.stage == 11:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/11/gym_animation_front.webm" loop
        show movie with dissolve
        "Going from left to right, Marie makes sure to give her legs plenty of exercise."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/11/gym_animation_back.webm" loop
        show movie with dissolve
    "While counting, you walk around Marie to make sure she is performing the workout correctly."
    window hide
    pause
    stop movie
    image marie_gym_end = "/marie/[marie.stage]/gym_end.webp"
    scene marie_gym_end
    marie "I know it looks easy, but after a few dozen your legs really start to burn."
    marie "Thank you for counting. I'll see later."
    pc "Bye, Marie."
    $ marie_gym_today = 1
    return

label vicky_gym:
    "Upon arriving at the gym, you see a familiar face."
    #[Image: Vicky doing squats]
    "Is that Vicky doing squats?"
    pc "Hey Vicky, I wasn't expecting to see you here."
    vicky "Oh, hey [playername]. Yeah, I need to, like, stay a little fit, regardless of my...other goals."
    vicky "I mean, actually it's *because* of my other goals."
    pc "...cool, well do you wanna work out together?"
    #[Image: Vicky turning to look at you.]
    vicky "Actually, there's something you can help me with."
    pc "Sure, what do you need?"
    "She leads you over to the punching bags."
    #[Image: Player holding the punching bag in place as Vicky hits it.]
    "You've done this before, but unlike Trista, it seems Vicky doesn't care much that there's a person on the other side of the bag."
    pc "Ow, easy!"
    "You're pretty sure she hits even harder."
    #[Image: Vicky looking sweaty, giving the player a smug smile as she rests.]
    vicky "Well, that's my workout done for the day, see you later [playername]."
    pc "Yep, see ya."
    "Vicky leaves you to continue your workout."
    $ vicky_gym_today = 1
    return
