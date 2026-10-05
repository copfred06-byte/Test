default gymLeftW = False
default gymRightW = False
default gymBench = False
default gymLeftT = False
default gymRightT = False
default gymStand = False
default gymTut = False

init python:
    def populateGym():
        global gymLeftW, gymRightW, gymBench, gymLeftT, gymRightT, gymStand
        gymLeftW = False
        gymRightW = False
        gymBench = False
        gymLeftT = False
        gymRightT = False
        gymStand = False
        possibleLeftW = []
        possibleRightW = []
        possibleBench = []
        possibleLeftT = []
        possibleRightT = []
        possibleStand = []
        freeSpots = ["gymLeftW", "gymRightW", "gymBench", "gymLeftT", "gymRightT", "gymStand"]
        if bonnie_gym_today == 0 and bonniestage1event == 0:
            possibleRightW.append(bonnie)
            if bonniegymfirsttime == 0:
                possibleLeftT.append(bonnie)
        if rebecca_gym_today == 0 and bonniestage11event == 0:
            possibleRightW.append(rebecca)
        if maya_stats_visible == 1 and maya_gym_today == 0:
            possibleLeftT.append(maya)
        if cayenne_gym_today == 0 and cayennestage2event == 0:
            possibleStand.append(cayenne)
        if teacher_gym_today == 0 and teacher.stage > 2:
            possibleStand.append(teacher)
        if lisa_gym_today == 0 and mariestage1event == 0:
            if lisagymfirsttime == 0:
                possibleRightT.append(lisa)
            possibleLeftW.append(lisa)
        if hari_gym_today == 0 and haristage4event == 0 and hari_mad == 0:
            possibleStand.append(hari)
        if marie_gym_today == 0 and mariestage1event == 0:
            possibleRightW.append(marie)
        if roxie_gym_today == 0 and roxiestage4event == 0:
            possibleBench.append(roxie)
        rand = renpy.random.randint(1, 2)
        if rand == 1 and katrine.stage != 8 and katrine_gym_today == 0:
            rand2 = renpy.random.randint(1, 2)
            if rand2 == 1:
                if katrine.stage >= 10:
                    gymRightW = katrine
                    freeSpots.remove("gymRightW")
                elif katrine.stage >= 7:
                    gymLeftW = katrine
                    freeSpots.remove("gymLeftW")
                else:
                    gymBench = katrine
                    freeSpots.remove("gymBench")
            else:
                gymLeftT = katrine
                freeSpots.remove("gymLeftT")
        elif trista_gym_today == 0:
            rand2 = renpy.random.randint(1, 2)
            if strength < 12:
                gymRightW = trista
                freeSpots.remove("gymRightW")
            else:
                if rand2 == 1 or trista.stage == 1 or trista.stage >= 9:
                    gymBench = trista
                    freeSpots.remove("gymBench")
                else:
                    gymRightT = trista
                    freeSpots.remove("gymRightT")
        numberOfGirls = renpy.random.choice([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6])
        if gymRightW != False:
            numberOfGirls -= 1
        if gymBench != False:
            numberOfGirls -= 1
        if gymRightT != False:
            numberOfGirls -= 1
        if numberOfGirls > 0:
            for x in range(numberOfGirls):
                girl = False
                spot = renpy.random.choice(freeSpots)
                spotName = spot
                spot = spot.replace("gym", "")
                if len(locals()["possible" + spot]) > 0:
                    girl = renpy.random.choice(locals()["possible" + spot])
                    globals()[spotName] = girl
                    freeSpots.remove(spotName)
                    if girl in gymSplit:              
                        try:
                            possibleLeftW.remove(girl)
                        except:
                            pass
                        try:
                            possibleRightW.remove(girl)
                        except:
                            pass
                        try:
                            possibleBench.remove(girl)
                        except:
                            pass
                        try:
                            possibleLeftT.remove(girl)
                        except:
                            pass
                        try:
                            possibleRightT.remove(girl)
                        except:
                            pass
                        try:
                            possibleStand.remove(girl)
                        except:
                            pass
                else:
                    pass


label gymCall(girl, split=False):
    if girl == lisa:
        if split == 1:
            call lisa_gym1 from _call_lisa_gym1
        else:
            call lisa_gym2 from _call_lisa_gym2
    if girl == bonnie:
        if split == 1:
            call bonnie_gym1 from _call_bonnie_gym1
        else:
            call bonnie_gym2 from _call_bonnie_gym2

    if girl == katrine:
        if split == 1:
            call katrine_gym_1 from _call_katrine_gym_1_1
        else:
            call katrine_gym_2 from _call_katrine_gym_2_1

    if girl == trista:
        if split == 1 or trista.stage == 1 or trista.stage >= 9:
            call trista_gym_1 from _call_trista_gym_1_1
        else:
            call trista_gym_2 from _call_trista_gym_2
    
    if girl == marie:
        call marie_gym from _call_marie_gym
    if girl == hari:
        call hari_gym from _call_hari_gym
    if girl == teacher:
        call daisy_gym from _call_daisy_gym
    if girl == rebecca:
        call rebecca_gym from _call_rebecca_gym
    if girl == cayenne:
        call cayenne_gym from _call_cayenne_gym
    if girl == maya:
        call maya_gym1
    if girl == roxie:
        call roxie_gym

screen gymmenu:
    zorder -1
    add "bg gym"
    if not gymTut:
        on "hide" action SetVariable("gymTut", True)
    #LeftW
    if gymLeftW != False:
        if gymLeftW == katrine:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/katrine/gym1/" + str(katrine.stage) + "_%s.png"
                action Call("gymCall", katrine, 1)
        if gymLeftW == lisa:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/lisa/gym1/" + str(lisa.stage) + "_%s.png"
                action Call("gymCall", lisa, 1)

    #RightW
    if gymRightW != False:
        if gymRightW == bonnie:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/bonnie/gym1/" + str(bonnie.stage) + "_%s.png"
                action Call("gymCall", bonnie, 1)
        elif gymRightW == katrine:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/katrine/gym1/" + str(katrine.stage) + "_%s.png"
                action Call("gymCall", katrine, 1)
        elif gymRightW == trista:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/trista/strfail/" + str(trista.stage) + "_%s.png"
                action Call("gymCall", trista, 1)
        else:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/" + str.lower(gymRightW.name) + "/" + str(gymRightW.stage) + "_%s.png"
                action Call("gymCall", gymRightW)

    #Bench
    if gymBench != False:
        if gymBench == katrine:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/katrine/gym1/" + str(katrine.stage) + "_%s.png"
                action Call("gymCall", katrine, 1)
        elif gymBench == trista:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/trista/gym1/" + str(trista.stage) + "_%s.png"
                action Call("gymCall", trista, 1)
        else:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/" + str.lower(gymBench.name) + "/" + str(gymBench.stage) + "_%s.png"
                action Call("gymCall", gymBench)

    #LeftT
    if gymLeftT != False:
        if gymLeftT == katrine:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/katrine/gym2/" + str(katrine.stage) + "_%s.png"
                action Call("gymCall", katrine, 2)
        elif gymLeftT == bonnie:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/bonnie/gym2/" + str(bonnie.stage) + "_%s.png"
                action Call("gymCall", bonnie, 2)
        else:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/" + str.lower(gymLeftT.name) + "/" + str(gymLeftT.stage) + "_%s.png"
                action Call("gymCall", gymLeftT)

    #RightT
    if gymRightT != False:
        if gymRightT == lisa:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/lisa/gym2/" + str(lisa.stage) + "_%s.png"
                action Call("gymCall", lisa, 2)
        elif gymRightT == trista:
            imagebutton:
                focus_mask True
                auto "images/gymmenu/trista/gym2/" + str(trista.stage) + "_%s.png"
                action Call("gymCall", trista, 2)

    #Stand

    if gymStand != False:
        imagebutton:
            focus_mask True
            auto "images/gymmenu/" + gymStand.name + "/" + str(gymStand.stage) + "_%s.png"
            action Call("gymCall", gymStand)

    if not gymTut:
        text "Pick someone to work out with." xalign 0.5 yalign 0.05 size 36 outlines [ (2,"#000000",0,0) ]