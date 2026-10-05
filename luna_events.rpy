## LUNA EVENTS
label Luna_Stage_3_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Luna', dialogue=dialogue_one)
    $ msg ("Hey [playername], I have something I want to show you.", who=1)
    pause
    $ msg ("Could you come over to my office?", who=1)
    menu:
        "Yes.":
            $ msg ("Your office? Where do you work?")
            pause
            $ msg ("At the hospital, just tell the receptionist you came to see me.", who=1)
            pause
            $ hide_messenger()

        "Not today.":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return

    image luna_stage3_1 = "/luna/events/stage3/1.webp"
    scene luna_stage3_1
    "Upon arriving at the hospital, you then immediately go to see the receptionist, a woman also wearing a nurse’s outfit and with red hair."
    natalie "How can I help you?"
    pc "Luna asked to see me."
    image luna_stage3_2 = "/luna/events/stage3/2.webp"
    scene luna_stage3_2
    natalie "Oh, you must be [playername]. Luna told us loads about you."
    natalie "Only good things of course."
    pc "She’s talked about me?"
    natalie "Yes, she seems to have taken a great liking to you, you must be doing something right if Luna holds you in such regard."
    pc "I’m glad that she does, I guess I’m just surprised is all."
    image luna_stage3_3 = "/luna/events/stage3/3.webp"
    scene luna_stage3_3
    natalie "Well, Luna has a way of seeing the potential in people."
    natalie "For example when I applied to work here, I was trying to get out of an abusive relationship which made me feel very bad about myself."
    natalie "I just needed a job so I could be able to afford to get out of that relationship and find someplace else to live."
    natalie "I didn’t think anyone would want to hire me, but Luna still saw something in me and hired me anyway."
    natalie "She will never know just how taking a chance on me and hiring me and giving me a fresh start in life made such an impact on my life."
    pc "That’s great that that happened to you and I had no idea Luna could be so caring. Then again I have to confess that I don’t really know her all that well yet."
    image luna_stage3_4 = "/luna/events/stage3/4.webp"
    scene luna_stage3_4
    natalie "Well, it seems Luna wants to get to know you better and sees something in you."
    natalie "I would agree that she is a caring person and genuinely wants to help others but that doesn’t mean people can get away with anything with her, she can also expect a lot."
    natalie "Fortunately at least the people that work here respect her enough that they are more than happy to try and meet her approval."
    pc "Well, I definitely do want to meet her approval myself. Thank you for the conversation."
    image luna_stage3_5 = "/luna/events/stage3/5.webp"
    scene luna_stage3_5
    natalie "You as well. Luna will be in her office. If you take the elevator to the top floor, Luna will be waiting for you there."
    pc "Thank you."
    image luna_stage3_6 = "/luna/events/stage3/6.webp"
    scene luna_stage3_6
    "While walking to the elevator you suddenly see two nurses rushing in with a patient on a stretcher."
    "The patient looks to be in a lot of pain."
    image luna_stage3_7 = "/luna/events/stage3/7.webp"
    scene luna_stage3_7
    "Before you get a chance to press the elevator button, another nurse rushes out towards the patient, leaving the elevator empty."
    "You enter the elevator and press the button to go up to the top floor."
    "After a while the elevator opens up, showing you a familiar face."
    image luna_stage3_8 = "/luna/events/stage3/8.webp"
    scene luna_stage3_8
    luna "Hey, [playername]. Good to see you here."
    luna "Come, I will take you to my office."
    "Following Luna to her office, you notice a sign saying Director L. Kendall."
    image luna_stage3_9 = "/luna/events/stage3/9.webp"
    scene luna_stage3_9
    luna "Here we are, welcome to my office."
    "She lets you inside and you look around at the quite nicely furnished office."
    "You are guessing that Luna is in charge of some of the hiring as a building manager or something, but this looks too nice for even such a role."
    pc "This is quite a nice office, I’m assuming that the owner of the hospital is letting you use it?"
    image luna_stage3_10 = "/luna/events/stage3/10.webp"
    scene luna_stage3_10
    luna "Haha, I am the owner."
    pc "You own this hospital?"
    "That was certainly surprising especially considering how young Luna looked. She seems to guess at what you are thinking."
    image luna_stage3_11 = "/luna/events/stage3/11.webp"
    scene luna_stage3_11
    luna "Yeah, I get that all the time. Let’s just say that my parents were quite wealthy and when they died I inherited a lot of money from them and used it to buy this hospital."
    luna "I didn’t want to just use the money to benefit myself and I wanted to also be able to help people."
    pc "That’s certainly very admirable."
    luna "Oh, it's not like I would consider myself to be some sort of saint. I do truly want to help people, but I also have to confess that I did it for my own personal desires."
    luna "If both things can be achieved, however; that would be ideal."
    pc "So what is it you hope to achieve?"
    "Luna takes off her blouse."
    image luna_stage3_12 = "/luna/events/stage3/12.webp"
    scene luna_stage3_12
    luna "I will get into that in a moment. You see, while we do everything a normal hospital does, we also host a research center that specializes in breast research."
    pc "Breast research? You mean like breast cancer research or something?"
    luna "That is indeed one thing we are hoping to eradicate with our research, but there is a lot more to it than that."
    image luna_stage3_13 = "/luna/events/stage3/13.webp"
    scene luna_stage3_13
    luna "You see, I've always been fascinated with the breasts on a woman; not only because of their sex appeal, but because of what they can do."
    luna "For example, how upon pregnancy and then eventual lactation they provide necessary nutrients to a baby."
    luna "Did you know that milk provides a baby with safety from different diseases?"
    pc "I can't say that I did, I don’t really have a medical background, but it is quite interesting."
    image luna_stage3_14 = "/luna/events/stage3/14.webp"
    scene luna_stage3_14
    luna "I won’t bore you with all the medical terminology you may not understand then."
    luna "Let’s just say that I was quite curious with just how this kind of protection was achieved and a woman’s body’s role in it."
    luna "It led me to buy this hospital and invest heavily into such research. It's taken us years to get to this point but I think we have finally gotten to the point where we can start testing."
    pc "What is it you are testing?"
    image luna_stage3_15 = "/luna/events/stage3/15.webp"
    scene luna_stage3_15
    luna "Only possibly one of the greatest scientific breakthroughs in the history of mankind! Well possibly, assuming it works as well as we hope it does, but I can’t help but be optimistic and excited."
    luna "I’ve developed a drug that will cause most accumulated fat to be stored in the breasts."
    luna "This will also hopefully have the side effect of eradicating certain diseases, breast cancer once again as an example."
    pc "Well, if you can achieve that, I can see why you would be excited!"
    image luna_stage3_16 = "/luna/events/stage3/16.webp"
    scene luna_stage3_16
    luna "For sure, I’m glad you can see the potential. I could tell very quickly that you could appreciate what I’m trying to achieve."
    pc "I wouldn't say that makes me special. Who wouldn't want breast cancer and other diseases eradicated?"
    luna "Oh, I believe that you are a lot more special than even you realize, I have a knack for being able to see the potential in people."
    pc "I’m not sure I see the potential you see but I’m certainly glad that you feel that way."
    image luna_stage3_17 = "/luna/events/stage3/17.webp"
    scene luna_stage3_17
    luna "Don't worry. You will eventually - or at least I hope so. For now, it is sufficient for you to know about your desire to help women eat more and gain weight."
    pc "I’m certainly not denying it."
    pc "I’ve loved seeing Daisy gain weight as the semester has gone on."
    pc "As well as the times that you’ve come to our class and eaten a lot."
    pc "Especially you putting on more weight each time that I see you."
    pc "You look super hot and sexy by the way if you don’t mind me saying."
    image luna_stage3_18 = "/luna/events/stage3/18.webp"
    scene luna_stage3_18
    luna "Not at all. Say it all you want to me. A woman likes being told that, but I think we can both agree that I should definitely put on a lot more."
    pc "It will only just mean there is more and more of you to love."
    luna "Indeed. I think you can also agree then that there are plenty of desirable qualities in a fat woman."
    luna "How she can eat whatever she wants and only have that add to her curves with more of her to love as you say."
    pc "Oh, definitely."
    image luna_stage3_19 = "/luna/events/stage3/19.webp"
    scene luna_stage3_19
    luna "When I was a child and then a teenager, my parents forced me to be in beauty pageants."
    luna "I was constantly being forced to starve myself and never got to eat what I wanted just to match someone else’s ideals of beauty."
    luna "Beauty, I eventually realized, was in the eye of the beholder and I find that a fat woman is far more beautiful than a stick figure and she gets to eat whatever she wants."
    pc "I couldn’t agree with you more. Also women should be allowed to eat and enjoy themselves and find themselves beautiful at any size."
    image luna_stage3_20 = "/luna/events/stage3/20.webp"
    scene luna_stage3_20
    luna "The only downside then would be potential health risks from getting fat but I’m working on that as well."
    luna "I want any woman to eat and gain as much as they want without having to worry about any of that."
    pc "That would be like a dream come true I think for a lot of people, including me."
    image luna_stage3_21 = "/luna/events/stage3/21.webp"
    scene luna_stage3_21
    luna "Haha, yeah, I just knew you would appreciate my vision, which is why I had you come here."
    luna "From what I've heard from Daisy, your teacher, and watching first hand how your potential has unfolded on her body with her recent massive weight gain,"
    luna "I've decided you are worthy in helping me achieve the same thing regarding weight gain. Only in my case, I'm hoping that the weight is concentrated much more in my breasts."
    luna "You see, I've decided to be the guinea pig in testing out the new drug that we've been developing first myself."
    luna "It isn’t considered safe yet for mass testing but someone needs to test it, and I figured I should be the one to take such a risk first."
    luna "As you can see, however, I'm already seeing some great results."
    image luna_stage3_22 = "/luna/events/stage3/22.webp"
    scene luna_stage3_22
    "Luna happily shows off her already quite a bit larger breasts with pride and satisfaction."
    pc "They really do look incredible."
    image luna_stage3_23 = "/luna/events/stage3/23.webp"
    scene luna_stage3_23
    window hide
    pause
    "Luna drops her skirt, showing that she wasn't wearing any panties."
    luna "They certainly are. I mean, I was already well endowed to begin with, but I just love them more and more the bigger they get."
    luna "I also hope that they get bigger... much, much bigger and I want you to help me grow them. In fact, I want you to help me grow all of me."
    pc "No way I could ever say no to that kind of offer. Of course I will help."
    luna "I figured you would easily agree. Well, why don't we start now?"
    pc "Well, I certainly can't think of a better thing to do with my time than help a beautiful woman stuff herself full of food and make her fatter and her breasts bigger."
    image luna_stage3_24 = "/luna/events/stage3/24.webp"
    scene luna_stage3_24
    "Luna then reaches into her desk and pulls out a bunch of food that she has apparently brought for the occasion."
    image luna_stage3_25 = "/luna/events/stage3/25.webp"
    scene luna_stage3_25
    window hide
    pause
    "There really is quite a lot of food there and you aren’t sure if Luna is even going to be able to eat all of it."
    "Luna does seem like the type to be more than willing to take on a difficult challenge."
    image luna_stage3_26 = "/luna/events/stage3/26.webp"
    scene luna_stage3_26
    luna "Ooh, it all just looks so delicious! You see, the side effects of the drug I'm testing are constant hunger and rapid digestion."
    luna "I definitely find that I’m eating a lot more than I used to, but of course I have no problem with that. It only makes me bigger, in particular these babies."
    image luna_stage3_27 = "/luna/events/stage3/27.webp"
    scene luna_stage3_27
    window hide
    pause
    "She happily and proudly squeezes her breasts and looks down at them."
    image luna_stage3_28 = "/luna/events/stage3/28.webp"
    scene luna_stage3_28
    luna "Are you ready to make these two even bigger? Would you like that?"
    pc "I would definitely like that."
    image luna_stage3_29 = "/luna/events/stage3/29.webp"
    scene luna_stage3_29
    window hide
    pause
    "Luna sits back down in her chair and looks at you."
    luna "Then let's get started. Feed me."
    image luna_stage3_30 = "/luna/events/stage3/30.webp"
    scene luna_stage3_30
    window hide
    pause
    "You are only too happy to oblige, picking up the first food item and placing it into Luna’s hungry mouth."
    image luna_stage3_31 = "/luna/events/stage3/31.webp"
    scene luna_stage3_31
    window hide
    pause
    "Luna happily begins eating, a smile on her face as she begins to indulge and enjoy herself, while you enjoy watching her and helping her eat."
    image luna_stage3_32 = "/luna/events/stage3/32.webp"
    scene luna_stage3_32
    window hide
    pause
    "After finishing a couple food items, Luna then asks:"
    luna "While you are feeding me, could you please tell me what you think of helping me eat and helping me get fatter?"
    image luna_stage3_33 = "/luna/events/stage3/33.webp"
    scene luna_stage3_33
    window hide
    pause
    "You are once again only too happy to oblige as you feed her while telling her what you think."
    pc "That’s right, my sexy glutton, eat and enjoy yourself, as much as you want and as much as your beautiful growing tummy can hold."
    pc "You are still much too skinny and you need all of this food to make you nice and fat and beautiful. That’s what you want, to be big and fat with absolutely gigantic boobs."
    image luna_stage3_34 = "/luna/events/stage3/34.webp"
    scene luna_stage3_34
    window hide
    pause
    "A moan from Luna as she eats tells you, you are doing great in talking about her like this. She already seems to be quite enjoying it."
    image luna_stage3_35 = "/luna/events/stage3/35.webp"
    scene luna_stage3_35
    window hide
    pause
    "You reach down and touch one of her breasts while you continue to feed her with the other hand."
    image luna_stage3_36 = "/luna/events/stage3/36.webp"
    scene luna_stage3_36
    pc "That’s right, these boobs of yours are going to grow, bigger than melons, bigger than watermelons, bigger than prized pumpkins."
    pc "Everyone will stare at just how truly massive they are wherever you go."
    luna "Mmm."
    image luna_stage3_37 = "/luna/events/stage3/37.webp"
    scene luna_stage3_37
    window hide
    pause
    pc "The rest of you will also continue to grow as well, making you not just a massively busty woman but a fat one as well."
    pc "With your belly growing to help increase the huge amounts of delicious food you can consume."
    pc "While your butt and hips and thighs will grow to help counterbalance the immense weight of your breasts."
    image luna_stage3_38 = "/luna/events/stage3/38.webp"
    scene luna_stage3_38
    window hide
    pause
    pc "Your butt will grow big enough that it eventually overflows either side of the desk chair that you now sit on while you continue to eat and add more and more sexy curves to your delicious body."
    image luna_stage3_39 = "/luna/events/stage3/39.webp"
    scene luna_stage3_39
    window hide
    pause
    "Luna stops eating for a moment and looks at you as hungrily as she does at the food."
    luna "Ooh, that kind of talk turns me on so much. It doesn't help that another side effect of the drug is that it seems to make me even more horny."
    pc "Well, I'm happy to help alleviate those sexual needs and desires of yours, but you have to finish eating first."
    image luna_stage3_40 = "/luna/events/stage3/40.webp"
    scene luna_stage3_40
    window hide
    pause
    luna "I’m just worried that if I keep eating I won’t be able to move and have sex afterwards."
    pc "I guess that’s your choice then. I would enjoy either decision."
    image luna_stage3_41 = "/luna/events/stage3/41.webp"
    scene luna_stage3_41
    window hide
    pause
    luna "Mmm, how about I eat all of it and then next time I can show you what all of this feeding me has done to my sexy body?"
    pc "Sounds great to me."
    image luna_stage3_42 = "/luna/events/stage3/42.webp"
    scene luna_stage3_42
    window hide
    pause
    "Luna then resumes eating and you resume helping her, you can tell she is getting full, but you encourage her to eat the last of the food that she ordered."
    image luna_stage3_43 = "/luna/events/stage3/43.webp"
    scene luna_stage3_43
    window hide
    pause
    pc "That’s right, you can do it, finish it all, every bite counts, just think every bite will only make you bigger."
    image luna_stage3_44 = "/luna/events/stage3/44.webp"
    scene luna_stage3_44
    window hide
    pause
    "Luna forces herself to finish the last of it with your encouragement and then sits back in her chair with a deep sigh."
    image luna_stage3_45 = "/luna/events/stage3/45.webp"
    scene luna_stage3_45
    luna "That was truly wonderful, thank you. I’m definitely glad I decided to involve you in all this."
    pc "Anytime, always happy to help."
    "You leave the stuffed Luna behind to digest all the food you fed her."

    if recollection == False:
        $ luna.weight += 1
        $ daytime += 1
        $ phonecall = 1
    $ lunastage3event = 0
    return

label Luna_Stage_4_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Luna', dialogue=dialogue_one)
    $ msg ("Hey, hottie. Care to meet me at the hospital again? There's something else I want to show you.", who=1)
    pause
    "The last time you met Luna at the hospital was certainly quite enjoyable, so you certainly hope this time will be as well. Knowing what you know of Luna so far it almost definitely will."
    pause
    menu:
        "Yes.":
            $ msg ("Sure, I’ll come right over.")
            pause
            $ hide_messenger()

        "Not today.":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return
    image luna_stage4_1 = "/luna/events/stage4/1.webp"
    scene luna_stage4_1
    "Upon getting to the hospital, you once again greet the receptionist you met last time."
    natalie "You can just go right ahead to see Luna. I'm assuming you remember where to go?"
    pc "Yes, I do. Thank you. I just figured I'd say hi to you on my way up."
    image luna_stage4_2 = "/luna/events/stage4/2.webp"
    scene luna_stage4_2
    natalie "Oh. Well, hi then!"
    pc "How are you doing today?"
    image luna_stage4_3 = "/luna/events/stage4/3.webp"
    scene luna_stage4_3
    natalie "I’m good, just surprised you are taking the time to talk to me is all."
    pc "I don’t see why I shouldn’t."
    image luna_stage4_4 = "/luna/events/stage4/4.webp"
    scene luna_stage4_4
    natalie "Maybe because most people tend to mostly ignore the receptionist unless they need something."
    natalie "Or because you have a really hot woman waiting for you to do…whatever it is you are going to do with her."
    natalie "I’m guessing that your relationship with Luna is not exactly business related."
    pc "With Luna I would say business and pleasure are often related."
    image luna_stage4_5 = "/luna/events/stage4/5.webp"
    scene luna_stage4_5
    natalie "Ha Ha, very true."
    pc "Anyway, I don’t see why I shouldn’t try and take the time to be nice to people regardless of their position."
    pc "Besides you play a valuable role here at the hospital, making sure everyone finds where they need to go."
    pc "Reassuring sick or injured patients or their friends and family, coordinating getting a nurse or doctor involved, all of that is extremely valuable and often thankless."
    image luna_stage4_6 = "/luna/events/stage4/6.webp"
    scene luna_stage4_6
    natalie "Thank you. Most people don't seem to recognize that. You honestly sound like Luna. She's always talking about how valuable each of us on her staff are."
    luna "That’s exactly right."
    image luna_stage4_7 = "/luna/events/stage4/7.webp"
    scene luna_stage4_7
    "The both of you turn to see Luna standing there. It's unclear just how long she has been standing there, but it's obvious that she at least overheard the last part of your conversation."
    pc "Hi Luna, I was just talking to your receptionist for a minute and then was coming to see you."
    image luna_stage4_8 = "/luna/events/stage4/8.webp"
    scene luna_stage4_8
    luna "Oh, I don't mind. In fact, I'm glad that you are doing so."
    luna "I appreciate you trying to help Natalie here with her self-worth. That just tells me that my assessment of you was well placed. You're a great person."
    pc "Thanks. I try. I feel like I can say the same thing about you."
    image luna_stage4_9 = "/luna/events/stage4/9.webp"
    scene luna_stage4_9
    "Luna brushed this compliment off as if it was no big deal."
    luna "Well, I try as well. So, are you ready to go?"
    pc "Sure."
    "Before beginning to follow Luna, however; you take a moment to say goodbye to Natalie, the receptionist."
    image luna_stage4_10 = "/luna/events/stage4/10.webp"
    scene luna_stage4_10
    pc "Well, I hope to see you later, Natalie."
    natalie "Yes, thank you, see you later."
    image luna_stage4_11 = "/luna/events/stage4/11.webp"
    scene luna_stage4_11
    "As you and Luna head up to her office, you notice a big, amused grin on Luna’s face."
    pc "What?"
    image luna_stage4_12 = "/luna/events/stage4/12.webp"
    scene luna_stage4_12
    luna "Do you have to go charming every woman you meet?"
    "Based on her grin and her tone she doesn’t seem annoyed or angry about it, just amused."
    pc "No, just trying to be nice is all. If I wanted to be charming then I would tell you how sexy you are."
    image luna_stage4_13 = "/luna/events/stage4/13.webp"
    scene luna_stage4_13
    luna "Not bad, but anyone could just say that to me. I'm an attractive woman after all. You're going to have to try a little harder than that."
    pc "How about I tell you that I’m hoping that this visit with you involves stuffing that sexy body of yours full of food to add even more to that sexy body of yours?"
    luna "That’s better, but is there anything else?"
    pc "I’m thinking you can definitely beat Daisy in your next eating competition with her, with my help of course."
    image luna_stage4_14 = "/luna/events/stage4/14.webp"
    scene luna_stage4_14
    luna "There, now that’s my kind of charm!"
    pc "Told you I knew how to charm you."
    luna "Well, keep it up and I'll be happy to keep you around."
    image luna_stage4_15 = "/luna/events/stage4/15.webp"
    scene luna_stage4_15
    luna "I definitely will be having you help me feast and enjoy myself today, but first things first I want you to meet the scientist that’s been working on the breast growth drug."
    luna "She’s also got another drug we recently produced that I think you will also be very interested in."
    pc "I’m not sure what kind of drug I could be as interested in as one that makes breasts grow, especially when it’s yours."
    image luna_stage4_16 = "/luna/events/stage4/16.webp"
    scene luna_stage4_16
    "Luna takes off her coat."
    luna "There's that charm again. No, you'll see. I promise you'll like it."
    luna "Now let's go to the scientist I was talking about."
    image luna_stage4_17 = "/luna/events/stage4/17.webp"
    scene luna_stage4_17
    "Luna takes you over to a lab of some sort where a woman is sitting at a computer, looking at a screen of various complicated math formulas that you have no hope of ever understanding."
    luna "How is the work going, Britta?"
    image luna_stage4_18 = "/luna/events/stage4/18.webp"
    scene luna_stage4_18
    "Britta, as concentrated on her work as she is, is startled at hearing Luna’s voice."
    britta "Uh great, it’s going great, just going over the formula composition, the chemical bonding that-"
    luna "We've got a visitor with us. Speak plain English, please."
    image luna_stage4_19 = "/luna/events/stage4/19.webp"
    scene luna_stage4_19
    britta "Oh, yes, right, well... It's kind of difficult to explain in simple terms."
    pc "Sorry, you can talk however the two of you want."
    luna "No, it's fine. Honestly, most of what she says goes over my head too. All I know is it works."
    image luna_stage4_20 = "/luna/events/stage4/20.webp"
    scene luna_stage4_20
    "Luna happily shows off her large breasts. It seems every time you see her they seem larger."
    britta "Would you like me to examine them again for you? Check to make sure that the treatment is going well?"
    luna "I’m thinking that I will let [playername] examine them for me later instead."
    pc "Definitely happy to help with that."
    luna "I figured you would."
    image luna_stage4_21 = "/luna/events/stage4/21.webp"
    scene luna_stage4_21
    "However, Britta couldn't help but stare at Luna's already enlarged bosom anyway, even though she was seemingly only looking at them from fascination and excitement."
    britta "Amazing how just simply growing those two guinea pig breasts of yours could be such a medical and scientific breakthrough."
    britta "Just think of the diseases we could cure with this research. Even I couldn't say for certain what the possibilities could be."
    image luna_stage4_22 = "/luna/events/stage4/22.webp"
    scene luna_stage4_22
    "Luna squeezes each of her breasts happily at that."
    luna "It really is quite exciting. So, when do you think we can start the next phase and have more human testing?"
    image luna_stage4_23 = "/luna/events/stage4/23.webp"
    scene luna_stage4_23
    britta "I want to make sure there are no further adverse side effects with you first. I didn't even advise that you start taking it, but you insisted."
    luna "Well, it has gone rather well so far. And honestly, the nurses that know what we are up to have seen the results on me and keep asking to try it themselves."
    britta "They keep asking me as well and I keep telling them no. I suppose we can start further human testing soon."
    image luna_stage4_24 = "/luna/events/stage4/24.webp"
    scene luna_stage4_24
    luna "Great! I'll let the nurses that want it tested on them know."
    britta "I didn’t mean that soon…by soon I meant-"
    luna "Would you not agree that all testing has risks and the only way to know for sure if something works is to test it and find out?"
    image luna_stage4_25 = "/luna/events/stage4/25.webp"
    scene luna_stage4_25
    britta "I suppose so. Well, you're the director and if those wanting to participate are aware of the risks and still want to proceed, I won't stop them."
    luna "I wouldn’t even suggest that they do so if I didn’t think it would be highly unlikely to be not safe."
    luna "I am after all taking it myself first so if something does happen it will happen to me first and not somebody else."
    image luna_stage4_26 = "/luna/events/stage4/26.webp"
    scene luna_stage4_26
    britta "I do admire that about you."
    britta "Perhaps as the developer of the drug I ought to test it on myself... to show my own faith in the drug and so I can have a better understanding and firsthand knowledge of what it does."
    luna "Are you sure it isn't because you secretly want a lot more up top? Come on, Britta. A woman who develops a breast growth drug and looks at mine like you do has to want that."
    image luna_stage4_27 = "/luna/events/stage4/27.webp"
    scene luna_stage4_27
    britta "It would purely be for scientific reasons... Well, not that I would say no to a larger... bosom."
    image luna_stage4_28 = "/luna/events/stage4/28.webp"
    scene luna_stage4_28
    luna "I knew it! You want huge breasts of your own, just admit it."
    image luna_stage4_29 = "/luna/events/stage4/29.webp"
    scene luna_stage4_29
    "Instead of answering, however, Britta just blushes and turns her head back to look at her computer."
    britta "I need to get back to work."
    image luna_stage4_30 = "/luna/events/stage4/30.webp"
    scene luna_stage4_30
    luna "I don't know why you feel like you can't admit it. You can grow huge boobs and cure a bunch of diseases at the same time. That's what I'm doing and I'm loving it."
    "Britta just ignores Luna and tries to focus on her work."
    image luna_stage4_31 = "/luna/events/stage4/31.webp"
    scene luna_stage4_31
    luna "Just letting you know then, Britta; I'm taking a dose of the muscle relaxant before I go."
    britta "Go ahead."
    "Luna goes over to a drawer and picks out a vial of green liquid and has you follow her out."
    image luna_stage4_32 = "/luna/events/stage4/32.webp"
    scene luna_stage4_32
    luna "Britta can try to deny it all she wants, but I can see she wants hers to grow. As for me, well..."
    pc "You are most definitely not denying it."
    luna "For sure, so come on back with me to my office so we can have some fun."
    image luna_stage4_33 = "/luna/events/stage4/33.webp"
    scene luna_stage4_33
    "Upon arriving in her office, you see a bunch of delivered food sitting there. It appears to be even more than last time."
    "You weren't sure how she could eat so much then, and you definitely don't think she can finish it this time."
    pc "I know you’re an impressive eater, but I’m not sure even you can eat all this."
    luna "Do you doubt me?"
    pc "Perhaps I should know by now to never doubt you."
    image luna_stage4_34 = "/luna/events/stage4/34.webp"
    scene luna_stage4_34
    luna "Very good. Well, normally you would be correct. I couldn't eat all of this, but I've come up with a way of eating far more than normal."
    luna "You see there is another drug that I’ve had developed that works as a stomach muscle relaxant."
    luna "You may not be aware that when a person feels full they in fact still have plenty more stomach capacity than that."
    luna "And they could keep eating if the stomach muscles didn't tighten up to prevent you from doing so. This drug helps in that regard."
    pc "Very cool, do you think I could get some of that?"
    luna "So you can better help fatten up other women?"
    pc "Guilty."
    luna "While I admire your dedication, sorry, but it isn't considered safe to the general public yet and I can't have it be used outside of this building until it's officially approved."
    pc "Shame."
    image luna_stage4_35 = "/luna/events/stage4/35.webp"
    scene luna_stage4_35
    window hide
    pause
    "Luna takes off her skirt."
    luna "You still get to use it on me though."
    pc "Oh. Well, that definitely sounds good to me."
    luna "I figured you would approve. Well, let's get started."
    image luna_stage4_36 = "/luna/events/stage4/36.webp"
    scene luna_stage4_36
    "She downs the vial of the stomach muscle relaxant and then looks hungrily at all the food."
    image luna_stage4_37 = "/luna/events/stage4/37.webp"
    scene luna_stage4_37
    window hide
    pause
    pc "What do you want first?"
    luna "Ooh, all of it. It just all looks so good."
    pc "Well, you're going to get to eat all of it, so it probably doesn't matter what you eat first."
    luna "True, bring on whatever you want to give me first."
    image luna_stage4_38 = "/luna/events/stage4/38.webp"
    scene luna_stage4_38
    window hide
    pause
    "Luna sits down in her chair, waiting for you to feed her."
    "You start by picking up the first food item and putting it into Luna’s hungry mouth and she happily begins chewing,"
    "Savoring and enjoying each bite, but still eating quickly as if she can’t wait to try the next delicious food you are going to give her."
    "As you feed her, you decide to once again indulge her other appetite and desires."
    image luna_stage4_39 = "/luna/events/stage4/39.webp"
    scene luna_stage4_39
    pc "That's right, more delicious food to add to your growing figure. You're still much too skinny and unable to beat Daisy in an eating contest."
    pc "Well, we're going to change all that. You're going to get nice and fat with gigantic boobs and enough eating capacity to destroy Daisy and show her who really is the best eater."
    image luna_stage4_40 = "/luna/events/stage4/40.webp"
    scene luna_stage4_40
    "Luna moans at hearing that, even as she is eating."
    pc "You’ll become the teacher in showing Daisy just how much a sexy woman can really eat."
    pc "Then all that food that you stuff yourself with, all that food that I’m stuffing you with right now will only add to your growing curves, especially your boobs."
    pc "I know you want them gigantic, beyond gigantic, I know you want-"
    image luna_stage4_41 = "/luna/events/stage4/41.webp"
    scene luna_stage4_41
    window hide
    pause
    "At that Luna can’t resist any longer as she plunges her hand down into her underwear to find her nether regions and finger herself."
    luna "Mmm, I just can’t help it."
    pc "Oh, no problem at all. Just as long as you keep eating."
    image luna_stage4_42 = "/luna/events/stage4/42.webp"
    scene luna_stage4_42
    "Luna continues to furiously finger herself even as she eats, while you continue to press more food into her face."
    "By this point she might have been too full to continue but the stomach muscle relaxant seemed to be doing it’s job as she continued."
    image luna_stage4_43 = "/luna/events/stage4/43.webp"
    scene luna_stage4_43
    pc "Not too far to go now, then you can stop with a truly full belly and pleasure yourself, or maybe let me do it for you as a reward for all your great effort eating."
    image luna_stage4_44 = "/luna/events/stage4/44.webp"
    scene luna_stage4_44
    window hide
    pause
    "You then notice Luna’s top seems to already be straining more than normal, almost as if the food that she has been eating is already being digested and stored in her breasts."
    "Is it possible to do so, so quickly?"
    image luna_stage4_45 = "/luna/events/stage4/45.webp"
    scene luna_stage4_45
    window hide
    pause
    pc "Looks like your breasts are already getting bigger, full of delicious fat made by all the food you are eating."
    image luna_stage4_46 = "/luna/events/stage4/46.webp"
    scene luna_stage4_46
    window hide
    pause
    "Luna grasps her enlarged breasts happily."
    luna "Yes! Bigger! Bigger and bigger!"
    image luna_stage4_47 = "/luna/events/stage4/47.webp"
    scene luna_stage4_47
    window hide
    pause
    "You feed her the last of the food and even as she does so, her top has finally had enough as it rips open, displaying her incredible cleavage."
    window hide
    pause
    $ movielength = 8
    $ movieplaying = "/images/luna/events/stage4/48.webm"
    call screen custommoviescreen
    image luna_stage4_49 = "/luna/events/stage4/49.webp"
    scene luna_stage4_49
    window hide
    pause
    luna "YES!!"
    "She stops, panting a little from the exertion."
    luna "Wow, that was great!"
    pc "It’s always a great time with you."
    image luna_stage4_50 = "/luna/events/stage4/50.webp"
    scene luna_stage4_50
    luna "Mmm, glad you think so. Only problem is I might have eaten too much again for sex."
    pc "That’s okay, just watching you eat was plenty of enjoyment for me."
    luna "I'm glad you liked it. You definitely deserve a reward though for helping stuff me so well."
    image luna_stage4_51 = "/luna/events/stage4/51.webp"
    scene luna_stage4_51
    window hide
    pause
    "She presents her enlarged boobs to you."
    luna "Well, you can at least feel up my boobs. After all, you did say that you would check them over for me."
    pc "Oh, definitely. I'm your official booby checker."
    image luna_stage4_52 = "/luna/events/stage4/52.webp"
    scene luna_stage4_52
    window hide
    pause
    "You look over Luna’s enlarged breasts and give them some nice squeezes."
    pc "They are getting so big already."
    image luna_stage4_53 = "/luna/events/stage4/53.webp"
    scene luna_stage4_53
    window hide
    pause
    luna "Oh, this is nothing. Just you wait."
    pc "Just how huge do you want them?"
    image luna_stage4_54 = "/luna/events/stage4/54.webp"
    scene luna_stage4_54
    luna "I'm not sure. I guess it depends on how massive you can help me make them."
    pc "Oh, is that so? It's up to me, huh?"
    image luna_stage4_55 = "/luna/events/stage4/55.webp"
    scene luna_stage4_55
    luna "Well, if you keep doing as good of a job as you already are, I'm expecting some truly massive results."
    pc "Oh, is that my role or my job to you then? Helping you eat lots of food and helping your breasts grow?"
    luna "Yes... among many other things. There is a lot I'm hoping you can accomplish."
    pc "Care to tell me what those things are?"
    image luna_stage4_56 = "/luna/events/stage4/56.webp"
    scene luna_stage4_56
    luna "Oh, you'll find out one of those things very soon, but I want it to be a surprise."
    pc "Could you at least give me a hint?"
    image luna_stage4_57 = "/luna/events/stage4/57.webp"
    scene luna_stage4_57
    luna "Haha, no, sorry, I will say you’ll really like it though and if you also do well with that there will be even more to look forward to from me."
    pc "Ooh, I like the sound of that."
    luna "Yes, there is a lot to look forward to for both of us."
    scene outside
    "You leave Luna and go back home."
    if recollection == False:
        $ luna.weight += 1
        $ daytime += 1
        $ phonecall = 1
    $ lunastage4event = 0
    return

label Luna_Stage_5_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Luna', dialogue=dialogue_one)
    $ msg ("Hey, hottie. Today is the day! I'm ready to show you that surprise I've been planning for you. Meet me at the hospital again.", who=1)
    pause
    menu:
        "Yes.":
            $ msg ("I’ll be there.")
            pause
            $ hide_messenger()

        "Not today.":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return

    image luna_stage5_1 = "/luna/events/stage5/1.webp"
    scene luna_stage5_1
    "Upon arriving at the hospital, you once again take a moment to say hi to Natalie the receptionist."
    pc "Hi, Natalie. How are you?"
    image luna_stage5_2 = "/luna/events/stage5/2.webp"
    scene luna_stage5_2
    "Natalie smiles warmly at you, as she seems to enjoy your visits. She also seems pretty excited and happy about something."
    natalie "I'm great. How are you?"
    pc "Good. Luna says she has a surprise for me today. Any idea what that is about?"
    image luna_stage5_3 = "/luna/events/stage5/3.webp"
    scene luna_stage5_3
    natalie "Yes. Well, at least I have a pretty good idea. Luna asked me not to tell you if you asked though. She loves her surprises."
    pc "Can’t you just give me a little hint?"
    natalie "Sorry. Luna made me promise that I wouldn't or I definitely would. I can't wait to talk to you about it afterwards once you find out."
    "You can tell whatever it is she is dying to tell you but her loyalty to Luna is preventing her."
    "You don’t want to pressure her any further if she really can’t tell you."
    pc "Alright. I get it. I guess I'll probably find out real soon from Luna anyway. Nice to see you by the way."
    image luna_stage5_4 = "/luna/events/stage5/4.webp"
    scene luna_stage5_4
    natalie "Nice to see you too. I’ll probably see you again real soon."
    image luna_stage5_5 = "/luna/events/stage5/5.webp"
    scene luna_stage5_5
    "Now really curious just what this is all about, you head up the elevator."
    image luna_stage5_6 = "/luna/events/stage5/6.webp"
    scene luna_stage5_6
    "Upon getting out, you find Luna waiting for you there again. This time she looks particularly excited about something."
    luna "Great you’re here!"
    pc "I’m here! So what’s going on?"
    image luna_stage5_7 = "/luna/events/stage5/7.webp"
    scene luna_stage5_7
    luna "We’re going to start the next phase of testing the drug!"
    pc "Really? That’s awesome!"
    image luna_stage5_8 = "/luna/events/stage5/8.webp"
    scene luna_stage5_8
    luna "Yes! It's finally happening! I've got four of the nurses to agree to take it. Actually, they were quite eager about it."
    luna "And then of course Britta, the scientist who did much of the work in creating it and whom you've already met."
    pc "So, is that the surprise you were planning for me? For me to get to see the drug tested on other women?"
    image luna_stage5_9 = "/luna/events/stage5/9.webp"
    scene luna_stage5_9
    luna "Not just that. How would you like another part-time job as my assistant in the drug trials?"
    "You are definitely surprised by the offer."
    pc "Well, I certainly appreciate it. But why me? I'm not a scientist or a doctor or anything. I wouldn't say I'm qualified."
    image luna_stage5_10 = "/luna/events/stage5/10.webp"
    scene luna_stage5_10
    luna "I don't care about that. I already have Britta, myself, and the nurses involved for the science and the medicine."
    luna "What I do need you for and what you’ve proven to be quite good at is encouragement."
    luna "Nothing makes me want to eat more and more or gain and grow like you do and I know that you are already succeeding with other women too."
    luna "I want you to do the same for each of the additional test subjects."
    pc "I suppose I have had some success with that as of late, although I never would have thought it would get me a job."
    image luna_stage5_11 = "/luna/events/stage5/11.webp"
    scene luna_stage5_11
    luna "No need to be so modest about it. Just looking at me could tell you that you are already having great success."
    "Looking over Luna’s already much more curvy body, especially her now huge breasts, she did have a point, and it certainly wasn’t just Luna that you had been lucky enough to see fatten up."
    image luna_stage5_12 = "/luna/events/stage5/12.webp"
    scene luna_stage5_12
    luna "There will of course be more to it than just helping fatten them up. I also want you to monitor their progress, take continual measurements and record their growth."
    luna "Check up on them to see how they are doing and if they report any side effects to the drug."
    luna "Help them eat, give advice and support, and also really get to know them and make them feel good about what they are going through."
    luna "Then of course report all of your findings to me although I will likely be with you for most of that time."
    pc "Well, that sounds like a total dream job."
    image luna_stage5_13 = "/luna/events/stage5/13.webp"
    scene luna_stage5_13
    luna "Great. I knew you would accept."
    pc "Not like I could ever say no to an offer like that. I'll do my best."
    luna "I know you will."
    "You can’t resist teasing Luna a little though."
    pc "Only thing is what if I do too good of a job and you end up with some serious competition?"
    image luna_stage5_14 = "/luna/events/stage5/14.webp"
    scene luna_stage5_14
    luna "Oh no, I'm not worried about that. I want everyone to reach their full potential. In this case, I want you to make each of them as fat and curvy with the biggest breasts you can."
    luna "As for the competition; you should know by now I'm not scared of some competition. I'm still going to be the biggest by a wide margin."
    pc "With my help you will."
    luna "That's what I'm counting on. Now, let's have you meet our test subjects."
    image luna_stage5_15 = "/luna/events/stage5/15.webp"
    scene luna_stage5_15
    "You follow Luna into a examination room where Britta is instructing four different nurses."
    "You think they are nurses as they are wearing nurses uniforms but they are very revealing."
    "Luna probably just isn’t at all concerned about the lax dress code, which knowing Luna isn’t too surprising, especially given the outfits she herself usually wears."
    image luna_stage5_16 = "/luna/events/stage5/16.webp"
    scene luna_stage5_16
    "You do however recognize one of the test subjects, Natalie the receptionist, who smiles and waves at you."
    "No wonder she was so excited earlier and eager to tell you what is going on; she got selected to be one of the test subjects."
    "Luna waits until Britta is done explaining the process."
    image luna_stage5_17 = "/luna/events/stage5/17.webp"
    scene luna_stage5_17
    luna "[playername], these are the nurses that also have agreed to be test subjects in the drug trial: Nurses Roxie, Natalie, whom you already know, Charlene and Sally."
    "The first nurse you don't already know, Roxie, you notice has dark brown hair and the brightest green eyes that you’ve ever seen."
    "Charlene has black hair and dark skin, and Sally has short, dark brown hair."
    "All of them look nervous but also excited to be here."
    image luna_stage5_18 = "/luna/events/stage5/18.webp"
    scene luna_stage5_18
    luna "Girls, this is [playername]. He is the new assistant of mine I was telling you about. He's going to be helping me and Britta out as well as each of you with the drug trial."
    "Charlene, the dark skinned nurse seemed to have some problems with that."
    image luna_stage5_19 = "/luna/events/stage5/19.webp"
    scene luna_stage5_19
    charlene "Wait, I didn’t realize that it was a man you were bringing in."
    charlene "I thought this whole thing was supposed to be just us women? Also why him? He doesn’t seem to be a doctor or a scientist or anything."
    "You were afraid of this as it was the same initial concerns you had, and you open your mouth to speak, but Luna touches your arm and looks at you as if to say she will handle this."
    luna "You’re right, he isn’t a doctor or a scientist, but the skills that he does have I believe will be extremely important going forward if we are to succeed."
    luna "And I hope each of you will soon see the value that he brings. I think even he doesn't really understand his value yet."
    luna "What I will say however is that I wouldn’t bring him in if I didn’t think it would greatly benefit each of you and the project."
    image luna_stage5_20 = "/luna/events/stage5/20.webp"
    scene luna_stage5_20
    "Natalie also spoke up to vouch for you."
    natalie "I think that it's a great idea to be bringing him in. He seems like a really nice guy from already meeting him. And Luna, if you think that bringing him in will help, then I'm all for it."
    natalie "You know I would do anything for you or for the success of the drug."
    luna "Thank you, Natalie. I appreciate the support."
    image luna_stage5_21 = "/luna/events/stage5/21.webp"
    scene luna_stage5_21
    "Britta the scientist of course also seemed to feel this way."
    britta "Yes. The success of the project should come first."
    "The nurse with bright green eyes named Roxie spoke up."
    image luna_stage5_22 = "/luna/events/stage5/22.webp"
    scene luna_stage5_22
    roxie "Whatever. I don't care as long as I get to take the drug and make my tits bigger."
    "Sally the nurse on the far right then gave her opinion."
    image luna_stage5_23 = "/luna/events/stage5/23.webp"
    scene luna_stage5_23
    sally "I don’t care either, just as long as this means I get to eat whatever I want and not have to worry about health problems. If he wants to help me do that then I’m all for it."
    "Charlene still didn't seem to like having you on the team, but seemingly relented at the last minute."
    image luna_stage5_24 = "/luna/events/stage5/24.webp"
    scene luna_stage5_24
    charlene "Very well. I still have to confess that I don't like it, but I won't object further. Let's just get to the testing."
    image luna_stage5_25 = "/luna/events/stage5/25.webp"
    scene luna_stage5_25
    luna "Great. I'm glad that's resolved. Anyway, I think we can get started then. Britta, I'm assuming that you've got everything ready?"
    britta "Of course. How about I administer the drug to all the test subjects first?"
    britta "Then you and [playername] can monitor them and me to see if there are any initial side effects or reactions as well as get their initial measurements."
    luna "Sounds like a plan. Then I can administer the drug to you last and do the same for you."
    if persistent.needles:
        "The test subject have to drink a serum containing the drug."
    else:
        image luna_stage5_26 = "/luna/events/stage5/26.webp"
        scene luna_stage5_26
        "Britta had already picked up a large needle and a syringe with a dose of what appeared to be a white substance inside."
        britta "Now then, who wants to be first?"
        image luna_stage5_27 = "/luna/events/stage5/27.webp"
        scene luna_stage5_27
        natalie "Me! I’ll do it!"
        luna "I guess I should have expected you to volunteer first, Natalie. Well, go right ahead."
        image luna_stage5_28 = "/luna/events/stage5/28.webp"
        scene luna_stage5_28
        "Natalie stepped forward and held out her arm while Britta held out the dose of the drug and prepared to inject it into her."
        natalie "One small step for man, one giant leap for mankind."
        "She seemed to be trying to quote Neil Armstrong, when he was the first man to step on the moon."
        "Which to be fair if all went well this could prove to be just as momentous an occasion, but that remained to be seen."
        "Luna however decided to edit the quote."
        image luna_stage5_29 = "/luna/events/stage5/29.webp"
        scene luna_stage5_29
        luna "You mean one small step for a woman, and one giant leap for womankind."
        sally "Girl power!"
        image luna_stage5_30 = "/luna/events/stage5/30.webp"
        scene luna_stage5_30
        "Britta then injected the dose of the drug into Natalie’s arm."
        "You were sure that it had to hurt, but Natalie was still smiling nonetheless as if the pain was nothing in comparison to how important doing this was."
        "After the drug was fully administered, Natalie gave a small cheer of triumph."
        image luna_stage5_31 = "/luna/events/stage5/31.webp"
        scene luna_stage5_31
        natalie "It’s done!"
        luna "Congratulations! This really is so exciting to watch."
        britta "This is only the beginning too. I can't imagine what we will be able to accomplish in time. So, who is next?"
        image luna_stage5_32 = "/luna/events/stage5/32.webp"
        scene luna_stage5_32
        roxie "I am."
        image luna_stage5_33 = "/luna/events/stage5/33.webp"
        scene luna_stage5_33
        "Britta then got out another syringe and needle and got another dose of the drug ready."
        image luna_stage5_34 = "/luna/events/stage5/34.webp"
        scene luna_stage5_34
        "One by one each of the nurses and then Britta herself was injected with the drug."
        window hide
        pause
        image luna_stage5_35 = "/luna/events/stage5/35.webp"
        scene luna_stage5_35
        pause
    image luna_stage5_36 = "/luna/events/stage5/36.webp"
    scene luna_stage5_36
    britta "Now we monitor for potential side effects."
    roxie "Well, other than my arm hurting, I do feel more hungry than I did before."
    luna "That's indeed one of the side effects. Don't worry though. I've got that covered and I'll make sure each of you are well fed."
    luna "But it's probably best if we wait half an hour and monitor for other unforeseen side effects before we do so."
    sally "I can't wait to start eating. I feel like I've starved myself all my life. And for what? I just want to eat and enjoy myself."
    luna "So you shall. From now on each of you will be provided with extra, extra large meals while at work."
    luna "Money for extra food expenses and a budget for new clothes, when you outgrow yours, will also be provided."
    image luna_stage5_37 = "/luna/events/stage5/37.webp"
    scene luna_stage5_37
    sally "Really? That’s great!"
    luna "The more you eat and the bigger that you get the more likely the chances of having success."
    natalie "I’ll eat as much as I can then."
    sally "I will too."
    roxie "We all will."
    image luna_stage5_38 = "/luna/events/stage5/38.webp"
    scene luna_stage5_38
    britta "Well, I think it is still too early to start eating so soon after the drug was administered, but we can probably start getting initial measurements now."
    luna "[playername], would you like to do that with at least a couple of them while I get the rest?"
    "Of course you would like to do that but you aren’t sure all the nurses will."
    "Charlene in particular doesn’t seem at all willing to have you anywhere near her body and measure her, especially if she is going to be naked."
    "She looks like she might kill you if you even suggest it."
    pc "Um, I’m not sure that is a good idea."
    luna "You forget you’re in a hospital, seeing people naked happens a lot."
    roxie "Yeah. We're more than used to it. Although, we aren't usually the ones naked though."
    natalie "It is admittedly different when you’re the one that's a patient, but I don’t mind if he measures me."
    luna "Thank you, Natalie. Why don't the two of you go into the room next door where I had a lot of food brought in? Once you're done, it should be safe to start eating by then."
    natalie "Sounds great. Thanks, Luna."
    image luna_stage5_39 = "/luna/events/stage5/39.webp"
    scene luna_stage5_39
    "You follow Natalie into the room next door."
    natalie "So, how long have you known Luna?"
    pc "Not long. But I feel like I already know her really well but also not know her at all, if that makes sense."
    image luna_stage5_40 = "/luna/events/stage5/40.webp"
    scene luna_stage5_40
    natalie "Makes sense to me. I've known Luna for years and I know her personality really well, but I also feel like there is a lot to her that remains a mystery."
    natalie "What I do know of her though is that she is one of the best people that I’ve ever met."
    natalie "She is so dedicated to helping people, even taking on patients that would have no hope of recovery anywhere else."
    natalie "But I know she wants to achieve more than that, curing currently incurable diseases and even making it so people don’t even get sick in the first place."
    natalie "This drug trial is a major step in achieving that goal and I’m so excited she selected me to be a part of it."
    pc "Is that why you wanted to be part of the trial group? That’s admirable."
    image luna_stage5_41 = "/luna/events/stage5/41.webp"
    scene luna_stage5_41
    natalie "Yes. I really want to make a difference. Once I started working here as a receptionist and saw the difference we were making, I've been working towards getting my nursing degree."
    natalie "Luna has been helping me a lot with that as well as some of the other nurses."
    natalie "I just barely started as a nurse-in-training while also working as a receptionist but I’m hoping to eventually become a full-fledged nurse."
    pc "Well, good for you. I'm sure you will do great at it."
    image luna_stage5_42 = "/luna/events/stage5/42.webp"
    scene luna_stage5_42
    natalie "Thanks, I certainly hope so, but for right now I think doing the drug trial is the most important thing."
    natalie "I would say each of the nurses feels the same way although they have other reasons as well for wanting to be part of the test group."
    pc "Well, it seems like Sally just wants to be able to eat as much as she wants."
    pc "Roxie just wants much bigger breasts, and Britta I think secretly wants that too as well as just being interested in the science aspect to it."
    natalie "Very good. At least you know most of our motivations by now."
    pc "I have no idea about Charlene though."
    image luna_stage5_43 = "/luna/events/stage5/43.webp"
    scene luna_stage5_43
    natalie "Ah, Charlene is doing it because she is at high risk for a certain disease that also killed her mother. She’s hoping that taking the drug will prevent her from also getting it."
    pc "Ah, that’s a real shame about her mother but hopefully the drug will prevent her from getting sick as well. She doesn’t seem to like me very much though."
    natalie "No, I imagine that she wouldn't. Don't take it personally. She has just had some bad experiences with men in the past, kind of like me with my ex."
    natalie "So she doesn’t like them at all. We usually have to just give her female patients."
    pc "I see. Well, hopefully I can eventually show her that not all men are bad."
    image luna_stage5_44 = "/luna/events/stage5/44.webp"
    scene luna_stage5_44
    natalie "I'd like to think so. You've certainly changed my opinion. You seem like such a great guy and not at all like my ex."
    pc "Well, I'm glad that I've been able to make you feel that way about me."
    natalie "Luna is a lucky woman to have you."
    pc "Oh, I suppose so. Although, I would say that I'm the lucky one."
    image luna_stage5_45 = "/luna/events/stage5/45.webp"
    scene luna_stage5_45
    natalie "Yeah. Luna is an amazing woman, that's for sure. So, are you two...?"
    pc "Oh, no. Well, not exactly. I mean, I suppose we are a thing and we do hook up, but it's not exclusive or anything like that. We are both free to be with other people."
    natalie "I see."
    image luna_stage5_46 = "/luna/events/stage5/46.webp"
    scene luna_stage5_46
    "She seems to be thinking about something, but instead seems to reject whatever she was thinking about."
    natalie "So shall we get started?"
    pc "Sure."
    image luna_stage5_47 = "/luna/events/stage5/47.webp"
    scene luna_stage5_47
    "Natalie then begins stripping and removes all of her clothes, standing naked in front of you."
    "You try not to look too much but Natalie admittedly does have an attractive body."
    "She however still notices you admiring her body anyway."
    image luna_stage5_48 = "/luna/events/stage5/48.webp"
    scene luna_stage5_48
    natalie "Is it nice? My body?"
    pc "Um yes, it’s very nice."
    natalie "I'm glad although you should probably know it isn’t normally acceptable for a doctor or a nurse to look at a patient in such a way."
    pc "Sorry. I didn't mean to-"
    image luna_stage5_49 = "/luna/events/stage5/49.webp"
    scene luna_stage5_49
    natalie "I did say normally, however since you aren’t a doctor or a nurse and I happen to be the patient and this is my body then I’m totally okay with you staring."
    natalie "You’re going to be seeing me naked a lot anyway. Look all you want."
    "You cautiously do so."
    image luna_stage5_50 = "/luna/events/stage5/50.webp"
    scene luna_stage5_50
    "Natalie then looked over her body herself for a long moment."
    natalie "It is admittedly still hard to imagine just how drastically my body is going to change though."
    pc "Are you okay with that?"
    image luna_stage5_51 = "/luna/events/stage5/51.webp"
    scene luna_stage5_51
    natalie "Yes. I'm committed to doing anything that is necessary for the success of the project."
    pc "I know that but…do you want the changes to your body?"
    image luna_stage5_52 = "/luna/events/stage5/52.webp"
    scene luna_stage5_52
    natalie "I'm not really sure to be honest. I guess I just haven't allowed myself to think much about my appearance for a long time. I haven't dated anyone since my abusive ex years ago."
    natalie "He always said I was too plain and nobody else would want to be with me."
    image luna_stage5_53 = "/luna/events/stage5/53.webp"
    scene luna_stage5_53
    "A few tears came to her eyes."
    pc "That is totally false. You really are incredibly beautiful. I don't see how anyone could ever say that to you. Your ex was a total liar and a real jerk to you."
    image luna_stage5_54 = "/luna/events/stage5/54.webp"
    scene luna_stage5_54
    "That brought a smile to Natalie’s face."
    natalie "You really think so?"
    pc "Definitely."
    image luna_stage5_55 = "/luna/events/stage5/55.webp"
    scene luna_stage5_55
    natalie "Do you think I would look even more attractive if there was…more of me? Like when I get bigger and fatter?"
    pc "If you are asking me, then the answer once again is definitely. But you should do what makes you happy."
    natalie "Well, since the success of the project requires that I gain weight and make my boobs grow and I'm fully committed to seeing it succeed, then I guess it's going to happen either way."
    natalie "So I’m glad that you’re going to like it."
    image luna_stage5_56 = "/luna/events/stage5/56.webp"
    scene luna_stage5_56
    "She looks into your eyes and starts to lean in to kiss you, but then pulls back."
    image luna_stage5_57 = "/luna/events/stage5/57.webp"
    scene luna_stage5_57
    natalie "Sorry."
    pc "It’s okay."
    natalie "I think this might just be that side effect of the drug that Luna warned us about. She did say it could make you more horny."
    pc "Right."
    image luna_stage5_58 = "/luna/events/stage5/58.webp"
    scene luna_stage5_58
    natalie "Well, we really should get those measurements."
    pc "Yeah, we probably should."
    image luna_stage5_59 = "/luna/events/stage5/59.webp"
    scene luna_stage5_59
    "You start by having Natalie get on the scale to check her weight and read what it says on the scale."
    if persistent.imperial:
        pc "You weigh 163 lbs."
    else:
        pc "You weigh 74 kg."
    image luna_stage5_60 = "/luna/events/stage5/60.webp"
    scene luna_stage5_60
    window hide
    pause
    "You get out the measuring tape and measure first Natalie’s hips, then her waist, and finally her bust, writing down what you got on a clipboard that Luna had provided earlier."
    "Even though you are clearly very close to Natalie’s body, even lightly touching it while getting her measurements, she doesn’t seem to mind."
    if persistent.imperial:
        pc "Let’s see you’ve got 41 and a half inch hips, about a 24 inch waist, and with your bust and underbust measurements you’re a 30C."
    else:
        pc "Let’s see you’ve got 105.4 cm hips, about a 61 cm waist, and with your bust and underbust measurements you’re a 30C."
    image luna_stage5_61 = "/luna/events/stage5/61.webp"
    scene luna_stage5_61
    "After getting her breasts measured, Natalie lifts them up and looks them over."
    natalie "You know, I am finding that I do want to see them get a lot bigger. I have to confess that it more than turns me on just thinking about it."
    pc "Well, there's nothing wrong with that."
    natalie "I mean, I've been watching the way that Luna's has already been growing and thinking about my own boobs growing like that..."
    pc "I have quite enjoyed watching and helping Luna grow hers along with the rest of her and I have to confess I definitely will with you as well."
    image luna_stage5_62 = "/luna/events/stage5/62.webp"
    scene luna_stage5_62
    natalie "Mmm, sounds good. Well, perhaps I should start right now then, I feel like I'm starving."
    pc "You can probably start eating by now, it’s been long enough."
    "Natalie puts on her clothing and takes her leave."
    image luna_stage5_63 = "/luna/events/stage5/63.webp"
    scene luna_stage5_63
    natalie "I certainly will…also thank you…for the conversation, it’s been quite helpful."
    pc "You're welcome. I'm glad I was able to help."
    image luna_stage5_64 = "/luna/events/stage5/64.webp"
    scene luna_stage5_64
    "Natalie then goes over to the room where the food is to start eating and you see that Nurse Roxie is already waiting for you."
    pc "I’m guessing that you’re up next?"
    roxie "Yes. You two certainly took a long time."
    pc "Yeah, sorry about that. I was trying to help her with something."
    image luna_stage5_65 = "/luna/events/stage5/65.webp"
    scene luna_stage5_65
    roxie "Trying to help Natalie get more in touch with her sexuality?"
    pc "How did you know?"
    roxie "Just a guess. Call it a nurse's intuition. Thank you for that by the way. I keep telling Natalie that she needs to open up more in that regard."
    pc "Well, I wasn't trying to force her into anything... just maybe make her think and decide what she wants."
    image luna_stage5_66 = "/luna/events/stage5/66.webp"
    scene luna_stage5_66
    roxie "That’s all I’ve been trying to do. Well, as for me, I already know what I want."
    pc "Bigger boobs."
    image luna_stage5_67 = "/luna/events/stage5/67.webp"
    scene luna_stage5_67
    roxie "Yes. Is that so wrong?"
    pc "Not at all. I will admit to liking very well endowed women myself. And if you want to be bigger up top, then I obviously have no problem with that."
    roxie "Well, seeing as how I know you're already doing it with Luna I would say so."
    pc "Do I need to deny it now that she is technically my boss?"
    image luna_stage5_68 = "/luna/events/stage5/68.webp"
    scene luna_stage5_68
    roxie "I doubt anyone cares enough to report you, so I would say you're safe. Anyway, as soon as I saw the effects that the drug was having on Luna and her tits I knew I had to have it for myself."
    pc "I suppose congratulations are in order then, since you managed to get in the drug trial and you just got injected with it."
    roxie "I did indeed."
    image luna_stage5_69 = "/luna/events/stage5/69.webp"
    scene luna_stage5_69
    "She happily touches her boobs."
    roxie "So, should we proceed with you measuring me?"
    pc "Sure."
    image luna_stage5_70 = "/luna/events/stage5/70.webp"
    scene luna_stage5_70
    "Roxie then strips naked for you and allows you to weigh and measure her."
    if persistent.imperial:
        pc "You weigh 141 lbs."
    else:
        pc "You weigh 64 kg."
    image luna_stage5_71 = "/luna/events/stage5/71.webp"
    scene luna_stage5_71
    "After measuring her, you tell her her measurements."
    if persistent.imperial:
        pc "You’ve got nearly 37 inch hips, a 22 inch waist, and your breasts are a 30D."
    else:
        pc "You’ve got nearly 94 cm hips, a 55.9 cm waist, and your breasts are a 30D."
    image luna_stage5_72 = "/luna/events/stage5/72.webp"
    scene luna_stage5_72
    roxie "Do you want to measure my tits again, just to be sure?"
    pc "Well, I guess if you want me to that's fine."
    "Of course you don’t have a problem with that."
    image luna_stage5_73 = "/luna/events/stage5/73.webp"
    scene luna_stage5_73
    "As you measure her boobs again you can’t help but lightly touch one of them."
    "Roxie doesn’t seem to mind however."
    image luna_stage5_74 = "/luna/events/stage5/74.webp"
    scene luna_stage5_74
    roxie "You can touch them some more if you want?"
    pc "Not that I don’t want to, but are you sure?"
    image luna_stage5_75 = "/luna/events/stage5/75.webp"
    scene luna_stage5_75
    roxie "Yes, if in exchange you tell me how Luna’s boobs feel."
    pc "I mean, I'd be happy to tell you, but you could just ask her if you can feel them for yourself. She would probably be happy to let you."
    image luna_stage5_76 = "/luna/events/stage5/76.webp"
    scene luna_stage5_76
    roxie "I’m sure she would, other than the fact that she is my boss."
    pc "Hey, if you aren't going to tell on me, then I won't tell on you. I also doubt that Luna will say anything."
    pc "Besides, you could argue that it's purely for scientific purposes as both of you are now part of the drug trial."
    roxie "Great point. Well, then I would definitely say that you've earned getting to feel up my tits."
    image luna_stage5_77 = "/luna/events/stage5/77.webp"
    scene luna_stage5_77
    window hide
    pause
    "You happily do so, lifting up and squeezing Roxie’s boobs."
    "She clearly is turned on by you doing so."
    image luna_stage5_78 = "/luna/events/stage5/78.webp"
    scene luna_stage5_78
    window hide
    pause
    roxie "Ooh, I hope that they are just as sensitive when they get a lot bigger."
    luna "Possibly more so in my own experience."
    image luna_stage5_79 = "/luna/events/stage5/79.webp"
    scene luna_stage5_79
    "You turn around to see Luna standing there watching you. It is unclear just how long she has been standing there without either you or Roxie noticing."
    luna "Don’t stop on my account, give her boobs a nice massage. Also Roxie if you wanted to feel up my boobs all you had to do was ask."
    "Apparently she’s been standing there for a while unnoticed."
    "Despite Luna’s obvious increase in size and how much attention she can command, she still has the magical ability to go unnoticed if she wants to."
    image luna_stage5_80 = "/luna/events/stage5/80.webp"
    scene luna_stage5_80
    roxie "I would love to…assuming that is okay?"
    image luna_stage5_81 = "/luna/events/stage5/81.webp"
    scene luna_stage5_81
    luna "Of course, but unfortunately just not now. I regrettably have a meeting I have to attend."
    luna "I would love to stay and watch you girls eat or rather join you as I feel super hungry, but I really can’t miss this meeting."
    pc "Understandable. See you later then, Luna."
    image luna_stage5_82 = "/luna/events/stage5/82.webp"
    scene luna_stage5_82
    luna "Make sure these girls eat a lot in my absence though."
    pc "Will do."
    image luna_stage5_83 = "/luna/events/stage5/83.webp"
    scene luna_stage5_83
    "Luna then hands you a clipboard."
    luna "Also here are the initial measurements for the other test subjects. See you later."
    image luna_stage5_84 = "/luna/events/stage5/84.webp"
    scene luna_stage5_84
    "You watch Luna leave, enjoying watching the sway of her wide hips as you do so and then once she disappears from  you, you take a look at the clipboard."
    if persistent.imperial:
        "Charlene. 37.3 inch bust (32D), 26.2 inch waist, 38.6 inch hips, 172 lbs."
        "Sally. 35.6 inch bust (32D), 25.7 inch waist, 39.3 inch hips, 176 lbs."
        "Britta. 34.3 inch bust (32B), 25.2 inch waist, 40.2 inch hips, 172 lbs."
    else:
        "Charlene. 94.7 cm bust (32D), 66.5 cm waist, 98 cm hips, 78 kg."
        "Sally. 90.4 cm bust (32D), 65.3 cm waist, 99.8 cm hips, 80 kg."
        "Britta. 87.1 cm bust (32B), 64 cm waist, 102.1 cm hips, 78 kg."
    "After you look up you see that Roxie left."
    image luna_stage5_85 = "/luna/events/stage5/85.webp"
    scene luna_stage5_85
    "You go to the room where all the food is."
    "Roxie and the rest of the test subjects have come in and joined Natalie and begun eating."
    "You notice that they all seem to be quite hungry and eating a lot, either as a side effect of the drug or because they want the project to succeed or probably a combination of both."
    image luna_stage5_86 = "/luna/events/stage5/86.webp"
    scene luna_stage5_86
    "The nurse named Sally seems to be eating particularly well as she eats an entire box of donuts."
    sally "Mmm, it's all so good. I am so going to enjoy this drug trial."
    roxie "Me too."
    sally "I’m just going to eat anything I want, as much as I want, and not care how fat I get."
    natalie "I don’t think any of us need be worrying about our weight anymore, just focus on eating and the success of the drug trial."
    sally "It’s all thanks to you Britta and then of course Luna."
    natalie "Yes. Thank you, Britta."
    image luna_stage5_87 = "/luna/events/stage5/87.webp"
    scene luna_stage5_87
    "Britta, while having only tentatively and slowly started eating herself at first, had finally given in and started eating just as much as the rest of them were."
    "She doesn’t even bother responding, just continues eating."
    image luna_stage5_88 = "/luna/events/stage5/88.webp"
    scene luna_stage5_88
    "You continue to watch and enjoy the girls eat, occasionally going over to grab stuff for them and bring it to them until each of them look so stuffed that they couldn’t possibly eat another bite."
    "It seems this is going to be happening a lot helping out with the drug trial."
    "Best job ever."
    $ britta_stats_visible = 1
    $ charlene_stats_visible = 1
    $ natalie_stats_visible = 1
    $ roxie_stats_visible = 1
    $ sally_stats_visible = 1
    "The test subjects have been added to the stats screen."
    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
        #Unlocks Natalie Undress in the stats page.
        $ renpy.notify("Natalie Undress option unlocked in stats screen.")
        window hide
        pause
        #Unlocks Roxie Undress in the stats page.
        $ renpy.notify("Roxie Undress option unlocked in stats screen.")
        window hide
        pause

    $ lunastage5event = 0
    return

label Luna_Stage_6_Event:
    image luna_stage6_1 = "/luna/events/stage6/1.webp"
    scene luna_stage6_1
    "You receive a package from your grandmother. Upon opening it, you find a nice, big homemade chocolate birthday cake in it."
    "The only problem is your birthday isn’t for several more months."
    "She must have forgotten when your birthday was, which wouldn’t be the first time."
    "Still she makes an absolutely delicious chocolate cake, which means you could just try and eat it yourself or you can give most of it to someone else."
    "You then think of Luna and all the “medical surprises” she keeps having for you."
    "Such as the stomach muscle relaxant and the breast growth drug and having you get involved in the test study for it. Perhaps she deserves a surprise of her own?"
    "You decide to bring the cake to Luna and instead of calling her, you decide to just show up and surprise her at work at the hospital."
    image luna_stage6_2 = "/luna/events/stage6/2.webp"
    scene luna_stage6_2
    "Upon getting to the hospital you see Natalie sitting at the reception desk, currently snacking on some donuts."
    pc "Hi, Natalie!"
    image luna_stage6_3 = "/luna/events/stage6/3.webp"
    scene luna_stage6_3
    natalie "Hi, [playername]! Did I forget something? Was there supposed to be a drug trial thing going on today?"
    pc "No, you’re fine."
    "This was actually the first time that you’ve been back to the hospital since the test subjects took the drug, as Luna hadn’t called you back in yet."
    image luna_stage6_4 = "/luna/events/stage6/4.webp"
    scene luna_stage6_4
    natalie "Oh? So what are you here for then? Business or pleasure?"
    pc "Well, I would say my business here is always a pleasure - especially seeing you."
    natalie "Oh, you're such a charmer. Thank you. It's always a pleasure to see you too."
    image luna_stage6_5 = "/luna/events/stage6/5.webp"
    scene luna_stage6_5
    "She grabs another donut."
    pc "So, how are you doing then?"
    image luna_stage6_6 = "/luna/events/stage6/6.webp"
    scene luna_stage6_6
    natalie "Great! Luna lets me snack and eat at my desk as much as I want, she actually encourages it."
    pc "So, have you seen any growth yet?"
    image luna_stage6_7 = "/luna/events/stage6/7.webp"
    scene luna_stage6_7
    natalie "I haven’t really gained or grown too much just yet, at least not anything noticeable, but I’m doing my best to get there."
    natalie "I did notice this morning when I was trying to put my bra on that it was feeling tight so I might have gone up a cup size already."
    pc "That’s good."
    image luna_stage6_8 = "/luna/events/stage6/8.webp"
    scene luna_stage6_8
    natalie "Yes, it is good. It means the drug is starting to work."
    pc "What about any side effects? Have you noticed anything else?"
    image luna_stage6_9 = "/luna/events/stage6/9.webp"
    scene luna_stage6_9
    natalie "Well, I’m not sure if this is even a side effect but I have noticed that my nipples have been sore."
    pc "Oh, that's... well, I'm not really sure what that is."
    natalie "It's okay. I already told Luna and she didn't know what it was either as she hasn't dealt with that side effect herself."
    natalie "I've talked to the other test subjects and none of them seem to experience the same issue."
    pc "Well, I suppose that the drug works a bit differently on everybody."
    image luna_stage6_10 = "/luna/events/stage6/10.webp"
    scene luna_stage6_10
    natalie "True. It is probably nothing to worry about just yet."
    pc "So what about the other test subjects? Have they reported anything to you?"
    image luna_stage6_11 = "/luna/events/stage6/11.webp"
    scene luna_stage6_11
    natalie "Not really much from them either just yet. Although, Roxie said she's gone up a cup size. You might have to ask them or Luna, because I haven't really talked to them much."
    pc "I’ll probably just ask Luna then. I actually came to see her but I wanted to check up on you first."
    natalie "Well, thanks for checking up on me. I'm doing great."
    image luna_stage6_12 = "/luna/events/stage6/12.webp"
    scene luna_stage6_12
    "She grabs another donut."
    pc "I can see that and keep up the good work, I’m sure you’ll start seeing results in no time."
    "You then head to the elevator and go up to Luna’s office."
    image luna_stage6_13 = "/luna/events/stage6/13.webp"
    scene luna_stage6_13
    "You find Luna standing at her desk, currently going over what appears to be a bunch of paperwork."
    pc "Hey, Luna. Are you not too busy?"
    image luna_stage6_14 = "/luna/events/stage6/14.webp"
    scene luna_stage6_14
    "Luna turns around and smiles happily when she sees you."
    luna "I'm always busy, unfortunately. Mostly, it is way too much paperwork that needs doing, but I'm never too busy for a fun break with you."
    luna "Did you bring me something? Something edible perchance?"
    image luna_stage6_15 = "/luna/events/stage6/15.webp"
    scene luna_stage6_15
    "She is eyeing the package you brought with the cake secretly inside it."
    pc "Of course. Something extra delicious."
    luna "Ooh! What is it?"
    "You bring over the package with the chocolate cake inside and open it up for her."
    image luna_stage6_16 = "/luna/events/stage6/16.webp"
    scene luna_stage6_16
    luna "A birthday cake! It’s not my birthday though."
    pc "I know and it isn’t mine but my grandma messed up and thought it was my birthday. You’ve given me plenty of surprises lately so I figured I would bring you one."
    image luna_stage6_17 = "/luna/events/stage6/17.webp"
    scene luna_stage6_17
    luna "Wow! Well, thank you! I've actually never had a birthday cake before."
    pc "Wait, seriously? You’ve never had a birthday cake?"
    image luna_stage6_18 = "/luna/events/stage6/18.webp"
    scene luna_stage6_18
    luna "No. I mean, I've obviously had cake lots of times now, but never an actual birthday cake."
    luna "Unless you count the times I've had some when friends or someone at the hospital were celebrating their birthdays. Never an actual birthday cake for me though."
    luna "My parents never let me have sweets growing up as they worried it would ruin my figure."
    pc "Not even on your birthday?"
    image luna_stage6_19 = "/luna/events/stage6/19.webp"
    scene luna_stage6_19
    luna "No. I tried asking for one a couple of times, but all I got was vegetable trays and dietetic food."
    luna "I mean, it wasn't all bad. I always got plenty of presents - just not a birthday cake or any other kind of sweets."
    pc "What about when you were older and could get your own birthday cake?"
    image luna_stage6_20 = "/luna/events/stage6/20.webp"
    scene luna_stage6_20
    luna "Well, I guess I was just too busy the last couple of birthdays after my parents died to really celebrate my birthday. Running a hospital is a lot more work than I realised."
    pc "I can imagine. Can I do something to help you with that?"
    image luna_stage6_21 = "/luna/events/stage6/21.webp"
    scene luna_stage6_21
    luna "You're sweet. Unfortunately, most of it are things you wouldn't have any clue on how to deal with and they require my direct attention. Most of them are bills anyway."
    pc "I’m sure running a hospital is quite expensive."
    image luna_stage6_22 = "/luna/events/stage6/22.webp"
    scene luna_stage6_22
    luna "It is. People often complain about the cost of their medical bills, but they don't seem to realise just how expensive it is for the hospital to treat them."
    luna "I mean, I'm not going to deny that plenty of hospitals do overcharge their patients for no reason, but I like to think that I'm not one of them."
    luna "Sometimes I do feel like I should be charging more though - especially now."
    pc "Why? What’s wrong?"
    image luna_stage6_23 = "/luna/events/stage6/23.webp"
    scene luna_stage6_23
    luna "Oh, nothing for you to worry about. I'll be fine."
    "From the look on Luna’s face, she clearly was not fine, which was surprising considering how composed and optimistic Luna usually was."
    pc "It’s okay if you don’t want to talk to me about it, but I’m here for you if you do."
    image luna_stage6_24 = "/luna/events/stage6/24.webp"
    scene luna_stage6_24
    luna "Well, let's just say I've already used up most of the family fortune on buying the hospital, all the medical equipment, making sure my staff is paid, the drugs I've had created and it all adds up."
    luna "Like I said; I should be fine for a while longer. I do admittedly have a lot riding on the breast growth drug though."
    luna "If it is as successful as I believe it will be, money will definitely not be a problem, but if not I’m going to be in trouble."
    pc "Well, I'm sure it will work out great."
    image luna_stage6_25 = "/luna/events/stage6/25.webp"
    scene luna_stage6_25
    luna "Yeah, I'm sure it will. Anyway, sorry to burden you with my problems."
    pc "No, it's totally fine. I want you to feel like you can tell me anything and trust that I'm going to be here to support you."
    luna "Ah, so you aren't just a handsome man feeding me delicious treats?"
    pc "I’d like to think that I can be more than just that for you."
    image luna_stage6_26 = "/luna/events/stage6/26.webp"
    scene luna_stage6_26
    "Luna looks at you curiously."
    luna "Are you suggesting that we take our relationship to the next level?"
    "This really wasn't what you were implying, but now that she brought it up, you fumble your words."
    pc "Um, I don't know... I mean, I've certainly enjoyed spending time with you - especially all the sexy parts."
    pc "But I also do have other women that I’m also…sort of doing things with and I don’t really want that to end."
    image luna_stage6_27 = "/luna/events/stage6/27.webp"
    scene luna_stage6_27
    luna "You know I don't care about what you do with other women."
    luna "I don’t know what Daisy has told you about our shared beliefs but let’s just say that as long as nobody gets hurt and everyone is enjoying themselves…"
    luna "I think sex should be shared amongst more than just two people. It’s not like you’re the only one I’ve had some fun with since we met."
    pc "You’ve been with other guys since then?"
    image luna_stage6_28 = "/luna/events/stage6/28.webp"
    scene luna_stage6_28
    luna "I never said that I’ve been with other guys."
    "You suddenly realize just what she meant by that."
    pc "Oh, so you're...?"
    image luna_stage6_29 = "/luna/events/stage6/29.webp"
    scene luna_stage6_29
    luna "I'm bisexual, yes."
    pc "Oh, well, I don't really have a problem with that. Honestly, it's kind of hot thinking about you being with another woman."
    image luna_stage6_30 = "/luna/events/stage6/30.webp"
    scene luna_stage6_30
    luna "It's hot, huh?"
    pc "Uh, unless you have a problem with me thinking that?"
    image luna_stage6_31 = "/luna/events/stage6/31.webp"
    scene luna_stage6_31
    luna "Definitely not, it certainly is hot. I think it’s hot thinking about you being with other women, especially you fattening them up while you do so."
    luna "Speaking of which, I think Natalie has a major crush on you."
    pc "You think so?"
    "You hadn’t really thought about it, you were just trying to be nice to her, but if Natalie maybe wanted to do something some time and if Luna was encouraging it…"
    image luna_stage6_32 = "/luna/events/stage6/32.webp"
    scene luna_stage6_32
    luna "Definitely. I mean, I wouldn't rush into anything. She has admittedly had some really bad experiences with guys, but I think you could really be good for her in that regard."
    luna "Assuming of course that she doesn’t mind sharing you with me."
    pc "Well, I'm not going to lie; Natalie is quite attractive."
    pc "With the drug trial and her constant eating I'm assuming that statement is only going to become more true. For now, I guess I'll just see how it goes and what she wants."
    pc "I don’t want to hurt her."
    image luna_stage6_33 = "/luna/events/stage6/33.webp"
    scene luna_stage6_33
    luna "See that you don’t or I’ll have to hurt you myself."
    "From the look that Luna is giving you, she doesn’t seem to be at all joking about that."
    "You definitely do not want to see Luna angry and what she might do to you."
    image luna_stage6_34 = "/luna/events/stage6/34.webp"
    scene luna_stage6_34
    luna "Anyway, as far as our relationship goes, how about this?"
    luna "I'll agree that you be the only guy that I'm with. Honestly, you're one of the few guys I've ever been interested in."
    luna "That way you can be my one and only boyfriend and I’ll let you have…however many girlfriends that you can manage to get."
    pc "That sounds great to me. Does that mean I get to call you my girlfriend?"
    image luna_stage6_35 = "/luna/events/stage6/35.webp"
    scene luna_stage6_35
    luna "Uh, no. I'm your boss, remember?"
    pc "Oh. Well, I guess it probably would be safer not to go with such labels if you're my boss."
    image luna_stage6_36 = "/luna/events/stage6/36.webp"
    scene luna_stage6_36
    luna "I'm just teasing you. Besides, I have you listed as an independent contractor, which means you aren't actually a hospital employee and I'm not technically your boss, so we can do whatever we want."
    pc "Smart. I figured we just needed to sneak around."
    luna "Not with you, no. Although maybe I shouldn't have told you. It would have been more fun that way."
    pc "We can still pretend."
    image luna_stage6_37 = "/luna/events/stage6/37.webp"
    scene luna_stage6_37
    luna "Good idea! I'm sure we can have some fun with that. For now, however, I'm thinking maybe I could have that chocolate cake you brought me. This conversation is making me hungry."
    pc "You’re always hungry though."
    luna "When you’re around I am."
    pc "Well, you can have as much cake as you would like."
    image luna_stage6_38 = "/luna/events/stage6/38.webp"
    scene luna_stage6_38
    luna "If you tell me that then I’m going to want to eat all of it."
    pc "Save me a slice at least."
    image luna_stage6_39 = "/luna/events/stage6/39.webp"
    scene luna_stage6_39
    luna "Will do. I feel like the girls are definitely going to grow from eating this."
    pc "Were you planning on sharing with the other test subjects then?"
    image luna_stage6_40 = "/luna/events/stage6/40.webp"
    scene luna_stage6_40
    "However, Luna is already taking her first big bite of cake - her eyes widening as she chews."
    luna "Oh my! This is definitely the best birthday cake I've ever had! No, not just birthday cake, but any cake! So moist and rich!"
    pc "What can I say? My grandma makes the best cakes."
    image luna_stage6_41 = "/luna/events/stage6/41.webp"
    scene luna_stage6_41
    luna "Yeah, no. Definitely not sharing this with anyone else - especially not when it tastes this good. When I was talking about the girls growing, I was talking about my boobs."
    "You look down at Luna's now truly huge boobs. It seems that every time you see Luna they are just a little bit bigger."
    image luna_stage6_42 = "/luna/events/stage6/42.webp"
    scene luna_stage6_42
    luna "I can’t wait to see the other girls really start to grow though, but they aren’t getting any of this cake."
    image luna_stage6_43 = "/luna/events/stage6/43.webp"
    scene luna_stage6_43
    "She continues happily eating it."
    pc "I think it's fair. It sort of makes up for the lack of birthday cake growing up."
    image luna_stage6_44 = "/luna/events/stage6/44.webp"
    scene luna_stage6_44
    luna "Well, if you were to persuade your grandma to make me another one of these I would certainly appreciate it."
    pc "I'll see what I can do. I know she loves to bake, but she lives kind of far away, which is why she had the cake shipped to where I live."
    image luna_stage6_45 = "/luna/events/stage6/45.webp"
    scene luna_stage6_45
    "Luna continues to eat the cake and you decide you had better try and get your piece before she eats it."
    image luna_stage6_46 = "/luna/events/stage6/46.webp"
    scene luna_stage6_46
    "However, Luna is all too happy to work on finishing the rest."
    pc "Happy not-your-birthday, my girlfriend."
    image luna_stage6_47 = "/luna/events/stage6/47.webp"
    scene luna_stage6_47
    "She smiles when she hears that."
    luna "Thank you, my boyfriend."
    image luna_stage6_48 = "/luna/events/stage6/48.webp"
    scene luna_stage6_48
    "She then gives you a look... yes, that look, the one you like to see most of all."
    window hide
    pause
    luna "You know, now that we’re boyfriend and girlfriend, I think we ought to consummate it, to make it official."
    "You can’t help but grin back."
    pc "Well, we definitely do need to do that. As long as you aren't too full from eating all that cake?"
    image luna_stage6_49 = "/luna/events/stage6/49.webp"
    scene luna_stage6_49
    luna "Not this time. Instead, I'm thinking I want something else inside me to fill me up - something long and hard that you possess."
    pc "I do indeed have such a long and hard thing for you, with your own sexy, curvy body making it so long and hard."
    image luna_stage6_50 = "/luna/events/stage6/50.webp"
    scene luna_stage6_50
    luna "Mmm, happy to make it grow. As you know I'm in the business of making sexy body parts grow."
    "Luna shows off her enlarged breasts."
    pc "That you are, and I’m in the business of inspecting those grown body parts."
    image luna_stage6_51 = "/luna/events/stage6/51.webp"
    scene luna_stage6_51
    luna "You're right. I am after all a test subject and you need to inspect me as well... every inch of me."
    pc "Well, you're the boss, so I guess I'll have to do this quite... dirty job."
    image luna_stage6_52 = "/luna/events/stage6/52.webp"
    scene luna_stage6_52
    luna "Yes, I am the boss. And I order you to give me some absolutely mindblowing sex."
    pc "I sure will try."
    image luna_stage6_53 = "/luna/events/stage6/53.webp"
    scene luna_stage6_53
    window hide
    pause
    "The two of you then remove your clothes and are totally naked, as you then look at Luna’s curvy body."
    "She has already grown quite a bit since you met her and it's amazing to think about just how big Luna is going to get considering what her goals are."
    image luna_stage6_54 = "/luna/events/stage6/54.webp"
    scene luna_stage6_54
    window hide
    pause
    luna "That's right. Look me over, inspect me and note just how much more of me there is."
    pc "More of you to love. And more is always better."
    luna "Mmm, for sure."
    image luna_stage6_55 = "/luna/events/stage6/55.webp"
    scene luna_stage6_55
    window hide
    pause
    "You get right up next to her and start by placing your hands under her huge breasts, marveling at how heavy they feel now."
    luna "Mmm, so what do you think? Am I making some good progress in their growth?"
    pc "Let me check some more to make sure."
    luna "Take your time. I expect you to do a thorough job and then give me a full and accurate report on it."
    image luna_stage6_56 = "/luna/events/stage6/56.webp"
    scene luna_stage6_56
    window hide
    pause
    "You make it a point of running your fingers over each square millimeter of boob flesh and lean your head down even closer as if to inspect them more closely."
    pc "They seem to be making some good progress in their development and growth and they still look healthy to me."
    pc "However, I'm going to recommend a very large diet for you as well as having them massaged and felt up frequently."
    image luna_stage6_57 = "/luna/events/stage6/57.webp"
    scene luna_stage6_57
    window hide
    pause
    luna "I appreciate your opinion and I concur with your recommendation. Good work."
    pc "Thanks, boss. So should I continue with my examination?"
    luna "Please do."
    image luna_stage6_58 = "/luna/events/stage6/58.webp"
    scene luna_stage6_58
    window hide
    pause
    "You then look over her belly, which is already sticking out quite a bit, both from eating all that chocolate cake and from her gaining in other areas besides just her breasts."
    image luna_stage6_59 = "/luna/events/stage6/59.webp"
    scene luna_stage6_59
    window hide
    pause
    "You also run your hands happily along her belly, enjoying the bit of chub there."
    pc "Your belly also looks good but you’re going to want to make it grow some more too so you can increase your stomach capacity and eat more."
    pc "Those small meals you’ve been eating are still insufficient."
    image luna_stage6_60 = "/luna/events/stage6/60.webp"
    scene luna_stage6_60
    window hide
    pause
    luna "You’re right, I’ll make sure to work on that."
    pc "Now, turn around for me. I need to inspect your hips and butt."
    image luna_stage6_61 = "/luna/events/stage6/61.webp"
    scene luna_stage6_61
    window hide
    pause
    "Luna obligingly turns around for you and shows off her curvy hips and butt."
    image luna_stage6_62 = "/luna/events/stage6/62.webp"
    scene luna_stage6_62
    window hide
    pause
    "You also inspect that part of her naked body closely and run your hands along each butt cheek."
    pc "It’s not bad, but you’re going to need to grow some more in this area as well in order to counterbalance the weight of your breasts."
    pc "As massive as they need to be and are going to get, your ass and hips getting bigger will help greatly with this."
    image luna_stage6_63 = "/luna/events/stage6/63.webp"
    scene luna_stage6_63
    window hide
    pause
    luna "I'll also work on that. Thank you for your examination."
    image luna_stage6_64 = "/luna/events/stage6/64.webp"
    scene luna_stage6_64
    window hide
    pause
    "You turn her around."
    pc "Oh, it's definitely not over yet. I still have one thing left to do."
    image luna_stage6_65 = "/luna/events/stage6/65.webp"
    scene luna_stage6_65
    window hide
    pause
    luna "Fuck your girlfriend and boss?"
    pc "Yes, that’s definitely my recommendation."
    image luna_stage6_66 = "/luna/events/stage6/66.webp"
    scene luna_stage6_66
    window hide
    pause
    luna "I agree. I think that would benefit me greatly."
    if persistent.nosexscene == True:
        scene black with dissolve
        "Luna and I had a great time together."
        pc "Did I do a good enough job?"
        image luna_stage6_71 = "/luna/events/stage6/71.webp"
        scene luna_stage6_71
        window hide
        pause
        luna "Good enough but we’ll definitely have to practice more so you can improve."
        pc "Yes, my boss and my girlfriend."
        scene outside
        "You go back home."
        if recollection == False:
            $ luna.weight += 1
            $ daytime += 1
            $ phonecall = 1
        $ lunastage6event = 0
        return
    image luna_stage6_67 = "/luna/events/stage6/67.webp"
    scene luna_stage6_67
    window hide
    pause
    "With foreplay already done with your so-called examination, you line up your erection with her nether regions and slowly start to enter her."
    luna "No need to go too slow, just shove it in me! I want it!"
    pc "I’m just trying to let you get used to my size first."
    image luna_stage6_68 = "/luna/events/stage6/68.webp"
    scene luna_stage6_68
    window hide
    pause
    luna "In case you haven’t noticed I’m not a girl who feels the need to get used to size. You’re quite large but you could never be too big for me."
    pc "And you could never be too big for me. In fact, I want you a lot bigger."
    luna "Mmm, me too!"
    image luna_stage6_69 = "/luna/events/stage6/69.webp"
    scene luna_stage6_69
    window hide
    pause
    "Thoughts of a much bigger and more curvy Luna fill your mind as you ram your erection deep inside her."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage6/69_video.webm" loop
    show movie with dissolve
    window hide
    pause
    "She lets out a gasp but you continue as you start pounding into her."
    luna "Ooh, yes! This is how to do a deep and thorough examination!"
    pc "I aim to please. Maybe I can earn myself a raise after this?"
    luna "I’d like to say I’ll think about it, but I’d also like to think about other things right now, such as how good it feels having you inside me."
    pc "I can live with that. Besides, I'm getting paid in sex with a gorgeous woman right now."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage6/69_video2.webm" loop
    show movie with dissolve
    window hide
    pause
    "At that you continue to pound into her until you can feel a climax beginning to build."
    pc "I’m about to cum!"
    luna "Give it to me! Fill me up! I'm hungry for your cum now!"
    "You are only too happy to oblige, since your spurt after spurt deep into Luna made it impossible to hold it in any longer."
    stop movie
    image luna_stage6_70 = "/luna/events/stage6/70.webp"
    scene luna_stage6_70
    window hide
    pause
    "Even after coming, you stay inside her for a moment longer, resting and enjoying still being inside your new girlfriend."
    pc "Did I do a good enough job?"
    image luna_stage6_71 = "/luna/events/stage6/71.webp"
    scene luna_stage6_71
    window hide
    pause
    luna "Good enough, but we'll definitely need to practice this some more... only for you to improve, of course."
    pc "Yes, my boss and my girlfriend."
    scene outside
    "You go back home."
    scene player_room
    if recollection == False:
        $ luna.weight += 1
        $ daytime += 1
        $ phonecall = 1
    "Upon getting back home you decide to check on the other test subjects you didn’t get to see earlier and see how they are doing."
    "You first text message Roxie."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Roxie', dialogue=dialogue_one)
    $ msg ("Roxie, how are things going with the drug testing?")
    pause
    $ msg ("Anything I should know about?")
    pause
    $ msg (None, who=1, pic="stage1_roxie")
    pause
    $ msg ("Do my boobs look any bigger to you?", who=1)
    pause
    $ msg ("Yeah, they look a little bigger.")
    pause
    $ msg ("That’s good. It’s progress at least.", who=1)
    pause
    $ msg ("Let me know if there is anything else.")
    pause
    $ msg ("Will do.", who=1)
    pause
    $ hide_messenger()

    "You next text message Sally."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Sally', dialogue=dialogue_one)
    $ msg ("Sally, how are things going with the drug testing?")
    pause
    $ msg ("Anything I should know about?")
    pause
    $ msg ("Yeah, I’m all out of food.", who=1)
    pause
    $ msg ("SEND ME MORE!", who=1)
    pause
    $ msg ("I’m hungry!", who=1)
    pause
    $ msg ("You wouldn’t want to leave a girl hungry would you?", who=1)
    pause
    $ msg ("Definitely not, I’ll send you some more.")
    pause
    $ msg ("Thank you!", who=1)
    pause
    $ hide_messenger()

    "You arrange to have food delivered to Sally using the food budget that Luna provided you."
    "While you are at it you send some to the other girls too."
    "Along with thanks from most of them when it arrives, you receive a text message back from Charlene."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Charlene', dialogue=dialogue_one)
    $ msg ("Why did you have to send me more food?", who=1)
    pause
    $ msg ("I just finished eating all the food I had at home.", who=1)
    pause
    $ msg ("Great timing then, so now you have some more.")
    pause
    $ msg ("Yeah and now I won’t be able to resist eating that too.", who=1)
    pause
    $ msg ("Thanks a lot!", who=1)
    pause
    "You can tell that is sarcastic but you decide to ignore it."
    $ msg ("You’re welcome!")
    pause
    $ hide_messenger()

    "Britta’s response is much more positive."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Britta', dialogue=dialogue_one)
    $ msg (None, who=1, pic="stage1_britta")
    pause
    $ msg ("Thanks for the combined 20,183 calories!", who=1)
    pause
    $ msg ("This will be perfect to get me through the long all-nighter I’ll need to pull to work out these equations I’m working on.", who=1)
    pause
    $ msg ("Want to hear about them?", who=1)
    pause
    $ msg ("I’ll pass, I don’t think I’ll understand any of it but good luck.")
    pause
    $ msg ("Thanks!", who=1)
    pause
    $ hide_messenger()

    "Having checked on and provided food for all the test subjects, you feel you can move on with the rest of your day."

    $ lunastage6event = 0
    return

label Luna_Stage_7_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Luna', dialogue=dialogue_one)
    $ msg ("Today is another big day! We’re going to check the growth and the progress of all the test subjects today! Can you come into the hospital to help out?", who=1)
    pause
    menu:
        "Yes.":
            "You quickly reply back."
            pause
            $ msg ("Of course! I'm looking forward to it. I'll be right there!")
            pause
            $ hide_messenger()

        "Not today.":
            $ msg ("Sorry, I’m a little busy tonight.")
            pause
            $ msg ("Alright. I’ll catch you some other time.", who=1)
            pause
            $ hide_messenger()
            return

    if recollection == False:
        $ britta.stage = 2
        $ sally.stage = 2
        $ natalie.stage = 2
        $ charlene.stage = 2
        $ roxie.stage = 2
    "While you haven’t gone into the hospital much yet, you have still been doing things for your new side job helping out with the drug trial."
    "Mainly getting emailed submissions from the test subjects on what and how much they ate each day."
    "While you try to convert that into a rough estimate of how many calories, carbs, fats, etc., and what all of that totals up to,"
    "you've also been trying to do your part in trying to encourage each participant and see how they are doing -"
    "either through replying to their emails or interacting with them while working at your other side job at Bunny Bites."
    "Even so, by now it's clear that they have all grown and gained and you are eager to find out just how much."
    "The fact that you also get to see them naked and measure them as well as help them eat a lot of food makes your decision a no-brainer."
    image luna_stage7_1 = "/luna/events/stage7/1.webp"
    scene luna_stage7_1
    "Upon getting to the hospital, you see Natalie sitting at the reception desk and the closer you get to her, the more obvious it becomes just how much she has grown already."
    image luna_stage7_2 = "/luna/events/stage7/2.webp"
    scene luna_stage7_2
    "Her breasts seem to have somehow already doubled in size and her butt and hips seem to occupy just a little more of her chair."
    image luna_stage7_3 = "/luna/events/stage7/3.webp"
    scene luna_stage7_3
    "You can’t help but stare at the now much curvier receptionist. Natalie doesn’t mind though as she grins and seems to like your reaction."
    pc "Wow."
    natalie "I know, right?! I can't believe how much I've grown already. I mean, just look at these babies!"
    image luna_stage7_4 = "/luna/events/stage7/4.webp"
    scene luna_stage7_4
    "She happily sticks out her chest."
    pc "Oh, I'm definitely looking... I mean, I'm sorry, I don't mean to stare so much."
    image luna_stage7_5 = "/luna/events/stage7/5.webp"
    scene luna_stage7_5
    natalie "Oh, no need to apologize. I was actually kind of hoping that I would get this reaction out of you."
    natalie "Besides, this is, like, your job anyway; to inspect each of us and our progress, right?"
    pc "Yes, I suppose it is. I would have to say that you're making good progress then."
    natalie "Mmm, yes, it seems I am. I've been trying to do my part - eating as much as I can."
    image luna_stage7_6 = "/luna/events/stage7/6.webp"
    scene luna_stage7_6
    "You look down at the empty food containers next to her as proof of this, if the proof wasn’t already obviously now on her chest.."
    pc "Yeah, as you know I’ve been keeping track of how much each of you girls have been eating, you’re actually eating slightly more than anybody else."
    image luna_stage7_7 = "/luna/events/stage7/7.webp"
    scene luna_stage7_7
    natalie "Oh... I didn't know that. I mean, I suppose I have more opportunities to eat than the others, mainly sitting at this desk all day."
    pc "It’s definitely not a bad thing, it’s a good thing! It means it’s showing your dedication to making sure the drug trial is a success."
    natalie "Well, that's true. I'm really glad that I'm pulling my weight, so to speak. Speaking of which, so you really like that there is even more of me now?"
    pc "Oh, definitely! It looks great on you!"
    "Natalie smiles widely at hearing that as she looks back at you."
    image luna_stage7_8 = "/luna/events/stage7/8.webp"
    scene luna_stage7_8
    natalie "Mmm, I figured you would say that but it’s nice to hear. So you’ll like it even more when there’s a lot more of me?"
    pc "Definitely."
    image luna_stage7_9 = "/luna/events/stage7/9.webp"
    scene luna_stage7_9
    "Natalie grins again at hearing that but then she frowns."
    natalie "Well, there is one thing that you might not like. There seems to be an unexpected side effect of the drug for me."
    pc "Yeah? What is it? I’m sure it can’t be too bad."
    image luna_stage7_10 = "/luna/events/stage7/10.webp"
    scene luna_stage7_10
    natalie "Well, you know I told you that my nipples were sore? Well, they continued to be sore until I noticed one morning when I woke up... they were leaking."
    pc "Leaking? Like with-"
    image luna_stage7_11 = "/luna/events/stage7/11.webp"
    scene luna_stage7_11
    natalie "With milk, yes. I'm lactating. At first it was just a little bit, but over the next several days I produced more and more. I told Luna and Britta about it and they were just as surprised as I was."
    natalie "They did say they were going to get me something today to help deal with it while they try to figure out what’s causing it. I’m not really sure myself as I’ve never been pregnant."
    pc "Yeah, that is strange. It doesn't seem like it's particularly dangerous though."
    image luna_stage7_12 = "/luna/events/stage7/12.webp"
    scene luna_stage7_12
    natalie "No, it doesn’t seem like it. I was worried about telling you though as I wasn’t sure how you would react."
    pc "You don’t need to worry about what I might think."
    natalie "Well, I do worry what you think. You see, I really..."
    image luna_stage7_13 = "/luna/events/stage7/13.webp"
    scene luna_stage7_13
    "She stops and then just shakes her head."
    "She seems like she wants to say something and you have a guess just what it is, that she likes you, but you don’t want to assume that or guess for her as it will be awkward if you are wrong."
    "Or perhaps she just might not be ready to tell you."
    image luna_stage7_14 = "/luna/events/stage7/14.webp"
    scene luna_stage7_14
    natalie "Never mind. Anyway, we had both better go to the lab and meet up with the other test subjects. I'm sure you're curious to see how much each of them have grown."
    pc "Yeah, admittedly I am - especially after seeing you."
    natalie "I don't blame you. They've all grown quite a bit in a short amount of time."
    image luna_stage7_15 = "/luna/events/stage7/15.webp"
    scene luna_stage7_15
    "You and Natalie head up to the examination room to find all the others, including Luna waiting for you and Natalie."
    "Your eyes grow wide at seeing each of the test subjects and their growth."
    "All of them have definitely grown, including Luna herself, who still has everybody else beat by the size of her assets."
    "But now doesn’t look so out of place with all the other busty, curvy women around her."
    image luna_stage7_16 = "/luna/events/stage7/16.webp"
    scene luna_stage7_16
    luna "Hi, [playername]! Just look how much progress we've made! The drug is working!"
    britta "It seems premature to assume that. However, yes, it appears that our assets have grown."
    britta "But the primary purpose of the drug - of being able to cure or prevent diseases - still remains to be seen. We are going to need to do a lot more research to-"
    luna "Yes, yes, I know. But at least we can say that the breast growth part of the drug is clearly working so far and we're off to a really good start. Good work, ladies."
    image luna_stage7_17 = "/luna/events/stage7/17.webp"
    scene luna_stage7_17
    roxie "Thanks, boss. Just trying to do our part. They also look great and nice and big, don't they?"
    "Luna gives Roxie’s chest a nice look which causes Roxie to smile and glow with pride and happiness."
    roxie "They aren’t nearly as big or impressive as yours but they will get there."
    luna "Indeed, I certainly hope so."
    roxie "Would you like to be the one to inspect them?"
    luna "I normally would love to, but I, unfortunately, once again have another meeting to go to right after this, so perhaps some other time."
    luna "Actually, I was thinking that I would have [playername] do that for all of you."
    image luna_stage7_18 = "/luna/events/stage7/18.webp"
    scene luna_stage7_18
    charlene "Why does it have to be him? Just so he can get his jollies off to measuring us and seeing us naked?"
    pc "Well, I mean, I'm happy to do all that, but I don't want to do it if it would make anyone feel uncomfortable."
    image luna_stage7_19 = "/luna/events/stage7/19.webp"
    scene luna_stage7_19
    roxie "With the exception of Charlene, I don’t think any of us mind."
    image luna_stage7_20 = "/luna/events/stage7/20.webp"
    scene luna_stage7_20
    luna "Very good. Well, I need to leave for my meeting, but I'll try to get back as soon as I can. Hopefully, it won't take too long, but you might have already finished by then."
    "Luna then leaves and Natalie starts coming closer to you to be the first one to have her private checkup with you, but Britta stops her."
    image luna_stage7_21 = "/luna/events/stage7/21.webp"
    scene luna_stage7_21
    britta "Hold on for a moment, Natalie. I wanted to talk to you and give you something that I think might help with your condition."
    "Natalie looks disappointed at that."
    pc "I’ll check you over later."
    image luna_stage7_22 = "/luna/events/stage7/22.webp"
    scene luna_stage7_22
    "Natalie nods and then goes over to talk to Britta, while Roxie steps forward."
    roxie "I guess I’ll go first then."
    pc "Sure."
    image luna_stage7_23 = "/luna/events/stage7/23.webp"
    scene luna_stage7_23
    "The two of you then head out of the room over to the room next to it where Roxie strips naked. She also doesn’t seem to mind you staring."
    roxie "Already some impressive growth, huh?"
    pc "Yes, for sure."
    image luna_stage7_24 = "/luna/events/stage7/24.webp"
    scene luna_stage7_24
    roxie "Do you think Luna liked looking at them?"
    pc "I’m guessing that she did. Is that important to you? What Luna thinks?"
    image luna_stage7_25 = "/luna/events/stage7/25.webp"
    scene luna_stage7_25
    "Roxie blushes at being asked that."
    roxie "Well, please don't tell Luna or anyone else, but I kind of have... feelings for her. Strong feelings."
    pc "Nothing wrong with that, I have feelings for her too."
    image luna_stage7_26 = "/luna/events/stage7/26.webp"
    scene luna_stage7_26
    roxie "Yes, but she’s also my boss."
    pc "Well, I guess I'm not the right person to talk to seeing as she's my boss too. Also, I'm having sex with her and she calls me 'boyfriend' and I her 'girlfriend'."
    image luna_stage7_27 = "/luna/events/stage7/27.webp"
    scene luna_stage7_27
    "Roxie seems disappointed at hearing that."
    roxie "I didn't know that you were, like... boyfriend and girlfriend now. I mean, congratulations though, you're a lucky guy."
    pc "I am a lucky guy. Don't worry though, it's still more of an open relationship - at least when it comes to being with other women for the both of us."
    pc "I wouldn't have anything against it if you and Luna-"
    image luna_stage7_28 = "/luna/events/stage7/28.webp"
    scene luna_stage7_28
    roxie "Yeah... I definitely appreciate the encouragement, but I don't know."
    roxie "I mean, I've had really strong feelings for her for a while now."
    roxie "But when she took the breast growth drug and just got so much more curvy and sexy with just those huge boobs of hers that only seem to continue to get bigger…"
    roxie "I want her more and more. Only problem is, I also feel like I have just no chance with her."
    pc "Is that the real reason you wanted to take the breast growth drug so bad? To impress Luna? If you don’t mind me asking."
    image luna_stage7_29 = "/luna/events/stage7/29.webp"
    scene luna_stage7_29
    roxie "No, it's okay, and yes, that's partially why. I mean, I also did it for me because I have a thing for huge breasts - and not just Luna's."
    roxie "I wanted a pair of my own, but... I really want Luna to like me as much as I like her."
    pc "Well, maybe you should try talking to Luna and see what she thinks. I mean, I know that she is your boss and all, but that hasn't really stopped me."
    roxie "Yes, but your situation is different; you were already with Luna before your employment here. And now, you apparently have some loophole around the boss-employee relationship thing."
    roxie "My situation is different. I don't want Luna getting in trouble because of me."
    roxie "I also really don’t want to quit because I love this job, but if it meant I could be with Luna…"
    pc "Well, I guess I'd rather just let you figure that out. I'm not really sure what else to say, but I'm sure it's a tough situation to be in."
    image luna_stage7_30 = "/luna/events/stage7/30.webp"
    scene luna_stage7_30
    roxie "Yeah, it is. In any case, I think I'll still just wait a while. Hopefully, I'll gain some more curves that Luna will like and eventually be irresistible to her."
    roxie "Once I know she likes me a lot back, maybe I can make my move and work something out."
    pc "That sounds like a plan! What I can say is just how excited and turned on Luna gets from thinking about growing and gaining."
    roxie "That’s what I’m counting on. Anyway, why don’t you get your measurements?"
    image luna_stage7_31 = "/luna/events/stage7/31.webp"
    scene luna_stage7_31
    "Roxie stands on the scale and reads her weight."
    if persistent.imperial:
        roxie "I weigh just shy of 150lbs now, which means I gained nearly 9 pounds."
    else:
        roxie "I weigh 68Kg now, which means I gained 4 kilograms."
    image luna_stage7_32 = "/luna/events/stage7/32.webp"
    scene luna_stage7_32
    "You measure each part of her body and get her measurements and then read the results to her."
    if persistent.imperial:
        pc "You’ve added more than three inches to your bust and are now at nearly 37 inches around with a bra size of 32E."
        pc "You’ve added only a half inch to your waist at just over 22 and a half inches, and you’ve added more than an inch to your hips at just over 38 inches."
    else:
        pc "You’ve added more than seven and a half centimeters to your bust and are now at nearly 94 cm around with a bra size of 32E."
        pc "You’ve added only a bit more then a centimeter to your waist at just over 57 cm, and you’ve added more than two and a half centimeters to your hips at just over 96.5 cm."
    image luna_stage7_33 = "/luna/events/stage7/33.webp"
    scene luna_stage7_33
    window hide
    pause
    "Roxie looked over her more curvy body with satisfaction."
    roxie "Most of the extra weight went to my boobs. That's good. Or, at least a start, anyway. Some more pounds finding their way to my tits and Luna is definitely going to be checking these babies out."
    pc "Well, if it helps, I'm definitely already checking them out."
    image luna_stage7_34 = "/luna/events/stage7/34.webp"
    scene luna_stage7_34
    roxie "You're sweet. Well, feel free to check them out as much as you want. I don't mind."
    pc "Sounds good to me."
    image luna_stage7_35 = "/luna/events/stage7/35.webp"
    scene luna_stage7_35
    window hide
    pause
    "Roxie lets you look for a moment at her naked body."
    roxie "You can touch them again too if you want, feel how they feel heavier too."
    image luna_stage7_36 = "/luna/events/stage7/36.webp"
    scene luna_stage7_36
    window hide
    pause
    "You are more than happy to do so, feeling the added weight of Roxie’s chest."
    image luna_stage7_37 = "/luna/events/stage7/37.webp"
    scene luna_stage7_37
    window hide
    pause
    "After a moment though, Roxie decides that it is enough for now and gets dressed. She leaves the room to call in the next test subject."
    image luna_stage7_38 = "/luna/events/stage7/38.webp"
    scene luna_stage7_38
    window hide
    pause
    "To your total surprise it’s Charlene."
    roxie "I’m surprised to see you here Charly to get measured and examined."
    image luna_stage7_39 = "/luna/events/stage7/39.webp"
    scene luna_stage7_39
    charlene "Yeah, I’m definitely not…doing that."
    roxie "Suit yourself."
    image luna_stage7_40 = "/luna/events/stage7/40.webp"
    scene luna_stage7_40
    "Roxie leaves, leaving you and Charlene alone."
    "You aren’t sure what to say to her so you ask her the first question that comes to mind."
    pc "Charly?"
    image luna_stage7_41 = "/luna/events/stage7/41.webp"
    scene luna_stage7_41
    charlene "Yeah, it's a nickname. Well, at least it's a nickname for people I care one bit about, so you aren't allowed to use it."
    pc "Noted. I won't call you that."
    charlene "I’m actually just here to tell you that me getting naked in front of you is never going to happen."
    charlene "And if you hurt any of those other girls in any way I’ll see to it that you can never use that dick of yours again."
    pc "Well, I definitely still... want to be able to use that, so I promise that I will do my best to never hurt any of them."
    charlene "See that you do."
    image luna_stage7_42 = "/luna/events/stage7/42.webp"
    scene luna_stage7_42
    "She turns to leave but then you try to stop her."
    pc "Wait, can we at least talk? All I want to do is talk, nothing more."
    image luna_stage7_43 = "/luna/events/stage7/43.webp"
    scene luna_stage7_43
    "She sighs in annoyance but finally nods."
    pc "I just want to know how you are doing after taking the drug. Any side effects I should know about or anything?"
    charlene "I’m doing fine, and my side effects aren’t anything different from any of the others. Is that all? If you’re expecting me to open up and share my deepest feelings it’s not going to happen."
    pc "Do you mind if I ask why you seem to hate me so much? Other than the fact that I’m a man?"
    image luna_stage7_44 = "/luna/events/stage7/44.webp"
    scene luna_stage7_44
    charlene "I don't hate you. Well, at least not you specifically."
    charlene "It’s just I’ve learned that all men that I’ve known have all turned out to be total jerks."
    charlene "They only want you for sex or to assert power and control over you just because they are bigger and stronger and are men."
    pc "Well, if there is one thing that I hope to convince you of, it is that not all men are like that."
    charlene "I doubt you will succeed."
    pc "Can I at least try? We don’t have to be friends or anything but we are going to be working together and I would like to be able to do that without worrying if you are going to cut my dick off."
    charlene "I wasn't going to cut it off, just render it inoperable. I am a nurse after all and there are certain drugs that I could use to-"
    pc "I’ll just trust that you could really do it, I don’t need to know the details."
    image luna_stage7_45 = "/luna/events/stage7/45.webp"
    scene luna_stage7_45
    charlene "Fine. Well, I suppose if you want to... try to convince me that you aren't like any other man I've known then I'll let you. You won't succeed, but you can try."
    pc "Thank you. It's a start at least. So, what's the reason you wanted to take part in the drug test?"
    charlene "I’m sure one of the others has already told you that."
    pc "Yes, but I want to hear it from you."
    image luna_stage7_46 = "/luna/events/stage7/46.webp"
    scene luna_stage7_46
    charlene "Fine, if you must."
    charlene "The thing is, my mother and grandmother both died of a rare disease. A disease so rare that it wasn't being researched because there wasn't enough money in it to justify trying to find a cure."
    charlene "I also have a very high risk of getting it - if I don't already have it in the early stages. Basically, If I don't take this drug, I'll most likely die. With the drug I seem to have a chance."
    charlene "I actually started working at this particular hospital because I heard about the drug trial and it's the only real shot at a cure that I have."
    pc "I see. That's a pretty good reason."
    charlene "I’m also doing it because I want to prove that women can do amazing things, even when it comes to things like life-saving drugs."
    charlene "Honestly, I feel that having you here as a man takes some of that away when we really don't even need you."
    pc "Honestly, I don't really feel like you need me here either. However, I can assure you that I'm not here to take away any credit or glory or anything like that from you ladies."
    pc "Luna, Britta, and you and the other test subjects can have all that."
    charlene "At least you understand that. Well, I suppose I will just have to email you my measurements once I get them."
    pc "That would work."
    image luna_stage7_47 = "/luna/events/stage7/47.webp"
    scene luna_stage7_47
    "Charlene seems like she is about to leave, but then stops to tell you one last thing:"
    charlene "You may call me Charly, if you wish. See that you don't let me down, like I expect you to, and lose the right to call me that."
    pc "I’ll do my best to prove you wrong."
    "She nods and then leaves, allowing the next test subject to come in, who it turns out to be Sally."
    image luna_stage7_48 = "/luna/events/stage7/48.webp"
    scene luna_stage7_48
    sally "Are you ready for me?"
    pc "Yes. Please come in."
    image luna_stage7_49 = "/luna/events/stage7/49.webp"
    scene luna_stage7_49
    "Sally then strips naked for you and stands on the scale."
    if persistent.imperial:
        sally "I now weigh 194 lbs, which means I gained about 17.5 Pounds!"
    else:
        sally "I now weigh 88Kg, which means I gained 8 Kilograms!"
    image luna_stage7_50 = "/luna/events/stage7/50.webp"
    scene luna_stage7_50
    window hide
    pause
    "Sally turns around and raises her hands above her head and allows you to get her measurements."
    "It seems even before you get her measurements that it’s obvious more of her weight made its way into her hips and butt than the others."
    if persistent.imperial:
        pc "You’ve added about 3 and a half inches to your bust at around 39 inches, with a bra size of 34E."
        pc "Your waist has grown 2 inches. Your hips and butt have grown the most, adding 5 inches there, which puts you at 44 and a half inches around."
    else:
        pc "You’ve added about nine centimeters to your bust at around 99 cm, with a bra size of 34E."
        pc "Your waist has grown five centimeters. Your hips and butt have grown the most, adding about 13 centimeters there, which puts you at 113 centimeters around."
    image luna_stage7_51 = "/luna/events/stage7/51.webp"
    scene luna_stage7_51
    window hide
    pause
    "Sally looks over her now much more expanded, curvy body."
    sally "I thought the breast growth drug was supposed to mainly... well, make my breasts grow, not everywhere else."
    pc "Well, I'm sure it also depends on the woman taking it. You might just be predisposed to gain more in your hips, butt and thighs."
    sally "No matter. I'm perfectly okay with it, just curious is all. Besides, I've definitely been catching guys staring at my ass a lot lately."
    sally "As long as I get to eat as much as I want, whatever I want and this ass gets me laid I don’t mind."
    image luna_stage7_52 = "/luna/events/stage7/52.webp"
    scene luna_stage7_52
    "She turns around to show you it."
    sally "Do you like it?"
    pc "I’ll admit it, it is rather nice."
    image luna_stage7_53 = "/luna/events/stage7/53.webp"
    scene luna_stage7_53
    sally "You can have it if you want. In fact, you can have all of me if you want, right here and right now."
    "Her sudden offer for sex has you completely surprised."
    pc "Wait, what? Are you suggesting...?"
    image luna_stage7_54 = "/luna/events/stage7/54.webp"
    scene luna_stage7_54
    window hide
    pause
    sally "Yes. If you want to have sex with me you can, right here and now."
    sally "Honestly, this drug has been making me extra horny. My vibrator and fingers are nice, but I think I want something more real for once."
    sally "You’re an attractive enough looking guy and I bet you have a nice sized dick for me to enjoy getting impaled on."
    pc "Well, I'm not going to say I don't want to have sex with you, because of course I do, but I want to make sure it isn't just the drug influencing your judgement too much."
    pc "I don’t want to take advantage of you."
    image luna_stage7_55 = "/luna/events/stage7/55.webp"
    scene luna_stage7_55
    window hide
    pause
    sally "I wouldn't say it's really the drug. I mean, it does make me more horny, but I was already plenty horny before, I just never really acted much on it."
    sally "It's the same way with food. I always craved just eating and enjoying myself without having to worry about the extra pounds I would gain or the health downsides."
    sally "If anything this drug has only allowed me to free myself so I can have what I want and have been denying myself."
    pc "I see. Well, I'm glad you feel like you can allow yourself to be happy."
    pc "Honestly though, you sound kind of like Luna and her cause of being free to eat and enjoy sex as much as you want."
    image luna_stage7_56 = "/luna/events/stage7/56.webp"
    scene luna_stage7_56
    window hide
    pause
    sally "Yeah, me and Luna certainly do agree on that. In her case though it’s because of a cause that she’s actively working for while I’m more focused on just myself."
    sally "It's because I just want food and sex and I don't see any reason why I can't have those things now. Also, just in case you were worried; I'm safe, so no worries there."
    pc "Well, I suppose if you really do want to have sex it's not like I'm going to say no to a beautiful woman wanting to have sex with me."
    sally "A beautiful woman with a fat ass, no less. Like I said, you can have it along with the rest of me."
    image luna_stage7_57 = "/luna/events/stage7/57.webp"
    scene luna_stage7_57
    window hide
    pause
    "She pushes her big butt into you and you can’t resist placing your hands onto each cheek."
    image luna_stage7_58 = "/luna/events/stage7/58.webp"
    scene luna_stage7_58
    window hide
    pause
    "You can definitely appreciate a large behind and given Sally’s growth already in that area, she is definitely going to be gaining even more there."
    image luna_stage7_59 = "/luna/events/stage7/59.webp"
    scene luna_stage7_59
    window hide
    pause
    "After a moment of feeling up her ass, Sally pulls away."
    sally "Alright, I've let you enjoy my ass enough. Now I want to see that dick of yours."

    if persistent.nosexscene == True:
        "Sally and you had some quick and dirty sex."
    else:
        image luna_stage7_60 = "/luna/events/stage7/60.webp"
        scene luna_stage7_60
        window hide
        pause
        "She helps you pull down your pants, revealing your now fully erect penis to her."
        sally "Very nice. Even better and bigger than I thought. No wonder Luna keeps you around."
        pc "I’d like to think Luna keeps me around for other reasons besides just that."
        sally "Yeah, yeah. Well, at least for me you don't need to be all sappy and romantic and loving. I just want sex."
        sally "Also, no need for foreplay or anything like that either. I just want your dick in me."
        image luna_stage7_62 = "/luna/events/stage7/62.webp"
        scene luna_stage7_62
        "You decide that was enough talking and it was time to just give it her. You bend her over and do her doggy style."
        "You insert your dick into her warm and inviting pussy - slowly moving in deeper until your pelvis touches her soft and jiggly ass."
        window hide
        pause
        image luna_stage7_61 = "/luna/events/stage7/61.webp"
        scene luna_stage7_61
        sally "Mmm, yes. This is what I want."
        window hide
        pause
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage7/sex1_start.webm" loop
        show movie with dissolve
        pause
        "You slowly start thrusting into her, letting both of you get used to the feeling."
        sally "Do me harder and faster."
        stop movie
        window hide
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage7/sex1_ride1.webm" loop
        show movie with dissolve
        pause
        "Sally starts thrusting her hips into your big cock at a rapid pace."
        stop movie
        window hide
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage7/sex1_ride2.webm" loop
        show movie with dissolve
        pause
        "You guess she likes it hard and fast."
        "Instead of letting Sally do all the work, you decide to add to the motion by thrusting faster and harder yourself."
        stop movie
        window hide
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage7/sex1_thrust1.webm" loop
        show movie with dissolve
        pause
        sally "Ooh yeah! Give it to me!"
        "Before long as you ram into her you feel the pressure begin to build."
        stop movie
        window hide
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage7/sex1_thrust2.webm" loop
        show movie with dissolve
        pause
        "Well, she did say she was safe."
        "You let loose and allow each spurt of cum deep into her."
        stop movie
        image luna_stage7_63 = "/luna/events/stage7/63.webp"
        scene luna_stage7_63
        "After a moment, you then pull out."
        sally "Thanks for that."
        pc "You're welcome. Thank you too."

    image luna_stage7_64 = "/luna/events/stage7/64.webp"
    scene luna_stage7_64
    sally "Maybe I'll even let you do that to me again, when my ass and the rest of me is even fatter."
    pc "I have to admit I’m looking forward to it."
    "While you hadn’t exactly planned on this happening and it was rather quick, you still admittedly quite enjoyed it."
    image luna_stage7_65 = "/luna/events/stage7/65.webp"
    scene luna_stage7_65
    "Sally puts on her clothes and leaves. Britta comes in afterwards."
    britta "I guess it’s my turn?"
    pc "I guess so."
    image luna_stage7_66 = "/luna/events/stage7/66.webp"
    scene luna_stage7_66
    britta "I have to admit I am rather curious about your process."
    pc "My process?"
    britta "Well, yes. Every scientific study and measuring of results has a process."
    pc "I mean, I've just been taking measurements and seeing how each of the test subjects are doing."
    image luna_stage7_67 = "/luna/events/stage7/67.webp"
    scene luna_stage7_67
    "Britta is however now studying you with great interest, but for a totally different reason than what you were just discussing."
    britta "You just had sex, didn't you?"
    pc "Well…how would you even know that?"
    britta "Your pupils are still dilated, your body has produced a mild amount of sweat from recent physical exertion, your breathing is heavier than normal."
    britta "You seem to also bare the signs of having just released dopamine and other endorphins, which are-"
    pc "Okay, I get it. Yes, I'll admit I just had sex with Sally. She just kind of asked me for it and I kind of... just went along with it and agreed."
    image luna_stage7_68 = "/luna/events/stage7/68.webp"
    scene luna_stage7_68
    britta "Well, sex is a perfectly natural occurrence between humans - animals too for that matter - although humans don't merely do it for procreation, but also for pleasure."
    britta "The release of endorphins during intercourse-"
    pc "Sorry, you're really going to have to speak more... in a way that I can understand if you could, please. I'm nowhere near as smart as you."
    image luna_stage7_69 = "/luna/events/stage7/69.webp"
    scene luna_stage7_69
    britta "Sorry. I often have difficulty talking... normally. I will try to do so with you though."
    pc "I appreciate it."
    image luna_stage7_70 = "/luna/events/stage7/70.webp"
    scene luna_stage7_70
    "She seems to now be thinking hard about something again."
    britta "I have admittedly sometimes wondered what it would feel like to have sex."
    pc "You're a virgin? I mean, sorry if I said something wrong."
    image luna_stage7_71 = "/luna/events/stage7/71.webp"
    scene luna_stage7_71
    britta "It's fine. Yes, I am what you would call a virgin."
    britta "Apparently my intelligence can be rather much for a lot of people and I’ve mostly been focused on university or now my work, so I haven’t allowed myself time for romantic relationships."
    britta "That being said I have been curious about things of a sexual nature, especially lately, as it appears my sexual desires have increased since taking the drug."
    pc "It seems most - if not all - of the test subjects are going through the same side effect. It doesn't appear to be too overwhelming, like you need sex constantly, but it has increased."
    britta "Yes. It is something I am already researching further. Anyway, I think it's time for you to take my measurements and record my progress."
    pc "Yes, of course."
    image luna_stage7_72 = "/luna/events/stage7/72.webp"
    scene luna_stage7_72
    "Britta strips naked and goes over to the scale to weigh herself."
    if persistent.imperial:
        britta "I weigh 183 lbs which means I gained 11 Pounds!"
    else:
        britta "I weigh 83Kg which means I gained 5 Kilograms!"
    image luna_stage7_73 = "/luna/events/stage7/73.webp"
    scene luna_stage7_73
    "She then raises her hands above her head so you can get her measurements."
    britta "I do find it interesting how much attention my body seems to be getting lately. I've never really been noticed before - at least not for my body, only my intelligence."
    britta "It seems clear to me though that you at least find my body attractive based on the signs I’ve just noticed."
    pc "Well, I'm not going to deny it; you're an attractive woman. No need to worry though, I will try to keep things, umm..."
    image luna_stage7_74 = "/luna/events/stage7/74.webp"
    scene luna_stage7_74
    britta "Strictly professional, or at least as can be expected under the circumstances?"
    pc "Um, yeah. That."
    britta "I would admittedly normally want a strictly professional relationship with a male colleague, but perhaps in these particular circumstances…my approach may need to change."
    britta "I will have to do some research into the matter and let you know what my conclusion is."
    pc "Okay. Well... good luck with that."
    image luna_stage7_75 = "/luna/events/stage7/75.webp"
    scene luna_stage7_75
    "You aren’t really sure what to say to her and so instead you opt to start getting her measurements and then writing them down."
    "You then read the results to her."
    if persistent.imperial:
        pc "You’ve added nearly 4 inches to your bust now at 38 inches and a bra size of 34D."
        pc "You’ve added 2 inches to your waist, now at over 27 inches, and you’ve also added nearly 2 inches to your hips, which are now at 42 inches around."
    else:
        pc "You’ve added nearly ten centimeters to your bust now at 96,5 cm and a bra size of 34D."
        pc "You’ve added five centimeters to your waist, now at over 68,5 cm, and you’ve also added nearly five centimeters to your hips, which are now at 106,5 cm around."
    image luna_stage7_76 = "/luna/events/stage7/76.webp"
    scene luna_stage7_76
    "Britta nodded, seeming pleased with the results, but in a different way than most women probably would."
    britta "That seems right in line with my own predicted growth rate, based off of the amount of calories, fats, sugars, and other dietary considerations I’ve consumed."
    britta "Thanks by the way for calculating all that out for me and all the girls."
    pc "Yeah, I tried to get accurate or at least close guesses on all that. It was a lot of work though."
    britta "Well, you did a decent job."
    pc "Thanks."
    image luna_stage7_77 = "/luna/events/stage7/77.webp"
    scene luna_stage7_77
    britta "This will all be worth it! You'll see! We are making history here!"
    pc "Well, I'm glad that you are excited about that, but what do you think of the changes to your body?"
    image luna_stage7_78 = "/luna/events/stage7/78.webp"
    scene luna_stage7_78
    britta "Well, I... like them. Admittedly, I'm still getting used to them, but... they are nice."
    pc "Well, if you don't mind me saying; you look really good."
    britta "Thank you…you look good too."
    image luna_stage7_79 = "/luna/events/stage7/79.webp"
    scene luna_stage7_79
    "She looks at you again for a moment, but then her mind seems to go elsewhere."
    britta "Can I look at the measurements that you got from the other test subjects?"
    pc "Absolutely. Here you go."
    image luna_stage7_80 = "/luna/events/stage7/80.webp"
    scene luna_stage7_80
    "You hand over the notebook with each of the girls’ previous and current measurements and Britta looks it over."
    britta "Very good. All of them are still pretty much in the range of my predicted growth patterns."
    pc "Well, that's good then."
    britta "Yes, it is good. We are off to a decent start at least, but we will need to continue to monitor for further results."
    pc "Yes."
    image luna_stage7_81 = "/luna/events/stage7/81.webp"
    scene luna_stage7_81
    "You seem to think you are done with Britta but she has other ideas."
    britta "Are you not going to inspect my body further and more closely?"
    pc "Well, yes, if you want me to. I mean, I did with most of the other test subjects."
    "In some cases you inspected more closely than others, Sally for example both on the outside and inside."
    britta "I think it is important to the scientific process so of course I do."
    image luna_stage7_82 = "/luna/events/stage7/82.webp"
    scene luna_stage7_82
    window hide
    pause
    "You look over her body closely and then even touch and squeeze her breasts, purely for scientific reasons of course, to make sure they are fine.."
    pc "Your body seems to be perfectly fine and healthy."
    britta "That’s what I’ve concluded as well, thank you."
    image luna_stage7_83 = "/luna/events/stage7/83.webp"
    scene luna_stage7_83
    "She gets her clothes back on and leaves, allowing the last test subject to come in after her, which is Natalie."
    natalie "Sorry I was the last one, I’m still trying to figure out how to use the breast pump that they gave me."
    pc "It's fine. Do you maybe want some help or something... if you want?"
    image luna_stage7_84 = "/luna/events/stage7/84.webp"
    scene luna_stage7_84
    natalie "I would love some help, thanks, after you get my measurements and inspect my body."
    pc "No problem, happy to help."
    image luna_stage7_85 = "/luna/events/stage7/85.webp"
    scene luna_stage7_85
    "Natalie then strips naked and she actually seems eager and excited to do so, showing off her more curvy body to you."
    "In all honesty you were the most excited to see the improvements to Natalie’s body and she didn’t disappoint. She was already sexy to begin with but now even more so."
    image luna_stage7_86 = "/luna/events/stage7/86.webp"
    scene luna_stage7_86
    "Natalie goes over to the scale to weigh herself."
    if persistent.imperial:
        natalie "I now weigh 176 lbs, which means I gained 13 Pounds!"
    else:
        natalie "I now weigh 80Kg, which means I gained 6 Kilograms!"
    image luna_stage7_87 = "/luna/events/stage7/87.webp"
    scene luna_stage7_87
    "You get each of her measurements and then read the results all at once to her."
    if persistent.imperial:
        pc "You’ve added more than 5 inches to your bust with it now at nearly 38 and a half inches with you now at a 32F bra size."
        pc "Your waist grew less than half an inch now at more than 24 inches, your hips grew a little more than an inch and is now at 42 and a half inches."
    else:
        pc "You’ve added around 13 centimeters to your bust with it now at nearly 98 cm with you now at a 32F bra size."
        pc "Your waist grew only around a centimeter now at more than 61 cm, your hips grew a little more than two and a half centimeters and is now at 108 cm."
    image luna_stage7_88 = "/luna/events/stage7/88.webp"
    scene luna_stage7_88
    natalie "Mmm, I really do like the changes so far."
    pc "Me too…I mean-I’m glad for you."
    natalie "I especially like that you like them."
    image luna_stage7_89 = "/luna/events/stage7/89.webp"
    scene luna_stage7_89
    window hide
    pause
    "She gives you a look as if inviting you to look further, which you do."
    natalie "You can also touch me if you want. After all, you need to do an inspection, right? Make sure I'm healthy and progressing well?"
    pc "Um, yes."
    image luna_stage7_90 = "/luna/events/stage7/90.webp"
    scene luna_stage7_90
    window hide
    pause
    "You try your best to really inspect her body, but you end up touching her more than is needed."
    "Natalie probably knows this, but she also doesn't seem to mind. In fact, she seems to enjoy the feeling of your fingers on her skin."
    "You particularly can’t help but linger the most on her breasts, her big now F-cup breasts that even with a bunch of other busty women around still manage to command attention."
    image luna_stage7_91 = "/luna/events/stage7/91.webp"
    scene luna_stage7_91
    "However, Natalie then frowns and pulls away as she covers up her breasts."
    pc "Sorry if that was too much. I didn't mean to-"
    image luna_stage7_92 = "/luna/events/stage7/92.webp"
    scene luna_stage7_92
    natalie "No, you're fine. I like you touching them. It's just... your hands on them are getting them... excited, and it's causing me to lactate."
    pc "Oh, I see."
    natalie "Gross, right?"
    pc "Not at all. You don't need to worry about that with me. Do you want me to help you with the breast pump now then? I did offer after all."
    image luna_stage7_93 = "/luna/events/stage7/93.webp"
    scene luna_stage7_93
    "Natalie seems to relax at hearing you say that and instead smiles."
    natalie "Yes, please. Thanks."
    image luna_stage7_94 = "/luna/events/stage7/94.webp"
    scene luna_stage7_94
    window hide
    pause
    "She goes and gets the breast pump that Britta gave her. The two of you then try to figure the pump out."
    natalie "So maybe just stick the cup or whatever it’s called on my boob then and-"
    image luna_stage7_95 = "/luna/events/stage7/95.webp"
    scene luna_stage7_95
    "You press the button to see if it works and to the surprise of both of you it begins sucking hard on her nipple as milk is being squeezed out."
    pc "How does that feel?"
    natalie "Kind of weird, but also good at the same time."
    pc "Have you tried tasting some?"
    image luna_stage7_96 = "/luna/events/stage7/96.webp"
    scene luna_stage7_96
    natalie "Yes. It's actually really sweet. Do you maybe want to try some yourself?"
    pc "Sure, I guess I’ll have a taste."
    natalie "Well, you can have what I've gotten into the bottle so far or, if you want... you can drink it straight from the source."
    "Your eyes widen when hearing that."
    pc "Uh, yeah... but only if you want me to?"
    image luna_stage7_97 = "/luna/events/stage7/97.webp"
    scene luna_stage7_97
    natalie "I admit I’m kind of curious to find out just what it feels like with you in comparison to the machine."
    pc "Well, okay then... Here goes."
    image luna_stage7_98 = "/luna/events/stage7/98.webp"
    scene luna_stage7_98
    window hide
    pause
    "You lean down and put her nipple into your mouth and begin sucking."
    "Your eyes widen when you taste the first bit of milk."
    pc "You’re right, that is sweet!"
    natalie "I know, right?"
    image luna_stage7_99 = "/luna/events/stage7/99.webp"
    scene luna_stage7_99
    window hide
    pause
    "You suck a little more and taste it."
    pc "It’s also thicker than I would have expected. Is all breast milk like this?"
    natalie "I don't really know. I haven't actually tasted any since I was a baby."
    pc "Me neither."
    image luna_stage7_100 = "/luna/events/stage7/100.webp"
    scene luna_stage7_100
    natalie "I’m really glad that you liked it though as well as sucking my breast."
    pc "Yes, thank you."
    image luna_stage7_101 = "/luna/events/stage7/101.webp"
    scene luna_stage7_101
    "The two of you look at each for a moment before Natalie then shakes her head and starts putting her clothes back on."
    natalie "Well, thank you for helping me with that."
    pc "You’re welcome."
    "The two of you then go rejoin the others."
    image luna_stage7_125 = "/luna/events/stage7/125.webp"
    scene luna_stage7_125
    window hide
    pause
    "The others are already eating the massive amount of food that had apparently been ordered."
    sally "Great! You're finally back! Better hurry, Natalie, or we're going to eat it all."
    natalie "Coming!"
    roxie "I’m sure there is plenty for all of us."
    sally "Not the way I intend to eat, I’m starving! Could someone pass me the meatball subs?"
    pc "I’ll get them!"
    image luna_stage7_126 = "/luna/events/stage7/126.webp"
    scene luna_stage7_126
    window hide
    pause
    "You hurry and grab some meatball subs for Sally."
    pc "Anything else you girls want or need?"
    charlene "Well, I will admit it is nice having our own personal server."
    natalie "That isn’t just what he is."
    charlene "Yeah, yeah, but I'm just trying to come up with ways he's actually useful."
    image luna_stage7_127 = "/luna/events/stage7/127.webp"
    scene luna_stage7_127
    window hide
    pause
    natalie "He’s plenty useful!"
    pc "Thanks for standing up for me, Natalie, but it's okay. Besides, my other job is at a diner and I do sometimes serve food, so I'm pretty used to it by now. I'm just trying to help."
    natalie "Um... well, would you mind finding out if there are any more chocolate milkshakes?"
    pc "Sure."
    sally "I think Luna ordered us the weight gain powder ones."
    natalie "That's fine as long as it tastes great. Besides, we are all trying to gain weight and grow after all."
    image luna_stage7_128 = "/luna/events/stage7/128.webp"
    scene luna_stage7_128
    window hide
    pause
    "The girls keep you busy with trying to get them things, but you definitely don’t mind as you watch them eat and enjoy themselves to their hearts’ content."
    "They are just finishing all of the food when Luna finally comes back."
    image luna_stage7_122 = "/luna/events/stage7/122.webp"
    scene luna_stage7_122
    window hide
    pause
    roxie "Sorry, Luna, we kind of didn't save you any. We didn't know when you would be back."
    luna "Well, I don't know whether to be disappointed that you didn't save me any or proud that you managed to eat all of the food I had delivered for you."
    pc "They’ve all been good eaters."
    image luna_stage7_123 = "/luna/events/stage7/123.webp"
    scene luna_stage7_123
    window hide
    pause
    luna "I can see that. Keep up the good work!"
    roxie "We’ll certainly do our best."
    luna "Well, anyway, it's a good thing I also had some food sent to my office because I'm starving! Also, [playername], will you come see me in my office?"
    sally "Ooh, someone's in trouble!"
    image luna_stage7_124 = "/luna/events/stage7/124.webp"
    scene luna_stage7_124
    window hide
    pause
    "Roxie says something but it’s so quiet you are pretty sure you are the only one who heard."
    roxie "I wish I was inside Luna’s office with her for being naughty."
    "At any rate you follow Luna, and you are pretty sure that she wasn’t having you come join her because you are in trouble."
    image luna_stage7_102 = "/luna/events/stage7/102.webp"
    scene luna_stage7_102
    window hide
    pause
    "Upon arriving in her office, Luna sits down and starts eating all the food that she has sitting on her desk."
    luna "Mmm, that's better. I wish I could eat during those meetings. Honestly, I'm kept so busy I don't get nearly enough time to eat as much as I want."
    image luna_stage7_103 = "/luna/events/stage7/103.webp"
    scene luna_stage7_103
    "She then looks at you and starts up a conversation in between bites."
    luna "So, how are my girls doing?"
    pc "Are you referring to the test subject or your boobs? Because in your case it can sometimes be hard to tell."
    image luna_stage7_104 = "/luna/events/stage7/104.webp"
    scene luna_stage7_104
    luna "Hah, hah, very funny. You may be right about that, but this time I'm referring to the test subjects."
    "You try to fill her in on the growth that each of them has achieved so far, which seems to make Luna happy."
    image luna_stage7_105 = "/luna/events/stage7/105.webp"
    scene luna_stage7_105
    luna "Very good. Wonderful to hear. That kind of progress is something that I can bring to investors."
    pc "Investors?"
    luna "Yes. What do you think the meeting I was just in was about? A lot of my meetings in person and on the phone involve trying to gather investors for the drug."
    luna "Even if the drug is successful we’re still going to need money to get us through until the drug makes it to market and even getting it to market will be expensive."
    luna "It's a rather annoying task, but, unfortunately, a necessary one. I'm hoping to get some good investments soon."
    pc "Well, I wish you luck with that. Anything I can do to help?"
    image luna_stage7_106 = "/luna/events/stage7/106.webp"
    scene luna_stage7_106
    luna "You're sweet for always offering to help, but no, I'm fine. I think I'd rather hear about how much you enjoyed each of the girls. So which of them have you had sex with so far?"
    "Your eyes widen at her asking so blatantly."
    pc "Wait, how do you know?"
    image luna_stage7_107 = "/luna/events/stage7/107.webp"
    scene luna_stage7_107
    "Luna just grinned widely."
    luna "I didn’t know but you just confirmed it for me. So who is it?"
    luna "I know it isn’t Britta, she doesn’t even know anything about sex beyond what she’s read about."
    luna "No way it would be Charly, even though I’m betting some great sex would probably do her a world of good and make her not so uptight, hmm…so that leaves Roxie, Natalie, and Sally."
    pc "I guess I could just tell you."
    image luna_stage7_108 = "/luna/events/stage7/108.webp"
    scene luna_stage7_108
    luna "No. I want to figure it out myself. Well, Natalie, I know has a thing for you and you have a thing for her, but I don't think she would ready to go that far just yet."
    luna "Roxie might do it, but she clearly has a massive thing for me already."
    pc "Wait, you already know about that?"
    image luna_stage7_109 = "/luna/events/stage7/109.webp"
    scene luna_stage7_109
    luna "Of course. It's been so obvious for the longest time. I mean, she isn't bad-looking and she's got just these gorgeous green eyes."
    luna "She's always been rather too thin for my taste though, but, of course, that's all going to change."
    luna "I suspect she might have actually wanted to be a test subject so bad in order to get me more interested in her, and I have to confess it is starting to work."
    pc "Well, based on what she told me that does seem to be a major reason for her taking the drug."
    image luna_stage7_110 = "/luna/events/stage7/110.webp"
    scene luna_stage7_110
    luna "Well, if she continues to grow like she is, I just might give her what she wants."
    luna "Of course that means I'm going to have to figure out how to get around the whole boss-employee relationship thing again."
    pc "Well, I suppose you did find a way around it with me, but then again, we were also together even before I started working for you."
    luna "Ah, well, I'll figure it out. Anyway, if I thought it was Roxie you had sex with I would definitely want to know how it was, so I know what to potentially expect for myself."
    luna "I'm pretty sure it must have been Sally. Am I right?"
    pc "Yes, you’re right."
    image luna_stage7_111 = "/luna/events/stage7/111.webp"
    scene luna_stage7_111
    luna "I knew it! That girl has really been turning into such a glutton lately."
    pc "Glutton?"
    luna "Don’t you pay attention in Daisy’s health classes or are you too busy staring at or feeding the teacher?"
    pc "I know what a glutton is, but doesn't that apply to food? I mean, I know Sally really seems to enjoy eating whatever she wants."
    pc "But I’m not sure how that relates to why she would want to have sex with me, not that I’m complaining of course."
    image luna_stage7_112 = "/luna/events/stage7/112.webp"
    scene luna_stage7_112
    luna "Well, you're right, a glutton is a person who just eats lots of food without any worries for the consequences."
    luna "But I’d like to think it can also mean a person giving in and enjoying themselves with their desires in other ways too such as sex."
    luna "Of course I identify with that, I’m trying to get her to join my cause and not just focus on herself."
    luna "But alas, she still doesn't seem interested. Maybe someday I'll get her to join. How was the sex then?"
    pc "Pretty quick but pretty good."
    image luna_stage7_113 = "/luna/events/stage7/113.webp"
    scene luna_stage7_113
    luna "Oh, come on! Give me details! Don't leave a girl hanging!"
    "You do your best to try to explain how the sex was, which was rather quick so there really isn’t much to tell anyway, but at the end you try to quickly point out something."
    pc "The sex was still nowhere near as good as it is with you though."
    image luna_stage7_114 = "/luna/events/stage7/114.webp"
    scene luna_stage7_114
    "Luna just smiled knowingly."
    luna "Well, of course not. I certainly wasn't worried about that. I'm happy to see the girls are growing and gaining, but I'm always going to be the biggest and the best - sex included."
    pc "If I disagree will it mean I can get you to eat more so you can make sure to maintain your lead?"
    luna "You could but you don’t need to do that to get me to eat more."
    pc "True. How about I just try to stuff you full again?"
    luna "Sounds good to me."
    image luna_stage7_115 = "/luna/events/stage7/115.webp"
    scene luna_stage7_115
    window hide
    pause
    "As you try feeding her, you also take the opportunity to feel up her huge boobs, which despite the other test subjects’ recent growth are still quite a bit bigger than any of theirs."
    pc "You know maybe I should measure you and inspect you as well? You are a test subject after all."
    image luna_stage7_116 = "/luna/events/stage7/116.webp"
    scene luna_stage7_116
    window hide
    pause
    "She looks at you with amusement."
    luna "Is that an excuse to see me naked and feel me up?"
    pc "I don't need an excuse to see you naked and feel you up. I would just start taking off your clothes and start touching you wherever I please and you would welcome it."
    luna "Of course. But sure, if you want to start taking my measurements too, you certainly can. It saves me the hassle of trying to do it myself."
    image luna_stage7_117 = "/luna/events/stage7/117.webp"
    scene luna_stage7_117
    window hide
    pause
    "Luna then strips naked for you with you helping her. She then finds some measuring tape for you."
    image luna_stage7_118 = "/luna/events/stage7/118.webp"
    scene luna_stage7_118
    window hide
    pause
    "As you measure her, you also take the opportunity to touch each part of her body that you measure. This isn't needed, but you do it because you want to and you know Luna won't mind."
    "After getting all the measurements, you let Luna know the results."
    if persistent.imperial:
        pc "Your bust is now 46 inches around and you now need a 36J bra."
        pc "I can't measure your waist accurately right now because of all the food that is crammed in there, and your hips are 44 and a third inches around."
    else:
        pc "Your bust is now 117 centimeters around and you now need a 36J bra."
        pc "I can't measure your waist accurately right now because of all the food that is crammed in there, and your hips are 114 cm around."
    image luna_stage7_119 = "/luna/events/stage7/119.webp"
    scene luna_stage7_119
    window hide
    pause
    luna "Not bad, but not nearly as much as I would like. I'm still beating the other test subjects though, right?"
    pc "Well, your bust definitely is, but it seems Sally now has ever so slightly wider hips and butt than you."
    luna "She already caught up to me and is now beating me?"
    pc "I guess so, but don’t worry, you still-"
    luna "No need to reassure me that I'm still beautiful and sexy and all that. I'm a big girl, I can handle it. Besides, I'm still the biggest where it matters most and that's really what I care about."
    image luna_stage7_120 = "/luna/events/stage7/120.webp"
    scene luna_stage7_120
    window hide
    pause
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage7/boobshake.webm" loop
    show movie with dissolve
    pause
    "She shows off her naked huge breasts proudly and she happily jiggles them around, letting you enjoy the view of her huge 36 J-cup breasts."
    pc "So big and beautiful."
    stop movie
    image luna_stage7_121 = "/luna/events/stage7/121.webp"
    scene luna_stage7_121
    window hide
    pause
    luna "Mmm, for sure. I want all of me to be big and beautiful, but especially these. I also can't wait to see just how big the other test subjects get. They are making such good progress already."
    pc "I guess we can look forward to finding out."
    "You say goodbye to Luna and go back home."

    if recollection == False:
        $ luna.weight += 1
        $ daytime += 1
        $ phonecall = 1
        #Unlocks Sally Undress in the stats page.
        $ renpy.notify("Sally Undress option unlocked in stats screen.")
        window hide
        pause
        #Unlocks Britta Undress in the stats page.
        $ renpy.notify("Britta Undress option unlocked in stats screen.")
        window hide
        pause
    $ lunastage7event = 0
    return

label Luna_Stage_8_Event:
    "You get a phone call from Luna."
    pc "Hey, Luna. What's up?"
    luna "Can you come meet me at the hospital again for something at the drug research lab? It won’t take long but I was also thinking of maybe going on a date afterwards if you would like?"
    pc "Of course! I’ll meet you there."

    image luna_stage8_1 = "/luna/events/stage8/1.webp"
    scene luna_stage8_1
    "Upon getting to the hospital, you are expecting to see Natalie sitting at her usual place at the receptionist desk, instead you find Luna sitting there, who smiles when she sees you."
    image luna_stage8_2 = "/luna/events/stage8/2.webp"
    scene luna_stage8_2
    luna "Hi, [playername]! Expecting to see your favorite sexy redhead receptionist only to find your sexy girlfriend instead?"
    pc "Hi, Luna! Well, I kind of was expecting Natalie to be here. So, where is she anyway?"
    image luna_stage8_3 = "/luna/events/stage8/3.webp"
    scene luna_stage8_3
    luna "I fired her of course."
    "Luna tried to sound really serious, but you know her well enough not to fall for it."
    pc "You’re just messing with me, aren’t you?"
    image luna_stage8_4 = "/luna/events/stage8/4.webp"
    scene luna_stage8_4
    luna "Of course. I could never fire Natalie. I'm just watching the front desk for her while she's pumping breast milk. She's really starting to produce quite a bit."
    pc "Yeah, I would definitely have been upset if you really had fired her."
    luna "Don't worry about that, she does a great job. Besides, I know how much you like her."
    pc "Well, yeah... I do."
    image luna_stage8_5 = "/luna/events/stage8/5.webp"
    scene luna_stage8_5
    luna "So when are you going to ask her out?"
    pc "I don't know. I mean, she's had rough relationships in the past and I don't want to hurt her."
    pc "And of course I already have you as my girlfriend and all the other female relationships I have going on and-"
    luna "Just be open and honest with her. That's exactly what a girl like Natalie really needs, I think."
    luna "Let her know that anything between you two won't be exclusive. She obviously already knows about me and can probably guess that I'm not the only one."
    luna "If she is okay with that, then you can go from there."
    pc "That's actually really good advice. Thank you."
    luna "Of course! I'd like to think I give good advice when it comes to women - I am one after all."
    image luna_stage8_6 = "/luna/events/stage8/6.webp"
    scene luna_stage8_6
    "You give a look at Luna’s huge boobs."
    pc "It sort of feels more and more like you are three girls though, you and the girls on your chest."
    image luna_stage8_7 = "/luna/events/stage8/7.webp"
    scene luna_stage8_7
    luna "Haha, yeah, and I do love my girls!"
    "Luna happily shows off her increasingly more massive breasts."
    image luna_stage8_8 = "/luna/events/stage8/8.webp"
    scene luna_stage8_8
    luna "Speaking of girls, what is your decision regarding Natalie? I know you like each other."
    luna "It's just... I feel like Natalie is so shy and nervous when it comes to you and you are so worried about hurting her that neither of you will ask the other one out if I don't intervene."
    pc "I suppose you've got a point there and I do want to ask her out. I am, however, still surprised that you are actually encouraging this."
    luna "I could say that you clearly don’t know me as well as I would have thought you did."
    luna "I’m guessing it’s because you still can’t get over the fact that your girlfriend is encouraging you to date or hook up with another girl?"
    pc "Yes, that."
    luna "Do you want me to be honest?"
    pc "Yes, please."
    image luna_stage8_9 = "/luna/events/stage8/9.webp"
    scene luna_stage8_9
    luna "It's hot of course! I mean, I could say I just want Natalie and you to be happy, which I do."
    luna "But I can’t help but think of you doing her, making her feel incredible and sexy just like the way that you do for me, all while stuffing her full of food to make her even more sexy."
    pc "Well, I guess I appreciate the honesty, but I feel like I should take things a little slower with Natalie if I do end up dating her. So probably no sex for at least a while."
    luna "Which is why I think you will be perfect for her."
    luna "However long it takes, I’m confident you two are going to hook up and when you do you have to at the very least give me all the very juicy and sexy details."
    luna "Or you know, let me watch, or even better than that, join in."
    pc "I feel like I should probably warn you that Natalie might not go for that."
    image luna_stage8_10 = "/luna/events/stage8/10.webp"
    scene luna_stage8_10
    luna "Hey, a girl can dream and fantasize, can't she? I mean, it's not like Natalie is the only girl that I've imagined you with."
    pc "You’ve imagined me with other girls then? How many?"
    image luna_stage8_11 = "/luna/events/stage8/11.webp"
    scene luna_stage8_11
    luna "Um, no comment on that. I don't mean to fantasize about it too often, but sometimes I just can't help myself."
    pc "Maybe it’s for the best I don’t know just what kind of thoughts go through your head."
    luna "You're probably right. Well, I think telling you that I want you and Natalie to start dating is enough sharing of my thoughts for now."
    pc "Okay. Thank you, Luna."
    luna "You’re very welcome!"
    image luna_stage8_12 = "/luna/events/stage8/12.webp"
    scene luna_stage8_12
    "Luna then leans over and helps herself to some of Natalie's donuts."
    luna "What can I say other than that Natalie has great taste in snacks?"
    image luna_stage8_13 = "/luna/events/stage8/13.webp"
    scene luna_stage8_13
    luna "I figure since I'm helping her out I can have a little bit, but it is really hard not to just eat all of them. I really have to stop myself. It almost feels like I'm on a diet."
    pc "The only diet you’re on is the seefood diet, as in you see food and you eat it."
    luna "Haha, yeah, and that’s the only diet I’m ever going on, ever again!"
    image luna_stage8_14 = "/luna/events/stage8/14.webp"
    scene luna_stage8_14
    "Luna takes another donut to eat."
    image luna_stage8_15 = "/luna/events/stage8/15.webp"
    scene luna_stage8_15
    "Before she can eat too much however, a woman comes into the hospital."
    "She clearly looks quite sick and weak and seems to be struggling to walk."
    image luna_stage8_16 = "/luna/events/stage8/16.webp"
    scene luna_stage8_16
    luna "Oh, hi, Mylenna! So nice to see you again! Are you ready?"
    mylenna "Oh, hi, Luna! Yes, I'm ready! I'm pretty nervous, but I want you to know I'm super grateful for this opportunity. You have no idea how much it means to me!"
    luna "Well, you know I can't exactly guarantee anything, but I will say there is at least a chance."
    mylenna "I understand. But a chance, no matter how small, is much better than what I had before. At least now I have a reason to have some hope."
    image luna_stage8_17 = "/luna/events/stage8/17.webp"
    scene luna_stage8_17
    "Luna then turns to you."
    luna "This is Mylenna, one of our patients. She's unfortunately got a terminal illness and doesn't have long to live."
    luna "She’s actually the reason I wanted you to meet me here briefly, I’ve decided to have her test out the new drug as it could still potentially save her."
    luna "Obviously, I wouldn't normally do this for public use already, but she really doesn't have the time to wait."
    mylenna "Unfortunately, no, I don't. The doctors tell me I only have months to live."
    pc "Oh. I'm... so sorry to hear that... I really don't know what to say."
    image luna_stage8_18 = "/luna/events/stage8/18.webp"
    scene luna_stage8_18
    mylenna "It's fine, really. Nobody knows what to say to me."
    mylenna "I mean, I've known about my diagnosis for long enough for me to make my peace with it."
    mylenna "The hardest part is worrying about what will happen to my daughter though. She is only three and I'm all that she has."
    mylenna "When or if I’m gone what happens to her? Does she end up in foster care or somewhere where she doesn’t get the love and attention she deserves? I would hate to see that happen."
    luna "I mean, I'm not involved with Child Protective Services or anything like that, but I would still try to do my best to see that your daughter went to a loving home if the worst should happen."
    natalie "I would even adopt her myself before I let her go into foster care or ended up in a bad place."
    image luna_stage8_19 = "/luna/events/stage8/19.webp"
    scene luna_stage8_19
    "You turn to see Natalie standing there, having apparently gotten back from breast pumping. She sets a large glass of milk on the desk."
    "Luna wasn’t kidding, she is already producing a lot of milk."
    image luna_stage8_20 = "/luna/events/stage8/20.webp"
    scene luna_stage8_20
    "Mylenna, however, seems touched by Natalie's generous offer."
    mylenna "You would actually do that for me? You barely even know me though."
    natalie "Yes, I really would if you wanted me to. Although, to be fair, I'm not sure they would let me since I'm a single woman and I work odd, often overnight hours. But yes, I would."
    natalie "I’ve always wanted to be a mom and your daughter is super cute and so sweet every time she comes in! Where is she this time by the way?"
    mylenna "At home being watched by a babysitter. I know she doesn't like needles, so I didn't want her here to see that part."
    image luna_stage8_21 = "/luna/events/stage8/21.webp"
    scene luna_stage8_21
    luna "We actually won't need to use a needle on you. We've developed a new way to have you just drink the drug instead."
    luna "We figured that method would be safer as it will take longer to take effect."
    luna "It won’t be such a shock to your system and with your current weakened condition we didn’t want to take any risks we didn’t have to."
    mylenna "Well, that's... very thoughtful of you. Thank you."
    mylenna "You’ve already made me aware of the risks and side effects and I’ll gladly go through whatever I have to if it means I get to live and be there for my little girl."
    luna "Well, we are certainly rooting for you and hoping that it works."
    image luna_stage8_22 = "/luna/events/stage8/22.webp"
    scene luna_stage8_22
    "Mylenna, however, couldn't help but look at Luna's chest worriedly."
    mylenna "Forgive me but I can’t help but wonder if mine are going to get as big as yours? I don’t really want that to be honest."
    luna "Possibly. But probably not. This is a result of me eating massive quantities of food and trying to make them as big as possible."
    image luna_stage8_23 = "/luna/events/stage8/23.webp"
    scene luna_stage8_23
    mylenna "Wouldn’t eating a lot help the drug take effect better?"
    luna "Well, yes. That is true."
    mylenna "I guess I'm eating as much as I can then if it means I have a better chance of survival. I'll just have to deal with having really huge boobs."
    image luna_stage8_24 = "/luna/events/stage8/24.webp"
    scene luna_stage8_24
    luna "You make it sound like it's a bad thing. Really, all of the side effects of the drug I think are great - especially the boobs."
    natalie "Honestly, I agree. I love eating whatever and however much I want and I love the curves it's giving me."
    image luna_stage8_25 = "/luna/events/stage8/25.webp"
    scene luna_stage8_25
    "She proudly shows off her own now large assets and looks at you, enjoying the look you are giving her back."
    image luna_stage8_26 = "/luna/events/stage8/26.webp"
    scene luna_stage8_26
    luna "It really will all be okay, Mylenna. Trust me."
    mylenna "Thank you for the support. I guess I'll just have to get used to whatever side effects I go through."
    image luna_stage8_27 = "/luna/events/stage8/27.webp"
    scene luna_stage8_27
    "Luna then looks at Natalie."
    luna "I should probably admit that I helped myself to your snacks, Natalie. I didn't eat all of them though."
    natalie "I kind of figured you wouldn't be able to resist. It's fine though since you definitely earned it for helping me out. Thanks again by the way."
    image luna_stage8_28 = "/luna/events/stage8/28.webp"
    scene luna_stage8_28
    luna "You're totally welcome! So, Mylenna, I think it is about time we got you to the lab to get you that dose of the drug."
    "Mylenna still looks nervous, but nods."
    image luna_stage8_29 = "/luna/events/stage8/29.webp"
    scene luna_stage8_29
    "You, Luna, and Mylenna head off to the lab, and you quickly realize it’s probably a good thing that you are accompanying Mylenna as she seems really weak."
    "Luna offers to get her a wheelchair but Mylenna declines, seeming to want to do this herself."
    image luna_stage8_30 = "/luna/events/stage8/30.webp"
    scene luna_stage8_30
    "In any case, while it takes longer than normal since Mylenna walks slower than you and Luna walk, you make it inside the lab where Britta is waiting - snacks in mouth and reading a book."
    "Britta seems pretty interested in whatever she is reading, which at first you just assume is some complicated math or science book."
    luna "Hi, Britta."
    image luna_stage8_31 = "/luna/events/stage8/31.webp"
    scene luna_stage8_31
    "Britta is startled as she realizes suddenly that she has company."
    britta "Uh, hi... Sorry. I was just... doing some independent study."
    luna "What are you reading? Also, more importantly, what are you eating?"
    image luna_stage8_32 = "/luna/events/stage8/32.webp"
    scene luna_stage8_32
    "Luna tries to go over and help herself to Britta’s snacks, who seems much less willing to share than Natalie."
    britta "Hey! No touching!"
    luna "Just a little, besides you could argue that I paid for those snacks since I pay you and you bought them with money I gave you."
    image luna_stage8_33 = "/luna/events/stage8/33.webp"
    scene luna_stage8_33
    britta "Interesting logic, but I need this food for higher brain function."
    luna "Chicken nuggets are higher brain function food? Just admit it, you just want to pig out on tasty snacks."
    image luna_stage8_34 = "/luna/events/stage8/34.webp"
    scene luna_stage8_34
    britta "Alright fine, I love to eat now and I don’t care how unhealthy they are, happy?"
    "Britta seems quite annoyed but also nervous."
    pc "Is there something going on, Britta? You seem worried about something."
    image luna_stage8_35 = "/luna/events/stage8/35.webp"
    scene luna_stage8_35
    "Britta sighs."
    britta "Well, if you really must know. You remember our last conversation? You know, about sexual intercourse?"
    pc "Yes, I do."
    image luna_stage8_36 = "/luna/events/stage8/36.webp"
    scene luna_stage8_36
    britta "Well, I've been doing a lot of studying into sexual intercourse and the best scientifically proven method with which to engage in it."
    britta "It's fascinating in study, but it seems rather difficult in practice."
    luna "Well, books can only teach you so much when it comes to sex. The best way to learn is by actually doing it."
    britta "I…suppose so."
    image luna_stage8_37 = "/luna/events/stage8/37.webp"
    scene luna_stage8_37
    "She looks at you for a moment and then starts shaking her head."
    britta "Anyway, it's something I should be worrying about later. I have work to do now."
    luna "While I don't see anything wrong with wanting to study sex, you do indeed have work to do, Britta. This here is Mylenna."
    image luna_stage8_38 = "/luna/events/stage8/38.webp"
    scene luna_stage8_38
    "Through all of their conversation, Mylenna has stood there quietly."
    britta "Hi, Mylenna. Sorry to ignore you. If you want to come have a seat over here, I'll administer the drug to you."
    image luna_stage8_39 = "/luna/events/stage8/39.webp"
    scene luna_stage8_39
    "Mylenna goes over and sits down."
    britta "So, of course I ordinarily would never want to have a drug tested on the public so early into testing, but given your situation and with Luna persuading me, I've agreed to test it out on you."
    britta "I figured it really couldn't hurt to try. And if it does work on you and saves your life, it would certainly show just how effective and useful it could be."
    luna "I care much more about saving lives, but it would admittedly be a strong selling point for potential investors."
    pc "So how is that going by the way in getting investors?"
    image luna_stage8_40 = "/luna/events/stage8/40.webp"
    scene luna_stage8_40
    luna "Honestly, it could still be better. Most people seem to think it all sounds too good to be true. I'll find someone though, don't worry."
    "Despite Luna saying not to worry, it seems obvious that Luna herself is rather worried, but you decide not to push her on it."
    image luna_stage8_41 = "/luna/events/stage8/41.webp"
    scene luna_stage8_41
    "Meanwhile, Britta has been going over the drug and potential side effects with Mylenna."
    britta "Having taken the drug myself the side effects can be a bit…challenging. It’s difficult to mentally function as you tend to think more about food or sex."
    pc "That just sounds like the same things most men mostly think about anyway and I manage to still function."
    image luna_stage8_42 = "/luna/events/stage8/42.webp"
    scene luna_stage8_42
    luna "It's not just men, you know. I was already obsessed with both of those things before the drug and really only just a little more so now."
    britta "I was always totally focused on my work and never had such urges. I would even sometimes forget to eat and sexual desires were foreign to me, so this has taken some getting used to."
    image luna_stage8_43 = "/luna/events/stage8/43.webp"
    scene luna_stage8_43
    mylenna "Well, in any case, given the alternative, I'll take any side effects over death."
    britta "Good point. So, are you ready?"
    image luna_stage8_44 = "/luna/events/stage8/44.webp"
    scene luna_stage8_44
    mylenna "Yes, I’m ready."
    "She still looks nervous but definitely willing to try it."
    image luna_stage8_45 = "/luna/events/stage8/45.webp"
    scene luna_stage8_45
    "Britta gets out a vial of green liquid."
    luna "Don't worry, it actually tasted pretty good. I tried some myself earlier."
    britta "You weren't supposed to drink all of it though. Who knows what a second dose will do?"
    luna "Make my boobs even bigger? Besides, I seemed to have stopped growing anyway. I needed that second dose if I wanted to continue growing."
    pc "Well, I certainly want to see you continue to grow."
    image luna_stage8_46 = "/luna/events/stage8/46.webp"
    scene luna_stage8_46
    "You don’t see any need to hide it and Luna smiles happily at you."
    image luna_stage8_47 = "/luna/events/stage8/47.webp"
    scene luna_stage8_47
    "Meanwhile Britta hands Mylenna the vial of the drug."
    image luna_stage8_48 = "/luna/events/stage8/48.webp"
    scene luna_stage8_48
    "Mylenna drinks it."
    image luna_stage8_49 = "/luna/events/stage8/49.webp"
    scene luna_stage8_49
    mylenna "You’re right, it is pretty good."
    image luna_stage8_50 = "/luna/events/stage8/50.webp"
    scene luna_stage8_50
    luna "Told you. Honestly, I wish I could drink a lot more."
    pc "What would happen if you did drink a lot more? Like a couple dozen vials of it or something?"
    image luna_stage8_51 = "/luna/events/stage8/51.webp"
    scene luna_stage8_51
    luna "What, are you hoping that if I were to do that, it would make my boobs the size of yoga balls in a matter of days?"
    pc "Um…just wondering."
    image luna_stage8_52 = "/luna/events/stage8/52.webp"
    scene luna_stage8_52
    "Luna, however, laughed, seeming to be quite amused by the question."
    image luna_stage8_53 = "/luna/events/stage8/53.webp"
    scene luna_stage8_53
    britta "I don't see what is so funny! Taking that much of the drug at once would be highly dangerous!"
    image luna_stage8_54 = "/luna/events/stage8/54.webp"
    scene luna_stage8_54
    luna "It also wouldn't work, unfortunately, or I might be at least tempted to try a larger dose."
    luna "The size growth is also dependent on the amount of food you can eat, and while I can eat a lot more than a normal person even I have my limits."
    pc "Apparently I need to work on you greatly increasing your limits."
    luna "Indeed. Maybe we need to test those limits again on our date. I'm assuming that you can finish up with Mylenna, Britta?"
    britta "Of course, no problem."
    image luna_stage8_55 = "/luna/events/stage8/55.webp"
    scene luna_stage8_55
    "You and Luna head off and on your way out, you see Natalie again."
    "Remembering your conversation with Luna about Natalie, you decide to just go ahead and do it."
    image luna_stage8_56 = "/luna/events/stage8/56.webp"
    scene luna_stage8_56
    pc "Hey, Natalie, I was just wondering if maybe you wanted to do something together sometime?"
    image luna_stage8_57 = "/luna/events/stage8/57.webp"
    scene luna_stage8_57
    "Natalie definitely looks surprised, but then smiles happily."
    natalie "Really? You mean like on a date? Like with me?"
    "She still seems unable to believe that this is actually happening and you are asking her out."
    pc "Uh, yeah, if you want to, of course."
    natalie "I definitely want to but what about…"
    image luna_stage8_58 = "/luna/events/stage8/58.webp"
    scene luna_stage8_58
    "Natalie then looks over at Luna worriedly."
    luna "Oh, don't worry about me, I've actually been encouraging him to ask you out. I think you two would be good together."
    pc "Honestly, I really like you, Natalie, but I would never ask you out if Luna didn't approve."
    image luna_stage8_59 = "/luna/events/stage8/59.webp"
    scene luna_stage8_59
    natalie "Are... are you sure? I mean, I really, really like you too, but I don't want to mess anything up or make anyone mad."
    luna "And both you and [playername] being so concerned is exactly why I’m not worried."
    pc "I'll also come clean with you right now, Natalie. Luna isn't the only one I'm having relations with and anything we might end up having won't be exclusive either."
    image luna_stage8_60 = "/luna/events/stage8/60.webp"
    scene luna_stage8_60
    natalie "I'll admit I would rather have you to myself but I can live with having to share you. Are you sure you want me though?"
    pc "Why would anyone not want you? You’re such a beautiful woman on the inside and out."
    luna "You’re probably a more beautiful person than even me."
    image luna_stage8_61 = "/luna/events/stage8/61.webp"
    scene luna_stage8_61
    "Natalie blushes at the compliments."
    image luna_stage8_62 = "/luna/events/stage8/62.webp"
    scene luna_stage8_62
    natalie "Oh, I don't know about that, Luna. You're one of the most beautiful women and one of the best people I've ever met. I'm just hoping to be half the woman you are."
    luna "Thank you for the compliments. We still definitely need to work on your self-confidence though."
    pc "Agreed. You have no reason to feel less than anybody and I hope that I can show you just how incredible you are. So, anyway, would you like to go on that date with me then?"
    image luna_stage8_63 = "/luna/events/stage8/63.webp"
    scene luna_stage8_63
    "Natalie smiled widely with excitement."
    natalie "I would love to go out with you on a date!"
    "You can’t help but smile back happily."
    pc "Great! So when are you available?"
    image luna_stage8_64 = "/luna/events/stage8/64.webp"
    scene luna_stage8_64
    natalie "Well, I'm busy with work for the next while. But how about after our next measurements and weigh in?"
    natalie "That will give me time to work extra hard on eating and growing and gaining for you for our date."
    pc "That certainly sounds good, but you don’t have to do that for me."
    image luna_stage8_65 = "/luna/events/stage8/65.webp"
    scene luna_stage8_65
    natalie "I really want to though. I know how much you like big boobs and bigger girls and I want to be sexy for you."
    luna "If she wants to do that for you, then let her."
    luna "I mean, I'm trying to grow as much as possible - not just for you - but it certainly is a factor. I think it's great that Natalie is feeling the same way as well."
    pc "Well, alright then, sounds good. We'll have our date after my next visit then."
    natalie "Looking forward to it."
    image luna_stage8_66 = "/luna/events/stage8/66.webp"
    scene luna_stage8_66
    "You are about to leave with Luna, but then Natalie stops you."
    natalie "Wait! Actually, I was wondering if you might like to have something."
    luna "Presents already? You really do must like him."
    image luna_stage8_67 = "/luna/events/stage8/67.webp"
    scene luna_stage8_67
    "Natalie blushes, but then she goes and pulls out a container of milk."
    natalie "I know you liked drinking my milk last time, so I was wondering if you might like it now? I tried donating the milk, but apparently it's too thick and much too fattening for babies."
    luna "If he doesn’t want it, I’ll drink it!"
    pc "Sure. Thanks, Natalie. That was really thoughtful of you."
    image luna_stage8_68 = "/luna/events/stage8/68.webp"
    scene luna_stage8_68
    "Natalie smiles happily once again."
    natalie "You’re very welcome!"
    image luna_stage8_69 = "/luna/events/stage8/69.webp"
    scene luna_stage8_69
    luna "Mind if I try it?"
    pc "Sure."
    image luna_stage8_70 = "/luna/events/stage8/70.webp"
    scene luna_stage8_70
    "Luna takes the bottle of milk and drinks some of it."
    image luna_stage8_71 = "/luna/events/stage8/71.webp"
    scene luna_stage8_71
    luna "Wow, Natalie, you’re delicious!"
    pc "Well, we already know Natalie is delicious, but what about her milk?"
    image luna_stage8_72 = "/luna/events/stage8/72.webp"
    scene luna_stage8_72
    "Natalie blushes at the compliment."
    luna "It’s seriously the best milk I’ve ever had! So rich and creamy!"
    natalie "You really like it?"
    luna "I love it! I’m definitely going to have to ask you for more…I think the only thing that would make it even better is if we could somehow make ice cream out of it."
    pc "Well, Bunny Bites has an ice cream machine. I'm sure they wouldn't mind us using it and trying it out."
    image luna_stage8_73 = "/luna/events/stage8/73.webp"
    scene luna_stage8_73
    luna "Ooh, that sounds delicious! I guess we know where we are going for our date."
    pc "Sounds good to me!"
    image luna_stage8_74 = "/luna/events/stage8/74.webp"
    scene luna_stage8_74
    play music "/music/bunny_bites.ogg" if_changed
    "You and Luna head to Bunny Bites."
    "Here you take the opportunity as an employee - even though you aren't on shift - to go behind the counter and work the ice cream machine, which fortunately isn't currently in use."
    "After making the ice cream with Natalie’s milk, making a nice, big container of ice cream, you bring it to Luna."
    image luna_stage8_75 = "/luna/events/stage8/75.webp"
    scene luna_stage8_75
    luna "Wow, that looks amazing! I hope it tastes as good as it looks."
    "She tries the first bite and her eyes go wide!"
    image luna_stage8_76 = "/luna/events/stage8/76.webp"
    scene luna_stage8_76
    luna "Wow, that’s absolutely delicious! One of the best things I’ve ever had and that’s saying something!"
    pc "I guess we know what Natalie can do with her milk then."
    luna "I’ll take all of it!"
    image luna_stage8_77 = "/luna/events/stage8/77.webp"
    scene luna_stage8_77
    "She continues to try and eat all of it when a woman notices what Luna is eating."
    woman "I didn't know Bunny Bites had ice cream like that! It looks great! I'll have to go get some."
    pc "Oh no, this is just something I personally made. Bunny Bites doesn't really have this kind of ice cream, unfortunately."
    image luna_stage8_78 = "/luna/events/stage8/78.webp"
    scene luna_stage8_78
    woman "Oh, that's a real shame. I would have loved to try it."
    "The woman walks away, leaving Luna to finish her ice cream."
    image luna_stage8_79 = "/luna/events/stage8/79.webp"
    scene luna_stage8_79
    pc "I guess it actually is a shame that Natalie isn't producing more, so we could offer it at Bunny Bites."
    pc "I’m sure even when they find out it’s breast milk ice cream people would love it."
    "Luna is just now finishing the last of the ice cream."
    luna "True. Maybe it could be sold as an extra special, limited quantity product. Anyway, that was good, but I'm definitely still hungry."
    pc "You're always hungry. Well, let's order some food then."
    "You and Luna then order some food, with Luna of course ordering a lot."
    image luna_stage8_80 = "/luna/events/stage8/80.webp"
    scene luna_stage8_80
    "When the food arrives, you can’t help but tease Luna a little."
    pc "So how does it feel now that you have even more competition? What with Natalie now of course?"
    image luna_stage8_81 = "/luna/events/stage8/81.webp"
    scene luna_stage8_81
    luna "I can still out-eat and outgrow her easily."
    pc "I don’t know, Natalie seems pretty determined to eat and grow and gain for me."
    luna "As much as I think Natalie already likes you, she’d probably happily let herself get to be the size of a house if you wanted her to."
    pc "I only want her to get as big as she herself wants to."
    image luna_stage8_82 = "/luna/events/stage8/82.webp"
    scene luna_stage8_82
    luna "What about me then?"
    pc "Now you I plan to grow and fatten up as much as possible because I know that’s what you want, so eat up!"
    image luna_stage8_83 = "/luna/events/stage8/83.webp"
    scene luna_stage8_83
    luna "Oh, I love it when a man talks dirty to me in public."
    "Luna then gives you a wink followed by her normal mischievous smile."
    "After enough flirting and playful teasing, Luna turned her attention back to the food laid before her."
    "You think to yourself: Is there any better way to end a first date than watching your large-breasted girlfriend make quick work of a table full of food? Surely not."
    scene outside
    stop music fadeout 1.0
    "After Luna finishes eating, you drop her off at home and then go back home yourself."
    scene player_room
    if recollection == False:
        $ luna.weight += 1
        $ daytime += 1
        $ phonecall = 1
    "With some free time, you decide now is a good time to check on some of the other test subjects as you send out some texts to see how they are doing."
    "Roxie is the first to get back to you."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Roxie', dialogue=dialogue_one)
    $ msg ("I’m doing great!", who=1)
    pause
    $ msg ("Natalie has been telling me all about you asking her out.", who=1)
    pause
    $ msg ("She’s so excited!", who=1)
    pause
    $ msg ("I’m excited too.")
    pause
    $ msg ("Natalie is such a nice girl and I got to admit she’s starting to look good with some extra fat on her.", who=1)
    pause
    $ msg ("I agree.")
    pause
    $ msg ("So…", who=1)
    pause
    $ msg ("How stuffed full was Luna looking by the end of your date with her?", who=1)
    pause
    $ msg ("Here I think I took a picture.")
    pause
    $ msg (None, pic="stage8_luna")
    pause
    $ msg ("Wow, that’s hot!", who=1)
    pause
    $ msg ("I don’t know if there is any better sight than a beautiful woman with a full tummy.")
    pause
    $ msg ("Mmm, you might be right about that.", who=1)
    pause
    $ msg ("Speaking of which, I'm going to go stuff my tummy full of food.", who=1)
    pause
    $ msg ("Don’t worry, I’ll send you a picture after.", who=1)
    pause
    $ hide_messenger()

    "While you wait for Roxie to get back to you, you get a picture sent from Sally."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Sally', dialogue=dialogue_one)
    $ msg (None, pic="stage2_sally")
    pause
    $ msg ("Just so you don’t forget what it looks like.", who=1)
    pause
    $ msg ("How could I forget?")
    pause
    $ msg ("It’s for whenever you want something nice to look at.", who=1)
    pause
    $ msg ("Does it turn you on knowing it’s probably going to be so much bigger the next time you see it?", who=1)
    pause
    $ msg ("Yeah.")
    pause
    $ msg ("So…now that I’ve sent you a picture and turned you on, aren’t you going to send me a dick pic?", who=1)
    pause
    $ msg ("Ah, so this was your plan.")
    pause
    $ msg ("Maybe.", who=1)
    pause
    $ hide_messenger()

    "At that moment however Charlene sends you a picture."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Charlene', dialogue=dialogue_one)
    $ msg (None, pic="stage2_charlene")
    pause
    $ msg ("You did this to me!", who=1)
    pause
    $ msg ("How did I do that?")
    pause
    $ msg ("I don’t know.", who=1)
    pause
    $ msg ("Somehow.", who=1)
    pause
    $ msg ("Just thinking about you makes me want to eat.", who=1)
    pause
    $ msg ("Looks like you keep thinking about me a lot then.")
    pause
    $ msg ("OH…never mind.", who=1)
    pause
    $ hide_messenger()

    "You then get another text from Sally."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Sally', dialogue=dialogue_one)
    $ msg ("I’m waiting.", who=1)
    pause
    $ msg (None, pic="stage2_charlene")
    pause
    $ msg ("Hey, that’s not the kind of dick pic I was hoping for.", who=1)
    pause
    $ msg ("Nice to see Charlene embracing her secret gluttonous side though.", who=1)
    pause
    $ msg ("Hopefully it will make her softer in more ways than one.", who=1)
    pause
    $ msg ("Anyway apparently as I’m being reminded my break is now over so I guess I’ll have to get that picture from you later.", who=1)
    pause
    $ msg ("Maybe.")
    pause
    $ hide_messenger()

    "A few minutes later and Roxie sends you a picture."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Roxie', dialogue=dialogue_one)
    $ msg (None, pic="stage2_roxie")
    pause
    $ msg ("You were right, this is hot.", who=1)
    pause
    $ msg ("Told you.")
    pause
    $ msg ("It is really hard to text one handed.", who=1)
    pause
    $ msg ("And I want the other hand to grab more food.", who=1)
    pause
    $ msg ("So talk to you later.", who=1)
    pause
    $ msg ("Talk to you later.")
    pause
    $ hide_messenger()

    "Evidently all the test subjects are doing quite well."

    $ lunastage8event = 0
    return

label Luna_Stage_9_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Luna', dialogue=dialogue_one)
    $ msg ("Today is the day! Time for another measurement taking and weigh-in for the test subjects!", who=1)
    pause
    menu:
        "Go to the hospital.":
            $ msg ("Alright! I’ll be right there.")
            pause
            $ hide_messenger()

        "Delay the measurements to a later date.":
            $ msg ("Sorry, I’m a little busy today, could we do this another time?")
            pause
            $ msg ("That's alright, lets do this another time.", who=1)
            pause
            $ hide_messenger()
            return
    if recollection == False:
        $ britta.stage = 3
        $ sally.stage = 3
        $ natalie.stage = 3
        $ charlene.stage = 3
        $ roxie.stage = 3

    image luna_stage9_1 = "/luna/events/stage9/1.webp"
    scene luna_stage9_1
    "Upon getting to the hospital, you find Natalie there waiting for you. Even from a distance it’s obvious that she’s grown again."
    pc "Hi, Natalie! You’re looking great!"
    image luna_stage9_2 = "/luna/events/stage9/2.webp"
    scene luna_stage9_2
    "Natalie blushes at the compliment."
    natalie "Thanks! I’ve been really trying to eat and grow plenty for our date! I’m really looking forward to it!"
    pc "Me too!"
    image luna_stage9_3 = "/luna/events/stage9/3.webp"
    scene luna_stage9_3
    natalie "I've grown a lot, but I guess I'm not really that special - just wait until you see the other girls."
    pc "I'm looking forward to seeing the other girls too, but I would say you’ve always been special and beautiful."
    image luna_stage9_4 = "/luna/events/stage9/4.webp"
    scene luna_stage9_4
    "Natalie blushed again at the compliment."
    natalie "I'm sorry. It's just still hard to believe that you like me so much. I just really, really like you and I worry."
    pc "You are totally fine, just relax and be yourself and I’ll like you a lot just fine."
    natalie "Okay. I'll try."
    pc "Well, I guess we should both get going to the testing lab. Do we need to wait for a replacement for you?"
    image luna_stage9_5 = "/luna/events/stage9/5.webp"
    scene luna_stage9_5
    natalie "I asked one of the other nurses that isn't a test subject to cover for me. She's right over there, so I can just leave now and she should be coming right over."
    pc "Okay. Great."
    image luna_stage9_6 = "/luna/events/stage9/6.webp"
    scene luna_stage9_6
    natalie "Mmm, I can’t wait to have you measure and inspect my body."
    pc "Yeah, I’m definitely looking forward to that and our date afterwards."
    image luna_stage9_7 = "/luna/events/stage9/7.webp"
    scene luna_stage9_7
    "You and Natalie head over to the testing lab to find everyone else waiting for you."
    image luna_stage9_8 = "/luna/events/stage9/8.webp"
    scene luna_stage9_8
    "Like Natalie it’s obvious all of the others have grown once again and that includes Luna, who still clearly has the biggest breasts out of all of them."
    "That being said, with the others growing so much Luna is looking less and less out of place as a very busty woman."
    image luna_stage9_9 = "/luna/events/stage9/9.webp"
    scene luna_stage9_9
    luna "Hi, [playername] and Natalie! You’re finally here which means we can get started!"
    "Luna sure seems to be in an excited and eager mood."
    image luna_stage9_10 = "/luna/events/stage9/10.webp"
    scene luna_stage9_10
    "Luna then addresses all of the test subjects."
    luna "Well, once again, ladies, you seem to have done a great job eating and growing. The test study is really going to be helped out by your efforts."
    image luna_stage9_11 = "/luna/events/stage9/11.webp"
    scene luna_stage9_11
    "Most of the girls smiled happily at the compliment."
    luna "I know I’ve been rather busy lately, but this time I’m really happy that I will be here so we can check the progress you’ve all made."
    luna "We’ll start by getting your current measurements and weights, and we also want to check your overall health and see what difference has been made."
    luna "Britta will be checking your vitals while me and [playername] will be getting your measurements and weights afterwards."
    image luna_stage9_12 = "/luna/events/stage9/12.webp"
    scene luna_stage9_12
    britta "Who is first with me then?"
    image luna_stage9_13 = "/luna/events/stage9/13.webp"
    scene luna_stage9_13
    roxie "I’ll go first."
    "Roxie immediately volunteered to go first and seemed pretty eager."
    "She wasn’t looking at Britta, she was looking at Luna, and it didn’t take a medical degree to guess why."
    "She was likely eager to strip naked and be inspected by her major crush Luna."
    image luna_stage9_14 = "/luna/events/stage9/14.webp"
    scene luna_stage9_14
    "You also couldn’t help notice Luna has an amused and knowing smile of her own."
    luna "Very well. I've already had my vitals taken earlier, but I think I'd better get my own measurements and weight taken first while the rest of you are busy or waiting."
    image luna_stage9_15 = "/luna/events/stage9/15.webp"
    scene luna_stage9_15
    "You follow Luna over to the room next door and you notice the big smile still on her face."
    pc "Why are you so happy? Are you just excited about stripping naked and showing off your sexy body to me? To be fair I know I’m excited."
    image luna_stage9_16 = "/luna/events/stage9/16.webp"
    scene luna_stage9_16
    luna "Mmm, well, I'm a little excited for that, but honestly, I have a lot to be excited for today - as do you."
    pc "Well, we do both get to see and inspect some naked, sexy and busty women and see how much they've grown. Also, there is my date with Natalie afterwards."
    luna "I don't think you fully realise the reason for my excitement. I missed this last time and I intend to try to make up for it this time. I really think this time is going to be special."
    luna "I'm a little worried though that I’m not going to be able to stop myself from going too far so you might have to intervene."
    pc "Well, you know I'm here for you, but what are you talking about? What do you think is going to happen?"
    image luna_stage9_17 = "/luna/events/stage9/17.webp"
    scene luna_stage9_17
    luna "You'll find out. I won't spoil the surprise."
    pc "As much as I love your surprises, it always makes me wonder just what you are hinting at."
    image luna_stage9_18 = "/luna/events/stage9/18.webp"
    scene luna_stage9_18
    "Luna just smiles again in amusement and then starts stripping off her clothes."
    image luna_stage9_19 = "/luna/events/stage9/19.webp"
    scene luna_stage9_19
    "Once she is totally naked, you can’t help but once again notice just how big your girlfriend is getting."
    image luna_stage9_20 = "/luna/events/stage9/20.webp"
    scene luna_stage9_20
    "Not just her huge boobs which continue to dominate more and more of her frame, but the rest of her has clearly grown as well."
    luna "You like?"
    pc "I love it!"
    image luna_stage9_21 = "/luna/events/stage9/21.webp"
    scene luna_stage9_21
    luna "Mmm, are you saying you love me already?"
    pc "Um, sorry. I meant to say I love your body and the changes to it. I mean, saying I love you would be too soon, wouldn't it?"
    image luna_stage9_22 = "/luna/events/stage9/22.webp"
    scene luna_stage9_22
    luna "It's fine. I was just teasing you."
    "Even so, you can't help but feel like Luna is just little disappointed, but she hides it well."
    luna "Well, let's get started then."
    image luna_stage9_23 = "/luna/events/stage9/23.webp"
    scene luna_stage9_23
    "You wrap the measuring tape around different parts of her body and let her know the measurements that you get, starting with her hips."
    if persistent.imperial:
        pc "Your hips are now 46 and a half inches around."
    else:
        pc "Your hips are now 118 centimeters around."
    image luna_stage9_24 = "/luna/events/stage9/24.webp"
    scene luna_stage9_24
    "You can't help but give each cheek of her big butt a nice squeeze. While her breasts usually got most of the attention, Luna really is developing such a nice, big and round ass."
    image luna_stage9_25 = "/luna/events/stage9/25.webp"
    scene luna_stage9_25
    "You then get her waist."
    if persistent.imperial:
        pc "Your waist is now over 35 and a half inches around."
    else:
        pc "Your waist is now over 90 centimeters around."
    "Luna does not seem satisfied with that one, however."
    image luna_stage9_26 = "/luna/events/stage9/26.webp"
    scene luna_stage9_26
    luna "Still much too small, I need more stomach capacity so I can eat more."
    pc "We'll work on it. Don't worry, we'll get you a nice, big and proper pudgy tummy."
    luna "Daisy’s big belly is looking so good now. It makes me wish I had one like that."
    pc "Yes, but need I remind you that the reason you don’t is because so much of the weight keeps going to your boobs, which is where you really want it to go the most, remember?"
    luna "Oh, yeah. Good point. That is indeed what I want. Well, let's see how big these babies have gotten then."
    image luna_stage9_27 = "/luna/events/stage9/27.webp"
    scene luna_stage9_27
    "You measure first her underbust and then around the fullest part of her bust."
    if persistent.imperial:
        pc "Your bust is now nearly 50 and a half inches around and you should now need a 40K bra."
    else:
        pc "Your bust is now nearly 128 centimeters around and you should now need a 40K bra."
    image luna_stage9_28 = "/luna/events/stage9/28.webp"
    scene luna_stage9_28
    luna "Mmm, now we're talking! A 40K bra! The only problem is bras that size just about cost 40K. Well, that's an exaggeration, but they are expensive."
    pc "Where do you even get your bras anyway?"
    image luna_stage9_29 = "/luna/events/stage9/29.webp"
    scene luna_stage9_29
    luna "Lately online, as you can’t exactly find my size in regular stores, but even online seems to be getting hard to do. There just aren’t enough places out there for really busty women."
    pc "Well, maybe if you can get enough women to take the drug, there will be a big enough market for it and there will be a lot more places with much larger sizes."
    image luna_stage9_30 = "/luna/events/stage9/30.webp"
    scene luna_stage9_30
    luna "Ooh, that would be a dream come true! Just think of all those happy, healthy, super busty women walking around!"
    luna "I mean, I already feel like I'm living the dream just a little bit with how big the test subjects are starting to get and getting to work with them every day."
    pc "They certainly are all becoming sights to see."
    luna "Well, let's try to hurry and get my weight before the others start to get done with Britta."
    image luna_stage9_31 = "/luna/events/stage9/31.webp"
    scene luna_stage9_31
    "You have Luna step onto the scale and get her weight."
    if persistent.imperial:
        pc "You’re now 209 lbs."
    else:
        pc "You’re now 95 kg."
    luna "I’m finally starting to get to be a big, fat girl."
    pc "Only starting though of course."
    image luna_stage9_32 = "/luna/events/stage9/32.webp"
    scene luna_stage9_32
    luna "Of course. Besides, I don't think I even really count as fat when so much of the weight is in my boobs. I'm not complaining, mind you. But I want to be mega, super busty and fat."
    pc "I want that very much too."
    image luna_stage9_33 = "/luna/events/stage9/33.webp"
    scene luna_stage9_33
    "Luna stops for a moment, still totally naked and seeming to be waiting for something."
    luna "She should be here any second."
    image luna_stage9_34 = "/luna/events/stage9/34.webp"
    scene luna_stage9_34
    "From the look on Luna's face - which seems to be the same look when she is going to do something naughty - she is clearly up to something."
    "A moment later there is a knock on the door."
    luna "Come in!"
    image luna_stage9_35 = "/luna/events/stage9/35.webp"
    scene luna_stage9_35
    "Roxie opens the door, her gorgeous green eyes going wide when she sees Luna standing there totally naked in front of her."
    "However, Luna makes no move to try and cover herself and instead just lets Roxie stare at her, who seems unable to tear her attention away from her."
    "Finally Roxie comes to her senses."
    image luna_stage9_36 = "/luna/events/stage9/36.webp"
    scene luna_stage9_36
    roxie "Uh, sorry. I just thought I heard for me to come in and I-"
    luna "Oh, I meant don't come in, but that's okay. We're both women and fellow test subjects, so being naked in front of each other shouldn't be a big deal, right?"
    roxie "Uh, no, I suppose not."
    "Roxie still can’t help but just stare at Luna and Luna seems to be struggling to hide just how amused she is by the situation she clearly intended to happen."
    luna "He was just about to inspect my breasts more closely, but perhaps it would be best if you did it this time if you wouldn’t mind?"
    image luna_stage9_37 = "/luna/events/stage9/37.webp"
    scene luna_stage9_37
    luna "I mean, you're also a woman and it might be good to get another woman's perspective."
    roxie "Oh, um, I don't mind... don't mind at all."
    image luna_stage9_38 = "/luna/events/stage9/38.webp"
    scene luna_stage9_38
    "By this point Roxie is blushing just about as red as Natalie’s hair and hardly able to believe her luck."
    image luna_stage9_39 = "/luna/events/stage9/39.webp"
    scene luna_stage9_39
    luna "Great. Thank you so much. I, of course, would be happy to do the same for you afterwards. I mean, I am your boss, but this would purely be for scientific and research purposes."
    roxie "Of…of course."
    luna "How about you strip naked so we can inspect each other at the same time?"
    roxie "Yeah, um... good idea."
    "Luna is clearly enjoying this. All of you are, really. Although - despite Luna's claims - this isn't purely for scientific or research purposes."
    image luna_stage9_40 = "/luna/events/stage9/40.webp"
    scene luna_stage9_40
    "Roxie takes off her clothes, leaving both women totally naked and admiring each other."
    luna "So should we begin?"
    roxie "Yes! I mean yes, of course."
    image luna_stage9_41 = "/luna/events/stage9/41.webp"
    scene luna_stage9_41
    "Both of them come closer and face each other as they grab each other's now huge boobs. Luna's are quite a bit bigger still, but Roxie now also has a nice, huge pair of her own."
    "Neither of them seem to be able to resist spending a couple minutes feeling each other's boobs up before finally realizing they should probably say something."
    roxie "Well, your boobs seem nice and big and healthy."
    luna "Thank you, yours too. You've clearly been doing a great job doing your part as a test subject."
    image luna_stage9_42 = "/luna/events/stage9/42.webp"
    scene luna_stage9_42
    roxie "Thank you. That mean a lot coming from you and I'm glad that you appreciate them... uh, I mean, me."
    luna "Of course I appreciate you and you’ve really grown a lot…as a valuable employee and I really like the changes that you’ve made to improve yourself."
    roxie "Thanks. I've really been trying to grow as a person."
    "It seems even Roxie is now getting into her and Luna’s little game."
    luna "Well, keep up the good work. Let's find out just how much your person has grown. Are you ready to be measured and weighed now?"
    pc "Maybe you should do it this time, Luna."
    image luna_stage9_43 = "/luna/events/stage9/43.webp"
    scene luna_stage9_43
    "You are just enjoying watching what is going on with the two women enough that you decide to let it continue."
    luna "Well, okay. Is that okay with you, Roxie?"
    image luna_stage9_44 = "/luna/events/stage9/44.webp"
    scene luna_stage9_44
    roxie "For sure. No objections from me."
    "You get Luna the measuring tape and then Luna measures Roxie."
    image luna_stage9_45 = "/luna/events/stage9/45.webp"
    scene luna_stage9_45
    "Making it a point to not so subtly touch each part of her body that she is supposed to be measuring, Luna instead very obviously feels around Roxie's breasts, butt and hips -"
    "much like you 'accidentally' do when you are measuring the test subjects."
    "Roxie doesn't seem to mind at all, however, and seems to be very much enjoying the attention."
    if persistent.imperial:
        luna "You now have 41 inch hips, a more than 24 inch waist, and a nearly 42 inch bust and you now need a 34H bra."
    else:
        luna "You now have 104 cm hips, a more than 61 cm waist, and a nearly 106.5 cm bust and you now need a 34H bra."
    image luna_stage9_46 = "/luna/events/stage9/46.webp"
    scene luna_stage9_46
    "Luna then has Roxie get on the scale."
    if persistent.imperial:
        luna "You are now at 165 lbs which means you’ve gained an additional 15.5 pounds since your last measurement and weigh in."
    else:
        luna "You are now at 75 kg which means you’ve gained an additional 7 kg since your last measurement and weigh in."
    image luna_stage9_47 = "/luna/events/stage9/47.webp"
    scene luna_stage9_47
    roxie "Mmm, is it acceptable for you…for the project?"
    luna "You’re making very good progress and the results are quite nice."
    image luna_stage9_48 = "/luna/events/stage9/48.webp"
    scene luna_stage9_48
    "Luna couldn’t resist giving Roxie’s boobs another squeeze."
    roxie "Thank you. I've been doing my best to grow and I'm not nearly done yet."
    image luna_stage9_49 = "/luna/events/stage9/49.webp"
    scene luna_stage9_49
    luna "Oh, I'm counting on it and I'm looking forward to see you make much more progress."
    roxie "I'll once again do my best…for you…and for the good of the drug test."
    luna "Very good. I shall look forward to seeing such progress next time. Do well enough and I just might have a bonus for you."
    roxie "Well, I definitely want to earn that bonus."
    "You aren't sure just what that bonus is supposed to be, but you are confident Roxie is going to do her best to try and find out."
    "Roxie gets dressed and then leaves. Luna gets dressed as well."
    image luna_stage9_50 = "/luna/events/stage9/50.webp"
    scene luna_stage9_50
    pc "Was that what made you so excited? To get to do that with Roxie?"
    "Luna just smiled at you again."
    luna "Oh, no no no. That's just the beginning of the surprises and fun. I'm assuming you enjoyed watching that?"
    pc "For sure. It was really hot."
    image luna_stage9_51 = "/luna/events/stage9/51.webp"
    scene luna_stage9_51
    luna "Good to see you also enjoy me being with other women."
    luna "Really, with just how much I know Roxie wants me and how much she's been growing and getting oh-so sexy, I just couldn't help myself from having some fun."
    pc "I don’t blame you."
    luna "Well, now it is your turn to have fun while I get to to watch."
    image luna_stage9_52 = "/luna/events/stage9/52.webp"
    scene luna_stage9_52
    "The next test subject that came in turned out to be Sally, who was currently eating something."
    luna "Trying to get in an extra few ounces for the weigh in I see? Every little bit counts."
    image luna_stage9_53 = "/luna/events/stage9/53.webp"
    scene luna_stage9_53
    sally "Sorry to disappoint, but I just like eating and being a fat-ass."
    pc "That works too."
    image luna_stage9_54 = "/luna/events/stage9/54.webp"
    scene luna_stage9_54
    "Sally quickly finishes what she’s eating and then strips naked, happily allowing you and Luna to look her body over."
    luna "You seem to have been eating well. Good job."
    sally "Once again, I just like eating. But I'm glad that you are happy with my progress."
    pc "How about we get your weight first?"
    image luna_stage9_55 = "/luna/events/stage9/55.webp"
    scene luna_stage9_55
    "Sally gets onto the scale."
    if persistent.imperial:
        pc "You are now at 209 lbs, which means you’ve gained an additional 15.5 pounds since last weigh in."
    else:
        pc "You are now at 95 kg, which means you’ve gained an additional 7 kg since last weigh in."
    image luna_stage9_56 = "/luna/events/stage9/56.webp"
    scene luna_stage9_56
    "You then get her measurements."
    image luna_stage9_57 = "/luna/events/stage9/57.webp"
    scene luna_stage9_57
    if persistent.imperial:
        pc "You now have a 43 inch bust measurement and need a 36G bra, your waist is at 31 inches, and your hips are now at almost 50 inches."
    else:
        pc "You now have a 109 cm bust measurement and need a 36G bra, your waist is at 79 cm, and your hips are now at almost 127 cm."
    image luna_stage9_58 = "/luna/events/stage9/58.webp"
    scene luna_stage9_58
    "Sally looks disappointed with that."
    if persistent.imperial:
        sally "Only almost 50, huh? I was really hoping to actually hit 50 for this measurement/weigh in check."
        pc "You’re so close you’ll probably hit that easily in the next day or so."
    else:
        sally "Only almost 127, huh? I was really hoping to hit 130 for this measurement/weigh in check."
        pc "You’re so close you’ll probably hit that easily in a week or two."
    image luna_stage9_59 = "/luna/events/stage9/59.webp"
    scene luna_stage9_59
    sally "True. I guess I have something extra to work on then."
    if persistent.imperial:
        sally "I want to be able to advertise that I have a 50 inch around ass."
    else:
        sally "I want to be able to advertise that I have a 130 centimeters around ass."
    sally "I can’t help but imagine that people wonder just how big it is even if they aren’t brave enough to actually ask and I’ll be happy to tell them."
    image luna_stage9_60 = "/luna/events/stage9/60.webp"
    scene luna_stage9_60
    luna "I totally get that. I like to imagine people wondering just how big my boobs are."
    luna "In your case though you seem to be predisposed to be much more bottom heavy, even with the drug."
    luna "I also find it interesting that you are much more interested in your butt and hips growing, since most of the other test subjects are much more interested in their boobs growing."
    image luna_stage9_61 = "/luna/events/stage9/61.webp"
    scene luna_stage9_61
    sally "I don't know. I guess I just like being different."
    sally "And while I like the attention I get from my boobs, I like the attention my ass gets even more, because I can just imagine how much everyone stares at it as I walk past."
    sally "And I fantasize about them thinking about how much they want to pound against it as they take me from behind. Speaking of which..."
    image luna_stage9_62 = "/luna/events/stage9/62.webp"
    scene luna_stage9_62
    "Sally looks over at you and gives you a wink."
    sally "Care to take my nearly 50 inch ass out for some fun?"
    "You of course are going to say yes, but, surprisingly, Luna stops you."
    image luna_stage9_63 = "/luna/events/stage9/63.webp"
    scene luna_stage9_63
    luna "Actually, he hurt his penis doing me earlier, so he can't. Sorry."
    sally "Well, that's certainly a disappointment. I kept thinking about that penis inside me all day."
    luna "I’ve got some nice equally sized toys about as big as him. You can try them out if you are just looking for some relief and pleasure?"
    sally "Ooh, yes, please!"
    luna "I’ll show you afterwards."
    image luna_stage9_64 = "/luna/events/stage9/64.webp"
    scene luna_stage9_64
    "Sally then left, leaving you and Luna alone again for a minute."
    pc "Do you mind if I ask why you essentially cock-blocked me from having sex with Sally?"
    pc "Knowing you, I figure you would want me to have sex with her while you watch."
    image luna_stage9_65 = "/luna/events/stage9/65.webp"
    scene luna_stage9_65
    luna "Normally I would very much encourage it and want to watch, but first of all, I have to point out that Sally doesn’t really want you so much as she just wants your cock inside her."
    pc "I suppose that’s true, but I still would have been okay with that arrangement."
    luna "That being said I’d still normally probably happily encourage sex."
    luna "Sex just for mutual pleasure and enjoyment with no strings attached and no worries about relationships can still be fun as long as that’s all both parties want."
    luna "That's what Sally thinks she wants, but I think deep down she wants something more than just eating and having sex."
    pc "Are you trying to set me up with Sally now?"
    luna "Not yet, but we’ll see."
    image luna_stage9_66 = "/luna/events/stage9/66.webp"
    scene luna_stage9_66
    luna "Anyway, the other reason that I didn't want you to have sex with Sally is because-"
    luna "I already plan on you having sex with someone else in just a bit and I want to make sure you are fully ready to go for that."
    pc "Are you talking about my date with Natalie, because I don’t think she’s going to be ready for that yet. Or are you talking about yourself?"
    image luna_stage9_67 = "/luna/events/stage9/67.webp"
    scene luna_stage9_67
    "Luna just smiles in amusement at your questions and provides no answers. She once again wants to keep her secrets."
    "Charlene then comes in."
    image luna_stage9_68 = "/luna/events/stage9/68.webp"
    scene luna_stage9_68
    charlene "I’m only doing this if he isn’t here."
    pc "I’ll leave the room."
    image luna_stage9_69 = "/luna/events/stage9/69.webp"
    scene luna_stage9_69
    luna "I still don’t see what the big deal is, but okay, I’ll get your measurements and then I’ll have him come back in to help discuss the results."
    charlene "I guess I can live with that."
    image luna_stage9_70 = "/luna/events/stage9/70.webp"
    scene luna_stage9_70
    "You leave the room for a while and then wait until Luna calls you back in, with Charlene fully dressed again."
    image luna_stage9_71 = "/luna/events/stage9/71.webp"
    scene luna_stage9_71
    if persistent.imperial:
        luna "So, Charlene, you now have a more than 42 inch bust and now need a 36F bra, you have a slightly bigger than 36 inch waist, and more than 47 inch hips."
        luna "What I think is most outstanding, however, is how much weight you've gained. You've gained 26.5 lbs since your last official weigh in and are now at 216 lbs."
    else:
        luna "So, Charlene, you now have a more than 116.5 cm bust and now need a 36F bra, you have a slightly bigger than 91.5 cm waist, and more than 119 cm hips."
        luna "What I think is most outstanding, however, is how much weight you've gained. You've gained 12 kg since your last official weigh in and are now at 98 kg."
    luna "We haven't finished weighing everyone yet, but I think it's safe to say that is the most out of everyone."
    image luna_stage9_72 = "/luna/events/stage9/72.webp"
    scene luna_stage9_72
    "Charlene does not look at all happy though."
    charlene "I thought the drug and all this eating was supposed to give me bigger boobs, but it's mostly just making me fat. I mean, just look at this tummy I'm getting."
    image luna_stage9_73 = "/luna/events/stage9/73.webp"
    scene luna_stage9_73
    "Charlene shows off her definitely no longer flat belly."
    luna "I think it looks great on you."
    pc "If it helps any I think you’re looking good too."
    image luna_stage9_74 = "/luna/events/stage9/74.webp"
    scene luna_stage9_74
    charlene "Oh, shut up! I didn't ask you."
    charlene "Besides, it's partly your fault that I'm getting fat and can't seem to stop eating; what, with your encouragement and feeding me so well when I come into Bunny Bites."
    luna "I would say that he’s just doing his job and he’s doing well at it."
    image luna_stage9_75 = "/luna/events/stage9/75.webp"
    scene luna_stage9_75
    charlene "Alright, fine. I guess that is the goal, but still... I'll be glad when this is over and I can try to trim back down and get rid of all this extra weight."
    luna "Well, I suppose if you want to do that, that's up to you, but I'm hoping that you can find the benefits of being a larger woman."
    charlene "I don't think I will."
    charlene "I only did this for you, Luna, and for the success of the project and because I got those terrible prospects of getting that awful disease that killed my mother and grandmother."
    luna "Fair enough, but I’m still hoping to convince you otherwise."
    "Charlene just nods and then leaves."
    image luna_stage9_76 = "/luna/events/stage9/76.webp"
    scene luna_stage9_76
    pc "You know not every woman is going to enjoy gaining weight. In fact, most women wouldn't no matter how hard you try."
    pc "I’ve honestly been super lucky being around all of the women I have that do enjoy it."
    luna "True, unfortunately. But I'm still hoping to change that perception. Why does being fat have to be looked down upon so much?"
    pc "If it helps though we are still having a lot of success."
    pc "I’m seeing a lot of women gaining quite a bit of weight lately."
    pc "They seem to mostly be happy about it so maybe that could lead to other women deciding to gain weight kind of like a snowball effect."
    image luna_stage9_77 = "/luna/events/stage9/77.webp"
    scene luna_stage9_77
    luna "I can only hope so - especially with you around. I would say that if anyone can convince Charlene otherwise it would be you."
    pc "That’s assuming she will even let me talk to her or stop being disgusted by me for being a man."
    luna "I think she's gradually liking you more and more. I know it may not seem like it and it may take a while for her to come around, but I still have hope for her."
    pc "You have hope for everybody though. That's one of the things that I like about you."
    luna "Thanks! You’re sweet."
    image luna_stage9_78 = "/luna/events/stage9/78.webp"
    scene luna_stage9_78
    "She goes and gives you a kiss just for that."
    image luna_stage9_79 = "/luna/events/stage9/79.webp"
    scene luna_stage9_79
    "Soon after Natalie finally comes in, looking worried."
    natalie "Sorry it took me so long! I had to go pump more milk."
    pc "You’re totally fine, you’re more than worth the wait."
    image luna_stage9_80 = "/luna/events/stage9/80.webp"
    scene luna_stage9_80
    "Natalie blushes at the compliment."
    natalie "Thanks."
    luna "I think I’ll just watch for this one."
    image luna_stage9_81 = "/luna/events/stage9/81.webp"
    scene luna_stage9_81
    "Natalie takes off all of her clothes and lets you look over her incredible naked body."
    pc "You've got such a beautiful body, Natalie. I mean, you were already really pretty before. But now? You just keep looking better and better."
    image luna_stage9_82 = "/luna/events/stage9/82.webp"
    scene luna_stage9_82
    "Natalie blushes again."
    natalie "Thanks. I really love how much you like it. The thought of you liking me more and more with every bite I take really makes me happy."
    pc "I don’t know if it’s possible for me to like you anymore to be honest and while I appreciate it, you don’t need to do this just for me."
    image luna_stage9_83 = "/luna/events/stage9/83.webp"
    scene luna_stage9_83
    natalie "I'm not doing it just for you, don't worry! I mean, it does play a large role, but... I really like eating and growing and gaining."
    pc "Okay, just making sure."
    natalie "Do you want to feel my body up? It just feels so good when you touch and enjoy my body."
    pc "Of course."
    image luna_stage9_84 = "/luna/events/stage9/84.webp"
    scene luna_stage9_84
    "You feel up Natalie’s body, going all over it, but paying extra attention to her now huge breasts and then her wide and thick butt."
    natalie "Mmm, that feels good."
    pc "Good. I'm glad. Honestly, I feel like I could feel up your body all day, but we probably do need to get your measurements."
    image luna_stage9_85 = "/luna/events/stage9/85.webp"
    scene luna_stage9_85
    luna "I certainly didn't mind. I was just enjoying watching the show and admiring your gorgeous body too... assuming you don't mind me saying so, Natalie?"
    image luna_stage9_86 = "/luna/events/stage9/86.webp"
    scene luna_stage9_86
    natalie "Not at all. After all, you did help give me this body by helping to create the drug. Also, you were the one to help me meet [playername]. I feel like I'm in your debt."
    luna "I was happy to do all that and you don’t owe me anything."
    natalie "I know, but I still want to show my appreciation. You can feel me up too if you want. I promise I won't say anything, so you don't get into trouble."
    luna "Yet another thing to like about you, Natalie. Well, if you are offering, I just can't say no."
    image luna_stage9_87 = "/luna/events/stage9/87.webp"
    scene luna_stage9_87
    "Luna takes the opportunity to feel up Natalie's body, but Natalie doesn't seem to mind at all-"
    "In fact, she seems to be enjoying the attention almost as much as when it was you doing it."
    natalie "It doesn't feel as good as when [playername] does it, but it still feels really good having you touch me, Luna."
    luna "Well, you're welcome then."
    image luna_stage9_88 = "/luna/events/stage9/88.webp"
    scene luna_stage9_88
    natalie "Really, both of you make me feel so good about my body. Now I just want more and more of it, so there is more of it to enjoy - both for me and for you."
    pc "Mmm, looking forward to seeing you grow even more then."
    luna "Me too."
    pc "Well, we really should get those measurements and find out just how much you've grown then."
    natalie "For sure. I'm quite curious what the results will be."
    image luna_stage9_89 = "/luna/events/stage9/89.webp"
    scene luna_stage9_89
    "You take all of Natalie’s measurements, being not at all careful about where you touch her as you are doing so."
    image luna_stage9_90 = "/luna/events/stage9/90.webp"
    scene luna_stage9_90
    if persistent.imperial:
        pc "You now have a 43 inch bust and now need a 34I bra, you have a nearly 26 inch waist, and have 45 inch hips."
    else:
        pc "You now have a 109 cm bust and now need a 34I bra, you have a nearly 66 cm waist, and have 114 cm hips."
    image luna_stage9_91 = "/luna/events/stage9/91.webp"
    scene luna_stage9_91
    natalie "Oh. Well, that sounds all good then. I can't wait for more though."
    pc "Me too."
    luna "Same for me."
    image luna_stage9_92 = "/luna/events/stage9/92.webp"
    scene luna_stage9_92
    "You then have Natalie get on the scale to check her weight."
    if persistent.imperial:
        pc "You now weigh 189.5 lbs, which means you've gained more then 13 lbs."
    else:
        pc "You now weigh 86 kg, which means you've gained an additional 6 kg."
    image luna_stage9_93 = "/luna/events/stage9/93.webp"
    scene luna_stage9_93
    natalie "That seems good then. Hopefully, I can get more than that next time though."
    luna "I love the way you are starting to talk."
    pc "You must be rubbing off on her."
    natalie "Well, I'm definitely looking forward to our date later."
    pc "Me too. Actually, Natalie, did you keep some of your milk from earlier?"
    "You suddenly have an idea."
    image luna_stage9_94 = "/luna/events/stage9/94.webp"
    scene luna_stage9_94
    natalie "Yeah, I've kept all of it. Actually, I have way more than I know what to do with. I've been storing it all here in one of the great big refrigerators we aren't using."
    natalie "I know Britta has been studying some of it, but she definitely doesn't need that much."
    pc "That’s great! Would you mind getting it? I just have an idea for our date."
    natalie "Sure, I'd be happy to! I'm not sure what you are planning to do, but at least we might get some good use out of all that milk. It does seem such a shame to throw it all away."
    image luna_stage9_95 = "/luna/events/stage9/95.webp"
    scene luna_stage9_95
    "Natalie leaves and Britta comes in right after."
    "She seems really nervous about something though."
    image luna_stage9_96 = "/luna/events/stage9/96.webp"
    scene luna_stage9_96
    luna "Don't worry, it's going to be great and I'm sure you'll do great too."
    britta "Thanks. I have been doing plenty of research, but... actually doing it sound much more difficult."
    luna "Yes, actually doing it is quite different, but you will have both of us here to help you."
    pc "Um, what’s going on that I feel I should know about?"
    image luna_stage9_97 = "/luna/events/stage9/97.webp"
    scene luna_stage9_97
    "Britta looks surprised and then angrily at Luna."
    britta "Luna, you mean to tell me that you didn't ask him? You told me you did and he said yes."
    image luna_stage9_98 = "/luna/events/stage9/98.webp"
    scene luna_stage9_98
    luna "Okay, fine. I lied. I just wanted it to be a surprise. Besides, I knew he was going to say yes."
    luna "I mean, just look at you and that body. I couldn't resist having sex with you either if you asked me to."
    britta "Well, you aren't joining in, if that's what you were hoping for. I'm also inclined to not let you watch either."
    luna "Oh, but I was going to be here to show you how."
    britta "You can watch and instruct from a distance then... Of course that's all assuming that he actually agrees."
    pc "You want me to have sex with you, Britta?"
    image luna_stage9_99 = "/luna/events/stage9/99.webp"
    scene luna_stage9_99
    britta "Yes, please... If you are okay with that...? I mean, I know it's not the way that social convention would have it, but-"
    pc "Of course I would love to."
    image luna_stage9_100 = "/luna/events/stage9/100.webp"
    scene luna_stage9_100
    luna "Told you."
    britta "You still should have asked him first."
    luna "Yeah, I know. I'm sorry. I just really thought it would be more fun as a surprise. You know I love my surprises."
    pc "Yes, we know. I would have appreciated knowing beforehand, but mainly because I would want to make sure that I was prepared and ready, so I could make Britta's first time special."
    britta "I really appreciate that. I think I definitely made a great choice for the man to lose my virginity to."
    luna "You definitely did. He's incredible."
    image luna_stage9_101 = "/luna/events/stage9/101.webp"
    scene luna_stage9_101
    britta "I guess I will find that out for myself, huh?"
    pc "Yes, you will. And I get to find out how incredible you are as well."
    britta "Well, I hope that I do an adequate job. After all, I am quite inexperienced, as you know."
    pc "It's totally fine - no judgment here. Just try to relax and enjoy yourself. That will make the experience much better for you."
    britta "I’ll try."
    image luna_stage9_102 = "/luna/events/stage9/102.webp"
    scene luna_stage9_102
    "Both you and Britta strip naked and then allow each other to look the other's body over."
    pc "You look gorgeous."
    image luna_stage9_103 = "/luna/events/stage9/103.webp"
    scene luna_stage9_103
    "Britta blushes at that."
    britta "Thank you. You look really handsome."
    image luna_stage9_104 = "/luna/events/stage9/104.webp"
    scene luna_stage9_104
    "Britta can't help herself from staring at your erect penis though."
    britta "It's amazing. I mean, I've seen them in books or in my, um... research videos. Seeing one in real life is totally different though and this also seems to be quite a large one."
    britta "I can't help but wonder just how on earth that is going to fit inside me. I mean, I know scientifically how it is going to fit, but..."
    image luna_stage9_105 = "/luna/events/stage9/105.webp"
    scene luna_stage9_105
    luna "Don't worry, it will fit. It will just take some time for you to get used to his size."
    luna "Anyway, the most important thing to remember about sex is it's never quite exactly the same for any two people."
    luna "That's why researching it can only get you so far. It is more important to just do it and then find out what feels exactly right for you."
    image luna_stage9_106 = "/luna/events/stage9/106.webp"
    scene luna_stage9_106
    britta "That’s good advice and I have been thinking a lot about what I want."
    pc "Yeah, this time should be all about you, I just want to make it as best as possible for you."
    britta "Well, first of all, I was thinking we could kind of lead into it while you take my measurements, which we still need."
    britta "Maybe you could play up the numbers or something. I have a thing for numbers."
    pc "I never thought of numbers as sexy, but okay, sure, I'll try that."
    image luna_stage9_107 = "/luna/events/stage9/107.webp"
    scene luna_stage9_107
    "You get out the measuring tape and start with her hips."
    if persistent.imperial:
        pc "You have nearly 43 inch hips now."
    else:
        pc "You have nearly 109 cm hips now."
    britta "No, get the exact measurement."
    "You measure her again then."
    if persistent.imperial:
        pc "You have 42.9 inch hips. You have wonderful, thick, oh-so delicious 42.9 inch hips."
    else:
        pc "You have 108.97 cm hips. You have wonderful, thick, oh-so delicious 108.97 cm hips."
    britta "Now we’re talking."
    image luna_stage9_108 = "/luna/events/stage9/108.webp"
    scene luna_stage9_108
    "You run your hands over each cheek of her butt and over each hip."
    if persistent.imperial:
        pc "42.9 inches around, so very close to 43 and yet not quite."
    else:
        pc "108.97 cm around, so very close to 109 and yet not quite."
    image luna_stage9_109 = "/luna/events/stage9/109.webp"
    scene luna_stage9_109
    if persistent.imperial:
        britta "It's going to hit 43 inches by the end of the day if I have anything to say about it. After we have sex I am SO eating like 5,000 calories worth of food."
        pc "Oh, you definitely should do that. How many calories and fats and sugars would you have to eat to make that big ass of yours 50 inches?"
        britta "There are too many variables to figure that out for sure, but now that you bring that up I intend to find out."
        britta "I want to leave the 40's behind when it comes to my ass and hips. The 40's are still too small a number for them."
        pc "The 40’s are a really good place to be when it comes to your ass and hips, but yes, the 50’s would be even better."
    else:
        britta "It's going to hit 109 cm by the end of the day if I have anything to say about it. After we have sex I am SO eating like 5,000 calories worth of food."
        pc "Oh, you definitely should do that. How many calories and fats and sugars would you have to eat to make that big ass of yours 150 cm?"
        britta "There are too many variables to figure that out for sure, but now that you bring that up I intend to find out."
        britta "I want to leave the 100's behind when it comes to my ass and hips. The 100's are still too small a number for them."
        pc "The 100’s are a really good place to be when it comes to your ass and hips, but yes, the 200’s would be even better."
    britta "Mmm, for sure. So what about my belly and waist?"
    image luna_stage9_110 = "/luna/events/stage9/110.webp"
    scene luna_stage9_110
    "You measure around her waist next."
    if persistent.imperial:
        pc "You now have a 27.9 inch waist. That's nearly 28 inches around your still rather slim waist."
    else:
        pc "You now have a 70.86 cm waist. That's nearly 71 cm around your still rather slim waist."
    image luna_stage9_111 = "/luna/events/stage9/111.webp"
    scene luna_stage9_111
    if persistent.imperial:
        britta "I'll make sure to get that to 28 inches by the end of the day too, but even that number sounds too small. What do you think is a good number?"
        pc "How about 35?"
    else:
        britta "I'll make sure to get that to 71 cm by the end of the day too, but even that number sounds too small. What do you think is a good number?"
        pc "How about 100?"
    britta "That will likely take me a while to get to, but sure, sounds good to me. That just means I can greatly increase my caloric intake and eat so much more food."
    pc "Just think of all those calories and fats and sugars that you can eat, all the high numbers of all of those things."
    britta "Oh yes, definitely. So what about my breasts then?"
    image luna_stage9_112 = "/luna/events/stage9/112.webp"
    scene luna_stage9_112
    "You then measure her underbust and then around the fullest part of her bust."
    if persistent.imperial:
        pc "You now need a 36H bra and your bust is now 43.6 inches around, which is actually the biggest out of any of the test subject other than Luna."
    else:
        pc "You now need a 36H bra and your bust is now 110.74 cm around, which is actually the biggest out of any of the test subject other than Luna."
    pc "That is quite impressive considering you were once the smallest."
    britta "Yes. I've been trying to optimize my breast growth, but I suspect that my recent major growth spurt is for a certain other reason."
    image luna_stage9_113 = "/luna/events/stage9/113.webp"
    scene luna_stage9_113
    "Luna who had just watched for a while was now leaning in to look closer at Britta’s breasts."
    luna "Is that what I think it is?"
    image luna_stage9_114 = "/luna/events/stage9/114.webp"
    scene luna_stage9_114
    "Britta smiled widely."
    britta "It sure is. You aren't the only one who likes her surprises, Luna. I'm starting to lactate like Natalie is."
    luna "That's awesome! Can I see you try to get some milk out?"
    britta "Of course."
    image luna_stage9_115 = "/luna/events/stage9/115.webp"
    scene luna_stage9_115
    "Britta squeezed at one of her breasts in order to get milk out. It wasn’t a lot, but you could definitely see some milk coming out."
    britta "I haven’t been able to get too much out yet, but if I’m anything like Natalie I’ll start producing a lot more."
    luna "Well, I think I know of one way to get more to come out... like maybe someone sucking it out for you?"
    image luna_stage9_116 = "/luna/events/stage9/116.webp"
    scene luna_stage9_116
    britta "You're right, maybe I should try that. [playername], would you like some?"
    pc "For sure. I've tried some of Natalie's and it was actually quite good."
    image luna_stage9_117 = "/luna/events/stage9/117.webp"
    scene luna_stage9_117
    luna "How come I don’t get some too?"
    britta "Since you're still being punished, remember?"
    luna "I'm your boss though. I should be the one punishing you - not the other way around."
    britta "Well, since you're my boss, shouldn't you not be doing anything sexual with your employees - including sucking their breasts?"
    luna "Well, I've been trying to hold back, but I just haven't been able to help myself after today and seeing all of you sexy girls get bigger."
    pc "I doubt anyone will report you though."
    image luna_stage9_118 = "/luna/events/stage9/118.webp"
    scene luna_stage9_118
    luna "True. I'm far more likely to be removed as Managing Director of the hospital for financial reasons."
    luna "But hey, at least if I'm no longer anyone's boss, I can fuck whomever I want and whoever wants to fuck me can do so."
    pc "Well, there is that. Roxie would probably be sad that you were no longer her boss, but happy that you got to start doing it with her."
    image luna_stage9_119 = "/luna/events/stage9/119.webp"
    scene luna_stage9_119
    britta "Well, not this time, Luna, but in that case I think I would let you have sex with me. It would be interesting to see what sex with a woman is like in comparison to a man."
    pc "I'm not going to lie; it does sound really hot. Do you think you might be bisexual, Britta?"
    image luna_stage9_120 = "/luna/events/stage9/120.webp"
    scene luna_stage9_120
    britta "I don't know. Really, sexual desire and attraction is all new to me, so I'm still trying to figure it out, but I think so?"
    britta "I mean, I find myself attracted to the changes my own body is going through and looking over and studying each of the test subjects and their progress."
    britta "I have been finding an appreciation for the female form, more in particular how that female form changes as it grows."
    luna "Mmm, I like that too. Even with the breast growth drug, none of the test subjects have grown quite the same way."
    britta "It really is quite fascinating. Anyway, I would really like to get back to where we left off."
    pc "Of course. So you wanted me to suck on your breasts then?"
    britta "Mmm, yes, while how about I be the one to talk about numbers?"
    image luna_stage9_121 = "/luna/events/stage9/121.webp"
    scene luna_stage9_121
    "You lean down and begin sucking on Britta's breast and the taste of her sweet and delicious milk starts to come to your mouth - not a lot, but still you are getting some."
    britta "Mmm, that feels good. It feels odd, but way better than I would have thought."
    if persistent.imperial:
        britta "So my breasts are now 43.6 inches around and I need a 36H bra?"
        britta "That's good. I'm quite happy with the progress that I've made there, but I'm sure I can do better. How does another 50 inches around sound to you?"
    else:
        britta "So my breasts are now 110.74 cm around and I need a 36H bra?"
        britta "That's good. I'm quite happy with the progress that I've made there, but I'm sure I can do better. How does another 100 cm around sound to you?"
    "You can't really talk with Britta's nipple still in your mouth, but you manage to say something muffled."
    britta "I’ll take that as a yes."
    image luna_stage9_122 = "/luna/events/stage9/122.webp"
    scene luna_stage9_122
    if persistent.imperial:
        luna "As a woman with boobs more than 50 inches around herself I think such an incredible size will look great on you."
    else:
        luna "As a woman with boobs more than 127 cm around herself I think such an incredible size will look great on you."
    britta "Well, I would really love to demonstrate just how effective my drug is in increasing breast size dramatically, and what better way to do that than to demonstrate it on myself?"
    "At that point it seems you’ve already sucked Britta dry and so you pop her nipple out of your mouth."
    image luna_stage9_148 = "/luna/events/stage9/148.webp"
    scene luna_stage9_148
    britta "Thank you for that. It felt really good... I think I'm ready now."
    pc "For me to-"
    if persistent.nosexscene == True:
        scene black with dissolve
        "Britta and you had a great time together."
    else:
        image luna_stage9_149 = "/luna/events/stage9/149.webp"
        scene luna_stage9_149
        britta "Yes! I wish to have you penetrate me and let me experience sex. Do you mind if I ask just how big your penis is?"
        if persistent.imperial:
            pc "It’s nine inches when hard."
        else:
            pc "It’s 23 cm when hard."
        #Bladerune9 note: I’m not sure just how big the Pc’s penis is or if it has been mentioned before but that can of course easily be changed here.
        image luna_stage9_150 = "/luna/events/stage9/150.webp"
        scene luna_stage9_150
        if persistent.imperial:
            britta "Mmm, so I'll have nine inches of penis inside me. That's good."
            pc "That’s right, nine inches of penis, made that size due to your delicious and curvy body."
        else:
            britta "Mmm, so I'll have 23 cm of penis inside me. That's good."
            pc "That’s right, 23 cm of penis, made that size due to your delicious and curvy body."
        britta "Mmm."
        image luna_stage9_151 = "/luna/events/stage9/151.webp"
        scene luna_stage9_151
        "You start to line up your penis with her entrance."
        pc "Are you ready?"
        britta "Yes, I’m ready."
        luna "You'll just want to go slow - especially since you are so large and this is Britta's first time."
        pc "Will do."
        image luna_stage9_152 = "/luna/events/stage9/152.webp"
        scene luna_stage9_152
        "You slowly start to enter her and Britta gasps as she starts to feel you inside her. Since she is a virgin she is extra tight."
        pc "You okay?"
        britta "Yes. I just... wasn't expecting it to feel like this. Luna was right; you really can't experience this kind of feeling from research."
        image luna_stage9_153 = "/luna/events/stage9/153.webp"
        scene luna_stage9_153
        britta "Go ahead, push further."
        luna "Time for you to lose your virginity and become a real woman."
        britta "Yes, time for that."
        image luna_stage9_154 = "/luna/events/stage9/154.webp"
        scene luna_stage9_154
        "You push forward, until Britta recoils slightly."
        "Britta seems to be in some pain, but seems to recover quickly."
        britta "I’m fine, please continue."
        image luna_stage9_155 = "/luna/events/stage9/155.webp"
        scene luna_stage9_155
        "You continue to push slowly deeper as Britta gets used to your size."
        britta "Oh my…"
        image luna_stage9_156 = "/luna/events/stage9/156.webp"
        scene luna_stage9_156
        "Once you are fully in her, you allow Britta a moment."
        britta "Wow, I feel so full... but, like, in a good way - like I just ate a ton of delicious food."
        image luna_stage9_157 = "/luna/events/stage9/157.webp"
        scene luna_stage9_157
        luna "Great way to put it. Now comes the fun part though, which is why - when it comes to food and sex - I have to admit, sex always wins."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage9/158.webm" loop
        show movie with dissolve
        window hide
        pause
        "You start to ram into Britta, enjoying the incredibly satisfied look on Britta’s face."
        britta "Ooh, so this is sex! Ooh, it feels so good!"
        luna "That's right, pound into her, deep into her. Show her how sexy she is."
        britta "Why did I wait so long to experience this? Sex feels so good!"
        "The pressure begins to build up."
        pc "I’m about to cum!"
        britta "Do it, cum inside me! Give me all of that sperm of yours!"
        "You do so, letting loose deep inside her with spurt after spurt."
        "After you finish, you both rest and relax."
        stop movie
        image luna_stage9_159 = "/luna/events/stage9/159.webp"
        scene luna_stage9_159
        britta "Thank you, thank you so much for that! Sex really is incredible and I’m glad that it was you that I got to experience it with for the first time."
        pc "No problem. I was more than happy to do it and I'm glad that I made you feel so good."
        britta "Definitely! I'm also definitely going to want to do that again with you, if that's okay?"
        pc "Absolutely, I would love to."
    image luna_stage9_123 = "/luna/events/stage9/123.webp"
    scene luna_stage9_123
    luna "That was really hot!"
    pc "I'm glad that you enjoyed that too, Luna."
    image luna_stage9_124 = "/luna/events/stage9/124.webp"
    scene luna_stage9_124
    "After talking for a little while longer you get dressed and go to meet Natalie in the hallway for your date."
    pc "Are you ready?"
    image luna_stage9_125 = "/luna/events/stage9/125.webp"
    scene luna_stage9_125
    natalie "Yes, I'm so ready! Where were you planning for us to go?"
    pc "Bunny Bites. I know it's not exactly super fancy or anything, but-"
    natalie "That's totally fine. I like Bunny Bites. Well, to be fair I mostly like it because I'm hoping to find you there. Besides, anywhere with you sounds great."
    pc "Anywhere with you sounds great too."
    pc "The reason, I want to go to Bunny Bites, is because last time I went there with Luna I made some ice cream from the breast milk you gave me and Luna loved it."
    pc "Actually, there were other customers asking to try it out, but I didn't have enough milk to make it for them."
    image luna_stage9_126 = "/luna/events/stage9/126.webp"
    scene luna_stage9_126
    natalie "Oh, I would love to do that and make ice cream from my milk! Also, if other people want to try it, then I should bring plenty of milk to do it."
    natalie "I really like the idea of people enjoying the milk that I produce and that way it doesn’t have to go to waste."
    image luna_stage9_127 = "/luna/events/stage9/127.webp"
    scene luna_stage9_127
    play music "/music/bunny_bites.ogg" if_changed
    "You and Natalie travel to Bunny Bites and Natalie goes and takes a seat and orders some food while you make the ice cream."
    image luna_stage9_128 = "/luna/events/stage9/128.webp"
    scene luna_stage9_128
    "When you come back with some of the ice cream, you let Natalie try some."
    natalie "Oh my, it really is delicious!"
    pc "You really are delicious that’s for sure."
    image luna_stage9_129 = "/luna/events/stage9/129.webp"
    scene luna_stage9_129
    "Natalie blushes and then looks over at a woman standing nearby watching."
    natalie "Do you want to try some really delicious ice cream we made? I will warn you though that we made it out of my breast milk."
    woman "Breast milk ice cream, huh? Well, that does sound kind of strange, but it does look delicious. I guess I'll try some."
    image luna_stage9_130 = "/luna/events/stage9/130.webp"
    scene luna_stage9_130
    "The woman takes a spoonful and then her eyes widen."
    woman "Wow, that is easily the best ice cream I’ve ever had!"
    image luna_stage9_131 = "/luna/events/stage9/131.webp"
    scene luna_stage9_131
    person "Hey, can I try some?"
    natalie "Sure! I think we can make enough for everyone!"
    image luna_stage9_132 = "/luna/events/stage9/132.webp"
    scene luna_stage9_132
    "You go back to make more and Natalie starts passing it out as it's made. It ends up being a huge hit with all the people at the diner."
    image luna_stage9_133 = "/luna/events/stage9/133.webp"
    scene luna_stage9_133
    natalie "Wow, I guess I know what to do with all my milk from now on."
    pc "Well, if you want I can talk to the owner of Bunny Bites and see if we can make your breast milk ice cream a special limited amount menu item?"
    natalie "Ooh, I would love that! It would feel so good knowing that the milk that I produce is so appreciated and liked... just like how you make me feel appreciated and liked."
    image luna_stage9_134 = "/luna/events/stage9/134.webp"
    scene luna_stage9_134
    "Natalie looks into your eyes and you look back into hers."
    pc "I’m glad that I make you feel that way."
    natalie "You definitely do. Nobody makes me feel as good as you."
    natalie "Before you came along I just felt so plain and unwanted and unappreciated and now…I feel better about myself and my life than I ever have before."
    pc "That’s great and I think it’s completely deserved for such an amazing and beautiful woman."
    "You look into each other’s eyes for a long moment until Natalie’s and your food arrives, with Natalie having ordered even more than her usual large order."
    image luna_stage9_135 = "/luna/events/stage9/135.webp"
    scene luna_stage9_135
    natalie "I ordered extra food because I was thinking maybe you would like to see me stuff myself to my limit?"
    natalie "I know you like seeing that with Luna and I want you to know you can do the same thing with me anytime."
    pc "I would love to of course."
    image luna_stage9_136 = "/luna/events/stage9/136.webp"
    scene luna_stage9_136
    "You watch Natalie pig out on all the fattening fast food."
    natalie "You really love this, don't you? Watching me eat all this food?"
    pc "I do."
    image luna_stage9_137 = "/luna/events/stage9/137.webp"
    scene luna_stage9_137
    "Natalie seems quite pleased with how you are looking at her as she continues to eat to her heart’s content."
    image luna_stage9_138 = "/luna/events/stage9/138.webp"
    scene luna_stage9_138
    natalie "Of course you know what the result will be?"
    natalie "My already huge breasts and the rest of me is just going to continue growing and there will be even more of me for you to love. Is that what you want?"
    pc "Yes, that’s what I want. Is that what you want?"
    natalie "Yes! I love eating so much food now and I love getting bigger, you helped me realize that. I never want to go back to plain, small, and unhappy Natalie. I’m moving onto bigger and better things!"
    image luna_stage9_139 = "/luna/events/stage9/139.webp"
    scene luna_stage9_139
    "At that Natalie launches back into eating with you encouraging her."
    image luna_stage9_140 = "/luna/events/stage9/140.webp"
    scene luna_stage9_140
    "Once Natalie finally finishes with a totally full belly, she has a pleased look on her face."
    image luna_stage9_141 = "/luna/events/stage9/141.webp"
    scene luna_stage9_141
    natalie "Did you like that?"
    pc "I did."
    natalie "Mmm, I did too. I'm really enjoying our date."
    pc "I'm glad you are. I'm really enjoying it too. Perhaps we can do this again sometime."
    image luna_stage9_142 = "/luna/events/stage9/142.webp"
    scene luna_stage9_142
    "Natalie smiled widely at that."
    natalie "I would love to anytime I'm available! You could even bring Luna or whomever else you want to bring... I know that we aren't going to be exclusive and that's okay."
    natalie "I'm willing to share if I need to... You are worth sharing."
    pc "Well, you deserve someone that can devote even more attention and time to you, and I'm sorry that I can't give you that."
    image luna_stage9_143 = "/luna/events/stage9/143.webp"
    scene luna_stage9_143
    natalie "It's okay. I understand. Can I, um... do something... something I've really been wanting to do?"
    pc "Yes. What is it?"
    image luna_stage9_144 = "/luna/events/stage9/144.webp"
    scene luna_stage9_144
    "Natalie stands up and looks at you nervously."
    natalie "Can I kiss you?"
    pc "Of course you can!"
    image luna_stage9_145 = "/luna/events/stage9/145.webp"
    scene luna_stage9_145
    "Natalie smiles again and happily leans in and kisses you."
    image luna_stage9_146 = "/luna/events/stage9/146.webp"
    scene luna_stage9_146
    natalie "Was the kiss good? Sorry. I know I'm not a good kisser and-"
    pc "It was great, don’t worry, and I’m looking forward to kissing you again on our next date."
    image luna_stage9_147 = "/luna/events/stage9/147.webp"
    scene luna_stage9_147
    natalie "Mmm, I guess I have another thing to look forward to then."
    "You say goodbye to Natalie and head home."
    stop music fadeout 1.0
    if recollection == False:
        $ luna.weight += 1
        $ mylenna.weight = 63
        $ daytime += 1
        $ phonecall = 1
    $ lunastage9event = 0
    return

label Luna_Stage_10_Event_1:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Luna', dialogue=dialogue_one)
    $ msg ("Hey do you have time to visit me? This time it will be at my house.", who=1)
    pause
    $ msg ("Sure, I’ll be right there.")
    pause
    $ hide_messenger()

    image luna_stage10_1 = "/luna/events/stage10/1.webp"
    scene luna_stage10_1
    "Upon getting to Luna’s house and ringing the doorbell you hear for you to just come in and so as you enter."
    image luna_stage10_2 = "/luna/events/stage10/2.webp"
    scene luna_stage10_2
    "You find Luna sitting on her bed with a bunch of food containers sitting next to her, some of which are empty and some are still full."
    "Luna herself however is currently busy stuffing herself silly."
    image luna_stage10_3 = "/luna/events/stage10/3.webp"
    scene luna_stage10_3
    luna "Great, you’re here, now help stuff me full of food until all I can think about is how stuffed I am."
    "You of course are more than happy to agree as you help feed her more and more food as her belly continues to increase in size."
    image luna_stage10_4 = "/luna/events/stage10/4.webp"
    scene luna_stage10_4
    "You shift some of the boxes around to sit next to her on the bed."
    pc "So is this your day off from work then?"
    image luna_stage10_5 = "/luna/events/stage10/5.webp"
    scene luna_stage10_5
    "Luna frowns at hearing that."
    luna "I don’t want to even think about work, just food."
    "You can tell that there is something seriously wrong, but Luna doesn’t want to admit it."
    pc "Is there something going on with work?"
    image luna_stage10_6 = "/luna/events/stage10/6.webp"
    scene luna_stage10_6
    luna "Oh just losing most of my dreams at once is all, I’m no longer Managing Director of the Hospital."
    luna "The Hospital Board wants to change everything I’ve worked for so they can squeeze out every last penny from every last patient they can."
    luna "They even want to defund and shut down the drug trial is all."
    pc "I’m so sorry! Is there anything I can do?"
    image luna_stage10_7 = "/luna/events/stage10/7.webp"
    scene luna_stage10_7
    luna "Just try and help me take my mind off it by helping me eat, eating makes me feel better."
    pc "Well normally I would be all for you eating as much as possible, but in this case I feel like it might be better if you try to let out how you are feeling."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage10/vid1.webm" loop
    show movie with dissolve
    luna "I suppose you might be right, well you’ve obviously known for a while that this was becoming more and more of a possibility and I knew it was going to happen."
    luna "I was just hoping I could delay it until after I started getting a lot of funding for the drug trial."
    luna "That by the way I still have total control over, the only problem is I can no longer use the hospital’s profits to fund it."
    luna "That’s partly why they forced me to step down."
    luna "I refused to charge patients way more money like they wanted and a lot of the profits that we were getting I was putting into the breast growth drug development."
    pc "So if we can find some external funding we can at least continue with that?"
    luna "Yes, the only problem is I’ve already called everyone who could possibly be interested in investing in it."
    luna "So I might as well just give up and try to live out the last dream I have remaining that I can actually achieve, which is to get my breasts and the rest of me as big and fat as possible."
    luna "With all of this free time I’ll now have and using the remaining drug samples."
    stop movie
    image luna_stage10_8 = "/luna/events/stage10/8.webp"
    scene luna_stage10_8
    luna "I can just sit on this bed and eat and eat, watching my ass take up more and more of this bed, and my breasts reach the size of bean bag chairs."
    luna "At some point I’ll get so big I can no longer walk or move on my own, but I’m guessing you won’t mind helping me get around when I get that big?"
    pc "No, of course not."
    image luna_stage10_9 = "/luna/events/stage10/9.webp"
    scene luna_stage10_9
    luna "Good, I knew I could count on you."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage10/vid2.webm" loop
    show movie with dissolve
    luna "You won’t have to do all the work though, I figure I can make plenty of money doing online stuff and have enough money to hire someone to help me."
    luna "Maybe I can even get Roxie to do it, I bet she’d love that job."
    pc "I’m sure she would."
    luna "So you don’t need to worry about me, I’ve got this figured out."
    luna "I’ll never have to worry about dieting or exercise or making those greedy, heartless jerks on the hospital board happy again."
    luna "I can just focus on eating and making myself as massive as possible."
    pc "As hot as that sounds and I would of course be willing to help."
    pc "I feel like you really shouldn’t give up just yet on the drug trial, I just feel like it has so much potential and could help so many people, surely someone will be more than willing to help."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage10/vid3.webm" loop
    show movie with dissolve
    luna "That’s what I thought too but I guess people care more about themselves and how much money they can make."
    luna "The problem is most any potential investor in a medical drug trial is likely already making money from other medical drugs or health care of some sort."
    luna "Which would suddenly lose a lot of money if you could cure a lot of those diseases and health problems with our drug."
    luna "They also seem to be pretty turned off from the gaining weight and much larger breasts thing."
    pc "I’m still not willing to give up even if you are, it’s just like how I will never give up on you."
    stop movie
    image luna_stage10_10 = "/luna/events/stage10/10.webp"
    scene luna_stage10_10
    "Luna smiles, seemingly touched by your support."
    luna "Well I’m not sure what you can really do, but I certainly appreciate it in any case."
    image luna_stage10_11 = "/luna/events/stage10/11.webp"
    scene luna_stage10_11
    "At that moment Luna gets a phone call and she decides to answer it."
    image luna_stage10_12 = "/luna/events/stage10/12.webp"
    scene luna_stage10_12
    luna "Yes?"
    "You can hear Britta’s voice coming from the phone."
    britta "You’ve got to come down here! Something amazing has happened!"
    image luna_stage10_13 = "/luna/events/stage10/13.webp"
    scene luna_stage10_13
    luna "Something to do with the drug trial?"
    britta "Yes! I don’t want to tell you over the phone, I think it’s best if you see for yourself."
    luna "Okay I’ll be right over."
    image luna_stage10_14 = "/luna/events/stage10/14.webp"
    scene luna_stage10_14
    "She ends the phone call."
    pc "I’ll come with you."
    image luna_stage10_15 = "/luna/events/stage10/15.webp"
    scene luna_stage10_15
    luna "Sure. I think we will sneak in through the back though."
    luna "I mean I still am a part owner and I’m still in charge of the drug trial for however long that lasts but I would still rather not see anyone else and have it be awkward with me just getting fired."
    pc "Understandable although it will be disappointing not to get to see Natalie."
    image luna_stage10_16 = "/luna/events/stage10/16.webp"
    scene luna_stage10_16
    luna "Yeah, I started to feel guilty about you not getting to see her but then I remembered it’s Natalie’s day off anyway so she won’t be around."
    pc "Disappointing but okay."
    image luna_stage10_17 = "/luna/events/stage10/17.webp"
    scene luna_stage10_17
    "Upon getting to the hospital and going in through the back and then to Britta’s research lab, you find Britta there with Mylenna…or at least you think it is Mylenna."
    image luna_stage10_18 = "/luna/events/stage10/18.webp"
    scene luna_stage10_18
    "Mylenna looks almost like a totally different person, she looks much healthier and stronger and she smiles when she sees you."
    image luna_stage10_19 = "/luna/events/stage10/19.webp"
    scene luna_stage10_19
    mylenna "It’s working! I feel so much better now!"
    britta "Yes, isn’t it just wonderful? She still has a ways to go to make a full recovery, but I think her current results and progress speak for itself."
    image luna_stage10_20 = "/luna/events/stage10/20.webp"
    scene luna_stage10_20
    "Luna goes to look over Mylenna in amazement and Mylenna is more than happy to oblige as tears come to her eyes."
    image luna_stage10_21 = "/luna/events/stage10/21.webp"
    scene luna_stage10_21
    mylenna "Thank you! Thank you all of you, because of this miracle drug you created I now have a chance to live and see my daughter grow up."
    image luna_stage10_22 = "/luna/events/stage10/22.webp"
    scene luna_stage10_22
    "Luna can’t help but cry herself at hearing this likely news."
    luna "You’re very welcome! Just knowing that the drug development will likely help save you makes it more than worth it."
    pc "Well this settles it then, the drug works, which means we simply can’t give up on it now."
    image luna_stage10_23 = "/luna/events/stage10/23.webp"
    scene luna_stage10_23
    luna "Agreed, we’ll find a way to see it continue with its development."
    pc "I’ll make phone calls or try to get in contact with whoever I can think of."
    image luna_stage10_24 = "/luna/events/stage10/24.webp"
    scene luna_stage10_24
    britta "You won’t be alone, I’ll help too and get all the test subject nurses involved as well."
    britta "I’m sure they would be more than happy to help and with all of us trying to find a financial backer I’m sure we can find someone."
    image luna_stage10_25 = "/luna/events/stage10/25.webp"
    scene luna_stage10_25
    pc "Maybe that was the problem all along, you don’t need to do this alone anymore Luna, you have all of us here to support you, you have a lot of people that I’m sure care about and love you."
    image luna_stage10_26 = "/luna/events/stage10/26.webp"
    scene luna_stage10_26
    "Tears come once more to Luna’s eyes as she seems overwhelmed by all the love and support."
    luna "Thank you! Yes, you’re right, of course we will never give up and we will succeed somehow. Also I love you too!"
    image luna_stage10_27 = "/luna/events/stage10/27.webp"
    scene luna_stage10_27
    "Luna reaches forward and gives you a hug, crushing her massive breasts into you."
    luna "I love you!"
    pc "I love you too."
    image luna_stage10_28 = "/luna/events/stage10/28.webp"
    scene luna_stage10_28
    "It’s the first time both of you have said it, but it feels right and you feel like you can say it and mean it."
    "You aren’t sure just what the future holds but you know now that Luna loves you and you love her too and together you feel like you can achieve anything."
    "After a moment of bliss, Luna, Mylenna and you decide to go home."
    image luna_stage10_29 = "/luna/events/stage10/29.webp"
    scene luna_stage10_29
    britta "Wait [playername], because we gave Mylenna the drug she has also been growing."
    image luna_stage10_30 = "/luna/events/stage10/30.webp"
    scene luna_stage10_30
    britta "I recorded her measurements for now. Here they are."
    $ mylenna_stats_visible = 1
    "Mylenna has been added to stats menu."
    image luna_stage10_31 = "/luna/events/stage10/31.webp"
    scene luna_stage10_31
    britta "Just like us, she will be growing for a while longer."
    britta "I want you to visit her once in a while and check up on her progress to make sure that everything is going well, can you do that for me?"
    pc "Sure, leave it to me."
    image luna_stage10_32 = "/luna/events/stage10/32.webp"
    scene luna_stage10_32
    britta "Thank you, I have a lot of work to do so I better get back to it, see you later."
    pc "See you later, Britta."
    "You head home."
    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
    $ lunastage10event = 0
    return

label Luna_Stage_10_Event_2:
    "You decide to ask Natalie out on another date and she asks you to pick her up at the hospital after work."
    image luna_stage10_33 = "/luna/events/stage10/33.webp"
    scene luna_stage10_33
    "She is already off work when you get there so you find out that she is with Britta at the drug research lab."
    "The two of them are talking quite excitedly about something and don’t seem to notice you as they continue talking."
    image luna_stage10_34 = "/luna/events/stage10/34.webp"
    scene luna_stage10_34
    britta "Oh he’s huge! All those wonderful inches and centimeters and volume of his beautiful penis inside of me!"
    britta "I totally have to get exact measurements of it, each and every part of it, it’s incredible length, width, and girth."
    britta "Then the force at which he was able to push in and out of me and the pleasure I felt…it felt better than if I won the Nobel prize."
    "Natalie seemed to listen to Britta’s every word with great interest."
    image luna_stage10_35 = "/luna/events/stage10/35.webp"
    scene luna_stage10_35
    natalie "Wow, that sounds so amazing, I’m so happy for you! Having sex with him really felt that good? Yet how were you able to take all of him and his penis though?"
    britta "It was a challenge but one I was certainly glad to take on, getting such a huge and magnificent penis inside of me."
    image luna_stage10_36 = "/luna/events/stage10/36.webp"
    scene luna_stage10_36
    "Natalie however looked a little worried."
    natalie "I’m just not sure if I will be able to handle it when…or if…me and him have sex. What if I can’t or what if I perform badly for him and he doesn’t want me anymore?"
    image luna_stage10_37 = "/luna/events/stage10/37.webp"
    scene luna_stage10_37
    britta "First of all, don’t worry, you will stretch out and you might just need time to adjust to his size."
    britta "Also you continuing to get bigger should also help, not only in how much of his dick you can handle but also the quality of the sex."
    britta "I’ve been doing some reading and there are some interesting articles that show that sex with a bigger girl is definitely better."
    britta "I’d say the bigger you continue to get, the even better the sex will be especially when you know how much he likes big, curvy girls."
    britta "Speaking of which, how could he not want you with your curves and sweet personality? You’re way better than you give yourself credit for, you’re like an 11 out of 10."
    image luna_stage10_38 = "/luna/events/stage10/38.webp"
    scene luna_stage10_38
    "You then decide to make your presence known."
    pc "An 11 out of 10 for sure."
    image luna_stage10_39 = "/luna/events/stage10/39.webp"
    scene luna_stage10_39
    "Both girls then turned to look at you and blushed."
    pc "Sorry I couldn’t help but overhear."
    image luna_stage10_40 = "/luna/events/stage10/40.webp"
    scene luna_stage10_40
    natalie "It’s fine, I’m sorry too though, Britta really wanted to tell me about her first time with you and I got really curious."
    pc "I don’t mind at all, Britta can tell you whatever she wants."
    image luna_stage10_41 = "/luna/events/stage10/41.webp"
    scene luna_stage10_41
    britta "I told you he wouldn’t mind Natalie."
    natalie "Yeah I know and I and I really want to do it too, I’m just…really nervous about it."
    pc "Like I told you before Natalie we will do it when you are ready, you are more than worth waiting over but you don’t need to worry about everything going perfect."
    pc "We can figure it out when the times comes, also if talking it over with Britta or someone else would help then by all means feel free to do so."
    image luna_stage10_42 = "/luna/events/stage10/42.webp"
    scene luna_stage10_42
    "Natalie sighed and looked at you with appreciation."
    natalie "You really are so wonderful…and I may not be ready for that but there is something I am ready for."
    image luna_stage10_43 = "/luna/events/stage10/43.webp"
    scene luna_stage10_43
    "She looks nervous but then goes over to you and kisses you, pressing her now huge breasts into you as you start kissing her back."
    image luna_stage10_44 = "/luna/events/stage10/44.webp"
    scene luna_stage10_44
    "She moans and hungrily starts going at it, with you happy to follow. You can also feel your now growing erection pressing into her, but this only seems to encourage her to continue."
    image luna_stage10_45 = "/luna/events/stage10/45.webp"
    scene luna_stage10_45
    "Finally Natalie breaks apart from you, a pleased smile on her face."
    britta "That was certainly interesting to watch, do you mind if I ask how you felt while doing that? Sorry I’m just curious."
    pc "Well I was thinking there is this totally hot woman that I really like now kissing me and I definitely want to kiss her back."
    image luna_stage10_46 = "/luna/events/stage10/46.webp"
    scene luna_stage10_46
    "Natalie smiles at hearing you admit that which gives her the courage to admit what she is really thinking."
    natalie "It feels like I just want him, like I hunger for him more than food, I just want him to desire me just like I desire him, and I want us to come together and feel like we are a part of each other."
    britta "That’s a really beautiful way of putting it Natalie, I hadn’t thought of it like that."
    pc "I wish I explained it so nicely, you’re right that was really beautiful Natalie."
    image luna_stage10_47 = "/luna/events/stage10/47.webp"
    scene luna_stage10_47
    "Natalie smiles at the compliment."
    britta "The thing is I’m just curious because I’ve always been so focused on facts and logic but now…after having had sex for the first time…"
    britta "A whole new world of feelings and emotions and desires has opened up for me and I want to explore and understand them."
    image luna_stage10_48 = "/luna/events/stage10/48.webp"
    scene luna_stage10_48
    natalie "I feel much the same way, I’ve definitely felt things that I’ve never felt before meeting him. Then there are the changes with how I feel about food and my growing body."
    natalie "I feel like I’m still learning so much about myself with these changes but so far they’ve all been very good changes."
    pc "Well I’m happy to help both of you girls as much as I can with figuring out your feelings."
    image luna_stage10_49 = "/luna/events/stage10/49.webp"
    scene luna_stage10_49
    natalie "I think it would be really great if all 3 of us tried to figure them out together."
    britta "What are you suggesting Natalie?"
    natalie "I was kind of thinking maybe you might like to come with us on our date?"
    natalie "I know how excited you are about all this sex and relationship stuff and I think it would be good for you to experience it more yourself."
    image luna_stage10_50 = "/luna/events/stage10/50.webp"
    scene luna_stage10_50
    "Britta seems quite surprised."
    britta "Oh no, I wouldn’t want to intrude."
    natalie "You wouldn’t be intruding! I know I’m already sharing him with other women anyway and I think you deserve to be happy too."
    "Of course you have no objections if Natalie is actually encouraging it."
    pc "I would of course love to have you with us on our date if Natalie wants you to."
    image luna_stage10_51 = "/luna/events/stage10/51.webp"
    scene luna_stage10_51
    britta "Really? Are you sure?"
    natalie "Yes, I’m sure!"
    britta "Thank you! Just warn me if I’m too much of a bother though or if you get tired of hearing about it if I start talking about my research or something."
    pc "We like hearing about your research too even if we don’t understand it, so what have you been studying?"
    image luna_stage10_52 = "/luna/events/stage10/52.webp"
    scene luna_stage10_52
    britta "Well with the drug project’s status currently in limbo, I haven’t really been sure what to work on with that, my own personal research about sex however has been far more fascinating."
    britta "For example I had no idea there is even a sex position called a 69, can you believe it? A sex position that is also a number! That sounds totally for me."
    pc "Yeah, we can definitely try that."
    image luna_stage10_53 = "/luna/events/stage10/53.webp"
    scene luna_stage10_53
    britta "I want to try all of it, all the vaginal sex positions, oral, anal, titfucks, I want to experience the full range of sexual experiences."
    "Apparently Britta has a lot she wants to try out…apparently you’ve got some interesting things to look forward to."
    pc "I certainly don’t have a problem at least trying all that with you."
    britta "It doesn’t need to be all at once, just whenever, in fact there are a lot of things I want to try when I hopefully am able to get a whole lot bigger as I think it will enhance the experience."
    pc "Sounds great to me and we can discuss it later, anyway as for right now I’m just looking forward to taking two gorgeous girls out on a date."
    image luna_stage10_54 = "/luna/events/stage10/54.webp"
    scene luna_stage10_54
    "Both girls smiled at hearing that and happily agreed."
    pc "Actually it’s rather good that I’m taking both of you as there is something I was planning to show you both anyway."
    image luna_stage10_55 = "/luna/events/stage10/55.webp"
    scene luna_stage10_55
    natalie "What do you want to show us?"
    pc "It’s a surprise."
    image luna_stage10_56 = "/luna/events/stage10/56.webp"
    scene luna_stage10_56
    britta "Now you’re starting to sound too much like Luna with the surprises."
    pc "I wouldn’t say being more like Luna is a bad thing."
    natalie "I agree, Luna is the best!"
    britta "I’m not going to argue with that, so should we get going then? I’m now pretty curious just what the surprise is."
    natalie "Me too, and yes, let’s get going."
    image luna_stage10_57 = "/luna/events/stage10/57.webp"
    scene luna_stage10_57
    play music "/music/date_cozy.ogg" if_changed
    "The three of you then head out and go to Bunny Bites where you find a booth to sit at."
    image luna_stage10_58 = "/luna/events/stage10/58.webp"
    scene luna_stage10_58
    pause
    image luna_stage10_59 = "/luna/events/stage10/59.webp"
    scene luna_stage10_59
    natalie "Is the surprise feeding us lots of food and trying to fatten us up and make our breasts larger?"
    britta "That wouldn’t be a surprise at all though, we should expect him to try to do that."
    pc "No, look at the bottom of the menu on the back."
    image luna_stage10_60 = "/luna/events/stage10/60.webp"
    scene luna_stage10_60
    "Both girls looked and their eyes widened."
    natalie "Our breast milk ice cream is now on the menu?"
    pc "That’s right."
    pc "I convinced the owner to put it on there on a limited basis based on supply, in exchange both of you will be receiving major discounts on food here depending on how much milk you bring in."
    natalie "That’s awesome! I’m totally bringing all of my milk in here now."
    image luna_stage10_61 = "/luna/events/stage10/61.webp"
    scene luna_stage10_61
    britta "Me too, I do wonder though what will be the effects of people eating or drinking our milk though."
    britta "I’ve been analyzing both mine and Natalie’s and it seems to be very fattening, but also packed full of nutrients and antibodies so the people who eat it could expect to gain weight more quickly,"
    britta "but also receive a lot of the health benefits that we are receiving from the drug."
    image luna_stage10_62 = "/luna/events/stage10/62.webp"
    scene luna_stage10_62
    natalie "So the more milk we produce and the more ice cream from it people eat, the more healthy and fat people would get?"
    britta "Yes, it’s impossible to say how much right now, but it will definitely be interesting to study."
    britta "It also seems that the more we grow and the more that we let the drug affect us the more milk we will produce and the more powerful it will become."
    natalie "Then I definitely want to grow a lot more if it means I can help more people."
    britta "I will want to do the same as it will only help with my research."
    pc "If both of you girls want to for those reasons that sounds great to me and I’m happy to help."
    image luna_stage10_63 = "/luna/events/stage10/63.webp"
    scene luna_stage10_63
    "Both girls smiled at that."
    britta "I figured you would agree."
    image luna_stage10_64 = "/luna/events/stage10/64.webp"
    scene luna_stage10_64
    "The girls then settled in to look at what they were going to order."
    pc "What do you think you’re going to get?"
    image luna_stage10_65 = "/luna/events/stage10/65.webp"
    scene luna_stage10_65
    britta "I don’t know, maybe 3 or 4 large pizzas for me, I’m so hungry I feel like I could eat 3.14159 pizza pies!"
    pc "What about you Natalie?"
    image luna_stage10_66 = "/luna/events/stage10/66.webp"
    scene luna_stage10_66
    natalie "I don’t know, everything looks good right now. Actually there is something that I’ve been wanting to try…I’m just not sure I can do it yet."
    pc "What?"
    natalie "I keep wanting to try to eat…everything on the menu at once."
    pc "Bunny Bites has a quite large menu, that’s um…a lot of food. I think even Luna could really only eat half of it."
    image luna_stage10_67 = "/luna/events/stage10/67.webp"
    scene luna_stage10_67
    natalie "I know, but I still want to try...you’re right though it’s definitely too much."
    britta "I think I might have something that can help."
    image luna_stage10_68 = "/luna/events/stage10/68.webp"
    scene luna_stage10_68
    "She looks through her purse before then pulling out a couple vials."
    britta "Two of the stomach muscle relaxants. One for each of us."
    pc "Each?"
    image luna_stage10_69 = "/luna/events/stage10/69.webp"
    scene luna_stage10_69
    britta "I’ve decided I want to try and do the same thing too and help you, we will get and share one of everything on the menu. I want to see if we can do this together with our combined eating power."
    natalie "Mmm, sounds good then, the only problem is there is no way we will have room on the table."
    pc "I’ll just tell the server to just keep it coming and take away empty dishes until you girls go through everything."
    "You walk to the front desk to place your gigantic order, even Marie seemed surprised."
    image luna_stage10_70 = "/luna/events/stage10/70.webp"
    scene luna_stage10_70
    "You and the two girls went back to chatting while you waited for the food to arrive."
    britta "So anyway, how is finding investors for the drug project going?"
    pc "I wish I could say it’s going better, but it’s not from a lack of trying and each of you have been trying to help by giving me names of companies and individuals."
    pc "The problem is I can’t really talk to anyone in charge directly."
    pc "I just end up talking to some secretary or receptionist who won’t let me directly talk with anyone who could really help and make decisions."
    image luna_stage10_71 = "/luna/events/stage10/71.webp"
    scene luna_stage10_71
    natalie "Maybe I could help with that, I do speak receptionist after all."
    natalie "First of all you need to treat them with kindness and show that you care about them, not what they can do for you first, much like the way you first talked to me."
    pc "That’s actually really good advice and I would welcome any further help you can give."
    natalie "Of course, I would love to help!"
    image luna_stage10_72 = "/luna/events/stage10/72.webp"
    scene luna_stage10_72
    britta "I can of course explain all of the science stuff to people once you get that far."
    pc "Yes I will definitely need you for that, thank you. With you and the other girls helping out I’m sure we will find someone to invest in us."
    image luna_stage10_73 = "/luna/events/stage10/73.webp"
    scene luna_stage10_73
    "By that point the food begins to arrive and you enjoy the excited looks on Natalie’s and Britta’s faces as they first take the muscle relaxant and then start eating."
    image luna_stage10_74 = "/luna/events/stage10/74.webp"
    scene luna_stage10_74
    natalie "Ooh, can I have the rest of that pepperoni pizza?"
    britta "Sure if I can have the rest of that burger."
    pc "You know, when you girls talked of sharing, I didn’t think you also meant this."
    "You are of course clearly joking."
    image luna_stage10_75 = "/luna/events/stage10/75.webp"
    scene luna_stage10_75
    britta "Just as long as there is enough of you and enough food to share."
    pc "I’ll do my best to try and keep you both happy."
    image luna_stage10_76 = "/luna/events/stage10/76.webp"
    scene luna_stage10_76
    natalie "Well we’re going to do our best to eat all of this."
    image luna_stage10_77 = "/luna/events/stage10/77.webp"
    scene luna_stage10_77
    "Plate after plate of food continues to arrive, with both girls struggling to keep up with clearing dishes so that even more food can be brought to the table."
    image luna_stage10_78 = "/luna/events/stage10/78.webp"
    scene luna_stage10_78
    "Even so, you are incredibly amazed at just how much both girls are now eating."
    pc "No way you two could eat like this before the drug trial, that’s for sure."
    image luna_stage10_79 = "/luna/events/stage10/79.webp"
    scene luna_stage10_79
    natalie "No way, and no way I’m ever going back to eating so little ever again."
    britta "Same. No more skipping or forgetting meals just to work on my research, more like constantly eating while I do my research, and pushing my stomach capacity to further and further limits."
    image luna_stage10_80 = "/luna/events/stage10/80.webp"
    scene luna_stage10_80
    "By this point, the girls are clearly getting very full even with the stomach muscle relaxant, but they seem to have eaten most things by now, except for…"
    pc "I hope you girls still have room for dessert."
    image luna_stage10_81 = "/luna/events/stage10/81.webp"
    scene luna_stage10_81
    natalie "There’s always room for dessert! There will always be room in my heart and my stomach for dessert."
    image luna_stage10_82 = "/luna/events/stage10/82.webp"
    scene luna_stage10_82
    "The regular desserts at Bunny Bites start being brought out, which Natalie and Britta struggle to, but still manage to finish."
    image luna_stage10_83 = "/luna/events/stage10/83.webp"
    scene luna_stage10_83
    "You marvel at their now absolutely huge bellies, full and tight with food."
    image luna_stage10_84 = "/luna/events/stage10/84.webp"
    scene luna_stage10_84
    "However you notice there is still one thing left on the menu now that the girls haven’t gotten yet."
    pc "Hey, where is the ice cream?"
    image marie_workattire_counter = "/marie/[marie.stage]/workattire_counter.webp"
    scene marie_workattire_counter
    "Since it seems Marie and the other staff are in the back, you just decide to go in the back yourself and ask them."
    "After doing so you then return to the table with Natalie and Britta."
    image luna_stage10_85 = "/luna/events/stage10/85.webp"
    scene luna_stage10_85
    pc "Apparently they are already out of stock of your milk for the ice cream, it only just started being served today and they already ran out hours ago."
    natalie "How much of our milk did you give them?"
    pc "It should have been plenty, it just seems that your ice cream breast milk is already that popular."
    image luna_stage10_86 = "/luna/events/stage10/86.webp"
    scene luna_stage10_86
    "Natalie and Britta however just smile."
    natalie "I guess we just need to make some more then, want to help?"
    pc "Oh absolutely."
    image luna_stage10_87 = "/luna/events/stage10/87.webp"
    scene luna_stage10_87
    "The three of you go into the back where Natalie and Britta strip naked and then start breast pumping."
    image luna_stage10_88 = "/luna/events/stage10/88.webp"
    scene luna_stage10_88
    "The three of you go into the back where Natalie and Britta strip naked and then start breast pumping."
    image luna_stage10_89 = "/luna/events/stage10/89.webp"
    scene luna_stage10_89
    britta "I can’t say I’ve read about this being a potential date activity."
    pc "It is a bit weird, but I’m certainly not complaining, it’s basically like getting to see a show after dinner. I also love how busty and milky you girls are getting."
    image luna_stage10_90 = "/luna/events/stage10/90.webp"
    scene luna_stage10_90
    natalie "Mmm, glad you enjoy it, and we’re only going to get even more busty and milky."
    pc "I’m looking forward to it."
    image luna_stage10_91 = "/luna/events/stage10/91.webp"
    scene luna_stage10_91
    "You then can’t resist giving a kiss to both Natalie and then Britta, causing both of the girls to smile happily."
    image luna_stage10_92 = "/luna/events/stage10/92.webp"
    scene luna_stage10_92
    "You then can’t resist giving a kiss to both Natalie and then Britta, causing both of the girls to smile happily."
    image luna_stage10_88 = "/luna/events/stage10/88.webp"
    scene luna_stage10_88
    "This was certainly a very enjoyable and milky date."
    stop music fadeout 1.0
    if recollection == False:
        $ phonecall = 1
        $ daytime += 1

    scene player_room
    "Upon getting home, you start trying to see who might be able to help Luna get an investor."
    "Each of the test subjects immediately offer their support as you start getting text messages from them."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Roxie', dialogue=dialogue_one)
    $ msg (None, pic="stage3_roxie1")
    pause
    $ msg (None, pic="stage3_roxie2")
    pause
    $ msg ("Do you think if I try going up to and talking to a potential investor dressed like this it might help?", who=1)
    pause
    $ msg ("Uh…yeah that definitely might work.")
    pause
    $ msg ("A little more sex appeal than this might help too.", who=1)
    pause
    $ msg ("Guess I’ll just need to eat plenty and see how much I can overflow this outfit before it rips?", who=1)
    pause
    $ msg ("Then again it ripping might actually help the cause even more.", who=1)
    pause
    $ msg ("Whatever I’ve got to do to help Luna.", who=1)
    pause
    $ msg ("You don’t need to do anything too extreme.")
    pause
    $ msg ("Especially nothing you would feel too uncomfortable with or that might get you arrested.")
    pause
    $ msg ("Although those curves already feel like they should be illegal.")
    pause
    $ msg ("Maybe you should arrest me then?", who=1)
    pause
    $ msg ("Handcuff me and lock me up somewhere?", who=1)
    pause
    $ msg ("Then not let me go until I eat an enormous amount of food.", who=1)
    pause
    $ msg ("Sounds tempting.")
    pause
    $ msg ("It also sounds like a fantasy you have.")
    pause
    $ msg ("You got me.", who=1)
    pause
    $ msg ("Maybe someday I might even decide to roleplay it with you.", who=1)
    pause
    $ msg ("For the record I wouldn’t want to go beyond dressing a certain way and flirting a little when it comes to guys.", who=1)
    pause
    $ msg ("Although I might be willing to make a major exception in your case.", who=1)
    pause
    $ msg ("Should I be asking you just what you mean by that?")
    pause
    $ msg ("How about for now let’s focus on helping Luna?", who=1)
    pause
    $ msg ("Agreed. Let’s focus on helping Luna.")
    pause
    $ hide_messenger()

    "You next get a picture and a text message from Sally."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Sally', dialogue=dialogue_one)
    $ msg (None, pic="stage3_sally1")
    pause
    $ msg (None, pic="stage3_sally2")
    pause
    $ msg ("Alright, who do I got to seduce a little to get an investor?", who=1)
    pause
    $ msg ("I think Roxie already has that covered.")
    pause
    $ msg ("I can see that.", who=1)
    pause
    $ msg ("It’s the eyes, they are like fuck me eyes.", who=1)
    pause
    $ msg ("Even I sometimes find myself lost in them and thinking naughty thoughts.", who=1)
    pause
    $ msg ("Anyway I don’t think we should be relying on just sex appeal.")
    pause
    $ msg ("To be fair if we were to rely heavily on that with all of you girls we could get an investor by the end of the day.")
    pause
    $ msg ("What we want though is to find an investor who is truly committed to the cause, one who believes in what we are doing.")
    pause
    $ msg ("That is going to be a lot harder then.", who=1)
    pause
    $ msg ("Most drug companies aren’t going to help invest in something that is going to make most of their products obsolete.", who=1)
    pause
    $ msg ("Which is why it’s been so hard to find an investor.")
    pause
    $ msg ("Maybe you need to think outside the box or rather outgrow the box?", who=1)
    pause
    $ msg ("Do you have any ideas?")
    pause
    $ msg ("Maybe, I’ll have to get back to you.", who=1)
    pause
    $ msg ("Okay, any help you can give would be great, thanks.")
    pause
    $ hide_messenger()

    "You next get a text from Natalie."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Natalie', dialogue=dialogue_one)
    $ msg ("I would love to help but I don’t know how I can.", who=1)
    pause
    $ msg ("Unless I were to use my family’s secret brownie recipe and give brownies out to some companies in exchange for getting them to listen.", who=1)
    pause
    $ msg ("It might be a struggle not to eat them all myself though.", who=1)
    pause
    $ msg ("To be honest I’d rather see you eat all those brownies too.")
    pause
    $ msg ("Maybe just one for myself.")
    pause
    $ msg ("However, maybe we can send them some after getting to talk to them, as a way to sweeten the deal.")
    pause
    $ msg ("Okay, will do.", who=1)
    pause
    $ hide_messenger()

    "You lastly get a text from Charlene."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Charlene', dialogue=dialogue_one)
    $ msg ("Hey, just because I don’t personally like the effects that the drug is having on me doesn’t mean I don’t want the drug trial to succeed.", who=1)
    pause
    $ msg ("I’ll help however I can.", who=1)
    pause
    $ msg ("Thank you, I appreciate the support.")
    pause
    $ msg ("I’ll try to come up with ideas.")
    pause
    $ msg ("Sally suggested I try and think of someone I wouldn’t ordinarily think of.")
    pause
    $ msg ("You just need a company who would benefit and actually want women to get fatter.", who=1)
    pause
    $ msg ("Somebody like you who likes fat women only they have lots of money or perhaps a junk food company who would want more women unable to resist eating more and more of their products.", who=1)
    pause
    $ msg ("I feel like I single handedly am keeping many of them in business.", who=1)
    pause
    $ msg ("That’s not a bad idea, I could try some of them although I fear as soon as I say it is also a health drug they might immediately not be interested.")
    pause
    $ msg ("Junk food and health drugs sound like a bad combination unless we get the time to explain it, which might be difficult to get.")
    pause
    $ msg ("Well if you do get the chance, I’ll talk to them and make sure they listen.", who=1)
    pause
    $ msg ("I’d love to see someone else get a stern talking to from you that isn’t me.")
    pause
    $ msg ("Yeah, maybe you don’t deserve that.", who=1)
    pause
    $ msg ("What’s this? Are you suddenly getting soft on me?")
    pause
    $ msg ("No.", who=1)
    pause
    $ msg ("I mean I am getting soft, particularly around the middle but what I mean is.", who=1)
    pause
    $ msg ("I want something from you.", who=1)
    pause
    $ msg ("That’s all and I’m trying to be nice to get it.", who=1)
    pause
    $ msg ("Let me guess.")
    pause
    $ msg ("Do you want more food sent to you?")
    pause
    $ msg ("Yes.", who=1)
    pause
    $ msg ("I know I shouldn’t but I already ate everything I have and I’m still hungry.", who=1)
    pause
    $ msg ("I’ll have some delivered to you.")
    pause
    $ msg ("Thanks.", who=1)
    pause
    $ hide_messenger()

    "You have a lot of food arranged to be delivered to Charlene and you then get back to trying to help Luna."
    "It’s likely going to take a lot of effort, but you apparently have plenty of support."

    $ lunastage10event2 = 0
    return


label Luna_Stage_11_Event:
    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Luna', dialogue=dialogue_one)
    $ msg ("Hey, looks like we will be able to get one final measurement and weigh-in for the test subjects before the project shuts down, they should at least have finished growing by now with the dosage that they got.", who=1)
    pause
    $ msg ("Okay, I’ll be right there.")
    pause
    $ hide_messenger()

    if recollection == False:
        $ luna.weight += 1
        $ britta.stage = 4
        $ natalie.stage = 4
        $ sally.stage = 4
        $ charlene.stage = 4
        $ roxie.stage = 4
    "Little does she know that the drug trial project is hopefully not shutting down, it isn’t a done deal yet, but you do have one very solid lead."
    "You were actually just about to try and call Luna to let her know about it, but since you are going to go see her anyway, you might as well just let her know in person."
    image luna_stage11_1 = "/luna/events/stage11/1.webp"
    scene luna_stage11_1
    "Upon getting to the hospital, you immediately look for Natalie."
    "By now you should be used to seeing a more and more busty and curvy Natalie every time you come here, but once again your mind is completely blown by just how huge she’s gotten."
    "Even from a distance it’s impossible not to notice those massive funbags of hers and they of course only seem to get bigger the closer you get to her."
    image luna_stage11_2 = "/luna/events/stage11/2.webp"
    scene luna_stage11_2
    "That being said, while her gigantic bosom now absolutely dominates her frame, the rest of her has clearly grown as well, it just can’t keep up with her enormous boobs."
    "She actually reminds you of Luna and Luna now has some serious competition."
    image luna_stage11_3 = "/luna/events/stage11/3.webp"
    scene luna_stage11_3
    "By the time Natalie finally notices you, you are already almost right up to her desk, but she smiles when she sees you, especially when she sees the way you are looking at her."
    "She seems to fully enjoy the attention that you are giving her and seems happy to just allow you to look as much as you want, which is good because you can’t help but stare at her anyway."
    image luna_stage11_4 = "/luna/events/stage11/4.webp"
    scene luna_stage11_4
    natalie "You like?"
    pc "Uh yeah…I mean I don’t even know what to say, I mean you’ve gotten just so…"
    natalie "Busty?"
    pc "Well yeah, but I was going to say just absolutely, ridiculously gorgeous although you were of course gorgeous before."
    image luna_stage11_5 = "/luna/events/stage11/5.webp"
    scene luna_stage11_5
    "It’s a compliment you’ve given to her before but you know it’s one Natalie loves hearing and she blushes once again at hearing it."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage11/vid1.webm" loop
    show movie with dissolve
    natalie "Thanks! I worked really hard to get them and the rest of me this huge, especially this last stage of the breast growth drug before it ran out."
    natalie "With the drug trial ending I figured I should try and take as much advantage as I could when I had the chance."
    natalie "I also figured with it ending and Luna no longer working here you wouldn’t really have much reason to come by and visit me here…so I wanted to give you 2 extra large reasons to visit."
    "Hopefully it won’t need to shut down, but even if it did, you can still see yourself coming by a lot anyway."
    pc "You didn’t need to worry about that, I would still find reasons to visit you no matter what, I love getting to see you."
    stop movie
    image luna_stage11_6 = "/luna/events/stage11/6.webp"
    scene luna_stage11_6
    natalie "Me too! Whatever day you come visit is the highlight of that day for me. I also especially like the times when you measure me and feel me up, it makes me feel so good."
    pc "I’m glad I make you feel that way, I’m definitely looking forward to that today."
    natalie "Well let’s go then!"
    image luna_stage11_7 = "/luna/events/stage11/7.webp"
    scene luna_stage11_7
    "Natalie walks up to you, your eyes unable to prevent themselves from staring at the massive weights on her chest."
    "They must be really heavy by now, especially when moving around but Natalie shows no sign of them bothering her, instead she just continues to enjoy the attention that you are giving her."
    image luna_stage11_8 = "/luna/events/stage11/8.webp"
    scene luna_stage11_8
    "As she walks past you, you get a good look then at her huge butt, while not as noticeable as her gigantic boobs, her butt and hips also now look incredible."
    "Natalie also seems to realize the attention that you are giving that part of her body as well."
    image luna_stage11_9 = "/luna/events/stage11/9.webp"
    scene luna_stage11_9
    natalie "You like my hips and butt as well?"
    pc "Yes! Though to be fair I don’t think there is any part of your body I don’t like, I just can’t stop staring at you."
    natalie "Mmm, well stare at me all you like."
    pc "Oh I will, thank you for the generous offer, much like how all of you is quite generous now."
    natalie "Haha, yeah."
    image luna_stage11_10 = "/luna/events/stage11/10.webp"
    scene luna_stage11_10
    "Upon getting to the research lab, you find everyone else once again waiting for you and once again you are stunned by just how much each of them has grown."
    "Is this really just from one dose of the drug each?"
    "To be fair though each of them ate pretty much everything they could for the entire drug trial to achieve maximum results, but still, the results were quite impressive."
    "So much eye candy of massive boobs, very curvy thick hips, and at least in Charlene’s case a quite nice great big tummy, although she clearly doesn’t seem happy about it.."
    "To be fair though nobody seems particularly happy and it isn’t hard to guess why."
    image luna_stage11_11 = "/luna/events/stage11/11.webp"
    scene luna_stage11_11
    luna "I guess this will be the last day of the drug trial unfortunately, even so you’ve all done so remarkably well and I couldn’t be prouder of each of you."
    roxie "We’re just proud to be part of it and we’re really, really going to miss you."
    "Most of the girls nodded their agreement except for Charlene, which was quickly noticed by Roxie."
    image luna_stage11_12 = "/luna/events/stage11/12.webp"
    scene luna_stage11_12
    roxie "Aren’t you sad about the drug trial ending Charly?"
    image luna_stage11_13 = "/luna/events/stage11/13.webp"
    scene luna_stage11_13
    charlene "Actually no, not at all, I mean I’m sad about Luna no longer going to be around, and I’m grateful that the drug probably prevented me from getting that disease I had to worry about,"
    charlene "but what I’m not happy about is all of this extra weight that I’ve gained!"
    image luna_stage11_14 = "/luna/events/stage11/14.webp"
    scene luna_stage11_14
    luna "I think the extra weight looks great on you."
    natalie "Oh definitely, it’s very nice, I don’t know why you are so worried about it."
    image luna_stage11_15 = "/luna/events/stage11/15.webp"
    scene luna_stage11_15
    charlene "I’m fat! Sure I’m now super healthy but I have all this extra weight now to lug around, I know the rest of you are going to say you like the extra curves, but I don’t."
    charlene "Besides none of you have this great big belly I now have."
    image luna_stage11_16 = "/luna/events/stage11/16.webp"
    scene luna_stage11_16
    luna "Mmm, I think you have a quite nice tummy, I’m actually rather jealous of it. Besides, think of how much more food you can now eat."
    image luna_stage11_17 = "/luna/events/stage11/17.webp"
    scene luna_stage11_17
    charlene "That’s the other problem I can’t seem to stop eating!"
    charlene "All I want to do is eat all the time and while I suppose that was necessary for the drug trial it’s going to be really hard to stop now and try to diet and exercise instead."
    image luna_stage11_18 = "/luna/events/stage11/18.webp"
    scene luna_stage11_18
    sally "Why stop now that the drug trial is ending? You really need to just give in and truly enjoy yourself and not worry what it does to your figure or better yet embrace it."
    sally "You’ll feel so much better and free to just indulge and enjoy yourself."
    image luna_stage11_19 = "/luna/events/stage11/19.webp"
    scene luna_stage11_19
    luna "Even with the drug used up you shouldn’t have to worry about any health problems due to your weight if that is an issue."
    image luna_stage11_20 = "/luna/events/stage11/20.webp"
    scene luna_stage11_20
    charlene "I will admit not having to worry about that is rather nice, but I mean being fat is…"
    image luna_stage11_21 = "/luna/events/stage11/21.webp"
    scene luna_stage11_21
    luna "Beautiful."
    image luna_stage11_22 = "/luna/events/stage11/22.webp"
    scene luna_stage11_22
    charlene "I don’t think most of society would agree with you unfortunately."
    image luna_stage11_23 = "/luna/events/stage11/23.webp"
    scene luna_stage11_23
    sally "Who cares what society thinks? Do what makes you happy, not them."
    sally "Besides I can tell you lots more guys and girls for that matter like my much curvier figure than you would think and they would probably think the same way about you."
    pc "I’m of the opinion that a lot more guys are into big girls than you would think, they just are scared to admit it due to society telling them what they should think."
    image luna_stage11_24 = "/luna/events/stage11/24.webp"
    scene luna_stage11_24
    charlene "Yes but I don’t really care what guys think about me either including you."
    image luna_stage11_25 = "/luna/events/stage11/25.webp"
    scene luna_stage11_25
    natalie "I don’t care what other guys think about me either, sure I get lots of attention now, but the only male attention I really want is from him, and I love the way that he looks at me now."
    image luna_stage11_26 = "/luna/events/stage11/26.webp"
    scene luna_stage11_26
    charlene "I think you are too focused on just what one guy thinks of you."
    image luna_stage11_27 = "/luna/events/stage11/27.webp"
    scene luna_stage11_27
    natalie "That guy happens to be the kindest, sweetest, best guy I’ve ever met and it would do you some good to actually try and get to know him so you can finally realize not all guys are so bad."
    image luna_stage11_28 = "/luna/events/stage11/28.webp"
    scene luna_stage11_28
    sally "He’s also quite good for sex, speaking of which some sex I think would really do you some good Charly, you are way too uptight and stressed, you would feel so much better, trust me."
    image luna_stage11_29 = "/luna/events/stage11/29.webp"
    scene luna_stage11_29
    charlene "Never going to happen!"
    image luna_stage11_30 = "/luna/events/stage11/30.webp"
    scene luna_stage11_30
    "Whatever might have happened next however was stopped with Luna getting a phone call and then answering it."
    image luna_stage11_31 = "/luna/events/stage11/31.webp"
    scene luna_stage11_31
    "After a brief conversation where you can’t hear what is being said, Luna stops talking on the phone to explain herself:"
    image luna_stage11_32 = "/luna/events/stage11/32.webp"
    scene luna_stage11_32
    luna "Excuse me, I’d better take this. I guess you can start without me because it might take awhile."
    "Luna then leaves."
    image luna_stage11_33 = "/luna/events/stage11/33.webp"
    scene luna_stage11_33
    britta "Well we should probably get started then with final measurements and weigh-ins, I’ll go first."
    image luna_stage11_34 = "/luna/events/stage11/34.webp"
    scene luna_stage11_34
    "At that, you follow Britta over to the room next door."
    image luna_stage11_35 = "/luna/events/stage11/35.webp"
    scene luna_stage11_35
    "She quickly strips and shows off her body to you."
    image luna_stage11_36 = "/luna/events/stage11/36.webp"
    scene luna_stage11_36
    britta "I can’t seem to stop examining and admiring my own body and how much it’s grown, especially my breasts."
    pc "I don’t blame you with a body like yours."
    image luna_stage11_37 = "/luna/events/stage11/37.webp"
    scene luna_stage11_37
    britta "Ooh I can’t wait to find out what my measurements are now and how physically successful the drug trial was for me."
    pc "Let’s find out then."
    image luna_stage11_38 = "/luna/events/stage11/38.webp"
    scene luna_stage11_38
    "You get first her weight and then her measurements, taking the opportunity to touch parts of her body as you do so. Also knowing her appreciation for numbers you give her the exact numbers."
    image luna_stage11_39 = "/luna/events/stage11/39.webp"
    scene luna_stage11_39
    window hide
    pause
    image luna_stage11_40 = "/luna/events/stage11/40.webp"
    scene luna_stage11_40
    window hide
    pause
    image luna_stage11_41 = "/luna/events/stage11/41.webp"
    scene luna_stage11_41
    if persistent.imperial:
        pc "You now weigh 191.8 lbs, you have a 46.9 inch bust with a bra size of a 38I, you have a 29.2 inch waist, and 45.0 inch hips."
    else:
        pc "You now weigh 87 Kg, you have a 109.1 cm bust with a bra size of a 38I, you have a 74.2 cm waist, and 114.3 cm hips."
    britta "Do you have the list of what my starting measurements were at the beginning just after taking the drug?"
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage11/vid2.webm" loop
    show movie with dissolve
    if persistent.imperial:
        pc "Yes I have them here and you really did grow a lot. You’ve added 12.6 inches to your bust, exactly 2.2 inches to your waist, exactly 3.5 inches to your hips, and you’ve gained 41.9 lbs."
    else:
        pc "Yes I have them here and you really did grow a lot. You’ve added 32 cm to your bust, exactly 5.6 cm to your waist, exactly 8.9 cm to your hips, and you’ve gained 19 Kg."
    britta "Mmm well that does sound like quite a lot then in such a short amount of time, honestly hearing all those numbers sounds sexy to me too."
    pc "You’re definitely very sexy that’s for sure."
    britta "Thanks and yes I’m quite happy with the results and I certainly did grow a lot, even more so than I calculated, but I still feel like I need further testing on myself."
    pc "Well couldn’t you just take another dose like Luna did if you wanted?"
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage11/vid3.webm" loop
    show movie with dissolve
    britta "I could but with the project shutting down I won’t have access to the lab or any of my equipment to make sure everything going on in my body is safe."
    britta "I mean it should but you never know and as a scientist I couldn’t justify taking that kind of risk either on myself or anyone else."
    pc "Understandable."
    britta "If the drug’s development was still continuing I definitely would want to take a 2nd dose, first of all I love the changes to my body and would want to continue that."
    britta "I also see no better way to show the drug’s potential then using it further on myself as the creator of it, but that would all depend on if it really does continue."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage11/vid4.webm" loop
    show movie with dissolve
    "Britta now seemed pretty concerned"
    britta "I’ve been worrying about if this really is the end of the drug testing and development?"
    britta "It’s such a life changing drug and it deserves to be developed and used by as many women that want it. Also what am I going to do with my life now that I don’t have that to work on?"
    pc "I’d like to think you would find something else worthwhile of your time."
    pc "I’m really hoping that the phone call Luna got was from the investment group I had you talk to and explain about the science behind the drug, thank you for that by the way."
    "That was definitely something you were grateful to have Britta for."
    britta "You’re welcome. I hope that is indeed who Luna is talking to and that it is going well. Also thank you for working so hard to find an investor."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage11/vid5.webm" loop
    show movie with dissolve
    pc "Really I couldn’t have done it without all of you girls’ help."
    pc "Roxie and Sally helped me find some leads of people and companies I could try and contact."
    pc "Charlene proofread all of my emails and messages I sent out so I would not sound like a total clueless idiot in her words."
    pc "You were the one who could explain the science and medical stuff that I couldn’t begin to understand."
    pc "Natalie however was really helpful as well."
    pc "It turns out she’s really good at talking to other receptionists and secretaries and convincing them to give out the personal information of their bosses so I can contact them directly."
    pc "That’s how I got this one that I’m most hopeful for actually."
    britta "A true team effort then, I love it. You know I spent most of the drug’s development working alone so it’s been nice this last part to have others around."
    britta "Sure none of you can really help me with the science and medical stuff, but it’s nice to be supported in other ways."
    britta "All of you would check on me to see how I was doing, or drop off some food for me to eat while I was working."
    pc "You’re welcome and while the drug trial may be ending but I would like to try and continue to see each of you."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage11/vid6.webm" loop
    show movie with dissolve
    britta "Especially for sex?"
    pc "Well yes that certainly is a great incentive, but for other reasons too."
    britta "Can we have sex though? Sorry I’ve just been craving it since our first time and-"
    pc "Oh definitely."
    britta "Can we try 69? I just really want to try the sex position that’s also a number."
    pc "Sure we can try it."
    stop movie

    #(sex scene here)
    if persistent.nosexscene:
        scene black with dissolve
        "Britta and you have a good time."
    else:
        image luna_stage11_136 = "/luna/events/stage11/136.webp"
        scene luna_stage11_136
        "After both of you strip off your clothing, Britta has you lie down, your erect penis pointing straight up."
        "Britta happily grabs it in her hand, seeming to enjoy the feel of it as well as its size and shape."
        pc "I do recall you saying that you wanted to measure it? Am I also getting measured today?"
        "She looks at you with amusement."
        britta "Mmm, I did say that and I do, but I fear that it would also take away the mystery and my fantasies of its exact dimensions for me."
        britta "I want to keep that going for a while longer. For now there are other things that I want to study with you."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/sex7.webm" loop
        show movie with dissolve
        "She starts rubbing her hand up and down your penis."
        britta "I just want to get it nice and ready first."
        pc "Oh it’s plenty ready."
        britta "I think so too, but we ought to test it out real quick just to be sure."
        stop movie
        image luna_stage11_138 = "/luna/events/stage11/138.webp"
        scene luna_stage11_138
        "Britta gets on top of you, guiding herself onto your penis until she fully impales herself on to it."
        britta "Ooh yeah, it’s definitely ready."
        image luna_stage11_139 = "/luna/events/stage11/139.webp"
        scene luna_stage11_139
        "She didn’t need to check, but Britta couldn’t seem to resist having you inside her once again."
        "She however quickly pulls you out of her."
        britta "Want to check my labia and vulva now?"
        pc "Of course."
        image luna_stage11_135 = "/luna/events/stage11/135.webp"
        scene luna_stage11_135
        "She turns around and positions herself so her slit is directly in front of your face."
        image luna_stage11_137 = "/luna/events/stage11/137.webp"
        scene luna_stage11_137
        "She then lowers herself down further as you then stick out your tongue and start to lick at her folds."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/sex9.webm" loop
        show movie with dissolve
        britta "Ooh, this feels different…but so, so good!"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/sex8.webm" loop
        show movie with dissolve
        "You continue to lick or start to suck and Britta starts moving up and down and moaning at the pleasure you are giving her."
        britta "Your turn for some pleasure."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/sex10.webm" loop
        show movie with dissolve
        "She moves her head downward onto your penis and pops it into her mouth and begins furiously sucking and bobbing her head up and down it."
        "You can taste for yourself just how wet she is getting and she is reciprocating the pleasure given by really going all out with your penis."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/sex11.webm" loop
        show movie with dissolve
        "The pressure begins to build and with your mouth still busy with Britta’s nether regions it is hard to warn her."
        stop movie
        image luna_stage11_140 = "/luna/events/stage11/140.webp"
        scene luna_stage11_140
        "You can’t hold it however and let loose inside of Britta’s mouth and she doesn’t seem able to contain it all as some of your cum gets onto her face."
        pc "Sorry."
        image luna_stage11_141 = "/luna/events/stage11/141.webp"
        scene luna_stage11_141
        britta "Don’t be sorry, that’s delicious! Definitely my new favorite snack."
        britta "Maybe if the drug trial does indeed have to shut down I can work on making a cum flavored snack."
        pc "I can admittedly see people buying it."
        britta "Especially if it actually tastes like yours."
        britta "Anyway we will definitely have to study more on how to 69 in the future."
        pc "For sure."
        "The two of you then get dressed."

    image luna_stage11_42 = "/luna/events/stage11/42.webp"
    scene luna_stage11_42
    britta "Well I’m sure I’ve kept the others waiting long enough, I’ll see you when I see you then."
    pc "Sure, sounds great."
    image luna_stage11_43 = "/luna/events/stage11/43.webp"
    scene luna_stage11_43
    "Britta gets dressed and then leaves with Sally coming in after that."
    image luna_stage11_44 = "/luna/events/stage11/44.webp"
    scene luna_stage11_44
    sally "You certainly seem to be now popular with the ladies, I really had to fight to be next."
    pc "You didn’t need to fight, but I’m glad that I’m thought of so highly."
    image luna_stage11_45 = "/luna/events/stage11/45.webp"
    scene luna_stage11_45
    sally "I just really wanted to get to you before the other girls could have you and wear you out."
    image luna_stage11_46 = "/luna/events/stage11/46.webp"
    scene luna_stage11_46
    sally "That being said, are you already worn out from having sex with Britta again? I’m assuming that’s why you and her took so long."
    pc "Um well yes."
    image luna_stage11_47 = "/luna/events/stage11/47.webp"
    scene luna_stage11_47
    sally "I don’t mind as long as you saved enough of your energy and enough of your cum for me, ready to take this huge fat ass of mine to pound town?"
    pc "I’m certainly not saying no, quite the opposite but we should probably get your weight and measurements first. Then I’m happy to take you to pound town as you put it."
    image luna_stage11_48 = "/luna/events/stage11/48.webp"
    scene luna_stage11_48
    sally "Sounds great, you also know how I want it, I want a nice good and fast pounding and then I get to go eat a ton of food afterwards. Would you know if I’ll still continue to get money for food?"
    pc "Unfortunately I don’t think so with this being the end of the drug trial."
    image luna_stage11_49 = "/luna/events/stage11/49.webp"
    scene luna_stage11_49
    sally "What? Well that’s disappointing, well I don’t care, I’m still going to keep eating like I have been anyway."
    sally "It will just be harder without all the extra money for food I was getting as part of the drug trial. Maybe I should start selling pictures and videos of myself online for extra money."
    pc "You can certainly try, I’ve heard that some women make a lot of money doing that as long as they are okay showing off their bodies which I’m sure is not a problem for you."
    image luna_stage11_50 = "/luna/events/stage11/50.webp"
    scene luna_stage11_50
    sally "Nope, and I figure this huge fat ass of mine is going to be a real moneymaker. Don’t worry though, you can have it for free."
    pc "How very generous of you. Well, let's get your weight and measurements then."
    image luna_stage11_51 = "/luna/events/stage11/51.webp"
    scene luna_stage11_51
    "You measure each part of Sally’s body and then tell her the results, including the total results throughout the drug trial."
    image luna_stage11_52 = "/luna/events/stage11/52.webp"
    scene luna_stage11_52
    window hide
    pause
    image luna_stage11_53 = "/luna/events/stage11/53.webp"
    scene luna_stage11_53
    window hide
    pause
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage11/vid7.webm" loop
    show movie with dissolve
    if persistent.imperial:
        pc "You now weigh 229.2 lbs, you have a 48.1 inch bust and need a 38J bra, you have a nearly 35 inch waist, and 56 inch hips."
        pc "In total for the drug trial, you’ve gained 66.1 lbs, added around 12 and a half inches to your bust, around 9 inches to your waist, and 16 and a half inches to your hips."
    else:
        pc "You now weigh 104 Kg, you have a 122.1 cm bust and need a 38J bra, you have a nearly 88.9 cm waist, and 142.2 cm hips."
        pc "In total for the drug trial, you’ve gained 30 Kg, added nearly 32 cm to your bust, around 23 cm to your waist, and 42 cm to your hips."
    sally "I’ve gotten to be a big girl haven’t I? Are you ready to show me how much you like big girls?"
    pc "Oh definitely."
    stop movie

    #(potential sex scene here)
    if persistent.nosexscene:
        scene black with dissolve
        "Sally and you had a good time."
    else:
        image luna_stage11_54 = "/luna/events/stage11/54.webp"
        scene luna_stage11_54
        "Having also spent time feeling up Sally’s body while you measured her and being plenty horny yourself."
        "You don’t even bother with more foreplay and just get behind Sally and her great big butt and try entering her."
        pc "It’s definitely a bit harder to do this than it was last time."
        sally "That’s just because there is just more ass in the way, ooh but fortunately there is plenty of your dick to get past it and into me."
        image luna_stage11_55 = "/luna/events/stage11/55.webp"
        scene luna_stage11_55
        "She was of course right as you entered her and pushed deeper in."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/sex1.webm" loop
        show movie with dissolve
        window hide
        pause
        sally "Ooh that’s right, give it to me! Pound into me!"
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/sex2.webm" loop
        show movie with dissolve
        window hide
        pause
        "You are more than happy to oblige as you pound hard into her, giving it to her fast and rough."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/sex3.webm" loop
        show movie with dissolve
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/sex4.webm" loop
        show movie with dissolve
        window hide
        pause
        "You enjoy the way her body moves and jiggles as you do so."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/sex5.webm" loop
        show movie with dissolve
        window hide
        pause
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/sex6.webm" loop
        show movie with dissolve
        window hide
        pause
        "It isn’t long before the pressure begins to build up and you let loose and cum deep inside her."
        stop movie
        image luna_stage11_56 = "/luna/events/stage11/56.webp"
        scene luna_stage11_56
        window hide
        pause

    image luna_stage11_57 = "/luna/events/stage11/57.webp"
    scene luna_stage11_57
    sally "Mmm, yes, that’s what I needed. Even with this drug trial ending, you’ll still come back and see me to have sex a lot won’t you?"
    pc "Of course I will, you’re going to keep growing and adding to this huge butt of yours and the rest of you aren’t you?"
    sally "Definitely, I see no reason to stop so there will be more and more delicious food to eat and more of me to enjoy."
    image luna_stage11_58 = "/luna/events/stage11/58.webp"
    scene luna_stage11_58
    "Sally gets dressed and leaves."
    image luna_stage11_59 = "/luna/events/stage11/59.webp"
    scene luna_stage11_59
    "Surprisingly it is actually Charlene that is next."
    image luna_stage11_60 = "/luna/events/stage11/60.webp"
    scene luna_stage11_60
    play music "/music/charlene.ogg" if_changed
    charlene "Natalie and Roxie let me go first."
    pc "Well Luna isn’t back yet to measure you."
    image luna_stage11_61 = "/luna/events/stage11/61.webp"
    scene luna_stage11_61
    charlene "I know, actually I was thinking maybe this time…I would let you do it?"
    "You are definitely surprised by that."
    pc "Are you sure?"
    "She seemed to hesitate for a moment but still agreed."
    image luna_stage11_62 = "/luna/events/stage11/62.webp"
    scene luna_stage11_62
    charlene "Yes, I’ve been thinking and um…I know how highly the other girls think of you…and I’ve been thinking maybe I haven’t given you enough of a chance."
    charlene "I would really like to be proven wrong about guys…at least in your case."
    pc "That’s certainly something that I’m glad that you want and I hope that I don’t let you down but you don’t have to get naked in front of me if you don’t want to just for that."
    image luna_stage11_63 = "/luna/events/stage11/63.webp"
    scene luna_stage11_63
    charlene "I’m guessing it’s just because you don’t want to look at my naked ugly, fat body?"
    pc "Oh no, that’s not it at all, you’ve got a beautiful body."
    image luna_stage11_64 = "/luna/events/stage11/64.webp"
    scene luna_stage11_64
    "Charlene doesn’t seem convinced by your compliment."
    charlene "I’m not sure how you would think that, but I guess I’ll show you anyway."
    image luna_stage11_65 = "/luna/events/stage11/65.webp"
    scene luna_stage11_65
    "She somewhat nervously takes off all of her clothes and then stands naked in front of you."
    image luna_stage11_66 = "/luna/events/stage11/66.webp"
    scene luna_stage11_66
    charlene "Well?"
    pc "Honestly, you have a very nice and attractive body."
    image luna_stage11_67 = "/luna/events/stage11/67.webp"
    scene luna_stage11_67
    charlene "Even this great big belly of mine?"
    pc "I think that’s the best and sexiest part of you."
    image luna_stage11_68 = "/luna/events/stage11/68.webp"
    scene luna_stage11_68
    charlene "You’re weird…but I will admit that I kind of like that you like me."
    pc "That’s a big thing for you to admit that you like that a man likes you."
    image luna_stage11_69 = "/luna/events/stage11/69.webp"
    scene luna_stage11_69
    charlene "Well maybe I really have grown as a person in other ways besides physically, probably slower than you would like as I’m still a total bitch."
    pc "You have been difficult to get along with, but I still just wish I could make you feel better about yourself and your life."
    image luna_stage11_70 = "/luna/events/stage11/70.webp"
    scene luna_stage11_70
    "Charlene looks at you as if unsure what to think of you now or what to say."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage11/vid8.webm" loop
    show movie with dissolve
    charlene "So you think like the others I should try to let loose and enjoy myself more?"
    pc "I think it could help."
    charlene "The problem is I kind of did that when it came to food during the drug trial."
    charlene "All of my problems I seemed to just forget about while I was eating."
    charlene "Food has become a coping mechanism for me and my problems, and that’s why I feel bad about how much food I keep eating and how fat I keep getting."
    pc "Well that’s certainly not good to be trying to bury all of your feelings and problems, but you shouldn’t worry about how much food you are eating or how fat you are getting, you look great."
    charlene "Thank you…and thank you for talking to me, I do feel better."
    pc "You’re welcome, so then are you sure you are okay with me measuring you?"
    charlene "Yes, I’m okay…I also realize that you might be unable to avoid touching me, but please do try to avoid it if possible."
    pc "Will do, I’ll try my best."
    stop movie
    image luna_stage11_71 = "/luna/events/stage11/71.webp"
    scene luna_stage11_71
    "Unlike the other girls you do your best not to touch Charlene as much as possible, despite the part of your brain desperately wanting to."
    image luna_stage11_72 = "/luna/events/stage11/72.webp"
    scene luna_stage11_72
    pause
    image luna_stage11_73 = "/luna/events/stage11/73.webp"
    scene luna_stage11_73
    "After getting her weight and measurements, you tell her the results:"
    if persistent.imperial:
        pc "You now weigh 260 lbs, you have a more than 46 inch bust and need a 38H bra, you have a more than 41 inch waist, and have more than 49 and a half inch around hips."
        pc "In total through the drug trial you’ve gained 88.2 lbs, added nearly 9 inches to your bust, 15 inches to your waist, and 11 inches to your hips."
    else:
        pc "You now weigh 118 Kg, you have a more than 116 cm bust and need a 38H bra, you have a more than 104 cm waist, and have more than 125 and a half cm around hips."
        pc "In total through the drug trial you’ve gained 40 Kg, added more than 22 cm to your bust, 38.1 cm to your waist, and 28 cm to your hips."
    image luna_stage11_74 = "/luna/events/stage11/74.webp"
    scene luna_stage11_74
    "Charlene however did not seem pleased by the results as she started crying."
    charlene "I just can’t believe how big and fat I’ve gotten."
    pc "Also incredibly beautiful."
    image luna_stage11_75 = "/luna/events/stage11/75.webp"
    scene luna_stage11_75
    "You instinctively reach out to comfort her and she surprisingly hugs you back as she cries against you."
    "You however quickly realize that she is still naked and that you are touching her, nowhere particularly sexual, just her back, but still you pull away from her."
    image luna_stage11_76 = "/luna/events/stage11/76.webp"
    scene luna_stage11_76
    pc "Sorry."
    charlene "It’s okay I um…didn’t mind, it was actually kind of nice being held by you."
    pc "Okay, that’s good, I just was worried."
    image luna_stage11_77 = "/luna/events/stage11/77.webp"
    scene luna_stage11_77
    charlene "I just don’t understand how you can be so nice to me when all I’ve been is a total bitch to you or be attracted to me when I’ve gotten this fat?"
    pc "I don’t know, maybe I’m just a good person and a fat admirer?"
    image luna_stage11_78 = "/luna/events/stage11/78.webp"
    scene luna_stage11_78
    charlene "Well you clearly are a lot better of a guy than I gave you credit for at least, I’m sorry for the way I treated you."
    pc "I hope I at least made you realize not all guys are horrible."
    charlene "You did do that, it makes me now wish we had more time for me to really try and get to know you."
    charlene "But even if by some miracle the drug trial continues I will not be participating so I guess this is probably goodbye."
    pc "Goodbye then."
    image luna_stage11_79 = "/luna/events/stage11/79.webp"
    scene luna_stage11_79
    "Charlene gets dressed and then leaves."
    image luna_stage11_80 = "/luna/events/stage11/80.webp"
    scene luna_stage11_80
    play music "/music/natalie.ogg" if_changed
    "The next girl to come in is Natalie."
    image luna_stage11_81 = "/luna/events/stage11/81.webp"
    scene luna_stage11_81
    natalie "My turn finally! I’ve been wanting to be nice and let others go first, partially because I don’t want to keep them waiting when I want to spend more time with you."
    natalie "It seems they are all taking a long time with you today."
    pc "Yeah, sorry about that, we’ve gotten to talking or um…doing other things."
    natalie "You mean having sex?"
    pc "Well in Britta’s and Sally’s case yes."
    natalie "It’s fine I don’t mind, actually looking forward to hearing all about it from them and how it went later. For now though I want you to enjoy feeling up my body and how much it’s grown."
    image luna_stage11_82 = "/luna/events/stage11/82.webp"
    scene luna_stage11_82
    "She then takes off all of her clothes, allowing you to look over and then touch all of her as much as you want, with Natalie happily enjoying the attention you are giving her."
    image luna_stage11_83 = "/luna/events/stage11/83.webp"
    scene luna_stage11_83
    "She then takes off all of her clothes, allowing you to look over and then touch all of her as much as you want, with Natalie happily enjoying the attention you are giving her."
    image luna_stage11_84 = "/luna/events/stage11/84.webp"
    scene luna_stage11_84
    "You feel up and lift her huge breasts, touch her belly, and squeeze each of her delicious butt cheeks."
    image luna_stage11_85 = "/luna/events/stage11/85.webp"
    scene luna_stage11_85
    "You feel up and lift her huge breasts, touch her belly, and squeeze each of her delicious butt cheeks."
    image luna_stage11_86 = "/luna/events/stage11/86.webp"
    scene luna_stage11_86
    natalie "Mmm, that feels so good and it just feels better and better the bigger that I get too."
    image luna_stage11_87 = "/luna/events/stage11/87.webp"
    scene luna_stage11_87
    "You get her weight and then all of her measurements and you let her know what they are as well as her total results."
    image luna_stage11_88 = "/luna/events/stage11/88.webp"
    scene luna_stage11_88
    window hide
    pause
    image luna_stage11_89 = "/luna/events/stage11/89.webp"
    scene luna_stage11_89
    if persistent.imperial:
        pc "You now weigh 198.4 lbs, you now have a more than 50 inch bust and need a 36N bra, you have a nearly 32 inch waist, and 49 inch hips."
        pc "In total you’ve gained 57.3 lbs, you’ve added 17 inches to your bust, 8 inches to your waist, and more than 7 inches to your hips."
    else:
        pc "You now weigh 90 Kg, you now have a more than 127 cm bust and need a 36N bra, you have a nearly 81.3 cm waist, and more than 124 cm hips."
        pc "In total you’ve gained 26 Kg, you’ve added nearly 43.2 cm to your bust, more than 20 cm to your waist, and about 19 cm to your hips."
    natalie "That’s certainly a lot more than I ever dreamed that I would grow originally, I mean just look how huge these things have gotten."
    image luna_stage11_90 = "/luna/events/stage11/90.webp"
    scene luna_stage11_90
    "She lifts up her huge boobs."
    natalie "I mean I'm an L-cup now, isn’t that crazy?"
    natalie "No way I’m finding that size in a regular store."
    natalie "My breasts are incredibly heavy, and I get constant attention now everywhere I go, and I am constantly needing to stop and milk myself…all that being said though I love them and the rest of me."
    pc "Me too."
    image luna_stage11_91 = "/luna/events/stage11/91.webp"
    scene luna_stage11_91
    natalie "I love the thrill of trying to outgrow each bra size I wear and make my way down the alphabet."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage11/vid9.webm" loop
    show movie with dissolve
    natalie "I love how heavy they are as a constant reminder of just how huge they are and how they are all mine."
    natalie "I absolutely love the attention you give them and the rest of me, and then I especially like how much milk I am producing because it means I can help a lot of people get healthier from my milk."
    pc "I’m really glad that you are happy."
    natalie "I am happy and yet sad that it’s over, I just wish I could keep gaining and growing."
    pc "You aren’t the only one to say that. If the project really doesn’t shut down maybe you could take a 2nd dose if you wanted?"
    natalie "I would like to if I can, I’m sure you would like that as well."
    pc "I’m not going to lie, I would love to see that."
    stop movie
    image luna_stage11_92 = "/luna/events/stage11/92.webp"
    scene luna_stage11_92
    natalie "Well I guess we'll just have to wait and see then."
    image luna_stage11_93 = "/luna/events/stage11/93.webp"
    scene luna_stage11_93
    "Natalie then leaves and Roxie then comes in."
    image luna_stage11_94 = "/luna/events/stage11/94.webp"
    scene luna_stage11_94
    stop music fadeout 1.0
    "Natalie then leaves and Roxie then comes in."
    image luna_stage11_95 = "/luna/events/stage11/95.webp"
    scene luna_stage11_95
    roxie "I was really hoping that Luna would be back by now."
    pc "I’m sure you were hoping that Luna would be the one to measure you again?"
    image luna_stage11_96 = "/luna/events/stage11/96.webp"
    scene luna_stage11_96
    roxie "Yes, no offense to you, but I was hoping that it would be Luna."
    roxie "Also if the project really does shut down and Luna is no longer my boss or will even be around, I was thinking this might be my last chance to try something with her. I’m really nervous though."
    pc "I say you just go for it, I’m pretty sure Luna would welcome it. She keeps talking about how sexy you’ve been getting and now are."
    image luna_stage11_97 = "/luna/events/stage11/97.webp"
    scene luna_stage11_97
    roxie "I keep thinking the same thing about Luna, she just keeps getting more and more sexy and irresistible to me and I want to be the same for her."
    pc "If it helps I don’t know how Luna or really anyone would be able to resist you, with those gorgeous green eyes of yours, those huge breasts, or that figure you now have."
    roxie "Mmm, thank you. Well since it seems I have no idea when Luna gets back how about you inspect my supposedly irresistible body over."
    image luna_stage11_98 = "/luna/events/stage11/98.webp"
    scene luna_stage11_98
    "At that Roxie then began stripping naked and then allowed you to take her weight and measurements."
    image luna_stage11_99 = "/luna/events/stage11/99.webp"
    scene luna_stage11_99
    "At that Roxie then began stripping naked and then allowed you to take her weight and measurements."
    image luna_stage11_100 = "/luna/events/stage11/100.webp"
    scene luna_stage11_100
    "Like all the other girls you get all of her measurements and weight and then let her know the results."
    image luna_stage11_101 = "/luna/events/stage11/101.webp"
    scene luna_stage11_101
    window hide
    pause
    image luna_stage11_102 = "/luna/events/stage11/102.webp"
    scene luna_stage11_102
    if persistent.imperial:
        pc "You now weigh 174.2 lbs, you have a more than 46.3 inch bust and need a 34L bra, have a 26 inch waist, and more than 43 and a half inch hips."
        pc "In total through the drug trial you’ve gained 39.7 lbs, added around 12 and a half inches to your bust, nearly 4 inches to your waist, and 6 inches to your hips."
    else:
        pc "You now weigh 79Kg, you have a more than 117.6 cm bust and need a 34L bra, have a 66 cm waist, and more than 110 cm hips."
        pc "In total through the drug trial you’ve gained 18 Kg, added around 31.7 cm to your bust, nearly 10.2 cm to your waist, and 15.2 cm to your hips."
    roxie "Not bad, more than enough attention to get Luna’s attention at least. I still can’t get over how my measurement taking with her last time went."
    pc "Yeah, that was hot."
    image luna_stage11_103 = "/luna/events/stage11/103.webp"
    scene luna_stage11_103
    roxie "For sure, it however just made me want her even more."
    pc "It made me want both of you even more."
    image luna_stage11_104 = "/luna/events/stage11/104.webp"
    scene luna_stage11_104
    roxie "Help me get Luna and you can have both of us at the same time."
    pc "That’s definitely a deal."
    image luna_stage11_105 = "/luna/events/stage11/105.webp"
    scene luna_stage11_105
    "Roxie then gets dressed and you go out with her to join the others, who seem to have just finished eating the last of the food."
    image luna_stage11_106 = "/luna/events/stage11/106.webp"
    scene luna_stage11_106
    pause
    image luna_stage11_107 = "/luna/events/stage11/107.webp"
    scene luna_stage11_107
    "Roxie sure didn’t look happy."
    roxie "You didn’t save me any?"
    image luna_stage11_108 = "/luna/events/stage11/108.webp"
    scene luna_stage11_108
    natalie "Sorry Roxie, there wasn’t much left when I got here either."
    sally "They didn’t bring us nearly enough food."
    image luna_stage11_109 = "/luna/events/stage11/109.webp"
    scene luna_stage11_109
    charlene "I’m sorry for eating so much, I just can’t seem to stop eating even with the drug trial over. I really need to get away from all of this food."
    image luna_stage11_110 = "/luna/events/stage11/110.webp"
    scene luna_stage11_110
    "Charlene then leaves in annoyance."
    image luna_stage11_111 = "/luna/events/stage11/111.webp"
    scene luna_stage11_111
    pc "Well I suppose with the drug trial ending maybe Luna didn’t see the need to order as much food. She also probably needs to worry more about finances now that she isn’t going to be working."
    image luna_stage11_112 = "/luna/events/stage11/112.webp"
    scene luna_stage11_112
    britta "Actually she ordered just as much food as usual, we all apparently can just eat way more than we could before. I guess we might all need to learn how to eat normal amounts of food again."
    image luna_stage11_113 = "/luna/events/stage11/113.webp"
    scene luna_stage11_113
    sally "Screw that, I’ll eat as much as I want."
    image luna_stage11_114 = "/luna/events/stage11/114.webp"
    scene luna_stage11_114
    roxie "I still wish you would have saved me some, I’m so hungry!"
    image luna_stage11_115 = "/luna/events/stage11/115.webp"
    scene luna_stage11_115
    "Luna then comes into the room with a big smile on her face."
    luna "Did I hear someone say that they were still hungry? Good thing I just ordered a lot more! I think we should celebrate!"
    pc "Wait…do you mean-?"
    image luna_stage11_116 = "/luna/events/stage11/116.webp"
    scene luna_stage11_116
    luna "YES! We just got a very, very sizable investment, far more actually than even I was hoping for."
    luna "We will have more than enough to not only continue the drug trials, but then go through the entire process, including all the way up to mass distribution to the public."
    luna "It will likely be years before we get that far, but the investor is fully committed to whatever help and support they can provide."
    image luna_stage11_117 = "/luna/events/stage11/117.webp"
    scene luna_stage11_117
    natalie "That’s awesome! Congratulations!"
    "Of course everyone else including you also chimed in to offer their congratulations as well."
    image luna_stage11_118 = "/luna/events/stage11/118.webp"
    scene luna_stage11_118
    "Luna couldn’t seem to stop smiling."
    luna "Of course I really couldn’t have done it without all of your help."
    luna "Volunteering to do the drug trials, and then I’m also told of the role each of you had in helping to get this investor, I owe each of you massive thanks."
    image luna_stage11_119 = "/luna/events/stage11/119.webp"
    scene luna_stage11_119
    roxie "You’re welcome Luna, we were more than happy to do it."
    image luna_stage11_120 = "/luna/events/stage11/120.webp"
    scene luna_stage11_120
    luna "However, I would like to give each of you more than just thanks."
    luna "Like I said we will have more than enough of the money we need and I mentioned to the investor how valuable each of you have been and they agree with me so…"
    luna "I would like to provide each of you with a generous amount of money for doing the drug trial and doing such a good job with it."
    luna "I still have to work out just how much I can afford to give each of you, but I want it to make it this whole experience more than financially worth it to you.."
    image luna_stage11_121 = "/luna/events/stage11/121.webp"
    scene luna_stage11_121
    natalie "You don’t have to do that Luna."
    sally "You still shouldn’t say no to free money if it’s offered to you though, thanks Luna."
    image luna_stage11_122 = "/luna/events/stage11/122.webp"
    scene luna_stage11_122
    luna "You’re very welcome."
    image luna_stage11_123 = "/luna/events/stage11/123.webp"
    scene luna_stage11_123
    sally "I don’t suppose if we were to say take another dose of the drug you would give us the same offer again would you?"
    image luna_stage11_124 = "/luna/events/stage11/124.webp"
    scene luna_stage11_124
    "Luna however just smiled."
    luna "Of course I’d love to have each of you take another dose of the drug."
    luna "It’s actually something me and the investor discussed about that possibility, and she said if any of you wanted to, she would be happy to help pay for that as well."
    image luna_stage11_125 = "/luna/events/stage11/125.webp"
    scene luna_stage11_125
    pc "Sounds like a really committed investor then."
    luna "Yes, very much so, it appears that we’ve all gotten very lucky."
    image luna_stage11_126 = "/luna/events/stage11/126.webp"
    scene luna_stage11_126
    britta "It would admittedly be very nice to study the continued effects of another dose on each of us and would only help in my research, assuming that each of you would be willing."
    image luna_stage11_127 = "/luna/events/stage11/127.webp"
    scene luna_stage11_127
    natalie "I’ll do it!"
    sally "Me too!"
    image luna_stage11_128 = "/luna/events/stage11/128.webp"
    scene luna_stage11_128
    roxie "I will!"
    image luna_stage11_129 = "/luna/events/stage11/129.webp"
    scene luna_stage11_129
    "All of the women didn’t seem to even need time to think about it, they immediately volunteered."
    "The only one apparently who didn’t want to take another dose was Charlene, which was totally understandable."
    "Considering just how food crazy she’s gotten, you have a strong feeling she won’t be able to help herself eating so much and avoid gaining a lot of weight anyway."
    image luna_stage11_130 = "/luna/events/stage11/130.webp"
    scene luna_stage11_130
    "Luna of course just smiled again, clearly very happy with all of them being so willing and likely already imagining the results…to be fair so are you."
    "If the girls are already as huge as they are, they will be just plain ridiculous with another dose."
    image luna_stage11_131 = "/luna/events/stage11/131.webp"
    scene luna_stage11_131
    "After all of the girls eat and take another dose of the drug, you and Roxie hatch a plan to seduce Luna…which you figure should be quite easy as you know by now what really turns Luna on."
    image luna_stage11_132 = "/luna/events/stage11/132.webp"
    scene luna_stage11_132
    "You and Roxie knock on Luna’s office door and Luna opens it for the both of you."
    image luna_stage11_133 = "/luna/events/stage11/133.webp"
    scene luna_stage11_133
    luna "Oh hi! I was just busy putting back the things I had already put away from my office."
    luna "I am glad I didn’t put away too much, seeing as how I’ll still need my office as head of the drug trial…thanks to you."
    "Luna gives you a big smile at that."
    pc "You’re welcome, but Roxie here helped too and she wants more than just your thanks as a reward."
    image luna_stage11_134 = "/luna/events/stage11/134.webp"
    scene luna_stage11_134
    "Luna seems amused by this."
    luna "Well Roxie, what did you have in mind as a reward then?"

    #(possible sex scene)
    image luna_stage11_142 = "/luna/events/stage11/142.webp"
    scene luna_stage11_142
    roxie "You, I want you. I simply can’t resist you anymore and I have to have you."
    image luna_stage11_143 = "/luna/events/stage11/143.webp"
    scene luna_stage11_143
    "Luna just smiled again."
    luna "You want me?"
    image luna_stage11_144 = "/luna/events/stage11/144.webp"
    scene luna_stage11_144
    roxie "Yes, I want all of you, those big, wide curvy hips of yours, that big belly, and those massive breasts and I’m going to have all of it."
    image luna_stage11_145 = "/luna/events/stage11/145.webp"
    scene luna_stage11_145
    "Luna decided to still have some fun with it."
    luna "I don’t know, are you sure you can handle all of me?"
    pc "That’s actually why I’m having to get Roxie involved now, you’ve gotten to be too much and too big for me to properly handle on my own."
    image luna_stage11_146 = "/luna/events/stage11/146.webp"
    scene luna_stage11_146
    luna "Mmm, is that so?"
    pc "Only problem is you also aren’t enough for both of us combined so we plan to fix that, we are both going to make sure there is a lot more of you, plenty for both of us to enjoy."
    luna "Mmm, and how do you plan to do that?"
    image luna_stage11_147 = "/luna/events/stage11/147.webp"
    scene luna_stage11_147
    "You and Roxie then reveal all the bags upon bags of food you had tried to hide, but with so much of it, Luna had likely already seen it."
    pc "We figure we can start by feeding you like you’ve never been fed before."
    roxie "Like stuffing that belly of yours so full of food it hurts. I want to see you with an absolutely huge, incredibly full belly for us to rub and admire."
    pc "With the only room left just barely enough for my penis to enter you."
    luna "I like the sound of that."
    pc "Good because you don’t really have a choice in the matter, your body and your belly is ours now to do what we want with."
    image luna_stage11_148 = "/luna/events/stage11/148.webp"
    scene luna_stage11_148
    roxie "In return you can have me and my body to do whatever you want with."
    luna "Oh, I can definitely think of a lot of things I want to do to you and your body."
    roxie "Great, well you can do whatever you want to me after you finish eating."
    image luna_stage11_149 = "/luna/events/stage11/149.webp"
    scene luna_stage11_149
    "Luna then gets out a vial of the stomach muscle relaxant to help her eat more and drinks it while you and Roxie start getting out food for her to eat."
    image luna_stage11_150 = "/luna/events/stage11/150.webp"
    scene luna_stage11_150
    "Luna also decides to strip naked, probably necessary if she doesn't want her clothes ripping with all the food you plan to stuff into her, and Roxie happily strips naked herself."
    image luna_stage11_151 = "/luna/events/stage11/151.webp"
    scene luna_stage11_151
    window hide
    pause
    image luna_stage11_152 = "/luna/events/stage11/152.webp"
    scene luna_stage11_152
    roxie "I figured I would give you some eye candy to look at while you eat."
    luna "I feel like even my eyes are going to get full then looking at you with all that eye candy you are presenting, you’ve gotten to be so gorgeous Roxie."
    roxie "Thank you, I did it in large part for you and I’m glad that it worked."
    luna "Oh it definitely did."
    image luna_stage11_153 = "/luna/events/stage11/153.webp"
    scene luna_stage11_153
    "Both women couldn’t resist going up and kissing each other, pressing their huge breasts against each other’s and running their hands over each other’s bodies."
    "You obviously quite enjoy watching, but after a moment of seeing this, you stop them momentarily."
    pc "Hold on, you can have some fun together after you’ve earned it, Luna you still need to finish eating all of this food."
    image luna_stage11_154 = "/luna/events/stage11/154.webp"
    scene luna_stage11_154
    "Both women broke apart, a bit disappointed, but now even more eager for more."
    luna "I guess you’re right, I have to earn having both of you of course, bring on the food!"
    image luna_stage11_155 = "/luna/events/stage11/155.webp"
    scene luna_stage11_155
    "No longer having to deal with the stress of keeping her job, Luna clearly is in a much better and a much hungrier mood than you have ever seen her as she eats with a passion and lust in her eyes."
    roxie "That’s right, my beautiful, big Luna, keep eating and giving us more of you to enjoy."
    "Luna just moans and keeps eating."
    image luna_stage11_156 = "/luna/events/stage11/156.webp"
    scene luna_stage11_156
    "Meanwhile you and Roxie trade off pressing food into Luna’s mouth while the other runs their hands along her naked body, especially her huge breasts and increasingly full belly."
    image luna_stage11_157 = "/luna/events/stage11/157.webp"
    scene luna_stage11_157
    roxie "Your belly is getting so big!"
    luna "You haven’t seen anything yet!"
    image luna_stage11_158 = "/luna/events/stage11/158.webp"
    scene luna_stage11_158
    "Luna keeps going at it with even more determination and both you and Roxie are amazed at just how massive her belly is getting."
    "It seems impossible just how beyond massive it is getting and yet Luna continues to press on, until it seems she can’t take anymore."
    image luna_stage11_159 = "/luna/events/stage11/159.webp"
    scene luna_stage11_159
    pc "Is that all you can take?"
    luna "How much food is left?"
    pc "Just a burger."
    luna "Give it to me!"
    image luna_stage11_160 = "/luna/events/stage11/160.webp"
    scene luna_stage11_160
    "You feed Luna the burger and she eats it, even as she strains to do so, finally however she manages to finish it."
    image luna_stage11_161 = "/luna/events/stage11/161.webp"
    scene luna_stage11_161
    luna "Oh! I’ve never felt so full!"
    roxie "I don’t know how you could manage to eat all that, your belly looks gigantic!"
    image luna_stage11_162 = "/luna/events/stage11/162.webp"
    scene luna_stage11_162
    "Luna looks down at her own now massive belly in amazement and can’t help but point out an interesting fact."
    luna "I can actually see it! It sticks out past my boobs now."
    pc "You probably haven’t even seen your belly much in some time huh with your boobs getting so huge."
    image luna_stage11_163 = "/luna/events/stage11/163.webp"
    scene luna_stage11_163
    luna "Nope, and I’ve missed it, oh it looks so gigantic and beautiful, this is like a dream come true seeing my belly like this."
    roxie "It’s a dream come true for me too."
    image luna_stage11_164 = "/luna/events/stage11/164.webp"
    scene luna_stage11_164
    luna "Yes, I’ve known for some time about your major crush on me and fortunately from now on you can have me whenever you want."
    roxie "Mmm, sounds great and in return you can have me whenever you want."
    roxie "I also meant it when I said that me and my body was all yours to do with as you want. I don’t care how big you make me or what you have me do, I’m all yours."
    luna "If that is really what you want then sounds amazing, for right now however I want to watch the two of you have sex while I recover a little, then both of you can have some fun with me."
    roxie "For sure."
    image luna_stage11_165 = "/luna/events/stage11/165.webp"
    scene luna_stage11_165
    "Roxie then looks at you with lust in her gorgeous green eyes."
    roxie "A deal is a deal after all, you helped me get Luna, and it’s a deal I’m happy to fulfill."
    image luna_stage11_166 = "/luna/events/stage11/166.webp"
    scene luna_stage11_166
    "The two of you lean in and kiss each other while you enjoy Roxie’s sexy body."
    "She may come to regret giving her body over to Luna in such a way, because you are sure there is going to be a lot more of her to enjoy in the future too."
    image luna_stage11_167 = "/luna/events/stage11/167.webp"
    scene luna_stage11_167
    "As you play with her now huge breasts, Roxie lets out a moan. She’s quite breast sensitive just like Luna."
    "Roxie also must surely be grateful to you and trying to fulfill her part of the deal or she is just really enjoying it because she happily gives in and gets into it as well."
    image luna_stage11_168 = "/luna/events/stage11/168.webp"
    scene luna_stage11_168
    pc "Are you ready?"
    roxie "Mmm, yes I’m ready, give it to me."
    if persistent.nosexscene:
        scene black with dissolve
        "Roxie, Luna and you had a good time."
    else:
        "The two of you face each other and you grab at your now full erection."
        image luna_stage11_169 = "/luna/events/stage11/169.webp"
        scene luna_stage11_169
        roxie "Wait, I want to do it."
        image luna_stage11_170 = "/luna/events/stage11/170.webp"
        scene luna_stage11_170
        "She grabs at your cock and starts guiding it into her."
        roxie "I haven’t had cock in quite awhile, and never anywhere near this big, but I’ll make it fit."
        image luna_stage11_171 = "/luna/events/stage11/171.webp"
        scene luna_stage11_171
        "As soon as you feel the tip at her entrance, you suddenly aren’t so sure it’s actually going to fit, it feels quite small and tight, but Roxie looks determined."
        "She slowly pulls you in deeper and deeper into her and you enjoy seeing her gorgeous green eyes widen even further at being filled so completely."
        "Her cunt walls are definitely pressing really hard against your cock."
        image luna_stage11_172 = "/luna/events/stage11/172.webp"
        scene luna_stage11_172
        roxie "I guess Luna isn’t the only one being totally filled up, wow that feels tight, but good though."
        pc "Yeah, you’re definitely the smallest and tightest I’ve ever had, are you ready for the rest?"
        image luna_stage11_173 = "/luna/events/stage11/173.webp"
        scene luna_stage11_173
        roxie "Wait rest?"
        "Roxie had stopped gripping the base of your cock, thinking it was already all the way in."
        pc "Yes, rest, there is still more to go."
        roxie "Oof, I’m really going to get filled up today huh, well bring it on!"
        image luna_stage11_174 = "/luna/events/stage11/174.webp"
        scene luna_stage11_174
        "You push all the way into her, again enjoying the satisfied but completely stuffed look on her face."
        pc "Are you okay?"
        roxie "Mmm, yes, like I said bring it on."
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/175.webm" loop
        show movie with dissolve
        window hide
        pause
        "You are forced to take it slower than normal in order to avoid hurting her and because she’s just that tight, even with her cunt walls adjusting to make room for all of you."
        "It however feels incredible and apparently Roxie is enjoying it too."
        roxie "Okay Luna I’m going to have to take it back a little, you can have me most of the time, but I definitely now realize I have to have this dick inside me again and again too."
        roxie "Wow it’s so much and yet feels so good!"
        luna "It really is great isn’t it? Also no problem, I think you need it and him sometimes too for sure, I know I’m sure going to need it myself."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/176.webm" loop
        show movie with dissolve
        window hide
        pause
        "You then continue to pound into Roxie, enjoying the feel of her tits pressing against your chest while they jiggle."
        "You can feel the pressure beginning to build."
        pc "I’m about to-"
        roxie "Let me have it! Fill me up even more!"
        stop movie
        image luna_stage11_177 = "/luna/events/stage11/177.webp"
        scene luna_stage11_177
        "You let loose, letting spurt after spurt deep inside her and then pulling out."
        image luna_stage11_178 = "/luna/events/stage11/178.webp"
        scene luna_stage11_178
        roxie "I definitely wasn’t expecting to like that so much, but now I’m definitely going to want more from now on."
        pc "Maybe I’ll get you as addicted to me as you are to Luna."
        roxie "You can try and I definitely want you to try but Luna is still going to always be number one for me."
        pc "Totally understandable, well how about you finally truly have your fun with Luna."
        roxie "Mmm, yes!"
        image luna_stage11_179 = "/luna/events/stage11/179.webp"
        scene luna_stage11_179
        "Roxie goes over to Luna and the two women start to truly enjoy each other, with you mostly content to rest and watch the two of them go at it."
        image luna_stage11_180 = "/luna/events/stage11/180.webp"
        scene luna_stage11_180
        "After a while however you go over and decide to get in on the fun."
        "Despite all the huge boobs you’ve seen and helped grow during the drug trial, Luna is still the reigning tit queen and you are sure Luna is going to do her best not to relinquish her throne."
        image luna_stage11_181 = "/luna/events/stage11/181.webp"
        scene luna_stage11_181
        "Your hands then drop down to feel her still totally gigantic belly, she truly outdid herself eating and growing this massive monster of a belly."
        "Luna finally had the belly she had been wanting."
        "It evidently still had just enough room in there though."
        image luna_stage11_182 = "/luna/events/stage11/182.webp"
        scene luna_stage11_182
        luna "Ooh I want you in me now, still covered in yours and Roxie’s cum."
        pc "Are you sure you can handle all of me in your state?"
        luna "I saved just barely enough room for you."
        image luna_stage11_183 = "/luna/events/stage11/183.webp"
        scene luna_stage11_183
        "You push up against her full tummy and then get your dick under it to enter her. It really is another tight squeeze."
        pc "I’m not sure who is tighter, you or Roxie."
        image luna_stage11_184 = "/luna/events/stage11/184.webp"
        scene luna_stage11_184
        roxie "I definitely like the comparison between me and Luna."
        pc "Well then I should warn you, me and Luna or going to make you even bigger than Luna is right now."
        "Roxie just smiles at that."
        roxie "Looking forward to it."
        image luna_stage11_185 = "/luna/events/stage11/185.webp"
        scene luna_stage11_185
        "You press deeper into Luna, amazed at how much Luna can take, but Luna just urges you on."
        luna "Give it to me!"
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/186.webm" loop
        show movie with dissolve
        window hide
        pause
        "You happily do so, pounding away into her, enjoying Luna’s huge body move as you do so, it’s so full and heavy, she doesn’t jiggle so much as rock about with all of her titanic curves."
        stop movie
        image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
        play movie "/images/luna/events/stage11/186.webm" loop
        show movie with dissolve
        window hide
        pause
        "As you pound away into her, you can’t help but think how great this is…and just how much better (and bigger) it’s going to get."
        "As both of you reach your climax, Luna tries to say something during all her moaning."
        luna "Cum... all over... my belly."
        stop movie
        image luna_stage11_188 = "/luna/events/stage11/188.webp"
        scene luna_stage11_188
        "You do as Luna asks and pull to cum all over her huge round gut."
    image luna_stage11_189 = "/luna/events/stage11/189.webp"
    scene luna_stage11_189
    "After cleaning up, You, Luna and Roxie say goodbye to each other."
    "You head home."
    if recollection == False:
        $ luna.weight += 1
        $ daytime += 1
        $ phonecall = 1
        #Unlocks Charlene Undress in the stats page.
        $ renpy.notify("Charlene Undress option unlocked in stats screen.")
        window hide
        pause
    $ lunastage11event = 0
    return

label Luna_Stage_12_Event:
    "You get a phone call."
    "It’s Luna!"
    image luna_stage12_1 = "/luna/events/stage12/1.webp"
    scene luna_stage12_1
    luna "Hey, do you have time to come over to my house?"
    luna "I need your help with something."
    pc "Sure, I’ll be right there."

    image luna_stage12_2 = "/luna/events/stage12/2.webp"
    scene luna_stage12_2
    "When you get to Luna’s house, she greets you with a big smile on her face."
    pc "You seem happy!"
    luna "Mmm, I am!"
    luna "Thanks to you."
    image luna_stage12_3 = "/luna/events/stage12/3.webp"
    scene luna_stage12_3
    "She goes and gives you a quick kiss."
    image luna_stage12_4 = "/luna/events/stage12/4.webp"
    scene luna_stage12_4
    pc "So what did you need my help with?"
    luna "First of all, what do you think of this new outfit?"
    image luna_stage12_5 = "/luna/events/stage12/5.webp"
    scene luna_stage12_5
    window hide
    pause
    image luna_stage12_6 = "/luna/events/stage12/6.webp"
    scene luna_stage12_6
    pc "It looks amazing on you!"
    image luna_stage12_7 = "/luna/events/stage12/7.webp"
    scene luna_stage12_7
    luna "Thanks! I actually got it from the investor."
    luna "They are a clothing company that caters to extra curvy or plus sized women called BBW Plus."
    pc "Yes, I remember that from when I was trying to find an investor for you."
    image luna_stage12_8 = "/luna/events/stage12/8.webp"
    scene luna_stage12_8
    luna "I honestly would never have thought of trying to get a clothing company of all companies to invest, but that truly was a genius idea."
    pc "It was actually Sally’s idea originally."
    pc "She buys some of their clothes."
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage12/luna_vid1.webm" loop
    show movie with dissolve
    luna "I’ve never worn anything from them before but I got to say I’m pretty impressed with the quality and comfort of their clothing as well as the reasonable prices and them catering to bigger women."
    luna "Which by the way in my experience is definitely not usual for the clothing and fashion industry."
    luna "I’ll be honest, I was a bit skeptical that a clothing company would want to invest in a drug, but from my talks with them, they just want what I want."
    luna "For women to feel like being bigger is beautiful, that they no longer need to try and hide or be ashamed of their size."
    luna "That instead they can embrace it and be proud of what they have, wearing clothes that show off their beautiful curves to the world."
    luna "Also even choosing to add to those curves, eating the foods they want to eat, no longer concerned with health problems or having to maintain a certain size."
    pc "It’s great they seem to share your vision."
    luna "Yes it is."
    luna "It also helps for them that widespread use of the drug will only cause women to gain more weight."
    luna "Which means they are going to continually need bigger clothes, and we will be advertising their clothing company right alongside the drug so they know where to go to get them."
    pc "That’s awesome! Congratulations for apparently finding such a great partner."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage12/luna_vid2.webm" loop
    show movie with dissolve
    luna "Yeah, I just finished signing the contract this morning."
    luna "I’ll be giving up 18 percent of the company and doing advertising for them, but I’m guaranteed all the financing I need for the drug trial to reach the market."
    luna "Everything will be generously covered, including helping with food and clothing costs for me and the other test subjects."
    luna "Money will no longer be a problem in reaching our goals."
    luna "I just received their first check and it was quite substantial."
    pc "That’s great! I’m glad it’s working out so well for you."
    luna "Yes, but money is going to be just one obstacle we no longer need to worry about, there is going to be a lot of work involved to achieve our end results."
    pc "I’m happy to help however I can and I’m sure the other test subjects would be more than happy to help as well."
    luna "I appreciate that. Having all of you help me in securing our funding means so much to me and made me realize that I can’t do it alone but that I have the support that I need."
    pc "Of course."
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage12/luna_vid3.webm" loop
    show movie with dissolve
    luna "Speaking of help, BBW Plus did however have one stipulation and that is what I need your help with."
    luna "They were aware of who I was and my background as a somewhat famous model and they felt that me modeling their clothes would really help their brand."
    luna "So as part of our deal I agreed to have some pictures taken wearing their clothes and send them to them."
    luna "I would really like you to take the pictures please."
    pc "Sure, but I should warn you that I’m definitely not a professional photographer or anything."
    luna "It’s okay, I can do the fancy editing stuff myself later, I just…"
    luna "I really wanted it to be you who does it, you’re the only person I think I would feel comfortable enough doing it."
    luna "I never dreamed I would ever end up modeling again, with my parents always forcing me to do it even from the time I was 4, I grew to hate and dread having to keep doing it."
    pc "I can imagine how hard that must have been for you growing up. I bet if you really don’t want to do it you could maybe-"
    stop movie
    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    play movie "/images/luna/events/stage12/luna_vid4.webm" loop
    show movie with dissolve
    luna "No, I want to do it, I want to be able to show women everywhere that being bigger and fatter can be beautiful."
    luna "That what the media and the fashion industry keeps saying is that you have to be a certain size to be beautiful or healthy is wrong."
    luna "I also want to be able to show off the physical effects the drug are having to the women of the world."
    luna "I want them to feel inspired to take the drug themselves when it becomes available, to enjoy better health, to eat as much or whatever they want."
    luna "I want them to feel beautiful and happy as they continue to gain weight and grow."
    luna "All that being said…I have to admit I’m nervous to be modeling again."
    luna "Maybe it’s just a few photos but…"
    pc "I can understand it’s still a really big deal to you to be doing it though."
    pc "I’ll of course be happy to help however I can."
    luna "Thank you. I’m really glad I have you to help me with this."
    pc "No problem and I’m glad I have you too."
    stop movie
    image luna_stage12_9 = "/luna/events/stage12/9.webp"
    scene luna_stage12_9
    luna "So why don’t we start with you taking some pictures of me in this outfit first."
    pc "Sure."
    image luna_stage12_10 = "/luna/events/stage12/10.webp"
    scene luna_stage12_10
    "Luna hands you a very nice looking camera and goes over the controls with you."
    image luna_stage12_11 = "/luna/events/stage12/11.webp"
    scene luna_stage12_11
    "She then goes and stands in front of you, adopting a certain pose."
    image luna_stage12_12 = "/luna/events/stage12/12.webp"
    scene luna_stage12_12
    "You do your best to take some good photos."
    image luna_stage12_13 = "/luna/events/stage12/13.webp"
    scene luna_stage12_13
    "Fortunately it helps that Luna has so much experience posing in front of a camera."
    image luna_stage12_14 = "/luna/events/stage12/14.webp"
    scene luna_stage12_14
    pc "You’re doing great!"
    image luna_stage12_15 = "/luna/events/stage12/15.webp"
    scene luna_stage12_15
    luna "Thanks, and you’re doing great too, but make sure you are getting plenty of photos that really show off my breasts well."
    pc "Considering just how wonderfully enormous your boobs have gotten, that shouldn’t be hard."
    image luna_stage12_16 = "/luna/events/stage12/16.webp"
    scene luna_stage12_16
    luna "I’m just saying, boobs can be real money makers when it comes to modeling."
    pc "If that is the case we might want to sell some of these photos ourselves and make you an instant billionaire."
    image luna_stage12_17 = "/luna/events/stage12/17.webp"
    scene luna_stage12_17
    luna "Mmm, probably not, but seeing how much the drug has made my breasts grow will definitely help sell the drug."
    pc "I’m sure it will."
    pc "How are you doing personally with doing this though?"
    image luna_stage12_18 = "/luna/events/stage12/18.webp"
    scene luna_stage12_18
    luna "It’s kind of fun doing this with you actually."
    luna "I was worried that this would just bring back painful memories, but just having you here makes it a lot easier and more comfortable for me."
    pc "I’m glad."
    image luna_stage12_19 = "/luna/events/stage12/19.webp"
    scene luna_stage12_19
    luna "I think that’s enough of me wearing this outfit, let’s try something else."
    image luna_stage12_20 = "/luna/events/stage12/20.webp"
    scene luna_stage12_20
    "Luna strips in front of you, not concerned about you watching, in fact she seems eager to see you watching as she changes into another outfit."
    image luna_stage12_21 = "/luna/events/stage12/21.webp"
    scene luna_stage12_21
    window hide
    pause
    image luna_stage12_22 = "/luna/events/stage12/22.webp"
    scene luna_stage12_22
    "You then start taking more photos while Luna adopts different poses."
    image luna_stage12_23 = "/luna/events/stage12/23.webp"
    scene luna_stage12_23
    luna "You know, it’s rather interesting the differences there are with me taking certain poses for when I was only half this size versus now."
    pc "I’ll bet. I’m sure it’s harder now versus back then."
    image luna_stage12_24 = "/luna/events/stage12/24.webp"
    scene luna_stage12_24
    luna "Yes, but I don’t mind, in fact I welcome it. It feels so sexy to me knowing that I’m now a big and very busty girl and it’s harder to do certain things."
    luna "Those certain things are only going to keep getting harder as I continue to grow and I’m going to enjoy experiencing every part of that rather than be too annoyed by it."
    image luna_stage12_25 = "/luna/events/stage12/25.webp"
    scene luna_stage12_25
    luna "Accidentally bumping into and knocking things over with my breasts."
    luna "Dealing with carrying around their increased weight."
    image luna_stage12_26 = "/luna/events/stage12/26.webp"
    scene luna_stage12_26
    luna "Continually outgrowing clothing and busting out of ever larger bras."
    luna "An entire alphabets’ worth of bras and beyond…"
    image luna_stage12_27 = "/luna/events/stage12/27.webp"
    scene luna_stage12_27
    luna "I want all of that."
    pc "And I’m going to enjoy watching you experience it and be there to help you when you need it."
    image luna_stage12_28 = "/luna/events/stage12/28.webp"
    scene luna_stage12_28
    luna "Mmm, I love you so much."
    pc "I love you too."
    image luna_stage12_29 = "/luna/events/stage12/29.webp"
    scene luna_stage12_29
    luna "I can’t wait to see where we go from here, with the drug trial and then it coming to market, my new partnership with the clothing company, and especially with our relationship."
    luna "It all seems really exciting to see where it all goes."
    pc "Me too, it will be very interesting to see how it all plays out."
    image luna_stage12_30 = "/luna/events/stage12/30.webp"
    scene luna_stage12_30
    "Looking at Luna, you can tell this begins the next step in an exciting journey with her."
    scene player_room
    "After you get back home you get a text from Sally."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Sally', dialogue=dialogue_one)
    $ msg ("So what kind of discounts and free clothes are we getting with this deal?", who=1)
    pause
    $ msg ("I don’t know, Luna handled the details.")
    pause
    $ msg ("You will have to ask her.")
    pause
    $ msg ("We better be getting plenty, why else would I have set you up with a clothing company to have invest in us?", who=1)
    pause
    $ msg ("Maybe because it’s a great opportunity for Luna.")
    pause
    $ msg ("Well yes that too, but nothing wrong with getting some benefits out of it.", who=1)
    pause
    $ msg ("Speaking of food and clothes, can you send me more food?", who=1)
    pause
    $ msg ("I need to outgrow all of my clothes.", who=1)
    pause
    $ msg ("Sure I can send you some food but why do you need to outgrow all your clothes?")
    pause
    $ msg ("So I have an excuse to go get more of course.", who=1)
    pause
    $ msg ("Using whatever I’m getting from Luna’s deal.", who=1)
    pause
    $ msg ("Again I’m not sure what the details are, you’ll have to ask Luna.")
    pause
    $ msg ("Or you could just get me this.", who=1)
    pause
    $ msg (None, pic="stage4_sally1")
    pause
    $ msg (None, pic="stage4_sally2")
    pause
    $ msg ("Wouldn’t you love seeing me in it?", who=1)
    pause
    $ msg ("Well yes, but-")
    pause
    $ msg ("Great! Then you will get it for me.", who=1)
    pause
    $ msg ("I might…but I’ll be getting too big of a size so you’ll need to grow into it.")
    pause
    $ msg ("Deal!", who=1)
    pause
    $ msg ("Send me the food to help me out with that then.", who=1)
    pause
    $ hide_messenger()

    "With Luna having gotten an investor you can now afford to provide the test subjects with even more food."
    "You arrange to have a lot of food delivered to Sally and the other test subjects."
    "You soon get a thank you text back from Roxie."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Roxie', dialogue=dialogue_one)
    $ msg ("Thanks for all the food!", who=1)
    pause
    $ msg ("I’m going to enjoy all of it!", who=1)
    pause
    $ msg ("You’re welcome.")
    pause
    $ msg ("By the way, I went out with some friends last night and convinced them to get a second dessert for dinner.", who=1)
    pause
    $ msg ("I know it’s just a little thing but I’m feeling a little proud of myself.", who=1)
    pause
    $ msg ("You should be.")
    pause
    $ msg ("Nice work, we’ll make you into an encourager and feeder yet.")
    pause
    $ msg ("I sure hope so.", who=1)
    pause
    $ msg ("Anyway I’m going to get to eating a solid dent in all this food you just sent me, so talk to you later.", who=1)
    pause
    $ msg ("Talk to you later.")
    pause
    $ hide_messenger()

    "You get some quick thank yous from the other test subjects."
    "You also get a follow up text from Natalie later on."

    $ show_messenger()

    $ dialogue_one = []

    $ switch_dialogue(name='Natalie', dialogue=dialogue_one)
    $ msg (None, pic="stage4_natalie")
    pause
    $ msg ("I think I might have overdid it on the food you sent me.", who=1)
    pause
    $ msg ("I kind of already ate it all.", who=1)
    pause
    $ msg ("You already ate all of it?")
    pause
    $ msg ("Yeah.", who=1)
    pause
    $ msg ("It’s just the thought that the food came from you and was sent with love makes me just want to eat more and more of it.", who=1)
    pause
    $ msg ("Sorry.", who=1)
    pause
    $ msg ("Oh no need to be sorry, I’ll just have to send you more tomorrow.")
    pause
    $ msg ("Do you have the money for that?", who=1)
    pause
    $ msg ("It should no longer be an issue, it looks like Luna was able to drastically increase the food budget for you girls.")
    pause
    $ msg ("Okay, that’s great to hear.", who=1)
    pause
    $ msg ("I really love getting food from you.", who=1)
    pause
    $ msg ("And I love sending it to you.")
    pause
    $ hide_messenger()

    "With the test subjects taken care of for now, it causes you to think of the test subject you no longer have, Charlene."
    "Perhaps you should check on her anyway?"
    menu:
        "Check on Charlene.":
            "You decide to check on her anyway as at the very least, Luna and Britta might find it helpful for their research to see how a test subject no longer on the drug responds to being off of it."
            "You send a text message to Charlene."

            $ show_messenger()

            $ dialogue_one = []

            $ switch_dialogue(name='Charlene', dialogue=dialogue_one)
            $ msg ("Hey, I just wanted to see how you are doing.")
            pause
            $ msg ("I’m fine.", who=1)
            pause
            $ msg ("You don’t need to check up on me anymore since I’m no longer a test subject.", who=1)
            pause
            $ msg ("I figured Luna and Britta might want to see how you are doing now that you are no longer on the drug.")
            pause
            $ msg ("Well I would have thought I wouldn’t have such an insatiable desire to eat all the time anymore.", who=1)
            pause
            $ msg ("You shouldn’t at least not because of the drug.")
            pause
            $ msg ("Then maybe it’s not the drug.", who=1)
            pause
            $ msg ("Maybe I need to accept that it’s me that is the problem.", who=1)
            pause
            $ msg ("Personally I feel like a girl who likes to eat isn’t really a problem.")
            pause
            $ msg ("Well it’s awkward now.", who=1)
            pause
            $ msg ("Last night I got out of a buffet.", who=1)
            pause
            $ msg ("Don’t judge.", who=1)
            pause
            $ msg ("I’m not.")
            pause
            $ msg ("Anyway I got out of a buffet and some lady asked me how far along I was.", who=1)
            pause
            $ msg ("I’m not pregnant!", who=1)
            pause
            $ msg ("I just have this big ole belly.", who=1)
            pause
            $ msg ("Nothing wrong with a big belly.")
            pause
            $ msg ("Of course in your case you probably just think me being mistaken for being pregnant because of my belly is hot.", who=1)
            pause
            $ msg ("Yeah kind of.")
            pause
            $ msg (None, pic="stage4_charlene1")
            pause
            $ msg ("If uh…you want to look at it and maybe even do some…things with it I wouldn’t mind.", who=1)
            pause
            $ msg ("I can send you some more even if you would like them.", who=1)
            pause
            $ msg ("Consider it an apology for how I’ve treated you.", who=1)
            pause
            $ msg ("Just don’t show them to anyone else or I’ll have to eat you.", who=1)
            pause
            $ msg ("Yeah um, if you want, and I promise I won’t show them to anyone else.")
            pause
            $ msg ("Okay thanks.", who=1)
            pause
            $ msg (None, pic="stage4_charlene2")
            pause
            $ hide_messenger()
        "Leave it.":
            "You decide not to bother as Charlene probably wouldn’t want to talk to you anyway."

    "DEV NOTE: This is Luna's final event in this update."

    if recollection == False:
        $ daytime += 1
        $ phonecall = 1
    $ lunastage12event = 0
    return
