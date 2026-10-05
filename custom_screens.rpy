## Show day and week
screen Day:
    if day == 1:
        $ day2 = 'Monday'
    elif day == 2:
        $ day2 = 'Tuesday'
    elif day == 3:
        $ day2 = 'Wednesday'
    elif day == 4:
        $ day2 = 'Thursday'
    elif day == 5:
        $ day2 = 'Friday'
    elif day == 6:
        $ day2 = 'Saturday'
    elif day == 7:
        $ day2 = 'Sunday'
    if daytime == 1:
        $ time2 = 'Morning'
    elif daytime == 2:
        $ time2 = 'Afternoon'
    elif daytime == 3:
        $ time2 = 'Evening'
    frame background Frame("ui/quickframe.webp",0,0) area(0.01, 0.01, 180, 90):
        vbox:
            xalign 0.5
            yalign 0.5
            text "[day2]  [time2]" xalign 0.5 font "fonts/asapcon.ttf" size 20
            text "Week  [week]" xalign 0.5 font "fonts/asapcon.ttf" size 20
            if foodheld == 1:
                text "$[money],  [foodheld]  Meal" xalign 0.5 font "fonts/asapcon.ttf" size 20
            else:
                text "$[money],  [foodheld]  Meals" xalign 0.5 font "fonts/asapcon.ttf" size 20

## Show fullness bar
screen teacherfullness:
    bar value StaticValue(teacher.fullness, teacher.stomach_capacity) xsize 300 xoffset 80 xalign 0.9 yalign 0.09
    text "Fullness: [teacher.fullness]" xalign 0.99 yalign 0.13 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]

screen lunafullness:
    bar value StaticValue(luna.fullness, luna.stomach_capacity) xsize 300 xoffset 80 xalign 0.9 yalign 0.09
    text "Fullness: [luna.fullness]" xalign 0.99 yalign 0.13 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]

screen cayennefullness:
    bar value StaticValue(cayenne.fullness, cayenne.stomach_capacity) xsize 300 xoffset 80 xalign 0.9 yalign 0.09
    text "Fullness: [cayenne.fullness]" xalign 0.99 yalign 0.13 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]

screen bonniefullness:
    bar value StaticValue(bonnie.fullness, bonnie.stomach_capacity) xsize 300 xoffset 80 xalign 0.9 yalign 0.09
    text "Fullness: [bonnie.fullness]" xalign 0.99 yalign 0.13 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]

screen katrinefullness:
    bar value StaticValue(katrine.fullness, katrine.stomach_capacity) xsize 300 xoffset 80 xalign 0.9 yalign 0.09
    text "Fullness: [katrine.fullness]" xalign 0.99 yalign 0.13 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]

screen tristafullness:
    bar value StaticValue(trista.fullness, trista.stomach_capacity) xsize 300 xoffset 80 xalign 0.9 yalign 0.09
    text "Fullness: [trista.fullness]" xalign 0.99 yalign 0.13 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]

screen amberfullness:
    bar value StaticValue(amber.fullness, amber.stomach_capacity) xsize 300 xoffset 80 xalign 0.9 yalign 0.09
    text "Fullness: [amber.fullness]" xalign 0.99 yalign 0.13 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]

## Screen with Stats Button
screen gameUI:
    modal False
    if renpy.variant("steam_deck"):
        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -10
            yoffset 10
            auto "UI/stats_%s_sd.webp"
            action SetVariable("viewstage", selectedCharacter.stage), SetVariable("undress", False), SetVariable("turnaround", 0), Show("StatsUI")
    else:
        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -10
            yoffset 10
            auto "UI/stats_%s.webp"
            action SetVariable("viewstage", selectedCharacter.stage), SetVariable("undress", False), SetVariable("turnaround", 0), Show("StatsUI")

    if phoneMessages == True:
        hbox spacing -110:
            xalign 0.995
            yalign 0.11
            xoffset -10
            add "UI/phone/[phonegirl].png"
        imagebutton:
            xalign 1.0
            yalign 0.10
            xoffset -10
            idle "images/ui/phonehighlight.webp"
            hover "images/ui/phoneselect.webp"
            action Call("view_phone", from_current=True)
    key "i" action SetVariable("viewstage", selectedCharacter.stage), SetVariable("undress", False), SetVariable("turnaround", 0), Show("StatsUI")
    key "pad_x_press" action SetVariable("viewstage", selectedCharacter.stage), SetVariable("undress", False), SetVariable("turnaround", 0), Show("StatsUI")

screen menuBB:
    modal False
    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -10
        yoffset 10
        auto "UI/choice2_%s_background.webp"
        action SetVariable("keep_working", 1), Return()
    imagebutton:
        xalign 0.5
        yalign 0.4
        xoffset -10
        yoffset 10
        auto "UI/choice2_%s_background.webp"
        action SetVariable("keep_working", 0), Return()
    text "Keep Working" xalign 0.5 yalign 0.317 size 20
    text "Go home" xalign 0.5 yalign 0.418 size 20

## Stats UI
screen StatsUI():
    modal True
    tag statsUI
    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    add "UI/chaulkboard.webp"
    hbox:
        ## middle frame
        add "ui/statsthin.webp"
        frame:
            background Frame("ui/statsframe.webp",0,0)
            ysize 720
            xsize 500
            vbox:
                xalign 0.5
                yoffset 10
                text "[selectedCharacter.name]" font "fonts/asapcon.ttf" xalign 0.5 size 25
                text "[selectedCharacter.age] years old" font "fonts/asapcon.ttf" xalign 0.5 size 25
                if viewstage == selectedCharacter.stage:
                    if persistent.imperial:
                        $ imperialweight = (selectedCharacter.weight * 2.2)
                        text "[imperialweight:.02f]lbs" font "fonts/asapcon.ttf" xalign 0.5 size 25
                    else:
                        text "[selectedCharacter.weight:.02f]kg" font "fonts/asapcon.ttf" xalign 0.5 size 25
                else:
                    $ statscharacter = str.lower(selectedCharacter.name)
                    if statscharacter == "lyn":
                        $ statscharacter = "leanne"
                    $ viewweight = char_weight[statscharacter][viewstage]
                    if persistent.imperial:
                        $ imperialweight = (viewweight * 2.2)
                        $ imperialweight2 = (selectedCharacter.weight * 2.2)
                        text "[imperialweight:.02f]lbs ([imperialweight2:.02f]lbs)" font "fonts/asapcon.ttf" xalign 0.5 size 25
                    else:
                        text "[viewweight:.02f]kg ([selectedCharacter.weight:.02f]kg)" font "fonts/asapcon.ttf" xalign 0.5 size 25

                if persistent.imperial:
                    text "Height:  [selectedCharacter.characterheightimperial]" font "fonts/asapcon.ttf" xalign 0.5 size 25
                else:
                    text "Height:  [selectedCharacter.characterheight]cm" font "fonts/asapcon.ttf" xalign 0.5  size 25

                text ""

                if teaching_bmi_check == 1:
                    if viewstage == selectedCharacter.stage:
                        $ bmi = (selectedCharacter.weight / ((selectedCharacter.characterheight / 100)**2))
                        if bmi <= 18.5:
                            $ bmistatus = "{color=#00ffe4}Underweight{/color}"
                        elif bmi <= 25:
                            $ bmistatus = "{color=#04ff00}Healthy weight{/color}"
                        elif bmi <= 30:
                            $ bmistatus = "{color=#fcff20}Overweight{/color}"
                        elif bmi <= 35:
                            $ bmistatus = "{color=#ffc100}Obese Class I{/color}"
                        elif bmi <= 40:
                            $ bmistatus = "{color=#ff9a00}Obese Class II{/color}"
                        elif bmi <= 50:
                            $ bmistatus = "{color=#ff7400}Obese Class III{/color}"
                        elif bmi <= 60:
                            $ bmistatus = "{color=#ff4d00}Obese Class IV{/color}"
                        else:
                            $ bmistatus = "{color=#ff0000}Obese Class V{/color}"
                        text "BMI:  [bmi:.01f]  ([bmistatus])" font "fonts/asapcon.ttf" xalign 0.5 size 25

                    else:
                        $ statscharacter = str.lower(selectedCharacter.name)
                        if statscharacter == "lyn":
                            $ statscharacter = "leanne"
                        $ viewweight = char_weight[statscharacter][viewstage]
                        $ bmi = (viewweight / ((selectedCharacter.characterheight / 100)**2))
                        $ bmi2 = (selectedCharacter.weight / ((selectedCharacter.characterheight / 100)**2))
                        text "BMI:  [bmi:.01f] ([bmi2:.01f])" font "fonts/asapcon.ttf" xalign 0.5 size 25

                if teaching_bodyfat_check == 1:
                    if viewstage == selectedCharacter.stage:
                        $ bodyfat = (((selectedCharacter.weight - selectedCharacter.leanweight) / selectedCharacter.weight) * 100)
                        text "Body fat percentage:  [bodyfat:.02f]%" font "fonts/asapcon.ttf" xalign 0.5 size 25

                    else:
                        $ statscharacter = str.lower(selectedCharacter.name)
                        if statscharacter == "lyn":
                            $ statscharacter = "leanne"
                        $ viewweight = char_weight[statscharacter][viewstage]
                        $ viewleanweight = char_leanweight[statscharacter][viewstage]
                        $ bodyfat = (((viewweight - viewleanweight) / viewweight) * 100)
                        $ bodyfat2 = (((selectedCharacter.weight - selectedCharacter.leanweight) / selectedCharacter.weight) * 100)
                        text "Body fat percentage:  [bodyfat:.02f]% ([bodyfat2:.02f]%)" font "fonts/asapcon.ttf" xalign 0.5 size 25

                if selectedCharacter == teacher or (selectedCharacter == amber and amberstage6event == 0) or (selectedCharacter == bonnie and bonniestage8event == 0) or (selectedCharacter == cayenne and cayennestage2event == 0) or (selectedCharacter == katrine and katrinestage4event == 0) or (selectedCharacter == trista and tristastage7event == 0) or (selectedCharacter == luna and teacherstage5event == 0):
                    if viewstage == selectedCharacter.stage:
                        if persistent.imperial:
                            $ imperialstomachcapacity = (selectedCharacter.stomach_capacity * 33.814)
                            text "Stomach Capacity:  [imperialstomachcapacity:.02f]oz" font "fonts/asapcon.ttf" xalign 0.5 size 25
                        else:
                            text "Stomach Capacity:  [selectedCharacter.stomach_capacity:.02f]L" font "fonts/asapcon.ttf" xalign 0.5 size 25

                    else:
                        $ statscharacter = str.lower(selectedCharacter.name)
                        if statscharacter == "lyn":
                            $ statscharacter = "leanne"
                        $ viewstomachcapacity = char_stomachcapacity[statscharacter][viewstage]
                        if persistent.imperial:
                            $ imperialstomachcapacity = (viewstomachcapacity * 33.814)
                            $ imperialstomachcapacity2 = (selectedCharacter.stomach_capacity * 33.814)
                            text "Stomach Capacity:  [imperialstomachcapacity:.02f]oz ([imperialstomachcapacity2:.02f]oz)" font "fonts/asapcon.ttf" xalign 0.5 size 25
                        else:
                            text "Stomach Capacity:  [viewstomachcapacity:.02f]L ([selectedCharacter.stomach_capacity:.02f]L)" font "fonts/asapcon.ttf" xalign 0.5 size 25

                if selectedCharacter == britta or selectedCharacter == natalie:
                    if viewstage == selectedCharacter.stage:
                        if persistent.imperial:
                            $ imperiallactation = (selectedCharacter.lactation * 33.814)
                            text "Weekly Milk Production:  [imperiallactation:.02f]oz" font "fonts/asapcon.ttf" xalign 0.5 size 25
                        else:
                            text "Weekly Milk Production:  [selectedCharacter.lactation:.02f]L" font "fonts/asapcon.ttf" xalign 0.5 size 25

                    else:
                        $ statscharacter = str.lower(selectedCharacter.name)
                        if statscharacter == "lyn":
                            $ statscharacter = "leanne"
                        $ viewlactation = char_lactation[statscharacter][viewstage]
                        if persistent.imperial:
                            $ imperiallactation = (viewlactation * 33.814)
                            $ imperiallactation2 = (selectedCharacter.lactation * 33.814)
                            text "Weekly Milk Production:  [imperiallactation:.02f]oz ([imperiallactation2:.02f]oz)" font "fonts/asapcon.ttf" xalign 0.5 size 25
                        else:
                            text "Weekly Milk Production:  [viewlactation:.02f]L ([selectedCharacter.lactation:.02f]L)" font "fonts/asapcon.ttf" xalign 0.5 size 25


                if selectedCharacter == teacher or selectedCharacter == luna or selectedCharacter == roxie or selectedCharacter == sally or selectedCharacter == charlene or selectedCharacter == natalie or selectedCharacter == britta:
                    if viewstage == selectedCharacter.stage:
                        if persistent.imperial:
                            $ imperialbreastweight = (selectedCharacter.breast_weight * 2.2)
                            text "Breasts Weight:  [imperialbreastweight:.02f]lbs" font "fonts/asapcon.ttf" xalign 0.5 size 25
                        else:
                            text "Breasts Weight:  [selectedCharacter.breast_weight:.02f]kg" font "fonts/asapcon.ttf" xalign 0.5 size 25

                    else:
                        $ statscharacter = str.lower(selectedCharacter.name)
                        if statscharacter == "lyn":
                            $ statscharacter = "leanne"
                        $ viewboobweight = char_boobweight[statscharacter][viewstage]
                        if persistent.imperial:
                            $ imperialbreastweight = (viewboobweight * 2.2)
                            $ imperialbreastweight2 = (selectedCharacter.breast_weight * 2.2)
                            text "Breasts Weight:  [imperialbreastweight:.02f]lbs ([imperialbreastweight2:.02f]lbs)" font "fonts/asapcon.ttf" xalign 0.5 size 25
                        else:
                            text "Breasts Weight:  [viewboobweight:.02f]kg ([selectedCharacter.breast_weight:.02f]kg)" font "fonts/asapcon.ttf" xalign 0.5 size 25

                if viewstage == selectedCharacter.stage:
                    text "Breast Cup:  [selectedCharacter.breast_cup]" font "fonts/asapcon.ttf" xalign 0.5 size 25
                else:
                    $ statscharacter = str.lower(selectedCharacter.name)
                    if statscharacter == "lyn":
                        $ statscharacter = "leanne"
                    $ viewcup = char_cup[statscharacter][viewstage]
                    text "Breast Cup:  [viewcup] ([selectedCharacter.breast_cup])" font "fonts/asapcon.ttf" xalign 0.5 size 25

                if viewstage == selectedCharacter.stage:
                    if persistent.imperial:
                        text "Breast Size:  [selectedCharacter.breast_size]inches" font "fonts/asapcon.ttf" xalign 0.5 size 25
                    else:
                        $ metricbreast_size = (selectedCharacter.breast_size * 2.54)
                        text "Breast Size:  [metricbreast_size:.02f]cm" font "fonts/asapcon.ttf" xalign 0.5 size 25
                else:
                    $ statscharacter = str.lower(selectedCharacter.name)
                    if statscharacter == "lyn":
                        $ statscharacter = "leanne"
                    $ viewboobs = char_boobs[statscharacter][viewstage]
                    if persistent.imperial:
                        text "Breast Size:  [viewboobs]inches ([selectedCharacter.breast_size]inches)" font "fonts/asapcon.ttf" xalign 0.5 size 25
                    else:
                        $ metricbreast_size = (viewboobs * 2.54)
                        $ metricbreast_size2 = (selectedCharacter.breast_size * 2.54)
                        text "Breast Size:  [metricbreast_size:.02f]cm ([metricbreast_size2:.02f]cm)" font "fonts/asapcon.ttf" xalign 0.5 size 25

                if viewstage == selectedCharacter.stage:
                    if persistent.imperial:
                        text "Waist Size:  [selectedCharacter.waist_size]inches" font "fonts/asapcon.ttf" xalign 0.5 size 25
                    else:
                        $ metricwaist_size = (selectedCharacter.waist_size * 2.54)
                        text "Waist Size:  [metricwaist_size:.02f]cm" font "fonts/asapcon.ttf" xalign 0.5 size 25
                else:
                    $ statscharacter = str.lower(selectedCharacter.name)
                    if statscharacter == "lyn":
                        $ statscharacter = "leanne"
                    $ viewwaist = char_waist[statscharacter][viewstage]
                    if persistent.imperial:
                        text "Waist Size:  [viewwaist]inches ([selectedCharacter.waist_size]inches)" font "fonts/asapcon.ttf" xalign 0.5 size 25
                    else:
                        $ metricwaist_size = (viewwaist * 2.54)
                        $ metricwaist_size2 = (selectedCharacter.waist_size * 2.54)
                        text "Waist Size:  [metricwaist_size:.02f]cm ([metricwaist_size2:.02f]cm)" font "fonts/asapcon.ttf" xalign 0.5 size 25

                if viewstage == selectedCharacter.stage:
                    if persistent.imperial:
                        text "Ass Size:  [selectedCharacter.ass_size]inches" font "fonts/asapcon.ttf" xalign 0.5 size 25
                    else:
                        $ metricass_size = (selectedCharacter.ass_size * 2.54)
                        text "Ass Size:  [metricass_size:.02f]cm" font "fonts/asapcon.ttf" xalign 0.5 size 25
                else:
                    $ statscharacter = str.lower(selectedCharacter.name)
                    if statscharacter == "lyn":
                        $ statscharacter = "leanne"
                    $ viewass = char_ass[statscharacter][viewstage]
                    if persistent.imperial:
                        text "Ass Size:  [viewass]inches ([selectedCharacter.ass_size]inches)" font "fonts/asapcon.ttf" xalign 0.5 size 25
                    else:
                        $ metricass_size = (viewass * 2.54)
                        $ metricass_size2 = (selectedCharacter.ass_size * 2.54)
                        text "Ass Size:  [metricass_size:.02f]cm ([metricass_size2:.02f]cm)" font "fonts/asapcon.ttf" xalign 0.5 size 25

                text ""
                text "Stage  [selectedCharacter.stage]/[selectedCharacter.maxstage]"font "fonts/asapcon.ttf" xalign 0.5  size 25
                text "Body Type:  [selectedCharacter.type!c]" font "fonts/asapcon.ttf" xalign 0.5 size 25

                text ""
                text "Your own Charisma: [charisma]" font "fonts/asapcon.ttf" xalign 0.5  size 25
                #text "Your own Knowledge: [knowledge]" font "fonts/asapcon.ttf" xalign 0.5  size 25
                text "Your own Strength: [strength]" font "fonts/asapcon.ttf" xalign 0.5  size 25

                if (selectedCharacter.stage != selectedCharacter.maxstage) and (selectedCharacter.stage == viewstage):
                    $ statscharacter = str.lower(selectedCharacter.name)
                    if statscharacter == "lyn":
                        $ statscharacter = "leanne"
                    $ weight_difference1 = (char_weight[statscharacter][selectedCharacter.stage + 1] - char_weight[statscharacter][selectedCharacter.stage])
                    $ weight_difference2 = (selectedCharacter.weight - char_weight[statscharacter][selectedCharacter.stage])

                    text "Stage Progress:" font "fonts/asapcon.ttf" xalign 0.5  size 25 
                    bar value StaticValue(weight_difference2, weight_difference1) xsize 300 xalign 0.5

                if (selectedCharacter == bonnie and bonniestory >= 1) or (selectedCharacter == trista and tristastory >= 1) or (selectedCharacter == katrine and katrinestory >= 1) or (selectedCharacter == natalie and nataliestory >= 1) or (selectedCharacter == sally and sallystory >= 1) or (selectedCharacter == roxie and roxiestory >= 1) or (selectedCharacter == britta and brittastory >= 1) or (selectedCharacter == charlene and charlenestory >= 1) or (selectedCharacter == luna and lunastory >= 1) or (selectedCharacter == hari and haristory >= 1) or (selectedCharacter == teacher and teacherstory >= 1) or (selectedCharacter == cayenne and cayennestory >= 1) or (selectedCharacter == leanne and leannestory >= 1) or (selectedCharacter == lisa and lisastory >= 1) or (selectedCharacter == amber and amberstory >= 1) or (selectedCharacter == marie and mariestory >= 1):
                    imagebutton:
                        xalign 0.5
                        ypos 0.9
                        if renpy.variant("steam_deck"):
                            auto "UI/story_%s_sd.webp"
                        else:
                            auto "UI/story_%s.webp"
                        action SetVariable("storyview", True), Show("StoryView")
                    key "pad_x_press" action SetVariable("storyview", True), Show("StoryView")

        frame:
            # right frame
            background Frame("ui/statsframe.webp",0,0)
            ysize 720
            xsize 420
            xalign 1.0
            yalign 0.0
            if outfit == 1 and turnaround == 2:
                add "UI/[selectedCharacter.name][viewstage]xb.webp"
            elif outfit == 1 and turnaround == 1:
                add "UI/[selectedCharacter.name][viewstage]xs.webp"
            elif outfit == 1:
                add "UI/[selectedCharacter.name][viewstage]x.webp"
            elif turnaround == 2 and undress == True:
                add "UI/[selectedCharacter.name][viewstage]nb.webp"
            elif turnaround == 2:
                add "UI/[selectedCharacter.name][viewstage]b.webp"
            elif turnaround == 1 and undress == True:
                add "UI/[selectedCharacter.name][viewstage]ns.webp"
            elif turnaround == 1:
                add "UI/[selectedCharacter.name][viewstage]s.webp"
            elif undress == True:
                add "UI/[selectedCharacter.name][viewstage]n.webp"
            else:
                add "UI/[selectedCharacter.name][viewstage].webp"

            if (selectedCharacter == trista and trista.stage >= 12) or (selectedCharacter == leanne and leanne.stage >= 15):
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.05
                    idle "UI/costume_idle.webp"
                    hover "UI/costume_hover.webp"
                    if outfit == 1:
                        action SetVariable("outfit", 0)
                    elif outfit == 0:
                        action SetVariable("outfit", 1)
            elif (selectedCharacter == trista and trista.stage <= 11) or (selectedCharacter == leanne and leanne.stage <= 14):
                add "UI/costume_bw.webp" xanchor 0.5 yanchor 0.5 xpos 0.1 ypos 0.05

            if viewstage == 1:
                add "UI/arrowleft_bw.webp" xanchor 0.5 yanchor 0.5 xpos 0.1 ypos 0.95
            else:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.95
                    idle "UI/arrowleft_idle.webp"
                    hover "UI/arrowleft_hover.webp"
                    action SetVariable("viewstage", viewstage - 1)

            text "Stage: [viewstage]" xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.95 size 25 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]

            if selectedCharacter.stage == viewstage:
                add "UI/arrowright_bw.webp" xanchor 0.5 yanchor 0.5 xpos 0.9 ypos 0.95
            else:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.9
                    ypos 0.95
                    idle "UI/arrowright_idle.webp"
                    hover "UI/arrowright_hover.webp"
                    action SetVariable("viewstage", viewstage + 1)

            if selectedCharacter == lisa or selectedCharacter == bonnie or selectedCharacter == trista or selectedCharacter == amber or selectedCharacter == cayenne or selectedCharacter == hari or selectedCharacter == teacher or selectedCharacter == marie or selectedCharacter == luna or selectedCharacter == maya or selectedCharacter == leanne or selectedCharacter == katrine or selectedCharacter == britta or selectedCharacter == charlene or selectedCharacter == natalie or selectedCharacter == roxie or selectedCharacter == sally or selectedCharacter == caroline or selectedCharacter == vicky:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.78
                    ypos 0.95
                    idle "UI/turn_idle.webp"
                    hover "UI/turn_hover.webp"
                    if turnaround == False:
                        action SetVariable("turnaround", 1)
                    elif turnaround == 1:
                        action SetVariable("turnaround", 2)
                    elif turnaround == 2:
                        action SetVariable("turnaround", False)
            else:
                add "UI/turn_bw.webp" xanchor 0.5 yanchor 0.5 xpos 0.78 ypos 0.95

            if (selectedCharacter == lisa and lisaundressoption == 1) or (selectedCharacter == bonnie and bonniestage7event == 0) or (selectedCharacter == trista and tristastage3event == 0) or (selectedCharacter == amber and amberundressoption == 1) or (selectedCharacter == hari and haristage7event == 0) or (selectedCharacter == cayenne and cayennestage4event == 0) or (selectedCharacter == teacher and teacherstage2event == 0) or (selectedCharacter == marie and mariestage2event == 0) or (selectedCharacter == luna and teacherstage5event == 0) or (selectedCharacter == maya and mayaundressoption == 1) or (selectedCharacter == leanne and leannestage12event == 0) or (selectedCharacter == katrine and katrinestage1event == 0) or (selectedCharacter == natalie and lunastage5event == 0) or (selectedCharacter == roxie and lunastage5event == 0) or (selectedCharacter == britta and lunastage7event == 0) or (selectedCharacter == sally and lunastage7event == 0) or (selectedCharacter == charlene and lunastage11event == 0):
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.22
                    ypos 0.95
                    idle "UI/undress_idle.webp"
                    hover "UI/undress_hover.webp"
                    action [ToggleVariable("undress"), SetVariable("outfit", 0)]
            else:
                add "UI/undress_bw.webp" xanchor 0.5 yanchor 0.5 xpos 0.22 ypos 0.95

    viewport id "stat_scroller":
        # left frame
        area (60, 50, 360, 610)
        draggable True mousewheel True
        has vbox spacing -55 xpos 0.5 yalign 0.5
        if amber_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/ambericon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(amber.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (amber.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[amber.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [amber.stage]/[amber.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == amber)
                action SetVariable("selectedCharacter", amber), SetVariable("viewstage", amber.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)
        if bonnie_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/bonnieicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(bonnie.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (bonnie.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[bonnie.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [bonnie.stage]/[bonnie.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == bonnie)
                action SetVariable("selectedCharacter", bonnie), SetVariable("viewstage", bonnie.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)
        if britta_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/brittaicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(britta.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (britta.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[britta.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [britta.stage]/[britta.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == britta)
                action SetVariable("selectedCharacter", britta), SetVariable("viewstage", britta.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)

        if caroline_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/carolineicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(caroline.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (caroline.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[caroline.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [caroline.stage]/[caroline.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == caroline)
                action SetVariable("selectedCharacter", caroline), SetVariable("viewstage", caroline.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)

        if cayenne_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/cayenneicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(cayenne.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (cayenne.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[cayenne.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [cayenne.stage]/[cayenne.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == cayenne)
                action SetVariable("selectedCharacter", cayenne), SetVariable("viewstage", cayenne.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)

        if charlene_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/charleneicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(charlene.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (charlene.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[charlene.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [charlene.stage]/[charlene.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == charlene)
                action SetVariable("selectedCharacter", charlene), SetVariable("viewstage", charlene.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0), SelectedIf(selectedCharacter == charlene)

        hbox spacing -110:
            add "images/ui/faces/daisyicon_idle.webp"
            vbox:
                xalign 0.0
                yalign 0.5
                text _(teacher.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                if persistent.imperial:
                    $ imperialweight = (teacher.weight * 2.2)
                    text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                else:
                    text "[teacher.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                text "Stage [teacher.stage]/[teacher.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
        imagebutton:
            ypos -60
            xpos -5
            idle "images/ui/blankframe.webp"
            hover "images/ui/stathighlight.webp"
            selected_idle "images/ui/statselect.webp"
            selected_hover "images/ui/statselect.webp"
            selected (selectedCharacter == teacher)
            action SetVariable("selectedCharacter", teacher), SetVariable("viewstage", teacher.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)

        if hari_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/hariicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(hari.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (hari.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[hari.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [hari.stage]/[hari.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == hari)
                action SetVariable("selectedCharacter", hari), SetVariable("viewstage", hari.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)
        if katrine_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/katrineicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(katrine.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (katrine.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[katrine.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [katrine.stage]/[katrine.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == katrine)
                action SetVariable("selectedCharacter", katrine), SetVariable("viewstage", katrine.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)

        if leanne_stats_visible == 1:
            hbox spacing -110:
                if leannechoice == 1 and leanne.stage >= 12:
                    add "images/ui/faces/lynicon_idle.webp"
                else:
                    add "images/ui/faces/leanneicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(leanne.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (leanne.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[leanne.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [leanne.stage]/[leanne.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == leanne)
                action SetVariable("selectedCharacter", leanne), SetVariable("viewstage", leanne.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)

        if lisa_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/lisaicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(lisa.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (lisa.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[lisa.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [lisa.stage]/[lisa.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == lisa)
                action SetVariable("selectedCharacter", lisa), SetVariable("viewstage", lisa.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)
        if luna_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/lunaicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(luna.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (luna.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[luna.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [luna.stage]/[luna.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == luna)
                action SetVariable("selectedCharacter", luna), SetVariable("viewstage", luna.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)
        if marie_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/marieicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(marie.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (marie.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[marie.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [marie.stage]/[marie.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == marie)
                action SetVariable("selectedCharacter", marie), SetVariable("viewstage", marie.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)
        if maya_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/mayaicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(maya.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (maya.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[maya.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [maya.stage]/[maya.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == maya)
                action SetVariable("selectedCharacter", maya), SetVariable("viewstage", maya.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)
        if mylenna_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/mylennaicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(mylenna.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (mylenna.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[mylenna.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [mylenna.stage]/[mylenna.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == mylenna)
                action SetVariable("selectedCharacter", mylenna), SetVariable("viewstage", mylenna.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)
        if natalie_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/natalieicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(natalie.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (natalie.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[natalie.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [natalie.stage]/[natalie.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == natalie)
                action SetVariable("selectedCharacter", natalie), SetVariable("viewstage", natalie.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)
        if rebecca_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/rebeccaicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(rebecca.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (rebecca.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[rebecca.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [rebecca.stage]/[rebecca.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == rebecca)
                action SetVariable("selectedCharacter", rebecca), SetVariable("viewstage", rebecca.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)
        if roxie_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/roxieicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(roxie.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (roxie.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[roxie.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [roxie.stage]/[roxie.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == roxie)
                action SetVariable("selectedCharacter", roxie), SetVariable("viewstage", roxie.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)
        if sally_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/sallyicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(sally.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (sally.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[sally.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [sally.stage]/[sally.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == sally)
                action SetVariable("selectedCharacter", sally), SetVariable("viewstage", sally.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)
        if trista_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/tristaicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(trista.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (trista.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[trista.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [trista.stage]/[trista.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == trista)
                action SetVariable("selectedCharacter", trista), SetVariable("viewstage", trista.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)
        if vicky_stats_visible == 1:
            hbox spacing -110:
                add "images/ui/faces/vickyicon_idle.webp"
                vbox:
                    xalign 0.5
                    yalign 0.5
                    text _(vicky.name) xalign 0.0 font "fonts/asapcon.ttf" size 25
                    if persistent.imperial:
                        $ imperialweight = (vicky.weight * 2.2)
                        text "[imperialweight:.02f] lbs" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    else:
                        text "[vicky.weight:.02f] kg" xalign 0.0 font "fonts/asapcon.ttf" size 20
                    text "Stage [vicky.stage]/[vicky.maxstage]" xalign 0.0 font "fonts/asapcon.ttf" size 20
            imagebutton:
                ypos -60
                xpos -5
                idle "images/ui/blankframe.webp"
                hover "images/ui/stathighlight.webp"
                selected_idle "images/ui/statselect.webp"
                selected_hover "images/ui/statselect.webp"
                selected (selectedCharacter == vicky)
                action SetVariable("selectedCharacter", vicky), SetVariable("viewstage", vicky.stage), SetVariable("undress", False), SetVariable("turnaround", False), SetVariable("outfit", 0)

    vbar value YScrollValue("stat_scroller") xalign 0.255 ymaximum 0.95 yalign 0.5
    if renpy.variant("steam_deck"):
        imagebutton:
            auto "UI/return_%s_sd.webp"
            yalign 0.97
            xalign 0.02
            action Hide("StatsUI")
    else:
        imagebutton:
            auto "UI/return_%s.webp"
            yalign 0.97
            xalign 0.02
            action Hide("StatsUI")
    key "i" action Hide("StatsUI")
    key "pad_b_press" action Hide("StatsUI")

screen StoryView():
    modal True
    frame:
        xalign -0.02
        yalign 0.0
        xsize 880
        ysize 720
        xpadding 25
        ypadding 15
        background Frame("ui/storyframe.webp",0,0)
        viewport id "story_scroller":
            area (0.0, 0.0, 880, 660)
            draggable True mousewheel True
            child_size (830, 10000)
            has vbox spacing 20 xpos 0.5 yalign 0.1
            if selectedCharacter == amber:
                if amberstory >= 5:
                    text """Growing up on a farm, Amber enjoyed the freedom it brought her while she was a kid to run and play. Her parents always treated her more like an adult, allowing her the opportunity to try new things and discover what she liked and didn’t like. However, there was always the assumption that she would follow in her parents footsteps and once old enough would take a role on the farm. That had been Amber’s plan too, until she went away to live with her grandmother for a summer. She had been sent to France to learn about the financial management of farming, but instead found herself enamoured with another industry altogether.

    After attending her classes in the day she would return home and help her grandmother, a small town seamstress. It was a type of creativity that drew Amber in, the colours, patterns and ability to turn even the most mundane looking fabric into beautiful outfits. Begging her parents to stay longer than a summer, she learned all she could in the next few months and returned with a new hobby and potential career. With a year left in school, she preoccupied herself mending, sowing and developing her style. Quickly seeing the writing on the wall, her parents began to save up all they could and on her 18th birthday surprised her with a set of college applications. To Amber it had been a bit of fun, but with her parents permission she put her famlife on hold and went to college to study fashion.

    Moving to the city was a new experience for Amber who felt a little bit like a fish out of water. The differences between her and her classmates didn’t help, most of whom being rich and studying high fashion. One such classmate soon became more than that as they started dating, although it wasn’t the healthiest relationship. Her upbringing combined with spending formative years in another country had meant dating wasn’t high on her agenda or something she had done before. Her naivety and desire to fit in caused her to overlook many of the negative things in her first real relationship.Thankfully, she would soon run into Maya, a dancer at a local strip joint. It wasn’t the place she expected to make a good friend, but she was glad she did. Helping her realise she wasn’t happy she broke up with her boyfriend and the two became close, Maya almost becoming an older sister figure to Amber.

    Things continued to improve as she sought out a job to help support her while in college. Seeing a job opening for someone to design work uniforms for a restaurant in town she put her knowledge of style and working clothes to good use. The designs were a little out there, but it seemed like they were happy with them. Chatting to the manager Marie the two got on well and enjoyed working together. Having had a waitress recently quit Amber was asked if she wanted to work as a waitress as well. The flexible shift pattern giving her plenty of opportunity to fit shifts around her college work. Finally starting to find her feet, Amber felt happier and more at home in the city.

    With friends by her side she began to explore the city and try new things. On a fateful day off she was invited by Maya to a local farm show where she would discover a new side of herself. Enjoying the familiar sights and smells, the two friends' paths would cross a pie eating contest. Goaded by her friend the pair would enter it, determined to beat each other in the friendly competition. Consuming pie after pie their stomachs grew and so did the feeling deep inside Amber. Stuffed to her limit and bloated for all the world to see she felt alive, something inside of her awakened as people pointed and commented on her giant belly. It was something she couldn’t ignore and wanted more of. Going as far as to learn the attendants shift patterns she returned once a week to experience it, stuffing her face with more and more pies. It was a summer to remember that ended too soon as the fair picked up and moved on, having had a lasting impact on Amber's life.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif amberstory == 4:
                    text """Growing up on a farm, Amber enjoyed the freedom it brought her while she was a kid to run and play. Her parents always treated her more like an adult, allowing her the opportunity to try new things and discover what she liked and didn’t like. However, there was always the assumption that she would follow in her parents footsteps and once old enough would take a role on the farm. That had been Amber’s plan too, until she went away to live with her grandmother for a summer. She had been sent to France to learn about the financial management of farming, but instead found herself enamoured with another industry altogether.

    After attending her classes in the day she would return home and help her grandmother, a small town seamstress. It was a type of creativity that drew Amber in, the colours, patterns and ability to turn even the most mundane looking fabric into beautiful outfits. Begging her parents to stay longer than a summer, she learned all she could in the next few months and returned with a new hobby and potential career. With a year left in school, she preoccupied herself mending, sowing and developing her style. Quickly seeing the writing on the wall, her parents began to save up all they could and on her 18th birthday surprised her with a set of college applications. To Amber it had been a bit of fun, but with her parents permission she put her famlife on hold and went to college to study fashion.

    Moving to the city was a new experience for Amber who felt a little bit like a fish out of water. The differences between her and her classmates didn’t help, most of whom being rich and studying high fashion. One such classmate soon became more than that as they started dating, although it wasn’t the healthiest relationship. Her upbringing combined with spending formative years in another country had meant dating wasn’t high on her agenda or something she had done before. Her naivety and desire to fit in caused her to overlook many of the negative things in her first real relationship.Thankfully, she would soon run into Maya, a dancer at a local strip joint. It wasn’t the place she expected to make a good friend, but she was glad she did. Helping her realise she wasn’t happy she broke up with her boyfriend and the two became close, Maya almost becoming an older sister figure to Amber.

    Things continued to improve as she sought out a job to help support her while in college. Seeing a job opening for someone to design work uniforms for a restaurant in town she put her knowledge of style and working clothes to good use. The designs were a little out there, but it seemed like they were happy with them. Chatting to the manager Marie the two got on well and enjoyed working together. Having had a waitress recently quit Amber was asked if she wanted to work as a waitress as well. The flexible shift pattern giving her plenty of opportunity to fit shifts around her college work. Finally starting to find her feet, Amber felt happier and more at home in the city.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif amberstory == 3:
                    text """Growing up on a farm, Amber enjoyed the freedom it brought her while she was a kid to run and play. Her parents always treated her more like an adult, allowing her the opportunity to try new things and discover what she liked and didn’t like. However, there was always the assumption that she would follow in her parents footsteps and once old enough would take a role on the farm. That had been Amber’s plan too, until she went away to live with her grandmother for a summer. She had been sent to France to learn about the financial management of farming, but instead found herself enamoured with another industry altogether.

    After attending her classes in the day she would return home and help her grandmother, a small town seamstress. It was a type of creativity that drew Amber in, the colours, patterns and ability to turn even the most mundane looking fabric into beautiful outfits. Begging her parents to stay longer than a summer, she learned all she could in the next few months and returned with a new hobby and potential career. With a year left in school, she preoccupied herself mending, sowing and developing her style. Quickly seeing the writing on the wall, her parents began to save up all they could and on her 18th birthday surprised her with a set of college applications. To Amber it had been a bit of fun, but with her parents permission she put her famlife on hold and went to college to study fashion.

    Moving to the city was a new experience for Amber who felt a little bit like a fish out of water. The differences between her and her classmates didn’t help, most of whom being rich and studying high fashion. One such classmate soon became more than that as they started dating, although it wasn’t the healthiest relationship. Her upbringing combined with spending formative years in another country had meant dating wasn’t high on her agenda or something she had done before. Her naivety and desire to fit in caused her to overlook many of the negative things in her first real relationship.Thankfully, she would soon run into Maya, a dancer at a local strip joint. It wasn’t the place she expected to make a good friend, but she was glad she did. Helping her realise she wasn’t happy she broke up with her boyfriend and the two became close, Maya almost becoming an older sister figure to Amber.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif amberstory == 2:
                    text """Growing up on a farm, Amber enjoyed the freedom it brought her while she was a kid to run and play. Her parents always treated her more like an adult, allowing her the opportunity to try new things and discover what she liked and didn’t like. However, there was always the assumption that she would follow in her parents footsteps and once old enough would take a role on the farm. That had been Amber’s plan too, until she went away to live with her grandmother for a summer. She had been sent to France to learn about the financial management of farming, but instead found herself enamoured with another industry altogether.

    After attending her classes in the day she would return home and help her grandmother, a small town seamstress. It was a type of creativity that drew Amber in, the colours, patterns and ability to turn even the most mundane looking fabric into beautiful outfits. Begging her parents to stay longer than a summer, she learned all she could in the next few months and returned with a new hobby and potential career. With a year left in school, she preoccupied herself mending, sowing and developing her style. Quickly seeing the writing on the wall, her parents began to save up all they could and on her 18th birthday surprised her with a set of college applications. To Amber it had been a bit of fun, but with her parents permission she put her famlife on hold and went to college to study fashion.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif amberstory == 1:
                    text """Growing up on a farm, Amber enjoyed the freedom it brought her while she was a kid to run and play. Her parents always treated her more like an adult, allowing her the opportunity to try new things and discover what she liked and didn’t like. However, there was always the assumption that she would follow in her parents footsteps and once old enough would take a role on the farm. That had been Amber’s plan too, until she went away to live with her grandmother for a summer. She had been sent to France to learn about the financial management of farming, but instead found herself enamoured with another industry altogether.
                    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == bonnie:
                if bonniestory >= 6:
                    text """Ever since Bonnie was little, she dreamed of running her own chocolate shop. She’d always had a sweet tooth, but it was more than that to her. It was the enjoyment people got, the happiness that seemed to go with eating a simple bar of chocolate. It was the perfect food, great for smiles and good times, as well as making you feel better when you might be a little down. No matter how she was feeling, a bit of chocolate or a sweet cake could pick her up.

    After leaving school Bonnie found herself a job working retail in a small food store. It was good at first, but soon the glamour seemed to fade in the face of working for an anonymous business. Her boss was halfway across the country and caring more for profit than the customers enjoyment. She wanted more than that, not just to sell but to be involved and put her love into what she made. Even in a world bent on restricting her’s and everyone else’s enjoyment of sweet treats, she was determined to bring a little more joy to it.

    Handing in her notice Bonnie took the plunge, signing up for a year long pâtissière course she embarked on the next chapter of her life. It was here that she not only learned her incredible skills, but also met her would be partner. Put together by chance on a project they both soon realised that what they lacked individually, the other made up for. Bonnies love of the craft and people skills, complimented by a detail oriented and somewhat clinical approach. Even in their personal lives, her new partners confidence seemed to rub off on Bonnie and helped her become a little more confident in herself. Watching them defend their dishes during tasting reviews made her feel good about her skills, even if she doubted them sometimes.

    Graduating with top marks, the pair quickly found funding to open their own chocolate shop in town. A dream come true for Bonnie who could now feel much more connected to her customers as they ate her delicious treats. Taking the front of shop role Bonnie was greeted with the happy faces of customers who were quickly drawn to the shop, due to their home-made goods in a world of mass-produced blandness.

    Unfortunately, after more than a year it became apparent that the chocolate making duo were not perfectly aligned in what they wanted. Bonnie was content to serve customers, doing it for the love of good food. However, her partner was seemingly more ambitious and unhappy to settle for their quaint little shop. Despite the customers only increasing in number (and size), the rift in their attitudes only seemed to deepen until finally it broke. After a final confrontation, her partner packed up her recipes and left, insulting Bonnie for her lack of ambition to change the world.

    Now with a chocolate shop to run on her own, the world had felt much less fun and much more stressful. The dozens of varieties of chocolates their customers had learned to love, dwindling too just a few. Worrying about keeping the shop open Bonnie would make her way to a local restaurant, hoping a nice meal would distract her. Perhaps there she could get some new ideas of how to turn around the store.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif bonniestory == 5:
                    text """Ever since Bonnie was little, she dreamed of running her own chocolate shop. She’d always had a sweet tooth, but it was more than that to her. It was the enjoyment people got, the happiness that seemed to go with eating a simple bar of chocolate. It was the perfect food, great for smiles and good times, as well as making you feel better when you might be a little down. No matter how she was feeling, a bit of chocolate or a sweet cake could pick her up.

    After leaving school Bonnie found herself a job working retail in a small food store. It was good at first, but soon the glamour seemed to fade in the face of working for an anonymous business. Her boss was halfway across the country and caring more for profit than the customers enjoyment. She wanted more than that, not just to sell but to be involved and put her love into what she made. Even in a world bent on restricting her’s and everyone else’s enjoyment of sweet treats, she was determined to bring a little more joy to it.

    Handing in her notice Bonnie took the plunge, signing up for a year long pâtissière course she embarked on the next chapter of her life. It was here that she not only learned her incredible skills, but also met her would be partner. Put together by chance on a project they both soon realised that what they lacked individually, the other made up for. Bonnies love of the craft and people skills, complimented by a detail oriented and somewhat clinical approach. Even in their personal lives, her new partners confidence seemed to rub off on Bonnie and helped her become a little more confident in herself. Watching them defend their dishes during tasting reviews made her feel good about her skills, even if she doubted them sometimes.

    Graduating with top marks, the pair quickly found funding to open their own chocolate shop in town. A dream come true for Bonnie who could now feel much more connected to her customers as they ate her delicious treats. Taking the front of shop role Bonnie was greeted with the happy faces of customers who were quickly drawn to the shop, due to their home-made goods in a world of mass-produced blandness.

    Unfortunately, after more than a year it became apparent that the chocolate making duo were not perfectly aligned in what they wanted. Bonnie was content to serve customers, doing it for the love of good food. However, her partner was seemingly more ambitious and unhappy to settle for their quaint little shop. Despite the customers only increasing in number (and size), the rift in their attitudes only seemed to deepen until finally it broke. After a final confrontation, her partner packed up her recipes and left, insulting Bonnie for her lack of ambition to change the world.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif bonniestory == 4:
                    text """Ever since Bonnie was little, she dreamed of running her own chocolate shop. She’d always had a sweet tooth, but it was more than that to her. It was the enjoyment people got, the happiness that seemed to go with eating a simple bar of chocolate. It was the perfect food, great for smiles and good times, as well as making you feel better when you might be a little down. No matter how she was feeling, a bit of chocolate or a sweet cake could pick her up.

    After leaving school Bonnie found herself a job working retail in a small food store. It was good at first, but soon the glamour seemed to fade in the face of working for an anonymous business. Her boss was halfway across the country and caring more for profit than the customers enjoyment. She wanted more than that, not just to sell but to be involved and put her love into what she made. Even in a world bent on restricting her’s and everyone else’s enjoyment of sweet treats, she was determined to bring a little more joy to it.

    Handing in her notice Bonnie took the plunge, signing up for a year long pâtissière course she embarked on the next chapter of her life. It was here that she not only learned her incredible skills, but also met her would be partner. Put together by chance on a project they both soon realised that what they lacked individually, the other made up for. Bonnies love of the craft and people skills, complimented by a detail oriented and somewhat clinical approach. Even in their personal lives, her new partners confidence seemed to rub off on Bonnie and helped her become a little more confident in herself. Watching them defend their dishes during tasting reviews made her feel good about her skills, even if she doubted them sometimes.

    Graduating with top marks, the pair quickly found funding to open their own chocolate shop in town. A dream come true for Bonnie who could now feel much more connected to her customers as they ate her delicious treats. Taking the front of shop role Bonnie was greeted with the happy faces of customers who were quickly drawn to the shop, due to their home-made goods in a world of mass-produced blandness.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif bonniestory == 3:
                    text """Ever since Bonnie was little, she dreamed of running her own chocolate shop. She’d always had a sweet tooth, but it was more than that to her. It was the enjoyment people got, the happiness that seemed to go with eating a simple bar of chocolate. It was the perfect food, great for smiles and good times, as well as making you feel better when you might be a little down. No matter how she was feeling, a bit of chocolate or a sweet cake could pick her up.

    After leaving school Bonnie found herself a job working retail in a small food store. It was good at first, but soon the glamour seemed to fade in the face of working for an anonymous business. Her boss was halfway across the country and caring more for profit than the customers enjoyment. She wanted more than that, not just to sell but to be involved and put her love into what she made. Even in a world bent on restricting her’s and everyone else’s enjoyment of sweet treats, she was determined to bring a little more joy to it.

    Handing in her notice Bonnie took the plunge, signing up for a year long pâtissière course she embarked on the next chapter of her life. It was here that she not only learned her incredible skills, but also met her would be partner. Put together by chance on a project they both soon realised that what they lacked individually, the other made up for. Bonnies love of the craft and people skills, complimented by a detail oriented and somewhat clinical approach. Even in their personal lives, her new partners confidence seemed to rub off on Bonnie and helped her become a little more confident in herself. Watching them defend their dishes during tasting reviews made her feel good about her skills, even if she doubted them sometimes.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif bonniestory == 2:
                    text """Ever since Bonnie was little, she dreamed of running her own chocolate shop. She’d always had a sweet tooth, but it was more than that to her. It was the enjoyment people got, the happiness that seemed to go with eating a simple bar of chocolate. It was the perfect food, great for smiles and good times, as well as making you feel better when you might be a little down. No matter how she was feeling, a bit of chocolate or a sweet cake could pick her up.

    After leaving school Bonnie found herself a job working retail in a small food store. It was good at first, but soon the glamour seemed to fade in the face of working for an anonymous business. Her boss was halfway across the country and caring more for profit than the customers enjoyment. She wanted more than that, not just to sell but to be involved and put her love into what she made. Even in a world bent on restricting her’s and everyone else’s enjoyment of sweet treats, she was determined to bring a little more joy to it.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif bonniestory == 1:
                    text """Ever since Bonnie was little, she dreamed of running her own chocolate shop. She’d always had a sweet tooth, but it was more than that to her. It was the enjoyment people got, the happiness that seemed to go with eating a simple bar of chocolate. It was the perfect food, great for smiles and good times, as well as making you feel better when you might be a little down. No matter how she was feeling, a bit of chocolate or a sweet cake could pick her up.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]

            elif selectedCharacter == britta:
                text """Growing up, Britta was always a lot smarter than the other kids, making it difficult to socialize with them and make friends, so she spent all her time focusing on school work and her own projects instead. She became particularly interested in developing a drug that could cure many diseases and not just one. Unfortunately, her efforts were considered crazy and impossible by nearly all of the medical and scientific community until Luna found out about her research and offered her funding and support. Eventually, Britta was able to come up with a drug that also had some other interesting side effects. Britta is determined to prove that her drug works and can change the world, and what better way than to test it on herself.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == caroline:
                text """Story goes here.
Triple quoted strings can have newlines and all that fun stuff.
The intentation is weird for them though.
Weird.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == cayenne:
                if cayennestory >= 5:
                    text """Cayenne's family always had to struggle with money. While most other kids were playing with new bikes and games, she had to settle for whatever she could get from her local library. Rather than bemoan her lack of options, she managed to find a fascination with the books most kids left behind.

When she wasn’t at school or helping her parents around the house Cayenne would indulge her growing interest in history. It didn’t matter if it was ancient history or something within the last 50 years, it was enough to grab her attention. Anything that came before her was treated as precious knowledge that she would absorb at every chance she got. To her, it felt like she was living others’ lives just by reading over their past accomplishments.

It was because of this interest in history that Cayenne got interested in her own past. Over the years, she would repeatedly ask her parents for information about her ancestors. Each time, they would brush it off or try to change the subject. On the one occasion where she was bold enough to directly confront them, they were blunt in saying that it was better off that she didn’t know.

Unable to completely drop her curiosity for where she came from, Cayenne began to do her research. Unfortunately she didn’t manage to get very far with a budget of nothing. By the time she had reached adulthood, she was still left without even a scrap of information about who she was and where she came from. The worst part was that she knew how to remedy this, but it was far outside of her budget.

Scraping and saving everywhere she could, Cayenne began to build up a fund to get a proper test on her lineage. This meant working grueling jobs as a waitress, retail worker, or any other place that was hiring. Though she ended every day absolutely exhausted, she was certain that it would eventually pay off. Especially thanks to a certain deal she had with the employees at Bunny Bites who were more than willing to lend her a hand when it came to saving money on her meals.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif cayennestory == 4:
                    text """Cayenne's family always had to struggle with money. While most other kids were playing with new bikes and games, she had to settle for whatever she could get from her local library. Rather than bemoan her lack of options, she managed to find a fascination with the books most kids left behind.

When she wasn’t at school or helping her parents around the house Cayenne would indulge her growing interest in history. It didn’t matter if it was ancient history or something within the last 50 years, it was enough to grab her attention. Anything that came before her was treated as precious knowledge that she would absorb at every chance she got. To her, it felt like she was living others’ lives just by reading over their past accomplishments.

It was because of this interest in history that Cayenne got interested in her own past. Over the years, she would repeatedly ask her parents for information about her ancestors. Each time, they would brush it off or try to change the subject. On the one occasion where she was bold enough to directly confront them, they were blunt in saying that it was better off that she didn’t know.

Unable to completely drop her curiosity for where she came from, Cayenne began to do her research. Unfortunately she didn’t manage to get very far with a budget of nothing. By the time she had reached adulthood, she was still left without even a scrap of information about who she was and where she came from. The worst part was that she knew how to remedy this, but it was far outside of her budget.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif cayennestory == 3:
                    text """Cayenne's family always had to struggle with money. While most other kids were playing with new bikes and games, she had to settle for whatever she could get from her local library. Rather than bemoan her lack of options, she managed to find a fascination with the books most kids left behind.

When she wasn’t at school or helping her parents around the house Cayenne would indulge her growing interest in history. It didn’t matter if it was ancient history or something within the last 50 years, it was enough to grab her attention. Anything that came before her was treated as precious knowledge that she would absorb at every chance she got. To her, it felt like she was living others’ lives just by reading over their past accomplishments.

It was because of this interest in history that Cayenne got interested in her own past. Over the years, she would repeatedly ask her parents for information about her ancestors. Each time, they would brush it off or try to change the subject. On the one occasion where she was bold enough to directly confront them, they were blunt in saying that it was better off that she didn’t know.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif cayennestory == 2:
                    text """Cayenne's family always had to struggle with money. While most other kids were playing with new bikes and games, she had to settle for whatever she could get from her local library. Rather than bemoan her lack of options, she managed to find a fascination with the books most kids left behind.

When she wasn’t at school or helping her parents around the house Cayenne would indulge her growing interest in history. It didn’t matter if it was ancient history or something within the last 50 years, it was enough to grab her attention. Anything that came before her was treated as precious knowledge that she would absorb at every chance she got. To her, it felt like she was living others’ lives just by reading over their past accomplishments.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif cayennestory == 1:
                    text """Cayenne's family always had to struggle with money. While most other kids were playing with new bikes and games, she had to settle for whatever she could get from her local library. Rather than bemoan her lack of options, she managed to find a fascination with the books most kids left behind.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == charlene:
                text """Charlene was known as the fat girl growing up and was teased a lot because of it. The problem was that she loved to eat, yet she was also made to feel ashamed of eating like she wanted or gaining weight. Eventually, Charlene worked hard at dieting and exercising to be likable and lose weight. At first, it worked; she became more popular and even got herself a boyfriend. Yet her love of food continued, and when Charlene gained back a bit of the weight, she was again judged for it, especially by her abusive boyfriend. She grew to hate society, especially men, and her emotional scars have taken their toll. Charlene knows if she takes the drug, she won't be able to resist the temptation of eating crazy amounts of food like she wants and yet will feel guilt and shame for doing so. Unfortunately, if she doesn’t take it, there is a good chance of inheriting a deadly disease that has killed several of her family members. With a difficult choice, she ultimately decided to take the drug.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == teacher:
                if teacherstory >= 8:
                    text """Freshly out of school with a master's degree, Daisy Tanwen was set on the path to success. The only problem was that she wasn’t sure exactly what that meant for her. No longer bound and propped up by her academic prowess, she was at a loss on what to do with her life.

Lacking a purpose, Daisy hoped to discover it by joining a friend on a trip to Egypt. The goal was to get inspired by absorbing another culture. Though she did enjoy herself, there was still the feeling of something was off. It was if she was missing something that was vital to defining who she was.

While exploring some ruins, Daisy managed to separate from the tour group. Wandering aimlessly in the hopes of finding someone, she ended up stumbling upon a hidden passage that led beneath the surface. Her better judgement told her to turn back. A strong sense of purpose coming from the ancient hallway convinced her to go further with the feeling that she would find what she was looking for.

Daisy’s stumble through darkness gave way to the dim lighting of torches. The flames guided her to a large chamber filled with people in strange attire. The group’s worship of the mural of a large, obese woman came to a halt as they noticed her presence. Surrounded on all sides, Daisy had little reason to believe that she would be getting out of there alive. However, she was greeted not with violence, but with a willingness to share.

Sitting down with the members of the Followers of Heset, Daisy listened intently as they described their beliefs. As astounding as it was to hear how they worshipped the act of gaining weight, there was something about it that seemed to click with her. Eagerly absorbing every bit of information, she was more than ready to join them by the end of the evening. Seeing the spark in her eyes, the group made a unanimous decision to let her into the folds of the religion.

Now an active member of the Followers of Heset, Daisy was sent out on various trips to gather information from across the world. Between meeting up with other chapters of the religion, she was certain to keep her eyes peeled for anything that could help the cause. With a goal now in mind, everything around her appeared to be more vibrant and enticing. Things as simple as a delicious plate of food or an exotic dress were enough to get her mind running on how they could be used to support the Followers’ ambitious goals.

Daisy’s journey came to an end when she received a summons to a seemingly normal town. Having gained access to the Follower’s main headquarters, it was there she was given a chance to fully enjoy their benefits. Seeing what they planned for the future first hand, she was more than ready to volunteer to do anything to achieve it.

Hearing that her part to play would be that of a teacher, Daisy’s enthusiasm waivered a bit. She had never taught anyone before but was assured by the others that she would be excellent at the job. Feeling nervous the for the first time in years, she prepared herself to take on the role of the Nutritional Studies teacher at the university. Knowing her chances were slim, she hoped that she would at least be able to reach out to one student. Someone equally as willing and eager as her to spread the teachings of the Followers of Heset.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif teacherstory == 7:
                    text """Freshly out of school with a master's degree, Daisy Tanwen was set on the path to success. The only problem was that she wasn’t sure exactly what that meant for her. No longer bound and propped up by her academic prowess, she was at a loss on what to do with her life.

Lacking a purpose, Daisy hoped to discover it by joining a friend on a trip to Egypt. The goal was to get inspired by absorbing another culture. Though she did enjoy herself, there was still the feeling of something was off. It was if she was missing something that was vital to defining who she was.

While exploring some ruins, Daisy managed to separate from the tour group. Wandering aimlessly in the hopes of finding someone, she ended up stumbling upon a hidden passage that led beneath the surface. Her better judgement told her to turn back. A strong sense of purpose coming from the ancient hallway convinced her to go further with the feeling that she would find what she was looking for.

Daisy’s stumble through darkness gave way to the dim lighting of torches. The flames guided her to a large chamber filled with people in strange attire. The group’s worship of the mural of a large, obese woman came to a halt as they noticed her presence. Surrounded on all sides, Daisy had little reason to believe that she would be getting out of there alive. However, she was greeted not with violence, but with a willingness to share.

Sitting down with the members of the Followers of Heset, Daisy listened intently as they described their beliefs. As astounding as it was to hear how they worshipped the act of gaining weight, there was something about it that seemed to click with her. Eagerly absorbing every bit of information, she was more than ready to join them by the end of the evening. Seeing the spark in her eyes, the group made a unanimous decision to let her into the folds of the religion.

Now an active member of the Followers of Heset, Daisy was sent out on various trips to gather information from across the world. Between meeting up with other chapters of the religion, she was certain to keep her eyes peeled for anything that could help the cause. With a goal now in mind, everything around her appeared to be more vibrant and enticing. Things as simple as a delicious plate of food or an exotic dress were enough to get her mind running on how they could be used to support the Followers’ ambitious goals.

Daisy’s journey came to an end when she received a summons to a seemingly normal town. Having gained access to the Follower’s main headquarters, it was there she was given a chance to fully enjoy their benefits. Seeing what they planned for the future first hand, she was more than ready to volunteer to do anything to achieve it.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif teacherstory == 6:
                    text """Freshly out of school with a master's degree, Daisy Tanwen was set on the path to success. The only problem was that she wasn’t sure exactly what that meant for her. No longer bound and propped up by her academic prowess, she was at a loss on what to do with her life.

Lacking a purpose, Daisy hoped to discover it by joining a friend on a trip to Egypt. The goal was to get inspired by absorbing another culture. Though she did enjoy herself, there was still the feeling of something was off. It was if she was missing something that was vital to defining who she was.

While exploring some ruins, Daisy managed to separate from the tour group. Wandering aimlessly in the hopes of finding someone, she ended up stumbling upon a hidden passage that led beneath the surface. Her better judgement told her to turn back. A strong sense of purpose coming from the ancient hallway convinced her to go further with the feeling that she would find what she was looking for.

Daisy’s stumble through darkness gave way to the dim lighting of torches. The flames guided her to a large chamber filled with people in strange attire. The group’s worship of the mural of a large, obese woman came to a halt as they noticed her presence. Surrounded on all sides, Daisy had little reason to believe that she would be getting out of there alive. However, she was greeted not with violence, but with a willingness to share.

Sitting down with the members of the Followers of Heset, Daisy listened intently as they described their beliefs. As astounding as it was to hear how they worshipped the act of gaining weight, there was something about it that seemed to click with her. Eagerly absorbing every bit of information, she was more than ready to join them by the end of the evening. Seeing the spark in her eyes, the group made a unanimous decision to let her into the folds of the religion.

Now an active member of the Followers of Heset, Daisy was sent out on various trips to gather information from across the world. Between meeting up with other chapters of the religion, she was certain to keep her eyes peeled for anything that could help the cause. With a goal now in mind, everything around her appeared to be more vibrant and enticing. Things as simple as a delicious plate of food or an exotic dress were enough to get her mind running on how they could be used to support the Followers’ ambitious goals.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif teacherstory == 5:
                    text """Freshly out of school with a master's degree, Daisy Tanwen was set on the path to success. The only problem was that she wasn’t sure exactly what that meant for her. No longer bound and propped up by her academic prowess, she was at a loss on what to do with her life.

Lacking a purpose, Daisy hoped to discover it by joining a friend on a trip to Egypt. The goal was to get inspired by absorbing another culture. Though she did enjoy herself, there was still the feeling of something was off. It was if she was missing something that was vital to defining who she was.

While exploring some ruins, Daisy managed to separate from the tour group. Wandering aimlessly in the hopes of finding someone, she ended up stumbling upon a hidden passage that led beneath the surface. Her better judgement told her to turn back. A strong sense of purpose coming from the ancient hallway convinced her to go further with the feeling that she would find what she was looking for.

Daisy’s stumble through darkness gave way to the dim lighting of torches. The flames guided her to a large chamber filled with people in strange attire. The group’s worship of the mural of a large, obese woman came to a halt as they noticed her presence. Surrounded on all sides, Daisy had little reason to believe that she would be getting out of there alive. However, she was greeted not with violence, but with a willingness to share.

Sitting down with the members of the Followers of Heset, Daisy listened intently as they described their beliefs. As astounding as it was to hear how they worshipped the act of gaining weight, there was something about it that seemed to click with her. Eagerly absorbing every bit of information, she was more than ready to join them by the end of the evening. Seeing the spark in her eyes, the group made a unanimous decision to let her into the folds of the religion.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif teacherstory == 4:
                    text """Freshly out of school with a master's degree, Daisy Tanwen was set on the path to success. The only problem was that she wasn’t sure exactly what that meant for her. No longer bound and propped up by her academic prowess, she was at a loss on what to do with her life.

Lacking a purpose, Daisy hoped to discover it by joining a friend on a trip to Egypt. The goal was to get inspired by absorbing another culture. Though she did enjoy herself, there was still the feeling of something was off. It was if she was missing something that was vital to defining who she was.

While exploring some ruins, Daisy managed to separate from the tour group. Wandering aimlessly in the hopes of finding someone, she ended up stumbling upon a hidden passage that led beneath the surface. Her better judgement told her to turn back. A strong sense of purpose coming from the ancient hallway convinced her to go further with the feeling that she would find what she was looking for.

Daisy’s stumble through darkness gave way to the dim lighting of torches. The flames guided her to a large chamber filled with people in strange attire. The group’s worship of the mural of a large, obese woman came to a halt as they noticed her presence. Surrounded on all sides, Daisy had little reason to believe that she would be getting out of there alive. However, she was greeted not with violence, but with a willingness to share.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif teacherstory == 3:
                    text """Freshly out of school with a master's degree, Daisy Tanwen was set on the path to success. The only problem was that she wasn’t sure exactly what that meant for her. No longer bound and propped up by her academic prowess, she was at a loss on what to do with her life.

Lacking a purpose, Daisy hoped to discover it by joining a friend on a trip to Egypt. The goal was to get inspired by absorbing another culture. Though she did enjoy herself, there was still the feeling of something was off. It was if she was missing something that was vital to defining who she was.

While exploring some ruins, Daisy managed to separate from the tour group. Wandering aimlessly in the hopes of finding someone, she ended up stumbling upon a hidden passage that led beneath the surface. Her better judgement told her to turn back. A strong sense of purpose coming from the ancient hallway convinced her to go further with the feeling that she would find what she was looking for.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif teacherstory == 2:
                    text """Freshly out of school with a master's degree, Daisy Tanwen was set on the path to success. The only problem was that she wasn’t sure exactly what that meant for her. No longer bound and propped up by her academic prowess, she was at a loss on what to do with her life.

Lacking a purpose, Daisy hoped to discover it by joining a friend on a trip to Egypt. The goal was to get inspired by absorbing another culture. Though she did enjoy herself, there was still the feeling of something was off. It was if she was missing something that was vital to defining who she was.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif teacherstory == 1:
                    text """Freshly out of school with a master's degree, Daisy Tanwen was set on the path to success. The only problem was that she wasn’t sure exactly what that meant for her. No longer bound and propped up by her academic prowess, she was at a loss on what to do with her life.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == hari:
                if haristory >= 6:
                    text """In her early days, Hari overflowed with optimism and energy. At a moment’s notice she was more than willing to share what she was passionate about with the world. Whether that was simply by hanging pictures of cute animals on her bags or participating in the drama club, she was eager to show people who she was and what she was about. However, her childhood innocence could only last so long.

When it came time for her to attend high school, Hari’s sense of individuality clashed against the typical angst of surviving amongst other teenagers. Rampant bullying targeted each and every part of her that stood out. Anything from the color of her hair, to whatever was hanging from her backpack, and even the way she walked singled her out as a target. Though she tried multiple times to seek outside help, nothing seemed to work. In the end, she assumed that she could only rely on herself.

Hari stopped speaking up in class, or anywhere else for that matter. The various trinkets that used to hang from her bag were taken off and exchanged for a backpack that could easily be mistaken for countless of others. She purposefully dressed herself in drab, unassuming clothes to act as camouflage in an attempt to avoid getting any attention. While her acts of hiding her true self worked, it came at the heavy cost of isolating herself from most of the other students. She kept telling herself that the isolation would be the best for her, that was until she became aware of something she couldn’t take care of on her own.

When Hari came of age and had many questions regarding her own sexuality, she found it impossible to come to anyone for advice. Her lack of options led her to turn to the internet for answers. Though she did sate her initial inquiries, her curiosity only grew as she continued to look through various porn sites to try and sate a hunger for more knowledge. During these dives into the internet, she could feel her former spark well in her chest and other areas to push her to seek out more.

Hari’s search eventually led her down the rabbit hole that was the gainer community. For hours on end she would scroll through various websites, digesting as many images, stories, and videos as she could. The more she consumed, the stronger her will to become like the larger women she saw. She did her research. She knew how to gain weight at a rapid pace. She constantly daydreamed about what she would do with her new, plump body. However, what stood in her way was a single, insurmountable hurdle: herself.

As Hari graduated from high school and all through college, she repressed this desire to gain along with the rest of her more eccentric ideas. She thought of this side of herself as just being another part she had to hide if she hoped to live in peace. However, that part of her still managed to guide her hand when it came time to pick her classes and she signed up for the Nutritional Studies course.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif haristory == 5:
                    text """In her early days, Hari overflowed with optimism and energy. At a moment’s notice she was more than willing to share what she was passionate about with the world. Whether that was simply by hanging pictures of cute animals on her bags or participating in the drama club, she was eager to show people who she was and what she was about. However, her childhood innocence could only last so long.

When it came time for her to attend high school, Hari’s sense of individuality clashed against the typical angst of surviving amongst other teenagers. Rampant bullying targeted each and every part of her that stood out. Anything from the color of her hair, to whatever was hanging from her backpack, and even the way she walked singled her out as a target. Though she tried multiple times to seek outside help, nothing seemed to work. In the end, she assumed that she could only rely on herself.

Hari stopped speaking up in class, or anywhere else for that matter. The various trinkets that used to hang from her bag were taken off and exchanged for a backpack that could easily be mistaken for countless of others. She purposefully dressed herself in drab, unassuming clothes to act as camouflage in an attempt to avoid getting any attention. While her acts of hiding her true self worked, it came at the heavy cost of isolating herself from most of the other students. She kept telling herself that the isolation would be the best for her, that was until she became aware of something she couldn’t take care of on her own.

When Hari came of age and had many questions regarding her own sexuality, she found it impossible to come to anyone for advice. Her lack of options led her to turn to the internet for answers. Though she did sate her initial inquiries, her curiosity only grew as she continued to look through various porn sites to try and sate a hunger for more knowledge. During these dives into the internet, she could feel her former spark well in her chest and other areas to push her to seek out more.

Hari’s search eventually led her down the rabbit hole that was the gainer community. For hours on end she would scroll through various websites, digesting as many images, stories, and videos as she could. The more she consumed, the stronger her will to become like the larger women she saw. She did her research. She knew how to gain weight at a rapid pace. She constantly daydreamed about what she would do with her new, plump body. However, what stood in her way was a single, insurmountable hurdle: herself.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif haristory == 4:
                    text """In her early days, Hari overflowed with optimism and energy. At a moment’s notice she was more than willing to share what she was passionate about with the world. Whether that was simply by hanging pictures of cute animals on her bags or participating in the drama club, she was eager to show people who she was and what she was about. However, her childhood innocence could only last so long.

When it came time for her to attend high school, Hari’s sense of individuality clashed against the typical angst of surviving amongst other teenagers. Rampant bullying targeted each and every part of her that stood out. Anything from the color of her hair, to whatever was hanging from her backpack, and even the way she walked singled her out as a target. Though she tried multiple times to seek outside help, nothing seemed to work. In the end, she assumed that she could only rely on herself.

Hari stopped speaking up in class, or anywhere else for that matter. The various trinkets that used to hang from her bag were taken off and exchanged for a backpack that could easily be mistaken for countless of others. She purposefully dressed herself in drab, unassuming clothes to act as camouflage in an attempt to avoid getting any attention. While her acts of hiding her true self worked, it came at the heavy cost of isolating herself from most of the other students. She kept telling herself that the isolation would be the best for her, that was until she became aware of something she couldn’t take care of on her own.

When Hari came of age and had many questions regarding her own sexuality, she found it impossible to come to anyone for advice. Her lack of options led her to turn to the internet for answers. Though she did sate her initial inquiries, her curiosity only grew as she continued to look through various porn sites to try and sate a hunger for more knowledge. During these dives into the internet, she could feel her former spark well in her chest and other areas to push her to seek out more.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif haristory == 3:
                    text """In her early days, Hari overflowed with optimism and energy. At a moment’s notice she was more than willing to share what she was passionate about with the world. Whether that was simply by hanging pictures of cute animals on her bags or participating in the drama club, she was eager to show people who she was and what she was about. However, her childhood innocence could only last so long.

When it came time for her to attend high school, Hari’s sense of individuality clashed against the typical angst of surviving amongst other teenagers. Rampant bullying targeted each and every part of her that stood out. Anything from the color of her hair, to whatever was hanging from her backpack, and even the way she walked singled her out as a target. Though she tried multiple times to seek outside help, nothing seemed to work. In the end, she assumed that she could only rely on herself.

Hari stopped speaking up in class, or anywhere else for that matter. The various trinkets that used to hang from her bag were taken off and exchanged for a backpack that could easily be mistaken for countless of others. She purposefully dressed herself in drab, unassuming clothes to act as camouflage in an attempt to avoid getting any attention. While her acts of hiding her true self worked, it came at the heavy cost of isolating herself from most of the other students. She kept telling herself that the isolation would be the best for her, that was until she became aware of something she couldn’t take care of on her own.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif haristory == 2:
                    text """In her early days, Hari overflowed with optimism and energy. At a moment’s notice she was more than willing to share what she was passionate about with the world. Whether that was simply by hanging pictures of cute animals on her bags or participating in the drama club, she was eager to show people who she was and what she was about. However, her childhood innocence could only last so long.

When it came time for her to attend high school, Hari’s sense of individuality clashed against the typical angst of surviving amongst other teenagers. Rampant bullying targeted each and every part of her that stood out. Anything from the color of her hair, to whatever was hanging from her backpack, and even the way she walked singled her out as a target. Though she tried multiple times to seek outside help, nothing seemed to work. In the end, she assumed that she could only rely on herself.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif haristory == 1:
                    text """In her early days, Hari overflowed with optimism and energy. At a moment’s notice she was more than willing to share what she was passionate about with the world. Whether that was simply by hanging pictures of cute animals on her bags or participating in the drama club, she was eager to show people who she was and what she was about. However, her childhood innocence could only last so long.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == katrine:
                if katrinestory >= 5:
                    text """To her mother’s lamenting Katrine had always been a bit of a tom-boy, preferring to spend time playing sports than with her at home. With Katrine taking little interest in girly things, the stay at home mum had quickly found only one thing brought them together, a love of food. After days out at the weekly match, she always made sure to have a large cake or tasty desert ready for them when they got back. Some of their best heart to hearts were shared over an extra large slice of cake. Even when the other mums started to complain about not knowing their teenage daughters anymore, this routine helped keep the two of them close.

    It was these heart-to-heart chats that also helped nurture the creative side of Katrine and sparked her interest in writing. The things she was going through often feeling like only she had experienced them, but thanks to the chats with her parents she soon realised that they had been through them too. Puberty, dating, mean girls at school, nothing was really new.
    Seeing their daughter's love of writing and despite not having much money, Katrine was gifted her own computer on her 16th birthday. A decisive moment for her, giving her the tools to read and write online instead of the journal under her bed. Starting a blog Katrine shared her conversations with her mum online and quickly gathered a following. It was a little daunting at first to have so many people reading her content, but soon she saw it was an opportunity. She had never been one to excel in school, so perhaps her future was in online content?

    With her parents’ permission she dropped out of school to write full time, a decision that would turn out to be a great one. Her online following kept growing, enjoying her down to earth conversations and relatable content. It wasn’t long after leaving school that a company offered to buy her blog and website from her, seeing the potential in her content and fan base. The offer was more money than she had ever seen and after growing up in a family tight with money, it was simple too good to pass up. Besides, now an adult writing the same angsty teen drama blog had started to feel weird and out of place for her. She wanted to do more, write about more important topics that she loved. The buyout was the perfect opportunity to rebrand herself. The only problem was the internet was now full of copy-cat blogs covering every topic imaginable.

    After struggling for a couple of years to get another project off the ground, Katrine soon realised that maybe she needed to starting thinking about becoming more official. Moving into the city was a little scary, not knowing anyone in the area. But it was a great opportunity, enabling her to sign up with a freelance agency and work on any topic she wanted too. With her talent the jobs came quick and fast, different topics each week and barely giving her enough time to get to grips with it before the deadline. It was hectic and not as fun as she remembered, but with most of the buyout money gone it at least paid the bills. Besides, it was surely only a matter of time before she found something she really enjoyed writing about.

    But as she looked out of the window of her house at the blue skies, Katrine hit send to submit her latest story and grabbed her running shoes. It was time for another lap around the estate, and who knows maybe inspiration would hit on her run.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif katrinestory == 4:
                    text """To her mother’s lamenting Katrine had always been a bit of a tom-boy, preferring to spend time playing sports than with her at home. With Katrine taking little interest in girly things, the stay at home mum had quickly found only one thing brought them together, a love of food. After days out at the weekly match, she always made sure to have a large cake or tasty desert ready for them when they got back. Some of their best heart to hearts were shared over an extra large slice of cake. Even when the other mums started to complain about not knowing their teenage daughters anymore, this routine helped keep the two of them close.

    It was these heart-to-heart chats that also helped nurture the creative side of Katrine and sparked her interest in writing. The things she was going through often feeling like only she had experienced them, but thanks to the chats with her parents she soon realised that they had been through them too. Puberty, dating, mean girls at school, nothing was really new.
    Seeing their daughter's love of writing and despite not having much money, Katrine was gifted her own computer on her 16th birthday. A decisive moment for her, giving her the tools to read and write online instead of the journal under her bed. Starting a blog Katrine shared her conversations with her mum online and quickly gathered a following. It was a little daunting at first to have so many people reading her content, but soon she saw it was an opportunity. She had never been one to excel in school, so perhaps her future was in online content?

    With her parents’ permission she dropped out of school to write full time, a decision that would turn out to be a great one. Her online following kept growing, enjoying her down to earth conversations and relatable content. It wasn’t long after leaving school that a company offered to buy her blog and website from her, seeing the potential in her content and fan base. The offer was more money than she had ever seen and after growing up in a family tight with money, it was simple too good to pass up. Besides, now an adult writing the same angsty teen drama blog had started to feel weird and out of place for her. She wanted to do more, write about more important topics that she loved. The buyout was the perfect opportunity to rebrand herself. The only problem was the internet was now full of copy-cat blogs covering every topic imaginable.

    After struggling for a couple of years to get another project off the ground, Katrine soon realised that maybe she needed to starting thinking about becoming more official. Moving into the city was a little scary, not knowing anyone in the area. But it was a great opportunity, enabling her to sign up with a freelance agency and work on any topic she wanted too. With her talent the jobs came quick and fast, different topics each week and barely giving her enough time to get to grips with it before the deadline. It was hectic and not as fun as she remembered, but with most of the buyout money gone it at least paid the bills. Besides, it was surely only a matter of time before she found something she really enjoyed writing about.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif katrinestory == 3:
                    text """To her mother’s lamenting Katrine had always been a bit of a tom-boy, preferring to spend time playing sports than with her at home. With Katrine taking little interest in girly things, the stay at home mum had quickly found only one thing brought them together, a love of food. After days out at the weekly match, she always made sure to have a large cake or tasty desert ready for them when they got back. Some of their best heart to hearts were shared over an extra large slice of cake. Even when the other mums started to complain about not knowing their teenage daughters anymore, this routine helped keep the two of them close.

    It was these heart-to-heart chats that also helped nurture the creative side of Katrine and sparked her interest in writing. The things she was going through often feeling like only she had experienced them, but thanks to the chats with her parents she soon realised that they had been through them too. Puberty, dating, mean girls at school, nothing was really new.
    Seeing their daughter's love of writing and despite not having much money, Katrine was gifted her own computer on her 16th birthday. A decisive moment for her, giving her the tools to read and write online instead of the journal under her bed. Starting a blog Katrine shared her conversations with her mum online and quickly gathered a following. It was a little daunting at first to have so many people reading her content, but soon she saw it was an opportunity. She had never been one to excel in school, so perhaps her future was in online content?

    With her parents’ permission she dropped out of school to write full time, a decision that would turn out to be a great one. Her online following kept growing, enjoying her down to earth conversations and relatable content. It wasn’t long after leaving school that a company offered to buy her blog and website from her, seeing the potential in her content and fan base. The offer was more money than she had ever seen and after growing up in a family tight with money, it was simple too good to pass up. Besides, now an adult writing the same angsty teen drama blog had started to feel weird and out of place for her. She wanted to do more, write about more important topics that she loved. The buyout was the perfect opportunity to rebrand herself. The only problem was the internet was now full of copy-cat blogs covering every topic imaginable.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif katrinestory == 2:
                    text """To her mother’s lamenting Katrine had always been a bit of a tom-boy, preferring to spend time playing sports than with her at home. With Katrine taking little interest in girly things, the stay at home mum had quickly found only one thing brought them together, a love of food. After days out at the weekly match, she always made sure to have a large cake or tasty desert ready for them when they got back. Some of their best heart to hearts were shared over an extra large slice of cake. Even when the other mums started to complain about not knowing their teenage daughters anymore, this routine helped keep the two of them close.

    It was these heart-to-heart chats that also helped nurture the creative side of Katrine and sparked her interest in writing. The things she was going through often feeling like only she had experienced them, but thanks to the chats with her parents she soon realised that they had been through them too. Puberty, dating, mean girls at school, nothing was really new.
    Seeing their daughter's love of writing and despite not having much money, Katrine was gifted her own computer on her 16th birthday. A decisive moment for her, giving her the tools to read and write online instead of the journal under her bed. Starting a blog Katrine shared her conversations with her mum online and quickly gathered a following. It was a little daunting at first to have so many people reading her content, but soon she saw it was an opportunity. She had never been one to excel in school, so perhaps her future was in online content?
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif katrinestory == 1:
                    text """To her mother’s lamenting Katrine had always been a bit of a tom-boy, preferring to spend time playing sports than with her at home. With Katrine taking little interest in girly things, the stay at home mum had quickly found only one thing brought them together, a love of food. After days out at the weekly match, she always made sure to have a large cake or tasty desert ready for them when they got back. Some of their best heart to hearts were shared over an extra large slice of cake. Even when the other mums started to complain about not knowing their teenage daughters anymore, this routine helped keep the two of them close.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == leanne:
                if leannestory >= 5:
                    text """From a young age, Lyn wasn’t afraid to show off her interests. All the way through high school and beyond, she would spend time hanging out with friends to play games and talk about the latest, obscure anime she discovered. These obsessions continued into university where they started to have a negative effect on her grades.

No longer bound to the rules of her house, Lyn kept putting off school work in favor of enjoying herself. The wakeup call came after she failed her first series of exams. Motivated by the threat of being expelled, she promised herself that she would hunker down and study. This lasted up until she found her new obsession.

Lyn’s self-imposed ban on games still left an itch that she needed to satisfy. Looking to put something on to watch while she studied, she tuned into a streaming site called Fidget. Over time, the quick glances up from her notes became long gazes at the multitude of streamers and content creators that caught her eye. Though this meant that her grades were declining once more, she didn’t care. She had found what she wanted to do with her life.

Dropping out of college before the weight of her various failing grades could catch up to her, Lyn set to work on achieving her new goal of becoming a streamer. Working multiple part time jobs, she slowly managed to accrue the necessary funds to get the equipment she needed. When the day finally came, she was ecstatic to go live and stream. However, there was a dire fear keeping her from fully enjoying the moment.

Lyn knew how difficult it would be to become popular on Fidget. Even worse, she was aware of how little time she would have before the need to pay rent and food forced her back into the grueling work she despised. She was only going to have one chance to make a name for herself and gain enough followers to make streaming her career. If that meant becoming a completely different person, she was more than willing to fabricate a story that fit with her new persona: Luxury Leanne.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif leannestory == 4:
                    text """From a young age, Lyn wasn’t afraid to show off her interests. All the way through high school and beyond, she would spend time hanging out with friends to play games and talk about the latest, obscure anime she discovered. These obsessions continued into university where they started to have a negative effect on her grades.

No longer bound to the rules of her house, Lyn kept putting off school work in favor of enjoying herself. The wakeup call came after she failed her first series of exams. Motivated by the threat of being expelled, she promised herself that she would hunker down and study. This lasted up until she found her new obsession.

Lyn’s self-imposed ban on games still left an itch that she needed to satisfy. Looking to put something on to watch while she studied, she tuned into a streaming site called Fidget. Over time, the quick glances up from her notes became long gazes at the multitude of streamers and content creators that caught her eye. Though this meant that her grades were declining once more, she didn’t care. She had found what she wanted to do with her life.

Dropping out of college before the weight of her various failing grades could catch up to her, Lyn set to work on achieving her new goal of becoming a streamer. Working multiple part time jobs, she slowly managed to accrue the necessary funds to get the equipment she needed. When the day finally came, she was ecstatic to go live and stream. However, there was a dire fear keeping her from fully enjoying the moment.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif leannestory == 3:
                    text """From a young age, Lyn wasn’t afraid to show off her interests. All the way through high school and beyond, she would spend time hanging out with friends to play games and talk about the latest, obscure anime she discovered. These obsessions continued into university where they started to have a negative effect on her grades.

No longer bound to the rules of her house, Lyn kept putting off school work in favor of enjoying herself. The wakeup call came after she failed her first series of exams. Motivated by the threat of being expelled, she promised herself that she would hunker down and study. This lasted up until she found her new obsession.

Lyn’s self-imposed ban on games still left an itch that she needed to satisfy. Looking to put something on to watch while she studied, she tuned into a streaming site called Fidget. Over time, the quick glances up from her notes became long gazes at the multitude of streamers and content creators that caught her eye. Though this meant that her grades were declining once more, she didn’t care. She had found what she wanted to do with her life.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif leannestory == 2:
                    text """From a young age, Lyn wasn’t afraid to show off her interests. All the way through high school and beyond, she would spend time hanging out with friends to play games and talk about the latest, obscure anime she discovered. These obsessions continued into university where they started to have a negative effect on her grades.

No longer bound to the rules of her house, Lyn kept putting off school work in favor of enjoying herself. The wakeup call came after she failed her first series of exams. Motivated by the threat of being expelled, she promised herself that she would hunker down and study. This lasted up until she found her new obsession.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif leannestory == 1:
                    text """From a young age, Lyn wasn’t afraid to show off her interests. All the way through high school and beyond, she would spend time hanging out with friends to play games and talk about the latest, obscure anime she discovered. These obsessions continued into university where they started to have a negative effect on her grades.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == lisa:
                if lisastory >= 4:
                    text """As the youngest of 6 siblings, Lisa was used to a busy house growing up. The moderate house they shared was barely able to hold together as 4 teenage boys charged through it. Her mother had hoped for another daughter like her sister Mandy, one that would follow in her footsteps and not the rambunctious older brothers. However, to her dismay Lisa very early on took on traits more similar to her brothers. Enjoying sports and cars she was very much the girl next door type, choosing Ice hockey over figure skating. Outside of her home life Lisa was popular throughout school, with the large family well known in their community. She seemed to have a sense of self confidence and seemed sure of who she was at an early age. Coming out to her parents had been easy for her, telling them matter of factly on prom night she was going with a girlfriend. The lack of drama or nerves left little room for her parents to say or do much, even if they were going too.

    Despite her parents' ease of acceptance, it would be her sister that would be the only one to comment on it. Mandy had been the first to know but only because she had accused Lisa of going after her boyfriend at the time, after seeing them spending time together without her. She was sceptical at the time thinking Lisa was just saying it to get out of the argument, but it has since turned into her thinking she knows Lisa better than Lisa knows herself. Having found love with a new fiance, Mandy still believes Lisa would be better off and happier in a relationship with a man.

    Leaving school Lisa had a series of temp jobs before Mandy got her a job serving at Bunny Bites with her. The pair got on well and worked hard although the restaurant was soon sold to new owners. With that came new management in the form of Marie, a slim and friendly brunette that Lisa became infatuated with from the first moment she saw her. Desiring to keep her job she kept things professional, settling for admiring her from afar. While she wasn’t a fan of the new outfits to start with, they certainly increased the amount of tips she got. Besides, it wasn’t like Marie wasn’t wearing one, she was right there with them despite being manager. However, it was the free food and drinks that seemed to upset her sister the most and eventually caused her to leave the restaurant, claiming Marie had been fattening them all up.

    The job wasn’t available for long and Amber joined the trio who started to run the place by themselves. As the oldest Amber had taken it upon herself to look after Lisa but soon found it to be much more of an even playing field in terms of her maturity and experience. All three quickly became friends and the restaurant's popularity took off. It was hard work and long hours but it forged strong bonds between them.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif lisastory == 3:
                    text """As the youngest of 6 siblings, Lisa was used to a busy house growing up. The moderate house they shared was barely able to hold together as 4 teenage boys charged through it. Her mother had hoped for another daughter like her sister Mandy, one that would follow in her footsteps and not the rambunctious older brothers. However, to her dismay Lisa very early on took on traits more similar to her brothers. Enjoying sports and cars she was very much the girl next door type, choosing Ice hockey over figure skating. Outside of her home life Lisa was popular throughout school, with the large family well known in their community. She seemed to have a sense of self confidence and seemed sure of who she was at an early age. Coming out to her parents had been easy for her, telling them matter of factly on prom night she was going with a girlfriend. The lack of drama or nerves left little room for her parents to say or do much, even if they were going too.

    Despite her parents' ease of acceptance, it would be her sister that would be the only one to comment on it. Mandy had been the first to know but only because she had accused Lisa of going after her boyfriend at the time, after seeing them spending time together without her. She was sceptical at the time thinking Lisa was just saying it to get out of the argument, but it has since turned into her thinking she knows Lisa better than Lisa knows herself. Having found love with a new fiance, Mandy still believes Lisa would be better off and happier in a relationship with a man.

    Leaving school Lisa had a series of temp jobs before Mandy got her a job serving at Bunny Bites with her. The pair got on well and worked hard although the restaurant was soon sold to new owners. With that came new management in the form of Marie, a slim and friendly brunette that Lisa became infatuated with from the first moment she saw her. Desiring to keep her job she kept things professional, settling for admiring her from afar. While she wasn’t a fan of the new outfits to start with, they certainly increased the amount of tips she got. Besides, it wasn’t like Marie wasn’t wearing one, she was right there with them despite being manager. However, it was the free food and drinks that seemed to upset her sister the most and eventually caused her to leave the restaurant, claiming Marie had been fattening them all up.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif lisastory == 2:
                    text """As the youngest of 6 siblings, Lisa was used to a busy house growing up. The moderate house they shared was barely able to hold together as 4 teenage boys charged through it. Her mother had hoped for another daughter like her sister Mandy, one that would follow in her footsteps and not the rambunctious older brothers. However, to her dismay Lisa very early on took on traits more similar to her brothers. Enjoying sports and cars she was very much the girl next door type, choosing Ice hockey over figure skating. Outside of her home life Lisa was popular throughout school, with the large family well known in their community. She seemed to have a sense of self confidence and seemed sure of who she was at an early age. Coming out to her parents had been easy for her, telling them matter of factly on prom night she was going with a girlfriend. The lack of drama or nerves left little room for her parents to say or do much, even if they were going too.

    Despite her parents' ease of acceptance, it would be her sister that would be the only one to comment on it. Mandy had been the first to know but only because she had accused Lisa of going after her boyfriend at the time, after seeing them spending time together without her. She was sceptical at the time thinking Lisa was just saying it to get out of the argument, but it has since turned into her thinking she knows Lisa better than Lisa knows herself. Having found love with a new fiance, Mandy still believes Lisa would be better off and happier in a relationship with a man.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif lisastory == 1:
                    text """As the youngest of 6 siblings, Lisa was used to a busy house growing up. The moderate house they shared was barely able to hold together as 4 teenage boys charged through it. Her mother had hoped for another daughter like her sister Mandy, one that would follow in her footsteps and not the rambunctious older brothers. However, to her dismay Lisa very early on took on traits more similar to her brothers. Enjoying sports and cars she was very much the girl next door type, choosing Ice hockey over figure skating. Outside of her home life Lisa was popular throughout school, with the large family well known in their community. She seemed to have a sense of self confidence and seemed sure of who she was at an early age. Coming out to her parents had been easy for her, telling them matter of factly on prom night she was going with a girlfriend. The lack of drama or nerves left little room for her parents to say or do much, even if they were going too.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == luna:
                if lunastory >= 5:
                    text """Luna was the daughter and heir of a rich businessman while her mother was a former beauty pageant queen. Growing up both of her parents tried to force their own lifestyles on her, she was forced to endure hours each day of extra lessons by tutors on how to run a successful business at the insistence of her father, mainly being told that she needed to be ruthless and screw over as many people as she could to get as much money as possible. Her mother on the other hand forced her into child and teen beauty pageants, showing off her thin body that she needed to maintain with constant dieting and exercise and never being able to have sweets or junk food of any kind.

    Luna however eventually developed her own secret views that were quite different from that of her parents that she hid from them. She came to believe that a business could be even more successful by engaging in fair business deals and paying and treating your employees well so they would willingly work harder and better. She also came to see that beauty came in many different shapes and sizes, and in her mind it was fat women that were the ones to be envied and admired, they got to eat whatever and however much they wanted. All of that beautiful fat on them represented countless sweets and treats that she never got to eat herself. Yet she could never manage to confront her parents, knowing they would never understand, to them showing kindness or fairness in business was to be weak and fat people were to be looked down upon and disgusted by.

    During this time, she also developed a particular fascination with breasts as they were the one part of her body that had fat to them and could also be appreciated by even that of her parents and the beauty pageant community. To her though they were the ultimate form of fat, representing femininity, sexuality, and power. She eventually got into breast expansion content, most of it was not real, especially not the extra, extra large sizes she found herself liking the most, but still she enjoyed seeing other women’s breasts getting bigger and bigger and then dreaming of her own  breasts growing somehow as well, the bigger the better.

    When she was old enough she followed her father’s wishes and started working for his company, only to discover it was a company that heavily exploited its workers, paying them as little as possible and making them work as much as they could get out of them without any concern for them as people. She hated working for her father, who demanded she treat the employees cruelly and get as much as she possibly could out of them.

    Luna felt very much trapped in a life she didn’t want, but then the most bittersweet moment of her life would come when both of her parents died in a plane crash. All of a sudden, she now had the freedom to do as she wanted, not what her parents wanted for her. She had inherited her father’s love for business, but instead she wanted to build a good company that valued and appreciated its employees and made good quality products. She had also inherited her mother’s drive to be the most beautiful, but instead she wanted to be what she considered to be beautiful, fat with the biggest breasts that she could grow.

    She then quickly made changes starting by shutting down her father’s company, giving the employees generous severance packages, and used the money she inherited to invest into buying a hospital.

    In buying a hospital she hoped to help people instead of exploiting them by giving them quality and affordable health care, but the main reason was to have access to research facilities that could hopefully create drugs that would hopefully do as she wanted them to, to cause breasts to grow, to cause women to gain weight more quickly and easily, to cause them to be able to eat more, and in particular allow them to eat as they wanted and gain weight without having to worry about health problems.To Luna, eliminating those health problems would help encourage women to want to gain weight, to eat as they truly wanted, and eventually come to find that being fat is beautiful.

    When they heard of her research, members of the Followers of Heset contacted Luna wanting to know more and explained about their own goals. Luna soon then became quite eager to join them and became a strong and important member to them. She also met Daisy there, who became a friend of hers.

    Later on, she also found out about a young scientist named Britta and her research, who proposed the idea of a drug that could achieve all of Luna’s goals in just one drug. It sounded far too good to be true and Britta was considered crazy and her ideas impossible to the scientific community, but upon actually talking with Britta she became convinced that Britta could actually achieve what she claimed she could do and invested heavily into her and her research.

    Eventually a drug was created, and Luna insisted on being the first one to take it, if there were indeed any unintended side effects she would have to be the one who went through them first, but she also couldn’t wait any longer to finally be able to achieve her dreams: truly eating as she wanted, getting bigger and fatter as a result, and making her breasts as big as possible.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif lunastory == 4:
                    text """Luna was the daughter and heir of a rich businessman while her mother was a former beauty pageant queen. Growing up both of her parents tried to force their own lifestyles on her, she was forced to endure hours each day of extra lessons by tutors on how to run a successful business at the insistence of her father, mainly being told that she needed to be ruthless and screw over as many people as she could to get as much money as possible. Her mother on the other hand forced her into child and teen beauty pageants, showing off her thin body that she needed to maintain with constant dieting and exercise and never being able to have sweets or junk food of any kind.

    Luna however eventually developed her own secret views that were quite different from that of her parents that she hid from them. She came to believe that a business could be even more successful by engaging in fair business deals and paying and treating your employees well so they would willingly work harder and better. She also came to see that beauty came in many different shapes and sizes, and in her mind it was fat women that were the ones to be envied and admired, they got to eat whatever and however much they wanted. All of that beautiful fat on them represented countless sweets and treats that she never got to eat herself. Yet she could never manage to confront her parents, knowing they would never understand, to them showing kindness or fairness in business was to be weak and fat people were to be looked down upon and disgusted by.

    During this time, she also developed a particular fascination with breasts as they were the one part of her body that had fat to them and could also be appreciated by even that of her parents and the beauty pageant community. To her though they were the ultimate form of fat, representing femininity, sexuality, and power. She eventually got into breast expansion content, most of it was not real, especially not the extra, extra large sizes she found herself liking the most, but still she enjoyed seeing other women’s breasts getting bigger and bigger and then dreaming of her own  breasts growing somehow as well, the bigger the better.

    When she was old enough she followed her father’s wishes and started working for his company, only to discover it was a company that heavily exploited its workers, paying them as little as possible and making them work as much as they could get out of them without any concern for them as people. She hated working for her father, who demanded she treat the employees cruelly and get as much as she possibly could out of them.

    Luna felt very much trapped in a life she didn’t want, but then the most bittersweet moment of her life would come when both of her parents died in a plane crash. All of a sudden, she now had the freedom to do as she wanted, not what her parents wanted for her. She had inherited her father’s love for business, but instead she wanted to build a good company that valued and appreciated its employees and made good quality products. She had also inherited her mother’s drive to be the most beautiful, but instead she wanted to be what she considered to be beautiful, fat with the biggest breasts that she could grow.

    She then quickly made changes starting by shutting down her father’s company, giving the employees generous severance packages, and used the money she inherited to invest into buying a hospital.

    In buying a hospital she hoped to help people instead of exploiting them by giving them quality and affordable health care, but the main reason was to have access to research facilities that could hopefully create drugs that would hopefully do as she wanted them to, to cause breasts to grow, to cause women to gain weight more quickly and easily, to cause them to be able to eat more, and in particular allow them to eat as they wanted and gain weight without having to worry about health problems.To Luna, eliminating those health problems would help encourage women to want to gain weight, to eat as they truly wanted, and eventually come to find that being fat is beautiful.

    When they heard of her research, members of the Followers of Heset contacted Luna wanting to know more and explained about their own goals. Luna soon then became quite eager to join them and became a strong and important member to them. She also met Daisy there, who became a friend of hers.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif lunastory == 3:
                    text """Luna was the daughter and heir of a rich businessman while her mother was a former beauty pageant queen. Growing up both of her parents tried to force their own lifestyles on her, she was forced to endure hours each day of extra lessons by tutors on how to run a successful business at the insistence of her father, mainly being told that she needed to be ruthless and screw over as many people as she could to get as much money as possible. Her mother on the other hand forced her into child and teen beauty pageants, showing off her thin body that she needed to maintain with constant dieting and exercise and never being able to have sweets or junk food of any kind.

    Luna however eventually developed her own secret views that were quite different from that of her parents that she hid from them. She came to believe that a business could be even more successful by engaging in fair business deals and paying and treating your employees well so they would willingly work harder and better. She also came to see that beauty came in many different shapes and sizes, and in her mind it was fat women that were the ones to be envied and admired, they got to eat whatever and however much they wanted. All of that beautiful fat on them represented countless sweets and treats that she never got to eat herself. Yet she could never manage to confront her parents, knowing they would never understand, to them showing kindness or fairness in business was to be weak and fat people were to be looked down upon and disgusted by.

    During this time, she also developed a particular fascination with breasts as they were the one part of her body that had fat to them and could also be appreciated by even that of her parents and the beauty pageant community. To her though they were the ultimate form of fat, representing femininity, sexuality, and power. She eventually got into breast expansion content, most of it was not real, especially not the extra, extra large sizes she found herself liking the most, but still she enjoyed seeing other women’s breasts getting bigger and bigger and then dreaming of her own  breasts growing somehow as well, the bigger the better.

    When she was old enough she followed her father’s wishes and started working for his company, only to discover it was a company that heavily exploited its workers, paying them as little as possible and making them work as much as they could get out of them without any concern for them as people. She hated working for her father, who demanded she treat the employees cruelly and get as much as she possibly could out of them.

    Luna felt very much trapped in a life she didn’t want, but then the most bittersweet moment of her life would come when both of her parents died in a plane crash. All of a sudden, she now had the freedom to do as she wanted, not what her parents wanted for her. She had inherited her father’s love for business, but instead she wanted to build a good company that valued and appreciated its employees and made good quality products. She had also inherited her mother’s drive to be the most beautiful, but instead she wanted to be what she considered to be beautiful, fat with the biggest breasts that she could grow.

    She then quickly made changes starting by shutting down her father’s company, giving the employees generous severance packages, and used the money she inherited to invest into buying a hospital.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif lunastory == 2:
                    text """Luna was the daughter and heir of a rich businessman while her mother was a former beauty pageant queen. Growing up both of her parents tried to force their own lifestyles on her, she was forced to endure hours each day of extra lessons by tutors on how to run a successful business at the insistence of her father, mainly being told that she needed to be ruthless and screw over as many people as she could to get as much money as possible. Her mother on the other hand forced her into child and teen beauty pageants, showing off her thin body that she needed to maintain with constant dieting and exercise and never being able to have sweets or junk food of any kind.

    Luna however eventually developed her own secret views that were quite different from that of her parents that she hid from them. She came to believe that a business could be even more successful by engaging in fair business deals and paying and treating your employees well so they would willingly work harder and better. She also came to see that beauty came in many different shapes and sizes, and in her mind it was fat women that were the ones to be envied and admired, they got to eat whatever and however much they wanted. All of that beautiful fat on them represented countless sweets and treats that she never got to eat herself. Yet she could never manage to confront her parents, knowing they would never understand, to them showing kindness or fairness in business was to be weak and fat people were to be looked down upon and disgusted by.

    During this time, she also developed a particular fascination with breasts as they were the one part of her body that had fat to them and could also be appreciated by even that of her parents and the beauty pageant community. To her though they were the ultimate form of fat, representing femininity, sexuality, and power. She eventually got into breast expansion content, most of it was not real, especially not the extra, extra large sizes she found herself liking the most, but still she enjoyed seeing other women’s breasts getting bigger and bigger and then dreaming of her own  breasts growing somehow as well, the bigger the better.

    When she was old enough she followed her father’s wishes and started working for his company, only to discover it was a company that heavily exploited its workers, paying them as little as possible and making them work as much as they could get out of them without any concern for them as people. She hated working for her father, who demanded she treat the employees cruelly and get as much as she possibly could out of them.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif lunastory == 1:
                    text """Luna was the daughter and heir of a rich businessman while her mother was a former beauty pageant queen. Growing up both of her parents tried to force their own lifestyles on her, she was forced to endure hours each day of extra lessons by tutors on how to run a successful business at the insistence of her father, mainly being told that she needed to be ruthless and screw over as many people as she could to get as much money as possible. Her mother on the other hand forced her into child and teen beauty pageants, showing off her thin body that she needed to maintain with constant dieting and exercise and never being able to have sweets or junk food of any kind.

    Luna however eventually developed her own secret views that were quite different from that of her parents that she hid from them. She came to believe that a business could be even more successful by engaging in fair business deals and paying and treating your employees well so they would willingly work harder and better. She also came to see that beauty came in many different shapes and sizes, and in her mind it was fat women that were the ones to be envied and admired, they got to eat whatever and however much they wanted. All of that beautiful fat on them represented countless sweets and treats that she never got to eat herself. Yet she could never manage to confront her parents, knowing they would never understand, to them showing kindness or fairness in business was to be weak and fat people were to be looked down upon and disgusted by.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == marie:
                if mariestory >= 4:
                    text """Despite always being a hard worker, Marie never excelled in school and knew college would likely be a waste of time. That being said, wherever she went her bosses could only sing her praises. From her first summer job working in the local cinema, it was her attitude and maturity that impressed and led to her becoming assistant manager despite being the youngest. At 19 Marie wanted a change and  became a bar manager, excited to join the more adult world of serving drinks. However, she soon found out that it came with the downsides of dealing with drunk idiots. Her patience wearing thin she decided she needed a new challenge in life and one that she would enjoy.

    When she first saw the job at the newly refurbished Bunny Bites she wasn’t sure it was for her. Slinging burgers wasn’t exactly the sort of direction she saw her future going , especially in a bunny outfit. Despite this, the autonomy and power it gave her as manager was appealing. It would let her take the next step in getting experience and she could always leave in a year or two if she fancied it. Over four years later Marie can’t picture herself doing anything but her current job. She has fallen in love with the restaurant, customers and staff to a level she never thought possible. It also helps that some of the customers have started to become larger, the frequent visitors eating to their hearts and stomach’s content.

    Marie had never considered herself to have a fetish, but watching the regulars plump up as well as the gluttonous behaviour of those that came in to complete food challenges excited her. Was it their hedonistic faces being filled, or bursting bellies stuffed beyond their limits? Whatever it was, Marie knew she was a fan and wanted more, much more!

    With her powers of management Marie was able to start enacting small changes here and there, lowering prices and upping portion sizes. Changing recipes to be more filling and focusing on making the best tasting food in the city no expense was spared. While her efforts may have been carnally motivated, they proved financially beneficial as well. Slightly accidentally the restaurant started doing well, getting more and more people in through the doors and repeating the cycle of her needs and wants. However, this soon caught the attention of the owners, pleased with what they were seeing her bosses had indicated they wanted her to move somewhere else. While it would have been good for her career, Marie just had no interest in moving. She had grown close to both Amber and Lisa and with her other desires being satiated, she was more than happy to stay where she was. Thinking quickly, Marie had managed to get things to look more normal although her bosses were still interested, sending out an inspector every now and then to check in on her. So far, Marie had managed to avoid any good or bad reports being published, ensuring her place at Bunny Bites wasn’t about to be taken away.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif mariestory == 3:
                    text """Despite always being a hard worker, Marie never excelled in school and knew college would likely be a waste of time. That being said, wherever she went her bosses could only sing her praises. From her first summer job working in the local cinema, it was her attitude and maturity that impressed and led to her becoming assistant manager despite being the youngest. At 19 Marie wanted a change and  became a bar manager, excited to join the more adult world of serving drinks. However, she soon found out that it came with the downsides of dealing with drunk idiots. Her patience wearing thin she decided she needed a new challenge in life and one that she would enjoy.

    When she first saw the job at the newly refurbished Bunny Bites she wasn’t sure it was for her. Slinging burgers wasn’t exactly the sort of direction she saw her future going , especially in a bunny outfit. Despite this, the autonomy and power it gave her as manager was appealing. It would let her take the next step in getting experience and she could always leave in a year or two if she fancied it. Over four years later Marie can’t picture herself doing anything but her current job. She has fallen in love with the restaurant, customers and staff to a level she never thought possible. It also helps that some of the customers have started to become larger, the frequent visitors eating to their hearts and stomach’s content.

    Marie had never considered herself to have a fetish, but watching the regulars plump up as well as the gluttonous behaviour of those that came in to complete food challenges excited her. Was it their hedonistic faces being filled, or bursting bellies stuffed beyond their limits? Whatever it was, Marie knew she was a fan and wanted more, much more!
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif mariestory == 2:
                    text """Despite always being a hard worker, Marie never excelled in school and knew college would likely be a waste of time. That being said, wherever she went her bosses could only sing her praises. From her first summer job working in the local cinema, it was her attitude and maturity that impressed and led to her becoming assistant manager despite being the youngest. At 19 Marie wanted a change and  became a bar manager, excited to join the more adult world of serving drinks. However, she soon found out that it came with the downsides of dealing with drunk idiots. Her patience wearing thin she decided she needed a new challenge in life and one that she would enjoy.

    When she first saw the job at the newly refurbished Bunny Bites she wasn’t sure it was for her. Slinging burgers wasn’t exactly the sort of direction she saw her future going , especially in a bunny outfit. Despite this, the autonomy and power it gave her as manager was appealing. It would let her take the next step in getting experience and she could always leave in a year or two if she fancied it. Over four years later Marie can’t picture herself doing anything but her current job. She has fallen in love with the restaurant, customers and staff to a level she never thought possible. It also helps that some of the customers have started to become larger, the frequent visitors eating to their hearts and stomach’s content.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif mariestory == 1:
                    text """Despite always being a hard worker, Marie never excelled in school and knew college would likely be a waste of time. That being said, wherever she went her bosses could only sing her praises. From her first summer job working in the local cinema, it was her attitude and maturity that impressed and led to her becoming assistant manager despite being the youngest. At 19 Marie wanted a change and  became a bar manager, excited to join the more adult world of serving drinks. However, she soon found out that it came with the downsides of dealing with drunk idiots. Her patience wearing thin she decided she needed a new challenge in life and one that she would enjoy.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == maya:
                text """Story goes here.
Triple quoted strings can have newlines and all that fun stuff.
The intentation is weird for them though.
Weird.
""" xalign 0.5 yalign 0.05 text_align 0.5
            elif selectedCharacter == mylenna:
                text """Story goes here.
Triple quoted strings can have newlines and all that fun stuff.
The intentation is weird for them though.
Weird.
""" xalign 0.5 yalign 0.05 text_align 0.5
            elif selectedCharacter == natalie:
                text """Natalie has always loved to help people and dreams of becoming a nurse. She, however, can also be too trusting. Unfortunately, Natalie has had some bad relationships with people taking advantage of her quickly loving and trusting nature with some emotional abuse that has left her having lots of feelings of self-doubt. With the right person, however, who treats her as well as she deserves and she can tell genuinely loves her, there is little that she wouldn’t do for them…
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == rebecca:
                text """Story goes here.
Triple quoted strings can have newlines and all that fun stuff.
The intentation is weird for them though.
Weird.
""" xalign 0.5 yalign 0.05 text_align 0.5
            elif selectedCharacter == roxie:
                text """Roxie always got a lot of attention from guys due to her figure and gorgeous green eyes; too bad she was always much more attracted to other girls, more specifically, fat girls with huge breasts. She knew she would be teased and lose friends over it, so she kept such desires to herself. Upon applying to work as a nurse at the hospital, Roxie found an immediate attraction to Luna, who did her interview. Upon taking the job partially for that reason, she only fell more and more for her boss, especially when she saw Luna start to gain and grow from the drug. When Roxie learned of the opportunity to take the drug herself, she immediately volunteered; getting to see other women gain weight and grow huge breasts around her seemed like a dream come true, especially for her crush, Luna. Of course, becoming herself what she lusts and fantasizes over sounds pretty great, too…
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == sally:
                text """Sally was the eldest of a family of 6 children, and she had to spend much of her time helping raise her younger siblings. In addition, they were pretty poor, and there often wasn’t a lot of food, so she had to eat much less than she would want, and she never had any time for dating. Sally originally became a nurse to help financially support her family and worked long hours at the hospital to make as much as she could to give to them. Yet, no matter how much Sally sacrificed, her family was still ungrateful and didn’t appreciate her. One day, however, Sally realized that she should focus on her own wants and desires first and not worry about what her family or anyone else thinks of her; she’s just going to be enjoying life in the most pleasurable ways she can think of.
""" text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
            elif selectedCharacter == trista:
                if tristastory >= 7:
                    text """The gym has been something that is ever present in Trista’s life, having practically grown up in her Father’s gym. Most of her childhood memories were typically in one gym or another. As a champion boxer whose career had been cut short by an injury, her Father had taken up coaching. That meant a lot of traveling for competitions of his clients, takeaway meals in motels and late nights on the road traveling back for school.

    Being raised by her single father hadn’t been easy for either of them, but it had its moments. While her schooling may have suffered a little with how much time she spent at the gym, it taught her a lot about people. Some of it good, some of it bad, she saw people overcome adversity but also give into dark temptations. More than one client was fired for using enhancing drugs, something she should have been too young to know about. But no matter what was going on in the gym her father always made time for her, especially as she started to follow in his footsteps.

    Even from a young age her talent was getting a lot of attention, winning kickboxing championships all around the country. The training and discipline she had gained from her father helping her raise above even those with more experience. In a way, it was because it didn’t feel like work to Trista but time with her father, the routine of traveling to competitions also second nature to her. The only problem was, as she grew older those same competitions often meant she had to compete without her father present. His time split between her and his clients. She understood why, after all they needed money, but it still made her feel a little lonely at times as she sat alone in her cheap motel room.

    Unsurprisingly the homesickness started to impact her, causing her to lose sponsors and funding. The buzz around her slowly disappearing as 1st place wins became 2nd or 3rd place runner ups. Still big achievements for an 18 year old fighting grown adults, but she was apparently not living up to the expectations everyone seemingly had for her. She wasn’t supposed to be the underdog, she was supposed to be the favourite odds-on winner.

    After spending some time in the global competition scene Trista returned home to find her father had moved out. Some big sponsor in Japan had asked him to fly out for a few months, then a year, or years. He still phoned from time to time to check up on her, and check up on his gym which was nice. Running it for him had been hard, most of his clients left when he did since he was their trainer. Attracting new people to the gym was equally hard, it had a certain reputation for being a no nonsense gym for professionals. But as the numbers of those declined to almost 0, it was in serious need of a rebrand.

    The cheques from Japan had kept coming and easily covered any costs, but if felt wrong to let the gym die completely. It gave her plenty of time to train for herself, but there was something slightly creepy about working out in a silent gym. Maybe if she got some people in for free that might help attract others once they see it bustling again.

    A few locals had expressed interest, but nothing major. Despite that Trista was quietly confident that things would turn around soon. Competition season was fast approaching and if she could get some sponsors for herself, they could bring more attention to the gym as well. Speaking of which, she really did need to move those extra boxes of confectionary to the main counter. They gym was opening soon and who knew who might turn up today.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif tristastory == 6:
                    text """The gym has been something that is ever present in Trista’s life, having practically grown up in her Father’s gym. Most of her childhood memories were typically in one gym or another. As a champion boxer whose career had been cut short by an injury, her Father had taken up coaching. That meant a lot of traveling for competitions of his clients, takeaway meals in motels and late nights on the road traveling back for school.

    Being raised by her single father hadn’t been easy for either of them, but it had its moments. While her schooling may have suffered a little with how much time she spent at the gym, it taught her a lot about people. Some of it good, some of it bad, she saw people overcome adversity but also give into dark temptations. More than one client was fired for using enhancing drugs, something she should have been too young to know about. But no matter what was going on in the gym her father always made time for her, especially as she started to follow in his footsteps.

    Even from a young age her talent was getting a lot of attention, winning kickboxing championships all around the country. The training and discipline she had gained from her father helping her raise above even those with more experience. In a way, it was because it didn’t feel like work to Trista but time with her father, the routine of traveling to competitions also second nature to her. The only problem was, as she grew older those same competitions often meant she had to compete without her father present. His time split between her and his clients. She understood why, after all they needed money, but it still made her feel a little lonely at times as she sat alone in her cheap motel room.

    Unsurprisingly the homesickness started to impact her, causing her to lose sponsors and funding. The buzz around her slowly disappearing as 1st place wins became 2nd or 3rd place runner ups. Still big achievements for an 18 year old fighting grown adults, but she was apparently not living up to the expectations everyone seemingly had for her. She wasn’t supposed to be the underdog, she was supposed to be the favourite odds-on winner.

    After spending some time in the global competition scene Trista returned home to find her father had moved out. Some big sponsor in Japan had asked him to fly out for a few months, then a year, or years. He still phoned from time to time to check up on her, and check up on his gym which was nice. Running it for him had been hard, most of his clients left when he did since he was their trainer. Attracting new people to the gym was equally hard, it had a certain reputation for being a no nonsense gym for professionals. But as the numbers of those declined to almost 0, it was in serious need of a rebrand.

    The cheques from Japan had kept coming and easily covered any costs, but if felt wrong to let the gym die completely. It gave her plenty of time to train for herself, but there was something slightly creepy about working out in a silent gym. Maybe if she got some people in for free that might help attract others once they see it bustling again.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif tristastory == 5:
                    text """The gym has been something that is ever present in Trista’s life, having practically grown up in her Father’s gym. Most of her childhood memories were typically in one gym or another. As a champion boxer whose career had been cut short by an injury, her Father had taken up coaching. That meant a lot of traveling for competitions of his clients, takeaway meals in motels and late nights on the road traveling back for school.

    Being raised by her single father hadn’t been easy for either of them, but it had its moments. While her schooling may have suffered a little with how much time she spent at the gym, it taught her a lot about people. Some of it good, some of it bad, she saw people overcome adversity but also give into dark temptations. More than one client was fired for using enhancing drugs, something she should have been too young to know about. But no matter what was going on in the gym her father always made time for her, especially as she started to follow in his footsteps.

    Even from a young age her talent was getting a lot of attention, winning kickboxing championships all around the country. The training and discipline she had gained from her father helping her raise above even those with more experience. In a way, it was because it didn’t feel like work to Trista but time with her father, the routine of traveling to competitions also second nature to her. The only problem was, as she grew older those same competitions often meant she had to compete without her father present. His time split between her and his clients. She understood why, after all they needed money, but it still made her feel a little lonely at times as she sat alone in her cheap motel room.

    Unsurprisingly the homesickness started to impact her, causing her to lose sponsors and funding. The buzz around her slowly disappearing as 1st place wins became 2nd or 3rd place runner ups. Still big achievements for an 18 year old fighting grown adults, but she was apparently not living up to the expectations everyone seemingly had for her. She wasn’t supposed to be the underdog, she was supposed to be the favourite odds-on winner.

    After spending some time in the global competition scene Trista returned home to find her father had moved out. Some big sponsor in Japan had asked him to fly out for a few months, then a year, or years. He still phoned from time to time to check up on her, and check up on his gym which was nice. Running it for him had been hard, most of his clients left when he did since he was their trainer. Attracting new people to the gym was equally hard, it had a certain reputation for being a no nonsense gym for professionals. But as the numbers of those declined to almost 0, it was in serious need of a rebrand.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif tristastory == 4:
                    text """The gym has been something that is ever present in Trista’s life, having practically grown up in her Father’s gym. Most of her childhood memories were typically in one gym or another. As a champion boxer whose career had been cut short by an injury, her Father had taken up coaching. That meant a lot of traveling for competitions of his clients, takeaway meals in motels and late nights on the road traveling back for school.

    Being raised by her single father hadn’t been easy for either of them, but it had its moments. While her schooling may have suffered a little with how much time she spent at the gym, it taught her a lot about people. Some of it good, some of it bad, she saw people overcome adversity but also give into dark temptations. More than one client was fired for using enhancing drugs, something she should have been too young to know about. But no matter what was going on in the gym her father always made time for her, especially as she started to follow in his footsteps.

    Even from a young age her talent was getting a lot of attention, winning kickboxing championships all around the country. The training and discipline she had gained from her father helping her raise above even those with more experience. In a way, it was because it didn’t feel like work to Trista but time with her father, the routine of traveling to competitions also second nature to her. The only problem was, as she grew older those same competitions often meant she had to compete without her father present. His time split between her and his clients. She understood why, after all they needed money, but it still made her feel a little lonely at times as she sat alone in her cheap motel room.

    Unsurprisingly the homesickness started to impact her, causing her to lose sponsors and funding. The buzz around her slowly disappearing as 1st place wins became 2nd or 3rd place runner ups. Still big achievements for an 18 year old fighting grown adults, but she was apparently not living up to the expectations everyone seemingly had for her. She wasn’t supposed to be the underdog, she was supposed to be the favourite odds-on winner.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif tristastory == 3:
                    text """The gym has been something that is ever present in Trista’s life, having practically grown up in her Father’s gym. Most of her childhood memories were typically in one gym or another. As a champion boxer whose career had been cut short by an injury, her Father had taken up coaching. That meant a lot of traveling for competitions of his clients, takeaway meals in motels and late nights on the road traveling back for school.

    Being raised by her single father hadn’t been easy for either of them, but it had its moments. While her schooling may have suffered a little with how much time she spent at the gym, it taught her a lot about people. Some of it good, some of it bad, she saw people overcome adversity but also give into dark temptations. More than one client was fired for using enhancing drugs, something she should have been too young to know about. But no matter what was going on in the gym her father always made time for her, especially as she started to follow in his footsteps.

    Even from a young age her talent was getting a lot of attention, winning kickboxing championships all around the country. The training and discipline she had gained from her father helping her raise above even those with more experience. In a way, it was because it didn’t feel like work to Trista but time with her father, the routine of traveling to competitions also second nature to her. The only problem was, as she grew older those same competitions often meant she had to compete without her father present. His time split between her and his clients. She understood why, after all they needed money, but it still made her feel a little lonely at times as she sat alone in her cheap motel room.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif tristastory == 2:
                    text """The gym has been something that is ever present in Trista’s life, having practically grown up in her Father’s gym. Most of her childhood memories were typically in one gym or another. As a champion boxer whose career had been cut short by an injury, her Father had taken up coaching. That meant a lot of traveling for competitions of his clients, takeaway meals in motels and late nights on the road traveling back for school.

    Being raised by her single father hadn’t been easy for either of them, but it had its moments. While her schooling may have suffered a little with how much time she spent at the gym, it taught her a lot about people. Some of it good, some of it bad, she saw people overcome adversity but also give into dark temptations. More than one client was fired for using enhancing drugs, something she should have been too young to know about. But no matter what was going on in the gym her father always made time for her, especially as she started to follow in his footsteps.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
                elif tristastory == 1:
                    text """The gym has been something that is ever present in Trista’s life, having practically grown up in her Father’s gym. Most of her childhood memories were typically in one gym or another. As a champion boxer whose career had been cut short by an injury, her Father had taken up coaching. That meant a lot of traveling for competitions of his clients, takeaway meals in motels and late nights on the road traveling back for school.
    """ text_align 0.5 font "fonts/asapcon.ttf" outlines [ (1,"#000000",0,0) ]
        if renpy.variant("steam_deck"):
            imagebutton:
                yalign 0.99
                xalign 0.01
                auto "UI/return_%s_sd.webp"
                action SetVariable("storyview", False), Hide("StoryView")
        else:
            imagebutton:
                yalign 0.99
                xalign 0.01
                auto "UI/return_%s.webp"
                action SetVariable("storyview", False), Hide("StoryView")
        key "i" action SetVariable("storyview", False), Hide("StoryView")
        key "pad_b_press" action SetVariable("storyview", False), Hide("StoryView")
    vbar value YScrollValue("story_scroller") xalign 0.67 yalign 0.5 ymaximum 700

screen GallerySelect():
    modal True
    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    add "UI/chaulkboard.webp"
    hbox:
        spacing 5
        xalign 0.5
        yalign 0.0
        vbox:
            spacing -60
            add "UI/" + availableGirls[galPage * 3].name + str(availableGirls[galPage * 3].stage) + ".webp" xsize 390
            text _(availableGirls[galPage * 3].name) xalign 0.5 font "fonts/asapcon.ttf" size 40 outlines [(3, "#000000", 0, 0)]
            imagebutton:
                ypos -645
                xsize 400
                xalign 0.5
                idle "UI/galleryblank.webp"
                hover "UI/galleryhighlight.webp"
                action [SetVariable("selectedCharacter", availableGirls[galPage * 3]), Hide("GallerySelect"), Show("Gallery"), Function(ClearEvents)]

        if galPage < galMaxPage or len(availableGirls) % 3 == 2 or len(availableGirls) % 3 == 0:
            vbox:
                spacing -60
                add "UI/" + availableGirls[galPage * 3 + 1].name + str(availableGirls[galPage * 3 + 1].stage) + ".webp" xsize 390
                text _(availableGirls[galPage * 3 + 1].name) xalign 0.5 font "fonts/asapcon.ttf" size 40 outlines [(3, "#000000", 0, 0)]
                imagebutton:
                    ypos -645
                    xsize 400
                    xalign 0.5
                    idle "UI/galleryblank.webp"
                    hover "UI/galleryhighlight.webp"
                    action [SetVariable("selectedCharacter", availableGirls[galPage * 3 + 1]), Hide("GallerySelect"), Show("Gallery"), Function(ClearEvents)]

        if galPage < galMaxPage or len(availableGirls) % 3 == 0:
            vbox:
                spacing -60
                add "UI/" + availableGirls[galPage * 3 + 2].name + str(availableGirls[galPage * 3 + 2].stage) + ".webp" xsize 390
                text _(availableGirls[galPage * 3 + 2].name) xalign 0.5 font "fonts/asapcon.ttf" size 40 outlines [(3, "#000000", 0, 0)]
                imagebutton:
                    ypos -645
                    xsize 400
                    xalign 0.5
                    idle "UI/galleryblank.webp"
                    hover "UI/galleryhighlight.webp"
                    action [SetVariable("selectedCharacter", availableGirls[galPage * 3 + 2]), Hide("GallerySelect"), Show("Gallery"), Function(ClearEvents)]

    imagebutton:
        xalign 0
        yalign 0.5
        if galPage == 0:
            idle "UI/arrowbigleft_bw.webp"
        else:
            if renpy.variant("steam_deck"):
                auto "UI/arrowbigleft_%s_sd.webp"
            else:
                auto "UI/arrowbigleft_%s.webp"
            action [SetVariable("galPage", galPage - 1)]
    if galPage != 0:
        key "pad_leftshoulder_press" action [SetVariable("galPage", galPage - 1)]
    else:
        key "pad_leftshoulder_press" action NullAction()
    imagebutton:
        xalign 1.0
        yalign 0.5
        if galPage == galMaxPage:
            idle "UI/arrowbigright_bw.webp"
        else:
            if renpy.variant("steam_deck"):
                auto "UI/arrowbigright_%s_sd.webp"
            else:
                auto "UI/arrowbigright_%s.webp"
            action [SetVariable("galPage", galPage + 1)]
    if galPage != galMaxPage:
        key "pad_rightshoulder_press" action [SetVariable("galPage", galPage + 1)]
    else:
        key "pad_rightshoulder_press" action NullAction()

    if renpy.variant("steam_deck"):
        imagebutton:
            auto "UI/return_%s_sd.webp"
            yalign 0.97
            xalign 0.02
            action [SetVariable("galPage", 0), SetVariable("galMaxPage", 0), Return()]
    else:
        imagebutton:
            auto "UI/return_%s.webp"
            yalign 1.0
            xalign 0.0
            action [SetVariable("galPage", 0), SetVariable("galMaxPage", 0), Return()]
    key "i" action [SetVariable("galPage", 0), SetVariable("galMaxPage", 0), Return()]
    key "pad_b_press" action [SetVariable("galPage", 0), SetVariable("galMaxPage", 0), Return()]

# Scene Selector
screen Gallery():
    modal True
    add "UI/chaulkboard.webp"
    on "show" action Function(PopulateEvents, selectedCharacter)
    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    if bool(events):
        viewport id "gallery_scroller":
            area (0.15, 0.1, 1100, 610)
            draggable True mousewheel True
            has vbox spacing 20 xpos 0.5 yalign 0.1
            for x in range(int(len(events)/3+1)):
                if not bool(events):
                    break
                hbox:
                    xalign 0.5
                    spacing 20
                    for y in events[x*3:(x*3)+3]:
                        vbox:
                            hbox:
                                spacing -300
                                if selectedCharacter == teacher:
                                    if str(y).endswith("1"):
                                        hbox:
                                            spacing -100
                                            add "UI/event_thumbnails/teacher_events/" + str.lower(y).replace("teacher" + "_","").replace(str.lower("_Event"),"").replace("_","",1)[:-2] + ".jpg"
                                    else:
                                        add "UI/event_thumbnails/teacher_events/" + str.lower(y).replace("teacher" + "_","").replace(str.lower("_Event"),"").replace("_","",1) + ".jpg"
                                elif selectedCharacter.name == "Lyn":
                                    if str(y).endswith("1"):
                                        add "UI/event_thumbnails/lyn_events/" + str.lower(y).replace("leanne" + "_","").replace(str.lower("_Event"),"").replace("_","",1)[:-2] + ".jpg"
                                    else:
                                        add "UI/event_thumbnails/lyn_events/" + str.lower(y).replace("leanne" + "_","").replace(str.lower("_Event"),"").replace("_","",1) + ".jpg"
                                elif str(y).endswith("1"):
                                    add "UI/event_thumbnails/" + str.lower(selectedCharacter.name) + "_events/" + str.lower(y).replace(str.lower(selectedCharacter.name) + "_","").replace(str.lower("_Event"),"").replace("_","",1)[:-2] + ".jpg"
                                else:
                                    add "UI/event_thumbnails/" + str.lower(selectedCharacter.name) + "_events/" + str.lower(y).replace(str.lower(selectedCharacter.name) + "_","").replace(str.lower("_Event"),"").replace("_","",1) + ".jpg"
                                imagebutton:
                                    idle "UI/event_blank.webp"
                                    hover "UI/event_highlight.webp"
                                    action [Hide("Gallery"), SetVariable("recollection", True), Call(str(y))]
                            if selectedCharacter == teacher:
                                if y[-1].isdigit():
                                    text "Stage " + y.replace("Teacher_Stage_","")[:-8]  + " Event " + str(y[-1]) color "#ffffff" font "fonts/asapcon.ttf" size 25 xalign 0.5
                                else:
                                    text "Stage " + y.replace("Teacher_Stage_","")[:-6] color "#ffffff" font "fonts/asapcon.ttf" size 25 xalign 0.5
                            elif selectedCharacter.name == "Lyn":
                                if y[-1].isdigit():
                                    text "Stage " + y.replace("Leanne_Stage_","")[:-8]  + " Event " + str(y[-1]) color "#ffffff" font "fonts/asapcon.ttf" size 25 xalign 0.5
                                else:
                                    text "Stage " + y.replace("Leanne_Stage_","")[:-6] color "#ffffff" font "fonts/asapcon.ttf" size 25 xalign 0.5
                            elif y[-1].isdigit():
                                text "Stage " + y.replace(selectedCharacter.name + "_Stage_","")[:-8]  + " Event " + str(y[-1]) color "#ffffff" font "fonts/asapcon.ttf" size 25 xalign 0.5
                            else:
                                text "Stage " + y.replace(selectedCharacter.name + "_Stage_","")[:-6] color "#ffffff" font "fonts/asapcon.ttf" size 25 xalign 0.5

        vbar value YScrollValue("gallery_scroller") xalign 0.9 yalign 0.5 ymaximum 700

    if renpy.variant("steam_deck"):
        imagebutton:
            auto "UI/return_%s_sd.webp"
            yalign 0.97
            xalign 0.02
            action [Hide("Gallery"), Show("GallerySelect")]
            #action [Hide("Gallery"), Show("StatsUI")]
    else:
        imagebutton:
            idle "UI/return_idle.webp"
            yalign 0.97
            xalign 0.02
            action [Hide("Gallery"), Show("GallerySelect")]
            #action [Hide("Gallery"), Show("StatsUI")]
    key "i" action [Hide("Gallery"), Show("GallerySelect")]
    key "pad_b_press" action [Hide("Gallery"), Show("GallerySelect")]

style stats_button_text:
    xalign 0.5

#Movie screen
screen custommoviescreen:
        add Movie(size=(1280,720))
        on "show" action Play("movie", movieplaying, loop=False)
        on "hide" action Stop("movie")

        timer 0.1 repeat True action If(movielength > 0.0, true=(SetVariable('movielength', movielength - 0.1)), false=(Return(0)))

        textbutton "Skip":
            action Return(0)
            sensitive (not renpy.get_screen("say"))
            align (.95,.95)
            text_style "txt_base"
