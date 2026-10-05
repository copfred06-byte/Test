label daisy_home_feeding:
    menu:
        "Feed her more food.":
            $ final_food_capacity = (teacher.stomach_capacity * teacher.addiction_to_food)
            if foodheld <= 0:
                "You do not have anymore food with you to feed Daisy with."
                teacher "What else would you like to do?"
                menu:
                    "Want to work off some of that lethargy?":
                        if persistent.nosexscene == True:
                            "You have sex scenes disabled in preferences, now leaving daisy her home."
                            return
                        hide screen teacherfullness
                        call Daisy_Home_Sex from _call_Daisy_Home_Sex
                        return
                    "I think that will do it for me today.":
                        teacher "I was hoping for a little more, but I understand. Thank you very much for the food and feeding. Let's get this place cleaned up."
                        "After helping Daisy clean up, I say goodbye and head home."
                hide screen teacherfullness
                return
            elif final_food_capacity <= teacher.fullness:
                teacher "Hold on, I don't think I can take anymore. It feels like I'm about to burst."
                pc "Come on, we're almost there. Just one more bite."
                teacher "Alright, but this will probably do it for me."
                call rngeatingdaisyhome from _call_rngeatingdaisyhome
                window hide
                pause
                teacher "That really hit the spot."
                $ stuffed = 2
                "Her belly looks even bigger than before."
                image daisy_home_stuffed_full = "/teacher/[teacher.stage]/[stuffed]/home_stuffed_full.webp"
                scene daisy_home_stuffed_full
                $ teacher.fullness += 0.5
                $ foodheld -= 1
                return
            elif final_food_capacity <= (teacher.fullness * 2) and stuffed == 1:
                image daisy_home_stuffed_half = "/teacher/[teacher.stage]/[stuffed]/home_stuffed_half.webp"
                scene daisy_home_stuffed_half
                teacher "Pff, I feel so stuffed, but I want more food."
                call rngeatingdaisyhome from _call_rngeatingdaisyhome_1
                window hide
                pause
                image daisy_home_feeding_choice = "/teacher/[teacher.stage]/[stuffed]/home_feeding_choice.webp"
                scene daisy_home_feeding_choice
                $ teacher.fullness += 0.5
                $ foodheld -= 1
                jump daisy_home_feeding
            elif final_food_capacity <= (teacher.fullness * 2):
                teacher "I'm starting to reach my limits. If we keep going, I may not be able to do much else."
                menu:
                    "Let's keep going.":
                        teacher "I was hoping you would say that. Bring on the next serving."
                        call rngeatingdaisyhome from _call_rngeatingdaisyhome_2
                        window hide
                        pause
                        $ stuffed = 1
                        "Her belly starts to look bigger from all the food."
                        image daisy_home_feeding_choice = "/teacher/[teacher.stage]/[stuffed]/home_feeding_choice.webp"
                        scene daisy_home_feeding_choice
                        $ teacher.fullness += 0.5
                        $ foodheld -= 1
                        jump daisy_home_feeding
                    "Fair enough, want to work off some of that lethargy?":
                        if persistent.nosexscene == True:
                            "You have sex scenes disabled in preferences, now leaving daisy her home."
                            return
                        hide screen teacherfullness
                        call Daisy_Home_Sex from _call_Daisy_Home_Sex_1
                        return
                    "I think that will do it for me today.":
                        teacher "I was hoping for a little more, but I understand. Thank you very much for the food and feeding. Let’s get this place cleaned up."
                        "After helping Daisy pick up, I say goodbye and head home."
                        hide screen teacherfullness
                        return
            else:
                call rngeatingdaisyhome from _call_rngeatingdaisyhome_3
                window hide
                pause
                image daisy_home_feeding_choice = "/teacher/[teacher.stage]/[stuffed]/home_feeding_choice.webp"
                scene daisy_home_feeding_choice
                teacher "Thank you very much for the food. I can keep going if you want."
                $ teacher.fullness += 0.5
                $ foodheld -= 1
                jump daisy_home_feeding

        "Stop feeding her.":
            teacher "What else would you like to do?"
            menu:
                "Want to work off some of that lethargy?":
                    if persistent.nosexscene == True:
                        "You have sex scenes disabled in preferences, now leaving daisy her home."
                        return
                    hide screen teacherfullness
                    call Daisy_Home_Sex from _call_Daisy_Home_Sex_2
                    return
                "I think that will do it for me today.":
                    teacher "I was hoping for a little more, but I understand. Thank you very much for the food and feeding. Let's get this place cleaned up."
                    "After helping Daisy clean up, I say goodbye and head home."
            hide screen teacherfullness
            return

label luna_home_feeding:
    image luna_home_feeding_choice = "/luna/[luna.stage]/home_feeding_choice1_[stuffed].webp"
    scene luna_home_feeding_choice
    menu:
        "Feed her more food.":
            $ final_food_capacity = (luna.stomach_capacity * luna.addiction_to_food)
            if foodheld <= 0:
                "You do not have anymore food with you to feed Luna with."
                return

            elif final_food_capacity <= luna.fullness and lastfooditem == 1:
                luna "I can't eat anymore, I am completely full."
                $ lastfooditem = 0
                return

            elif final_food_capacity <= luna.fullness and lastfooditem == 0:
                luna "I am not sure I can eat anymore."
                pc "I think you can eat one more thing."
                luna "Only one more, then I need to take a nap to digest all this."
                call rngeatinglunahome from _call_rngeatinglunahome
                window hide
                pause
                $ stuffed = 3
                "Her belly looks even bigger than before."
                $ lastfooditem = 1
                $ luna.fullness += 0.5
                $ foodheld -= 1
                jump luna_home_feeding

            elif final_food_capacity <= (luna.fullness * 2) and stuffed == 2:
                luna "Pff, I feel so stuffed, but I want more food."
                call rngeatinglunahome from _call_rngeatinglunahome_1
                window hide
                pause
                $ luna.fullness += 0.5
                $ foodheld -= 1
                jump luna_home_feeding

            elif final_food_capacity <= (luna.fullness * 2):
                luna "If you want to do anything other than feed me I think we should stop the feeding before I am unable to move."
                menu:
                    "Continue feeding her.":
                        luna "I hoped you would say that."
                        call rngeatinglunahome from _call_rngeatinglunahome_2
                        window hide
                        pause
                        $ stuffed = 2
                        "Her belly starts to look bigger from all the food."
                        $ luna.fullness += 0.5
                        $ foodheld -= 1
                        jump luna_home_feeding

                    "Stop feeding her.":
                        luna "I could have guessed you were here for more reasons than just feeding me."
                        return
            else:
                luna "Yes, I'd love to eat more. There is still plenty of room."
                call rngeatinglunahome from _call_rngeatinglunahome_3
                window hide
                pause
                $ luna.fullness += 0.5
                $ foodheld -= 1
                jump luna_home_feeding

        "Rub her belly." if stuffed >= 2 and bellyrubs == 1 and bellyrub == 0 and luna.stage >= 7:
            image luna_home_bellyrub1 = "/luna/[luna.stage]/home_bellyrub1_[stuffed].webp"
            scene luna_home_bellyrub1
            "You reach your hands down and begin rubbing Luna's belly."
            pc "Looks like your beautiful belly deserves a massage break."
            image luna_home_bellyrub2 = "/luna/[luna.stage]/home_bellyrub2_[stuffed].webp"
            scene luna_home_bellyrub2
            luna "Mmm, it feels so big and full."
            luna "Yet I still can't see it past my boobs."
            pc "Maybe if we keep feeding you, you might."
            luna "I don't know, my boobs are really big."
            image luna_home_bellyrub3 = "/luna/[luna.stage]/home_bellyrub3_[stuffed].webp"
            scene luna_home_bellyrub3
            luna "Growing to overshadow my belly."
            pc "Yes, but don't forget stuffing your belly full of food is what made your breasts this big."
            image luna_home_bellyrub4 = "/luna/[luna.stage]/home_bellyrub4_[stuffed].webp"
            scene luna_home_bellyrub4
            pc "Your belly is truly magnificent too."
            luna "Give me more food!"
            luna "I'm going to eat and make it big enough to see it."
            pc "That's the spirit!"
            $ luna.fullness -= 1
            $ lastfooditem = 0
            $ bellyrub = 1
            jump luna_home_feeding

        "Stop feeding her.":
            return


label cayenne_home_feeding:
    call rngeatingcayennehomefoodchoice from _call_rngeatingcayennehomefoodchoice
    menu:
        "Give her even more food.":
            $ final_food_capacity = (cayenne.stomach_capacity * cayenne.addiction_to_food)
            if foodheld <= 0:
                "You do not have anymore food with you to feed Cayenne with."
                return

            elif final_food_capacity <= cayenne.fullness and lastfooditem == 1:
                call rngeatingcayennehomefoodchoice from _call_rngeatingcayennehomefoodchoice_1
                cayenne "I can't eat anymore, I am completely full."
                $ lastfooditem = 0
                return

            elif final_food_capacity <= cayenne.fullness and lastfooditem == 0:
                call rngeatingcayennehomefoodchoice from _call_rngeatingcayennehomefoodchoice_2
                cayenne "I am not sure I can eat anymore."
                image cayenne_home_afterfeed1 = "/cayenne/[cayenne.stage]/home_afterfeed1.webp"
                scene cayenne_home_afterfeed1
                "Upon revealing her final course, Cayenne makes it clear that she can't handle it by herself."
                image cayenne_home_afterfeed2 = "/cayenne/[cayenne.stage]/home_afterfeed2.webp"
                scene cayenne_home_afterfeed2
                "Taking the charge as her tutor, you proceed to hand feed her."
                $ stuffed = 3
                "While the going is slow, you manage to help her get through the rest of her stuffing session."
                window hide
                pause
                $ lastfooditem = 1
                $ cayenne.fullness += 0.5
                $ foodheld -= 1
                image cayenne_home_afterfeed3 = "/cayenne/[cayenne.stage]/home_afterfeed3.webp"
                scene cayenne_home_afterfeed3
                return

            elif final_food_capacity <= (cayenne.fullness * 2) and stuffed == 2:
                call rngeatingcayennehomefoodchoice from _call_rngeatingcayennehomefoodchoice_3
                cayenne "Pff, I feel so stuffed, but I want more food."
                call rngeatingcayennehome from _call_rngeatingcayennehome_1
                window hide
                pause
                $ cayenne.fullness += 0.5
                $ foodheld -= 1
                jump cayenne_home_feeding

            elif final_food_capacity <= (cayenne.fullness * 2):
                cayenne "If you want to do anything other than feed me I think we should stop the feeding before I am unable to move."
                menu:
                    "Continue feeding her.":
                        cayenne "I hoped you would say that."
                        call rngeatingcayennehome from _call_rngeatingcayennehome_2
                        window hide
                        pause
                        $ stuffed = 2
                        "Her belly starts to look bigger from all the food."
                        $ cayenne.fullness += 0.5
                        $ foodheld -= 1
                        jump cayenne_home_feeding

                    "Stop feeding her.":
                        cayenne "I could have guessed you were here for more reasons than just feeding me."
                        return
            else:
                cayenne "Yes, I'd love to eat more. There is still plenty of room."
                call rngeatingcayennehome from _call_rngeatingcayennehome_3
                window hide
                pause
                $ cayenne.fullness += 0.5
                $ foodheld -= 1
                jump cayenne_home_feeding

        "Rub her belly." if stuffed >= 2 and bellyrubs == 1 and bellyrub == 0:
            if cayennebellyrubfirsttime == 1:
                image cayenne_home_bellyrub2 = "/cayenne/[cayenne.stage]/home_bellyrub2_[stuffed].webp"
                scene cayenne_home_bellyrub2
                "Reaching over, you spread your hands across her belly."
                cayenne "What are you doing?"
                pc "I thought it would help."
                cayenne "It does feel good…ok keep going."
                "You let your hands wander all over her body."
                image cayenne_home_bellyrub3 = "/cayenne/[cayenne.stage]/home_bellyrub3_[stuffed].webp"
                scene cayenne_home_bellyrub3
                "You can feel Cayenne reacting to your sensual touch."
                cayenne "I guess that does help a little."
                "It seems she is ready to continue."
                $ cayennebellyrubfirsttime = 0
            elif cayenne.stage <= 7:
                image cayenne_home_bellyrub1 = "/cayenne/[cayenne.stage]/home_bellyrub1_[stuffed].webp"
                scene cayenne_home_bellyrub1
                "Cayenne grabs your hand."
                cayenne "I love to feel your touch on my body when I am this full."
                cayenne "I don't know why, it just feels so good!"
                image cayenne_home_bellyrub2 = "/cayenne/[cayenne.stage]/home_bellyrub2_[stuffed].webp"
                scene cayenne_home_bellyrub2
                "Letting yourself press and massage her belly harder, Cayenne almost squirms in pleasure."
                "She really seems to enjoy the attention you are giving her."
                image cayenne_home_bellyrub3 = "/cayenne/[cayenne.stage]/home_bellyrub3_[stuffed].webp"
                scene cayenne_home_bellyrub3
                cayenne "That feels good, you know just how to get rid of that uncomfortable tightness."
                "It seems she is ready to continue."
            else:
                image cayenne_home_bellyrub1 = "/cayenne/[cayenne.stage]/home_bellyrub1_[stuffed].webp"
                scene cayenne_home_bellyrub1
                "Cayenne grabs your hand."
                cayenne "I love to feel your touch on my body when I am this full."
                image cayenne_home_bellyrub2 = "/cayenne/[cayenne.stage]/home_bellyrub2_[stuffed].webp"
                scene cayenne_home_bellyrub2
                "Reaching around, you spread your hands across her belly."
                cayenne "Oooah, just there, that's the spot."
                cayenne "Keep going, don't stop!"
                "Pressing harder you enjoy the feel of her fattening body under your hands."
                image cayenne_home_bellyrub3 = "/cayenne/[cayenne.stage]/home_bellyrub3_[stuffed].webp"
                scene cayenne_home_bellyrub3
                "You worry you are being too rough, but it seems like the harder you press into her, the more Cayenne enjoys it."
                cayenne "I can't believe how good that feels."
                "It seems she is ready to continue."

            $ cayenne.fullness -= 1
            $ lastfooditem = 0
            $ bellyrub = 1
            jump cayenne_home_feeding

        "No, that's it.":
            return

label amber_home_feeding:
    image amber_home9_stuffed = "/amber/[amber.stage]/home9_[stuffed].webp"
    scene amber_home9_stuffed
    menu:
        "Feed her more food.":
            $ final_food_capacity = (amber.stomach_capacity * amber.addiction_to_food)
            if foodheld <= 0:
                "You do not have anymore food with you to feed Amber with."
                return

            elif final_food_capacity <= amber.fullness and lastfooditem == 4:
                call rngeatingamberhome
                amber "I'm so full, everything feels so tight and aches."
                "Deciding she had eaten enough, you put the snacks away."
                $ lastfooditem = 0
                return

            elif final_food_capacity <= amber.fullness and lastfooditem == 3:
                call rngeatingamberhome
                amber "Ughh, no more please."
                "For the first time, you can hear the sincerity in her voice instead of the playful submissiveness."
                $ lastfooditem = 4
                $ amber.fullness += 0.5
                $ foodheld -= 1
                jump amber_home_feeding

            elif final_food_capacity <= amber.fullness and lastfooditem == 2:
                call rngeatingamberhome
                amber "I thought I said one more, I'm too full for any more."
                $ lastfooditem = 3
                $ amber.fullness += 0.5
                $ foodheld -= 1
                jump amber_home_feeding

            elif final_food_capacity <= amber.fullness and lastfooditem == 1:
                call rngeatingamberhome
                amber "One more then I am done!"
                $ lastfooditem = 2
                $ amber.fullness += 0.5
                $ foodheld -= 1
                jump amber_home_feeding

            elif final_food_capacity <= amber.fullness and lastfooditem == 0:
                call rngeatingamberhome
                amber "I can't eat any more."
                image amber_home_feeding_grow = "/amber/[amber.stage]/home_feeding_grow[stuffed].webp"
                scene amber_home_feeding_grow
                window hide
                pause
                $ stuffed = 2
                "Her stomach had certainly grown, but you can tell she doesn't mean it."
                "Her mouth is already open and waiting for the next snack."
                $ lastfooditem = 1
                $ amber.fullness += 0.5
                $ foodheld -= 1
                jump amber_home_feeding

            elif final_food_capacity <= (amber.fullness * 2) and stuffed == 1:
                call rngeatingamberhome
                amber "Mmm, so good."
                window hide
                pause
                $ amber.fullness += 0.5
                $ foodheld -= 1
                jump amber_home_feeding

            elif final_food_capacity <= (amber.fullness * 2):
                call rngeatingamberhome
                window hide
                pause
                amber "I'm going to burst, my stomach is so big."
                $ amber.fullness += 0.5
                $ foodheld -= 1
                jump amber_home_feeding
                    
            else:
                call rngeatingamberhome
                amber "Mmm, so good."
                window hide
                pause
                $ amber.fullness += 0.5
                $ foodheld -= 1
                jump amber_home_feeding

        "Rub her belly." if stuffed >= 1 and bellyrubs == 1 and bellyrub == 0:
            #Variation1
            $ rng = 1
            if rng == 1:
                image amber_home_bellyrub_1 = "/amber/[amber.stage]/bellyrub1_[stuffed].webp"
                scene amber_home_bellyrub_1
                "Reaching over, you press your hands into Amber's bloated stomach."
                amber "Mmm, I feel so full."
                pc "You have eaten a lot, it's not surprising."
                image amber_home_bellyrub_2 = "/amber/[amber.stage]/bellyrub2_[stuffed].webp"
                scene amber_home_bellyrub_2
                amber "I know, I can feel my skin stretching."
                amber "It's so tight, it feels amazing."
                pc "Just imagine how you will feel in a few more weeks."
                image amber_home_bellyrub_3 = "/amber/[amber.stage]/bellyrub3_[stuffed].webp"
                scene amber_home_bellyrub_3
                amber "I'm going to get so fat, I can't wait!"
                amber "Now, keep feeding me. We are not done yet."

            #Variation2
            elif rng == 2:
                "Reaching over, you press your hands into Amber's bloated stomach."
                amber "Oh yeah, press harder."
                pc "You feel like a rock, your stomach is so full."
                amber "I know, but I am not big enough yet."
                amber "I just need a moment to feel more comfortable."
                "Pressing harder into her belly, Amber moans in pleasure."
                amber "It aches so badly, I'm definitely going to get more stretch marks after this."
                pc "Maybe I can help with that."
                "Grabbing a bottle of lotion from the night stand, you rub it into her swollen body."
                amber "Fuck, this is so sexy, feeling your hands all over my body like this."
                amber "But let's keep going, I want to be even bigger by the time you leave."

            $ amber.fullness -= 1
            $ lastfooditem = 0
            $ bellyrub = 1
            jump amber_home_feeding

        "Stop feeding her.":
            return


label lisa_home_feeding:
    #PIC NEEDED
    menu:
        "Feed her more food.":
            $ final_food_capacity = (lisa.stomach_capacity * lisa.addiction_to_food)
            if foodheld <= 0:
                "You do not have anymore food with you to feed Lisa with."
                return

            elif final_food_capacity <= lisa.fullness and lastfooditem == 4:
                #PIC NEEDED
                lisa "I'm so full, everything feels so tight and aches."
                "Deciding she had eaten enough, you put the snacks away."
                $ lastfooditem = 0
                return

            elif final_food_capacity <= lisa.fullness and lastfooditem == 3:
                #PIC NEEDED
                lisa "Ughh, no more please."
                "For the first time, you can hear the sincerity in her voice instead of the playful submissiveness."
                $ lastfooditem = 4
                $ lisa.fullness += 0.5
                $ foodheld -= 1
                jump lisa_home_feeding

            elif final_food_capacity <= lisa.fullness and lastfooditem == 2:
                #PIC NEEDED
                lisa "I thought I said one more, I'm too full for any more."
                $ lastfooditem = 3
                $ lisa.fullness += 0.5
                $ foodheld -= 1
                jump lisa_home_feeding

            elif final_food_capacity <= lisa.fullness and lastfooditem == 1:
                #PIC NEEDED
                lisa "One more then I am done!"
                $ lastfooditem = 2
                $ lisa.fullness += 0.5
                $ foodheld -= 1
                jump lisa_home_feeding

            elif final_food_capacity <= lisa.fullness and lastfooditem == 0:
                #PIC NEEDED
                lisa "I can't eat any more."
                #PIC NEEDED
                window hide
                pause
                $ stuffed = 2
                "Her stomach had certainly grown, but you can tell she doesn't mean it."
                "Her mouth is already open and waiting for the next snack."
                $ lastfooditem = 1
                $ lisa.fullness += 0.5
                $ foodheld -= 1
                jump lisa_home_feeding

            elif final_food_capacity <= (lisa.fullness * 2) and stuffed == 1:
                #PIC NEEDED
                lisa "Mmm, so good."
                window hide
                pause
                $ lisa.fullness += 0.5
                $ foodheld -= 1
                jump lisa_home_feeding

            elif final_food_capacity <= (lisa.fullness * 2):
                #PIC NEEDED
                window hide
                pause
                lisa "I'm going to burst, my stomach is so big."
                $ lisa.fullness += 0.5
                $ foodheld -= 1
                jump lisa_home_feeding
                    
            else:
                #PIC NEEDED
                lisa "Mmm, so good."
                window hide
                pause
                $ lisa.fullness += 0.5
                $ foodheld -= 1
                jump lisa_home_feeding

        "Rub her belly." if stuffed >= 1 and bellyrubs == 1 and bellyrub == 0:
            #Variation1
            $ rng = 1
            if rng == 1:
                "Giving Lisa a break from the feeding, you gently massage her stomach."
                lisa "That feels nice."
                pc "You feel pretty full."
                lisa "You don't have to tell me…but it will be worth it in the end."
                lisa "I hope Marie appreciates all this."
                pc "I have no doubts she will."
                "Rubbing Lisa's belly, you feel her relax slightly."

            #Variation2
            elif rng == 2:
                "Giving Lisa a break from the feeding, you gently massage her stomach."
                lisa "Couldn't keep your hands to yourself."
                pc "You didn't seem to complain last time."
                lisa "It feels too good to complain, keep going."
                lisa "Part of me thinks I could get used to this."
                lisa "Being fed and having my belly rubbed like this."
                pc "I'm sure Marie would be happy to hear that."
                "Rubbing Lisa's belly, you feel her relax slightly."

            $ lisa.fullness -= 1
            $ lastfooditem = 0
            $ bellyrub = 1
            jump lisa_home_feeding

        "Stop feeding her.":
            return


label bonnie_home_feeding:
    image cafe_bonnie_home_feeding_start = "/bonnie/[bonnie.stage]/feeding_start_[stuffed].webp"
    scene cafe_bonnie_home_feeding_start
    menu:
        "Feed her more food.":
            $ final_food_capacity = (bonnie.stomach_capacity * bonnie.addiction_to_food)
            if foodheld <= 0:
                "You do not have anymore food with you to feed Bonnie with."
                return

            elif final_food_capacity <= bonnie.fullness and lastfooditem == 1:
                image cafe_bonnie_home_feeding_start = "/bonnie/[bonnie.stage]/feeding_start_[stuffed].webp"
                scene cafe_bonnie_home_feeding_start
                bonnie "I can't eat anymore, I'm completely full."
                $ lastfooditem = 0
                return

            elif final_food_capacity <= bonnie.fullness and lastfooditem == 0:
                image cafe_bonnie_home_feeding_start = "/bonnie/[bonnie.stage]/feeding_start_[stuffed].webp"
                scene cafe_bonnie_home_feeding_start
                bonnie "I am not sure I can eat anymore."
                pc "I think you can eat one more box of chocolates."
                bonnie "Only one more. After that, I really need to go sleep it off."
                call rngeatingbonniehome from _call_rngeatingbonniehome
                window hide
                pause
                $ stuffed = 2
                "Her belly looks even bigger than before."
                $ lastfooditem = 1
                $ bonnie.fullness += 0.5
                $ foodheld -= 1
                jump bonnie_home_feeding

            elif final_food_capacity <= (bonnie.fullness * 2) and stuffed == 1:
                image cafe_bonnie_home_feeding_start = "/bonnie/[bonnie.stage]/feeding_start_[stuffed].webp"
                scene cafe_bonnie_home_feeding_start
                bonnie "Pff, I feel so stuffed, but I need more chocolates."
                call rngeatingbonniehome from _call_rngeatingbonniehome_1
                window hide
                pause
                $ bonnie.fullness += 0.5
                $ foodheld -= 1
                jump bonnie_home_feeding

            elif final_food_capacity <= (bonnie.fullness * 2):
                bonnie "I know you like to stuff me to the brim with chocolates, but if we're thinking about having some great sex, I really should stop eating chocolates."
                menu:
                    "Continue feeding her chocolates.":
                        bonnie "I hoped you would say that."
                        call rngeatingbonniehome from _call_rngeatingbonniehome_2
                        window hide
                        pause
                        if stuffed == 0:
                            $ stuffed = 1
                        "Her belly starts to look bigger from all the food."
                        $ bonnie.fullness += 0.5
                        $ foodheld -= 1
                        jump bonnie_home_feeding

                    "Stop feeding her.":
                        bonnie "Let's have some fun together."
                        return
            else:
                bonnie "Yes, I'd love to eat more. There is still plenty of room."
                call rngeatingbonniehome from _call_rngeatingbonniehome_3
                window hide
                pause
                $ bonnie.fullness += 0.5
                $ foodheld -= 1
                jump bonnie_home_feeding

        "Rub her belly." if stuffed >= 1 and bellyrubs == 1 and bellyrub == 0:
            image cafe_bonnie_home_bellyrub_1 = "/bonnie/[bonnie.stage]/bellyrub_1_[stuffed].webp"
            scene cafe_bonnie_home_bellyrub_1
            "Reaching over, you gently rub Bonnie's belly."
            bonnie "Do you like seeing me like this?"
            pc "I do, your belly is so big from all the chocolates."
            image cafe_bonnie_home_bellyrub_2 = "/bonnie/[bonnie.stage]/bellyrub_2_[stuffed].webp"
            scene cafe_bonnie_home_bellyrub_2
            bonnie "I'm so round and full, it feels nice for me too."
            bonnie "In fact, I think I might be able to manage a few more now."
            pc "Are you sure, you are already so big."
            image cafe_bonnie_home_bellyrub_3 = "/bonnie/[bonnie.stage]/bellyrub_3_[stuffed].webp"
            scene cafe_bonnie_home_bellyrub_3
            bonnie "I can manage another one, maybe a couple more for you."
            bonnie "I want to make you happy."
            $ bonnie.fullness -= 1
            $ lastfooditem = 0
            $ bellyrub = 1
            jump bonnie_home_feeding

        "Stop feeding her.":
            return

label katrine_home_feeding:
    menu:
        "Feed her.":
            $ final_food_capacity = (katrine.stomach_capacity * katrine.addiction_to_food)
            if foodheld <= 0:
                "You do not have anymore food with you to feed Katrine with."
                return

            elif final_food_capacity <= katrine.fullness and lastfooditem == 1:
                image katrine_home_afterfeeding = "/katrine/[katrine.stage]/home_afterfeeding.webp"
                scene katrine_home_afterfeeding
                katrine "I can't eat anymore, I'm completely full."
                $ lastfooditem = 0
                return

            elif final_food_capacity <= katrine.fullness and lastfooditem == 0:
                katrine "Oooh, this is so amazing. But I'm not sure I can eat any more."
                pc "I think you can eat one more thing."
                katrine "Ok, you're right. One more thing, but then I'm going to need attention of a different kind."
                call rngeatingkatrinehome from _call_rngeatingkatrinehome
                window hide
                pause
                $ stuffed = 3
                "Her belly looks even bigger than before. Her tights starting to strain against her growing body."
                $ lastfooditem = 1
                $ katrine.fullness += 0.5
                $ foodheld -= 1
                jump katrine_home_feeding

            elif final_food_capacity <= (katrine.fullness * 2) and stuffed == 2:
                katrine "I feel so stuffed, but I want more!"
                call rngeatingkatrinehome from _call_rngeatingkatrinehome_1
                window hide
                pause
                $ katrine.fullness += 0.5
                $ foodheld -= 1
                jump katrine_home_feeding

            elif final_food_capacity <= (katrine.fullness * 2):
                katrine "Yes, keep feeding me."
                menu:
                    "Continue feeding her.":
                        katrine "Keep going, please don't stop feeding me."
                        call rngeatingkatrinehome from _call_rngeatingkatrinehome_2
                        window hide
                        pause
                        if stuffed == 1:
                            $ stuffed = 2
                        katrine "Mmm, I cant believe how good this feels. My belly is feeling so tight."
                        "Her belly is looking bigger from all the food, but she doesn’t seem to care."
                        $ katrine.fullness += 0.5
                        $ foodheld -= 1
                        jump katrine_home_feeding

                    "Stop feeding her.":
                        katrine "Well, let's get it on then."
                        return
            else:
                katrine "Mmm, this is perfect."
                call rngeatingkatrinehome from _call_rngeatingkatrinehome_3
                window hide
                pause
                $ katrine.fullness += 0.5
                $ foodheld -= 1
                jump katrine_home_feeding

        "Rub her belly." if stuffed >= 2 and bellyrubs == 1 and bellyrub == 0:
            image katrine_home_bellyrub_1 = "/katrine/[katrine.stage]/home_bellyrub_1_[stuffed].webp"
            scene katrine_home_bellyrub_1
            "Reaching over, you gently knead her bulging belly."
            pc "You really seemed to enjoy that."
            image katrine_home_bellyrub_2 = "/katrine/[katrine.stage]/home_bellyrub_2_[stuffed].webp"
            scene katrine_home_bellyrub_2
            katrine "I'm enjoying this more, you really know what you are doing."
            katrine "That feels so nice, it doesn't ache any more."
            pc "You want to carry on going?"
            image katrine_home_bellyrub_3 = "/katrine/[katrine.stage]/home_bellyrub_3_[stuffed].webp"
            scene katrine_home_bellyrub_3
            katrine "Definitely, just keep rubbing my stomach a little longer."
            pc "Of course."
            $ katrine.fullness -= 1
            $ lastfooditem = 0
            $ bellyrub = 1
            jump katrine_home_feeding

        "Don't feed her.":
            katrine "Well, let's get it on then."
            return

label trista_gym_feeding:
    menu:
        "Feed her.":
            $ final_food_capacity = (trista.stomach_capacity * trista.addiction_to_food)

            if final_food_capacity <= trista.fullness and lastfooditem == 1:
                image trista_gym_afterfeeding1 = "/trista/[trista.stage]/gym_afterfeeding1_[stuffed].webp"
                scene trista_gym_afterfeeding1
                trista "I can't eat anymore, I'm completely full."
                $ lastfooditem = 0
                return

            elif final_food_capacity <= trista.fullness and lastfooditem == 0:
                trista "Ok, I think I'm at my limit now. We might have to stop."
                pc "I think you can eat one more thing. You wanted to push your limits right."
                trista "Ok, you're right. I can squeeze in one more."
                call rngeatingtristagym from _call_rngeatingtristagym
                window hide
                pause
                image trista_gym_feed_grow1 = "/trista/[trista.stage]/gym_feed_grow1_[stuffed].webp"
                scene trista_gym_feed_grow1
                pause
                $ stuffed = 3
                pause
                "Finishing up, her belly has grown substantially from when you started. Packed tight with fattening treats."
                $ lastfooditem = 1
                $ trista.fullness += 0.5
                jump trista_gym_feeding

            elif final_food_capacity <= (trista.fullness * 2) and stuffed == 2:
                trista "I feel so stuffed, but no pain no gains."
                call rngeatingtristagym from _call_rngeatingtristagym_1
                window hide
                pause
                $ trista.fullness += 0.5
                jump trista_gym_feeding

            elif final_food_capacity <= (trista.fullness * 2):
                trista "Plenty of room left, don't stop feeding me!"
                menu:
                    "Continue feeding her.":
                        trista "My belly is feeling full, but let's keep going. Need to push my limits!"
                        call rngeatingtristagym from _call_rngeatingtristagym_2
                        window hide
                        pause
                        image trista_gym_feed_grow1 = "/trista/[trista.stage]/gym_feed_grow1_[stuffed].webp"
                        scene trista_gym_feed_grow1
                        pause
                        if stuffed == 1:
                            $ stuffed = 2
                        pause
                        "Her belly is growing bigger from this latest binge, but she clearly wants you to continue."
                        $ trista.fullness += 0.5
                        jump trista_gym_feeding

                    "Stop feeding her.":
                        trista "You can't stop feeding me, I need your help to push myself to the limit."
                        jump trista_gym_feeding
            else:
                trista "Yes, keep feeding me, fill me up to my capacity."
                call rngeatingtristagym from _call_rngeatingtristagym_3
                window hide
                pause
                $ trista.fullness += 0.5
                jump trista_gym_feeding

        "Rub her belly." if stuffed >= 2 and bellyrubs == 1 and bellyrub == 0:
            image trista_gym_bellyrub_1 = "/trista/[trista.stage]/gym_bellyrub1_[stuffed].webp"
            scene trista_gym_bellyrub_1
            "Reaching out, you touch Trista's straining stomach with your hands."
            pc "Do you think a massage would help?"
            trista "Maybe, it helps after a workout."
            image trista_gym_bellyrub_2 = "/trista/[trista.stage]/gym_bellyrub2_[stuffed].webp"
            scene trista_gym_bellyrub_2
            "Pressing your hands onto Trista's taught belly, you can feel how stuffed and hard it is."
            trista "Mmm, that feels good."
            trista "But you can press harder."
            "Despite her words, it is hard to find anywhere that isn't rock solid with food."
            image trista_gym_bellyrub_3 = "/trista/[trista.stage]/gym_bellyrub3_[stuffed].webp"
            scene trista_gym_bellyrub_3
            trista "I think that worked, my stomach doesn't feel so tight anymore."
            trista "I can keep going now."
            $ trista.fullness -= 1
            $ lastfooditem = 0
            $ bellyrub = 1
            jump trista_gym_feeding

        "Don't feed her.":
            trista "You can't stop feeding me, I need your help to push myself to the limit."
            jump trista_gym_feeding
