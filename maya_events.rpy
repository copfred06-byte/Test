label Maya_Poledance:
    #Velvet Shadows main floor
    if mayastage6event == 0:
        "You decide to go to The Curvy Corner."
        scene stripclub_entrance2
        play music "/music/stripclub.ogg" if_changed
        "You enter The Curvy Corner."
        scene stripclub2
    else:
        "You decide to go to Velvet Shadows."
        scene stripclub_entrance
        play music "/music/stripclub.ogg" if_changed
        "You enter Velvet Shadows."
        scene stripclub
    "Looking around the main room, you spot Maya."
    image maya_stripclub_crowd = "/maya/[maya.stage]/stripclub_crowd.webp"
    scene maya_stripclub_crowd
    pause
    "You decide to go over to her."
    image maya_stripclub_talk = "/maya/[maya.stage]/stripclub_talk.webp"
    scene maya_stripclub_talk
    maya "Hey [playername], what can I do for you? Did you come in for a private dance?"
    menu:
        "Private Dance (-20$)":
            if money <= 19:
                "You do not have enough money for a private dance."
                image maya_stripclub_talk2 = "/maya/[maya.stage]/stripclub_talk2.webp"
                scene maya_stripclub_talk2
                if maya.stage == 1:
                    maya "Perfect timing. I'm about to go on. Why don't you find a seat close to the stage?"
                elif maya.stage == 2 or maya.stage == 3 or maya.stage == 4:
                    maya "I'm just about to go on. Normally Tessa would be going on right now, but I've been covering her stage time while she's gone. Why don't you find a seat close to the stage?"
                elif maya.stage >= 5:
                    maya "Perfect timing, I'm just about to go on. Why don't you find a seat close to the stage?"
                "Maya leaves."
                scene stripclub_dancer
                "You find a seat next to the stage. Soon the music starts and Maya comes on to perform her stage routine."
                image maya_stripclub_poledance_start = "/maya/[maya.stage]/stripclub_poledance_start.webp"
                scene maya_stripclub_poledance_start
                window hide
                pause
                image maya_stripclub_poledance1 = "/maya/[maya.stage]/stripclub_poledance1.webp"
                scene maya_stripclub_poledance1
                pause
                image maya_stripclub_poledance2 = "/maya/[maya.stage]/stripclub_poledance2.webp"
                scene maya_stripclub_poledance2
                pause
                image maya_stripclub_poledance3 = "/maya/[maya.stage]/stripclub_poledance3.webp"
                scene maya_stripclub_poledance3
                pause
                image maya_stripclub_poledance4 = "/maya/[maya.stage]/stripclub_poledance4.webp"
                scene maya_stripclub_poledance4
                pause
                image maya_stripclub_poledance5 = "/maya/[maya.stage]/stripclub_poledance5.webp"
                scene maya_stripclub_poledance5
                pause
                image maya_stripclub_poledance6 = "/maya/[maya.stage]/stripclub_poledance6.webp"
                scene maya_stripclub_poledance6
                pause
                image maya_stripclub_poledance_end = "/maya/[maya.stage]/stripclub_poledance_end.webp"
                scene maya_stripclub_poledance_end
                "When Maya is done, you get up and head home."
                if mayastage6event == 0:
                    $ maya.weight += 1
                stop music fadeout 1.0
                $ daytime += 1
                jump freetime
            image maya_stripclub_talk3 = "/maya/[maya.stage]/stripclub_talk3.webp"
            scene maya_stripclub_talk3
            $ money -= 20
            if maya.stage == 1:
                maya "I see you're taking me up on my friendship discount. Smart boy. Right this way."
            elif maya.stage == 2 or maya.stage == 3 or maya.stage == 4:
                maya "That's great, I could use a break from the main floor."
            elif maya.stage >= 5:
                maya "That's great, I could use a break from the main floor. It's just been so busy."
            image maya_stripclub_follow = "/maya/[maya.stage]/stripclub_follow.webp"
            scene maya_stripclub_follow
            "Maya leads you to her private room."
            #Maya’s Private Room
            image maya_private_arrive = "/maya/[maya.stage]/private_arrive.webp"
            scene maya_private_arrive
            maya "You remember the rules?"
            pc "No touching."
            image maya_private_talk = "/maya/[maya.stage]/private_talk.webp"
            scene maya_private_talk
            maya "Good. Now sit back and enjoy the show."
            if mayadance == 0:
                image maya_private_dance = "/maya/[maya.stage]/private_dance.webp"
                scene maya_private_dance
                window hide
                pause
                if maya.stage == 1:
                    $ renpy.movie_cutscene("/images/maya/1/private_dance_video.webm", stop_music=False)
                elif maya.stage == 2:
                    $ renpy.movie_cutscene("/images/maya/2/private_dance_video.webm", stop_music=False)
                elif maya.stage == 3:
                    $ renpy.movie_cutscene("/images/maya/3/private_dance_video.webm", stop_music=False)
                elif maya.stage == 4:
                    $ renpy.movie_cutscene("/images/maya/4/private_dance_video.webm", stop_music=False)
                elif maya.stage == 5:
                    $ renpy.movie_cutscene("/images/maya/5/private_dance_video.webm", stop_music=False)
                elif maya.stage == 6:
                    $ renpy.movie_cutscene("/images/maya/6/private_dance_video.webm", stop_music=False)
                elif maya.stage == 7:
                    $ renpy.movie_cutscene("/images/maya/7/private_dance_video.webm", stop_music=False)
                elif maya.stage == 8:
                    $ renpy.movie_cutscene("/images/maya/8/private_dance_video.webm", stop_music=False)
                elif maya.stage == 9:
                    $ renpy.movie_cutscene("/images/maya/9/private_dance_video.webm", stop_music=False)
                elif maya.stage == 10:
                    $ renpy.movie_cutscene("/images/maya/10/private_dance_video.webm", stop_music=False)
                elif maya.stage == 11:
                    $ renpy.movie_cutscene("/images/maya/11/private_dance_video.webm", stop_music=False)
                image maya_private_dance2 = "/maya/[maya.stage]/private_dance2.webp"
                scene maya_private_dance2
                $ mayadance = 1
            elif mayadance == 1:
                image maya_private_dance2 = "/maya/[maya.stage]/private_dance2.webp"
                scene maya_private_dance2
                window hide
                pause
                if maya.stage == 1:
                    $ renpy.movie_cutscene("/images/maya/1/private_dance2_video.webm", stop_music=False)
                elif maya.stage == 2:
                    $ renpy.movie_cutscene("/images/maya/2/private_dance2_video.webm", stop_music=False)
                elif maya.stage == 3:
                    $ renpy.movie_cutscene("/images/maya/3/private_dance2_video.webm", stop_music=False)
                elif maya.stage == 4:
                    $ renpy.movie_cutscene("/images/maya/4/private_dance2_video.webm", stop_music=False)
                elif maya.stage == 5:
                    $ renpy.movie_cutscene("/images/maya/5/private_dance2_video.webm", stop_music=False)
                elif maya.stage == 6:
                    $ renpy.movie_cutscene("/images/maya/6/private_dance2_video.webm", stop_music=False)
                elif maya.stage == 7:
                    $ renpy.movie_cutscene("/images/maya/7/private_dance2_video.webm", stop_music=False)
                elif maya.stage == 8:
                    $ renpy.movie_cutscene("/images/maya/8/private_dance2_video.webm", stop_music=False)
                elif maya.stage == 9:
                    $ renpy.movie_cutscene("/images/maya/9/private_dance2_video.webm", stop_music=False)
                elif maya.stage == 10:
                    $ renpy.movie_cutscene("/images/maya/10/private_dance2_video.webm", stop_music=False)
                elif maya.stage == 11:
                    $ renpy.movie_cutscene("/images/maya/11/private_dance2_video.webm", stop_music=False)
                image maya_private_dance = "/maya/[maya.stage]/private_dance.webp"
                scene maya_private_dance
                $ mayadance = 0
            maya "Thank you for coming today."
            image maya_private_bye = "/maya/[maya.stage]/private_bye.webp"
            scene maya_private_bye
            "After saying goodbye, you go back home."
            if maya.stage >= 11 and mayaundressoption == 0:
                $ mayaundressoption = 1
                #Unlocks Maya Undress in the stats page.
                $ renpy.notify("Maya Undress option unlocked in stats screen.")
                window hide
                pause
            #Maya dances for Pc.
            #When she's done Pc goes home.
            if mayastage6event == 0:
                $ maya.weight += 2
            stop music fadeout 1.0
            $ daytime += 1
            jump freetime
        "Watch a stage dance.":
            image maya_stripclub_talk2 = "/maya/[maya.stage]/stripclub_talk2.webp"
            scene maya_stripclub_talk2
            if maya.stage == 1:
                maya "Perfect timing. I'm about to go on. Why don't you find a seat close to the stage?"
            else:
                maya "I'm just about to go on. Normally Tessa would be going on right now, but I've been covering her stage time while she's gone. Why don't you find a seat close to the stage?"
            "Maya leaves."
            scene stripclub_dancer
            "You find a seat next to the stage. Soon the music starts and Maya comes on to perform her stage routine."
            image maya_stripclub_poledance_start = "/maya/[maya.stage]/stripclub_poledance_start.webp"
            scene maya_stripclub_poledance_start
            window hide
            pause
            image maya_stripclub_poledance1 = "/maya/[maya.stage]/stripclub_poledance1.webp"
            scene maya_stripclub_poledance1
            pause
            image maya_stripclub_poledance2 = "/maya/[maya.stage]/stripclub_poledance2.webp"
            scene maya_stripclub_poledance2
            pause
            image maya_stripclub_poledance3 = "/maya/[maya.stage]/stripclub_poledance3.webp"
            scene maya_stripclub_poledance3
            pause
            image maya_stripclub_poledance4 = "/maya/[maya.stage]/stripclub_poledance4.webp"
            scene maya_stripclub_poledance4
            pause
            image maya_stripclub_poledance5 = "/maya/[maya.stage]/stripclub_poledance5.webp"
            scene maya_stripclub_poledance5
            pause
            image maya_stripclub_poledance6 = "/maya/[maya.stage]/stripclub_poledance6.webp"
            scene maya_stripclub_poledance6
            pause
            image maya_stripclub_poledance_end = "/maya/[maya.stage]/stripclub_poledance_end.webp"
            scene maya_stripclub_poledance_end
            "When Maya is done, you get up and head home."
            if mayastage6event == 0:
                $ maya.weight += 1
            stop music fadeout 1.0
            $ daytime += 1
            jump freetime

label Maya_Stage_1_Event_1:
    "You receive a message from Amber."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Amber', dialogue=dialogue_one)
    $ msg ("Hey [playername], is there any way you could come into work today? We are really busy here and could use the help.", who=1)
    pause
    $ msg ("Sure thing. I'll be there as soon as I can.")
    pause
    $ msg ("You're a lifesaver!", who=1)
    pause
    $ hide_messenger()

    image amber_workattire_counter_eventmaya = "/amber/2/workattire_counter.webp"
    scene amber_workattire_counter_eventmaya
    play music "/music/bunny_bites.ogg" if_changed
    amber "Thank you for coming in on such short notice."
    "You make yourself ready and start working."
    if recollection == False:
        $ amber_work_today = 1
        $ lisa_work_today = 1
        $ marie_work_today = 1
        call work_randomizer from _call_work_randomizer_22
        call work_randomizer from _call_work_randomizer_23

    #Bunny Bites
    #Pc works their shift at Bunny Bites. At the end of the day, an exhausted Amber approaches the Pc.
    image amber_afterwork_sitdown3_eventmaya = "/amber/2/afterwork_sitdown3.webp"
    scene amber_afterwork_sitdown3_eventmaya
    amber "What a crazy day. That's the busiest we have been in a long time. Thanks for helping out."
    image amber_afterwork_sitdown1_eventmaya = "/amber/2/afterwork_sitdown1.webp"
    scene amber_afterwork_sitdown1_eventmaya
    pc "No problem, glad to help. Extra cash is always a welcome bonus."
    amber "So, do you have any plans for tonight?"
    pc "Not really. I had nothing on the agenda until you called."
    amber "Would you like to go have another drink with me tonight then?"
    pc "I would love to!"
    amber "Great! Oh shoot I just remembered I need to get home, but you can still go and have some fun, if you know what I mean." 
    amber "Maybe you'll meet my friend there."
    pc "You know what, I think I will check it out. I've never had a lap dance before."
    "Amber smiles and the two of you finish closing up the place."
    stop music fadeout 1.0

    scene stripclub_entrance
    play music "/music/stripclub.ogg" if_changed
    "Oh wow they seem pretty busy tonight."
    image maya_stage_1_event_1 = "/maya/events/stage1/1.webp"
    scene maya_stage_1_event_1
    #Pc sees the bar
    "Maybe I should get a drink first."
    #On his way to the bar, the Pc runs into someone
    image maya_stage_1_event_2 = "/maya/events/stage1/2.webp"
    scene maya_stage_1_event_2
    bartender "Excuse me."
    pc "Oh, I'm sorry."
    image maya_stage_1_event_3 = "/maya/events/stage1/3.webp"
    scene maya_stage_1_event_3
    "You are a little frazzled by the waitress."
    image maya_stage_1_event_4 = "/maya/events/stage1/4.webp"
    scene maya_stage_1_event_4
    "I don't know where to go or what to do."
    image maya_stage_1_event_5 = "/maya/events/stage1/5.webp"
    scene maya_stage_1_event_5
    "You see a woman with black bunny ears looking in your direction. She starts walking over to you."
    image maya_stage_1_event_6 = "/maya/events/stage1/6.webp"
    scene maya_stage_1_event_6
    "Oh no, what do I do? I don't even know what to say."
    $ unknownname = 'Lady with bunny ears'
    #The strip club dancer comes up to the Pc
    image maya_stage_1_event_7 = "/maya/events/stage1/7.webp"
    scene maya_stage_1_event_7
    unknown "Hi. I don't think I've ever seen you in here before. What's your name?"
    pc "[playername]."
    unknown "Is this your first time here?"
    pc "I've been here to have a few drinks with a friend, but this is my first time alone. Thought I'd see what else this place has."
    $ unknownname = 'Old man'
    image maya_stage_1_event_8 = "/maya/events/stage1/8.webp"
    scene maya_stage_1_event_8
    maya "Oh really, first-timers are my favorite. I'm Maya, and welcome to Velvet Shadows. How can I make your night any better?"
    pc "I'm… not… sure."
    maya "A first-timer and a shy one too. You keep getting better."
    #Maya touches Pc's shoulder and subtly brushes against him.
    maya "Well, you know about the bar."
    maya "You can always go over there and get a drink and find a seat by the stage, or my personal favorite, let me take you to my private room for a personal dance—for a fee, of course."
    image maya_stage_1_event_9 = "/maya/events/stage1/9.webp"
    scene maya_stage_1_event_9
    "Maya playfully bops you on the nose."
    maya "So, which one interests you the most?"
    pc "Um… I think I'll …. I choose…"
    image maya_stage_1_event_10 = "/maya/events/stage1/10.webp"
    scene maya_stage_1_event_10
    maya "It's so cute how shy you are. Let's get to know each other a little more to break the tension, maybe that will help you decide."
    maya "We've already introduced ourselves, so I'd like to know a little more about you. Do you go to the university here? Do you have a job? What's your favorite position?"
    pc "ahh… position?"
    image maya_stage_1_event_11 = "/maya/events/stage1/11.webp"
    scene maya_stage_1_event_11
    maya "I was just joking. I was trying to be funny."
    pc "Oh… of course, haha. But for what I'm currently doing, I'm taking classes at the university and just finished my day at work down the road."
    image maya_stage_1_event_12 = "/maya/events/stage1/12.webp"
    scene maya_stage_1_event_12
    maya "Just down the road from here. Where do you work?"
    pc "I work at…"
    image maya_stage_1_event_13 = "/maya/events/stage1/13.webp"
    scene maya_stage_1_event_13
    unknown "Uh-hm."
    image maya_stage_1_event_14 = "/maya/events/stage1/14.webp"
    scene maya_stage_1_event_14
    "An old man appears behind Maya. She looks caught doing something she shouldn't."
    maya "Oh, Mr. Vanthorne. I didn't see you there; I was just chatting with..."
    $ unknownname = 'Unknown'
    image maya_stage_1_event_15 = "/maya/events/stage1/15.webp"
    scene maya_stage_1_event_15
    vanthorne "Oh really. What I see you just standing around chitchatting and not doing your job."
    maya "Well, it's his first time…"
    image maya_stage_1_event_16 = "/maya/events/stage1/16.webp"
    scene maya_stage_1_event_16
    vanthorne "I don't care whose first time it is. There are plenty of other customers you could be attending to, like over there."
    image maya_stage_1_event_17 = "/maya/events/stage1/17.webp"
    scene maya_stage_1_event_17
    "Mr. Vanthorne points over to a chair where a man is sitting holding a beer, he sees them and pats his lap."
    image maya_stage_1_event_18 = "/maya/events/stage1/18.webp"
    scene maya_stage_1_event_18
    window hide
    pause
    image maya_stage_1_event_17 = "/maya/events/stage1/17.webp"
    scene maya_stage_1_event_17
    vanthorne "That man has been sitting there for the last twenty minutes, and none of you girls have even gotten close to him. He's one of our best customers."
    image maya_stage_1_event_19 = "/maya/events/stage1/19.webp"
    scene maya_stage_1_event_19
    "Maya quickly looks back at you, her eyes screaming for help."
    maya "Umm, I'm sorry Mr. Vanthorne, but right before you got here, this gentleman asked for a private dance from me."
    #Mr. Vanthorne looks at the Pc.
    image maya_stage_1_event_20 = "/maya/events/stage1/20.webp"
    scene maya_stage_1_event_20
    vanthorne "Is that so?"
    "You look over at Maya."
    image maya_stage_1_event_21 = "/maya/events/stage1/21.webp"
    scene maya_stage_1_event_21
    "Her eyes seem to be pleading that you say the right thing."
    pc "Oh, of course. I'm sorry for the confusion. I just asked for a private dance right before you came up to us."
    image maya_stage_1_event_22 = "/maya/events/stage1/22.webp"
    scene maya_stage_1_event_22
    "Maya looks relieved by your answer."
    maya "Well, we better get going. Like you always say, time is money."
    image maya_stage_1_event_23 = "/maya/events/stage1/23.webp"
    scene maya_stage_1_event_23
    "Maya grabs your hand and leads you away."

    #Maya private room
    image maya_stage_1_event_24 = "/maya/events/stage1/24.webp"
    scene maya_stage_1_event_24
    pc "What was that all about?"
    maya "I'm so sorry. I didn't mean to force you into anything."
    pc "No, it's fine. I was probably going to ask you for a private dance anyway."
    image maya_stage_1_event_25 = "/maya/events/stage1/25.webp"
    scene maya_stage_1_event_25
    maya "Oh good, I'm glad to hear that. That makes me feel better."
    pc "What I mean is, who was that guy? He seemed pretty rude."
    image maya_stage_1_event_26 = "/maya/events/stage1/26.webp"
    scene maya_stage_1_event_26
    maya "Mr. Vanthorne? Oh, he's the owner of the Velvet Shadows."
    pc "Really! He's the owner, and he talks to you that way."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/maya/events/stage1/vid1.webm" loop
    show movie with dissolve
    maya "Well, to be honest, He talks to everyone that way. There's not much we can do about it."
    pc "Has he always been that way?"
    maya "Ever since he bought this place."
    maya "A little over a year ago. When he bought the Velvet Shadows, he's changed quite a few rules around here, not all for the best, but anyways, this is stuff you don’t need to worry yourself about."
    stop movie
    image maya_stage_1_event_27 = "/maya/events/stage1/27.webp"
    scene maya_stage_1_event_27
    maya "Where did we leave off? Oh yeah, you were about to tell me where you work."
    pc "That's right. I recently started working at Bunny Bites just down the road."
    image maya_stage_1_event_28 = "/maya/events/stage1/28.webp"
    scene maya_stage_1_event_28
    maya "Really? I used to go there all the time. Does Amber still work there?"
    pc "She's the one that told me about this place."
    #Maya smiles at the Pc
    image maya_stage_1_event_29 = "/maya/events/stage1/29.webp"
    scene maya_stage_1_event_29
    maya "Amber and I used to be good friends."
    pc "Used to be? What happened to you two?"
    image maya_stage_1_event_30 = "/maya/events/stage1/30.webp"
    scene maya_stage_1_event_30
    maya "We didn't have a falling out or anything like that. Once Mr. Vanthorne bought the place, he became stringent about what we eat, so I stopped going to Bunny Bites."
    maya "Now that I think about it, I really miss seeing her."
    pc "I'm sure Amber misses seeing you too. You should come by and visit one of these days, and you two can catch up."
    image maya_stage_1_event_31 = "/maya/events/stage1/31.webp"
    scene maya_stage_1_event_31
    maya "I'd like to, but I don't know."
    pc "I also make a pretty good burger."
    image maya_stage_1_event_32 = "/maya/events/stage1/32.webp"
    scene maya_stage_1_event_32
    maya "A burger! I haven't had one of those in so long."
    #Maya stands there, lost in thought.
    image maya_stage_1_event_33 = "/maya/events/stage1/33.webp"
    scene maya_stage_1_event_33
    maya "Let's do this. Since I feel bad for dragging you in here, I'll give you your first dance on the house."
    maya "In exchange for one of your burgers when I come by Bunny Bites. I get to see an old friend and get a meal out of it. What do you say?"
    pc "Deal."
    # Maya smiles at the Pc
    image maya_stage_1_event_34 = "/maya/events/stage1/34.webp"
    scene maya_stage_1_event_34
    maya "Let's get the first part of the deal done."
    pc "So, what do I do?"
    # Maya laughs
    image maya_stage_1_event_35 = "/maya/events/stage1/35.webp"
    scene maya_stage_1_event_35
    maya "You're not lying about this being your first time."
    pc "Nope, that was the truth."
    maya "Well, first things first, go sit on the bed over there."
    #Maya leads Pc to a chair in the room
    image maya_stage_1_event_36 = "/maya/events/stage1/36.webp"
    scene maya_stage_1_event_36
    maya "Next, and this is very important, keep your hands to yourself. Not that I don't trust you, but that's the rule. I can touch you, but you don't touch me."
    pc "No touching. I think I got it. Then what?"
    image maya_stage_1_event_37 = "/maya/events/stage1/37.webp"
    scene maya_stage_1_event_37
    maya "That all depends on how much of a good boy you've been."

    # Maya turns on the music and starts dancing
    image maya_stage_1_event_dancestart = "/maya/events/stage1/dancestart.webp"
    scene maya_stage_1_event_dancestart
    window hide
    pause
    $ renpy.movie_cutscene("/images/maya/events/stage1/dance.webm", stop_music=False)
    image maya_stage_1_event_danceend = "/maya/events/stage1/danceend.webp"
    scene maya_stage_1_event_danceend
    pause

    image maya_stage_1_event_38 = "/maya/events/stage1/38.webp"
    scene maya_stage_1_event_38
    maya "So, how was it?"
    pc "It was great."
    maya "I'm glad you liked it. Well, we better get going. Don't want Mr. Vanthorne upset if I spend too much time with just one customer."
    #Maya leads the Pc to the door.
    image maya_stage_1_event_39 = "/maya/events/stage1/39.webp"
    scene maya_stage_1_event_39
    maya "I hope your burger is as good as you say it is."
    pc "I'll make sure it is."
    image maya_stage_1_event_40 = "/maya/events/stage1/40.webp"
    scene maya_stage_1_event_40
    maya "I'm looking forward to it. I'll see you soon."
    if maya_stats_visible == 0:
        $ maya_stats_visible = 1
        "Maya's stats are now visible."
    "You leave Velvet Shadows and return home"
    stop music fadeout 1.0
    if recollection == False:
        $ mayadance = 1
        $ daytime += 2
        $ phonecall = 1
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
    $ mayastage1event = 0
    return


label Maya_Stage_1_Event_2:
    "You receive a message from Amber."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Amber', dialogue=dialogue_one)
    $ msg ("Hey [playername], hate to bother you again but Lisa isn’t feeling the greatest. Are you able to come in today and cover the rest of her shift?", who=1)
    pause
    $ msg ("Of course I can. I’ll be there shortly.")
    pause
    $ msg ("I’m sure Lisa will be really grateful.", who=1)
    pause
    $ hide_messenger()

    image lisa_standing_on_chair_workattire = "/lisa/[lisa.stage]/standing_on_chair_workattire.webp"
    scene lisa_standing_on_chair_workattire
    play music "/music/bunny_bites.ogg" if_changed
    lisa "Thank you so much for covering the rest of my shift."
    pc "No problem. Hope you feel better."
    if recollection == False:
        $ amber_work_today = 1
        $ lisa_work_today = 1
        $ marie_work_today = 1
        call work_randomizer from _call_work_randomizer_24
    #Pc helps out a few customers. At the end of his shift, Maya walks in and smiles when she sees the Pc

    image cafe_maya_talk_event1 = "/maya/1/cafe_talk.webp"
    scene cafe_maya_talk_event1
    maya "Long time no see."
    pc "You made it."
    image cafe_maya_talk2_event1 = "/maya/1/cafe_talk2.webp"
    scene cafe_maya_talk2_event1
    maya "Did you think I would pass up on a free meal?"
    pc "No, I was..."
    image maya_stage_1_event_41 = "/maya/events/stage1/41.webp"
    scene maya_stage_1_event_41
    amber "Oh My God!!!! Maya, is that you?"
    #Amber runs over and gives Maya a big hug.
    image maya_stage_1_event_42 = "/maya/events/stage1/42.webp"
    scene maya_stage_1_event_42
    maya "I’m glad to see you too."
    image maya_stage_1_event_43 = "/maya/events/stage1/43.webp"
    scene maya_stage_1_event_43
    amber "Look at you. You look amazing. How long has it been?"
    maya "Too long."
    amber "I can’t get over how little you look."
    #amber turns to the Pc
    image maya_stage_1_event_44 = "/maya/events/stage1/44.webp"
    scene maya_stage_1_event_44
    amber "Doesn’t she look amazing? You should have seen her over a year ago, she was…"
    maya "Amber, calm down."
    #Maya laughs
    image maya_stage_1_event_45 = "/maya/events/stage1/45.webp"
    scene maya_stage_1_event_45
    maya "He doesn’t need to know my life’s story."
    amber "Oh sorry, I’m just so excited to see you again. What brings you back here?"
    maya "To tell you the truth, [playername]."
    amber "How do you know him?"
    pc "Remember the other day you told me to check out Velvet Shadows. I ran into Maya at the club, and we started talking."
    #Amber looks slyly at Maya
    image maya_stage_1_event_46 = "/maya/events/stage1/46.webp"
    scene maya_stage_1_event_46
    amber "Oh, of course. So, you guys must have hit it off. Yeah."
    maya "No, nothing like that. We kinda just stumbled into each other and made a little deal."
    #Amber looks confused
    image maya_stage_1_event_47 = "/maya/events/stage1/47.webp"
    scene maya_stage_1_event_47
    amber "A deal?"
    maya "He helped me out, so I gave him a free dance in exchange for a free meal."
    image maya_stage_1_event_48 = "/maya/events/stage1/48.webp"
    scene maya_stage_1_event_48
    amber "A dance for a free meal. I don’t care what that’s about; I’m just so happy to see you."
    amber "Oh shoot, I forgot I have a few burgers cooking in the back. I better get back there and make sure they're not burnt. You better not leave without saying goodbye."
    maya "I won’t."

    #Amber heads back to the kitchen
    image maya_stage_1_event_49 = "/maya/events/stage1/49.webp"
    scene maya_stage_1_event_49
    pc "Are you glad you came by?"
    maya "Amber is something else. Anyways, I’m starving, so what can that dance I gave you get me."
    pc "How does a burger and some fries sound?"
    image maya_stage_1_event_50 = "/maya/events/stage1/50.webp"
    scene maya_stage_1_event_50
    maya "That sounds perfect."
    pc "Find a seat, and I’ll bring your food out shortly."
    #Pc brings out maya’s food
    image maya_stage_1_event_51 = "/maya/events/stage1/51.webp"
    scene maya_stage_1_event_51
    pc "Here you go."
    maya "Oh wow, that’s a lot of food."
    pc "Is that okay?"
    image maya_stage_1_event_52 = "/maya/events/stage1/52.webp"
    scene maya_stage_1_event_52
    maya "Oh yeah, I’ve been thinking about this ever since you left that day. I just hope I can finish it all. It looks so good."
    pc "I hope you enjoy."
    "You leave Maya to eat her food."
    image maya_stage_1_event_53 = "/maya/events/stage1/53.webp"
    scene maya_stage_1_event_53
    "Later, after finishing your shift, you notice Maya again. She’s rubbing her stomach but has a worried look on her face."
    pc "Was everything okay?"
    image maya_stage_1_event_54 = "/maya/events/stage1/54.webp"
    scene maya_stage_1_event_54
    "Maya gets startled like she was deeply thinking about something."
    maya "Everything was great. You weren’t lying about how good your burger was. In fact, I think you undersold it."
    pc "I was just asking since you looked unhappy."
    image maya_stage_1_event_55 = "/maya/events/stage1/55.webp"
    scene maya_stage_1_event_55
    maya "Oh, I was just thinking to myself, that's all. Thank you again for the meal."
    pc "No problem. I’m glad you enjoyed it. Don’t forget to say goodbye to Amber."
    image maya_stage_1_event_56 = "/maya/events/stage1/56.webp"
    scene maya_stage_1_event_56
    maya "She wouldn’t let me leave without saying goodbye if I wanted to. Thanks again for everything."
    maya "Let's exchange numbers."
    "You give her your phone number, and she gives you hers."
    maya "Come by the club whenever you like, I’m there most days. I’ll even give you the friend's discount for the private dances."
    pc "I think I will, as long as you don’t stay a stranger and never come back again for over a year."
    image maya_stage_1_event_57 = "/maya/events/stage1/57.webp"
    scene maya_stage_1_event_57
    maya "I don’t think Amber will ever let me do that again, and besides, I’ll have to come back for another burger, it was so good."
    "You finish your shift and go home."
    if recollection == False:
        $ maya.weight += 1.5
        $ daytime += 1
        $ phonecall = 1
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
    stop music fadeout 1.0
    $ mayastage1event2 = 0
    #Pc goes home

    return


label Maya_Stage_1_Event_3:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Maya', dialogue=dialogue_one)
    $ msg ("If you're not doing anything today, you should stop by the club.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("I think I will. See you soon.")
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright. Another time then.", who=1)
            pause
            $ hide_messenger()
            return


    #Velvet Shadows Main Room
    image maya_stage_1_event_58 = "/maya/events/stage1/58.webp"
    scene maya_stage_1_event_58
    play music "/music/stripclub.ogg" if_changed
    "You enter the club and start to look for Maya."
    image maya_stage_1_event_59 = "/maya/events/stage1/59.webp"
    scene maya_stage_1_event_59
    "You spot her in a group of other woman."
    image maya_stage_1_event_60 = "/maya/events/stage1/60.webp"
    scene maya_stage_1_event_60
    "There's Maya. Who are the other girls she's with? It looks like one of them is crying."
    $ unknownname = 'Redhead'
    unknown "He can’t seriously do this to her!"
    $ unknownname = 'Tattoed woman'
    unknown "What else can we do? Once he makes up his mind, you know you can't change it."
    $ unknownname = 'Brunette'
    unknown "You looked fine a week ago. This really progressed quickly."
    $ unknownname = 'Crying Blonde'
    image maya_stage_1_event_61 = "/maya/events/stage1/61.webp"
    scene maya_stage_1_event_61
    unknown "I really thought I had more time. Like another month before I would start showing. What am I going to do?"
    maya "Tessa, don’t worry. The girls and I have already discussed this a few weeks ago that we would all chip in a portion of our earnings every week to help you."
    maya "We just didn’t know it was going to happen so soon."
    #Tessa sniffling through tears
    image maya_stage_1_event_62 = "/maya/events/stage1/62.webp"
    scene maya_stage_1_event_62
    tessa "I don’t want to be a burden on all of you."
    $ unknownname = 'Brunette'
    unknown "Nonsense, it was a unanimous decision from all of us. You should be happy, not sad."
    #Pc walks up to the group.
    image maya_stage_1_event_63 = "/maya/events/stage1/63.webp"
    scene maya_stage_1_event_63
    $ unknownname = 'Tattoed woman'
    unknown "What do you want?"
    $ unknownname = 'Redhead'
    unknown "Can’t you see that this is a private conversation."
    #Maya moves over to Pc
    image maya_stage_1_event_64 = "/maya/events/stage1/64.webp"
    scene maya_stage_1_event_64
    maya "Don’t worry girls. I know this guy. He’s the one I told you about. Hey, [playername]."
    $ unknownname = 'Brunette'
    unknown "Is he the guy that works at Bunny Bites."
    maya "Yeah."
    $ unknownname = 'Unknown'
    pc "Is everything ok?"
    image maya_stage_1_event_65 = "/maya/events/stage1/65.webp"
    scene maya_stage_1_event_65
    maya "Yeah, everything is going to be ok. I’ll make sure of it. Oh, by the way. Have you met my coworkers? We have Rayla, Jaimy, Gina, and Tessa."
    image maya_stage_1_event_66 = "/maya/events/stage1/66.webp"
    scene maya_stage_1_event_66
    tessa "If Mr. Vanthorne ever lets me come back."
    maya "Don’t talk like that Tessa, I’ll do whatever I can to make sure you are able to come back."
    tessa "You really mean it?"
    #Tessa starts to cry again
    pc "What’s happening?"
    image maya_stage_1_event_67 = "/maya/events/stage1/67.webp"
    scene maya_stage_1_event_67
    gina "Mr. Vanthorne is kicking Tessa off the floor."
    image maya_stage_1_event_68 = "/maya/events/stage1/68.webp"
    scene maya_stage_1_event_68
    rayla "Gina!"
    gina "What! He is."
    jaimy "You don’t need to say it like that."
    pc "Why is he doing that?"
    image maya_stage_1_event_69 = "/maya/events/stage1/69.webp"
    scene maya_stage_1_event_69
    tessa "He thinks I won’t bring in any money to the club because of this."
    #The girls were all kinda blocking Pc's view of Tessa then she walks forward to show a decently sized belly.
    tessa "Mr. Vanthorne doesn’t want a pregnant girl out on the dance floor."
    #Tessa starts to cry again
    image maya_stage_1_event_70 = "/maya/events/stage1/70.webp"
    scene maya_stage_1_event_70
    tessa "I should get going. I don’t want you girls to get in trouble."
    maya "Just remember Tessa we all have your back, Ok. Jaimy, why don’t you make sure Tessa gets to her car just fine."
    maya "Tessa, I’ll call you after my shift tonight to make sure you're ok."
    tessa "I don’t deserve friends like you."
    image maya_stage_1_event_71 = "/maya/events/stage1/71.webp"
    scene maya_stage_1_event_71
    jaimy "Let’s go Tessa."
    #Jaimy leads Tessa away.
    image maya_stage_1_event_72 = "/maya/events/stage1/72.webp"
    scene maya_stage_1_event_72
    rayla "Do you really think she’ll be ok?"
    maya "When I call her, I’ll go over everything we discussed we would do for her. That should put her mind at ease."
    vanthorne "Uh-hm."
    #Mr. Vanthore appears.
    image maya_stage_1_event_73 = "/maya/events/stage1/73.webp"
    scene maya_stage_1_event_73
    vanthorne "What do you girls think you're doing?"
    maya "Mr. Vanthore, we were just making sure Tessa was ok."
    image maya_stage_1_event_74 = "/maya/events/stage1/74.webp"
    scene maya_stage_1_event_74
    vanthorne "I hope you all can learn from this. Knocking yourself up. What a stupid thing to do. Especially in this line of work."
    maya "She had her reasons."
    vanthorne "I don’t care about the reasons. She's losing me money and so are all of you. Get back out there."
    image maya_stage_1_event_75 = "/maya/events/stage1/75.webp"
    scene maya_stage_1_event_75
    rayla "Yes, sir."
    gina "Yes, sir."
    #Rayla and Gina leave and Mr. Vanthore points to Maya.
    image maya_stage_1_event_76 = "/maya/events/stage1/76.webp"
    scene maya_stage_1_event_76
    vanthorne "You better get those girls back in line. We’re lucky it was Tessa that got knocked up. She was our lowest earner."
    #Maya looks ashamed.
    image maya_stage_1_event_77 = "/maya/events/stage1/77.webp"
    scene maya_stage_1_event_77
    maya "I’ll do my best."
    vanthorne "Good, now get back to work."
    #Mr. Vanthore leaves. Maya still looks ashamed.
    image maya_stage_1_event_78 = "/maya/events/stage1/78.webp"
    scene maya_stage_1_event_78
    pc "What a horrible man."
    maya "I know, but I blame myself. I knew her decision wasn't going to turn out well, but nothing I could have said was going to stop her."
    maya "The best I can do is make sure she’s supported. Anyways, you came down here all this way."
    image maya_stage_1_event_79 = "/maya/events/stage1/79.webp"
    scene maya_stage_1_event_79
    maya "Do you want a private dance? Remember I’ll give you the friends' price."
    #Options: Private Dance or hang out on the main floor.
    menu:
        "Private Dance. (-20$)":
            if money <= 19 and recollection == False:
                "You do not have enough money for a private dance."
                pc "I think I’ll stick around out here."
                image maya_stage_1_event_81 = "/maya/events/stage1/81.webp"
                scene maya_stage_1_event_81
                maya "You should find a spot close to the stage. My turn is coming up soon."
                image maya_stage_1_event_82 = "/maya/events/stage1/82.webp"
                scene maya_stage_1_event_82
                "You find a seat next to the stage and watch Maya do her routine."
                image maya_stripclub_poledance_start_event1 = "/maya/1/stripclub_poledance_start.webp"
                scene maya_stripclub_poledance_start_event1
                window hide
                pause
                image maya_stripclub_poledance1_event1 = "/maya/1/stripclub_poledance1.webp"
                scene maya_stripclub_poledance1_event1
                pause
                image maya_stripclub_poledance2_event1 = "/maya/1/stripclub_poledance2.webp"
                scene maya_stripclub_poledance2_event1
                pause
                image maya_stripclub_poledance3_event1 = "/maya/1/stripclub_poledance3.webp"
                scene maya_stripclub_poledance3_event1
                pause
                image maya_stripclub_poledance4_event1 = "/maya/1/stripclub_poledance4.webp"
                scene maya_stripclub_poledance4_event1
                pause
                image maya_stripclub_poledance5_event1 = "/maya/1/stripclub_poledance5.webp"
                scene maya_stripclub_poledance5_event1
                pause
                image maya_stripclub_poledance6_event1 = "/maya/1/stripclub_poledance6.webp"
                scene maya_stripclub_poledance6_event1
                pause
                image maya_stripclub_poledance_end_event1 = "/maya/1/stripclub_poledance_end.webp"
                scene maya_stripclub_poledance_end_event1
                "When Maya is done, you get up and head home."
            else:
                # Option Private Dance
                pc "I think a private dance sounds good."
                if recollection == False:
                    $ money -= 20
                image maya_stage_1_event_80 = "/maya/events/stage1/80.webp"
                scene maya_stage_1_event_80
                maya "Glad to hear. I wouldn’t mind getting away from the main room."
                image maya_private_arrive_event1 = "/maya/1/private_arrive.webp"
                scene maya_private_arrive_event1
                maya "You remember the rules?"
                pc "No touching."
                image maya_private_talk_event1 = "/maya/1/private_talk.webp"
                scene maya_private_talk_event1
                maya "Good. Now sit back and enjoy the show."
                if mayadance == 0:
                    image maya_private_dance_event1 = "/maya/1/private_dance.webp"
                    scene maya_private_dance_event1
                    window hide
                    pause
                    $ renpy.movie_cutscene("/images/maya/1/private_dance_video.webm", stop_music=False)
                    image maya_private_dance2_event1 = "/maya/1/private_dance2.webp"
                    scene maya_private_dance2_event1
                    if recollection == False:
                        $ mayadance = 1
                elif mayadance == 1:
                    image maya_private_dance2_event1 = "/maya/1/private_dance2.webp"
                    scene maya_private_dance2_event1
                    window hide
                    pause
                    $ renpy.movie_cutscene("/images/maya/1/private_dance2_video.webm", stop_music=False)
                    image maya_private_dance_event1 = "/maya/1/private_dance.webp"
                    scene maya_private_dance_event1
                    if recollection == False:
                        $ mayadance = 0
                pause
                image maya_private_bye_event1 = "/maya/1/private_bye.webp"
                scene maya_private_bye_event1
                "When Maya is done, you get up and head home."
        "Stay here.":
            #Option Main Floor
            pc "I think I’ll stick around out here."
            image maya_stage_1_event_81 = "/maya/events/stage1/81.webp"
            scene maya_stage_1_event_81
            maya "You should find a spot close to the stage. My turn is coming up soon."
            image maya_stage_1_event_82 = "/maya/events/stage1/82.webp"
            scene maya_stage_1_event_82
            "You find a seat next to the stage and watch Maya do her routine."
            image maya_stripclub_poledance_start_event1 = "/maya/1/stripclub_poledance_start.webp"
            scene maya_stripclub_poledance_start_event1
            window hide
            pause
            image maya_stripclub_poledance1_event1 = "/maya/1/stripclub_poledance1.webp"
            scene maya_stripclub_poledance1_event1
            pause
            image maya_stripclub_poledance2_event1 = "/maya/1/stripclub_poledance2.webp"
            scene maya_stripclub_poledance2_event1
            pause
            image maya_stripclub_poledance3_event1 = "/maya/1/stripclub_poledance3.webp"
            scene maya_stripclub_poledance3_event1
            pause
            image maya_stripclub_poledance4_event1 = "/maya/1/stripclub_poledance4.webp"
            scene maya_stripclub_poledance4_event1
            pause
            image maya_stripclub_poledance5_event1 = "/maya/1/stripclub_poledance5.webp"
            scene maya_stripclub_poledance5_event1
            pause
            image maya_stripclub_poledance6_event1 = "/maya/1/stripclub_poledance6.webp"
            scene maya_stripclub_poledance6_event1
            pause
            image maya_stripclub_poledance_end_event1 = "/maya/1/stripclub_poledance_end.webp"
            scene maya_stripclub_poledance_end_event1
            "When Maya is done, you get up and head home."

    #Pc leaves and goes home.
    stop music fadeout 1.0
    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
        $ maya.weight = 80
    $ mayastage1event3 = 0
    return

label Maya_Stage_2_Event_1:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Maya', dialogue=dialogue_one)
    $ msg ("If you're not doing anything today, you should stop by the club.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("I think I will. See you soon.")
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright. Another time then.", who=1)
            pause
            $ hide_messenger()
            return

    #Velvet Shadows Main Floor
    scene stripclub_entrance
    play music "/music/stripclub.ogg" if_changed
    "You walk into the entrance."
    scene stripclub
    "After walking into the main floor you look for Maya."
    image maya_stage_2_event_1 = "/maya/events/stage2/1.webp"
    scene maya_stage_2_event_1
    "Just as you notice her you see her already walking over to you."
    image maya_stage_2_event_2 = "/maya/events/stage2/2.webp"
    scene maya_stage_2_event_2
    maya "Glad you could make it. We have a special deal for private dances today, so I’m not taking no for an answer."
    pc "Then today is my lucky day."
    #Maya smiles and leads Pc to her private room.
    image maya_stage_2_event_3 = "/maya/events/stage2/3.webp"
    scene maya_stage_2_event_3
    window hide
    pause

    image maya_stage_2_event_4 = "/maya/events/stage2/4.webp"
    scene maya_stage_2_event_4
    pc "I’ve been meaning to ask, how is Tessa doing?"
    maya "She’s doing well. I call her every day. She keeps me posted on how she’s doing. Everyone is good and healthy."
    pc "I’m glad to hear."
    image maya_stage_2_event_5 = "/maya/events/stage2/5.webp"
    scene maya_stage_2_event_5
    maya "You remember the rules?"
    pc "Keep my hands to myself."
    image maya_stage_2_event_6 = "/maya/events/stage2/6.webp"
    scene maya_stage_2_event_6
    "Maya boops your nose and turns on the music, starting her dance."

    image maya_private_dance_event2 = "/maya/2/private_dance.webp"
    scene maya_private_dance_event2
    window hide
    pause
    $ renpy.movie_cutscene("/images/maya/events/stage2/half_dance.webm", stop_music=False)

    image maya_stage_2_event_7 = "/maya/events/stage2/7.webp"
    scene maya_stage_2_event_7
    "Halfway through the dance, Rayla and Gina barge in."
    image maya_stage_2_event_8 = "/maya/events/stage2/8.webp"
    scene maya_stage_2_event_8
    maya "I’m with a customer."
    image maya_stage_2_event_9 = "/maya/events/stage2/9.webp"
    scene maya_stage_2_event_9
    rayla "We’re sorry, but Jaimy needs your help."
    gina "You know that big guy who's always in here? I think his name is Gabe. He’s trying to get Jaimy to sit on his lap."
    rayla "Jaimy’s trying to resist, but he keeps grabbing her, trying to force her onto his lap."
    image maya_stage_2_event_10 = "/maya/events/stage2/10.webp"
    scene maya_stage_2_event_10
    maya "This guy is such a creep. Alright, why don’t you two give a dance for [playername] while I take care of this."
    gina "Thanks, Maya. I’m sure Jaimy will be grateful."
    image maya_stage_2_event_11 = "/maya/events/stage2/11.webp"
    scene maya_stage_2_event_11
    "Maya whispers something to Rayla and Gina before leaving."
    image maya_stage_2_event_12 = "/maya/events/stage2/12.webp"
    scene maya_stage_2_event_12
    rayla "Sorry we interrupted, but I guess it works out you get a two-for-one."
    pc "I guess today really is my lucky day, but why don’t you go to Mr. Vanthore about this."
    image maya_stage_2_event_13 = "/maya/events/stage2/13.webp"
    scene maya_stage_2_event_13
    gina "Mr. Vanthore would just tell us to take it and do whatever the customer wants."
    rayla "Yeah, Mr. Vanthore is pretty relaxed on the rules. I can’t count how many times my ass has been pinched or slapped."
    gina "One night, it was so bad I couldn’t sit down because my butt was so sore."
    pc "That's awful. So why come to Maya for help?"
    image maya_stage_2_event_14 = "/maya/events/stage2/14.webp"
    scene maya_stage_2_event_14
    rayla "She’s kind of like a big sister to all of us. Whenever we have problems with a customer, we always go to her."
    gina "She’s been here the longest, so she knows how to deal with these types of customers. I bet she’s out there sitting on the creepy guy's lap, taking one for the team."
    pc "She really looks out for you girls. No wonder Tessa's situation hit her so hard."
    image maya_stage_2_event_15 = "/maya/events/stage2/15.webp"
    scene maya_stage_2_event_15
    gina "Yeah, Maya’s pretty worried about her, but I know she’ll do anything to make it work. She’s family, after all."
    pc "Family?"
    image maya_stage_2_event_16 = "/maya/events/stage2/16.webp"
    scene maya_stage_2_event_16
    rayla "Yeah, family. We all take care of each other, and I guess you can say Maya is kind of our leader or big sis."
    pc "I can see that. I think it's great you gals all have each other's backs."
    rayla "Yep. So…"
    image maya_stage_2_event_17 = "/maya/events/stage2/17.webp"
    scene maya_stage_2_event_17
    "Rayla looks over to Gina."
    image maya_stage_2_event_18 = "/maya/events/stage2/18.webp"
    scene maya_stage_2_event_18
    rayla "Maya said we should take good care of you."
    image maya_stage_2_event_19 = "/maya/events/stage2/19.webp"
    scene maya_stage_2_event_19
    gina "She seems to have taken a liking to you. She also told us not to worry about paying, this is on the house."

    #DANCE
    image maya_stage_2_event_dancestart = "/maya/events/stage2/dancestart.webp"
    scene maya_stage_2_event_dancestart
    window hide
    pause
    $ renpy.movie_cutscene("/images/maya/events/stage2/dance.webm", stop_music=False)
    image maya_stage_2_event_danceend = "/maya/events/stage2/danceend.webp"
    scene maya_stage_2_event_danceend
    pause
    image maya_stage_2_event_danceend2 = "/maya/events/stage2/danceend2.webp"
    scene maya_stage_2_event_danceend2
    gina "I hope you enjoyed that."
    rayla "Thank you for coming today."
    "You go back home."

    #Pc heads home.
    if recollection == False:
        $ maya.weight += 1
        $ daytime += 1
        $ phonecall = 1
    stop music fadeout 1.0
    $ mayastage2event = 0
    return


label Maya_Stage_2_Event_2:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Maya', dialogue=dialogue_one)
    $ msg ("Hey, you should swing by the club today. I’m going to try out a new move on the pole. I’m on in like an hour; you should come by early to get a good seat.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sounds fun. I’ll be there soon.")
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright. Another time then.", who=1)
            pause
            $ hide_messenger()
            return

    #Velvet Shadows Main Room
    image maya_stripclub_crowd_event2 = "/maya/2/stripclub_crowd.webp"
    scene maya_stripclub_crowd_event2
    play music "/music/stripclub.ogg" if_changed
    "You find Maya and approach her."
    image maya_stripclub_talk_event2 = "/maya/2/stripclub_talk.webp"
    scene maya_stripclub_talk_event2
    maya "You made it! Just in time, I’m about to head on back to get ready."
    image maya_stripclub_talk2_event2 = "/maya/2/stripclub_talk2.webp"
    scene maya_stripclub_talk2_event2
    maya "Why don’t you get a seat close to the stage?"
    pc "I think I see an open seat in front. I’m going to go so I don’t lose it."
    scene stripclub_dancer
    "You secure a seat up front and wait for Maya to take the stage, but before she does, Mr. Vanthorne walks over to you."
    image maya_stage_2_event_20 = "/maya/events/stage2/20.webp"
    scene maya_stage_2_event_20
    vanthorne "Are you waiting for the show?"
    pc "I am. Maya said she’d be on soon."
    vanthorne "She is our best dancer, after all. Anyways, I came over to properly introduce myself."
    pc "Why now?"
    image maya_stage_2_event_21 = "/maya/events/stage2/21.webp"
    scene maya_stage_2_event_21
    vanthorne "I didn’t know if you were a serious customer or not. You never know these days if someone just coming is to take a peek at my girls."
    vanthorne "I should charge people for just coming in. But I’ve noticed you getting some private dances so I know you're truly a customer. People like you are getting harder and harder to find."
    pc "Is the club not doing well?"
    image maya_stage_2_event_22 = "/maya/events/stage2/22.webp"
    scene maya_stage_2_event_22
    vanthorne "Business is good, but I know we could do better if only the girls would stop complaining. These girls don’t know what’s good for them."
    vanthorne "What’s so bad about a slap on the ass or a squeeze of the cheeks? These girls would be raking in the dough if they just let them grab a breast or two."
    pc "Maybe they don’t like to be touched like that."
    vanthorne "Oh, really."
    image maya_stage_2_event_23 = "/maya/events/stage2/23.webp"
    scene maya_stage_2_event_23
    "Mr. Vanthorne waves Jaimy over to you two."
    image maya_stage_2_event_24 = "/maya/events/stage2/24.webp"
    scene maya_stage_2_event_24
    vanthorne "Could you be a doll and get me a scotch and whatever this fine gentleman would like. On the house, of course."
    pc "No, thank you, I’m fine."
    image maya_stage_2_event_25 = "/maya/events/stage2/25.webp"
    scene maya_stage_2_event_25
    vanthorne "Alright, just the scotch. Thanks, darling."
    jaimy "Right away, Mr. Vanthorne."
    image maya_stage_2_event_26 = "/maya/events/stage2/26.webp"
    scene maya_stage_2_event_26
    "Mr. Vanthorne slaps Jaimy’s behind as she walks away."
    image maya_stage_2_event_27 = "/maya/events/stage2/27.webp"
    scene maya_stage_2_event_27
    vanthorne "You see, they like it. Besides, that rule is what they want. My rules are what make this place profitable. You should have seen some of these girls before I bought this place."
    vanthorne "Especially Maya. I made her the star she is now. She’s my little money maker. I think she’s about to get on stage. I best get going. I appreciate your business. Enjoy the show."
    image maya_stage_2_event_28 = "/maya/events/stage2/28.webp"
    scene maya_stage_2_event_28
    "Mr. Vanthorne leaves."
    "What a horrible guy. How can anyone work for him?"
    image maya_stripclub_poledance_start_event2 = "/maya/2/stripclub_poledance_start.webp"
    scene maya_stripclub_poledance_start_event2
    "Maya takes the stage and performs her routine."
    image maya_stripclub_poledance1_event2 = "/maya/2/stripclub_poledance1.webp"
    scene maya_stripclub_poledance1_event2
    window hide
    pause
    image maya_stripclub_poledance2_event2 = "/maya/2/stripclub_poledance2.webp"
    scene maya_stripclub_poledance2_event2
    pause
    image maya_stripclub_poledance3_event2 = "/maya/2/stripclub_poledance3.webp"
    scene maya_stripclub_poledance3_event2
    pause
    image maya_stripclub_poledance4_event2 = "/maya/2/stripclub_poledance4.webp"
    scene maya_stripclub_poledance4_event2
    pause
    image maya_stripclub_poledance5_event2 = "/maya/2/stripclub_poledance5.webp"
    scene maya_stripclub_poledance5_event2
    pause
    image maya_stripclub_poledance6_event2 = "/maya/2/stripclub_poledance6.webp"
    scene maya_stripclub_poledance6_event2
    pause
    image maya_stripclub_poledance_end_event2 = "/maya/2/stripclub_poledance_end.webp"
    scene maya_stripclub_poledance_end_event2
    "You leave after Maya is done."
    if recollection == False:
        $ maya.weight += 1
        $ daytime += 1
        $ phonecall = 1
    stop music fadeout 1.0
    $ mayastage2event2 = 0
    return


label Maya_Stage_2_Event_3:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Maya', dialogue=dialogue_one)
    $ msg ("Hey [playername], do you want to swing by the club? It’s been pretty slow, so I wouldn’t mind seeing a friendly face come in.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("That sounds like fun. I’ll head over shortly.")
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright. Another time then.", who=1)
            pause
            $ hide_messenger()
            return

    #Velvet Shadows Main Room
    scene stripclub
    play music "/music/stripclub.ogg" if_changed
    "It doesn’t look too busy today. Where is Maya?"
    image maya_stage_2_event_29 = "/maya/events/stage2/29.webp"
    scene maya_stage_2_event_29
    "You look around the club and spot Maya serving a couple of drinks."
    image maya_stage_2_event_30 = "/maya/events/stage2/30.webp"
    scene maya_stage_2_event_30
    "She looks up and waves to you."
    #$ unknownname = 'Customer'
    #unknown "Thanks for the drinks, darling."
    image maya_stage_2_event_31 = "/maya/events/stage2/31.webp"
    scene maya_stage_2_event_31
    "The customer slaps Maya’s behind. Maya looks upset by his action and sees that you saw it too."
    image maya_stage_2_event_32 = "/maya/events/stage2/32.webp"
    scene maya_stage_2_event_32
    "Her face turns to disappointment. She hands her drink tray off to a dancer passing by and walks up to you."
    $ unknownname = 'Unknown'
    image maya_stage_2_event_33 = "/maya/events/stage2/33.webp"
    scene maya_stage_2_event_33
    maya "Hey, I guess you saw all that, didn’t you?"
    pc "You should have said something to him."
    image maya_stage_2_event_34 = "/maya/events/stage2/34.webp"
    scene maya_stage_2_event_34
    maya "I didn’t want to cause a scene with Mr. Vanthorne still here and in his office. Can we do that same deal as last time? I just want to get away from these disgusting guys."
    maya "Can’t count how many times my ass has been slapped or pinched today, but what’s new?"
    pc "Sure, we can do that again. Are you sure you're okay?"
    image maya_stage_2_event_35 = "/maya/events/stage2/35.webp"
    scene maya_stage_2_event_35
    maya "Not out here. Let’s go back to my room and we can talk, okay?"
    pc "Yeah, of course."
    image maya_stage_2_event_36 = "/maya/events/stage2/36.webp"
    scene maya_stage_2_event_36
    window hide
    pause

    #Maya’s Private Room
    image maya_stage_2_event_37 = "/maya/events/stage2/37.webp"
    scene maya_stage_2_event_37
    play music "/music/sadness.ogg" if_changed
    "Maya closes the door and leans her back against it."
    image maya_stage_2_event_38 = "/maya/events/stage2/38.webp"
    scene maya_stage_2_event_38
    maya "I keep telling myself every night that the next day won’t be as bad as this one. And every day life proves me wrong."
    image maya_stage_2_event_39 = "/maya/events/stage2/39.webp"
    scene maya_stage_2_event_39
    "Maya slides down and sits on the ground. Hands cover her face."
    pc "You want me to go out there and teach him some lessons."
    image maya_stage_2_event_40 = "/maya/events/stage2/40.webp"
    scene maya_stage_2_event_40
    "Maya laughs, putting down her hands, and gives you a little smile. She looks like she’s been crying."
    maya "As much as I’d like that, I wouldn’t want you to get kicked out. I like seeing you. It’s nice seeing a friendly face in here every once in a while."
    pc "This seems to happen to all the girls."
    image maya_stage_2_event_41 = "/maya/events/stage2/41.webp"
    scene maya_stage_2_event_41
    maya "Pretty much. The worst part is they think I can do something about it. I try my best, but there is only so much I can do."
    pc "Yeah, Rayla and Gina said you’re like a big sister to them."
    image maya_stage_2_event_42 = "/maya/events/stage2/42.webp"
    scene maya_stage_2_event_42
    maya "I guess I sort of am like a big sister to them. I’ve been here the longest, almost 8 years now. It hasn’t always been this bad."
    image maya_stage_2_event_43 = "/maya/events/stage2/43.webp"
    scene maya_stage_2_event_43
    maya "The previous owners were nice people. They weren’t mean or judgmental."
    maya "They made sure us girls were safe and taken care of, but Mr. Vanthorne, he is the complete opposite. He never looks out for us. You’ve seen what he's like."
    pc "I’m getting the picture the more I come here. I don’t know how you girls can stand the man."
    image maya_stage_2_event_44 = "/maya/events/stage2/44.webp"
    scene maya_stage_2_event_44
    maya "I know, but I don’t know what to do. They deserve someone better than me. I'm just one person."
    pc "The responsibility for all of them shouldn’t all rest on your shoulders."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/maya/events/stage2/vid1.webm" loop
    show movie with dissolve
    maya "I know that’s not fair for me, but that’s how it is. I’m their big sister and they’re like family, and I’ll do anything to help them."
    pc "How can you help them if you don’t stand up to Mr. Vanthorne?"
    maya "By doing nothing means they keep their jobs."
    pc "How does that work?"
    maya "If I start making a fuss about things to Mr. Vanthorne, other girls will start doing the same."
    pc "Why would that be bad?"
    maya "That would be bad because Mr. Vanthorne knows I’m looked up to by all the girls here and he wouldn’t dare do anything to me since I bring in the most money to his club."
    maya "But that wouldn’t stop him from doing that to any girl that isn’t performing well."
    stop movie
    image maya_stage_2_event_45 = "/maya/events/stage2/45.webp"
    scene maya_stage_2_event_45
    maya "He’ll start letting them go, one after another, and I’ll know it was all my fault for standing up to him. I can’t do that to them."
    pc "I see, you're stuck between a rock and a hard place."
    image maya_stage_2_event_46 = "/maya/events/stage2/46.webp"
    scene maya_stage_2_event_46
    maya "Pretty much. Hey, thanks for letting me vent a little."
    image maya_stage_2_event_47 = "/maya/events/stage2/47.webp"
    scene maya_stage_2_event_47
    "Maya and you stand up."
    image maya_stage_2_event_48 = "/maya/events/stage2/48.webp"
    scene maya_stage_2_event_48
    pause
    image maya_stage_2_event_49 = "/maya/events/stage2/49.webp"
    scene maya_stage_2_event_49
    maya "Sorry for being such a mess, give me a moment to fix my make-up."
    image maya_stage_2_event_50 = "/maya/events/stage2/50.webp"
    scene maya_stage_2_event_50
    play music "/music/stripclub.ogg" if_changed
    "Maya moves over to her mirror to fix her smeared make-up."
    image maya_stage_2_event_51 = "/maya/events/stage2/51.webp"
    scene maya_stage_2_event_51
    maya "I think I owe you a dance."
    pc "Oh, we don’t have to do that. It was nice just listening to you. No need for a dance."
    image maya_stage_2_event_52 = "/maya/events/stage2/52.webp"
    scene maya_stage_2_event_52
    "Maya looks disappointed."
    pc "I’ll still give you that free meal the next time you come in."
    image maya_stage_2_event_53 = "/maya/events/stage2/53.webp"
    scene maya_stage_2_event_53
    "Maya's smile reappears."
    maya "Phew, I thought I wasn’t getting that since you said no to the dance."
    pc "You just seem to have a lot on your plate right now."
    image maya_stage_2_event_54 = "/maya/events/stage2/54.webp"
    scene maya_stage_2_event_54
    #Maya hugs PC.
    maya "Thanks for understanding."
    image maya_stage_2_event_55 = "/maya/events/stage2/55.webp"
    scene maya_stage_2_event_55
    pc "You see, no touching."
    "Maya laughs."
    image maya_stage_2_event_56 = "/maya/events/stage2/56.webp"
    scene maya_stage_2_event_56
    maya "You're such a great guy. Thanks, because of you I’ve reconnected with Amber."
    pc "I’m not sure that’s a good thing."
    "Maya laughs again."
    image maya_stage_2_event_57 = "/maya/events/stage2/57.webp"
    scene maya_stage_2_event_57
    maya "You do know how to make someone feel better. I think I’m ready to get back out there. I’ll see you soon."
    image maya_stage_2_event_58 = "/maya/events/stage2/58.webp"
    scene maya_stage_2_event_58
    "After saying goodbye, you go back home."
    if recollection == False:
        $ maya.weight += 1
        $ daytime += 1
        $ phonecall = 1
    stop music fadeout 1.0
    $ mayastage2event3 = 0
    return



label Maya_Stage_2_Event_4:
    #A few days later, Pc gets a call from Amber.
    "You receive a message from Amber."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Amber', dialogue=dialogue_one)
    $ msg ("You’ll never guess what I just won off the radio.", who=1)
    pause
    $ msg ("What did you win?")
    pause
    $ msg ("Concert tickets!! Only problem is there this afternoon. Are you able to cover my shift today?", who=1)
    pause
    $ msg ("Sure thing. Have fun at the concert.")
    pause
    $ msg ("Thank you so much.", who=1)
    pause
    $ hide_messenger()

    #Bunny Bites
    image lisa_workattire_counter = "/lisa/[lisa.stage]/workattire_counter.webp"
    scene lisa_workattire_counter
    play music "/music/bunny_bites.ogg" if_changed
    lisa "So, Amber got you to cover her shift, I see."
    pc "Yep."
    lisa "Wonder why she didn’t invite any of us to the concert. Anyways, glad you could make it in."
    if recollection == False:
        $ amber_work_today = 1
        $ lisa_work_today = 1
        $ marie_work_today = 1
        $ maya_work_today = 1
        call work_randomizer from _call_work_randomizer_25
    # Pc works his job when Maya comes in.
    image cafe_maya_talk_event2 = "/maya/2/cafe_talk.webp"
    scene cafe_maya_talk_event2
    maya "I’m here for my meal."
    pc "The same as last time?"
    image cafe_maya_talk2_event2 = "/maya/2/cafe_talk2.webp"
    scene cafe_maya_talk2_event2
    maya "Umm, can I make it a double cheeseburger."
    pc "Sure can, find a seat and I’ll bring that out to you in a few minutes."
    image maya_stage_2_event_59 = "/maya/events/stage2/59.webp"
    scene maya_stage_2_event_59
    "You bring Maya her food, she looks happy to get it."
    image maya_stage_2_event_60 = "/maya/events/stage2/60.webp"
    scene maya_stage_2_event_60
    "Later, you notice Maya again sitting there holding her stomach, thinking about something."
    "You go over to her."
    pc "Is it okay if I sit down with you?"
    image maya_stage_2_event_61 = "/maya/events/stage2/61.webp"
    scene maya_stage_2_event_61
    "Maya, once again lost in thought, is startled by you."
    maya "I don’t mind."
    #Pc sits with Maya.
    image maya_stage_2_event_62 = "/maya/events/stage2/62.webp"
    scene maya_stage_2_event_62
    pc "Is everything okay? Was it too much food?"
    maya "The food was amazing, and no, that wasn’t too much food. In fact, I’m still pretty hungry. I guess that's what I was sitting here thinking about."
    pc "What is that?"
    image maya_stage_2_event_63 = "/maya/events/stage2/63.webp"
    scene maya_stage_2_event_63
    maya "How I’m still hungry after a meal like that. I’ve been eating such small portions since Mr. Vanthorne set those strict diet guidelines."
    maya "I haven’t felt full for over a year. I thought for sure this would have done it, but I’m still hungry."
    pc "I can go make you more if you want."
    image maya_stage_2_event_64 = "/maya/events/stage2/64.webp"
    scene maya_stage_2_event_64
    maya "Oh no, this was plenty. Maybe I am full, but I just don’t remember how that feels. I better get going or I’ll be late to work. Thanks again for the meal."
    image maya_stage_2_event_65 = "/maya/events/stage2/65.webp"
    scene maya_stage_2_event_65
    "Maya leaves, and you finish your shift."
    stop music fadeout 1.0
    if recollection == False:
        $ maya.weight = 84
        $ daytime += 1
        $ phonecall = 1
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
    $ mayastage2event4 = 0
    return

label Maya_Stage_3_Event_1:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Maya', dialogue=dialogue_one)
    $ msg ("Hey [playername]. If you're not doing anything,  would you like to stop by the club.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sounds fun.")
            pause
            $ msg ("I’ll see you later ;-D", who=1)
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Sorry, kinda busy today.")
            pause
            $ msg ("No problem, maybe some other time.", who=1)
            pause
            $ hide_messenger()
            return

    #Velvet Shadows Main Room
    scene stripclub
    play music "/music/stripclub.ogg" if_changed
    "While entering the club you hear an argument going on."
    image maya_stage_3_event_1 = "/maya/events/stage3/1.webp"
    scene maya_stage_3_event_1
    "You see Maya standing between Gina and a customer."
    image maya_stage_3_event_2 = "/maya/events/stage3/2.webp"
    scene maya_stage_3_event_2
    maya "She said no!"
    $ unknownname = 'Customer'
    image maya_stage_3_event_3 = "/maya/events/stage3/3.webp"
    scene maya_stage_3_event_3
    unknown "Who’s got your panties in a bunch? This is between me and her. Besides, she looked like she was enjoying it."
    image maya_stage_3_event_4 = "/maya/events/stage3/4.webp"
    scene maya_stage_3_event_4
    gina "Maya, please stop, you’re making a scene."
    image maya_stage_3_event_5 = "/maya/events/stage3/5.webp"
    scene maya_stage_3_event_5
    "Maya, looking upset, sees you."
    image maya_stage_3_event_6 = "/maya/events/stage3/6.webp"
    scene maya_stage_3_event_6
    "She then turns to the customer and slaps him."
    image maya_stage_3_event_7 = "/maya/events/stage3/7.webp"
    scene maya_stage_3_event_7
    maya "How does that feel? Keep your hands off the girls."
    image maya_stage_3_event_8 = "/maya/events/stage3/8.webp"
    scene maya_stage_3_event_8
    "Maya storms over to you."
    unknown "I’m going to tell your boss about this."
    maya "Fine! Go ahead."
    pc "Are you okay?"
    image maya_stage_3_event_9 = "/maya/events/stage3/9.webp"
    scene maya_stage_3_event_9
    maya "Let’s go. Same deal as last time."
    $ unknownname = 'Unknown'
    "Before you can answer, Maya grabs your hand and walks you back to her room."
    image maya_stage_3_event_10 = "/maya/events/stage3/10.webp"
    scene maya_stage_3_event_10
    maya "Why did I do that? I’ve never hit a customer before."
    pc "What happened?"
    image maya_stage_3_event_11 = "/maya/events/stage3/11.webp"
    scene maya_stage_3_event_11
    maya "Gina was just walking by when that monster grabbed her and forced her onto his lap."
    maya "She started resisting, but he kept pulling her back, grabbing her breast and sticking his hand in her crotch."
    maya "I couldn’t stomach it anymore, I snapped."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/maya/events/stage3/vid1.webm" loop
    show movie with dissolve
    maya "What is Mr. Vanthorne going to say?"
    pc "Who cares. Sounds like he deserved it."
    maya "It did feel pretty good."
    pc "Is Gina okay?"
    maya "Oh no! I forgot about Gina. What is Mr. Vanthorne going to do with her? I know he’s going to blame her for this. First Tessa and now maybe Gina."
    pc "I’m more concerned about you."
    maya "Who cares about me."
    pc "I think all the girls care about you."
    stop movie
    image maya_stage_3_event_12 = "/maya/events/stage3/12.webp"
    scene maya_stage_3_event_12
    maya "You’re probably right. I need to calm down and think about them. I know what I did was right. I need to be strong."
    image maya_stage_3_event_13 = "/maya/events/stage3/13.webp"
    scene maya_stage_3_event_13
    vanthorne "What the hell happened out there? Did you seriously think that was a good idea?"
    image maya_stage_3_event_14 = "/maya/events/stage3/14.webp"
    scene maya_stage_3_event_14
    maya "He was molesting Gina."
    vanthorne "I don’t give a shit what he was doing. You don’t ever hit a customer in my establishment, you hear!"
    maya "But—"
    vanthorne "No buts! I think you’re done for the night. Go home and think about what you’ve done."
    maya "I’m not fired?"
    image maya_stage_3_event_15 = "/maya/events/stage3/15.webp"
    scene maya_stage_3_event_15
    vanthorne "Fired? No, You make me too much money to fire you now, but you’re on thin ice."
    vanthorne "Another outburst of disobedience like tonight, and I won't hesitate to kick you out of here."
    image maya_stage_3_event_16 = "/maya/events/stage3/16.webp"
    scene maya_stage_3_event_16
    vanthorne "I’m sorry for any inconvenience this may have caused you. Would you like me to get another girl to come in for a private dance?"
    pc "I was just about to leave."
    image maya_stage_3_event_17 = "/maya/events/stage3/17.webp"
    scene maya_stage_3_event_17
    vanthorne "As for you, I’d get going before I change my mind."
    image maya_stage_3_event_18 = "/maya/events/stage3/18.webp"
    scene maya_stage_3_event_18
    vanthorne "And don’t think I haven’t noticed your little weight gain. Get that under control too."
    image maya_stage_3_event_19 = "/maya/events/stage3/19.webp"
    scene maya_stage_3_event_19
    maya "That went better than I thought it would."
    pc "You still have a job."
    maya "I also have a night off."
    #Maya looks relieved.
    image maya_stage_3_event_20 = "/maya/events/stage3/20.webp"
    scene maya_stage_3_event_20
    maya "I could use a drink. Would you like to join me? I could use some company."
    pc "Of course."
    maya "I’ll meet you at the entrance."
    image maya_stage_3_event_21 = "/maya/events/stage3/21.webp"
    scene maya_stage_3_event_21
    "You wait for Maya in the entrance of the club. Pretty soon, Maya comes out."
    pc "So, where are we going?"
    image maya_stage_3_event_22 = "/maya/events/stage3/22.webp"
    scene maya_stage_3_event_22
    maya "There’s a pub not too far from here. They have cheap drinks and good food."
    maya "I wonder if they still have that one special on the menu. We will see when we get there."
    stop music fadeout 1.0
    #Pc follows Maya to the Pub

    #Pub
    play music "<loop 0.2 from 39>/music/generic_date.ogg" if_changed fadein 1.0
    image maya_stage_3_event_23 = "/maya/events/stage3/23.webp"
    scene maya_stage_3_event_23
    "Maya and you find an open table. Soon the waitress comes over."
    image maya_stage_3_event_24 = "/maya/events/stage3/24.webp"
    scene maya_stage_3_event_24
    waitress "So what can I get you for drinks?"
    maya "I’ll take your biggest, cheapest beer you got."
    waitress "I know just the thing."
    image maya_stage_3_event_25 = "/maya/events/stage3/25.webp"
    scene maya_stage_3_event_25
    waitress "And what can I get you?"
    pc "I’ll do the same."
    image maya_stage_3_event_26 = "/maya/events/stage3/26.webp"
    scene maya_stage_3_event_26
    waitress "Sounds good. Here’s the menu. I’ll take your order when I come back with your drinks."
    image maya_stage_3_event_27 = "/maya/events/stage3/27.webp"
    scene maya_stage_3_event_27
    "Maya looks over the menu and gets excited."
    maya "They still have it! Here, you can have the menu, I know what I’m getting."
    image maya_stage_3_event_28 = "/maya/events/stage3/28.webp"
    scene maya_stage_3_event_28
    "You study the menu, looking for something to get when the waitress comes back with two very large glasses of beer."
    waitress "So, have you found something to order?"
    pc "I’ll have a burger with fries."
    image maya_stage_3_event_29 = "/maya/events/stage3/29.webp"
    scene maya_stage_3_event_29
    waitress "And for you, darling?"
    maya "I’ll have the “Everything but the kitchen sink.”"
    waitress "Okay, I’ll send this ticket to the kitchen. It might be a bit as the “Everything but the kitchen sink” takes a while to get together."
    image maya_stage_3_event_30 = "/maya/events/stage3/30.webp"
    scene maya_stage_3_event_30
    maya "That’s fine. Could you possibly bring another glass of beer over when the food comes?"
    waitress "I’ll make sure I do that."
    image maya_stage_3_event_31 = "/maya/events/stage3/31.webp"
    scene maya_stage_3_event_31
    pc "What’s “Everything but the kitchen sink”?"
    maya "You’ll have to wait and see."
    image maya_stage_3_event_32 = "/maya/events/stage3/32.webp"
    scene maya_stage_3_event_32
    "Maya grabs her glass and chugs half her beer."
    image maya_stage_3_event_33 = "/maya/events/stage3/33.webp"
    scene maya_stage_3_event_33
    "Maya puts her glass down and leans back."
    maya "Ahhh. This is exactly what I needed."
    image maya_stage_3_event_34 = "/maya/events/stage3/34.webp"
    scene maya_stage_3_event_34
    maya "I still can’t believe I slapped that guy."
    pc "Yeah, I was pretty shocked when you slapped him, but he deserved it."
    maya "Yeah, still pretty crazy though. And my punishment is getting the night off. I have no clue what Mr. Vanthorne was thinking there. Oh well, his loss."
    image maya_stage_3_event_35 = "/maya/events/stage3/35.webp"
    scene maya_stage_3_event_35
    "Maya grabs her glass and finishes the rest of her beer. Sets it down and leans back."
    image maya_stage_3_event_36 = "/maya/events/stage3/36.webp"
    scene maya_stage_3_event_36
    maya "I hope the other girls don’t get any backlash from this. Mr. Vanthorne was pretty angry."
    pc "I’m sure they’ll be okay. He seemed more upset with you, than anyone else."
    maya "I hope so."
    "Maya still seems worried about the other girls."
    image maya_stage_3_event_37 = "/maya/events/stage3/37.webp"
    scene maya_stage_3_event_37
    "Soon the waitress brings out your food."
    image maya_stage_3_event_38 = "/maya/events/stage3/38.webp"
    scene maya_stage_3_event_38
    waitress "Here’s your burger, sir and here is your beer and your “Everything but the kitchen sink."
    image maya_stage_3_event_39 = "/maya/events/stage3/39.webp"
    scene maya_stage_3_event_39
    waitress "Enjoy!"
    image maya_stage_3_event_40 = "/maya/events/stage3/40.webp"
    scene maya_stage_3_event_40
    maya "There’s a lot more here than I remember."
    pc "It looks like you got everything on the menu."
    image maya_stage_3_event_41 = "/maya/events/stage3/41.webp"
    scene maya_stage_3_event_41
    maya "Yep. It’s a little bit of everything they have. It smells amazing."
    image maya_stage_3_event_42 = "/maya/events/stage3/42.webp"
    scene maya_stage_3_event_42
    "Maya starts digging into her meal."
    image maya_stage_3_event_43 = "/maya/events/stage3/43.webp"
    scene maya_stage_3_event_43
    "Maya nonstop finishes one plate after another, you watch as her belly grows bigger with each plate."
    image maya_stage_3_event_44 = "/maya/events/stage3/44.webp"
    scene maya_stage_3_event_44
    "She only pauses to take big gulps from her beer."
    image maya_stage_3_event_45 = "/maya/events/stage3/45.webp"
    scene maya_stage_3_event_45
    "Plate after plate, she shows no sign of slowing down as her belly swells with all the food."
    image maya_stage_3_event_46 = "/maya/events/stage3/46.webp"
    scene maya_stage_3_event_46
    "Her shirt lifting up as her stomach expands."
    image maya_stage_3_event_47 = "/maya/events/stage3/47.webp"
    scene maya_stage_3_event_47
    "She finishes her last plate and drinks the last of her beer, leans back, and lets out a huge belch."
    image maya_stage_3_event_48 = "/maya/events/stage3/48.webp"
    scene maya_stage_3_event_48 with vpunch
    maya "Burp!…. Oops sorry."
    image maya_stage_3_event_49 = "/maya/events/stage3/49.webp"
    scene maya_stage_3_event_49
    maya "Phew. I haven’t done that for so long."
    image maya_stage_3_event_50 = "/maya/events/stage3/50.webp"
    scene maya_stage_3_event_50
    maya "Oh."
    image maya_stage_3_event_51 = "/maya/events/stage3/51.webp"
    scene maya_stage_3_event_51
    "Maya looks down at her enlarged belly."
    image maya_stage_3_event_52 = "/maya/events/stage3/52.webp"
    scene maya_stage_3_event_52
    maya "Guess I got a little carried away there."
    pc "That was amazing."
    image maya_stage_3_event_53 = "/maya/events/stage3/53.webp"
    scene maya_stage_3_event_53
    "Maya looks shocked."
    maya "Really? You're not disgusted by it?"
    pc "Not at all, I’m kinda impressed. I bet you're pretty full after that."
    image maya_stage_3_event_54 = "/maya/events/stage3/54.webp"
    scene maya_stage_3_event_54
    maya "Full? Oh yeah, I’m stuffed, I’m sure I couldn’t eat another bit."
    "You feel that Maya is hiding something. Suddenly, the waitress appears."
    image maya_stage_3_event_55 = "/maya/events/stage3/55.webp"
    scene maya_stage_3_event_55
    waitress "How is everything? Oh wow! You're done with your meal. That’s impressive and in record time."
    waitress "It's a shame we don’t do that challenge anymore, you would have gotten your meal for free."
    pc "Challenge?"
    image maya_stage_3_event_56 = "/maya/events/stage3/56.webp"
    scene maya_stage_3_event_56
    waitress "Yeah, the “Everything but the kitchen sink” was our food eating challenge. If you finished it in a certain amount of time, you got the meal for free."
    pc "Why don’t you do the challenge anymore?"
    waitress "Umm, a few years ago someone came in and ate two “Everything but the kitchen sink” in a row."
    pc "Wow, Maya, could you imagine eating two orders of that?"
    image maya_stage_3_event_57 = "/maya/events/stage3/57.webp"
    scene maya_stage_3_event_57
    maya "Oh my. One was enough for me."
    "Maya looks off to the side, seeming embarrassed."
    image maya_stage_3_event_58 = "/maya/events/stage3/58.webp"
    scene maya_stage_3_event_58
    waitress "Yeah, after that I thought the challenge was too easy and stopped it. I kept it on the menu since it's a nice way to try everything."
    maya "It was very good."
    waitress "I’m glad you liked it. Let me get those plates out of your way."
    image maya_stage_3_event_59 = "/maya/events/stage3/59.webp"
    scene maya_stage_3_event_59
    "The waitress takes the plates from the table and leaves."
    image maya_stage_3_event_60 = "/maya/events/stage3/60.webp"
    scene maya_stage_3_event_60
    maya "I bet if Mr. Vanthorne could see me now he would flip. Telling me that I put on some weight."
    pc "I bet he would."
    maya "I don’t know what his deal is. My numbers aren’t down or anything, they're actually up the last few weeks."
    pc "I’d say do whatever makes you happy."
    maya "What would make me happy would be going back to the club with my food baby here and get on that pole, seeing Mr. Vanthorne's face as all the money starts flowing onto the stage."
    image maya_stage_3_event_61 = "/maya/events/stage3/61.webp"
    scene maya_stage_3_event_61
    "Maya starts to laugh but soon gets quiet, rubbing her stomach."
    "You can hear her mutter quietly to herself."
    maya "Baby."
    pc "Oh, I’ve been meaning to ask you. How is Tessa doing?"
    image maya_stage_3_event_62 = "/maya/events/stage3/62.webp"
    scene maya_stage_3_event_62
    maya "I’m not too sure. I talked to her the other day, and she said she wants to come in and talk to Mr. Vanthorne about her pregnancy."
    pc "Why does she want to do that?"
    maya "She wouldn’t tell me much. She said she’s having unexpected complications with her pregnancy and wanted to explain it to Mr. Vanthorne."
    pc "Oh no, is the baby okay?"
    image maya_stage_3_event_63 = "/maya/events/stage3/63.webp"
    scene maya_stage_3_event_63
    maya "Yeah, the baby’s fine. Both her and the baby are healthy, at least that’s what she tells me."
    pc "That’s good."
    maya "I’m just not sure her coming in will help with her situation."
    maya "I’m sure whatever baby weight she gains she can lose quickly and be back to work in no time, once the baby comes."
    image maya_stage_3_event_64 = "/maya/events/stage3/64.webp"
    scene maya_stage_3_event_64
    "Maya seems to cheer up a bit."
    maya "Oh, you barely touched your burger and fries."
    pc "I completely forgot, I still have my burger."
    image maya_stage_3_event_65 = "/maya/events/stage3/65.webp"
    scene maya_stage_3_event_65
    maya "Would you mind if I bum a few fries?"
    pc "Not at all."
    image maya_stage_3_event_66 = "/maya/events/stage3/66.webp"
    scene maya_stage_3_event_66
    "Maya helps you finish your meal."
    image maya_stage_3_event_67 = "/maya/events/stage3/67.webp"
    scene maya_stage_3_event_67
    "After the meal, Maya struggles to get up. Trying to figure out the best way to get up with her enormous stomach."
    image maya_stage_3_event_68 = "/maya/events/stage3/68.webp"
    scene maya_stage_3_event_68
    maya "I might have overdone it a little."
    "Maya smiles while rubbing her stomach."
    image maya_stage_3_event_69 = "/maya/events/stage3/69.webp"
    scene maya_stage_3_event_69
    maya "Thanks for coming out with me tonight. I had a lot of fun."
    pc "Me too. I wouldn’t mind doing this again sometime."
    image maya_stage_3_event_70 = "/maya/events/stage3/70.webp"
    scene maya_stage_3_event_70
    maya "Me too. I don’t know about this though."
    image maya_stage_3_event_71 = "/maya/events/stage3/71.webp"
    scene maya_stage_3_event_71
    "Maya pats her big belly."
    maya "Mr. Vanthorne would surely fire me if he saw me like this."
    image maya_stage_3_event_72 = "/maya/events/stage3/72.webp"
    scene maya_stage_3_event_72
    "Maya presses her giant belly against you and kisses you on the cheek."
    image maya_stage_3_event_73 = "/maya/events/stage3/73.webp"
    scene maya_stage_3_event_73
    maya "Thank you. For some reason when I’m around you I feel like my old self. Do you mind walking me home?"
    pc "Not at all."
    image maya_stage_3_event_74 = "/maya/events/stage3/74.webp"
    scene maya_stage_3_event_74
    "You walk Maya home and return to your place."
    stop music fadeout 1.0
    if recollection == False:
        $ maya.weight += 1
        $ daytime += 1
        $ phonecall = 1
    $ mayastage3event = 0
    return


label Maya_Stage_3_Event_2:
    #Event 7
    #End of a BB shift with Amber
    image amber_standing_on_chair_workattire = "/amber/[amber.stage]/standing_on_chair_workattire.webp"
    scene amber_standing_on_chair_workattire
    play music "/music/bb_amber.ogg" if_changed
    amber "Another day, another dollar. Oh shoot! I just remembered there’s something I need from the grocery store across town before they close."
    amber "Can you finish up here by yourself?"
    pc "Not a problem."
    amber "Thanks."

    image maya_stage_3_event_75 = "/maya/events/stage3/75.webp"
    scene maya_stage_3_event_75
    "Amber leaves. You finish cleaning up for the night when suddenly there’s a knock on the door. You can also hear crying."
    $ unknownname = 'Womans voice'
    image maya_stage_3_event_76 = "/maya/events/stage3/76.webp"
    scene maya_stage_3_event_76
    unknown "Amber, are you still here? I need to talk to someone."
    #Pc unlocks the door and opens it.
    pc "Sorry, Amber left for the night…"
    $ unknownname = 'Unknown'
    image maya_stage_3_event_77 = "/maya/events/stage3/77.webp"
    scene maya_stage_3_event_77
    play music "/music/sadness.ogg" if_changed
    "Maya rushes in and embraces you."
    maya "Oh, [playername], he’s letting her go. He wants her to pack up her things and leave. I don’t know what to do."
    pc "Calm down. Take deep breaths."
    image maya_stage_3_event_78 = "/maya/events/stage3/78.webp"
    scene maya_stage_3_event_78
    "Maya lets go of her embrace. Wipes the tears from her eyes."
    pc "Why don’t we sit down, and you can tell me what happened."
    image maya_stage_3_event_79 = "/maya/events/stage3/79.webp"
    scene maya_stage_3_event_79
    "You lead Maya to a nearby booth."
    "Maya takes a few deep breaths, composing herself."
    image maya_stage_3_event_80 = "/maya/events/stage3/80.webp"
    scene maya_stage_3_event_80
    maya "It seems like 100 years ago. I was sitting right here when I saw that flier on the door looking for dancers."
    maya "I really never thought I’d ever do anything like that or if they would be interested in someone like me, but they did. I loved my job."
    maya "I’ve made many friends over the years, and now Mr. Vanthorne is taking everything I love away from me."
    pc "What happened?"
    image maya_stage_3_event_81 = "/maya/events/stage3/81.webp"
    scene maya_stage_3_event_81
    maya "It’s Tessa. She finally came in to talk to Mr. Vanthorne."
    pc "I’m guessing it didn’t go too well."
    maya "Tessa couldn’t even get a word in once he saw her, it was over. He never even gave her a chance to tell her side of the story."
    pc "I thought you said she might have a chance once she loses the baby weight."
    image maya_stage_3_event_82 = "/maya/events/stage3/82.webp"
    scene maya_stage_3_event_82
    maya "That’s what I thought too, until I saw her."
    pc "What’s wrong?"
    maya "Remember I said she had unexpected complications."
    pc "I do, but you said Tessa and the baby are fine."
    maya "It’s Babies."
    pc "Shes having twins?"
    maya "The way she looks. I’d be surprised if it’s just twins. She’s huge. She looks like she’s been past due for weeks."
    #Maya sighs
    image maya_stage_3_event_83 = "/maya/events/stage3/83.webp"
    scene maya_stage_3_event_83
    maya "It’s no wonder she thought she had more time before showing. It felt like yesterday that she just found out she was pregnant."
    pc "Can’t her husband or boyfriend say something to Mr. Vanthorne? Tell him he’s being unreasonable or something."
    #Maya looks down at the table.
    image maya_stage_3_event_84 = "/maya/events/stage3/84.webp"
    scene maya_stage_3_event_84
    maya "We are all she has left."
    pc "Did they leave her?"
    image maya_stage_3_event_85 = "/maya/events/stage3/85.webp"
    scene maya_stage_3_event_85
    maya "In a way, yes. But it would be better if I started from the beginning."
    maya "Tessa was the first person at the club I got really close to. She started working there shortly after me. So we were kinda in the same boat together."
    maya "About a year after we started, she grew close to one of her regulars. It was a perfect match. They loved each other so much, and shortly after that, they were married."
    maya "She never really wanted to stay in this business. She always talked about having kids and starting a family, but the money was good so they both decided that starting a family would have to wait."
    maya "They were only married for three years before they found out that he had cancer and didn’t have much time left."
    maya "He fought it for a little over a year, but in the end, it got him."
    #Tears start running down Maya’s face.
    image maya_stage_3_event_86 = "/maya/events/stage3/86.webp"
    scene maya_stage_3_event_86
    maya "But before he died, they went to a sperm bank to save a part of him for if she ever wanted to start a family she could."
    maya "At the time, she never would have thought of having a kid without a father figure being around, but over time her heart couldn’t handle not having a part of him in her life."
    maya "So she took his sample and went to a fertility clinic. So that’s why we are all she has left."
    pc "That’s so sad."
    maya "How could you tell someone not to do something like that? I’m sure she wasn’t expecting this though."
    image maya_stage_3_event_87 = "/maya/events/stage3/87.webp"
    scene maya_stage_3_event_87
    "Suddenly there's a knock on the door."
    image maya_stage_3_event_88 = "/maya/events/stage3/88.webp"
    scene maya_stage_3_event_88
    play music "/music/date_cozy.ogg" if_changed
    "You get up to see who it is. When you open the door, it’s Tessa."
    tessa "Is Maya here?"
    image maya_stage_3_event_89 = "/maya/events/stage3/89.webp"
    scene maya_stage_3_event_89
    "You are shocked at how big she has gotten since the last time you saw her. From her breasts the size of melons and her beach ball size belly."
    image maya_stage_3_event_90 = "/maya/events/stage3/90.webp"
    scene maya_stage_3_event_90
    tessa "I guess I look a little different from the first time we met."
    image maya_stage_3_event_91 = "/maya/events/stage3/91.webp"
    scene maya_stage_3_event_91
    maya "Tessa, what are you doing here?"
    image maya_stage_3_event_92 = "/maya/events/stage3/92.webp"
    scene maya_stage_3_event_92
    tessa "I came looking for you. The girls saw you leave the club heading this way, and I knew you had a friend that worked here."
    tessa "So, I put two and two together and thought maybe that’s where you went."
    pc "Please come have a seat."
    tessa "Thank you. I’m not used to walking this much like this."
    image maya_stage_3_event_93 = "/maya/events/stage3/93.webp"
    scene maya_stage_3_event_93
    "Tessa squeezes by just fitting in the booth, holding up her belly she sits next to Maya."
    image maya_stage_3_event_94 = "/maya/events/stage3/94.webp"
    scene maya_stage_3_event_94
    maya "I’m sorry about Mr. Vanthorne."
    tessa "Maya, please stop apologizing for that man. I did this to myself. I didn’t expect this either, but I’m still glad I did it. I guess the doctor is really the one to blame."
    #"Tessa rubs her belly."
    image maya_stage_3_event_95 = "/maya/events/stage3/95.webp"
    scene maya_stage_3_event_95
    tessa "They’re shocked by this too."
    maya "What do you mean? Didn’t they say that this was a possibility?"
    tessa "Nope. They have never seen a result like this before."
    maya "But I’ve heard stories of people doing in vitro fertilization and having a bunch of babies at one time."
    image maya_stage_3_event_96 = "/maya/events/stage3/96.webp"
    scene maya_stage_3_event_96
    tessa "That’s true, but I was trying out a new type of in vitro."
    tessa "Normal in vitro, they fertilize the egg outside the body and at a certain point they plant the eggs, but sometimes the babies come with different side effects from doing it that way."
    tessa "This new way is a little more natural. They still harvest the eggs, but they kinda just throw them in and hope one sticks."
    tessa "Most of the time it takes multiple sessions to get just one, and they did have one person that had twins. But then there's me."
    image maya_stage_3_event_97 = "/maya/events/stage3/97.webp"
    scene maya_stage_3_event_97
    "Tessa pats her giant belly."
    tessa "I’m having triplets."
    pc "Triplets!"
    image maya_stage_3_event_98 = "/maya/events/stage3/98.webp"
    scene maya_stage_3_event_98
    maya "But what about your job? What are you going to do for money?"
    tessa "I wish I could have stayed at the club. I’m sure if the old owners were still there I’d still be dancing until the babies come. I still have the moves."
    image maya_stage_3_event_99 = "/maya/events/stage3/99.webp"
    scene maya_stage_3_event_99
    "Tessa gets up and starts swaying side to side. Throwing her weight around."
    image maya_stage_3_event_100 = "/maya/events/stage3/100.webp"
    scene maya_stage_3_event_100
    pause
    image maya_stage_3_event_101 = "/maya/events/stage3/101.webp"
    scene maya_stage_3_event_101
    "You are fixated on how big Tessa's belly has gotten, but couldn’t shake this feeling Maya was watching you."
    image maya_stage_3_event_102 = "/maya/events/stage3/102.webp"
    scene maya_stage_3_event_102
    tessa "Wow, that’s exhausting but it feels amazing having your weight pull you in different directions. I guess I know how you felt when…"
    maya "Tessa, this isn’t a game. How are you going to support yourself once the babies come."
    tessa "I’ll figure something out. I still have the girls for support."
    maya "Tessa, of course you will always have our support. We’ll do anything for you."
    #Pc gets an idea
    pc "Why don’t you girls go on strike?"
    image maya_stage_3_event_103 = "/maya/events/stage3/103.webp"
    scene maya_stage_3_event_103
    maya "I don’t know."
    pc "Hear me out. If you girls all go on strike, he’ll have no one working the floor. You could make him enforce the rules you want and treat you girls with respect or he’ll lose the business."
    maya "That sounds good, but the last part is what worries me. If he loses the business, we are all out of jobs. I wouldn’t want that kind of pressure to put on the rest of the girls."
    pc "Have you ever asked them?"
    image maya_stage_3_event_104 = "/maya/events/stage3/104.webp"
    scene maya_stage_3_event_104
    tessa "I know I would have done anything for you. If you would have asked for anything. I’m sure all the girls feel the same way and would like for things to change too."
    maya "I don’t know. I don’t want to rush into something like this. I’ll need to think about it."
    pc "Take your time, no need to rush."
    tessa "Yeah, take you time with this. I just appreciate that you are even thinking about doing it."
    maya "If it was just you and me, I’d do it in a heartbeat, but there are all the other girls to think about too."
    tessa "I get it."
    #Maya hugs Tessa.
    image maya_stage_3_event_105 = "/maya/events/stage3/105.webp"
    scene maya_stage_3_event_105
    maya "No matter what I decide. I’m going to support you anyway I can."
    tessa "I know."
    maya "Now, let’s get you home."
    #Maya turns to Pc
    image maya_stage_3_event_106 = "/maya/events/stage3/106.webp"
    scene maya_stage_3_event_106
    maya "Thanks for listening. I hate to burden you with all my problems."
    pc "You're no burden. I just wish there was more I could do for you."
    image maya_stage_3_event_107 = "/maya/events/stage3/107.webp"
    scene maya_stage_3_event_107
    "Maya smiles and kisses you on the cheek."
    image maya_stage_3_event_108 = "/maya/events/stage3/108.webp"
    scene maya_stage_3_event_108
    maya "I know, I just need some time to think about it."
    "Maya leaves with Tessa. You finish cleaning up and head home."
    stop music fadeout 1.0
    if recollection == False:
        $ maya.weight += 1.5
    $ mayastage3event2 = 0
    return

label Maya_Stage_3_Event_3:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Maya', dialogue=dialogue_one)
    $ msg ("Hey [playername], would you like to grab something to eat? Maybe Bunny Bites?", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("I’d love to. Is this a date?")
            pause
            $ msg ("Oh, no. I just need someone to vent to. I really like talking to you.", who=1)
            pause
            $ msg ("I like listening.")
            pause
            $ msg ("I’m glad you do. I’ll see you soon.", who=1)
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Sorry, I have other plans today.")
            pause
            $ msg ("That’s okay, maybe some other time.", who=1)
            pause
            $ hide_messenger()
            return


    #Bunny Bites
    image maya_stage_3_event_109 = "/maya/events/stage3/109.webp"
    scene maya_stage_3_event_109
    play music "/music/bb_amber.ogg" if_changed
    "You see Maya sitting in a booth. Amber is there talking to her."
    image maya_stage_3_event_110 = "/maya/events/stage3/110.webp"
    scene maya_stage_3_event_110
    amber "There he is. Your date has arrived."
    maya "Stop it. I already told you this isn’t a date."
    amber "Fine, it’s “not” a date. I should get back to work. You two have fun."
    image maya_stage_3_event_111 = "/maya/events/stage3/111.webp"
    scene maya_stage_3_event_111
    "Amber leaves and you take a seat across from Maya."
    maya "She can be so embarrassing sometimes."
    pc "She’s a blast to work with."
    #Marie comes over
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Oh hey [playername]. Are you on a date?"
    pc "No, we…"
    marie "Just joking. Amber told me to give you a hard time. Anyways, what can I get you?"
    pc "I’ll get my usual."
    marie "And for you?"
    image maya_stage_3_event_112 = "/maya/events/stage3/112.webp"
    scene maya_stage_3_event_112
    maya "I think I’ll have what he’s having."
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Two [playername] specials coming right up."
    "As Marie leaves, you notice a little smile from her."
    image maya_stage_3_event_113 = "/maya/events/stage3/113.webp"
    scene maya_stage_3_event_113
    "You have a bad feeling about it, she might be up to her old tricks."
    pc "So what did you want to talk about? You didn’t hit anyone again."
    image maya_stage_3_event_114 = "/maya/events/stage3/114.webp"
    scene maya_stage_3_event_114
    maya "Ha ha, you're so funny. No, I’ve just been thinking about what you said the other day. Going on strike and stuff."
    pc "I still think it’s a good idea."
    image maya_stage_3_event_115 = "/maya/events/stage3/115.webp"
    scene maya_stage_3_event_115
    maya "I agree it’s an idea, but is it a good one? Sure, I can make that decision, but it’s not just me who would be affected if there was a strike."
    maya "I know Tessa would be all for it, but there’s Rayla, Jaimy, and Gina I have to think about as well."
    maya "I also can’t forget all the part-timers too. If we don’t have everyone's full cooperation, it’ll be doomed to fail."
    pc "I didn’t even think about the part-timers. I guess it would be too risky."
    image maya_stage_3_event_116 = "/maya/events/stage3/116.webp"
    scene maya_stage_3_event_116
    maya "Maybe, maybe not. Ever since that night, I keep thinking 'what if?' So the last few days I’ve talked to as many of the girls I could find to see what they thought."
    pc "Wouldn’t you get in trouble if Mr. Vanthorne found out about this?"
    maya "Yeah, but I needed to know. I didn’t go around asking them “Hey, do you want to go on strike?” I discreetly asked them how they felt things are going."
    pc "So, what did you find out?"
    image maya_stage_3_event_117 = "/maya/events/stage3/117.webp"
    scene maya_stage_3_event_117
    maya "That pretty much everyone has an issue with how Mr. Vanthorne runs the place. I blame myself for letting it get this bad."
    pc "It’s not your fault."
    maya "I’ve been so focused on the full-timers like Tessa, Gina, Rayla, and Jaimy. I never really went out of my way to see how this affected the rest."
    pc "So, what are you going to do?"
    maya "I don’t know. Ahh! This is so frustrating. I just need time to think. Usually when I’m stressed, I turn to…"
    #Marie shows up with their food
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Here you go, two [playername] specials."
    "Marie loads the table full of food. As she leaves, Marie winks at you."
    image maya_stage_3_event_118 = "/maya/events/stage3/118.webp"
    scene maya_stage_3_event_118
    maya "Oh wow, this is your usual? It smells so good."
    pc "Sorry, I should have warned you about…"
    image maya_stage_3_event_119 = "/maya/events/stage3/119.webp"
    scene maya_stage_3_event_119
    "Before you are able to finish your sentence, Maya starts inhaling the food in front of her."
    image maya_stage_3_event_120 = "/maya/events/stage3/120.webp"
    scene maya_stage_3_event_120
    "You watch as Maya devours her portion of the meal. Her belly getting rounder and rounder."
    image maya_stage_3_event_121 = "/maya/events/stage3/121.webp"
    scene maya_stage_3_event_121
    window hide
    pause
    image maya_stage_3_event_122 = "/maya/events/stage3/122.webp"
    scene maya_stage_3_event_122
    pause
    image maya_stage_3_event_123 = "/maya/events/stage3/123.webp"
    scene maya_stage_3_event_123
    "Maya show no sign of slowing down grabbing anything that’s in front of her, she starts eating your portion too."
    image maya_stage_3_event_124 = "/maya/events/stage3/124.webp"
    scene maya_stage_3_event_124
    "Soon Maya stops, leaning back, revealing her very large belly, leaving only a burger and some fries for you."
    image maya_stage_3_event_125 = "/maya/events/stage3/125.webp"
    scene maya_stage_3_event_125
    maya "Oh, I feel so much better. That was just what I needed. I couldn’t think with all those delicious smells coming from the kitchen."
    image maya_stage_3_event_126 = "/maya/events/stage3/126.webp"
    scene maya_stage_3_event_126
    "Maya rubs her belly and sees all she has left for you."
    maya "I’m sorry, I kinda got carried away there. I even ate a little bit of your food."
    pc "That’s totally fine. I’m happy with just this anyways. I’m just glad you feel better."
    image maya_stage_3_event_127 = "/maya/events/stage3/127.webp"
    scene maya_stage_3_event_127
    maya "Yeah. It really cleared up my mind."
    pc "Have you made a decision?"
    maya "I think so. I feel that most, if not all, the part-timers would join us if we went on strike."
    maya "So now I just need to get Tessa, Gina, Rayla, and Jaimy together and see what they want to do. I won’t do this if not everyone is willing to do it."
    pc "I think that’s a great idea."
    maya "I still have something I need to do before I can do that. Plus, I need to find a place to have it, but I’m sure I’ll think of something."
    image maya_stage_3_event_128 = "/maya/events/stage3/128.webp"
    scene maya_stage_3_event_128
    "Maya smiles at you. She seems relieved, like she finally got some weight off her shoulders."
    maya "Could you maybe come to it? I could use all the support I can."
    pc "Wouldn’t miss it for the world."
    maya "Thanks, I really appreciate it."
    image maya_stage_3_event_129 = "/maya/events/stage3/129.webp"
    scene maya_stage_3_event_129
    "You finish your meal, then you both get up."
    image maya_stage_3_event_130 = "/maya/events/stage3/130.webp"
    scene maya_stage_3_event_130
    maya "Thanks again for letting me vent. This really helped."
    image maya_stage_3_event_131 = "/maya/events/stage3/131.webp"
    scene maya_stage_3_event_131
    "Maya boops you on the nose and kisses you on the cheek. You walk Maya out and head home."
    stop music fadeout 1.0
    if recollection == False:
        $ maya.weight = 88
        $ daytime += 1
        $ phonecall = 1
    $ mayastage3event3 = 0
    return


label Maya_Stage_4_Event_1:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Maya', dialogue=dialogue_one)
    $ msg ("Hey [playername], I need a favor. Everyone is ready to meet with me, but we need a place where Mr. Vanthorne won't find us. Can we use your place?", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Of course you can.")
            pause
            $ msg ("Thank you so much! I really hope we aren’t intruding on you.", who=1)
            pause
            $ msg ("Just give me a little time to clean things up and get ready for it.")
            pause
            $ msg ("Sounds good. I’ll be there a little bit before the meeting to help you set up. I’ll bring some snacks for the meeting as well. I’ll see you soon, and thank you.", who=1)
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Sorry, I have other plans today.")
            pause
            $ msg ("That’s okay; we can try again some other time.", who=1)
            pause
            $ hide_messenger()
            return

    scene player_room
    "You hear the doorbell ring."
    image maya_stage_4_event_1 = "/maya/events/stage4/1.webp"
    scene maya_stage_4_event_1
    "Maya is standing in the doorway with a stack of donut boxes, barely visible over them."
    maya "Hey [playername], can you grab a few of these?"
    pc "Of course. Wow, how many people are you expecting?"
    maya "Just four. I guess I got carried away with ordering. Everything looks so good, and when I’m stressed, my stomach kinda takes over my thinking."
    #Maya and Pc place the boxes on the table.
    image maya_stage_4_event_2 = "/maya/events/stage4/2.webp"
    scene maya_stage_4_event_2
    maya "Well, it looks like you already got everything all set for the meeting. I can’t thank you enough for everything you’re doing for us."
    image maya_stage_4_event_3 = "/maya/events/stage4/3.webp"
    scene maya_stage_4_event_3
    "Maya hugs you."
    pc "I’m still following the rules, no touching."
    maya "This is your place. You can touch if you want."
    image maya_stage_4_event_4 = "/maya/events/stage4/4.webp"
    scene maya_stage_4_event_4
    "You hold Maya in a warm embrace."
    pc "You're doing the right thing. I’m sure you will get support from all of them."
    image maya_stage_4_event_5 = "/maya/events/stage4/5.webp"
    scene maya_stage_4_event_5
    maya "I hope so. I am still really stressed about this whole situation."
    maya "I had to do everything to control myself from diving into these boxes and eating everything before getting here."
    maya "But now I’m here, I don’t feel too stressed. I still can’t believe we are doing this."
    pc "So it was never this bad before?"
    image maya_stage_4_event_6 = "/maya/events/stage4/6.webp"
    scene maya_stage_4_event_6
    maya "Sure, you had an occasional client that would come in and slap someone on the butt or try to cop a feel, but we always had the old owners to step in and deal with the situation."
    maya "But now they're gone."
    pc "Why did they sell the place? Was it not doing well?"
    maya "Business was booming, but they were getting old and wanted to retire."
    pc "I see."
    image maya_stage_4_event_7 = "/maya/events/stage4/7.webp"
    scene maya_stage_4_event_7
    maya "The worst part is this all could have been avoided if… (Sigh)"
    pc "What’s wrong? How could you have avoided this?"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/maya/events/stage4/vid1.webm" loop
    show movie with dissolve
    maya "Mr. Vanthorne wasn’t the first person to offer to buy the club. They first offered it to me."
    pc "Really? Why didn’t you buy it?"
    maya "I tried, but in the end, I couldn’t get the money they wanted for the place. Did you know it wasn’t called Velvet Shadows?"
    pc "It wasn’t?"
    maya "Nope, it was called Curvy Corner, but Mr. Vanthorne changed it."
    pc "Why did he do that?"
    maya "I suspect he changed it because 'Curvy Corner' might imply larger dancers, and he prefers supermodels on his dance floor."
    maya "So, he swiftly renamed it to Velvet Shadows."
    pc "I like the name. I wish I could have seen it back then."
    #Maya smiles at Pc.
    stop movie
    image maya_stage_4_event_8 = "/maya/events/stage4/8.webp"
    scene maya_stage_4_event_8
    maya "You wouldn’t mind having bigger girls on the stage?"
    pc "I’d say be yourself. I want to see a happy dancer, not someone trying to be something they're not."
    image maya_stage_4_event_9 = "/maya/events/stage4/9.webp"
    scene maya_stage_4_event_9
    "Maya looks surprised by your answer."
    maya "Be myself? Oh, what time is it?"
    pc "It’s just a little past eight. What time did you tell them to come?"
    image maya_stage_4_event_10 = "/maya/events/stage4/10.webp"
    scene maya_stage_4_event_10
    maya "Eight."
    pc "I’m sure they are on their way."
    maya "Yeah. I’m sure they are."
    image maya_stage_4_event_11 = "/maya/events/stage4/11.webp"
    scene maya_stage_4_event_11
    "Maya seems unaware that she has opened the first box of donuts and started eating."
    image maya_stage_4_event_12 = "/maya/events/stage4/12.webp"
    scene maya_stage_4_event_12
    "Slowly Maya works her way through the first box of donuts, nervously checking her phone. She moves onto the next box."
    pc "I’m sure they are just running late. They will be here."
    image maya_stage_4_event_13 = "/maya/events/stage4/13.webp"
    scene maya_stage_4_event_13
    maya "Maybe, but you’d think they would have texted or something."
    image maya_stage_4_event_14 = "/maya/events/stage4/14.webp"
    scene maya_stage_4_event_14
    "Maya's pace speeds up. Soon, box two is gone."
    image maya_stage_4_event_15 = "/maya/events/stage4/15.webp"
    scene maya_stage_4_event_15
    "You notice Maya’s belly getting bigger with every donut as she finishes box three and starts on box four."
    image maya_stage_4_event_16 = "/maya/events/stage4/16.webp"
    scene maya_stage_4_event_16
    "Maya fixates on her phone, waiting for some kind of message from the others. Eating donut after donut, still not noticing her ever-growing stomach."
    image maya_stage_4_event_17 = "/maya/events/stage4/17.webp"
    scene maya_stage_4_event_17
    "You watch as she moves onto the last box."
    image maya_stage_4_event_18 = "/maya/events/stage4/18.webp"
    scene maya_stage_4_event_18
    "Maya’s shorts that was once covering her small belly now stretched tight across it, unable to hide it anymore."
    image maya_stage_4_event_19 = "/maya/events/stage4/19.webp"
    scene maya_stage_4_event_19
    "Maya reaches into the last box of donuts and finds nothing there."
    maya "I knew this was a bad idea."
    image maya_stage_4_event_20 = "/maya/events/stage4/20.webp"
    scene maya_stage_4_event_20
    "Maya tosses her phone to the side."
    pc "I’m sure they have a good reason for being late."
    image maya_stage_4_event_21 = "/maya/events/stage4/21.webp"
    scene maya_stage_4_event_21
    "Maya leans back and starts rubbing her stomach."
    maya "They should have been here by now. Can you grab me another box of donuts? I’m so stressed out right now I feel I could eat a bakery."
    pc "I think you ate the last box."
    image maya_stage_4_event_22 = "/maya/events/stage4/22.webp"
    scene maya_stage_4_event_22
    "Maya sits up and looks at all the empty boxes of donuts."
    maya "Did I just eat all the donuts that I brought for the meeting?"
    pc "I’m afraid so."
    image maya_stage_4_event_23 = "/maya/events/stage4/23.webp"
    scene maya_stage_4_event_23
    maya "Great! Not only is no one coming. I’ve…"
    "Suddenly Maya’s phone dinged with a message."
    image maya_stage_4_event_24 = "/maya/events/stage4/24.webp"
    scene maya_stage_4_event_24
    "She scrambles for her phone."
    pc "Is it them?"
    image maya_stage_4_event_25 = "/maya/events/stage4/25.webp"
    scene maya_stage_4_event_25
    "Maya looks relieved."
    maya "Yes. They're on their way and will be here in fifteen minutes."
    pc "That’s great! I told you they would come."
    image maya_stage_4_event_26 = "/maya/events/stage4/26.webp"
    scene maya_stage_4_event_26
    "Maya looks around at all the empty boxes, then at her giant belly."
    maya "I can’t have them see me like this."
    pc "We have a little time before they get here. I think I have a large sweater you can wear."
    image maya_stage_4_event_27 = "/maya/events/stage4/27.webp"
    scene maya_stage_4_event_27
    maya "That should work. While you go get that, I’ll clean up here."
    pc "Sounds like a plan."
    scene player_room
    "You head to your room to grab the sweater while Maya cleans up all the empty boxes."
    image maya_stage_4_event_28 = "/maya/events/stage4/28.webp"
    scene maya_stage_4_event_28
    pc "Here you go."
    "Maya takes it and puts it on."
    image maya_stage_4_event_29 = "/maya/events/stage4/29.webp"
    scene maya_stage_4_event_29
    maya "Well, how do I look?"
    image maya_stage_4_event_30 = "/maya/events/stage4/30.webp"
    scene maya_stage_4_event_30
    "Maya spins around."
    image maya_stage_4_event_31 = "/maya/events/stage4/31.webp"
    scene maya_stage_4_event_31
    maya "Are you able to tell?"
    pc "I think that hides it pretty well."
    maya "That’s good."
    "The doorbell rings."
    image maya_stage_4_event_32 = "/maya/events/stage4/32.webp"
    scene maya_stage_4_event_32
    maya "Perfect timing."
    "You go and answer the door."
    image maya_stage_4_event_33 = "/maya/events/stage4/33.webp"
    scene maya_stage_4_event_33
    "Tessa is in front even bigger than before, with Rayla, Jaimy, and Gina behind her, all holding more boxes of donuts."
    tessa "Sorry, we’re late. I hope it’s okay that we brought snacks."
    pc "Come in."
    #Pc leads the girls into the living room.
    image maya_stage_4_event_34 = "/maya/events/stage4/34.webp"
    scene maya_stage_4_event_34
    pc "You can put those on the table there and make yourselves comfortable."
    tessa "I hope we didn’t make you worry."
    gina "Yeah, we’re sorry for being late. That bastard pulled us aside right when we were about to leave to talk to us about “the rules”."
    jaimy "Yeah, I’m getting pretty sick and tired of his rules."
    image maya_stage_4_event_35 = "/maya/events/stage4/35.webp"
    scene maya_stage_4_event_35
    rayla "This is what I think of his rules."
    "Rayla grabs a donut from the box and takes a big bite."
    image maya_stage_4_event_36 = "/maya/events/stage4/36.webp"
    scene maya_stage_4_event_36
    rayla "Oh my god! It’s so good. I can’t remember the last time I’ve had one of these."
    image maya_stage_4_event_37 = "/maya/events/stage4/37.webp"
    scene maya_stage_4_event_37
    "The rest of the girls all grab a donut and start eating, except for Maya."
    image maya_stage_4_event_38 = "/maya/events/stage4/38.webp"
    scene maya_stage_4_event_38
    gina "You're not lying, they taste amazing. Maya, you have to try them. We got a box for everyone."
    image maya_stage_4_event_39 = "/maya/events/stage4/39.webp"
    scene maya_stage_4_event_39
    maya "Oh, I’m good."
    image maya_stage_4_event_40 = "/maya/events/stage4/40.webp"
    scene maya_stage_4_event_40
    rayla "There she goes trying to set a good example for everyone."
    image maya_stage_4_event_41 = "/maya/events/stage4/41.webp"
    scene maya_stage_4_event_41
    tessa "Is it okay if I have yours then? I’m constantly hungry."
    "Tessa pats her large pregnant belly."
    image maya_stage_4_event_42 = "/maya/events/stage4/42.webp"
    scene maya_stage_4_event_42
    gina "I bet you are, with all those mouths to feed. You’re huge! You remind me of that time when Maya…"
    image maya_stage_4_event_43 = "/maya/events/stage4/43.webp"
    scene maya_stage_4_event_43
    maya "Alright, enough chit-chat. Yes, you can have mine Tessa. So, let’s get down to business. Do you know why we’re here?"
    jaimy "Tessa just said it was something to do with Mr. Vanthorne."
    maya "I want to talk to you about doing something drastic. I, for one, am sick and tired of how we are treated there."
    image maya_stage_4_event_44 = "/maya/events/stage4/44.webp"
    scene maya_stage_4_event_44
    gina "Here here!"
    "Gina cheers with her mouth full of donut."
    rayla "What do you have in mind?"
    image maya_stage_4_event_45 = "/maya/events/stage4/45.webp"
    scene maya_stage_4_event_45
    maya "I don’t want to pressure anyone. If even one of you isn't on board, we won’t proceed."
    #Still with her mouth full
    image maya_stage_4_event_46 = "/maya/events/stage4/46.webp"
    scene maya_stage_4_event_46
    gina "Come on, tell us already."
    image maya_stage_4_event_47 = "/maya/events/stage4/47.webp"
    scene maya_stage_4_event_47
    jaimy "Gina, slow down, you're going to choke."
    image maya_stage_4_event_48 = "/maya/events/stage4/48.webp"
    scene maya_stage_4_event_48
    rayla "Come on, you two. We came here to hear what Maya wanted to talk about. Let’s hear her out. How drastic are we talking about?"
    image maya_stage_4_event_49 = "/maya/events/stage4/49.webp"
    scene maya_stage_4_event_49
    maya "I want to go on strike."
    #With her mouth full
    image maya_stage_4_event_50 = "/maya/events/stage4/50.webp"
    scene maya_stage_4_event_50
    gina "Oh hell yeah! A strike, let’s fucking go!"
    image maya_stage_4_event_51 = "/maya/events/stage4/51.webp"
    scene maya_stage_4_event_51
    gina "*Cough* *cough*"
    jaimy "See, I told you."
    gina "*cough* I’m okay. I'm 100 percent with you."
    image maya_stage_4_event_52 = "/maya/events/stage4/52.webp"
    scene maya_stage_4_event_52
    rayla "I’m not as enthusiastic about it as Gina, but I truly don’t see any other way."
    image maya_stage_4_event_53 = "/maya/events/stage4/53.webp"
    scene maya_stage_4_event_53
    maya "There’s a chance we’ll lose our job."
    jaimy "That’s a risk I’m willing to take."
    image maya_stage_4_event_54 = "/maya/events/stage4/54.webp"
    scene maya_stage_4_event_54
    rayla "Me too."
    gina "Mr. Vanthorne is going down."
    rayla "So what are we asking for?"
    image maya_stage_4_event_55 = "/maya/events/stage4/55.webp"
    scene maya_stage_4_event_55
    maya "I want him to respect our personal space and to get rid of his dumb diet restrictions."
    maya "Also, he should let whoever wants to be a dancer there, dance. No matter their shape or size."
    jaimy "Would that mean Tessa could come back?"
    maya "Yes, if she wants too."
    image maya_stage_4_event_56 = "/maya/events/stage4/56.webp"
    scene maya_stage_4_event_56
    tessa "I don’t want anyone to do it just for me."
    jaimy "Nonsense, of course we would. You’re part of the family."
    image maya_stage_4_event_57 = "/maya/events/stage4/57.webp"
    scene maya_stage_4_event_57
    rayla "I wouldn’t mind not having my ass grabbed or poked every time I walk by some creep."
    gina "I could eat whatever I want. I’ve been starving myself for what seems like forever."
    gina "I started making a list of foods I wanted to try if I got the chance."
    image maya_stage_4_event_58 = "/maya/events/stage4/58.webp"
    scene maya_stage_4_event_58
    "Maya seems happy with how the conversation is going."
    maya "Is it safe to say everyone is on board with this?"
    image maya_stage_4_event_59 = "/maya/events/stage4/59.webp"
    scene maya_stage_4_event_59
    jaimy "I’m in."
    image maya_stage_4_event_60 = "/maya/events/stage4/60.webp"
    scene maya_stage_4_event_60
    rayla "We do this together."
    gina "Let’s fucking do this!"
    image maya_stage_4_event_61 = "/maya/events/stage4/61.webp"
    scene maya_stage_4_event_61
    tessa "Thank you, everyone."
    image maya_stage_4_event_62 = "/maya/events/stage4/62.webp"
    scene maya_stage_4_event_62
    maya "I’ve made a list of things we should do before we go ahead."
    image maya_stage_4_event_63 = "/maya/events/stage4/63.webp"
    scene maya_stage_4_event_63
    "Maya and the girls discuss the plan for the strike while enjoying their treats."
    "After a while, everyone seems happy with the plan and knows what they need to do to get ready."
    image maya_stage_4_event_64 = "/maya/events/stage4/64.webp"
    scene maya_stage_4_event_64
    "They all hug, and Maya leads them to the front door."
    image maya_stage_4_event_65 = "/maya/events/stage4/65.webp"
    scene maya_stage_4_event_65
    "She comes back, taking off the sweater and hands it back to you."
    image maya_stage_4_event_66 = "/maya/events/stage4/66.webp"
    scene maya_stage_4_event_66
    pc "That went well."
    maya "I think so too."
    image maya_stage_4_event_67 = "/maya/events/stage4/67.webp"
    scene maya_stage_4_event_67
    "Maya looks down and rubs her still large stomach."
    pc "I wasn’t surprised when you gave your donuts to Tessa."
    maya "To be honest, I wish I didn’t share. Watching all of them eating their donuts. I had to hold myself back from grabbing mine back."
    pc "You did just eat six boxes by yourself."
    maya "Yeah, I guess that is a lot."
    image maya_stage_4_event_68 = "/maya/events/stage4/68.webp"
    scene maya_stage_4_event_68
    "Maya looks like she is deep in thought. She snaps out of it."
    image maya_stage_4_event_69 = "/maya/events/stage4/69.webp"
    scene maya_stage_4_event_69
    maya "Anyways, thanks for letting us do this here."
    pc "No Problem."
    maya "Would you like some help cleaning up?"
    pc "No worries, I got this."
    image maya_stage_4_event_70 = "/maya/events/stage4/70.webp"
    scene maya_stage_4_event_70
    maya "I just hope we are doing the right thing."
    pc "I think you are. You should do what your heart wants to do."
    maya "What my heart wants to do."
    image maya_stage_4_event_71 = "/maya/events/stage4/71.webp"
    scene maya_stage_4_event_71
    "Maya looks down at her stomach then up to you."
    image maya_stage_4_event_72 = "/maya/events/stage4/72.webp"
    scene maya_stage_4_event_72
    maya "Maybe I will."
    image maya_stage_4_event_73 = "/maya/events/stage4/73.webp"
    scene maya_stage_4_event_73
    "Maya kisses you on the cheek."
    image maya_stage_4_event_74 = "/maya/events/stage4/74.webp"
    scene maya_stage_4_event_74
    maya "Thank you, for doing this."
    "Maya leaves, and you finish cleaning up."
    if recollection == False:
        $ maya.weight += 1
        $ daytime += 1
        $ phonecall = 1
    $ mayastage4event = 0
    return



label Maya_Stage_4_Event_2:
    #Event 10
    #Pc’s house
    "You get a message from Maya."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Maya', dialogue=dialogue_one)
    $ msg ("Today's the big day. We are officially on strike. We would all love it if you came down and showed us some support.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Of course, I would.")
            pause
            $ msg ("That's great! We will see you soon.", who=1)
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Can’t today. Maybe some other time.")
            pause
            $ msg ("Don’t worry. I don’t think this will work itself out overnight. So come by anytime when you get the chance.", who=1)
            pause
            $ hide_messenger()
            return

    #Outside Velvet Shadows
    image maya_stage_4_event_75 = "/maya/events/stage4/75.webp"
    scene maya_stage_4_event_75
    "You hear chanting from a crowd of people outside the club. you see the girls holding signs. It's a pretty good-sized group."
    image maya_stage_4_event_76 = "/maya/events/stage4/76.webp"
    scene maya_stage_4_event_76
    "They must have talked to the part-timers and got them on board too. Maya notices you and waves you over."
    image maya_stage_4_event_77 = "/maya/events/stage4/77.webp"
    scene maya_stage_4_event_77
    maya "You made it."
    pc "Wouldn't miss it. Looks like a good turnout."
    maya "Yeah. I think we have all the part-timers on board too. Everyone wants something to change."
    pc "That's great."
    image maya_stage_4_event_78 = "/maya/events/stage4/78.webp"
    scene maya_stage_4_event_78
    maya "Hey, would you like to hold a sign and join us for a while?"
    pc "Sure, I'd love to."
    "Maya hands a sign to you with the word 'respect' written on it."
    image maya_stage_4_event_79 = "/maya/events/stage4/79.webp"
    scene maya_stage_4_event_79
    "You join the group, chatting with them." 
    "You look around the group and sees that Tessa has made it."
    image maya_stage_4_event_80 = "/maya/events/stage4/80.webp"
    scene maya_stage_4_event_80
    "Rayla and Jaimy are talking to passersby who are curious about what the strike is about."
    "There are a few people that go in, but they soon come out after figuring out there is no entertainment in there."
    image maya_stage_4_event_81 = "/maya/events/stage4/81.webp"
    scene maya_stage_4_event_81
    "You see Gina yelling her heart out. Looks like she's put on a few pounds since the meeting."
    "You wonder if she already got started on her list of foods she's always wanted to try. You turn to say something to Maya when you hear slow clapping."
    "*Clap* … *Clap*"
    image maya_stage_4_event_82 = "/maya/events/stage4/82.webp"
    scene maya_stage_4_event_82
    "You turn to see Mr. Vanthorne standing there."
    vanthorne "Bravo! Bravo!"
    image maya_stage_4_event_83 = "/maya/events/stage4/83.webp"
    scene maya_stage_4_event_83
    "Mr. Vanthorne notices you."
    vanthorne "I see they got you to be part of this shit show. You don't happen to have anything to do with this."
    #Maya steps in.
    image maya_stage_4_event_84 = "/maya/events/stage4/84.webp"
    scene maya_stage_4_event_84
    maya "He has nothing to do with this."
    vanthorne "Oh really. I suppose after all this time you never had the nerve to do anything like this."
    image maya_stage_4_event_85 = "/maya/events/stage4/85.webp"
    scene maya_stage_4_event_85
    vanthorne "Then all of a sudden this guy shows up and now you all want “respect.” Don't treat me like a fool."
    vanthorne "If you only knew how the real world works missy. If you all would just listen to me, you'd all be racking in the dough."
    vanthorne "I know how the world works, men want a nice tight ass and feel a nice set of firm breasts. Men don't want to see some chunky woman dancing around on stage."
    image maya_stage_4_event_86 = "/maya/events/stage4/86.webp"
    scene maya_stage_4_event_86
    vanthorne "They want supermodels, not some cow like your friend over there."
    #Mr. Vanthorne points at Tessa.
    image maya_stage_4_event_87 = "/maya/events/stage4/87.webp"
    scene maya_stage_4_event_87
    maya "Hey! You take that back."
    vanthorne "Did I hurt her feelings? I'm just looking out for what's best for my business. This “respect” and “all body types are beautiful” is a bunch of bullshit."
    vanthorne "I can be a reasonable man so if you end this farce and come back to work. I'll look the other way and past this little charade of a protest and not punish anyone."
    maya "Only if you meet our demands."
    image maya_stage_4_event_88 = "/maya/events/stage4/88.webp"
    scene maya_stage_4_event_88
    protesters "Yeah!"
    image maya_stage_4_event_89 = "/maya/events/stage4/89.webp"
    scene maya_stage_4_event_89
    vanthorne "Ha! Not a chance. Fine, have it your way. We will see who can last longer. My offer won't last forever."
    image maya_stage_4_event_90 = "/maya/events/stage4/90.webp"
    scene maya_stage_4_event_90
    "Mr. Vanthorne leaves and heads back into the club."
    image maya_stage_4_event_91 = "/maya/events/stage4/91.webp"
    scene maya_stage_4_event_91
    pc "Sounds like he’s not budging."
    maya "Which is fine with me. We planned on this taking a while."
    maya "One of the things I had the girls do was save up all their tips since our meeting to cover their living expenses for a while."
    image maya_stage_4_event_92 = "/maya/events/stage4/92.webp"
    scene maya_stage_4_event_92
    maya "Only thing we haven’t budgeted for was food during the protest."
    pc "Maybe I can help with your food situation."
    image maya_stage_4_event_93 = "/maya/events/stage4/93.webp"
    scene maya_stage_4_event_93
    maya "Really! How?"
    pc "I might know someone who would be able to help out."
    maya "That would be great."
    pc "Let me make a call quick."
    "You call Marie."
    image maya_stage_4_event_94 = "/maya/events/stage4/94.webp"
    scene maya_stage_4_event_94
    marie "Hey [playername], what’s up? You're not scheduled to work today."
    pc "No, I’m at the protest outside Velvet Shadows."
    marie "I’ve been hearing a lot about that today. Seems like everyone is talking about it."
    marie "Poor things, the way they have been treated. The owner should be ashamed of himself."
    pc "I was calling to see if Bunny Bites would like to help out."
    image maya_stage_4_event_95 = "/maya/events/stage4/95.webp"
    scene maya_stage_4_event_95
    marie "Of course, what do you have in mind?"
    pc "They could really use some food while they protest. Do you think we could provide them food while they protest?"
    pc "Not sure how long the protest will take, but if you can possibly give them a discount or something."
    marie "Nonsense, it’s on the house. We will support them as long as it takes. How many orders are you thinking?"
    pc "I’m not sure."
    marie "I’ll see what I can do. Come by in a little bit, and I’ll have everything ready."
    pc "Thanks a lot."
    marie "See you soon."
    image maya_stage_4_event_96 = "/maya/events/stage4/96.webp"
    scene maya_stage_4_event_96
    "You hang up the phone and walk over to Maya."
    pc "I solved your food situation. Bunny Bites will be providing the food, till the strike is over."
    image maya_stage_4_event_97 = "/maya/events/stage4/97.webp"
    scene maya_stage_4_event_97
    maya "Really! Is this Amber's doing?"
    pc "It’s actually the manager, Marie. She said she’d be happy to support you all."
    maya "That’s great. I didn’t realize we had so much support on the outside."
    pc "I’m going to go get the order."
    maya "Thank you. I’ll let the others know the good news."
    image maya_stage_4_event_98 = "/maya/events/stage4/98.webp"
    scene maya_stage_4_event_98
    "You go and get the order and brings it to the protest group."
    "Everyone looks happy to have gotten something to eat."
    image maya_stage_4_event_99 = "/maya/events/stage4/99.webp"
    scene maya_stage_4_event_99
    "You spend a little more time helping out at the protest before heading home."
    if recollection == False:
        $ maya.weight += 1
        $ daytime += 1
        $ phonecall = 1
    $ mayastage4event2 = 0
    return



label Maya_Stage_4_Event_3:
    #Event 11
    #Pc house

    "You go to the strike."
    #Outside Velvet Shadows
    image maya_stage_4_event_100 = "/maya/events/stage4/100.webp"
    scene maya_stage_4_event_100
    maya "Hey [playername]. Care to join us today?"
    pc "Don't mind if I do."
    image maya_stage_4_event_101 = "/maya/events/stage4/101.webp"
    scene maya_stage_4_event_101
    "Maya hands you a sign."
    image maya_stage_4_event_102 = "/maya/events/stage4/102.webp"
    scene maya_stage_4_event_102
    "You protest for a while when suddenly the sky gets dark."
    image maya_stage_4_event_103 = "/maya/events/stage4/103.webp"
    scene maya_stage_4_event_103
    maya "Looks like it's going to rain. We should call it for today. Would you mind helping me gather our stuff and bringing it back to my place?"
    pc "I'd be happy to help."
    image maya_stage_4_event_104 = "/maya/events/stage4/104.webp"
    scene maya_stage_4_event_104
    "Maya tells the rest that she's calling off the protest today due to weather while you go around collecting signs."
    image maya_stage_4_event_105 = "/maya/events/stage4/105.webp"
    scene maya_stage_4_event_105
    "On your way to Maya's place, it starts to pour. You hurry over to her place."
    #Maya’s Apartment
    #Drenched Maya and Pc made it to her apartment.
    image maya_stage_4_event_106 = "/maya/events/stage4/106.webp"
    scene maya_stage_4_event_106
    maya "Phew, that was close. I'm soaked."
    image maya_stage_4_event_107 = "/maya/events/stage4/107.webp"
    scene maya_stage_4_event_107
    "Maya strips down to her underwear."
    image maya_stage_4_event_108 = "/maya/events/stage4/108.webp"
    scene maya_stage_4_event_108
    maya "Much better, make yourself comfortable. If you'd like, I can throw your clothes in the dryer. If you want to wait out the rain here."
    pc "Umm, sure."
    image maya_stage_4_event_109 = "/maya/events/stage4/109.webp"
    scene maya_stage_4_event_109
    "You strip off your wet clothes, down to your underwear and hand them to Maya."
    image maya_stage_4_event_110 = "/maya/events/stage4/110.webp"
    scene maya_stage_4_event_110
    maya "I'll get these drying. You can sit on the couch over there."
    "Maya points over to her couch. She leaves, and you go over to the couch and sit down."
    image maya_stage_4_event_111 = "/maya/events/stage4/111.webp"
    scene maya_stage_4_event_111
    "Maya comes back now wearing her PJs and joins you on the couch."
    image maya_stage_4_event_112 = "/maya/events/stage4/112.webp"
    scene maya_stage_4_event_112
    maya "I should have checked what the weather was going to be like today. I'm sorry for getting you in this mess."
    pc "I don't mind."
    maya "There's just so much to do and think about. Weather was the last thing on my mind."
    pc "How do you feel the protest is going?"
    image maya_stage_4_event_113 = "/maya/events/stage4/113.webp"
    scene maya_stage_4_event_113
    maya "I think it's going well. Everyone still seems enthusiastic about this whole thing."
    pc "That's good. Any idea if Mr. Vanthorne is budging on this yet?"
    maya "No clue. I'm kinda hoping he doesn't."
    pc "Wouldn't that mean he'd go out of business and have to sell the place? You could be out of a job if he does that."
    maya "Not if I buy it from him. I told you the previous owners offered me the place first."
    pc "Yeah, but you couldn't get the money to buy it."
    image maya_stage_4_event_114 = "/maya/events/stage4/114.webp"
    scene maya_stage_4_event_114
    maya "That was true last time, but this time I'm ready. I am not going to let that opportunity slip by me again."
    maya "Before we went on strike, I made sure I had enough money to buy the club back."
    pc "Oh wow."
    maya "I'm even willing to pay him more for it than what he originally paid for."
    pc "How much did he spend on the club?"
    maya "$400,000, and if I have to, I could offer him as much as $500,000. There is no way he'd turn down that offer."
    pc "He'd be crazy not to. You seem to have thought of everything."
    #Maya smiles at Pc.
    image maya_stage_4_event_115 = "/maya/events/stage4/115.webp"
    scene maya_stage_4_event_115
    maya "And now all we have to do is wait."
    pc "That's pretty smart. If you don't mind me asking, how did you get into this business? I feel that you should have gone to college instead of working in a strip club."
    image maya_stage_4_event_116 = "/maya/events/stage4/116.webp"
    scene maya_stage_4_event_116
    maya "It's kind of a long story."
    pc "I have time. Doesn't look like the rain is letting up anytime soon."
    maya "I guess you're right. Well, I did go to college. I did really well there too. Top of my class."
    pc "That's impressive."
    image maya_stage_4_event_117 = "/maya/events/stage4/117.webp"
    scene maya_stage_4_event_117
    maya "I thought so too, but after college, no one wanted to hire me."
    pc "They'd be crazy not to. Why didn't they?"
    maya "They had their reasons."
    #Maya looks a little sad.
    image maya_stage_4_event_118 = "/maya/events/stage4/118.webp"
    scene maya_stage_4_event_118
    maya "That's something I'm not quite ready to talk about."
    maya "Anyways, I told you already that I was sitting at Bunny Bites when I saw that flyer on the wall looking for dancers."
    maya "Dancing was always something I was passionate about, but since college, I was so focused on studying I never had time for it."
    maya "So I took a chance. I needed money since I didn't have a job and I guess it kinda worked out."
    pc "What did you go to school for?"
    image maya_stage_4_event_119 = "/maya/events/stage4/119.webp"
    scene maya_stage_4_event_119
    maya "Business."
    pc "So running a business like the Velvet Shadows is something you should be able to do."
    maya "I know exactly how the business works. The old owners had me do their book work before Mr. Vanthorne took the place over."
    "There is a ding from the other room."
    maya "Well, it sounds like your clothes are dry."
    image maya_stage_4_event_120 = "/maya/events/stage4/120.webp"
    scene maya_stage_4_event_120
    "Maya gets up and grabs your clothes."
    image maya_stage_4_event_121 = "/maya/events/stage4/121.webp"
    scene maya_stage_4_event_121
    maya "Looks like the rain is letting up too. You should be able to make it back to your place."
    pc "Thanks for drying my clothes off."
    image maya_stage_4_event_122 = "/maya/events/stage4/122.webp"
    scene maya_stage_4_event_122
    maya "No problem. Thank you for helping me get all my stuff back to my apartment. I'm sure if I didn't have your help, we would have lost our signs and stuff."
    pc "I'm just happy to have helped out. I think you are doing a great job motivating the staff in the strike. You seem to have everything under control with all your bases covered."
    maya "I hope so. Mr. Vanthorne has been really stubborn, but hopefully soon he'll meet our demands or will be forced to sell, and when that day comes I'll be ready."
    image maya_stage_4_event_123 = "/maya/events/stage4/123.webp"
    scene maya_stage_4_event_123
    "Maya smiles and kisses you on the cheek."
    image maya_stage_4_event_124 = "/maya/events/stage4/124.webp"
    scene maya_stage_4_event_124
    maya "It's been nice talking with you about this stuff. You have a safe walk home. I'll see you around."
    "You leave and head home."
    $ mayastage4event3 = 0
    if recollection == False:
        $ maya.weight += 1.5
        $ daytime += 1
        jump freetime
    return



label Maya_Stage_4_Event_4:
    #Event 12
    #Pc's house

    "You go to the strike."
    #Outside Velvet Shadows
    image maya_stage_4_event_125 = "/maya/events/stage4/125.webp"
    scene maya_stage_4_event_125
    "Getting closer to Velvet Shadows, you notice how quiet it is."
    "There's no chanting, and you see the girls all huddled around in little groups talking to each other. You walk up to Rayla."
    image maya_stage_4_event_126 = "/maya/events/stage4/126.webp"
    scene maya_stage_4_event_126
    pc "Hey Rayla, what's going on?"
    rayla "Oh hi [playername], we're not sure. Mr. Vanthorne has the place all locked up. He's never done this before."
    #Maya comes over
    image maya_stage_4_event_127 = "/maya/events/stage4/127.webp"
    scene maya_stage_4_event_127
    maya "[playername], you made it! I think Mr. Vanthorne is cracking."
    maya "He came by not too long ago with a few other guys I haven't seen before and went into the club and locked the doors behind them."
    pc "Any clue who they might be?"
    rayla "Mr. Vanthorne was pointing out stuff to them. I think they might be realtors. He's probably showing them around the property."
    maya "That's what I was thinking as well."
    pc "That's good news, right? Isn't that what you wanted?"
    maya "Yeah, it is, but I wasn't expecting it so soon. I'm still pretty nervous about the whole thing."
    image maya_stage_4_event_128 = "/maya/events/stage4/128.webp"
    scene maya_stage_4_event_128
    "You hear the door of the club open and see two men followed by Mr. Vanthorne come out. They are deep in discussion."
    image maya_stage_4_event_129 = "/maya/events/stage4/129.webp"
    scene maya_stage_4_event_129
    "They seem to have come to an agreement. Mr. Vanthorne shakes the two men's hands, and the two men leave."
    image maya_stage_4_event_130 = "/maya/events/stage4/130.webp"
    scene maya_stage_4_event_130
    "Mr. Vanthorne turns and smiles at the crowd of protesters and walks over."
    image maya_stage_4_event_131 = "/maya/events/stage4/131.webp"
    scene maya_stage_4_event_131
    maya "So, are you willing to meet our demands?"
    vanthorne "Meet your demands? *chuckles* No. I've just finished showing those fine men around the place."
    vanthorne "They felt this is a perfect place to build a nice high-end apartment complex."
    maya "Wait, what, an apartment complex?"
    vanthorne "Oh, Did you think I was just going to put this place up for sale and just let anyone get a hold of it."
    vanthorne "I'd rather see this place torn down before letting anyone like the likes of you get your hands on it."
    image maya_stage_4_event_132 = "/maya/events/stage4/132.webp"
    scene maya_stage_4_event_132
    rayla "You can't do this!"
    vanthorne "I most certainly can. You all left me no choice."
    image maya_stage_4_event_133 = "/maya/events/stage4/133.webp"
    scene maya_stage_4_event_133
    maya "Mr. Vanthorne, please be reasonable. There are a lot of girls here that need this job."
    vanthorne "What can I say? I tried to be reasonable."
    image maya_stage_4_event_134 = "/maya/events/stage4/134.webp"
    scene maya_stage_4_event_134
    gina "Reasonable my ass! You didn't even try!"
    maya "Gina, stop. Mr. Vanthorne. Please, I'll buy the club from you."
    image maya_stage_4_event_135 = "/maya/events/stage4/135.webp"
    scene maya_stage_4_event_135
    vanthorne "Oh really, what are you offering?"
    maya "I'll pay you $400,000."
    vanthorne "Ha! Don't make me laugh. You'll have to do better than that."
    maya "Fine, I'll give you $500,000. That's my final offer."
    vanthorne "Final offer you say, well you see those gentlemen I was just talking to are offering me $900,000 for the place."
    maya "$900,000!"
    image maya_stage_4_event_136 = "/maya/events/stage4/136.webp"
    scene maya_stage_4_event_136
    "Maya looks defeated."
    image maya_stage_4_event_137 = "/maya/events/stage4/137.webp"
    scene maya_stage_4_event_137
    vanthorne "Gosh, and I'd really feel bad if I backed out of this deal, but I guess if you can come up with, let's say, 1 million, maybe that wouldn't feel so bad."
    #Mr. Vanthorne smiles
    image maya_stage_4_event_138 = "/maya/events/stage4/138.webp"
    scene maya_stage_4_event_138
    maya "A million! Mr. Vanthorne, you can't be serious. $500,000 was everything I had."
    vanthorne "Well, I guess you really don't want it."
    maya "I'll do anything to get the club back."
    maya "Please Mr. Vanthorne, I know you own a bunch of other places. Why can't you just let us have this one."
    image maya_stage_4_event_139 = "/maya/events/stage4/139.webp"
    scene maya_stage_4_event_139
    vanthorne "All my other businesses aren't a pain in my ass as this one. Well, you better figure out how to get more money without a job."
    vanthorne "*chuckles* But you know what, I'm in a giving mood. You've got some time before I finalize the other deal with those two." 
    vanthorne "There's a significant sum of money in play, so if you can come up with money and get that to me before I sign the place over to them, then the club is yours." 
    vanthorne "What do you say?"
    image maya_stage_4_event_140 = "/maya/events/stage4/140.webp"
    scene maya_stage_4_event_140
    maya "I don't know."
    image maya_stage_4_event_141 = "/maya/events/stage4/141.webp"
    scene maya_stage_4_event_141
    vanthorne "I see. I'll give you a little bit of time to think it over, but don't take too long or this opportunity will slip by your fingers again."
    "Mr. Vanthorne leaves."
    image maya_stage_4_event_142 = "/maya/events/stage4/142.webp"
    scene maya_stage_4_event_142
    rayla "Where are we supposed to come up with that kind of dough?"
    jaimy "Maya, what are we going to do?"
    gina "This can't be happening. Maya, please say something."
    image maya_stage_4_event_143 = "/maya/events/stage4/143.webp"
    scene maya_stage_4_event_143
    "Maya looks lost for words. She sees the panic building in the crowd."
    maya "I'm sorry. Let's call it for today, I need time to think."
    "The crowd disperses quietly, leaving Maya deep in thought."
    image maya_stage_4_event_144 = "/maya/events/stage4/144.webp"
    scene maya_stage_4_event_144
    pc "Are you okay?"
    maya "No, I'm not okay. I never thought he'd do something like this."
    maya "A million dollars! How are we supposed to come up with that kind of money so quickly? I need to go home and think."
    pc "Would you like me to walk you home?"
    image maya_stage_4_event_145 = "/maya/events/stage4/145.webp"
    scene maya_stage_4_event_145
    maya "No, I need some alone time. Thanks for coming by. I wish things turned out differently."
    image maya_stage_4_event_146 = "/maya/events/stage4/146.webp"
    scene maya_stage_4_event_146
    "Maya grabs her things and walks away. With nothing left for you to do, you head home."
    $ mayastage4event4 = 0
    if recollection == False:
        $ maya.weight = 93
        $ daytime += 1
        jump freetime
    return

label Maya_Stage_5_Event_1:
    #Event 13
    #Pc's house
    scene player_room
    "While you are figuring out what to do for the day, you hear a knock at the door."
    image maya_stage_5_event_1 = "/maya/events/stage5/1.webp"
    scene maya_stage_5_event_1
    "You answer the door and see Rayla and Jaimy standing there."
    rayla "Good, you're home."
    pc "What's up?"
    image maya_stage_5_event_2 = "/maya/events/stage5/2.webp"
    scene maya_stage_5_event_2
    jaimy "Have you heard from Maya recently?"
    pc "Haven't seen her since she told everyone to go home from the strike. What's wrong?"
    image maya_stage_5_event_3 = "/maya/events/stage5/3.webp"
    scene maya_stage_5_event_3
    rayla "Same here. No one has heard from her since then. We went by Velvet Shadows to see if maybe she was protesting by herself, but no one was there."
    rayla "We did see Mr. Vanthorne, and he told us he needs an answer by tonight."
    jaimy "We need to find Maya and let her know."
    pc "Have you tried calling her?"
    image maya_stage_5_event_4 = "/maya/events/stage5/4.webp"
    scene maya_stage_5_event_4
    rayla "Of course, but she's not picking up."
    jaimy "We've left a bunch of messages, but still no response."
    pc "I'll see what I can do."
    image maya_stage_5_event_5 = "/maya/events/stage5/5.webp"
    scene maya_stage_5_event_5
    jaimy "Thanks, [playername]."
    rayla "Yeah, thanks. Please let us know if you find her."
    pc "Will do."
    image maya_stage_5_event_6 = "/maya/events/stage5/6.webp"
    scene maya_stage_5_event_6
    "Rayla and Jaimy leave. You decide to check Maya's apartment first."

    #Maya’s apartment
    image maya_stage_5_event_7 = "/maya/events/stage5/7.webp"
    scene maya_stage_5_event_7
    maya "Please go away." 
    pc "Maya, it's me. Everyone is worried about you. I also have an urgent message for you."
    maya "Fine, come in."
    image maya_stage_5_event_8 = "/maya/events/stage5/8.webp"
    scene maya_stage_5_event_8
    "You open the door and notice boxes of empty food containers scattered all over the place." 
    "You don't see Maya, so you head towards the bedroom door." 
    image maya_stage_5_event_9 = "/maya/events/stage5/9.webp"
    scene maya_stage_5_event_9
    "When you open it, you see Maya sitting up in her bed wearing nothing but a bra and panties, surrounded by empty boxes of food. Her stomach is as round as ever."
    image maya_stage_5_event_10 = "/maya/events/stage5/10.webp"
    scene maya_stage_5_event_10
    pc "Maya, what are you doing?"
    maya "Trying to eat my problems away, but it's not working. I ran out of food."
    image maya_stage_5_event_11 = "/maya/events/stage5/11.webp"
    scene maya_stage_5_event_11
    "Maya starts to cry."
    pc "Everyone is worried about you. They keep asking about a plan."
    image maya_stage_5_event_12 = "/maya/events/stage5/12.webp"
    scene maya_stage_5_event_12
    maya "What's the point? Mr. Vanthorne has won. There's no way we can raise that kind of money."
    pc "I know it sounds impossible, but you should at least try."
    maya "How can we come up with $500,000 in such a short amount of time?"
    pc "I'm sure we can think of something, but Mr. Vanthorne needs to know by the end of the day if you're going to try." 
    pc "You should at least tell him you are and buy yourself some time."
    maya "I guess that wouldn't hurt. I'll call him after you leave, okay? You can leave now. Also, let everyone know I'm okay."
    pc "I'm not leaving."
    image maya_stage_5_event_13 = "/maya/events/stage5/13.webp"
    scene maya_stage_5_event_13
    "You approach Maya's bed and sit down next to her. She collapses onto your arms."
    "You comfort Maya as she cries, and look around at all the empty food containers."
    pc "Why are you doing this to yourself?"
    image maya_stage_5_event_14 = "/maya/events/stage5/14.webp"
    scene maya_stage_5_event_14
    maya "I didn't know what to do. I couldn't think, I was so hungry. I couldn't stop myself." 
    maya "I just wanted to stop feeling so hungry so I could think, and I couldn't even do that. I've let everyone down."
    pc "Don't say that. They all knew the risk before this even started. It's not over yet."
    image maya_stage_5_event_15 = "/maya/events/stage5/15.webp"
    scene maya_stage_5_event_15
    maya "How can we get the money?"
    pc "Let's think about how people raise money for things."
    maya "Well, there are fundraisers or selling stuff."
    pc "Ok. What kind of fundraisers?"
    #Maya seems to be calming down. 
    image maya_stage_5_event_16 = "/maya/events/stage5/16.webp"
    scene maya_stage_5_event_16
    maya "Ahh, it's no use, I can't think right now. You didn't happen to bring anything to eat?"
    pc "I'm afraid I didn't." 
    image maya_stage_5_event_17 = "/maya/events/stage5/17.webp"
    scene maya_stage_5_event_17
    maya "I could go for another couple dozen of those donuts right now. I must look pretty crazy right now with such a huge belly, wanting more food."
    pc "I think you still look beautiful."
    image maya_stage_5_event_18 = "/maya/events/stage5/18.webp"
    scene maya_stage_5_event_18
    maya "Really? You're not disgusted by this."
    pc "Not at all."
    image maya_stage_5_event_19 = "/maya/events/stage5/19.webp"
    scene maya_stage_5_event_19
    maya "What are we going to do? I just can't keep hiding here, stuffing my face."
    pc "This is not something that only you need to do. Why not get the girls together and try and brainstorm an idea."
    maya "I suppose having more people thinking of something is better than one."
    pc "Exactly."
    image maya_stage_5_event_20 = "/maya/events/stage5/20.webp"
    scene maya_stage_5_event_20
    "Maya hugs you." 
    image maya_stage_5_event_21 = "/maya/events/stage5/21.webp"
    scene maya_stage_5_event_21
    maya "I can't thank you enough for all the help you've given." 
    maya "I'll get on the phone with Mr. Vanthorne and tell him the deal is on, and I'll send a message to all the girls about meeting to think of something we can do." 
    maya "Do you think we can do it over at your place again?"
    pc "Of course."
    image maya_stage_5_event_22 = "/maya/events/stage5/22.webp"
    scene maya_stage_5_event_22
    "You can't help but look at how large Maya's belly is. Maya sees you staring." 
    image maya_stage_5_event_23 = "/maya/events/stage5/23.webp"
    scene maya_stage_5_event_23
    maya "Sorry, I wasn't expecting company. I'm glad it was you. I hate for the girls to see me like this. Can we keep this our little secret?"
    pc "Totally."
    image maya_stage_5_event_24 = "/maya/events/stage5/24.webp"
    scene maya_stage_5_event_24
    "Maya boops you on the nose."
    scene outside
    "You leave and head home."
    if recollection == False:
        $ maya.weight += 1.5

    $ mayastage5event = 0
    return

label Maya_Stage_5_Event_2:
    #Event 14
    #Pc’s House
    scene player_room
    "Your phone rings. You glance at the screen and answer."
    image maya_stage_5_event_25 = "/maya/events/stage5/25.webp"
    scene maya_stage_5_event_25
    maya "Hey [playername]! The girls are ready to meet up. Are we good to come over?"
    pc "Absolutely! I'll see you all soon."

    image maya_stage_5_event_26 = "/maya/events/stage5/26.webp"
    scene maya_stage_5_event_26
    "Maya arrives first, shortly followed by the rest of the group."
    image maya_stage_5_event_27 = "/maya/events/stage5/27.webp"
    scene maya_stage_5_event_27
    pause
    image maya_stage_5_event_28 = "/maya/events/stage5/28.webp"
    scene maya_stage_5_event_28
    pause
    image maya_stage_5_event_29 = "/maya/events/stage5/29.webp"
    scene maya_stage_5_event_29
    pause
    image maya_stage_5_event_30 = "/maya/events/stage5/30.webp"
    scene maya_stage_5_event_30
    maya "Thanks for coming, everyone! I want to apologize right off the bat for not getting back to you sooner."
    rayla "I'm just relieved you're okay."
    jaimy "I was really worried about you. So glad to hear from you!"
    image maya_stage_5_event_31 = "/maya/events/stage5/31.webp"
    scene maya_stage_5_event_31
    gina "Stop with the pleasantries! What's the plan? You mentioned brainstorming ideas in your message."
    maya "Honestly, I'm a bit blank right now. Does anyone have suggestions for raising funds?"
    image maya_stage_5_event_32 = "/maya/events/stage5/32.webp"
    scene maya_stage_5_event_32
    tessa "What if we did a bake sale? I know places that successfully do that. Though, I'll admit I'm not exactly a master baker."
    image maya_stage_5_event_33 = "/maya/events/stage5/33.webp"
    scene maya_stage_5_event_33
    gina "Same here! Baking is not my strong suit."
    maya "I like the idea, but let's put that one on hold. Anyone else have anything?"
    image maya_stage_5_event_34 = "/maya/events/stage5/34.webp"
    scene maya_stage_5_event_34
    rayla "How about a car wash? I bet we could attract attention if we wore bikinis. Those old pin-up calendars always had girls washing cars!"
    image maya_stage_5_event_35 = "/maya/events/stage5/35.webp"
    scene maya_stage_5_event_35
    tessa "I'm not sure how much help I can be with that."
    "Tessa pats her large pregnant belly, emphasizing her point."
    image maya_stage_5_event_36 = "/maya/events/stage5/36.webp"
    scene maya_stage_5_event_36
    jaimy "I think Rayla's on to something here."
    image maya_stage_5_event_37 = "/maya/events/stage5/37.webp"
    scene maya_stage_5_event_37
    maya "We need something everyone can pitch in for."
    image maya_stage_5_event_38 = "/maya/events/stage5/38.webp"
    scene maya_stage_5_event_38
    jaimy "Not the car wash, I'm talking about the pin-up calendar.  We could dress up in our cutest swimsuits, take pictures, and sell them!"
    maya "You really think we can raise $500,000 from calendars?"
    rayla "Actually, we only need to make about $300,000."
    image maya_stage_5_event_39 = "/maya/events/stage5/39.webp"
    scene maya_stage_5_event_39
    gina "Right! When we heard you were putting everything into this, we all decided to pitch in as well."
    maya "You didn't have to do that!"
    image maya_stage_5_event_40 = "/maya/events/stage5/40.webp"
    scene maya_stage_5_event_40
    jaimy "The point is, you're not alone in this. We're all affected by it."
    rayla "Exactly. When we pooled our funds, we came up with just a little over $200,000." 
    rayla "With your $500,000, we only need to raise $300,000 more. If we sell the calendars for $30 each, we need to sell just 10,000 of them."
    image maya_stage_5_event_41 = "/maya/events/stage5/41.webp"
    scene maya_stage_5_event_41
    tessa "Oh wow, only 10,000? That sounds doable!"
    image maya_stage_5_event_42 = "/maya/events/stage5/42.webp"
    scene maya_stage_5_event_42
    gina "Oh, hell yeah! I think we've got a solid plan here."
    image maya_stage_5_event_43 = "/maya/events/stage5/43.webp"
    scene maya_stage_5_event_43
    jaimy "Hold on, Gina. We still need to figure out where to print them and the costs involved."
    image maya_stage_5_event_44 = "/maya/events/stage5/44.webp"
    scene maya_stage_5_event_44
    maya "This definitely feels like the right idea. Let's start looking into it right away!"
    image maya_stage_5_event_45 = "/maya/events/stage5/45.webp"
    scene maya_stage_5_event_45
    rayla "I'll start searching for printing options right now."
    "Rayla grabs her phone and begins typing."
    image maya_stage_5_event_46 = "/maya/events/stage5/46.webp"
    scene maya_stage_5_event_46
    maya "Great! Now we need a good location for the photo shoot."
    image maya_stage_5_event_47 = "/maya/events/stage5/47.webp"
    scene maya_stage_5_event_47
    tessa "Why not do it here? [playername] has a lovely big pool and patio."
    image maya_stage_5_event_48 = "/maya/events/stage5/48.webp"
    scene maya_stage_5_event_48
    maya "Is it alright with you if we shoot some photos here?"
    pc "I'd be crazy to say no to a bunch of beautiful women in bikinis!"
    image maya_stage_5_event_49 = "/maya/events/stage5/49.webp"
    scene maya_stage_5_event_49
    rayla "Perfect! I found a printing place that can deliver the calendars in just a few days." 
    rayla "The cost for each calendar will be about $5. That means we'll need to sell 12,000 calendars to meet our goal."
    maya "That sounds fantastic, Rayla!"
    rayla "I'm emailing them right now to get more details."
    image maya_stage_5_event_50 = "/maya/events/stage5/50.webp"
    scene maya_stage_5_event_50
    maya "Alright, I think we have a solid plan. Can everyone meet back here tomorrow for the photo shoot? If that's okay with you, [playername]."
    pc "Sounds good to me. The sooner, the better!"
    maya "Awesome! Also, everyone should bring something to share for snacks. I have a feeling it's going to be a long day."
    image maya_stage_5_event_51 = "/maya/events/stage5/51.webp"
    scene maya_stage_5_event_51
    gina "Alright! I think I'll swing by the mall and find a new swimsuit."
    jaimy "Mind if I join you?"
    image maya_stage_5_event_52 = "/maya/events/stage5/52.webp"
    scene maya_stage_5_event_52
    maya "Let's all go! We can help each other find the perfect suits."
    "The girls rise, buzzing with excitement as they chatter while leaving. Maya stays behind for a moment."
    image maya_stage_5_event_53 = "/maya/events/stage5/53.webp"
    scene maya_stage_5_event_53
    maya "I know I keep saying this, but thank you. I was foolish to think I could handle this alone." 
    maya "It's comforting to realize how many people truly care about this."
    image maya_stage_5_event_54 = "/maya/events/stage5/54.webp"
    scene maya_stage_5_event_54
    "Maya leans in and kisses you on the cheek."
    image maya_stage_5_event_55 = "/maya/events/stage5/55.webp"
    scene maya_stage_5_event_55
    maya "I'll see you tomorrow!"
    scene player_room
    "She exits, joining the others."

    if recollection == False:
        $ maya.weight += 1
        $ daytime += 1
        $ phonecall = 1
        # to make the next event happen on the next day garantued
        $ maya.fullness = 1
    $ mayastage5event2 = 0
    return



label Maya_Stage_5_Event_3:

    #The Next Day
    image maya_stage_5_event_56 = "/maya/events/stage5/56.webp"
    scene maya_stage_5_event_56
    "Maya is the first to arrive, balancing a stack of donut boxes in her arms."
    maya "Morning, [playername]! Am I the first one here?"
    pc "You sure are. Need a hand with those?"
    maya "I'm good! Just help me resist eating all of them like last time."
    image maya_stage_5_event_57 = "/maya/events/stage5/57.webp"
    scene maya_stage_5_event_57
    "She smiles at you."
    maya "I want to keep my figure until after the shoot."
    image maya_stage_5_event_58 = "/maya/events/stage5/58.webp"
    scene maya_stage_5_event_58
    "She sets the donuts on the table prepared for the group." 
    image maya_stage_5_event_59 = "/maya/events/stage5/59.webp"
    scene maya_stage_5_event_59
    "Soon, the girls trickle in one by one, piling the table high with assorted goodies. Gina arrives last."
    image maya_stage_5_event_60 = "/maya/events/stage5/60.webp"
    scene maya_stage_5_event_60
    pause
    image maya_stage_5_event_61 = "/maya/events/stage5/61.webp"
    scene maya_stage_5_event_61
    pause
    image maya_stage_5_event_62 = "/maya/events/stage5/62.webp"
    scene maya_stage_5_event_62
    gina "I couldn't decide what to bring. We passed this amazing Chinese restaurant at the mall yesterday, so I picked up a bunch of different dishes." 
    gina "Just a heads-up: if you don't like spicy food, steer clear of the dumpling-looking ones. They're super spicy!"
    pc "Just set everything on that table over there."
    image maya_stage_5_event_63 = "/maya/events/stage5/63.webp"
    scene maya_stage_5_event_63
    maya "Alright, everyone! Thanks for being here. Today is going to be a blast. Rayla, any updates from the printing company?"
    rayla "Yes! They got back to me pretty quickly, which is awesome." 
    rayla "They said if we can get them the images by 4 PM today, they'll have 12,000 calendars ready by the end of the week."
    maya "Let's not waste any time! Who wants to go first? I think it should be Gina."
    image maya_stage_5_event_64 = "/maya/events/stage5/64.webp"
    scene maya_stage_5_event_64
    gina "Why me?"
    maya "Because I'm worried that if I leave you alone with all this food, you'll ruin your figure before your shoot!"
    gina "Yeah, yeah, I get it! I'll go change."
    maya "I'll call you out one by one throughout the day. Feel free to snack, but don't overdo it!"
    image maya_stage_5_event_65 = "/maya/events/stage5/65.webp"
    scene maya_stage_5_event_65
    "As Maya and you head out to the patio, the sun shines brightly."
    maya "What a beautiful day!"
    pc "It really is perfect."
    image maya_stage_5_event_66 = "/maya/events/stage5/66.webp"
    scene maya_stage_5_event_66
    "Gina soon struts out in her swimsuit."
    gina "Alright, let's get this over with. I have a box of donuts waiting for me!"
    image maya_stage_5_event_67 = "/maya/events/stage5/67.webp"
    scene maya_stage_5_event_67
    "One by one, the girls come out in their new swimsuits, striking poses for the camera."
    image maya_stage_5_event_68 = "/maya/events/stage5/68.webp"
    scene maya_stage_5_event_68
    window hide
    pause
    image maya_stage_5_event_69 = "/maya/events/stage5/69.webp"
    scene maya_stage_5_event_69
    pause
    image maya_stage_5_event_70 = "/maya/events/stage5/70.webp"
    scene maya_stage_5_event_70
    pause
    image maya_stage_5_event_71 = "/maya/events/stage5/71.webp"
    scene maya_stage_5_event_71
    pause
    image maya_stage_5_event_72 = "/maya/events/stage5/72.webp"
    scene maya_stage_5_event_72
    pause
    image maya_stage_5_event_73 = "/maya/events/stage5/73.webp"
    scene maya_stage_5_event_73
    pause
    image maya_stage_5_event_74 = "/maya/events/stage5/74.webp"
    scene maya_stage_5_event_74
    pause
    image maya_stage_5_event_75 = "/maya/events/stage5/76.webp"
    scene maya_stage_5_event_75
    pause
    image maya_stage_5_event_76 = "/maya/events/stage5/76.webp"
    scene maya_stage_5_event_76
    pause
    image maya_stage_5_event_77 = "/maya/events/stage5/77.webp"
    scene maya_stage_5_event_77
    pause
    image maya_stage_5_event_78 = "/maya/events/stage5/78.webp"
    scene maya_stage_5_event_78
    pause
    image maya_stage_5_event_79 = "/maya/events/stage5/79.webp"
    scene maya_stage_5_event_79
    pause
    image maya_stage_5_event_80 = "/maya/events/stage5/80.webp"
    scene maya_stage_5_event_80
    pause
    image maya_stage_5_event_81 = "/maya/events/stage5/81.webp"
    scene maya_stage_5_event_81
    pause
    image maya_stage_5_event_82 = "/maya/events/stage5/82.webp"
    scene maya_stage_5_event_82
    pause
    image maya_stage_5_event_83 = "/maya/events/stage5/83.webp"
    scene maya_stage_5_event_83
    pause
    image maya_stage_5_event_84 = "/maya/events/stage5/84.webp"
    scene maya_stage_5_event_84
    pc "I think we've got all the shots we need. Now we just need to pick your favorite."
    maya "Sounds good! I'll let the girls know they can head out."
    image maya_stage_5_event_85 = "/maya/events/stage5/85.webp"
    scene maya_stage_5_event_85
    "You return inside, only to find Gina stuffed in a food coma." 
    "You guess Maya was right to have Gina go first."
    image maya_stage_5_event_86 = "/maya/events/stage5/86.webp"
    scene maya_stage_5_event_86
    maya "Great job, everyone! I think we have everything. You're all free to go. Rayla, I'll send you the photos once I've made my selections."
    rayla "I'll be ready for them!"
    image maya_stage_5_event_87 = "/maya/events/stage5/87.webp"
    scene maya_stage_5_event_87
    "Jaimy gently shakes Gina awake and helps her up, struggling with her swollen stomach." 
    image maya_stage_5_event_88 = "/maya/events/stage5/88.webp"
    scene maya_stage_5_event_88
    pause
    image maya_stage_5_event_89 = "/maya/events/stage5/89.webp"
    scene maya_stage_5_event_89
    "Soon, it's just Maya and you left in the room."
    maya "Phew! I'm relieved that it's over. I hope they left me something to eat."
    pc "When do you want to look at the photos?"
    maya "Not until I eat something first. I'm starving!"
    image maya_stage_5_event_90 = "/maya/events/stage5/90.webp"
    scene maya_stage_5_event_90
    "Maya approaches the table, which was once brimming with treats but is now nearly empty, only a few half-eaten boxes left."
    maya "Looks like they didn't leave much for me."
    image maya_stage_5_event_91 = "/maya/events/stage5/91.webp"
    scene maya_stage_5_event_91
    "She quickly finishes off the remaining donuts and baked goods, clearing out the leftovers."
    image maya_stage_5_event_92 = "/maya/events/stage5/92.webp"
    scene maya_stage_5_event_92
    "You watch, amazed by her voracious appetite."
    image maya_stage_5_event_93 = "/maya/events/stage5/93.webp"
    scene maya_stage_5_event_93
    "Suddenly, Maya discovers the bag of dumplings."
    maya "Dumplings? I love dumplings!"
    image maya_stage_5_event_94 = "/maya/events/stage5/94.webp"
    scene maya_stage_5_event_94
    "Before you can warn her, Maya devours the bag in no time."
    image maya_stage_5_event_95 = "/maya/events/stage5/95.webp"
    scene maya_stage_5_event_95
    maya "Wow, those were delicious! Oh, they have quite a kick!"
    image maya_stage_5_event_96 = "/maya/events/stage5/96.webp"
    scene maya_stage_5_event_96
    "She opens her mouth and starts fanning her tongue."
    maya "They're really spicy!"
    pc "Yeah, Gina warned me about those. She said they're super hot."
    image maya_stage_5_event_97 = "/maya/events/stage5/97.webp"
    scene maya_stage_5_event_97
    maya "My mouth is on fire! I need water!"
    pc "I can grab you a glass of water or there's the hose outside if you'd …"
    image maya_stage_5_event_98 = "/maya/events/stage5/98.webp"
    scene maya_stage_5_event_98
    "Before you can finish, Maya bolts out. You quickly follow her." 
    "Outside, Maya turns on the hose and runs the water over her tongue, desperately seeking relief."
    image maya_stage_5_event_99 = "/maya/events/stage5/99.webp"
    scene maya_stage_5_event_99
    maya "It's no use! I can feel the burn all the way down!"
    image maya_stage_5_event_100 = "/maya/events/stage5/100.webp"
    scene maya_stage_5_event_100
    "In a fit of urgency, she shoves the hose into her mouth and starts gulping down water." 
    image maya_stage_5_event_101 = "/maya/events/stage5/101.webp"
    scene maya_stage_5_event_101
    "You watch, wide-eyed, as her midsection begins to swell." 
    image maya_stage_5_event_102 = "/maya/events/stage5/102.webp"
    scene maya_stage_5_event_102
    "Maya greedily drinks, her belly expanding more and more with each gulp." 
    image maya_stage_5_event_103 = "/maya/events/stage5/103.webp"
    scene maya_stage_5_event_103
    "She rubs her growing belly, seemingly savoring the sensation." 
    image maya_stage_5_event_104 = "/maya/events/stage5/104.webp"
    scene maya_stage_5_event_104
    "As she continues, her stomach balloons, nearing the size of a giant beach ball."
    image maya_stage_5_event_105 = "/maya/events/stage5/105.webp"
    scene maya_stage_5_event_105
    "Maya finally stops, relieved as the burning sensation fades."
    maya "I honestly thought it would never end."
    "She sets the hose down and catches you staring at her." 
    image maya_stage_5_event_106 = "/maya/events/stage5/106.webp"
    scene maya_stage_5_event_106
    "Looking down, she finally notices the enormous, water-bloated state of her belly, and a wave of embarrassment washes over her."
    maya "Why do I always end up embarrassing myself around you?"
    pc "There's no need to feel embarrassed. I actually think it's kind of adorable."
    image maya_stage_5_event_107 = "/maya/events/stage5/107.webp"
    scene maya_stage_5_event_107
    maya "Really? You find this cute?"
    "As her embarrassment dissipates, Maya lifts her belly slightly and lets it drop, with the audible sound of the water sloshing inside."
    pc "Do you think this changes how I feel about you?"
    "Once again, a blush creeps onto her cheeks."
    image maya_stage_5_event_108 = "/maya/events/stage5/108.webp"
    scene maya_stage_5_event_108
    maya "Um… how do you feel about me?"
    pc "I really like you. You're strong, passionate, caring, and kind. The list goes on and on." 
    pc "Your appearance doesn't matter to me. Even if you kept growing and turned into a giant beach ball, I'd still like you." 
    pc "Just imagine, I'd have to roll you back inside so we could sort through all the pictures from today."
    image maya_stage_5_event_109 = "/maya/events/stage5/109.webp"
    scene maya_stage_5_event_109
    "Maya chuckles, her mood brightening."
    maya "I'm relieved to know you wouldn't mind rolling me around! I'm really surprised by how big I've gotten." 
    maya "I feel like I'm as big as Tessa! But I'm glad I met you, and I appreciate how you feel about me. Honestly, I like you too."
    image maya_stage_5_event_110 = "/maya/events/stage5/110.webp"
    scene maya_stage_5_event_110
    "She bites her lower lip, as if wanting to say something more."
    pc "We should really go through those photos. We don't want to miss that deadline."
    image maya_stage_5_event_111 = "/maya/events/stage5/111.webp"
    scene maya_stage_5_event_111
    maya "Yes, we should handle that next."
    "Maya's expression saddens, as if she's missed a chance to share what truly was on her mind."
    image maya_stage_5_event_112 = "/maya/events/stage5/112.webp"
    scene maya_stage_5_event_112
    "Together, you head back inside and settle on the couch." 
    "Maya leans against you, resting her head on your shoulder as you scroll through the photos." 
    image maya_stage_5_event_113 = "/maya/events/stage5/113.webp"
    scene maya_stage_5_event_113
    "She seems a little distracted, lost in thought, while her hand absentmindedly rubs her swollen belly."
    "You can hear the gentle sloshing of water inside her." 
    "After a moment, you finalize the selection and send the images to Rayla."
    image maya_stage_5_event_114 = "/maya/events/stage5/114.webp"
    scene maya_stage_5_event_114
    maya "That should be it. I should probably get going now. I can't express how grateful I am for everything you've done."
    "As she stands up to collect her things, she pauses."
    image maya_stage_5_event_115 = "/maya/events/stage5/115.webp"
    scene maya_stage_5_event_115
    maya "Can I ask you for one more favor?"
    pc "Of course."
    maya "Would it be alright if I borrowed that sweater I wore last time this happened?"
    image maya_stage_5_event_116 = "/maya/events/stage5/116.webp"
    scene maya_stage_5_event_116
    "She gestures toward her ballooning belly."
    maya "And maybe a pair of sweatpants? I look like a whale."
    pc "No problem! I'll grab them for you right away."
    "You head upstairs, quickly retrieving the sweater and sweatpants before returning to Maya." 
    image maya_stage_5_event_117 = "/maya/events/stage5/117.webp"
    scene maya_stage_5_event_117
    "She manages to pull on the sweatpants, though she struggles with the sweater, which barely covers half of her enormous belly."
    maya "Well, it's better than nothing, I guess!"
    image maya_stage_5_event_118 = "/maya/events/stage5/118.webp"
    scene maya_stage_5_event_118
    "She leans in and kisses you on the cheek, a warm smile on her face."
    image maya_stage_5_event_119 = "/maya/events/stage5/119.webp"
    scene maya_stage_5_event_119
    maya "Thanks again! I'll see you later."
    "With that, Maya heads out."
    scene player_room

    if recollection == False:
        $ maya.weight += 1
        $ maya.fullness = 0
        $ daytime += 2
        $ phonecall = 1
    $ mayastage5event3 = 0
    return


label Maya_Stage_5_Event_4:
    #Event 15
    #Pc’s House
    scene player_room
    "You get a text from Maya."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Maya', dialogue=dialogue_one)
    $ msg ("Hey [playername].", who=1)
    pause
    $ msg ("Hey Maya, what's up?")
    pause
    $ msg ("Hate to bother you, but could you come over to The Sugar Shop? It's kind of urgent.", who=1)
    pause
    $ msg ("Sure thing, I'm on my way.")
    pause
    $ hide_messenger()
    
    #The Sugar Shop
    image maya_stage_5_event_120 = "/maya/events/stage5/120.webp"
    scene maya_stage_5_event_120
    "You enter The Sugar Shop and spot Maya sitting at a table with their calendars laid out and a couple of big boxes stacked next to her."
    image maya_stage_5_event_121 = "/maya/events/stage5/121.webp"
    scene maya_stage_5_event_121
    maya "Thanks for coming so quickly."
    pc "No problem, what's up?"
    image maya_stage_5_event_122 = "/maya/events/stage5/122.webp"
    scene maya_stage_5_event_122
    maya "I just got a call from Rayla. Jaimy and her are over at the mall selling and are about to run out. Are you able to run over there and stock them up?"
    "Maya pats the boxes next to her."
    maya "Gina was supposed to help with keeping everyone's supplies full, but I haven't heard from her since I sent her over to the mall to help Rayla and Jaimy set up."
    pc "I can definitely do that."
    image maya_stage_5_event_123 = "/maya/events/stage5/123.webp"
    scene maya_stage_5_event_123
    maya "Thanks, you're a lifesaver. We can't afford to lose any sales."
    pc "How are sales?"
    maya "Sales are great. I've already gone through a box myself. I just hope we have enough time, Mr. Vanthorne can call any minute."
    pc "I'll head over right away."
    image maya_stage_5_event_124 = "/maya/events/stage5/124.webp"
    scene maya_stage_5_event_124
    maya "Thanks, [playername]. Oh, and on your way back, can you check on Tessa? She's selling calendars over at Bunny Bites."
    pc "Sure."
    "You grab the boxes of calendars and heads to the mall."
    
    #The Mall
    image maya_stage_5_event_125 = "/maya/events/stage5/125.webp"
    scene maya_stage_5_event_125
    "You enter the mall and see Jaimy and Rayla set up with a table in the center of the lobby." 
    "You walk over."
    image maya_stage_5_event_126 = "/maya/events/stage5/126.webp"
    scene maya_stage_5_event_126
    pc "I have a delivery here for… let's see here…"
    "You pretend to read an order form."
    pc "Two gorgeous girls."
    image maya_stage_5_event_127 = "/maya/events/stage5/127.webp"
    scene maya_stage_5_event_127
    rayla "That would be us."
    "Rayla smiles at you. You set the boxes down."
    jaimy "Perfect timing, we only had a couple left."
    rayla "Yeah, but why are you bringing us the calendars? I thought Gina was supposed to be checking in on us."
    pc "Maya hasn't seen her since she sent her here to help you set up."
    image maya_stage_5_event_128 = "/maya/events/stage5/128.webp"
    scene maya_stage_5_event_128
    jaimy "I bet she's over at the buffet we passed on the way over here."
    rayla "Gina has had nothing but food on her mind ever since we started ignoring Mr. Vanthorne's restrictions."
    jaimy "I can't blame her. I know I went home and stuffed my face until I couldn't eat anymore when we did."
    rayla "I get it, those restrictions were ridiculous. I think I lost like 20 pounds in the first week."
    jaimy "Well, just look at Maya. What she went through was crazy. I don't know how she did it."
    pc "What happened to Maya?"
    image maya_stage_5_event_129 = "/maya/events/stage5/129.webp"
    scene maya_stage_5_event_129
    jaimy "She hasn't said anything to you?"
    pc "I've heard bits and pieces of what happened, but not really."
    image maya_stage_5_event_130 = "/maya/events/stage5/130.webp"
    scene maya_stage_5_event_130
    rayla "Then it's none of our business. She can tell you when she's ready."
    "Rayla glares at Jaimy."
    image maya_stage_5_event_131 = "/maya/events/stage5/131.webp"
    scene maya_stage_5_event_131
    jaimy "Umm… yeah. So, speaking of Maya. Are you two… like… dating?"
    pc "I like her, but we've never really talked about that."
    image maya_stage_5_event_132 = "/maya/events/stage5/132.webp"
    scene maya_stage_5_event_132
    rayla "Really? You're always doing things together."
    image maya_stage_5_event_133 = "/maya/events/stage5/133.webp"
    scene maya_stage_5_event_133
    jaimy "Yeah, you always pick Maya when you come over to the club. I'm a little hurt, I wouldn't have minded giving you a private dance."
    image maya_stage_5_event_134 = "/maya/events/stage5/134.webp"
    scene maya_stage_5_event_134
    "Jaimy presses her body into yours."
    jaimy "Some would say I was a little jealous, with a handsome man coming in all the time and only picking one girl."
    image maya_stage_5_event_135 = "/maya/events/stage5/135.webp"
    scene maya_stage_5_event_135
    pc "I don't know what to say."
    image maya_stage_5_event_136 = "/maya/events/stage5/136.webp"
    scene maya_stage_5_event_136
    rayla "Jaimy is only giving you a hard time."
    image maya_stage_5_event_137 = "/maya/events/stage5/137.webp"
    scene maya_stage_5_event_137
    jaimy "Something's hard, alright."
    "Jaimy brushes against your crotch. Jaimy steps back and giggles."
    image maya_stage_5_event_138 = "/maya/events/stage5/138.webp"
    scene maya_stage_5_event_138
    jaimy "I was just joking. Only trying to figure out what kind of guy you are."
    pc "Why is that?"
    image maya_stage_5_event_139 = "/maya/events/stage5/139.webp"
    scene maya_stage_5_event_139
    jaimy "Because I can tell Maya really likes you."
    rayla "I've never seen her so happy. Sure, she has some sad moments, but she's the happiest I've ever seen her."
    jaimy "Yeah, you were able to talk to Maya when no one else could. You must be something special."
    image maya_stage_5_event_140 = "/maya/events/stage5/140.webp"
    scene maya_stage_5_event_140
    jaimy "So don't mess it up."
    "Jaimy pretends to scold you."
    pc "I don't intend to."
    image maya_stage_5_event_141 = "/maya/events/stage5/141.webp"
    scene maya_stage_5_event_141
    rayla "Glad to hear it."
    pc "Is there anything else you gals need? I'm supposed to check in on Tessa at Bunny Bites."
    image maya_stage_5_event_142 = "/maya/events/stage5/142.webp"
    scene maya_stage_5_event_142
    rayla "I think we are good here."
    jaimy "Thanks for helping out."
    pc "No problem."
    "You leave and head over to Bunny Bites."

    #Bunny Bites
    image maya_stage_5_event_143 = "/maya/events/stage5/143.webp"
    scene maya_stage_5_event_143
    "You enter Bunny Bites. You look around for Tessa." 
    "You see her set up in the corner, but something seems off. Tessa's big pregnant belly is fully exposed."
    image maya_stage_5_event_144 = "/maya/events/stage5/144.webp"
    scene maya_stage_5_event_144
    "As you get closer, you thought it was an optical illusion, but the closer you get, the bigger Tessa's belly appears." 
    "The shirt she's wearing is acting as a makeshift bra for her giant breasts. You approach the table."
    image maya_stage_5_event_145 = "/maya/events/stage5/145.webp"
    scene maya_stage_5_event_145
    tessa "Hi [playername]!"
    "Tessa seems out of breath. She rubs her enormous stomach, unable to reach the front of it."
    pc "Hi Tessa. Is everything okay?"
    image maya_stage_5_event_146 = "/maya/events/stage5/146.webp"
    scene maya_stage_5_event_146
    tessa "Oh yeah, sales are great. Still have plenty of calendars if that's what you're asking."
    pc "I mean, are you okay?"
    image maya_stage_5_event_147 = "/maya/events/stage5/147.webp"
    scene maya_stage_5_event_147
    tessa "Oh, you mean this."
    "Tessa pats her enormous belly."
    tessa "Marie, the manager, has been treating me very well. She's been bringing me wrong orders."
    pc "I see that."
    image maya_stage_5_event_148 = "/maya/events/stage5/148.webp"
    scene maya_stage_5_event_148
    tessa "She says I need to eat plenty of food now since I'm pregnant." 
    tessa "I can't say no to free food, besides, I missed the food from here. It was my favorite part of the day while we were striking."
    if marie.stage <= 4:
        image maya_stage_5_event_149_1 = "/maya/events/stage5/149_1.webp"
        scene maya_stage_5_event_149_1
    elif marie.stage == 5 or marie.stage == 6:
        image maya_stage_5_event_149_2 = "/maya/events/stage5/149_2.webp"
        scene maya_stage_5_event_149_2
    elif marie.stage == 7 or marie.stage == 8:
        image maya_stage_5_event_149_3 = "/maya/events/stage5/149_3.webp"
        scene maya_stage_5_event_149_3
    elif marie.stage == 9 or marie.stage == 10:
        image maya_stage_5_event_149_4 = "/maya/events/stage5/149_4.webp"
        scene maya_stage_5_event_149_4
    elif marie.stage == 11:
        image maya_stage_5_event_149_5 = "/maya/events/stage5/149_5.webp"
        scene maya_stage_5_event_149_5
    elif marie.stage >= 12:
        image maya_stage_5_event_149_6 = "/maya/events/stage5/149_6.webp"
        scene maya_stage_5_event_149_6
    "Marie comes by with a tray of food and sets it in front of Tessa."
    marie "Whoops, I did another wrong order."
    tessa "Not a problem. I think I still have some room. I swear these babies are eating everything before I can. I'm always so hungry."
    image maya_stage_5_event_150 = "/maya/events/stage5/150.webp"
    scene maya_stage_5_event_150
    "Tessa turns sideways to grab a burger off the tray. Her stomach makes it impossible to reach around."
    if marie.stage <= 4:
        image maya_stage_5_event_151_1 = "/maya/events/stage5/151_1.webp"
        scene maya_stage_5_event_151_1
    elif marie.stage == 5 or marie.stage == 6:
        image maya_stage_5_event_151_2 = "/maya/events/stage5/151_2.webp"
        scene maya_stage_5_event_151_2
    elif marie.stage == 7 or marie.stage == 8:
        image maya_stage_5_event_151_3 = "/maya/events/stage5/151_3.webp"
        scene maya_stage_5_event_151_3
    elif marie.stage == 9 or marie.stage == 10:
        image maya_stage_5_event_151_4 = "/maya/events/stage5/151_4.webp"
        scene maya_stage_5_event_151_4
    elif marie.stage == 11:
        image maya_stage_5_event_151_5 = "/maya/events/stage5/151_5.webp"
        scene maya_stage_5_event_151_5
    elif marie.stage >= 12:
        image maya_stage_5_event_151_6 = "/maya/events/stage5/151_6.webp"
        scene maya_stage_5_event_151_6
    marie "Oh, hi [playername]."
    pc "Can we talk?"
    "You pull Marie out of Tessa's earshot."
    if marie.stage <= 4:
        image maya_stage_5_event_152_1 = "/maya/events/stage5/152_1.webp"
        scene maya_stage_5_event_152_1
    elif marie.stage == 5 or marie.stage == 6:
        image maya_stage_5_event_152_2 = "/maya/events/stage5/152_2.webp"
        scene maya_stage_5_event_152_2
    elif marie.stage == 7 or marie.stage == 8:
        image maya_stage_5_event_152_3 = "/maya/events/stage5/152_3.webp"
        scene maya_stage_5_event_152_3
    elif marie.stage == 9 or marie.stage == 10:
        image maya_stage_5_event_152_4 = "/maya/events/stage5/152_4.webp"
        scene maya_stage_5_event_152_4
    elif marie.stage == 11:
        image maya_stage_5_event_152_5 = "/maya/events/stage5/152_5.webp"
        scene maya_stage_5_event_152_5
    elif marie.stage >= 12:
        image maya_stage_5_event_152_6 = "/maya/events/stage5/152_6.webp"
        scene maya_stage_5_event_152_6
    marie "Isn't she amazing? I swear those babies are giving her superpowers. This is the fourth tray I've brought her."
    pc "I think that's enough for her today. If you keep this up, I don't think she will be able to leave."
    marie "You really think so? Please, I always wanted to make someone so big they can't fit through the doors. This is my chance!"
    pc "You can try some other time. We need her to be able to sell the calendars."
    if marie.stage <= 4:
        image maya_stage_5_event_153_1 = "/maya/events/stage5/153_1.webp"
        scene maya_stage_5_event_153_1
    elif marie.stage == 5 or marie.stage == 6:
        image maya_stage_5_event_153_2 = "/maya/events/stage5/153_2.webp"
        scene maya_stage_5_event_153_2
    elif marie.stage == 7 or marie.stage == 8:
        image maya_stage_5_event_153_3 = "/maya/events/stage5/153_3.webp"
        scene maya_stage_5_event_153_3
    elif marie.stage == 9 or marie.stage == 10:
        image maya_stage_5_event_153_4 = "/maya/events/stage5/153_4.webp"
        scene maya_stage_5_event_153_4
    elif marie.stage == 11:
        image maya_stage_5_event_153_5 = "/maya/events/stage5/153_5.webp"
        scene maya_stage_5_event_153_5
    elif marie.stage >= 12:
        image maya_stage_5_event_153_6 = "/maya/events/stage5/153_6.webp"
        scene maya_stage_5_event_153_6
    marie "Oh, fine!"
    "Marie pouts."
    pc "Besides, I think she might be done. I can't imagine her being able to finish what you just brought."
    if marie.stage <= 4:
        image maya_stage_5_event_154_1 = "/maya/events/stage5/154_1.webp"
        scene maya_stage_5_event_154_1
    elif marie.stage == 5 or marie.stage == 6:
        image maya_stage_5_event_154_2 = "/maya/events/stage5/154_2.webp"
        scene maya_stage_5_event_154_2
    elif marie.stage == 7 or marie.stage == 8:
        image maya_stage_5_event_154_3 = "/maya/events/stage5/154_3.webp"
        scene maya_stage_5_event_154_3
    elif marie.stage == 9 or marie.stage == 10:
        image maya_stage_5_event_154_4 = "/maya/events/stage5/154_4.webp"
        scene maya_stage_5_event_154_4
    elif marie.stage == 11:
        image maya_stage_5_event_154_5 = "/maya/events/stage5/154_5.webp"
        scene maya_stage_5_event_154_5
    elif marie.stage >= 12:
        image maya_stage_5_event_154_6 = "/maya/events/stage5/154_6.webp"
        scene maya_stage_5_event_154_6
    "Marie looks over to Tessa."
    marie "Ummm, I wouldn't be too sure about that."
    image maya_stage_5_event_155 = "/maya/events/stage5/155.webp"
    scene maya_stage_5_event_155
    "You look and see that most of the tray is empty except for a few fries. Tessa's belly is resting on the table."
    pc "Maybe you are right about the superpowers."
    if marie.stage <= 4:
        image maya_stage_5_event_156_1 = "/maya/events/stage5/156_1.webp"
        scene maya_stage_5_event_156_1
    elif marie.stage == 5 or marie.stage == 6:
        image maya_stage_5_event_156_2 = "/maya/events/stage5/156_2.webp"
        scene maya_stage_5_event_156_2
    elif marie.stage == 7 or marie.stage == 8:
        image maya_stage_5_event_156_3 = "/maya/events/stage5/156_3.webp"
        scene maya_stage_5_event_156_3
    elif marie.stage == 9 or marie.stage == 10:
        image maya_stage_5_event_156_4 = "/maya/events/stage5/156_4.webp"
        scene maya_stage_5_event_156_4
    elif marie.stage == 11:
        image maya_stage_5_event_156_5 = "/maya/events/stage5/156_5.webp"
        scene maya_stage_5_event_156_5
    elif marie.stage >= 12:
        image maya_stage_5_event_156_6 = "/maya/events/stage5/156_6.webp"
        scene maya_stage_5_event_156_6
    "Marie looks upset at you."
    marie "You're no fun. Now I'm horny as hell and don't know what to do. Thanks!"
    pc "Sorry."
    "Marie storms off. You decide you better head back to Maya."

    #The Sugar Shop
    image maya_stage_5_event_157 = "/maya/events/stage5/157.webp"
    scene maya_stage_5_event_157
    "You enter The Sugar Shop and see Maya selling one of the calendars to a customer." 
    "You wait until they are done."
    image maya_stage_5_event_158 = "/maya/events/stage5/158.webp"
    scene maya_stage_5_event_158
    maya "[playername], you're back. How is everyone doing?"
    pc "Got to Rayla and Jaimy just in time, they only had a few left."
    maya "That's great. And did you check in on Tessa?"
    pc "Yeah, about Tessa…"
    image maya_stage_5_event_159 = "/maya/events/stage5/159.webp"
    scene maya_stage_5_event_159
    "At that moment, Gina waddles in."
    gina "Sorry, I just saw your message."
    image maya_stage_5_event_160 = "/maya/events/stage5/160.webp"
    scene maya_stage_5_event_160
    "Maya looks upset."
    maya "Where were you? I can see you went someplace with food."
    gina "I said I'm sorry. I passed a buffet when you sent me to help Rayla and Jaimy set up. I did that and then went to get something to eat." 
    gina "I couldn't help myself. It smelled so good."
    image maya_stage_5_event_161 = "/maya/events/stage5/161.webp"
    scene maya_stage_5_event_161
    maya "I really wish you'd take this more seriously. I'm still glad you're here."
    gina "I know, and I'm really, really sorry. Please put me to work anywhere, just not around any more food. I think I'm done for the day."
    pc "Gina could relieve Tessa over at Bunny Bites."
    image maya_stage_5_event_162 = "/maya/events/stage5/162.webp"
    scene maya_stage_5_event_162
    maya "You were going to say something about Tessa before Gina came in."
    pc "I was just going to suggest that Tessa comes here to take over your spot and you could check in on everyone."
    image maya_stage_5_event_163 = "/maya/events/stage5/163.webp"
    scene maya_stage_5_event_163
    maya "I like the idea. Gina, why don't you go relieve Tessa and tell her to come over here."
    gina "But Bunny Bites is the worst place if I don't want to think about food."
    maya "Too bad. You said to put you anywhere, so that's where you're going."
    gina "Fine."
    image maya_stage_5_event_164 = "/maya/events/stage5/164.webp"
    scene maya_stage_5_event_164
    "Gina leaves." 
    "You think to yourself, hopefully, Gina can survive Marie's temptations."
    image maya_stage_5_event_165 = "/maya/events/stage5/165.webp"
    scene maya_stage_5_event_165
    maya "Thanks for checking in on everyone. I think we can handle it from here."
    pc "Sounds good. Just call if you need anything else. I'll be available."
    image maya_stage_5_event_166 = "/maya/events/stage5/166.webp"
    scene maya_stage_5_event_166
    "Maya kisses you on the cheek. You can't help but think of what Rayla and Jaimy said about Maya."
    maya "It means a lot to me that you're always there."
    image maya_stage_5_event_167 = "/maya/events/stage5/167.webp"
    scene maya_stage_5_event_167
    "You embrace Maya."
    pc "You got this. I believe in you. Never give up."
    "Maya and you spend a moment holding each other until a customer comes along."
    image maya_stage_5_event_168 = "/maya/events/stage5/168.webp"
    scene maya_stage_5_event_168
    maya "I just hope we have enough time to sell these calendars before Mr. Vanthorne calls. I better get going. I'll talk to you later."
    "Maya starts talking with the customer. You head home."

    if recollection == False:
        $ maya.weight += 0.5
        $ daytime += 1
        $ phonecall = 1
    stop music fadeout 1.0
    $ mayastage5event4 = 0
    return


label Maya_Stage_5_Event_5:
    #Event 16
    #Pc's house
    scene player_room
    "You get a call from Maya."
    image maya_stage_5_event_193 = "/maya/events/stage5/193.webp"
    scene maya_stage_5_event_193
    maya "Hey, [playername]."
    pc "What's up?"
    maya "Mr. Vanthorne just messaged me. It seems we are out of time, and we were looking so good."
    maya "The calendars were selling like crazy, but we are still short by about $150,000. I'm sure if we had just had a little more time, we could have done it."
    pc "You girls really tried your hardest."
    maya "They really did. I'm very proud of them."
    pc "So what does Mr. Vanthorne want?"
    image maya_stage_5_event_194 = "/maya/events/stage5/194.webp"
    scene maya_stage_5_event_194
    maya "He wants us to meet him at Velvet Shadows. I'm sure just to rub it our faces that we couldn't raise the money."
    pc "He sure wants to be a giant dick till the very end."
    maya "Pretty much. Do you think you could come over? I could use moral support for whatever happens."
    pc "I'll head over right away."
    maya "Thanks."

    scene player_room
    "You get ready to leave when you get a text from Daisy."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Daisy', dialogue=dialogue_one)
    $ msg ("How's my favorite student doing? I just got an order delivered today and wouldn't you guess it, they brought me too much food.", who=1)
    pause
    $ msg ("I think I'll need some help if I'm going to eat it all. Would you like to come over and help me stuff my face?", who=1)
    pause
    $ msg ("I'd love to, but I already promised someone I'd help them out today. Maybe some other time.")
    pause
    $ msg ("What can be more important than filling me up?", who=1)
    pause
    $ msg ("Have you heard anything about the Velvet Shadows strike?")
    pause
    $ msg ("A little bit?", who=1)
    pause
    $ msg ("So the owner has been pretty ruthless with the girls working there. They have been mistreated, harassed, and put on extremely strict diets.")
    pause
    $ msg ("Thats not good. So what do they want?", who=1)
    pause
    $ msg ("Mainly to be treated with respect and to lift the strict diet.")
    pause
    $ msg ("Really.", who=1)
    pause
    $ msg ("Yeah, they had a coworker who got pregnant with triplets, and she was let go because she was getting too big.")
    pause
    $ msg ("That doesn't seem fair. So what's happening there right now that you can't come over and see me?", who=1)
    pause
    $ msg ("The owner Mr. Vanthorne is selling the place to a company to build an apartment complex.")
    pause
    $ msg ("Can't the girls offer to buy it first?", who=1)
    pause
    $ msg ("They tried, but the owner is asking for a million dollars. They tried raising the funds, but they just couldn't get enough money in time.")
    pause
    $ msg ("You don't say, a million dollars. Hmmm. Well, I guess you should get going. I've decided this can wait for another time.", who=1)
    pause
    $ msg ("Thanks for understanding.")
    pause
    $ msg ("I think everything will work out just fine.", who=1)
    pause
    $ hide_messenger()

    "You finish getting ready and you head over to Velvet Shadows."
    
    #Velvet Shadows
    #Maya is there with the rest of the girls. 
    image maya_stage_5_event_169 = "/maya/events/stage5/169.webp"
    scene maya_stage_5_event_169
    maya "Thanks for coming."
    pc "Has Mr. Vanthorne said anything yet?"
    image maya_stage_5_event_170 = "/maya/events/stage5/170.webp"
    scene maya_stage_5_event_170
    "Mr. Vanthorne comes out."
    vanthorne "Time's up. Do you have the money?"
    image maya_stage_5_event_171 = "/maya/events/stage5/171.webp"
    scene maya_stage_5_event_171
    maya "We tried. We have $850,000. Please, you can have it all if you'd just let us buy the place from you."
    vanthorne "And lose $50,000? No way."
    maya "I understand, but please think of all the people that rely on this job."
    vanthorne "You people put me in this situation. You really think I'm going to throw away this opportunity over feelings? Ha!" 
    vanthorne "Now if you don't mind, since you clearly don't have the money, I'm going to make that call to those fine gentlemen." 
    vanthorne "I would suggest that you all start finding work elsewhere."
    $ unknownname = 'Woman in suit'
    image maya_stage_5_event_172 = "/maya/events/stage5/172.webp"
    scene maya_stage_5_event_172
    "Mr. Vanthorne turns to head into the club when a woman in a suit walks over to him."
    unknown "Mr. Vanthorne?"
    vanthorne "Who's asking?"
    unknown "I represent a sizable organization that recently has become very interested in this particular establishment. May we talk?"
    vanthorne "A sizable organization you say. Fine, go on, what do you want?"
    unknown "The organization would like to offer you a hefty sum for the place."
    vanthorne "How hefty are we talking about?"
    unknown "One million dollars."
    image maya_stage_5_event_173 = "/maya/events/stage5/173.webp"
    scene maya_stage_5_event_173
    vanthorne "A million dollars? You can't be serious."
    unknown "Oh, we are very serious."
    vanthorne "Well, give me some time to think about it."
    unknown "I'm afraid they would like an answer now."
    vanthorne "Sorry, missy, but I had a previous agreement with another."
    unknown "We would also like to give you an extra $200,000 if you sign over the place to us today."
    image maya_stage_5_event_174 = "/maya/events/stage5/174.webp"
    scene maya_stage_5_event_174
    "The woman in the suit pulls out a check and hands it to Mr. Vanthorne."
    vanthorne "This can't be real." 
    unknown "Believe me, it's very real. You can call your bank to verify the funds are all there, but after that, I will need an answer From you right away."
    vanthorne "Fine, I'll make a quick call."
    image maya_stage_5_event_175 = "/maya/events/stage5/175.webp"
    scene maya_stage_5_event_175
    "Mr. Vanthorne calls his bank. After a bit, he hangs up the phone."
    image maya_stage_5_event_176 = "/maya/events/stage5/176.webp"
    scene maya_stage_5_event_176
    vanthorne "Who the hell are you guys?"
    unknown "Is everything accounted for?"
    vanthorne "The bank said the check is good."
    unknown "Then I need an answer, Mr. Vanthorne."
    vanthorne "I can't believe this is real. You are out of your mind."
    unknown "Last chance, Mr. Vanthorne."
    vanthorne "Fine, yes, you have a deal."
    unknown "Very good, Mr. Vanthorne. I've already taken the liberty to start the paperwork."
    image maya_stage_5_event_177 = "/maya/events/stage5/177.webp"
    scene maya_stage_5_event_177
    "The woman in the suit pulls out a stack of documents and hands them to Mr. Vanthorne."
    unknown "If you wouldn't mind going inside and start looking them over. I'll be in shortly. I have a few things I need to discuss with the group over there."
    vanthorne "What do they have to do with this?"
    unknown "Don't worry about it. Now go on, I'll be in shortly."
    image maya_stage_5_event_178 = "/maya/events/stage5/178.webp"
    scene maya_stage_5_event_178
    "Mr. Vanthorne heads into the club. The woman in the suit walks over to the crowd."
    unknown "Now who's the one in charge?"
    "Maya steps forward."
    image maya_stage_5_event_179 = "/maya/events/stage5/179.webp"
    scene maya_stage_5_event_179
    maya "I guess that's me. Who are you guys?" 
    unknown "The organization I represent has heard about your cause and wanted to help out."
    maya "May I ask who this organization is?"
    unknown "They would like to remain anonymous."
    maya "Ok. I guess if you can thank your employers for us. That would be greatly appreciated. How did you know how much to offer?"
    unknown "They have their sources."
    maya "But what would have happened if he refused the money."
    unknown "We have our ways. My firm I represent also deals with discrimination lawsuits." 
    unknown "From what I've been told, I'm sure I could have twisted his arm a little bit if needed, but his greed seemed to have won in the long run."
    maya "You really think we had a case."
    unknown "From what I've been told a very strong one. Anyways we've made our deal so no need for a lawsuit."
    unknown "Oh, I'm also supposed to ask if you would also like to become the owner of the club . They trust in your ability to run it."
    maya "Really there just giving it away. What would they like in return?"
    unknown "Nothing."
    image maya_stage_5_event_180 = "/maya/events/stage5/180.webp"
    scene maya_stage_5_event_180
    maya "Nothing!"
    unknown "Yes. After I'm done with Mr. Vanthorne, we will need to sign the place over to you if you'd like."
    image maya_stage_5_event_181 = "/maya/events/stage5/181.webp"
    scene maya_stage_5_event_181
    maya "Ah, sure, we can do that."
    unknown "Very good. If you can stick around, miss…"
    maya "Maya. Sure, I can stick around."
    unknown "Very good, I have a few other things to go over with you, but that can wait. It was very nice to meet you all."
    image maya_stage_5_event_182 = "/maya/events/stage5/182.webp"
    scene maya_stage_5_event_182
    "The woman in the suit enters the club. Everyone is silent for a while."
    image maya_stage_5_event_183 = "/maya/events/stage5/183.webp"
    scene maya_stage_5_event_183
    gina "What the hell just happened?"
    rayla "I think Maya has just gotten ownership of the club."
    jaimy "Maya, you did it."
    $ unknownname = 'Unknown'
    image maya_stage_5_event_184 = "/maya/events/stage5/184.webp"
    scene maya_stage_5_event_184
    "Maya bursts into tears."
    tessa "This is a miracle."
    maya "I don't know what to say."
    gina "Who cares, the club is ours!"
    maya "I don't know how we did it, but I would like to thank everyone for all the hard work they have put in this whole time. Thank you."
    image maya_stage_5_event_185 = "/maya/events/stage5/185.webp"
    scene maya_stage_5_event_185
    "Everyone does a big group hug."
    maya "You guys go celebrate. I'll meet up with you once I finish up things here."
    image maya_stage_5_event_186 = "/maya/events/stage5/186.webp"
    scene maya_stage_5_event_186
    "Everyone leaves chatting over what just happened here. You stay with Maya."
    maya "Pinch me, I must be dreaming. You didn't have anything to do with this."
    pc "Me! I'm as speechless as the rest of them. I'm really happy for you."
    image maya_stage_5_event_187 = "/maya/events/stage5/187.webp"
    scene maya_stage_5_event_187
    "Maya hugs you."
    maya "Me too."
    pc "So, what's next?"
    image maya_stage_5_event_188 = "/maya/events/stage5/188.webp"
    scene maya_stage_5_event_188
    maya "I'm not sure. I came here thinking the worst, but now I'm going to be the owner of the Velvet Shadows." 
    maya "I have so many things running through my mind. I have some big changes I'd like to make." 
    maya "So, I don't think we will be up and running right away, but I'll message you once we are back. Maybe we can do a grand reopening."
    pc "That sounds great. I can't wait."
    image maya_stage_5_event_189 = "/maya/events/stage5/189.webp"
    scene maya_stage_5_event_189
    "Maya boops you on the nose."
    maya "I have things covered here. Why don't you go celebrate with the rest? I'll see you when it's done."
    pc "I think I'll keep the celebrating to you guys. I'm just happy things worked out."
    image maya_stage_5_event_190 = "/maya/events/stage5/190.webp"
    scene maya_stage_5_event_190
    "Maya kisses you on the cheeks."
    image maya_stage_5_event_191 = "/maya/events/stage5/191.webp"
    scene maya_stage_5_event_191
    maya "I'm glad that you were here for this. You have helped me out so much ever since I met you. Thank you."
    image maya_stage_5_event_192 = "/maya/events/stage5/192.webp"
    scene maya_stage_5_event_192
    "Maya hugs you again." 
    "You head home."

    if recollection == False:
        $ maya.weight = 98
        $ daytime += 1
        $ phonecall = 1
        $ daycount5 = 0
    stop music fadeout 1.0
    $ mayastage5event5 = 0
    return

label Maya_Stage_6_Event:
    #Event 17
    #Pc's house
    scene player_room
    "You get a message from Maya."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Maya', dialogue=dialogue_one)
    $ msg ("Today's the big day. We are reopening for business.", who=1)
    pause
    $ msg ("You should stop by for our big grand reopening celebration.", who=1)
    pause
    $ msg ("I can't wait to see what you've done with the place. I'll head over right away.")
    pause
    $ msg ("See you soon.", who=1)
    pause
    $ hide_messenger()

    #Curvy Corner
    scene stripclub_entrance2
    play music "/music/stripclub.ogg" if_changed
    "The first thing you notice is that the sign has been changed back to the old name, the Curvy Corner."
    scene stripclub2
    "You enter the club to find it super busy."
    image maya_stage_6_event_1 = "/maya/events/stage6/1.webp"
    scene maya_stage_6_event_1
    "You see Maya. She notices you, waves, and comes over."
    image maya_stripclub_talk = "/maya/[maya.stage]/stripclub_talk.webp"
    scene maya_stripclub_talk
    maya "So, what do you think?"
    pc "This all looks great! Looks like everyone is excited."
    image maya_stripclub_talk2 = "/maya/[maya.stage]/stripclub_talk2.webp"
    scene maya_stripclub_talk2
    maya "I know, right? I still can't believe this is really happening. Did you notice the we changed the name."
    pc "That was the first thing I saw. You changed it back. How did you get the signs so quickly?"
    image maya_stripclub_talk3 = "/maya/[maya.stage]/stripclub_talk3.webp"
    scene maya_stripclub_talk3
    "Maya smiles."
    maya "I'm changing everything back to the way it was. We found the old signs in the back room. I guess Mr. Vanthorne kept them all this time."
    image maya_stripclub_follow = "/maya/[maya.stage]/stripclub_follow.webp"
    scene maya_stripclub_follow
    maya "Oh, I need to show you another thing."
    "Maya grabs your hand and pulls you through the crowd of people."
    image maya_stage_6_event_2 = "/maya/events/stage6/2.webp"
    scene maya_stage_6_event_2
    "She leads you over to a banquet of tables covered with food."
    pc "You guys serving food for the grand reopening?"
    image maya_stage_6_event_3 = "/maya/events/stage6/3.webp"
    scene maya_stage_6_event_3
    maya "Nope, this will be a permanent thing. The organization that bought the place wanted to provide food for the establishment."
    pc "Really?"
    image maya_stage_6_event_4 = "/maya/events/stage6/4.webp"
    scene maya_stage_6_event_4
    maya "Do you want to know the strangest part? They are providing the food free of charge. They even have a table set up in our changing room for just the employees." 
    maya "Isn't that crazy?" 
    pc "They're not asking anything for this? Who are these people?"
    image maya_stage_6_event_5 = "/maya/events/stage6/5.webp"
    scene maya_stage_6_event_5
    maya "No clue. They were really secretive about the whole thing. Wish there was a way I could show how much I appreciate there commitment to this place"
    pc "Do you think they can be trusted?"
    maya "I've had someone look over the paperwork they had me fill out. Everything looks legit according to them. The club is 100 percent mine."
    pc "Still seems weird that they didn't ask for anything."
    maya "They only asked that they have this buffet here."
    pc "That's it! You didn't discuss anything else?"
    maya "After we signed the documents and Mr. Vanthorne left, she was very interested in his other businesses, but other then that, just the buffet, I'm not complaining, free food." 
    image maya_stage_6_event_6 = "/maya/events/stage6/6.webp"
    scene maya_stage_6_event_6
    maya "Kinda thought the girls would have been more excited for it since a lot of them were starving themselves because of Mr. Vanthorne's stupid rule." 
    maya "Gina's the only one that seems taking full advantage of this, but I guess that the rest are still a little weary about the whole thing."
    maya "I assured them that that the rule is gone and they will never be disciplined for gaining weight." 
    maya "This club accepts all sizes." 
    pc "That's great to hear. So, what's next for Curvy Corner?"
    image maya_stage_6_event_7 = "/maya/events/stage6/7.webp"
    scene maya_stage_6_event_7
    maya "I'm not sure yet. I have a few ideas I'm thinking about, but you'll have to wait and see."
    image maya_stage_6_event_8 = "/maya/events/stage6/8.webp"
    scene maya_stage_6_event_8
    "Maya boops your nose."
    pc "Oh, come on, just a little hint."
    image maya_stage_6_event_9 = "/maya/events/stage6/9.webp"
    scene maya_stage_6_event_9
    maya "You will have to wait just like the rest of them."
    pc "Well, I'm really happy for you. This is something amazing you have been able to achieve."
    maya "You really think so?"
    image maya_stage_6_event_10 = "/maya/events/stage6/10.webp"
    scene maya_stage_6_event_10
    "Maya bites her bottom lip. You feel like she really wants to say something."
    maya "Umm… Can I show you one more thing?"
    image maya_stage_6_event_11 = "/maya/events/stage6/11.webp"
    scene maya_stage_6_event_11
    "Before you can answer, Maya grabs your hand once again and leads you to her private room. She closes the door behind you."
    image maya_stage_6_event_12 = "/maya/events/stage6/12.webp"
    scene maya_stage_6_event_12
    pc "This place looks the same. What am I looking for?"
    image maya_stage_6_event_13 = "/maya/events/stage6/13.webp"
    scene maya_stage_6_event_13
    "Maya comes up close to you."
    maya "I just needed somewhere private. I've been meaning to ask you this for a while now."
    image maya_stage_6_event_14 = "/maya/events/stage6/14.webp"
    scene maya_stage_6_event_14
    "Maya looks nervous."
    maya "Ahh. This is just so hard to say. I've told myself never to do this."
    pc "What is that?"
    image maya_stage_6_event_15 = "/maya/events/stage6/15.webp"
    scene maya_stage_6_event_15
    maya "I… I like you."
    "You laugh."
    pc "I like you too."
    image maya_stage_6_event_16 = "/maya/events/stage6/16.webp"
    scene maya_stage_6_event_16
    "Maya looks even more embarrassed."
    maya "No, I mean I like, like you. God, I sound like an idiot. I mean…"
    pc "I know what you mean. I like, like you too."
    image maya_stage_6_event_17 = "/maya/events/stage6/17.webp"
    scene maya_stage_6_event_17
    "Maya suddenly kisses you on the mouth. You embrace Maya while kissing."
    image maya_stage_6_event_18 = "/maya/events/stage6/18.webp"
    scene maya_stage_6_event_18
    maya "I've wanted to do that for a long time now."
    pc "Me too."
    image maya_stage_6_event_19 = "/maya/events/stage6/19.webp"
    scene maya_stage_6_event_19
    maya "We've gotten so close over this whole ordeal. It's been driving me crazy not to say anything about how I feel about you." 
    maya "You've been so great to me, you listen to my problems, you help me when I needed help the most." 
    maya "You're an amazing person and I want to spend more time with you. I want you to know the whole me. God, I just want you right now."
    pc "I'm not going to stop you."
    image maya_stage_6_event_20 = "/maya/events/stage6/20.webp"
    scene maya_stage_6_event_20
    "Maya presses up against you, guiding your hands to her breasts when suddenly there's a knock on the door."
    image maya_stage_6_event_21 = "/maya/events/stage6/21.webp"
    scene maya_stage_6_event_21
    rayla "Maya are you in here."
    maya "Yeah Rayla, I'm here."
    rayla "The girls want to take a picture together."
    maya "Sounds good, I'll be out shortly."
    image maya_stage_6_event_22 = "/maya/events/stage6/22.webp"
    scene maya_stage_6_event_22
    "Maya kisses you one more time."
    image maya_stage_6_event_23 = "/maya/events/stage6/23.webp"
    scene maya_stage_6_event_23
    maya "I should get back out there and make sure everything is running smoothly. This will have to wait for another time." 
    maya "Now don't forget, we are now open again. You can come by anytime for a private dance or just come and watch me or any of the other girls."
    pc "Will I still need to pay for a private dance?"
    image maya_stage_6_event_24 = "/maya/events/stage6/24.webp"
    scene maya_stage_6_event_24
    maya "For now, just so it doesn't look like I'm playing favorites, but what we do afterwards."
    "Maya winks at you."
    maya "That will be off the clock."
    image maya_stage_6_event_25 = "/maya/events/stage6/25.webp"
    scene maya_stage_6_event_25
    "Maya boops your nose." 
    scene stripclub2
    "You head out back to the main room." 
    "You stick around and watches a few dances from the other girls and leaves."
    "This is Maya's final event in this update, her story will continue next update. You can now visit The Curvy Corner."

    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
    stop music fadeout 1.0
    $ mayastage6event = 0
    return


label Maya_BB_Normal:
    image cafe_maya_booth = "/maya/[maya.stage]/cafe_booth.webp"
    scene cafe_maya_booth
    pc "Here you go."
    if maya.stage == 1:
        maya "This looks so good. I can't believe I stopped coming in here for so long. This food is amazing."
        pc "I'm glad you like it."
    elif maya.stage == 2:
        maya "This looks and smells amazing. Maybe I should have made it a double cheeseburger."
        pc "I can go back and make you one quick."
        maya "No, that's ok. Thanks for the offer, but I'm good with this."
    elif maya.stage >= 3 and mayastage4event2 == 1:
        maya "This looks great. Now I’m thinking I should have ordered a little bit more."
        pc "I can go back and make you something else."
        maya "No, that's ok. I'm good with this"

    if maya.stage == 4 and mayastage4event2 == 0:
        maya "This looks great. Kinda feel bad for abandoning everyone for a bit, but it feels good to sit down and enjoy a meal."
        pc "I don't blame you. You're working pretty hard out there."
        image cafe_maya_booth2 = "/maya/[maya.stage]/cafe_booth2.webp"
        scene cafe_maya_booth2
        maya "Thanks."
        pc "Enjoy your meal. I'll make sure your other order is ready by the time you're done."
        image cafe_maya_eat = "/maya/[maya.stage]/cafe_eat.webp"
        scene cafe_maya_eat
        "Maya quickly eats her meal."
        image cafe_maya_bye = "/maya/[maya.stage]/cafe_bye.webp"
        scene cafe_maya_bye
        "Maya leaves with bags full of food for the strikers."
    elif maya.stage == 5 and mayastage5event2 == 0 and mayastage5event3 == 1:
        maya "This looks great. "
        pc "Enjoy your meal."
        image cafe_maya_eat = "/maya/[maya.stage]/cafe_eat.webp"
        scene cafe_maya_eat
        "Maya quickly eats her meal."
        image cafe_maya_booth2 = "/maya/[maya.stage]/cafe_booth2.webp"
        scene cafe_maya_booth2
        maya "Well I better get back out there. The calendars won't sell themselves."
        "Maya gets up and leaves."
    elif maya.stage == 5 and mayastage5event3 == 0:
        maya "This looks great."
        pc "Enjoy your meal."
        image cafe_maya_eat = "/maya/[maya.stage]/cafe_eat.webp"
        scene cafe_maya_eat
        "Maya quickly eats her meal."
        image cafe_maya_booth2 = "/maya/[maya.stage]/cafe_booth2.webp"
        scene cafe_maya_booth2
        maya "Thanks for the meal. I'll message you once we get things up and running."
        "Maya gets up and leaves."
    elif maya.stage >= 5 and mayastage5event4 == 0:
        maya "This looks great."
        pc "Enjoy your meal."
        image cafe_maya_eat = "/maya/[maya.stage]/cafe_eat.webp"
        scene cafe_maya_eat
        "Maya quickly eats her meal."
        image cafe_maya_booth2 = "/maya/[maya.stage]/cafe_booth2.webp"
        scene cafe_maya_booth2
        maya "Thanks for the meal. I better get back to work."
        "Maya gets up and leaves."
    else:
        image cafe_maya_booth2 = "/maya/[maya.stage]/cafe_booth2.webp"
        scene cafe_maya_booth2
        maya "Say hi to Amber for me the next time you see her."
        pc "Sure thing, enjoy your meal."
        "Maya quickly eats her meal and leaves."

    return
