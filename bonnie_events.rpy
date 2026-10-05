#Bonnie Events

label bonnie_home1:

    if bonnie.stage <= 4:
        ##### Scene image – Bonnie in front of shop like normal (Normal clothing)####
        image cafe_bonnie_home_outside = "/bonnie/[bonnie.stage]/home_outside.webp"
        scene cafe_bonnie_home_outside
        bonnie "Thank you for offering to do this. It really means a lot."
        pc "No problem. Is everything ready in the kitchen?"
        image cafe_bonnie_home_showkitchen = "/bonnie/[bonnie.stage]/home_showkitchen.webp"
        scene cafe_bonnie_home_showkitchen
        play music "/music/bonnie.ogg" if_changed
        bonnie "Sure is!"
    elif bonnie.stage == 5:
        image cafe_bonnie_home_outside = "/bonnie/[bonnie.stage]/home_outside.webp"
        scene cafe_bonnie_home_outside
        bonnie "I don’t know why I keep meeting you out here."
        image bonnie_stage5_home_outside2 = "/bonnie/events/stage5/home_outside2.webp"
        scene bonnie_stage5_home_outside2
        bonnie "Guess I am just excited."
        pc "I'm excited too, making chocolates with you is always fun."
        image cafe_bonnie_home_showkitchen = "/bonnie/[bonnie.stage]/home_showkitchen.webp"
        scene cafe_bonnie_home_showkitchen
        play music "/music/bonnie.ogg" if_changed
        bonnie "Sure is!"
    elif bonnie.stage == 6:
        image cafe_bonnie_home_showkitchen_alt = "/bonnie/[bonnie.stage]/home_showkitchen_alt.webp"
        scene cafe_bonnie_home_showkitchen_alt
        play music "/music/bonnie.ogg" if_changed

    if bonnie.stage == 4:
        "Walking in, you notice that some of the bags of ingredients seem bigger this time. Did she want more to deal with another rush of customers?"
        "Or was she secretly hoping for some more leftovers?"
    elif bonnie.stage == 5 or bonnie.stage == 6:
        "Walking in you notice the same larger bags of ingredients that have become the new normal."

    if bonnie.stage == 6:
        "You also notice Bonnie standing at the counter waiting for you."
        image bonnie_stage6_talk1 = "/bonnie/events/stage6/talk1.webp"
        scene bonnie_stage6_talk1
        bonnie "Hey, didn’t get lost then!"
        pc "Nope, although I did almost get lost somewhere between the door and the coat rack."
        image bonnie_stage6_talk2 = "/bonnie/events/stage6/talk2.webp"
        scene bonnie_stage6_talk2
        "Bonnie smiles back at you, the two of you seeming to share a moment."
        pc "Shall I?"
        image bonnie_stage6_talk3 = "/bonnie/events/stage6/talk3.webp"
        scene bonnie_stage6_talk3
        bonnie "Oh right, the chocolates."
        image cafe_bonnie_home_cooking1_alt = "/bonnie/[bonnie.stage]/cooking1_alt.webp"
        scene cafe_bonnie_home_cooking1_alt
    else:
        image cafe_bonnie_home_cooking1 = "/bonnie/[bonnie.stage]/cooking1.webp"
        scene cafe_bonnie_home_cooking1
    "Grabbing a cooking pan you begin to prepare the chocolates."
    if bonnie.stage == 2:
        bonnie "The customers are excited to have these chocolates again."
        image cafe_bonnie_home_cooking2 = "/bonnie/[bonnie.stage]/cooking2.webp"
        scene cafe_bonnie_home_cooking2
        pc "That’s good to hear."
        bonnie "I still don’t know how you did it."
        pc "Here, the first ones are ready if you want to taste them."
    elif bonnie.stage == 3:
        bonnie "The customers have been telling me how much they are enjoying your chocolates."
        bonnie "Some of them even thought my old partner had come back."
        image cafe_bonnie_home_cooking2 = "/bonnie/[bonnie.stage]/cooking2.webp"
        scene cafe_bonnie_home_cooking2
        pc "I'm glad they are enjoying them."
        bonnie "They are not the only ones."
        image bonnie_stage3_talk1 = "/bonnie/events/stage3/talk1.webp"
        scene bonnie_stage3_talk1
        "Bonnie seems to look down at her growing waistline nervously."
        pc "That’s good too, you deserve to treat yourself sometimes too."
        image bonnie_stage3_talk2 = "/bonnie/events/stage3/talk2.webp"
        scene bonnie_stage3_talk2
        bonnie "You’re right. Maybe just in moderation though."
        pc "Here, the first ones are ready if you want to taste them."
    elif bonnie.stage == 4:
        bonnie "The customers are loving the chocolates. I think we are selling more than we ever did before."
        image cafe_bonnie_home_cooking2 = "/bonnie/[bonnie.stage]/cooking2.webp"
        scene cafe_bonnie_home_cooking2
        pc "That’s good to hear. Hopefully it takes some of the worry off your shoulders."
        "As things get underway you notice Bonnie loitering around you more than she had done before, her eyes glued to the dark brown sugary mixture you are stirring."
        "As the room fills with the sweet scent of melting chocolate Bonnie is practically salivating."
    elif bonnie.stage == 5:
        bonnie "Thank you for doing this again, the shop has been doing much better since you started helping out."
        image cafe_bonnie_home_cooking2 = "/bonnie/[bonnie.stage]/cooking2.webp"
        scene cafe_bonnie_home_cooking2
        pc "That’s good to hear."
        image bonnie_stage5_home_talking1 = "/bonnie/events/stage5/home_talking1.webp"
        scene bonnie_stage5_home_talking1
        bonnie "No I mean it, you saved me, the shop. I'm not sure what I would have done without you."
        pc "I'm sure you would have been fine. People love you and your shop."
        "As things get underway you notice Bonnie loitering around you once again."
        image bonnie_stage5_home_talking2 = "/bonnie/events/stage5/home_talking2.webp"
        scene bonnie_stage5_home_talking2
        "Her eyes watching you intently as you stir the sweet-smelling chocolate."
    elif bonnie.stage == 6:
        image cafe_bonnie_home_cooking2_alt = "/bonnie/[bonnie.stage]/cooking2_alt.webp"
        scene cafe_bonnie_home_cooking2_alt
        "As things get underway you notice Bonnie loitering around you once again."
        image bonnie_stage6_home_talking1 = "/bonnie/events/stage6/home_talking1.webp"
        scene bonnie_stage6_home_talking1
        "Her eyes watching you intently as you stir the sweet-smelling chocolate."
        pc "Here, the first ones are ready if you want to taste them."
        image cafe_bonnie_home_eating3_alt = "/bonnie/[bonnie.stage]/eating3_alt.webp"
        scene cafe_bonnie_home_eating3_alt
        "Bonnie quickly takes the chocolate from you, chewing slowly to savour the flavour."
        "Despite her eagerness it's clear something is bothering her."
        pc "Something wrong with the chocolates."
        image bonnie_stage6_talk4 = "/bonnie/events/stage6/talk4.webp"
        scene bonnie_stage6_talk4
        bonnie "What! No they are as good as they ever were."
        bonnie "Its just, the new ones you made were so special these seem a bit plain now."
        bonnie "Guess I've just been spoiled."
        bonnie "Would certainly explain this."
        image bonnie_stage6_talk5 = "/bonnie/events/stage6/talk5.webp"
        scene bonnie_stage6_talk5
        "Bonnie gestures to her growing body, allowing you to stare at it without feeling guilty."
        image bonnie_stage6_talk6 = "/bonnie/events/stage6/talk6.webp"
        scene bonnie_stage6_talk6
        pc "I can make some more for you if you would like me to."
        image bonnie_stage6_talk7 = "/bonnie/events/stage6/talk7.webp"
        scene bonnie_stage6_talk7
        bonnie "Really, that would be great!"
        pc "Sure thing."
        image cafe_bonnie_home_cooking3_alt = "/bonnie/[bonnie.stage]/cooking3_alt.webp"
        scene cafe_bonnie_home_cooking3_alt
        "Starting on the next batch you continue to hand her tasters throughout the evening."
        image cafe_bonnie_home_eating4_alt = "/bonnie/[bonnie.stage]/eating4_alt.webp"
        scene cafe_bonnie_home_eating4_alt
        "While not the new chocolates she was hoping for she still takes them eagerly."
        "With enough made for the shop for the week you make a batch of the new chocolates."
        image cafe_bonnie_home_finishedcooking_alt = "/bonnie/[bonnie.stage]/finishedcooking_alt.webp"
        scene cafe_bonnie_home_finishedcooking_alt
        bonnie "I think that should do. Besides, you have earned a break."
        if bonniestage4event == 0:
            $ money += 10
            "You earned ten dollars."
        bonnie "Why don't you follow me to the couch? We can continue watching Choc-off, if you like."
        pc "Good timing, I think the last batches have just finished up."

    if bonnie.stage <= 3:
        image cafe_bonnie_home_eating3 = "/bonnie/[bonnie.stage]/eating3.webp"
        scene cafe_bonnie_home_eating3
        "Bonnie quickly takes the chocolate from you, chewing slowly to savour the flavour."
        image cafe_bonnie_home_cooking3 = "/bonnie/[bonnie.stage]/cooking3.webp"
        scene cafe_bonnie_home_cooking3
        "Starting on the next few batches you continue to hand her tasters from time to time."
        image cafe_bonnie_home_eating4 = "/bonnie/[bonnie.stage]/eating4.webp"
        scene cafe_bonnie_home_eating4
        "Each one she takes gleefully, both of you enjoying your working relationship."
        "After a couple of hours the room is filled with chocolates to satisfy Bonnie's customers for the next week. Plus a few extra you have put aside or fed to your assistant."
        image cafe_bonnie_home_finishedcooking = "/bonnie/[bonnie.stage]/finishedcooking.webp"
        scene cafe_bonnie_home_finishedcooking
        bonnie "I think that should do. Besides, you have earned a break."
        bonnie "Why don’t you follow me to the couch, we can watch something while that last batch finishes setting up."
    elif bonnie.stage <= 5:
        pc "Here, the first ones are ready if you want to taste them."
        image cafe_bonnie_home_eating3 = "/bonnie/[bonnie.stage]/eating3.webp"
        scene cafe_bonnie_home_eating3
        "Bonnie quickly takes the chocolate from you, chewing slowly to savour the flavour."
        "Starting on the next batches you continue to hand her tasters."
        image cafe_bonnie_home_eating4 = "/bonnie/[bonnie.stage]/eating4.webp"
        scene cafe_bonnie_home_eating4
        if bonnie.stage == 4:
            "Unlike before she seems happy to take any and all of them from you, all of her inhibitions removed."
            "Grabbing some of the brown sugar you “accidentally” add an extra cup knowing it will ruin the smoothness and alter the colour."
        elif bonnie.stage == 5:
            "She seems happy to take any and all of them from you, her inhibitions gone and replaced with the freedom to eat what she wants."
            "No longer needing to disguise it you make another batch for tonight’s viewing."
        "Taking the previous batch out of the fridge you hand Bonnie a few from the tray to “test”."
        "Not that there was much testing going on at this point."
        image cafe_bonnie_home_cooking3 = "/bonnie/[bonnie.stage]/cooking3.webp"
        scene cafe_bonnie_home_cooking3
        "After a couple of hours the room is filled with chocolates to satisfy Bonnie's customers for the next week."
        bonnie "I think that should do. Besides, you have earned a break."
        if bonniestage4event == 0:
            $ money += 10
            "You earned ten dollars."
        bonnie "Why don't you follow me to the couch? We can continue watching Choc-off, if you like."
        pc "Sure thing. I will just check on the last couple of batches."
        if bonnie.stage == 4:
            "Finding the “ruined” batch you are happy to see they have a totally different texture and colouration."


    ##### Scene image – Bonnie sitting on couch with TV on ####
    if bonnie.stage == 2:
        image cafe_bonnie_home_sitting1 = "/bonnie/[bonnie.stage]/sitting1.webp"
        scene cafe_bonnie_home_sitting1
        "Grabbing a few “spares” you join Bonnie on the couch and hand them to her."
        bonnie "What are these?"
        pc "You can't watch something without snacks."
        pc "These are a few that didn’t go quite right anyway. Wouldn’t want them to go to waste."
        image cafe_bonnie_home_eating1 = "/bonnie/[bonnie.stage]/eating1.webp"
        scene cafe_bonnie_home_eating1
        "Taking a bite you see the familiar look in her eyes."
        bonnie "They taste fine to me."
        "But despite that comment, she doesn’t seem in any hurry to give them back."
        "Flicking through the channels you manage to find the latest season of choc-off. The chocolate making contest that has taken the country by storm."
        image cafe_bonnie_home_sitting2 = "/bonnie/[bonnie.stage]/sitting2.webp"
        scene cafe_bonnie_home_sitting2
        bonnie "I really hope Sue wins, her desserts always look so nice."
    elif bonnie.stage == 3:
        image cafe_bonnie_home_sitting1 = "/bonnie/[bonnie.stage]/sitting1.webp"
        scene cafe_bonnie_home_sitting1
        "Grabbing some extras, you join Bonnie on the couch and hand them to her."
        bonnie "More snacks?"
        pc "I can put them back if you don’t want them?"
        bonnie "I…I didn’t say that, just had a lot of them already."
        "Despite her slight protest Bonnie takes the chocolates and begins to make her way through them."
        image cafe_bonnie_home_eating1 = "/bonnie/[bonnie.stage]/eating1.webp"
        scene cafe_bonnie_home_eating1
        "Taking a bite you see the familiar look in her eyes."
        "Flicking through the channels you manage to find the latest season of choc-off. The chocolate making contest that has taken the country by storm."
        image cafe_bonnie_home_sitting2 = "/bonnie/[bonnie.stage]/sitting2.webp"
        scene cafe_bonnie_home_sitting2
        bonnie "I'm so happy to see Sue made it, her desserts always look so nice."
        bonnie "I was a bit nervous when she was in the elimination trial last week."
        pc "Her chocolate eclair looked so good though."
        bonnie "Ughh, now I want an eclair."
    elif bonnie.stage == 4:
        image cafe_bonnie_home_sitting1 = "/bonnie/[bonnie.stage]/sitting1.webp"
        scene cafe_bonnie_home_sitting1
        "Walking over with the pile of chocolates in hand you join Bonnie on the couch, laying them down next to her."
        bonnie "What are these?"
        pc "Looks like I must have made a mistake with one of the batches, but no point in wasting them right?"
        bonnie "Definitely don’t want to waste any."
        image cafe_bonnie_home_eating1 = "/bonnie/[bonnie.stage]/eating1.webp"
        scene cafe_bonnie_home_eating1
        "Watching her take a bite you see the familiar look in her eyes."
        bonnie "They are still good, but they taste a bit too sweet."
        "Despite that comment, she doesn’t seem in any hurry to give them back."
        "Flicking through the channels, you find the latest Choc-off; the chocolate making contest that has taken the country by storm."
        image cafe_bonnie_home_sitting2 = "/bonnie/[bonnie.stage]/sitting2.webp"
        scene cafe_bonnie_home_sitting2
        bonnie "I'm happy Sue is still doing well. Her desserts last week were amazing."
        "Over the next hour you watch the contestants sweat it out as they try to make a showstopping chocolate treat for the judges."
        image cafe_bonnie_home_eating2 = "/bonnie/[bonnie.stage]/eating2.webp"
        scene cafe_bonnie_home_eating2
        "Enthralled by the contest, Bonnie manages to demolish the entire batch of chocolates you have given to her in no time at all."
        image cafe_bonnie_home_stuffed1 = "/bonnie/[bonnie.stage]/stuffed1.webp"
        scene cafe_bonnie_home_stuffed1
        "The bulge in her stomach is larger than it was last week. Had she gained weight or is it just your imagination?"
        image cafe_bonnie_home_stuffed2 = "/bonnie/[bonnie.stage]/stuffed2.webp"
        scene cafe_bonnie_home_stuffed2
        "Staring at her bulging belly you wonder how many extra calories that cup of sugar might have added to the already substantial number they contained."
    elif bonnie.stage == 5:
        image cafe_bonnie_home_sitting1 = "/bonnie/[bonnie.stage]/sitting1.webp"
        scene cafe_bonnie_home_sitting1
        "Walking over with the pile of chocolates in hand you join Bonnie on the couch, laying them down next to her."
        bonnie "You’d think I’d be sick of these by now. But they are just so damn good."
        image cafe_bonnie_home_eating1 = "/bonnie/[bonnie.stage]/eating1.webp"
        scene cafe_bonnie_home_eating1
        "Watching her take a bite you see the familiar look in her eyes."
        "Flicking through the channels, you find the latest Choc-off; the chocolate making contest that has taken the country by storm."
        image cafe_bonnie_home_sitting2 = "/bonnie/[bonnie.stage]/sitting2.webp"
        scene cafe_bonnie_home_sitting2
        bonnie "Sue has almost made it to the final, it was a bit touch and go though."
        pc "Nah, we knew she would always make it. Although I still think John’s was the best show stopper last week."
        bonnie "It looked so good! I wish I could have tasted it."
        image cafe_bonnie_home_eating2 = "/bonnie/[bonnie.stage]/eating2.webp"
        scene cafe_bonnie_home_eating2
        "Over the next hour you watch the contestants sweat it out as they try to make a showstopping chocolate treat for the judges."
        "Enthralled by the contest, Bonnie manages to demolish the entire batch of chocolates you have given to her in no time at all."
        image cafe_bonnie_home_stuffed1 = "/bonnie/[bonnie.stage]/stuffed1.webp"
        scene cafe_bonnie_home_stuffed1
        "The bulge in her stomach still growing week after week, the overindulgence on fattening treats really having an impact now."
        image cafe_bonnie_home_stuffed2 = "/bonnie/[bonnie.stage]/stuffed2.webp"
        scene cafe_bonnie_home_stuffed2
        "As the completed chocolate deserts are taken to the judges, you let yourself fantasise about what it would be like to feed those masses of sugar, butter and chocolate to Bonnie."
        image cafe_bonnie_home_sitting3 = "/bonnie/[bonnie.stage]/sitting3.webp"
        scene cafe_bonnie_home_sitting3
        bonnie "That was so good, I hope you enjoyed it."
        pc "I did, although I still think you could beat them all."
        image cafe_bonnie_home_sitting4 = "/bonnie/[bonnie.stage]/sitting4.webp"
        scene cafe_bonnie_home_sitting4
        bonnie "No way, although your chocolates might."
        bonnie "We should totally enter next year. Between us we would be unstoppable!"
        pc "Only if I can have you as chief taster!"
        bonnie "Like you even have to ask?"
    elif bonnie.stage == 6:
        image cafe_bonnie_home_sitting1_alt = "/bonnie/[bonnie.stage]/sitting1_alt.webp"
        scene cafe_bonnie_home_sitting1_alt
        "Walking over with the new  chocolates in hand you join Bonnie on the couch, laying them down next to her."
        image bonnie_stage6_newbox = "/bonnie/events/stage6/newbox.webp"
        scene bonnie_stage6_newbox
        bonnie "Are these the new ones?"
        image cafe_bonnie_home_eating1_alt = "/bonnie/[bonnie.stage]/eating1_alt.webp"
        scene cafe_bonnie_home_eating1_alt
        "Watching her take a bite you see the familiar look in her eyes."
        bonnie "These new chocolates are just amazing."
        image cafe_bonnie_home_sitting2_alt = "/bonnie/[bonnie.stage]/sitting2_alt.webp"
        scene cafe_bonnie_home_sitting2_alt
        bonnie "There is no way you would loose if you took these on the Choc-off."
        pc "I think you might be a little biased."
        bonnie "Maybe a little…."
        image cafe_bonnie_home_eating2_alt = "/bonnie/[bonnie.stage]/eating2_alt.webp"
        scene cafe_bonnie_home_eating2_alt
        "Flicking through the channels you find the multi-stage semi final of the choc-off. The chocolate making contest that has taken the country by storm."
        "Over the next hour you watch the contestants sweat it out as they try to make a showstopping chocolate treat for the judges."
        image cafe_bonnie_home_stuffed1_alt = "/bonnie/[bonnie.stage]/stuffed1_alt.webp"
        scene cafe_bonnie_home_stuffed1_alt
        "Enthralled by the contest, Bonnie manages to demolish the entire batch of chocolates you have given to her in no time at all."
        image cafe_bonnie_home_stuffed2_alt = "/bonnie/[bonnie.stage]/stuffed2_alt.webp"
        scene cafe_bonnie_home_stuffed2_alt
        "The bulge in her stomach still growing week after week, the overindulgence on fattening treats really having an impact now."
        image cafe_bonnie_home_sitting3_alt = "/bonnie/[bonnie.stage]/sitting3_alt.webp"
        scene cafe_bonnie_home_sitting3_alt
        bonnie "That was so good."
        bonnie "I still think we should enter next season!"
        pc "Only if I can have you as chief taster!"
        image cafe_bonnie_home_sitting4_alt = "/bonnie/[bonnie.stage]/sitting4_alt.webp"
        scene cafe_bonnie_home_sitting4_alt
        bonnie "Like you even have to ask?"
    if bonnie.stage <= 3:
        "Over the next hour you watch the contestants sweat it out as they try to make a showstopping chocolate treat for the judges."
        image cafe_bonnie_home_eating2 = "/bonnie/[bonnie.stage]/eating2.webp"
        scene cafe_bonnie_home_eating2
        "Enthralled by the contest, Bonnie manages to demolish the chocolates you have given to her in no time at all."
        image cafe_bonnie_home_stuffed1 = "/bonnie/[bonnie.stage]/stuffed1.webp"
        scene cafe_bonnie_home_stuffed1
        "Out of the corner of your eye you can definitely see her belly growing in size."
        image cafe_bonnie_home_stuffed2 = "/bonnie/[bonnie.stage]/stuffed2.webp"
        scene cafe_bonnie_home_stuffed2
        "The cost of such a thorough taste testing."
    if bonnie.stage <= 4:
        "As the completed giant chocolate desserts are taken to the judges, you can't help but fantasise about what it would be like to feed those masses of sugar, butter and chocolate to Bonnie."
        image cafe_bonnie_home_sitting3 = "/bonnie/[bonnie.stage]/sitting3.webp"
        scene cafe_bonnie_home_sitting3
        bonnie "That was so good, I hope you enjoyed it."
        pc "Totally, but I still think you could beat them all."
        image cafe_bonnie_home_sitting4 = "/bonnie/[bonnie.stage]/sitting4.webp"
        scene cafe_bonnie_home_sitting4
        bonnie "No way, although your chocolates might."
    if bonniestory <= 1 and bonnie.stage >= 4:
        call bonniestoryask from _call_bonniestoryask
    elif bonniestory == 0 and bonnie.stage >= 3:
        call bonniestoryask from _call_bonniestoryask_1
    bonnie "By the way, that last batch should be done by now."

    scene outside2
    stop music fadeout 1.0
    "Grabbing the last batch out of the fridge you help Bonnie clear up and head home."
    "You hope her customers enjoy all the chocolates you made."

    $ bonnie.weight += 0.5
    return


label bonnie_home2:

    ##### Scene image – Bonnie in front of shop like normal (Normal clothing)####
    if bonnie.stage == 4:
        image cafe_bonnie_home_outside = "/bonnie/[bonnie.stage]/home_outside.webp"
        scene cafe_bonnie_home_outside
        bonnie "Thank you for offering to do this. It really means a lot."
        pc "No problem. Is everything ready in the kitchen?"
        image cafe_bonnie_home_showkitchen = "/bonnie/[bonnie.stage]/home_showkitchen.webp"
        scene cafe_bonnie_home_showkitchen
        play music "/music/bonnie.ogg" if_changed
        bonnie "Sure is!"
    elif bonnie.stage == 5:
        image cafe_bonnie_home_outside = "/bonnie/[bonnie.stage]/home_outside.webp"
        scene cafe_bonnie_home_outside
        bonnie "I don’t know why I keep meeting you out here."
        image bonnie_stage5_home_outside2 = "/bonnie/events/stage5/home_outside2.webp"
        scene bonnie_stage5_home_outside2
        bonnie "Guess I am just excited."
        pc "I'm excited too, making chocolates with you is always fun."
        image cafe_bonnie_home_showkitchen = "/bonnie/[bonnie.stage]/home_showkitchen.webp"
        scene cafe_bonnie_home_showkitchen
        play music "/music/bonnie.ogg" if_changed
        bonnie "Sure is!"


    ##### Scene image – Bonnie next to counter in her apron and underwear ####
    if bonnie.stage == 4:
        "Walking in, you notice that some of the bags of ingredients seem bigger this time. Did she want more to deal with another rush of customers?"
        "Or was she secretly hoping for some more leftovers?"
        image cafe_bonnie_home_cooking1 = "/bonnie/[bonnie.stage]/cooking1.webp"
        scene cafe_bonnie_home_cooking1
        "Grabbing a cooking pan you begin to prepare the chocolates."
        bonnie "The customers are loving the chocolates. I think we are selling more than we ever did before."
        image cafe_bonnie_home_cooking2 = "/bonnie/[bonnie.stage]/cooking2.webp"
        scene cafe_bonnie_home_cooking2
        pc "That’s good to hear. Hopefully it takes some of the worry off your shoulders."
        "As things get underway you notice Bonnie loitering around you more than she had done before, her eyes glued to the dark brown sugary mixture you are stirring."
        "As the room fills with the sweet scent of melting chocolate Bonnie is practically salivating."
        pc "Here, the first ones are ready if you want to taste them."
        image cafe_bonnie_home_eating3 = "/bonnie/[bonnie.stage]/eating3.webp"
        scene cafe_bonnie_home_eating3
        "Bonnie quickly takes the chocolate from you, chewing slowly to savour the flavour."
        "Starting on the next batches you continue to hand her tasters."
        image cafe_bonnie_home_eating4 = "/bonnie/[bonnie.stage]/eating4.webp"
        scene cafe_bonnie_home_eating4
        "Unlike before she seems happy to take any and all of them from you, all of her inhibitions removed."
        "Grabbing some of the brown sugar you “accidentally” add an extra cup knowing it will ruin the smoothness and alter the colour."
        "Taking the previous batch out of the fridge you hand Bonnie a few from the tray to “test”."
        "Not that there was much testing going on at this point."
        image cafe_bonnie_home_cooking3 = "/bonnie/[bonnie.stage]/cooking3.webp"
        scene cafe_bonnie_home_cooking3
        "After a couple of hours the room is filled with chocolates to satisfy Bonnie's customers for the next week."
        image cafe_bonnie_home_finishedcooking = "/bonnie/[bonnie.stage]/finishedcooking.webp"
        scene cafe_bonnie_home_finishedcooking
        bonnie "I think that should do. Besides, you have earned a break."
        if bonniestage4event == 0:
            $ money += 10
            "You earned ten dollars."
        bonnie "Why don't you follow me to the couch? We can continue watching Choc-off, if you like."
        pc "Sure thing. I will just check on the last couple of batches."
        "Finding the “ruined” batch you are happy to see they have a totally different texture and colouration."
    if bonnie.stage == 5:
        "Walking in you notice the same larger bags of ingredients that have become the new normal."
        image cafe_bonnie_home_cooking1 = "/bonnie/[bonnie.stage]/cooking1.webp"
        scene cafe_bonnie_home_cooking1
        "Grabbing a cooking pan you begin to prepare the chocolates."
        bonnie "Thank you for doing this again, the shop has been doing much better since you started helping out."
        image cafe_bonnie_home_cooking2 = "/bonnie/[bonnie.stage]/cooking2.webp"
        scene cafe_bonnie_home_cooking2
        pc "That’s good to hear."
        image bonnie_stage5_home_talking1 = "/bonnie/events/stage5/home_talking1.webp"
        scene bonnie_stage5_home_talking1
        bonnie "No I mean it, you saved me, the shop. I'm not sure what I would have done without you."
        pc "I'm sure you would have been fine. People love you and your shop."
        "As things get underway you notice Bonnie loitering around you once again."
        image bonnie_stage5_home_talking2 = "/bonnie/events/stage5/home_talking2.webp"
        scene bonnie_stage5_home_talking2
        "Her eyes watching you intently as you stir the sweet-smelling chocolate."
        pc "Here, the first ones are ready if you want to taste them."
        image cafe_bonnie_home_eating3 = "/bonnie/[bonnie.stage]/eating3.webp"
        scene cafe_bonnie_home_eating3
        "Bonnie quickly takes the chocolate from you, chewing slowly to savour the flavour."
        "Starting on the next batches you continue to hand her tasters."
        image cafe_bonnie_home_eating4 = "/bonnie/[bonnie.stage]/eating4.webp"
        scene cafe_bonnie_home_eating4
        "She seems happy to take any and all of them from you, her inhibitions gone and replaced with the freedom to eat what she wants."
        "No longer needing to disguise it you make another batch for tonight’s viewing."
        "Taking the previous batch out of the fridge you hand Bonnie a few from the tray to test."
        "Not that there was much testing going on at this point."
        image cafe_bonnie_home_cooking3 = "/bonnie/[bonnie.stage]/cooking3.webp"
        scene cafe_bonnie_home_cooking3
        "After a couple of hours the room is filled with chocolates to satisfy Bonnie's customers for the next week."
        image cafe_bonnie_home_finishedcooking = "/bonnie/[bonnie.stage]/finishedcooking.webp"
        scene cafe_bonnie_home_finishedcooking
        bonnie "I think that should do. Besides, you have earned a break."
        if bonniestage4event == 0:
            $ money += 10
            "You earned ten dollars."
        bonnie "Why don't you follow me to the couch? We can continue watching Choc-off, if you like."
        pc "Sure thing. I will just check on the last couple of batches."
    if bonnie.stage == 6:
        image cafe_bonnie_home_showkitchen_alt = "/bonnie/[bonnie.stage]/home_showkitchen_alt.webp"
        scene cafe_bonnie_home_showkitchen_alt
        play music "/music/bonnie.ogg" if_changed
        "Walking in you notice the same larger bags of ingredients that have become the new normal."
        "You also notice Bonnie standing at the counter waiting for you."
        image bonnie_stage6_talk1 = "/bonnie/events/stage6/talk1.webp"
        scene bonnie_stage6_talk1
        bonnie "Hey, didn’t get lost then!"
        pc "Nope, although I did almost get lost somewhere between the door and the coat rack."
        image bonnie_stage6_talk2 = "/bonnie/events/stage6/talk2.webp"
        scene bonnie_stage6_talk2
        "Bonnie smiles back at you, the two of you seeming to share a moment."
        pc "Shall I?"
        image bonnie_stage6_talk3 = "/bonnie/events/stage6/talk3.webp"
        scene bonnie_stage6_talk3
        bonnie "Oh right, the chocolates."
        image cafe_bonnie_home_cooking1_alt = "/bonnie/[bonnie.stage]/cooking1_alt.webp"
        scene cafe_bonnie_home_cooking1_alt
        "Grabbing a cooking pan you begin to prepare the chocolates."
        image cafe_bonnie_home_cooking2_alt = "/bonnie/[bonnie.stage]/cooking2_alt.webp"
        scene cafe_bonnie_home_cooking2_alt
        "As things get underway you notice Bonnie loitering around you once again."
        image bonnie_stage6_home_talking1 = "/bonnie/events/stage6/home_talking1.webp"
        scene bonnie_stage6_home_talking1
        "Her eyes watching you intently as you stir the sweet-smelling chocolate."
        pc "Here, the first ones are ready if you want to taste them."
        image cafe_bonnie_home_eating3_alt = "/bonnie/[bonnie.stage]/eating3_alt.webp"
        scene cafe_bonnie_home_eating3_alt
        "Bonnie quickly takes the chocolate from you, chewing slowly to savour the flavour."
        "Despite her eagerness it's clear something is bothering her."
        pc "Something wrong with the chocolates."
        image bonnie_stage6_talk4 = "/bonnie/events/stage6/talk4.webp"
        scene bonnie_stage6_talk4
        bonnie "What! No they are as good as they ever were."
        bonnie "Its just, the new ones you made were so special these seem a bit plain now."
        bonnie "Guess I've just been spoiled."
        bonnie "Would certainly explain this."
        image bonnie_stage6_talk5 = "/bonnie/events/stage6/talk5.webp"
        scene bonnie_stage6_talk5
        "Bonnie gestures to her growing body, allowing you to stare at it without feeling guilty."
        image bonnie_stage6_talk6 = "/bonnie/events/stage6/talk6.webp"
        scene bonnie_stage6_talk6
        pc "I can make some more for you if you would like me to."
        image bonnie_stage6_talk7 = "/bonnie/events/stage6/talk7.webp"
        scene bonnie_stage6_talk7
        bonnie "Really, that would be great!"
        pc "Sure thing."
        image cafe_bonnie_home_cooking3_alt = "/bonnie/[bonnie.stage]/cooking3_alt.webp"
        scene cafe_bonnie_home_cooking3_alt
        "Starting on the next batch you continue to hand her tasters throughout the evening."
        image cafe_bonnie_home_eating4_alt = "/bonnie/[bonnie.stage]/eating4_alt.webp"
        scene cafe_bonnie_home_eating4_alt
        "While not the new chocolates she was hoping for she still takes them eagerly."
        "With enough made for the shop for the week you make a batch of the new chocolates."
        image cafe_bonnie_home_finishedcooking_alt = "/bonnie/[bonnie.stage]/finishedcooking_alt.webp"
        scene cafe_bonnie_home_finishedcooking_alt
        bonnie "I think that should do. Besides, you have earned a break."
        if bonniestage4event == 0:
            $ money += 10
            "You earned ten dollars."
        bonnie "Why don't you follow me to the couch? We can continue watching Choc-off, if you like."
        pc "Good timing, I think the last batches have just finished up."



    ##### Scene image – Bonnie sitting on couch ####
    if bonnie.stage == 4:
        image cafe_bonnie_home_sitting1 = "/bonnie/[bonnie.stage]/sitting1.webp"
        scene cafe_bonnie_home_sitting1
        "Walking over with the pile of chocolates in hand you join Bonnie on the couch, laying them down next to her."
        bonnie "What are these?"
        pc "Looks like I must have made a mistake with one of the batches, but no point in wasting them right?"
        bonnie "Definitely don’t want to waste any."
        image cafe_bonnie_home_eating1 = "/bonnie/[bonnie.stage]/eating1.webp"
        scene cafe_bonnie_home_eating1
        "Watching her take a bite you see the familiar look in her eyes."
        bonnie "They are still good, but they taste a bit too sweet."
        "Despite that comment, she doesn’t seem in any hurry to give them back."
        "Flicking through the channels, you find the latest Choc-off; the chocolate making contest that has taken the country by storm."
        image cafe_bonnie_home_sitting2 = "/bonnie/[bonnie.stage]/sitting2.webp"
        scene cafe_bonnie_home_sitting2
        bonnie "I'm happy Sue is still doing well. Her desserts last week were amazing."
        "Over the next hour you watch the contestants sweat it out as they try to make a showstopping chocolate treat for the judges."
        image cafe_bonnie_home_eating2 = "/bonnie/[bonnie.stage]/eating2.webp"
        scene cafe_bonnie_home_eating2
        "Enthralled by the contest, Bonnie manages to demolish the entire batch of chocolates you have given to her in no time at all."
        image cafe_bonnie_home_stuffed1 = "/bonnie/[bonnie.stage]/stuffed1.webp"
        scene cafe_bonnie_home_stuffed1
        "The bulge in her stomach is larger than it was last week. Had she gained weight or is it just your imagination?"
        image cafe_bonnie_home_stuffed2 = "/bonnie/[bonnie.stage]/stuffed2.webp"
        scene cafe_bonnie_home_stuffed2
        "Staring at her bulging belly you wonder how many extra calories that cup of sugar might have added to the already substantial number they contained."
        "As the completed giant chocolate desserts are taken to the judges, you let yourself fantasise about what it would be like to feed those masses of sugar, butter and chocolate to Bonnie."
        image cafe_bonnie_home_sitting3 = "/bonnie/[bonnie.stage]/sitting3.webp"
        scene cafe_bonnie_home_sitting3
        bonnie "That was so good, I hope you enjoyed it."
        pc "I did. Although, I still think you could beat them all."
        image cafe_bonnie_home_sitting4 = "/bonnie/[bonnie.stage]/sitting4.webp"
        scene cafe_bonnie_home_sitting4
        bonnie "No way. Although, your chocolates might."
        if bonniestory <= 1:
            menu:
                "Ask Bonnie about her past.":
                    "You decide to ask Bonnie about her past."
                    bonnie "Sure, I would love to talk about myself."
                    "Bonnie talks a bit about herself."
                    $ bonniestory += 1
                    #Unlocks more Bonnie story in the stats page.
                    $ renpy.notify("New Bonnie story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Bonnie anything."
        bonnie "By the way, that last batch should be done by now."
    elif bonnie.stage == 5:
        image cafe_bonnie_home_sitting1 = "/bonnie/[bonnie.stage]/sitting1.webp"
        scene cafe_bonnie_home_sitting1
        "Walking over with the pile of chocolates in hand you join Bonnie on the couch, laying them down next to her."
        bonnie "You’d think I’d be sick of these by now. But they are just so damn good."
        image cafe_bonnie_home_eating1 = "/bonnie/[bonnie.stage]/eating1.webp"
        scene cafe_bonnie_home_eating1
        "Watching her take a bite you see the familiar look in her eyes."
        "Flicking through the channels, you find the latest Choc-off; the chocolate making contest that has taken the country by storm."
        image cafe_bonnie_home_sitting2 = "/bonnie/[bonnie.stage]/sitting2.webp"
        scene cafe_bonnie_home_sitting2
        bonnie "Sue has almost made it to the final, it was a bit touch and go though."
        pc "Nah, we knew she would always make it. Although I still think John’s was the best show stopper last week."
        bonnie "It looked so good! I wish I could have tasted it."
        image cafe_bonnie_home_eating2 = "/bonnie/[bonnie.stage]/eating2.webp"
        scene cafe_bonnie_home_eating2
        "Over the next hour you watch the contestants sweat it out as they try to make a showstopping chocolate treat for the judges."
        "Enthralled by the contest, Bonnie manages to demolish the entire batch of chocolates you have given to her in no time at all."
        image cafe_bonnie_home_stuffed1 = "/bonnie/[bonnie.stage]/stuffed1.webp"
        scene cafe_bonnie_home_stuffed1
        "The bulge in her stomach still growing week after week, the overindulgence on fattening treats really having an impact now."
        image cafe_bonnie_home_stuffed2 = "/bonnie/[bonnie.stage]/stuffed2.webp"
        scene cafe_bonnie_home_stuffed2
        "As the completed chocolate deserts are taken to the judges, you let yourself fantasise about what it would be like to feed those masses of sugar, butter and chocolate to Bonnie."
        image cafe_bonnie_home_sitting3 = "/bonnie/[bonnie.stage]/sitting3.webp"
        scene cafe_bonnie_home_sitting3
        bonnie "That was so good, I hope you enjoyed it."
        pc "I did, although I still think you could beat them all."
        image cafe_bonnie_home_sitting4 = "/bonnie/[bonnie.stage]/sitting4.webp"
        scene cafe_bonnie_home_sitting4
        bonnie "No way, although your chocolates might."
        bonnie "We should totally enter next year. Between us we would be unstoppable!"
        pc "Only if I can have you as chief taster!"
        bonnie "Like you even have to ask?"
    elif bonnie.stage == 6:
        image cafe_bonnie_home_sitting1_alt = "/bonnie/[bonnie.stage]/sitting1_alt.webp"
        scene cafe_bonnie_home_sitting1_alt
        "Walking over with the new  chocolates in hand you join Bonnie on the couch, laying them down next to her."
        image bonnie_stage6_newbox = "/bonnie/events/stage6/newbox.webp"
        scene bonnie_stage6_newbox
        bonnie "Are these the new ones?"
        image cafe_bonnie_home_eating1_alt = "/bonnie/[bonnie.stage]/eating1_alt.webp"
        scene cafe_bonnie_home_eating1_alt
        "Watching her take a bite you see the familiar look in her eyes."
        bonnie "These new chocolates are just amazing."
        image cafe_bonnie_home_sitting2_alt = "/bonnie/[bonnie.stage]/sitting2_alt.webp"
        scene cafe_bonnie_home_sitting2_alt
        bonnie "There is no way you would loose if you took these on the Choc-off."
        pc "I think you might be a little biased."
        bonnie "Maybe a little…."
        image cafe_bonnie_home_eating2_alt = "/bonnie/[bonnie.stage]/eating2_alt.webp"
        scene cafe_bonnie_home_eating2_alt
        "Flicking through the channels you find the multi-stage semi final of the choc-off. The chocolate making contest that has taken the country by storm."
        "Over the next hour you watch the contestants sweat it out as they try to make a showstopping chocolate treat for the judges."
        image cafe_bonnie_home_stuffed1_alt = "/bonnie/[bonnie.stage]/stuffed1_alt.webp"
        scene cafe_bonnie_home_stuffed1_alt
        "Enthralled by the contest, Bonnie manages to demolish the entire batch of chocolates you have given to her in no time at all."
        image cafe_bonnie_home_stuffed2_alt = "/bonnie/[bonnie.stage]/stuffed2_alt.webp"
        scene cafe_bonnie_home_stuffed2_alt
        "The bulge in her stomach still growing week after week, the overindulgence on fattening treats really having an impact now."
        image cafe_bonnie_home_sitting3_alt = "/bonnie/[bonnie.stage]/sitting3_alt.webp"
        scene cafe_bonnie_home_sitting3_alt
        bonnie "That was so good."
        bonnie "I still think we should enter next season!"
        pc "Only if I can have you as chief taster!"
        image cafe_bonnie_home_sitting4_alt = "/bonnie/[bonnie.stage]/sitting4_alt.webp"
        scene cafe_bonnie_home_sitting4_alt
        bonnie "Like you even have to ask?"

    scene outside2
    stop music fadeout 1.0
    "Grabbing the last batch out of the fridge, you help Bonnie clear up and head home."
    "You hope her customers enjoy all the chocolates you made."

    $ bonnie.weight += 0.8
    return

label bonnie_home3:
    ##### Scene image – Bonnie next to counter in her apron and underwear ####
    image cafe_bonnie_home_showkitchen = "/bonnie/[bonnie.stage]/home_showkitchen.webp"
    scene cafe_bonnie_home_showkitchen
    play music "/music/bonnie.ogg" if_changed
    "Walking in you notice the same larger bags of ingredients that have become the new normal."
    bonnie "Hey, I'm glad you came."
    pc "Me too. Is everything ready?"
    bonnie "Sure is."
    if bonnie.stage == 8:
        bonnie "Plus, this week I picked up a label machine so I won't make the same mistake again."

    image cafe_bonnie_home_cooking1 = "/bonnie/[bonnie.stage]/cooking1.webp"
    scene cafe_bonnie_home_cooking1
    "Grabbing a mixing bowl you begin to prepare the chocolates."
    "As usual Bonnie is never far from you as you make your various chocolate mixtures."
    image cafe_bonnie_home_cooking2 = "/bonnie/[bonnie.stage]/cooking2.webp"
    scene cafe_bonnie_home_cooking2
    "Her eyes are watching you intently as you stir the sweet-smelling chocolate."
    "Despite having watched you do this for weeks, it seems she is still interested to watch you work your magic."

    image cafe_bonnie_home_eating3 = "/bonnie/[bonnie.stage]/eating3.webp"
    scene cafe_bonnie_home_eating3
    pc "Here, the first ones are ready if you want to taste them."
    "Bonnie quickly takes the chocolate from you, chewing slowly to savour the flavour."
    bonnie "As good as ever."
    pc "I’ll make a batch of the new ones for you now if you would like?"
    bonnie "Yes, please!"

    image cafe_bonnie_home_cooking3 = "/bonnie/[bonnie.stage]/cooking3.webp"
    scene cafe_bonnie_home_cooking3
    "You would usually have waited until the end of the night but it seems Bonnie has been getting eager to try these again."
    "Adapting the recipe you knock up a batch of the new ones for Bonnie in no time."
    "You can see her waiting impatiently next to the fridge for the timer to go off."
    "Eventually the timer goes off and she wastes no time in pulling out the tray."
    "Walking back over to you she continues to watch, now popping chocolates into her mouth from time to time."

    if bonnie.stage == 8:
        pc "Do you think we should start selling them in the shop?"
        bonnie "I don’t know, I don't want to upset the customers."
        pc "They all seemed to love them."
        bonnie "Maybe, I’ll think about it."

    image cafe_bonnie_home_eating4 = "/bonnie/[bonnie.stage]/eating4.webp"
    scene cafe_bonnie_home_eating4
    "Starting on the next batches you continue to hand her tasters throughout the evening, despite Bonnie already having her own."
    "With enough made for the shop for the week, but Bonnie's tray running empty, you make an additional batch of the new chocolates."
    image cafe_bonnie_home_finishedcooking = "/bonnie/[bonnie.stage]/finishedcooking.webp"
    scene cafe_bonnie_home_finishedcooking
    bonnie "I think that should do."
    $ money += 10
    "You earned ten dollars."
    bonnie "Why don't you join me on the couch?"
    image cafe_bonnie_home_sitting1 = "/bonnie/[bonnie.stage]/sitting1.webp"
    scene cafe_bonnie_home_sitting1
    bonnie "It's a shame Choc-off ended, I really enjoyed that show."
    bonnie "Seeing all those delicious chocolates and cakes always made me hungry myself."
    if bonniestory <= 2 and bonnie.stage >= 7:
        menu:
            "Ask Bonnie about her past.":
                "You decide to ask Bonnie about her past."
                bonnie "Sure, I would love to talk about myself."
                bonnie "Always good to know you care about me."
                "Bonnie talks a bit about herself."
                $ bonniestory += 1
                #Unlocks more Bonnie story in the stats page.
                $ renpy.notify("New Bonnie story unlocked in the stats screen.")
                window hide
                pause
            "Nevermind.":
                "You decide not to ask Bonnie anything."
    image cafe_bonnie_home_sitting2 = "/bonnie/[bonnie.stage]/sitting2.webp"
    scene cafe_bonnie_home_sitting2
    bonnie "On that note, could you pass me those delicious chocolates you made?"
    pc "Here you go."
    image cafe_bonnie_home_eating1 = "/bonnie/[bonnie.stage]/eating1.webp"
    scene cafe_bonnie_home_eating1
    "Bonnie starts eating the chocolates you made for her."
    bonnie "These taste great, like always."
    image cafe_bonnie_home_sitting3 = "/bonnie/[bonnie.stage]/sitting3.webp"
    scene cafe_bonnie_home_sitting3
    "The following moments are spend talking about various topics relating to food."
    image cafe_bonnie_home_eating2 = "/bonnie/[bonnie.stage]/eating2.webp"
    scene cafe_bonnie_home_eating2
    "While talking, Bonnie doesn't spend much time without her mouth full of chocolates."
    image cafe_bonnie_home_sitting4 = "/bonnie/[bonnie.stage]/sitting4.webp"
    scene cafe_bonnie_home_sitting4
    bonnie "And that's why I think chocolates are better than pizza."
    pc "But what about chocolate pizza?"
    bonnie "That is quite an interesting idea. We should try that sometime."
    bonnie "What would you like to do now?"
    menu:
        "Let's have sex together.":
            bonnie "I hoped you would say that. I can't stop thinking about sex with you lately."
            call bonnie_sex from _call_bonnie_sex_3
            $ bonnie.weight += 0.5
        "I think we should fill your belly to the brim with chocolates." if bonnie.stage >= 8:
            image cafe_bonnie_home_sitting1 = "/bonnie/[bonnie.stage]/sitting1.webp"
            scene cafe_bonnie_home_sitting1
            bonnie "I will show you how many chocolates I can fit into this growing belly."
            image cafe_bonnie_home_eating1 = "/bonnie/[bonnie.stage]/eating1.webp"
            scene cafe_bonnie_home_eating1
            "Bonnie starts to eat her chocolates at a faster pace than before."
            image cafe_bonnie_home_eating2 = "/bonnie/[bonnie.stage]/eating2.webp"
            scene cafe_bonnie_home_eating2
            "You can't help but watch how Bonnie devours entire boxes of chocolates."
            image cafe_bonnie_home_stuffed1 = "/bonnie/[bonnie.stage]/stuffed1.webp"
            scene cafe_bonnie_home_stuffed1
            "You wonder how many more chocolates her belly can hold."
            image cafe_bonnie_home_stuffed2 = "/bonnie/[bonnie.stage]/stuffed2.webp"
            scene cafe_bonnie_home_stuffed2
            "Her belly seemingly growing in real time."
            bonnie "Let's move over to the kitchen."
            $ stuffed = 0
            call rngeatingbonniehome from _call_rngeatingbonniehome_4
            show screen bonniefullness
            call bonnie_home_feeding from _call_bonnie_home_feeding
            pause
            $ bonnie.weight += (bonnie.fullness / 2)
            $ bonnie.fullness = 0
            hide screen bonniefullness
            pause
            if stuffed == 0:
                call bonnie_sex from _call_bonnie_sex_4
                $ bonnie.weight += 0.5
            else:
                image cafe_bonnie_home_feeding_end = "/bonnie/[bonnie.stage]/feeding_end_[stuffed].webp"
                scene cafe_bonnie_home_feeding_end
                "Bonnie proudly looks and rubs her round belly."
                bonnie "Look at this beautiful belly of mine, so nice and full."


    ####Scene image – outside walking home###
    scene outside2
    stop music fadeout 1.0
    $ bellyrub = 0
    $ stuffed = 0
    "After helping Bonnie clean up you head home."
    return

label bonnie_home4:
    ##### Scene image – Bonnie next to counter in her apron and underwear ####
    image cafe_bonnie_home_showkitchen = "/bonnie/[bonnie.stage]/home_showkitchen.webp"
    scene cafe_bonnie_home_showkitchen
    play music "/music/bonnie.ogg" if_changed
    "Walking in you notice the same larger bags of ingredients that have become the new normal."
    bonnie "Hey, I'm glad you came."
    pc "Me too. Is everything ready?"
    bonnie "Sure is."

    image cafe_bonnie_home_cooking1 = "/bonnie/[bonnie.stage]/cooking1.webp"
    scene cafe_bonnie_home_cooking1
    "Grabbing a mixing bowl you begin to prepare the chocolates."
    "As usual Bonnie is never far from you as you make your various chocolate mixtures."
    image cafe_bonnie_home_cooking2 = "/bonnie/[bonnie.stage]/cooking2.webp"
    scene cafe_bonnie_home_cooking2
    if bonnie.stage >= 12:
        "Bonnie takes off her bra to show you her fat round breasts."
        bonnie "Here you have something nice to look at while making chocolates for me."
    "Her eyes are watching you intently as you stir the sweet-smelling chocolate."
    "Despite having watched you do this for weeks, it seems she is still interested to watch you work your magic."

    if bonnie_ask_bigger == 1:
        image cafe_bonnie_home_talk1 = "/bonnie/[bonnie.stage]/talk1.webp"
        scene cafe_bonnie_home_talk1
        "Bonnie looks like she wants to ask you something."
        bonnie "Hey [playername], can I ask you something?"
        pc "You can always ask me anything."
        $ bonnie_ask_bigger = 0
        image cafe_bonnie_home_talk2 = "/bonnie/[bonnie.stage]/talk2.webp"
        scene cafe_bonnie_home_talk2
        bonnie "I know you like bigger girls, and I have no issue being larger."
        bonnie "To be honest I actually really like becoming fatter."
        image cafe_bonnie_home_talk3 = "/bonnie/[bonnie.stage]/talk3.webp"
        scene cafe_bonnie_home_talk3
        bonnie "I always felt limited in my ability to enjoy myself because I wanted to stay thin."
        bonnie "But now I can enjoy life to the fullest, and look at me, I look better than ever."
        bonnie "I really enjoy seeing my breasts and belly progressively grow bigger, getting softer every single day."
        image cafe_bonnie_home_talk5 = "/bonnie/[bonnie.stage]/talk5.webp"
        scene cafe_bonnie_home_talk5
        bonnie "And then look at this huge butt I am rocking nowadays."
        window hide
        pause
        bonnie "I always had a large ass, but recently it seems like it grew at least twice as big."
        image cafe_bonnie_home_talk4 = "/bonnie/[bonnie.stage]/talk4.webp"
        scene cafe_bonnie_home_talk4
        bonnie "But let me get to the point; we got something together and I want to know what you think."
        bonnie "Do you think I'm gaining too much weight? Or would you like me to get even bigger?"
        menu:
            "I think you would look even better if you were bigger.":
                image cafe_bonnie_home_talk3 = "/bonnie/[bonnie.stage]/talk3.webp"
                scene cafe_bonnie_home_talk3
                bonnie "I am so happy to hear you say that. I am not sure what I would do if you didn't like me bigger."
                bonnie "Staying away from these chocolates would be impossible."
                bonnie "I want nothing more than to be with you, while having my fat soft belly filled with delicious sweets."
                bonnie "On that note, do you have some chocolates I can start eating?"
            "I would prefer if you ate a little less.":
                image cafe_bonnie_home_talk1 = "/bonnie/[bonnie.stage]/talk1.webp"
                scene cafe_bonnie_home_talk1
                bonnie "I see. I guess I will have to stay away from the chocolates then."
                bonnie "From tomorrow onwards I will be dieting then."
                "This is not implemented yet. Bonnie's gain cannot be stopped until her next update."

    if bonnie.stage == 10:
        image cafe_bonnie_home_eating3 = "/bonnie/[bonnie.stage]/eating3.webp"
        scene cafe_bonnie_home_eating3
        pc "Here, I made some of the deluxe chocolates first so you don't have to watch on an empty stomach."
        "Bonnie quickly takes the chocolate from you, chewing slowly to savour the flavour."
        bonnie "These are amazing."
        bonnie "I have been thinking about what you said."
        bonnie "I'm still a little reluctant to start selling them, but I think you are right."
        bonnie "I might do another promotion here in the shop so I can tell if people like them or not."
        pc "Trust me, people like them."

    if bonnie.stage == 11:
        image cafe_bonnie_home_eating3 = "/bonnie/[bonnie.stage]/eating3.webp"
        scene cafe_bonnie_home_eating3
        pc "Here, I made some of the deluxe chocolates first so you don't have to watch on an empty stomach."
        "Bonnie quickly takes the chocolate from you, chewing slowly to savour the flavour."
        bonnie "These are amazing. I could eat an entire shops worth of just these."
        pc "Well, since we're now partners, they are not going anywhere."
        bonnie "Well, that's another great thing about us making it official."
        bonnie "You can't escape with these delicious treats."

    if bonnie.stage == 9:
        image cafe_bonnie_home_eating3 = "/bonnie/[bonnie.stage]/eating3.webp"
        scene cafe_bonnie_home_eating3
        pc "Here, the first ones are ready if you want to taste them."
        "Bonnie quickly takes the chocolate from you, chewing slowly to savour the flavour."
        bonnie "As good as ever."
        pc "I’ll make a batch of the new ones for you now if you would like?"
        bonnie "Yes, please!"

    if bonnie.stage >= 12:
        image cafe_bonnie_home_cooking3 = "/bonnie/[bonnie.stage]/cooking3.webp"
        scene cafe_bonnie_home_cooking3
        "You would usually have waited until the end of the night but it seems Bonnie has been getting eager to try these again."
        "Adapting the recipe you knock up a batch of the new ones for Bonnie in no time."
        "You can see her waiting impatiently next to the fridge for the timer to go off."
        "You grab some more ingredients from the other side of the kitchen, but when you turn around Bonnie is standing there."
        image cafe_bonnie_home_boobshake = "/bonnie/[bonnie.stage]/boobshake.webp"
        scene cafe_bonnie_home_boobshake
        bonnie "Do you like my breasts?"
        pc "I love them, just like the rest of your growing body."
        if bonnie.stage == 12:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/12/boobshake_shake.webm" loop
        elif bonnie.stage == 13:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/13/boobshake_shake.webm" loop
        show movie with dissolve
        window hide
        pause
        "Happy to hear your answer, Bonnie decides to give you a little show by shaking her lovely breasts from left to right."
        stop movie
        image cafe_bonnie_home_boobshake2 = "/bonnie/[bonnie.stage]/boobshake2.webp"
        scene cafe_bonnie_home_boobshake2
        bonnie "You love to see these fat boobs jiggle, don't you?"
        pc "For sure, I can't keep my eyes off them."
        if bonnie.stage == 12:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/12/boobshake2_shake.webm" loop
        elif bonnie.stage == 13:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/13/boobshake2_shake.webm" loop
        show movie with dissolve
        window hide
        pause
        "Eager to please, she jumps up and down to show off her big bounching breasts."
        stop movie
        image cafe_bonnie_home_cooking3 = "/bonnie/[bonnie.stage]/cooking3.webp"
        scene cafe_bonnie_home_cooking3
        "Eventually the timer goes off and she wastes no time in pulling out the tray."
        "Walking back over to you she continues to watch, now popping chocolates into her mouth from time to time."

        image cafe_bonnie_home_eating4 = "/bonnie/[bonnie.stage]/eating4.webp"
        scene cafe_bonnie_home_eating4
        "Starting on the next batches you continue to hand her tasters throughout the evening, despite Bonnie already having her own."
        "With enough made for the shop for the week, but Bonnie's tray running empty, you make an additional batch of the new chocolates."
        image cafe_bonnie_home_finishedcooking = "/bonnie/[bonnie.stage]/finishedcooking.webp"
        scene cafe_bonnie_home_finishedcooking
        bonnie "I think that should do."
        $ money += 10
        "You earned ten dollars."
        bonnie "Why don't you join me on the couch?"
        image cafe_bonnie_home_sitting1 = "/bonnie/[bonnie.stage]/sitting1.webp"
        scene cafe_bonnie_home_sitting1
        bonnie "It's a shame Choc-off ended, I really enjoyed that show."
        bonnie "Seeing all those delicious chocolates and cakes always made me hungry myself."
        if bonniestory <= 5:
            menu:
                "Ask Bonnie about her past.":
                    "You decide to ask Bonnie about her past."
                    bonnie "Sure, I would love to talk about myself."
                    bonnie "Always good to know you care about me."
                    "Bonnie talks a bit about herself."
                    $ bonniestory += 1
                    #Unlocks more Bonnie story in the stats page.
                    $ renpy.notify("New Bonnie story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Bonnie anything."
        image cafe_bonnie_home_sitting2 = "/bonnie/[bonnie.stage]/sitting2.webp"
        scene cafe_bonnie_home_sitting2
        bonnie "On that note, could you pass me those delicious chocolates you made?"
        pc "Here you go."
        image cafe_bonnie_home_eating1 = "/bonnie/[bonnie.stage]/eating1.webp"
        scene cafe_bonnie_home_eating1
        "Bonnie starts eating the chocolates you made for her."
        bonnie "These taste great, like always."
        image cafe_bonnie_home_sitting3 = "/bonnie/[bonnie.stage]/sitting3.webp"
        scene cafe_bonnie_home_sitting3
        "The following moments are spend talking about various topics relating to food."
        image cafe_bonnie_home_eating2 = "/bonnie/[bonnie.stage]/eating2.webp"
        scene cafe_bonnie_home_eating2
        "While talking, Bonnie doesn't spend much time without her mouth full of chocolates."
        image cafe_bonnie_home_sitting4 = "/bonnie/[bonnie.stage]/sitting4.webp"
        scene cafe_bonnie_home_sitting4
        bonnie "And that's why I think chocolates are better than pizza."
        pc "But what about chocolate pizza?"
        bonnie "That is quite an interesting idea. We should try that sometime."
        bonnie "What would you like to do now?"
        menu:
            "Let's have sex together.":
                bonnie "I hoped you would say that. I can't stop thinking about sex with you lately."
                call bonnie_sex from _call_bonnie_sex_6
                scene outside2
                stop music fadeout 1.0
                "After helping Bonnie clean up and ready the store for the next week, you head home."
                $ stuffed = 0
                $ bonnie.weight += 0.8
                return
            "I think we should fill your belly to the brim with chocolates.":
                image cafe_bonnie_home_sitting1 = "/bonnie/[bonnie.stage]/sitting1.webp"
                scene cafe_bonnie_home_sitting1
                bonnie "I will show you how many chocolates I can fit into this growing belly."
                bonnie "Let's move over to the kitchen."
                $ stuffed = 0
                call rngeatingbonniehome from _call_rngeatingbonniehome_6
                show screen bonniefullness
                call bonnie_home_feeding from _call_bonnie_home_feeding_2
                pause
                $ bonnie.weight += (bonnie.fullness / 2)
                $ bonnie.fullness = 0
                hide screen bonniefullness
                pause
                if stuffed == 0:
                    call bonnie_sex from _call_bonnie_sex_7
                    scene outside2
                    stop music fadeout 1.0
                    "After helping Bonnie clean up and ready the store for the next week, you head home."
                    $ stuffed = 0
                    $ bellyrub = 0
                    $ bonnie.weight += 0.5
                    if rebeccastage3event == 1 and rebeccastage2event == 0:
                        call Rebecca_Stage_3_Event
                    return
                else:
                    image cafe_bonnie_home_feeding_end = "/bonnie/[bonnie.stage]/feeding_end_[stuffed].webp"
                    scene cafe_bonnie_home_feeding_end
                    "Bonnie proudly looks and rubs her round belly."
                    bonnie "Look at this beautiful belly of mine, so nice and full."
                    scene outside2
                    stop music fadeout 1.0
                    "After helping Bonnie clean up and ready the store for the next week, you head home."
                    $ stuffed = 0
                    $ bellyrub = 0
                    if rebeccastage3event == 1 and rebeccastage2event == 0:
                        call Rebecca_Stage_3_Event
                    return


    #TITS or NO TITS
    if bonnietits == 2:
        $ bonnietits = 1
        image cafe_bonnie_home_cooking2_tits = "/bonnie/[bonnie.stage]/cooking2_tits.webp"
        scene cafe_bonnie_home_cooking2_tits
        "Bonnie takes off her bra to show you her fat round breasts."
        bonnie "Here you have something nice to look at while making chocolates for me."
        image cafe_bonnie_home_cooking3_tits = "/bonnie/[bonnie.stage]/cooking3_tits.webp"
        scene cafe_bonnie_home_cooking3_tits
        "You would usually have waited until the end of the night but it seems Bonnie has been getting eager to try these again."
        "Adapting the recipe you knock up a batch of the new ones for Bonnie in no time."
        "You can see her waiting impatiently next to the fridge for the timer to go off."
        "You grab some more ingredients from the other side of the kitchen, but when you turn around Bonnie is standing there."
        image cafe_bonnie_home_boobshake = "/bonnie/[bonnie.stage]/boobshake.webp"
        scene cafe_bonnie_home_boobshake
        bonnie "Do you like my breasts?"
        pc "I love them, just like the rest of your growing body."
        if bonnie.stage == 9:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/9/boobshake_shake.webm" loop
            show movie with dissolve
            window hide
            pause
        elif bonnie.stage == 10:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/10/boobshake_shake.webm" loop
            show movie with dissolve
            window hide
            pause
        elif bonnie.stage == 11:
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/11/boobshake_shake.webm" loop
            show movie with dissolve
            window hide
            pause
        "Happy to hear your answer, Bonnie decides to give you a little show by shaking her lovely breasts from left to right."
        stop movie
        image cafe_bonnie_home_cooking3_tits = "/bonnie/[bonnie.stage]/cooking3_tits.webp"
        scene cafe_bonnie_home_cooking3_tits
        "Eventually the timer goes off and she wastes no time in pulling out the tray."
        "Walking back over to you she continues to watch, now popping chocolates into her mouth from time to time."

        if bonnie.stage == 9:
            pc "Do you think we should start selling them in the shop?"
            bonnie "I don’t know, I don't want to upset the customers."
            pc "They all seemed to love them."
            bonnie "Maybe, I’ll think about it."

        image cafe_bonnie_home_eating4_tits = "/bonnie/[bonnie.stage]/eating4_tits.webp"
        scene cafe_bonnie_home_eating4_tits
        "Starting on the next batches you continue to hand her tasters throughout the evening, despite Bonnie already having her own."
        "With enough made for the shop for the week, but Bonnie's tray running empty, you make an additional batch of the new chocolates."
        image cafe_bonnie_home_finishedcooking_tits = "/bonnie/[bonnie.stage]/finishedcooking_tits.webp"
        scene cafe_bonnie_home_finishedcooking_tits
        bonnie "I think that should do."
        $ money += 10
        "You earned ten dollars."
        bonnie "Why don't you join me on the couch?"
        image cafe_bonnie_home_sitting1_tits = "/bonnie/[bonnie.stage]/sitting1_tits.webp"
        scene cafe_bonnie_home_sitting1_tits
        bonnie "It's a shame Choc-off ended, I really enjoyed that show."
        bonnie "Seeing all those delicious chocolates and cakes always made me hungry myself."
        if bonniestory <= 4 and bonnie.stage >= 10:
            menu:
                "Ask Bonnie about her past.":
                    "You decide to ask Bonnie about her past."
                    bonnie "Sure, I would love to talk about myself."
                    bonnie "Always good to know you care about me."
                    "Bonnie talks a bit about herself."
                    $ bonniestory += 1
                    #Unlocks more Bonnie story in the stats page.
                    $ renpy.notify("New Bonnie story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Bonnie anything."
        elif bonniestory <= 3:
            menu:
                "Ask Bonnie about her past.":
                    "You decide to ask Bonnie about her past."
                    bonnie "Sure, I would love to talk about myself."
                    bonnie "Always good to know you care about me."
                    "Bonnie talks a bit about herself."
                    $ bonniestory += 1
                    #Unlocks more Bonnie story in the stats page.
                    $ renpy.notify("New Bonnie story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Bonnie anything."
        image cafe_bonnie_home_sitting2_tits = "/bonnie/[bonnie.stage]/sitting2_tits.webp"
        scene cafe_bonnie_home_sitting2_tits
        bonnie "On that note, could you pass me those delicious chocolates you made?"
        pc "Here you go."
        image cafe_bonnie_home_eating1_tits = "/bonnie/[bonnie.stage]/eating1_tits.webp"
        scene cafe_bonnie_home_eating1_tits
        "Bonnie starts eating the chocolates you made for her."
        bonnie "These taste great, like always."
        image cafe_bonnie_home_sitting3_tits = "/bonnie/[bonnie.stage]/sitting3_tits.webp"
        scene cafe_bonnie_home_sitting3_tits
        "The following moments are spend talking about various topics relating to food."
        image cafe_bonnie_home_eating2_tits = "/bonnie/[bonnie.stage]/eating2_tits.webp"
        scene cafe_bonnie_home_eating2_tits
        "While talking, Bonnie doesn't spend much time without her mouth full of chocolates."
        image cafe_bonnie_home_sitting4_tits = "/bonnie/[bonnie.stage]/sitting4_tits.webp"
        scene cafe_bonnie_home_sitting4_tits
        bonnie "And that's why I think chocolates are better than pizza."
        pc "But what about chocolate pizza?"
        bonnie "That is quite an interesting idea. We should try that sometime."
        bonnie "What would you like to do now?"
        menu:
            "Let's have sex together.":
                bonnie "I hoped you would say that. I can't stop thinking about sex with you lately."
                call bonnie_sex from _call_bonnie_sex
            "I think we should fill your belly to the brim with chocolates.":
                image cafe_bonnie_home_sitting1_tits = "/bonnie/[bonnie.stage]/sitting1_tits.webp"
                scene cafe_bonnie_home_sitting1_tits
                bonnie "I will show you how many chocolates I can fit into this growing belly."
                image cafe_bonnie_home_eating1_tits = "/bonnie/[bonnie.stage]/eating1_tits.webp"
                scene cafe_bonnie_home_eating1_tits
                "Bonnie starts to eat her chocolates at a faster pace than before."
                image cafe_bonnie_home_eating2_tits = "/bonnie/[bonnie.stage]/eating2_tits.webp"
                scene cafe_bonnie_home_eating2_tits
                "You can't help but watch how Bonnie devours entire boxes of chocolates."
                image cafe_bonnie_home_stuffed1_tits = "/bonnie/[bonnie.stage]/stuffed1_tits.webp"
                scene cafe_bonnie_home_stuffed1_tits
                "You wonder how many more chocolates her belly can hold."
                image cafe_bonnie_home_stuffed2_tits = "/bonnie/[bonnie.stage]/stuffed2_tits.webp"
                scene cafe_bonnie_home_stuffed2_tits
                "Her belly seemingly growing in real time."
                if bonnie.stage == 11:
                    image cafe_bonnie_home_stuffed2_alt = "/bonnie/[bonnie.stage]/stuffed2_alt.webp"
                    scene cafe_bonnie_home_stuffed2_alt
                    window hide
                    pause
                $ bonnie.weight += 0.2
                bonnie "Normally I would continue eating until I am completely stuffed, but today I need you to help me take care of my other urges."
                call bonnie_sex from _call_bonnie_sex_1



    elif bonnietits == 1:
        $ bonnietits = 2
        image cafe_bonnie_home_cooking2 = "/bonnie/[bonnie.stage]/cooking2.webp"
        scene cafe_bonnie_home_cooking2
        "You would usually have waited until the end of the night but it seems Bonnie has been getting eager to try these again."
        "Adapting the recipe you knock up a batch of the new ones for Bonnie in no time."
        image cafe_bonnie_home_cooking3 = "/bonnie/[bonnie.stage]/cooking3.webp"
        scene cafe_bonnie_home_cooking3
        "You can see her waiting impatiently next to the fridge for the timer to go off."
        "Eventually the timer goes off and she wastes no time in pulling out the tray."
        "Walking back over to you she continues to watch, now popping chocolates into her mouth from time to time."

        if bonnie.stage == 9:
            pc "Do you think we should start selling them in the shop?"
            bonnie "I don’t know, I don't want to upset the customers"
            pc "They all seemed to love them."
            bonnie "Maybe, I’ll think about it."

        image cafe_bonnie_home_eating4 = "/bonnie/[bonnie.stage]/eating4.webp"
        scene cafe_bonnie_home_eating4
        "Starting on the next batches you continue to hand her tasters throughout the evening, despite Bonnie already having her own."
        "With enough made for the shop for the week, but Bonnie's tray running empty, you make an additional batch of the new chocolates."
        image cafe_bonnie_home_finishedcooking = "/bonnie/[bonnie.stage]/finishedcooking.webp"
        scene cafe_bonnie_home_finishedcooking
        bonnie "I think that should do."
        $ money += 10
        "You earned ten dollars."
        bonnie "Why don't you join me on the couch?"
        image cafe_bonnie_home_sitting1 = "/bonnie/[bonnie.stage]/sitting1.webp"
        scene cafe_bonnie_home_sitting1
        bonnie "It's a shame Choc-off ended, I really enjoyed that show."
        bonnie "Seeing all those delicious chocolates and cakes always made me hungry myself."
        if bonniestory <= 4 and bonnie.stage >= 10:
            menu:
                "Ask Bonnie about her past.":
                    "You decide to ask Bonnie about her past."
                    bonnie "Sure, I would love to talk about myself."
                    bonnie "Always good to know you care about me."
                    "Bonnie talks a bit about herself."
                    $ bonniestory += 1
                    #Unlocks more Bonnie story in the stats page.
                    $ renpy.notify("New Bonnie story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Bonnie anything."
        elif bonniestory <= 3:
            menu:
                "Ask Bonnie about her past.":
                    "You decide to ask Bonnie about her past."
                    bonnie "Sure, I would love to talk about myself."
                    bonnie "Always good to know you care about me."
                    "Bonnie talks a bit about herself."
                    $ bonniestory += 1
                    #Unlocks more Bonnie story in the stats page.
                    $ renpy.notify("New Bonnie story unlocked in the stats screen.")
                    window hide
                    pause
                "Nevermind.":
                    "You decide not to ask Bonnie anything."
        image cafe_bonnie_home_sitting2 = "/bonnie/[bonnie.stage]/sitting2.webp"
        scene cafe_bonnie_home_sitting2
        bonnie "On that note, could you pass me those delicious chocolates you made?"
        pc "Here you go."
        image cafe_bonnie_home_eating1 = "/bonnie/[bonnie.stage]/eating1.webp"
        scene cafe_bonnie_home_eating1
        "Bonnie starts eating the chocolates you made for her."
        bonnie "These taste great, like always."
        image cafe_bonnie_home_sitting3 = "/bonnie/[bonnie.stage]/sitting3.webp"
        scene cafe_bonnie_home_sitting3
        "The following moments are spend talking about various topics relating to food."
        image cafe_bonnie_home_eating2 = "/bonnie/[bonnie.stage]/eating2.webp"
        scene cafe_bonnie_home_eating2
        "While talking, Bonnie doesn't spend much time without her mouth full of chocolates."
        image cafe_bonnie_home_sitting4 = "/bonnie/[bonnie.stage]/sitting4.webp"
        scene cafe_bonnie_home_sitting4
        bonnie "And that's why I think chocolates are better than pizza."
        pc "But what about chocolate pizza?"
        bonnie "That is quite an interesting idea. We should try that sometime."
        bonnie "What would you like to do now?"
        menu:
            "Let's have sex together.":
                bonnie "I hoped you would say that. I can't stop thinking about sex with you lately."
                call bonnie_sex from _call_bonnie_sex_2
                $ bonnie.weight += 0.5
            "I think we should fill your belly to the brim with chocolates.":
                image cafe_bonnie_home_sitting1 = "/bonnie/[bonnie.stage]/sitting1.webp"
                scene cafe_bonnie_home_sitting1
                bonnie "I will show you how many chocolates I can fit into this growing belly."
                image cafe_bonnie_home_eating1 = "/bonnie/[bonnie.stage]/eating1.webp"
                scene cafe_bonnie_home_eating1
                "Bonnie starts to eat her chocolates at a faster pace than before."
                image cafe_bonnie_home_eating2 = "/bonnie/[bonnie.stage]/eating2.webp"
                scene cafe_bonnie_home_eating2
                "You can't help but watch how Bonnie devours entire boxes of chocolates."
                image cafe_bonnie_home_stuffed1 = "/bonnie/[bonnie.stage]/stuffed1.webp"
                scene cafe_bonnie_home_stuffed1
                "You wonder how many more chocolates her belly can hold."
                image cafe_bonnie_home_stuffed2 = "/bonnie/[bonnie.stage]/stuffed2.webp"
                scene cafe_bonnie_home_stuffed2
                "Her belly seemingly growing in real time."
                bonnie "Let's move over to the kitchen."
                $ stuffed = 0
                call rngeatingbonniehome from _call_rngeatingbonniehome_5
                show screen bonniefullness
                call bonnie_home_feeding from _call_bonnie_home_feeding_1
                pause
                $ bonnie.weight += (bonnie.fullness / 2)
                $ bonnie.fullness = 0
                hide screen bonniefullness
                pause
                if stuffed == 0:
                    call bonnie_sex from _call_bonnie_sex_5
                    $ bonnie.weight += 0.5
                else:
                    image cafe_bonnie_home_feeding_end = "/bonnie/[bonnie.stage]/feeding_end_[stuffed].webp"
                    scene cafe_bonnie_home_feeding_end
                    "Bonnie proudly looks and rubs her round belly."
                    bonnie "Look at this beautiful belly of mine, so nice and full."

    scene outside2
    stop music fadeout 1.0
    if bonnie.stage <= 10:
        "After helping Bonnie clean up you head home."
    if bonnie.stage >= 11:
        "After helping Bonnie clean up and ready the store for the next week, you head home."
    $ stuffed = 0
    $ bellyrub = 0
    return

label bonnie_sex:
    #play music "/music/bonnie_sex.ogg" if_changed fadein 1.0
    if persistent.nosexscene == True:
        scene black with dissolve
        "Bonnie and i had a great time together."
        return
    if bonnie.stage >= 13:
        image cafe_bonnie_home_undress = "/bonnie/[bonnie.stage]/undress.webp"
        scene cafe_bonnie_home_undress
        "Bonnie stands up and takes off her underwear."
        window hide
        pause
        image cafe_bonnie_home_tease1 = "/bonnie/[bonnie.stage]/tease1.webp"
        scene cafe_bonnie_home_tease1
        "It is clear what Bonnie wants."
        window hide
        pause
        image cafe_bonnie_home_pussyview = "/bonnie/[bonnie.stage]/pussyview.webp"
        scene cafe_bonnie_home_pussyview
        "Bonnie lifts up her fat belly to show you her soaking wet pussy."
        bonnie "You make me so wet, [playername]. Come fill me up."
        window hide
        pause
        image cafe_bonnie_home_tease3 = "/bonnie/[bonnie.stage]/tease3.webp"
        scene cafe_bonnie_home_tease3
        "Bonnie moves over to the side to lean forward on the counter."
        "With her big belly hanging there on full display, it is no wonder you had issues lifting her."
        bonnie "Come over here, big boy. Take me from behind."
        window hide
        pause
        image cafe_bonnie_home_buttshake = "/bonnie/[bonnie.stage]/buttshake.webp"
        scene cafe_bonnie_home_buttshake
        "Moving behind her, you get a good view of her big round ass waiting to be impaled once again."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/13/buttshake_shake.webm" loop
        show movie with dissolve
        pause
        "Before you get close enough to insert your rock solid cock, Bonnie starts to shake her soft ass from left to right, creating a mesmerizing view of her behind."
        stop movie
        image cafe_bonnie_home_beforesex = "/bonnie/[bonnie.stage]/beforesex.webp"
        scene cafe_bonnie_home_beforesex
        bonnie "What are you waiting for? Give me your meat."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/13/sex1.webm" loop
        show movie with dissolve
        window hide
        pause
        "Just as you enter her, she begins rocking her body back and forth."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/13/sex2.webm" loop
        show movie with dissolve
        window hide
        pause
        "With everything jiggling in front of you, it is a feast for your eyes."
        "All the food you bought her and helped create, all accumulated to this."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/13/sex3.webm" loop
        show movie with dissolve
        window hide
        pause
        "And you are not the only one enjoying the growing curves on Bonnie's soft body."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/13/sex4.webm" loop
        show movie with dissolve
        window hide
        pause
        "Her moans grow louder with each push and with each jiggle of her blubbery breasts."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/13/sex5.webm" loop
        show movie with dissolve
        window hide
        pause
        bonnie "Oh god, I'm coming."
        pc "Me too!"
        stop movie
        $ renpy.movie_cutscene("/images/bonnie/13/sex6.webm", stop_music=False)
        image cafe_bonnie_home_aftersex = "/bonnie/[bonnie.stage]/aftersex.webp"
        scene cafe_bonnie_home_aftersex
        "After pulling out, you blow your load all over Bonnie's ass and back."
        image cafe_bonnie_home_aftersex2 = "/bonnie/[bonnie.stage]/aftersex2.webp"
        scene cafe_bonnie_home_aftersex2
        pause
        image cafe_bonnie_home_aftersex3 = "/bonnie/[bonnie.stage]/aftersex3.webp"
        scene cafe_bonnie_home_aftersex3
        bonnie "That was some amazing sex, babe. You never disappoint."

        return

    elif bonnie.stage >= 12:
        image cafe_bonnie_home_undress = "/bonnie/[bonnie.stage]/undress.webp"
        scene cafe_bonnie_home_undress
        "Bonnie stands up and takes off her underwear."
        window hide
        pause
        image cafe_bonnie_home_tease1 = "/bonnie/[bonnie.stage]/tease1.webp"
        scene cafe_bonnie_home_tease1
        "It is clear what Bonnie wants."
        window hide
        pause
        image cafe_bonnie_home_pussyview = "/bonnie/[bonnie.stage]/pussyview.webp"
        scene cafe_bonnie_home_pussyview
        "Bonnie lifts up her fat belly to show you her soaking wet pussy."
        bonnie "You make me so wet, [playername]. Come fill me up."
        window hide
        pause
        image cafe_bonnie_home_beforesex = "/bonnie/[bonnie.stage]/beforesex.webp"
        scene cafe_bonnie_home_beforesex
        "You move up to her and lift up her legs to create the perfect view of her fat blubbery belly."
        "You take a moment to appriciate the sheer size of what her once flat stomach has become while you slide you dick into her."
        window hide
        pause
        bonnie "Fuck me [playername], I'm so ready for it."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/12/sex_top.webm" loop
        show movie with dissolve
        window hide
        pause
        "You start rocking you hips back an forth to push your cock into her."
        bonnie "That's it, I'm addicted to this feeling."
        pc "Just like you are addicted to growing this huge gut of yours."
        "With every push you make, you see her soft parts jiggle around with layers of fat cultivated since Bonnie let herself go."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/12/sex_side.webm" loop
        show movie with dissolve
        window hide
        pause
        "While steadily thrusting your hips back and forth, you feel your arms cramp up."
        "You seem to have clearly underestimated Bonnie's rapid growth, where you were able to handle her weight before to lift her up in exotic positions."
        "Your strength now seems to have reached a limit."
        pc "Let's move over to another position."
        stop movie
        image cafe_bonnie_home_tease3 = "/bonnie/[bonnie.stage]/tease3.webp"
        scene cafe_bonnie_home_tease3
        "Bonnie moves over to the side to lean forward on the counter."
        "With her big belly hanging there on full display, it is no wonder you had issues lifting her."
        bonnie "Come over here, big boy. Take me from behind."
        window hide
        pause
        image cafe_bonnie_home_buttshake = "/bonnie/[bonnie.stage]/buttshake.webp"
        scene cafe_bonnie_home_buttshake
        "Moving behind her, you get a good view of her big round ass waiting to be impaled once again."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/12/buttshake_shake.webm" loop
        show movie with dissolve
        pause
        "Before you get close enough to insert your rock solid cock, Bonnie starts to shake her soft ass from left to right, creating a mesmerizing view of her behind."
        stop movie
        image cafe_bonnie_home_beforesex2 = "/bonnie/[bonnie.stage]/beforesex2.webp"
        scene cafe_bonnie_home_beforesex2
        bonnie "What are you waiting for? Give me your meat."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/12/sex2_top.webm" loop
        show movie with dissolve
        window hide
        pause
        "Just as you enter her, she begins rocking her body back and forth."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/12/sex2_side.webm" loop
        show movie with dissolve
        window hide
        pause
        "With everything jiggling in front of you, it is a feast for your eyes."
        "All the food you bought her and helped create, all accumulated to this."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/12/sex2_front.webm" loop
        show movie with dissolve
        window hide
        pause
        "And you are not the only one enjoying the growing curves on Bonnie's soft body."
        "Her moans grow louder with each push and with each jiggle of her blubbery breasts."
        bonnie "Oh god, I'm coming."
        pc "Me too!"
        stop movie
        image cafe_bonnie_home_aftersex = "/bonnie/[bonnie.stage]/aftersex.webp"
        scene cafe_bonnie_home_aftersex
        "After pulling out, you blow your load all over Bonnie's ass and back."
        image cafe_bonnie_home_aftersex2 = "/bonnie/[bonnie.stage]/aftersex2.webp"
        scene cafe_bonnie_home_aftersex2
        bonnie "That was some amazing sex, babe. You never disappoint."

        return

    image cafe_bonnie_home_undress = "/bonnie/[bonnie.stage]/undress.webp"
    scene cafe_bonnie_home_undress
    "Bonnie stands up and takes off her underwear."
    window hide
    pause
    image cafe_bonnie_home_tease1 = "/bonnie/[bonnie.stage]/tease1.webp"
    scene cafe_bonnie_home_tease1
    "It is clear what Bonnie wants."
    window hide
    pause
    image cafe_bonnie_home_pussyview = "/bonnie/[bonnie.stage]/pussyview.webp"
    scene cafe_bonnie_home_pussyview
    "Bonnie lifts up her fat belly to show you her soaking wet pussy."
    bonnie "You make me so wet, [playername]. Come fill me up."
    window hide
    pause
    image cafe_bonnie_home_sex1 = "/bonnie/[bonnie.stage]/sex1.webp"
    scene cafe_bonnie_home_sex1
    "You take off you clothes and lie down on the couch, letting Bonnie take the lead."
    "She grabs your rock solid cock and inserts it in her hungry pussy, slowly lowering her hips until her fat ass is firmly planted down on your lap."
    window hide
    pause
    if bonnie.stage == 7:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/7/sex1_grind.webm" loop
        show movie with dissolve
        pause
        "Bonnie starts off by moving her large hips up and down, her motion triggering a series of jiggles all over her soft flabby body."
        menu:
            "Thrust":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/7/sex1_thrust.webm" loop
                show movie with dissolve
                pause
                "You decide to thrust your hips at a similar pace to hers. Her moans are now clearly audible with every thrust you make."
                stop movie
            "Change position":
                stop movie
                image cafe_bonnie_home_sex2 = "/bonnie/[bonnie.stage]/sex2.webp"
                scene cafe_bonnie_home_sex2
                pc "I know a better position."
                "Bonnie happily moves over, squatting down onto your rock solid dick."
                window hide
                pause
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/7/sex2_grind.webm" loop
                show movie with dissolve
                pause
                "Bonnie swings her heavy body up and down, making both of you loudly moan everytime she comes down on your hard cock."
                menu:
                    "Thrust.":
                        stop movie
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/bonnie/7/sex2_thrust.webm" loop
                        show movie with dissolve
                        pause
                        "Thrusting your cock into her drenched womanhood makes her body jiggle even harder."
                        "At some point it becomes clear that she can no longer handle the squatting position as she begins to collapse onto you."
                        bonnie "Let's go for another position. I am getting a bit too fat for this."
                        "Both of you get up, getting ready for another position."
                stop movie

        image cafe_bonnie_home_tease2 = "/bonnie/[bonnie.stage]/tease2.webp"
        scene cafe_bonnie_home_tease2
        "Bonnie rubs her vagina and then licks the same hand while giving you an enticing view of her ass and pussy."
        "You don't know what is happening, but it definitely turns you on."
        window hide
        pause
        image cafe_bonnie_home_sex3 = "/bonnie/[bonnie.stage]/sex3.webp"
        scene cafe_bonnie_home_sex3
        pc "Come over here, babe."
        "Bonnie comes over and lets you take her from behind."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/7/sex3_grind.webm" loop
        show movie with dissolve
        pause
        "While pushing her body against you she immediately starts grinding your private region."
        menu:
            "Thrust":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/7/sex3_thrust.webm" loop
                show movie with dissolve
                pause
                "You firmly thrust your rigid meat into Bonnie, creating loud moans in the process."
        if kamasutravol1 == 1:
            "You remember reading about a certain position in the Kama Sutra. You decide to try it out."
            pc "I want to try out something exotic I read about."
            bonnie "Let's do it. I will follow your lead."
            stop movie
            image cafe_bonnie_home_sex5 = "/bonnie/[bonnie.stage]/sex5.webp"
            scene cafe_bonnie_home_sex5
            "It takes a few tries, but for some reason you ended up with Bonnie upside down."
            "While the position itself might not be the most practical, it does leave you with a good view of her juicy pussy."
            window hide
            pause
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/7/sex5_thrust.webm" loop
            show movie with dissolve
            pause
            "You thrust your solid cock into her tasty-looking womanhood."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/7/sex5_alt.webm" loop
            show movie with dissolve
            window hide
            pause
            "Having such a good view of her pussy getting penetrated makes all the hassle worth it."
            "After a while it does get quite tiring to keep up this position so you decide to change it up again."
        stop movie
        image cafe_bonnie_home_tease3 = "/bonnie/[bonnie.stage]/tease3.webp"
        scene cafe_bonnie_home_tease3
        bonnie "Come over here, big boy. Take me from behind."
        window hide
        pause
        image cafe_bonnie_home_buttshake = "/bonnie/[bonnie.stage]/buttshake.webp"
        scene cafe_bonnie_home_buttshake
        "Moving behind her, you get a good view of her big round ass waiting to be impaled once again."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/7/buttshake_shake.webm" loop
        show movie with dissolve
        pause
        "Before you get close enough to insert your rock solid cock, Bonnie starts to shake her soft ass from left to right, creating a mesmerizing view of her behind."
        stop movie
        image cafe_bonnie_home_sex4 = "/bonnie/[bonnie.stage]/sex4.webp"
        scene cafe_bonnie_home_sex4
        bonnie "What are you waiting for? Give me your meat."
        "You happily oblige by shoving your erect cock in her soaking wet vagina."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/7/sex4_grind.webm" loop
        show movie with dissolve
        pause
        "Before you fully insert your dick into Bonnie, she begins to push her ass towards you."
        "Her sweaty fat body grinding against your waist captures you in a lusty trance."
        menu:
            "Thrust.":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/7/sex4_thrust.webm" loop
                show movie with dissolve
                window hide
                pause
                "While thrusting, you feel Bonnie reaching her limits, her moans become screams of pleasure while her body begins twitching."
                bonnie "AAAHHH, YES, YEESSS, AAAAAHH!"
                "Her climaxing, twitching body also brings you to your point of explosive relief."
        stop movie
        image cafe_bonnie_home_after_sex = "/bonnie/[bonnie.stage]/after_sex.webp"
        scene cafe_bonnie_home_after_sex
        window hide
        pause
        "After pulling out, you blow your load all over Bonnie's ass and back."
        bonnie "That was some amazing sex, babe. You never disappoint."
        return
    elif bonnie.stage == 8:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/8/sex1_grind.webm" loop
        show movie with dissolve
        pause
        "Bonnie starts off by moving her large hips up and down, her motion triggering a series of jiggles all over her soft flabby body."
        menu:
            "Thrust":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/8/sex1_thrust.webm" loop
                show movie with dissolve
                pause
                "You decide to thrust your hips at a similar pace to hers. Her moans are now clearly audible with every thrust you make."
                stop movie
            "Change position":
                stop movie
                image cafe_bonnie_home_sex2 = "/bonnie/[bonnie.stage]/sex2.webp"
                scene cafe_bonnie_home_sex2
                pc "I know a better position."
                "Bonnie happily moves over, squatting down onto your rock solid dick."
                window hide
                pause
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/8/sex2_grind.webm" loop
                show movie with dissolve
                pause
                "Bonnie swings her heavy body up and down, making both of you loudly moan everytime she comes down on your hard cock."
                menu:
                    "Thrust.":
                        stop movie
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/bonnie/8/sex2_thrust.webm" loop
                        show movie with dissolve
                        pause
                        "Thrusting your cock into her drenched womanhood makes her body jiggle even harder."
                        "At some point it becomes clear that she can no longer handle the squatting position as she begins to collapse onto you."
                        bonnie "Let's go for another position. I am getting a bit too fat for this."
                        "Both of you get up, getting ready for another position."
                stop movie

        image cafe_bonnie_home_tease2 = "/bonnie/[bonnie.stage]/tease2.webp"
        scene cafe_bonnie_home_tease2
        "Bonnie rubs her vagina and then licks the same hand while giving you an enticing view of her ass and pussy."
        "You don't know what is happening, but it definitely turns you on."
        window hide
        pause
        image cafe_bonnie_home_sex3 = "/bonnie/[bonnie.stage]/sex3.webp"
        scene cafe_bonnie_home_sex3
        pc "Come over here, babe."
        "Bonnie comes over and lets you take her from behind."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/8/sex3_grind.webm" loop
        show movie with dissolve
        pause
        "While pushing her body against you she immediately starts grinding your private region."
        menu:
            "Thrust":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/8/sex3_thrust.webm" loop
                show movie with dissolve
                pause
                "You firmly thrust your rigid meat into Bonnie, creating loud moans in the process."
        if kamasutravol1 == 1:
            "You remember reading about a certain position in the Kama Sutra. You decide to try it out."
            pc "I want to try out something exotic I read about."
            bonnie "Let's do it. I will follow your lead."
            stop movie
            image cafe_bonnie_home_sex5 = "/bonnie/[bonnie.stage]/sex5.webp"
            scene cafe_bonnie_home_sex5
            "It takes a few tries, but for some reason you ended up with Bonnie upside down."
            "While the position itself might not be the most practical, it does leave you with a good view of her juicy pussy."
            window hide
            pause
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/8/sex5_thrust.webm" loop
            show movie with dissolve
            pause
            "You thrust your solid cock into her tasty-looking womanhood."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/8/sex5_alt.webm" loop
            show movie with dissolve
            window hide
            pause
            "Having such a good view of her pussy getting penetrated makes all the hassle worth it."
            "After a while it does get quite tiring to keep up this position so you decide to change it up again."
        stop movie
        image cafe_bonnie_home_tease3 = "/bonnie/[bonnie.stage]/tease3.webp"
        scene cafe_bonnie_home_tease3
        bonnie "Come over here, big boy. Take me from behind."
        window hide
        pause
        image cafe_bonnie_home_buttshake = "/bonnie/[bonnie.stage]/buttshake.webp"
        scene cafe_bonnie_home_buttshake
        "Moving behind her, you get a good view of her big round ass waiting to be impaled once again."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/8/buttshake_shake.webm" loop
        show movie with dissolve
        pause
        "Before you get close enough to insert your rock solid cock, Bonnie starts to shake her soft ass from left to right, creating a mesmerizing view of her behind."
        stop movie
        image cafe_bonnie_home_sex4 = "/bonnie/[bonnie.stage]/sex4.webp"
        scene cafe_bonnie_home_sex4
        bonnie "What are you waiting for? Give me your meat."
        "You happily oblige by shoving your erect cock in her soaking wet vagina."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/8/sex4_grind.webm" loop
        show movie with dissolve
        pause
        "Before you fully insert your dick into Bonnie, she begins to push her ass towards you."
        "Her sweaty fat body grinding against your waist captures you in a lusty trance."
        menu:
            "Thrust.":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/8/sex4_thrust.webm" loop
                show movie with dissolve
                window hide
                pause
                "While thrusting, you feel Bonnie reaching her limits, her moans become screams of pleasure while her body begins twitching."
                bonnie "AAAHHH, YES, YEESSS, AAAAAHH!"
                "Her climaxing, twitching body also brings you to your point of explosive relief."
        stop movie
        image cafe_bonnie_home_after_sex = "/bonnie/[bonnie.stage]/after_sex.webp"
        scene cafe_bonnie_home_after_sex
        window hide
        pause
        "After pulling out, you blow your load all over Bonnie's ass and back."
        bonnie "That was some amazing sex, babe. You never disappoint."
        return
    elif bonnie.stage == 9:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/9/sex1_grind.webm" loop
        show movie with dissolve
        pause
        "Bonnie starts off by moving her large hips up and down, her motion triggering a series of jiggles all over her soft flabby body."
        menu:
            "Thrust":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/9/sex1_thrust.webm" loop
                show movie with dissolve
                pause
                "You decide to thrust your hips at a similar pace to hers. Her moans are now clearly audible with every thrust you make."
                stop movie
            "Change position":
                stop movie
                image cafe_bonnie_home_sex2 = "/bonnie/[bonnie.stage]/sex2.webp"
                scene cafe_bonnie_home_sex2
                pc "I know a better position."
                "Bonnie happily moves over, squatting down onto your rock solid dick."
                window hide
                pause
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/9/sex2_grind.webm" loop
                show movie with dissolve
                pause
                "Bonnie swings her heavy body up and down, making both of you loudly moan everytime she comes down on your hard cock."
                menu:
                    "Thrust.":
                        stop movie
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/bonnie/9/sex2_thrust.webm" loop
                        show movie with dissolve
                        pause
                        "Thrusting your cock into her drenched womanhood makes her body jiggle even harder."
                        "At some point it becomes clear that she can no longer handle the squatting position as she begins to collapse onto you."
                        bonnie "Let's go for another position. I am getting a bit too fat for this."
                        "Both of you get up, getting ready for another position."
                stop movie

        image cafe_bonnie_home_tease2 = "/bonnie/[bonnie.stage]/tease2.webp"
        scene cafe_bonnie_home_tease2
        "Bonnie rubs her vagina and then licks the same hand while giving you an enticing view of her ass and pussy."
        "You don't know what is happening, but it definitely turns you on."
        window hide
        pause
        image cafe_bonnie_home_sex3 = "/bonnie/[bonnie.stage]/sex3.webp"
        scene cafe_bonnie_home_sex3
        pc "Come over here, babe."
        "Bonnie comes over and lets you take her from behind."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/9/sex3_grind.webm" loop
        show movie with dissolve
        pause
        "While pushing her body against you she immediately starts grinding your private region."
        menu:
            "Thrust":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/9/sex3_thrust.webm" loop
                show movie with dissolve
                pause
                "You firmly thrust your rigid meat into Bonnie, creating loud moans in the process."
        if kamasutravol1 == 1:
            "You remember reading about a certain position in the Kama Sutra. You decide to try it out."
            pc "I want to try out something exotic I read about."
            bonnie "Let's do it. I will follow your lead."
            stop movie
            image cafe_bonnie_home_sex5 = "/bonnie/[bonnie.stage]/sex5.webp"
            scene cafe_bonnie_home_sex5
            "It takes a few tries, but for some reason you ended up with Bonnie upside down."
            "While the position itself might not be the most practical, it does leave you with a good view of her juicy pussy."
            window hide
            pause
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/9/sex5_thrust.webm" loop
            show movie with dissolve
            pause
            "You thrust your solid cock into her tasty-looking womanhood."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/9/sex5_alt.webm" loop
            show movie with dissolve
            window hide
            pause
            "Having such a good view of her pussy getting penetrated makes all the hassle worth it."
            "After a while it does get quite tiring to keep up this position so you decide to change it up again."
        stop movie
        image cafe_bonnie_home_tease3 = "/bonnie/[bonnie.stage]/tease3.webp"
        scene cafe_bonnie_home_tease3
        bonnie "Come over here, big boy. Take me from behind."
        window hide
        pause
        image cafe_bonnie_home_buttshake = "/bonnie/[bonnie.stage]/buttshake.webp"
        scene cafe_bonnie_home_buttshake
        "Moving behind her, you get a good view of her big round ass waiting to be impaled once again."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/9/buttshake_shake.webm" loop
        show movie with dissolve
        pause
        "Before you get close enough to insert your rock solid cock, Bonnie starts to shake her soft ass from left to right, creating a mesmerizing view of her behind."
        stop movie
        image cafe_bonnie_home_sex4 = "/bonnie/[bonnie.stage]/sex4.webp"
        scene cafe_bonnie_home_sex4
        bonnie "What are you waiting for? Give me your meat."
        "You happily oblige by shoving your erect cock in her soaking wet vagina."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/9/sex4_grind.webm" loop
        show movie with dissolve
        pause
        "Before you fully insert your dick into Bonnie, she begins to push her ass towards you."
        "Her sweaty fat body grinding against your waist captures you in a lusty trance."
        menu:
            "Thrust.":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/9/sex4_thrust.webm" loop
                show movie with dissolve
                window hide
                pause
                "While thrusting, you feel Bonnie reaching her limits, her moans become screams of pleasure while her body begins twitching."
                bonnie "AAAHHH, YES, YEESSS, AAAAAHH!"
                "Her climaxing, twitching body also brings you to your point of explosive relief."
        stop movie
        image cafe_bonnie_home_after_sex = "/bonnie/[bonnie.stage]/after_sex.webp"
        scene cafe_bonnie_home_after_sex
        window hide
        pause
        "After pulling out, you blow your load all over Bonnie's ass and back."
        bonnie "That was some amazing sex, babe. You never disappoint."
        return
    elif bonnie.stage == 10:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/10/sex1_grind.webm" loop
        show movie with dissolve
        pause
        "Bonnie starts off by moving her large hips up and down, her motion triggering a series of jiggles all over her soft flabby body."
        menu:
            "Thrust":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/10/sex1_thrust.webm" loop
                show movie with dissolve
                pause
                "You decide to thrust your hips at a similar pace to hers. Her moans are now clearly audible with every thrust you make."
                stop movie
            "Change position":
                stop movie
                image cafe_bonnie_home_sex2 = "/bonnie/[bonnie.stage]/sex2.webp"
                scene cafe_bonnie_home_sex2
                pc "I know a better position."
                "Bonnie happily moves over, squatting down onto your rock solid dick."
                window hide
                pause
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/10/sex2_grind.webm" loop
                show movie with dissolve
                pause
                "Bonnie swings her heavy body up and down, making both of you loudly moan everytime she comes down on your hard cock."
                menu:
                    "Thrust.":
                        stop movie
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/bonnie/10/sex2_thrust.webm" loop
                        show movie with dissolve
                        pause
                        "Thrusting your cock into her drenched womanhood makes her body jiggle even harder."
                        "At some point it becomes clear that she can no longer handle the squatting position as she begins to collapse onto you."
                        bonnie "Let's go for another position. I am getting a bit too fat for this."
                        "Both of you get up, getting ready for another position."
                stop movie

        image cafe_bonnie_home_tease2 = "/bonnie/[bonnie.stage]/tease2.webp"
        scene cafe_bonnie_home_tease2
        "Bonnie rubs her vagina and then licks the same hand while giving you an enticing view of her ass and pussy."
        "You don't know what is happening, but it definitely turns you on."
        window hide
        pause
        image cafe_bonnie_home_sex3 = "/bonnie/[bonnie.stage]/sex3.webp"
        scene cafe_bonnie_home_sex3
        pc "Come over here, babe."
        "Bonnie comes over and lets you take her from behind."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/10/sex3_grind.webm" loop
        show movie with dissolve
        pause
        "While pushing her body against you she immediately starts grinding your private region."
        menu:
            "Thrust":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/10/sex3_thrust.webm" loop
                show movie with dissolve
                pause
                "You firmly thrust your rigid meat into Bonnie, creating loud moans in the process."
        if kamasutravol1 == 1:
            "You remember reading about a certain position in the Kama Sutra. You decide to try it out."
            pc "I want to try out something exotic I read about."
            bonnie "Let's do it. I will follow your lead."
            stop movie
            image cafe_bonnie_home_sex5 = "/bonnie/[bonnie.stage]/sex5.webp"
            scene cafe_bonnie_home_sex5
            "It takes a few tries, but for some reason you ended up with Bonnie upside down."
            "While the position itself might not be the most practical, it does leave you with a good view of her juicy pussy."
            window hide
            pause
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/10/sex5_thrust.webm" loop
            show movie with dissolve
            pause
            "You thrust your solid cock into her tasty-looking womanhood."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/10/sex5_alt.webm" loop
            show movie with dissolve
            window hide
            pause
            "Having such a good view of her pussy getting penetrated makes all the hassle worth it."
            "After a while it does get quite tiring to keep up this position so you decide to change it up again."
        stop movie
        image cafe_bonnie_home_tease3 = "/bonnie/[bonnie.stage]/tease3.webp"
        scene cafe_bonnie_home_tease3
        bonnie "Come over here, big boy. Take me from behind."
        window hide
        pause
        image cafe_bonnie_home_buttshake = "/bonnie/[bonnie.stage]/buttshake.webp"
        scene cafe_bonnie_home_buttshake
        "Moving behind her, you get a good view of her big round ass waiting to be impaled once again."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/10/buttshake_shake.webm" loop
        show movie with dissolve
        pause
        "Before you get close enough to insert your rock solid cock, Bonnie starts to shake her soft ass from left to right, creating a mesmerizing view of her behind."
        stop movie
        image cafe_bonnie_home_sex4 = "/bonnie/[bonnie.stage]/sex4.webp"
        scene cafe_bonnie_home_sex4
        bonnie "What are you waiting for? Give me your meat."
        "You happily oblige by shoving your erect cock in her soaking wet vagina."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/10/sex4_grind.webm" loop
        show movie with dissolve
        pause
        "Before you fully insert your dick into Bonnie, she begins to push her ass towards you."
        "Her sweaty fat body grinding against your waist captures you in a lusty trance."
        menu:
            "Thrust.":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/10/sex4_thrust.webm" loop
                show movie with dissolve
                window hide
                pause
                "While thrusting, you feel Bonnie reaching her limits, her moans become screams of pleasure while her body begins twitching."
                bonnie "AAAHHH, YES, YEESSS, AAAAAHH!"
                "Her climaxing, twitching body also brings you to your point of explosive relief."
        stop movie
        image cafe_bonnie_home_after_sex = "/bonnie/[bonnie.stage]/after_sex.webp"
        scene cafe_bonnie_home_after_sex
        window hide
        pause
        "After pulling out, you blow your load all over Bonnie's ass and back."
        bonnie "That was some amazing sex, babe. You never disappoint."
        return
    elif bonnie.stage == 11:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/11/sex1_grind.webm" loop
        show movie with dissolve
        pause
        "Bonnie starts off by moving her large hips up and down, her motion triggering a series of jiggles all over her soft flabby body."
        menu:
            "Thrust":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/11/sex1_thrust.webm" loop
                show movie with dissolve
                pause
                "You decide to thrust your hips at a similar pace to hers. Her moans are now clearly audible with every thrust you make."
                stop movie
            "Change position":
                stop movie
                image cafe_bonnie_home_sex2 = "/bonnie/[bonnie.stage]/sex2.webp"
                scene cafe_bonnie_home_sex2
                pc "I know a better position."
                "Bonnie happily moves over, squatting down onto your rock solid dick."
                window hide
                pause
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/11/sex2_grind.webm" loop
                show movie with dissolve
                pause
                "Bonnie swings her heavy body up and down, making both of you loudly moan everytime she comes down on your hard cock."
                menu:
                    "Thrust.":
                        stop movie
                        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                        play movie "/images/bonnie/11/sex2_thrust.webm" loop
                        show movie with dissolve
                        pause
                        "Thrusting your cock into her drenched womanhood makes her body jiggle even harder."
                        "At some point it becomes clear that she can no longer handle the squatting position as she begins to collapse onto you."
                        bonnie "Let's go for another position. I am getting a bit too fat for this."
                        "Both of you get up, getting ready for another position."
                stop movie

        image cafe_bonnie_home_tease2 = "/bonnie/[bonnie.stage]/tease2.webp"
        scene cafe_bonnie_home_tease2
        "Bonnie rubs her vagina and then licks the same hand while giving you an enticing view of her ass and pussy."
        "You don't know what is happening, but it definitely turns you on."
        window hide
        pause
        image cafe_bonnie_home_sex3 = "/bonnie/[bonnie.stage]/sex3.webp"
        scene cafe_bonnie_home_sex3
        pc "Come over here, babe."
        "Bonnie comes over and lets you take her from behind."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/11/sex3_grind.webm" loop
        show movie with dissolve
        pause
        "While pushing her body against you she immediately starts grinding your private region."
        menu:
            "Thrust":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/11/sex3_thrust.webm" loop
                show movie with dissolve
                pause
                "You firmly thrust your rigid meat into Bonnie, creating loud moans in the process."
        if kamasutravol1 == 1:
            "You remember reading about a certain position in the Kama Sutra. You decide to try it out."
            pc "I want to try out something exotic I read about."
            bonnie "Let's do it. I will follow your lead."
            stop movie
            image cafe_bonnie_home_sex5 = "/bonnie/[bonnie.stage]/sex5.webp"
            scene cafe_bonnie_home_sex5
            "It takes a few tries, but for some reason you ended up with Bonnie upside down."
            "While the position itself might not be the most practical, it does leave you with a good view of her juicy pussy."
            window hide
            pause
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/11/sex5_thrust.webm" loop
            show movie with dissolve
            pause
            "You thrust your solid cock into her tasty-looking womanhood."
            stop movie
            image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
            play movie "/images/bonnie/11/sex5_alt.webm" loop
            show movie with dissolve
            window hide
            pause
            "Having such a good view of her pussy getting penetrated makes all the hassle worth it."
            "After a while it does get quite tiring to keep up this position so you decide to change it up again."
        stop movie
        image cafe_bonnie_home_tease3 = "/bonnie/[bonnie.stage]/tease3.webp"
        scene cafe_bonnie_home_tease3
        bonnie "Come over here, big boy. Take me from behind."
        window hide
        pause
        image cafe_bonnie_home_buttshake = "/bonnie/[bonnie.stage]/buttshake.webp"
        scene cafe_bonnie_home_buttshake
        "Moving behind her, you get a good view of her big round ass waiting to be impaled once again."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/11/buttshake_shake.webm" loop
        show movie with dissolve
        pause
        "Before you get close enough to insert your rock solid cock, Bonnie starts to shake her soft ass from left to right, creating a mesmerizing view of her behind."
        stop movie
        image cafe_bonnie_home_sex4 = "/bonnie/[bonnie.stage]/sex4.webp"
        scene cafe_bonnie_home_sex4
        bonnie "What are you waiting for? Give me your meat."
        "You happily oblige by shoving your erect cock in her soaking wet vagina."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/11/sex4_grind.webm" loop
        show movie with dissolve
        pause
        "Before you fully insert your dick into Bonnie, she begins to push her ass towards you."
        "Her sweaty fat body grinding against your waist captures you in a lusty trance."
        menu:
            "Thrust.":
                stop movie
                image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                play movie "/images/bonnie/11/sex4_thrust.webm" loop
                show movie with dissolve
                window hide
                pause
                "While thrusting, you feel Bonnie reaching her limits, her moans become screams of pleasure while her body begins twitching."
                bonnie "AAAHHH, YES, YEESSS, AAAAAHH!"
                "Her climaxing, twitching body also brings you to your point of explosive relief."
        stop movie
        image cafe_bonnie_home_after_sex = "/bonnie/[bonnie.stage]/after_sex.webp"
        scene cafe_bonnie_home_after_sex
        window hide
        pause
        "After pulling out, you blow your load all over Bonnie's ass and back."
        bonnie "That was some amazing sex, babe. You never disappoint."
        return

label Bonnie_Introduction:
    ###Scene 1: Bunny Bites (Working)###
    image cafe_bonnie_arrive = "/bonnie/[bonnie.stage]/cafe_arrive.webp"
    scene cafe_bonnie_arrive
    play music "/music/bunny_bites.ogg" if_changed
    "Bonnie arrives as a customer."
    pc "Hey, it’s the girl from the sweets shop."
    image cafe_bonnie_talk = "/bonnie/[bonnie.stage]/cafe_talk.webp"
    scene cafe_bonnie_talk
    bonnie "Hey, how is my best customer?"
    pc "Best customer?"
    "Bonnie looks down a little awkwardly."
    bonnie "Things have been a little slow, so I really appreciate you coming in."
    pc "I'm sorry to hear that, I'm sure it's just a bad week."
    bonnie "More like month."
    bonnie "Sorry, I didn’t mean to drop this on you. Mind taking my order?"
    pc "Sure, What can I get you today?"
    bonnie "I would like to order a hamburger and one slice of pizza."
    pc "Coming right up, please find a nice place to sit down."
    "You create her food."

    ###Scene image - Bonnie sitting in booth###
    image cafe_bonnie_booth = "/bonnie/[bonnie.stage]/cafe_booth.webp"
    scene cafe_bonnie_booth
    pc "Here you are, have a nice meal."
    bonnie "Thank you!"
    $ bonnie.weight += 0.3

    #call work_randomizer from _call_work_randomizer_3
    "A while later."

    ### (At end of shift) Scene image – Bonnie still sitting in booth####
    image bonnie_stage1_start = "/bonnie/events/stage1/start.webp"
    scene bonnie_stage1_start
    pc "Bonnie is still here, maybe I should go and speak to her."
    #[GAME OPTION – YES or NO]
    menu:
        "Speak to her.":
            #IF YES
            image bonnie_stage1_1 = "/bonnie/events/stage1/1.webp"
            scene bonnie_stage1_1
            pc "Hi Bonnie, sorry to disturb you. You just seemed a little down. Are you ok?"
            bonnie "Oh, it's kind of you to ask."
            image bonnie_stage1_2 = "/bonnie/events/stage1/2.webp"
            scene bonnie_stage1_2
            bonnie "I’m still thinking about the shop. I’m not sure how much longer I can keep it open."
            pc "Why? I thought people loved your sweets."
            image bonnie_stage1_3 = "/bonnie/events/stage1/3.webp"
            scene bonnie_stage1_3
            bonnie "They did...before my partner left."
            bonnie "They took the recipe for our famous quadruple chocolate fudge bombs with them."
            image bonnie_stage1_4 = "/bonnie/events/stage1/4.webp"
            scene bonnie_stage1_4
            bonnie "Those chocolates were our best sellers. Without them, I’m worried I won’t be able to keep the store profitable."
            pc "Maybe you can try to recreate the recipe?"
            image bonnie_stage1_5 = "/bonnie/events/stage1/5.webp"
            scene bonnie_stage1_5
            bonnie "I’ve been trying. But there are so many variations and doing it all myself is harder than I thought it would be."
            bonnie "The real problem is when I'm tasting them I know what recipe I’ve used. I need to find a way of testing them without being able to tell which ones they are."
            bonnie "That way I would have no expectations before tasting them."
            pc "Maybe I could help with that?"
            image bonnie_stage1_6 = "/bonnie/events/stage1/6.webp"
            scene bonnie_stage1_6
            bonnie "What do you mean?"
            pc "You only need a way of randomising it right?"
            image bonnie_stage1_7 = "/bonnie/events/stage1/7.webp"
            scene bonnie_stage1_7
            bonnie "Sure."
            pc "Then if you make all the chocolates, I could come and give them to you in a random order. That way you wouldn’t know which ones are which."
            image bonnie_stage1_8 = "/bonnie/events/stage1/8.webp"
            scene bonnie_stage1_8
            bonnie "You’re right!"
            image bonnie_stage1_9 = "/bonnie/events/stage1/9.webp"
            scene bonnie_stage1_9
            bonnie "Then I could focus on the flavours and maybe figure out what is different."
            image bonnie_stage1_10 = "/bonnie/events/stage1/10.webp"
            scene bonnie_stage1_10
            bonnie "But are you sure you want to do that? It might be a little boring."
            pc "Absolutely, and who knows I might pick up a thing or two about the perfect chocolate."
            image bonnie_stage1_standup = "/bonnie/events/stage1/standup.webp"
            scene bonnie_stage1_standup
            bonnie "Amazing! Thank you so much. I have some things to prepare but I will give you a call when I am ready to start testing."
            image bonnie_stage1_phone = "/bonnie/events/stage1/phone.webp"
            scene bonnie_stage1_phone
            "Bonnie quickly hands you her phone to put your number into it before leaving."
            image bonnie_stage1_eventend = "/bonnie/events/stage1/eventend.webp"
            scene bonnie_stage1_eventend
            $ bonnieintroduction = 0
        "Leave her be.":
            return
    return

label Bonnie_Stage_1_Event:
    ### Scene image - In PC room scene like normal###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("Hi, thank you for offering to help. I think I have everything ready if you are free today?", who=1)
    pause
    menu:
        "Yes":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "Not tonight":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
    #[GAME – YES / Not tonight options]
    #IF YES

    ### Scene image – Bonnie front of shop [Normal image wearing her normal dress]####
    image cafe_bonnie_home_outside_event = "/bonnie/1/home_outside.webp"
    scene cafe_bonnie_home_outside_event
    bonnie "You came!"
    pc "Of course, can’t let you or my favourite sweet shop go out of business."
    bonnie "That’s kind of you to say. I think everything is prepared if you want to come through."
    "You follow Bonnie into her shop. As she walks in, she opens and then walks through a door behind the counter, she motions to you to follow her."

    ### Scene image change – Bonnie in her hallway####
    image cafe_bonnie_home_arrive_event = "/bonnie/1/home_arrive.webp"
    scene cafe_bonnie_home_arrive_event
    play music "/music/bonnie.ogg" if_changed
    pc "Wait, do you live here?"
    bonnie "Of course. What did you think was back here?"
    pc "I don’t know, I just thought there would be a big kitchen or lab or something."
    bonnie "Nope, just me. Don’t need anything that fancy and it saves on renting somewhere else. Although living so close to the shop does make it harder not to sneak a midnight snack."
    bonnie "Especially since my partner is not here anymore to stop me."
    bonnie "The kitchen is through here."


    ### Scene image change– Bonnie in her kitchen####
    image bonnie_stage1_2_1 = "/bonnie/events/stage1/2_1.webp"
    scene bonnie_stage1_2_1
    "Walking into the kitchen your nose is filled with the sweet smell of fresh chocolate."
    "Looking around you marvel at the large kitchen covered with chocolates of all kinds."
    image bonnie_stage1_2_2 = "/bonnie/events/stage1/2_2.webp"
    scene bonnie_stage1_2_2
    "The shape and sizes were similar, but each varied slightly in colour, texture and finish. No wonder Bonnie was having so much trouble."
    pc "This is a lot of chocolate, are these all for the taste testing?"
    image bonnie_stage1_2_3 = "/bonnie/events/stage1/2_3.webp"
    scene bonnie_stage1_2_3
    bonnie "Oh sorry, is it too much?"
    pc "Shouldn’t I be asking you that? I don’t want to make you sick."
    image bonnie_stage1_2_4 = "/bonnie/events/stage1/2_4.webp"
    scene bonnie_stage1_2_4
    bonnie "Don’t worry about that. I have a super high tolerance for sweets. Wouldn’t have made it this far working in a sweet shop without it."
    bonnie "Although if I'm not careful, our menu won't be the only thing expanding."

    ### Scene image change– Bonnie in her Lounge on sofa####
    image bonnie_stage1_hopeful = "/bonnie/events/stage1/hopeful.webp"
    scene bonnie_stage1_hopeful
    bonnie "Ready whenever you are."
    "Grabbing a chocolate at random you walk over to her."
    pc "Here is chocolate number one."
    image bonnie_stage1_2_5 = "/bonnie/events/stage1/2_5.webp"
    scene bonnie_stage1_2_5
    "Taking it Bonnie closes her eyes, focusing on the tastes as she lets the chocolate melt on her tongue, coating her mouth with it."
    bonnie "Mmm, it's good but too much white chocolate."
    image bonnie_stage1_hopeful = "/bonnie/events/stage1/hopeful.webp"
    scene bonnie_stage1_hopeful
    bonnie "Would you mind taking notes, there should be little cards next to the chocolates with numbers on."
    pc "Sure thing."
    "Quickly making a note of what Bonnie thought of each chocolate you go to grab the next one."
    pc "Here is chocolate number two."
    image bonnie_stage1_2_6 = "/bonnie/events/stage1/2_6.webp"
    scene bonnie_stage1_2_6
    "Again, Bonnie closes her eyes, focusing on the tastes as she lets the chocolate melt on her tongue, coating her mouth with it."
    bonnie "That’s better, but I’m not sure why. Can I have another?"
    pc "Sure."
    image bonnie_stage1_2_7 = "/bonnie/events/stage1/2_7.webp"
    scene bonnie_stage1_2_7
    "This time she takes a bite through the centre, chewing it thoroughly before popping in the second half."
    bonnie "Definitely too much fudge."
    pc "Here is the next one."
    image bonnie_stage1_2_8 = "/bonnie/events/stage1/2_8.webp"
    scene bonnie_stage1_2_8
    "Over the next hour you keep feeding Bonnie chocolate after chocolate."
    "Each one is carefully considered before her expert tongue finds something wrong with it."
    image bonnie_stage1_2_9 = "/bonnie/events/stage1/2_9.webp"
    scene bonnie_stage1_2_9
    "As the evening wears on you are starting to wonder if she has a limit to the number of chocolates she can eat."
    "But as the number of empty plates begin to outweigh the number of chocolates left, Bonnie seems to be beginning to struggle."
    image bonnie_stage1_hopeful = "/bonnie/events/stage1/hopeful.webp"
    scene bonnie_stage1_hopeful
    bonnie "Ugh, I think that’s enough for today."
    pc "There are only a few left."
    image bonnie_stage1_desire = "/bonnie/events/stage1/desire.webp"
    scene bonnie_stage1_desire
    bonnie "But I’ve eaten so many already."
    pc "I thought you wanted to find the right recipe."
    image bonnie_stage1_angry = "/bonnie/events/stage1/angry.webp"
    scene bonnie_stage1_angry
    bonnie "You are right, I can handle a few more for the sake of the shop."
    "Handing her another chocolate there is an obvious pause before she puts it into her mouth."
    pc "Just a couple more."
    bonnie "Good, I don’t think I've ever been this full of chocolate."
    image bonnie_stage1_2_10 = "/bonnie/events/stage1/2_10.webp"
    scene bonnie_stage1_2_10
    window hide
    pause
    image bonnie_stage1_2_11 = "/bonnie/events/stage1/2_11.webp"
    scene bonnie_stage1_2_11
    "Handing her the last of the chocolates there is a visible relief as Bonnie slouches back on the sofa."
    image bonnie_stage1_stuffed = "/bonnie/events/stage1/stuffed.webp"
    scene bonnie_stage1_stuffed
    "Gently rubbing her bloated stomach it was clear Bonnie was regretting this slightly."
    pc "Any luck with the recipes?"
    bonnie "I think so. Thank you for your help."
    pc "Anytime."
    image bonnie_stage1_eventend2 = "/bonnie/events/stage1/eventend2.webp"
    scene bonnie_stage1_eventend2
    bonnie "Do you mean that? It really does make it easier if I'm not sure which version I'm eating each time."
    bonnie "If you are up for it, I’d love to do it again…once I have recovered from today."
    pc "Absolutely!"

    scene outside2
    stop music fadeout 1.0
    "Leaving the stuffed Bonnie to sleep it off, you let yourself out and head home excited for the next taste testing."

    if recollection == False:
        $ daytime += 1
        $ bonnie.weight = 76
        $ phonecall = 1
    $ bonniestage1event = 0
    return

label Bonnie_Stage_2_Event_1:
    ### Scene image - In PC room scene like normal###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("Hi, you won't believe what I found down the back of the counter. It's my partners old cookbook and it's full of recipes! I think this could be a real game changer, are you free to do some more experimenting?", who=1)
    pause
    menu:
        "Yes":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "Not tonight":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
    ##[GAME – YES / Not tonight options]
    ##IF YES

    ##### Scene image – Bonnie in front of shop like normal (Normal clothing)####
    image cafe_bonnie_home_outside_event2 = "/bonnie/2/home_outside.webp"
    scene cafe_bonnie_home_outside_event2
    bonnie "Thanks again for helping. I'm so excited to try out these recipes."
    pc "No problem."

    ##### Scene image – Bonnie back on her Sofa####
    image bonnie_stage2_1 = "/bonnie/events/stage2/1.webp"
    scene bonnie_stage2_1
    play music "/music/bonnie.ogg" if_changed
    "Walking in you notice just as many chocolates as last time, possibly more."
    pc "I thought you said you found the recipe?"
    image bonnie_stage2_2 = "/bonnie/events/stage2/2.webp"
    scene bonnie_stage2_2
    bonnie "Oh, sort of."
    bonnie "It had a lot of what I needed, but some of the pages were damaged."
    bonnie "So I thought it would be best to just try everything."
    image bonnie_stage2_3 = "/bonnie/events/stage2/3.webp"
    scene bonnie_stage2_3
    "Grabbing the first chocolate you hand it to Bonnie who hastily puts it into her mouth."
    bonnie "MMMmm!"
    bonnie "These are already so much better."
    pc "So is that it, is that the one?"
    image bonnie_stage2_4 = "/bonnie/events/stage2/4.webp"
    scene bonnie_stage2_4
    bonnie "No, it's closer than anything I made before, but still something is off."
    bonnie "Think I'm going to need a few more to figure it out."
    image bonnie_stage2_5 = "/bonnie/events/stage2/5.webp"
    scene bonnie_stage2_5
    "Handing her the next chocolate you make sure to keep her hands and mouth full of delicious chocolates at all times."
    image bonnie_stage2_6 = "/bonnie/events/stage2/6.webp"
    scene bonnie_stage2_6
    "Each one seems to almost make her purr in delight as she eats them down."
    image bonnie_stage2_7 = "/bonnie/events/stage2/7.webp"
    scene bonnie_stage2_7
    "Unlike last time, the careful consideration seems to have been replaced by pure enjoyment."
    image bonnie_stage2_8a = "/bonnie/events/stage2/8a.webp"
    scene bonnie_stage2_8a
    window hide
    pause
    image bonnie_stage2_8b= "/bonnie/events/stage2/8b.webp"
    scene bonnie_stage2_8b
    "One after another they disappear down her throat and into her stomach."
    image bonnie_stage2_9 = "/bonnie/events/stage2/9.webp"
    scene bonnie_stage2_9
    bonnie "That’s the closest one yet. Which one was that?"
    pc "The note on the plate says blend six high sugar."
    bonnie "Interesting. I'm starting to feel full again though."
    bonnie "But I think we should keep going, don’t want to miss out if we have got it completely right in one of the others."
    image bonnie_stage2_10 = "/bonnie/events/stage2/10.webp"
    scene bonnie_stage2_10
    "Happy to oblige, you continue handing her the small chocolates."
    image cafe_bonnie_home_stuffed1_event2 = "/bonnie/2/stuffed1.webp"
    scene cafe_bonnie_home_stuffed1_event2
    "You watch on as Bonnie's belly seems to grow a little with each chocolate."
    "Her appetite for sweets only matched by her desire to find the right recipe."
    image cafe_bonnie_home_stuffed2_event2 = "/bonnie/2/stuffed2.webp"
    scene cafe_bonnie_home_stuffed2_event2
    "But soon her stomach is too full to be ignored."
    image bonnie_stage2_11 = "/bonnie/events/stage2/11.webp"
    scene bonnie_stage2_11
    bonnie "Oooh, definitely running out of room down there."
    image bonnie_stage2_12 = "/bonnie/events/stage2/12.webp"
    scene bonnie_stage2_12
    bonnie "How many are left?"
    pc "Just a few."
    bonnie "Ok, I can do this."
    image bonnie_stage2_13 = "/bonnie/events/stage2/13.webp"
    scene bonnie_stage2_13
    "Bonnie continues eating, although at a noticeably slower speed."
    "Her chewing is becoming more and more laboured with each new chocolate."
    image bonnie_stage2_14 = "/bonnie/events/stage2/14.webp"
    scene bonnie_stage2_14
    "The pure enjoyment was dwindling in her eyes as she forced herself to eat more."
    bonnie "I think I'm done, I can't eat any more chocolates."
    pc "But there is just one more."
    "Reluctantly Bonnie outstretches a hand to take it."
    image bonnie_stage2_lastchocolate = "/bonnie/events/stage2/lastchocolate.webp"
    scene bonnie_stage2_lastchocolate
    "Leaning backwards she tries to manoeuvre herself to give her bloated belly more room as she finishes the last chocolate."
    "Going back into the kitchen you make a final check for any escaped chocolates but fail to find any."
    image bonnie_stage2_asleep1 = "/bonnie/events/stage2/asleep1.webp"
    scene bonnie_stage2_asleep1
    "Looking over at the sofa it seems that now full to the brim Bonnie has passed out on her sofa."
    "You notice her phone is unlocked, showing a dieting app."
    "You decide to share her progress to yourself."
    image bonnie_stage2_asleep2 = "/bonnie/events/stage2/asleep2.webp"
    scene bonnie_stage2_asleep2
    $ bonnie_stats_visible = 1
    "Bonnie is now added to the stats menu."
    "Clearing up the empty plates as Bonnie sleeps, you are about to leave when you notice something."
    image bonnie_stage2_book = "/bonnie/events/stage2/book.webp"
    scene bonnie_stage2_book
    "On the counter is a cookbook, it must be the one her partner had."
    "Glancing over at it you are surprised to see something you recognise."
    "In one corner it mentions the university library, with a small set of numbers after it. Was Bonnie's partner an old pupil at the university?"
    pc "I wonder if the librarian might know something about this?"
    "Ripping the corner off the page you place it in your pocket."

    ##### Scene  2 image – Library with Librarian####
    image bonnie_stage2_lib1 = "/bonnie/events/stage2/lib1.webp"
    scene bonnie_stage2_lib1
    stop music fadeout 1.0
    librarian "Hi, I'm sorry we are closing shortly."
    pc "That’s ok, I won't be long."
    image bonnie_stage2_lib2 = "/bonnie/events/stage2/lib2.webp"
    scene bonnie_stage2_lib2
    pc "I was wondering If you know what this is?"
    librarian "That’s a book code."
    image bonnie_stage2_lib3 = "/bonnie/events/stage2/lib3.webp"
    scene bonnie_stage2_lib3
    "The librarian disappears down one of the bookshelves."
    ###(Image of library with no librarian, then she comes back for next line)###
    image bonnie_stage2_lib4 = "/bonnie/events/stage2/lib4.webp"
    scene bonnie_stage2_lib4
    librarian "It seems to be for a book called “Sweet tooths volume 1” if that’s what you are looking for."
    librarian "Would you like to buy it?"
    $ bonniestage2event = 0
    call buybook from _call_buybook

    scene outside2
    "After a long day you head home."
    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
        $ bonnie.weight += 0.5
    return

label Bonnie_Stage_2_Event_2:
    #Once The Book Has been read
    ### Scene image - In PC room scene like normal###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("Hi [playername], are you free tonight? I really think we are close to a break through with these taste tests.", who=1)
    pause
    menu:
        "Yes":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "Not tonight":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
    #[GAME – YES / Not tonight options]
    #IF YES

    ##### Scene image – Bonnie in front of shop like normal (Normal clothing)####
    image cafe_bonnie_home_outside_event2 = "/bonnie/2/home_outside.webp"
    scene cafe_bonnie_home_outside_event2
    bonnie "Thanks again for helping. I'm excited to try out these recipes."
    pc "No problem."

    ##### Scene image – Bonnie back on her Sofa####
    image bonnie_stage2_1 = "/bonnie/events/stage2/1.webp"
    scene bonnie_stage2_1
    play music "/music/bonnie.ogg" if_changed
    "Once again the counters are covered in chocolates of all types."
    bonnie "I really think we are close to a breakthrough."
    pc "Even if you can't get the recipe exactly the same, I'm sure some of these would sell well."
    image bonnie_stage2_15 = "/bonnie/events/stage2/15.webp"
    scene bonnie_stage2_15
    bonnie "I know, but it's not the same."
    bonnie "People know our…my chocolates."
    bonnie "We have to find it, it has to be perfect no matter how many times we have to do this."
    "You can see the desire in her eyes, this means more to her than just money."
    pc "Well, in that case, let's get started."
    image bonnie_stage2_3 = "/bonnie/events/stage2/3.webp"
    scene bonnie_stage2_3
    "Handing Bonnie the first chocolate she begins to repeat your tests."
    image cafe_bonnie_home_stuffed1_event2 = "/bonnie/2/stuffed1.webp"
    scene cafe_bonnie_home_stuffed1_event2
    "Again and again you hand her chocolates, watching her belly swell before your eyes."
    image cafe_bonnie_home_stuffed2_event2 = "/bonnie/2/stuffed2.webp"
    scene cafe_bonnie_home_stuffed2_event2
    "Stopping from time to time she makes small notes in the old notebook next to the recipes."
    image bonnie_stage2_16 = "/bonnie/events/stage2/16.webp"
    scene bonnie_stage2_16
    bonnie "Not quite right again."
    bonnie "I'm sorry this is taking so long."
    pc "You don’t have to apologise. I want to help."
    image bonnie_stage2_17 = "/bonnie/events/stage2/17.webp"
    scene bonnie_stage2_17
    bonnie "I know, but we have spent weeks on this and I've eaten hundreds of chocolates."
    bonnie "Not to mention the weight I’ve gained, it will take even longer to work this off in the gym."
    pc "Let's not give up yet."
    bonnie "But we are almost out of chocolates, I just don’t think I can do this."
    pc "Maybe I can give it a go. Sometimes a fresh perspective can help?"
    image bonnie_stage2_18 = "/bonnie/events/stage2/18.webp"
    scene bonnie_stage2_18
    bonnie "Not to be mean, but do you even know how to make chocolates?"
    pc "I’ve read about it in a book."
    image bonnie_stage2_19 = "/bonnie/events/stage2/19.webp"
    scene bonnie_stage2_19
    bonnie "That’s not quite what I meant."
    bonnie "But what have we got to lose?"

    ### Scene image - In Bonnies kitchen###
    image bonnie_stage2_40 = "/bonnie/events/stage2/40.webp"
    scene bonnie_stage2_40
    "Taking the book out of your bag you carefully hide it under one of Bonnie's to keep it out of sight of her."
    "Grabbing the ingredients you carefully measure each one out as it says to in the book."
    "The blend of chocolates listed is very specific and clearly honed after many attempts."
    image bonnie_stage2_37 = "/bonnie/events/stage2/37.webp"
    scene bonnie_stage2_37
    "Breaking the chocolate into the pan you gently stir it as it melts from the heat."
    image bonnie_stage2_38 = "/bonnie/events/stage2/38.webp"
    scene bonnie_stage2_38
    "You finish by adding a dash of double fat cream to the mixture."
    image bonnie_stage2_39 = "/bonnie/events/stage2/39.webp"
    scene bonnie_stage2_39
    "Slowly tossing the fudge pieces through the chocolate until covered in a thick layer of the sweet brown concoction you scoop them out onto a tray."
    "Leaving the first batch to cool in her fridge you repeat the same steps until you have several plates of delicious looking chocolates, ready to be tasted."
    "Returning the book to your bag you call Bonnie over."


    ##### Scene image – Bonnie in the kitchen####
    image bonnie_stage2_20 = "/bonnie/events/stage2/20.webp"
    scene bonnie_stage2_20
    bonnie "Wow, these actually smell amazing."
    pc "Thanks, I think the first batch are ready if you want to try them?"
    image bonnie_stage2_21 = "/bonnie/events/stage2/21.webp"
    scene bonnie_stage2_21
    bonnie "I don’t know, I've eaten so many already."
    bonnie "Plus, I've never weighed this much before. What will people think?!"
    pc "Please, just a couple. I worked hard on them."
    image bonnie_stage2_22 = "/bonnie/events/stage2/22.webp"
    scene bonnie_stage2_22
    bonnie "Well, you are helping me, so the least I can do is to taste them."
    bonnie "Maybe just one bite…"
    image bonnie_stage2_23 = "/bonnie/events/stage2/23.webp"
    scene bonnie_stage2_23
    "Handing her one of the chocolates she reluctantly raises it to her mouth. Her belly already full of dozens of others."
    image bonnie_stage2_24 = "/bonnie/events/stage2/24.webp"
    scene bonnie_stage2_24
    "Hesitantly she gently bites down on the chocolate before her eyes go wide."
    bonnie "OH MY GOD!"
    bonnie "That’s it!"
    "Shoving the chocolate into her mouth she chews with renewed vigour as her knees seem to go weak for a moment."
    image bonnie_stage2_25 = "/bonnie/events/stage2/25.webp"
    scene bonnie_stage2_25
    bonnie "But how?"
    pc "I guess I must have picked something up from you."
    pc "We have been spending a lot of time in your kitchen."
    image bonnie_stage2_26 = "/bonnie/events/stage2/26.webp"
    scene bonnie_stage2_26
    bonnie "I don’t care, I just need more!"
    "You can see the same fire you saw earlier, but this time it’s for your chocolates."
    pc "You can eat…"
    image bonnie_stage2_27 = "/bonnie/events/stage2/27.webp"
    scene bonnie_stage2_27
    "Bonnie doesn’t even wait for you to finish that sentence."
    "Grabbing handfuls at a time Bonnie starts to devour the chocolates you have made."
    image bonnie_stage2_28 = "/bonnie/events/stage2/28.webp"
    scene bonnie_stage2_28
    "Her jaw in constant movement as she all but swallows them whole."
    "No matter how many she eats, it seems she can't get enough."
    image bonnie_stage2_41 = "/bonnie/events/stage2/41.webp"
    scene bonnie_stage2_41
    bonnie "More! I need more!"
    "Grabbing the last tray out of the fridge you place it on the counter."
    image bonnie_stage2_29 = "/bonnie/events/stage2/29.webp"
    scene bonnie_stage2_29
    "You watch as Bonnie begins to work her way through them."
    image bonnie_stage2_30 = "/bonnie/events/stage2/30.webp"
    scene bonnie_stage2_30
    window hide
    pause
    image bonnie_stage2_31 = "/bonnie/events/stage2/31.webp"
    scene bonnie_stage2_31
    "Her stomach bulging, but her appetite for chocolate unending."
    image bonnie_stage2_32 = "/bonnie/events/stage2/32.webp"
    scene bonnie_stage2_32
    window hide
    pause

    ####scene image, Bonnie stuffed on couch again####
    image bonnie_stage2_33 = "/bonnie/events/stage2/33.webp"
    scene bonnie_stage2_33
    "Finally as the last tray is emptied Bonnie falls back onto the sofa completely stuffed."
    bonnie "They are just like I remember."
    pc "So they are good then?"
    image bonnie_stage2_34 = "/bonnie/events/stage2/34.webp"
    scene bonnie_stage2_34
    bonnie "So…so good."
    pc "Should I make some more for you to sell?"
    image bonnie_stage2_35 = "/bonnie/events/stage2/35.webp"
    scene bonnie_stage2_35
    bonnie "Oh yeah, the shop."
    "It's clear Bonnie is starting to feel embarrassed about her frenzied feeding, having forgotten all about the shop and the reason for the chocolate testing."
    image bonnie_stage2_36 = "/bonnie/events/stage2/36.webp"
    scene bonnie_stage2_36
    bonnie "I will need to get some more ingredients for you since I ate… Since we ran out."
    bonnie "Maybe you can come by next week and make another batch so we can start selling them."
    pc "Sure. That sounds like a good plan."

    scene outside2
    stop music fadeout 1.0
    "That was amazing, you don’t think you have ever seen someone lose control over themselves like that. These chocolates must be the real deal."
    "I should keep an eye out for more books in that series."
    if recollection == False:
        $ bonnie.weight += 1.0
        $ daytime += 1
        $ phonecall = 1
    $ bonniestage2event2 = 0
    return

label Bonnie_Stage_3_Event:
    ### Scene image - In PC room scene like normal ###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("Hi, are you free tonight? I’ve restocked everything you will need to make those chocolates.", who=1)
    pause
    menu:
        "Yes":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "Not tonight":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
    #[GAME – YES / Not tonight options]
    #IF YES

    ##### Scene image – Empty  front of shop####
    image bonnie_stage3_1 = "/bonnie/events/stage3/1.webp"
    scene bonnie_stage3_1
    "That's weird. Bonnie usually meets you out here."
    pc "Bonnie, are you here?"
    "Maybe she is in the kitchen already?"

    ##### Scene image – Bonnies house - Empty  hallway####
    image bonnie_stage3_2 = "/bonnie/events/stage3/2.webp"
    scene bonnie_stage3_2
    pc "Bonnie?"

    ##### Scene image – Bonnies house – Bonnie slouched on the couch stuffed and in underwear####
    "Walking in you can hear faint groans coming from the living room."
    image bonnie_stage3_3 = "/bonnie/events/stage3/3.webp"
    scene bonnie_stage3_3
    play music "/music/bonnie.ogg" if_changed
    "Looking over to the couch you spot Bonnie, her usually small stomach completely ballooned up and stuffed to its limit."
    "You can see why as empty boxes of your chocolates litter the floor and couch."
    pc "Bonnie?"
    bonnie "Ooooh."
    image bonnie_stage3_4 = "/bonnie/events/stage3/4.webp"
    scene bonnie_stage3_4
    "Bonnie groans as she stirs from her chocolate food coma."
    bonnie "Hey, [playername]. Sorry I must have dozed off."
    pc "Are you ok?"
    image bonnie_stage3_5 = "/bonnie/events/stage3/5.webp"
    scene bonnie_stage3_5
    bonnie "Yeah, I guess I got a little hungry."
    pc "Bonnie, there must be half a week's worth of chocolates here."
    image bonnie_stage3_6 = "/bonnie/events/stage3/6.webp"
    scene bonnie_stage3_6
    bonnie "I'm sorry, I didn’t mean to give you extra work."
    bonnie "You must think I'm being really selfish right now."
    pc "No, it's no problem. In fact, if you want me to make extra each week for you, I am happy to."
    image bonnie_stage3_7 = "/bonnie/events/stage3/7.webp"
    scene bonnie_stage3_7
    bonnie "Really? That would be nice. But actually, I probably shouldn't; otherwise I'll never be able to slim back down."
    pc "You don’t need to worry about that, you look great."
    bonnie "Thank you."
    bonnie "I'm in my underwear!"
    image bonnie_stage3_8 = "/bonnie/events/stage3/8.webp"
    scene bonnie_stage3_8
    bonnie "I'm so sorry, this is hardly professional."
    pc "I don’t mind if you don’t."
    image bonnie_stage3_9 = "/bonnie/events/stage3/9.webp"
    scene bonnie_stage3_9
    bonnie "Well, I'm too full to move and get changed anyway."
    pc "So, what actually happened? This is more than a snack."
    image bonnie_stage3_10 = "/bonnie/events/stage3/10.webp"
    scene bonnie_stage3_10
    bonnie "I'm sorry, I guess I was missing my old partner. It had been months since I had tasted those chocolates and I guess they just reminded me of better times."
    bonnie "I had only meant to eat a couple but before I could stop myself I had gone through boxes and boxes of them."
    bonnie "But do you know what the worst part is?"
    pc "What?"
    image bonnie_stage3_11 = "/bonnie/events/stage3/11.webp"
    scene bonnie_stage3_11
    bonnie "I don’t regret it."
    bonnie "But what is  even worse, I still want more!"
    pc "Well, it looks like there are still a couple of boxes left."
    image bonnie_stage3_12 = "/bonnie/events/stage3/12.webp"
    scene bonnie_stage3_12
    bonnie "Ugh, I really shouldn't. I mean, look at me."
    pc "Everyone needs a little treat now and then, a cheat day."
    image bonnie_stage3_13 = "/bonnie/events/stage3/13.webp"
    scene bonnie_stage3_13
    bonnie "I suppose if I don’t do this again it should be ok. Just need to get it out of my system."
    "Walking over you pick up the last remaining two boxes of chocolates."
    image bonnie_stage3_14 = "/bonnie/events/stage3/14.webp"
    scene bonnie_stage3_14
    "Sitting next to Bonnie you begin to feed her the chocolates one by one."
    image bonnie_stage3_15 = "/bonnie/events/stage3/15.webp"
    scene bonnie_stage3_15
    "You can't help but notice her bulging belly, it looks even bigger when not covered by any clothes."
    "You wonder how many chocolates she has already eaten, how many she could eat if she really gave in."
    image bonnie_stage3_16 = "/bonnie/events/stage3/16.webp"
    scene bonnie_stage3_16
    "Now onto the last box Bonnie is physically starting to struggle, but seems determined to finish them all."
    image bonnie_stage3_17 = "/bonnie/events/stage3/17.webp"
    scene bonnie_stage3_17
    "You finish feeding her the remaining chocolates, a satisfied look on Bonnie's face."
    pc "I think that’s all of them."
    image bonnie_stage3_18 = "/bonnie/events/stage3/18.webp"
    scene bonnie_stage3_18
    bonnie "Oooh, I shouldn't have done that."
    image bonnie_stage3_19 = "/bonnie/events/stage3/19.webp"
    scene bonnie_stage3_19
    window hide
    pause
    image bonnie_stage3_20 = "/bonnie/events/stage3/20.webp"
    scene bonnie_stage3_20
    "Starting to collect all the empty boxes you notice Bonnie fall asleep once again on the couch."
    image bonnie_stage3_21 = "/bonnie/events/stage3/21.webp"
    scene bonnie_stage3_21
    "Her feeding frenzies too much for her to handle."
    image bonnie_stage3_22 = "/bonnie/events/stage3/22.webp"
    scene bonnie_stage3_22
    "Grabbing the ingredients from the store room, you begin to make this week's batch of chocolates for the shop."
    "You make sure to make a few extra and leave them on the counter for Bonnie later."

    scene outside2
    stop music fadeout 1.0
    "You walk back home after helping Bonnie up to her bed."
    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
        $ bonnie.weight += 1.0
    $ bonniestage3event = 0
    return

label Bonnie_Stage_4_Event:
    ### Scene image - In PC room scene like normal ###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("I need your help!", who=1)
    pause
    $ msg ("News about the chocolates coming back has brought all the customers back.", who=1)
    pause
    $ msg ("But there are so many here now we are running out.", who=1)
    pause
    $ msg ("Are you free to come and make some now? I'd owe you one.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "Not today.":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
    #[GAME – YES / Not tonight options]
    #IF YES

    ##### Scene image – Bonnie in front of shop like normal (Possible image with que?) ####
    image bonnie_stage4_1 = "/bonnie/events/stage4/1.webp"
    scene bonnie_stage4_1
    bonnie "Thank goodness you came."
    bonnie "As you can see your chocolates are a hit, but we are running out."
    pc "But I made dozens last week."
    bonnie "I… may have helped myself to some last night."
    bonnie "But I have all the ingredients ready for you to make more!"
    pc "Okay. I'll see what I can do."

    ##### Scene image – in kitchen without Bonnie ####
    image bonnie_stage4_2 = "/bonnie/events/stage4/2.webp"
    scene bonnie_stage4_2
    play music "/music/bonnie.ogg" if_changed
    "Grabbing the supplies Bonnie has left out for you, you begin to craft your delicious chocolates."
    image bonnie_stage4_3 = "/bonnie/events/stage4/3.webp"
    scene bonnie_stage4_3
    "Over the next couple of hours you churn out batch after batch."
    "Pulling out the latest batch they are quickly whisked away by Bonnie to be sold. The chocolates are being sold almost as fast as you can make them."
    "Bonnie wasn’t lying when she said these were the best sellers."
    image bonnie_stage4_4 = "/bonnie/events/stage4/4.webp"
    scene bonnie_stage4_4
    "You wonder just how many are being eaten around town. These sweet and fattening treats being consumed by people who have been hungry for them for weeks."

    ##### Scene image – Bonnie in kitchen normal clothes####
    image bonnie_stage4_5 = "/bonnie/events/stage4/5.webp"
    scene bonnie_stage4_5
    bonnie "And that is that."
    bonnie "We are officially closed for the day!"
    pc "Good. My arms were starting to get tired."
    image bonnie_stage4_6 = "/bonnie/events/stage4/6.webp"
    scene bonnie_stage4_6
    bonnie "I really appreciate you coming in today to help like this."
    bonnie "I see there are still a few extra batches left. Do you want to take them home with you?"
    image bonnie_stage4_7 = "/bonnie/events/stage4/7.webp"
    scene bonnie_stage4_7
    bonnie "Or maybe…you want to stick around and watch me eat them?"
    "Wait, had she found out about your interest?"
    pc "I..uh not sure what…"
    image bonnie_stage4_8 = "/bonnie/events/stage4/8.webp"
    scene bonnie_stage4_8
    bonnie "It's ok. You don’t have to hide it from me."
    bonnie "I make sweet treats for a living. It's not the first time I've come across this."
    image bonnie_stage4_9 = "/bonnie/events/stage4/9.webp"
    scene bonnie_stage4_9
    bonnie "Honestly, it's kind of a nice change. People have been telling me to be careful with how much I eat my whole life."
    pc "But I didn’t think you wanted to gain weight?"
    image bonnie_stage4_10 = "/bonnie/events/stage4/10.webp"
    scene bonnie_stage4_10
    bonnie "I didn’t but the more I have given into my eating desires, the better I’ve felt. So much less stressful."
    bonnie "I have always loved to eat sweets but I felt I needed to restrain myself from overindulging because of how other people might see it."
    image bonnie_stage4_11 = "/bonnie/events/stage4/11.webp"
    scene bonnie_stage4_11
    bonnie "Besides, I work in a sweet shop. If I gain a little, it's almost like a sign of how good the food is, if the person running the shop can't keep her hand out of the sweetie jar."
    pc "So you are not upset?"
    image bonnie_stage4_12 = "/bonnie/events/stage4/12.webp"
    scene bonnie_stage4_12
    bonnie "No. In fact, I'm happier than I have been in a while."
    bonnie "I spent too much time worrying about what other people want and not enough about what I want."
    pc "And what is it that you want?"
    image bonnie_stage4_13 = "/bonnie/events/stage4/13.webp"
    scene bonnie_stage4_13
    bonnie "To eat as much as I want, as much as I can!"
    image bonnie_stage4_14 = "/bonnie/events/stage4/14.webp"
    scene bonnie_stage4_14
    bonnie "And I think you would like that too…right?"
    pc "Absolutely, if you are sure?"
    image bonnie_stage4_15 = "/bonnie/events/stage4/15.webp"
    scene bonnie_stage4_15
    "As if to answer that question, Bonnie grabs a piece of chocolate from the latest batch and pops it into her mouth before moving over to the sofa."
    bonnie "Guess I won't be needing this."
    image bonnie_stage4_16 = "/bonnie/events/stage4/16.webp"
    scene bonnie_stage4_16
    "Bonnie begins to strip. She throws off her clothes, leaving her in just her underwear as she looks at you teasingly."

    ##### Scene image – Bonnie on sofa in underwear####
    image bonnie_stage4_17 = "/bonnie/events/stage4/17.webp"
    scene bonnie_stage4_17
    bonnie "It feels so good to finally give in."
    bonnie "Okay. Bring on the chocolates."
    pc "It's lucky I made a lot of extras, so you won't have to worry about the shop running out tomorrow."
    "Gathering up the chocolates you surround yourself with the sweet treats as Bonnie salivates at the mound of deliciousness."
    image bonnie_stage4_18 = "/bonnie/events/stage4/18.webp"
    scene bonnie_stage4_18
    "Picking up the first chocolate you hand it to Bonnie who pops it into her mouth."
    bonnie "Still as good as ever!"
    image bonnie_stage4_19 = "/bonnie/events/stage4/19.webp"
    scene bonnie_stage4_19
    "You start handing her chocolate after chocolate, each one gone in a single mouthful."
    "Even after the first two dozen disappear she doesn’t seem to slow down at all."
    image bonnie_stage4_20 = "/bonnie/events/stage4/20.webp"
    scene bonnie_stage4_20
    "But after the third box Bonnie looks to be having some trouble eating them at the same speed."
    "Not that it seems to be stopping her as she reaches out a hand for the next one."
    image bonnie_stage4_21 = "/bonnie/events/stage4/21.webp"
    scene bonnie_stage4_21
    bonnie "Ugh, think I'm starting to get full now."
    pc "You can handle a few more."
    image bonnie_stage4_22 = "/bonnie/events/stage4/22.webp"
    scene bonnie_stage4_22
    "Taking your words to heart she doubles down, continuing to stuff herself with the sweet treats."
    "Despite her comments about being full Bonnie sits there, accepting every chocolate you continue to offer to her."
    image bonnie_stage4_23 = "/bonnie/events/stage4/23.webp"
    scene bonnie_stage4_23
    "You can already see the impact they are having on her body."
    image bonnie_stage4_24 = "/bonnie/events/stage4/24.webp"
    scene bonnie_stage4_24
    "Her belly sticking out noticeably further than it was before you started."
    "As the fifth box is emptied Bonnie lets out another groan."
    image bonnie_stage4_25 = "/bonnie/events/stage4/25.webp"
    scene bonnie_stage4_25
    bonnie "Okay, that's it. I'm full."
    bonnie "But this feels so good."
    image bonnie_stage4_26 = "/bonnie/events/stage4/26.webp"
    scene bonnie_stage4_26
    "You watch as Bonnie gently caresses her stomach, almost admiring it for its size."
    pc "Wow, I didn’t think you would ever stop."
    image bonnie_stage4_27 = "/bonnie/events/stage4/27.webp"
    scene bonnie_stage4_27
    bonnie "Me either, but it seems even this giant stomach has a limit."
    bonnie "Although I bet you would like to see it get even bigger?"
    image bonnie_stage4_28 = "/bonnie/events/stage4/28.webp"
    scene bonnie_stage4_28
    "Leaning over Bonnie gives you a kiss on the cheek."
    image bonnie_stage4_29 = "/bonnie/events/stage4/29.webp"
    scene bonnie_stage4_29
    bonnie "Thank you for today, for both parts."
    pc "Anytime."
    image bonnie_stage4_30 = "/bonnie/events/stage4/30.webp"
    scene bonnie_stage4_30
    bonnie "Well, I can't think of a better business partner to help the shop and also help me live out my sweet dreams."
    bonnie "That is if you are still interested in working with and feeding me?"
    pc "Absolutely!"
    bonnie "In that case I would like to pay you for making chocolates from now on."
    if recollection == False:
        $ money += 10
    "You earned ten dollars."
    bonnie "It isn't much, but this is all I can afford with the shop currently."
    pc "Thank you."
    image bonnie_stage4_31 = "/bonnie/events/stage4/31.webp"
    scene bonnie_stage4_31
    bonnie "It seems we have made quite the mess."

    scene outside2
    stop music fadeout 1.0
    "Helping Bonnie clean up you say goodbye and head home."

    scene player_room
    "As you arrive back home, you feel your phone vibrating."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg (None, who=1, pic="stage4_bonnie")
    pause
    $ msg ("I think someone’s shrunk my underwear.", who=1)
    pause
    $ msg ("What do you think?", who=1)
    pause
    $ msg ("Looks good to me.")
    pause
    $ msg ("I’m sure it does.", who=1)
    pause
    $ msg ("Thanks again, it was nice to talk with you.", who=1)
    pause
    $ msg ("No problem, I’ll always be here if you need me.")
    pause
    $ msg ("That’s sweet, thanks!", who=1)
    pause
    $ hide_messenger()

    if recollection == False:
        $ daytime += 2
        $ phonecall = 1
        $ bonnie.weight += 1.0
    $ bonniestage4event = 0
    return


label Bonnie_Stage_5_Event:
    ### Scene image - In PC room scene like normal ###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("[playername], you have to come over. I need your help. It's an emergency!", who=1)
    pause
    $ msg ("The shop's freezer has packed up and all the food in it needs eat…moving.", who=1)
    pause
    menu:
        "I'll come over right away.":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "Not today.":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
    #[GAME – YES / Not tonight options]
    #IF YES

    ##### Scene image – Empty  front of shop####
    image bonnie_stage5_1 = "/bonnie/events/stage5/1.webp"
    scene bonnie_stage5_1
    "That's weird. Bonnie usually meets you out here."
    image bonnie_stage5_2 = "/bonnie/events/stage5/2.webp"
    scene bonnie_stage5_2
    pc "Bonnie, are you here?"
    bonnie "In here!"

    ##### Scene image – Bonnie’s house – Bonnie looking a little stuffed and in underwear sat on the floor####
    image bonnie_stage5_3 = "/bonnie/events/stage5/3.webp"
    scene bonnie_stage5_3
    play music "/music/bonnie.ogg" if_changed
    "Walking in the usually well organised room is a mess."
    "There are piles of boxes, containers and food everywhere."
    "Empty containers surround Bonnie as she chomps down on something."
    pc "What happened?"
    bonnie "The freezer broke. I’ve managed to move most of the essentials to the back up one, but it's not big enough for everything."
    pc "So what are you going to do with the rest of this?"
    bonnie "Well, I paid good money for it so I'm not going to waste it."
    pc "Do you need a hand moving it to another freezer somewhere else?"
    image bonnie_stage5_4 = "/bonnie/events/stage5/4.webp"
    scene bonnie_stage5_4
    bonnie "That’s not exactly what I was thinking…"
    "Taking the spoon out of the frozen yoghurt pot she was eating from Bonnie sucks on it while making eye contact with you."
    pc "You mean you are going to eat it?"
    image bonnie_stage5_5 = "/bonnie/events/stage5/5.webp"
    scene bonnie_stage5_5
    bonnie "Unless you have any other ideas?"
    "You are not sure you would say even if you did."
    pc "But why am I here?"
    bonnie "Well, I figured I might need some help and that you might be interested in that job."
    pc "Absolutely."
    image bonnie_stage5_6 = "/bonnie/events/stage5/6.webp"
    scene bonnie_stage5_6
    bonnie "Great. Now, grab some of those frozen chocolate delicacies. Can't let them melt."
    "Picking up the box she had pointed to, you are surprised by the weight of it."
    "Setting it on the floor next to her you hand her the first sweet."
    "The dense frozen treats filled with a slowly melting caramel inside."
    image bonnie_stage5_25 = "/bonnie/events/stage5/25.webp"
    scene bonnie_stage5_25
    bonnie "Mmmm, I don’t make these often enough. They are so good."
    "Quickly stuffing it into her mouth she seems to wince from the cold."
    image bonnie_stage5_26 = "/bonnie/events/stage5/26.webp"
    scene bonnie_stage5_26
    "Handing her another and then another she continues to eat."
    "By the tenth she is forced to pause."
    image bonnie_stage5_27 = "/bonnie/events/stage5/27.webp"
    scene bonnie_stage5_27
    bonnie "Oooh."
    pc "Brain freeze?"
    bonnie "I'm okay. Let's keep going."
    image bonnie_stage5_28 = "/bonnie/events/stage5/28.webp"
    scene bonnie_stage5_28
    "True to her word she begins to power through them."
    "The full box emptied in less than ten minutes of constant chewing and swallowing."
    image bonnie_stage5_29 = "/bonnie/events/stage5/29.webp"
    scene bonnie_stage5_29 with vpunch
    "Bonnie burps loudly."
    bonnie "Next!"
    "Wow, Bonnie was really enjoying letting herself loose like this."
    image bonnie_stage5_30 = "/bonnie/events/stage5/30.webp"
    scene bonnie_stage5_30
    "Grabbing another box of chocolate goodies you begin to feed her again."
    "One by one they disappear into Bonnie's stretching stomach."
    "Her chewing constant and mechanical as she beats back any discomfort from the cold desserts."
    image bonnie_stage5_31 = "/bonnie/events/stage5/31.webp"
    scene bonnie_stage5_31
    "Reaching for another box you keep the conveyor belt of food going."
    "Soon the empty boxes are beginning to pile up and outnumber the full ones."
    image bonnie_stage5_32 = "/bonnie/events/stage5/32.webp"
    scene bonnie_stage5_32
    "The effect on Bonnie's belly is easy to see as she crammed in the sweet and fattening treats."
    image bonnie_stage5_33 = "/bonnie/events/stage5/33.webp"
    scene bonnie_stage5_33
    "As you hand her the last treat you take a moment to admire her enlarged body."
    pc "Looks like that is it for these boxes."
    bonnie "Oooaah."
    image bonnie_stage5_20 = "/bonnie/events/stage5/20.webp"
    scene bonnie_stage5_20
    bonnie "There is still one more over there."
    "Pointing towards the counter in the far corner you spot a slightly old and giant box."
    "It seems to be filled with a dozen tubs of ice cream."
    pc "I think unfortunately it's already melted."
    image bonnie_stage5_21 = "/bonnie/events/stage5/21.webp"
    scene bonnie_stage5_21
    bonnie "That's okay. I'll drink it if I have to."
    "Looking at Bonnie's already stuffed belly you wonder how she could manage to eat all of this ice cream as well."
    "The label on the side reading “contains 144 servings”."
    pc "Isn’t it going to be a bit difficult with a spoon?"
    image bonnie_stage5_22 = "/bonnie/events/stage5/22.webp"
    scene bonnie_stage5_22
    bonnie "I have an idea."
    bonnie "Open that cupboard to your left. You should find it in there."
    "Opening the door you immediately see what she is after."
    image bonnie_stage5_23 = "/bonnie/events/stage5/23.webp"
    scene bonnie_stage5_23
    "A large funnel probably made for icing or filling piping bags sits there invitingly."
    bonnie "That’s the one."
    pc "Are you sure you can take this much?"
    image bonnie_stage5_24 = "/bonnie/events/stage5/24.webp"
    scene bonnie_stage5_24
    bonnie "I've always dreamt of putting my mouth under the ice cream machine and just letting it fill me."
    bonnie "This is just as good, or maybe even better."
    image bonnie_stage5_7 = "/bonnie/events/stage5/7.webp"
    scene bonnie_stage5_7
    "Handing her the large funnel she places it tightly into her mouth, not wanting to spill a drop."
    image bonnie_stage5_8 = "/bonnie/events/stage5/8.webp"
    scene bonnie_stage5_8
    pc "Here it comes."
    "Pouring the liquid ice cream down the funnel it quickly disappears into Bonnie."
    image bonnie_stage5_9 = "/bonnie/events/stage5/9.webp"
    scene bonnie_stage5_9
    "You watch as her already bloated stomach continues to swell with each mouthful."
    "The calorie rich cream is sure to leave a lasting impact on her waistline."
    "As the first pint of ice cream finishes being poured into her, Bonnie waves at you to get the next."
    "It seemed she had no intention of stopping now."
    image bonnie_stage5_10 = "/bonnie/events/stage5/10.webp"
    scene bonnie_stage5_10
    "One after another the pints are poured down."
    "Each one stuffing Bonnie even more and causing her once flat tummy to expand."
    image bonnie_stage5_11 = "/bonnie/events/stage5/11.webp"
    scene bonnie_stage5_11
    "By the twelfth pint you can barely believe the size of her gut."
    "It's hard to picture the once slim figure she had before today."
    image bonnie_stage5_12 = "/bonnie/events/stage5/12.webp"
    scene bonnie_stage5_12
    pc "Wow, I didn’t think you would be able to manage all of that."
    image bonnie_stage5_13 = "/bonnie/events/stage5/13.webp"
    scene bonnie_stage5_13 with vpunch
    "Bonnie burps loudly."
    image bonnie_stage5_14 = "/bonnie/events/stage5/14.webp"
    scene bonnie_stage5_14
    bonnie "Oooh, I don’t think I've ever been this full."
    image bonnie_stage5_15 = "/bonnie/events/stage5/15.webp"
    scene bonnie_stage5_15
    bonnie "My stomach, it's so big!"
    image bonnie_stage5_16 = "/bonnie/events/stage5/16.webp"
    scene bonnie_stage5_16
    "You watch as Bonnie fondles her giant belly, marvelling at its size."
    image bonnie_stage5_17 = "/bonnie/events/stage5/17.webp"
    scene bonnie_stage5_17
    bonnie "I'm so sleepy….think I'll just take a nap."
    image bonnie_stage5_18 = "/bonnie/events/stage5/18.webp"
    scene bonnie_stage5_18
    "As Bonnie tries to sleep off her overindulgence, you decided to clear up."
    "Grabbing the boxes you tidy up the wreckage of what had just happened."
    image bonnie_stage5_19 = "/bonnie/events/stage5/19.webp"
    scene bonnie_stage5_19
    "But grabbing one of the ice cream tubs you notice something stuck to the bottom of it."
    "Inspecting the torn page it seems to be one of the missing ones from Bonnie's partner's notebook."
    "It seems to describe a new recipe they were trying out, an even more delicious and fattening one."
    "Somehow it must have gotten stuck in the old box Bonnie used to store the ice creams."
    "Putting it into your pocket, you make a mental note to try these out when making Bonnie's next batch of chocolates."
    "With the house tidy you let yourself out and head home."

    scene outside2
    stop music fadeout 1.0
    "Wow, that was super hot."
    "Bonnie seems to have really given in to eating what she wants, which is apparently a lot."
    "She was surely going to start packing on the pounds if she kept going like this."
    if recollection == False:
        $ bonnie.weight += 1
        $ daytime += 1
        $ phonecall = 1
    $ bonniestage5event = 0
    return


label Bonnie_Stage_6_Event:
    ### Scene image - In PC room scene like normal ###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("Hey! You free to make some more of those amazing chocolates today?", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "Not today.":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
    #[GAME – YES / Not tonight options]
    #IF YES

    ##### Scene image – Bonnie next to counter in underwear and apron ####
    image cafe_bonnie_home_cooking1_event6 = "/bonnie/6/cooking1.webp"
    scene cafe_bonnie_home_cooking1_event6
    play music "/music/bonnie.ogg" if_changed
    "Grabbing a pan, you begin to prepare the chocolates."
    bonnie "The customers are excited to have these chocolates again."
    pc "That’s good to hear."
    bonnie "I still don’t know how you did it."
    pc "Here, the first ones are ready if you want to taste them."
    image bonnie_stage6_1 = "/bonnie/events/stage6/1.webp"
    scene bonnie_stage6_1
    "Bonnie quickly takes the chocolate from you, chewing slowly to savour the flavour."
    "Starting on the next batches you continue to hand her tasters."
    image bonnie_stage6_2 = "/bonnie/events/stage6/2.webp"
    scene bonnie_stage6_2
    "Each one she takes gleefully, the both of you enjoying your working relationship."
    image cafe_bonnie_home_finishedcooking_event6 = "/bonnie/6/finishedcooking.webp"
    scene cafe_bonnie_home_finishedcooking_event6
    "After a couple of hours the room is filled with chocolates to satisfy Bonnie's customers for the next week. Plus a few extra you have put aside or fed to your assistant."
    bonnie "I think that should do. Besides, you have earned a break."
    pc "Actually, I’ve been working on another recipe if you wanted to try it?"
    bonnie "Would I ever say no to more chocolates?"
    image cafe_bonnie_home_cooking2_event6 = "/bonnie/6/cooking2.webp"
    scene cafe_bonnie_home_cooking2_event6
    "Following the recipe you found on that loose piece of paper during Bonnie's ice cream binge you start to create the new deluxe chocolate fudge bombs."
    "Tipping in double the amount of sugar and double cream into the mixture, these are sure to be a lot more unhealthy than the normal chocolates."
    image cafe_bonnie_home_cooking3_event6 = "/bonnie/6/cooking3.webp"
    scene cafe_bonnie_home_cooking3_event6
    "You wonder if Bonnie's customers would mind."
    "Carefully drizzling the white chocolate pattern over the top you are pleased to see the new slightly larger chocolates look just as good as the others."
    image bonnie_stage6_3 = "/bonnie/events/stage6/3.webp"
    scene bonnie_stage6_3
    pc "Here, Bonnie. You can be the first official taste tester of these new chocolates."
    bonnie "It would be my honour."
    image bonnie_stage6_4 = "/bonnie/events/stage6/4.webp"
    scene bonnie_stage6_4
    "Taking the chocolate from you Bonnie gives it a once over before taking big bite out of it."
    image bonnie_stage6_5 = "/bonnie/events/stage6/5.webp"
    scene bonnie_stage6_5
    "Immediately her eyes light up."
    bonnie "Wow, these are even better than the regular ones!"
    image bonnie_stage6_6 = "/bonnie/events/stage6/6.webp"
    scene bonnie_stage6_6
    "Without even asking she grabs another from the tray, closing her eyes as she savours the flavour."
    bonnie "So good!"
    image bonnie_stage6_7 = "/bonnie/events/stage6/7.webp"
    scene bonnie_stage6_7
    "You can tell she is trying to control herself, eyeing the rest of the tray hungrily."
    pc "They might be a little bit more unhealthy than the usual ones."
    bonnie "Uh huh."
    "With her eyes fixed on the chocolates it's clear Bonnie isn’t really paying attention."
    pc "I don’t know if you would need to tell your customers not to eat too many?"
    "Getting no reply, you can see Bonnie licking her lips with her attention fully on the chocolates."
    pc "Bonnie?"
    image bonnie_stage6_8 = "/bonnie/events/stage6/8.webp"
    scene bonnie_stage6_8
    bonnie "I, sorry."
    bonnie "Are they for the customers?"
    pc "No, I just wanted to test them this week and see if you approved?"
    image bonnie_stage6_9 = "/bonnie/events/stage6/9.webp"
    scene bonnie_stage6_9
    bonnie "So, I can eat them?"
    pc "Sure."
    image bonnie_stage6_10 = "/bonnie/events/stage6/10.webp"
    scene bonnie_stage6_10
    "Throwing herself at them Bonnie begins to devour the fattening chocolates."
    "Shoveling them into her mouth a handful at a time she chews them aggressively."
    image bonnie_stage6_11 = "/bonnie/events/stage6/11.webp"
    scene bonnie_stage6_11
    "It seems like she is desperate to get as many of them into her mouth and belly as possible."
    "In less than a minute the tray is empty, Bonnie having rapidly stuffed herself with them all."
    image bonnie_stage6_12 = "/bonnie/events/stage6/12.webp"
    scene bonnie_stage6_12
    bonnie "More, there has to be more?"
    image bonnie_stage6_13 = "/bonnie/events/stage6/13.webp"
    scene bonnie_stage6_13
    "Pointing over to the two additional trays you smile as Bonnie rushes over."
    image bonnie_stage6_14 = "/bonnie/events/stage6/14.webp"
    scene bonnie_stage6_14
    "It seems she has completely lost control of herself, the power of the chocolates too much for her to fight."
    image bonnie_stage6_15 = "/bonnie/events/stage6/15.webp"
    scene bonnie_stage6_15
    "Especially since she had already admitted to giving in and eating anything and everything she wanted."
    "Looking over Bonnie is already almost through the first dozen."
    image bonnie_stage6_16 = "/bonnie/events/stage6/16.webp"
    scene bonnie_stage6_16
    "Her belly hanging under her as she continues to stuff mouthfuls of chocolates into her waiting mouth."
    image bonnie_stage6_17 = "/bonnie/events/stage6/17.webp"
    scene bonnie_stage6_17
    "In record time she demolished almost three dozen of the new fattening chocolates."
    image bonnie_stage6_18 = "/bonnie/events/stage6/18.webp"
    scene bonnie_stage6_18
    pc "I take it you approve."
    bonnie "Sorry, they are so good. I just couldn’t control myself."
    image bonnie_stage6_19 = "/bonnie/events/stage6/19.webp"
    scene bonnie_stage6_19
    bonnie "No wonder I’ve been gaining all this extra weight."
    image bonnie_stage6_20 = "/bonnie/events/stage6/20.webp"
    scene bonnie_stage6_20
    bonnie "Although I doubt you mind?"
    "Rubbing her enlarged belly Bonnie looks you in the eyes, enjoying the look of appreciation after her stuffing display."
    image bonnie_stage6_21 = "/bonnie/events/stage6/21.webp"
    scene bonnie_stage6_21
    bonnie "Maybe we keep these new chocolates just between us for now?"
    pc "Sure, whatever you want."
    "After helping Bonnie clean up you head home."

    scene outside2
    stop music fadeout 1.0
    "Wow, Bonnie really seemed to like those chocolates."
    "Maybe they are a bit too addictive?"
    if recollection == False:
        $ daytime += 1
        $ bonnie.weight += 1
        $ phonecall = 1
    $ bonniestage6event = 0
    return


label Bonnie_Stage_7_Event_1:
    ### Scene image - In PC room scene like normal ###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("Hey, [playername]. I was wondering if you would be able to help me with something today?", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "Not today.":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
    #[GAME – YES / Not tonight options]
    #IF YES

    ##### Scene image – Bonnie in casual wear in front of shop ####
    image cafe_bonnie_home_outside_event7 = "/bonnie/7/home_outside.webp"
    scene cafe_bonnie_home_outside_event7
    bonnie "Hey, [playername]. I’ve closed the shop early for the day."
    bonnie "I could do with some of that chocolate making magic."
    pc "Sure, what do you need?"
    image bonnie_stage7_1 = "/bonnie/events/stage7/1.webp"
    scene bonnie_stage7_1
    bonnie "I'm supposed to be catering for an exclusive event next week."
    bonnie "But they have some specific requests that I'm not super confident on."
    bonnie "Do you think you could help me like you were doing before by helping me with the recipe and taste testing some options?"
    pc "Of course, happy to help."
    image bonnie_stage7_2 = "/bonnie/events/stage7/2.webp"
    scene bonnie_stage7_2
    "Bonnie smiles at you."

    ##### Scene image – Bonnie in the kitchen ‘#####
    image cafe_bonnie_home_showkitchen_event7 = "/bonnie/7/home_showkitchen.webp"
    scene cafe_bonnie_home_showkitchen_event7
    play music "/music/bonnie.ogg" if_changed
    bonnie "So, they are after a whole bunch of things - most of which I have already figured out."
    bonnie "The main one I'm still trying to figure out is the chocolate liqueurs."
    pc "Chocolate liqueurs?"
    image bonnie_stage7_3 = "/bonnie/events/stage7/3.webp"
    scene bonnie_stage7_3
    bonnie "Yes. It's an alcoholic chocolate that is typically made with a spirit like whiskey."
    bonnie "One thing to keep in mind is it will need more sweetness to balance it out."
    pc "Sure, I can try that."
    "Grabbing the ingredients you begin to prepare the chocolates."
    image bonnie_stage7_50 = "/bonnie/events/stage7/50.webp"
    scene bonnie_stage7_50
    "You have never made these before, but how hard can it be?"
    "Following the new more fattening and sweeter recipe you begin to construct the chocolate shells."
    image bonnie_stage7_4 = "/bonnie/events/stage7/4.webp"
    scene bonnie_stage7_4
    pc "Bonnie, those are not done yet."
    bonnie "Sorry. They just look so good."
    image bonnie_stage7_51 = "/bonnie/events/stage7/51.webp"
    scene bonnie_stage7_51
    "Mixing the chocolate ganache, liquor and heavy cream you whisk it into an alcoholic filling."
    "Carefully piping it into each of the chocolates you apply a thin layer of new chocolate to cover the hole."
    "You probably only really needed to make one, but it's so hard to get the right ratio with such small quantities."
    "Besides, you have a feeling Bonnie won't mind a few extras to keep herself busy between batches."
    image bonnie_stage7_5 = "/bonnie/events/stage7/5.webp"
    scene bonnie_stage7_5
    pc "Okay, the first batch is ready. Let me know what you think."
    image bonnie_stage7_6 = "/bonnie/events/stage7/6.webp"
    scene bonnie_stage7_6
    "Taking the chocolate from you Bonnie pops it into her mouth."
    bonnie "MMmmm."
    bonnie "It's really good."
    image bonnie_stage7_7 = "/bonnie/events/stage7/7.webp"
    scene bonnie_stage7_7
    "Despite that she seems deep in thought for a moment."
    bonnie "Maybe it's slightly too bitter."
    pc "Well, in that case, you may as well have these."
    image bonnie_stage7_8 = "/bonnie/events/stage7/8.webp"
    scene bonnie_stage7_8
    "You see a smile come across her face as she gleefully accepts the now unwanted chocolates."
    image bonnie_stage7_14 = "/bonnie/events/stage7/14.webp"
    scene bonnie_stage7_14
    "Okay, Bonnie said that it was too bitter. What's the best way to counteract that?"
    menu:
        "Add Sugar":
            "You add more sugar to the mixture."
        "Add Cream":
            "You add more cream to the mixture."
        "Add Liquor":
            "You add more liquor to the mixture."
        "Add Cocoa":
            "You add more cocoa to the mixture."
    "Stirring the new mixture, you hope that adding more has helped make it less bitter."
    "Although part of you doesn’t want to get it right yet, the longer it takes the more time you get to spend with Bonnie."
    "Piping the mixture into the next batch you wait for them to set before calling Bonnie over."
    pc "Any better?"
    image bonnie_stage7_9 = "/bonnie/events/stage7/9.webp"
    scene bonnie_stage7_9
    "Taking the new chocolate Bonnie pops it into her mouth, taking a moment to consider its flavour again."
    image bonnie_stage7_10 = "/bonnie/events/stage7/10.webp"
    scene bonnie_stage7_10
    bonnie "It's good, but maybe a little soft this time. Don’t want them melting before anyone can eat them."
    pc "Sure thing. I can work on that."
    image bonnie_stage7_15 = "/bonnie/events/stage7/15.webp"
    scene bonnie_stage7_15
    "Once again she grabs the tray of extra chocolates that she takes happily."
    image bonnie_stage7_14 = "/bonnie/events/stage7/14.webp"
    scene bonnie_stage7_14
    "Okay, Bonnie said that it was too soft. Maybe I should try adding something that isn't liquid?"
    menu:
        "Add Sugar":
            "You add more sugar to the mixture."
        "Add Cream":
            "You add more cream to the mixture."
        "Add Liquor":
            "You add more liquor to the mixture."
        "Add Cocoa":
            "You add more cocoa to the mixture."
    "Stirring the new mixture, you wonder if this will make it any better."
    "Piping the mixture into the next batch you wait for them to set before calling Bonnie over."
    pc "Any better?"
    image bonnie_stage7_17 = "/bonnie/events/stage7/17.webp"
    scene bonnie_stage7_17
    "Taking the new chocolate Bonnie pops it into her mouth, taking a moment to consider its flavour again."
    image bonnie_stage7_11 = "/bonnie/events/stage7/11.webp"
    scene bonnie_stage7_11
    bonnie "It's good, but maybe a little dark this time."
    pc "Sure thing. I can work on that."
    image bonnie_stage7_16 = "/bonnie/events/stage7/16.webp"
    scene bonnie_stage7_16
    "Once again she grabs the tray of extra chocolates that she takes happily."
    image bonnie_stage7_14 = "/bonnie/events/stage7/14.webp"
    scene bonnie_stage7_14
    "Okay, Bonnie said that it was too dark. That probably means there is too much cocoa?"
    menu:
        "Add Sugar":
            "You add more sugar to the mixture."
        "Add Cream":
            "You add more cream to the mixture."
        "Add Liquor":
            "You add more liquor to the mixture."
        "Add Cocoa":
            "You add more cocoa to the mixture."
    "Stirring the new mixture, you wonder if this will make it any better."
    "Piping the mixture into the next batch you wait for them to set before calling Bonnie over."
    pc "Any better?"
    image bonnie_stage7_19 = "/bonnie/events/stage7/19.webp"
    scene bonnie_stage7_19
    "Taking the new chocolate Bonnie pops it into her mouth, taking a moment to consider its flavour again."
    image bonnie_stage7_12 = "/bonnie/events/stage7/12.webp"
    scene bonnie_stage7_12
    bonnie "It's good, but maybe a little sweet this time?"
    pc "Sure thing. I can work on that."
    image bonnie_stage7_20 = "/bonnie/events/stage7/20.webp"
    scene bonnie_stage7_20
    "Once again Bonnie reaches out to the tray of extra chocolates."
    "But unlike the previous times, Bonnie doesn't look too eager to grab it."
    "It's clear that even Bonnie is starting to struggle under the weight of the chocolates she is consuming."
    pc "Everything ok?"
    image bonnie_stage7_21 = "/bonnie/events/stage7/21.webp"
    scene bonnie_stage7_21
    bonnie "Yeah! Why wouldn't it be?"
    "Taking the chocolates she tries to play it off and pretends to eagerly chew one of them."
    image bonnie_stage7_14 = "/bonnie/events/stage7/14.webp"
    scene bonnie_stage7_14
    "Okay, Bonnie said that it was too sweet. Maybe I should try balancing that out. But how?"
    menu:
        "Add Sugar":
            "You add more sugar to the mixture."
        "Add Cream":
            "You add more cream to the mixture."
        "Add Liquor":
            "You add more liquor to the mixture."
        "Add Cocoa":
            "You add more cocoa to the mixture."
    "Stirring the new mixture, you wonder if this will make it any better."
    "Piping the mixture into the next batch you wait for them to set before calling Bonnie over."
    image bonnie_stage7_23 = "/bonnie/events/stage7/23.webp"
    scene bonnie_stage7_23
    "But looking over to the couch where Bonnie is sat you can see she has only just finished the last batch."
    image bonnie_stage7_24 = "/bonnie/events/stage7/24.webp"
    scene bonnie_stage7_24
    "Standing with a bit of difficulty due to her expanded body she comes over, still smiling."
    pc "How are these?"
    image bonnie_stage7_18 = "/bonnie/events/stage7/18.webp"
    scene bonnie_stage7_18
    "Taking the new chocolate Bonnie pops it into her mouth, taking a moment to consider its flavour again."
    image bonnie_stage7_13 = "/bonnie/events/stage7/13.webp"
    scene bonnie_stage7_13
    bonnie "It's good, but maybe a little soft again."
    pc "Sure thing. I can work on that."
    image bonnie_stage7_22 = "/bonnie/events/stage7/22.webp"
    scene bonnie_stage7_22
    "Once again Bonnie seems to pause before accepting the tray from you."
    image bonnie_stage7_14 = "/bonnie/events/stage7/14.webp"
    scene bonnie_stage7_14
    "Okay, Bonnie said that it was too soft. Maybe I should try adding something that isn't liquid?"
    menu:
        "Add Sugar":
            "You add more sugar to the mixture."
        "Add Cream":
            "You add more cream to the mixture."
        "Add Liquor":
            "You add more liquor to the mixture."
        "Add Cocoa":
            "You add more cocoa to the mixture."
    "Stirring the new mixture, you wonder if this will make it any better."
    "Piping the mixture into the next batch you wait for them to set before calling Bonnie over."
    image bonnie_stage7_25 = "/bonnie/events/stage7/25.webp"
    scene bonnie_stage7_25
    "Looking over at her you can see she is still eating the last batch, her pace getting slower and slower as she filled up."
    image bonnie_stage7_26 = "/bonnie/events/stage7/26.webp"
    scene bonnie_stage7_26
    "While Bonnie is walking over you admire her body for a second."
    image bonnie_stage7_27 = "/bonnie/events/stage7/27.webp"
    scene bonnie_stage7_27
    bonnie "Ugh, I'm so full."
    pc "I told you not to fill up before we found the right ones."
    image bonnie_stage7_28 = "/bonnie/events/stage7/28.webp"
    scene bonnie_stage7_28
    bonnie "Do you think you can help me with this belt?"
    image bonnie_stage7_29 = "/bonnie/events/stage7/29.webp"
    scene bonnie_stage7_29
    "Nervously you walk over, helping undo the belt restricting Bonnie's growing gut."
    bonnie "Ahhh."
    image bonnie_stage7_30 = "/bonnie/events/stage7/30.webp"
    scene bonnie_stage7_30
    "The relief is obvious as she stands."
    image bonnie_stage7_31 = "/bonnie/events/stage7/31.webp"
    scene bonnie_stage7_31
    "Facing away from you, she lets her clothes fall to the floor."
    "You watch as she steps out of her clothes, leaving her completely naked in front of you for the first time."
    image bonnie_stage7_32 = "/bonnie/events/stage7/32.webp"
    scene bonnie_stage7_32
    window hide
    pause
    "You can't help but stare at her supple body."
    image bonnie_stage7_33 = "/bonnie/events/stage7/33.webp"
    scene bonnie_stage7_33
    window hide
    pause
    bonnie "That should have made some room."
    bonnie "But I still think I’m going to need some help eating the rest of them."
    image bonnie_stage7_34 = "/bonnie/events/stage7/34.webp"
    scene bonnie_stage7_34
    window hide
    pause
    "Sitting back down, she invites you to feed her the new chocolates."
    image bonnie_stage7_35 = "/bonnie/events/stage7/35.webp"
    scene bonnie_stage7_35
    window hide
    pause
    "Leaning back she opens her mouth invitingly as you gently place a chocolate inside it."
    image bonnie_stage7_36 = "/bonnie/events/stage7/36.webp"
    scene bonnie_stage7_36
    window hide
    pause
    "Moments later it's gone and her mouth is open once again, waiting for the next one."
    image bonnie_stage7_37 = "/bonnie/events/stage7/37.webp"
    scene bonnie_stage7_37
    window hide
    pause
    "One after another the chocolates disappear down her seductive mouth."
    image bonnie_stage7_38 = "/bonnie/events/stage7/38.webp"
    scene bonnie_stage7_38
    "Unable to look away you stick out a hand to get the next one, only to find the tray empty."
    pc "I'm sorry. I think that's...."
    image bonnie_stage7_39 = "/bonnie/events/stage7/39.webp"
    scene bonnie_stage7_39
    "You are interrupted as Bonnie leans forwards, planting her lips on yours."
    window hide
    pause
    if persistent.nosexscene == True:
        scene black with dissolve
        "Bonnie and I had a great time together."
        pc "But what about the chocolates?"
        image bonnie_stage7_40 = "/bonnie/events/stage7/40.webp"
        scene bonnie_stage7_40
        bonnie "Oh, don't worry. You had the recipe right on the first try."
        pc "Then why test them all?"
        image bonnie_stage7_41 = "/bonnie/events/stage7/41.webp"
        scene bonnie_stage7_41
        bonnie "I needed an excuse to get you to feed me."
        "Leaving Bonnie to sleep it off you manage to find enough ingredients to make another few batches of chocolates."
        "One regular for the shop, the delux for Bonnie and the Liqour chocolates or her event."
        "Unless she was lying about that too?"
        stop music fadeout 1.0

        scene player_room
        "Later that night you receive a message from Bonnie."

        $ show_messenger()

        $ dialogue_one = []

        $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
        $ msg (None, who=1, pic="stage7_bonnie1")
        pause
        $ msg ("Thank you for coming over today, sorry for tricking you again.", who=1)
        pause
        $ msg ("I’m still so bloated!", who=1)
        pause
        $ msg ("No need to apologise for tricking me, it was for a good cause.")
        pause
        $ msg ("Mmm, making me fat?", who=1)
        pause
        $ msg ("Exactly.")
        pause
        $ msg ("Maybe…we could do it again sometime.", who=1)
        pause
        $ msg ("Definitely.")
        pause
        $ hide_messenger()

        $ bonniestage7event = 0
        if recollection == False:
            $ daytime += 1
            $ phonecall = 1
            $ bonnie.weight += 1
            #Unlocks Bonnie Undress in the stats page.
            $ renpy.notify("Bonnie Undress option unlocked in stats screen.")
            window hide
            pause
        return

    #[Sex scene] – Will leave this to you.
    "After the passionate kiss, Bonnie slowly takes off your shirt and pants, revealing your hard cock to her for the first time."
    bonnie "It looks like you were waiting for this moment."
    image bonnie_stage7_42 = "/bonnie/events/stage7/42.webp"
    scene bonnie_stage7_42
    "Bonnie moves over to you, planting her big ass on your lap."
    "While her wet pussy slowly envelops your hard cock, you decide to feel her soft breasts."
    window hide
    pause
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/bonnie/events/stage7/43.webm" loop
    show movie with dissolve
    pause
    "After Bonnie gets used to the feeling of having you inside her, you start to thrust your hips up and down."
    "It is clear that Bonnie enjoys the interaction as she slowly starts pushing her hips into you a little bit more with each additional thrust."
    stop movie
    image bonnie_stage7_44 = "/bonnie/events/stage7/44.webp"
    scene bonnie_stage7_44
    bonnie "Let me take the lead."
    "More than happy to comply, you lie down and let Bonnie sit on top of you."
    "She looks you in the eyes while slowly lowering her body onto your cock."
    window hide
    pause
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/bonnie/events/stage7/45.webm" loop
    show movie with dissolve
    pause
    bonnie "Oh! My! God! This feels so good!"
    "Bonnie screams in pleasure while she lifts her hips up and down."
    "The following moments are filled with incredibly hot sex with the woman of your dreams."
    stop movie
    image bonnie_stage7_46 = "/bonnie/events/stage7/48.webp"
    scene bonnie_stage7_46
    bonnie "Can you take over, babe? This growing body of mine is getting a bit tired."
    "You help Bonnie on her feet, taking the opportunity to feel her fat stuffed belly and soft tits."
    "While playing with her round belly you insert you penis into her soaking wet pussy."
    window hide
    pause
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/bonnie/events/stage7/49.webm" loop
    show movie with dissolve
    pause
    "The following moments can only be described as a dream come true."
    "The wonderful feeling of playing with a growing fat belly while having sex did it, ending with a euphoric explosion of cum inside of her."
    stop movie
    image bonnie_stage7_48 = "/bonnie/events/stage7/46.webp"
    scene bonnie_stage7_48
    bonnie "Don't worry, I'm on the pill. Come help me finish too."
    "You lift up Bonnie's legs while she balances her upper body with her arms."
    "Wanting to pleasure your partner, you decide to make her finish with your mouth."
    window hide
    pause
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/bonnie/events/stage7/47.webm" loop
    show movie with dissolve
    pause
    "While licking her clitoris Bonnie begins to loudly moan and push her body into you."
    "Moments later the moans turn to screams and her legs begin to shake and clamp your head while your partner also reaches her climax."
    bonnie "Oh, OHH, OOOHHHHHH, YEAH!"
    stop movie
    ###After sex scene###
    image bonnie_stage7_52 = "/bonnie/events/stage7/52.webp"
    scene bonnie_stage7_52
    "You slowly put Bonnie back down on the couch."
    bonnie "That was amazing! I don't think I've ever had sex that great before."
    pc "Couldn't agree more. We really should do this more often."
    image bonnie_stage7_53 = "/bonnie/events/stage7/53.webp"
    scene bonnie_stage7_53
    "Bonnie slowly regains her senses."
    bonnie "Yeah. This is probably just as addicting as those chocolates."
    image bonnie_stage7_54 = "/bonnie/events/stage7/54.webp"
    scene bonnie_stage7_54
    pc "I would say it's even more addicting."
    bonnie "Having sex with a belly full of chocolates is something I didn't expect to be doing."
    bonnie "But I'm glad I did."
    image bonnie_stage7_40 = "/bonnie/events/stage7/40.webp"
    scene bonnie_stage7_40
    pc "But what about the chocolates?"
    bonnie "Oh, don't worry. You had the recipe right on the first try."
    pc "Then why test them all?"
    image bonnie_stage7_41 = "/bonnie/events/stage7/41.webp"
    scene bonnie_stage7_41
    bonnie "I needed an excuse to get you to feed me."
    "Leaving Bonnie to sleep it off you manage to find enough ingredients to make another few batches of chocolates."
    "One regular for the shop, the deluxe for Bonnie and the Liqour chocolates for her event."
    "Unless she was lying about that too?"
    stop music fadeout 1.0

    scene player_room
    "Later that night you receive a message from Bonnie."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg (None, who=1, pic="stage7_bonnie1")
    pause
    $ msg ("The sex was amazing, sorry for tricking you again.", who=1)
    pause
    $ msg ("I’m still so bloated!", who=1)
    pause
    $ msg ("No need to apologise for tricking me, it was for a good cause.")
    pause
    $ msg ("Mmm, making me fat?", who=1)
    pause
    $ msg ("Exactly.")
    pause
    $ msg ("Maybe…we could do it again sometime.", who=1)
    pause
    $ msg ("Definitely.")
    pause
    $ hide_messenger()

    $ bonniestage7event = 0
    if recollection == False:
        $ bonnie.weight += 1
        $ daytime += 1
        $ phonecall = 1
        #Unlocks Bonnie Undress in the stats page.
        $ renpy.notify("Bonnie Undress option unlocked in stats screen.")
        window hide
        pause
    return

label Bonnie_Stage_7_Event_2:
    ###Bonnie stage 7 sex event###
    ###At your house###
    scene player_room
    "As you are about to get ready for bed, you feel your phone vibrate."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("Hi, I just wanted to say thank you for the other night. It was incredible.", who=1)
    pause
    $ msg ("No need to thank me, I had fun too.")
    pause
    $ msg ("Oh, I wasn't sure you would still be up.", who=1)
    pause
    $ msg ("I've been thinking about that night a lot lately...", who=1)
    pause
    "You notice the three dots coming up and going again, as if she is unsure of what to say next."
    pause
    $ msg (None, who=1, pic="stage7_bonnie3")
    pause
    $ msg ("Do you think this outfit makes my ass look big?", who=1)
    pause
    $ msg ("It looks perfect.")
    pause
    $ msg ("What about the rest of me?", who=1)
    pause
    $ msg (None, who=1, pic="stage7_bonnie2")
    pause
    $ msg ("All of you is perfect.")
    pause
    $ msg ("Perfect, so you wouldn't change anything?", who=1)
    pause
    $ msg ("Not even to make me bigger?", who=1)
    pause
    $ msg ("You know what I like.")
    pause
    $ msg ("And what I like is you!", who=1)
    pause
    $ msg ("I know it is getting late but would you maybe, want to come over tonight?", who=1)
    pause
    $ msg ("I’ll make it worth your while.", who=1)
    pause
    $ msg (None, who=1, pic="stage7_bonnie4")
    pause
    $ msg ("I’ll be right there!")
    pause
    $ hide_messenger()

    scene city_night
    "Grabbing a coat, you barely remember to lock the door as you rush over to Bonnie's shop."
    "Knocking the door, you hear a bustle of activity on the other side before it opens."
    image bonnie_stage7_55 = "/bonnie/events/stage7/55.webp"
    scene bonnie_stage7_55
    bonnie "Oh, I thought you were someone else."
    bonnie "Why didn’t you just come in?"
    pc "Expecting someone else, how many mysterious suitors do you have?"
    bonnie "Maybe, but it is something we can both enjoy."
    image bonnie_stage7_56 = "/bonnie/events/stage7/56.webp"
    scene bonnie_stage7_56
    "Bonnie goes in for a hug."
    image bonnie_stage7_57 = "/bonnie/events/stage7/57.webp"
    scene bonnie_stage7_57
    bonnie "But right now, I want to enjoy something else."
    image bonnie_stage7_58 = "/bonnie/events/stage7/58.webp"
    scene bonnie_stage7_58
    "Leading you back towards her bedroom, you can see the excitement in her face."
    image bonnie_stage7_59 = "/bonnie/events/stage7/59.webp"
    scene bonnie_stage7_59
    "Stripping off her coat, Bonnie reveals the outfit she was teasing you with earlier."
    image bonnie_stage7_60 = "/bonnie/events/stage7/60.webp"
    scene bonnie_stage7_60
    window hide
    pause
    image bonnie_stage7_61 = "/bonnie/events/stage7/61.webp"
    scene bonnie_stage7_61
    pause
    image bonnie_stage7_62 = "/bonnie/events/stage7/62.webp"
    scene bonnie_stage7_62
    pause
    image bonnie_stage7_63 = "/bonnie/events/stage7/63.webp"
    scene bonnie_stage7_63
    bonnie "Now you are seeing it in person, what do you think?"
    pc "I can barely think, seeing you looking like that."
    bonnie "Mmm, oh yeah?"
    image bonnie_stage7_64 = "/bonnie/events/stage7/64.webp"
    scene bonnie_stage7_64
    bonnie "I bet you just want to bury your face in my giant boobs, right?"
    image bonnie_stage7_65 = "/bonnie/events/stage7/65.webp"
    scene bonnie_stage7_65
    bonnie "No need to be shy."
    image bonnie_stage7_66 = "/bonnie/events/stage7/66.webp"
    scene bonnie_stage7_66
    "Pulling you into her, you kiss passionately."
    image bonnie_stage7_67 = "/bonnie/events/stage7/67.webp"
    scene bonnie_stage7_67
    window hide
    pause
    image bonnie_stage7_68 = "/bonnie/events/stage7/68.webp"
    scene bonnie_stage7_68
    "Your hands exploring each other as you feel the heat radiating off her body."
    image bonnie_stage7_69 = "/bonnie/events/stage7/69.webp"
    scene bonnie_stage7_69
    "Pulling you closer she presses your face against her soft and voluptuous breasts."
    image bonnie_stage7_70 = "/bonnie/events/stage7/70.webp"
    scene bonnie_stage7_70
    window hide
    pause
    image bonnie_stage7_71 = "/bonnie/events/stage7/71.webp"
    scene bonnie_stage7_71
    bonnie "Mmm, I want you!"
    image bonnie_stage7_72 = "/bonnie/events/stage7/72.webp"
    scene bonnie_stage7_72
    "Gently you manoeuvre her and let Bonnie fall onto the bed."
    image bonnie_stage7_73 = "/bonnie/events/stage7/73.webp"
    scene bonnie_stage7_73
    window hide
    pause
    image bonnie_stage7_74 = "/bonnie/events/stage7/74.webp"
    scene bonnie_stage7_74
    "The sudden movement catching her off guard, but the grinning face looking back at you telling you she enjoyed it."
    bonnie "I like it when you take charge like that."
    bonnie "Now, I need you to rip these clothes off me!"
    image bonnie_stage7_75 = "/bonnie/events/stage7/75.webp"
    scene bonnie_stage7_75
    "Stretching her top, you pull it under her weight bust, revealing her perfect tits."
    image bonnie_stage7_76 = "/bonnie/events/stage7/76.webp"
    scene bonnie_stage7_76
    window hide
    pause
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/bonnie/events/stage7/boobplay.webm" loop
    show movie with dissolve
    window hide
    pause
    "You allow yourself to play around with her soft bouncy breasts."
    bonnie "I bet you would love it if they were to grow a few cups larger."
    pc "You know I would."
    stop movie
    image bonnie_stage7_77 = "/bonnie/events/stage7/77.webp"
    scene bonnie_stage7_77
    "Grabbing the bottom half, you caress her before pulling open her tight bodysuit."
    image bonnie_stage7_78 = "/bonnie/events/stage7/78.webp"
    scene bonnie_stage7_78
    window hide
    pause
    image bonnie_stage7_79 = "/bonnie/events/stage7/79.webp"
    scene bonnie_stage7_79
    pause
    image bonnie_stage7_80 = "/bonnie/events/stage7/80.webp"
    scene bonnie_stage7_80
    "You can already see how wet she was becoming."
    image bonnie_stage7_81 = "/bonnie/events/stage7/81.webp"
    scene bonnie_stage7_81
    window hide
    pause
    if persistent.nosexscene:
        scene black with dissolve
        "Bonnie and you had a good time."
    else:
        image bonnie_stage7_82 = "/bonnie/events/stage7/82.webp"
        scene bonnie_stage7_82
        "Seeing her cheeks flush with excitement, you place your hand between her legs."
        image bonnie_stage7_83 = "/bonnie/events/stage7/83.webp"
        scene bonnie_stage7_83
        "Looking deep into her eyes, Bonnies moans at your touch."
        image bonnie_stage7_84 = "/bonnie/events/stage7/84.webp"
        scene bonnie_stage7_84
        window hide
        pause
        image bonnie_stage7_85 = "/bonnie/events/stage7/85.webp"
        scene bonnie_stage7_85
        bonnie "You feel so good."
        image bonnie_stage7_86 = "/bonnie/events/stage7/86.webp"
        scene bonnie_stage7_86
        "Gripping your arm, Bonnie moans louder and louder."
        image bonnie_stage7_87 = "/bonnie/events/stage7/87.webp"
        scene bonnie_stage7_87
        "Watching her eyes roll back into her head, you move your hand faster and deeper inside her."
        image bonnie_stage7_88 = "/bonnie/events/stage7/88.webp"
        scene bonnie_stage7_88
        window hide
        pause
        image bonnie_stage7_89 = "/bonnie/events/stage7/89.webp"
        scene bonnie_stage7_89
        "Screaming in ecstasy, Bonnie shudders in delight, you hand covered in her juices."
        image bonnie_stage7_90 = "/bonnie/events/stage7/90.webp"
        scene bonnie_stage7_90
        bonnie "That felt incredible."
        pc "You are so fucking hot."
        bonnie "You are not so bad yourself."
        bonnie "But don't think we are done already, you are not getting off that easily…or maybe you are."
        image bonnie_stage7_91 = "/bonnie/events/stage7/91.webp"
        scene bonnie_stage7_91
        "Opening her legs, Bonnie invites you in to clean up the mess you had just made."
        image bonnie_stage7_92 = "/bonnie/events/stage7/92.webp"
        scene bonnie_stage7_92
        "Despite having just cum, you can already hear Bonnie's breath quickening again."
        image bonnie_stage7_93 = "/bonnie/events/stage7/93.webp"
        scene bonnie_stage7_93
        "Placing your head between her legs, you see her grab the bedsheets between her clenched fingers as the pleasure builds within her once again."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/oral1.webm" loop
        show movie with dissolve
        window hide
        pause
        "Continuing to work your magic, and possibly still riding the high from her last orgasm."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/oral2.webm" loop
        show movie with dissolve
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/oral3.webm" loop
        show movie with dissolve
        pause
        "It doesn't take long for Bonnie's body to shudder again as her hips buck and thighs press against you head still between her legs."
        stop movie
        image bonnie_stage7_94 = "/bonnie/events/stage7/94.webp"
        scene bonnie_stage7_94
        window hide
        pause
    image bonnie_stage7_95 = "/bonnie/events/stage7/95.webp"
    scene bonnie_stage7_95
    pc "Wow, someone was horny tonight."
    image bonnie_stage7_96 = "/bonnie/events/stage7/96.webp"
    scene bonnie_stage7_96
    bonnie "You have no idea, and besides, it's ‘is’ not was."
    bonnie "But I think it’s only fair we let you get some relief too."
    image bonnie_stage7_97 = "/bonnie/events/stage7/97.webp"
    scene bonnie_stage7_97
    "Tossing her body suit to the floor, Bonnie approaches you on her hands and knees."
    image bonnie_stage7_98 = "/bonnie/events/stage7/98.webp"
    scene bonnie_stage7_98
    window hide
    pause
    image bonnie_stage7_99 = "/bonnie/events/stage7/99.webp"
    scene bonnie_stage7_99
    window hide
    pause
    if persistent.nosexscene:
        scene black with dissolve
        "Bonnie and you had a good time."
    else:
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/bj1.webm" loop
        show movie with dissolve
        "You sit down on her bed when Bonnie stands up in front of you."
        pc "You are a work of art."
        pc "And you are looking tastier than any of your treats."
        bonnie "Stop."
        pc "I could almost compare you to your pastries."
        pc "Sculped by a gifted artist, that's for sure."
        bonnie "I'm already standing in front of you naked, you don't have to use your silver tongue."
        bonnie "Although I quite enjoyed it a moment ago."
        bonnie "And if anyone is the artist with their hands, I'd have to give you the credit."
        stop movie
        $ renpy.movie_cutscene("/images/bonnie/events/stage7/bj2.webm", stop_music=False)
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/bj3.webm" loop
        show movie with dissolve
        bonnie "Ah, I see your flattery was not unfounded."
        pc "You caused quite a stir alright."
        bonnie "Well, let me help you out with that."
        bonnie "Since apparently I'm the one that caused it."
        pc "Oh, you absolutely were."
        bonnie "You ate me out so nicely tonight, I feel like I have something to prove."
        bonnie "I have to remind you who has the biggest appetite between us."
        stop movie
        $ renpy.movie_cutscene("/images/bonnie/events/stage7/bj4.webm", stop_music=False)
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/bj5.webm" loop
        show movie with dissolve
        "Placing your cock into her mouth, she moves her head back and forth."
        pc "That's it."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/bj6.webm" loop
        show movie with dissolve
        "After everything you had already seen, you can feel the pleasure building inside you."
        pc "Mmm, Bonnie."
        pc "I knew you could put down an impressive amount of chocolate, but it's nice to know you can handle your meat as well."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/bj7.webm" loop
        show movie with dissolve
        "The gentle caress of her mouth and tongue threatening to send you over the edge."
        pc "You're going to end me!"
        window hide
        pause
        "But just as you are about to fill her mouth, you hear a loud knock on the door."
        stop movie
        image bonnie_stage7_129 = "/bonnie/events/stage7/129.webp"
        scene bonnie_stage7_129
        pc "Fuck, I'm so close."
        bonnie "Mmm, too bad."
    image bonnie_stage7_130 = "/bonnie/events/stage7/130.webp"
    scene bonnie_stage7_130
    bonnie "Can you get that for me, I’m not exactly in a position to answer it."
    pc "Could be fun, making you answer the door like that."
    bonnie "In a way, it’s for you anyway."
    image bonnie_stage7_100 = "/bonnie/events/stage7/100.webp"
    scene bonnie_stage7_100
    "Leaving the naked Bonnie in her bedroom you quickly grab your shirt and answer the door."
    image bonnie_stage7_101 = "/bonnie/events/stage7/101.webp"
    scene bonnie_stage7_101
    "Opening it, you can tell what Bonnie meant, two large bags of food have been left at the door."
    image bonnie_stage7_102 = "/bonnie/events/stage7/102.webp"
    scene bonnie_stage7_102
    pc "Someones hungry."
    bonnie "I am starving, and horny."
    pc "Still?"
    image bonnie_stage7_103 = "/bonnie/events/stage7/103.webp"
    scene bonnie_stage7_103
    bonnie "What can I say, you just do something to me."
    bonnie "But now I want you to do something different to me, I’m looking far too skinny right now."
    bonnie "Then we can carry on where we left off."
    image bonnie_stage7_104 = "/bonnie/events/stage7/104.webp"
    scene bonnie_stage7_104
    "Unpacking the bags, you are surprised by just how much Bonnie had ordered, it would have been enough to feed a family or more."
    image bonnie_stage7_105 = "/bonnie/events/stage7/105.webp"
    scene bonnie_stage7_105
    bonnie "It all smells so good, it almost seems a waste to shove it in so recklessly."
    pc "I’m sure we can let you enjoy some of it first if you just want to sit and eat for a bit?"
    bonnie "I think you are miss understanding the point of a late night booty call."
    bonnie "Now feed me the burger!"
    image bonnie_stage7_106 = "/bonnie/events/stage7/106.webp"
    scene bonnie_stage7_106
    "Listening to her you grab the burger and hold it up to her mouth so she could eat it."
    "Locking eyes with you Bonnie greedily bites into the burger."
    "The force and desire in her bites causing the burger to move away from her unless you put some force behind it."
    image bonnie_stage7_107 = "/bonnie/events/stage7/107.webp"
    scene bonnie_stage7_107
    "Licking the sauce from her lips, you can see her eyes scanning over the food again."
    image bonnie_stage7_108 = "/bonnie/events/stage7/108.webp"
    scene bonnie_stage7_108
    "Picking up some fries you stuff her mouth full as she smiles happily."
    image bonnie_stage7_109 = "/bonnie/events/stage7/109.webp"
    scene bonnie_stage7_109
    window hide
    pause
    image bonnie_stage7_110 = "/bonnie/events/stage7/110.webp"
    scene bonnie_stage7_110
    "Moving on you feed her piece after pice of her giant meal."
    image bonnie_stage7_111 = "/bonnie/events/stage7/111.webp"
    scene bonnie_stage7_111
    "Each one causes her stomach to bloat even more, but you don't see a moment's hesitation out of Bonnie."
    image bonnie_stage7_112 = "/bonnie/events/stage7/112.webp"
    scene bonnie_stage7_112
    window hide
    pause
    image bonnie_stage7_113 = "/bonnie/events/stage7/113.webp"
    scene bonnie_stage7_113
    "Despite looking full, each time she finishes a mouthful, she opens it waiting for the next."
    image bonnie_stage7_114 = "/bonnie/events/stage7/114.webp"
    scene bonnie_stage7_114
    "Reaching over you massage her giant belly as she eats."
    pc "You feel as hard as a rock down there."
    image bonnie_stage7_115 = "/bonnie/events/stage7/115.webp"
    scene bonnie_stage7_115
    bonnie "Does it turn you on to see me so full?"
    pc "It does, you look amazing."
    bonnie "Well then, don't stop feeding me!"
    image bonnie_stage7_116 = "/bonnie/events/stage7/116.webp"
    scene bonnie_stage7_116
    "Grabbing a donut she continues eating for your pleasure."
    image bonnie_stage7_117 = "/bonnie/events/stage7/117.webp"
    scene bonnie_stage7_117
    "Her stomach growing more and more, until finally the last bite of food has been eaten."
    image bonnie_stage7_118 = "/bonnie/events/stage7/118.webp"
    scene bonnie_stage7_118
    window hide
    pause
    image bonnie_stage7_119 = "/bonnie/events/stage7/119.webp"
    scene bonnie_stage7_119
    bonnie "I’m so tight, I love it."
    bonnie "I love being your little feedee, stuffed so full for you."
    image bonnie_stage7_120 = "/bonnie/events/stage7/120.webp"
    scene bonnie_stage7_120
    "Running your hand along her body, you admire its new size."
    pc "You are incredible."
    image bonnie_stage7_121 = "/bonnie/events/stage7/121.webp"
    scene bonnie_stage7_121
    "Leaning over, you kiss her passionately."
    image bonnie_stage7_122 = "/bonnie/events/stage7/122.webp"
    scene bonnie_stage7_122
    "With your lips locked, you feel Bonnie's hands reaching down and into your pants."
    image bonnie_stage7_123 = "/bonnie/events/stage7/123.webp"
    scene bonnie_stage7_123
    "Gently stroking your cock, she pulls you in closer."
    image bonnie_stage7_124 = "/bonnie/events/stage7/124.webp"
    scene bonnie_stage7_124
    "Moving around and getting on her knees, you strip naked."
    if persistent.nosexscene:
        scene black with dissolve
        "Bonnie and you had a good time."
    else:
        image bonnie_stage7_125 = "/bonnie/events/stage7/125.webp"
        scene bonnie_stage7_125
        "Entering her, you gently thrust forwards, feeling more resistance than usual from her full stomach."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/sex1.webm" loop
        show movie with dissolve
        "Moaning loudly into the room, Bonnie rocks herself back and forth, desperate to get as much of you into her as possible."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/sex2.webm" loop
        show movie with dissolve
        window hide
        pause
        pc "Fuck, this feels incredible."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/sex3.webm" loop
        show movie with dissolve
        window hide
        pause
        bonnie "Fuck me faster, fill me up even more!"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/sex4.webm" loop
        show movie with dissolve
        "Picking up the pace, you slide in and out of her."
        "Each thrust eliciting moans of pleasure from Bonnie."
        "Your toned muscles sending ripples through her soft rear."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/sex5.webm" loop
        show movie with dissolve
        bonnie "Mmm, do you like this, feeding me and fucking me."
        pc "Yeah."
        bonnie "You like it when I am so stuffed like this."
        bonnie "But I bet you want me bigger, much bigger."
        pc "Fuck yeah."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/sex6.webm" loop
        show movie with dissolve
        bonnie "I want that too, to be your greedy little play thing."
        bonnie "Feed me!"
        "With her words of encouragement, you can feel yourself getting close."
        bonnie "Don't cum yet."
        stop movie
        image bonnie_stage7_126 = "/bonnie/events/stage7/126.webp"
        scene bonnie_stage7_126
        bonnie "Mmm, I want to see more."
        pc "More?"
        bonnie "Fuck me up against the mirror so I can see my fat body taking all your cock."
        stop movie
        image bonnie_stage7_127 = "/bonnie/events/stage7/127.webp"
        scene bonnie_stage7_127
        "Moving over to the mirror Bonnie steadies her hands against the reflective surface."
        image bonnie_stage7_128 = "/bonnie/events/stage7/128.webp"
        scene bonnie_stage7_128
        "You move behind her to continue fucking her."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/sex7.webm" loop
        show movie with dissolve
        window hide
        pause
        bonnie "Oh yeah, look at my flabby body move."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/sex8.webm" loop
        show movie with dissolve
        window hide
        pause
        bonnie "I bet you love this, seeing me shake like this."
        bonnie "Look at what you have done to me, you have made me so fat."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/sex9.webm" loop
        show movie with dissolve
        window hide
        pause
        pc "Oh fuck, I'm close!"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/sex10.webm" loop
        show movie with dissolve
        bonnie "Keep going, don't stop!"
        window hide
        pause
        stop movie
        image bonnie_stage7_131 = "/bonnie/events/stage7/131.webp"
        scene bonnie_stage7_131
        "Feeling the pleasure build inside of you, you both orgasm at the same time."
        #"Feeling the pleasure build inside of you, you pull out showering Bonnie as she cums as well."
    image bonnie_stage7_132 = "/bonnie/events/stage7/132.webp"
    scene bonnie_stage7_132
    bonnie "Wow, that felt amazing."
    pc "Yeah, I just can't help myself around you."
    image bonnie_stage7_133 = "/bonnie/events/stage7/133.webp"
    scene bonnie_stage7_133
    "Both exhausted, you lie down in Bonnie's bed."
    image bonnie_stage7_134 = "/bonnie/events/stage7/134.webp"
    scene bonnie_stage7_134
    "Your physical activity causing sleep to come easily to you both as you lay next to your bloated Bonnie."
    scene black with dissolve
    window hide
    pause
    if recollection == False:
        $ phonecall = 0
        $ daytime = 1
        $ day += 1
        $ strip = 0
        $ worked_today = 0
    ###Night / black screen###
    ###Morning###
    image bonnie_stage7_135 = "/bonnie/events/stage7/135.webp"
    scene bonnie_stage7_135 with dissolve
    "Feeling movement beside you, it stirs you from your sleep."
    image bonnie_stage7_136 = "/bonnie/events/stage7/136.webp"
    scene bonnie_stage7_136
    bonnie "Morning, seems like we made quite the mess last night."
    pc "I’d say we got most of it in the right place."
    image bonnie_stage7_137 = "/bonnie/events/stage7/137.webp"
    scene bonnie_stage7_137
    "Sitting up you caress her still bloated looking stomach."
    "It had gone down since last night’s binge, but she was still sporting quite the food baby."
    "Rubbing it gently, Bonnie smiles as you admire both your handiwork."
    bonnie "I love how much I can turn you on like this."
    image bonnie_stage7_138 = "/bonnie/events/stage7/138.webp"
    scene bonnie_stage7_138
    "Kissing you, Bonnie slowly rolls onto you as you lay there."
    image bonnie_stage7_139 = "/bonnie/events/stage7/139.webp"
    scene bonnie_stage7_139
    window hide
    pause
    if persistent.nosexscene:
        scene black with dissolve
        "Bonnie and you had a good time."
    else:
        bonnie "Hey..."
        image bonnie_stage7_140 = "/bonnie/events/stage7/140.webp"
        scene bonnie_stage7_140
        bonnie "I was really enjoying our banter last night."
        bonnie "Is it too early for me to ask you to tease me?"
        pc "Never too early to enjoy this view."
        pc "Especially with that round belly you got there."
        bonnie "Right answer."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/cowgirl1.webm" loop
        show movie with dissolve
        bonnie "You know, I could blame you for this."
        pc "Could you now?"
        bonnie "The way your eyes light up when see me is so cute."
        bonnie "It makes me want to get bigger for you."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/cowgirl2.webm" loop
        show movie with dissolve
        pc "So I'm the reason you've gained such a prominent belly, huh?"
        bonnie "Excuse me, you aren't supposed to comment on a girl's weight!"
        bonnie "It's very rude."
        pc "Oh, is that right?"
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/cowgirl3.webm" loop
        show movie with dissolve
        pc "What about the size of her ass?"
        pc "That's okay, right?"
        bonnie "Not unless you plan on getting yourself slapped!"
        pc "My mistake. I suppose I'll keep my thoughts to myself from now on."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/cowgirl4.webm" loop
        show movie with dissolve
        bonnie "What thoughts are those?"
        bonnie "Are you imagining what I'd look like if I was fatter?"
        bonnie "If things kept moving in the direction they've been going..."
        bonnie "And I keep putting on weight the way I have been..."
        bonnie "Can you even imagine what that could look like?"
        pc "I can, yes."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/cowgirl5.webm" loop
        show movie with dissolve
        bonnie "Tell me."
        pc "To be honest, the first thing that comes to mind your ass."
        bonnie "Mmm, yes."
        pc "But right now, watching your breasts bounce is very distracting."
        pc "They're bigger, fuller-"
        bonnie "Heavier."
        pc "-than they were when we met."
        pc "Hell, they're bigger than the last time I saw you."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/cowgirl6.webm" loop
        show movie with dissolve
        pc "So it's not just your boobs."
        pc "It's not just your thighs."
        pc "Or your ass, or your belly."
        pc "It's all of you."
        bonnie "What about me?"
        pc "You are... delicious."
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage7/cowgirl7.webm" loop
        show movie with dissolve
        bonnie "Yes!"
        pc "Bonnie!"
        pc "You're so fucking hot!"
        bonnie "Yessss!"
        pc "I love how much you bounce!"
        pc "Every time I see you, you're even more of a dream come true!"
        window hide
        pause
        stop movie
        image bonnie_stage7_141 = "/bonnie/events/stage7/141.webp"
        scene bonnie_stage7_141
        bonnie "Fuuuuuck!"
        pc "{i}*Grunts*{/i}"
    image bonnie_stage7_142 = "/bonnie/events/stage7/142.webp"
    scene bonnie_stage7_142
    bonnie "Mmm, that was hot."
    pc "That was amazing."
    bonnie "Your teasing turned more into compliments there at the end, but I'm not complaining."
    image bonnie_stage7_143 = "/bonnie/events/stage7/143.webp"
    scene bonnie_stage7_143
    bonnie "Well, I’d love to suggest round two but now I need to get showered before I go an open up the shop."
    pc "Yeah, I need to head out too."
    pc "But honestly, last night was so amazing."
    pc "I hope you know how much it means to me."
    image bonnie_stage7_144 = "/bonnie/events/stage7/144.webp"
    scene bonnie_stage7_144
    bonnie "Me too, and it gives me plenty to think about until next time."
    "Next time, you like the sound of that."
    image bonnie_stage7_145 = "/bonnie/events/stage7/145.webp"
    scene bonnie_stage7_145
    "Getting dressed you hear Bonnie turning on the shower and decide not to join her."
    "Closing the door behind you, you leave her to her morning routine and head home to your own shower."
    if recollection == False:
        $ bonnie.weight += 0.5
    $ bonniestage7event2 = 0
    return


    #LATER
    bonnie "Good I don't want you too."
    bonnie "I want you to give me everything you have."
    bonnie "Although we have made quite the mess."
    bonnie "Why don't you hop in the shower and I’ll join you in a minute."
    pc "Sure thing."
    ### In shower###
    "Turning on the hot water, you feel it refreshing your muscles."
    "A couple of minutes later Bonnie returns."
    bonnie "Room for one more."
    pc "I think so."
    bonnie "Well, we will have to change that soon."
    "Joining you in the shower, your bodies press invitingly against each other."
    bonnie "Do you mind getting my back."
    "Grabbing the soap you massage Bonnie's back, before your hands start to wander."
    "Exploring her growing ass first, you then reach around to hold her bloated belly."
    "Pressing herself back into you, you can already feel yourself getting worked up again."

    #[Sex scene in shower]#

    "Turning off the water, you dry yourself off."
    "Pulling up your pants a few minutes later you hear the doorbell ring."
    bonnie "I got it."
    "Who would be calling at this time of night?"
    "Emerging out of the bathroom you can see Bonnies hands full with two large bags of takeaway."
    bonnie "Ready for round 2?"
    pc "Round 2, isn’t it like 5 at this point."
    bonnie "Is that a no?"
    pc "I’ll be quiet now."
    "Laughing, Bonnie leads you into her bedroom carrying her next large meal."
    pc "Are you sure you can manage all of this?"
    pc "You are already looking pretty full."
    bonnie "No, but that’s what makes it exciting right?"
    "Throwing off her clothes, you unpack the food."
    "Soon the room is filled with delicious smelling food."
    "Grabbing an onion ring, Bonnie takes a bite."
    pc "I thought that was my job?"
    bonnie "Sorry, got a little excited there."
    bonnie "It is your job, feed me, make me as big and as full as you want."
    bonnie "Whatever you want me to eat, I’ll eat it."
    ###I'm picturing her naked and lying on the bed. But feel free to change the next sentence to match renders if that isn't possible.###
    "Placing her hands above her head, Bonnie surrenders entirely to you and your desires to feed her."
    "Grabbing a burrito you hold it up for her to eat."
    "Quickly munching away at her food, she does her best to eat tidily but in this position its almost impossible."
    "Pieces of mince and sauce dropping onto her sizable chest."
    pc "Wouldn’t want to waste any would we."
    "Picking up the crumbs, Bonnies sucks them off your fingers."
    pc "Room for more?"
    bonnie "Always."
    "Grabbing a burger you feed her another fattening and greasy meal."
    "Interspersing it with fries, onion rings and soda she continues to devour everything you put up to her lips."
    "Her already full stomach growing more with each bite."
    pc "You look ready to burst."
    bonnie "Do you like that?"
    pc "I do."
    bonnie "Then keep feeding me, I can take it."
    "Rubbing your hand over her engorged gut, you play with her stomach while you feed her."
    "Each morsel of food adding to the mountain of a belly protruding out of her."
    "It was hard to believe just how much food she was packing away."
    "Although it was obvious where it was going."
    "Hearing her gut gurgle loudly, you see a moment of discomfort on her face before the smile returns."
    pc "Just a few things left."
    bonnie "Maybe I should have ordered more."
    pc "Despite the confident bravado, you can tell she is nearing her limit."
    "Picking up another handful of fries you feed her the remaining items."
    "Finally Bonnie was done with her second family sized meal."
    "Rubbing your hand over her belly, Bonnie could only groan under the weight of her own gluttony."
    "The giant mound of food pushing her down into her own bed."
    bonnie "I'm so big, I feel like a whale."
    pc "Mmm, you look so sexy right now."
    bonnie "Oh yeah, do you like me this fat, full of a month's worth of food just for you."
    pc "I do."
    "Leaning over, you gently kiss her bulging stomach."
    "Moving up you kiss a trail up her body until you lock lips with her’s."
    "You can still taste the salt from the fries she just finished as you make out."
    #[Sex scene goes here] picturing her surrounded by boxes and crumbs in quite the mess as you do so, unless that breaks the physics of it obviously.#
    "Brushing away a few of the crumbs now coating her bed, you fall down together in euphoric bliss."
    "Your physical activity causing sleep to come easily to you both as you lay next to your bloated Bonnie."
    ###Night / black screen###

    ###Morning###
    "Feeling movement beside you, it stirs you from your sleep."
    bonnie "Morning, seems like we made quite the mess last night."
    pc "I’d say we got most of it in the right place."
    "Sitting up you caress her still bloated looking stomach."
    "It had gone down since last night’s binge, but she was still sporting quite the food baby."
    "Rubbing it gently, Bonnie smiles as you admire both your handiwork."
    bonnie "I love how much I can turn you on like this."
    "Kissing you, Bonnie slowly rolls onto you as you lay there."
    "Her thighs either side of you as you feel her weight press down on you."
    "Enjoying the sensation, you both lock lips as your hands explore Bonnie's new folds."
    "Breaking her kiss, Bonnie slowly moves downwards."
    "Looking up at you she slowly wraps her mouth around you now hard cock."
    bonnie "I promise to finish it this time, no distractions."
    "Looking into your eyes she softly caresses you with her lips."
    "Moving her head back and forth, you try not to cum too soon."
    "However, Bonnie had other plans."
    "Picking up the pace you feel yourself losing the battle."
    pc "I’m going to cum."
    bonnie "Cum for me baby."
    "Unable to control yourself, you cover Bonnie in a thick layer of cum."
    bonnie "Mmm, that was hot."
    pc "That was amazing."
    bonnie "Well, I’d love to suggest round two but now I need to get showered before I go an open up the shop."
    pc "Yeah, I need to head out too."
    pc "But honestly, last night was so amazing."
    pc "I hope you know how much it means to me."
    bonnie "Me too, and it gives me plenty to think about until next time."
    "Next time, you like the sound of that."
    "Getting dressed you hear Bonnie turning on the shower and decide not to join her."
    "Closing the door behind you, you leave her to her morning routine and head home to your own shower."
    $ bonniestage7event2 = 0
    return


label Bonnie_Stage_8_Event:
    ### Scene image - In PC room scene like normal ###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("[playername], I need your help!", who=1)
    pause
    $ msg ("I’ve made a terrible mistake.", who=1)
    pause
    $ msg ("Can you come over now?", who=1)
    menu:
        "Yes.":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "Not today.":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
    #[GAME – YES / Not tonight options]
    #IF YES

    ##### Scene image – Bonnie in orange dress inside of shop behind counter as if serving you ####
    image bonnie_stage8_1 = "/bonnie/events/stage8/1.webp"
    scene bonnie_stage8_1
    bonnie "[playername], I'm so happy to see you."
    pc "What happened?"
    bonnie "So you know those super nice new chocolates you have been making for me."
    pc "The super unhealthy ones?"
    image bonnie_stage8_2 = "/bonnie/events/stage8/2.webp"
    scene bonnie_stage8_2
    bonnie "Yes, and that’s the problem."
    bonnie "I was supposed to be running a free sample promotion this week with the regular chocolates."
    bonnie "But I was so busy this morning I accidentally told them to take the wrong chocolates. They took the ones you made for me and not the ones for the promotion!"
    pc "I am sure it will be fine. Can't you just call them and get them returned?"
    image bonnie_stage8_3 = "/bonnie/events/stage8/3.webp"
    scene bonnie_stage8_3
    bonnie "I tried, but the delivery company said they had already been given to the customers."
    bonnie "I am sorry to ask this of you, but would you mind trying to get them back for me?"
    bonnie "I can't leave the shop unattended."
    pc "Sure. What do I need to do?"
    image bonnie_stage8_4 = "/bonnie/events/stage8/4.webp"
    scene bonnie_stage8_4
    bonnie "I managed to get the list of deliveries, there were only three today."
    bonnie "If you could go and just tell them there was a mistake and I will send the proper ones out tomorrow and get back any you can."
    pc "Sounds easy enough."
    image bonnie_stage8_5 = "/bonnie/events/stage8/5.webp"
    scene bonnie_stage8_5
    "Bonnie hands you a note with three addresses on."
    bonnie "You are a life saver."
    image bonnie_stage8_10 = "/bonnie/events/stage8/10.webp"
    scene bonnie_stage8_10
    "Looking at the list you recognise the first location, it’s Bunny Bites."

    #### Bunny bites café background then talking to Marie at the counter, maybe she looks a little stuffed / bloated  although will be hard to tell behind the counter so maybe not####
    image work_marie_workattire_counter = "/marie/[marie.stage]/workattire_counter.webp"
    scene work_marie_workattire_counter
    play music "/music/bunny_bites.ogg" if_changed
    marie "Hey, [playername]. Here to pick up a shift?"
    pc "Not right now. I'm here for Bonnie."
    pc "Apparently there was a mistake this morning and you got sent the wrong chocolates."
    marie "You work for Bonnie?"
    image work_marie_workattire_counter2 = "/marie/[marie.stage]/workattire_counter2.webp"
    scene work_marie_workattire_counter2
    marie "I didn’t know you knew how to make chocolates this good."
    pc "Haha, yeah, it's a hobby I picked up recently."
    pc "So are the chocolates here?"
    image work_marie_workattire_counter = "/marie/[marie.stage]/workattire_counter.webp"
    scene work_marie_workattire_counter
    marie "I mean, they were."
    marie "I think we sold out. You wouldn't happen to have any more?"
    marie "People have been coming in all day asking for them."
    pc "Sold out? Bonnie said they should have lasted a week?"
    marie "What can I say? People really liked them."
    image work_marie_workattire_counter3 = "/marie/[marie.stage]/workattire_counter3.webp"
    scene work_marie_workattire_counter3
    marie "And between you and me, I don’t think Amber or Lisa could get enough of them."
    "As she whispers close to you, you detect the faint sweetness of your chocolates on her breath. It seems Amber and Lisa were not the only ones enjoying your chocolates."
    pc "So you have really sold out?"
    image work_marie_workattire_counter = "/marie/[marie.stage]/workattire_counter.webp"
    scene work_marie_workattire_counter
    marie "I'm afraid so."
    marie "But tell Bonnie we would happily run another promotion any time she wants."
    pc "Sure thing."
    pc "See you later, Marie."
    stop music fadeout 1.0
    image bonnie_stage8_10 = "/bonnie/events/stage8/10.webp"
    scene bonnie_stage8_10
    "Checking the note the next address is the café in town."

    #### In café alone, quite busy in there with random npc’s if you have them. ####
    image bonnie_stage8_12 = "/bonnie/events/stage8/12.webp"
    scene bonnie_stage8_12
    "You enter the café to see it bustling with people."
    "You try to get the attention of one of the servers but they are too distracted with their customers."
    image katrine_date_chocolate1 = "/katrine/[katrine.stage]/date_chocolate1.webp"
    scene katrine_date_chocolate1
    katrine "[playername]? Fancy running into you here."
    pc "Hey, Katrine. How are you doing?"
    katrine "I'm good. Just enjoying a post-workout treat."
    image katrine_date_eat4 = "/katrine/[katrine.stage]/date_eat4.webp"
    scene katrine_date_eat4
    "You see her pop a chocolate into her mouth."
    pc "Are those the chocolates from Bonnie's?"
    katrine "Sure are. Think they are the best ones she has ever made."
    pc "Are they still selling them?"
    image katrine_date_chocolate2 = "/katrine/[katrine.stage]/date_chocolate2.webp"
    scene katrine_date_chocolate2
    katrine "No. I think I was lucky enough to get the last box, and maybe a couple more before that."
    katrine "But it's nothing I can't work off."
    pc "Sold out?"
    katrine "Yeah. People have been going crazy for them."
    katrine "I swear I saw one woman demolish half a dozen boxes of them in under ten minutes."
    pc "Really?"
    katrine "Yeah. I don't know what she puts in them, but when they ran out it almost started a riot."
    "You really need to get to that last box if you can."
    pc "It was nice seeing you again, Katrine, but I have to go."
    katrine "Sure thing. When you see Bonnie, be sure to let her know that I'll definitely soon be popping in to buy some more of these if she is selling them."
    image bonnie_stage8_10 = "/bonnie/events/stage8/10.webp"
    scene bonnie_stage8_10
    "You had no idea these chocolates were this powerful."
    "It's both exciting and a little scary, you don’t want to ruin Bonnie's shop's reputation."
    "You need to find the last box before anything bad happens."
    "You recognise the last address on the list too, it's the university."

    ### In the univercity hallway ###
    image bonnie_stage8_11 = "/bonnie/events/stage8/11.webp"
    scene bonnie_stage8_11
    play music "/music/university.ogg" if_changed
    "I need to find those chocolates."
    "But where would they be sent? Maybe you should check the cafeteria."
    unknown "Mmmm."
    "What was that?"
    image uni_sexy_teacher_food_eating_chocolate = "/teacher/[teacher.stage]/4/food_eating_chocolate.webp"
    scene uni_sexy_teacher_food_eating_chocolate
    pc "Daisy?"
    teacher "What are you doing here at this time?"
    pc "I’m looking for those."
    image uni_sexy_teacher_teaching2_bonnie = "/teacher/[teacher.stage]/4/teaching2.webp"
    scene uni_sexy_teacher_teaching2_bonnie
    teacher "My chocolates?"
    pc "There was a mix-up at Bonnie's shop and those were sent out by mistake."
    pc "How did you get them?"
    image uni_sexy_teacher_teaching1_bonnie = "/teacher/[teacher.stage]/4/teaching1.webp"
    scene uni_sexy_teacher_teaching1_bonnie
    teacher "I forgot something and when I came back to get it there was a delivery driver waiting outside."
    teacher "I said I would sign for them and brought them in here. I guess the smell was too much for me."
    pc "That’s probably a good thing."
    image uni_sexy_teacher_showoff7 = "/teacher/[teacher.stage]/4/showoff7.webp"
    scene uni_sexy_teacher_showoff7
    teacher "So you work with Bonnie at the chocolate shop."
    pc "Yes. I have been helping her recently."
    teacher "So these are your chocolates?"
    pc "Sure are. How are they?"
    image uni_sexy_teacher_showoff8 = "/teacher/[teacher.stage]/4/showoff8.webp"
    scene uni_sexy_teacher_showoff8
    teacher "Good, and I'm guessing rather fattening?"
    pc "They may be a little unhealthier than the usual ones, yes."
    image uni_sexy_teacher_showoff4 = "/teacher/[teacher.stage]/4/showoff4.webp"
    scene uni_sexy_teacher_showoff4
    teacher "Interesting... They could come in handy."
    teacher "But I suppose you will want these back then?"
    pc "I did promise Bonnie to bring them back if I could."
    image uni_sexy_teacher_showoff2 = "/teacher/[teacher.stage]/4/showoff2.webp"
    scene uni_sexy_teacher_showoff2
    teacher "It's ok."
    "Daisy hands you back the box, almost half of the chocolates are missing."
    pc "Thank you, Daisy."
    image uni_sexy_teacher_showoff3 = "/teacher/[teacher.stage]/4/showoff3.webp"
    scene uni_sexy_teacher_showoff3
    teacher "On your way out I’d drop by the library, they might have something for you."
    "You decide to follow Daisy's instructions by going to the library."
    stop music fadeout 1.0

    #### Library with Librarian ####
    image bonnie_stage2_lib1 = "/bonnie/events/stage2/lib1.webp"
    scene bonnie_stage2_lib1
    librarian "Hi. How can I help you?"
    pc "Daisy said you might have something?"
    $ bonniestage8event = 0
    image bonnie_stage2_lib2 = "/bonnie/events/stage2/lib2.webp"
    scene bonnie_stage2_lib2
    librarian "Oh, right. We got a new book in the sweet tooth series if you are interested?"
    #[Opens game menu to buy the book]
    call buybook from _call_buybook_1

    pc "Thanks."
    librarian "No problem."

    #### Bonnie’s shop with her behind counter still in orange dress ###
    image bonnie_stage8_6 = "/bonnie/events/stage8/6.webp"
    scene bonnie_stage8_6
    bonnie "You’re back!"
    pc "I'm afraid I only managed to get back one of the boxes."
    image bonnie_stage8_7 = "/bonnie/events/stage8/7.webp"
    scene bonnie_stage8_7
    bonnie "Oh, I hope nothing bad has happened."
    pc "For what it’s worth, people seemed to really love the new chocolates."
    image bonnie_stage8_8 = "/bonnie/events/stage8/8.webp"
    scene bonnie_stage8_8
    bonnie "Really?"
    bonnie "Thank you for your help with this."
    image bonnie_stage8_9 = "/bonnie/events/stage8/9.webp"
    scene bonnie_stage8_9
    bonnie "You must be tired after going all over town for me. I have just closed the shop for the evening, so why don't you come back here with me?"

    ####Bonnies kitchen####
    image bonnie_stage8_13 = "/bonnie/events/stage8/13.webp"
    scene bonnie_stage8_13
    play music "/music/bonnie.ogg" if_changed
    bonnie "Maybe I can pay you back for all your hard work in another way."
    image bonnie_stage8_14 = "/bonnie/events/stage8/14.webp"
    scene bonnie_stage8_14
    "Bonnie slowly takes off her skirt while looking you in the eyes to watch your reaction."
    bonnie "You like the progress I have made recently?"
    pc "You know I do."
    image bonnie_stage8_15 = "/bonnie/events/stage8/15.webp"
    scene bonnie_stage8_15
    "Bonnie then lifts up her orange shirt to reveal her big bossom."
    "You get to have a good look at her growing body, her belly now clearly fat, round and soft."
    "While her belly and bottom steal the show, her breasts are certainly looking bigger too."
    pc "Where shall I put these chocolates I did manage to get back?"
    image bonnie_stage8_16 = "/bonnie/events/stage8/16.webp"
    scene bonnie_stage8_16
    bonnie "Why don’t you bring them over here?"
    image bonnie_stage8_17 = "/bonnie/events/stage8/17.webp"
    scene bonnie_stage8_17
    "Placing the boxes next to her, Bonnie then gives you a kiss."
    "She then whispers in your ear."
    bonnie "Feed them to me."
    $ stuffed = 0

    image cafe_bonnie_home_feeding_start_event8 = "/bonnie/8/feeding_start_[stuffed].webp"
    scene cafe_bonnie_home_feeding_start_event8
    window hide
    pause
    image bonnie_home_eating_sweets1_event8 = "/bonnie/8/feeding_1_[stuffed].webp"
    scene bonnie_home_eating_sweets1_event8
    pause
    image bonnie_home_eating_sweets2_event8 = "/bonnie/8/feeding_2_[stuffed].webp"
    scene bonnie_home_eating_sweets2_event8
    bonnie "Yes, I'd love to eat more. There is still plenty of room."
    image bonnie_home_eating_sweets3_event8 = "/bonnie/8/feeding_3_[stuffed].webp"
    scene bonnie_home_eating_sweets3_event8
    window hide
    pause
    $ stuffed = 1
    "Her belly starts to look bigger from all the chocolates."
    image bonnie_home_eating_sweets7_event8 = "/bonnie/8/feeding_7_[stuffed].webp"
    scene bonnie_home_eating_sweets7_event8
    bonnie "Pff, I feel so stuffed, but I need more chocolates."
    image bonnie_home_eating_sweets5_event8 = "/bonnie/8/feeding_5_[stuffed].webp"
    scene bonnie_home_eating_sweets5_event8
    window hide
    pause
    image bonnie_home_eating_sweets6_event8 = "/bonnie/8/feeding_6_[stuffed].webp"
    scene bonnie_home_eating_sweets6_event8
    pause
    $ stuffed = 2
    "Bonnie takes of her bra, letting her enlarged breasts hang down on her stuffed belly."
    image bonnie_home_eating_sweets4_event8 = "/bonnie/8/feeding_4_[stuffed].webp"
    scene bonnie_home_eating_sweets4_event8
    window hide
    pause
    image cafe_bonnie_home_feeding_end_event8 = "/bonnie/8/feeding_end_[stuffed].webp"
    scene cafe_bonnie_home_feeding_end_event8
    bonnie "Ugh, if you feed me any more I'm definitely going to fall asleep and I don't want to miss the Choc-off final!"
    pc "I think Choc-off already started. Let's go over to the couch."

    ###After stuffing scene – back on sofa###
    image bonnie_stage8_18 = "/bonnie/events/stage8/18.webp"
    scene bonnie_stage8_18
    "With a stuffed Bonnie barely staying awake you switch on the TV."
    "Tonight was the grand final of the Choc-off. You have missed the start while getting your own show from Bonnie."
    image bonnie_stage8_19 = "/bonnie/events/stage8/19.webp"
    scene bonnie_stage8_19
    "Now down to the final two, Sue and John have made their final show stoppers."
    "Despite having eaten her fill, it's clear Bonnie still likes the looks of both of them."
    "Sue has gone all out; a three-tiered chocolate cake with a shiny ganache that slowly rolls down the sides as the judges dig in."
    image bonnie_stage8_20 = "/bonnie/events/stage8/20.webp"
    scene bonnie_stage8_20
    "Not to be outdone, John has presented a classic, but perfect-looking twelve-layer fondant chocolate cake coated in buttercream, caramel drizzle and flakes of honeycomb."
    "Glued to the screen, you both cheer as Sue is announced the winner."
    image bonnie_stage8_21 = "/bonnie/events/stage8/21.webp"
    scene bonnie_stage8_21
    bonnie "I knew she could do it!"
    pc "That cake looked so good, I could almost taste it."
    image bonnie_stage8_18 = "/bonnie/events/stage8/18.webp"
    scene bonnie_stage8_18
    bonnie "You know they put their recipes online."
    bonnie "If you wanted to, we could try and recreate it?"
    pc "That sounds like a great idea."
    "Maybe you would get to live your fantasies of feeding Bonnie a showstopper after all."

    scene outside2
    stop music fadeout 1.0
    "After helping clear up you head home."
    "Despite Bonnie's nervousness about those chocolates getting into the town, you can't help but feel a little excited to know so many people have tried and eaten your fattening chocolates."

    #So the description I put there would be changed to whatever asset you make or find. Basically thinking of a very large cake that we would then have to feed her later on if that sounds doable? If not then I can tweak this and remove the last couple of comments
    if recollection == False:
        $ daytime += 2
        $ bonnie.weight += 1
        $ librarianstage = 2
        $ phonecall = 1
    $ stuffed = 0
    return


label Bonnie_Stage_9_Event:
    ### Scene image - In PC room scene like normal ###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("Hey, [playername]. Are you free today? I want to talk to you about something!", who=1)
    pause
    $ msg ("Can we meet at the café?", who=1)
    menu:
        "Yes.":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "Not today.":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
    #[GAME – YES / Not tonight options]
    #IF YES

    #####Cafe –  Bonnie sat in the booth in casual clothes.#####
    image bonnie_stage9_1 = "/bonnie/events/stage9/1.webp"
    scene bonnie_stage9_1
    bonnie "Hey, [playername]. Thanks for coming."
    pc "Sure, no problem. Is everything okay?"
    image bonnie_stage9_2 = "/bonnie/events/stage9/2.webp"
    scene bonnie_stage9_2
    bonnie "Yes. Well, sort of."
    pc "What is it? Maybe I can help."
    image bonnie_stage9_3 = "/bonnie/events/stage9/3.webp"
    scene bonnie_stage9_3
    bonnie "That’s kind of what I wanted to talk to you about."
    bonnie "You have done so much for me and the shop already."
    bonnie "So, I was wondering if maybe you wanted to become my new partner?"
    pc "Partner?"
    image bonnie_stage9_4 = "/bonnie/events/stage9/4.webp"
    scene bonnie_stage9_4
    bonnie "Yes. As in a formal business one."
    bonnie "You wouldn’t have to do anything more than you are doing now."
    bonnie "It would just recognise you as a part of the business."
    pc "Are you sure?"
    bonnie "Of course. You already are basically my partner."
    image bonnie_stage9_5 = "/bonnie/events/stage9/5.webp"
    scene bonnie_stage9_5
    bonnie "As in business partner."
    pc "Why were you nervous to ask me about this, or was there something else?"
    image bonnie_stage9_6 = "/bonnie/events/stage9/6.webp"
    scene bonnie_stage9_6
    bonnie "It's something else."
    bonnie "Despite your amazing chocolates bringing back the customers to start with I have been noticing a drop in them recently."
    bonnie "I am worried that it might be due to the chocolates I sent out by accident."
    bonnie "I think I might have damaged the trust of our customers."
    pc "I don't think that's true. Everyone loved them. There must be something else."
    image bonnie_stage9_7 = "/bonnie/events/stage9/7.webp"
    scene bonnie_stage9_7
    bonnie "I just don't know."
    pc "Why don't I grab us something to eat and we can try and figure it out?"
    bonnie "Sure thing."

    #### Standing at the ordering point in Café (if it has one)####
    image bonnie_stage9_8 = "/bonnie/events/stage9/8.webp"
    scene bonnie_stage9_8
    "You walk up to the barista to order a bit of food for Bonnie and yourself."
    image bonnie_stage9_9 = "/bonnie/events/stage9/9.webp"
    scene bonnie_stage9_9
    "Waiting for the barista to return with your food you eyes begin to wander."
    "As you scan past the counter your eyes are drawn to a part of the menu you haven’t seen before."
    image bonnie_stage9_10 = "/bonnie/events/stage9/10.webp"
    scene bonnie_stage9_10
    "The menu states that the chocolates are made by a new chocolate shop that opened up in town. That must be why sales are down!"
    "Worse than that, as you look closer you could swear they were selling chocolates that looked identical to ones Bonnie sells."
    "You write down the details on your notepad so you can show Bonnie."

    ### Back at table with Bonnie####
    image bonnie_stage9_11 = "/bonnie/events/stage9/11.webp"
    scene bonnie_stage9_11
    pc "I think I've found your problem."
    "Handing Bonnie the notepad she reads over it."
    image bonnie_stage9_12 = "/bonnie/events/stage9/12.webp"
    scene bonnie_stage9_12
    bonnie "These look identical to our chocolates!"
    pc "Do you think they are ripping off yours to sell more?"
    image bonnie_stage9_13 = "/bonnie/events/stage9/13.webp"
    scene bonnie_stage9_13
    bonnie "I don’t know, but there is one way to find out!"

    ###Outside, or maybe on the train / underground####
    image bonnie_stage9_14 = "/bonnie/events/stage9/14.webp"
    scene bonnie_stage9_14
    "Going across town, you make your way to the imposter's chocolate shop."
    ###Outside new chocolates shop####
    image bonnie_stage9_15 = "/bonnie/events/stage9/15.webp"
    scene bonnie_stage9_15
    bonnie "It even looks like my shop!"
    pc "So what do you want to do?"
    image bonnie_stage9_16 = "/bonnie/events/stage9/16.webp"
    scene bonnie_stage9_16
    bonnie "Well, even though they may look like ours, there are no rules about someone opening a chocolate shop."
    bonnie "We need to check if they taste the same."
    pc "Okay. Should be easy enough. We just need to buy some."
    image bonnie_stage9_17 = "/bonnie/events/stage9/17.webp"
    scene bonnie_stage9_17
    bonnie "Why don't you go in without me?"
    bonnie "If they are copying me they probably know what I look like and might get suspicious."
    pc "I have always wanted to go under cover, be right back."

    #### Inside the shop with “Rebecca” behind the counter #####
    image bonnie_stage9_18 = "/bonnie/events/stage9/18.webp"
    scene bonnie_stage9_18
    $ unknownname = 'Friendly Cashier'
    unknown "Hi. How can I help you?"
    pc "Can I get your Deluxe Chocolate Fudge Bomb, please?"
    unknown "Sure thing. How many would you like?"
    pc "Just one, please."
    $ unknownname = 'Unknown'
    "As she hands you the chocolate it looks and smells identical to the ones you make."
    image bonnie_stage9_19 = "/bonnie/events/stage9/19.webp"
    scene bonnie_stage9_19
    ##### Outside with Bonnie again ####
    pc "Here you go."
    "Handing her the chocolate Bonnie takes a bite."
    image bonnie_stage9_20 = "/bonnie/events/stage9/20.webp"
    scene bonnie_stage9_20
    "Her eyes light up like normal before a frown appears on her face."
    pc "Something wrong?"
    image bonnie_stage9_21 = "/bonnie/events/stage9/21.webp"
    scene bonnie_stage9_21
    bonnie "It's identical to our chocolates. I would know this taste anywhere."
    pc "Are they just buying yours and reselling them?"
    bonnie "I don’t know, but there is one way to find out."
    "You follow Bonnie as she storms into the shop."

    #####Rebecca behind the counter, maybe with Bonnie in front of you. Or could just do Bonnies name in the text and just have Rebecca as the character on the screen.#####
    image bonnie_stage9_22 = "/bonnie/events/stage9/22.webp"
    scene bonnie_stage9_22
    bonnie "I knew it had to be you, Rebecca!"
    rebecca "Wow, Bonnie? I almost didn’t recognise you."
    rebecca "Someone has really let themselves go. I warned you about your midnight snacking."
    bonnie "You are selling my chocolates!"
    rebecca "Wrong. I'm selling MY chocolates."
    image bonnie_stage9_23 = "/bonnie/events/stage9/23.webp"
    scene bonnie_stage9_23
    bonnie "That recipe belongs to the business! You agreed to it in the contract you signed!"
    rebecca "Wrong again. And I thought you were the one with the business sense."
    rebecca "We were selling this recipe before we made those stupid contracts, which only states any recipes created by us would belong to the business."
    rebecca "Since it was an older recipe it doesn’t count."
    image bonnie_stage9_24 = "/bonnie/events/stage9/24.webp"
    scene bonnie_stage9_24
    bonnie "You know that’s not how it works."
    rebecca "Maybe, maybe not. But I'm guessing if you are here, it's because the shop isn’t doing well."
    rebecca "I wondered how long it would take for even your loyal customers to leave once you ran out of my famous recipe."
    image bonnie_stage9_25 = "/bonnie/events/stage9/25.webp"
    scene bonnie_stage9_25
    bonnie "Actually, we are doing better than ever, thanks to [playername] here."
    rebecca "Him? He doesn't look like he would know a Criollo from a Nacional."  #(Types of cocoa beans)
    bonnie "His chocolates are even better than yours."
    image bonnie_stage9_26 = "/bonnie/events/stage9/26.webp"
    scene bonnie_stage9_26
    rebecca "I doubt that!"
    pc "Well, if you are so sure, why don't we have a little competition?"
    pc "Whoever's chocolates are the best gets the rights to the original recipe."
    image bonnie_stage9_27 = "/bonnie/events/stage9/27.webp"
    scene bonnie_stage9_27
    rebecca "Deal. This should be easy."
    rebecca "I’ll even let you use my kitchen, not that it will help you."


    ##### Rebecca kitchen ### (Don’t know if its possible but maybe change the wall colour / something in the kitchen to make it a little different. Unless there is a better environment you want to use for this
    image bonnie_stage9_28 = "/bonnie/events/stage9/28.webp"
    scene bonnie_stage9_28
    "Despite Rebecca's confidence, you are sure you can beat her."
    "After all, she was still selling the old chocolates and you have a new recipe to try out."
    "Grabbing everything you need, you begin to make your new chocolates."
    "The recipe is similar, but with slight variations on each quantity and ratio."
    image bonnie_stage9_29 = "/bonnie/events/stage9/29.webp"
    scene bonnie_stage9_29
    "Across the room you can see Rebecca eyeing you up suspiciously."
    "Tipping the sugar into the mixture you hear Rebecca scoff at you."
    rebecca "Amateur. Doesn't even strain or sift the sugar to get a smoother finish."
    rebecca "Really, where did you find this guy?"
    "Ignoring her, you continue to make your chocolates. The other recipes in this series haven't failed you yet."
    image bonnie_stage9_30 = "/bonnie/events/stage9/30.webp"
    scene bonnie_stage9_30
    "Finishing up the set you place the tray down in front of them both."
    bonnie "So who are the judges going to be?"
    rebecca "Why, us two, of course. You should be good at it. Looks like you have had a lot of practice since I've been gone."
    image bonnie_stage9_31 = "/bonnie/events/stage9/31.webp"
    scene bonnie_stage9_31
    bonnie "Oh, shut it! Besides, I don't even see your chocolates."
    "From the look on Rebecca's face it seems like this is the first time Bonnie had spoken back at her like that."
    rebecca "Fine."
    image bonnie_stage9_32 = "/bonnie/events/stage9/32.webp"
    scene bonnie_stage9_32
    "Pulling out a box you are unsurprised to see it full of the same chocolates she sells in the shop."
    bonnie "Those old chocolates?"
    bonnie "We sold thousands of those, they can't possibly win."
    rebecca "Well, actually, I have a bit of a surprise for you."
    rebecca "A new recipe I came up with all by myself."
    image bonnie_stage9_33 = "/bonnie/events/stage9/33.webp"
    scene bonnie_stage9_33
    "Opening the box she pulls out a couple of slightly larger chocolates."
    "You recognise these too. These are the ones you made based on Rebecca's lost notebook page."
    "Although something was slightly different about them."
    image bonnie_stage9_34 = "/bonnie/events/stage9/34.webp"
    scene bonnie_stage9_34
    pc "So what now?"
    rebecca "We taste them, it's not rocket science."
    rebecca "Ladies first."
    "Picking up her chocolate she gives one to Bonnie."
    image bonnie_stage9_35 = "/bonnie/events/stage9/35.webp"
    scene bonnie_stage9_35
    "Taking a bite out of it both of them let out a quiet moan."
    "It's clearly good, but you knew it would be. After all Rebecca is the one who unknowingly helped you with your recipes."
    rebecca "And now for the inferior chocolate."
    image bonnie_stage9_36 = "/bonnie/events/stage9/36.webp"
    scene bonnie_stage9_36
    "Picking it up she all but throws it into her mouth with a nonchalant look on her face."
    image bonnie_stage9_37 = "/bonnie/events/stage9/37.webp"
    scene bonnie_stage9_37
    "But closing her eyes it's clear something is wrong."
    "Despite her stoic outward appearance you can see her eye twitching slightly."
    "Doing her best to fight against it, she tries to play it off."
    "But as she chews Rebecca can't help but let out a muffled moan of delight."
    image bonnie_stage9_38 = "/bonnie/events/stage9/38.webp"
    scene bonnie_stage9_38
    rebecca "It's….it's…Godly!"
    image bonnie_stage9_39 = "/bonnie/events/stage9/39.webp"
    scene bonnie_stage9_39
    "Not even waiting for Bonnie to try it Rebecca begins to eat the other chocolates you prepared."
    "Unable to control herself she demolishes the remainders of the dozen you made."
    image bonnie_stage9_40 = "/bonnie/events/stage9/40.webp"
    scene bonnie_stage9_40
    rebecca "How?! How?!"
    pc "I take it mine are better?"
    rebecca "Yes! They are the best chocolates I've ever tasted!"
    pc "So you agree to stop selling the recipes you made at Bonnie's shop?"
    image bonnie_stage9_41 = "/bonnie/events/stage9/41.webp"
    scene bonnie_stage9_41
    rebecca "Yes, anything! Just promise me you will make me some more of those delicious chocolates!"
    bonnie "Amazing! You have saved the store again!"
    image bonnie_stage9_42 = "/bonnie/events/stage9/42.webp"
    scene bonnie_stage9_42
    "Leaning in Bonnie hugs you tightly, her body a little softer than the last time she did."

    #### Outside again with Bonnie ###
    image bonnie_stage9_43 = "/bonnie/events/stage9/43.webp"
    scene bonnie_stage9_43
    "After spending the next hour making a few extra batches of your chocolates, you leave Rebecca behind with them."
    bonnie "I bet you wish you could stay back there and watch her eat those chocolates."
    pc "I, uh..."
    bonnie "It's okay. You know you don't have to hide it from me."
    image bonnie_stage9_44 = "/bonnie/events/stage9/44.webp"
    scene bonnie_stage9_44
    bonnie "But given you just saved the store again, I might have a little thank you present back at my place for you." ###Flirty Look again ###

    #### In Bonnies corridor####
    image bonnie_stage9_45 = "/bonnie/events/stage9/45.webp"
    scene bonnie_stage9_45
    play music "/music/bonnie.ogg" if_changed
    bonnie "Okay, wait here. I'll get the surprise."
    "Standing in the hallway you hear a lot of crashing and banging from the kitchen. What is Bonnie doing?"
    bonnie "Okay, it's ready! Come on!"

    ###Bonnies kitchen – large cake on the counter Bonnie in the red and black underwear outfit from earlier stage event###
    image bonnie_stage9_46 = "/bonnie/events/stage9/46.webp"
    scene bonnie_stage9_46
    "Entering the kitchen you immediately spot the giant tiered cake on the countertop."
    "It's an exact replica of the one from the Choc-off finale."
    pc "Did you make this?"
    image bonnie_stage9_47 = "/bonnie/events/stage9/47.webp"
    scene bonnie_stage9_47
    bonnie "Do you like it?"
    pc "It's even bigger in person."
    bonnie "I know. By the time I put the top layer on, I was worrying if it was too much even for me."
    pc "Too much for you?"
    image bonnie_stage9_48 = "/bonnie/events/stage9/48.webp"
    scene bonnie_stage9_48
    bonnie "Well, I know how much you like to watch me eat."
    image bonnie_stage9_49 = "/bonnie/events/stage9/49.webp"
    scene bonnie_stage9_49
    "Moving over to the sofa Bonnie lays back, giving her soon to be growing stomach some extra room."
    "Knowing how much cake she will be eating, Bonnie decides not to use a fork and instead just goes ahead and picks up the pieces of cake with her hands."
    image bonnie_stage9_50 = "/bonnie/events/stage9/50.webp"
    scene bonnie_stage9_50
    "Handing her the first plate and slice she takes a bite, moaning in delight as she tastes its sweet gooey filling."
    image bonnie_stage9_51 = "/bonnie/events/stage9/51.webp"
    scene bonnie_stage9_51
    "You watch as the first plate is quickly eaten, Bonnie’s hand outstretched for you to fill it with the next."
    image bonnie_stage9_52 = "/bonnie/events/stage9/52.webp"
    scene bonnie_stage9_52
    "Happy to oblige you hand her another slice which she digs into."
    image bonnie_stage9_53 = "/bonnie/events/stage9/53.webp"
    scene bonnie_stage9_53
    "Slice after slice makes it towards her, their impact already beginning to show on her belly."
    "Bonnie's steady pace starts to slow as they take their toll."
    image bonnie_stage9_54 = "/bonnie/events/stage9/54.webp"
    scene bonnie_stage9_54
    bonnie "Ugh, this is starting to be sickly even for me."
    "Finishing her latest slice, she hands you back the plate."
    image bonnie_stage9_55 = "/bonnie/events/stage9/55.webp"
    scene bonnie_stage9_55
    "Resting a hand on her bloated belly, you are wondering if she is done."
    "But after a few moments she looks back up to you."
    image bonnie_stage9_56 = "/bonnie/events/stage9/56.webp"
    scene bonnie_stage9_56
    bonnie "Okay. Next slice, please."
    image bonnie_stage9_77 = "/bonnie/events/stage9/77.webp"
    scene bonnie_stage9_77
    pc "Are you sure? There is a lot left."
    image bonnie_stage9_57 = "/bonnie/events/stage9/57.webp"
    scene bonnie_stage9_57
    bonnie "That's okay. I'm up for the challenge."
    bonnie "Plus, it's the least I can do after you saved the shop earlier."
    "With her mind made up you hand her the next slice as the process repeats."
    image bonnie_stage9_58 = "/bonnie/events/stage9/58.webp"
    scene bonnie_stage9_58
    "After almost a full hour of chewing and swallowing Bonnie is starting to make headway."
    image bonnie_stage9_59 = "/bonnie/events/stage9/59.webp"
    scene bonnie_stage9_59
    "But her chewing has become even slower than it had been, but it's obvious why."
    image bonnie_stage9_60 = "/bonnie/events/stage9/60.webp"
    scene bonnie_stage9_60
    window hide
    pause
    image bonnie_stage9_61 = "/bonnie/events/stage9/61.webp"
    scene bonnie_stage9_61
    "Her stomach has almost doubled in size, the three tier cake really doing a number on her."
    image bonnie_stage9_62 = "/bonnie/events/stage9/62.webp"
    scene bonnie_stage9_62
    "Pausing for a moment you wonder if she has gone to far, an uneasy look on her face."
    image bonnie_stage9_63 = "/bonnie/events/stage9/63.webp"
    scene bonnie_stage9_63 with vpunch
    bonnie "Buuurrrp"
    image bonnie_stage9_64 = "/bonnie/events/stage9/64.webp"
    scene bonnie_stage9_64
    bonnie "Ugh, that should have freed up some more room."
    pc "More room? How have you got any left?"
    image bonnie_stage9_65 = "/bonnie/events/stage9/65.webp"
    scene bonnie_stage9_65
    bonnie "It's getting tight in there, but still a bit of room left."
    image bonnie_stage9_78 = "/bonnie/events/stage9/78.webp"
    scene bonnie_stage9_78
    bonnie "Besides, I'm not giving up until that whole cake is gone!"
    image bonnie_stage9_66 = "/bonnie/events/stage9/66.webp"
    scene bonnie_stage9_66
    "Hearing that you need no more convincing as you go back to handing her slice after slice of the remaining cake."
    image bonnie_stage9_67 = "/bonnie/events/stage9/67.webp"
    scene bonnie_stage9_67
    window hide
    pause
    image bonnie_stage9_68 = "/bonnie/events/stage9/68.webp"
    scene bonnie_stage9_68
    "After almost two hours Bonnie lays down the last plate."
    image bonnie_stage9_69 = "/bonnie/events/stage9/69.webp"
    scene bonnie_stage9_69
    "The giant cake gone, the only evidence of it a few crumbs and Bonnie's giant stomach."
    image bonnie_stage9_70 = "/bonnie/events/stage9/70.webp"
    scene bonnie_stage9_70
    "You would have thought it impossible if you hadn’t seen it with your own eyes."
    image bonnie_stage9_71 = "/bonnie/events/stage9/71.webp"
    scene bonnie_stage9_71
    "Her soft stomach is almost creaking under the weight of everything she has forced into it."
    pc "Wow."
    image bonnie_stage9_72 = "/bonnie/events/stage9/72.webp"
    scene bonnie_stage9_72
    bonnie "I told you it was possible."
    bonnie "Oooh, I don’t think I've ever been this full before."
    pc "That was a lot of cake."
    image bonnie_stage9_73 = "/bonnie/events/stage9/73.webp"
    scene bonnie_stage9_73
    bonnie "That was a lot of cake."
    image bonnie_stage9_74 = "/bonnie/events/stage9/74.webp"
    scene bonnie_stage9_74
    "Caressing her skin Bonnie continues to make uncomfortable noises as she almost seems to struggle to understand the size of her body."
    image bonnie_stage9_75 = "/bonnie/events/stage9/75.webp"
    scene bonnie_stage9_75
    window hide
    pause
    "Bonnie takes off her bra to unleash her swollen breasts."
    bonnie "Everything feels so heavy, so tight."
    if persistent.nosexscene == True:
        scene black with dissolve
        "Bonnie and i had a great time together."
        scene outside2
        stop music fadeout 1.0
        "That was amazing."
        "Even with all the stuffings, you didn’t realise Bonnie had that level of capacity."
        if recollection == False:
            $ daytime += 2
            $ phonecall = 1
            $ bonnie_ask_bigger = 1
            $ bonnie.weight += 1
        $ bonniestage9event = 0
        return

    "Bonnie then slowly takes off the rest of her clothes."
    bonnie "Come, fill me up even more with your cock."
    image bonnie_stage9_76 = "/bonnie/events/stage9/76.webp"
    scene bonnie_stage9_76
    "Bonnie lays down on the couch with her legs spread, her gigantic belly sticking out while her pussy is waiting."
    "You grab her hands and slowly shove your rigid dick into her soaking wet pussy."
    "The pressure of her stuffed belly seems to nearly make her climax from the insertion alone."
    bonnie "OHH, it's so tight! Please take it slow."
    window hide
    pause
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/bonnie/events/stage9/79.webm" loop
    show movie with dissolve
    pause
    "You slowly, but firmly start thrusting into Bonnie's stuffed body, feeling the weight with every move you make."
    "You can't help but stare at her huge belly and breasts jiggling. What seemed like fantasy was now happening for real."
    "Not long after sex starts both Bonnie and you climax, turning the room into a combination of moans and screams of pleasure."
    stop movie
    image bonnie_stage9_80 = "/bonnie/events/stage9/80.webp"
    scene bonnie_stage9_80
    window hide
    pause
    "Bonnie lies down while shaking from euphoria."
    "It takes a while before Bonnie regains her senses."
    image bonnie_stage9_81 = "/bonnie/events/stage9/81.webp"
    scene bonnie_stage9_81
    window hide
    pause
    bonnie "Being completely stuffed while having sex is something else."
    bonnie "Thanks for the amazing evening. I don't think I can do much else besides sleeping for a while."
    "You help Bonnie move to her bed before taking your leave."
    scene outside2
    stop music fadeout 1.0
    "That was amazing."
    "Even with all the stuffings, you didn’t realise Bonnie had that level of capacity."

    scene player_room
    "Later that night you receive a message from Bonnie."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg (None, who=1, pic="stage9_bonnie")
    pause
    $ msg ("Look what you've done to me.", who=1)
    pause
    $ msg ("I don't remember baking that giant cake.")
    pause
    $ msg ("But I vividly remember you feeding it to me.", who=1)
    pause
    $ msg ("In fact, it’s all I can think about right now.", who=1)
    pause
    $ msg ("Maybe I should have made two.", who=1)
    pause
    $ msg ("I think one might have been enough.")
    pause
    $ msg ("True, but soon I want to be able to eat two, three or even four for you.", who=1)
    pause
    $ msg ("I can't wait to get even bigger for you.", who=1)
    pause
    $ msg ("If you would like that?", who=1)
    pause
    $ msg ("I do, if you do?")
    pause
    $ msg ("In that case, I better head to the shops.", who=1)
    pause
    $ msg ("I’m all out of flour and butter.", who=1)
    pause
    $ msg ("Can’t wait to see you again.", who=1)
    pause
    $ msg ("See you soon Bonnie.")
    pause
    $ hide_messenger()

    if recollection == False:
        $ daytime += 2
        $ phonecall = 1
        $ bonnie_ask_bigger = 1
        $ bonnie.weight += 1
    $ bonniestage9event = 0
    return

label Bonnie_Stage_10_Event:
    ### Scene image - In PC room scene like normal ###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("Hey, [playername]. Can you come over?", who=1)
    menu:
        "Yes.":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "Not today.":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
    #[GAME – YES / Not tonight options]
    #IF YES


    #### Meet Bonnie outside wearing her orange jumper ###
    image bonnie_stage10_29 = "/bonnie/events/stage10/29.webp"
    scene bonnie_stage10_29
    "Approaching the shop, something doesn't look right."
    bonnie "Hey, [playername]. I'm glad you came."
    pc "Hi, Bonnie. Are you okay?"
    image bonnie_stage10_30 = "/bonnie/events/stage10/30.webp"
    scene bonnie_stage10_30
    bonnie "Yeah, I'm okay. But I can't say the same for the shop."
    bonnie "This morning when I went out to get some ingredients from the store, someone broke in."
    pc "Oh no!"
    pc "What did they take?"
    image bonnie_stage10_31 = "/bonnie/events/stage10/31.webp"
    scene bonnie_stage10_31
    bonnie "That’s the weird thing, they didn’t take anything."
    bonnie "Well, they did. A bunch of the chocolates are missing."
    pc "Really?"
    pc "Could it have just been an animal?"
    image bonnie_stage10_32 = "/bonnie/events/stage10/32.webp"
    scene bonnie_stage10_32
    bonnie "I suppose it could have been, but even though it’s a mess in there it seemed like a person did it."
    bonnie "A lot of the boxes were opened, but only a couple of chocolates were taken."
    bonnie "If it was an animal, I would have expected them to eat them all instead of a couple."
    pc "True. That is weird."
    pc "Do you need a hand cleaning up?"
    image bonnie_stage10_33 = "/bonnie/events/stage10/33.webp"
    scene bonnie_stage10_33
    bonnie "If you wouldn’t mind that would be great."
    bonnie "I’ll have to close for the day and we could do with some more chocolates since we can't sell opened boxes."

    ###Inside the shop, boxes everywhere###
    image bonnie_stage10_34 = "/bonnie/events/stage10/34.webp"
    scene bonnie_stage10_34
    "Picking up the boxes, you see what Bonnie means."
    "Most of the boxes are only missing a handful of sweets."
    "Those containing other baked goods like cakes and pies are completely untouched."
    "It seems that whoever broke in had one thing on their mind."
    pc "What was in these?"
    image bonnie_stage10_36 = "/bonnie/events/stage10/36.webp"
    scene bonnie_stage10_36
    "You hand Bonnie a couple of empty boxes, all of their contents eaten."
    bonnie "That's weird. These are the ones you made for me."
    bonnie "We don’t even sell these yet."
    image bonnie_stage10_35 = "/bonnie/events/stage10/35.webp"
    scene bonnie_stage10_35
    "Continuing to clean up for the next few hours, you have the shop looking back to normal in no time."

    ###In kitchen with bonnie still in orange jumper ####
    image bonnie_stage10_37 = "/bonnie/events/stage10/37.webp"
    scene bonnie_stage10_37
    play music "/music/bonnie.ogg" if_changed
    bonnie "Sorry to ask you to do so much today."
    pc "No worries. Especially considering you asked me to be your partner. Got to pull my weight around here."
    image bonnie_stage10_38 = "/bonnie/events/stage10/38.webp"
    scene bonnie_stage10_38
    bonnie "You don't have to worry about that. At this point I think you are doing more than me."
    bonnie "I might have been pulling my weight at the start, but now...? Especially considering it's rather more weight than when we met."
    image bonnie_stage10_39 = "/bonnie/events/stage10/39.webp"
    scene bonnie_stage10_39
    "Bonnie looks down at her body, but not in regret or shame like she had done before."
    "In fact, she seems happy despite being several dress sizes larger than she had been before."
    pc "Do you want me to make some chocolates while I'm here?"
    image bonnie_stage10_40 = "/bonnie/events/stage10/40.webp"
    scene bonnie_stage10_40
    bonnie "If you wouldn’t mind."
    pc "Sure thing, but what do you want to do with the open boxes?"
    bonnie "Don’t worry about those, I’m sure I can find a way of making them disappear."
    image bonnie_stage10_41 = "/bonnie/events/stage10/41.webp"
    scene bonnie_stage10_41
    "Grabbing a mixing bowl you begin to prepare the chocolates."
    "As usual Bonnie is never far from you as you make your various chocolate mixtures."
    "Her eyes are watching you intently as you stir the sweet-smelling chocolate."
    image bonnie_stage10_42 = "/bonnie/events/stage10/42.webp"
    scene bonnie_stage10_42
    "However, with the abundance of other chocolates she continues to snack her way through them."
    image bonnie_stage10_43 = "/bonnie/events/stage10/43.webp"
    scene bonnie_stage10_43
    "Taking your time you allow yourself to watch Bonnie as much as she is watching you."
    image bonnie_stage10_44 = "/bonnie/events/stage10/44.webp"
    scene bonnie_stage10_44
    "After an hour Bonnie is really starting to stack up the empty boxes."
    image bonnie_stage10_45 = "/bonnie/events/stage10/45.webp"
    scene bonnie_stage10_45
    "Her belly already bloated and showing signs of her binging."
    image bonnie_stage10_46 = "/bonnie/events/stage10/46.webp"
    scene bonnie_stage10_46
    bonnie "Oooh."
    pc "Starting to run out of room?"
    image bonnie_stage10_47 = "/bonnie/events/stage10/47.webp"
    scene bonnie_stage10_47
    bonnie "Something like that, but I know how to make more."
    image bonnie_stage10_48 = "/bonnie/events/stage10/48.webp"
    scene bonnie_stage10_48
    "Pulling off her jumper and letting her dress fall to the floor she stands there in her underwear."
    image bonnie_stage10_49 = "/bonnie/events/stage10/49.webp"
    scene bonnie_stage10_49
    bonnie "Now I have nothing getting in the way, where was I?"
    image bonnie_stage10_50 = "/bonnie/events/stage10/50.webp"
    scene bonnie_stage10_50
    "Picking up another box she continues to eat her way through the unsellable chocolates."
    image bonnie_stage10_51 = "/bonnie/events/stage10/51.webp"
    scene bonnie_stage10_51
    pc "I think that should do."
    "Without the need for extras to feed Bonnie, you finish in half the time it usually takes."
    image bonnie_stage10_52 = "/bonnie/events/stage10/52.webp"
    scene bonnie_stage10_52
    bonnie "Good timing, because we have definitely been on our feet too much and I think I need I might need some help finishing off these final couple of boxes."
    "Bonnie leads you to her bedroom and takes off her underwear."
    ##### Scene image – Bonnie on her bed ####
    image bonnie_stage10_53 = "/bonnie/events/stage10/53.webp"
    scene bonnie_stage10_53
    window hide
    pause
    bonnie "What do you say? Do you want to finish feeding me on my bed and have some hot sex after?"
    pc "How could I ever say no to such a thing?"
    if persistent.nosexscene == True:
        scene black with dissolve
        "Bonnie and I had a great time together."
    else:
        image bonnie_stage10_54 = "/bonnie/events/stage10/54.webp"
        scene bonnie_stage10_54
        window hide
        pause
        "Bonnie sits down on her bed, showing her fat ass and juicy pussy."
        image bonnie_stage10_55 = "/bonnie/events/stage10/55.webp"
        scene bonnie_stage10_55
        window hide
        pause
        "She then turns around and looks at you seductively."
        bonnie "Well, what are you waiting for? Feed me!"
        image bonnie_stage10_56 = "/bonnie/events/stage10/56.webp"
        scene bonnie_stage10_56
        window hide
        pause
        "Her words make you move instantly, throwing your clothes to the ground and picking up a box of chocolates."
        "You start feeding her chocolates while reaching down to her vagina, making sure both her needs are satiated."
        image bonnie_stage10_57 = "/bonnie/events/stage10/57.webp"
        scene bonnie_stage10_57
        window hide
        pause
        bonnie "Mmhhhm, yeah, this is it. Please talk dirty to me to complete the experience."
        bonnie "Tell me how you want me to grow bigger."
        image bonnie_stage10_58 = "/bonnie/events/stage10/58.webp"
        scene bonnie_stage10_58
        window hide
        pause
        "You are surprised by her request, since Bonnie hadn't asked this before. Has her gluttonous side taken over completely?"
        pc "I want you to eat all the chocolates I made for you. You’ve been such a little piggy these past few weeks. Unable to control herself around all the delicious chocolates I’ve made for you."
        pc "I want you to beg me to keep stuffing you. Show me you want to keep this beautiful body growing fatter and fatter across this bed."
        image bonnie_stage10_59 = "/bonnie/events/stage10/59.webp"
        scene bonnie_stage10_59
        window hide
        pause
        bonnie "Please keep filling me up with delicious chocolates. I want more. I need more. Please make your piggy girlfriend the biggest pig she can be."
        "Bonnie moans as her belly seems to grow bigger with every bite she takes."
        "At last she eats all of the chocolates."
        pc "You did well, my beautiful sexy pig. As a reward I will give you a meaty dessert."
        image bonnie_stage10_60 = "/bonnie/events/stage10/60.webp"
        scene bonnie_stage10_60
        window hide
        pause
        "Bonnie couldn't wait to receive her reward, she pushes you down and slowly lowers her huge body onto your rock solid penis."
        image bonnie_stage10_61 = "/bonnie/events/stage10/61.webp"
        scene bonnie_stage10_61
        window hide
        pause
        "After Bonnie lowers her body onto you, you come to realize how much bigger your partner has become."
        image bonnie_stage10_62 = "/bonnie/events/stage10/62.webp"
        scene bonnie_stage10_62
        window hide
        pause
        "The sheer weight of her stuffed body sitting on top of you makes it clear; her gain has gone off the charts."
        image bonnie_stage10_63 = "/bonnie/events/stage10/63.webp"
        scene bonnie_stage10_63
        window hide
        pause
        "But not only do you have trouble understanding how much bigger Bonnie has become, she seems to have trouble lifting herself."
        bonnie "I didn't think it would be this hard to move. Let's lie down."
        pc "What's the matter? Is my piggy getting too fat to be on top?"
        bonnie "*huff* YES! *huff* I’ve been far too greedy, and gluttonous!"
        bonnie "You’ve been feeding me too well."
        bonnie "OHHH!"
        bonnie "I’m having more and more trouble lifting this fat ass."
        bonnie "MMM!"
        "It takes considerable effort for your bloated and sweaty partner to heave herself off your rigid member."
        "But your dirty talk has clearly been effective in riling Bonnie up and she soon lifts herself off of you and rolls on to her side."
        image bonnie_stage10_64 = "/bonnie/events/stage10/64.webp"
        scene bonnie_stage10_64
        window hide
        pause
        "Following her lead, you end up in a spooning position. You lift up her leg and insert your cock into her hungry pussy."
        image bonnie_stage10_65 = "/bonnie/events/stage10/65.webp"
        scene bonnie_stage10_65
        window hide
        pause
        "With every thrust you feel the whole bed shaking and hear Bonnie moaning."
        image bonnie_stage10_66 = "/bonnie/events/stage10/66.webp"
        scene bonnie_stage10_66
        window hide
        pause
        bonnie "Let me lie down on my back. I know you like to see my big fat belly while we fuck."
        image bonnie_stage10_67 = "/bonnie/events/stage10/67.webp"
        scene bonnie_stage10_67
        window hide
        pause
        "Bonnie was right; you do like to see the fruits of your labor - seeing her growing belly jiggling while you fuck her."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage10/67_video.webm" loop
        show movie with dissolve
        window hide
        pause
        "You slowly start thrusting into her food-filled body, creating a symphony of moans from Bonnie, creaks from the bed, and wet slapping from sex."
        stop movie
        image bonnie_stage10_68 = "/bonnie/events/stage10/68.webp"
        scene bonnie_stage10_68
        window hide
        pause
        "Both of you, entranced into a lust-filled hypnosis, make love to each other."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/bonnie/events/stage10/68_video.webm" loop
        show movie with dissolve
        window hide
        pause
        "Moans turn into screams while you both reach your climaxes."
        "As both you and Bonnie finish at the same time, you pull out and cum. Your eyes are glued to Bonnie's stuffed stomach as you coat the huge jiggling mass."
        stop movie
        image bonnie_stage10_69 = "/bonnie/events/stage10/69.webp"
        scene bonnie_stage10_69
        window hide
        pause
        "Bonnie, drenched in cum, is laying on her back. It is clear that she won't be getting up for a while."
        "Her climax together with her enormous stuffed belly has taken its toll on her - making her fall asleep in a food/pleasure coma."


    scene outside
    stop music fadeout 1.0
    "Cleaning up the empty boxes, you leave Bonnie to sleep it off in her bed."
    scene outside2
    "…."
    "You don’t know why, but you get the strange feeling someone is following you."
    "But turning around, you don't see anyone. Maybe it is just your imagination."
    image bonnie_stage10_28 = "/bonnie/events/stage10/28.webp"
    scene bonnie_stage10_28
    "Returning home, you are about to unlock the door as you hear a noise behind you."
    "You don't know what happened, but suddenly everything goes dark."
    scene black with dissolve
    pause

    ### Dark version of Rebecca’s kitchen if that’s possible?”
    image bonnie_stage10_1 = "/bonnie/events/stage10/1.webp"
    scene bonnie_stage10_1
    "You don’t know how much time has passed."
    "But you wake up with your arms and legs tied in a dim room."
    image bonnie_stage10_2 = "/bonnie/events/stage10/2.webp"
    scene bonnie_stage10_2
    "You can't make out who it is, but you can see a figure walking around ahead of you, or are you just hallucinating?"
    pc "Hello?"
    $ unknownname = 'Shadowy Figure'
    unknown "You are finally awake."
    pc "What is happening? What is this about?"
    unknown "It's about your chocolates!"
    image bonnie_stage10_3 = "/bonnie/events/stage10/3.webp"
    scene bonnie_stage10_3
    pc "Rebecca?"
    pc "What do you mean 'my chocolates'? You agreed not to sell them."
    $ unknownname = 'Unknown'
    image bonnie_stage10_4 = "/bonnie/events/stage10/4.webp"
    scene bonnie_stage10_4
    rebecca "It's not about selling them."
    pc "Then what is it about?"
    image bonnie_stage10_5 = "/bonnie/events/stage10/5.webp"
    scene bonnie_stage10_5
    rebecca "It's about me needing them!"
    rebecca "They are so chocolaty, smooth, creamy, delicious…."
    pc "Rebecca?"
    image bonnie_stage10_6 = "/bonnie/events/stage10/6.webp"
    scene bonnie_stage10_6
    rebecca "I need them!"
    rebecca "They are the best thing I have ever tasted. I've never felt like this about anything before."
    rebecca "It's like I can't think without them."
    pc "It was you that broke into the shop, wasn't it?"
    image bonnie_stage10_7 = "/bonnie/events/stage10/7.webp"
    scene bonnie_stage10_7
    rebecca "I had to. It was the only way to get my hands on them."
    rebecca "You don’t understand what it's like to feel this way."
    rebecca "To be a chocolate maker but not be able to replicate them."
    rebecca "So I did the only thing I could think of: To bring you here and force you to make them."
    pc "What?"
    rebecca "I don’t care how loyal to Bonnie you might be, you are going to make me all the chocolates I desire or you are never going to leave."
    pc "Wait, you just want me to make you chocolates?"
    image bonnie_stage10_8 = "/bonnie/events/stage10/8.webp"
    scene bonnie_stage10_8
    rebecca "I don't want you to. You are going to whether you like it or not!"
    pc "That's the thing; I'd be happy to make them for you."
    image bonnie_stage10_9 = "/bonnie/events/stage10/9.webp"
    scene bonnie_stage10_9
    rebecca "Wait, what?"
    rebecca "What about you and Bonnie? The shop? Your partnership?"
    pc "Well, as long as you agree not to sell them, I don’t see why I can't make some for you."
    rebecca "Really?"
    pc "Sure. You could have just asked, you know."
    image bonnie_stage10_10 = "/bonnie/events/stage10/10.webp"
    scene bonnie_stage10_10
    rebecca "I'm sorry, I just haven’t been thinking clearly since…since I tasted them."
    "Wow, maybe Bonnie is right about not selling these if they can cause this sort of reaction in some people."
    "Coming over, Rebecca quickly unties you and turns on the light."

    #### Rebecca’s kitchen, normal version###
    image bonnie_stage10_11 = "/bonnie/events/stage10/11.webp"
    scene bonnie_stage10_11
    "Wait, this is just her kitchen."
    rebecca "I should have everything you could possibly need."
    image bonnie_stage10_12 = "/bonnie/events/stage10/12.webp"
    scene bonnie_stage10_12
    "Tentatively picking up the pan and ingredients, you start to make the first batch."
    "Despite calming down you can't help but be a little put off by her staring."
    "It's much more intense and hungry than Bonnie, even on her worst days."
    pc "So, how many should I be making?"
    image bonnie_stage10_13 = "/bonnie/events/stage10/13.webp"
    scene bonnie_stage10_13
    rebecca "As many as you can with the ingredients I have provided."
    pc "Sure thing."
    image bonnie_stage10_12 = "/bonnie/events/stage10/12.webp"
    scene bonnie_stage10_12
    "Only needing to make the one recipe, you are able to make it in much larger batches."
    "As you add to the large pan, chocolate starts to overflow on the counter."
    rebecca "Oh no!"
    image bonnie_stage10_14 = "/bonnie/events/stage10/14.webp"
    scene bonnie_stage10_14
    "Sticking out a finger she wipes a small amount of the chocolate off the counter before sucking her finger and moaning."
    "You can't help but feel this would be a dream come true if you hadn’t been kidnapped by her."
    image bonnie_stage10_15 = "/bonnie/events/stage10/15.webp"
    scene bonnie_stage10_15
    "An hour later the kitchen is full of chocolates, much to yours and Rebecca’s delight."
    pc "Well, I guess I'm done."
    image bonnie_stage10_16 = "/bonnie/events/stage10/16.webp"
    scene bonnie_stage10_16
    rebecca "So... many... chocolates...!"
    "She looks around the room with wide eyes, before lunging at the nearest tray."
    image bonnie_stage10_17 = "/bonnie/events/stage10/17.webp"
    scene bonnie_stage10_17
    rebecca "Mmmmughmm."
    "Shoveling them into her mouth she lets out muffled moans of delight."
    image bonnie_stage10_18 = "/bonnie/events/stage10/18.webp"
    scene bonnie_stage10_18
    rebecca "Soo mmmm good."
    "In the blink of an eye the first tray is demolished - all the chocolates now sitting in her growing stomach."
    image bonnie_stage10_19 = "/bonnie/events/stage10/19.webp"
    scene bonnie_stage10_19
    "Without a moment's hesitation she moves onto the next, using both hands to grab and move the chocolates into her mouth as fast as possible."
    rebecca "I….can't….too good."
    image bonnie_stage10_20 = "/bonnie/events/stage10/20.webp"
    scene bonnie_stage10_20
    "Letting out a muffled whimper she somehow starts chewing and grabbing even faster."
    "Her waistline expanding quickly due to the rapid influx of sweet, fatty and calorie-rich treats."
    image bonnie_stage10_21 = "/bonnie/events/stage10/21.webp"
    scene bonnie_stage10_21
    "With her full attention on the chocolates, you are able to freely watch the ravenous display in front of you."
    image bonnie_stage10_22 = "/bonnie/events/stage10/22.webp"
    scene bonnie_stage10_22
    "Each minute ticking by as you watch her stomach groan and grow."
    image bonnie_stage10_23 = "/bonnie/events/stage10/23.webp"
    scene bonnie_stage10_23
    "Finally, after just ten minutes, the kitchen is empty."
    image bonnie_stage10_24 = "/bonnie/events/stage10/24.webp"
    scene bonnie_stage10_24
    "Each and every chocolate devoured, not a scrap or crumb left behind."
    image bonnie_stage10_25 = "/bonnie/events/stage10/25.webp"
    scene bonnie_stage10_25
    "Sinking onto the floor, Rebecca lets out a quiet groan as her arms wrap around her expanded stomach before falling into a chocolate-fuelled coma on the floor."
    "It turns out that Rebecca and Bonnie might have more in common than they think."
    image bonnie_stage10_26 = "/bonnie/events/stage10/26.webp"
    scene bonnie_stage10_26
    "With her stomach truly bulging, you leave Rebecca to recover in her food coma."
    "But before you leave you find a notepad on the counter."
    image bonnie_stage10_27 = "/bonnie/events/stage10/27.webp"
    scene bonnie_stage10_27
    "The pages are full of her measurements and weight."
    $ rebecca_stats_visible = 1
    "Rebecca has been added to the stats page!"
    "As much as she might have been putting pressure on Bonnie, it seems she was doing the same to you."
    "Scribbling your phone number down on the page, you leave it open so Rebecca can see it when she wakes up."

    scene outside2
    "What a weird day. Who knew those chocolates can have that much power?"
    "You wonder if you should tell Bonnie - of course omitting a few bits of what just happened."
    if recollection == False:
        $ daytime += 2
        $ phonecall = 1
        $ rebecca.weight = 92
        $ bonnie_ask_bigger = 1
        $ bonnie.weight += 1
    $ bonniestage10event = 0
    return

label BonnieStage10Phone:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("Hey, I was sad to see you weren’t at Bunny bites today.", who=1)
    pause
    $ msg ("Although Marie was feeling particularly generous today.", who=1)
    pause
    $ msg ("You really should get that till fixed…or maybe don't.", who=1)
    pause
    $ msg (None, who=1, pic="stage10_bonnie")
    pause
    $ msg ("I think the till works perfectly.")
    pause
    $ msg ("Me too.", who=1)
    pause
    $ hide_messenger()

    $ bonniestage10phone = 0
    return

label Bonnie_Stage_11_Event:
    ### Scene image - In PC room scene like normal ###
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Bonnie', dialogue=dialogue_one)
    $ msg ("Hey, [playername]. I’ve got something for you at the shop I think you might like.", who=1)
    pause
    $ msg ("Come by after closing if you are free?", who=1)
    menu:
        "Yes.":
            $ msg ("Sure, I'll be there in a minute.")
            pause
            $ hide_messenger()

        "Not today.":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
    #[GAME – YES / Not tonight options]
    #IF YES

    ####Bonnies shop, bonnie sat at the table in the shop waiting for you in her casual clothes ###
    image bonnie_stage11_1 = "/bonnie/events/stage11/1.webp"
    scene bonnie_stage11_1
    bonnie "Hi, [playername]."
    pc "Hi, Bonnie. What's this big surprise?"
    image bonnie_stage11_2 = "/bonnie/events/stage11/2.webp"
    scene bonnie_stage11_2
    "Bonnie takes out a tablet and places it on the table."
    bonnie "Well, you remember I talked about making you an official partner?"
    bonnie "This is a contract to do just that."
    bonnie "With your signature you replace Rebecca and become my new partner, if you are still interested?"
    pc "Of course, but are you sure you want me to be your partner?"
    image bonnie_stage11_3 = "/bonnie/events/stage11/3.webp"
    scene bonnie_stage11_3
    bonnie "Definitely. You have already done so much."
    bonnie "You saved the shop with your chocolate recipes, helped me out when I accidentally sent those chocolates around town, got Rebecca to back off and so much more."
    image bonnie_stage11_4 = "/bonnie/events/stage11/4.webp"
    scene bonnie_stage11_4
    bonnie "Plus, you have really helped me personally."
    bonnie "I used to be so worried about what I eat and was super stressed all the time. But lately I’ve just been so happy with everything."
    bonnie "I couldn’t think of anyone better to be my partner."
    image bonnie_stage11_5 = "/bonnie/events/stage11/5.webp"
    scene bonnie_stage11_5
    "Needing no more convincing you pick up the tablet and sign the document."
    pc "So is that it? Is it official?"
    image bonnie_stage11_6 = "/bonnie/events/stage11/6.webp"
    scene bonnie_stage11_6
    bonnie "Well, there is one other thing, but I'm sure you will enjoy this even more."
    pc "Really?"
    bonnie "So, with everything that has been happening, I've been putting this off for a few weeks."
    image bonnie_stage11_7 = "/bonnie/events/stage11/7.webp"
    scene bonnie_stage11_7
    bonnie "But today is the last day to submit these forms, otherwise Rebecca would be my partner for another year."
    bonnie "But that’s not the only problem."
    pc "Problem?"
    bonnie "Well, it might be a problem for me."
    image bonnie_stage11_8 = "/bonnie/events/stage11/8.webp"
    scene bonnie_stage11_8
    bonnie "You see when we first made the contract we put in a clause that the contract can only be altered if the store is empty."
    pc "Why did it have to be empty?"
    image bonnie_stage11_9 = "/bonnie/events/stage11/9.webp"
    scene bonnie_stage11_9
    bonnie "It was just a stupid thing we included so the other person couldn’t change things without the other one noticing."
    bonnie "I guess you could say we had some trust issues right from the start."
    pc "So do you need a hand getting rid of everything?"
    image bonnie_stage11_10 = "/bonnie/events/stage11/10.webp"
    scene bonnie_stage11_10
    bonnie "I've been trying. I've been giving out free samples all week - throwing in extras to people's orders. Anything to empty the store."
    bonnie "But I guess I underestimated how many goods we sell each week and how many we had in storage."
    pc "Ok, but what do you want to do with them now?"
    image bonnie_stage11_11 = "/bonnie/events/stage11/11.webp"
    scene bonnie_stage11_11
    bonnie "I was hoping…you might feed them to me."
    pc "Feed them to you?"
    pc "Bonnie, there has to be half a store's worth of things left."
    image bonnie_stage11_12 = "/bonnie/events/stage11/12.webp"
    scene bonnie_stage11_12
    bonnie "I know. I'm definitely regretting the big lunch I had earlier."
    bonnie "But I know I can do it, we can do it."
    pc "If you are sure?"
    image bonnie_stage11_13 = "/bonnie/events/stage11/13.webp"
    scene bonnie_stage11_13
    bonnie "I am. And we better get started since the administrator will be here at 8 pm, so we only have a few hours."
    pc "What do you need from me?"
    image bonnie_stage11_14 = "/bonnie/events/stage11/14.webp"
    scene bonnie_stage11_14
    bonnie "I just need you to go through the shop and bring anything you find to me here."
    "Grabbing a half-empty box of coconut whirls, you pass them to her before starting your search."
    image bonnie_stage11_15 = "/bonnie/events/stage11/15.webp"
    scene bonnie_stage11_15
    "Smiling, Bonnie grabs the first chocolate and starts eating."
    "It's not hard to find things for her; despite her best efforts there are sweet treats everywhere."
    image bonnie_stage11_16 = "/bonnie/events/stage11/16.webp"
    scene bonnie_stage11_16
    "A couple of unopened chocolate boxes that didn’t sell this week, some sugar bombs, half a box of caramel drizzle cakes and even a few slices of a Victoria sponge cake." ###Dont have to show or can change to things you already have assets for####
    "As you open cupboards and take their sweet bounty over to her, you can see Bonnie chomping her way through everything."
    image bonnie_stage11_17 = "/bonnie/events/stage11/17.webp"
    scene bonnie_stage11_17
    "The empty boxes already starting to stack up and her belly already growing."
    "Going methodically around the room you empty the cupboards, dumping their treasures next to Bonnie."
    image bonnie_stage11_18 = "/bonnie/events/stage11/18.webp"
    scene bonnie_stage11_18
    "By the halfway mark it's clear Bonnie may have underestimated the size of the task."
    window hide
    pause
    image bonnie_stage11_19 = "/bonnie/events/stage11/19.webp"
    scene bonnie_stage11_19
    pause
    "Her bloated belly pushing outwards far more than it had at the start, but with many more sweet treats to go."
    window hide
    pause
    image bonnie_stage11_20 = "/bonnie/events/stage11/20.webp"
    scene bonnie_stage11_20
    pause
    "Standing at the counter, you watch her mechanically chewing - the enjoyment somewhat gone from her face as she forces herself to keep eating."
    "Opening the back of one of the display cabinets, you find a few untouched boxes of her marshmallow snowballs."
    pc "Are you going to be able to manage all of this? I still have a quarter of the room left and I just found these."
    image bonnie_stage11_21 = "/bonnie/events/stage11/21.webp"
    scene bonnie_stage11_21
    bonnie "I'm fine, still plenty of room."
    bonnie "Besides, these are some of my favourites."
    "You get the feeling that despite her confident words, Bonnie is putting on a brave face."
    image bonnie_stage11_22 = "/bonnie/events/stage11/22.webp"
    scene bonnie_stage11_22
    "Going back to searching, the food keeps piling up next to her."
    "You are now finding things faster than she can eat them, but at least you are almost done with the shop."
    "Looking at the clock, you are shocked to see it's almost half past 7."
    image bonnie_stage11_23 = "/bonnie/events/stage11/23.webp"
    scene bonnie_stage11_23
    pc "You need to eat faster, only fourty minutes to go."
    bonnie "Ughh, I'm going as fast as I can."
    pc "Maybe I can help you."
    pc "Go sit on the floor."
    image bonnie_stage11_24 = "/bonnie/events/stage11/24.webp"
    scene bonnie_stage11_24
    "Going over, you begin feeding her - giving her little rest between mouthfuls of sugar."
    image bonnie_stage11_25 = "/bonnie/events/stage11/25.webp"
    scene bonnie_stage11_25
    "Despite this, the look on her face is telling you she is enjoying eating a lot more now."
    image bonnie_stage11_26 = "/bonnie/events/stage11/26.webp"
    scene bonnie_stage11_26
    "Leaning back, Bonnie tries to find a pose that's more comfortable as her belly strains against her outfit."
    "You would have expected her to have chosen something less restrictive, but with the administrator coming around it wasn’t like she could strip down like normal."
    image bonnie_stage11_27 = "/bonnie/events/stage11/27.webp"
    scene bonnie_stage11_27
    "Feeding her with one hand, you use the other to rub her giant belly - trying to soothe it for her and enjoying the feel of her taut skin over her stretching abdomen."
    image bonnie_stage11_28 = "/bonnie/events/stage11/28.webp"
    scene bonnie_stage11_28
    "Box after box empties, their contents all entering Bonnie's mouth and disappearing in rapid succession."
    image bonnie_stage11_29 = "/bonnie/events/stage11/29.webp"
    scene bonnie_stage11_29
    window hide
    pause
    "Finally, as the clock shows two minutes to 8, the last box joins the pile of empty boxes."
    image bonnie_stage11_30 = "/bonnie/events/stage11/30.webp"
    scene bonnie_stage11_30
    bonnie "Ugggh, I thought that would be more fun than that."
    pc "I'm surprised you managed to eat everything."
    image bonnie_stage11_31 = "/bonnie/events/stage11/31.webp"
    scene bonnie_stage11_31
    bonnie "You keep doubting me when I say I can handle it."
    pc "Not doubting, more impressed."
    bonnie "Either way, I'm glad that is done. I could definitely do with a nap now though."
    image bonnie_stage11_32 = "/bonnie/events/stage11/32.webp"
    scene bonnie_stage11_32
    "Almost on cue you hear the door open and in steps the administrator, with Rebecca in tow."
    image bonnie_stage11_33 = "/bonnie/events/stage11/33.webp"
    scene bonnie_stage11_33
    "Grabbing the giant pile of empty boxes, you quickly shuffle them into a corner and out of sight."
    image bonnie_stage11_34 = "/bonnie/events/stage11/34.webp"
    scene bonnie_stage11_34
    bonnie "I didn't realise you would be coming, Rebecca."
    rebecca "Well, apparently they need all of us to agree to the changes."
    image bonnie_stage11_35 = "/bonnie/events/stage11/35.webp"
    scene bonnie_stage11_35
    bonnie "Not going to cause any trouble, are you?"
    rebecca "Not at all. Your new partner and I came to an agreement last time, so no need for unpleasantries."
    image bonnie_stage11_36 = "/bonnie/events/stage11/36.webp"
    scene bonnie_stage11_36
    "A look from Rebecca tells you that you might not have been fast enough in hiding the evidence."
    "Or maybe it was about the deal the pair of you had made."
    "At least this time she hadn’t kidnapped you."
    image bonnie_stage11_37 = "/bonnie/events/stage11/37.webp"
    scene bonnie_stage11_37
    admin "So, shall we get started?"
    bonnie "Yes, please."
    admin "If I'm correct, you, Bonnie, are looking to change your business operating partner from Rebecca here to [playername]."
    bonnie "Correct."
    admin "Are the other two parties in agreement as well?"
    image bonnie_stage11_38 = "/bonnie/events/stage11/38.webp"
    scene bonnie_stage11_38
    pc "Yes."
    rebecca "Yes."
    image bonnie_stage11_39 = "/bonnie/events/stage11/39.webp"
    scene bonnie_stage11_39
    admin "Okay. Well, I can see you have the signed documents ready."
    admin "The last stipulation was that the shop must be empty and by the looks of it that seems to be true."
    admin "So I'm happy to announce that as of tomorrow Rebecca will be removed and [playername] will be added as your operating partner."
    image bonnie_stage11_40 = "/bonnie/events/stage11/40.webp"
    scene bonnie_stage11_40
    bonnie "Amazing! Thank you!"
    admin "No problem. If any of you have a change of heart, or if anything else comes up, you have 48 hours to challenge this change."
    admin "But if that is everything, I will leave you all to it."
    image bonnie_stage11_41 = "/bonnie/events/stage11/41.webp"
    scene bonnie_stage11_41
    bonnie "Thank you for accepting this, Rebecca. I'm sure it will work out better for the both of us in the long run."
    rebecca "I agree. So why don't we go out to celebrate? A last dinner together."
    image bonnie_stage11_42 = "/bonnie/events/stage11/42.webp"
    scene bonnie_stage11_42
    "The mere thought of more food clearly making Bonnie a little nauseous."
    bonnie "That's nice, but I think-"
    image bonnie_stage11_43 = "/bonnie/events/stage11/43.webp"
    scene bonnie_stage11_43
    rebecca "Nonsense. My treat. Come on."
    rebecca "I’ve been meaning to try out that Bunny Bites in town."
    image bonnie_stage11_44 = "/bonnie/events/stage11/44.webp"
    scene bonnie_stage11_44
    "Bonnie looks at you with pleading wide eyes for help, but you can't think of a way out as Rebecca all but ushers you out the door."

    ###Bunnie bites in booth with Bonnie and Rebecca
    image cafe_marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene cafe_marie_serving2
    play music "/music/bunny_bites.ogg" if_changed
    marie "Hey. What can I get you all?"
    image bonnie_stage11_45 = "/bonnie/events/stage11/45.webp"
    scene bonnie_stage11_45
    bonnie "I'll just have a soda."
    rebecca "Oh, nonsense. I'm paying."
    image bonnie_stage11_46 = "/bonnie/events/stage11/46.webp"
    scene bonnie_stage11_46
    rebecca "Bring her whatever she usually orders."
    rebecca "Then I think I'll have a burger, some onion rings and a soda."
    image cafe_marie_serving2 = "/marie/[marie.stage]/serving2.webp"
    scene cafe_marie_serving2
    marie "What about you, [playername]?"
    pc "I'll just have a double cheeseburger and soda, please, Marie."
    marie "Coming right up!"
    image bonnie_stage11_47 = "/bonnie/events/stage11/47.webp"
    scene bonnie_stage11_47
    "Making small talk the food quickly arrives, the table in front of Bonnie filled with a whole pizza, two burgers, some fries, onion rings and a large soda."
    "It is more than Bonnie usually orders. Marie must have made a mistake, which is unlike her."
    "Unless she was just feeling “generous”."
    image bonnie_stage11_48 = "/bonnie/events/stage11/48.webp"
    scene bonnie_stage11_48
    "Gulping, the already stuffed Bonnie gives you a look across the table."
    image bonnie_stage11_49 = "/bonnie/events/stage11/49.webp"
    scene bonnie_stage11_49
    "Reluctantly picking up a slice of the large pizza, she begins forcing herself to eat."
    "After all she doesn’t want to be rude to Rebecca, given she still has the power to break off this entire partnership."
    image bonnie_stage11_50 = "/bonnie/events/stage11/50.webp"
    scene bonnie_stage11_50
    "Slowly picking at her food, Bonnie continues to eat - her stuffed belly complaining as she swallows each mouthful."
    image bonnie_stage11_51 = "/bonnie/events/stage11/51.webp"
    scene bonnie_stage11_51
    rebecca "Everything alright, Bonnie? You have barely touched your fries or onion rings."
    bonnie "Yeah, everything is fine."
    image bonnie_stage11_52 = "/bonnie/events/stage11/52.webp"
    scene bonnie_stage11_52
    "Despite the smile on her face, it is clear she is anything but fine."
    "Is Rebecca doing this on purpose? It definitely seems like she is enjoying watching Bonnie struggle."
    image bonnie_stage11_53 = "/bonnie/events/stage11/53.webp"
    scene bonnie_stage11_53
    "Somehow, and despite having already eaten half a shop's worth of food before dinner, Bonnie pushes the last handful of fries into her mouth."
    image bonnie_stage11_54 = "/bonnie/events/stage11/54.webp"
    scene bonnie_stage11_54
    rebecca "I can see why people rave about this place, the food is great."
    rebecca "Don’t you agree, Bonnie?"
    bonnie "Ughh, Yeah…it's really good."
    image bonnie_stage11_55 = "/bonnie/events/stage11/55.webp"
    scene bonnie_stage11_55
    "Covering her mouth, Bonnie stifles a burp."
    image bonnie_stage11_56 = "/bonnie/events/stage11/56.webp"
    scene bonnie_stage11_56
    "Her giant stomach almost trapping her against the table."
    image bonnie_stage11_57 = "/bonnie/events/stage11/57.webp"
    scene bonnie_stage11_57
    rebecca "Well, I better get a move on."
    rebecca "It was a pleasure to see you both."
    pc "Yeah, you too."
    image bonnie_stage11_58 = "/bonnie/events/stage11/58.webp"
    scene bonnie_stage11_58
    "Watching Rebecca leave, Bonnie lets out a groan as her hands rub her stomach."
    image bonnie_stage11_59 = "/bonnie/events/stage11/59.webp"
    scene bonnie_stage11_59
    bonnie "Oh god. I thought I was going to burst."
    bonnie "I need to get out of these clothes before I ruin them."
    stop music fadeout 1.0

    #### Bonnie's place###
    image bonnie_stage11_60 = "/bonnie/events/stage11/60.webp"
    scene bonnie_stage11_60
    play music "/music/bonnie.ogg" if_changed
    "As soon as you walk in Bonnie lets out another groan."
    image bonnie_stage11_61 = "/bonnie/events/stage11/61.webp"
    scene bonnie_stage11_61
    "No longer needing to act decently in public, she quickly drops her clothes - allowing her giant body to breathe and stretch freely."
    image bonnie_stage11_62 = "/bonnie/events/stage11/62.webp"
    scene bonnie_stage11_62
    "No longer held in by her clothes, her body looks even bigger."
    image bonnie_stage11_63 = "/bonnie/events/stage11/63.webp"
    scene bonnie_stage11_63
    bonnie "I bet you are loving this."
    pc "I’d be lying if I said I wasn’t a little."
    image bonnie_stage11_64 = "/bonnie/events/stage11/64.webp"
    scene bonnie_stage11_64
    bonnie "You couldn’t take your eyes off me when I was stuffing myself at Bunny Bites."
    pc "Ok, maybe I was enjoying it a lot."
    bonnie "That’s good, because maybe I was enjoying the attention."
    "Bonnie grabs you by the arm to take you to her bedroom."
    image bonnie_stage11_65 = "/bonnie/events/stage11/65.webp"
    scene bonnie_stage11_65
    "Once you arrive in her bedroom, Bonnie turns around and gives you a look."
    "The look she gives you when she wants something from you."
    if persistent.nosexscene == True:
        scene black with dissolve
        "Bonnie and I had a great time together."
        "You lie down on her bed."
        "You instantly fall asleep."
        image bonnie_stage11_70 = "/bonnie/events/stage11/70.webp"
        scene bonnie_stage11_70
        "You wake up early next morning."
        "Bonnie is still asleep next to you."
        window hide
        pause
        image bonnie_stage11_71 = "/bonnie/events/stage11/71.webp"
        scene bonnie_stage11_71
        "Not long after, Bonnie also wakes up."
        window hide
        pause
        bonnie "Oh, hello. I hope you slept well."
        image bonnie_stage11_72 = "/bonnie/events/stage11/72.webp"
        scene bonnie_stage11_72
        "You both have some casual talk about the day before."
        scene outside2
        stop music fadeout 1.0
        "After having breakfast together with Bonnie you take your leave."
        if recollection == False:
            $ daytime += 2
            $ phonecall = 1
            $ bonnie_ask_bigger = 1
            $ bonnie.weight += 2
        $ bonniestage11event = 0
        return
    image bonnie_stage11_66 = "/bonnie/events/stage11/66.webp"
    scene bonnie_stage11_66
    "She then moves over to her mirror."
    image bonnie_stage11_67 = "/bonnie/events/stage11/67.webp"
    scene bonnie_stage11_67
    "It is clear where she wants you to put your cock."
    image bonnie_stage11_69 = "/bonnie/events/stage11/69.webp"
    scene bonnie_stage11_69
    window hide
    pause
    "You move behind her, placing your hands on her gigantic ass and inserting your big dick in her wet pussy."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/bonnie/events/stage11/sex1.webm" loop
    show movie with dissolve
    "Both Bonnie and you start rocking your hips back and forth."
    window hide
    pause
    "The softness of her butt captures your attention - the layers of fat that are now covering her ass compressing every time they reach your hips."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/bonnie/events/stage11/sex2.webm" loop
    show movie with dissolve
    window hide
    pause
    "The mirror also gives you a perfect view of her big breasts and belly."
    "While thrusting, you hear the floor creaking as her huge bulging belly moves around."
    "Not long after, both of you reach your climaxes."
    stop movie
    image bonnie_stage11_68 = "/bonnie/events/stage11/68.webp"
    scene bonnie_stage11_68
    "You pull out and shoot your load all over her ass."
    window hide
    pause
    bonnie "That was great!"
    pc "Yeah, that was godly."
    "You lie down on her bed."
    scene black with dissolve
    "You instantly fall asleep."
    image bonnie_stage11_70 = "/bonnie/events/stage11/70.webp"
    scene bonnie_stage11_70
    "You wake up early next morning."
    "Bonnie is still asleep next to you."
    window hide
    pause
    image bonnie_stage11_71 = "/bonnie/events/stage11/71.webp"
    scene bonnie_stage11_71
    "Not long after, Bonnie also wakes up."
    window hide
    pause
    bonnie "Oh, hello. I hope you slept well."
    image bonnie_stage11_72 = "/bonnie/events/stage11/72.webp"
    scene bonnie_stage11_72
    "You both have some casual talk about the day before."
    scene outside2
    stop music fadeout 1.0
    "After having breakfast together with Bonnie you take your leave."
    if recollection == False:
        $ daytime += 2
        $ phonecall = 1
        $ bonnie_ask_bigger = 1
        $ bonnie.weight += 2
        $ librarianstage = 3
    $ bonniestage11event = 0
    return

label Bonnie_BB_Normal:
    image cafe_bonnie_booth = "/bonnie/[bonnie.stage]/cafe_booth.webp"
    scene cafe_bonnie_booth
    pc "Here you go. Have a nice meal."
    bonnie "Thank you!"
    return

label Bonnie_BB_Extra:
    image cafe_bonnie_extrafood = "/bonnie/[bonnie.stage]/cafe_extrafood.webp"
    scene cafe_bonnie_extrafood
    if bonnie.stage <= 5:
        bonnie "Oh, I'm sorry. I think this might be someone else's order. I didn't ask for this much."
        pc "Oh, are you ok to have this order at no extra cost?"
        bonnie "I'm not sure I can eat this much, and isn't someone else missing out if I take this?"
        pc "Not at all, it was just a mix up with your order."
        bonnie "Oh ok. It's a lot of food, but I guess if it's free I wont say no."
        pc "In that case, enjoy your meal."
        bonnie "Thanks."
        image cafe_bonnie_struggle = "/bonnie/[bonnie.stage]/cafe_struggle.webp"
        scene cafe_bonnie_struggle
        "A short while later you can see Bonnie struggling to finish the extra food you gave her."
        if secretfeedervol2 == 1:
            $ bonnie.weight += 0.5
        elif secretfeedervol1 == 1:
            $ bonnie.weight += 0.3
        else:
            $ bonnie.weight += 0.2

    elif bonnie.stage <= 9 and bonnie.stage >= 6:
        bonnie "Oh, I'm sorry. I think this might be someone else's order. I didn't ask for this much."
        pc "Oh, are you ok to have this order at no extra cost?"
        bonnie "I guess that would be ok."
        bonnie "I am pretty hungry. Although this is probably too much even for me."
        pc "In that case, enjoy your meal."
        bonnie "Thanks."
        image cafe_bonnie_struggle = "/bonnie/[bonnie.stage]/cafe_struggle.webp"
        scene cafe_bonnie_struggle
        "A short while later you see Bonnie has managed to finish the extra food you gave her."
        "Her appetite has clearly increased, as has the size of her belly."
        if secretfeedervol2 == 1:
            $ bonnie.weight += 0.7
        elif secretfeedervol1 == 1:
            $ bonnie.weight += 0.4
        else:
            $ bonnie.weight += 0.3

    elif bonnie.stage >= 10:
        bonnie "I think this might be someone else's order. I didn't ask for this much."
        pc "Oh. Are you okay to have this order at no extra cost?"
        bonnie "Sure. Although, I am starting to get the feeling you are doing this on purpose."
        pc "I'm not sure what you mean. Just an honest mistake with the orders."
        image cafe_bonnie_extrafood2 = "/bonnie/[bonnie.stage]/cafe_extrafood2.webp"
        scene cafe_bonnie_extrafood2
        bonnie "You are a terrible liar."
        bonnie "But if you are paying, mind bringing me an extra portion of onion rings?"
        pc "Sure thing. Coming right up."
        bonnie "Thanks."
        "Bringing her an extra double size portion of onion rings, Bonnie gives you a knowing look before digging into her giant meal."
        image cafe_bonnie_struggle = "/bonnie/[bonnie.stage]/cafe_struggle.webp"
        scene cafe_bonnie_struggle
        "A short while later you see Bonnie has managed to finish the extra food you gave her."
        "Her appetite has clearly increased, as has the size of her belly."
        if secretfeedervol2 == 1:
            $ bonnie.weight += 0.9
        elif secretfeedervol1 == 1:
            $ bonnie.weight += 0.6
        else:
            $ bonnie.weight += 0.4
    
    return

label Bonnie_BB_Prize:
    image cafe_bonnie_prize1 = "/bonnie/[bonnie.stage]/cafe_prize1.webp"
    scene cafe_bonnie_prize1
    "Creating a sizable feast, you approach Bonnie."
    pc "Congratulations Bonnie, you have won our new weekly prize!"
    image cafe_bonnie_prize2 = "/bonnie/[bonnie.stage]/cafe_prize2.webp"
    scene cafe_bonnie_prize2
    if bonnieprizefirsttime == 1:
        bonnie "I've won something, but I don't remember entering anything?"
        pc "It is an automatic entry with every order."
        pc "The winner gets to eat as much as they want, kind of like an all you can eat buffet."
        bonnie "Really, that is so generous!"
        bonnie "But I don't want to take advantage of you, I feel like it is almost cheating with how often I come here."
        pc "You don't need to worry about that, part of the reason Marie set it up was to give back to our most loyal customers."
        "You decide not to add why Marie was feeling so generous."
        bonnie "Amazing, please thank Marie for me."
        image cafe_bonnie_prize3 = "/bonnie/[bonnie.stage]/cafe_prize3.webp"
        scene cafe_bonnie_prize3
        "As you begin placing the food down, you can see Bonnie is a bit surprised to see quite how much is arriving."
        image cafe_bonnie_prize4 = "/bonnie/[bonnie.stage]/cafe_prize4.webp"
        scene cafe_bonnie_prize4
        "Stacking the food on the table, Bonnie picks up the first burger and starts eating."
        "Picking up a bit of everything, she moves around the different options."
        image cafe_bonnie_prize5 = "/bonnie/[bonnie.stage]/cafe_prize5.webp"
        scene cafe_bonnie_prize5
        "Soon you can see her stomach growing as she enjoys the fattening food."
        image cafe_bonnie_prize6 = "/bonnie/[bonnie.stage]/cafe_prize6.webp"
        scene cafe_bonnie_prize6
        "However, it doesn't take too long before she is forced to stop."
        image cafe_bonnie_prize7 = "/bonnie/[bonnie.stage]/cafe_prize7.webp"
        scene cafe_bonnie_prize7
        pc "How was the food?"
        bonnie "Amazing as usual, I am sorry I couldn't eat more."
        pc "I'll pack the rest up so you can take it home with you."
        bonnie "That would be great, thank you so much."
        image cafe_bonnie_prize8 = "/bonnie/[bonnie.stage]/cafe_prize8.webp"
        scene cafe_bonnie_prize8
        "Returning a few minutes later, you hand Bonnie two large bags of food to take home with her."
        "Leaving the restaurant a stuffed Bonnie gives you a wave as you return to the front counter."
        $ bonnieprizefirsttime = 0
    elif bonnie.stage <= 8:
        bonnie "Really, again? Are you sure?"
        pc "Yep, you have won it fair and square."
        bonnie "That is great, thank you!"
        image cafe_bonnie_prize3 = "/bonnie/[bonnie.stage]/cafe_prize3.webp"
        scene cafe_bonnie_prize3
        "As you begin placing the food down, you can see Bonnie is eagerly looking at it."
        image cafe_bonnie_prize4 = "/bonnie/[bonnie.stage]/cafe_prize4.webp"
        scene cafe_bonnie_prize4
        "Stacking the food on the table, Bonnie picks up the first burger and starts eating."
        "Moving her hands around the mountain of food, she picks and eats little bits of everything."
        image cafe_bonnie_prize5 = "/bonnie/[bonnie.stage]/cafe_prize5.webp"
        scene cafe_bonnie_prize5
        "Her stomach is clearly growing as she enjoys trying everything you have to offer."
        image cafe_bonnie_prize6 = "/bonnie/[bonnie.stage]/cafe_prize6.webp"
        scene cafe_bonnie_prize6
        "However, it doesn't take too long before she is forced to stop."
        image cafe_bonnie_prize7 = "/bonnie/[bonnie.stage]/cafe_prize7.webp"
        scene cafe_bonnie_prize7
        pc "How was the food?"
        bonnie "Amazing as usual, but I couldn't eat another bite."
        pc "I'll pack the rest up so you can take it home with you."
        bonnie "That would be great, thank you so much."
        image cafe_bonnie_prize8 = "/bonnie/[bonnie.stage]/cafe_prize8.webp"
        scene cafe_bonnie_prize8
        "Returning a few minutes later, you hand Bonnie two large bags of food to take home with her."
        "Leaving the restaurant a stuffed Bonnie gives you a wave as you return to the front counter."
    elif bonnie.stage == 9 or bonnie.stage == 10:
        bonnie "Are you sure you don't have anything to do with this?"
        bonnie "I feel like I win this slightly more than I should."
        pc "Maybe it isn't completely random."
        bonnie "Good, I enjoy how much you like seeing me eat."
        image cafe_bonnie_prize3 = "/bonnie/[bonnie.stage]/cafe_prize3.webp"
        scene cafe_bonnie_prize3
        "As you begin placing the food down, you can see Bonnie is eagerly looking at it."
        image cafe_bonnie_prize4 = "/bonnie/[bonnie.stage]/cafe_prize4.webp"
        scene cafe_bonnie_prize4
        "Giving you a knowing glance, Bonnie picks up the first burger and starts eating."
        "Eating quickly, she makes short work of the first few items."
        "Occasionally glancing at you to see if you are enjoying it, catching your eye she picks up the pace."
        "Enjoying the food and your attention, it fuels her gluttony as she eats more and more."
        image cafe_bonnie_prize5 = "/bonnie/[bonnie.stage]/cafe_prize5.webp"
        scene cafe_bonnie_prize5
        "Her stomach is growing larger with each bite of food."
        image cafe_bonnie_prize6 = "/bonnie/[bonnie.stage]/cafe_prize6.webp"
        scene cafe_bonnie_prize6
        "However, with only a few items remaining she is forced to stop."
        image cafe_bonnie_prize7 = "/bonnie/[bonnie.stage]/cafe_prize7.webp"
        scene cafe_bonnie_prize7
        pc "How was the food?"
        bonnie "Honestly, I think I ate it all so fast I forgot to pay attention to it."
        bonnie "Just look at this big belly of mine."
        pc "I'll pack the rest up so you can take it home with you."
        bonnie "That would be great, thank you so much."
        image cafe_bonnie_prize8 = "/bonnie/[bonnie.stage]/cafe_prize8.webp"
        scene cafe_bonnie_prize8
        "Returning a few minutes later, you hand Bonnie two large bags of food to take home with her."
        "Leaving the restaurant a stuffed Bonnie gives you a wave as you return to the front counter."
    elif bonnie.stage >= 11:
        bonnie "Mmm, I was just thinking about how hungry I was."
        image cafe_bonnie_prize3 = "/bonnie/[bonnie.stage]/cafe_prize3.webp"
        scene cafe_bonnie_prize3
        "As you begin placing the food down, you can see how excited Bonnie is."
        image cafe_bonnie_prize4 = "/bonnie/[bonnie.stage]/cafe_prize4.webp"
        scene cafe_bonnie_prize4
        "Giving you a knowing glance, Bonnie picks up the first burger and starts eating."
        "Eating at a steady pace, she makes short work of the first few items."
        "Her hands and mouth are never empty as she continually eats through the massive feast."
        "Enjoying the food and your attention, it fuels her gluttony as she eats more and more."
        image cafe_bonnie_prize5 = "/bonnie/[bonnie.stage]/cafe_prize5.webp"
        scene cafe_bonnie_prize5
        "Her stomach is growing larger with each bite of food."
        image cafe_bonnie_prize6 = "/bonnie/[bonnie.stage]/cafe_prize6.webp"
        scene cafe_bonnie_prize6
        "It takes a while, but the table is cleared of food."
        image cafe_bonnie_prize7 = "/bonnie/[bonnie.stage]/cafe_prize7.webp"
        scene cafe_bonnie_prize7
        bonnie "Good, but I don't think I am quite full enough."
        pc "What?"
        bonnie "The deal is I get to eat as much as I want right, or more accurately as much as you want."
        bonnie "Unless you think I am full enough?"
        pc "I'll got get some more food."
        bonnie "Perfect."
        image cafe_bonnie_prize9 = "/bonnie/[bonnie.stage]/cafe_prize9.webp"
        scene cafe_bonnie_prize9
        "Quickly ringing through another large order, you take it out to the waiting Bonnie."
        image cafe_bonnie_prize10 = "/bonnie/[bonnie.stage]/cafe_prize10.webp"
        scene cafe_bonnie_prize10
        "Despite her bulging belly, she immediately digs into the new food."
        "Still eating at a steady pace, she has to occasionally stop to rub her aching stomach."
        image cafe_bonnie_prize11 = "/bonnie/[bonnie.stage]/cafe_prize11.webp"
        scene cafe_bonnie_prize11
        "Despite giving it her best go, you see Bonnie slouch back, her stomach filled to bursting point."
        pc "Need anything else?"
        bonnie "Not this time, I think I might have overdone it."
        bonnie "My stomach is so tight right now, another bite and I might explode."
        pc "I'll pack the rest up so you can take it home with you."
        bonnie "That would be great, thank you so much."
        image cafe_bonnie_prize12 = "/bonnie/[bonnie.stage]/cafe_prize12.webp"
        scene cafe_bonnie_prize12
        "Returning a few minutes later, you hand Bonnie two large bags of food to take home with her."
        "Barely able to walk, a very stuffed looking Bonnie leaves and you get back to work."
    return