label marie_home:
    if mariestage4event == 1 and mariestage3event2 == 0 and amberstage5event == 0 and lisastage5event == 0 and marie.stage >= 4:
        call Marie_Stage_4_Event_1
        return
    image marie_home_arrive = "/marie/[marie.stage]/home_arrive.webp"
    scene marie_home_arrive
    "Arriving at Marie's place, she turns to you with a wicked grin."
    image marie_home_sitting1 = "/marie/[marie.stage]/home_sitting1.webp"
    scene marie_home_sitting1
    marie "Ahhh, it's good to finally be home."
    pc "Tired from work?"
    image marie_home_sitting2 = "/marie/[marie.stage]/home_sitting2.webp"
    scene marie_home_sitting2
    marie "Not really, it's just a relief to drop out of waitress mode, you know?"
    pc "Definitely, it's tough to maintain that constant smile when some customers can be really unpleasant."
    image marie_home_sitting3 = "/marie/[marie.stage]/home_sitting3.webp"
    scene marie_home_sitting3
    marie "Yeah that, but more importantly I spend my day bringing girls food, all while resisting the urge to feed them myself or tease them about the sexy guts they're trying and failing to hide."
    marie "Speaking of guts..."
    "She stands up."
    image marie_home_strip = "/marie/[marie.stage]/home_strip.webp"
    scene marie_home_strip
    marie "Let me make some room so I can fill mine up."
    "She pulls off her sweater and unbuttons her pants."
    image marie_home_strip2 = "/marie/[marie.stage]/home_strip2.webp"
    scene marie_home_strip2
    marie "Now this pig can finally bloat herself as much as she wants."
    image marie_home_drink1 = "/marie/[marie.stage]/home_drink1.webp"
    scene marie_home_drink1
    "She heads to the kitchen and fills as many cups of soft drink as she can."
    image marie_home_drink2 = "/marie/[marie.stage]/home_drink2.webp"
    scene marie_home_drink2
    marie "Come to mama..."
    "Marie ravenously begins to chug a cup of coke, only pausing to breathe. Once the cup is done, she tosses it on the ground and looks at the others."
    marie "M-URRRRRRP-more..."
    image marie_home_stuffed1 = "/marie/[marie.stage]/home_stuffed1.webp"
    scene marie_home_stuffed1
    "Without a second thought, she grabs another cup."
    "So she drank..."
    "And drank..."
    image marie_home_stuffed2 = "/marie/[marie.stage]/home_stuffed2.webp"
    scene marie_home_stuffed2
    "And drank..."
    "And drank!"
    image marie_home_stuffed3 = "/marie/[marie.stage]/home_stuffed3.webp"
    scene marie_home_stuffed3
    "Having finished the drinks, Marie caresses her bloated belly while giving you what can only be described as 'fuck me' eyes."
    marie "Let's go to my room..."
    image marie_home_strip3 = "/marie/[marie.stage]/home_strip3.webp"
    scene marie_home_strip3
    "In her room, Marie immediately begins to take off her pants."
    marie "I'm full and horny, good thing I've got a handsome stud to keep me company."
    image marie_home_bed1 = "/marie/[marie.stage]/home_bed1.webp"
    scene marie_home_bed1
    "She crawls onto her bed."
    marie "Come over here."
    if persistent.nosexscene == True:
        scene black with dissolve
        "Marie and I had a great time together."
        $ marie.weight += 1
        return
    image marie_home_sex2 = "/marie/[marie.stage]/home_sex2.webp"
    scene marie_home_sex2
    if marie.stage <= 6:
        pc "I should warn you, I'm starting to have inappropriate thoughts about one of my coworkers."
        marie "Oh yeah?"
        marie "Which one?"
    elif marie.stage >= 7:
        pc "Damn, now I'm hungry."
        marie "Oh, I should have offered you something!"
        marie "I have some pizza-"
        pc "What I want is right here."
    image marie_home_sex3 = "/marie/[marie.stage]/home_sex3.webp"
    scene marie_home_sex3
    if marie.stage <= 6:
        pc "The hot one everyone is always flirting with."
        marie "Oh, I thought you might have meant me."
        pc "That's what I said."
        pc "I hope I'm not creating an uncomfortable workplace."
    elif marie.stage >= 7:
        marie "Oh! That's what you meant."
        pc "Thought I'd give you a moment to let your stomach settle."
        marie "So thoughtful."
        pc "Tell your friends!"
        marie "Very funny."
    image marie_home_sex4 = "/marie/[marie.stage]/home_sex4.webp"
    scene marie_home_sex4
    if marie.stage <= 6:
        marie "Ohhh!"
        marie "No complaints here."
        pc "That's a relief."
        marie "You really like me in this state?"
    elif marie.stage >= 7:
        marie "Ohhhh!"
        pc "You're ready?"
        marie "Only one way to find out."
    if marie.stage == 2:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/2/home_sex5.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Oh! I'll take that as a yes!"
        pc "Sometimes actions are better than words."
        marie "Most times, I'd say."
        pc "Is this you telling me to stop running my mouth?"
        marie "No!"
        marie "Unless it works in my favor."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/2/home_sex6.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Like that!"
        marie "Damn, [pc]!"
        pc "Not too much movement?"
        marie "I'd warn you."
        window hide
        pause
        marie "Can you hear my stomach sloshing around?"
        pc "Yep."
        pc "And I heard you aren't supposed to shake soda."
        marie "Would it be unattractive if I let out a huge burp?"
        pc "I dare you."
        marie "No!"
        marie "I'm a lady!"
        pc "Aww."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/2/home_sex7.webm" loop
        show movie with dissolve
        window hide
        pause
    elif marie.stage == 3:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/3/home_sex5.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Oh! I'll take that as a yes!"
        pc "Sometimes actions are better than words."
        marie "Most times, I'd say."
        pc "Is this you telling me to stop running my mouth?"
        marie "No!"
        marie "Unless it works in my favor."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/3/home_sex6.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Like that!"
        marie "Damn, [pc]!"
        pc "Not too much movement?"
        marie "I'd warn you."
        window hide
        pause
        marie "Can you hear my stomach sloshing around?"
        pc "Yep."
        pc "And I heard you aren't supposed to shake soda."
        marie "Would it be unattractive if I let out a huge burp?"
        pc "I dare you."
        marie "No!"
        marie "I'm a lady!"
        pc "Aww."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/3/home_sex7.webm" loop
        show movie with dissolve
        window hide
        pause
    elif marie.stage == 4:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/4/home_sex5.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Oh! I'll take that as a yes!"
        pc "Sometimes actions are better than words."
        marie "Most times, I'd say."
        pc "Is this you telling me to stop running my mouth?"
        marie "No!"
        marie "Unless it works in my favor."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/4/home_sex6.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Like that!"
        marie "Damn, [pc]!"
        pc "Not too much movement?"
        marie "I'd warn you."
        window hide
        pause
        marie "Can you hear my stomach sloshing around?"
        pc "Yep."
        pc "And I heard you aren't supposed to shake soda."
        marie "Would it be unattractive if I let out a huge burp?"
        pc "I dare you."
        marie "No!"
        marie "I'm a lady!"
        pc "Aww."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/4/home_sex7.webm" loop
        show movie with dissolve
        window hide
        pause
    elif marie.stage == 5:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/5/home_sex5.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Oh! I'll take that as a yes!"
        pc "Sometimes actions are better than words."
        marie "Most times, I'd say."
        pc "Is this you telling me to stop running my mouth?"
        marie "No!"
        marie "Unless it works in my favor."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/5/home_sex6.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Like that!"
        marie "Damn, [pc]!"
        pc "Not too much movement?"
        marie "I'd warn you."
        window hide
        pause
        marie "Can you hear my stomach sloshing around?"
        pc "Yep."
        pc "And I heard you aren't supposed to shake soda."
        marie "Would it be unattractive if I let out a huge burp?"
        pc "I dare you."
        marie "No!"
        marie "I'm a lady!"
        pc "Aww."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/5/home_sex7.webm" loop
        show movie with dissolve
        window hide
        pause
    elif marie.stage == 6:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/6/home_sex5.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Oh! I'll take that as a yes!"
        pc "Sometimes actions are better than words."
        marie "Most times, I'd say."
        pc "Is this you telling me to stop running my mouth?"
        marie "No!"
        marie "Unless it works in my favor."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/6/home_sex6.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Like that!"
        marie "Damn, [pc]!"
        pc "Not too much movement?"
        marie "I'd warn you."
        window hide
        pause
        marie "Can you hear my stomach sloshing around?"
        pc "Yep."
        pc "And I heard you aren't supposed to shake soda."
        marie "Would it be unattractive if I let out a huge burp?"
        pc "I dare you."
        marie "No!"
        marie "I'm a lady!"
        pc "Aww."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/6/home_sex7.webm" loop
        show movie with dissolve
        window hide
        pause
    elif marie.stage == 7:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/7/home_sex5.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Oh! I'll take that as a yes!"
        pc "Sometimes actions are better than words."
        marie "Most times, I'd say."
        pc "Is this you telling me to stop running my mouth?"
        marie "No!"
        marie "Unless it works in my favor."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/7/home_sex6.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Like that!"
        marie "Damn, [pc]!"
        pc "Not too much movement?"
        marie "I'd warn you."
        window hide
        pause
        marie "Can you hear my stomach sloshing around?"
        pc "Yep."
        pc "And I heard you aren't supposed to shake soda."
        marie "Would it be unattractive if I let out a huge burp?"
        pc "I dare you."
        marie "No!"
        marie "I'm a lady!"
        pc "Aww."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/7/home_sex7.webm" loop
        show movie with dissolve
        window hide
        pause
    elif marie.stage == 8:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/8/home_sex5.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Oh! I'll take that as a yes!"
        pc "Sometimes actions are better than words."
        marie "Most times, I'd say."
        pc "Is this you telling me to stop running my mouth?"
        marie "No!"
        marie "Unless it works in my favor."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/8/home_sex6.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Like that!"
        marie "Damn, [pc]!"
        pc "Not too much movement?"
        marie "I'd warn you."
        window hide
        pause
        marie "Can you hear my stomach sloshing around?"
        pc "Yep."
        pc "And I heard you aren't supposed to shake soda."
        marie "Would it be unattractive if I let out a huge burp?"
        pc "I dare you."
        marie "No!"
        marie "I'm a lady!"
        pc "Aww."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/8/home_sex7.webm" loop
        show movie with dissolve
        window hide
        pause
    elif marie.stage == 9:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/9/home_sex5.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Oh! I'll take that as a yes!"
        pc "Sometimes actions are better than words."
        marie "Most times, I'd say."
        pc "Is this you telling me to stop running my mouth?"
        marie "No!"
        marie "Unless it works in my favor."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/9/home_sex6.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Like that!"
        marie "Damn, [pc]!"
        pc "Not too much movement?"
        marie "I'd warn you."
        window hide
        pause
        marie "Can you hear my stomach sloshing around?"
        pc "Yep."
        pc "And I heard you aren't supposed to shake soda."
        marie "Would it be unattractive if I let out a huge burp?"
        pc "I dare you."
        marie "No!"
        marie "I'm a lady!"
        pc "Aww."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/9/home_sex7.webm" loop
        show movie with dissolve
        window hide
        pause
    elif marie.stage == 10:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/10/home_sex5.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Oh! I'll take that as a yes!"
        pc "Sometimes actions are better than words."
        marie "Most times, I'd say."
        pc "Is this you telling me to stop running my mouth?"
        marie "No!"
        marie "Unless it works in my favor."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/10/home_sex6.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Like that!"
        marie "Damn, [pc]!"
        pc "Not too much movement?"
        marie "I'd warn you."
        window hide
        pause
        marie "Can you hear my stomach sloshing around?"
        pc "Yep."
        pc "And I heard you aren't supposed to shake soda."
        marie "Would it be unattractive if I let out a huge burp?"
        pc "I dare you."
        marie "No!"
        marie "I'm a lady!"
        pc "Aww."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/10/home_sex7.webm" loop
        show movie with dissolve
        window hide
        pause
    elif marie.stage == 11:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/11/home_sex5.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Oh! I'll take that as a yes!"
        pc "Sometimes actions are better than words."
        marie "Most times, I'd say."
        pc "Is this you telling me to stop running my mouth?"
        marie "No!"
        marie "Unless it works in my favor."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/11/home_sex6.webm" loop
        show movie with dissolve
        window hide
        pause
        marie "Like that!"
        marie "Damn, [pc]!"
        pc "Not too much movement?"
        marie "I'd warn you."
        window hide
        pause
        marie "Can you hear my stomach sloshing around?"
        pc "Yep."
        pc "And I heard you aren't supposed to shake soda."
        marie "Would it be unattractive if I let out a huge burp?"
        pc "I dare you."
        marie "No!"
        marie "I'm a lady!"
        pc "Aww."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/marie/11/home_sex7.webm" loop
        show movie with dissolve
        window hide
        pause
    if marie.stage <= 6:
        marie "Whoa!"
        marie "Are you serious!"
        pc "Let it out, Marie!"
        marie "Nooo!"
        marie "But keep doing that!"
        marie "Exactly like that!"
        marie "Ahhhh!"
    elif marie.stage >= 7:
        marie "Ohhh!"
        marie "How long can you last like this?"
        pc "Long enough."
        marie "I know you're giving me some good dick right now..."
        marie "But you're starting to turn me on even more."
        pc "Yeah?"
        marie "You impress me, [pc]."
        pc "You're the one who just drank twenty seven sodas."
        marie "I'm amazed you can still even talk right now."
        pc "Is that your way of telling me to shut up?"
        marie "No."
        marie "Maybe for a minute?"
        marie "I'm really close..."
        window hide
        pause
        marie "Ohhhh!"
        marie "[pc]!"
        marie "Cum with me!"
        marie "Yessss!"
    stop movie
    image marie_home_sex8 = "/marie/[marie.stage]/home_sex8.webp"
    scene marie_home_sex8
    if marie.stage <= 6:
        marie "Can we do this every night?"
        pc "Yes, please."
    elif marie.stage >= 7:
        marie "Can I keep you?"
        pc "I'd like that."
        marie "Good, because I don't think I could chase you."
        pc "I'm sure you could roll after me."
    if marie.stage >= 6:
        $ marie.weight += 2
    else:
        $ marie.weight += 1
    pause
    return

#Bunnie Bites Intro
label bbintro:
    $ rngworkgirl = 3
    call bbworking
    play music "/music/bunny_bites.ogg" if_changed
    "You head down to Bunny Bites."
    pc "Very busy again."
    image lisa_workattire_counter = "/lisa/1/workattire_counter.webp"
    scene lisa_workattire_counter
    lisa "Hello, welcome to Bunny Bites, my name is Lisa, how can I help you?"
    pc "Hey there Lisa, can I get a large pizza to go please?"
    lisa "I'm sorry but all our pizzas are sold out."
    lisa "It has been so incredibly busy lately, and we are super short staffed."
    pc "Oh that sounds horrible, how many servers do you have?"
    lisa "There's only three of us, and we've been struggling to find a replacement."
    pc "Hey, I could help out. I was looking for a way to make some extra cash."
    lisa "Humm, well normally we wouldn't take a male employee as a server."
    lisa "The cafe requires its servers to wear these bunny suits, but I could ask my manager if we are willing to make an exception."
    lisa "We could really use the extra help."
    lisa "Please have a seat in one of the booths."
    image lisa_workattire_counter_assview = "/lisa/1/workattire_counter_assview.webp"
    scene lisa_workattire_counter_assview
    "You take a seat in one of the booths."
    "Five minutes later."
    image marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene marie_serving2
    marie "Hello. I am Marie. Nice to meet you."
    pc "Hello, Marie. I'm [playername]."
    marie "I heard you were asking about a job."
    pc "Yeah, sounds like you guys could use some help."
    marie "As Lisa probably told you, we normally don't allow male employees to work here because the servers are required to wear these outfits."
    marie "But I think you can work the counter."
    pc "Sounds good."
    marie "Well in that case you can come in to work whenever you have time, we are always busy."
    pc "Thank you, see you soon."
    $ workunlock = 1
    "Work unlocked."
    scene outside
    stop music fadeout 1.0
    "You make your way back home."
    $ daytime += 1
    jump freetime

#Marie Events
label Marie_Stage_0_Event:
    ###DAY 1 - Marie ###
    "You receive a message on your phone from Marie."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Marie', dialogue=dialogue_one)
    $ msg ("Hello [playername].", who=1)
    pause
    $ msg ("It’s Marie from Bunny Bites, I was wondering if you were free to come in so I can show you a few things?", who=1)
    pause
    $ msg ("It will only be a couple of hours tops.", who=1)
    pause
    $ msg ("Sure, I'll be there in a minute.")
    pause
    $ msg ("Great, see you soon.", who=1)
    pause
    $ hide_messenger()

    ###Bunny bites###
    image marie_stage_0_event_1 = "/marie/events/stage0/1.webp"
    scene marie_stage_0_event_1
    play music "/music/bunny_bites.ogg" if_changed
    "Walking in it seems pretty quiet today."
    image marie_stage_0_event_2 = "/marie/events/stage0/2.webp"
    scene marie_stage_0_event_2
    marie "[playername], thank you for coming."
    pc "No problem."
    marie "Don’t worry and don’t feel nervous, I am just going to introduce you to everything."
    marie "I won't make you work a full shift yet."
    pc "Great, where do we start?"
    image marie_stage_0_event_3 = "/marie/events/stage0/3.webp"
    scene marie_stage_0_event_3
    marie "Have you worked in customer services before?"
    pc "I had a summer job at a fast food chain when I was in school."
    marie "Perfect, it will be pretty similar to that."
    image marie_stage_0_event_4 = "/marie/events/stage0/4.webp"
    scene marie_stage_0_event_4
    marie "Since we are here, why don't we start at the front of house, the till."
    image marie_stage_0_event_5 = "/marie/events/stage0/5.webp"
    scene marie_stage_0_event_5
    "Moving around the counter, Marie runs you through the various buttons and dials on the till."
    "Luckily, they are all labelled so it's pretty easy even if you don’t remember where everything is immediately."
    image marie_stage_0_event_6 = "/marie/events/stage0/6.webp"
    scene marie_stage_0_event_6
    marie "Everything making sense so far?"
    pc "I think so, main food items on the left, sides in the middle and extras on the right."
    marie "You got it."
    image marie_stage_0_event_7 = "/marie/events/stage0/7.webp"
    scene marie_stage_0_event_7
    marie "Next it is important to be polite and approachable to the customers."
    marie "Why don't we do a little roleplay?"
    image marie_stage_0_event_8 = "/marie/events/stage0/8.webp"
    scene marie_stage_0_event_8
    "Going around the counter, Marie pretends to be a customer."
    pc "Hello and welcome to Bunny Bites, can I take your order please?"
    image marie_stage_0_event_9 = "/marie/events/stage0/9.webp"
    scene marie_stage_0_event_9
    marie "Can I get two burgers, two fries and two large soda’s."
    pc "Absolutely."
    image marie_stage_0_event_10 = "/marie/events/stage0/10.webp"
    scene marie_stage_0_event_10
    "Looking down at the till it takes you a moment but you manage to input the order fairly easily."
    "It helps that whoever set up the till did it in a sensible way."
    image marie_stage_0_event_11 = "/marie/events/stage0/11.webp"
    scene marie_stage_0_event_11
    pc "That will be twelve dollars please."
    "Completing the transaction you place the imaginary cash back into the till and ring in the food."
    pc "Thank you, your food will be out shortly."
    pc "If you need anything else, please let me know."
    image marie_stage_0_event_12 = "/marie/events/stage0/12.webp"
    scene marie_stage_0_event_12
    marie "That was perfect, although you should always make sure to ask if a customer wants more."
    marie "If we have specials or sales, it is always worth seeing if they might be interested in it."
    pc "Oh ok, I’ll make sure to ask next time."
    image marie_stage_0_event_13 = "/marie/events/stage0/13.webp"
    scene marie_stage_0_event_13
    marie "Great, now then since it’s a bit quiet why don't we have a seat while those burgers come through."
    image marie_stage_0_event_14 = "/marie/events/stage0/14.webp"
    scene marie_stage_0_event_14
    "Looking to her right she waves over another staff member, you remember seeing her when you applied for the job."
    image marie_stage_0_event_15 = "/marie/events/stage0/15.webp"
    scene marie_stage_0_event_15
    marie "Lisa, would you mind running the till while we have a quick chat?"
    lisa "Sure thing."
    marie "Great, oh and this is [playername]."
    image marie_stage_0_event_16 = "/marie/events/stage0/16.webp"
    scene marie_stage_0_event_16
    lisa "Hi, it’s nice to meet you properly."
    pc "You too Lisa."
    image marie_stage_0_event_17 = "/marie/events/stage0/17.webp"
    scene marie_stage_0_event_17
    marie "We also have another server you might have seen before."
    marie "I gave her the day off today, but you will meet her shortly."
    "Grabbing your food, you and Marie take a seat in one of the booth’s."
    ### In booth with Marie slowly eating her food###
    image marie_stage_0_event_18 = "/marie/events/stage0/18.webp"
    scene marie_stage_0_event_18
    marie "So I wanted to talk about the way things work around here for a minute."
    pc "Sure thing."
    marie "We tend to operate in three shifts, a morning, afternoon and evening."
    image marie_stage_0_event_19 = "/marie/events/stage0/19.webp"
    scene marie_stage_0_event_19
    marie "It is a very flexible shift pattern which has its benefits for us all since we are a small team."
    marie "You get paid per shift you work but we don't have any incentives or overtime."
    marie "Basically, if you want to work a shift just let us know, even on the day is fine."
    pc "Ok, that sounds good."
    image marie_stage_0_event_20 = "/marie/events/stage0/20.webp"
    scene marie_stage_0_event_20
    marie "You have my number but I will give you Lisa and Amber’s as well so you can all chat and arrange shift changes if you need too."
    marie "With the four of us now working it gives everyone a chance to work more favourable shifts."
    marie "It might take a couple of weeks to get up to speed and everything to sort itself out."
    marie "It is a bit of a big change for us, so I don't want you to feel like it is all on you."
    image marie_stage_0_event_21 = "/marie/events/stage0/21.webp"
    scene marie_stage_0_event_21
    pc "Thank you, that is nice of you to say."
    image marie_stage_0_event_22 = "/marie/events/stage0/22.webp"
    scene marie_stage_0_event_22
    marie "We really are a team here, so if there is anything you need to talk about or if you are struggling just let one of us know."
    image marie_stage_0_event_23 = "/marie/events/stage0/23.webp"
    scene marie_stage_0_event_23
    pc "I will."
    image marie_stage_0_event_24 = "/marie/events/stage0/24.webp"
    scene marie_stage_0_event_24
    marie "Perfect, now I think that is all I need from you today."
    marie "I’ll put another training day in the diary so we can make sure you are up to speed before getting you to do your first full shift."
    marie "We will be in touch."
    ### standing up to leave ###
    image marie_stage_0_event_25 = "/marie/events/stage0/25.webp"
    scene marie_stage_0_event_25
    pc "Thanks for your help today and all the advice."
    marie "No problem."
    if recollection == False:
        $ money += 10
        "You earned ten dollars."
        $ daytime += 1
    stop music fadeout 1.0
    $ mariestage0event = 0
    return


label Marie_Stage_1_Event_1:
    ## Marie 1.1 Till issue ##
    #### While working a regular shift ###
    ###Marie comes in as a customer - didn’t want to link it to anyone else ###
    image marie_stage_1_event_1 = "/marie/events/stage1/1.webp"
    scene marie_stage_1_event_1
    play music "/music/bunny_bites.ogg" if_changed
    "A customer arrives."
    pc "Hey, it's Marie."
    image marie_stage_1_event_2 = "/marie/events/stage1/2.webp"
    scene marie_stage_1_event_2
    marie "Hey, how is my favourite co-worker today?"
    pc "Pretty good thanks."
    image marie_stage_1_event_3 = "/marie/events/stage1/3.webp"
    scene marie_stage_1_event_3
    marie "Great, I am just passing by and fancied some food."
    pc "What can I get you?"
    marie "Can I get a whole pizza?"
    pc "Sure thing."
    image marie_stage_1_event_4 = "/marie/events/stage1/4.webp"
    scene marie_stage_1_event_4
    "Going to type it into the till, it seems to freeze."
    image marie_stage_1_event_5 = "/marie/events/stage1/5.webp"
    scene marie_stage_1_event_5
    pc "Sorry, just having difficulty getting the order in."
    marie "Oh, is it freezing again?"
    marie "I hate this thing sometimes."

    ###Marie behind the counter with you.###
    image marie_stage_1_event_6 = "/marie/events/stage1/6.webp"
    scene marie_stage_1_event_6
    "Trying her luck Marie has the same issue, frustratedly slapping the till but even that doesn't seem to work."
    image marie_stage_1_event_7 = "/marie/events/stage1/7.webp"
    scene marie_stage_1_event_7
    marie "It does this from time to time. I’ll turn it off for a few minutes, that usually fixes it."
    pc "Thanks Marie."
    marie "No problem, in the meantime I always have a few of these under here."
    image marie_stage_1_event_8 = "/marie/events/stage1/8.webp"
    scene marie_stage_1_event_8
    "Kneeling down Marie pulls out a notepad."
    image marie_stage_1_event_9 = "/marie/events/stage1/9.webp"
    scene marie_stage_1_event_9
    marie "Just take the orders manually and stick this through to the kitchen. They will know what to do."
    pc "Great, thanks again."
    marie "No worries."
    image marie_stage_1_event_10 = "/marie/events/stage1/10.webp"
    scene marie_stage_1_event_10
    "Looking around for a moment, Marie can see there are no other customers."
    image marie_stage_1_event_11 = "/marie/events/stage1/11.webp"
    scene marie_stage_1_event_11
    pause
    image marie_stage_1_event_12 = "/marie/events/stage1/12.webp"
    scene marie_stage_1_event_12
    marie "Since it is just us, fancy joining me while I eat. I’d love to catch up with how you are finding everything."
    marie "Or at least until a customer arrives."
    pc "That would be nice."

    ### At table ###
    image marie_stage_1_event_13 = "/marie/events/stage1/13.webp"
    scene marie_stage_1_event_13
    "Taking over Marie’s food a few minutes later, you join her at the table."
    marie "So, how are you finding everything?"
    pc "Yeah, I think everything is going well."
    image marie_stage_1_event_14 = "/marie/events/stage1/14.webp"
    scene marie_stage_1_event_14
    marie "You don't seem too sure?"
    pc "Sorry, it’s hard to know how I have been measuring up to your expectations."
    pc "Lisa and Amber have been super nice and showed me how to do everything."
    image marie_stage_1_event_15 = "/marie/events/stage1/15.webp"
    scene marie_stage_1_event_15
    marie "That is great to hear, it has been a hectic last few months since the last waitress quit."
    marie "It has been good to finally be able to let them both have some more time off."
    image marie_stage_1_event_16 = "/marie/events/stage1/16.webp"
    scene marie_stage_1_event_16
    "Taking a big bite from her Pizza Marie seems deep in thought for a moment as she enjoys her food."
    pc "What about me, anything I could do to improve?"
    image marie_stage_1_event_17 = "/marie/events/stage1/17.webp"
    scene marie_stage_1_event_17
    marie "Nothing springs to mind, haven't had any complaints if that is what you mean."
    marie "In fact, I think having you here might be bringing in some new customers."
    marie "Or at least bringing back old ones more regularly."
    pc "What do you mean?"
    image marie_stage_1_event_18 = "/marie/events/stage1/18.webp"
    scene marie_stage_1_event_18
    marie "Oh nothing, I just feel like I am seeing some of our customers a lot more lately."
    marie "Maybe it's just because I have more time to watch them."
    pc "Oh ok."
    image marie_stage_1_event_19 = "/marie/events/stage1/19.webp"
    scene marie_stage_1_event_19
    "Finishing off her pizza Marie leans back stretching, giving you a good view of her full stomach."
    image marie_stage_1_event_20 = "/marie/events/stage1/20.webp"
    scene marie_stage_1_event_20
    pause
    image marie_stage_1_event_21 = "/marie/events/stage1/21.webp"
    scene marie_stage_1_event_21
    "You are surprised that someone as small as Marie could eat so much."
    image marie_stage_1_event_22 = "/marie/events/stage1/22.webp"
    scene marie_stage_1_event_22
    "But looking up you accidentally catch her eyes, had she seen you staring at her belly?"
    "Behind you, you hear the door open as a customer arrives, saving you from this awkward moment."
    image marie_stage_1_event_23 = "/marie/events/stage1/23.webp"
    scene marie_stage_1_event_23
    pc "I uhhh, better get back to work."
    marie "Sure, it was nice catching up with you [playername]."
    ###Go back to working regular shift.###
    if recollection == True:
        $ marie.weight += 0.5
        stop music fadeout 1.0
    $ mariestage1event = 0
    return

label Marie_Stage_1_Event_2:
    #First sitdown where Marie admits her love for feeding girls
    image marie_idle_workattire_event1 = "/marie/1/idle_workattire.webp"
    scene marie_idle_workattire_event1
    play music "/music/bunny_bites.ogg" if_changed
    marie "Hey, do you want to hang out a bit before going home?"
    pc "Sure."
    image marie_afterwork_sitdown1_event1 = "/marie/1/afterwork_sitdown1.webp"
    scene marie_afterwork_sitdown1_event1
    "Marie sits down in one of the booths."
    marie "Finally, the day is done."
    image marie_afterwork_sitdown2_event1 = "/marie/1/afterwork_sitdown2.webp"
    scene marie_afterwork_sitdown2_event1
    marie "I need to talk to you about something."
    marie "I've been monitoring a lot of personal information about everyone who works here."
    image marie_afterwork_sitdown3_event1 = "/marie/1/afterwork_sitdown3.webp"
    scene marie_afterwork_sitdown3_event1
    marie "And I think we have something in common."
    pc "Oh?"
    marie "We both like seeing women get fatter."
    "Slightly terrified by how she found that out, you say nothing since it'd be a lie to say she's wrong."
    image marie_afterwork_sitdown4_event1 = "/marie/1/afterwork_sitdown4.webp"
    scene marie_afterwork_sitdown4_event1
    marie "I only realized this recently, when one of our customers gained some weight."
    marie "I felt so aroused just seeing her and thinking about how much she had gained."
    image marie_afterwork_sitdown5_event1 = "/marie/1/afterwork_sitdown5.webp"
    scene marie_afterwork_sitdown5_event1
    marie "I never thought this would be my fetish but it is and I can't do anything about it."
    marie "So my genius plan is to fatten up Amber and Lisa."
    marie "I made a new rule recently, that all employees can eat as much food after work as they want."
    image marie_afterwork_sitdown6_event1 = "/marie/1/afterwork_sitdown6.webp"
    scene marie_afterwork_sitdown6_event1
    marie "It helps that the girls already seem to have quite an appetite haha."
    marie "Could you help me fatten up Amber and Lisa?"
    pc "Well, as long as they are fine with their growing bodies I'm up for it."
    marie "This is going to be great, also please don’t tell them anything I told you, okay?"
    pc "Your secret is safe with me."
    marie "Would you want to help me clean this place up?"
    pc "Yeah of course."
    "Marie and you clean up the whole place."
    image marie_afterwork_sitdown7_event1 = "/marie/1/afterwork_sitdown7.webp"
    scene marie_afterwork_sitdown7_event1
    marie "Thanks for the help."
    marie "And thanks for the talk. It's nice to have a kindred spirit."
    pc "You can always talk to me about anything, Marie."
    marie "Glad to hear it. Good night."
    stop music fadeout 1.0
    $ mariestage1event2 = 0
    return


label Marie_Stage_2_Event_1:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Marie', dialogue=dialogue_one)
    $ msg ("Hi, [playername]. Can you come to Bunny Bites? It is extremely busy and we need your help.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright, We will try to handle it then.", who=1)
            pause
            $ hide_messenger()
            return
    image work_marie_workattire_counter_event2 = "/marie/2/workattire_counter.webp"
    scene work_marie_workattire_counter_event2
    if recollection == False:
        $ amber_work_today = 1
        $ lisa_work_today = 1
        $ marie_work_today = 1
    play music "/music/bunny_bites.ogg" if_changed
    marie "Hey, thanks for coming."
    marie "It's really busy today, I'll let you work the counter. Lisa, Amber and I will be handling service."
    image marie_stage_2_event_1 = "/marie/events/stage2/1.webp"
    scene marie_stage_2_event_1
    "Marie quickly walks off to help the other girls."
    if recollection == False:
        call work_randomizer from _call_work_randomizer_4
    image marie_stage_2_event_2 = "/marie/events/stage2/2.webp"
    scene marie_stage_2_event_2
    "You see the girls working their asses off."
    if recollection == False:
        call work_randomizer from _call_work_randomizer_5
    image marie_stage_2_event_3 = "/marie/events/stage2/3.webp"
    scene marie_stage_2_event_3
    "The rest of the shift goes by while you work as fast as you can."
    image marie_stage_2_event_4 = "/marie/events/stage2/4.webp"
    scene marie_stage_2_event_4
    "After a long day, all the customers are finally gone."
    if recollection == False:
        $ money += 30
        "You earned thirty dollars."
    marie "Thanks guys, I couldn't have done this without you."
    lisa "Don't worry, I'll always be here if you need me."
    amber "Same goes for me, together we can handle anything."
    pc "You can call me anytime you need me to come in for emergencies like these."
    image marie_stage_2_event_5 = "/marie/events/stage2/5.webp"
    scene marie_stage_2_event_5
    lisa "Could you clean some of the booths? I want to talk to the girls for a minute."
    pc "Sure thing!"
    image marie_stage_2_event_6 = "/marie/events/stage2/6.webp"
    scene marie_stage_2_event_6
    "While cleaning you see the girls listen to Lisa."
    "Is she telling them that she is attracted to women?"
    image marie_stage_2_event_7 = "/marie/events/stage2/7.webp"
    scene marie_stage_2_event_7
    "After a while they start hugging Lisa, I hope it's all good."
    image marie_stage_2_event_8 = "/marie/events/stage2/8.webp"
    scene marie_stage_2_event_8
    marie "Hey, would you want to come with me to my home after we are done cleaning?"
    marie "I want to discuss something with you."
    pc "Yeah, of course."
    image marie_stage_2_event_9 = "/marie/events/stage2/9.webp"
    scene marie_stage_2_event_9
    "The girls and you finish up cleaning the whole place."
    "After everyone switched their attire, we came back together for a little talk."
    image marie_stage_2_event_10 = "/marie/events/stage2/10.webp"
    scene marie_stage_2_event_10
    amber "Phew, I am glad we are done here today, I'm going home to take a nap."
    lisa "Yeah, I'm also leaving. See ya later."
    pc "Good evening, Amber and Lisa."
    marie "Have a good evening."
    image marie_stage_2_event_11 = "/marie/events/stage2/11.webp"
    scene marie_stage_2_event_11
    "Amber and Lisa left Bunny Bites, leaving you alone with Marie."
    marie "Ok, let's go to my home."
    stop music fadeout 1.0
    image marie_home_arrive_event2 = "/marie/2/home_arrive.webp"
    scene marie_home_arrive_event2
    play music "/music/date_cozy.ogg" if_changed
    marie "Make yourself at home."
    pc "Your home looks really nice and comfy."
    marie "Thank you!"
    image marie_home_sitting1_event2 = "/marie/2/home_sitting1.webp"
    scene marie_home_sitting1_event2
    marie "So there is another reason I brought you here."
    marie "Ever since our little chat last time, I can't stop thinking about Lisa and Amber."
    marie "What it would be like to see them fatten up and get all chubby."
    marie "It’s been driving me crazy, I could barely look them in the face earlier."
    pc "Wow, you are really into this aren’t you."
    marie "Yes, aren’t you?"
    pc "You know I am."
    marie "We need a plan on how to get them to eat more."
    pc "How do you suppose we do that?"
    marie "I’ve got a couple of ideas."
    marie "First I will give you the ability to increase the amount of food a customer orders on the till."
    marie "I’ll give you a special discount code to put in for the extra food so you won't have to pay too much for the difference."
    marie "I’d love it if you could use it on Lisa and Amber when they come in for their food, but feel free to use it on other customers too."
    pc "Great idea, I’ll certainly make use of this."
    image marie_home_sitting2_event2 = "/marie/2/home_sitting2.webp"
    scene marie_home_sitting2_event2
    marie "My second idea is about Amber."
    marie "She sometimes goes to this bar in town after work, you should go with her sometime."
    marie "I’ve seen her at parties and noticed that once she gets a bit tipsy she cant stop eating."
    marie "I remember our last christmas party, there was so much food and after a few drinks Amber was…"
    marie "But I am getting distracted, that's a story for another time."
    marie "However, I know we can use this to our advantage."
    pc "Sure, that sounds like a good plan."
    image marie_home_sitting3_event2 = "/marie/2/home_sitting3.webp"
    scene marie_home_sitting3_event2
    marie "As for Lisa, she told us earlier that she has a big crush on me and Amber."
    marie "Honestly, I was kind of surprised. I knew we had flirted sometimes but thought it was just for fun."
    marie "I think I’ll use this opportunity to tell her I like bigger women. Maybe she will want to gain a little bit to be with me."
    marie "Just make sure to be encouraging if she ever asks you about any of this."
    pc "Has anyone ever told you that you’d make a great evil mastermind."
    pc "But I love the ideas."
    image marie_home_strip_event2 = "/marie/2/home_strip.webp"
    scene marie_home_strip_event2
    marie "Amazing, between us, Lisa and Amber will be bursting out of their uniforms in no time."
    marie "Ughh, it's so hot to think of them gaining for us. Just fantasizing about all of this makes me so fucking horny."
    marie "It makes me want to do things to them, but for now I guess It’s just you and me."
    marie "Do you want to see what I do when I get horny on my own, I think you will enjoy it and I know I will."
    pc "Uhh, I don't know what to say."
    marie "Fuck it, I can take it any more. Stay there and enjoy."
    image marie_home_strip2_event2 = "/marie/2/home_strip2.webp"
    scene marie_home_strip2_event2
    "She takes off her sweater while looking at you with a look of pure desire. It is clear she is entranced by her own lusty thoughts."
    marie "Follow me."
    image marie_home_drink1_event2 = "/marie/2/home_drink1.webp"
    scene marie_home_drink1_event2
    "Marie walks over to her kitchen. She has a whole bunch of sugary drinks on her counter."
    marie "Would you like to see me drink all this soda?"
    pc "That's a lot of soda, are you sure?"
    marie "I've been doing this for a while, I know what I'm doing."
    pc "In that case, yes, I want to see you drink it all."
    image marie_home_drink2_event2 = "/marie/2/home_drink2.webp"
    scene marie_home_drink2_event2
    "As if it didn't matter what you said Marie started drinking the soda."
    "The speed of her drinking is astounding."
    image marie_home_stuffed1_event2 = "/marie/2/home_stuffed1.webp"
    scene marie_home_stuffed1_event2
    "You watch her belly grow in real time as she keeps drinking."
    image marie_home_stuffed2_event2 = "/marie/2/home_stuffed2.webp"
    scene marie_home_stuffed2_event2
    "Her belly just keeps getting bigger from the soda, you can hear the liquid slosh around with every move she makes."
    image marie_stage_2_event_12 = "/marie/events/stage2/12.webp"
    scene marie_stage_2_event_12
    "While Marie starts drinking the last soda cup, you can't stop looking at her now gigantic stuffed belly."
    image marie_home_stuffed3_event2 = "/marie/2/home_stuffed3.webp"
    scene marie_home_stuffed3_event2
    marie "That feels soo good."
    pc "You look nine months pregnant."
    marie "I know, it looks great doesn't it?"
    pc "Hell yeah."
    image marie_home_strip3_event2 = "/marie/2/home_strip3.webp"
    scene marie_home_strip3_event2
    "Marie slowly walks over to her bed, taking off her pants and laying down."
    image marie_home_bed1_event2 = "/marie/2/home_bed1.webp"
    scene marie_home_bed1_event2
    marie "This is what I do when I get horny."
    marie "The feeling of my belly being stuffed to the max with liquid feels sooo good."
    if persistent.masturbation:
        scene black with dissolve
        "Marie had a good time."
    else:
        image marie_stage_2_event_16 = "/marie/events/stage2/16.webp"
        scene marie_stage_2_event_16
        "Marie starts rubbing her clit while making sounds that can only be described as pure pleasure."
        image marie_stage_2_event_17 = "/marie/events/stage2/17.webp"
        scene marie_stage_2_event_17
        "A short while later she starts to climax with a loud moan."
    image marie_stage_2_event_18 = "/marie/events/stage2/18.webp"
    scene marie_stage_2_event_18
    "Marie slowly comes back to her senses."
    marie "I hope you enjoyed this little show, I always fantasize how it would be to have a big bulging fat belly."
    marie "Stuffing myself with soda is the closest I can come to this in reality."
    marie "Some days I just stuff myself and then admire myself in the mirror the rest of the day."
    image marie_home_end_event2 = "/marie/2/home_end.webp"
    scene marie_home_end_event2
    marie "Next time I'll let you join in on the fun, if you would like that of course."
    marie "But for now I'm gonna relax. Don't forget our plan with Amber and Lisa."
    marie "Have a good evening."
    pc "Good evening, Marie."
    stop music fadeout 1.0
    scene outside2
    pc "Wow, that was really hot. I had no idea Marie was into that."
    "You go back home."
    #Unlocks repeatable marie home visits where you feed and fuck her.
    if recollection == False:
        $ daytime += 2
        $ phonecall = 1
        $ marie.weight += 1
        $ mariestage2event = 0
        #Unlocks Marie Undress in the stats page.
        $ renpy.notify("Marie Undress option unlocked in stats screen.")
        window hide
        pause
    return

label Marie_Stage_2_Event_2:
    ## Marie 2.2 secret button (just a little extra bit of dialogue)##
    #### At the end of working a regular shift with Marie ###
    ###Marie behind / at the counter ###
    image marie_stage_2_event_19 = "/marie/events/stage2/19.webp"
    scene marie_stage_2_event_19
    play music "/music/bunny_bites.ogg" if_changed
    "You notice two woman arriving together."
    "You think you might have seen them before, although you remember the left woman being skinnier."
    image marie_stage_2_event_20 = "/marie/events/stage2/20.webp"
    scene marie_stage_2_event_20
    $ unknownname = 'Tanned woman'
    pc "Hello, welcome to Bunny Bites. What can I get you two?"
    unknown "Can I get the chungus deluxe meal please."
    pc "One chungus deluxe meal, and what can I get for you ma'am?"
    $ unknownname = 'Pale woman'
    unknown "Just a small cola please."
    pc "Coming right up. Why don’t you two find a booth and I’ll bring that out to you when it’s done."
    $ unknownname = 'Tanned woman'
    unknown "Thank you."
    image marie_stage_2_event_21 = "/marie/events/stage2/21.webp"
    scene marie_stage_2_event_21
    $ unknownname = 'Pale woman'
    unknown "Hey, could you double her meal. I'll pay the difference."
    pc "Uhh, yeah sure, I can do that."
    unknown "Nice, keep it between us though."
    "You take your time to make sure the double meal doesn't appear on the receipt."
    image marie_stage_2_event_22 = "/marie/events/stage2/22.webp"
    scene marie_stage_2_event_22
    "After the food is ready, you bring it over to their table."
    pc "Here you go, a chungus deluxe meal and a small cola."
    $ unknownname = 'Tanned woman'
    unknown "Woah, that is a lot, thank you though."
    image marie_stage_2_event_23 = "/marie/events/stage2/23.webp"
    scene marie_stage_2_event_23
    "As you walk back behind the counter, you keep an eye on the two woman."
    $ unknownname = 'Unknown'
    image marie_stage_2_event_24 = "/marie/events/stage2/24.webp"
    scene marie_stage_2_event_24
    marie "Hey [playername]."
    pc "Hi Marie."
    image marie_stage_2_event_25 = "/marie/events/stage2/25.webp"
    scene marie_stage_2_event_25
    marie "How is it all going?"
    pc "Yeah, everything is fine."
    pc "Thanks for sorting out the till before, haven’t had any problems since."
    marie "Great, glad to hear it."
    image marie_stage_2_event_26 = "/marie/events/stage2/26.webp"
    scene marie_stage_2_event_26
    marie "It acts up from time to time so don't worry too much if it happens again."
    "Moving slightly closer Marie’s demeanour changes."
    image marie_stage_2_event_27 = "/marie/events/stage2/27.webp"
    scene marie_stage_2_event_27
    marie "And good work on all those extra orders."
    marie "I have seen a few of our regulars packing on the pounds because of it."
    marie "Watching them get fat almost makes me want to work every shift, so I don't miss anything."
    marie "But to make it easier, I was rooting around with the till earlier and I added a new option to make it quicker."
    image marie_stage_2_event_28 = "/marie/events/stage2/28.webp"
    scene marie_stage_2_event_28
    "Leaning over she shows you an unmarked button on the till."
    marie "Pressing that will automatically add on the code and double the order size."
    marie "Although, feel free to add even more if you want."
    image marie_stage_2_event_29 = "/marie/events/stage2/29.webp"
    scene marie_stage_2_event_29
    pc "Great, that will make it easier."
    marie "Amazing, keep up the good work."
    ###New customer arrives###
    image marie_stage_2_event_30 = "/marie/events/stage2/30.webp"
    scene marie_stage_2_event_30
    "As Marie leaves to help more customers, you take a look back at the two woman you served before."
    "To your surprise the tanned woman has already eaten all the food."
    "Her belly seemingly stuffed to the limit, she looks to be in a state of discomfort."
    image marie_stage_2_event_31 = "/marie/events/stage2/31.webp"
    scene marie_stage_2_event_31
    "As they start to leave, you can clearly see her having trouble moving around in her engorged state."
    image marie_stage_2_event_32 = "/marie/events/stage2/32.webp"
    scene marie_stage_2_event_32
    "The pale woman seems to really enjoy this whole situation. She seems to be unable to keep her eyes off her friends round belly."
    if recollection == True:
        stop music fadeout 1.0
    $ mariestage2event2 = 0
    return


label Marie_Stage_3_Event_1:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Marie', dialogue=dialogue_one)
    $ msg ("Hi, [playername]. Can you come to Bunny Bites? It is extremely busy and we need your help.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright. We will try to handle it then.", who=1)
            pause
            $ hide_messenger()
            return

    image work_marie_workattire_counter_event3 = "/marie/3/workattire_counter.webp"
    scene work_marie_workattire_counter_event3
    if recollection == False:
        $ amber_work_today = 1
        $ lisa_work_today = 1
        $ marie_work_today = 1
    play music "/music/bunny_bites.ogg" if_changed
    marie "Hey. Thanks for coming."
    marie "It is really busy today. I'll let you work the counter. Lisa, Amber and I will be on service."
    image marie_stage_3_event_1 = "/marie/events/stage3/1.webp"
    scene marie_stage_3_event_1
    "Marie quickly walks off to help the other girls."
    if recollection == False:
        call work_randomizer from _call_work_randomizer_6
    image marie_stage_3_event_2 = "/marie/events/stage3/2.webp"
    scene marie_stage_3_event_2
    "You see the girls working their asses off."
    image marie_stage_3_event_3 = "/marie/events/stage3/3.webp"
    scene marie_stage_3_event_3
    "The rest of the shift goes by while you work as fast as you can."
    image marie_stage_3_event_4 = "/marie/events/stage3/4.webp"
    scene marie_stage_3_event_4
    "After a long day, all the customers are finally gone."
    if recollection == False:
        $ money += 30
        "You earned thirty dollars."
    marie "Thanks, guys. I couldn't have done this without you."
    image marie_stage_3_event_5 = "/marie/events/stage3/5.webp"
    scene marie_stage_3_event_5
    lisa "Now you have to hold up your end of the bargain."
    amber "Yeah, Marie. Start making those burgers for us."
    pc "What is this bargain you are talking about?"
    image marie_stage_3_event_6 = "/marie/events/stage3/6.webp"
    scene marie_stage_3_event_6
    lisa "She didn't tell you?"
    marie "I asked them to come in to help, but in return I would be making them as many burgers as they want."
    image marie_stage_3_event_7 = "/marie/events/stage3/7.webp"
    scene marie_stage_3_event_7
    amber "You realize that I'm gonna eat until I pass out, right?"
    lisa "Gimme some burgers!"
    marie "Can you help me out, [playername]?"
    pc "Sure thing!"
    "Marie and you start making burgers for the girls."
    image marie_stage_3_event_8 = "/marie/events/stage3/8.webp"
    scene marie_stage_3_event_8
    "While putting the burgers together, Marie whispers in your ear."
    marie "Make them extra greasy. They'll love it."
    "As requested, you make the burgers a lot more greasy."
    image marie_stage_3_event_9 = "/marie/events/stage3/9.webp"
    scene marie_stage_3_event_9
    marie "Here you go."
    lisa "Ha! You think Amber and I are satisfied with three burgers each?"
    amber "Yeah, Marie, this wasn't what you promised. You said we'd get as many as we wanted."
    marie "Sure I can make more, but you have to eat them all then."
    image marie_stage_3_event_10 = "/marie/events/stage3/10.webp"
    scene marie_stage_3_event_10
    lisa "Deal!"
    amber "No problem."
    marie "How many more should I make then?"
    amber "Two more."
    image marie_stage_3_event_11 = "/marie/events/stage3/11.webp"
    scene marie_stage_3_event_11
    lisa "No no, four."
    amber "Four?! Then we got to eat seven total."
    lisa "We got this, Amber."
    image marie_stage_3_event_12 = "/marie/events/stage3/12.webp"
    scene marie_stage_3_event_12
    marie "[playername], can you start making the extra burgers?"
    pc "Coming right up."
    image marie_stage_3_event_13 = "/marie/events/stage3/13.webp"
    scene marie_stage_3_event_13
    "You notice both Amber and Lisa going at it.They make pigs of themselves as they eat messily."
    image marie_stage_3_event_14 = "/marie/events/stage3/14.webp"
    scene marie_stage_3_event_14
    "Marie seems to really enjoy watching her coworkers eat all those burgers."
    image marie_stage_3_event_15 = "/marie/events/stage3/15.webp"
    scene marie_stage_3_event_15
    "You give both girls the remaining burgers."
    amber "Are you sure we can do this?"
    lisa "We got this."
    image marie_stage_3_event_16 = "/marie/events/stage3/16.webp"
    scene marie_stage_3_event_16
    "The girls keep eating the burgers at a reasonable speed."
    image marie_stage_3_event_17 = "/marie/events/stage3/17.webp"
    scene marie_stage_3_event_17
    "As Lisa continues to gleefully gorge herself, Amber has a sort of pained expression on her face. But her moans let you know that she's still enjoying this."
    image marie_stage_3_event_18 = "/marie/events/stage3/18.webp"
    scene marie_stage_3_event_18
    "Marie is clearly pleased with the girls' greed. She walks up to Lisa and shoves another burger into her mouth."
    "Lisa squeals with delight and you can hear Marie whisper something."
    marie "Good girl, good girl..."
    image marie_stage_3_event_19 = "/marie/events/stage3/19.webp"
    scene marie_stage_3_event_19
    "Once they're finished, you and Marie have to help the girls stand up."
    "Amber seems too stuffed to talk and just leaves."
    "Meanwhile, Marie is talking with Lisa as she helps her towards the door."
    marie "I think we should continue this interesting discussion at my place, Lisa."
    image marie_stage_3_event_20 = "/marie/events/stage3/20.webp"
    scene marie_stage_3_event_20
    "Marie gives you a wink as she walks out the door."
    "You lock up and head home."
    pc "I love this job..."
    stop music fadeout 1.0

    #After this you start stage4 for all characters, The stages will be syncronized and you get a lot more feeding prompts during normal work.
    if recollection == False:
        $ daytime += 2
        $ phonecall = 1
        $ amber.weight = 73
        $ lisa.weight = 67
        $ marie.weight = 80
    $ mariestage3event = 0
    return

label Marie_Stage_3_Event_2:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Marie', dialogue=dialogue_one)
    $ msg ("Hey, could you come over to my house?", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sure, what's up?")
            pause
            $ msg ("We better talk about that in person, see you in a bit.", who=1)
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright. Another time then.", who=1)
            pause
            $ hide_messenger()
            return
    "You wonder what it is about, hopefully it's nothing bad."
    "You make yourself ready and walk over to Marie's place."

    image marie_stage_3_event_21 = "/marie/events/stage3/21.webp"
    scene marie_stage_3_event_21
    play music "/music/date_cozy.ogg" if_changed
    pc "Hey Marie."
    marie "Hey [playername], thank you for coming on such short notice."
    marie "Let's sit on the couch for a bit."
    image marie_stage_3_event_22 = "/marie/events/stage3/22.webp"
    scene marie_stage_3_event_22
    "Watching Marie sit down on the couch, she seemed different, not her usually outgoing self."
    image marie_stage_3_event_43 = "/marie/events/stage3/43.webp"
    scene marie_stage_3_event_43
    pc "Is everything ok?"
    image marie_stage_3_event_44 = "/marie/events/stage3/44.webp"
    scene marie_stage_3_event_44
    marie "Honestly, I don't know."
    marie "It's kind of what I wanted to talk to you about, if you are ok with it."
    image marie_stage_3_event_32 = "/marie/events/stage3/32.webp"
    scene marie_stage_3_event_32
    pc "You can tell me anything, I would have thought you would have realised that by now."
    pc "What's wrong?"
    image marie_stage_3_event_40 = "/marie/events/stage3/40.webp"
    scene marie_stage_3_event_40
    marie "Nothing is wrong, or maybe it is, I don't know."
    image marie_stage_3_event_41 = "/marie/events/stage3/41.webp"
    scene marie_stage_3_event_41
    marie "You know how I asked you to help fatten up Lisa and Amber?"
    pc "It's hard to forget."
    image marie_stage_3_event_27 = "/marie/events/stage3/27.webp"
    scene marie_stage_3_event_27
    marie "Well, I have been watching them grow these past few days."
    marie "They have both been eating so much, I never thought it would happen this quickly."
    image marie_stage_3_event_25 = "/marie/events/stage3/25.webp"
    scene marie_stage_3_event_25
    marie "Their weight has gone up so quickly, and their bodies have really ballooned outwards."
    pc "I thought that's what you wanted?"
    image marie_stage_3_event_24 = "/marie/events/stage3/24.webp"
    scene marie_stage_3_event_24
    marie "It is, but I never stopped to think if it's what they want."
    marie "The three of us are like family, we have worked at the diner for years, just the three of us servers."
    image marie_stage_3_event_31 = "/marie/events/stage3/31.webp"
    scene marie_stage_3_event_31
    marie "I don't want to ruin that by pushing them to gain weight if it's not something they want for themselves."
    pc "It's kind of you to worry about them, although I feel like you have been pretty open with them."
    image marie_stage_3_event_40 = "/marie/events/stage3/40.webp"
    scene marie_stage_3_event_40
    marie "I am just worried I am manipulating them both, especially Lisa."
    image marie_stage_3_event_43 = "/marie/events/stage3/43.webp"
    scene marie_stage_3_event_43
    marie "I feel like I am using the fact she liked me against her."
    pc "Do you not like Lisa?"
    image marie_stage_3_event_42 = "/marie/events/stage3/42.webp"
    scene marie_stage_3_event_42
    marie "What, no it's not that …I don't know anymore."
    image marie_stage_3_event_41 = "/marie/events/stage3/41.webp"
    scene marie_stage_3_event_41
    marie "The more she has gained the more I can't keep my eyes off her."
    marie "But what if they don't like being fat?"
    image marie_stage_3_event_39 = "/marie/events/stage3/39.webp"
    scene marie_stage_3_event_39
    marie "I didn’t imagine that a little push to gain would cause them to gain so much so quickly."
    pc "If it would make you feel better, I can ask them and see how they are feeling."
    image marie_stage_3_event_36 = "/marie/events/stage3/36.webp"
    scene marie_stage_3_event_36
    marie "Really, that would be great!"
    image marie_stage_3_event_45 = "/marie/events/stage3/45.webp"
    scene marie_stage_3_event_45
    marie "I’ll make it worth your while."
    image marie_stage_3_event_46 = "/marie/events/stage3/46.webp"
    scene marie_stage_3_event_46
    marie "I can't imagine why, but we seem to have been doing really well recently."
    image marie_stage_3_event_47 = "/marie/events/stage3/47.webp"
    scene marie_stage_3_event_47
    marie "Even with all the extra food we seem to be misplacing."
    pc "Don't worry about that, I just want to make sure everyone is happy."
    marie "Thank you."
    image marie_stage_3_event_33 = "/marie/events/stage3/33.webp"
    scene marie_stage_3_event_33
    "Marie gives you a tight hug."
    "Although she is talking about the growth of Lisa and Amber, Marie herself feels a lot softer then before."
    image marie_stage_3_event_35 = "/marie/events/stage3/35.webp"
    scene marie_stage_3_event_35
    "You decide to bring up her own gain to have a practice conversation about it."
    pc "What about you though, do you enjoy the weight you have gained?"
    image marie_stage_3_event_36 = "/marie/events/stage3/36.webp"
    scene marie_stage_3_event_36
    "You seem to have caught Marie by surprise."
    marie "What?! I only gained a little bit."
    marie "If I wanted I would be just as slim as before in a week."
    image marie_stage_3_event_37 = "/marie/events/stage3/37.webp"
    scene marie_stage_3_event_37
    marie "I just happen to eat a bit more when I'm with Lisa and Amber."
    marie "All my clothes still fit just like before."
    marie "Maybe I'm still a bit bloated from the other day when I did another liquid bloating session."
    "Marie seems to be making excuses for her weight gain."
    image marie_stage_3_event_38 = "/marie/events/stage3/38.webp"
    scene marie_stage_3_event_38
    marie "Anyways, I think all of this has something to do with you."
    pc "What did I do?"
    image marie_stage_3_event_39 = "/marie/events/stage3/39.webp"
    scene marie_stage_3_event_39
    marie "Have you seen all the woman you hang out with lately, they have all blown up."
    marie "You are radiating some sort of aura, whenever I'm with you I feel it too."
    image marie_stage_3_event_40 = "/marie/events/stage3/40.webp"
    scene marie_stage_3_event_40
    "She seems to think for a moment."
    image marie_stage_3_event_41 = "/marie/events/stage3/41.webp"
    scene marie_stage_3_event_41
    marie "Maybe I have gained some weight, so what?"
    pc "I was just asking if you are okay with that."
    image marie_stage_3_event_42 = "/marie/events/stage3/42.webp"
    scene marie_stage_3_event_42
    marie "Yes."
    image marie_stage_3_event_43 = "/marie/events/stage3/43.webp"
    scene marie_stage_3_event_43
    "While she quickly answered, you can see her having a bit of internal conflict on this matter."
    "Marie went silent for minute."
    image marie_stage_3_event_44 = "/marie/events/stage3/44.webp"
    scene marie_stage_3_event_44
    menu:
        marie "Hey, do you like me being bigger?"
        "Yes, you look better then ever.":
            image marie_stage_3_event_45 = "/marie/events/stage3/45.webp"
            scene marie_stage_3_event_45
            "Marie blushes."
            marie "Thank you!"
            marie "I don't know why, but you telling me that puts me at ease."
            image marie_stage_3_event_46 = "/marie/events/stage3/46.webp"
            scene marie_stage_3_event_46
            marie "I should however hold back on eating so much."
            marie "At this rate, all employees except you will be unable to do their work effectively in a year."

        "You look great no matter what size you are.":
            image marie_stage_3_event_45 = "/marie/events/stage3/45.webp"
            scene marie_stage_3_event_45
            "Marie blushes."
            marie "Why do you have to be so cheesy about it."
            marie "But thanks."
            image marie_stage_3_event_46 = "/marie/events/stage3/46.webp"
            scene marie_stage_3_event_46
            marie "Man, I could really go for some food right now."
            marie "But, I need to stay strong, otherwise you'll have to do all the work at Bunny Bites while us three can't even get off their asses anymore."

    image marie_stage_3_event_47 = "/marie/events/stage3/47.webp"
    scene marie_stage_3_event_47
    "You talk a bit more about work with Marie before going home."
    "On your way out you can't help but think about the fact that this is the first time the ever confident, outgoing Marie has shown off a vulnerable, yet kind side of herself to you."
    image marie_stage_3_event_48 = "/marie/events/stage3/48.webp"
    scene marie_stage_3_event_48
    "She clearly has feelings for both Lisa and Amber beyond a physical attraction."
    "Internalizing her own conflicting feelings about her weight gain have likely started to make her feel a bit guilty for how she's handled her feelings thus far."
    "You realize you've been contemplating about the situation just a second too long, as your concentration is broken by the raise of Marie's hand waving goodbye to you."
    "Saying your farewells you head out."
    stop music fadeout 1.0
    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
    $ mariestage3event2 = 0
    return

label Marie_Stage_4_Event_1:
    ###Marie stage 4 event - After working with her and go home to bloat?###
    ### Standard work event with Marie where she asks you to go home with her.###
    "You're sure it must have been a rough week for Marie not knowing how the girls' felt about their weight gain after your previous talk."
    image marie_stage_4_event_1 = "/marie/events/stage4/1.webp"
    scene marie_stage_4_event_1
    play music "/music/date_cozy.ogg" if_changed
    "You take extra care to promptly arrive at Marie's. When you get there she is already seated on the couch and you make your way over to join her."
    "Seated next to you on the couch it’s clear Marie has been waiting to ask you something."
    marie "So I was wondering if you had gotten a chance to speak to Lisa and Amber yet?"
    pc "I did."
    image marie_stage_4_event_2 = "/marie/events/stage4/2.webp"
    scene marie_stage_4_event_2
    marie "How did it go, although I am not sure I can take it if they hate me for what I have done to them."
    pc "You don't have to worry about that."
    pc "They both like the weight they have gained."
    image marie_stage_4_event_3 = "/marie/events/stage4/3.webp"
    scene marie_stage_4_event_3
    marie "Really, you are not just saying that to make me happy are you?"
    pc "No, Amber even admitted she likes the idea of gaining more."
    pc "She was worried I was going to think she was weird, but I think it's safe to say she is not in the minority at Bunny Bites."
    image marie_stage_4_event_4 = "/marie/events/stage4/4.webp"
    scene marie_stage_4_event_4
    marie "Wait, she likes her weight gain?"
    pc "Yeah, although I didn't mention you specifically I did admit to her I like it too."
    image marie_stage_4_event_5 = "/marie/events/stage4/5.webp"
    scene marie_stage_4_event_5
    marie "That's amazing, but what made her change?"
    pc "Seeing the customers be so happy even as they gain weight."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage4/vid1.webm" loop
    show movie with dissolve
    marie "That explains all the snacking and eating the leftovers from customers plates."
    marie "What are the chances of that, of her working at the same place as both of us?"
    pc "I don't know, but maybe it's more common than we think."
    pc "Or maybe this town just attracts people who like it for some strange reason."
    marie "Either way, that's great news!"
    stop movie
    image marie_stage_4_event_6 = "/marie/events/stage4/6.webp"
    scene marie_stage_4_event_6
    marie "But what about Lisa?"
    pc "She is happy too, she would basically do anything for you."
    marie "Anything, that still sounds like it's for me and not her."
    pc "No, I think she genuinely likes the attention you give her now she has been getting bigger."
    pc "It's kind of like she wants to be the perfect partner and enjoys being it for you."
    image marie_stage_4_event_7 = "/marie/events/stage4/7.webp"
    scene marie_stage_4_event_7
    marie "That is kind of overwhelming, if I'm honest I haven't had many serious long term relationships in the past."
    marie "I don't really know what to do, what if I mess it up and she is all fat because of me."
    pc "You won't mess it up, and if Lisa is willing to give it a go why shouldn’t you."
    image marie_stage_4_event_8 = "/marie/events/stage4/8.webp"
    scene marie_stage_4_event_8
    marie "You are right, she deserves it."
    pc "You both deserve it."
    image marie_stage_4_event_9 = "/marie/events/stage4/9.webp"
    scene marie_stage_4_event_9
    marie "But what do I do?"
    pc "Why not ask her out on a proper date?"
    marie "Ok, I can do that."
    image marie_stage_4_event_10 = "/marie/events/stage4/10.webp"
    scene marie_stage_4_event_10
    marie "Thank you so much, I know it wasn’t really your job to go out and do everything you have."
    marie "I really appreciate it and like last time I think it's only fair you get a reward, or maybe two."
    marie "I had been thinking about increasing the wage I give to Lisa and Amber, partly so they could afford all the extra food they might want to eat now."
    marie "I don't see any reason why you should miss out, especially after what you have done for me."
    image marie_stage_4_event_11 = "/marie/events/stage4/11.webp"
    scene marie_stage_4_event_11
    marie "As for your second reward, why don't you follow me to the bed."

    ###Bedroom###
    image marie_stage_4_event_12 = "/marie/events/stage4/12.webp"
    scene marie_stage_4_event_12
    marie "Maybe you can think of something to do with these?"
    "Handing you a Bunny Bites bag, you pull out three large cheese burgers."
    pc "But I thought you were not into gaining weight?"
    image marie_stage_4_event_13 = "/marie/events/stage4/13.webp"
    scene marie_stage_4_event_13
    marie "I'm not, and don't expect what I have gained to stay around much longer."
    marie "But I figure we may as well enjoy it while it's here, right."
    image marie_stage_4_event_14 = "/marie/events/stage4/14.webp"
    scene marie_stage_4_event_14
    "Longing back Marie opens her mouth as you move the first burger into position."
    marie "Mmm, extra greasy."
    image marie_stage_4_event_15 = "/marie/events/stage4/15.webp"
    scene marie_stage_4_event_15
    "Giving her little rest between bites you make her demolish all three burgers quickly."
    image marie_stage_4_event_16 = "/marie/events/stage4/16.webp"
    scene marie_stage_4_event_16
    "Her stomach pressing outwards against her tight pants."
    image marie_stage_4_event_17 = "/marie/events/stage4/17.webp"
    scene marie_stage_4_event_17
    marie "Mmm, That hit the spot. I didn't have a chance for lunch."
    marie "Plus, liquid bloating on an empty stomach always gives me a stomach ache."
    marie "Speaking of, why don't you get comfy."
    image marie_stage_4_event_18 = "/marie/events/stage4/18.webp"
    scene marie_stage_4_event_18
    "Walking over to her counter Marie prepares her usual set of sodas."
    image marie_stage_4_event_19 = "/marie/events/stage4/19.webp"
    scene marie_stage_4_event_19
    "Picking up the first one she slurps it noisily, draining it quickly."
    image marie_stage_4_event_20 = "/marie/events/stage4/20.webp"
    scene marie_stage_4_event_20
    "Throwing it into the bin she grabs another, then another and another."
    image marie_stage_4_event_21 = "/marie/events/stage4/21.webp"
    scene marie_stage_4_event_21
    "You can see her stomach expanding rapidly, the extra weight of the liquid adding to her large belly."
    image marie_stage_4_event_22 = "/marie/events/stage4/22.webp"
    scene marie_stage_4_event_22
    "Downing another soda Maries stomach is clearly straining against her pants, the tight waistband cutting into her belly and forcing it over the top."
    image marie_stage_4_event_23 = "/marie/events/stage4/23.webp"
    scene marie_stage_4_event_23
    "Finally all the sodas are empty and Marie's stomach looks more than full and uncomfortably restrained by her clothes."
    image marie_stage_4_event_24 = "/marie/events/stage4/24.webp"
    scene marie_stage_4_event_24
    marie "Oooh, these pants are so tight."
    marie "It kind of feels good in a weird way. It tells me just how big I am now."
    image marie_stage_4_event_25 = "/marie/events/stage4/25.webp"
    scene marie_stage_4_event_25
    "Undoing the top button Marie sighs in relief as her bloated belly spills out of them."
    image marie_stage_4_event_26 = "/marie/events/stage4/26.webp"
    scene marie_stage_4_event_26
    marie "Now then, let's move onto the next part of your reward."
    stop music fadeout 1.0
    ###Usual Marie sex scene ###

    marie "Let's go to my bed..."
    image marie_stage_4_event_27 = "/marie/events/stage4/27.webp"
    scene marie_stage_4_event_27
    "In her room, Marie immediately begins to take off her pants."
    marie "I'm full and horny, good thing I've got a handsome stud to keep me company."
    image marie_stage_4_event_28 = "/marie/events/stage4/28.webp"
    scene marie_stage_4_event_28
    "She crawls onto her bed."
    marie "Come over here."
    if persistent.nosexscene == True:
        scene black with dissolve
        "Marie and I had a great time together."
        if recollection == False:
            $ marie.weight += 1
        $ mariestage4event = 0
        return

    image marie_stage_4_event_29 = "/marie/events/stage4/29.webp"
    scene marie_stage_4_event_29
    pc "I should warn you, I'm starting to have inappropriate thoughts about one of my coworkers."
    marie "Oh yeah?"
    marie "Which one?"
    image marie_stage_4_event_30 = "/marie/events/stage4/30.webp"
    scene marie_stage_4_event_30
    pc "The hot one everyone is always flirting with."
    marie "Oh, I thought you might have meant me."
    pc "That's what I said."
    pc "I hope I'm not creating an uncomfortable workplace."
    image marie_stage_4_event_31 = "/marie/events/stage4/31.webp"
    scene marie_stage_4_event_31
    marie "Ohhh!"
    marie "No complaints here."
    pc "That's a relief."
    marie "You really like me in this state?"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage4/sex1.webm" loop
    show movie with dissolve
    window hide
    pause
    marie "Oh! I'll take that as a yes!"
    pc "Sometimes actions are better than words."
    marie "Most times, I'd say."
    pc "Is this you telling me to stop running my mouth?"
    marie "No!"
    marie "Unless it works in my favor."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage4/sex2.webm" loop
    show movie with dissolve
    window hide
    pause
    marie "Like that!"
    marie "Damn, [pc]!"
    pc "Not too much movement?"
    marie "I'd warn you."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage4/sex3.webm" loop
    show movie with dissolve
    window hide
    pause
    marie "Can you hear my stomach sloshing around?"
    pc "Yep."
    pc "And I heard you aren't supposed to shake soda."
    marie "Would it be unattractive if I let out a huge burp?"
    pc "I dare you."
    marie "No!"
    marie "I'm a lady!"
    pc "Aww."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage4/sex4.webm" loop
    show movie with dissolve
    window hide
    pause
    marie "Whoa!"
    marie "Are you serious!"
    pc "Let it out, Marie!"
    marie "Nooo!"
    marie "But keep doing that!"
    marie "Exactly like that!"
    marie "Ahhhh!"
    stop movie
    image marie_stage_4_event_32 = "/marie/events/stage4/32.webp"
    scene marie_stage_4_event_32
    marie "Can we do this every night?"
    pc "Yes, please."

    if recollection == False:
        $ marie.weight += 1
    $ mariestage4event = 0
    return

label Marie_Stage_4_Event_2:
    ## Marie 4.2 Inspector (Potentially recurring character every couple of stages?) ##
    ### At work with Marie for regular shift ####
    ### New character arrives - recurring franchise inspector who is already a little large for stage 1 ###
    image marie_stage_4_event_33 = "/marie/events/stage4/33.webp"
    scene marie_stage_4_event_33
    play music "/music/bunny_bites.ogg" if_changed
    "A customer arrives."
    image marie_stage_4_event_34 = "/marie/events/stage4/34.webp"
    scene marie_stage_4_event_34
    "You don't think you have seen them in here before as they approach the counter."
    image marie_stage_4_event_35 = "/marie/events/stage4/35.webp"
    scene marie_stage_4_event_35
    chloe "Hello, my name is Chloe."
    chloe "I was wondering if I could ask you a few questions?"
    pc "Uhh… sure I guess."
    chloe "Great."
    image marie_stage_4_event_36 = "/marie/events/stage4/36.webp"
    scene marie_stage_4_event_36
    "Watching her pull out a notepad, this is starting to feel more like an interview than a few simple questions."
    chloe "How busy would you say you are usually?"
    pc "Fairly busy… I’m sorry, who are you?"
    image marie_stage_4_event_37 = "/marie/events/stage4/37.webp"
    scene marie_stage_4_event_37
    marie "This is Chloe, she is a franchise compliance officer and knows she should be asking to see me and not talking to you."
    "Coming to your rescue, Marie joins you at the till and clearly doesn't look too happy."
    image marie_stage_4_event_38 = "/marie/events/stage4/38.webp"
    scene marie_stage_4_event_38
    chloe "Marie, it's good to see you again."
    chloe "I would have asked to see you, but for some reason every time I come here I don't seem to get any clear answers."
    image marie_stage_4_event_39 = "/marie/events/stage4/39.webp"
    scene marie_stage_4_event_39
    marie "I can only apologise for that, why don't I offer you a moment of my undivided attention."
    marie "If you want to grab a table, I’ll be right over."
    chloe "That would be excellent, thank you."
    image marie_stage_4_event_40 = "/marie/events/stage4/40.webp"
    scene marie_stage_4_event_40
    "Waiting for Chloe to leave, Marie leans into you."
    marie "I want you to ring through an order for her, a big one."
    pc "What is going on?"
    marie "She is here to check how things are going and make sure everything is up to their standards."
    marie "While I might be the manager and have a lot of freedom here, this place is technically owned by someone else."
    pc "I thought we were doing great, everyone in town loves this place."
    image marie_stage_4_event_41 = "/marie/events/stage4/41.webp"
    scene marie_stage_4_event_41
    marie "Thanks, that is nice of you to say."
    marie "But that can be a problem as well. Sometimes they like to move managers around."
    marie "Take successful managers and put them into failing restaurants to help turn them around."
    marie "So whether it's good or bad, having a review score out of the ordinary can cause things to happen that I don't think any of us want."
    pc "So what’s with the meal?"
    image marie_stage_4_event_42 = "/marie/events/stage4/42.webp"
    scene marie_stage_4_event_42
    marie "Oh, Chloe is a distracted eater."
    marie "She was much slimmer the first time she came in."
    marie "Put a table of food in front of her during the interview and she will just eat until she can't think straight."
    image marie_stage_4_event_43 = "/marie/events/stage4/43.webp"
    scene marie_stage_4_event_43
    marie "Honestly, if she wasn't playing for enemy team it would be kind of hot."
    marie "Anyway, put the order through and bring it over when it’s done. I’ll do the rest."
    pc "Will do."
    image marie_stage_4_event_44 = "/marie/events/stage4/44.webp"
    scene marie_stage_4_event_44
    "Giving you a wink, Marie joins Chloe at her table."
    "After putting through the order it doesn't take long for the mountain of food to be cooked."
    image marie_stage_4_event_45 = "/marie/events/stage4/45.webp"
    scene marie_stage_4_event_45
    "Approaching the table you gently lay the food down, trying not to distract Chloe as she asked Marie something about staff turnover."
    image marie_stage_4_event_46 = "/marie/events/stage4/46.webp"
    scene marie_stage_4_event_46
    "With the table filled you retreat back to the counter, your eyes glued to the town women as Chloe began to absentmindedly pick at her food."
    image marie_stage_4_event_47 = "/marie/events/stage4/47.webp"
    scene marie_stage_4_event_47
    "Questions after question, plate after plate the two continued."
    image marie_stage_4_event_48 = "/marie/events/stage4/48.webp"
    scene marie_stage_4_event_48
    "Chloe’s hands constantly moving, burgers, fries and drinks grabbed between notes."
    image marie_stage_4_event_49 = "/marie/events/stage4/49.webp"
    scene marie_stage_4_event_49
    "It’s not long before the note taking becomes more sporadic, while picking up single fries turned to entire handfuls forced into her mouth."
    image marie_stage_4_event_50 = "/marie/events/stage4/50.webp"
    scene marie_stage_4_event_50
    "Her smart clothes straining against her overindulgence, to your and Marie's enjoyment."
    image marie_stage_4_event_51 = "/marie/events/stage4/51.webp"
    scene marie_stage_4_event_51
    "15 minutes of watching her eat leaves the table empty and Chloe’s belly stuffed to its limit."
    image marie_stage_4_event_52 = "/marie/events/stage4/52.webp"
    scene marie_stage_4_event_52
    pause
    image marie_stage_4_event_53 = "/marie/events/stage4/53.webp"
    scene marie_stage_4_event_53
    "Sitting back in the booth with her mouth closed, it's clear Marie’s plan has worked and the interview is over."
    image marie_stage_4_event_54 = "/marie/events/stage4/54.webp"
    scene marie_stage_4_event_54
    "Shaking her greasy hand, Marie leaves the groaning woman to her food coma."
    ###Marie approaching you.###
    image marie_stage_4_event_55 = "/marie/events/stage4/55.webp"
    scene marie_stage_4_event_55
    marie "Ok, maybe I lied."
    image marie_stage_4_event_56 = "/marie/events/stage4/56.webp"
    scene marie_stage_4_event_56
    marie "That was hot, even if she works for the enemy."
    pc "So, is everything ok?"
    image marie_stage_4_event_57 = "/marie/events/stage4/57.webp"
    scene marie_stage_4_event_57
    marie "If I know Chloe, she won’t have gotten enough information to be able to write anything conclusive."
    marie "Meaning we won't have to worry about any kind of report, good or bad."
    marie "Works every time."
    image marie_stage_4_event_58 = "/marie/events/stage4/58.webp"
    scene marie_stage_4_event_58
    "You both enjoy watching the poor woman struggle to her feet."
    image marie_stage_4_event_59 = "/marie/events/stage4/59.webp"
    scene marie_stage_4_event_59
    "Grabbing her notepad, the stuffed woman almost waddles out of the restaurant, now several times larger than when she arrived."
    image marie_stage_4_event_60 = "/marie/events/stage4/60.webp"
    scene marie_stage_4_event_60
    "Trying to get back to work, you take a few orders from customers."
    image marie_stage_4_event_61 = "/marie/events/stage4/61.webp"
    scene marie_stage_4_event_61
    "But it’s hard not to be distracted by what the two of you did to her, you make more than a couple of errors and this time they are not on purpose."
    image marie_stage_4_event_62 = "/marie/events/stage4/62.webp"
    scene marie_stage_4_event_62
    "The sight of the woman stuffing herself absentmindedly, her clothes stretching to their limits replaying in your mind."
    image marie_stage_4_event_63 = "/marie/events/stage4/63.webp"
    scene marie_stage_4_event_63
    "Hearing a crash, a couple of boxes go clattering to the floor as it seems you are not the only one distracted."
    image marie_stage_4_event_64 = "/marie/events/stage4/64.webp"
    scene marie_stage_4_event_64
    marie "Crap."
    image marie_stage_4_event_65 = "/marie/events/stage4/65.webp"
    scene marie_stage_4_event_65
    pause
    image marie_stage_4_event_66 = "/marie/events/stage4/66.webp"
    scene marie_stage_4_event_66
    "Walking over to you, Marie almost pulls you towards the supply cupboard."
    marie "I need your help with something."
    image marie_stage_4_event_67 = "/marie/events/stage4/67.webp"
    scene marie_stage_4_event_67
    "With no real option you let the surprisingly strong women pull you into the room, watching as she locks the door behind her."
    image marie_stage_4_event_68 = "/marie/events/stage4/68.webp"
    scene marie_stage_4_event_68
    marie "Fuck, I can't stop thinking about what we did to Chloe."
    image marie_stage_4_event_69 = "/marie/events/stage4/69.webp"
    scene marie_stage_4_event_69
    marie "It was just so, fucking, hot!"
    image marie_stage_4_event_70 = "/marie/events/stage4/70.webp"
    scene marie_stage_4_event_70
    pause
    image marie_stage_4_event_71 = "/marie/events/stage4/71.webp"
    scene marie_stage_4_event_71
    marie "So you are going to help me to be able to concentrate and make me cum."
    image marie_stage_4_event_72 = "/marie/events/stage4/72.webp"
    scene marie_stage_4_event_72
    "Moving over, Marie pushing you against the wall and plants her lips on yours."
    image marie_stage_4_event_73 = "/marie/events/stage4/73.webp"
    scene marie_stage_4_event_73
    "You let you hands explore her body, her growing frame giving you more than a handful to enjoy."
    image marie_stage_4_event_74 = "/marie/events/stage4/74.webp"
    scene marie_stage_4_event_74
    marie "I can't believe what we did to her, she ate so much."
    image marie_stage_4_event_75 = "/marie/events/stage4/75.webp"
    scene marie_stage_4_event_75
    marie "She was so fucking fat by the time she left."
    "Hearing her moan into you, she is filled with an insatiable lust."
    image marie_stage_4_event_76 = "/marie/events/stage4/76.webp"
    scene marie_stage_4_event_76
    "She turns around and pushes her butt into your crotch."
    "Grabbing her breasts you get another moan out of the brunette as her body heats up even more."
    image marie_stage_4_event_77 = "/marie/events/stage4/77.webp"
    scene marie_stage_4_event_77
    marie "Make me cum."
    image marie_stage_4_event_78 = "/marie/events/stage4/78.webp"
    scene marie_stage_4_event_78
    "Needing no more instructions you put a hand between her legs."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage4/Marie1.webm" loop
    show movie with dissolve
    "Sliding your hand between her folds, you can feel how wet she is."
    marie "Fuck yeah."
    marie "She ate so much, but I think we could have gotten her to eat more, and more and more."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage4/Marie2.webm" loop
    show movie with dissolve
    "Bucking on your hand, her sexual fantasies drive her wild."
    marie "I want to make her burst out of her shirt, make her belly so big she cant leave the booth ever again."
    marie "So I can keep feeding her, she would be trapped there, forever a feedee only able to do as I say and eat whatever I made her."
    marie "Shit, I’m going to cum soon, keep going."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage4/Marie4.webm" loop
    show movie with dissolve
    "Moving your hand quicker, Marie’s back arches in pleasure."
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage4/Marie3.webm" loop
    show movie with dissolve
    window hide
    pause
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage4/Marie5.webm" loop
    show movie with dissolve
    window hide
    pause
    marie "I'm gonna, I'm gonna…"
    "Feeling Marie start to cum, you once again increase your speed."
    stop movie
    image marie_stage_4_event_79 = "/marie/events/stage4/79.webp"
    scene marie_stage_4_event_79
    "The increased pace seemingly sending her over the edge as she screams out in pleasure."
    image marie_stage_4_event_80 = "/marie/events/stage4/80.webp"
    scene marie_stage_4_event_80
    "Legs quivering, Marie sinks to her knees on the floor."
    image marie_stage_4_event_81 = "/marie/events/stage4/81.webp"
    scene marie_stage_4_event_81
    marie "Holy shit, that felt amazing."
    marie "But I dont think I’m the only one who enjoyed that stuffing."
    marie "And I wouldn’t want any of my employees to be distracted either."
    image marie_stage_4_event_82 = "/marie/events/stage4/82.webp"
    scene marie_stage_4_event_82
    "Reaching up, she lowers your pants and takes hold of your erection."
    image marie_stage_4_event_83 = "/marie/events/stage4/83.webp"
    scene marie_stage_4_event_83
    "Putting it into her mouth, she wraps her lips around your penis."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage4/Marie6.webm" loop
    show movie with dissolve
    "Moving her head back and forth, her tongue glides across your cock."
    "After everything that happened, it doesn’t take long before you have your own orgasm."
    window hide
    pause
    "Marie swallows your load as you shoot it deep into her throat."
    stop movie
    image marie_stage_4_event_84 = "/marie/events/stage4/84.webp"
    scene marie_stage_4_event_84
    "As Marie lets go of your penis, your remaining spurts of cum cover her face."
    pc "Wow."
    image marie_stage_4_event_85 = "/marie/events/stage4/85.webp"
    scene marie_stage_4_event_85
    "Standing, Marie gives you a smile."
    "Grabbing a towel, Marie cleans her face before leaving you to recover in the supply room."
    call bbworking
    "Collecting your thoughts you go back to work, the rest of the shift is much less eventful."
    ###End of shift###
    $ mariestage4event2 = 0
    stop music fadeout 1.0
    return

#label Marie_Stage_5_Event:
    ###Event with all 3 stage 6 Lisa and Amber but stage 5 Marie. Day evening ###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Marie', dialogue=dialogue_one)
    $ msg ("Hey, guess who has a surprise health inspection coming up.", who=1)
    pause
    $ msg ("Any chance you can come in and help us with a deep clean?", who=1)
    pause
    $ msg ("I’ll make it worth your while afterwards.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sure, I'll be there in a few minutes.")
            pause
            $ msg ("Amazing, thank you so much.", who=1)
            pause
            $ hide_messenger()

        "I'm busy, sorry.":
            $ msg ("Sorry, I’m really busy today.")
            pause
            $ msg ("Alright. Another time then.", who=1)
            pause
            $ hide_messenger()
            return

    ###Bunny bites###
    "Arriving at bunny bites, the restaurant is closed for the evening."
    marie "Sorry to call you in like this."
    pc "No problem, what can I do to help?"
    marie "We are just doing a bit of a deep clean to make sure we pass the checks they do to make sure everything is ok to serve food."
    marie "I'm sure we would pass with flying colours even if we didn’t clean tonight."
    marie "But when it comes to these things it is better safe than sorry."
    marie "I think Lisa could do with some help in the stock room."
    pc "Oh great, I will head in."
    marie "Before you go, I had the kitchen make some extra burgers as a thank you."
    pc "A thank you…I’m guessing for Lisa?"
    marie "Feel free to share, but maybe I’ll have something more for you after we finish."
    marie "But I don't see why we can’t enjoy tonight before then as well."
    "Picking up the plates of burgers, you go to find Lisa in the supply cupboard."
    ### Supply cupboard ###
    "Walking in you see Lisa arranging a stack of boxes, a couple of empty packets sitting on top of them."
    pc "Hey Lisa, Marie sent me to help."
    lisa "Oh hey, I didn’t know you were here."
    pc "Marie called all hands on deck."
    pc "But I come with gifts, also from Marie."
    lisa "Mmm, I thought I could smell something."
    "Holding out her hands, you go to give her one plate but Lisa takes both instead."
    "You go to say something, but decide you are not hungry after all."
    "Sitting on one of the shelves, Lisa begins munching into her sets of burgers."
    pc "How can I help?"
    lisa "Just double check everything is in date and chuck out anything that is almost out of date."
    pc "Seems a bit of a waste to throw out good food."
    lisa "Yeah, Marie also said we could eat it instead if we wanted."
    "Cleaning up a few packets and rearranging a box or two, you start sorting through what is left while Lisa eats."
    "Cleaning up the empty packets you think Lisa had already eaten, you can see they had almost a month left."
    "Seems like Lisa was taking some liberties with what counted as almost out of date."
    "Continuing to work through the store room, you keep an eye on Lisa happily eating her large meal."
    lisa "Mmm, that hit the spot."
    lisa "Back to it I guess."
    "Leaning down to check a box Lisa moves next to you, going to grab a box from a higher self."
    "Her now bloated stomach brushing close to your face as she reached up, you swear you could see the seams of her outfit starting to fray."
    ###Does Not need to be obvious / shown - just setting up for redesign###
    lisa "So did you have any plans for tonight before this?"
    pc "No, I was just at home contemplating watching a live stream or something."
    pc "What about you?"
    lisa "Cool, I used to watch a lot of streams."
    lisa "No, I was thinking of going to visit my sister again."
    lisa "You could join again if you wanted."
    lisa "I promise not to leave you alone with her again."
    pc "Thanks, she wasn’t that bad."
    lisa "Try living with her and sharing a bedroom."
    "Working together, you quickly sort through the room and make sure everything is spotless."
    lisa "Phew, looks good to me."
    pc "Yeah, I think we might be done."
    lisa "Great, well I need to take these plates back to the kitchen so I think I’ll help cleaning in there."
    lisa "Amber could probably do with some help in the front of house."
    pc "Sure thing, I’ll go check in on her."
    lisa "Great, thanks for the burgers."
    ###main room###
    "Leaving the store room, you can see Marie speaking with Amber."
    "A large plate of burgers sitting on the table next to her, a sure sign of Marie’s continuing generosity."
    marie "How is the store room looking?"
    pc "Yeah, shouldn’t have any issues with that."
    pc "Lisa has just gone to start on the kitchen."
    marie "Great, can you two manage out here if I go and help Lisa?"
    amber "Yeah, we got you."
    marie "Perfect, oh and I’ll bring you out some more burgers as well."
    pc "Thanks."
    ###Marie leaves###
    pc "What’s still left to do out here?"
    amber "Most of the tables and booths."
    amber "I concentrated behind the till and have been doing the windows."
    amber "Just needs a quick sweep, mop and wipe down."
    pc "Sure I will get right on that."
    amber "Great, I’ll be right with you after I finish all of these."
    "Watching Amber eat you start sweeping the floors."
    "Catching her eyes for a moment she takes a large bite for you."
    "Finishing up sweeping, Amber seems to have finished her meal too."
    amber "Mmm, those were so good."
    amber "Nothing like some hard work to give me an appetite."
    ###Marie appears with two more plates of burgers###
    marie "Hey [playername], here are those burgers I promised."
    marie "There were a few left over, if you want some Amber?"
    amber "Sure, thanks."
    marie "Good work in here you two, looks spotless already."
    ###Marie disappears##
    pc "Well, sounds like it’s a good thing you worked up that appetite."
    amber "But if I eat too much more, I won't be able to help you clean."
    pc "In that case, why don't you sit here and eat these while I clean."
    "Placing your plate of burgers down next to the already full looking Amber, you can see a playful look on her face."
    amber "That could work too, I suppose."
    "Picking up the first burger Amber chows down again."
    "Mopping the floors and wiping down the tables, you share glances with Amber."
    "Each time you see her, she looks more full than the time before, even making sure to catch your gaze from time to time as she finishes a burger."
    "It’s a little hard to concentrate, but you manage to do a good job."
    ###Lisa and Marie emerge from the kitchen, Lisa finishing off another burger and maybe looking slightly larger than before.###
    marie "The kitchen is the cleanest it’s ever been."
    amber "We have just finished up out here as well."
    marie "Perfect, thank you guys for all your hard work today."
    marie "I know it was a pain to have to come in late this evening, but I really appreciate it."
    marie "Hopefully you can all still enjoy whatever is left of your plans for tonight."
    lisa "No problem Marie, we are a team."
    amber "Yeah, you should know we all have your back by now."
    marie "You guys are too much, now let's get out of here."
    lisa "I’ll just go and get changed and then we can head out [playername]."
    amber "Wait, I thought we had plans tonight?"
    marie "Or were you going to come over mine?"
    pc "Uhh…."
    "Seems like all three of them had plans for you, even if you hadn’t said yes to any of them."
    "Who should you go out with tonight?"

    #[Game options of the three buttons with their names on them.]
    menu:
        "Amber":
            ### If chose Amber###
            pc "Sorry guys, I have plans with Amber tonight."
            lisa "No problem, have a good night."
            marie "Your loss I guess, maybe we can do it another time."
            amber "I’ll just go get changed and we can head out."
            ###Lisa and Marie leave###
            "Returning a few minutes later in her casual clothes, Amber seems ready to go."
            amber "I swear these fit me better a couple of hours ago."
            amber "But let’s make a move and get out of here."
            pc "Lead the way."
            "Locking up the restaurant for the night you head to the club with Amber."
            ###Night club###
            "Going up to the bar, you both order drinks and take a seat."
            amber "I’m glad it didn’t take all night to clean."
            pc "Yeah, I think we made pretty short work out of it as a team."
            "Sipping at your drinks you see Amber shift slightly in her seat."
            pc "Everything ok?"
            amber "What?"
            pc "You seem a little uncomfortable."
            amber "Oh…It’s nothing, these shorts might be on their last legs though."
            amber "Digging in badly, but honestly It’s weirdly fun."
            pc "Fun?"
            amber "It’s like a constant reminder of how much I have grown, I'm literally pulling my clothes apart with my body."
            amber "Which sounds kind of hot, don't you think."
            pc "You know I do."
            amber "So, why don't we see how much life they have left?"
            "Holding up her hand, Amber orders a couple more beers."
            "Drinking the first quickly, she rubs her bloated stomach already filled with Marie’s generosity."
            amber "Still in one piece."
            "Grabbing another glass Amber steadily chugs it, her stomach expanding before your eyes."
            amber "Oooh, getting really tight now."
            amber "One more might do it."
            "Ordering another two just to be safe, you can see Amber looking at them with some anticipation."
            "Picking up the first Amber greedily drinks another, her other hand resting on her now sizable stomach."
            "Emptying the glass she quickly grabs the other, going for broke she chugs that as well."
            "Seeing her stomach swell as she drinks it quickly, you can hear a faint tearing noise."
            ###Think of just a closed and open shorts variation rather than actually breaking or tearing, if that is possible###
            "Moments later, her giant bloated belly bursts through her shorts."
            "Groaning in delight, it spills forwards to its true stuffed size."
            amber "That felt amazing, I’ve become such a glutton."
            amber "But now I am in the mood for something else, if you want to head back to mine for a little fun."
            amber "Looking this fat I can't believe how humiliating it feels breaking through my shorts."
            "Standing up, her shorts barely stay on but thankfully her chubby thighs and hips are still holding them up."
            "Even as her belly is on full display for anyone looking at her, something Amber seems to be enjoying."
            "Making your way home she occasionally shields it from passer’s by, but its too big for any of her attempts to actually work."
            ###Amber place ###
            "Arriving at her home she lets the destroyed shorts fall to the floor."
            #[Usual sex scene without the takeaway conversation before it]
            $ mariestage5event = 0
            return
        "Lisa":
            ### If chose Lisa###
            pc "Hey, sorry guys I have plans with Lisa tonight."
            amber "No problem, have a good night guys."
            marie "Your loss I guess, maybe we can do it another time."
            lisa "I’ll just go get changed and we can head out."
            ###Amber and Marie leave###
            "Returning a few minutes later in her casual clothes, you head out to her sisters pub."
            ###Lisa’s sisters pub - looking busy###
            lisa "Looks busy tonight, at least that's a blessing."
            pc "How so?"
            lisa "It means Mrs Nosy won't be able to bother us."
            lisa "Or maybe I spoke too soon."
            mandy "Hello you two, another date?"
            mandy "You must really like her."
            lisa "Can you not, just give us a menu and leave us alone."
            mandy "Rude…"
            "Handing over a menu she goes to serve another customer while you take a seat."
            lisa "Think I have had my fill of burgers, fancy a desert?"
            pc "You mean I get to eat my own one this time?"
            lisa "Maybe…haven't decided yet."
            "Deciding to order one on the off chance Lisa eats it too, you sip on your drinks."
            pc "So how have things been going with Marie?"
            lisa "Good, really good actually."
            lisa "We have always been good friends but now it’s even better."
            lisa "Last week I went around her place and we watched a film, I don't think we said anything for almost an hour but it still felt really nice to just be there with her."
            pc "That’s nice, I am happy to hear it."
            lisa "The only problem with it is that I think she wants to take it to the next level."
            pc "I thought you two had already…done it."
            lisa "Sex, no not that."
            lisa "She invited me out again and I think she wants to make it more, official."
            pc "Is that a bad thing?"
            lisa "No, it’s just only you and Amber know we are dating."
            lisa "I’m worried about what others might think."
            pc "Will it change how you feel about her?"
            lisa "No, of course not."
            pc "Then I say forget what other people might think and focus on your own happiness."
            lisa "Yeah, I know you are right."
            lisa "It’s just been a while and I know people will make a big deal of it."
            ##Mandy appears with deserts###
            mandy "Here are your deserts."
            mandy "Although you might want to try something healthier next time."
            lisa "Thanks…I think I’ll stick to these though."
            mandy "You're impossible sometimes."
            ###Mandy leaves###
            lisa "These look amazing."
            "Picking up her spoon, Lisa digs into her desert."
            lisa "So good!"
            "Spoonful after spoonful of delicious gooey chocolate disappears into her mouth."
            "Taking a few bites out of your own, you don't know how someone could stomach this much rich sweetness."
            "Opposite you, Lisa continues to chow down until the large desert is gone."
            lisa "Mmm…"
            pc "You want mine, I think it’s too big for me."
            lisa "I won't say no to more, thanks."
            "Sliding it across the table, Lisa digs into your desert as well."
            "Soon both are gone and it seems Lisa is finally full."
            lisa "That hit the spot."
            lisa "It is so fun being able to eat whatever I want these days."
            lisa "Even if it wasn’t for Marie, I don't think I would stop."
            lisa "Although, I better head home."
            lisa "Thanks for tonight."
            pc "No problem, I had fun."
            "Watching Lisa struggle to her feet you leave the bar and head home."
            $ mariestage5event = 0
            return
        "Marie":
            ### If chose Marie###
            pc "Hey, sorry guys I have plans with Marie tonight."
            lisa "No problem, have a good night."
            amber "Have fun, see you guys later."
            marie "I’ll just go get changed and we can head out."
            ###Others leave and Marie comes back###
            marie "Let’s lock up and then I can show you what I have planned for us this evening."
            "Given the look in her eyes, you are not sure if you should be excited or scared."
            "Closing the restaurant for the night, you head over to Marie’s place."
            ###Marie’s place.###
            "Walking in, you can already spot Marie's planned binge waiting for her on the table."
            pc "Someone was prepared."
            marie "Lets just say I woke up in the mood for some fun."
            pc "I didn't think you knew about the inspection."
            marie "I didn’t, this was going to be a solo thing."
            marie "But I figured I’d make the most of it since I got the chance."
            "Sitting back on the sofa, Marie makes herself comfortable before grabbing the first soda."
            "Picking up the first, you watch as she drains it in less than a minute."
            marie "Uhhh, I shouldn’t have joined in with Lisa eating in the kitchen."
            marie "Already feeling a little full down there, but not stopping now."
            "Grabbing another she puts the straw to her mouth and drinks it as quickly as possible."
            pc "In a rush."
            marie "I figure it will be more effective if I drink these quickly."
            pc "It?"
            marie "Oh you'll see, now why don't you help by passing me another."
            "Handing her another cup she continues drinking steadily, her stomach bloating out from the rush of bubbling liquid."
            "Swapping another empty for a full one you watch her belly continue to grow."
            "Drinking rapidly you keep the cup’s coming until eventually they are all empty and Marie seems fit to burst."
            marie "Oooh, I’m starting to think this might be a bad idea."
            marie "I’m so full already."
            "Ignoring her own complaints, Marie picks up a small tube of mints."
            "Squeezing the tube open, she dumps the contents into her mouth and after a few chews swallows them down."
            "Moments later, you see her stomach surging forwards once more as they react with the soda she had chugged so rapidly."
            ###I’m thinking this could even be an animation if you wanted to include one?”##
            marie "This feels incredible."
            marie "I’ve never been this big before, Oooh, I can barely stand it."
            marie "Uuuh, my skin is so tight, I feel like a drum."
            marie "Mmmm, I feel like I'm still growing even though I’m maxed out."
            marie "Everything is so tingly, so full."
            marie "Help me get these pants off."
            "Moving around the beached whale Marie had become, you manage to extract her pants from under the giant balloon her belly had become."
            marie "That’s better, but now I need you to do something else."
            "Grabbing your head, she guides you between her legs."
            ###Thinking similar to Katrine event###
            "Geting the idea you begin to give her Oral, her giant stomach almost stopping you from getting close enough."
            "With her bulbous belly pressing against your forehead you continue to eat her out."
            "You could swear you could almost hear it fizzing above you."
            marie "Fuck yes, keep going."
            "Picking up the pace, Marie writhes in pain and pleasure."
            "Reaching up to play with her belly causes Marie to moan deeply."
            "You can't even see her face from behind the mountain of soda and mints above you."
            "After a few more moments, Marie lets out a loud cry of pleasure and you feel her hips buck against you as she cums."
            ###Sweaty bloated Marie on the sofa.###
            marie "Fuck…that was amazing."
            marie "I’ve never felt like that before."
            marie "Almost like I was going to explode while I was cumming."
            marie "Oooh, god. I think I might still."
            marie "That is definitely my limit…for now."
            "Letting Marie recover on the couch and try not to pop, you clean up the mess you had both made."
            marie "Sorry for repaying the favour but I really don't think I should be moving around too much at the moment."
            pc "Trust me, just watching that was enough."
            marie "I’m glad you think so, maybe we can do this again another time."
            pc "Sure, I look forward to it."
            "Grabbing your things, you head home for the evening."
            $ mariestage5event = 0
            return

label Marie_Stage_6_Event_1:
    ###Marie stage 6.1###
    image marie_stage_6_event_1 = "/marie/events/stage6/1.webp"
    scene marie_stage_6_event_1
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    "Walking into the gym, you spot a familiar face on the treadmill."
    image marie_stage_6_event_2 = "/marie/events/stage6/2.webp"
    scene marie_stage_6_event_2
    pc "Hey Marie, how are you doing?"
    marie "Hey, I was just thinking about you."
    pc "Only good things I hope."
    image marie_stage_6_event_3 = "/marie/events/stage6/3.webp"
    scene marie_stage_6_event_3
    marie "No, this is all your fault."
    pc "What?"
    marie "How hard I have to work out, these fat cheeks are your fault too."
    pc "I don't know what you are talking about."
    marie "Oh really?"
    image marie_stage_6_event_4 = "/marie/events/stage6/4.webp"
    scene marie_stage_6_event_4
    "Stepping off the treadmill, Marie approaches you closely."
    image marie_stage_6_event_5 = "/marie/events/stage6/5.webp"
    scene marie_stage_6_event_5
    marie "So you don't know anything about all the extra food that has been turning up in my orders at work?"
    pc "Must be a problem with the till, seems to be happening more and more these days."
    image marie_stage_6_event_6 = "/marie/events/stage6/6.webp"
    scene marie_stage_6_event_6
    marie "Yeah, I’ve been noticing."
    marie "I guess I didn’t technically tell you not to use it on me, so that's on me I guess."
    marie "But this is still your fault, just look at me."
    ###Marie going through some poses to emphasise her growing body and showing it off for you.###
    image marie_stage_6_event_7 = "/marie/events/stage6/7.webp"
    scene marie_stage_6_event_7
    marie "My big, round, soft belly."
    image marie_stage_6_event_8 = "/marie/events/stage6/8.webp"
    scene marie_stage_6_event_8
    marie "I can feel it straining against my workout clothes."
    image marie_stage_6_event_9 = "/marie/events/stage6/9.webp"
    scene marie_stage_6_event_9
    marie "What about my boobs, I’m going to need a new bra soon."
    image marie_stage_6_event_10 = "/marie/events/stage6/10.webp"
    scene marie_stage_6_event_10
    marie "My ass hasn’t escaped either, my thighs practically rub against each other all day now."
    ###Leaning in like she is going to kiss you/whispering###
    image marie_stage_6_event_11 = "/marie/events/stage6/11.webp"
    scene marie_stage_6_event_11
    marie "And it’s all your fault."
    ### Maire standing back and winking at you ###
    image marie_stage_6_event_12 = "/marie/events/stage6/12.webp"
    scene marie_stage_6_event_12
    marie "Although it has been kind of fun to get a bit bigger."
    pc "So you don't mind?"
    image marie_stage_6_event_13 = "/marie/events/stage6/13.webp"
    scene marie_stage_6_event_13
    marie "Oh I do and I don't plan on gaining more."
    marie "So you better enjoy the view while you can."
    "That wasn’t the first time Marie had said that, but it hadn’t stopped her eating yet."
    image marie_stage_6_event_14 = "/marie/events/stage6/14.webp"
    scene marie_stage_6_event_14
    marie "But it has been nice to get even bigger when I bloat, guess the more I eat the more room I have down there to stretch myself out."
    ###Marie rubbing her belly###
    image marie_stage_6_event_15 = "/marie/events/stage6/15.webp"
    scene marie_stage_6_event_15
    marie "Mmmmm"
    image marie_stage_6_event_16 = "/marie/events/stage6/16.webp"
    scene marie_stage_6_event_16
    marie "C’mon we are going."
    pc "What, but I haven’t even worked out yet."
    ##Marie raising an eyebrow###
    image marie_stage_6_event_17 = "/marie/events/stage6/17.webp"
    scene marie_stage_6_event_17
    marie "So you don't want to watch what I am about to do to myself?"
    pc "I can come back later."
    marie "Good choice."
    image marie_stage_6_event_18 = "/marie/events/stage6/18.webp"
    scene marie_stage_6_event_18
    "Following Marie, she pulls you back to her place."
    stop music fadeout 1.0

    ###Marie’s house still in gym clothes###
    image marie_stage_6_event_19 = "/marie/events/stage6/19.webp"
    scene marie_stage_6_event_19
    marie "Wait there."
    image marie_stage_6_event_20 = "/marie/events/stage6/20.webp"
    scene marie_stage_6_event_20
    "Standing in the corner you can hear Marie rummaging around."
    image marie_stage_6_event_21 = "/marie/events/stage6/21.webp"
    scene marie_stage_6_event_21
    marie "Ok, let's do this!"
    "Emerging with even more sodas than usual, it seems something has gotten into Marie today."
    ###Marie sat upright on the bed if possible.###
    image marie_stage_6_event_22 = "/marie/events/stage6/22.webp"
    scene marie_stage_6_event_22
    "Helping her carry them to her bed, Marie starts taking off her gym outfit."
    image marie_stage_6_event_23 = "/marie/events/stage6/23.webp"
    scene marie_stage_6_event_23
    "Marie sits herself down on the bed and hands you a funnel."
    marie "Mmmm, I can't wait to be so big and full."
    marie "Are you going to stand there all day or are you going to funnel these sodas into me?"
    image marie_stage_6_event_24 = "/marie/events/stage6/24.webp"
    scene marie_stage_6_event_24
    "Grabbing the first of the large sodas, you pour it into the funnel."
    "Taking the funnel end into her mouth Marie begins sucking down the liquid."
    image marie_stage_6_event_25 = "/marie/events/stage6/25.webp"
    scene marie_stage_6_event_25
    "Breathing heavily through her nose, Marie determinedly drains the first one in a single go."
    image marie_stage_6_event_26 = "/marie/events/stage6/26.webp"
    scene marie_stage_6_event_26
    marie "Next!"
    "In no mood for a break, she orders the next extra large soda which you obligingly pour in for her to drink."
    image marie_stage_6_event_27 = "/marie/events/stage6/27.webp"
    scene marie_stage_6_event_27
    "Sucking on the funnel you can already see her stomach bloating out from all the liquid."
    image marie_stage_6_event_28 = "/marie/events/stage6/28.webp"
    scene marie_stage_6_event_28
    "As the second soda is emptied you pour in the third immediately, to the delight of Marie who obediently starts drinking it."
    image marie_stage_6_event_29 = "/marie/events/stage6/29.webp"
    scene marie_stage_6_event_29
    "You can see her stomach swelling rapidly, starting to cover more of her thighs."
    image marie_stage_6_event_30 = "/marie/events/stage6/30.webp"
    scene marie_stage_6_event_30
    "Unable to help herself, you watch Maries hands gravitating to her belly and exploring her growing body while you make her drink."
    image marie_stage_6_event_31 = "/marie/events/stage6/31.webp"
    scene marie_stage_6_event_31
    marie "Mmmm, this feels so good."
    marie "My skin is already so tight, but that's no reason to stop."
    image marie_stage_6_event_32 = "/marie/events/stage6/32.webp"
    scene marie_stage_6_event_32
    marie "I can get bigger!"
    image marie_stage_6_event_33 = "/marie/events/stage6/33.webp"
    scene marie_stage_6_event_33
    "Pouring in the fourth soda she greedily slurps it down, her hand continuing to rub and explore her body."
    image marie_stage_6_event_34 = "/marie/events/stage6/34.webp"
    scene marie_stage_6_event_34
    "As you quickly swap out the now empty soda for another full one you wonder just how she can fit so much inside her body."
    image marie_stage_6_event_35 = "/marie/events/stage6/35.webp"
    scene marie_stage_6_event_35
    "Each second that passes, her belly swells even more."
    image marie_stage_6_event_36 = "/marie/events/stage6/36.webp"
    scene marie_stage_6_event_36
    marie "Uhhhh."
    "You can see Marie’s hands pushing against her massive belly."
    "Grunting, she tries to shift her weight around."
    image marie_stage_6_event_37 = "/marie/events/stage6/37.webp"
    scene marie_stage_6_event_37
    marie "Oh god, my belly is too big, I can't reach around it."
    marie "Which is so hot, but also kind of like torture to not be able to play with myself while I am like this."
    pc "Maybe I can help."
    image marie_stage_6_event_38 = "/marie/events/stage6/38.webp"
    scene marie_stage_6_event_38
    "Reaching down, you caress between her legs."
    marie "That feels so good…but no I need you to keep filling me!"
    image marie_stage_6_event_39 = "/marie/events/stage6/39.webp"
    scene marie_stage_6_event_39
    marie "Over there, in the drawer, you should find something for this very occasion."
    image marie_stage_6_event_40 = "/marie/events/stage6/40.webp"
    scene marie_stage_6_event_40
    "Leaning over you pull open the drawer to find a large vibrator."
    marie "Mmm, perfect. Now get back over here I’m not nearly big enough yet!"
    image marie_stage_6_event_41 = "/marie/events/stage6/41.webp"
    scene marie_stage_6_event_41
    "Returning to Marie you place the vibrator between her legs and switch it on."
    marie "Woow, that feels amazing."
    marie "Now I need more!"
    image marie_stage_6_event_42 = "/marie/events/stage6/42.webp"
    scene marie_stage_6_event_42
    "Shivering in delight as the device whirs away under Marie, her face flushes as she resumes sucking down the soda."
    "Moaning down the funnel Marie keeps drinking as she forces her body bigger and bigger."
    image marie_stage_6_event_43 = "/marie/events/stage6/43.webp"
    scene marie_stage_6_event_43
    marie "Fuck yeah, this is incredible."
    marie "I’m so fucking big."
    pc "Looks like you have one soda left."
    marie "I don't know if I can manage it, I'm so big, so tight."
    marie "I feel like I am going to pop!"
    image marie_stage_6_event_44 = "/marie/events/stage6/44.webp"
    scene marie_stage_6_event_44
    marie "Ughhh, it makes me so hot to see myself like this, a beached whale."
    marie "Give me more!"
    image marie_stage_6_event_45 = "/marie/events/stage6/45.webp"
    scene marie_stage_6_event_45
    "Grabbing the last soda you pour it in for her to drink."
    "Halfway through the cup you can hear soft creaking noises but you don't know if it's Marie or just her bed frame struggling under her new weight."
    image marie_stage_6_event_46 = "/marie/events/stage6/46.webp"
    scene marie_stage_6_event_46
    "Either way it seems to be turning Marie on more and more."
    image marie_stage_6_event_47 = "/marie/events/stage6/47.webp"
    scene marie_stage_6_event_47
    "Starting to gyrate on the head of the vibrator, Marie keeps drinking."
    image marie_stage_6_event_48 = "/marie/events/stage6/48.webp"
    scene marie_stage_6_event_48
    "Hearing the last bubbles of air sucked up through the funnel, Marie moans loudly in pleasure as she bucks her hips on the bed."
    image marie_stage_6_event_49 = "/marie/events/stage6/49.webp"
    scene marie_stage_6_event_49
    "Falling back onto the bed, Marie cradles her belly as she recovers from her orgasm for a moment before looking up at you."
    image marie_stage_6_event_50 = "/marie/events/stage6/50.webp"
    scene marie_stage_6_event_50
    marie "I want you, I need you!"
    "Marie looks at you with a deep horny hunger."
    if persistent.nosexscene:
        scene black with dissolve
        "Marie and you had a good time."
        if recollection == False:
            $ marie.weight += 2
        $ mariestage6event = 0
        return
    "Taking off you clothes you move towards Marie."
    image marie_stage_6_event_51 = "/marie/events/stage6/51.webp"
    scene marie_stage_6_event_51
    "With your hands holding her legs you begin thrusting into her."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage6/sex1.webm" loop
    show movie with dissolve
    "You can feel the added pressure of her bloated belly inside her as Marie moans in pleasure again and again."
    marie "Fuck yeah, I feel so tight."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage6/sex2.webm" loop
    show movie with dissolve
    window hide
    pause
    pc "You like that?"
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage6/sex3.webm" loop
    show movie with dissolve
    marie "I love it, keep going!"
    marie "No need to be gentle!"
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage6/sex4.webm" loop
    show movie with dissolve
    "Picking up the pace you watch her belly sloshing around."
    marie "This feels so fucking good to be fucked with a belly this big!"
    marie "Keep going, just like that."
    marie "I’m close."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage6/sex5.webm" loop
    show movie with dissolve
    pc "Oh yeah, does it turn you on to be so big?"
    pc "To be so full you can barely move?"
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/marie/events/stage6/sex6.webm" loop
    show movie with dissolve
    marie "Yes!"
    marie "It's going to happen, cum with me!"
    "With a few final trusts you send Marie over the edge as she cums again."
    stop movie
    image marie_stage_6_event_52 = "/marie/events/stage6/52.webp"
    scene marie_stage_6_event_52
    "Pulling out you cum all over her giant belly as she twitches exhausted onto the bed."
    image marie_stage_6_event_53 = "/marie/events/stage6/53.webp"
    scene marie_stage_6_event_53
    marie "That was amazing."
    pc "I'm glad I skipped the gym for that."
    marie "Mmm, me too."
    image marie_stage_6_event_54 = "/marie/events/stage6/54.webp"
    scene marie_stage_6_event_54
    marie "But if you will excuse me, I need to clean up."
    "As Marie cleans herself up in the shower, you tidy up and head home."
    if recollection == False:
        $ marie.weight += 2
    $ mariestage6event = 0
    return

label Marie_Stage_6_Event_2:
    ###Marie 6.2 ###
    ###Go to work###
    play music "/music/bunny_bites.ogg" if_changed
    image marie_stage_6_event_55 = "/marie/events/stage6/55.webp"
    scene marie_stage_6_event_55
    "Arriving at work, the place seems pretty quiet."
    image marie_stage_6_event_56 = "/marie/events/stage6/56.webp"
    scene marie_stage_6_event_56
    marie "Hey, glad I caught you."
    pc "Hi, Marie. How have things been?"
    image marie_stage_6_event_57 = "/marie/events/stage6/57.webp"
    scene marie_stage_6_event_57
    marie "Not too busy yet, but I think it's just a lull."
    marie "Although it's finally given me a chance to implement something I've been working on for a little while."
    marie "Something that maybe we can just keep between you and me, or at least how it works."
    pc "Planning another gluttonous plot?"
    image marie_stage_6_event_58 = "/marie/events/stage6/58.webp"
    scene marie_stage_6_event_58
    marie "Sort of."
    marie "You know I was saying before about Bunny Bites doing really well?"
    pc "Yeah, people love it here."
    marie "Exactly, our customers keep coming back and seem to be ordering more and more food these days."
    marie "It's gotten to the point where more of our regulars are buying off the family sized meal menu than the individual menu."
    pc "You say that it's a bad thing, or that you don't love it as much as me."
    image marie_stage_6_event_59 = "/marie/events/stage6/59.webp"
    scene marie_stage_6_event_59
    marie "Trust me, I love it. It's beyond my wildest dreams."
    marie "But it's become more of a problem and requires more than putting off Chloe so I don't get moved."
    marie "I've tried to solve it by just giving away more large meals for free."
    pc "I thought you had been particularly generous lately."
    marie "I have, but food can't just keep going missing from our sales."
    marie "They sent an invoice last week that I had to fudge some numbers on, but I cant keep doing that. Someone will notice."
    pc "Ok, so what's the plan?"
    marie "I've come up with a plan, a lottery system of sorts."
    pc "Lottery system?"
    image marie_stage_6_event_60 = "/marie/events/stage6/60.webp"
    scene marie_stage_6_event_60
    marie "Yeah, every order now has the chance to win our champions lottery meal."
    marie "Which as a marketing tactic gives me an excuse to give away food and looks more legit to anyone else who looks at it."
    pc "Sounds like a good plan, so do we need to give out raffle tickets or something?"
    image marie_stage_6_event_61 = "/marie/events/stage6/61.webp"
    scene marie_stage_6_event_61
    marie "Uhh…not exactly."
    marie "I haven't really got the systems in place to do it."
    marie "We are going to just make it up…or choose."
    pc "So, we can just choose who wins?"
    pc "Is that fair?"
    image marie_stage_6_event_62 = "/marie/events/stage6/62.webp"
    scene marie_stage_6_event_62
    marie "Does it matter?"
    marie "It's free food and I am assuming having the power to give people more food isn't something you are against."
    marie "Given how many times I see orders being mistaken while you are working too."
    pc "You can see those?"
    marie "I can see everything."
    pc "Ok, so we just choose whoever we want to win it?"
    image marie_stage_6_event_63 = "/marie/events/stage6/63.webp"
    scene marie_stage_6_event_63
    marie "Yeah, we should probably not do it too often though."
    marie "Just keep it to once a week at the moment, and maybe don't just give it to the same person all the time."
    marie "Might make things look a bit suspicious if Bonnie wins it every time she comes in."
    pc "I…yeah."
    image marie_stage_6_event_64 = "/marie/events/stage6/64.webp"
    scene marie_stage_6_event_64
    marie "Just push this button here and it will mark it as the prize draw."
    marie "And if anyone asks, we can just say there is an automated order number in the till that activates it when that number order of the week is reached."
    pc "Sounds good to me."
    marie "I knew it would."
    pc "Great, well is there anything else I should know about it?"
    image marie_stage_6_event_65 = "/marie/events/stage6/65.webp"
    scene marie_stage_6_event_65
    marie "I think that covers the bases."
    marie "So I will let you get back to work, why don't you give it a go during your shift and we can see how it all works."
    image marie_stage_6_event_66 = "/marie/events/stage6/66.webp"
    scene marie_stage_6_event_66
    "Weekly prize option now available when working at Bunny Bites."
    if recollection == False:
        stop music fadeout 1.0
    $ mariestage6event2 = 0
    return

label Marie_Stage_6_Event_3:
    ##Going into work on a weekend -  maybe first event with new outfits?##
    "Walking into work, there seems to be a strange buzz of excitement in the place."
    marie "[playername]!"
    "Looking at the front desk you can see Marie waving you over excitedly."
    pc "Hey Marie, what’s up?"
    marie "Something I think you will enjoy as much as me."
    marie "You remember that eating contest we used to have when you first started here?"
    pc "Yeah, didn’t you have to stop that because people were beating it to easily?"
    marie "Yeah, especially that woman from the hospital. The one with the big…"
    pc "Luna?"
    marie "Exactly."
    pc "You have decided to put it back on?"
    marie "Sort of, but with an improvement."
    marie "People now have to eat their meals faster than a waitress."
    pc "So you set a time limit, how did you account for all the different orders or is it a set meal?"
    marie "No, it's a live competition."
    pc "You mean…?"
    marie "Exactly, each time someone takes on the challenge they have to take on Lisa or Amber."
    marie "And it has happened multiple times already."
    "Looking over to one of the tables, you can see an already bloated looking Lisa clearing away some plates."
    "On the other side of the room it seems like Amber has just finished a meal for the competition."
    ##slightly bloated NPC and Amber###
    pc "Did they both agree to it?"
    marie "They did once I told them they would get to keep whatever they win as a bonus."
    marie "Now, are you ok if I leave you here?"
    pc "Yeah, totally."
    marie "Great, make sure you remember to mention the challenge to all the customers that come in."
    pc "Will do."
    "Taking over from Maire, you start your shift."
    ###At the till - Not sure if you want to use TGT or Comic characters for these NPC’s?###
    ###I was thinking maybe Tracy, Catie and then Nadia and Jess together?”
    "Working the front desk, it doesn’t take long for a customer to arrive."
    pc "Hello and welcome to Bunny Bites, how can I help you today?"
    tracy "Hi, yeah can I get a pizza, fries and a medium drink please."
    pc "Sure thing."
    pc "Before I put that in, I should say we are having a special competition today if you are interested?"
    tracy "Competition?"
    pc "Yes, it is an eating contest between you and one of the waitresses."
    pc "If you win, you get your meal for free."
    tracy "So what you are saying is that if I agree and eat it faster than one of the staff here I get the meal for free."
    pc "Exactly, are you interested?"
    tracy "Why wouldn’t I be."
    tracy "A free meal and just for eating it quickly."
    pc "Ok, I can ring that through for you now."
    tracy "Actually, if it is free…"
    tracy "Can I add a couple of burgers and make that a large drink instead."
    pc "It’s only free if you win."
    tracy "I’m sure I can win."
    pc "In that case, I will put that order through and bring it out to you when it is ready."
    tracy "Great."
    pc "Which waitress would you like to challenge?"
    tracy "Oh, I'm not sure."
    tracy "Who would you recommend?"
    #[Game options of Amber, Lisa and Marie.]
    ###From here it splits into the three character options / stories###
    menu:
        "Amber":
            ###Amber events ####
            ###Amber first time###
            #[Chose Amber at till]
            pc "I would recommend Amber."
            tracy "Ok, Amber sounds great."
            pc "Thanks, I will be right out with your food."
            "Sending the double order through to the kitchen, you go to give Amber the good news."
            ###Talking to amber while she cleans up a table or something###
            pc "Hey Amber."
            amber "Hey, looks like Marie has called everyone in today."
            amber "Probably because of this crazy contest she has on."
            pc "Yeah about that, I’ve got another customer asking for you."
            amber "Another one already?"
            amber "Ughh, please tell me it isn’t too much this time."
            pc "Nothing I haven’t seen you eat as a snack when you are in the mood."
            ##Amber blushing##
            amber "Quiet!"
            pc "Worried someone might hear about how much you like stuffing your greedy face?"
            amber "We are at work."
            pc "And you have another meal to eat."
            "Hearing the service bell ring, it seems her food is ready."
            pc "Why don't you go and take a seat with the customer, it is that table over there."
            pc "I’ll bring over the food."
            "Grabbing the large meals, you take them over the customer and Amber."
            ##Meal is a Pizza, fries, two burgers and a large drink ##
            pc "Here you go."
            tracy "So how does this work?"
            pc "You can enjoy your meal, if you finish first it is on the house."
            pc "Meanwhile my co-worker will be trying to out eat you and at which point we will charge you for the meal."
            tracy "Sounds simple enough."
            "Grabbing the first slice of her Pizza, the customer smiles as she eyes her competition before taking a bite."
            "Following her example, Amber begins eating quickly."
            "Clearly a bit surprised by the ferocity of Amber's gluttony, the customer begins eating faster."
            "Sat opposite each other, they stuff their faces."
            "Despite all of Amber's practice, the hungry customer is putting up a good fight of it."
            "With half the pizza done, the customer finally starts to slow down, not that Amber notices."
            "Switching over to the burgers, she chomps down and the first disappears in a matter of moments."
            "Getting a bewildered look from the customer, you start to think Amber might be over doing it, but you are not about to stop her."
            "Soon Amber’s side is empty and she has finished her meal in record time."
            amber "Ughh, I think I’m done."
            "Looking over and seeing the customer with half the meal still on the table, Amber suddenly looks sheepish."
            tracy "Well, I can say I wasn’t expecting that."
            tracy "Maybe I shouldn’t have been so confident."
            pc "I am afraid I am going to have to give you the bill now, but you can finish your meal."
            tracy "That’s ok, you did warn me when I added extras so this is my own fault."
            tracy "And I think I am actually done, I ate that too fast."
            pc "No problem, you made a good attempt."
            "Putting the order through the till, you give them a 20% discount since they were so nice about it."
            "Returning to the table, the customer pays you and leaves looking a bit bloated despite all the food still on the table."
            amber "Uhhh, I am so full of Pizza."
            pc "You are not done yet though."
            amber "What do you mean, I won?"
            pc "Looks like there is plenty left, we wouldn’t want to waste food now would we?"
            amber "Are you serious, you are doing this to me now?"
            pc "Don't act like you don't enjoy it."
            amber "Now why don't you finish up."
            "Sliding the untouched burger and half a pizza over to Amber, she begrudgingly starts eating again."
            "Her bloated belly grows even more as you stand impatiently next to the table."
            amber "There, I’m done."
            pc "Good, I guess we can get back to work now."
            amber "Ughhh, I’m so full and it’s not even lunch time yet."

            ###At the till - same for all three characters###
            "Going back to work, you serve another few customers."
            "None of them take you up on the eating contest yet though."

            ####Afternoon shift###
            "Continuing to work, soon another customer arrives."
            catie "Hello."
            pc "Good afternoon, welcome to Bunny bites, how can I help you today?"
            catie "Can I get two burgers, two fries, onion rings and uhh…a milkshake."
            pc "That’s no problem."
            pc "We are having a special competition today if you are interested?"
            pc "If you manage to eat your meal faster than a waitress you get it for free."
            catie "That sounds fun."
            "Deciding to make things a bit more interesting, you add to Marie’s deal."
            pc "If you would like to add in any extras we won't add those to your bill even if you fail."
            catie "Why not, I’ll take an extra two burgers and another portion of onion rings in that case."
            pc "Ok, I can ring that through for you now."
            pc "Which waitress would you like to challenge?"
            catie "That is a good question."
            catie "Is there any one of them you recommend?"
            #[Game options of Amber, Lisa and Marie. - irrelevant (see below)]
            menu:
                "Amber":
                    catie "Are you sure, she already looks a little full."
                    catie "Although that works out in my favour right."
                    pc "You can choose anyone you want."
                    catie "No, I think you were right. I’ll go with Amber."
                "Lisa":
                    catie "But if you are choosing her, you must be confident she will beat me."
                    catie "Why would you choose to lose money."
                    catie "So I think I will go with…Amber actually."
                "Marie":
                    catie "But if you are choosing her, you must be confident she will beat me."
                    catie "Why would you choose to lose money."
                    catie "So I think I will go with…Amber actually."

            pc "Sure thing, I will get your food started and let Amber know you want to challenge her."
            catie "Great, thanks."
            ##Talking to bloated Amber##
            pc "You know how you were just thinking about how hungry you were?"
            amber "Please no, I’ve already eaten more than I would on a normal day and it's only just gone midday."
            pc "Hey, this was Marie’s idea not mine."
            pc "And you agreed to it."
            amber "I thought it would just be a few small things, a burger once in a while."
            amber "Please tell me this meal isn’t too big?"
            pc "A few burgers, nothing you can’t manage."
            amber "Ughhh, fine."

            ##At table##
            "Taking the food over to the table, Amber joins the customer."
            ##Meal is a  four burgers, two fries, two onion rings and a milkshake ##
            pc "You can start whenever you would like."
            pc "Finish your meal first and it’s free."
            catie "Great, thanks."
            "Eyeing Amber for a moment, the customer grabs the first burger and starts eating."
            "Following suit, the two of them make quick work of the first burger."
            "Moving onto the second, they alternate between burgers, fries and onion rings."
            "The pair of them are neck and neck at the halfway point, neither showing signs of slowing down despite Amber already telling you she was full."
            "With only a few onion rings left, it is almost impossible to tell who is going to win."
            "Finally they are both done, the table completely empty of food, their bellies growing rounder with all the food they had eaten."
            catie "So, who was it, who won?"
            pc "It was a draw…but."
            "Inspecting the packets left on the table, you find a single small fry left in Amber’s wrapper."
            pc "I am afraid, Amber hasn’t quite finished by the looks of it."
            amber "Come on, it’s one fry."
            pc "You know the rules, this round goes to the customer."
            catie "Yes!"
            catie "That was fun, thanks for suggesting it."
            catie "Oooh, although my waistline might not enjoy those extra calories."
            pc "No problem, thank you for competing."
            pc "This meal is on the house, so feel free to leave whenever you want and don't worry about the bill."
            ##With Amber at the front desk##
            amber "Ughhh, I don't know how many more of these I can do."
            amber "Just look at this belly."
            "Sticking her gut out, it’s hard not to see what she means."
            amber "Please, can you just get the next person to pick someone else."
            amber "I need a break."
            pc "I can try, but the choice is up to them."
            amber "I know…"

            "Going back to work, you deal with the lunch rush without any further competitions."
            ##Evening shift ##

            ###Jess and Nadia together###
            "Continuing to work, soon another couple of customers arrive."
            jess "Hi, we heard you were giving out free food today?"
            pc "Good evening, sort of."
            pc "We are running a contest where you can win your meal for free if you can beat a waitress in an eating contest."
            jess "That’s even better!"
            pc "Would you like to place an order?"
            jess "Absolutely, can we get two large pizzas, four… no five, burgers, six fries, six onion rings, two large milkshakes and two large soda’s."
            pc "That is a large order, are you ok to cover the cost if the waitresses beat you both?"
            jess "I am confident she will win."
            pc "In that case, I can put that order through."
            pc "Which waitress would you like to challenge, or I guess waitresses?"
            jess "Mmm, looks like they have had plenty to eat already today."
            jess "Let’s go with that one there and the one serving that table."
            pc "Amber and Lisa."
            jess "Sure."
            pc "Great, take your seat and I will bring the food over."
            pc "Given the size of it, it might take a few minutes."
            jess "That’s ok, we can wait."
            "Putting the larger order through, you go to break the good news to your colleagues."
            ###Approaching Amber###
            pc "Hey Amber."
            amber "Oh no, please I can’t eat any more."
            pc "Well there is good news and bad news."
            pc "They did choose you, but they also chose Lisa."
            pc "So at least you won’t be alone."
            amber "Ughhh, I really don't need any more to eat today."
            "Wrapping her hands around her bloated belly, you can see why she was saying that."
            "Her increasingly flabby midsection is clearly full and tight, even without the extra meal."
            amber "Maybe Lisa can manage most of it."
            ##Lisa appears##
            lisa "You guys talking about me?"
            pc "We’ve got another challenge from a customer."
            lisa "Oh, sure thing. I was starting to get hungry anyway."
            amber "That makes one of us."
            lisa "Let me just finish serving this table and I can be right over."
            "Piling up the plates, you take the mountain of food over to the table with the two customers."

            ##At the table with Nadia, Jess, Amber and Lisa.###
            ##Meal is two pizza’s, five burgers, six fries, six onion rings, two large milkshakes and two large soda##
            pc "Here is your food."
            pc "Just a reminder, if you both don't finish your food you will be charged for the meal."
            jess "Oh, it’s not both of us."
            pc "What?"
            jess "Only Nadia will be eating, isn’t that right."
            nadia "Yes."
            pc "Oh, I thought you were both entering, that's why both waitresses are here."
            jess "Don’t worry about that, I am sure Nadia can out eat both of them."
            "Exchanging nervous glances, Lisa and Amber seem to be wondering what they have gotten themselves in for."
            pc "In that case, I guess you can start whenever you want."
            "Grabbing the first slice of pizza the customer eats it in a matter of seconds before immediately going for a second."
            "It takes your two co-workers a moment to realise, shocked by the speed she had devoured it."
            "But grabbing a burger each they start eating."
            "Hands turned into blur’s as food disappeared into hungry mouths and growing stomachs."
            "While Amber and Lisa might have started strong, the day of eating competitions was drastically slowing Amber down."
            "Chomping through two burgers, she already looked ready to give up, or pop."
            "Lisa meanwhile was having no such issue, already onto the fries and onion rings."
            "Across the table, the customer was somehow keeping pace with two eaters."
            "An entire pizza, fries, drink and half a burger disappearing into her bloated belly."
            amber "I can’t…I’m too stuffed."
            lisa "Keep eating!"
            amber "My stomach hurts."
            "Grabbing some of Amber's side of the meal, Lisa begins to eat faster."
            jess "You could always concede?"
            lisa "Not happening, she can keep going."
            "Despite Lisa’s confidence it was clear Amber had reached her limit, although she was still shoving more food into her over stretched belly."
            "Going into the final stretch, the groups seemed neck and neck."
            "The now giant stomach of the competitor was seemingly not slowing her down one bit as she continued to eat at the speed of two people."
            "Slurping down the last of the milkshakes, she moved onto the final Pizza and soda’s."
            lisa "Come on Amber, eat!"
            amber "I can’t, I'm too full."
            "Shovelling fries and onion rings into her mouth, Lisa tried to encourage Amber."
            "It still looked like anyone could win, but even Lisa was slowing down."
            "Compensating for Amber, she had ended up eating much more of this meal and was struggling herself."
            "With only a few onion rings left on their side, their opponent raised her hands victoriously."
            "The customers had won, but at what cost."
            nadia "Ughhh…I don't feel so hot."
            "You could see why, the dark haired woman had put away an incredible amount of food in less than 30 minutes."
            "Her stomach is bigger than even Amber’s and dwarfs Lisa’s with just this one meal."
            pc "Well, congratulations. This meal is on the house."
            jess "I knew you could do it!"
            jess "It was a good effort by you two though."
            amber "Ughhh, I don't think I can stomach another bite."
            lisa "I know how you feel."
            "Sitting uncomfortably, they try to get their overfilled bellies to calm down."
            "Waving goodbye, the customers leave them to their misery."
            amber "I can’t move."
            pc "Well good news, it looks like those were our last customers for the evening."
            lisa "Good, I don't know if I could stomach another competition."
            "Leaving them to rest, you go and finish up all the last bits of work at the till."

        "Lisa":
            ###Lisa first time###
            #[Chose Lisa at till]
            pc "I would recommend Lisa."
            tracy "Ok, Lisa sounds great."
            pc "Thanks, I will be right out with your food."
            "Sending the double order through to the kitchen, you go to give Lisa the good news."
            ###Talking to amber while she cleans up a table or something###
            pc "Hey Lisa."
            lisa "Hey, sorry I didn’t see you get in."
            lisa "How are you doing?"
            pc "Good, thanks."
            pc "I’ve actually got another customer that wants to challenge you."
            lisa "Ughh, I am going to kill Marie."
            lisa "I think we both know why and where this genius idea has come from."
            pc "Yeah, I don't think she is as subtle or sneaky as she might like to believe."
            "Hearing the service bell ring, it seems her food is ready."
            pc "Why don't you go and take a seat with the customer, it is that table over there."
            pc "I’ll bring over the food."
            lisa "Sure thing, thanks."
            "Grabbing the large meals, you take them over the customer and Lisa."
            ##Meal is a Pizza, fries, two burgers and a large drink ##
            pc "Here you go."
            tracy "So how does this work?"
            pc "You can enjoy your meal, if you finish first it is on the house."
            pc "Meanwhile Lisa will be trying to out eat you and at which point we will charge you for the meal."
            tracy "Sounds simple enough."
            "Grabbing the first slice of her Pizza, the customer smiles as she eyes her competition before taking a bite."
            "Following her example, Lisa begins eating."
            "Keeping a similar pace, neither seems in a particular rush to finish the meal."
            "Sat opposite each other, they stuff their faces."
            "However, as the food disappears and plates empty, you notice them picking up the pace now they can see the finish line."
            "Despite all of Lisa’s practice with you and Marie, the hungry customer is putting up a good fight of it."
            "Neck and neck, their stomachs grow from all the food and soon only a couple of items are left."
            "Grabbing the last burger things seem to be becoming more intense as they race each other to the finish."
            "With only a few bites left, the customer cleans their plate first and wins the challenge."
            pc "Congratulations, you have won your meal for free!"
            tracy "Amazing, I knew I could do it."
            tracy "Although you had me worried for a moment there."
            lisa "Ughhh, that was close but I am glad that was all the food we had to eat."
            tracy "You an me both, think my eyes are still a bit bigger than my stomach."
            "As the customer pats her bloated belly, you wonder if that was true or not."
            pc "Well, you are free to leave and once again well done for winning."
            tracy "Thanks, that was fun."
            "Returning to the till with the bloated Lisa you see the customer leaving slowly."
            lisa "Uhhh, I am so full of Pizza."
            lisa "I don't think I can eat any more carbs, my mouth is so dry but I can’t even deal with the idea of drinking any more either."
            lisa "Please can you suggest someone else to the next customer."
            lisa "I could really do with a break."
            pc "I mean I can try, but it is up to them who they challenge."
            lisa "Ughh, I know."
            lisa "In that case I am going to go hide in the store room for a bit."
            "Walking off slowly, you see her push her way into the store room to take a well deserved break."

            ###At the till - same for all three characters###
            "Going back to work, you serve another few customers."
            "None of them take you up on the eating contest yet though."
            "Continuing to work, soon another customer arrives."
            catie "Hello."
            pc "Good afternoon, welcome to Bunny bites, how can I help you today?"
            catie "Can I get two burgers, two fries, onion rings and uhh…a milkshake."
            pc "That’s no problem."
            pc "We are having a special competition today if you are interested?"
            pc "If you manage to eat your meal faster than a waitress you get it for free."
            catie "That sounds fun."
            "Deciding to make things a bit more interesting, you add to Marie’s deal."
            pc "If you would like to add in any extras we won't add those to your bill even if you fail."
            catie "Why not, I’ll take an extra two burgers and another portion of onion rings in that case."
            pc "Sure thing, I can ring that through for you now."
            pc "Which waitress would you like to challenge?"
            catie "That is a good question."
            catie "Is there any one of them you recommend?"
            #[Game options of Amber, Lisa and Marie. - irrelevant (see below)]
            menu:
                "Lisa":
                    catie "Are you sure, she already looks a little full."
                    catie "Although that works out in my favour right."
                    pc "You can choose anyone you want."
                    catie "No, I think you were right. I’ll go with Lisa after all."
                "Amber":
                    catie "But if you are choosing her, you must be confident she will beat me."
                    catie "Why would you choose to lose money."
                    catie "So I think I will go with…Lisa."
                "Marie":
                    catie "But if you are choosing her, you must be confident she will beat me."
                    catie "Why would you choose to lose money."
                    catie "So I think I will go with…Lisa."

            ##Same for all options##
            pc "No problem, I will get your food started and let Lisa know you want to challenge her."
            catie "Great, thanks."
            ##Talking to bloated Lisa##
            pc "Hi Lisa, I hope your break went well?"
            lisa "Oh no, I am not doing another one."
            pc "Hey, this was Marie’s idea not mine."
            pc "And you agreed to it."
            lisa "Yeah but have you tried working a full shift while being this full."
            lisa "I would do anything for Marie, but it’s on her if I start messing things up."
            pc "I’ll cover for you if that would help."
            lisa "Yeah I guess I did agree to this."

            ##At table##
            "Taking the food over to the table, Lisa joins the customer."
            ##Meal is a  four burgers, two fries, two onion rings and a milkshake ##
            pc "You can start whenever you would like."
            pc "Finish your meal first and it’s free."
            catie "Great, thanks."
            "Eyeing Lisa for a moment, the customer grabs the first burger and starts eating."
            "Following suit, the two of them make quick work of the first burger."
            "Moving onto the second, they alternate between burgers, fries and onion rings."
            "The pair of them are neck and neck at the halfway point, although Lisa is beginning to slow down."
            "Any room she had made while on break now filled by the next meal she was forcing down her throat."
            "Across from her, the customer seemed to be enjoying the contest while taking large bites out of her last burger."
            "With only a few onion rings left for Lisa, the customer once again finishes first but it was a close call."
            "Both their bellies have clearly grown rounder with all the food they had eaten."
            catie "So, did I win?"
            pc "Congratulations, you finished your meal first so it is free."
            catie "Yes!"
            catie "That was fun, thanks for suggesting it."
            catie "Although my waistline might not enjoy those extra calories."
            pc "No problem, thank you for competing."
            pc "This meal is on the house, so feel free to leave whenever you want and don't worry about the bill."

            ##With Lisa at the front desk##
            lisa "Thanks for suggesting it, I knew you would be in this with Marie."
            pc "I don't know what you mean."
            lisa "Sure…"
            lisa "Ughh, just a few more hours to survive without exploding."
            "Going back to work, you deal with the lunch rush without any further competitions."

            ##Evening shift ##
            ###Jess and Nadia together###
            "Continuing to work, soon another couple of customers arrive."
            jess "Hi, we heard you were giving out free food today?"
            pc "Good evening, sort of."
            pc "We are running a contest where you can win your meal for free if you can beat a waitress in an eating contest."
            jess "That’s even better!"
            pc "Would you like to place an order?"
            jess "Absolutely, can we get two large pizzas, four… no five, burgers, six fries, six onion rings, two large milkshakes and two large soda’s."
            pc "That is a large order, are you ok to cover the cost if the waitresses beat you both?"
            jess "I am confident she will win."
            pc "In that case, I can put that order through."
            pc "Which waitress would you like to challenge, or I guess waitresses?"
            jess "Mmm, looks like they have had plenty to eat already today."
            jess "Let’s go with that one there and the one serving that table."
            pc "Amber and Lisa?"
            jess "Sure."
            pc "Great, take your seat and I will bring the food over."
            pc "Given the size of it, it might take a few minutes."
            jess "That’s ok, we can wait."
            "Putting the larger order through, you go to break the good news to your colleagues."

            ###Approaching Lisa###
            pc "Hey Lisa."
            lisa "No, no no, I am telling you I can’t eat any more."
            pc "Well there is good news and bad news."
            pc "They did choose you, but they also chose Amber."
            pc "So at least you won’t be alone."
            lisa "Ughhh, I really don't need any more to eat today."
            "Wrapping her hands around her bloated belly, you can see why she was saying that."
            "Her increasingly large belly is clearly full and tight, even without the extra meal."
            pc "Maybe Amber can manage most of it."
            lisa "I hope so."
            ##Amber appears##
            amber "You guys talking about me?"
            pc "We’ve got another challenge from a customer."
            amber "Oh, sure thing. I was starting to get hungry anyway."
            lisa "How, haven’t you had several challenges today."
            ###Amber blushing###
            amber "I don't know, I guess I was just hungry today."
            lisa "Let me just finish serving this table and I can be right over."
            "Going over to the table, it is clear one of your co-workers is feeling more excited than the other."
            "Piling up the plates, you take the mountain of food over to the table with the two customers."
            ##At the table with Nadia, Jess, Amber and Lisa.###
            ##Meal is two pizza’s, five burgers, six fries, six onion rings, two large milkshakes and two large soda##
            pc "Here is your food."
            pc "Just a reminder, if you both don't finish your food you will be charged for the meal."
            jess "Oh, it’s not both of us."
            pc "What?"
            jess "Only Nadia will be eating, isn’t that right."
            nadia "Yes."
            pc "Oh, I thought you were both entering, that's why both waitresses are here."
            jess "Don’t worry about that, I am sure Nadia can out eat both of them."
            "Exchanging nervous glances, Lisa and Amber seem to be wondering what they have gotten themselves in for."
            pc "In that case, I guess you can start whenever you want."
            "Grabbing the first slice of pizza the customer eats it in a matter of seconds before immediately going for a second."
            "It takes Amber and Lisa a moment to realise things had started, shocked by the speed the customer had devoured it."
            "But grabbing a burger each they start eating."
            "Hands turned into blur’s as food disappeared into hungry mouths and growing stomachs."
            "While Amber and Lisa might have started strong, the day of eating competitions was drastically slowing Lisa down."
            "Chomping through two burgers, she already looked ready to give up, or pop."
            "Amber meanwhile was having no such issue, already onto the fries and onion rings."
            "A smile on her face as she let her gluttony out for all to see."
            "Across the table, the customer was somehow keeping pace with two eaters."
            "An entire pizza, fries, drink and half a burger disappearing into her bloated belly."
            lisa "I can’t…I’m too stuffed."
            lisa "My stomach is really starting to hurt."
            "Looking down it was easy to see why, the giant orb of a stomach filled to capacity with so much food."
            amber "Give it here."
            "Grabbing some of Lisa’s side of the meal, Amber begins to eat faster."
            jess "You could always concede?"
            amber "Not happening, I’ve got plenty of room left!"
            "Despite Amber's confidence it was clear Lisa had reached her limit."
            "She had become almost an observer, watching the two gluttons stuff their faces with the mountain of food."
            "Going into the final stretch, the two remaining eaters seemed neck and neck."
            "The now giant stomach of the competitor was seemingly not slowing her down one bit as she continued to eat."
            "Slurping down the last of the milkshakes, she moved onto the final Pizza and soda."
            jess "Looks like it is going to be close."
            amber "I can do this, no stopping me!"
            jess "You still have plenty of room left, right Nadia?"
            nadia "Ughh, yeah sure."
            "For the first time you saw some hesitancy in the woman."
            jess "Why don't we make this interesting then, seems like we are running out of food."
            jess "Could you go and get us a couple of extra burgers and maybe some chicken nuggets please."
            pc "Uhhh…are you sure?"
            jess "We wouldn’t want to end this in a draw right."
            jess "Besides, if we lose it is more money for your guys right?"
            pc "Sure, I can go and get those."
            lisa "Dont worry about it, I’ll go and get them."
            "Standing with a grunt it seems Lisa has given up any attempts to eat anything else."
            "Waddling her way to the kitchen she goes in to place an order."
            "Back at the table, the two women were quickly running out of food and room."
            "Their giant stomach’s taking up most of the booth at this point."
            "Picking up the last packet of fries, they are risk of finishing but you notice Lisa returning with two large trays of food."
            amber "Good timing."
            "Unloading the food onto the table, a new round of eating begins."
            ##Three extra burgers and two large chicken nugget boxes each##
            "Grabbing her first burger Amber still seems to be in the zone, chomping at the bit to fill her swelling body even more."
            "Across from her you can see the first signs of discomfort from her opponent."
            amber "Mmm, these are so good when they are still warm."
            "Opening the large boxes of nuggets Amber digs in."
            nadia "Oooooh."
            "Pausing for a moment, the customer can’t help but massage her giant stomach."
            jess "Come on Nadia, you are almost there."
            nadia "I’m too full."
            jess "Less talking, more eating!"
            "Diving back into her meal the two big bellied women continue eating."
            "Even with the extra food the table is quickly emptying."
            "Down to the final burger, Amber is still going strong."
            "Finishing her meal Amber holds up her hands triumphantly."
            nadia "Ughhh."
            "With half a burger left, the customer's arms fall to the sides as she slumps in her seat, defeated."
            nadia "I’m going to explode, I can’t believe how much I just ate."
            "Opposite her, it doesn’t seem like Amber is doing much better."
            "Cradling her giant belly, it seems reality is starting to set in for the blonde woman."
            jess "Dang, I didn’t expect to meet anyone that could eat more than Nadia here."
            pc "I am afraid, I am going to have to ask you to pay for this meal now."
            jess "No problem."
            jess "Why don't we give them a moment and I will come and pay."

            ###At till with Jess##
            jess "Your friend sure can put food away."
            jess "Just look at them all over there."
            "Looking over at the three stuffed women, you know what she means."
            pc "Given how close it was, I won't charge you for the extra burgers."
            jess "That’s kind of you."
            "Paying her bill, you watch as her friend barely able to walk makes her way over to her."
            "With some helping hands, they both make their way out of the restaurant."

            ###Back at the table###
            pc "Well done, that should be a pretty nice bonus for you guys."
            amber "I can’t move."
            pc "Well good news, it looks like those were our last customers for the evening."
            lisa "Good, I don't know if I could stomach another competition."
            "Leaving them to rest, you go and finish up all the last bits of work at the till."
            ###End of day###

        "Marie":
            ###Marie first time###
            pc "I would recommend Marie."
            tracy "Ok, Marie sounds great."
            pc "Thanks, I will be right out with your food."
            "Sending the double order through to the kitchen, you go to give Lisa the good news."
            ###Talking to Marie while she cleans up a table or something###
            pc "Hey Marie."
            marie "Hey, have we had any takers on the competition yet?"
            pc "Actually, we’ve just had one."
            marie "Great, who did they choose?"
            pc "Actually, you."
            marie "Me!?"
            marie "When I said…"
            pc "The competition says any waitress."
            marie "I keep forgetting you are out to make me fat, aren’t you."
            pc "Maybe it was the customers choice?"
            marie "Was it?"
            pc "I may have suggested something."
            marie "As I thought."
            marie "But if I fail this, it is coming out of your pay."
            marie "You were not supposed to be the one enjoying this."
            pc "You say that like I don't know it turns you on too."
            pc "Why don't you go and take a seat with the customer, it is that table over there."
            pc "I’ll bring over the food."
            marie "Fine but this is the only time I am agreeing to this though."
            "Grabbing the large meals, you take them over the customer and Lisa."
            ##Meal is a Pizza, fries, two burgers and a large drink ##
            pc "Here you go."
            tracy "So how does this work?"
            pc "You can enjoy your meal, if you finish first it is on the house."
            pc "Meanwhile Marie will be trying to out eat you and at which point we will charge you for the meal."
            tracy "Sounds simple enough."
            "Grabbing the first slice of her Pizza, the customer takes a bite."
            "Giving you a knowing look, Marie follows suit and picks up a burger."
            "Keeping a similar pace, neither seems in a particular rush to finish the meal."
            "Despite her original complaints, it is clear Marie is enjoying watching the woman opposite her eat."
            "Usually stuck working while the customers binge, this was the first time she was up close and personal with them."
            "Neck and neck, their stomachs grow from all the food and soon only a couple of items are left."
            "You are not sure if Marie is doing this to eat herself or to make her opponent stuff her face even faster."
            "Grabbing the last burger things seem to be becoming more intense as they race each other to the finish."
            "With only a few bites left, the customer cleans their plate first and wins the challenge."
            pc "Congratulations, you have won your meal for free!"
            tracy "Amazing, I knew I could do it."
            tracy "Although you had me worried for a moment there."
            marie "Wouldn’t want it to be too easy for you."
            pc "Well, you are free to leave and once again well done for winning."
            tracy "Thanks."
            "Returning to the till with the bloated Marie you see the customer leaving slowly."
            marie "My stomach feels so heavy."
            marie "But did you see the way she was eating, I bet she could have eaten twice the amount."
            pc "And you, I know I have seen this belly bigger than this before."
            marie "Maybe, but a soda bloat is one thing. Stuffing myself full of greasy food is completely different."
            pc "So, up for another round?"
            marie "What?"
            pc "You seemed to enjoy the show."
            marie "I did, but I think one was enough for me."
            pc "I’ll see what I can do, but it is up to them who they challenge."
            marie "An oversight on my part."
            "Walking off slowly, Marie gathers the dirty plates and cleans down the tables for the next customers."

            ###At the till - same for all three characters###
            "Going back to work, you serve another few customers."
            "None of them take you up on the eating contest yet though."

            ###Afternoon shift###
            "Continuing to work, soon another customer arrives."
            catie "Hello."
            pc "Good afternoon, welcome to Bunny bites, how can I help you today?"
            catie "Can I get two burgers, two fries, onion rings and uhh…a milkshake."
            pc "That’s no problem."
            pc "We are having a special competition today if you are interested?"
            pc "If you manage to eat your meal faster than a waitress you get it for free."
            catie "That sounds fun."
            "Deciding to make things a bit more interesting, you add to Marie’s deal."
            pc "If you would like to add in any extras we won't add those to your bill even if you fail."
            catie "Why not, I’ll take an extra two burgers and another portion of onion rings in that case."
            pc "Sure thing, I can ring that through for you now."
            pc "Which waitress would you like to challenge?"
            catie "That is a good question."
            catie "How about her?"
            "Looking over you smile as you realise she is pointing at Marie."
            pc "Marie, are you sure?"
            catie "Even more so now, makes me think you wanted me to pick someone else."
            pc "No, that is fine."
            pc "I will get your food started and let Marie know you want to challenge her."
            catie "Great, thanks."

            ##Talking to bloated Marie##
            pc "Hi Marie"
            marie "Don’t tell me, you convinced another customer to challenge me."
            pc "Actually, she chose you this time."
            marie "Yeah, somehow I doubt that."
            pc "No honestly she did, you can even ask her."
            marie "What are the chances of that?"
            pc "Maybe it is karma, you plan to fatten Lisa and Amber backfiring on you."
            marie "Somehow I still feel like you had something to do with it."
            pc "Well, they are waiting if you want to join her."
            marie "Guess I don't really have much of a choice."

            ##At table##
            "Taking the food over to the table, Marie joins the customer."
            ##Meal is a  four burgers, two fries, two onion rings and a milkshake ##
            pc "You can start whenever you would like."
            pc "Finish your meal first and it’s free."
            catie "Great, thanks."
            "Grabbing the first burger the customer starts eating followed by Marie."
            "The two of them make quick work of the first burger, but it is clear your boss is still full from the last contest."
            "Moving onto the second, they alternate between burgers, fries and onion rings."
            "Despite her reluctance to join in, Marie is clearly enjoying the chance to watch the customer closely and enjoying the show."
            "The speed is much slower than the previous contest, Marie not forcing the customer to eat quickly."
            "Staying a little behind the customer Marie keeps eating."
            "Moving onto her last burger, you can tell Marie knows she has lost but is putting on a good show to keep her opponent eating."
            "With a few items left on Marie’s side, the customer once again finishes first."
            "Both their bellies have clearly grown rounder with all the food they had eaten."
            catie "So, did I win?"
            pc "Congratulations, you finished your meal first so it is free."
            catie "That was fun, thanks for suggesting it."
            catie "Although my waistline might not enjoy those extra calories."
            pc "No problem, thank you for competing."
            pc "Feel free to leave whenever you want and don't worry about the bill."

            ##With Marie at the front desk##
            marie "Ughh, maybe this wasn’t such a brilliant idea."
            pc "I don't know, I think it was pretty good."
            marie "I am sure you do, you are not the one who has had to eat five meals worth of food in half a shift."
            marie "Now if you excuse me, I’m going to find some paperwork or something to do."
            "Going back to work, you deal with the lunch rush without any further competitions."

            ##Evening shift ##
            ###Jess and Nadia together###
            "Continuing to work, soon another couple of customers arrive."
            jess "Hi, we heard you were giving out free food today?"
            pc "Good evening, sort of."
            pc "We are running a contest where you can win your meal for free if you can beat a waitress in an eating contest."
            jess "That’s even better!"
            pc "Would you like to place an order?"
            jess "Absolutely, can we get two large pizzas, four… no five, burgers, six fries, six onion rings, two large milkshakes and two large soda’s."
            pc "That is a large order, are you ok to cover the cost if the waitresses beat you both?"
            jess "I am confident she will win."
            pc "In that case, I can put that order through."
            pc "Which waitress would you like to challenge, or I guess waitresses?"
            jess "Mmm, looks like they have had plenty to eat already today."
            jess "Let’s go with that one there and the one serving that table."
            pc "Amber and Lisa?"
            jess "Sure."
            pc "Great, take your seat and I will bring the food over."
            pc "Given the size of it, it might take a few minutes."
            jess "That’s ok, we can wait."
            "Putting the larger order through, you go to break the good news to your colleagues."

            ###Approaching Lisa###
            pc "Hey Lisa."
            lisa "Hi, how is it going?"
            pc "Good, we have another request or challenge for you."
            lisa "Oh ok, you know I have been surprised by how few people have been taking on the challenge today."
            lisa "I didn’t have any lunch to make sure I had room, so i'm honestly a little hungry."
            pc "Great, it’s that table over there."
            pc "I just need to let Amber know as well since it is two of them."
            ##Amber serving a table next to you###
            amber "Let me know what?"
            pc "Oh, there is a food challenge over there who have requested both you and Lisa."
            amber "Ok great, I’ll just finish up serving this table and head over."
            "A few minutes later the large order is done and you head over."
            "Piling up the plates, you take the mountain of food over to the table with the two customers."

            ##At the table with Nadia, Jess, Amber and Lisa.###
            ##Meal is two pizza’s, five burgers, six fries, six onion rings, two large milkshakes and two large soda##
            pc "Here is your food."
            pc "Just a reminder, if you both don't finish your food you will be charged for the meal."
            jess "Oh, it’s not both of us."
            pc "What?"
            jess "Only Nadia will be eating, isn’t that right."
            nadia "Yes."
            pc "Oh, I thought you were both entering, that's why both waitresses are here."
            jess "Don’t worry about that, I am sure Nadia can out eat both of them."
            "Exchanging nervous glances, Lisa and Amber seem to be wondering what they have gotten themselves in for."
            pc "In that case, I guess you can start whenever you want."
            "Grabbing the first slice of pizza the customer eats it in a matter of seconds before immediately going for a second."
            "It takes Amber and Lisa a moment to realise things had started, shocked by the speed the customer had devoured it."
            "But grabbing a burger each they start eating."
            "Hands turn into blur’s as food disappears into hungry mouths and growing stomachs."
            "While Amber and Lisa might have started strong, there was no denying the speed of their opponent."
            "A whole pizza gobbled up by the hungry customer before either of your coworkers had finished half."
            "However, seeing the display of gluttony opposite her seemed to spur Amber on, or perhaps gave her a good reason to give in."
            "Moving onto a burger, fries and onion rings Amber picks up the pace, even grabbing a few extra from Lisa’s side."
            "A smile on her face as she let her gluttony out for all to see."
            "However, across the table the customer was somehow keeping pace with two eaters."
            "An entire pizza, fries, drink and two burgers disappearing into her bloated belly."
            lisa "I’m starting to get a bit full over here."
            amber "Give it here."
            "Grabbing more of Lisa’s side of the meal, Amber eats like a starving animal."
            jess "You could always concede?"
            amber "Not happening, I’ve got plenty of room left!"
            "Despite Amber's confidence Lisa was definitely slowing down."
            "Going into the final stretch, they seemed neck and neck."
            "The now giant stomach of the competitor was not slowing her down as she continued to eat."
            "Slurping down the last of the milkshakes, she moved onto the final Pizza and soda."
            jess "Looks like it is going to be close."
            amber "I can do this, no stopping me!"
            jess "You still have plenty of room left, right Nadia?"
            nadia "Ughh, yeah sure."
            "For the first time you saw some hesitancy in the woman."
            jess "Why don't we make this interesting then, seems like we are running out of food."
            jess "Could you go and get us a couple of extra burgers and maybe some chicken nuggets please."
            pc "Uhhh…are you sure?"
            jess "We wouldn’t want to end this in a draw right."
            jess "Besides, if we lose it is more money for you guys right?"
            pc "Sure, I can go and get those."
            "Not wanting to miss anything, you quickly rush over to Marie at the front desk to place the order."
            "Barely looking at you, she seemed entirely wrapped up in the eating contest as she put through the extra order."
            "Rushing back to “adjudicate” you can see the table is almost empty at this point."
            "Picking up the last packet of fries, they are risk of finishing but you notice Marie returning with two large trays of food."
            amber "Good timing."
            "Unloading the food onto the table, you notice it was more than you ordered."
            "Marie either making a mistake due to being distracted or genuinely wanting to push all their limits to the max."
            ##Six extra burgers and four large chicken nugget boxes each side##
            "Grabbing her first burger Amber still seems to be in the zone, chomping at the bit to fill her swelling body even more."
            "Across from her you can see the first signs of discomfort from her opponent."
            amber "Mmm, these are so good when they are still warm."
            "Opening the large boxes of nuggets Lisa slowly eats, content on letting Amber win this for them."
            nadia "Oooooh."
            "Pausing for a moment, the customer can’t help but massage her giant stomach."
            "All three now sporting giant distended bellies that almost trapped them into the booth."
            "You were genuinely starting to worry about how much the benches could hold."
            jess "Come on Nadia, you are almost there."
            nadia "I’m too full."
            jess "Less talking, more eating!"
            "Picking up a large nugget, she all but forced it into the mouth of her friend."
            "Reluctantly eating, she was back to her meal."
            "Even with the extra food the table is quickly emptying."
            "Down to the final burger, Amber is still going strong."
            "Finishing her meal Amber holds up her hands triumphantly."
            nadia "Ughhh."
            "With half a burger left, the customer's arms fall to the sides as she slumps in her seat, defeated."
            nadia "I’m going to explode, I can’t believe how much I just ate."
            "Opposite her, it doesn’t seem like Amber is doing much better."
            "Cradling her giant belly, it seems reality is starting to set in for the blonde woman."
            jess "Dang, I didn’t expect to meet anyone that could eat more than Nadia here."
            pc "I am afraid, I am going to have to ask you to pay for this meal now."
            pc "Although, given the mix up we wont charge you for the extra’s right Marie?"
            "Looking to your side, Marie hadn’t returned to the front desk and was instead salivating over the show of pure hedonistic gluttony."
            marie "Uhh…yeah that’s fine."
            jess "Mix up?"
            "It seems Marie wasn’t the only one two wrapped up in what was happening to notice."
            jess "No problem."
            jess "Why don't we give them a moment and I will come and pay."

            ###At till with Jess##
            jess "Your friends sure can put food away."
            jess "Just look at them all over there."
            "Looking over at the three stuffed women, you know what she means."
            "Paying her bill, you watch as her friend barely able to walk makes her way over."
            "With some helping hands, they both make their way out of the restaurant."
            ###Back at the table###
            pc "Well done, that should be a pretty nice bonus for you guys."
            amber "I can’t move."
            pc "Well good news, it looks like those were our last customers for the evening."
            lisa "Good, I don't know if I could stomach another competition."
            "Leaving them to rest, you go and finish up all the last bits of work at the till."
            ###End of day###

    ###End of day bit on last page - same for all###
    "Typing in something into the till, you keep getting a strange error code you don't recognise."
    "Looking around the restaurant, you are surprised to only see Amber."
    ##Amber Lounging in one of the booths looking very full ##
    pc "Hey, have you seen Marie?"
    amber "I think she and Lisa might be doing a stock check in the back."
    pc "Great thanks."
    "Going to the stock room to ask about the error code, you start to hear strange noises coming from the room."
    ###I am thinking Marie is pressed up against a wall with Lisa eating her out / head between her legs.###
    ##Marie can be bloated here for all endings, as if she had eaten in the contests or bloated herself with Lisa while you were still working.###
    "Poking your head in, you are shocked to see Marie and Lisa naked in the room."
    "Lisa’s head is currently between the legs of the moaning Marie."
    "Making eye contact with you, she gives you a knowing and horny look."
    marie "Fuck, I’m going to cum!"
    "Grabbing Lisa’s head and pressing it deeper between her legs, you see her body shake as an orgasm races through her body."
    "Watching Marie cum, you duck back out of the room and head back to the main room."
    ###Main room, Amber back in usual clothes ###
    amber "Any luck finding them?"
    pc "Yeah, although they seem pretty busy."
    amber "Yeah, we did sell a lot today."
    amber "Most of it is in here."
    "Looking down fondly, Amber plays with her belly."
    pc "Would you maybe want to come back to mine, maybe make the most of it?"
    amber "Tempting, sadly I agreed to meet up with Maya."
    amber "Although what she is going to think when she sees me looking like this."
    pc "That you look hotter than usual?"
    amber "You need to work on your flirting, but thanks."
    ##Amber kisses you on the cheek###
    amber "Anyway, I am going to head out."
    pc "See you soon Amber."
    amber "Bye."
    "Finishing cleaning up the place, the two love birds still haven’t left the back room."
    "Deciding they might still be a while, you decide to head home."
    if recollection == False:
        $ daytime = 4
        $ lisa.weight = 83
        $ amber.weight = 85
        $ marie.weight = 91
    $ mariestage6event3 = 0
    return


label MarieStage7Phone:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Marie', dialogue=dialogue_one)
    $ msg ("This could have all been yours.", who=1)
    pause
    $ msg (None, who=1, pic="stage7_marie")
    pause
    $ msg ("I missed you, it is always more fun with an audience.", who=1)
    pause
    $ msg ("Sorry, there was something I needed to do.")
    pause
    $ msg ("Maybe next time I'll let you feed me instead.", who=1)
    pause
    $ msg ("Mmm, but I have got to go.", who=1)
    pause
    $ msg ("Seeing myself this big and bloated has me too turned on again.", who=1)
    pause
    $ hide_messenger()

    $ mariestage7phone = 0
    return

label Marie_BB_Extra:
    "You decide to pay the difference yourself."
    $ money -= 5
    image cafe_marie_extrafood = "/marie/[marie.stage]/cafe_extrafood.webp"
    scene cafe_marie_extrafood
    marie "Err, I don't think this is my order. Burger and a slice, remember?"
    "You look at the order, faking surprise."
    pc "Damn, you're right. How could I have made such a huge mistake? I'll just take this back."
    "She gives you a smile that lets you know she sees through your trick (it was hers first, after all!)"
    marie "No no, that's fine. I'll take it."
    pc "Alright, if you say so. Enjoy the food."
    marie "Oh, I will."
    image cafe_marie_struggle = "/marie/[marie.stage]/cafe_struggle.webp"
    scene cafe_marie_struggle
    "When you next look back at Marie's table, she's leaning back in her seat with a mixture of pain and bliss on her face."
    "She clearly doesn't mind being on the receiving end of her own trick."
    return

label Marie_BB_Prize:
    image cafe_marie_prize1 = "/marie/[marie.stage]/cafe_prize1.webp"
    scene cafe_marie_prize1
    "Creating a sizable feast, you approach Mare."
    image cafe_marie_prize2 = "/marie/[marie.stage]/cafe_prize2.webp"
    scene cafe_marie_prize2
    if marieprizefirsttime == 1:
        marie "Wait, what is this?"
        pc "Congratulations, you are the winner of this week's prize!"
        marie "Me, I didn't think I even put myself in the till."
        pc "I may have made some…alterations."
        marie "Oh really…"
        marie "I'm starting to think giving you this much power was a bad decision."
        pc "So you don't want an excuse to stuff yourself as full as possible?"
        marie "I didn't say that."
        image cafe_marie_prize3 = "/marie/[marie.stage]/cafe_prize3.webp"
        scene cafe_marie_prize3
        "Putting the food on the table, Marie takes in the amount of food she has been pushing on others for the first time."
        image cafe_marie_prize4 = "/marie/[marie.stage]/cafe_prize4.webp"
        scene cafe_marie_prize4
        "Selecting a slice of pizza, Marie begins her binge."
        "Eating quickly she eats her way through the large cheese pizzas first."
        "Rubbing her stomach with one hand she continues to eat."
        image cafe_marie_prize5 = "/marie/[marie.stage]/cafe_prize5.webp"
        scene cafe_marie_prize5
        "Before too long before she lets out a satisfied but defeated sigh, lounging back in the seat."
        image cafe_marie_prize6 = "/marie/[marie.stage]/cafe_prize6.webp"
        scene cafe_marie_prize6
        pc "How was the food?"
        marie "Do you even need to ask, ooh I'm so full."
        marie "But this was fun, maybe it wasn't a mistake to let you do this to me after all."
        pc "I'll pack the rest up so you can take it home with you."
        marie "It's a shame you can't package yourself up and come back with me."
        $ marieprizefirsttime = 0
    else:
        marie "Seriously, again?"
        pc "Congratulations…"
        marie "Yeah yeah, you just want to see me too big to move don't you?"
        pc "Is that a problem?"
        marie "For my waistline maybe."
        marie "But I guess I reap what I sow, isn't that right."
        pc "So it would seem, enjoy your food."
        marie "Thanks..."
        image cafe_marie_prize3 = "/marie/[marie.stage]/cafe_prize3.webp"
        scene cafe_marie_prize3
        "Putting the food on the table, Marie picks up the first piece of her giant meal."
        image cafe_marie_prize4 = "/marie/[marie.stage]/cafe_prize4.webp"
        scene cafe_marie_prize4
        "Eating quickly Marie eats her way through a good portion of the food."
        "Rubbing her stomach with one hand she continues to eat."
        image cafe_marie_prize5 = "/marie/[marie.stage]/cafe_prize5.webp"
        scene cafe_marie_prize5
        "Before too long before she lets out a satisfied but defeated sigh, lounging back in the seat."
        image cafe_marie_prize6 = "/marie/[marie.stage]/cafe_prize6.webp"
        scene cafe_marie_prize6
        pc "How was the food?"
        marie "Mmm, I hope you enjoyed my little show."
        marie "I'm just glad I limited it to one a week, otherwise you would have me stuffed all the time."
        pc "You say it like you don't also find that a hot idea."
        marie "True, now go grab some boxes so I can take this back home and away from you."
        pc "Don't want me to join you?"
        marie "Let's call it a punishment for using this idea against me."
    image cafe_marie_prize7 = "/marie/[marie.stage]/cafe_prize7.webp"
    scene cafe_marie_prize7
    "Returning a few minutes later, you hand Marie two large bags of food to take home with her."
    "Watching her leave. you return to the front counter and continue working."
    return
