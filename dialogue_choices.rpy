label dialogue_choices:
    if teaching_calories_check == 1 and teaching_terminology_check == 1 and teaching_corndog_check == 1 and teaching_socialfood_check == 1 and teaching_gainingtips_check == 1  and teaching_milkshake_check == 1 and teaching_fatphobia_check == 1 and teaching_indulgence_check == 1 and teaching_feederfeedee_check == 1 and teaching_naturenurture_check == 1 and teaching_animal_check == 1 and teaching_onionring_check == 1 and teaching_hedonism_check == 1 and teaching_addiction_check == 1 and teaching_industry_check == 1 and teaching_bodytypes_check == 1 and teaching_careers_check == 1 and teaching_socialfood_check == 1 and teaching_clothing_check == 1:
        return
    call rngteachingscene from _call_rngteachingscene_70
    teacher "Now let's move on to today's lesson."
    if teaching_bmi_check == 0 and teacher.stage >= 7:
        call teaching_bmi
        return
    if teaching_bodyfat_check == 0 and teacher.stage >= 8:
        call teaching_bodyfat
        return
    teacher "What do you want to learn about today?"

    menu:

        "I want to learn about calories." if teaching_calories_check == 0:
            if teaching_calories_times == 0:
                call teaching_calories1 from _call_teaching_calories1
            elif teaching_calories_times == 1:
                call teaching_calories2 from _call_teaching_calories2

        "I want to learn some terminology." if teaching_terminology_check == 0:
            if teaching_terminology_times == 0:
                call teaching_terminology1 from _call_teaching_terminology1
            elif teaching_terminology_times == 1:
                call teaching_terminology2 from _call_teaching_terminology2

        "I want to learn about hedonism through the ages." if teaching_hedonism_check == 0:
            if teaching_hedonism_times == 0:
                call hedonism_through_the_ages1 from _call_hedonism_through_the_ages1
            elif teaching_hedonism_times == 1:
                call hedonism_through_the_ages2 from _call_hedonism_through_the_ages2
            elif teaching_hedonism_times == 2:
                call hedonism_through_the_ages3 from _call_hedonism_through_the_ages3

        "I want to learn about food addiction." if teaching_addiction_check == 0  and teacher.stage >= 11:
            if teaching_addiction_times == 0:
                call food_addiction1 from _call_food_addiction1
            elif teaching_addiction_times == 1:
                call food_addiction2 from _call_food_addiction2

        "I want to learn about the food industry." if teaching_industry_check == 0 and teacher.stage >= 3:
            if teaching_industry_times == 0:
                call food_industry1 from _call_food_industry1
            elif teaching_industry_times == 1:
                call food_industry2 from _call_food_industry2
            elif teaching_industry_times == 2:
                call food_industry3 from _call_food_industry3

        "I want to learn about nutrition in the animal kingdom." if teaching_animal_check == 0 and teacher.stage >= 10:
            if teaching_animal_times == 0:
                call animal_kingdom1 from _call_animal_kingdom1
            elif teaching_animal_times == 1:
                call animal_kingdom2 from _call_animal_kingdom2
            elif teaching_animal_times == 2:
                call animal_kingdom3 from _call_animal_kingdom3
            elif teaching_animal_times == 3:
                call animal_kingdom4 from _call_animal_kingdom4

        "I want to learn about body types." if teaching_bodytypes_check == 0:
            if teaching_bodytypes_times == 0:
                call body_types1 from _call_body_types1
            elif teaching_bodytypes_times == 1:
                call body_types2 from _call_body_types2

        "I want to learn about the subject of nature and nurture." if teaching_naturenurture_check == 0 and teacher.stage >= 4:
            if teaching_naturenurture_times == 0:
                call nature_nurture1 from _call_nature_nurture1
            elif teaching_naturenurture_times == 1:
                call nature_nurture2 from _call_nature_nurture2
            elif teaching_naturenurture_times == 2:
                call nature_nurture3 from _call_nature_nurture3

        "I want to learn about indulgence." if teaching_indulgence_check == 0 and teacher.stage >= 5:
            if teaching_indulgence_times == 0:
                call indulgence1 from _call_indulgence1
            elif teaching_indulgence_times == 1:
                call indulgence2 from _call_indulgence2
            elif teaching_indulgence_times == 2:
                call indulgence3 from _call_indulgence3

        "I want to learn about fattening careers." if teaching_careers_check == 0 and teacher.stage >= 15:
            if teaching_careers_times == 0:
                call fattening_careers1 from _call_fattening_careers1
            elif teaching_careers_times == 1:
                call fattening_careers2 from _call_fattening_careers2
            elif teaching_careers_times == 2:
                call fattening_careers3 from _call_fattening_careers3

        "I want to learn about the feeder and feedee relationship." if teaching_feederfeedee_check == 0 and teacher.stage >= 12:
            if teaching_feederfeedee_times == 0:
                call feeder_feedee1 from _call_feeder_feedee1
            elif teaching_feederfeedee_times == 1:
                call feeder_feedee2 from _call_feeder_feedee2
            elif teaching_feederfeedee_times == 2:
                call feeder_feedee3 from _call_feeder_feedee3
            elif teaching_feederfeedee_times == 3:
                call feeder_feedee4 from _call_feeder_feedee4

        "I want to learn about fatphobia." if teaching_fatphobia_check == 0 and teacher.stage >= 16:
            if teaching_fatphobia_times == 0:
                call fatphobia1 from _call_fatphobia1
            elif teaching_fatphobia_times == 1:
                call fatphobia2 from _call_fatphobia2
            elif teaching_fatphobia_times == 2:
                call fatphobia3 from _call_fatphobia3
            elif teaching_fatphobia_times == 3:
                call fatphobia4 from _call_fatphobia4

        "I want to learn about social food." if teaching_socialfood_check == 0 and teacher.stage >= 9:
            if teaching_socialfood_times == 0:
                call socialfood1 from _call_socialfood1
            elif teaching_socialfood_times == 1:
                call socialfood2 from _call_socialfood2
            elif teaching_socialfood_times == 2:
                call socialfood3 from _call_socialfood3

        "I want to learn about plus-sized clothing." if teaching_clothing_check == 0 and teacher.stage >= 7:
            if teaching_clothing_times == 0:
                call clothing1 from _call_clothing1
            elif teaching_clothing_times == 1:
                call clothing2 from _call_clothing2
            elif teaching_clothing_times == 2:
                call clothing3 from _call_clothing3
            elif teaching_clothing_times == 3:
                call clothing4 from _call_clothing4

        "I want to learn some gaining tips." if teaching_gainingtips_check == 0 and teacher.stage >= 9:
            if teaching_gainingtips_times == 0:
                call gaining_tips1 from _call_gaining_tips1
            elif teaching_gainingtips_times == 1:
                call gaining_tips2 from _call_gaining_tips2
            elif teaching_gainingtips_times == 2:
                call gaining_tips3 from _call_gaining_tips3
            elif teaching_gainingtips_times == 3:
                call gaining_tips4 from _call_gaining_tips4

        "I want to learn about corndogs." if teaching_corndog_check == 0 and teacher.stage >= 3:
            call corndog_unlock from _call_corndog_unlock

        "I want to learn about milkshakes." if teaching_milkshake_check == 0 and teacher.stage >= 3:
            call milkshake_unlock from _call_milkshake_unlock

        "I want to learn about onion rings." if teaching_onionring_check == 0 and teacher.stage >= 5:
            call onionring_unlock from _call_onionring_unlock

    return
