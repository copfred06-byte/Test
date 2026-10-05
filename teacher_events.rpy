## TEACHER EVENTS
label Daisy_Cayenne_tutor_intro:
    #(NOTE: The following should occur after class once the player has reached Daisy stage 6, but before the introduction of the Followers of Heset at Daisy stage 8)
    #Image: Daisy looking at the player in the classroom.X
    image stage_6_event_extra1 = "/teacher/events/stage6/extra1.webp"
    scene stage_6_event_extra1
    "Just as you’re about to head out of the classroom, Daisy grabs you by the shoulder."
    image stage_6_event_extra2 = "/teacher/events/stage6/extra2.webp"
    scene stage_6_event_extra2
    teacher "Hold on just a moment. I have a special assignment for you."
    pc "What do you mean?"
    image stage_6_event_extra3 = "/teacher/events/stage6/extra3.webp"
    scene stage_6_event_extra3
    teacher "There’s an at home student that’s been having issues with her studies in this course. You seem like the perfect person to give her a tutoring session."
    pc "Why’s that? I don’t recall taking any tests or anything."
    image stage_6_event_extra4 = "/teacher/events/stage6/extra4.webp"
    scene stage_6_event_extra4
    "Rather than immediately reply, she smiles at you and hands over a piece of paper with an address written on it."
    teacher "Just trust me. I think you’re the perfect fit for this. Call me whenever you’re ready to take on the job."
    teacher "Do well enough and I’ll be sure to give you some “extra credit” for this lesson. Think it over."
    "Pocketing the piece of paper, you leave the classroom and head home."
    #(NOTE: From here the player should be given the option to visit Cayenne whenever he is in his room.)
    $ daisycayennetutorintro = 0
    return

label Boring_Teacher:
    #First day with the boring teacher
    scene university_looking_into_class
    play music "/music/university.ogg" if_changed
    "After wandering through the halls for a bit, you walk into what you think is the correct classroom."
    scene university_looking_into_class2
    "Swiveling your head around the room, you’re met with a collection of new faces."
    "That’s to be expected considering so much has changed since you've been away. After all, with how long you've been away from home, it’s almost like it’s a completely new town to you."
    image teacher_stage_1_event_1 = "/teacher/events/stage1/1.webp"
    scene teacher_stage_1_event_1
    pc "This is Nutritional Studies 101, right?"
    ms "Unfortunately, yes. I take it you’ve also been sentenced to die of boredom?"
    fs "I still say you're overreacting. We're getting a brand new teacher, so maybe she can spice things up."
    image teacher_stage_1_event_2 = "/teacher/events/stage1/2.webp"
    scene teacher_stage_1_event_2
    ms "Did you say she?"
    fs "Yeah. She seemed pretty shy when I ran into her in the hall."
    ms "Is she hot?"
    image teacher_stage_1_event_3 = "/teacher/events/stage1/3.webp"
    scene teacher_stage_1_event_3
    fs "Is that all you can think about?"
    ms "You can’t blame me for wanting to make class a little more interesting. So spit it out. Is she hot? Does she have a huge pair of-"
    "The muttering in the classroom comes to a stop as the teacher finally arrives."
    image uni_boring_teacher_arrive = "/teacher/events/stage1/arrive.webp"
    scene uni_boring_teacher_arrive
    ms "Great. Just great. She might as well be dressed like a nun."
    "The student lets out a grunt as he gets an elbow nudged into his chest."
    fs "Didn’t your mom ever teach you how to whisper?"
    teacher "Settle down, please, and get to your seats. You too, young man."
    "Following her instructions, you make your way to an empty seat near the front of the room."
    image uni_boring_teacher_greet = "/teacher/events/stage1/greet.webp"
    scene uni_boring_teacher_greet
    teacher "Good morning everyone. My name is Daisy Tanwen. You can call me Ms. Tanwen."
    s "Good morning, Ms. Tanwen."
    teacher "I’ll be teaching you Nutritional Science this semester."
    teacher "Though I’m new to teaching, I’m really excited to share with you everything I know about the exhilarating world of the human digestive system."
    image uni_boring_teacher_teaching1 = "/teacher/events/stage1/teaching1.webp"
    scene uni_boring_teacher_teaching1
    teacher "I can’t think of a better place to start than by describing the makeup of a saturated fat molecule."
    teacher "A fat molecule consists of two main components: glycerol and fatty acids. Glycerol is an alcohol with three carbons, five hydrogens and three hydroxyl groups."
    "You begin to hear whispers throughout the classroom."
    ms "I already want to leave."
    fs "Hush! She’s trying her best."
    image uni_boring_teacher_teaching2 = "/teacher/events/stage1/teaching2.webp"
    scene uni_boring_teacher_teaching2
    teacher "Fatty acids have a long chain of hydrocarbons with a carboxyl group attached and may have 4 to 36 carbons. However, most of them have between 12 and 18."
    fs "Although, her teaching style does have some…issues."
    image uni_boring_teacher_teaching3 = "/teacher/events/stage1/teaching3.webp"
    scene uni_boring_teacher_teaching3
    teacher "In a fat molecule, the fatty acids are attached to each of the three carbons of the glycerol molecule with an ester bond through the oxygen atom."
    "Though you try to stay awake, your eyelids grow heavier with each word that comes from her mouth."
    image uni_boring_teacher_teaching4 = "/teacher/events/stage1/teaching4.webp"
    scene uni_boring_teacher_teaching4
    teacher "During the ester bond formation, three molecules are released. Since fats consist of three fatty acids and a glycerol, they are also called triacylglycerols or triglycerides."
    teacher "While the…it’s actually…which is really interesting because…"
    "Though you try to remain vigilant, it’s only a matter of time before her lecture puts you to sleep."
    scene black with dissolve
    "Thirty minutes later, you’re awoken from your deep slumber by the ring of the bell."
    image uni_boring_teacher_teaching5 = "/teacher/events/stage1/teaching5.webp"
    scene uni_boring_teacher_teaching5 with dissolve
    teacher "Whoops! I got so carried away that I didn’t realize what time it was. That’s the end of the first lesson."
    teacher "If anyone wants to stay to ask any questions I’ll be around for as long as you like."
    "Though she tries to smile in the wake of yourself and the other students rousing from their naps, her mood diminishes with each person that slogs their way out of the door."
    "Eventually you and her are the only ones left in the room."
    image uni_boring_teacher_sitting1 = "/teacher/events/stage1/sitting1.webp"
    scene uni_boring_teacher_sitting1
    teacher "Go ahead, you can leave as well."
    "She lets out a deep sigh that puts her on the very edge of tears."
    image uni_boring_teacher_sitting2 = "/teacher/events/stage1/sitting2.webp"
    scene uni_boring_teacher_sitting2
    teacher "I won’t make you suffer any longer."
    pc "Hey don’t say that. I think you have potential."
    image uni_boring_teacher_sitting3 = "/teacher/events/stage1/sitting3.webp"
    scene uni_boring_teacher_sitting3
    teacher "There’s no need to lie to try and protect my feelings. I could see you sleeping like the others."
    pc "Sure your delivery is a little dry, but you obviously know what you’re talking about. You just need to find some way to spice up your lectures a bit."
    image uni_boring_teacher_sitting4 = "/teacher/events/stage1/sitting4.webp"
    scene uni_boring_teacher_sitting4
    "She wipes away a tear from her cheek."
    teacher "What do you mean?"
    pc "I don’t have anything specific in mind, but maybe it would help to make the class more interactive?"
    pc "Maybe find some way to show rather than just tell the effects of nutrition or something like that."
    image uni_boring_teacher_sitting5 = "/teacher/events/stage1/sitting5.webp"
    scene uni_boring_teacher_sitting5
    "Lowering her head, she scratches her chin in thought."
    teacher "I think I get what you’re saying."
    image uni_boring_teacher_sitting6 = "/teacher/events/stage1/sitting6.webp"
    scene uni_boring_teacher_sitting6
    "Tilting her head back up, she smiles."
    teacher "Thanks a lot for the advice. I’ll reassess my lesson plan over the weekend. You can run along to your next class."
    pc "Oh this was my only one for the day."
    image uni_boring_teacher_sitting7 = "/teacher/events/stage1/sitting7.webp"
    scene uni_boring_teacher_sitting7
    "Ms. Tanwen gives you a confused look."
    teacher "What do you mean?"
    pc "I have an unusual deal with the university. Free tuition, board, and food, but I have to take this one class."
    pc "I know it’s strange, but I’m not complaining about an easy ride to a university diploma."
    teacher "Then I suppose you wouldn’t mind helping me out with further lesson plan changes?"
    teacher "Or at the very least, continuing to sit in the front of class to provide me feedback?"
    pc "Sure thing!"
    image uni_boring_teacher_sitting8 = "/teacher/events/stage1/sitting8.webp"
    scene uni_boring_teacher_sitting8
    teacher "Thanks a lot. You’re a lifesaver, um, what was your name again?"
    pc "Oh, it’s [playername]."
    image uni_boring_teacher_sitting9 = "/teacher/events/stage1/sitting9.webp"
    scene uni_boring_teacher_sitting9
    "Ms. Tanwen’s eyes go wide as she looks up and down your body."
    teacher "That’s…interesting."
    pc "What do you mean?"
    image uni_boring_teacher_sitting10 = "/teacher/events/stage1/sitting10.webp"
    scene uni_boring_teacher_sitting10
    teacher "Er, nothing. Just, um, enjoy your weekend."
    pc "Okay? You too."
    stop music fadeout 1.0
    image uni_leave_katrine = "/katrine/events/stage1/uni_leave_katrine.webp"
    scene uni_leave_katrine
    "On your way back from the university you notice a girl working out. Rather than approach, you end up speaking to yourself."
    pc "Man she’s hot. Wish I had the charisma to actually talk to her."
    pc "Or maybe the brains to have a conversation. At the very least, a body to keep up with her would be nice."
    scene player_room
    "After returning home, you end up falling into your usual vices and waste the entire, three day weekend playing video games."
    "You decide to play some Carl on Duty."
    pc "I keep getting destroyed by someone that goes by FTVLuxLeanne."
    pc "I wonder if they have a stream."
    pc "Oh, it's a good looking lady!"
    pc "Dammit, she just went offline. I’ll have to try to catch her stream another time."
    $ streamergirlunlock = 1
    $ day += 1
    jump start

label Sexy_Teacher_Tuesday:
    #Second day with the sexy teacher talking about breasts
    image teacher_stage_1_event_4 = "/teacher/events/stage1/4.webp"
    scene teacher_stage_1_event_4
    play music "/music/university.ogg" if_changed
    "You walk into class several minutes late on Tuesday morning, to find only two students sitting at their desks."
    image teacher_stage_1_event_5 = "/teacher/events/stage1/5.webp"
    scene teacher_stage_1_event_5
    pc "Where’s everyone else?"
    fs "They bailed to go eat at a diner called Bunny Bites instead of sitting through another one of Ms. Tanwen’s lectures."
    #ms "Yeah, and I would be joining them if a certain SOMEONE didn’t force me to come."
    #fs "It’s the least you can do after the comments you made last time."
    scene university_sitdown_front
    "Taking your seat at the front of the class, you get ready to console Ms. Tanwen after the disappointing turn out."
    image uni_sexy_teacher_arrive = "/teacher/[teacher.stage]/0/arrive.webp"
    scene uni_sexy_teacher_arrive
    "Your jaw drops as you behold a new and improved Daisy strolling into the room like a super model."
    #ms "Jackpot!"
    fs "What in the world?"
    "Getting a good look at her more risqué appearance as she takes her spot at the front of the room, you can’t help feeling that she might have taken your advice a little too far."
    image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
    scene uni_sexy_teacher_greet
    teacher "Good morning, students. I see we have a small group today. That’s alright. That means you lucky few will be the first to sample my new lesson plan."
    call rngteachingscene from _call_rngteachingscene_36
    teacher "Considering that this semester focuses heavily on fats, calories, and sugars, I’ve decided to show how these affect the human body."
    call rngteachingscene from _call_rngteachingscene_37
    teacher "The best way to do this will be to expose my body to said fat, calories and sugar through the help of you, my students."
    fs "Wait, are you really…?"
    teacher "That’s right. Over the course of the semester, I intend to put on as much weight as possible."
    call rngteachingscene from _call_rngteachingscene_38
    teacher "This way I can give an adequate demonstration of how nutrition can change certain aspects of the human body."
    teacher "To better illustrate my point, I’ll be doing weekly weigh ins every Monday."
    call rngteachingscene from _call_rngteachingscene_39
    teacher "For the sake of speeding up this process, I’ll be accepting food donations starting this Friday."
    teacher "But that’s for much later, for now let’s give you all a proper starting point."
    $ strip += 1
    "She begins to strip in front of the class."
    teacher "Let’s start things off nice and slow."
    call rngteachingscene from _call_rngteachingscene_40
    fs "Wait, is she really stripping? Is that allowed?"
    #ms "Who cares? It’s hot as hell."
    $ strip += 1
    teacher "I expect everyone to pay close attention."
    call rngteachingscene from _call_rngteachingscene_41
    teacher "Breasts are internally made up of fat tissue and connective ducts that deliver milk."
    $ strip += 1
    teacher "Considering this, we can conclude that having a higher than normal nutritional intake would increase their size."
    call rngteachingscene from _call_rngteachingscene_42
    "Your mind goes blank as you attempt to process the sight of a teacher stripping in front of her students."
    "Rather than let logic dictate your thoughts, your eyes focus to gaze at her bosom."
    call rngteachingscene from _call_rngteachingscene_43
    teacher "There are other factors that can increase breast size as well. For example, pregnancy and hormones."
    call rngteachingscene from _call_rngteachingscene_44
    teacher "However, we'll mostly be focusing on nutritional factors. There are certain mixtures that can be used to increase the size and weight of breasts."
    call rngteachingscene from _call_rngteachingscene_45
    teacher "To start, we’ll be measuring my bosom so we can use the data throughout the semester."
    image uni_sexy_teacher_measure_breasts1 = "/teacher/[teacher.stage]/3/measure_breasts1.webp"
    scene uni_sexy_teacher_measure_breasts1
    if persistent.imperial:
        $ imperialbreastweight = (teacher.breast_weight * 2.2)
        teacher "It looks like my breasts weigh [imperialbreastweight:.02f]lbs. Which is the average weight for a woman of my age and size."
    else:
        teacher "It looks like my breasts weigh [teacher.breast_weight:.02f]kg. Which is the average weight for a woman of my age and size."
    image uni_sexy_teacher_measure_breasts2 = "/teacher/[teacher.stage]/3/measure_breasts2.webp"
    scene uni_sexy_teacher_measure_breasts2
    if persistent.imperial:
        teacher "My cup size is [teacher.breast_cup], and my bust measures [teacher.breast_size:.02f] inches. I may not have the largest of breasts, but that may change as these lessons continue."
    else:
        $ metricbreast_size = (teacher.breast_size * 2.54)
        teacher "My cup size is [teacher.breast_cup], and my bust measures [metricbreast_size:.02f]cm. I may not have the largest of breasts, but that may change as these lessons continue."
    $ strip = 2
    call rngteachingscene from _call_rngteachingscene_46
    teacher "I believe that will be all for today. Tomorrow we’ll move onto talking about the glutes, better known as the butt cheeks. I hope to see you all then."
    #ms "You can bet on it!"
    image uni_sexy_teacher_after_class = "/teacher/events/stage1/after_class.webp"
    scene uni_sexy_teacher_after_class
    "As the other two students take their leave, you make your way towards Daisy."
    teacher "So, what did you think of my revised teaching method?"
    pc "It definitely got my attention. But is this even allowed? I don’t want you getting fired over this. Especially since it came from my advice."
    "She lets out a giggle."
    teacher "Have no fear. I had this lesson plan approved by the dean. This university is rather progressive, so it lets the teacher experiment with more radical teaching methods."
    pc "Well it seems to work. At the very least, it’s a hell of a motivator for me and the rest of class to pay attention."
    teacher "That’s what I like to hear. Just make sure you keep doing your best in my class and I might have a reward for you."
    image uni_sexy_teacher_after_class_nopanties = "/teacher/events/stage1/after_class_nopanties.webp"
    scene uni_sexy_teacher_after_class_nopanties
    window hide
    pause
    "Shuffling her legs around, she moves just slow enough to ensure you are very aware of the fact that she isn’t wearing any panties."
    teacher "As you can see, there’s a reason I only stuck to talking about my breasts today. Think of this as a special treat for helping me out."
    pc "Er, no problem, Ms. Tanwen."
    teacher "No need to be so formal. You can just call me Daisy when it’s just the two of us."
    pc "Okay…Daisy. I’ll do my best."
    image uni_sexy_teacher_after_class = "/teacher/events/stage1/after_class.webp"
    scene uni_sexy_teacher_after_class
    teacher "That’s good to hear. See you tomorrow then?"
    pc "Of course."
    stop music fadeout 1.0
    scene university_leave
    "You leave class and once more waste the day away playing video games."

    $ strip = 0
    $ day += 1
    jump start

label Sexy_Teacher_Wednesday:
    #Third day with the sexy teacher talking about ass
    scene university_looking_into_class
    play music "/music/university.ogg" if_changed
    "Arriving for class, you can immediately sense a drastic change in the atmosphere."
    image teacher_stage_1_event_6 = "/teacher/events/stage1/6.webp"
    scene teacher_stage_1_event_6
    pc "Guess word spread pretty fast."
    ms "You bet your ass it did."
    fs "I’m just here for the educational portion. It will be, um, enlightening to see a woman who’s so confident about her body go about her lessons."
    fs "I just hope she wasn’t serious about putting on weight. It could cause her long term problems."
    pc "I didn’t really think about that. She probably won’t go too far just for a class, right?"
    ms "If it means getting to see more of her skin, you don’t see me complaining."
    fs "Shhhh, she’s here."
    image uni_sexy_teacher_arrive = "/teacher/[teacher.stage]/0/arrive.webp"
    scene uni_sexy_teacher_arrive
    ms "Told you she was hot."
    "Murmurs are heard throughout the room agreeing with the male student’s comment."
    image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
    scene uni_sexy_teacher_greet
    teacher "Good morning, students."
    s "Good morning, Ms. Tanwen."
    teacher "I’m happy to see such an improved turn out. You can find notes for yesterday’s lesson plan, along with some ‘reference’ pictures in the group e-mail I sent."
    teacher "For now though, let’s pick up where I left off."
    call rngteachingscene from _call_rngteachingscene_47
    teacher "Today we will be talking about another part of the body greatly affected by how much you eat and drink."
    $ strip += 1
    teacher "As we established previously, when a woman has greater than normal nutritional intake it can enlarge her breasts."
    $ strip += 1
    pause
    call rngteachingscene from _call_rngteachingscene_48
    teacher "But these are only one part of the body that can change through nutrition."
    teacher "The glutes, commonly known as the buttocks, are made up of three muscles."
    call rngteachingscene from _call_rngteachingscene_49
    teacher "The gluteus maximus, the gluteus medius, and the gluteus minimus."
    teacher "If you have a lean and active body similar to mine, these muscles make up the bulk of the shape of your butt."
    $ strip += 1
    pause
    call rngteachingscene from _call_rngteachingscene_50
    teacher "However, if you have excess nutrition the shape of your buttocks will be largely dictated by the panniculus adiposus."
    call rngteachingscene from _call_rngteachingscene_51
    teacher "This fatty layer of your butt cheeks is very well developed in comparison to the rest of the human body."
    $ strip += 1
    pause
    call rngteachingscene from _call_rngteachingscene_52
    teacher "Another big factor in determining the size of the butt is genes and hormones."
    teacher "For example, women with genes that support a high concentration of fat in their rear are sometimes referred to as pear shaped."
    image uni_sexy_teacher_showoffass1 = "/teacher/[teacher.stage]/4/showoffass1.webp"
    scene uni_sexy_teacher_showoffass1
    teacher "Now let’s take a closer look at the butt."
    ms "Hell yes!"
    fs "I suppose it’s fine as long as it gets the point across."
    teacher "Human females tend to have proportionally wider and thicker backsides."
    image uni_sexy_teacher_showoffass2 = "/teacher/[teacher.stage]/4/showoffass2.webp"
    scene uni_sexy_teacher_showoffass2
    teacher "This is due to the fact that women have higher subcutaneous fat and proportionally wider hips."
    teacher "For this class, I want you all to see the the effect subcutaneous fat has on the shape and size of the butt."
    image uni_sexy_teacher_showoffass3 = "/teacher/[teacher.stage]/4/showoffass3.webp"
    scene uni_sexy_teacher_showoffass3
    teacher "How do we gain more subcutaneous fat in the buttocks?"
    teacher "By having a higher than normal nutritional intake of course."
    image uni_sexy_teacher_measure_ass1 = "/teacher/[teacher.stage]/4/measure_ass1.webp"
    scene uni_sexy_teacher_measure_ass1
    teacher "Let’s record a baseline measurement to start."
    if persistent.imperial:
        teacher "Right now, my butt measures [teacher.ass_size:.02f] inches. That’s around the average size."
    else:
        $ metricass_size = (teacher.ass_size * 2.54)
        teacher "Right now, my butt measures [metricass_size:.02f] cm. That’s around the average size."
    call rngteachingscene from _call_rngteachingscene_53
    teacher "That will be all for today, but I would like to give you all some homework."
    teacher "I want you to go out and find food and drinks that you think will have the largest effect on the amount of subcutaneous fat I carry."
    call rngteachingscene from _call_rngteachingscene_54
    teacher "I will evaluate the products you bring me and then elaborate on their effects."
    teacher "To be honest, I’m a little excited to see what you come up with."
    call rngshowoffscene from _call_rngshowoffscene
    teacher "Great work today everyone. I’ll see you again tomorrow."
    "You leave class, getting slowed down by the students stopping to ogle Daisy’s body."
    stop music fadeout 1.0
    scene university_leave
    "Thinking about what you should bring, you recall the Bunny Bites place mentioned the previous day."
    "After asking a few of your classmates for directions, you go to the diner."
    scene restaurant_lisa
    play music "/music/bunny_bites.ogg" if_changed
    pc "Wow, it’s pretty packed in here. Hope that means the food is good."
    image amber_workattire_counter = "/amber/[amber.stage]/workattire_counter.webp"
    scene amber_workattire_counter
    amber "Welcome to Bunny Bites! My name is Amber. Anything I can help you with?"
    "Your eyes look over the menu until you find something that would be perfect for the assignment."
    pc "Can I order some chicken nuggets for take out tomorrow morning?"
    amber "An excellent choice. We make the best nuggets in town. How many do you want?"
    pc "I guess give me the largest serving you have."
    amber "That’ll be the twenty piece meal for $10."
    pc "Thank you, see you tomorrow morning."
    $ money -= 10
    scene player_room
    stop music fadeout 1.0
    "You pay for the meal in advance and head home."
    $ strip = 0
    $ day += 1
    jump start

label Sexy_Teacher_Thursday:
    #Fourth day with the sexy teacher talking about the stomach
    scene university_looking_into_class
    play music "/music/university.ogg" if_changed
    "As you arrive to class, you ponder what everyone else brought."
    image teacher_stage_1_event_7 = "/teacher/events/stage1/7.webp"
    scene teacher_stage_1_event_7
    fs "What did you bring for Ms. Tanwen?"
    pc "Chicken nuggets. What about you?"
    fs "Donuts! Got it from this bakery called The Sugar Shop."
    image teacher_stage_1_event_8 = "/teacher/events/stage1/8.webp"
    scene teacher_stage_1_event_8
    ms "A burger of course. Nothing beats good greasy meat."
    image uni_sexy_teacher_arrive = "/teacher/[teacher.stage]/0/arrive.webp"
    scene uni_sexy_teacher_arrive
    "Daisy enters the classroom, and you take the seat at the front."
    image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
    scene uni_sexy_teacher_greet
    teacher "Good morning, students. I’m quite hungry today, so I hope you all brought something tasty."
    call rngteachingscene from _call_rngteachingscene_55
    $ strip += 1
    teacher "Before you hand in your homework, I want to talk about the belly."
    teacher "There’s a lot about this part of the body in particular, so I’ll only be explaining part of it today."
    $ strip += 1
    call rngteachingscene from _call_rngteachingscene_56
    teacher "Today’s focus is going to be on the stomach. It is a muscular, hollow organ located in the gastrointestinal tract."
    call rngteachingscene from _call_rngteachingscene_57
    teacher "The stomach is the second phase of the digestive system."
    teacher "After the food is properly chewed, the stomach performs a chemical breakdown by means of enzymes and hydrochloric acid."
    call rngteachingscene from _call_rngteachingscene_58
    teacher "Because it is a distensible organ, it normally expands to hold about one liter of food."
    teacher "But with proper training and large intakes of nutrition, it can stretch to accommodate much higher volumes."
    $ strip += 1
    pause
    call rngteachingscene from _call_rngteachingscene_59
    teacher "Today I will demonstrate how much my stomach can expand without too much discomfort."
    teacher "Please turn in your assignments and place them on my desk."
    "One by one, each of the students walks up to hand Daisy their bundles of food."
    image uni_sexy_teacher_food_teaching1 = "/teacher/[teacher.stage]/[strip]/food_teaching1.webp"
    scene uni_sexy_teacher_food_teaching1
    teacher "A very nice haul. Let’s see, how about we start with this box of donuts?"
    image uni_sexy_teacher_food_teaching_donut = "/teacher/[teacher.stage]/[strip]/food_teaching_donut.webp"
    scene uni_sexy_teacher_food_teaching_donut
    teacher "Donuts often contain high amounts of sugar, refined flour, and fat."
    teacher "As to be expected, they are typically high in calories as well. One glazed donut packs over 300 calories."
    image uni_sexy_teacher_food_eating_donut = "/teacher/[teacher.stage]/[strip]/food_eating_donut.webp"
    scene uni_sexy_teacher_food_eating_donut
    teacher "They’re also very tasty."
    teacher "Unless you want to gain weight like me, you shouldn’t eat more than one per day. Next up we have…oh! A burger."
    image uni_sexy_teacher_food_teaching_burger = "/teacher/[teacher.stage]/[strip]/food_teaching_burger.webp"
    scene uni_sexy_teacher_food_teaching_burger
    teacher "Burgers, like most fast food, have loads of calories, fat, sodium and added sugar. In most cases it is also highly processed."
    image uni_sexy_teacher_food_eating_burger = "/teacher/[teacher.stage]/[strip]/food_eating_burger.webp"
    scene uni_sexy_teacher_food_eating_burger
    teacher "Wow! This tastes great."
    image uni_sexy_teacher_food_teaching2 = "/teacher/[teacher.stage]/[strip]/food_teaching2.webp"
    scene uni_sexy_teacher_food_teaching2
    teacher "One burger usually suffices for a single adult’s dinner. However, I don’t intend to stop here. What else do we have? Oh, I see some delicious chicken nuggets."
    image uni_sexy_teacher_food_teaching_nuggets = "/teacher/[teacher.stage]/[strip]/food_teaching_nuggets.webp"
    scene uni_sexy_teacher_food_teaching_nuggets
    teacher "Chicken nuggets are often very high in carbs and fat. In normal circumstances, you should only have a few, but I’ll be eating the entire box."
    image uni_sexy_teacher_food_eating_nuggets = "/teacher/[teacher.stage]/[strip]/food_eating_nuggets.webp"
    scene uni_sexy_teacher_food_eating_nuggets
    teacher "Mmm, these might be the best nuggets I’ve had in my life. Ah, if you’ll excuse me for a moment."
    teacher "I need to free up a little room."
    $ strip += 1
    image uni_sexy_teacher_stuffed_half = "/teacher/[teacher.stage]/[strip]/stuffed_half.webp"
    scene uni_sexy_teacher_stuffed_half
    "Finishing off her meal, she unbuttons her shirt to reveal her mostly bare torso to the class."
    teacher "Ahhhh, much better. As you can see, the more food the stomach takes in the further the belly expands to make room."
    teacher "One very convenient thing is that the signal the stomach sends to the brain to stop eating takes about twenty minutes to register."
    image uni_sexy_teacher_food_eating_nuggets = "/teacher/[teacher.stage]/[strip]/food_eating_nuggets.webp"
    scene uni_sexy_teacher_food_eating_nuggets
    teacher "Let’s finish these up."
    image uni_sexy_teacher_food_teaching1_half_stuffed = "/teacher/[teacher.stage]/[strip]/food_teaching2.webp"
    scene uni_sexy_teacher_food_teaching1_half_stuffed
    teacher "I’ve basically eaten twice as much as an average human should eat for a meal, But it would be a shame to let the rest of this go to waste."
    teacher "Let’s see what else we have. Oh look here, we have some fries."
    image uni_sexy_teacher_food_teaching_fries = "/teacher/1/4/food_teaching_fries.webp"
    scene uni_sexy_teacher_food_teaching_fries
    teacher "French fries can be extremely high in fat, thanks to their deep-fried treatment. While they are made from potatoes, they aren’t generally healthy."
    teacher "Seasoning and sky-high levels of salt sometimes make a single serving take up more than a third of the recommended daily intake."
    image uni_sexy_teacher_food_eating_fries = "/teacher/[teacher.stage]/[strip]/food_eating_fries.webp"
    scene uni_sexy_teacher_food_eating_fries
    teacher "While these may wreak havoc on my waistline, they’re also delicious."
    image uni_sexy_teacher_food_eating_donut = "/teacher/[teacher.stage]/[strip]/food_eating_donut.webp"
    scene uni_sexy_teacher_food_eating_donut
    teacher "Let me go back to finish the remaining donuts."
    "She effortlessly shoves each sugary pastry down her throat in defiance of her already sizable meal."
    image uni_sexy_teacher_stuffed = "/teacher/[teacher.stage]/[strip]/stuffed.webp"
    scene uni_sexy_teacher_stuffed
    teacher "Phew, didn’t think I’d make it, but it was well worth it. As you can see, I’m pretty stuffed."
    teacher "My stomach is stretched to its limits, and I can certainly feel the pressure. The next step will be to wait for this food to digest, then repeat the process."
    teacher "Since tomorrow is Friday, I would like everyone to bring in more food. I’ll be sure to ingest anything you give me over the weekend so my weight gain can progress at a rapid pace."
    teacher "That’s all for today. I’ll see you tomorrow."
    "Upon leaving class, you start to think about what to bring next."
    "Looking back at the box of donuts, you decide to seek out the bakery in the hopes of finding something super sweet to give to Daisy."
    stop music fadeout 1.0
    scene city
    "You head downtown in search of The Sugar Shop bakery."
    "It doesn’t take you long to find the charming corner shop with the directions given to you by your classmates."
    image bonnie_sweetshop = "/bonnie/[bonnie.stage]/sweetshop.webp"
    scene bonnie_sweetshop
    "Stepping inside, you can’t help yourself from taking a deep whiff of the heavenly aromas drifting through the store."
    pc "Now I know why Daisy went back for seconds. This place is amazing."
    bonnie "Glad to hear you say that. Hi there, my name is Bonnie. How can I help you?"
    pc "This may be a bit of a weird request, but I would like to buy the most fattening sweets you have."
    bonnie "Strange, but I won’t question it. I think I have just the thing you’re looking for. It’s a meal package containing an assortment of our most sugary sweets."
    pc "That sounds perfect. How much does it cost?"
    bonnie "It’s $10 per package. How many can I get you?"
    pc "Just one for now."
    $ money -= 10
    $ foodheld += 1
    scene player_room
    "Exchanging money for the bundle of sugary goodness, you head home for the day."
    $ strip = 0
    $ day += 1
    jump start

label First_Friday:
    #First Friday where the teacher teaches about belly fat
    scene university_looking_into_class
    play music "/music/university.ogg" if_changed
    "Carefully holding the bundle of sweets, you walk into the classroom."
    image teacher_stage_1_event_9 = "/teacher/events/stage1/9.webp"
    scene teacher_stage_1_event_9
    pc "Good morning."
    fs "Morning. I see you found The Sugar Shop."
    pc "Yeah, thanks for the directions. This was exactly what I was looking for."
    fs "No problem. Always glad to help out small businesses."
    image uni_sexy_teacher_arrive = "/teacher/[teacher.stage]/0/arrive.webp"
    scene uni_sexy_teacher_arrive
    "Daisy arrives and you take your usual spot."
    image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
    scene uni_sexy_teacher_greet
    teacher "Good morning, students."
    s "Good morning, Ms. Tanwen."
    call rngteachingscene from _call_rngteachingscene_60
    $ foodheld -= 1
    teacher "I see that you brought me a lot of goodies for the weekend. Considering the work you put in, let me give you a reward."
    $ strip += 1
    window hide
    pause
    $ strip += 1
    pause
    $ strip += 1
    teacher "When we return Monday, I’ll report on my body’s weight progress and calorie intake. For now, let’s resume where I left off yesterday regarding the belly."
    call rngteachingscene from _call_rngteachingscene_61
    teacher "Previously we talked about the stomach, however that’s not the only part of the abdomen."
    $ strip += 1
    teacher "The abdomen is full of vital organs, but I want to talk about the layer of fat inside and surrounding it."
    call rngteachingscene from _call_rngteachingscene_62
    teacher "There are two types of fat in the waist area: visceral fat and subcutaneous fat."
    teacher "Visceral fat, also known as organ fat, is fat that concentrates around the organs."
    call rngteachingscene from _call_rngteachingscene_63
    teacher "This type of fat is often found in males and is quite poor for your health."
    teacher "Subcutaneous fat on the other hand is more common in women and isn't as bad for you. Some researchers even say it's beneficial to your body."
    call rngteachingscene from _call_rngteachingscene_64
    teacher "Subcutaneous fat is found right underneath the skin, mostly around the waistline and butt cheeks of women."
    teacher "We will be concentrating on increasing my amount of subcutaneous fat."
    call rngteachingscene from _call_rngteachingscene_65
    teacher "We can accurately gauge the amount of fat deposited in the abdomen by measuring the waist and overall weight of the body."
    teacher "That being said, it’s time for a weigh in."
    image uni_sexy_teacher_measure_belly1 = "/teacher/[teacher.stage]/4/measure_belly1.webp"
    scene uni_sexy_teacher_measure_belly1
    if persistent.imperial:
        $ imperialweight = (teacher.weight * 2.2)
        teacher "Right now I weigh [imperialweight:.02f] lbs."
    else:
        teacher "Right now I weigh [teacher.weight:.02f] kg."
    image uni_sexy_teacher_measure_belly2 = "/teacher/[teacher.stage]/4/measure_belly2.webp"
    scene uni_sexy_teacher_measure_belly2
    if persistent.imperial:
        teacher "And my waistline measures [teacher.waist_size:.02f] inches."
    else:
        $ metricwaist_size = (teacher.waist_size * 2.54)
        teacher "And my waistline measures [metricwaist_size:.02f] cm."
    call rngteachingscene from _call_rngteachingscene_66
    teacher "Make sure you’re keeping a record of my measurements throughout the year."
    show screen gameUI
    "Daisy's measurements are now available in the stats menu."
    "You can access the stats menu by clicking the button in the upper right corner."
    call rngshowoffscene from _call_rngshowoffscene_2
    teacher "Keep up the great work! Next week we’ll be doing some more measuring and teaching."
    call rngshowoffscene from _call_rngshowoffscene_3
    teacher "Towards the end of the first quarter, I plan to bring in two subjects with different body types so we can experience how weight distribution can differ between people."
    teacher "I wish you all a great weekend. I’m looking forward to seeing you all bright and early Monday morning."
    stop music fadeout 1.0
    scene university_leave
    pc "Finishing up with class, you head home to enjoy the weekend, somewhat confident in Daisy’s new lesson plan."

    $ strip = 0
    $ day += 1
    jump start

label Teacher_Stage_2_Event:
    image stage_2_event_arrive = "/teacher/events/stage2/arrive.webp"
    scene stage_2_event_arrive
    play music "/music/university.ogg" if_changed
    "You come into class and are astonished to see Daisy saunter in wearing an evening gown."
    ms "Looking good, teach!"
    fs "I have to admit, it’s pretty stunning."
    image stage_2_event_greet = "/teacher/events/stage2/greet.webp"
    scene stage_2_event_greet
    teacher "Good morning, students."
    s "Good morning, Ms. Tanwen."
    image stage_2_event_1 = "/teacher/events/stage2/1.webp"
    scene stage_2_event_1
    teacher "As you can probably tell, I’m a little more dressed up for today’s class."
    image stage_2_event_1_1 = "/teacher/events/stage2/1_1.webp"
    scene stage_2_event_1_1
    teacher "I’m wearing this dress in preparation for tonight’s staff party celebrating the university’s 20th anniversary."
    image stage_2_event_2 = "/teacher/events/stage2/2.webp"
    scene stage_2_event_2
    teacher "Since the party will start as soon as classes are over, I figured it would be easier to wear the dress rather than go home and change."
    image stage_2_event_3 = "/teacher/events/stage2/3.webp"
    scene stage_2_event_3
    teacher "I may have overheard a bit when I came in but let me make sure. What do you all think of my dress?"
    image stage_2_event_3_1 = "/teacher/events/stage2/3_1.webp"
    scene stage_2_event_3_1
    "The classroom erupts in a shower of praise and compliments both for her dress and her body."
    image stage_2_event_3_2 = "/teacher/events/stage2/3_2.webp"
    scene stage_2_event_3_2
    "Through this collection of adoration, you can’t help noticing how her gaze focuses on you to see your reaction."
    image stage_2_event_4 = "/teacher/events/stage2/4.webp"
    scene stage_2_event_4
    teacher "Thank you very much, class. I'm glad to hear it considering how difficult it was to put the outfit on this morning."
    image stage_2_event_5 = "/teacher/events/stage2/5.webp"
    scene stage_2_event_5
    teacher "My wardrobe is already starting to struggle with what little weight I’ve put on."
    image stage_2_event_5_1 = "/teacher/events/stage2/5_1.webp"
    scene stage_2_event_5_1
    teacher "This might be the last time I get to wear this dress."
    image stage_2_event_laugh = "/teacher/events/stage2/laugh.webp"
    scene stage_2_event_laugh
    teacher "As long as my amazing students keep up their lessons that is."
    image stage_2_event_6 = "/teacher/events/stage2/6.webp"
    scene stage_2_event_6
    teacher "Speaking of which, let’s move on to today’s lesson: mental support."
    image stage_2_event_7 = "/teacher/events/stage2/7.webp"
    scene stage_2_event_7
    teacher "Mental support for gaining weight isn’t too common. In most modern cultures, actively gaining weight or even being fat is frowned upon."
    image stage_2_event_7_1 = "/teacher/events/stage2/7_1.webp"
    scene stage_2_event_7_1
    teacher "As you’re probably aware through never ending advertisements and your own personal lives, society is mostly positive when it comes to people actively trying to lose weight."
    image stage_2_event_8 = "/teacher/events/stage2/8.webp"
    scene stage_2_event_8
    teacher "Physical health concerns are at the forefront of this idea. However, with certain diets and body types, gaining weight isn’t necessarily bad."
    image stage_2_event_8_1 = "/teacher/events/stage2/8_1.webp"
    scene stage_2_event_8_1
    teacher "With that in mind, I do hope you will all provide the mental support needed as I continue to gain for this class."
    image stage_2_event_9 = "/teacher/events/stage2/9.webp"
    scene stage_2_event_9
    teacher "That will be all for now. I hope you all have a great rest of the day."
    "The other students gradually file out - most of them lingering in the doorway to catch a glimpse of Daisy before they leave."
    "Just as you’re about to stand up, she comes up to you."
    image stage_2_event_10 = "/teacher/events/stage2/10.webp"
    scene stage_2_event_10
    teacher "No, I need you stay after class for a bit."
    pc "Did I do something wrong?"
    teacher "Not exactly. There’s just something I want to talk to you about concerning your homework."
    image stage_2_event_afterclass2 = "/teacher/events/stage2/afterclass2.webp"
    scene stage_2_event_afterclass2
    "You remain at the desk until everyone has left. With only Daisy and yourself in the room, she quickly closes the door and locks it."
    image stage_2_event_afterclass1 = "/teacher/events/stage2/afterclass1.webp"
    scene stage_2_event_afterclass1
    "Sitting on her desk, she spreads her legs to reveal that she has once more foregone underwear to leave her private area visible beneath her skirt."
    teacher "Now it’s just the two of us."
    teacher "Since we have some privacy, I would like to give you a chance for some extra credit."
    pc "What do you mean?"
    image stage_2_event_afterclass3 = "/teacher/events/stage2/afterclass3.webp"
    scene stage_2_event_afterclass3
    teacher "I want to give you a better look at my body’s progression."
    image stage_2_event_afterclass3_1 = "/teacher/events/stage2/afterclass3_1.webp"
    scene stage_2_event_afterclass3_1
    teacher "Do you like the sight of my bare breasts?"
    pc "They are pretty impressive."
    image stage_2_event_afterclass4 = "/teacher/events/stage2/afterclass4.webp"
    scene stage_2_event_afterclass4
    teacher "And what about my ass?"
    image stage_2_event_afterclass4_1 = "/teacher/events/stage2/afterclass4_1.webp"
    scene stage_2_event_afterclass4_1
    pause
    image stage_2_event_afterclass4_2 = "/teacher/events/stage2/afterclass4_2.webp"
    scene stage_2_event_afterclass4_2
    pause
    pc "Simply amazing. What little weight you’ve gained so far has really enhanced your curves. I can’t wait to see how you look when you get even bigger."
    image stage_2_event_afterclass5 = "/teacher/events/stage2/afterclass5.webp"
    scene stage_2_event_afterclass5
    teacher "Mmmmmppphhh yes."
    image stage_2_event_afterclass5_1 = "/teacher/events/stage2/afterclass5_1.webp"
    scene stage_2_event_afterclass5_1
    pc "Are you okay?"
    image stage_2_event_afterclass5_2 = "/teacher/events/stage2/afterclass5_2.webp"
    scene stage_2_event_afterclass5_2
    teacher "More than okay. The mere act of getting to show off my body makes me so horny."
    image stage_2_event_afterclass6 = "/teacher/events/stage2/afterclass6.webp"
    scene stage_2_event_afterclass6
    teacher "Especially when you say you want to see me get fatter."
    image stage_2_event_afterclass6_1 = "/teacher/events/stage2/afterclass6_1.webp"
    scene stage_2_event_afterclass6_1
    teacher "It almost pushes me to my limits. Though I would love to show you exactly what I mean, that will have to wait for another time."
    image stage_2_event_end = "/teacher/events/stage2/eventend.webp"
    scene stage_2_event_end
    "Just as quickly as she removed her clothes, she slips them back on and acts as if nothing had happened."
    teacher "Let’s keep this our little secret for now. See you tomorrow."
    pc "Yeah, see you then."
    stop music fadeout 1.0
    scene university_leave
    "Upon leaving class, your head is filled with numerous questions, mostly pertaining to whether or not Daisy’s behavior will get her fired."
    "In the end you decide to head home and play games to ease your mind."

    $ teacherstage2event = 0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        #Unlocks Daisy Undress in the stats page.
        $ renpy.notify("Daisy Undress option unlocked in stats screen.")
        window hide
        pause
        jump freetime
    return

label Teacher_Stage_3_Event:
    image stage_3_event_1 = "/teacher/events/stage3/1.webp"
    scene stage_3_event_1
    play music "/music/university.ogg" if_changed
    "You arrive to class and immediately your eyes shoot towards the setup at the front of the room."
    "There are two desks laden with numerous footlong meatball subs dripping with sauce and various toppings."
    "Amidst wondering if Daisy intends to eat the massive feast all on her own, you quickly get to your seat as you hear the door open up."
    image stage_3_event_2 = "/teacher/events/stage3/2.webp"
    scene stage_3_event_2
    teacher "Good morning, students."
    fs "What’s with all of the food?"
    ms "They look really good. Mind if I have one?"
    image stage_3_event_3 = "/teacher/events/stage3/3.webp"
    scene stage_3_event_3
    teacher "Settle down, class. Your questions will be answered in a moment."
    image stage_3_event_4 = "/teacher/events/stage3/4.webp"
    scene stage_3_event_4
    teacher "Before we begin, I would like to introduce you all to someone. Come on in!"
    image stage_3_event_5 = "/teacher/events/stage3/5.webp"
    scene stage_3_event_5
    "Another woman dressed in black strolls into the room."
    if lunabunnybitesevent == 0:
        "It is the attractive woman that completed the Big Bunny Challenge."
    image stage_3_event_6 = "/teacher/events/stage3/6.webp"
    scene stage_3_event_6
    teacher "Class, I would like to introduce you all to a dear friend of mine, Ms. Luna."
    luna "Good morning, everyone."
    s "Good morning, Ms. Luna."
    image stage_3_event_7 = "/teacher/events/stage3/7.webp"
    scene stage_3_event_7
    teacher "She’s with me today to participate in a fun contest."
    teacher "Considering the desks covered with food and the nature of our lesson plan, I’m assuming you all can figure out what kind of competition this is."
    "Luna and Daisy move over to the desks with food."
    image stage_3_event_8 = "/teacher/events/stage3/8.webp"
    scene stage_3_event_8
    teacher "The rules are fairly simple. We are both given the same amount of food to eat as fast as possible."
    teacher "The first one to finish their meal wins. Before we begin, Luna could you please let the students know your measurements?"
    image stage_3_event_9 = "/teacher/events/stage3/9.webp"
    scene stage_3_event_9
    if persistent.imperial:
        $ imperialweight = (luna.weight * 2.2)
        luna "Sure thing. I currently weigh [imperialweight:.02f] lbs. My breasts are a [luna.breast_cup] cup and measure [luna.breast_size] inches."
        luna "Lastly, my waist is [luna.waist_size] inches and my hips measure [luna.ass_size] inches."
    else:
        $ metricbreast_size = (luna.breast_size * 2.54)
        $ metricwaist_size = (luna.waist_size * 2.54)
        $ metricass_size = (luna.ass_size * 2.54)
        luna "Sure thing. I currently weigh [luna.weight:.02f]kg. My breasts are a [luna.breast_cup] cup and measure [metricbreast_size:.02f] cm."
        luna "Lastly, my waist is [metricwaist_size:.02f] cm and my hips measure [metricass_size:.02f] cm."
    image stage_3_event_10 = "/teacher/events/stage3/10.webp"
    scene stage_3_event_10
    teacher "Write that down, students. She will be returning to class in the future and you'll need to track her progress."
    $ luna_stats_visible = 1
    "Luna’s measurements are now visible in the Stats Screen."
    image stage_3_event_11 = "/teacher/events/stage3/11.webp"
    scene stage_3_event_11
    teacher "Now that that’s out of the way, let’s get on to the main event. [playername], would you mind doing the countdown?"
    pc "Sure thing. 3…2…1…GO!"
    image stage_3_event_12 = "/teacher/events/stage3/12.webp"
    scene stage_3_event_12
    "On your mark, the two women attack the subs like they haven’t eaten in days. In mere moments the room becomes filled with the sound of loud chewing and pleased hums."
    image stage_3_event_13 = "/teacher/events/stage3/13.webp"
    scene stage_3_event_13
    teacher "Hmmm, these are really good!"
    image stage_3_event_14 = "/teacher/events/stage3/14.webp"
    scene stage_3_event_14
    luna "Mmmph, I told you."
    image stage_3_event_15 = "/teacher/events/stage3/15.webp"
    scene stage_3_event_15
    teacher "Hold on, give me a break so I can make some room."
    image stage_3_event_16 = "/teacher/events/stage3/16.webp"
    scene stage_3_event_16
    "With a flick of her fingers, Daisy manages to unbutton her shirt to allow her belly to freely swing about."
    teacher "Ahhh, much better."
    image stage_3_event_17 = "/teacher/events/stage3/17.webp"
    scene stage_3_event_17
    luna "That's not a bad idea. Give me a second."
    "Luna in response unzips her shorts to let her belly out."
    image stage_3_event_18 = "/teacher/events/stage3/18.webp"
    scene stage_3_event_18
    luna "Yeah, that’s just what I needed. Alright, let’s get back to the contest."
    image stage_3_event_19 = "/teacher/events/stage3/19.webp"
    scene stage_3_event_19
    "No longer burdened by clothing, the two of them return to binge eating with renewed fervor."
    "While Luna appears to be taking the lead at first, Daisy has a clear advantage in the form of her own cheering squad."
    fs "Come on, Ms. Tanwen! You can do this!"
    ms "Yeah, you’ve been training for this. You eat way more food than this every Friday."
    image stage_3_event_20 = "/teacher/events/stage3/20.webp"
    scene stage_3_event_20
    "The constant cheering allows Daisy to take the lead in terms of both speed and how much her belly bulges out."
    "While the competition is fierce and their passions are high, the winner is inevitably decided."
    image stage_3_event_21 = "/teacher/events/stage3/21.webp"
    scene stage_3_event_21
    "Daisy manages to pull out a win while Luna still has a single sandwich remaining."
    "Holding her arms out, Daisy basks in the praise of her students and puts her swollen gut on full display."
    ms "Way to go big, Ms. Tanwen!"
    image stage_3_event_22 = "/teacher/events/stage3/22.webp"
    scene stage_3_event_22
    teacher "Thank you all. I couldn’t have done it without your help."
    luna "Don’t be so modest. Only a pig like you could eat that fast."
    image stage_3_event_23 = "/teacher/events/stage3/23.webp"
    scene stage_3_event_23
    "The two of them share a pair of mischievous smirks free of any actual malice."
    teacher "Don’t be getting cheeky with me. You recall what the prize is. Come over here. You need to finish your meal."
    image stage_3_event_24 = "/teacher/events/stage3/24.webp"
    scene stage_3_event_24
    "Lifting Luna up on the desk, Daisy proceeds to shove the remaining sub down her throat. As she continues to push, she lets the class watch as she massages her hand across Luna’s belly."
    teacher "I’d say you’re the real pig here with all this added weight. It’s almost like you’re pregnant. Then again, I guess pure size can’t beat training."
    image stage_3_event_25 = "/teacher/events/stage3/25.webp"
    scene stage_3_event_25
    "Managing to push the very last of the sandwich down her competitor’s throat, Luna looks at her foodbaby with a pained expression."
    image stage_3_event_26 = "/teacher/events/stage3/26.webp"
    scene stage_3_event_26
    teacher "Regardless of the outcome, I do hope that you all enjoyed our little event today."
    luna "I certainly did. Just watch your back, Daisy. I don't intend to lose next time."
    teacher "We'll see about that. Isn't that right, class?"
    "The room breaks out into a roar of applause, bringing the class to an end. Congratulating Daisy on her win and thanking Luna for coming, you head out for the day."
    stop music fadeout 1.0
    $ teacherstage3event = 0
    if recollection == False:
        $ luna.weight += 4
        $ teacher.weight += 1
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Teacher_Stage_4_Event:
    image stage_4_event_arrive = "/teacher/events/stage4/arrive.webp"
    scene stage_4_event_arrive
    play music "/music/university.ogg" if_changed
    "The usual pre-class chatter comes to a halt once Daisy walks in wearing a very revealing pair of yoga pants and a sporty shirt."
    fs "Wait, Sports Day is today?"
    ms "Hell yeah, it is! Looking good, Ms. Tanwen!"
    teacher "Thank you."
    image stage_4_event_greet = "/teacher/events/stage4/greet.webp"
    scene stage_4_event_greet
    teacher "Good morning, students."
    s "Good morning, Ms. Tanwen."
    image stage_4_event_1 = "/teacher/events/stage4/1.webp"
    scene stage_4_event_1
    teacher "As some of you are aware, today is National Sports Day."
    teacher "As a teacher, it is my duty to center today’s lesson on the topic of working out."
    image stage_4_event_2 = "/teacher/events/stage4/2.webp"
    scene stage_4_event_2
    teacher "Staying fit and mobile is heavily reliant on you working out on a regular basis."
    teacher "Even if your intention is to gain weight, it’s still a good idea to perform regular exercise."
    image stage_4_event_3 = "/teacher/events/stage4/3.webp"
    scene stage_4_event_3
    teacher "A regular workout regimen trains the muscles to have an easier time lugging around your growing body."
    teacher "People who gain weight too fast without exercising run the risk of reducing their mobility to next to nothing."
    image stage_4_event_4 = "/teacher/events/stage4/4.webp"
    scene stage_4_event_4
    teacher "It should be noted that immobility is the dream for some people. If that’s the case, they typically avoid straining their body too much on purpose."
    teacher "I on the other hand intend to dive into an extreme work out routine to get rid of all the extra weight you’ll be piling onto me during our lessons."
    image stage_4_event_5 = "/teacher/events/stage4/5.webp"
    scene stage_4_event_5
    teacher "Working out has the added benefit of improving the health of your heart."
    teacher "Periods of high blood pressure from sports and other athletic activities can have an overall positive effect on your body."
    image stage_4_event_6 = "/teacher/events/stage4/6.webp"
    scene stage_4_event_6
    teacher "For me, working out is a means to help out with my flexibility. To demonstrate, let me show off a few different types of exercise."
    image stage_4_event_7 = "/teacher/events/stage4/7.webp"
    scene stage_4_event_7
    teacher "Let's start with the most important part of any routine: stretching. You should stretch before every workout to reduce the risks of hurting yourself."
    image stage_4_event_8 = "/teacher/events/stage4/8.webp"
    scene stage_4_event_8
    pause
    image stage_4_event_9 = "/teacher/events/stage4/9.webp"
    scene stage_4_event_9
    teacher "This is called a push-up. I would advise doing at least ten or more before going to bed each night as the bare minimum of exercise."
    image stage_4_event_10 = "/teacher/events/stage4/10.webp"
    scene stage_4_event_10
    teacher "If you want something a bit more dynamic, you can try fighting sports. Despite the simulated violence, they are a great way to relieve stress and lower aggression."
    teacher "This ranges from quick footed boxers to even heavy weight sumo wrestling. I’d take it you all can guess which one I’m going to be giving a shot as the semester goes on."
    image stage_4_event_11 = "/teacher/events/stage4/11.webp"
    scene stage_4_event_11
    teacher "I personally like to focus on my legs while I work out. It helps to make my butt and thighs look even better."
    image stage_4_event_12 = "/teacher/events/stage4/12.webp"
    scene stage_4_event_12
    teacher "If you’re looking for a workout that’s both cheap and easy, I would recommend running. It’s also very popular."
    teacher "Marathons are held worldwide where tons of people come together to run the same route for charity, glory, and various other things."
    image stage_4_event_13 = "/teacher/events/stage4/13.webp"
    scene stage_4_event_13
    teacher "The only real downside of running is that you typically need some good shoes if you plan to go hard."
    teacher "They don’t have to be too expensive but be sure that they fit well to avoid getting sores."
    image stage_4_event_2 = "/teacher/events/stage4/2.webp"
    scene stage_4_event_2
    teacher "Now that the basics are out of the way, let me show you my preferred way of getting my body moving. As I’ve said before, I used to dance as a career."
    teacher "Though it’s no longer my main job, it’s still an excellent way to keep myself in shape and let loose every once in a while."
    image stage_4_event_11 = "/teacher/events/stage4/11.webp"
    scene stage_4_event_11
    "Putting on an upbeat song on her phone, she breaks out into a whirlwind of wild movements."
    teacher "As you may be able to tell, my knowledge of various dancing techniques is on par with my nutritional studies. What I would like to demonstrate for you is hip hop style."
    image stage_4_event_16 = "/teacher/events/stage4/16.webp"
    scene stage_4_event_16
    ms "Woo! Keep it up, teach!"
    image stage_4_event_17 = "/teacher/events/stage4/17.webp"
    scene stage_4_event_17
    "As Daisy continues to dance, the rest of the students speak up to praise the flexibility of her body’s movements."
    "Just as the song ends and she’s given a moment to catch her breath, she picks up her phone again to play a classical piece of music."
    image stage_4_event_18 = "/teacher/events/stage4/18.webp"
    scene stage_4_event_18
    "As the song fills the air, Daisy takes on a more graceful pose."
    teacher "I am also trained in ballet. Allow me to demonstrate."
    image stage_4_event_19 = "/teacher/events/stage4/19.webp"
    scene stage_4_event_19
    "Her dance moves look akin to flowing water, mesmerizing the room with each elegant pose. The class is thrown into a sort of trance as they watch."
    image stage_4_event_20 = "/teacher/events/stage4/20.webp"
    scene stage_4_event_20
    "You follow along with the group as you attempt to memorize every part of her performance."
    image stage_4_event_21 = "/teacher/events/stage4/21.webp"
    scene stage_4_event_21
    "As the song ends, the class erupts into applause as she takes a deep bow."
    fs "That was amazing. Bravo!"
    teacher "Thank you, thank you."
    image stage_4_event_eventend = "/teacher/events/stage4/eventend.webp"
    scene stage_4_event_eventend
    teacher "I’m a little sweaty after all that, but I hope you all learned something today. See you tomorrow."
    stop music fadeout 1.0
    scene university_leave
    "You leave class with a renewed energy to workout and get your body moving. The thought occurs that maybe you should check out the gym at some point."

    $ teacherstage4event = 0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Teacher_Stage_5_Event:
    image stage_5_event_start = "/teacher/events/stage5/start.webp"
    scene stage_5_event_start
    play music "/music/university.ogg" if_changed
    "You arrive to class to see two desks pushed to the front of the room covered in dozens of extra large cups of soda."
    "Thinking about the last time you saw something like this, you quickly take your seat."
    image stage_5_event_1 = "/teacher/events/stage5/1.webp"
    scene stage_5_event_1
    "The first thing you notice as Daisy steps inside is how her drastic weight gain has really filled out her figure."
    ms "Looking good, teach."
    fs "She keeps wearing that same outfit. How much longer is it going to last?"
    image stage_5_event_2 = "/teacher/events/stage5/2.webp"
    scene stage_5_event_2
    teacher "Good morning, students."
    s "Good morning, Ms. Tanwen."
    teacher "As you can see, I’ve procured a large collection of soda for today’s lesson. Though it is a lot, I don’t intend to take it on by myself."
    image stage_5_event_3 = "/teacher/events/stage5/3.webp"
    scene stage_5_event_3
    luna "Hi there, everyone!"
    teacher "Class, you remember Luna. Please give her a proper greeting."
    s "Hello, Ms. Luna."
    image stage_5_event_4 = "/teacher/events/stage5/4.webp"
    scene stage_5_event_4
    teacher "Very good. Now we can have our little rematch."
    luna "This time, victory WILL be mine."
    image stage_5_event_5 = "/teacher/events/stage5/5.webp"
    scene stage_5_event_5
    teacher "I’m not so sure your skinny body can hold as much as you think. Especially since we’re drinking soda, a beverage notoriously rich in sugars."
    teacher "To be a close race, we’ll both have to guzzle down the equivalent of half a kilo worth of sugar."
    image stage_5_event_6 = "/teacher/events/stage5/6.webp"
    scene stage_5_event_6
    luna "You say that like it’s a challenge."
    teacher "More like a lesson to my class. Enough talk though. The same rules apply as before. First one to finish their serving wins."
    image stage_5_event_7 = "/teacher/events/stage5/7.webp"
    scene stage_5_event_7
    teacher "I do hope you haven’t forgotten that the loser has to pay for the winner’s next meal."
    luna "I haven’t. Don’t worry, there’s this ritzy buffet place I’ve been dying to go to. I just hope you have some deep pockets."
    image stage_5_event_8 = "/teacher/events/stage5/8.webp"
    scene stage_5_event_8
    "Daisy and Luna pick up a cup in preparation."
    teacher "[playername], would you mind doing the honors?"
    pc "Sure thing. 3…2…1… {w}GO!"
    image stage_5_event_9 = "/teacher/events/stage5/9.webp"
    scene stage_5_event_9
    "Your words send the women into a flurry of binge drinking. They slurp up their first pair of sodas like they were nothing before moving onto the next."
    fs "Wow, all that carbonation can not be making that easy."
    image stage_5_event_10 = "/teacher/events/stage5/10.webp"
    scene stage_5_event_10
    "The competition is as fierce as ever, making it all the more curious when Daisy takes a pause between sips."
    image stage_5_event_11 = "/teacher/events/stage5/11.webp"
    scene stage_5_event_11
    "Unbuttoning her shirt, she allows the class to take a gander at her pudgy belly as it sags down."
    image stage_5_event_12 = "/teacher/events/stage5/12.webp"
    scene stage_5_event_12
    teacher "There. Now that my belly is free, I should have no problems."
    fs "No kidding. With how big you are, there’s no way you’ll lose."
    image stage_5_event_13 = "/teacher/events/stage5/13.webp"
    scene stage_5_event_13
    "The comments are not ignored by Luna."
    "Taking a break of her own, she quickly removes her clothing to leave her in just her undergarments."
    image stage_5_event_14 = "/teacher/events/stage5/14.webp"
    scene stage_5_event_14
    luna "Might as well even the playing field. Now I have plenty of space to grow."
    ms "Damn, she looks good. You got this, Luna!"
    image stage_5_event_15 = "/teacher/events/stage5/15.webp"
    scene stage_5_event_15
    "No longer restrained by their clothing, the two women resume drinking at a rapid pace."
    image stage_5_event_16 = "/teacher/events/stage5/16.webp"
    scene stage_5_event_16
    "The side effects are made quite clear as the entire class watches their bellies continue to swell."
    image stage_5_event_17 = "/teacher/events/stage5/17.webp"
    scene stage_5_event_17
    fs "They’re both inflating like a pair of balloons."
    image stage_5_event_18 = "/teacher/events/stage5/18.webp"
    scene stage_5_event_18
    ms "Yeah, but Luna is getting bigger."
    image stage_5_event_19 = "/teacher/events/stage5/19.webp"
    scene stage_5_event_19
    fs "Are you blind? Ms. Tanwen has this in the bag."
    "The class divides down the center on who they’re rooting for."
    "Caught in the middle, you’re given the opportunity to watch them fight each other for the lead. However, the winner is eventually determined to be…"
    image stage_5_event_20 = "/teacher/events/stage5/20.webp"
    scene stage_5_event_20 with vpunch
    teacher "Looks like I BWOOOOOORRRP win!"
    image stage_5_event_21 = "/teacher/events/stage5/21.webp"
    scene stage_5_event_21
    teacher "Whoops, sorry about that, class. Should have mentioned something about the fizziness."
    teacher "Ah well, I can tell you about it another time."
    image stage_5_event_22 = "/teacher/events/stage5/22.webp"
    scene stage_5_event_22
    luna "Dammit. It was so close."
    teacher "While I appreciate your determination, you know as well as I that there was no way you were going to win. You’re not nearly big enough."
    luna "Doesn’t mean I shouldn’t try."
    if persistent.imperial:
        teacher "True, true. How about we try this again once you reach over 220 lbs?"
    else:
        teacher "True, true. How about we try this again once you reach over 100kg?"
    luna "It’s a bet."
    image stage_5_event_23 = "/teacher/events/stage5/23.webp"
    scene stage_5_event_23
    teacher "That will be all for today, students. You can go home. [playername], please stay behind to help with the cleanup."
    image stage_5_event_24 = "/teacher/events/stage5/24.webp"
    scene stage_5_event_24
    "As the students file out, you’re left alone with Daisy and Luna. Watching Daisy lock the door and close the blinds, you wonder what’s about to happen."
    teacher "I thought perhaps you would be willing to help."
    pc "I'm curious, that's for sure."
    pc "What exactly is it you need help with?"
    image stage_5_event_25 = "/teacher/events/stage5/25.webp"
    scene stage_5_event_25
    teacher "Not me this time. Luna could use your... assistance."
    pc "Sure. Hello again, Luna. Big fan of your work today."
    image stage_5_event_26 = "/teacher/events/stage5/26.webp"
    scene stage_5_event_26
    luna "Even though I lost?"
    pc "Everyone in the class was a winner today, I'd say."
    pc "What is it I can help you with?"
    luna "I don't know exactly how to put it."
    image stage_5_event_27 = "/teacher/events/stage5/27.webp"
    scene stage_5_event_27
    "Luna gets up sits atop Daisy’s desk before tossing her panties on the ground."
    luna "Perhaps I could give you clues instead?"
    image stage_5_event_28 = "/teacher/events/stage5/28.webp"
    scene stage_5_event_28
    "With nothing in her way, she freely allows her fingers to vigorously rub against her womanhood."
    image stage_5_event_29 = "/teacher/events/stage5/29.webp"
    scene stage_5_event_29
    teacher "Luna has a reaction to stuffing."
    teacher "We noticed when we were out for dinner a few months back and ordered far too many appetizers."
    teacher "I noticed because I was feeling much the same way."
    teacher "But this time isn't about me."
    pc "Are you sure about this?"
    image stage_5_event_30 = "/teacher/events/stage5/30.webp"
    scene stage_5_event_30
    teacher "Are you not interested?"
    pc "The opposite, in fact."
    pc "But if someone walking by put their ear to the door..."
    image stage_5_event_31 = "/teacher/events/stage5/31.webp"
    scene stage_5_event_31
    luna "He's right. Perhaps you should leave to give us plausible deniability."
    image stage_5_event_32 = "/teacher/events/stage5/32.webp"
    scene stage_5_event_32
    "Daisy sighed."
    teacher "I have to admit, I was hoping to be here to oversee the fun."
    teacher "But I believe you're right, and I should leave you two alone."
    teacher "Don't worry, you are in no danger of getting expelled."
    teacher "To be safe, I'll stand outside the door to chase any students or faculty away."
    image stage_5_event_33 = "/teacher/events/stage5/33.webp"
    scene stage_5_event_33
    luna "Funny, it almost feels like I'm the winner today."
    pc "I was going to say the same."
    image stage_5_event_34 = "/teacher/events/stage5/34.webp"
    scene stage_5_event_34
    "Getting up from your desk, you begin to take off your clothes before approaching Luna."
    teacher "Have fun, you two."
    "You want to acknowledge her, but your eyes are glued to Luna as you hear the door closing and realize the two of you have the room all to yourselves."
    image stage_5_event_35 = "/teacher/events/stage5/35.webp"
    scene stage_5_event_35
    pc "Hey there."
    luna "Hi again."
    pc "Would you rather warm up between us or get right to business?"
    image stage_5_event_36 = "/teacher/events/stage5/36.webp"
    scene stage_5_event_36
    luna "Dealer's choice."
    menu:
        "Get to know her better":
            pc "Call me old fashioned, but I'm used to getting to know a woman a bit before getting intimate."
            luna "Believe me, so am I. This is very out of character for me."
            luna "But do you ever find yourself in a situation you can't help but get excited about feeling like you can't quite control yourself, but you know you're going to be very happy with the results anyway?"
            pc "At the moment? Absolutely."
            pc "I don't know exactly how this works, but I wouldn't mind taking you out to dinner something after this."
            luna "So you can watch me stuff myself again?"
            pc "Not exactly what I had in mind, but I'm not opposed."
            pc "But something tells me you are someone worth getting to know better."
            luna "I would absolutely adore that."
            luna "But in the meantime..."
            luna "Perhaps we should make the most of our time here?"
            pc "Nice to be on the same page."

        "Right to business":
            pc "Forgive me, but I don't think I can hold myself back another second."
            luna "Already forgiven."

    if persistent.nosexscene == True:
        scene black with dissolve
        "Luna and I had a great time together."
        "You return home."
        stop music fadeout 1.0
        if recollection == False:
            $ luna.weight = 62
            $ teacher.weight += 1
            $ teacherstage5event = 0
            $ strip = 0
            $ daytime = 2
            #Unlocks Luna Undress in the stats page.
            $ renpy.notify("Luna Undress option unlocked in stats screen.")
            window hide
            pause
            jump freetime
        return
    "You manage to get within a few inches of her before she decides to take the initiative."
    image stage_5_event_37 = "/teacher/events/stage5/37.webp"
    scene stage_5_event_37
    "Leaping off of the desk, Luna latches onto you as she forcefully shoves herself down onto your rigid member. Feeling her begin to slip, you quickly reach around to grasp her buttocks."
    image stage_5_event_38 = "/teacher/events/stage5/38.webp"
    scene stage_5_event_38
    luna "Fffff..."
    luna "That's what I needed!"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage5/39.webm" loop
    show movie with dissolve
    window hide
    pause
    "Heeding her words, you begin to rock your hips back and forth. The motion constantly slaps her taut belly against you, treating your ears to the sound of the soda inside of her sloshing around."
    "While the experience is absolute bliss, it’s obvious that you won’t be able to hold her up for much longer."
    pc "You are the sexiest thing I've ever seen in my life!"
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage5/40.webm" loop
    show movie with dissolve
    pc "But another minute in this position would give me a ninety percent chance of finishing early."
    luna "Change positions? I'd love to!"
    luna "Come on, boy. I want you to take me from behind."
    stop movie
    image stage_5_event_41 = "/teacher/events/stage5/41.webp"
    scene stage_5_event_41
    "Lowering Luna to the ground, the two of you shift positions to have her bending over with her arms holding onto Daisy’s desk."
    "With everything in the right place, you grasp onto her hips to slam your cock back inside of her needy womanhood."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage5/42.webm" loop
    show movie with dissolve
    window hide
    pause
    luna "Fuck yes! That’s it."
    luna "Now keep going."
    "No longer burdened by the brunt of her weight, you’re free to swing your hips back and forth at a much quicker pace."
    "The constant movement once more fills the room with the sound of soda swirling about inside of her."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage5/43.webm" loop
    show movie with dissolve
    "However, this noise is soon drowned out by Luna’s moans as she builds towards the orgasm she had been yearning for."
    luna "Yesss! Almost there!"
    luna "Keep going! Just a bit longer!"
    pc "Are you... {w}is it safe?"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage5/44.webm" loop
    show movie with dissolve
    luna "Yes!"
    luna "Are you close?"
    pc "I'm- {w}there!"
    luna "Yesss!"
    luna "Cum with me, [playername]!"
    "Feeling her body shiver around your cock, you give one last shove to fill her up with your seed."
    stop movie
    image stage_5_event_45 = "/teacher/events/stage5/45.webp"
    scene stage_5_event_45
    luna "That was... {w}no notes."
    pc "I have some."
    pc "But only positive ones."
    luna "M-more. I need more."
    image stage_5_event_46 = "/teacher/events/stage5/46.webp"
    scene stage_5_event_46
    pc "Yeah?"
    luna "Yeah, but I know Daisy is going to be annoyed if we go for another round."
    luna "HEY, DAISY!"
    "Daisy rushed inside to close the door behind her quickly."
    #luna "Do you have another round in you?"
    #luna "Daisy might be annoyed, but..."
    #luna "Maybe we could ask her?"
    #luna "HEY, DAISY!"
    #"Daisy rushed inside to close the door behind her quickly."
    #teacher "How was it?"
    #luna "Incredible."
    #luna "You have got to try this one out for yourself."
    #teacher "I'm not- {w}not right now."
    #luna "I know, silly. {w}But we called you in here to see if we have time for another round."
    #teacher "That's up to Bladerune."
    #luna "Oh."
    #teacher "Yeah, he already has a ton of work to animate and whatnot."
    #teacher "What would the scene consist of?"
    #luna "Mostly me taking charge and letting your prize pupil here have a break while I ride him."
    #teacher "That sounds fun."

    # back to the original scene ending, more or less:
    image stage_5_event_47 = "/teacher/events/stage5/47.webp"
    scene stage_5_event_47
    teacher "So Luna, what do you think of him?"
    luna "He’s a little rough, but I can definitely see his potential."
    pc "Thanks?"
    image stage_5_event_48 = "/teacher/events/stage5/48.webp"
    scene stage_5_event_48
    luna "Can I have your number? I want to spend more time with you."
    luna "Plus, I heard you make for a great feeder. I could use some help training for my next match with Daisy."
    pc "Sure thing."
    "You and Luna exchange contact information."
    image stage_5_event_49 = "/teacher/events/stage5/49.webp"
    scene stage_5_event_49
    teacher "Thanks again for helping me out today."
    luna "Yeah, we really have to do it again sometime."
    pc "You can count on it."
    stop music fadeout 1.0
    scene university_leave
    "Finishing up with the cleaning, you gather up your things and head home for the day, still in disbelief of the day’s class."
    if recollection == False:
        $ luna.weight = 62
        $ teacher.weight += 1
        $ teacherstage5event = 0
        $ strip = 0
        $ daytime = 2
        #Unlocks Luna Undress in the stats page.
        $ renpy.notify("Luna Undress option unlocked in stats screen.")
        window hide
        pause
        jump freetime
    return


label Teacher_Stage_6_Event_1:
    image stage_6_event_arrive = "/teacher/events/stage6/arrive.webp"
    scene stage_6_event_arrive
    play music "/music/university.ogg" if_changed
    "Upon entering class and seeing the modifications that have been made to the room overnight, you’re not surprised to turn around to see Daisy stroll in wearing yet another skimpy outfit."
    fs "Wow!"
    ms "Best. Class. EVER!"
    image stage_6_event_greet = "/teacher/events/stage6/greet.webp"
    scene stage_6_event_greet
    teacher "Good morning, students."
    s "Good morning, Ms. Tanwen."
    teacher "Today I would like to talk to you about attraction."
    image stage_6_event_front = "/teacher/events/stage6/front.webp"
    scene stage_6_event_front
    teacher "Even if your body isn’t considered beautiful according to conventional standards, that doesn’t mean that someone can’t be attracted to you."
    teacher "It’s all a matter of how you use what you have and your own personal confidence."
    image stage_6_event_ass = "/teacher/events/stage6/ass.webp"
    scene stage_6_event_ass
    teacher "For example, my belly and butt are too big for normal modeling. But with the right techniques, you can be sexy no matter what the size."
    image stage_6_event_poledance1 = "/teacher/events/stage6/poledance1.webp"
    scene stage_6_event_poledance1
    "Giving the class a few more seconds to gawk at her backside, Daisy struts over to the pole next to her desk and clings to it."
    teacher "One major way to show off one’s body is through the art of pole dancing. This type of display is great for those with strong legs."
    image stage_6_event_poledance2 = "/teacher/events/stage6/poledance2.webp"
    scene stage_6_event_poledance2
    teacher "The right moves and poses can really enhance the way people see your body. Allow me to demonstrate."
    image stage_6_event_poledance3 = "/teacher/events/stage6/poledance3.webp"
    scene stage_6_event_poledance3
    "Hoisting herself into the air, Daisy begins to twist and turn her body around the pole."
    fs "That’s simply amazing."
    ms "Yeah, amazingly sexy."
    image stage_6_event_poledance4 = "/teacher/events/stage6/poledance4.webp"
    scene stage_6_event_poledance4
    "The constant cheering from the students motivates her to move faster, showing off positions you didn’t think were possible."
    "Especially considering the extra heft she’s carrying around."
    image stage_6_event_poledance5 = "/teacher/events/stage6/poledance5.webp"
    scene stage_6_event_poledance5
    "What really sets her off is when one of the more daring students tosses out a few dollar bills in front of her."
    "Giggling at the sight, she finishes up her routine before giving herself a chance to rest. Getting down from the pole, she picks up the loose change and tosses it back to the student’s desk."
    image stage_6_event_poledance6 = "/teacher/events/stage6/poledance6.webp"
    scene stage_6_event_poledance6
    teacher "While I appreciate the tips, this was just meant to be a way to bring my point across."
    teacher "Save your money for the professionals down at Velvet Shadows. They’re the ones that were so kind to loan me this outfit and teach me some of their moves."
    image stage_6_event_eventend = "/teacher/events/stage6/eventend.webp"
    scene stage_6_event_eventend
    teacher "That will be all for today. I hope you enjoyed my little show."
    image stage_6_event_1 = "/teacher/events/stage6/1.webp"
    scene stage_6_event_1
    "As everyone begins to file out, you start to leave room only to be momentarily stopped by Daisy."
    "Without saying a word, she places a piece of paper in your hands. Looking at your palm, you see a pink colored business card for Velvet Shadows along with an address."
    image stage_6_event_2 = "/teacher/events/stage6/2.webp"
    scene stage_6_event_2
    "Turning back to see Daisy’s wide grin, it’s pretty obvious what she expects you to do with this information."
    stop music fadeout 1.0
    $ teacherstage6event = 0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Teacher_Stage_6_Event_2:
    #Daisy Stage 6.2 Event
    #(NOTE: The following should occur after the player visits the gym.)

    image stage_6_event_3 = "/teacher/events/stage6/3.webp"
    scene stage_6_event_3
    "On the way home from the gym, you end up passing by the Sugar Shop. You happen to arrive just as Daisy steps out with her arms laden with boxes of chocolate."
    teacher "Oh, hello [playername]. Good to see you."
    pc "What are you doing here?"
    teacher "I was picking up some chocolates to thank Luna for her help with class the other day. You actually came at a good time. Mind helping me get these into my car?"
    pc "Of course."
    image stage_6_event_4 = "/teacher/events/stage6/4.webp"
    scene stage_6_event_4
    "Taking on a portion of Daisy’s packages, you assist in loading the chocolates into her trunk."
    "Riding your way through town, you notice that you’re not heading towards her house."
    pc "Where are we going?"
    image stage_6_event_5 = "/teacher/events/stage6/5.webp"
    scene stage_6_event_5
    teacher "I’m getting a little hungry. Alright if we stop for a bite to eat?"
    pc "Sure, I’ve got time."
    image stage_6_event_6 = "/teacher/events/stage6/6.webp"
    scene stage_6_event_6
    "Arriving at Bunny Bites, you and Daisy take a seat."
    image stage_6_event_7 = "/teacher/events/stage6/7.webp"
    scene stage_6_event_7
    "In no time at all, the servers arrive with an order that shows you just how hungry she is."
    teacher "Perfect. This is just what I needed after resisting the temptation to eat all of those chocolates myself."
    image stage_6_event_8 = "/teacher/events/stage6/8.webp"
    scene stage_6_event_8
    teacher "This may not take care of my sweet tooth, but at least it will keep my belly happy long enough for the ride home."
    pc "So, how do you know Luna?"
    teacher "Ahh, we go way back."
    image stage_6_event_9 = "/teacher/events/stage6/9.webp"
    scene stage_6_event_9
    "Daisy pauses for a moment to move onto another plate of food after finishing her first one."
    image stage_6_event_10 = "/teacher/events/stage6/10.webp"
    scene stage_6_event_10
    teacher "The two of us met during my self-discovery phase. We were working in a similar field and ended up hitting it off."
    pc "As friends?"
    image stage_6_event_11 = "/teacher/events/stage6/11.webp"
    scene stage_6_event_11
    "Daisy raises an eyebrow and smirks at you."
    pc "Oh!"
    teacher "Haha, it’s alright. It’s been a long time since we’ve done anything serious."
    image stage_6_event_12 = "/teacher/events/stage6/12.webp"
    scene stage_6_event_12
    "Finished with another burger, she takes a moment to drink."
    image stage_6_event_13 = "/teacher/events/stage6/13.webp"
    scene stage_6_event_13
    teacher "While we did have some fun, we decided we were better off as friends rather than lovers."
    teacher "Doesn’t mean we don’t get together every so often to enjoy each other’s company or exchange notes."
    pc "What notes?"
    teacher "She uses me as a way to talk over some of her research. In turn, I have her look over my lesson plans for any suggestions."
    teacher "She was the one that encouraged me to do that little contest."
    image stage_6_event_14 = "/teacher/events/stage6/14.webp"
    scene stage_6_event_14
    "Pulling over the rest of her food, she begins to devour it at a fast pace."
    image stage_6_event_15 = "/teacher/events/stage6/15.webp"
    scene stage_6_event_15
    teacher "She’s always been a bit on the competitive side. Whether that’s for getting funding for her experiments or just seeing who can make a bigger pig out of themselves."
    pc "She was pretty impressive the other day. Even if she was smaller than you."
    teacher "That’s all a part of her drive that keeps her going and what made me interested in the first place. It’s also why she was able to join the…"
    image stage_6_event_16 = "/teacher/events/stage6/16.webp"
    scene stage_6_event_16
    "Pausing for a moment, Daisy wipes her lips with her hand."
    "You can’t help feeling that the attempt at making herself more presentable was done in order to hold something back."
    pc "Is everything okay?"
    image stage_6_event_17 = "/teacher/events/stage6/17.webp"
    scene stage_6_event_17
    teacher "Um, yeah. Just fine."
    pc "What were you saying about-"
    image stage_6_event_18 = "/teacher/events/stage6/18.webp"
    scene stage_6_event_18
    teacher "[playername] you haven’t touched your food yet. I wouldn’t want you to starve. Go on and eat."
    "Feeling like you’re not going to get much more out of her at the moment, you do as she says and enjoy the meal."

    image stage_6_event_19 = "/teacher/events/stage6/19.webp"
    scene stage_6_event_19
    "Finished with the impromptu dinner date, you head back home while Daisy goes her separate way."
    scene player_room
    "Just as you’re about to wind down for the day, you receive a message from her."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Daisy', dialogue=dialogue_one)
    $ msg ("Thank you for your help today. But I ran into a little problem with the chocolates.", who=1)
    pause
    $ msg ("What’s wrong?")
    pause
    $ msg ("We might have spent too long in Bunny Bites and they all melted.", who=1)
    pause
    $ msg ("That sucks.")
    pause
    $ msg ("It’s alright. I can always get more for Luna. Besides, I still managed to salvage some fun out of it.", who=1)
    pause
    "You receive a picture from Daisy."
    $ msg (None, who=1, pic="stage6_daisy")
    pause
    $ msg ("So, what do you think of my little photo shoot?", who=1)
    pause
    #CHOICE: A) Looks messy or B) Looks sexy
    menu:
        "Looks messy.":
            $ msg ("Looks messy.")
            pause
            $ msg ("True. But I think it was more than worth it.", who=1)
            pause
        "Looks sexy.":
            $ msg ("Looks sexy.")
            pause
            $ msg ("Thank you. Almost makes up for how much of a mess it made in my car.", who=1)
            pause
    #(NOTE: Regardless of choice, the following should play out.)
    $ msg ("Let’s call this picture a reward for your help today. Thanks again!", who=1)
    pause
    $ hide_messenger()

    $ teacherstage6event2 = 0
    if recollection == False:
        $ teacher.weight += 0.5
        $ daytime += 1
    return

label Teacher_Stage_7_Event:
    image stage_7_event_arrive = "/teacher/events/stage7/arrive.webp"
    scene stage_7_event_arrive
    play music "/music/university.ogg" if_changed
    "Arriving to class, your nose picks up a familiar aroma. Before you can figure out exactly what it is, Daisy strolls in wearing a red apron."
    fs "Why is she wearing that?"
    ms "I don't think she's wearing anything else under it."
    image stage_7_event_greet = "/teacher/events/stage7/greet.webp"
    scene stage_7_event_greet
    "Ducking behind her desk, she pulls out a take out bag and proceeds to pile up a collection of burritos."
    "Making sure her tower is stable, she turns towards the curious students."
    teacher "Good morning class."
    s "Good morning, Ms. Tanwen."
    teacher "As you can see, I made a little food run earlier to prepare for today's lesson."
    fs "Are you going to eat all of them?"
    image stage_7_event_1 = "/teacher/events/stage7/1.webp"
    scene stage_7_event_1
    teacher "Indeed. In order to speed up my weight gain, I'm going to be eating all of these burritos in one sitting."
    "Looking between the massive pile and Daisy, you can't help yourself from speaking out."
    pc "Are you sure you can do this? It's a lot of food."
    "Daisy lets out a laugh."
    teacher "I appreciate your concern, but you have nothing to worry about."
    image stage_7_event_2 = "/teacher/events/stage7/2.webp"
    scene stage_7_event_2
    teacher "As shown during my contest with Ms. Luna, my stomach is capable of stretching to accommodate this amount of food."
    teacher "That being said, this meal will most likely make my belly swell like a balloon."
    teacher "Especially since these burritos were specifically made to fatten me up. Each of them comes in at a whopping 1000 kcals each."
    image stage_7_event_3 = "/teacher/events/stage7/3.webp"
    scene stage_7_event_3
    teacher "Allow me to show you."
    "Opening up her mouth as wide as possible, she practically inhales a burrito before moving onto a second one."
    image stage_7_event_4 = "/teacher/events/stage7/4.webp"
    scene stage_7_event_4
    teacher "Hold on. Standing up should ease up the pressure on my belly to allow more room."
    "True to her word, the change in position comes with an increased hunger that allows her to absolutely destroy the burritos."
    "At one point she begins eating two at a time, alternating bites between whichever one she places in her hands."
    image stage_7_event_5 = "/teacher/events/stage7/5.webp"
    scene stage_7_event_5
    "Watching her slow down, you begin to think she’s reaching her limits."
    "However, her momentary pause serves the purpose of letting her toss away her apron to reveal the bra and panties underneath."
    "Given full access to her bulged out belly, she begins to rub gentle circles across its surface."
    teacher "Mmm, I can feel them right now. All of the burritos pushing up against my abdomen. It’s simply amazing."
    image stage_7_event_6 = "/teacher/events/stage7/6.webp"
    scene stage_7_event_6
    "No longer restrained by the apron, Daisy attacks the remaining burritos like a rabid animal on the brink of starvation."
    fs "I know what she did in the contest, but this still feels like absolute fiction to see firsthand."
    image stage_7_event_7 = "/teacher/events/stage7/7.webp"
    scene stage_7_event_7
    "Nearing the end of the pile, the class has their eyes glued to her gut. Each bite taken further strains the taut flesh as her belly continues to grow."
    teacher "Huff, huff, almost…there."
    "Pushing herself past her limits, she managed to forcefully shove the last chunk of burrito down her throat."
    image stage_7_event_8 = "/teacher/events/stage7/8.webp"
    scene stage_7_event_8
    "Upon finishing her meal, Daisy just stands in front of the class rubbing her belly and letting out soft moans."
    "Looking at the way she’s shivering, it’s almost as if she’s about to orgasm."
    teacher "That was simply…divine."
    fs "Are you okay? You look like you’re about eight months pregnant after all that."
    image stage_7_event_9 = "/teacher/events/stage7/9.webp"
    scene stage_7_event_9
    "The comment brings a smile to Daisy’s face."
    teacher "I suppose that’s fitting. A common term for a stuffed belly such as mine is a food baby."
    teacher "However, I intend to make this thing look absolutely tiny in comparison to my final goal. For now though, I think I’m going to have to call it for the day."
    teacher "I need a moment to catch my breath. [playername], can you stay behind? I need help with some papers."
    pc "Of course."
    teacher "Excellent. The rest of you, I hope you enjoy your day."
    s "Goodbye, Ms. Tanwen."
    "Waiting until the class empties out save for you, Daisy waddles her way over to the door and locks it."
    "Noticing your confused expression, she gestures for you to stand up as she walks back towards her desk."
    image stage_7_event_afterclass1 = "/teacher/events/stage7/afterclass1.webp"
    scene stage_7_event_afterclass1
    "After making sure we’re completely alone, she sits down on the ground and proceeds to take off her underwear."
    "Tossing it to the side of the room, she lifts up her belly and spreads her legs to ensure I have an unobstructed view of her dripping pussy."
    if persistent.nosexscene == True:
        scene black with dissolve
        "Daisy and i had a great time together."
        "You return home."
        stop music fadeout 1.0
        $ burritounlock = 1
        $ teacherstage7event = 0
        if recollection == False:
            $ teacher.weight += 1
            $ strip = 0
            $ daytime = 2
            jump freetime
        return
    pc "Daisy, what’s going on?"
    "She lets out a sound that's a mix of a laugh and of a moan."
    teacher "Being able to stuff myself so much in front of such a large group of people makes me extremely horny. Usually I’d take care of it myself, but…"
    "Though she doesn’t speak, the look in her eyes says it all. Part of you know the risks of what she’s implying, but your body doesn’t seem to care."
    "It only takes a few more moments of staring at her stuffed belly to get you to undress and approach her."
    teacher "I knew it. A rock hard cock as close to bursting as my own belly. You’re just as perverted as me. No need to be ashamed."
    teacher "I’ll let you indulge your little urges in exchange for giving me some meat flavored dessert. Come over here, I know just how to do it."
    image stage_7_event_afterclass2 = "/teacher/events/stage7/afterclass2.webp"
    scene stage_7_event_afterclass2
    "Following her commands, you lay down on the floor as she straddles your body."
    "Sinking herself down onto your rigid member with utmost care, she makes sure to lower her gaze to see your reaction as she goes all the way down."
    teacher "What a cute expression of yours. I wonder how long you’ll be able to keep up."
    pause
    window hide
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage7/afterclass2_video.webm" loop
    show movie with dissolve
    pause
    "She begins to move her hips up and down, letting you ease into the sensation. This gentle approach lasts for as long as it takes for a moan to be released from your lips."
    "Upon hearing the sound, she shoots you a grin as a single warning for what’s to come."
    window hide
    pause
    stop movie
    image stage_7_event_afterclass3 = "/teacher/events/stage7/afterclass3.webp"
    scene stage_7_event_afterclass3
    "Leaning backwards, Daisy lets you take full control by letting you hold up her legs."
    pause
    window hide
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage7/afterclass3_video.webm" loop
    show movie with dissolve
    pause
    "Pushing herself through the lingering lethargy of her feast, her breathing becomes heavier as you keep thrusting your cock."
    "Under the influence of your dick sliding in and out of her womanhood, alongside her added weight bearing down on you, the world becomes a blur of pleasure."
    "Both of you only come back to reality as you give your hips one last thrust to bring you both to a simultaneous orgasm."
    window hide
    pause
    stop movie
    image stage_7_event_afterclass3 = "/teacher/events/stage7/afterclass3.webp"
    scene stage_7_event_afterclass3
    "Taking a moment to catch her breath, she eventually pulls herself off of you and helps you back on your feet."
    image stage_7_event_afterclass4 = "/teacher/events/stage7/afterclass4.webp"
    scene stage_7_event_afterclass4
    teacher "So, how was it?"
    pc "It was…great."
    "Daisy chuckles."
    teacher "A bit lacking in how to express your feelings I see. Don’t worry, your performance spoke volumes about your inner passion. You did far better than I could have hoped."
    image stage_7_event_afterclass5 = "/teacher/events/stage7/afterclass5.webp"
    scene stage_7_event_afterclass5
    teacher "As enjoyable as that was, it’s needless to say that we should keep this little encounter to ourselves."
    teacher "I can’t imagine the rumors around campus will be very kind if people find out I’m having sex with one of my students. Do you understand?"
    pc "Of course."
    image stage_7_event_eventend = "/teacher/events/stage7/eventend.webp"
    scene stage_7_event_eventend
    "Reaching out, Daisy gives you a soft pat on the head."
    teacher "That’s a good boy. Go ahead and get dressed then head out. I’ll stay behind to clean up our little mess. I’ll see you tomorrow."
    "Putting your clothes back on, you wave goodbye to Daisy before heading out the door."
    "You unlocked burritos!"
    stop music fadeout 1.0
    $ burritounlock = 1
    scene university_leave
    "I go back home."

    $ teacherstage7event = 0
    if recollection == False:
        $ teacher.weight += 1
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Teacher_Stage_8_Event:
    image stage_8_event_empty_classroom = "/teacher/events/stage8/empty_classroom.webp"
    scene stage_8_event_empty_classroom
    "You enter the classroom, only to discover that you’re the only one there."
    pc "Wait, where is everyone?"
    "A creeping feeling goes down your spine at the sound of footsteps approaching the room."
    "Hearing the door open up, you turn to see Daisy enter wearing something bizarre even for her."
    image stage_8_event_arrive = "/teacher/events/stage8/arrive.webp"
    scene stage_8_event_arrive
    pc "What the hell is going on? Why am I the only one here? What are you wearing? Is that real blood?"
    teacher "Settle down, it’s just paint. As for your other questions, take a seat and I’ll tell you all you want to know."
    "Fighting against your innate instincts to run, you take your usual seat at the front of the classroom."
    image stage_8_event_greet = "/teacher/events/stage8/greet.webp"
    scene stage_8_event_greet
    teacher "Good morning class. Or more precisely, good morning [playername]."
    "You don’t see a reason not to at least play along."
    pc "Good morning, Ms. Tanwen."
    image stage_8_event_1 = "/teacher/events/stage8/1.webp"
    scene stage_8_event_1
    teacher "Please, call me Daisy. No one else will be coming today. I sent out an e-mail to the other students telling them to take the day off."
    pc "Why did you do that?"
    teacher "Because what I’m about to tell you is a well held secret that only a select few are privy to."
    image stage_8_event_2 = "/teacher/events/stage8/2.webp"
    scene stage_8_event_2
    teacher "Today I would like to teach you a very special lesson involving my religion, The Followers of Heset."
    pc "The followers of what?"
    image stage_8_event_13 = "/teacher/events/stage8/13.webp"
    scene stage_8_event_13
    teacher "Heset. She is an ancient Egyptian goddess that is the embodiment of food and drink."
    teacher "Though the mythology has been altered throughout the course of the millennia, our group has remained steadfast in our worship of Heset."
    teacher "She symbolizes the pinnacle of the feederism life we strive to embody."
    pc "It’s a cult focused on making people gain weight?"
    image stage_8_event_3 = "/teacher/events/stage8/3.webp"
    scene stage_8_event_3
    teacher "You are mostly correct. However, we classify our group more as a religion. It allows us some tax breaks alongside avoiding certain negative connotations."
    teacher "You should keep this all in mind considering I’m here today to invite you to join us."
    pc "What do you mean?"
    image stage_8_event_12 = "/teacher/events/stage8/12.webp"
    scene stage_8_event_12
    teacher "Whether intentional or not, you seem to exemplify our group’s values. I think it’s quite obvious that you enjoy big ladies becoming bigger. Correct?"
    "Though there's a moment of hesitation, you eventually nod your head."
    pc "You got me there."
    image stage_8_event_4 = "/teacher/events/stage8/4.webp"
    scene stage_8_event_4
    teacher "While I’m being honest with you, I might as well tell you about my part in the group."
    teacher "I am a researcher for the Followers of Heset. My work is focused on finding new ways to fatten up the female population."
    image stage_8_event_5 = "/teacher/events/stage8/5.webp"
    scene stage_8_event_5
    teacher "I initially took on this teaching job as a guide and recruiter for our religion. With my many worldly travels, I assumed it would have been easy."
    teacher "Thanks to you, I’ve been able to enthusiastically spread the teachings of our group to your class."
    image stage_8_event_15 = "/teacher/events/stage8/15.webp"
    scene stage_8_event_15
    teacher "That being the case, I believe you’ve more than earned my assistance in achieving our goal of widespread weight gain."
    pc "That seems awfully generous of you."
    image stage_8_event_6 = "/teacher/events/stage8/6.webp"
    scene stage_8_event_6
    teacher "That’s because the Followers of Heset has been stagnant for a very long time. We’ve only recently begun to revitalize due to tracking down a descendant of Heset."
    pc "Wait, are you saying that my ancestor was an actual goddess?"
    image stage_8_event_7 = "/teacher/events/stage8/7.webp"
    scene stage_8_event_7
    teacher "No, you are not the descendant. However, you do have some importance to our group."
    teacher "While I don’t think you’re quite ready yet to take on certain responsibilities, you can prove your importance to the Followers of Heset by taking on a very important task."
    pc "Which would be…?"
    image stage_8_event_8 = "/teacher/events/stage8/8.webp"
    scene stage_8_event_8
    teacher "For now, I just want you to continue doing what you have been doing. Keep an eye out for girls that are open to the idea of gaining weight."
    teacher "The more obese women we create, the stronger our organization becomes. As I said before, I’ll do my best to assist you where I can."
    pc "What kind of help can you provide?"
    image stage_8_event_9 = "/teacher/events/stage8/9.webp"
    scene stage_8_event_9
    teacher "Right now, our group cannot offer you much. All our funds are currently focused on developing our goddess."
    teacher "In the future we will be able to offer aid through various means. For now, all I can recommend is going to the library."
    image stage_8_event_14 = "/teacher/events/stage8/4.webp"
    scene stage_8_event_14
    teacher "The librarian is one of our members and will be more than willing to offer you books to help you with your mission."
    image stage_8_event_10 = "/teacher/events/stage8/10.webp"
    scene stage_8_event_10
    teacher "As a side note, the Followers of Heset believe in open relationships with multiple partners. Feel free to work with as many candidates as you like as long as they are willing."
    image stage_8_event_11 = "/teacher/events/stage8/11.webp"
    scene stage_8_event_11
    teacher "That being said, I would like to give you a personal invitation to my home."
    "Reaching into her pocket, she hands you a piece of paper with her address written on it."
    teacher "Think of it as extra credit for both the class and preparing you for your future amongst our society."
    image stage_8_event_greet = "/teacher/events/stage8/greet.webp"
    scene stage_8_event_greet
    teacher "That will be all for now. I’ll tell you more information regarding our religion in the future once you’ve proven yourself."
    teacher "For now, just enjoy your day off and I’ll see you tomorrow."
    scene university_leave
    "Leaving Daisy with a cautious wave, you step out of the classroom."
    "Glancing at the piece of paper clutched in your hand, you try to make sense of the overload of information that has been thrusted upon you."
    "It sounds absolutely crazy, but something inside tells you to go along with Daisy’s plan."
    "In the hopes of making sense of what’s going on, you resolve to take on her ridiculous request."
    $ teacherstage8event = 0
    if recollection == False:
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Teacher_Stage_9_Event_1:
    #Scene: Feedee Class Session (Vicky and Caroline Introduction)
    scene university_looking_into_class
    play music "/music/university.ogg" if_changed
    "Arriving to class, your nose picks up a familiar scent."
    image stage_9_event_23 = "/teacher/events/stage9/23.webp"
    scene stage_9_event_23
    "Your mouth starts to drool at the sight of the collection of pizzas at the front of the room."
    image stage_9_event_24 = "/teacher/events/stage9/24.webp"
    scene stage_9_event_24
    "A glance towards the other students lets you see similar looks of wanting on their faces."
    "Whether it’s for the food itself or who is going to be eating them is left unknown until Daisy makes her appearance."
    image stage_9_event_25 = "/teacher/events/stage9/25.webp"
    scene stage_9_event_25
    teacher "Good morning, class."
    s "Good morning, Ms. Tanwen."
    image stage_9_event_26 = "/teacher/events/stage9/26.webp"
    scene stage_9_event_26
    teacher "I take it you all are dying to get on with today’s lecture. Any guesses as to what we’ll be doing?"
    image stage_9_event_27 = "/teacher/events/stage9/27.webp"
    scene stage_9_event_27
    ms "A pizza party?"
    fs "No you idiot. She’s obviously going to stuff herself again."
    image stage_9_event_28 = "/teacher/events/stage9/28.webp"
    scene stage_9_event_28
    teacher "I’m afraid that both of you are incorrect. While these pizzas are meant to be eaten as fast as possible, it won’t be by me."
    teacher "Two of your classmates have volunteered to be the subjects for today’s lesson."
    image stage_9_event_29 = "/teacher/events/stage9/29.webp"
    scene stage_9_event_29
    teacher "Let me go ahead and introduce them to you. Caroline, would you mind coming up here?"
    image stage_9_event_30 = "/teacher/events/stage9/30.webp"
    scene stage_9_event_30
    "A student that had remained mostly silent over the course of the semester stands up and begins to walk towards Daisy."
    image stage_9_event_31 = "/teacher/events/stage9/31.webp"
    scene stage_9_event_31
    "Her white dress and slim form are more than enough to grab the class’s attention."
    image stage_9_event_32 = "/teacher/events/stage9/32.webp"
    scene stage_9_event_32
    "However, looking past her neatly bound hair you see an emotionless face that doesn’t seem to care about the way people are staring at her."
    image stage_9_event_33 = "/teacher/events/stage9/33.webp"
    scene stage_9_event_33
    "Disregarding the various murmurs from her fellow classmates, she makes her way up to the front of the class and stands next to Daisy."
    teacher "Would you please introduce yourself to the class?"
    image stage_9_event_34 = "/teacher/events/stage9/34.webp"
    scene stage_9_event_34
    "Caroline shoots an annoyed look at Daisy."
    caroline "With all due respect Ms. Tanwen, we’ve been together in this class for weeks and NOW you want to do introductions?"
    caroline "Seriously, at this point I might as well call them Male Student A or B."
    image stage_9_event_35 = "/teacher/events/stage9/35.webp"
    scene stage_9_event_35
    ms "Actually, my name is-"
    image stage_9_event_36 = "/teacher/events/stage9/36.webp"
    scene stage_9_event_36
    teacher "All the more reason we should get along. Now would you please formerly tell us your name."
    image stage_9_event_37 = "/teacher/events/stage9/37.webp"
    scene stage_9_event_37
    caroline "Fine. My name is Caroline. Can we start now?"
    image stage_9_event_38 = "/teacher/events/stage9/38.webp"
    scene stage_9_event_38
    teacher "In a moment, first we need to bring up your eating partner. Vicky, would you please come up here?"
    image stage_9_event_39 = "/teacher/events/stage9/39.webp"
    scene stage_9_event_39
    "In direct contrast, the next girl that approaches Daisy seems to revel in the attention of her classmates."
    "There’s a wide smile on her face as she saunters up to the front like a super model."
    image stage_9_event_40 = "/teacher/events/stage9/40.webp"
    scene stage_9_event_40
    "There’s no sense of hesitation as she waves about her long, red hair and shows off her skimpy outfit."
    image stage_9_event_41 = "/teacher/events/stage9/41.webp"
    scene stage_9_event_41
    teacher "Glad to see you have some pep in your step for the contest."
    vicky "It’s how I approach all of life’s challenges. Besides, it’s not going to be difficult winning against her."
    image stage_9_event_42 = "/teacher/events/stage9/42.webp"
    scene stage_9_event_42
    caroline "You want to say that again, you airheaded bimbo?"
    vicky "I said, you’re no match for me. Aww, what’s wrong? Worried about me beating you in something other than being sweaty and gross?"
    image stage_9_event_43 = "/teacher/events/stage9/43.webp"
    scene stage_9_event_43
    "Before things get too heated, Daisy steps forward to push them apart."
    teacher "Save that aggression for the contest. My teachings may be on the unorthodox side, but I still won’t allow fighting in here. Am I understood?"
    caroline "Yes, Ms. Tanwen."
    vicky "Yes, Ms. Tanwen."
    teacher "Good. Now get in position."
    image stage_9_event_44 = "/teacher/events/stage9/44.webp"
    scene stage_9_event_44
    teacher "Before we begin, let me tell you a little about the subject for today’s contest: pizza."
    teacher "It’s a dish that comes in a plethora of various shapes and sizes."
    image stage_9_event_45 = "/teacher/events/stage9/45.webp"
    scene stage_9_event_45
    teacher "From different cooking styles to a near endless possibility of toppings, pizzas can be quite the culinary treat if treated the right way."
    teacher "That being said, a near constant among most of them is that they aren’t the healthiest of meals. This makes them perfect for the up and coming feedees to stuff themselves silly."
    image stage_9_event_46 = "/teacher/events/stage9/46.webp"
    scene stage_9_event_46
    teacher "Are you two ready?"
    vicky "As I’ll ever be, Ms. Tanwen!"
    caroline "Let’s just get this over with."
    teacher "Then on my mark. Get set. GO!"
    image stage_9_event_47 = "/teacher/events/stage9/47.webp"
    scene stage_9_event_47
    "Upon Daisy’s shout, the two girls begin to eat the first pizza."
    "As the women continue to devour the slices, the class breaks out into their usual cheers in order to keep them motivated."
    "Though they push forward to try and come out on top, it’s only a matter of time before reality sets in."
    image stage_9_event_48 = "/teacher/events/stage9/48.webp"
    scene stage_9_event_48
    "Caroline and Vicky’s eating slows to a crawl after their second box of pizza."
    image stage_9_event_49 = "/teacher/events/stage9/49.webp"
    scene stage_9_event_49
    "Though their spirits are willing to push forward in order to claim victory, there’s only so much their bodies can handle."
    image stage_9_event_50 = "/teacher/events/stage9/50.webp"
    scene stage_9_event_50
    "Try as they might to keep going, they are forced to stop half way through their 3rd pizza."
    image stage_9_event_51 = "/teacher/events/stage9/51.webp"
    scene stage_9_event_51
    "The match comes to a premature end as both competitors step back to nurse their overly swollen guts."
    image stage_9_event_52 = "/teacher/events/stage9/52.webp"
    scene stage_9_event_52
    vicky "Come on. Just one more."
    image stage_9_event_53 = "/teacher/events/stage9/53.webp"
    scene stage_9_event_53
    caroline "You need to stop. We’re both about to burst. I don’t know how Ms. Tanwen does it."
    image stage_9_event_54 = "/teacher/events/stage9/54.webp"
    scene stage_9_event_54
    teacher "With lots of practice and a little bit of help."
    image stage_9_event_55 = "/teacher/events/stage9/55.webp"
    scene stage_9_event_55
    "Picking up what’s left of the pizza boxes, Daisy proceeds to effortlessly finish off what’s left."
    image stage_9_event_56 = "/teacher/events/stage9/56.webp"
    scene stage_9_event_56
    teacher "I do hope you all found this lecture enlightening."
    teacher "I know I gained quite a bit from this, in terms of both knowledge and weight. Vicky and Caroline, do you have any comments or questions?"
    "Though they try to speak, all that comes out are pained groans as they try to deal with their full bellies."
    image stage_9_event_57 = "/teacher/events/stage9/57.webp"
    scene stage_9_event_57
    teacher "Ah, I probably should have expected that. Why don’t the two of you digest for a bit?"
    teacher "In the meantime, the rest of you can head out for the day."
    image stage_9_event_58 = "/teacher/events/stage9/58.webp"
    scene stage_9_event_58
    "As you begin to walk out with the others, you can’t help noticing how Caroline and Vicky are staring at you."
    "Seeing you lingering at the door, Daisy sends you off with a wink. Left to wonder what exactly she’s planning, you decide to head home for the day."
    #(NOTE: After this, Caroline and Vicky should become available for the study sessions)
    stop music fadeout 1.0
    if recollection == False:
        $ teacher.weight += 0.5
        $ teacherstage9event = 0
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Teacher_Stage_9_Event_2:
    #Daisy Stage 9.2 Event
    #(NOTE: The following should take place when the player goes to the gym, after experiencing Daisy’s first stage 9 event)

    scene gym
    play music "<loop 0.2 from 19>/music/gym.ogg" if_changed fadein 1.0
    "Arriving at the gym for your usual routine, you can’t help noticing that the place is a lot emptier than usual."
    "This provides the unintended benefit of all of the machines being free and making it easy to spot a familiar face approaching you."
    image stage_9_event_9 = "/teacher/events/stage9/9.webp"
    scene stage_9_event_9
    teacher "Hello there, my favorite student. Good to see you working hard to keep your brain and muscles in top shape."
    teacher "Would you like to join me? I could use an exercise partner."
    image stage_9_event_10 = "/teacher/events/stage9/10.webp"
    scene stage_9_event_10
    "Seeing no reason to deny her request, you work alongside her for your gym session."
    "Though you try to keep up with your usual pace, you can’t help from being distracted."
    image stage_9_event_11 = "/teacher/events/stage9/11.webp"
    scene stage_9_event_11
    "In spite of the fat clinging to her body, Daisy seems to be putting in the effort to get through the routine."
    image stage_9_event_12 = "/teacher/events/stage9/12.webp"
    scene stage_9_event_12
    "Whether this is from a genuine desire to exercise or just a means to tease you is answered by the sly grin she gives you once she notices you staring."
    image stage_9_event_13 = "/teacher/events/stage9/13.webp"
    scene stage_9_event_13
    teacher "That felt good, but I think I’m tired out. Shame, I didn’t really work up the sweat I wanted."
    pc "There’s always the sauna."
    teacher "Hmm, that might be just what I’m looking for. Lead the way."
    image stage_9_event_14 = "/teacher/events/stage9/14.webp"
    scene stage_9_event_14
    play music "/music/sauna.ogg" if_changed
    "As you enter the sauna you pause as you notice a note hanging on the wall."
    "Note: “[playername], I had to head out early today to get some supplies for the gym. Feel free to use the private sauna after your workout. -Trista.”"
    image stage_9_event_15 = "/teacher/events/stage9/15.webp"
    scene stage_9_event_15
    "Finished reading over the message, you look at Daisy with an interested look on her face."
    teacher "Hmm, I thought so."
    pc "What are you talking about?"
    image stage_9_event_16 = "/teacher/events/stage9/16.webp"
    scene stage_9_event_16
    teacher "Well, the last few times I came here, I swore I heard some familiar moans coming from this direction."
    teacher "Looking to get some more exciting exercise routines in, huh?"
    #CHOICE: A) It’s not what you think or B) Yeah, you got me
    menu:
        "It’s not what you think.":
            teacher "Come on now. Don’t try to deny it. I’ve more than once seen Trista and Katrine come out of here with grins on their faces."
        "Yeah, you got me.":
            teacher "That would explain Katrine and Trista’s cheerful moods after those sessions inside."
    #(NOTE: Regardless of choice, the following should play out.)
    image stage_9_event_17 = "/teacher/events/stage9/17.webp"
    scene stage_9_event_17
    teacher "Regardless, I’m happy that you’ve found a pair of excellent workout partners. Especially considering how shapely they’re turning out to be."
    teacher "I’ve been keeping my eye on them on behalf of the Followers for quite a while."
    teacher "Ah, but where are my manners. Let’s not keep standing out here gossiping about your other feedees. We’ll continue on inside."
    image stage_9_event_18 = "/teacher/events/stage9/18.webp"
    scene stage_9_event_18
    "While you build up the steam Daisy gets herself comfortable."
    image stage_9_event_19 = "/teacher/events/stage9/19.webp"
    scene stage_9_event_19
    teacher "Well, this place is cozy. No wonder those girls chose this as their private room. I’m especially happy that it’s a mixed sauna."
    pc "What do you mean?"
    teacher "I mean, you get to enjoy staring at my body for a little longer."
    image stage_9_event_20 = "/teacher/events/stage9/20.webp"
    scene stage_9_event_20
    "With a flick of her arm, Daisy tosses off her towel to leave herself completely nude."
    teacher "Ah, feels good to let it all air out. Don’t be shy. Come join me."
    image stage_9_event_21 = "/teacher/events/stage9/21.webp"
    scene stage_9_event_21
    teacher "There, doesn’t that feel better? Now you can get a better look at my sweat-slicked body."
    #CHOICE: A) You don’t mind me staring? or B) With pleasure
    menu:
        "You don’t mind me staring?":
            teacher "Of course not. Please, this isn’t the first time you’ve seen me naked and then some."
        "With pleasure.":
            teacher "Of course. As long as you’re alright with me doing the same for you."
    #(NOTE: Regardless of choice, the following should play out.)
    "You spend time in the sauna letting your body release any leftover stress. Conversation between you and Daisy is minimal as you merely enjoy each other’s company."
    teacher "Hey [playername], I have a question."
    image stage_9_event_22 = "/teacher/events/stage9/22.webp"
    scene stage_9_event_22
    teacher "Is there a reason you're making me be the one to make the first move?"
    teacher "After all, we're alone. And naked."
    image stage_9_event_59 = "/teacher/events/stage9/59.webp"
    scene stage_9_event_59
    "Wrapping your arms around her body, you pull her in close."
    pc "I was enjoying the moment, and the view."
    pc "But don't be mistaken in thinking I don't desire you."
    teacher "I know you do."
    teacher "I was simply wondering what was holding you back."
    pc "Perhaps I'm too used to the default in our teacher/student dynamic."
    pc "And I have grown too comfortable letting you be the one to control your classroom."
    image stage_9_event_60 = "/teacher/events/stage9/60.webp"
    scene stage_9_event_60
    "Invigorated by the feeling of her sweaty belly folds pressing against your skin, you move forward to look her deep in her fiery eyes."
    pc "But you're right, we now find ourselves in a new environment."
    pc "And I'd love to show you exactly what I've been thinking about doing to your sweaty, naked body since we got in here."
    pc "Hell, since you started glistening from your workout."
    image stage_9_event_61 = "/teacher/events/stage9/61.webp"
    scene stage_9_event_61
    "Caressing each other's body increases the heat in the already warm room."
    teacher "Please do."
    teacher "It's your turn to give me instructions."
    teacher "Tell your teacher exactly what to do, and she will obey."
    pc "Bend over and place your hand against the wall."
    image stage_9_event_62 = "/teacher/events/stage9/62.webp"
    scene stage_9_event_62
    "She obeys."
    teacher "Like this?"
    pc "Great form, Teach."
    pc "The way you are arching your back is putting you on track to earn yourself an A."
    teacher "I aim to please."
    "You take a step forward and grab her wide hips."
    image stage_9_event_63 = "/teacher/events/stage9/63.webp"
    scene stage_9_event_63
    teacher "Oh!"
    teacher "Now what do you want me to-"
    image stage_9_event_64 = "/teacher/events/stage9/64.webp"
    scene stage_9_event_64
    window hide
    pause
    teacher "OH!"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage9/sex1.webm" loop
    show movie with dissolve
    window hide
    pause
    teacher "That's it!"
    teacher "Just like that!"
    teacher "I mean... am I doing it right, Teach?"
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage9/sex2.webm" loop
    show movie with dissolve
    window hide
    pause
    pc "That's Professor to you."
    teacher "Ohhh."
    teacher "Is there a classmate in particular you want me to roleplay as?"
    pc "Maybe next time."
    pc "I don't think there is anyone in class I could confuse you with from the back."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage9/sex3.webm" loop
    show movie with dissolve
    window hide
    pause
    pc "Or the front, for that matter."
    teacher "Oh? Is there someone in class you wish was a little... bigger?"
    pc "Hard to say. My eyes are usually on the teacher."
    teacher "Aw, you charmer."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage9/sex4.webm" loop
    show movie with dissolve
    window hide
    pause
    teacher "But out of curiousity, would the school girl costume be of any interest sometime?"
    pc "Are you offering to dress up in a short red checkered skirt and pigtails?"
    teacher "Maybe!"
    pc "Can't say I'm against the idea."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage9/sex5.webm" loop
    show movie with dissolve
    window hide
    pause
    teacher "Ohhh!"
    teacher "Imagining it now, huh?"
    teacher "I wonder what other kinds of roleplay we could get into."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage9/sex6.webm" loop
    show movie with dissolve
    window hide
    pause
    pc "Let's not get ahead of ourselves now."
    pc "I'm in a public sauna fucking my actual teacher."
    pc "If the wrong person walked in right now, we'd both be screwed."
    pc "We're living a roleplay fantasy in this very moment."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage9/sex7.webm" loop
    show movie with dissolve
    window hide
    pause
    teacher "Yesss!"
    teacher "Your dick is my fantasy!"
    teacher "Did I just say that out loud?"
    pc "Say what?"
    teacher "Good."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage9/sex8.webm" loop
    show movie with dissolve
    window hide
    pause
    teacher "So! Good!"
    teacher "I'm close!"
    pc "Me too."
    teacher "Just... a little longer!"
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/teacher/events/stage9/sex9.webm" loop
    show movie with dissolve
    window hide
    pause
    teacher "Ohhh Goddess!"
    teacher "Just like that!"
    teacher "Professor, student, whatever you want me to call you right now!"
    teacher "[playername]! [playername]! [playername]!"
    stop movie
    image stage_9_event_65 = "/teacher/events/stage9/65.webp"
    scene stage_9_event_65
    teacher "Yesss!"
    pc "Haaa!"
    teacher "So good!"
    "You pull out and absolutely cover her."
    image stage_9_event_66 = "/teacher/events/stage9/66.webp"
    scene stage_9_event_66
    window hide
    pause
    teacher "Was that a lot?"
    teacher "It felt like a lot."
    pc "You're going to need a shower, yeah."

    image stage_9_event_67 = "/teacher/events/stage9/67.webp"
    scene stage_9_event_67
    "Daisy stumbles as she tries to gain her balance."
    teacher "You're incredible."
    pc "Ah, thanks!"
    pc "By the way, this is going to help your grade, but you're still going to need to put in some work in class."
    teacher "Aw, what if I come in early and help you grade papers every day from under your desk?"
    pc "That would be the kind of good work ethic I'm talking about."
    image stage_9_event_68 = "/teacher/events/stage9/68.webp"
    scene stage_9_event_68
    "After cleaning up the sauna, you and Daisy move over to the showers to clean each other off."
    "Once you’ve properly washed away the remnants of your little indulgence, the two of you part ways."
    teacher "Thanks for the workout, gym partner!"
    pc "Is that another roleplay for us?"
    teacher "I'd say we're back in the realms of reality."
    pc "I'll take it."
    pc "Bye, Daisy."
    pc "It was a pleasure as always."
    stop music fadeout 1.0
    scene player_room
    "You receive a message. It’s Daisy."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Daisy', dialogue=dialogue_one)
    $ msg ("Well, well… I have to say, you played the role quite well, ‘Professor.’", who=1)
    pause
    $ msg ("Firm, yet… attentive. I think I learned a lot in that little lesson of ours. 😏", who=1)
    "A few moments later, another message pops up."
    $ msg ("Maybe next time, I’ll have to be the strict one. Wouldn’t want my student getting too full of himself, now would we?", who=1)
    pause
    $ msg (None, who=1, pic="stage9_daisy")
    pause
    $ msg ("Now be a good boy and make sure you’re ready for our next session. I expect full participation. 😉", who=1)
    pause
    $ hide_messenger()

    $ teacherstage9event2 = 0
    return


label Teacher_Stage_10_Event:
    image stage_10_event_before_event = "/teacher/events/stage10/before_event.webp"
    scene stage_10_event_before_event
    play music "/music/university.ogg" if_changed
    "You arrive at class to see that a desk has once more been pushed to the front of the room and loaded down with an excessive amount of food."
    "Looking over the collection of fresh donuts from The Sugar Shop, you’re tempted to eat them yourself."
    "However, you and the rest of the class are wise enough to leave the pile of sweets alone. Taking your seat, you join the others in watching and waiting for…"
    image stage_10_event_arrive = "/teacher/events/stage10/arrive.webp"
    scene stage_10_event_arrive
    pc "A coat?"
    fs "Pig ears?"
    ms "Fishnet stockings?"
    "Answering the questions with only a playful smile, Daisy makes her way to the front of the class."
    image stage_10_event_greet = "/teacher/events/stage10/greet.webp"
    scene stage_10_event_greet
    teacher "Good morning, students."
    s "Good morning, Ms. Tanwen."
    image stage_10_event_1 = "/teacher/events/stage10/1.webp"
    scene stage_10_event_1
    teacher "I’m assuming you’ve all seen the donuts and can make an educated guess on what they’re for."
    teacher "Today, my goal will be to eat all of them in a single sitting. It should make for a thrilling challenge."
    image stage_10_event_2 = "/teacher/events/stage10/2.webp"
    scene stage_10_event_2
    "Daisy begins to undo the sash around her coat, demanding the absolute attention of the entire room."
    teacher "Before I start, let me get a little more comfortable."
    teacher "As much as I would like to have worn this out in public, I do have to look semi-decent during my usual transit. You get to be the lucky ones to see me as I truly am."
    "Finishing undoing the sash, Daisy flings her coat away to reveal…"
    image stage_10_event_3 = "/teacher/events/stage10/3.webp"
    scene stage_10_event_3
    teacher "A fat pig."
    fs "Woah, what the hell?"
    ms "So damn sexy!"
    teacher "I do hope you all like the way I look."
    image stage_10_event_4 = "/teacher/events/stage10/4.webp"
    scene stage_10_event_4
    teacher "Especially since it took me a while to find an outfit suited for a stuffing session. This is a little on the tight side, but I think it will do just fine."
    image stage_10_event_5 = "/teacher/events/stage10/5.webp"
    scene stage_10_event_5
    teacher "Thankfully, it comes with plenty of free space in the back to keep me comfortable. But that’s enough talking, let’s move ahead to today’s lesson."
    image stage_10_event_6 = "/teacher/events/stage10/6.webp"
    scene stage_10_event_6
    teacher "I’ll admit I might have gone a little overboard when I bought this many."
    ms "Don’t say that. I know you can do it."
    fs "He’s right. You ate way more during your competitions with Ms. Luna."
    teacher "Why, thank you for the confidence boost. I really appreciate it."
    image stage_10_event_7 = "/teacher/events/stage10/7.webp"
    scene stage_10_event_7
    teacher "Onto the actual teaching portion, donuts are basically condensed sugar bombs."
    teacher "The amount of calories before me is absolutely astounding. On top of that, they have almost no nutritional value."
    teacher "Some even refer to them as having empty calories. What they lack in actual nutrition is more than made up for by their tastiness."
    image stage_10_event_8 = "/teacher/events/stage10/8.webp"
    scene stage_10_event_8
    teacher "That’s enough talking for now. Let’s see how many of these sweet treats I can actually eat. Wish me luck!"
    image stage_10_event_9 = "/teacher/events/stage10/9.webp"
    scene stage_10_event_9
    "Picking up the first donut, Daisy sinks her teeth into it and lets out a pleasant hum."
    teacher "The taste definitely helps. I’d offer you all some, but you’ll have to excuse a greedy piggy for wanting all of these for herself."
    image stage_10_event_10 = "/teacher/events/stage10/10.webp"
    scene stage_10_event_10
    "Upon savoring the last bite of the initial serving of donuts, she turns her attention towards the rest of the pile."
    "She attacks them like a rabid beast, sometimes devouring a whole one in as little as three bites."
    image stage_10_event_11 = "/teacher/events/stage10/11.webp"
    scene stage_10_event_11
    "Her initial breakneck speed begins to slow after she finishes off a few of the boxes. She pauses for a moment to wipe her face clean before taking a deep breath."
    teacher "Oof, I think these things are starting to get to me. I’m not sure how much further I can go."
    fs "Come on. You can handle a few more boxes, Ms. Tanwen!"
    ms "Yeah. Show those donuts who’s boss!"
    image stage_10_event_12 = "/teacher/events/stage10/12.webp"
    scene stage_10_event_12
    "Though the students’ words are enough to reinvigorate her, after only a single box she slows down again. Lazily swinging her head to the side, she locks her gaze with yours."
    teacher "[playername], would you mind helping me out?"
    "Nodding in agreement, you get up from your seat."
    image stage_10_event_13 = "/teacher/events/stage10/13.webp"
    scene stage_10_event_13
    "As you pick up a box of donuts, she takes a seat atop her desk."
    teacher "There. This should be the perfect spot to finish off the rest. You may begin when ready."
    "Opening up her mouth wide, she stares at you intently in anticipation for the start. Pulling out the first donut, you carefully push it past her waiting lips."
    image stage_10_event_14 = "/teacher/events/stage10/14.webp"
    scene stage_10_event_14
    "As you continue to stuff her with donuts, you notice how much larger her belly has grown since the lesson started."
    "Wondering just how much more her body can take, you keep up the task of feeding her."
    image stage_10_event_15 = "/teacher/events/stage10/15.webp"
    scene stage_10_event_15
    "The empty boxes begin to pile up as you go on, gradually becoming taller than the stack of donuts yet to be eaten."
    image stage_10_event_16 = "/teacher/events/stage10/16.webp"
    scene stage_10_event_16
    "Witnessing Daisy endure through this onslaught of sugar firsthand; it truly feels like her stomach capacity in endless. However, reality sets in as she grasps your wrist to make you stop."
    image stage_10_event_17 = "/teacher/events/stage10/17.webp"
    scene stage_10_event_17 with vpunch
    "Holding onto her overstuffed belly, she leans back to let out a huge burp."
    teacher "Yeah, I think that’ll be BWOOOOOORRRPPP enough for me."
    image stage_10_event_18 = "/teacher/events/stage10/18.webp"
    scene stage_10_event_18
    window hide
    pause
    teacher "Thank you a lot for feeding-UUUUURRRP!"
    "At the very tail end of the belch I hear her costume begin to tear."
    image stage_10_event_19 = "/teacher/events/stage10/19.webp"
    scene stage_10_event_19
    window hide
    pause
    "One last burp is enough to snap apart her outfit to leave her stuffed body even more exposed."
    "Hastily grabbing at the remnants of her clothing, she manages to keep herself at least somewhat covered up."
    image stage_10_event_20 = "/teacher/events/stage10/20.webp"
    scene stage_10_event_20
    teacher "Sorry about that. I guess I let myself go a little too far there. [playername], could you help me with my coat?"
    "Grabbing the jacket, you help wrap it around her body, struggling to get it over her sizable belly bump."
    image stage_10_event_21 = "/teacher/events/stage10/21.webp"
    scene stage_10_event_21
    teacher "Thank you. Sorry, everyone. Guess I'm still not enough of a pig to take on this much food at once."
    fs "Don’t let it get to you. It was still very impressive."
    ms "Yeah. You were awesome."
    teacher "Thank you, class. I think that will do it for today's lesson. See you all tomorrow!"
    image stage_10_event_22 = "/teacher/events/stage10/22.webp"
    scene stage_10_event_22
    "While the rest of the class files out, you walk over to the remaining donuts and notice there are three untouched boxes."
    "As you ponder what to do with them, Daisy approaches to tap your shoulder."
    image stage_10_event_23 = "/teacher/events/stage10/23.webp"
    scene stage_10_event_23
    teacher "It would be a shame to let these go to waste. What would you say to helping me finish these off back at my place?"
    pc "Absolutely."
    teacher "Excellent. Help me get these into my car."
    image stage_10_event_24 = "/teacher/events/stage10/24.webp"
    scene stage_10_event_24
    stop music fadeout 1.0
    play music "/music/daisy.ogg" if_changed
    "A short drive later, you walk into Daisy’s living room holding the remaining donuts and place them on the sofa in the living room."
    teacher "There we are. And just in time too. I think my belly’s recovered from the initial binging. Let me give my body some room."
    image stage_10_event_25 = "/teacher/events/stage10/25.webp"
    scene stage_10_event_25
    "Tossing her coat onto the couch, Daisy proceeds to tear apart what remains of her pig costume."
    "Left only wearing the ears and stockings, she looks absolutely relieved as she stretches out her swollen gut."
    teacher "There. That’s much better."
    pc "What about your costume?"
    teacher "Don’t worry about it. I have plenty more in my closet. It’s one of the many perks of being a member of the Followers of Heset."
    image stage_10_event_26 = "/teacher/events/stage10/26.webp"
    scene stage_10_event_26
    "Sitting down on the couch, Daisy leans back and rubs her tummy."
    teacher "It’s quite big, isn’t it?"
    pc "Absolutely huge. I still can’t believe you ate so much."
    image stage_10_event_27 = "/teacher/events/stage10/27.webp"
    scene stage_10_event_27
    teacher "Would you like for it to get bigger?"
    pc "Do you really need to ask?"
    teacher "Fair enough. Come over here. This fat piggy needs her donuts."
    image stage_10_event_28 = "/teacher/events/stage10/28.webp"
    scene stage_10_event_28
    "Squatting down next to her, you open up the first box and feed her a donut."
    teacher "Mmmm, just as tasty as ever. The feeling of it tumbling into my stretched out stomach is simply divine."
    "One after another you shove the donuts past her lips."
    "Gradually working through the boxes, you keep being pushed to continue by the sound of her pleased hums and the sight of her engorging belly."
    "Through your combined teamwork, Daisy manages to finish off the last donut before flopping down on the couch."
    image stage_10_event_eventend = "/teacher/events/stage10/eventend.webp"
    scene stage_10_event_eventend
    teacher "That was excellent. Would you mind cleaning these up? I don’t think I can move right now."
    pc "Not a problem."
    "Picking up the empty boxes you toss them into the trash and wash the leftover icing from your fingers."
    "Returning to the living room, you find the plumped up piggy peacefully sleeping off the indulgent meal."
    "Not wanting to wake her up from her blissful food coma, you head home."
    stop music fadeout 1.0
    if recollection == False:
        $ teacher.weight += 1
        $ teacherstage10event = 0
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Teacher_Stage_11_Event:
    image stage_11_event_arrive = "/teacher/events/stage11/arrive.webp"
    scene stage_11_event_arrive
    play music "/music/university.ogg" if_changed
    "Upon seeing Daisy arrive to class wearing another black coat, you and the rest of the class begin to ponder what exactly she has planned for the day’s lesson."
    ms "Is she going to pig out again?"
    fs "I don’t think so. She’s not wearing any ears. That pattern on her stockings look familiar, but I can’t quite figure out how."
    image stage_11_event_greet = "/teacher/events/stage11/greet.webp"
    scene stage_11_event_greet
    teacher "Hello students."
    s "Hello Ms. Tanwen."
    teacher "Time for another special lesson."
    image stage_11_event_1 = "/teacher/events/stage11/1.webp"
    scene stage_11_event_1
    "Tossing her coat to the side, Daisy stands before the class to show off her body clad in a cow-patterned outfit."
    "What little material that clings to her serves to emphasize the various lumps of fat across her body that are no doubt a result of her weekly feedings."
    teacher "As you can see, I’ve picked an outfit this time to give my belly plenty of room to spread out."
    image stage_11_event_2 = "/teacher/events/stage11/2.webp"
    scene stage_11_event_2
    teacher "It’s going to be a godsend for today’s session. I intend to stretch out this cute belly of mine as far as it can go."
    image stage_11_event_3 = "/teacher/events/stage11/3.webp"
    scene stage_11_event_3
    teacher "To do this, I will be showing you all a new feeding technique. It is a fast and efficient way of really packing on the pounds."
    image stage_11_event_4 = "/teacher/events/stage11/4.webp"
    scene stage_11_event_4
    teacher "Before that, I must ask that you allow me to indulge myself a bit. This beautiful outfit has a special place in my heart."
    teacher "I’m a huge fan of cows, so this costume really resonates with me."
    image stage_11_event_5 = "/teacher/events/stage11/5.webp"
    scene stage_11_event_5
    teacher "Not to mention how nicely it shows off my body. Especially the fat around my butt cheeks. Wouldn’t you agree?"
    "Though she doesn’t turn her face towards the class, you can all sense the smile on her face as one after another the students speak up to reassure how attractive she is."
    ms "That is a smoking sexy ass if I’ve ever seen one!"
    "Some more blunt than others."
    image stage_11_event_6 = "/teacher/events/stage11/6.webp"
    scene stage_11_event_6
    teacher "To prepare for the day’s session, I’ve taken a special drug to relax my stomach muscles."
    teacher "This way, I'll be able to fit a lot more inside of me. That's all the precautions covered. Now then, allow me to inform you of the actual method."
    image stage_11_event_10 = "/teacher/events/stage11/10.webp"
    scene stage_11_event_10
    "Reaching beneath her desk, Daisy fumbles around until she pulls out a remote and clicks a button. Part of the ceiling near her desk opens up to allow a long hose affixed to a nozzle to descend."
    "Walking over to the funnel, Daisy grasps the end and holds it up for everyone to see."
    teacher "I will be funnel feeding myself today. It is an advanced technique that allows for large amounts of liquid food to quickly enter the body."
    image stage_11_event_11 = "/teacher/events/stage11/11.webp"
    scene stage_11_event_11
    "Rolling a chair underneath the tube, she takes her seat. Grasping the nozzle with one hand, she holds up a remote to show off to the class."
    teacher "This remote will control the flow of the liquid. If I am in any danger, I can immediately shut it off."
    teacher "That being said, I don’t intend to give up until I’ve swallowed every last drop. Now without further ado…"
    "Upon pressing the button, Daisy sets the remote down and quickly shoves the nozzle into her mouth."
    "Leaning back in her seat, she and the rest of the class settles in as her feeding commences."
    window hide
    $ movielength = 43
    $ movieplaying = "/images/teacher/events/stage11/12.webm"
    call screen custommoviescreen
    image stage_11_event_13 = "/teacher/events/stage11/13.webp"
    scene stage_11_event_13
    "Just as it looks like she is about to pop, Daisy uses the remote once more to make the machinery above begin to whir down."
    "Releasing the hose from her mouth, she sends it back up the ceiling with another press of the button."
    "Looking quite satisfied with herself, she leans back to massage her belly and show it off to the class."
    teacher "This feels amazing."
    image stage_11_event_14 = "/teacher/events/stage11/14.webp"
    scene stage_11_event_14
    "Getting up from her chair, Daisy shows off the side effects of her rapid feeding as she slowly waddles her way to the front of the class."
    teacher "Didn’t think it would be this hard just moving around with such a stuffed stomach. I’ll have to keep that in mind for the future."
    image stage_11_event_15 = "/teacher/events/stage11/15.webp"
    scene stage_11_event_15
    "Though it’s a struggle, she eventually makes her way back to her usual teaching spot."
    teacher "There we go. I hope you all learned something from watching me fill my belly to the brim."
    image stage_11_event_16 = "/teacher/events/stage11/16.webp"
    scene stage_11_event_16
    teacher "If you recall one of my previous lessons, the further we stretch out the stomach the bigger it will become."
    teacher "In addition, in the coming weeks I have something special planned for you all."
    teacher "I will be inviting two people into class to go through similar feeding sessions."
    image stage_11_event_17 = "/teacher/events/stage11/17.webp"
    scene stage_11_event_17
    teacher "Of course, there is more to it than that. For now, I’ll keep it a secret to leave you all in suspense."
    image stage_11_event_18 = "/teacher/events/stage11/18.webp"
    scene stage_11_event_18
    teacher "Now if you’ll all excuse me, this fat cow is going to waddle her way home to let all of this liquid nourishment digest."
    teacher "Then again, maybe it would be better for me to stay here a while since it’s so hard to move around."
    image stage_11_event_19 = "/teacher/events/stage11/19.webp"
    scene stage_11_event_19
    teacher "That will be all for now. Have a good day!"
    "Following the others out of class, you wave goodbye to Daisy and head home."
    stop music fadeout 1.0
    if recollection == False:
        $ teacher.weight += 1
        $ teacherstage11event = 0
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Teacher_Stage_11_Event_2:
    #Daisy Stage 11.2 Event
    #(NOTE: The following should take place randomly when the player is working at Bunny Bites after the first stage 11 event with Daisy)

    #IMAGE: The counter of Bunny Bites
    "Your usual workflow is interrupted as you feel a tap on your shoulder."
    #IMAGE: One of the Bunny Bites waitresses speaking to the player (NOTE: Should be determined by whoever is on shift at the time.)
    marie "We just got a large delivery order. Mind making a run for us? We’ll pay you for a full day’s work."
    "Peeking at the address, you realize that the food is for Daisy. Will you take the job?"
    menu:
    #CHOICE: A) Yes or B) No
        "Yes":
            marie "Thank you so much. Good luck with the delivery."
        "No":
            marie "That’s fine. I’m sure we can get someone else to do the run."
            return
    #(NOTE: If the player chooses B) No, the Bunny Bites shift will continue as normal. If the player chooses A) they will be paid for a full shift’s work and then transition to delivering to Daisy’s house)
    #IMAGE: At Daisy’s front door with Daisy greeting the player
    "Trekking through town with arms laden with food, you eventually arrive at Daisy’s house."
    "When she answers the door, she bares a smile for both you and the delicious meals in your arm."
    teacher "Good to see my best student hard at work. Come on in."
    #IMAGE: Daisy sitting on the couch with food.
    teacher "Mind helping me work through this? I’ll give you a little extra credit."
    menu:
    #CHOICE: A) Leave or B) Stay and feed her
        "Leave":
            teacher "You’re busy? I understand. Some other time then."
            #(NOTE: After this the player should return home)
            $ teacherstage11event2 = 0
            return
        "Stay and feed her":
            teacher "Excellent. Then let’s get started."
            #(NOTE: From here, the scene will transition into Daisy’s home feeding sessions. If possible, make all of the levels of feeding her free since this is all her order from Bunny Bites)
            $ teacherstage11event2 = 0
            return

label Teacher_Stage_12_Event:
    #Scene: Poolside Daisy Date
    #(NOTE: The following should take place during the weekend when the player chooses to visit Daisy at her house.)
    "You decide to message Daisy to see if she’s up for a visit."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Daisy', dialogue=dialogue_one)
    $ msg ("Are you free this weekend? I could come over for another session if you’re up for it.")
    pause
    $ msg ("I am free and willing, but I’m looking for a change of scenery. How about we meet at your house?", who=1)
    pause
    $ msg ("Really? It’s not that special. Just a standard two-story house with a yard and a pool.")
    pause
    $ msg ("You have a pool?", who=1)
    pause
    $ msg ("Yeah. I don’t use it often though.")
    pause
    $ msg ("Then we’ll have to change that. I’ll see you in a little bit.", who=1)
    pause
    $ hide_messenger()

    "Taking a good guess at what Daisy intends to do, you change into your swim trunks and wait for her arrival."

    image stage_12_event_1 = "/teacher/events/stage12/1.webp"
    scene stage_12_event_1
    play music "/music/beach.ogg" if_changed
    "When Daisy finally arrives, you find it difficult not to gawk at the way her swimsuit shows off her body."
    image stage_12_event_2 = "/teacher/events/stage12/2.webp"
    scene stage_12_event_2
    teacher "I’d thank you for inviting me over, but that expression alone says you’re already enjoying yourself quite a lot."
    pc "Sorry. You just look amazing in that suit."
    teacher "Why, thank you. I do like it, but it still leaves quite a lot exposed to the elements."

    image stage_12_event_3 = "/teacher/events/stage12/3.webp"
    scene stage_12_event_3
    "Finding a poolside chair, Daisy holds up a bottle of sunscreen and points it towards you."
    teacher "Would you mind putting this on me? I’d rather not show up to class on Monday as red as a lobster."
    pc "You can count on me."
    image stage_12_event_4 = "/teacher/events/stage12/4.webp"
    scene stage_12_event_4
    window hide
    pause
    "While you’re a little nervous at first, the uneasiness goes away after the first few slides of your hands across her back."
    "To make sure every inch of her skin is covered, you carefully guide your fingers along any area that could be burnt. Just as your about to finish, Daisy tugs on your arm."
    teacher "Very good. Now let’s do the front. Oh, and no need to be careful with where you touch. I need every inch to be protected of course."
    image stage_12_event_5 = "/teacher/events/stage12/5.webp"
    scene stage_12_event_5
    window hide
    pause
    "Following her orders, you back off for a moment to let her roll over. With her body in place, you reach out to resume covering her in lotion, only to be pulled on top of her."
    teacher "Don’t be shy. Really get in there."
    "Daisy takes off her bikini top."
    image stage_12_event_6 = "/teacher/events/stage12/6.webp"
    scene stage_12_event_6
    window hide
    pause
    "Finally figuring out that this act is for more than just skin protection, you lotion up your fingers and reach out towards her chest."
    "Your boldness is rewarded with the sensation of getting to grope the added heft that’s been layered onto her breasts over the course of the semester."
    "While the feeling is heavenly, your attention in inevitably drawn elsewhere."
    image stage_12_event_7 = "/teacher/events/stage12/7.webp"
    scene stage_12_event_7
    window hide
    pause
    "Your hands make their way down in service of Daisy’s sizable gut. Pleasurable hums leave Daisy’s lips as you proceed to spread the lotion across her mid-section."
    "So lost in the sensation of getting to freely squeeze her belly rolls and fupa, it takes a moment for you to realize that she’s tapping your shoulder."
    teacher "I think that’ll do for now."
    pc "Sorry. I got a little carried away."
    teacher "It’s alright. You were just being thorough."
    image stage_12_event_8 = "/teacher/events/stage12/8.webp"
    scene stage_12_event_8
    "Finishing up with the sunscreen, the two of you dive into the pool. While you start doing a few laps, you eventually slow down to watch Daisy."
    "The way the water caresses her body as she glides through it makes you appreciate the results of the class’s efforts to fatten her up."
    "This awestruck stupor is broken by a call on your phone."
    "Climbing out of the pool, you pick it up off of one of the chairs and answer it."
    pc "Hello?"
    unknown "Hey. This is [playername]'s house, right? I've got your pizzas and I'm waiting at the door. Do you want it or not?"
    pc "Wait, I didn’t…"
    image stage_12_event_9 = "/teacher/events/stage12/9.webp"
    scene stage_12_event_9
    "You pause and look back to see Daisy take another lap across the pool. It doesn’t take long to put things together in your mind."
    unknown "You still there, dude?"
    pc "Yeah, I’ll be right there."
    image stage_12_event_10 = "/teacher/events/stage12/10.webp"
    scene stage_12_event_10
    "Hurrying up to the front door and accepting the delivery, you lumber back to the pool with the pizzas in hand."
    "Balancing the food on a table, you look for Daisy to find her wet body lounging on one of the chairs."
    teacher "I hope you don’t mind me ordering on your behalf. I needed a little extra food to make up for all of this exercise. I’m pretty worn out as is, so would you mind feeding me?"
    "With a nod of your head, you pick up one of the boxes and approach Daisy."
    image stage_12_event_11 = "/teacher/events/stage12/11.webp"
    scene stage_12_event_11
    window hide
    pause
    "Getting down on your knees, you hold up the first slice to Daisy’s face. Eagerly accepting it, she shows off just how hungry she is by downing it in a matter of seconds."
    "You waste little time giving her another slice, which she just as quickly gobbles up. Before you realize it, she’s eaten through the entire first box."
    pc "Hold on. Let me grab the next one."
    teacher "Would you mind handing me the box? I can feed myself, but I need you to take care of something else."
    image stage_12_event_12 = "/teacher/events/stage12/12.webp"
    scene stage_12_event_12
    window hide
    pause
    "After handing Daisy her pizza, you once more place your fingers on her stomach. Feeling her belly become tighter with each bite, you dutifully take on the task of massaging it to help her digest."
    image stage_12_event_13 = "/teacher/events/stage12/13.webp"
    scene stage_12_event_13
    "Your constant attention helps her through the second box before moving onto the third. Just as she opens up the fourth, you’re stopped from going any further."
    teacher "An excellent job, but I have another task for you. Would you mind taking care of my “other” needs?"
    if persistent.nosexscene == True:
        scene black with dissolve
        "Daisy and I had a great time together."
    else:
        image stage_12_event_14 = "/teacher/events/stage12/14.webp"
        scene stage_12_event_14
        window hide
        pause
        "With an eager nod, you get down on the ground and lift up her belly. Sliding your head in-between her thighs, you let her gut drop down onto your head."
        image stage_12_event_15 = "/teacher/events/stage12/15.webp"
        scene stage_12_event_15
        "Cradled on all sides by her soft flesh, you set to work dragging your tongue across her womanhood. Your efforts occasionally interrupt Daisy’s chewing noises with a cry of ecstasy."
        "Even as you focus all of your attention on bringing her to orgasm, she still finds the strength to shovel pizza down her gullet up until the moment she climaxes."
        image stage_12_event_16 = "/teacher/events/stage12/16.webp"
        scene stage_12_event_16
        "Feeling her body be overcome with euphoric shivers, you pull your head out just in time to hear her let out one last moan."
        "Though you attempt to stand up to clean up the empty pizza boxes, you’re stopped as she grasps your chin and brings you down to rest on her belly."
        "Keeping your head in place, she slides her fingers through your hair as she rocks you against her swollen gut."
        teacher "This was wonderful. Thank you for inviting me over."
        pc "It was my pleasure."

    "After lingering on Daisy’s body for a little while longer, you eventually clean up and she takes her leave."
    stop music fadeout 1.0
    scene player_room

    "You receive a message. It’s Daisy."
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Daisy', dialogue=dialogue_one)
    $ msg ("Now that… was a perfect afternoon. Sun, water, and more food than I could handle. You really know how to treat a lady.", who=1)
    pause
    $ msg ("I aim to please. You looked like you were in heaven.")
    pause
    $ msg ("Mmm, I was. And I can still feel it…", who=1)
    pause
    $ msg (None, who=1, pic="stage12_daisy")
    pause
    $ msg ("Careful, dear. Keep this up, and I might start expecting this kind of treatment all the time. 😏", who=1)
    pause
    $ hide_messenger()

    $ teacherstage12event = 0
    if recollection == False:
        $ teacher.weight += 0.5
        $ daytime += 1
        jump freetime
    return


#label Teacher_Stage_13_Event:
    if carolinestage1event4 == 0 and carolinestage2event == 1:
        scene university_looking_into_class3
    else:
        scene university_looking_into_class
    play music "/music/university.ogg" if_changed
    "Arriving to class, your nose picks up a familiar scent."
    image stage_13_event_1 = "/teacher/events/stage13/1.webp"
    scene stage_13_event_1
    "Your mouth starts to drool at the sight of the collection of pizzas at the front of the room. A glance towards the other students lets you see similar looks of wanting on their faces."
    "Whether it’s for the food itself or who is going to be eating them is left unknown until Daisy makes her appearance."
    image uni_sexy_teacher_arrive_event13 = "/teacher/13/0/arrive.webp"
    scene uni_sexy_teacher_arrive_event13
    teacher "Good morning, class."
    s "Good morning, Ms. Tanwen."
    image stage_13_event_2 = "/teacher/events/stage13/2.webp"
    scene stage_13_event_2
    teacher "I take it you all are dying to get on with today’s lesson. Any guesses as to what we’ll be doing?"
    ms "A pizza party?"
    fs "No, you idiot. She's obviously going to stuff herself again."
    image stage_13_event_3 = "/teacher/events/stage13/3.webp"
    scene stage_13_event_3
    teacher "I’m afraid that both of you are incorrect. While these pizzas are meant to be eaten as fast as possible, it won’t be by me."
    teacher "Two of your classmates have volunteered to be the subjects for today’s lesson. Let me go ahead and introduce them to you. Caroline, would you mind coming up here?"
    image stage_13_event_4 = "/teacher/events/stage13/4.webp"
    scene stage_13_event_4
    "A student that had remained mostly silent over the course of the semester stands up and begins to walk towards Daisy."
    "If her indie band T-shirt and red skirt weren't enough to ensure she was the center of the class's attention,"
    "her long strands of multi-coloured hair and near emotionless face are more than enough to make her stand out."
    image stage_13_event_5 = "/teacher/events/stage13/5.webp"
    scene stage_13_event_5
    "Disregarding the various murmurs from her fellow classmates, she makes her way to the front of the classroom and stands next to Daisy."
    teacher "Would you please introduce yourself to the class?"
    "Caroline shoots an annoyed look at Daisy."
    caroline "We’ve been together in this class for weeks and NOW you want to do introductions? Seriously, at this point I might as well call them Male Student A or B."
    ms "Actually, my name is-"
    teacher "All the more reason we should get along. Now, would you please formally tell us your name?"
    caroline "Ugh, fine. My name is Caroline. Can we start now?"
    teacher "In a moment. First we need to bring up your eating partner. Vicky, would you please come up here?"
    image stage_13_event_6 = "/teacher/events/stage13/6.webp"
    scene stage_13_event_6
    "In direct contrast, the next girl that stands up seems to revel in the attention of her classmates."
    "Showing off a wide smile as she saunters up to the front like a super model, she shows no hesitation as she waves about her long, red hair and shows off her skimpy outfit."
    image stage_13_event_7 = "/teacher/events/stage13/7.webp"
    scene stage_13_event_7
    teacher "Glad to see you have some pep in your step for the contest."
    vicky "It’s how I approach all of life’s challenges. Not like it’s going to be difficult winning against her."
    image stage_13_event_8 = "/teacher/events/stage13/8.webp"
    scene stage_13_event_8
    caroline "You want to say that again, you airheaded bimbo?"
    vicky "I said, you’re no match for me. Awww, what’s wrong? Did you go deaf from listening to all those crappy indie bands?"
    image stage_13_event_9 = "/teacher/events/stage13/9.webp"
    scene stage_13_event_9
    "Before things can get too heated, Daisy steps forward to push them apart."
    teacher "Save that aggression for the contest. Our class may be on the unorthodox side, but I still won’t allow fighting in here. Am I understood?"
    caroline "Yes, Ms. Tanwen."
    vicky "Yes, Ms. Tanwen."
    teacher "Good. Now get in position."
    image stage_13_event_10 = "/teacher/events/stage13/10.webp"
    scene stage_13_event_10
    teacher "Before we begin, let me tell you a little about the subject for today’s contest: pizza. It’s a dish that comes in a plethora of various shapes and sizes."
    teacher "From different cooking styles to a near endless possibility of toppings, pizzas can be quite the culinary treat if treated the right way."
    teacher "That being said, a near constant among most of them is that they aren’t the healthiest of meals. This makes them perfect for the up and coming feedees to stuff themselves silly."
    image stage_13_event_11 = "/teacher/events/stage13/11.webp"
    scene stage_13_event_11
    teacher "Are you two ready?"
    vicky "As ready as I'll ever be, Ms. Tanwen!"
    caroline "Let’s just get this over with."
    teacher "Then on my mark. Get set. GO!"
    image stage_13_event_12 = "/teacher/events/stage13/12.webp"
    scene stage_13_event_12
    "Upon Daisy’s shout, the two girls open up their first box of pizza and begin to eat."
    "As the women continue to devour the slices, the class breaks out into their usual cheers in order to keep them motivated."
    "Though they push forward to try and come out on top, it’s only a matter of time before reality sets in."
    image stage_13_event_13 = "/teacher/events/stage13/13.webp"
    scene stage_13_event_13
    "Caroline and Vicky’s eating slows to a crawl after their second box of pizza. Though their spirits are willing to push forward in order to claim victory, there’s only so much their bodies can handle."
    "Try as they might to keep going, they each are forced to stop halfway through their third pizza."
    image stage_13_event_14 = "/teacher/events/stage13/14.webp"
    scene stage_13_event_14
    "The match comes to a premature end as both competitors nurse their overly swollen guts."
    vicky "Come on. Just one more."
    caroline "You need to stop. We’re both about to burst. I don’t know how Ms. Tanwen does it."
    image stage_13_event_15 = "/teacher/events/stage13/15.webp"
    scene stage_13_event_15
    teacher "With lots of practice and a little bit of help."
    "Picking up what’s left of the pizza boxes, Daisy proceeds to effortlessly finish off what’s left."
    image stage_13_event_16 = "/teacher/events/stage13/16.webp"
    scene stage_13_event_16
    teacher "I do hope you all found this lesson enlightening. I know I gained quite a bit from this, in terms of both knowledge and weight. Vicky and Caroline, do you have any comments or questions?"
    "Though they try to speak, all that comes out are pained groans as they try to deal with their full bellies."
    teacher "Ah, I probably should have expected that. Why don’t the two of you go sit down to digest for a bit? In the meantime, the rest of you can head out for the day. Class dismissed."
    image stage_13_event_17 = "/teacher/events/stage13/17.webp"
    scene stage_13_event_17
    "As you begin to walk out with the others, you can’t help noticing how Caroline and Vicky are staring at you. Seeing you lingering at the door, Daisy sends you off with a wink."
    "Left to wonder what exactly she’s planning, you decide to head home for the day."
    stop music fadeout 1.0
    #(NOTE: After this, Caroline and Vicky should become available for the study sessions)
    if recollection == False:
        $ teacher.weight += 1
        $ teacherstage13event = 0
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

#label Teacher_Stage_13_Event_new:
    #(NOTE: The following should occur when the player is in their room during the evening time)

    "You receive a message from Daisy."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Daisy', dialogue=dialogue_one)
    $ msg ("Are you free tonight? I have a “reward” I want to give you for all of your hard work.", who=1)
    pause
    menu:
        "Sure, where did you want to meet up?":
            $ msg ("Sure, where did you want to meet up?")
            pause
            $ msg ("I’ll send you the address shortly. Make sure you’re there at 7pm sharp. It’s a very special place.", who=1)
            pause
            $ hide_messenger()
            "More than a little suspicious, you pack up an overnight bag and head over to Daisy’s house."
        "Maybe some other time.":
            $ msg ("Maybe some other time")
            pause
            $ msg ("I had an outfit picked out and everything too. Ah, well. We’ll try again another night.", who=1)
            pause
            $ hide_messenger()
            return

    "Somewhat concerned by what Daisy means by special, you get yourself together to head out for the evening."
    #IMAGE: Oriental restaurant lobby
    "Dressed in a nice shirt and pants, you follow Daisy’s directions to arrive at an oriental restaurant."
    "On the way in, you’re impressed by the variety of different Chinese, Japanese, and Korean food on offer."
    "You start to get the notion that this is all leading up to a massive buffet that is sure to please Daisy’s appetite."
    #IMAGE: Daisy sitting at a table wearing a nice dress
    "Telling the hostess why you’re there, you’re guided to a secluded table. Upon seeing you arrive, Daisy gets up from her seat to give you a hug."
    teacher "So glad that you could make it. Have a seat, I already made our orders."
    menu:
    #CHOICE: A) Thank you or B) What did you order?
        "Thank you.":
            teacher "You’re welcome. It will still be a moment before the food arrives so how about we chat for a bit?"
        "What did you order?":
            teacher "Aww, you want me to ruin the surprise? Just sit and chat. It’ll be here soon."

    #(NOTE: Regardless of choice, the following text will play out.)
    #IMAGE: The player sitting across from Daisy.
    teacher "So tell me a little more about yourself. I know we’ve gotten close physically, but I’m sure there’s more to you than that."
    pc "What do you want to know?"
    teacher "Well, you’ve been doing pretty well in my class so far. Have you always been this studious?"
    menu:
    #CHOICE: A) Yeah, I’ve always tried to do my best in school or B) Not really. I’m actually surprised I managed to make it into university with my grades.
        "Yeah, I’ve always tried to do my best in school.":
            teacher "And it shows. You’re quite the excellent student."
        "Not really. I’m actually surprised I managed to make it into university with my grades.":
            teacher "Well, there’s always room to improve. Your performance in my class is proof enough."
    #(NOTE: Regardless of choice, the following should play out.)
    teacher "Alright, your turn. What would you like to know about me?"
    menu:
    #CHOICE: A) What made you want to start gaining weight in the first place? Or B) How did you join the Followers of Heset?
        "What made you want to start gaining weight in the first place?":
            teacher "A simple question, but unfortunately it’s a bit of a complicated answer. It all has to do with my first meeting with the Followers of Heset."
        "How did you join the Followers of Heset?":
            teacher "It’s quite an interesting story. It might also give you an idea of why I’m, for lack of a better term, obsessed with gaining weight."
    #(NOTE: Regardless of choice, the following should play out.)
    teacher "It all started when I joined my friend for a trip to Egypt."
    teacher "They were looking for volunteers for an archaeological dig site and I was looking for something to do with my free time after graduating."
    teacher "The trip itself was interesting, less so the countless time spent digging through dirt. I can’t tell you how many hours I spent organizing pottery."
    teacher "Towards the end of one of the days when we were picking things up, I realized I had left behind one of my tools."
    teacher "When I ran back to get it, I noticed something odd about a mural we had recently uncovered."
    teacher "Under the light of dusk, a group of hieroglyphs lit up to reveal a switch. Pressing my palm against it opened up a dark passage deep underground."
    "Shifting in her seat a bit, Daisy leans forward to look you in the eyes."
    teacher "Tell me. If you were in my position, what would you have done?"
    menu:
    #CHOICE: A) I’d be too curious not to go in or B) I’d turn the other way and leave
        "I’d be too curious not to go in.":
            teacher "Daring as ever I see."
        "I’d turn the other way and leave.":
            teacher "Admittedly the wiser decision, but not the one I took at the time."
    #(NOTE: Regardless of choice, the following should play out)
    teacher "For me, the answer was simple. I had been searching for some kind of purpose and for some reason felt that I would find it in the dark, creepy corridor."
    teacher "Yes, I know how that sounds. Bear with me, I was a bit of a mess back then."
    teacher "Without even a flashlight to lead the way, I descended into the passageway. Even after I was plunged into pitch black, I continued pushing forward."
    teacher "My perseverance was rewarded by a faint glow at the end of the corridor."
    teacher "The small light turned into an eerie collection of torches as I made my way into a massive, stone chamber."
    teacher "Astounded by the ancient architecture, it took me a moment to realize that I wasn’t alone."
    teacher "Spread out in a pattern were a group of people in robes worshiping a mural of an extremely obese woman."
    teacher "Mesmerized by the sight, I couldn’t help gasping a little too loudly and drawing the attention of the crowd."
    #IMAGE: Daisy leaning up closer to the player
    teacher "Turning away from the mural, the hooded figures began to approach. Several of them appeared through a secret passage behind me to make escape impossible."
    teacher "At that moment I was certain that I would be sacrificed to an unknown god all because of my stupid decision. Drawing closer, the leader of the group lifted off their hood to reveal-"
    #IMAGE: A waitress standing next to the table with an order of food.
    waitress "Excuse me miss?"
    "Turning away from you, Daisy looks towards the server holding up two plates."
    teacher "Yes?"
    waitress "Sorry for the wait, but here’s your food. We hope you enjoy."
    teacher "Thank you very much."
    #IMAGE: Daisy sitting at the table with the player with plates of sushi in front of them.
    "Expecting an absolutely indulgent platter of food, you’re a little surprised to find a more modest serving of freshly made sushi."
    pc "That’s it?"
    teacher "What do you mean?"
    pc "I thought you would order more."
    teacher "It’s not that kind of restaurant. Just because I like to pig out, doesn’t mean I can’t take my time to savor a gourmet meal once in a while."
    #IMAGE: Daisy taking a bite of sushi.
    teacher "Especially when the food tastes this good."
    pc "Won’t you still be hungry?"
    teacher "Oh, I took care of that before I arrived. I’m treating this like an after dinner snack."
    pc "So what happened with the cult?"
    teacher "Again, not a cult. A religion."
    pc "Okay, what happened with the religion then?"
    teacher "Oh, the members were quite welcoming. They didn’t get many visitors for obvious reasons."
    teacher "The Followers of Heset were more than eager to share with me their beliefs. In return, I intently listened to every word they spoke."
    teacher "The notion of purposefully gaining weight to embody their deity filled the emptiness inside of me. It felt like I had finally found what I had been seeking for so long."
    teacher "The Followers seemed to think the same thing. All it took was a single conversation to convince them to let me join them."
    teacher "They gave me the very important job of traveling the world to meet with other sects of the group and accomplish various odd jobs."
    teacher "It was during these travels that I was able to feel alive again."
    teacher "Even when I wasn’t doing business for the Followers, I was eager just to experience other cultures with a new vigor for life."
    pc "That sounds amazing."
    teacher "Yes, but not as amazing as when they told me their plans when I returned home."
    teacher "Honestly, I think it was even more incredible that they convinced me to take on this teaching position without any prior experience."
    teacher "Whew, that took a lot more out of me than I thought. Let’s dig in."
    "Over the course of the meal, you continue to exchange conversation with Daisy. One of the main points of discussion being the various adventures she’s had during her travels."
    #IMAGE: Daisy and the player walking out of the restaurant.
    "Finished with the meal, you and Daisy decide it’s time to leave once she’s picked up the tab."
    pc "You didn’t have to pay for everything."
    teacher "Like I said, it’s a reward for all of the hard work you’ve been putting in. Although, if you want to pay me back, I can think of one thing."
    #IMAGE: Daisy and the Player kissing in front of the restaurant.
    "Pulling you in, Daisy embraces you for a kiss. Though it’s a bit awkward having to push up against her belly, you reciprocate the act to properly end the dinner date."

label Teacher_Stage_14_Event:
    #Scene: Luna 3rd Match Cake
    #2 Variants, Variant #1 Luna is stage 10 and eats more than Daisy.
    #Variant #2 Luna is stage 8 and Daisy eats more.
    if carolinestage1event4 == 0 and carolinestage2event == 1:
        scene university_looking_into_class3
    else:
        scene university_looking_into_class
    play music "/music/university.ogg" if_changed
    "Upon arriving to class, your nose picks up a distinct, sweet smell."
    image stage_14_event_1 = "/teacher/events/stage14/1.webp"
    scene stage_14_event_1
    "The scent becomes overwhelming as you gaze upon the large cake obscuring most of Daisy’s desk."
    fs "I wonder what that’s for. Is someone getting married?"
    ms "Either that or we’re about to see another one of Ms. Tanwen’s strip dances."
    if luna.stage >= 10:
        image stage_14_event_2_1 = "/teacher/events/stage14/2_1.webp"
        scene stage_14_event_2_1
    else:
        image stage_14_event_2_2 = "/teacher/events/stage14/2_2.webp"
        scene stage_14_event_2_2
    "Seeing Daisy walk in with Luna in tow, the class quickly figures out what the day’s curriculum will be."
    if luna.stage >= 10:
        image stage_14_event_3_1 = "/teacher/events/stage14/3_1.webp"
        scene stage_14_event_3_1
    else:
        image stage_14_event_3_2 = "/teacher/events/stage14/3_2.webp"
        scene stage_14_event_3_2
    teacher "Good morning, class. I believe you know how to properly greet Ms. Luna."
    s "Hello, Ms. Luna!"
    luna "Hello. Good to see you all again."
    if luna.stage >= 10:
        image stage_14_event_4_1 = "/teacher/events/stage14/4_1.webp"
        scene stage_14_event_4_1
    else:
        image stage_14_event_4_2 = "/teacher/events/stage14/4_2.webp"
        scene stage_14_event_4_2
    luna "As much as I enjoy seeing your faces, you all know why I’m here. Today I plan to be the winner."
    teacher "What makes you think this will be any different than the last two attempts?"
    luna "Because I’ve been practicing. This victory and my reward are as good as mine."
    if luna.stage >= 10:
        image stage_14_event_5_1 = "/teacher/events/stage14/5_1.webp"
        scene stage_14_event_5_1
    else:
        image stage_14_event_5_2 = "/teacher/events/stage14/5_2.webp"
        scene stage_14_event_5_2
    teacher "While I’m just as eager to get underway, we still have a lesson to teach. As to be expected, our focus will be on the contest food: cake."
    luna "I’ll take it from here. The cakes we know today started out as little more than flat discs of grain that were dried up and compacted together."
    luna "Over hundreds of years humanity has developed various different methods of creating the confection."
    luna "Everything from tiny cupcakes to the towering masterpiece you see before you can be attributed to human ingenuity."
    teacher "Wow, you really know your stuff."
    luna "Thanks. I wanted to be well-prepared for the contest."
    if luna.stage >= 10:
        image stage_14_event_6_1 = "/teacher/events/stage14/6_1.webp"
        scene stage_14_event_6_1
    else:
        image stage_14_event_6_2 = "/teacher/events/stage14/6_2.webp"
        scene stage_14_event_6_2
    luna "But enough talk, let’s get this show on the road. [playername], would you mind coming up here to do the countdown again?"
    pc "You got it."
    "You get up from your seat and walk towards the front. On the way, Daisy passes you a timer already set for half an hour."
    teacher "We'll be doing things a little differently this time. Whichever one of us eats more of our side of the cake in the allotted time will be the winner."
    luna "And claim the reward."
    if luna.stage >= 10:
        image stage_14_event_7_1 = "/teacher/events/stage14/7_1.webp"
        scene stage_14_event_7_1
    else:
        image stage_14_event_7_2 = "/teacher/events/stage14/7_2.webp"
        scene stage_14_event_7_2
    "Judging by the way the two of them glance at you, you can already tell what their prize is supposed to be."
    pc "Alright, are you ready? On your marks. Get set. GO!"
    if luna.stage >= 10:
        image stage_14_event_8_1 = "/teacher/events/stage14/8_1.webp"
        scene stage_14_event_8_1
    else:
        image stage_14_event_8_2 = "/teacher/events/stage14/8_2.webp"
        scene stage_14_event_8_2
    "On the word go, Daisy and Luna begin to go at the cake like wild animals."
    if luna.stage >= 10:
        image stage_14_event_9_1 = "/teacher/events/stage14/9_1.webp"
        scene stage_14_event_9_1
    else:
        image stage_14_event_9_2 = "/teacher/events/stage14/9_2.webp"
        scene stage_14_event_9_2
    "Though Daisy is quick to gain a head start, Luna shows the fruits of her labor as she begins to catch up."
    if luna.stage >= 10:
        image stage_14_event_10_1 = "/teacher/events/stage14/10_1.webp"
        scene stage_14_event_10_1
    else:
        image stage_14_event_10_2 = "/teacher/events/stage14/10_2.webp"
        scene stage_14_event_10_2
    "The two’s manic eating only stops long enough for them to toss away clothing."
    if luna.stage >= 10:
        image stage_14_event_11_1 = "/teacher/events/stage14/11_1.webp"
        scene stage_14_event_11_1
    else:
        image stage_14_event_11_2 = "/teacher/events/stage14/11_2.webp"
        scene stage_14_event_11_2
    "With only their undergarments clinging to their bodies, they are free to accumulate layers of crumbs and frosting in their pursuit of victory."
    if luna.stage >= 10:
        image stage_14_event_12_1 = "/teacher/events/stage14/12_1.webp"
        scene stage_14_event_12_1
    else:
        image stage_14_event_12_2 = "/teacher/events/stage14/12_2.webp"
        scene stage_14_event_12_2
    "Through a combination of cheers from the students and their own hunger the two women eat as much as they can. As the timer hits zero, the winner is…"
    #(NOTE: Here would be the split between if the player has fed Luna or Daisy more)

    if luna.stage >= 10:
        #Option B: Luna is larger

        image stage_14_event_L1 = "/teacher/events/stage14/L1.webp"
        scene stage_14_event_L1
        pc "LUNA!"
        "The classroom erupts into a roar of applause, leaving Luna to bask in the glory."
        luna "I knew I could do it."
        "Though she manages to force a smile on her face, it’s clear that she’s struggling to move even an inch with her added weight."
        image stage_14_event_L2 = "/teacher/events/stage14/L2.webp"
        scene stage_14_event_L2
        teacher "That was very impressive. You definitely earned that victory, along with your prize."
        teacher "For the rest of you, I think it would be a good idea to end class early today. [playername], would you mind-"
        pc "Yeah, yeah. I’ll stay behind."
        teacher "Splendid. For everyone else, enjoy your day."
        image stage_14_event_L3 = "/teacher/events/stage14/L3.webp"
        scene stage_14_event_L3
        "Waiting for the other students to leave, you lock up the door before turning your attention towards the overstuffed women."
        teacher "How did you manage to eat like that?"
        luna "As much as I’d like to take all the credit, my little helper here has been giving me one on one sessions to train me."
        image stage_14_event_L4 = "/teacher/events/stage14/L4.webp"
        scene stage_14_event_L4
        teacher "Is that so? Then I think it would be best for you to share your prize with him. Wouldn’t you agree?"
        luna "Of course. And by the looks of it, I think he’s more than eager to claim his prize. IF he’s willing of course."
        pc "You know I am. Daisy, did you want to-"
        image stage_14_event_L5 = "/teacher/events/stage14/L5.webp"
        scene stage_14_event_L5
        teacher "To the victor go the spoils. I’ll be fine taking care of myself here."
        teacher "Go on. I don’t think she’s able to move much on her own right now, so you’ll have to take the lead."
        image stage_14_event_L6 = "/teacher/events/stage14/L6.webp"
        scene stage_14_event_L6
        "Taking off your clothes, you kneel down in what little remains of the cake to help Luna out of her bra and panties."
        "Freed from her undergarments, she is more than willing to let you grope her swollen belly and squeeze her plethora of added fat."
        "Perhaps getting a little too excited, you end up pulling both of you down to the ground."
        if persistent.nosexscene == True:
            scene black with dissolve
            "Luna, Daisy and you had a wonderful time together."
            image stage_14_event_L11 = "/teacher/events/stage14/L11.webp"
            scene stage_14_event_L11
            "Taking a few moments to recover from our session, the three of us take our sweet time cleaning up our mess before we all take our leave."
            stop music fadeout 1.0
            if recollection == False:
                $ teacher.weight += 1
                $ luna.weight += 1
                $ teacherstage14event = 0
                $ strip = 0
                $ daytime = 2
                jump freetime
            return
        "Though you’re covered in icing, you don’t seem to care much. Your bodies move on their own to get in the right position."
        image stage_14_event_L7 = "/teacher/events/stage14/L7.webp"
        scene stage_14_event_L7
        "Gliding your cock along the surface of her butt cheeks, it eventually makes it way towards her dripping womanhood."
        "Getting a tight grip on her belly for stability, you give her a rough thrust to begin."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/teacher/events/stage14/L8.webm" loop
        show movie with dissolve
        window hide
        pause
        "Each shove of your member inside of Luna slams her heavy belly into the mess of icing below."
        "The constant slapping sound of her flesh jiggling about is soon joined with moans from both hers and your mouth."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/teacher/events/stage14/L9.webm" loop
        show movie with dissolve
        "From nearby you watch as Daisy fingers herself in time with the thrusts, soon joining in with her own euphoric cries."
        window hide
        pause
        "This moment of indulgence comes to a close as you give one last shove to press Luna’s face into a lingering pile of icing."
        stop movie
        image stage_14_event_L10 = "/teacher/events/stage14/L10.webp"
        scene stage_14_event_L10
        "Through the sweetness in her mouth you can hear her muffled moan as she finds release alongside yourself and Daisy."
        image stage_14_event_L11 = "/teacher/events/stage14/L11.webp"
        scene stage_14_event_L11
        "Taking a few moments to recover from the session, the three of you take your time cleaning up the mess before leaving."

    else:
        #Option A: Daisy is larger.

        image stage_14_event_D1 = "/teacher/events/stage14/D1.webp"
        scene stage_14_event_D1
        pc "DAISY!"
        "The classroom erupts into a roar of applause, leaving Daisy to bask in the glory."
        teacher "Thank you, thank you. Always feels good to test my limits like this. Not to say my competitor didn’t put up a good fight. Isn’t that right, Luna?"
        image stage_14_event_D2 = "/teacher/events/stage14/D2.webp"
        scene stage_14_event_D2
        luna "Damn…it."
        teacher "Hmmm, looks like that was a bit much for her."
        image stage_14_event_D3 = "/teacher/events/stage14/D3.webp"
        scene stage_14_event_D3
        teacher "I suppose that’s our sign for us to end class early for the day. [playername], could you-"
        pc "Yeah, yeah. I’ll stay behind."
        teacher "Splendid. For everyone else, enjoy your day."
        image stage_14_event_D4 = "/teacher/events/stage14/D4.webp"
        scene stage_14_event_D4
        "Waiting once more for the other students to leave, you take the initiative to lock the door for privacy."
        luna "I was so close this time."
        teacher "I’ll say. That was pretty impressive. You really made me work for this win. We should definitely do this again."
        luna "I’m all for it, but first I think it’s time you claim your prize."
        image stage_14_event_D5 = "/teacher/events/stage14/D5.webp"
        scene stage_14_event_D5
        teacher "Oh, I intend to. IF the prize is willing of course."
        pc "Don’t need to ask me twice. Luna, will you be alright?"
        luna "Yeah, I’ll be fine. You two go ahead. I’m more than happy to watch while I take care of myself. Not that I can move much on my own right now anyway."
        image stage_14_event_D6 = "/teacher/events/stage14/D6.webp"
        scene stage_14_event_D6
        "Tossing your clothes off, you embrace Daisy to celebrate her victory."
        "The enormous amount of cake stuffed inside of her belly makes it hard for you to completely wrap your arms around the bulge, but that doesn’t stop her."
        "She’s more than willing to envelop your body with her flab as she comes in for a kiss."
        if persistent.nosexscene == True:
            scene black with dissolve
            "Luna, Daisy and you had a wonderful time together."
            image stage_14_event_D10 = "/teacher/events/stage14/D10.webp"
            scene stage_14_event_D10
            "Taking a few moments to recover from our session, the three of us take our sweet time cleaning up our mess before we all take our leave."
            stop music fadeout 1.0
            if recollection == False:
                $ teacher.weight += 1
                $ luna.weight += 1
                $ teacherstage14event = 0
                $ strip = 0
                $ daytime = 2
                jump freetime
            return
        image stage_14_event_D7 = "/teacher/events/stage14/D7.webp"
        scene stage_14_event_D7
        "Pulling you down with her, Daisy brings you crashing into the leftover bits of cake that somehow survived the contest."
        "Your bodies are covered in icing after only a few turns, but neither of you seem to care."
        "All that matters is the feeling of ecstasy as Daisy climbs on top and plunges your cock into her waiting womanhood."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/teacher/events/stage14/D8.webm" loop
        show movie with dissolve
        window hide
        pause
        "Though Daisy’s movements are slowed down by the cake stuffed inside of her body, she shows that she is skilled with throwing her extra weight around."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/teacher/events/stage14/D9.webm" loop
        show movie with dissolve
        window hide
        pause
        "The icing clinging to her flesh makes a squishing sound as she slams herself down on you over and over again."
        "As the two of you begin to cry out in ecstasy, Luna joins in with her own moans as she rubs against her clit."
        "This moment of pure hedonism all comes to an end with one final thrust to bring the three of you to near simultaneous orgasm."
        stop movie
        image stage_14_event_D10 = "/teacher/events/stage14/D10.webp"
        scene stage_14_event_D10
        "It takes some time for you all to recover from the lingering euphoria, but eventually you manage to clean yourselves up before leaving the classroom."
    stop music fadeout 1.0
    if recollection == False:
        $ teacher.weight += 1
        $ luna.weight += 1
        $ teacherstage14event = 0
        $ strip = 0
        $ daytime = 2
        jump freetime
    return

label Teacher_Stage_15_Event:
    #Scene: Daisy Home Barbeque Stuffing
    #(NOTE: The following occurs on a Thursday after the player is finished with class and is sitting in his room.)
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Daisy', dialogue=dialogue_one)
    $ msg ("Hello, my favorite student. I have something special in mind for this evening. Want to come over to my place to help me out?", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ msg ("Wonderful. Meet me at my place around 7pm. Don’t be late.", who=1)
            pause
            $ hide_messenger()
            "More than a little suspicious, you pack up an overnight bag and head over to Daisy’s house."
        "No.":
            $ msg ("Sorry, I’m a little busy today.")
            pause
            $ msg ("A shame, but I understand. We’ll try again some other time.", who=1)
            pause
            $ hide_messenger()
            return

    image stage_15_event_1 = "/teacher/events/stage15/1.webp"
    scene stage_15_event_1
    play music "/music/daisy.ogg" if_changed
    teacher "Glad you could make it."
    pc "What are all these boxes?"
    teacher "The key to tonight’s entertainment. Let me show you."
    image stage_15_event_2 = "/teacher/events/stage15/2.webp"
    scene stage_15_event_2
    "Following Daisy over to the collection of boxes, she picks one off the top and opens it. Your mouth begins to water from just the aroma as it drifts into your face."
    "Given a chance to look over the tasty chicken in the box, you subconsciously smack your lips."
    teacher "Go ahead and try one. I ordered more than enough."
    image stage_15_event_3 = "/teacher/events/stage15/3.webp"
    scene stage_15_event_3
    "Picking up a chicken leg, you sink your teeth in and are overwhelmed with a rich, smoky flavor."
    "Going at the hunk of meat like a starving animal, you make a bit of a mess of sauce around your face as you eat down to the bone."
    "Taking away the remnants of your meal, Daisy reaches out to clean the sauce off your face."
    image stage_15_event_4 = "/teacher/events/stage15/4.webp"
    scene stage_15_event_4
    teacher "You seem to enjoy it."
    pc "It’s incredible. Where did you get this from?"
    teacher "The Followers of Heset. It’s part of an upcoming project intended to flood the restaurant industry in town with irresistible, fattening food."
    teacher "I was able to get my hands on a sample of their barbeque under one condition."
    image stage_15_event_5 = "/teacher/events/stage15/5.webp"
    scene stage_15_event_5
    "With a flick of her wrist, Daisy tosses away her robe to leave her pudgy body on full display."
    teacher "I have to be a taste tester for all of this delicious food. Don’t suppose you’d mind helping me work through my collection? Alongside any “side effects” of stuffing myself like a pig?"
    pc "Not at all."
    "Daisy lets out a giggle as she slides her tongue across her lips."
    teacher "Very good. Now be a good boy and get undressed. Things are going to get more than a little messy."
    image stage_15_event_6 = "/teacher/events/stage15/6.webp"
    scene stage_15_event_6
    "While you get undressed, Daisy busies herself with getting things set up. By the time you hang up your clothes, she’s already rolled out a white mat."
    "Helping her move the boxes over to the eating area, you place the feast around her to ensure everything is within reach."
    pc "Everything looks ready to go. What should I do now?"
    teacher "Just hand me the first box. I’ll let you know when it’s time to do your job."
    image stage_15_event_7 = "/teacher/events/stage15/7.webp"
    scene stage_15_event_7
    "Heeding Daisy’s orders, you begin to feed her one piece of meat after another. She eagerly eats up ribs and chicken like it was nothing."
    "With you taking on the duty of stuffing her face, her hands are left free to squeeze and grope her body to revel in her act of hedonism."
    image stage_15_event_8 = "/teacher/events/stage15/8.webp"
    scene stage_15_event_8
    "Finishing off one of the boxes, you attempt to pick up a napkin to clean her face, only to have her push your hand away."
    teacher "While I appreciate the gesture, I want to get as messy as possible tonight. Besides, I have another job in mind for you. Get on the floor."
    if persistent.nosexscene == True:
        scene black with dissolve
        "Daisy and I had a great time together."
    else:
        image stage_15_event_9 = "/teacher/events/stage15/9.webp"
        scene stage_15_event_9
        "Laying down on the ground, you’re given a prime view of her fatty body as she stands above you. Lifting up her belly, she makes sure you have a good look at her dripping pussy."
        teacher "Think your mouth is up to the task?"
        pc "Bring it on."
        teacher "Good boy. Now hold still."
        image stage_15_event_10 = "/teacher/events/stage15/10.webp"
        scene stage_15_event_10
        "Your world goes dark as Daisy’s ass cheeks slam against your face. Though you can’t see anything, you feel every bit of her flab as she shuffles along your body."
        "As something warm and wet slides against your face, you instinctively open your mouth to fulfill your duty."
        image stage_15_event_11 = "/teacher/events/stage15/11.webp"
        scene stage_15_event_11
        teacher "MMMMPH! Very good. Now keep it up. I still have a lot of food to go through."
        image stage_15_event_12 = "/teacher/events/stage15/12.webp"
        scene stage_15_event_12
        "Each drag of your tongue releases a moan from her lips. These euphoric cries are repeatedly stifled as she continues to stuff herself with food."
        image stage_15_event_13 = "/teacher/events/stage15/13.webp"
        scene stage_15_event_13
        "Between her busy eating and your frantic sucking, you can hear her free hands squeezing and prodding her fat. This overwhelming amount of stimulation inevitably brings her to a roaring orgasm."
        image stage_15_event_14 = "/teacher/events/stage15/14.webp"
        scene stage_15_event_14
        "Daisy’s resulting climax sends tremors through her body. Perhaps to stifle her own cries, she stuffs a chicken nugget into her mouth."
        "Despite her sudden release, she wastes little time moving her body again."
        image stage_15_event_sex = "/teacher/events/stage15/sex.webp"
        scene stage_15_event_sex
        "Daisy follows up her meaty meal by leaning forward to wrap her lips around your rigid cock."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/teacher/events/stage15/sexvideo.webm" loop
        show movie with dissolve
        window hide
        pause
        "Feeling her suck and lick with a fervor similar to how she ate the barbeque, you return the favor by giving her pussy some more attention."
        "This constant back and forth between the two of you lasts up until you hit the breaking point."
        stop movie
        image stage_15_event_15 = "/teacher/events/stage15/15.webp"
        scene stage_15_event_15
        "The eventual dual climax drains the rest of the strength from your bodies. Exhausted from the session, Daisy let’s her entire body go limp."
        "Feeling all of her weight smother you in an instant, you’re only able to stay awake for a few moments before falling unconscious."
    stop music fadeout 1.0
    scene black with dissolve
    if recollection == False:
        $ phonecall = 0
        $ daytime = 1
        $ day = 5
        $ strip = 0
        $ worked_today = 0
    "You're eventually woken up by a constant beeping noise. Though you open up your eyes, you're met with a sea of darkness."
    "You try to sit up, but your arms seem pinned down by a living blanket that rises and falls at a constant rate."
    "It’s only when the beeping noise becomes louder does the fleshy prison release you from its clutches."
    image stage_15_event_16 = "/teacher/events/stage15/16.webp"
    scene stage_15_event_16
    "Rolling out from beneath Daisy, you stretch your limbs to get rid of any lingering stiffness."
    "The sight of the sauce stains littering Daisy’s body are more than enough to remind you of the prior evening’s events."
    pc "Good morning. Are you feeling alright?"
    teacher "No, no, no. I’m late! We overslept."
    pc "What are you…OH CRAP! We have to get to class."
    teacher "Jump in the shower with me. I’m going to need your help to get ready fast."
    image stage_15_event_17 = "/teacher/events/stage15/17.webp"
    scene stage_15_event_17
    pc "I know you’re in a rush, but this does feel pretty nice."
    teacher "Yes, yes, it’s very sexy. Now hurry up! The dean is already being lenient with my behavior as is."
    teacher "Last thing I need is him marking me down for being late for my own class. Now get to scrubbing. I need my belly rolls clean before I try to stuff them in my shirt."
    pc "Yes, ma'am!"
    if carolinestage1event4 == 0 and carolinestage2event == 1:
        scene university_looking_into_class3
    else:
        scene university_looking_into_class
    play music "/music/university.ogg" if_changed
    "After going through the fastest morning routine ever, you and Daisy make your way back to school."
    "Unwilling to reveal the exact nature of your relationship, you two decide to split off and arrive to class at separate times."
    image teacher_stage_1_event_10 = "/teacher/events/stage1/10.webp"
    scene teacher_stage_1_event_10
    fs "Hey there. You doing alright? You look a little exhausted."
    ms "And you smell like meat."
    pc "Yeah, I’m fine. A bit of, um, indigestion kept me awake all night."
    "Before anyone else can start asking questions, you take the usual seat. Moments later, Daisy decides to waddle into the room."
    image stage_15_event_18 = "/teacher/events/stage15/18.webp"
    scene stage_15_event_18
    teacher "Good morning, students."
    "The class takes a moment to give out their usual response, everyone noticing the exasperated look on her face."
    image stage_15_event_19 = "/teacher/events/stage15/19.webp"
    scene stage_15_event_19
    teacher "Now, as for today's lesson, we will be talking about-"
    ms "Hey, teach, what's that on your belly?"
    image stage_15_event_20 = "/teacher/events/stage15/20.webp"
    scene stage_15_event_20
    "You and Daisy notice the stain at the same time. Amidst the rushed morning routine, it appears that you missed a spot on her gut."
    image stage_15_event_21 = "/teacher/events/stage15/21.webp"
    scene stage_15_event_21
    teacher "Oh, this? This is barbeque sauce. I was going to give you all a lesson about it, but I got hungry on the car ride here."
    teacher "Oh, well. Guess we’ll have to cancel class for the day. We’ll pick up some other time."
    fs "Wait, what about the Friday feeding?"
    teacher "Um, yes. Of course. How could I forget? Go ahead and bring your food up to the front."
    image stage_15_event_22 = "/teacher/events/stage15/22.webp"
    scene stage_15_event_22
    "Though the pile of offerings seems small for this week, you can tell by the look on Daisy’s face that she’s still full from last night’s feast."
    teacher "Thank you all for giving me such a wonderful spread. I don’t know where to start. Perhaps I’ll just taste a little from everything and finish the rest at home."
    image stage_15_event_23 = "/teacher/events/stage15/23.webp"
    scene stage_15_event_23
    "Though she tries to keep her overstuffed belly calm with small bites, the meager amount of food seems to be pushing her to her limits."
    image stage_15_event_24 = "/teacher/events/stage15/24.webp"
    scene stage_15_event_24
    "In an attempt to avoid suspicions, she gives a few extra bites here and there. The plan works up until her nerves lead her to eat way more than she intended to."
    image stage_15_event_25 = "/teacher/events/stage15/25.webp"
    scene stage_15_event_25
    teacher "So UUURRRP tasty. Thank you all so much for the food. You can go home now. I’ll sit here and digest for a bit."
    image stage_15_event_26 = "/teacher/events/stage15/26.webp"
    scene stage_15_event_26
    "As much as you want to help Daisy out, you can tell by the expression on her face that she'd rather not have anyone touch her right now."
    "Waving goodbye, you filter out with the rest of the class and head home to take a more thorough shower to get rid of the stench of barbequed meat."
    stop music fadeout 1.0
    if recollection == False:
        $ teacher.weight += 2
        $ teacherstage15event = 0
        $ strip = 0
        $ daytime = 2
        scene player_room
    return

#label Teacher_Stage_16_Event:
    #Scene: Follower of Heset Headquarters First Visit
    #(NOTE: The following takes place after a normal class day once the player has reached Stage 16 with Daisy)

    #Image: Daisy looking at the player while she grasps his arm.
    "Just as you’re about to leave the classroom, Daisy grabs your arm to pull you back in."
    teacher "Are you free this afternoon? There’s something important I want to show you regarding our cause."
    menu:
        "Yes.":
            teacher "Excellent. Follow me."
        "No.":
            teacher "Very well. Some other time then."
            return

    #Image: Church exterior.
    "Leaving from the university, you and Daisy travel to the very edge of town. The trek brings you to a crumbling church that looks absolutely ancient."
    "Despite the suspicions that the place might collapse at a moment’s notice, Daisy shows no hesitation as she gestures for you to follow her inside."
    #Image: Church interior with Daisy standing on the altar.
    pc "What is this place?"
    teacher "You’re standing in a very significant location for the Followers of Heset. It is a place our group’s ancestors built hundreds of years ago. For centuries it has been used as the basis for our operations to spread our teachings and empower our goals."
    pc "I don’t mean to sound rude, but I don’t think this place is up for the task."
    teacher "Oh this is just the entryway. Let me show you."
    "Going behind the altar, Daisy pulls on a series of levers. The floor begins to shake, and she quickly jumps back to your side."
    "Just as you think that the entire building is about to fall apart, you watch as the altar begins shift. As the church settles down, you’re given a chance to peer into the dim cavern that has just opened up."
    "An aroma of various delicious meals drifts out of the passageway, as if trying to tempt you into entering the dark abyss. You’re broken free from this trance as Daisy gives you a pat on the back and begins to descend."
    teacher "Come along. Best not to keep the other members waiting for too long."
    "Already too far in to stop now, you take a deep breath and follow Daisy into the passageway. You somehow manage to remain steadfast as the door closes up behind you and you continue down the dimly lit corridor."
    #Image: Followers of Heset Temple main chamber.
    "After walking through the corridor for a while, you come upon a large chamber. The stone walls and high ceiling look well maintained and a far cry from the run down church you entered from."
    "You’re given a better chance to admire the architecture thanks to the lit torches scattered about the area. As you get closer to the center, you can see other members milling about."
    #Image: Followers of Heset Temple main chamber with the members staring at the player.
    "Walking within a few feet of the women makes them stop mid-conversation to stare at you. Though your eyes momentarily linger on their skimpy outfits, your gaze is almost instantly drawn to the suspicious looks on their faces."
    teacher "It’s alright ladies. He’s with me. This is the one I was talking about."
    #Image: Daisy speaking with a Helper.
    "While the women give a nod to Daisy and go back to speaking with each other in hushed whispers, another girl in white robes approaches you."
    White Robed Woman "Is he truly the one you spoke of?"
    teacher "Possibly, yes. I still have a few things to test out. However, he has more than proven his devotion to the cause."
    White Robed Woman "We shall have to see. It’s been quite a while since an outsider has been to this location. The High Priestess will want to have a word with him."
    teacher "Understood. I will take him right away. (PLAYER), follow me. There’s someone you have to meet."
    #Image: Followers of Heset Basement with the High Priestess standing in the center.
    "Following Daisy down a set of spiraling stairs, you come upon another chamber adorned in numerous relics and baring banners with the Followers of Heset markings on them."
    "Standing amidst all of these artifacts is a woman dressed in the cult’s ceremonial outfit."
    "Most of her face is covered by a black visor, but you can still feel the way she’s looking at you. It almost feels like she’s staring into your very soul."
    High Priestess "This is [playername]?"
    teacher "Yes, he is the person I’ve been talking about."
    High Priestess "And you are sure he is the right one?"
    teacher "You’ve read my reports. The progress he’s been making with girls all over town has been astounding. If you still have any doubts, ask him yourself."
    #Image: The High Priestess standing close to the player.
    High Priestess "Tell me, is it true that you are devoted to our group’s cause? That you intend to make women gain weight to increase our power?"
    pc "It’s less of me being devoted, and more of me just stumbling into girls that like to gain."
    High Priestess "Are you saying you dislike making women fatter?"
    pc "I’m not saying that at all. It’s quite the opposite."
    High Priestess "Then what is the issue?"
    pc "The only issue is that I’m not entirely doing it on purpose. Opportunities to make women larger kind of just happen to me. It’s not like I have any control over it."
    "The High Priestess pauses, remaining silent as she once more looks over your body."
    High Priestess "If what you say is true, then you indeed may be the one we are looking for. I hereby acknowledge you as a recruit for the Followers of Heset."
    High Priestess "While you do not have the full benefits of a member yet, you will still have access to certain assistance from our organization. Daisy, I will place you in charge of him should he wish for our help."
    #Image: Followers of Heset Basement with Daisy standing next to the player with a big smile on her face.
    "After making her announcement, the High Priestess exits the room to leave you alone with Daisy."
    teacher "That went rather well. She’s usually a lot rougher when it comes to new members."
    pc "No wonder you have so few."
    teacher "Sorry, just something a lot of our higher ups have picked up over their struggle of getting our teachings across. Hopefully once the key to our plan is obtained, they might lighten up a bit. For now though, let me get you home."
    pc "But I just got here."
    teacher "Sorry, but there’s not much you can do right now at your rank. Don’t worry though. I’ll make sure to bring you back here soon. I have something special planned that I just know you’ll love."
    pc "If you say so."
    "Once more led by Daisy out of the temple, you exit the church."
    #Image: Exterior of the Church with Daisy standing next to the player.
    teacher "Ah, before I forget. Please remember that this place is supposed to be a secret. Don’t need you posting about it online or gossiping about it with your classmates. Promise not to tell?"
    pc "What happens if I do?"
    teacher "Severe and swift punishment."
    pc "Understood."
    teacher "Excellent. Then I’ll see you next time."
    "Parting ways from Daisy, you head home and go to bed."

    $ teacherstage16event = 0
    $ strip = 0
    $ daytime = 2
    jump freetime

#label Teacher_Stage_17_Event:

    #Scene: Daisy Oral and Anal Stuffing
    #(NOTE: The following takes place when the player is in his room once Daisy reaches Stage 17)

    "You receive a message from Daisy."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Daisy', dialogue=dialogue_one)
    $ msg ("I was able to get my hands on some special equipment thanks to the Followers of Heset. Are you free tonight to help me test them out?", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Good. Meet me at the temple in one hour.", who=1)
            pause
            $ hide_messenger()
        "No.":
            $ msg ("Shame, but I understand. I’ll message you again some other time.", who=1)
            pause
            $ hide_messenger()
            return

    #Image: Followers of Heset Temple main chamber with Daisy dressed in a robe.
    "It takes a few tries to get the combination right, but eventually you figure out the sequence of lever pulls needed to gain access to the temple."
    "Your reward after walking through the dim corridor is the sight of Daisy dressed in a robe."
    teacher "Glad you could make it."
    pc "What are we doing here?"
    teacher "Patience. All will be shown soon. Follow me."
    #Image: Temple basement chamber with two tubes hanging from the ceiling.
    "Following after Daisy, you arrive at a private chamber of the temple. You’re given the first clue of the night as you look at the two tubes hanging down from the ceiling."
    "While you recognize them as being similar to the feeding device Daisy used before, you’re still left a little confused."
    pc "We have a feeding device in the ceiling, but they can’t use regular lightbulbs for the temple?"
    #Image: Naked Daisy standing between the two tubes.
    teacher "It’s mostly for mood lighting. Makes the temple feel more authentic to our religion’s roots."
    pc "Okay, but why are there two tubes? Are you bringing in someone like Luna for the session?"
    teacher "Oh no, these are both meant for me."
    pc "But you only have one mouth."
    #Image: Daisy holding up the tubes in both hands.
    "She smiles at you as she picks up the tubes and holds them up to your face."
    teacher "I never got a chance to properly explain what I was stuffing myself with that day in class. It’s an experimental formula the Followers of Heset created to help promote weight gain."
    teacher "Though you saw me drink it down back then, the fluid merely has to enter the body to start working its magic. That means it can go into any orifice."
    #Image: Daisy stuffing one hose between her butt cheeks.
    "Rather than let you wonder the exact meaning of her words, she demonstrates her point by shoving one of the tubes up her anus."
    teacher "Oooh, been a while since I’ve done something like this, but I’m still more than capable. I’m leaving it to you to control the flow this time."
    "Pointing with her free hand, she gestures towards a control panel on the wall."
    teacher "You’ll be the one with the keys to the machine."
    pc "I’ve never used something like this before."
    teacher "Don’t worry, I have utmost faith in you. I’ll let you know when it gets too much. Now get in position."
    #Image: Daisy with both tubes shoved inside of her.
    "Following Daisy’s command, you take your place in front of the control panel. Looking over the various buttons, you once more look towards her for guidance."
    "Though she is incapable of speaking in her current state, she gives you the go ahead with a nod. Trusting in her judgement and more than a little curious, you take a deep breath and press the button."
    #Image: Daisy being stuffed from both ends.
    "A press of the button brings the machine in the ceiling to life. In mere moments the fattening fluid begins to chug through the tubes and into Daisy’s body."
    "You can hear a muffled moan from her lips as the liquid is swallowed. In mere moments her already sizable body begins to swell from the influx of fluid."
    "The tightening of her gut from the sheer volume leads to her releasing a cacophony of muffled moans as she gropes herself. This all culminates in an orgasmic shiver as she reaches the apex of her size."
    #Image: Daisy laying on the floor with her body engorged and fluid leaking from her mouth and rear.
    "A few claps of Daisy’s hands are enough to clue you in that that the machine needs to be turned off."
    "As the tubes give her a last helping of fluid, they pull themselves out of her body and retract into the ceiling. No longer able to stand on her own, Daisy slumps onto to the ground."
    #Image: Stuffed Daisy staring at the player.
    "Rushing to see if she’s alright, she lethargically lifts up her head to greet you."
    teacher "That was just as amazing as I’d hope it would be."
    pc "Are you feeling alright? That was a lot to take in."
    teacher "I’m fine. It’s just…I’m not done yet."
    pc "Then why did you tell me to stop?"
    teacher "Because I only have a little spare room left, and I’d prefer to save it for a special treat. Up to you on what hole needs a little extra attention."
    "Recognizing the look on her face, you weigh your options on how best to satisfy both of you."

    menu:
        "Oral.":
            #Image: Bloated Daisy leaning forward to swallow the player’s penis.
            "Figuring that Daisy values stuffing her face more than anything, you strip down and present your cock. The guess is proven correct as she leans forward to wrap her lips around the tip."
            "Though she is eager, her overstuffed state keeps her from moving too fast. While the slow slide of her lips and tongue against your shaft is pleasurable, you know it’s not nearly enough."
            #Image: The player with both hands on Daisy’s body as he roughly thrust his penis in and out of her mouth.
            "Placing your hands on Daisy’s shoulders, you take control by roughly shoving your cock into her mouth. Pushed forward by the moan that emanates from her, you continue to move your hips back and forth."
            "Though she tries to assist where she can with her tongue, her movements become more sluggish as she gives into the depravity of having her face fucked."
            #Image: Daisy with semen running down her lips.
            "Your eventual orgasm provides a sense of euphoria and gives her the dessert she so craves. Holding onto her body, you make sure to give her every last drop before pulling away."
            "Even then, her stuffed state leaves her incapable of stopping a few trickles of cum from spilling out."
            pc "Are you alright?"
            teacher "Y-yeah. Just give me a minute to collect myself. You can go home. The Helpers should be along shortly to take care of the rest."
            pc "The who?"
            teacher "The women in white are called Helpers. They have the job of cleaning up around the temple and assisting members."
            teacher "Thank you for being my personal helper for the day. I intend to make these sessions a regular thing. Will you be available for this again?"
            pc "When possible, sure."
            teacher "Good. Then I’ll see you later."
            "After getting dressed, you leave the temple and head home."

            $ teacher.weight += 3
            $ teacherstage17event = 0
            $ strip = 0
            $ daytime = 2
            jump freetime

        "Anal.":
            #Image: The player carefully sliding their penis inside of Daisy’s anus.
            "Guessing that Daisy requires more than just a meal, you make your way over to her backside. Tossing aside your clothes, you approach her fat ass with your rigid cock."
            "Carefully guiding the tip, you push past the lingering drops of fattening fluid to slide it inside of her anus. The moan heard from the other side is more than enough to get you to continue."
            #Image: The player with both hands on Daisy’s butt as he fucks her ass.
            "Grabbing handfuls of her ass fat, you begin to roughly shove your cock inside of her at a rapid pace."
            "The constant motion sends ripples through her blubbery body and towards her face."
            "These tremors result in a constant stream of moans leaking from Daisy’s mouth as she shares in the pleasure."
            "Feeling yourselves get closer and closer to release, you hazard to give her backside a few smacks to satisfy your desires."
            "This all culminates in one final thrust that overflows what little room remains in her anus with your seed."
            #Image: Daisy laying on the floor with her face lazily looking up at the player.
            "Waiting until you’ve spilled every last drop of cum, you carefully remove yourself from Daisy and make your way towards the front."
            "You arrive to see her face lost in leftover euphoria as she tries to contend with the lingering shivers."
            pc "Are you okay?"
            teacher "Y-yeah. It’s just been a while since someone has given my ass such a thorough pounding. You did wonderfully. Thank you for helping me today. Would you be up for doing this again sometime?"
            pc "You can count on me."
            teacher "Excellent. You can go home now. It’ll be a while before I can move again. You can leave the clean up to the Helpers."
            pc "The who?"
            teacher "The women in white are called Helpers. They have the job of cleaning up around the temple and assisting members. Thank you for being my personal helper for the day. See you later."
            "After getting dressed, you leave the temple and head home."

    $ teacher.weight += 3
    $ teacherstage17event = 0
    $ strip = 0
    $ daytime = 2
    jump freetime


#label Teacher_Stage_18_Event:

    #Scene: Daisy Mobility Issues
    #Image: University inside normal classroom.

    "You arrive for a typical day of class in the usual seat. The lack of any mountains of food or strange contraptions leaves you feeling like something is off."
    "Though you try to shake it off, things start to go wrong as the class start time passes by and Daisy is nowhere to be found."
    #Image: Classroom looking at students.
    fs "Where is Ms. Tanwen?"
    ms "Maybe she got lost?"
    fs "Don’t be stupid. She comes here five days a week. I wonder if something happened to her."

    "While the other students continue to discuss where Daisy is, you receive a text from her."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Daisy', dialogue=dialogue_one)
    $ msg ("Hey there, my ace student. I have a bit of a problem. Could you come meet me in the faculty parking lot? I need some help.", who=1)
    pause
    $ msg ("What about the class?")
    pause
    $ msg ("Don’t worry about them. I’m pretty sure I won’t be making it there anytime soon. Just hurry up.", who=1)
    pause
    $ hide_messenger()

    fs "Well, it’s been fifteen minutes. I think that means class is canceled."
    ms "Hell yeah! Who’s up for a trip to Bunny Bites?"
    "Watching the other students filter out to either go home or eat out, you get up and make your way to the parking lot."
    #Image: Faculty parking lot
    "Wandering between the cars, you begin to wonder exactly what could have happened to Daisy."
    "Making matters worse is that the lot is sizable enough to easily get lost in. Just as you wonder if you’ll ever be able to find her, you eventually see her along with her problem."
    #Image: Daisy stuck in the driver’s seat of her car.
    "The sight of Daisy’s belly sticking out of her car acts like a signal beacon."
    "Due to most of the student body being in class, it seems like no one has walked by to come and free her. Walking up to the car, you can see the relief wash over her face as she spots you."
    pc "Are you stuck?"
    teacher "Unfortunately. I made a little stop at the temple this morning to see if I could squeeze a stuffing session in. Guess I didn’t think about if my car could handle the added heft. Could you please help me?"
    #Image: Player holding onto Daisy’s arms as he tries to pull her out.
    "Rolling up your sleeves and grabbing hold of Daisy’s arms, you begin to pull with all of your might while she frantically wriggles around."
    "Your combined teamwork ever so slowly begins to pull her mass of flab out of the car."
    "The glacial movement wears on your muscles as you continue to yank on her, forcing you to push your limits to pull her out inch by inch."
    #Image: Daisy falling on top of the player in the parking lot.
    "One final yank manages to free Daisy from the vehicle’s clutches. This victory is short-lived as she comes flying out and pins you to the ground."
    "Managing to wriggle your way from beneath her, you pop your head out between her breasts to see the apologetic look on her face."
    teacher "Sorry, but at least I’m free. Thank you for your help."
    pc "Not a problem."
    "Despite having her entire mass push down on you, you try to keep up a friendly smile."
    pc "Most of the class already went home. What do you want to do?"
    teacher "Needless to say today’s lesson is cancelled. And I don’t think I’m fitting back in my car while I’m still carrying around all this fattening fluid. Would you mind helping me to the staff break room?"
    pc "Yeah, but could you get off of me first?"
    teacher "Oh! Sorry."
    #Image: Faculty break room.
    "Managing to roll Daisy onto her feet, the two of you move at a slow pace into the break room."
    #Image: Daisy slouched on a couch with her body slick with sweat.
    "Daisy practically collapses onto the couch. Slouching in her spot allows her wide rear to take up most of the cushions in the process."
    "Seeing how exhausted she is from the short walk; you take it upon yourself to grab her some water from the staff fridge."
    teacher "Thank you. That’s just what I needed."
    #Image: Daisy pouring water over her body.
    "Taking the bottle from your fingers, she holds it over her head to douse her body."
    "Though this leaves her even more drenched, the look of relief on her face makes it seem like the small mess was more than worth it. Even still, you’re left a little worried about her current state."
    #Image: Daisy on the couch looking at the player.
    pc "Why didn’t you call me earlier to help you?"
    "She pauses for a moment to collect her thoughts."
    teacher "Needless to say, having to be pulled out of a car can be a little embarrassing."
    pc "Being ashamed of your weight hasn’t really been an issue. Come on, tell me the real reason."
    "She once more goes silent, fidgeting with her plump fingers as she tries to come up with an answer. When she refuses to speak, you decide to take a guess."
    pc "You think I’m worried about how your weight is affecting you."
    #Image: Daisy with a soft smile.
    teacher "Guess nothing gets by my best student. I’ve known since the beginning how much you worry that my rapid weight gain is affecting my daily activities."
    pc "It does seem to get in the way a lot of the time. First with that night with the barbeque and now this with the car."
    teacher "Yes, but I think the pleasure it brings more than makes up for it."
    pc "I appreciate it, but I’m still worried about the long term effects this could have on your life. I don’t want you to ruin yourself just for the sake of seeing how big you can get."
    teacher "You have nothing to worry about, I promise. The Followers of Heset have ways of dealing with women of extraordinarily large sizes like myself."
    "Despite her words, you remain silent. The look of doubt on your face is more than enough to get your point across."
    teacher "I can see that words alone won’t convince you. Give me some time and I’ll prove how capable I can be when I’m this large. I promise."
    "Though you still have your doubts, you’ve been with Daisy long enough to learn to trust her to some extent."
    pc "Alright, we’ll keep going. Just make sure you don’t stuff yourself like crazy before class. I’d rather not have to pull you out of the car again."
    #Image: Daisy with a wide grin.
    teacher "A bit strange for a teacher to be lectured by her own student, but I promise."
    "Leaving Daisy to wait for her body to digest the fattening fluid, you say goodbye and head home for the day."


    $ teacher.weight += 2
    $ teacherstage18event = 0
    $ strip = 0
    $ daytime = 2
    jump freetime


label Daisy_Class_Normal:
    #(NOTE: The following plays out when the player decides to go to class)
    #IMAGE: Daisy standing in front of the class.
    image uni_sexy_teacher_arrive = "/teacher/[teacher.stage]/0/arrive.webp"
    scene uni_sexy_teacher_arrive
    window hide
    pause
    image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
    scene uni_sexy_teacher_greet
    teacher "Hello students."
    s "Hello Ms. Tanwen."
    call rngteachingscene from _call_rngteachingscene_277
    "How will you spend class?"
    menu:
        "Listen to Daisy’s Lesson.":
            call dialogue_choices from _call_dialogue_choices
            #(NOTE: Choice A would lead into either the lessons, pop quizzes, or guest presentations)
            call rngteachingscene from _call_rngteachingscene_278
            if carolineintro1 == 1 and teacher.stage >= 3 and day == 2:
                call Caroline_Intro1 from _call_Caroline_Intro1
            if vickyintro1 == 1 and teacher.stage >= 3 and day == 3:
                call Vicky_Intro1 from _call_Vicky_Intro1
            teacher "That’s it for today. See you all tomorrow!"
            if vickyintro2 == 1 and vickyintro1 == 0 and teacher.stage >= 3 and day == 2:
                call Vicky_Intro2 from _call_Vicky_Intro2
            scene university_leave
            return
        "Read a book." if strip == 0 and booksheld >= 1:
            #(NOTE: Choice B will be the same of giving the player the option to read a book)
            $ bookday = 2
            call book_read from _call_book_read
            if carolineintro1 == 1 and teacher.stage >= 3 and day == 2:
                call Caroline_Intro1
            return
        "Rest.":
            scene black with dissolve
            "A little tired, you see little harm in just spacing out during class."
            if carolineintro1 == 1 and teacher.stage >= 3 and day == 2:
                image caroline_stage1_17 = "/caroline/events/stage1/17.webp"
                scene caroline_stage1_17 with dissolve
                "You suddenly wake up."
                call Caroline_Intro1 from _call_Caroline_Intro1_1
                image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
                scene uni_sexy_teacher_greet
                "Waving goodbye to Daisy on the way out, you continue with your day."
            elif vickyintro1 == 1 and teacher.stage >= 3 and day == 3:
                image caroline_stage1_17 = "/caroline/events/stage1/17.webp"
                scene caroline_stage1_17 with dissolve
                "You suddenly wake up."
                call Vicky_Intro1 from _call_Vicky_Intro1_1
                image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
                scene uni_sexy_teacher_greet
                "Waving goodbye to Daisy on the way out, you continue with your day."
            else:
                image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
                scene uni_sexy_teacher_greet with dissolve
                "Your attention returns just in time to see the rest of the students leaving. You wave goodbye to Daisy on the way out."
                if vickyintro2 == 1 and vickyintro1 == 0 and teacher.stage >= 3 and day == 2:
                    call Vicky_Intro2 from _call_Vicky_Intro2_1
                    scene university_leave
                    return
                scene university_leave
                return
            return
